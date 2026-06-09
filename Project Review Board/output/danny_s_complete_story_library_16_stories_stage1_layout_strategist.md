# Layout Strategist — stage1

# Layout Strategist Review: Danny Tabach — One-Page Resume

---

## Recommended Section Order

For a candidate targeting AI labs, FAANG, and Tier 2 fintech, the section order should be:

```
[Name + Contact + Links]
EXPERIENCE
EDUCATION
SKILLS
PROJECTS
```

**Why this order, not the common Education-first or Skills-first variants:**

Experience leads because Danny has 5 YOE and his anchor story (ATLAS/BAR) is the entire argument for a callback. A recruiter scanning the top third needs to hit that story within 2 seconds. Education is short (MS in progress, BS) and goes below Experience — it adds credential without consuming prime real estate. Skills is a compact keyword row that bridges Experience and Projects. Projects is last because it houses the ArXiv papers, which are a differentiator but not the primary argument — they support the "I do AI research" claim made by the Experience section.

**What NOT to do:**
- Do not put a Summary/Objective section. Danny has 5 YOE and two ArXiv papers. The resume should show, not tell.
- Do not split JPMC into sub-roles (BAR/ABME/ARB as separate entries). One JPMC block with 4-5 bullets reads faster and preserves vertical space.
- Do not put Skills first. Danny is not a new grad padding with tools.

---

## Space Allocation

### The One-Page Math

A standard one-page resume at 10.5-11pt body text with 0.5" margins gives approximately **52-58 lines of usable content**. Here is how those lines should be spent:

| Section | Lines | Reasoning |
|---|---|---|
| Header (name, contact, links) | 3-4 | Tight. One row for links. |
| EXPERIENCE header | 1 | |
| JPMC — title + dates | 2 | One line company/title, one line dates or combined |
| JPMC bullets | 4-5 | This is the anchor. More below. |
| SwagUp — title + dates | 2 | |
| SwagUp bullets | 2-3 | One flagship (A/B test), one supporting |
| FAST — title + dates | 2 | |
| FAST bullets | 1-2 | One bullet only |
| EDUCATION header | 1 | |
| GT MS + GPA/expected | 1-2 | |
| Undergrad | 1 | |
| SKILLS header + row(s) | 2-3 | Compact keyword block |
| PROJECTS header | 1 | |
| ArXiv paper 1 (Story 14) | 2 | Title line + one-sentence finding |
| ArXiv paper 2 (Story 16) | 2 | Title line + one-sentence finding |
| Optional: ABME blog link | 1 | One line, no bullet — just the URL + descriptor |
| **Total** | **~52-58** | Fits one page |

### JPMC Space Allocation — The Critical Decision

JPMC gets the most real estate: **4-5 bullets maximum**. Here is the specific allocation:

- **1 bullet: ATLAS system** (what it is — Tier 1 bullet from Story 1)
- **1 bullet: ATLAS impact** ($9B projected, CEO sign-off, scale — from Story 2)
- **1 bullet: ABME experiment** (the 10k-employee staggered DiD — from Story 4)
- **1 bullet: architecture/methodology depth** (pick ONE from Story 3 — which one depends on target role variant, discussed below)
- **Optional 5th bullet: ARB or FAST propensity** — only if the 4 above fit comfortably and space remains

The ATLAS system bullet and ATLAS impact bullet should be adjacent and read as a unit. The reader should understand in two lines: *what Danny built* and *what it was worth*. Do not separate them with an unrelated bullet.

### SwagUp Space Allocation

**2-3 bullets maximum.** SwagUp demonstrates startup experience, experimentation, and product instinct — all three are valuable, but JPMC is the anchor. SwagUp should not compete for equal real estate.

- **1 bullet: A/B test (Story 9)** — always. This is the cleanest impact story outside JPMC.
- **1 bullet: Churn model (Story 11) OR product catalog (Story 10)** — pick based on target role. For AI labs and research roles, Story 11 (production ML). For product DS roles, Story 10 (product instinct).
- Story 12 (dashboards) only if targeting analytics engineering roles where GCP/Looker/Fivetran are keywords.

### FAST Space Allocation

**1 bullet maximum.** FAST predates Danny's senior work and the individual stories (propensity-to-pay, XGBoost segmentation) are supporting evidence, not headliners. One bullet, pick the strongest for the target role:
- For MLE/AI roles: Story 7 (XGBoost + PySpark, 5M customers)
- For experimentation/decision science roles: Story 6 (propensity-to-pay, behavioral features)
- Story 8 (household acquisition) should not appear on any version of this resume going forward.

### Projects Section Space Allocation

**4 lines total for both ArXiv papers.** Each paper gets:
- Line 1: Paper title + ArXiv ID + "Solo-authored preprint"
- Line 2: One sentence — the finding, not the methodology

The ABME blog (danieltabach.github.io) should appear as a single line under a "Technical Writing" label, not as a full project entry. It is a work sample, not a publication.

Story 13 (drift detection) does NOT appear in the Projects section unless targeting a pure MLE/monitoring role. It competes with the ArXiv papers for space and loses — the ArXiv papers are stronger credentials.

---

## Stories to Include vs. Cut

### Stories That Make the Cut (all target variants)

| Story | Reason |
|---|---|
| Story 1: ATLAS System | Non-negotiable anchor. Every version. |
| Story 2: ATLAS Impact | Non-negotiable. The $9B/CEO sign-off is the business punchline. |
| Story 4: ABME DiD | Non-negotiable for experimentation-heavy targets. The 10k-employee staggered DiD is Danny's strongest methodology story. |
| Story 9: SwagUp A/B Test | Always. Cleanest external impact story. |
| Story 14: ArXiv (AI Detection) | Non-negotiable per candidate brief. Projects section. |
| Story 16: ArXiv (LLM Vague Intensity) | Non-negotiable per candidate brief. Projects section. |

### Stories That Make the Cut Conditionally

| Story | Include When |
|---|---|
| Story 3: ATLAS Architecture | Include ONE bullet from this story when JD emphasizes production systems, solver design, or config-driven architecture. Replaces the "optional 5th" JPMC bullet. |
| Story 7: XGBoost/PySpark (FAST) | Include as the single FAST bullet for MLE-adjacent and AI lab targets. |
| Story 6: Propensity-to-Pay (FAST) | Include as the single FAST bullet for decision science and product DS targets. |
| Story 11: Churn Model (SwagUp) | Include as second SwagUp bullet for MLE and production ML roles. |
| Story 10: Product Catalog (SwagUp) | Include as second SwagUp bullet for product DS and GTM analytics roles. |
| Story 5: ARB Matched-Pairs | Include as optional 5th JPMC bullet only if the JD specifically mentions propensity modeling, small-sample causal inference, or matched-pairs. Drops off for most targets. |

### Stories That Are Cut

| Story | Why Cut |
|---|---|
| Story 8: Household Acquisition | Too vague, too old, no defensible numbers. Dropped from Danny's own resumes after #6. Remove permanently. |
| Story 12: Analytics Dashboards (SwagUp) | Replaced by stronger stories. Only resurfaces for analytics engineering roles where Fivetran/Looker/DBT are primary JD keywords. |
| Story 13: Drift Detection (GT) | Competes with ArXiv papers in Projects and loses. Use only for pure MLE/monitoring roles where the other two papers are less relevant. |
| Story 15: Consulting NLP | Lowest priority. Only if the resume has a gap that needs filling — which it won't. Remove from general rotation. |

### The Consulting Entry (Story 15) — Layout Consideration

If Consulting appears as a separate Experience entry, it consumes 2-3 lines (title, dates, 1 bullet) that could go to JPMC depth or Projects. The recommendation is to **remove Consulting as a standalone Experience entry** and, if the NLP work is relevant to a specific JD, fold it into the Skills section as a tool mention or omit entirely. The ArXiv papers already demonstrate Danny's research credibility. The consulting work does not add to that story.

---

## Visual Hierarchy Assessment

### Where Does the Eye Go?

On a standard resume, the eye lands on the **top third** first — roughly the first 18-20 lines. For Danny's resume, that top third must contain:

1. **Name + links** — including ArXiv profile or GitHub. The ArXiv papers are a differentiator; make them findable.
2. **JPMorgan Chase title + dates** — "Data Scientist" with the date range signals 5 YOE immediately.
3. **ATLAS system bullet** — the reader must hit this within 3 seconds.
4. **ATLAS impact bullet** — $9B projected, 4,300+ branches, CEO sign-off.

If ATLAS doesn't land in the top third, the resume is structurally broken regardless of bullet quality.

### Current Hierarchy Risks to Avoid

Based on the story library and historic resume variants, these are the visual hierarchy failure modes Danny has exhibited across his 20 resume versions:

**Risk 1: Three or more ATLAS bullets before any other story appears.** The reader needs to know Danny can do more than one thing. Four ATLAS bullets in a row reads as a one-trick portfolio. The ATLAS system + impact pair is the anchor; the third ATLAS bullet (if used) should follow an ABME or SwagUp bullet to show range.

**Risk 2: The $9B number appearing before the reader knows what ATLAS is.** Several historic resumes lead with "$150M" or "$9B" before explaining the system. Impact-first construction works only when the reader already has context. On a first-read cold resume, the system description must precede the impact claim.

**Risk 3: The Projects section buried below a long Skills block.** The ArXiv papers are a differentiator. If Skills runs 4-5 lines and Projects is at the bottom of the page, a 6-second scanner never reaches the papers. Skills should be a compact 2-line keyword block, not a categorized table.

**Risk 4: Education consuming prime real estate.** If Education appears before Experience (common in student-era resumes), the MS in progress and undergraduate degree are the first things a recruiter sees. For a 5-YOE candidate, this is the wrong hierarchy.

### What the Strongest Position Looks Like

```
[Name] | [email] | [LinkedIn] | [GitHub] | [ArXiv profile or personal site]

EXPERIENCE
──────────────────────────────────────────────────────────────────────
Data Scientist | JPMorgan Chase | [dates]
• [ATLAS system bullet — Tier 1-A or 1-B]
• [ATLAS impact bullet — $9B, CEO sign-off]
• [ABME DiD bullet — 10k employees, staggered event study]
• [Architecture or methodology depth — ONE bullet from Story 3]
```

The reader hits the most impressive content in lines 5-12. That is where the callback decision is made.

---

## Projects Section Strategy

### The ArXiv Papers Are Non-Negotiable — But Format Matters

The Projects section exists to do one job: signal "I do independent AI research." Two solo-authored ArXiv preprints accomplish this. The formatting must make that signal land fast.

**Recommended format for each paper:**

```
AI Detection Warning Effects on Writing Behavior | Solo-authored | ArXiv: 2604.23471
Designed two-phase controlled experiment (21 writers, 251 judges, ~2,000 evaluations); found 
judges identify warned writers as human at p=0.000243 — invisible to four ML classifiers.
```

```
Vague Intensity Words in LLM Tool-Use Actions | Solo-authored | ArXiv: 2605.21827  
Demonstrated that system state dominates user word choice 10:1 in LLM tool-call behavior; 
10 intensity words compress into ~5 distinct outputs across 6,620 controlled runs.
```

**What this format accomplishes:**
- "Solo-authored" appears immediately — signals independent research capability
- ArXiv ID is visible — verifiable, signals legitimacy
- The finding is in the second line — not the methodology, the finding
- Two papers together occupy ~8 lines — tight enough to fit below Skills

### How the Papers Should Be Framed vs. Work Experience

The work experience bullets should read as **builder stories** ("built," "designed," "deployed"). The Projects bullets should read as **research findings** — the punchline of what was discovered, not what was constructed. This distinction matters for AI lab targets: they want to see that Danny can formulate a question, not just ship a system.

The infrastructure details (Streamlit, Supabase, 29 automated tests) belong in interviews, not on the resume. The resume gets one sentence per paper — the finding. The conversation gets the rest.

### The Blog Post

`danieltabach.github.io` should appear as a single line in Projects or in the header links row:

```
Technical Writing: Staggered DiD Event-Study for Messy Rollouts — danieltabach.github.io
```

This is not a full project entry. It is a work sample link. It demonstrates the ABME methodology without consuming bullet space.

---

## Role-Specific Layout Variants

### Variant A: AI Labs (OpenAI, Anthropic, DeepMind)

These targets are reading for research credibility and systems thinking. The resume must communicate "I do independent research AND I build production systems."

**Layout changes:**
- Lead JPMC with **Story 1-A** (OR/Applied Scientist formulation bullet) — shows mathematical rigor
- Story 16 (LLM Vague Intensity) moves to **top of Projects** — it's directly relevant to alignment and agentic AI
- Story 14 (AI Detection) follows immediately
- The ABME bullet should use the **methodology-forward variant** (event-study DiD, staggered adoption) — shows experiment design maturity
- FAST bullet: Story 7 (XGBoost/PySpark) — signals ML production experience
- SwagUp: Story 9 only (one bullet) — the startup story is supporting evidence, not a headline
- Consider adding a one-line "Research Interests" field under Education: "Agentic AI safety, LLM behavioral measurement, constrained optimization" — this signals intent without consuming bullet space

**What to cut for this variant:** ARB (Story 5), Consulting (Story 15), SwagUp churn model (Story 11), dashboard story (Story 12)

### Variant B: Google/Apple/FAANG-Adjacent Decision Science

These targets are reading for experimentation depth, causal inference, and scale. The resume must communicate "I run rigorous experiments at scale AND I ship systems."

**Layout changes:**
- Lead JPMC with **Story 1-B** (Decision Scientist — causal value estimation + constrained optimization)
- ABME bullet uses **Tier 1-B** (event-study DiD, metrics framework, CEO approval)
- Include Story 3 architecture bullet using **[B — Causal + optimization blend]** as the 4th JPMC bullet
- FAST bullet: Story 6 (propensity-to-pay, behavioral features, ROC curve tuning)
- SwagUp: Story 9 (A/B test) + Story 10 (product catalog, product instinct) — two bullets
- Story 14 leads Projects (experiment design is the primary signal)

**What to cut for this variant:** ARB (Story 5), Consulting (Story 15), Story 11 (churn model)

### Variant C: Stripe/PayPal/Intuit/Shopify Product DS

These targets are reading for product instinct, GTM analytics, and end-to-end ownership. The resume must communicate "I identify problems, design solutions, and ship them."

**Layout changes:**
- Lead JPMC with **Story 1-C** (automated decision platform, 7+ teams, C-suite, enterprise