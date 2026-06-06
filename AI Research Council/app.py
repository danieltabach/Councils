"""AI Research Council — Streamlit interface."""

import asyncio
import tempfile
from datetime import datetime
from pathlib import Path

import streamlit as st
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

from config import (
    CHAIRMAN_MAX_TOKENS,
    CHAIRMAN_MODEL,
    MAX_CONCURRENT_REQUESTS,
    REVIEWERS,
)
from council import (
    CouncilReport,
    ReviewResult,
    calculate_cost,
    extract_figures,
    extract_title,
    generate_report,
)
from personas import (
    build_deliberation_prompt,
    build_review_prompt,
    build_synthesis_prompt,
)

load_dotenv("secrets.env")
load_dotenv()

st.set_page_config(page_title="AI Research Council", page_icon=":", layout="wide")


# ------------------------------------------------------------------
# Async helpers (adapted from council.py for Streamlit progress)
# ------------------------------------------------------------------

async def _call_single(client, persona, system, msgs, temperature, max_tokens, sem):
    import time
    async with sem:
        t0 = time.monotonic()
        kwargs = dict(
            model=persona.model,
            max_tokens=max_tokens,
            system=system,
            messages=msgs,
        )
        if not persona.model.startswith("claude-opus"):
            kwargs["temperature"] = temperature
        response = await client.messages.create(**kwargs)
        elapsed = round(time.monotonic() - t0, 1)
        usage = response.usage
        cost = calculate_cost(
            persona.model, usage.input_tokens, usage.output_tokens,
            getattr(usage, "cache_read_input_tokens", 0) or 0,
            getattr(usage, "cache_creation_input_tokens", 0) or 0,
        )
        text = "".join(b.text for b in response.content if b.type == "text")
        return ReviewResult(
            persona_name=persona.name, persona_slug=persona.slug,
            response_text=text, input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
            cache_read_tokens=getattr(usage, "cache_read_input_tokens", 0) or 0,
            cache_creation_tokens=getattr(usage, "cache_creation_input_tokens", 0) or 0,
            model=persona.model, elapsed_seconds=elapsed, cost_usd=cost,
        )


async def run_pipeline(paper_text, brief, figures, skip_delib, progress_container):
    client = AsyncAnthropic()
    sem = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
    running_cost = 0.0

    # --- Stage 1 ---
    with progress_container.status("Stage 1: Independent Reviews", expanded=True) as s1:
        s1.write(f"Dispatching {len(REVIEWERS)} reviewers in parallel...")
        tasks = []
        for p in REVIEWERS:
            sys_prompt, msgs = build_review_prompt(p.slug, paper_text, brief, figures)
            tasks.append(_call_single(client, p, sys_prompt, msgs,
                                      p.stage1_temp, p.max_tokens_review, sem))
        raw = await asyncio.gather(*tasks, return_exceptions=True)
        stage1 = {}
        for persona, result in zip(REVIEWERS, raw):
            if isinstance(result, Exception):
                s1.write(f"  {persona.name}: FAILED — {result}")
            else:
                stage1[persona.slug] = result
                s1.write(f"  {result.persona_name}: done ({result.elapsed_seconds}s, ${result.cost_usd:.2f})")
        stage_cost = sum(r.cost_usd for r in stage1.values())
        running_cost += stage_cost
        s1.update(label=f"Stage 1 complete — {len(stage1)}/6 succeeded — ${stage_cost:.2f}",
                  state="complete")

    if len(stage1) < 3:
        progress_container.error("Fewer than 3 reviewers succeeded. Aborting.")
        return None

    # --- Stage 2 ---
    stage2 = {}
    if not skip_delib:
        with progress_container.status("Stage 2: Deliberation Round", expanded=True) as s2:
            all_reviews = {s: r.response_text for s, r in stage1.items()}
            tasks = []
            active = []
            for p in REVIEWERS:
                if p.slug not in all_reviews:
                    continue
                sys_prompt, msgs = build_deliberation_prompt(
                    p.slug, paper_text, all_reviews, brief, figures)
                active.append(p)
                tasks.append(_call_single(client, p, sys_prompt, msgs,
                                          p.stage2_temp, p.max_tokens_deliberation, sem))
            raw = await asyncio.gather(*tasks, return_exceptions=True)
            for persona, result in zip(active, raw):
                if isinstance(result, Exception):
                    s2.write(f"  {persona.name}: FAILED — {result}")
                else:
                    stage2[persona.slug] = result
                    s2.write(f"  {result.persona_name}: done ({result.elapsed_seconds}s, ${result.cost_usd:.2f})")
            stage_cost = sum(r.cost_usd for r in stage2.values())
            running_cost += stage_cost
            s2.update(label=f"Stage 2 complete — {len(stage2)}/{len(active)} succeeded — ${stage_cost:.2f}",
                      state="complete")

    # --- Stage 3 ---
    with progress_container.status("Stage 3: Chairman Synthesis", expanded=True) as s3:
        s3.write(f"Chairman ({CHAIRMAN_MODEL}) synthesizing all reviews...")
        all_reviews = {s: r.response_text for s, r in stage1.items()}
        all_delib = {s: r.response_text for s, r in stage2.items()}
        sys_prompt, msgs = build_synthesis_prompt(
            paper_text, all_reviews, all_delib, brief, figures)

        import time
        t0 = time.monotonic()
        chairman_kwargs = dict(
            model=CHAIRMAN_MODEL, max_tokens=CHAIRMAN_MAX_TOKENS,
            system=sys_prompt, messages=msgs,
        )
        if not CHAIRMAN_MODEL.startswith("claude-opus"):
            chairman_kwargs["temperature"] = 0.3
        response = await client.messages.create(**chairman_kwargs)
        elapsed = round(time.monotonic() - t0, 1)
        usage = response.usage
        cost = calculate_cost(
            CHAIRMAN_MODEL, usage.input_tokens, usage.output_tokens,
            getattr(usage, "cache_read_input_tokens", 0) or 0,
            getattr(usage, "cache_creation_input_tokens", 0) or 0,
        )
        text = "".join(b.text for b in response.content if b.type == "text")
        synthesis = ReviewResult(
            "Chairman", "chairman", text,
            usage.input_tokens, usage.output_tokens,
            getattr(usage, "cache_read_input_tokens", 0) or 0,
            getattr(usage, "cache_creation_input_tokens", 0) or 0,
            CHAIRMAN_MODEL, elapsed, cost,
        )
        running_cost += cost
        s3.write(f"  Chairman: done ({elapsed}s, ${cost:.2f})")
        s3.update(label=f"Stage 3 complete — ${cost:.2f}", state="complete")

    # --- Compile ---
    all_results = list(stage1.values()) + list(stage2.values()) + [synthesis]
    report = CouncilReport(
        paper_path="uploaded",
        paper_title=extract_title(paper_text),
        brief=brief,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        stage1_reviews=stage1,
        stage2_deliberations=stage2,
        synthesis=synthesis,
        total_cost=running_cost,
        total_input_tokens=sum(r.input_tokens for r in all_results),
        total_output_tokens=sum(r.output_tokens for r in all_results),
    )
    return report


# ------------------------------------------------------------------
# UI
# ------------------------------------------------------------------

st.title("AI Research Council")
st.caption("Multi-persona research paper review powered by Claude")

# --- Upload section ---
col_upload, col_brief = st.columns([1, 1])

with col_upload:
    st.subheader("Paper")
    tex_file = st.file_uploader("Upload your .tex file", type=["tex"])
    fig_files = st.file_uploader(
        "Upload figures (optional)",
        type=["png", "jpg", "jpeg", "gif", "webp"],
        accept_multiple_files=True,
    )
    if tex_file:
        st.success(f"{tex_file.name} loaded")
    if fig_files:
        st.info(f"{len(fig_files)} figure(s) uploaded")

with col_brief:
    st.subheader("Review Brief")
    brief_input = st.text_area(
        "What do you need from the council?",
        height=260,
        placeholder=(
            "REVIEW TYPE: ArXiv readiness check\n"
            "TARGET: ArXiv preprint\n"
            "STAGE: Near-final draft\n"
            "GOALS: Establish priority\n"
            "CONCERNS: Are my statistical claims defensible?"
        ),
    )
    brief_file = st.file_uploader("...or upload a brief.txt", type=["txt"])

    with st.expander("Brief writing tips"):
        st.markdown("""
**Include:** Review type, target venue, stage, goals, specific concerns, context.

**Sweet spot:** 100-500 tokens (~1 structured paragraph). Costs < $0.01 extra.

**Don't include:** Raw data, full lit reviews, email threads, "be harsh/nice" requests.

See `BRIEF_GUIDE.md` for full guide with templates.
""")

# --- Settings ---
st.divider()
col_settings, col_run = st.columns([2, 1])

with col_settings:
    skip_delib = st.checkbox("Skip deliberation (faster, cheaper)")
    save_to_disk = st.checkbox("Also save report to output/ folder", value=True)

with col_run:
    st.markdown("")
    st.markdown("")
    cost_est = "~$1.91 – $3.02" if skip_delib else "~$2.76 – $4.37"
    st.metric("Estimated cost", cost_est)
    run_button = st.button("Run Council", type="primary", use_container_width=True)

# --- Execution ---
if run_button:
    # Validate
    brief = brief_input.strip()
    if brief_file:
        brief = brief_file.read().decode("utf-8").strip()
    if not tex_file:
        st.error("Upload a .tex file first.")
        st.stop()
    if not brief:
        st.error("Write a review brief or upload a brief.txt.")
        st.stop()

    # Save uploaded files to temp dir for figure resolution
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        paper_bytes = tex_file.read()
        paper_text = paper_bytes.decode("utf-8", errors="replace")
        tex_path = tmp / tex_file.name
        tex_path.write_bytes(paper_bytes)

        figures = []
        if fig_files:
            fig_dir = tmp / "figures"
            fig_dir.mkdir()
            for f in fig_files:
                (fig_dir / f.name).write_bytes(f.read())
            figures = extract_figures(paper_text, tmp)

        title = extract_title(paper_text)
        st.subheader(f"Reviewing: {title}")

        progress = st.container()
        report = asyncio.run(run_pipeline(paper_text, brief, figures, skip_delib, progress))

    if report:
        report_md = generate_report(report)

        st.divider()
        st.success(
            f"Council complete! Total cost: ${report.total_cost:.2f} | "
            f"Tokens: {report.total_input_tokens:,} in / {report.total_output_tokens:,} out"
        )

        # Save to disk
        if save_to_disk:
            import re
            out_dir = Path("output")
            out_dir.mkdir(exist_ok=True)
            slug = re.sub(r"[^\w]+", "_", title.lower()).strip("_")[:50]
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_file = out_dir / f"{slug}_{ts}.md"
            out_file.write_text(report_md, encoding="utf-8")
            st.caption(f"Report saved to: {out_file}")

        # Download button
        st.download_button(
            "Download Report (.md)",
            data=report_md,
            file_name=f"council_report_{datetime.now().strftime('%Y%m%d')}.md",
            mime="text/markdown",
        )

        # Display report in tabs
        tab_summary, tab_reviews, tab_delib, tab_full = st.tabs([
            "Summary & Next Steps", "Individual Reviews", "Deliberation", "Full Report"
        ])

        with tab_summary:
            if report.synthesis:
                st.markdown(report.synthesis.response_text)

        with tab_reviews:
            for i, (slug, result) in enumerate(report.stage1_reviews.items(), 1):
                with st.expander(f"{i}. {result.persona_name} ({result.elapsed_seconds}s, ${result.cost_usd:.2f})"):
                    st.markdown(result.response_text)

        with tab_delib:
            if report.stage2_deliberations:
                for slug, result in report.stage2_deliberations.items():
                    with st.expander(f"{result.persona_name} — Revised Position"):
                        st.markdown(result.response_text)
            else:
                st.info("Deliberation was skipped for this run.")

        with tab_full:
            st.markdown(report_md)
