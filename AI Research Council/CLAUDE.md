# AI Research Council

## What This Is

A Python CLI tool that sends a LaTeX research paper (.tex from Overleaf) to **6 AI reviewer personas** via the Anthropic API, runs a deliberation round where they react to each other's reviews, and synthesizes a final report with **concrete, prioritized next steps**.

Inspired by [Karpathy's LLM Council](https://github.com/karpathy/llm-council), but using persona diversity (same model, different expert lenses) instead of model diversity.

## How It Works

```
.tex file + review brief ──► Stage 1: 6 parallel Sonnet calls (independent reviews)
                           ──► Stage 2: 6 parallel Sonnet calls (anonymized deliberation)
                           ──► Stage 3: 1 Opus call (chairman synthesis + next steps)
                           ──► Markdown report saved to output/
```

**The 6 Reviewers:**
1. **Source Auditor** — Fact-checks claims, verifies citations
2. **Methodologist** — Experiment design, statistical rigor, assumptions
3. **Peer Reviewer** — Structure, clarity, novelty (NeurIPS-style)
4. **Domain Expert** — AI/ML depth, field positioning, alternative hypotheses
5. **Outsider / Red Team** — Fresh eyes, flags jargon and logical gaps
6. **Alignment Guide** — Checks if the paper delivers on its stated goals

Each reviewer stays in their lane (anti-pattern instructions prevent overlap).

## Running It

```bash
python council.py papers/my_paper.tex --brief "Is this ready for ArXiv?"
python council.py papers/my_paper.tex --brief-file briefs/my_brief.txt
python council.py papers/my_paper.tex --brief "Full peer review" --skip-deliberation
python council.py papers/my_paper.tex --brief "Quick check" --dry-run
```

- `--skip-deliberation` — skips Stage 2, costs ~$1.91 instead of ~$2.76
- `--dry-run` — estimates cost without making API calls
- `--verbose` — prints report to terminal
- `--save-intermediate` — saves each reviewer's output as a separate file

Figures in a `figures/` folder adjacent to the .tex are auto-detected and sent as images to all reviewers.

## Cost

~$2.76 per full run (20-page paper). ~$1.91 without deliberation. API key goes in `secrets.env`.

## The Brief — Why It Matters

The **brief** is the single most important input besides the paper itself. It tells all 6 reviewers what kind of feedback the author needs. Without it, they give a generic review. With it, every dollar spent produces targeted, actionable output.

The brief is passed via `--brief "..."` or `--brief-file path/to/brief.txt`.

### What the brief should contain

- **Review type**: What kind of review? (Preprint check, full peer review, methodology audit, framing evaluation, revision check)
- **Target**: Where is this going? (ArXiv, NeurIPS, ICML, journal, internal)
- **Stage**: Early draft, pre-submission, post-rejection revision, camera-ready?
- **Goals**: What is the author trying to achieve?
- **Concerns**: What specifically worries them? What needs extra attention?
- **Context**: Background not in the paper (prior rejection feedback, constraints, etc.)

### Brief length guidelines

- 1-2 sentences: too short, gets generic output
- **1 structured paragraph (100-500 tokens): ideal** — costs < $0.01 extra
- Multiple pages: diminishing returns, dilutes focus

### What NOT to put in the brief

- Raw experimental data (that belongs in the paper)
- Full literature reviews (mention specific papers by name if needed)
- Entire email threads (summarize the key points)
- Requests to "be harsh" or "be nice" (reviewers have fixed mandates)

### Example briefs

**ArXiv readiness:**
> REVIEW TYPE: Preprint readiness check. TARGET: ArXiv. STAGE: Near-final draft. GOALS: Establish priority quickly. CONCERNS: Any embarrassing errors or unsupported claims?

**Post-rejection resubmission:**
> REVIEW TYPE: Revision check. TARGET: NeurIPS 2026 (resubmission). STAGE: Revised after major revisions. GOALS: Address reviewer concerns from first round. CONCERNS: Main criticism was lack of real-world evaluation — added case study in Section 6. Is it convincing?

**Framing help:**
> REVIEW TYPE: Framing review. TARGET: Nature Machine Intelligence. GOALS: Frame this as AI Safety, but core work is a capability result. CONCERNS: Does the safety framing feel forced? Missing key references?

See `BRIEF_GUIDE.md` for the full guide with templates.

## File Structure

```
council.py       — Main CLI + async orchestration (run this)
personas.py      — 6 reviewer system prompts + prompt builders
config.py        — Model assignments, pricing, temperature settings
BRIEF_GUIDE.md   — Detailed guide on writing effective briefs
secrets.env      — API key (not committed)
papers/          — Drop .tex files here (with figures/ subfolder)
output/          — Reports land here
```

## How to Help the Author Write a Brief

When the author comes to you with a paper and needs help writing a brief:

1. **Ask what they need** — Are they checking ArXiv readiness? Preparing for a venue? Fixing a rejection? Reframing?
2. **Ask what worries them** — What section feels weakest? What feedback have they gotten before?
3. **Ask about constraints** — Deadline? Page limit? Specific reviewer concerns to address?
4. **Draft the brief using the structured format** — REVIEW TYPE / TARGET / STAGE / GOALS / CONCERNS / CONTEXT
5. **Keep it 100-500 tokens** — Specific enough to focus the reviewers, short enough to not dilute the signal
6. **Save it to a file** — e.g., `briefs/neurips_review.txt` so they can reuse and iterate

The author's research area is **AI / Machine Learning**. The domain expert persona is calibrated for this field.
