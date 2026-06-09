# Resume Review Board

## What This Is

A Python CLI tool that sends resume content (stories, bullets, career materials) to **6 AI reviewer personas** via the Anthropic API, runs a deliberation round where they react to each other's reviews, and synthesizes a final report with **concrete, prioritized next steps** for maximizing callbacks and competitive positioning.

Built on the same architecture as the AI Research Council, adapted for scrutinizing resume bullets, career narratives, and job-search positioning.

## How It Works

```
resume content + review brief ──► Stage 1: 6 parallel Sonnet calls (independent reviews)
                                ──► Stage 2: 6 parallel Sonnet calls (anonymized deliberation)
                                ──► Stage 3: 1 Opus call (chairman synthesis + next steps)
                                ──► Markdown report saved to output/
```

**The 6 Reviewers:**
1. **Hiring Manager** — Would I call this person? Signal vs. noise, ownership clarity, callback decision
2. **Recruiter & ATS Lens** — Keyword alignment, skills surfacing, ATS readability, recruiter quick-scan
3. **Story Architect** — Narrative coherence, personal brand, career arc, unique differentiator
4. **Bullet Surgeon** — Line-level craft: verb choice, structure, conciseness, quantification
5. **Skeptical Interviewer** — Defensibility, predicted interview questions, trap bullets, metrics scrutiny
6. **Market Benchmarker** — Competitive positioning, seniority calibration, undersold strengths, hire signal

Each reviewer stays in their lane (anti-pattern instructions prevent overlap).

## Running It

```bash
python council.py stories/01_atlas_the_system.md --brief "Review for senior DS callbacks"
python council.py stories/ --brief-file briefs/resume_review.txt
python council.py stories/09_swagup_ab_test.md --brief "Full review" --skip-deliberation
python council.py stories/01_atlas_the_system.md --brief "Quick check" --dry-run
python council.py stories/my_resume.md --brief "Review this" --images resume_screenshot.png
```

- `--images` — attach resume screenshots, JD screenshots, etc. for reviewers to see
- `--skip-deliberation` — skips Stage 2, costs ~$1.91 instead of ~$2.76
- `--dry-run` — estimates cost without making API calls
- `--verbose` — prints report to terminal
- `--save-intermediate` — saves each reviewer's output as a separate file

## Cost

~$2.76 per full run (typical story file). ~$1.91 without deliberation. API key goes in `secrets.env`.

## The Brief — Why It Matters

The **brief** tells all 6 reviewers what kind of feedback you need. Without it, they give a generic review. With it, every dollar spent produces targeted, actionable output.

Example briefs:
- "I'm targeting Senior Data Scientist roles. Will these bullets get callbacks? What's weak?"
- "Review this story for competitive positioning against other DS candidates with 5 YOE"
- "Focus on defensibility — which claims will get me in trouble during interviews?"
- "I want to position myself for Product DS roles. How should I reframe these bullets?"

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
projects/        — Drop resume content / stories here
briefs/          — Save reusable briefs here
output/          — Reports land here
```
