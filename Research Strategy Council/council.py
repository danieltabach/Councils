#!/usr/bin/env python3
"""Research Strategy Council — Multi-persona research strategy review via Anthropic API."""

import argparse
import asyncio
import base64
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from anthropic import AsyncAnthropic
from dotenv import load_dotenv

from config import (
    CHAIRMAN_MAX_TOKENS,
    CHAIRMAN_MODEL,
    CHAIRMAN_TEMP,
    MAX_CONCURRENT_REQUESTS,
    PRICING,
    REVIEWERS,
    PersonaConfig,
)
from personas import (
    build_deliberation_prompt,
    build_review_prompt,
    build_synthesis_prompt,
)

load_dotenv("secrets.env")
load_dotenv()


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ReviewResult:
    persona_name: str
    persona_slug: str
    response_text: str
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cache_creation_tokens: int
    model: str
    elapsed_seconds: float
    cost_usd: float


@dataclass
class CouncilReport:
    paper_path: str
    paper_title: str
    brief: str
    timestamp: str
    stage1_reviews: dict[str, ReviewResult]
    stage2_deliberations: dict[str, ReviewResult]
    synthesis: ReviewResult | None
    total_cost: float
    total_input_tokens: int
    total_output_tokens: int


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _timestamp() -> str:
    return datetime.now().strftime("%H:%M:%S")


def _log(msg: str) -> None:
    print(f"[{_timestamp()}] {msg}", flush=True)


def calculate_cost(model: str, input_tokens: int, output_tokens: int,
                   cache_read: int = 0, cache_create: int = 0) -> float:
    p = PRICING.get(model, PRICING["claude-sonnet-4-6"])
    cost = (
        input_tokens * p["input"] / 1_000_000
        + output_tokens * p["output"] / 1_000_000
        + cache_read * p["cache_read"] / 1_000_000
        + cache_create * p["cache_create"] / 1_000_000
    )
    return round(cost, 4)


def extract_title(tex: str) -> str:
    m = re.search(r"\\title\{([^}]+)\}", tex)
    if m:
        title = m.group(1)
        title = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", title)
        return title.strip()
    return "Untitled Paper"


def read_paper(path: str) -> str:
    p = Path(path)
    if not p.exists():
        print(f"Error: file not found: {path}")
        sys.exit(1)
    for enc in ("utf-8", "latin-1"):
        try:
            return p.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    print(f"Error: could not decode {path}")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Figure extraction
# ---------------------------------------------------------------------------

SUPPORTED_IMAGE_EXTENSIONS: dict[str, str] = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}

SUPPORTED_DOC_EXTENSIONS: dict[str, str] = {
    ".pdf": "application/pdf",
}

SUPPORTED_FIGURE_EXTENSIONS = {**SUPPORTED_IMAGE_EXTENSIONS, **SUPPORTED_DOC_EXTENSIONS}


def _resolve_figure_path(ref: str, tex_dir: Path) -> Path | None:
    search_dirs = [
        tex_dir,
        tex_dir / "figures",
        tex_dir / "images",
        tex_dir / "figs",
        tex_dir / "fig",
    ]
    ref_stem = Path(ref).stem
    ref_parent = Path(ref).parent

    for d in search_dirs:
        if not d.exists():
            continue
        # Try exact path first
        candidate = d / ref
        if candidate.is_file():
            return candidate
        # Try appending supported extensions (ref has no extension)
        for ext in SUPPORTED_FIGURE_EXTENSIONS:
            candidate = d / (ref + ext)
            if candidate.is_file():
                return candidate
        # Try swapping extension (e.g., .pdf -> .png)
        search_in = d / ref_parent if ref_parent != Path(".") else d
        if search_in.exists():
            for ext in SUPPORTED_FIGURE_EXTENSIONS:
                candidate = search_in / (ref_stem + ext)
                if candidate.is_file():
                    return candidate
    return None


def extract_figures(tex_content: str, tex_dir: Path) -> list[dict]:
    """Parse \\includegraphics refs from LaTeX and return API content blocks."""
    pattern = r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}"
    refs = re.findall(pattern, tex_content)

    if not refs:
        return []

    _log(f"  Found {len(refs)} figure reference(s) in LaTeX")
    blocks: list[dict] = []

    for ref_path in refs:
        ref_path = ref_path.strip()
        resolved = _resolve_figure_path(ref_path, tex_dir)
        if resolved is None:
            _log(f"    {ref_path} — not found, skipping")
            continue
        ext = resolved.suffix.lower()
        media_type = SUPPORTED_FIGURE_EXTENSIONS.get(ext)
        if media_type is None:
            _log(f"    {resolved.name} — unsupported format, skipping")
            continue

        data = base64.b64encode(resolved.read_bytes()).decode("utf-8")
        blocks.append({"type": "text", "text": f"[Figure: {ref_path}]"})
        if ext in SUPPORTED_DOC_EXTENSIONS:
            blocks.append({
                "type": "document",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": data,
                },
            })
        else:
            blocks.append({
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": data,
                },
            })
        _log(f"    {resolved.name} — loaded ({resolved.stat().st_size // 1024}KB)")

    if blocks:
        _log(f"  {len(blocks) // 2} figure(s) will be sent to reviewers")
    return blocks


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

async def call_reviewer(
    client: AsyncAnthropic,
    persona: PersonaConfig,
    system_prompt: str,
    user_messages: list[dict],
    temperature: float,
    max_tokens: int,
    stage_name: str,
    semaphore: asyncio.Semaphore,
) -> ReviewResult:
    async with semaphore:
        _log(f"  {persona.name} ({persona.model}) ... started")
        t0 = time.monotonic()

        kwargs: dict = dict(
            model=persona.model,
            max_tokens=max_tokens,
            system=system_prompt,
            messages=user_messages,
        )
        if not persona.model.startswith("claude-opus"):
            kwargs["temperature"] = temperature
        if persona.web_search:
            kwargs["tools"] = [{"type": "web_search_20250305", "name": "web_search"}]
        response = await client.messages.create(**kwargs)

        elapsed = round(time.monotonic() - t0, 1)
        usage = response.usage
        input_tok = usage.input_tokens
        output_tok = usage.output_tokens
        cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
        cache_create = getattr(usage, "cache_creation_input_tokens", 0) or 0
        cost = calculate_cost(persona.model, input_tok, output_tok, cache_read, cache_create)

        text = ""
        for block in response.content:
            if block.type == "text":
                text += block.text

        _log(
            f"  {persona.name} ... done "
            f"({elapsed}s, {output_tok} tokens out, ${cost:.2f})"
        )

        return ReviewResult(
            persona_name=persona.name,
            persona_slug=persona.slug,
            response_text=text,
            input_tokens=input_tok,
            output_tokens=output_tok,
            cache_read_tokens=cache_read,
            cache_creation_tokens=cache_create,
            model=persona.model,
            elapsed_seconds=elapsed,
            cost_usd=cost,
        )


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------

async def run_stage1(
    client: AsyncAnthropic,
    paper_text: str,
    brief: str,
    reviewers: list[PersonaConfig],
    semaphore: asyncio.Semaphore,
    figures: list[dict] | None = None,
) -> dict[str, ReviewResult]:
    _log(f"Stage 1: Dispatching {len(reviewers)} independent reviews...")

    tasks = []
    for persona in reviewers:
        system, msgs = build_review_prompt(persona.slug, paper_text, brief, figures)
        tasks.append(
            call_reviewer(
                client, persona, system, msgs,
                temperature=persona.stage1_temp,
                max_tokens=persona.max_tokens_review,
                stage_name="Stage 1",
                semaphore=semaphore,
            )
        )

    results = await asyncio.gather(*tasks, return_exceptions=True)

    successful: dict[str, ReviewResult] = {}
    for persona, result in zip(reviewers, results):
        if isinstance(result, Exception):
            _log(f"  WARNING: {persona.name} failed: {result}")
        else:
            successful[persona.slug] = result

    stage_cost = sum(r.cost_usd for r in successful.values())
    _log(f"Stage 1 complete. {len(successful)}/{len(reviewers)} succeeded. Cost: ${stage_cost:.2f}")

    if len(successful) < 3:
        _log("ERROR: Fewer than 3 reviewers succeeded. Aborting.")
        sys.exit(1)

    return successful


async def run_stage2(
    client: AsyncAnthropic,
    paper_text: str,
    brief: str,
    stage1_results: dict[str, ReviewResult],
    reviewers: list[PersonaConfig],
    semaphore: asyncio.Semaphore,
    figures: list[dict] | None = None,
) -> dict[str, ReviewResult]:
    _log(f"Stage 2: Dispatching deliberation round...")

    all_reviews = {slug: r.response_text for slug, r in stage1_results.items()}
    active_slugs = set(all_reviews.keys())

    tasks = []
    active_personas = []
    for persona in reviewers:
        if persona.slug not in active_slugs:
            continue
        system, msgs = build_deliberation_prompt(
            persona.slug, paper_text, all_reviews, brief, figures
        )
        active_personas.append(persona)
        tasks.append(
            call_reviewer(
                client, persona, system, msgs,
                temperature=persona.stage2_temp,
                max_tokens=persona.max_tokens_deliberation,
                stage_name="Stage 2",
                semaphore=semaphore,
            )
        )

    results = await asyncio.gather(*tasks, return_exceptions=True)

    successful: dict[str, ReviewResult] = {}
    for persona, result in zip(active_personas, results):
        if isinstance(result, Exception):
            _log(f"  WARNING: {persona.name} deliberation failed: {result}")
        else:
            successful[persona.slug] = result

    stage_cost = sum(r.cost_usd for r in successful.values())
    _log(f"Stage 2 complete. {len(successful)}/{len(active_personas)} succeeded. Cost: ${stage_cost:.2f}")

    return successful


async def run_stage3(
    client: AsyncAnthropic,
    paper_text: str,
    brief: str,
    stage1_results: dict[str, ReviewResult],
    stage2_results: dict[str, ReviewResult],
    figures: list[dict] | None = None,
) -> ReviewResult:
    _log("Stage 3: Chairman synthesis...")

    all_reviews = {slug: r.response_text for slug, r in stage1_results.items()}
    all_deliberations = {slug: r.response_text for slug, r in stage2_results.items()}

    system, msgs = build_synthesis_prompt(
        paper_text, all_reviews, all_deliberations, brief, figures
    )

    t0 = time.monotonic()
    chairman_kwargs: dict = dict(
        model=CHAIRMAN_MODEL,
        max_tokens=CHAIRMAN_MAX_TOKENS,
        system=system,
        messages=msgs,
    )
    if not CHAIRMAN_MODEL.startswith("claude-opus"):
        chairman_kwargs["temperature"] = CHAIRMAN_TEMP
    response = await client.messages.create(**chairman_kwargs)
    elapsed = round(time.monotonic() - t0, 1)

    usage = response.usage
    input_tok = usage.input_tokens
    output_tok = usage.output_tokens
    cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
    cache_create = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cost = calculate_cost(CHAIRMAN_MODEL, input_tok, output_tok, cache_read, cache_create)

    text = ""
    for block in response.content:
        if block.type == "text":
            text += block.text

    _log(f"Stage 3 complete. ({elapsed}s, {output_tok} tokens out, ${cost:.2f})")

    return ReviewResult(
        persona_name="Chairman",
        persona_slug="chairman",
        response_text=text,
        input_tokens=input_tok,
        output_tokens=output_tok,
        cache_read_tokens=cache_read,
        cache_creation_tokens=cache_create,
        model=CHAIRMAN_MODEL,
        elapsed_seconds=elapsed,
        cost_usd=cost,
    )


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(report: CouncilReport) -> str:
    lines = [
        f"# AI Research Council Report",
        f"**Paper:** {report.paper_title}",
        f"**Date:** {report.timestamp}",
        f"**Brief:** {report.brief}",
        f"**Cost:** ${report.total_cost:.2f} | "
        f"**Tokens:** {report.total_input_tokens:,} in / "
        f"{report.total_output_tokens:,} out",
        "",
        "---",
        "",
    ]

    if report.synthesis:
        lines.append(report.synthesis.response_text)
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## Individual Reviews")
    lines.append("")
    for i, (slug, result) in enumerate(report.stage1_reviews.items(), 1):
        lines.append(f"### {i}. {result.persona_name}")
        lines.append("")
        lines.append(result.response_text)
        lines.append("")

    if report.stage2_deliberations:
        lines.append("---")
        lines.append("")
        lines.append("## Deliberation Round")
        lines.append("")
        for slug, result in report.stage2_deliberations.items():
            lines.append(f"### {result.persona_name} — Revised Position")
            lines.append("")
            lines.append(result.response_text)
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Methodology")
    lines.append("")
    stages_run = "3 stages (Independent Review → Deliberation → Synthesis)"
    if not report.stage2_deliberations:
        stages_run = "2 stages (Independent Review → Synthesis, deliberation skipped)"
    lines.append(
        f"This report was generated by the AI Research Council using {stages_run}."
    )
    lines.append("")

    reviewer_models = set()
    for r in report.stage1_reviews.values():
        reviewer_models.add(r.model)
    chairman_model = report.synthesis.model if report.synthesis else "N/A"
    lines.append(f"**Reviewer models:** {', '.join(sorted(reviewer_models))}")
    lines.append(f"**Chairman model:** {chairman_model}")
    lines.append(f"**Total cost:** ${report.total_cost:.2f}")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

async def run_council(args: argparse.Namespace) -> None:
    paper_text = read_paper(args.paper_path)
    title = extract_title(paper_text)

    brief = args.brief
    if args.brief_file:
        brief = Path(args.brief_file).read_text(encoding="utf-8").strip()

    if not brief:
        print("Error: --brief or --brief-file is required.")
        sys.exit(1)

    _log(f"Paper: {title}")
    _log(f"Brief: {brief[:120]}{'...' if len(brief) > 120 else ''}")
    _log(f"Deliberation: {'ON' if not args.skip_deliberation else 'SKIPPED'}")

    if args.dry_run:
        tex_dir = Path(args.paper_path).resolve().parent
        figures = extract_figures(paper_text, tex_dir)
        num_figures = len(figures) // 2  # each figure = text label + image block
        paper_tokens_approx = len(paper_text) // 4
        figure_tokens_approx = num_figures * 1_600
        total_tokens = paper_tokens_approx + figure_tokens_approx
        _log(f"Paper size: ~{paper_tokens_approx:,} tokens (approx)")
        if num_figures:
            _log(f"Figures: {num_figures} images (~{figure_tokens_approx:,} tokens)")
        est = 2.76 if not args.skip_deliberation else 1.91
        scale = total_tokens / 15_000
        _log(f"Estimated cost: ~${est * scale:.2f} (scaled from 15K-token baseline)")
        _log("Dry run complete. No API calls made.")
        return

    client = AsyncAnthropic()
    semaphore = asyncio.Semaphore(args.max_concurrent)

    running_cost = 0.0

    # Extract figures
    tex_dir = Path(args.paper_path).resolve().parent
    figures = extract_figures(paper_text, tex_dir)

    # Stage 1
    stage1 = await run_stage1(client, paper_text, brief, REVIEWERS, semaphore, figures)
    running_cost += sum(r.cost_usd for r in stage1.values())

    if args.save_intermediate:
        _save_intermediate(args, title, "stage1", stage1)

    # Stage 2
    stage2: dict[str, ReviewResult] = {}
    if not args.skip_deliberation:
        stage2 = await run_stage2(
            client, paper_text, brief, stage1, REVIEWERS, semaphore, figures
        )
        running_cost += sum(r.cost_usd for r in stage2.values())
        if args.save_intermediate:
            _save_intermediate(args, title, "stage2", stage2)

    # Stage 3
    synthesis = await run_stage3(client, paper_text, brief, stage1, stage2, figures)
    running_cost += synthesis.cost_usd

    # Compile report
    all_results = list(stage1.values()) + list(stage2.values()) + [synthesis]
    total_input = sum(r.input_tokens for r in all_results)
    total_output = sum(r.output_tokens for r in all_results)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = CouncilReport(
        paper_path=args.paper_path,
        paper_title=title,
        brief=brief,
        timestamp=timestamp,
        stage1_reviews=stage1,
        stage2_deliberations=stage2,
        synthesis=synthesis,
        total_cost=running_cost,
        total_input_tokens=total_input,
        total_output_tokens=total_output,
    )

    report_md = generate_report(report)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^\w]+", "_", title.lower()).strip("_")[:50]
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = out_dir / f"{slug}_{ts}.md"
    out_file.write_text(report_md, encoding="utf-8")

    _log("=" * 50)
    _log("Council complete!")
    _log(f"  Total cost: ${running_cost:.2f}")
    _log(f"  Total tokens: {total_input:,} input / {total_output:,} output")
    _log(f"  Report saved to: {out_file}")

    if args.verbose:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        print("\n" + report_md)


def _save_intermediate(
    args: argparse.Namespace,
    title: str,
    stage: str,
    results: dict[str, ReviewResult],
) -> None:
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^\w]+", "_", title.lower()).strip("_")[:50]
    for persona_slug, result in results.items():
        path = out_dir / f"{slug}_{stage}_{persona_slug}.md"
        path.write_text(
            f"# {result.persona_name} — {stage}\n\n{result.response_text}",
            encoding="utf-8",
        )
    _log(f"  Saved {len(results)} intermediate files to {out_dir}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Research Strategy Council — multi-persona research direction review",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python council.py paper.tex --brief-file briefs/vision_brief.txt --verbose
  python council.py paper.tex --brief "Where should I take this research next?"
  python council.py paper.tex --brief-file briefs/strategy.txt --save-intermediate
  python council.py paper.tex --brief "Field viability check" --dry-run
""",
    )
    parser.add_argument("paper_path", help="Path to .tex file")
    parser.add_argument(
        "--brief", default="", help="Review brief: what you need from the council"
    )
    parser.add_argument(
        "--brief-file", default=None, help="Load brief from a text file"
    )
    parser.add_argument(
        "--skip-deliberation", action="store_true",
        help="Skip Stage 2 deliberation (faster, cheaper)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Estimate cost without making API calls"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print the full report to terminal after saving"
    )
    parser.add_argument(
        "--save-intermediate", action="store_true",
        help="Save individual stage results as separate files"
    )
    parser.add_argument(
        "--max-concurrent", type=int, default=MAX_CONCURRENT_REQUESTS,
        help=f"Max parallel API requests (default: {MAX_CONCURRENT_REQUESTS})"
    )
    parser.add_argument(
        "--output-dir", default="output", help="Output directory (default: output/)"
    )
    args = parser.parse_args()

    try:
        asyncio.run(run_council(args))
    except KeyboardInterrupt:
        _log("Interrupted by user. Partial results may be in the output directory.")
        sys.exit(130)


if __name__ == "__main__":
    main()
