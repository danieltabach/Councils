"""One-off script: re-run Stage 3 synthesis using saved intermediate files."""
import asyncio
import re
import time
from datetime import datetime
from pathlib import Path

from anthropic import AsyncAnthropic
from dotenv import load_dotenv

from config import CHAIRMAN_MAX_TOKENS, CHAIRMAN_MODEL, REVIEWERS
from council import (
    CouncilReport,
    ReviewResult,
    _log,
    calculate_cost,
    extract_figures,
    extract_title,
    generate_report,
    read_paper,
)
from personas import build_synthesis_prompt

load_dotenv("secrets.env")
load_dotenv()

PAPER_PATH = r"papers\Measuring Intensity Words at the Language-to-Action Boundary\main_v3.tex"
BRIEF_PATH = r"papers\Measuring Intensity Words at the Language-to-Action Boundary\brief.txt"
OUTPUT_DIR = Path("output")
PREFIX = "measuring_intensity_words_at_the_language_to_actio"

SLUGS = [r.slug for r in REVIEWERS]
NAME_MAP = {r.slug: r.name for r in REVIEWERS}


def load_intermediate(stage: str) -> dict[str, ReviewResult]:
    results = {}
    for slug in SLUGS:
        path = OUTPUT_DIR / f"{PREFIX}_{stage}_{slug}.md"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        # Strip the header line
        lines = text.split("\n", 2)
        body = lines[2] if len(lines) > 2 else text
        results[slug] = ReviewResult(
            persona_name=NAME_MAP[slug],
            persona_slug=slug,
            response_text=body,
            input_tokens=0, output_tokens=0,
            cache_read_tokens=0, cache_creation_tokens=0,
            model="claude-sonnet-4-6", elapsed_seconds=0, cost_usd=0,
        )
    return results


async def main():
    paper_text = read_paper(PAPER_PATH)
    title = extract_title(paper_text)
    brief = Path(BRIEF_PATH).read_text(encoding="utf-8").strip()
    tex_dir = Path(PAPER_PATH).resolve().parent
    figures = extract_figures(paper_text, tex_dir)

    stage1 = load_intermediate("stage1")
    stage2 = load_intermediate("stage2")
    _log(f"Loaded {len(stage1)} stage1 + {len(stage2)} stage2 reviews")

    all_reviews = {s: r.response_text for s, r in stage1.items()}
    all_delib = {s: r.response_text for s, r in stage2.items()}
    system, msgs = build_synthesis_prompt(paper_text, all_reviews, all_delib, brief, figures)

    client = AsyncAnthropic()
    _log("Stage 3: Chairman synthesis...")
    t0 = time.monotonic()

    kwargs = dict(model=CHAIRMAN_MODEL, max_tokens=CHAIRMAN_MAX_TOKENS,
                  system=system, messages=msgs)
    if not CHAIRMAN_MODEL.startswith("claude-opus"):
        kwargs["temperature"] = 0.3
    response = await client.messages.create(**kwargs)

    elapsed = round(time.monotonic() - t0, 1)
    usage = response.usage
    cost = calculate_cost(CHAIRMAN_MODEL, usage.input_tokens, usage.output_tokens,
                          getattr(usage, "cache_read_input_tokens", 0) or 0,
                          getattr(usage, "cache_creation_input_tokens", 0) or 0)
    text = "".join(b.text for b in response.content if b.type == "text")
    _log(f"Stage 3 complete. ({elapsed}s, {usage.output_tokens} tokens out, ${cost:.2f})")

    synthesis = ReviewResult("Chairman", "chairman", text,
                             usage.input_tokens, usage.output_tokens,
                             0, 0, CHAIRMAN_MODEL, elapsed, cost)

    # Approximate stage 1+2 cost from the original run
    prior_cost = 2.06
    total_cost = prior_cost + cost

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = CouncilReport(PAPER_PATH, title, brief, timestamp,
                           stage1, stage2, synthesis, total_cost,
                           usage.input_tokens, usage.output_tokens)
    report_md = generate_report(report)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = OUTPUT_DIR / f"{PREFIX}_{ts}.md"
    out_file.write_text(report_md, encoding="utf-8")
    _log(f"Report saved to: {out_file}")
    _log(f"Stage 3 cost: ${cost:.2f} | Total (incl. prior stages): ${total_cost:.2f}")
    print("\n" + report_md)


if __name__ == "__main__":
    asyncio.run(main())
