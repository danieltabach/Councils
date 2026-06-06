#!/usr/bin/env python3
"""Project Review Board — Multi-persona project/idea review via Anthropic API."""

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
class BoardReport:
    project_path: str
    project_title: str
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


def extract_title(text: str, filepath: str = "") -> str:
    """Extract a title from the proposal text or fall back to the filename."""
    for line in text.strip().splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        if line and not line.startswith("#"):
            title = line[:100].strip()
            if title:
                return title
            break
    if filepath:
        return Path(filepath).stem.replace("_", " ").replace("-", " ").title()
    return "Untitled Project"


def read_proposal(path: str) -> str:
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
# Image loading (optional attachments)
# ---------------------------------------------------------------------------

SUPPORTED_IMAGE_EXTENSIONS: dict[str, str] = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


def load_images(image_paths: list[str]) -> list[dict]:
    """Load image files and return API content blocks."""
    blocks: list[dict] = []
    for img_path in image_paths:
        p = Path(img_path)
        if not p.exists():
            _log(f"  Image not found: {img_path}, skipping")
            continue
        ext = p.suffix.lower()
        media_type = SUPPORTED_IMAGE_EXTENSIONS.get(ext)
        if media_type is None:
            _log(f"  Unsupported image format: {p.name}, skipping")
            continue
        data = base64.b64encode(p.read_bytes()).decode("utf-8")
        blocks.append({"type": "text", "text": f"[Image: {p.name}]"})
        blocks.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": data,
            },
        })
        _log(f"  {p.name} — loaded ({p.stat().st_size // 1024}KB)")

    if blocks:
        _log(f"  {len(blocks) // 2} image(s) will be sent to reviewers")
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
    proposal_text: str,
    brief: str,
    reviewers: list[PersonaConfig],
    semaphore: asyncio.Semaphore,
    images: list[dict] | None = None,
) -> dict[str, ReviewResult]:
    _log(f"Stage 1: Dispatching {len(reviewers)} independent reviews...")

    tasks = []
    for persona in reviewers:
        system, msgs = build_review_prompt(persona.slug, proposal_text, brief, images)
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
    proposal_text: str,
    brief: str,
    stage1_results: dict[str, ReviewResult],
    reviewers: list[PersonaConfig],
    semaphore: asyncio.Semaphore,
    images: list[dict] | None = None,
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
            persona.slug, proposal_text, all_reviews, brief, images
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
    proposal_text: str,
    brief: str,
    stage1_results: dict[str, ReviewResult],
    stage2_results: dict[str, ReviewResult],
    images: list[dict] | None = None,
) -> ReviewResult:
    _log("Stage 3: Chairman synthesis...")

    all_reviews = {slug: r.response_text for slug, r in stage1_results.items()}
    all_deliberations = {slug: r.response_text for slug, r in stage2_results.items()}

    system, msgs = build_synthesis_prompt(
        proposal_text, all_reviews, all_deliberations, brief, images
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

def generate_report(report: BoardReport) -> str:
    lines = [
        f"# Project Review Board Report",
        f"**Project:** {report.project_title}",
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
        f"This report was generated by the Project Review Board using {stages_run}."
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

async def run_board(args: argparse.Namespace) -> None:
    proposal_text = read_proposal(args.project_path)
    title = extract_title(proposal_text, args.project_path)

    brief = args.brief
    if args.brief_file:
        brief = Path(args.brief_file).read_text(encoding="utf-8").strip()

    if not brief:
        print("Error: --brief or --brief-file is required.")
        sys.exit(1)

    _log(f"Project: {title}")
    _log(f"Brief: {brief[:120]}{'...' if len(brief) > 120 else ''}")
    _log(f"Deliberation: {'ON' if not args.skip_deliberation else 'SKIPPED'}")

    if args.dry_run:
        proposal_tokens_approx = len(proposal_text) // 4
        _log(f"Proposal size: ~{proposal_tokens_approx:,} tokens (approx)")
        est = 2.76 if not args.skip_deliberation else 1.91
        scale = proposal_tokens_approx / 15_000
        _log(f"Estimated cost: ~${est * scale:.2f} (scaled from 15K-token baseline)")
        _log("Dry run complete. No API calls made.")
        return

    client = AsyncAnthropic()
    semaphore = asyncio.Semaphore(args.max_concurrent)

    running_cost = 0.0

    # Load optional images
    images = []
    if args.images:
        images = load_images(args.images)

    # Stage 1
    stage1 = await run_stage1(client, proposal_text, brief, REVIEWERS, semaphore, images)
    running_cost += sum(r.cost_usd for r in stage1.values())

    if args.save_intermediate:
        _save_intermediate(args, title, "stage1", stage1)

    # Stage 2
    stage2: dict[str, ReviewResult] = {}
    if not args.skip_deliberation:
        stage2 = await run_stage2(
            client, proposal_text, brief, stage1, REVIEWERS, semaphore, images
        )
        running_cost += sum(r.cost_usd for r in stage2.values())
        if args.save_intermediate:
            _save_intermediate(args, title, "stage2", stage2)

    # Stage 3
    synthesis = await run_stage3(client, proposal_text, brief, stage1, stage2, images)
    running_cost += synthesis.cost_usd

    # Compile report
    all_results = list(stage1.values()) + list(stage2.values()) + [synthesis]
    total_input = sum(r.input_tokens for r in all_results)
    total_output = sum(r.output_tokens for r in all_results)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = BoardReport(
        project_path=args.project_path,
        project_title=title,
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
    _log("Board review complete!")
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
        description="Project Review Board — multi-persona project/idea review",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  python council.py projects/my_idea.md --brief "Should I build this?"
  python council.py projects/startup_pitch.txt --brief "Is the MVP scoped right?"
  python council.py projects/app_concept.md --brief-file briefs/my_brief.txt --verbose
  python council.py projects/side_project.md --brief "Quick feasibility check" --dry-run
  python council.py projects/idea.md --brief "Full review" --images mockup.png arch.png
""",
    )
    parser.add_argument("project_path", help="Path to project description file (.md, .txt, etc.)")
    parser.add_argument(
        "--brief", default="", help="Review brief: what you need from the board"
    )
    parser.add_argument(
        "--brief-file", default=None, help="Load brief from a text file"
    )
    parser.add_argument(
        "--images", nargs="*", default=None,
        help="Optional image files to include (mockups, diagrams, etc.)"
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
        asyncio.run(run_board(args))
    except KeyboardInterrupt:
        _log("Interrupted by user. Partial results may be in the output directory.")
        sys.exit(130)


if __name__ == "__main__":
    main()
