# Business Advisory Council

## What This Is

A Python CLI tool that sends business materials (brand descriptions, marketing copy, landing pages, pitch decks) to **8 AI advisor personas** via the Anthropic API, runs a deliberation round where they react to each other's reviews, and synthesizes a final report with **concrete, prioritized next steps** for growing an ecommerce brand.

Built on the same architecture as the AI Research Council and Project Review Board. Tailored for an emerging apparel ecommerce brand run by a 2-person team.

## How It Works

```
business materials + advisory brief ──> Stage 1: 8 parallel Sonnet calls (independent reviews)
                                     ──> Stage 2: 8 parallel Sonnet calls (anonymized deliberation)
                                     ──> Stage 3: 1 Opus call (Chief Advisory Officer synthesis)
                                     ──> Markdown report saved to output/
```

**The 8 Advisors:**
1. **Strategy Consultant** — Mission alignment, competitive moat, go-to-market, scalability
2. **Marketing Strategist** — Messaging, channels, content strategy, brand voice, email/SMS
3. **Conversion Architect** — Funnel optimization, CRO, checkout flow, lead capture, AOV
4. **The Customer** — Real buyer perspective, first impressions, trust, confusion, purchase triggers
5. **Market Analyst** — Market sizing, competitive landscape, customer segments, pricing, benchmarks
6. **Business Evaluator** — Unit economics, margins, cash flow, operational capacity, breakeven
7. **Creative Director** — Visual identity, photography, website design, packaging, brand consistency
8. **Future Visionary** — 3-5 year trends, technology opportunities, cultural relevance, future risks

Each advisor stays in their lane (anti-pattern instructions prevent overlap).

## Running It

```bash
python council.py materials/brand_overview.md --brief "Is our positioning right?"
python council.py materials/landing_page.txt --brief-file briefs/full_review.txt
python council.py materials/pitch.md --brief "Quick gut check" --skip-deliberation
python council.py materials/brand.md --brief "Full review" --dry-run
python council.py materials/brand.md --brief "Review this" --images homepage.png product.png logo.png
```

- `--images` — attach screenshots, product photos, logos, etc. for advisors to see
- `--skip-deliberation` — skips Stage 2, costs ~$1.91 instead of ~$2.76
- `--dry-run` — estimates cost without making API calls
- `--verbose` — prints report to terminal
- `--save-intermediate` — saves each advisor's output as a separate file

## Cost

~$2.76 per full run (typical materials file). ~$1.91 without deliberation. API key goes in `secrets.env`.

## The Brief — Why It Matters

The **brief** tells all 8 advisors what kind of feedback you need. Without it, they give a generic review. With it, every dollar spent produces targeted, actionable output.

Example briefs:
- "We're an emerging apparel brand pre-launch. Is our positioning clear enough to convert?"
- "Where in our funnel are we losing the most customers? Focus on conversion."
- "Review our brand identity and visual assets. Do we look trustworthy for a new brand?"
- "Full business audit — we're 3 months in with low conversion. What's wrong?"

Pass via `--brief "..."` or `--brief-file path/to/brief.txt`.

See `BRIEF_GUIDE.md` for the full guide with templates. See `briefs/BRIEF_INTAKE.md` for a detailed intake form to fill out before running a review.

## File Structure

```
council.py       — Main CLI + async orchestration (run this)
personas.py      — 8 advisor system prompts + prompt builders
config.py        — Model assignments, pricing, temperature settings
app.py           — Streamlit web UI
BRIEF_GUIDE.md   — Detailed guide on writing effective briefs
secrets.env      — API key (not committed)
materials/       — Drop business materials here
briefs/          — Save reusable briefs here (includes BRIEF_INTAKE.md)
output/          — Reports land here
```
