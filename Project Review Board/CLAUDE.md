# Project Review Board

## What This Is

A Python CLI tool that sends a project description (any text file) to **6 AI reviewer personas** via the Anthropic API, runs a deliberation round where they react to each other's reviews, and synthesizes a final report with **concrete, prioritized next steps**.

Same architecture as the AI Research Council, but adapted for evaluating any project, idea, product, or thing you want to build.

## How It Works

```
project description + review brief ──► Stage 1: 6 parallel Sonnet calls (independent reviews)
                                     ──► Stage 2: 6 parallel Sonnet calls (anonymized deliberation)
                                     ──► Stage 3: 1 Opus call (chairman synthesis + next steps)
                                     ──► Markdown report saved to output/
```

**The 6 Reviewers:**
1. **Feasibility Analyst** — Can this actually be built? Resources, timeline, technical risk
2. **Market Strategist** — Is there demand? Competitors, positioning, business model
3. **Devil's Advocate** — What could go wrong? Failure modes, hidden assumptions, pre-mortem
4. **User Advocate** — Who uses this? UX, adoption barriers, value proposition from the user's POV
5. **Technical Architect** — How should this be built? Architecture, tech stack, build vs. buy
6. **Scope & Priority Coach** — What's the MVP? What to cut, what to keep, phase planning

Each reviewer stays in their lane (anti-pattern instructions prevent overlap).

## Running It

```bash
python council.py projects/my_idea.md --brief "Should I build this?"
python council.py projects/my_idea.md --brief-file briefs/my_brief.txt
python council.py projects/my_idea.md --brief "Full review" --skip-deliberation
python council.py projects/my_idea.md --brief "Quick check" --dry-run
python council.py projects/my_idea.md --brief "Review this" --images mockup.png diagram.png
```

- `--images` — attach mockups, diagrams, or screenshots for reviewers to see
- `--skip-deliberation` — skips Stage 2, costs ~$1.91 instead of ~$2.76
- `--dry-run` — estimates cost without making API calls
- `--verbose` — prints report to terminal
- `--save-intermediate` — saves each reviewer's output as a separate file

## Cost

~$2.76 per full run (typical project description). ~$1.91 without deliberation. API key goes in `secrets.env`.

## The Brief — Why It Matters

The **brief** tells all 6 reviewers what kind of feedback you need. Without it, they give a generic review. With it, every dollar spent produces targeted, actionable output.

Pass via `--brief "..."` or `--brief-file path/to/brief.txt`.

See `BRIEF_GUIDE.md` for the full guide with templates.

## File Structure

```
council.py       — Main CLI + async orchestration (run this)
personas.py      — 6 reviewer system prompts + prompt builders
config.py        — Model assignments, pricing, temperature settings
app.py           — Streamlit web UI
BRIEF_GUIDE.md   — Detailed guide on writing effective briefs
secrets.env      — API key (not committed)
projects/        — Drop project descriptions here
briefs/          — Save reusable briefs here
output/          — Reports land here
```
