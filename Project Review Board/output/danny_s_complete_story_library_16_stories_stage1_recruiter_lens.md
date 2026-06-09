# Recruiter & ATS Lens — stage1

# Recruiter & ATS Lens Review: Danny Tabach

---

## Preliminary Note on Scope

This is a story library review, not a formatted resume review. I'm evaluating the raw material — bullet variants, approved selections, agent rules — against the target role landscape. My job is to tell Danny which bullets survive the 6-second scan, which get past ATS, and which need rework before they touch a resume. I'll address all six items in the brief where they fall within my mandate.

---

## Keyword & Language Alignment

### What's Working

The story library uses language that maps well to the DS/Applied Scientist JD landscape, but coverage is uneven across role types.

**Strong keyword coverage:**
- "MILP," "constrained optimization," "XGBoost," "PySpark," "Snowflake," "config-driven" — all appear naturally and will parse cleanly
- "Difference-in-differences," "matched-pairs," "causal inference," "event-study" — strong alignment with experimentation-heavy JDs at Stripe, Google, and Anthropic
- "A/B testing," "propensity modeling," "staggered rollout" — hits the product DS vocabulary cleanly
- "ArXiv," "preprint," "controlled experiment" — research-tier signal that matters for OpenAI/Anthropic/DeepMind

**Keyword gaps by target tier:**

| Target | Missing Keywords | Present But Weak |
|--------|-----------------|-----------------|
| OpenAI/Anthropic/DeepMind | "alignment," "RLHF," "agent," "tool use," "safety" | "LLM" (appears only in Story 16) |
| Google/Apple | "large-scale," "production ML," "feature engineering," "model evaluation" | "productionized" (in FAST stories) |
| Stripe/Shopify | "growth," "conversion funnel," "self-serve," "GTM" | "$5M," "pricing" (SwagUp) |
| Applied Scientist | "hypothesis testing," "Bayesian," "statistical modeling" | "binomial test," "Kruskal-Wallis" (buried in Story 14/16) |

**Critical gap for the dream tier:** The word "alignment" appears nowhere in the approved bullets for Story 16. For Anthropic and OpenAI, this is a significant miss. The research is alignment-adjacent — the agent rules acknowledge it — but the approved bullets don't use the word. A recruiter scanning for "alignment research" will not find it. The agent rule says "this is alignment research, not NLP with a sticker" but then doesn't put "alignment" in the bullets. Fix this.

**Secondary gap:** "Agentic AI" and "tool-use" appear in Story 16's narrative but not prominently in the approved bullets. These are hot keywords in 2026 JDs. The [A] and [E] Tier 1 bullets gesture at it but bury it.

---

## Skills Surfacing

### Technical Skills Visibility Audit

**Properly surfaced:**
- MILP / constrained optimization — visible in Tier 1-A bullet immediately
- XGBoost — appears in multiple bullets, named explicitly
- Python — implied throughout but never explicitly stated in the approved bullets. **This is an ATS problem.** "Python" is one of the most-filtered keywords in DS JDs and it does not appear in any approved Story 1-3 bullet. The FAST stories mention PySpark (which implies Python) but that's not the same token.
- Causal inference — well-surfaced in Stories 4 and 5
- Snowflake — mentioned in Story 3 bullets
- Streamlit — appears in Story 14/16 infrastructure bullets but not in main experience bullets

**Buried or missing:**
- **SQL** — does not appear in any approved bullet. This is a serious ATS gap. SQL is in virtually every DS JD. Danny clearly uses it (Snowflake pipelines, data consolidation) but the word "SQL" never appears in the approved bullets for his Chase or SwagUp experience.
- **Python** — as noted, not explicitly named in JPMC bullets. Should appear at least once.
- **Statistics** — the statistical vocabulary (p-values, confidence intervals, Kruskal-Wallis, binomial test) is locked in the project stories, not in the work experience bullets. For roles requiring statistical rigor, this creates a gap in the experience section.
- **Fivetran, DBT, Looker** — confirmed by Danny, appear only in the SwagUp Story 12 bullets, which are lower priority. For analytics engineering roles these are valuable keywords.
- **PuLP/CBC** — correctly flagged in agent rules (don't say Gurobi), but the replacement "MILP solver" or "PuLP" is vague. "PuLP" should appear at least once in the technical skills section or a parenthetical.

**Recommendation:** Add a Skills section (one line) that explicitly lists: Python, SQL, PuLP, XGBoost, PySpark, Snowflake, Streamlit, Tableau, Looker, Fivetran. These keywords need to exist as standalone tokens for ATS parsing, not just embedded in bullet prose.

---

## ATS Readability

### Patterns That Will Hurt Parsing

**1. Over-long bullets in the approved set**

Several Tier 1 bullets are 50+ words. ATS systems parse bullet text and score keyword density. A 55-word bullet with 3 keywords scores worse than two 25-word bullets with 3 keywords each. The worst offenders:

Story 16, Tier 1-A:
> "Built an autonomous scenario planner on top of a production-grade optimization engine, then measured why natural-language control interfaces silently fail: across 6,620 controlled runs, vague instructions compress into fewer distinct actions than words used, system state dominates user word choice 10:1, and two near-synonyms produce categorically different behavior (act vs. abstain) in identical system states — a specification failure invisible to the operator (ArXiv: 2605.21827)"

This is 80 words. It reads beautifully. An ATS will score it on keyword density and find: "optimization," "natural-language," "controlled," "ArXiv" — four hits in 80 words. A tighter 35-word version would score higher. **For dream-tier roles, this specific bullet is going in the Projects section, not experience — so it's slightly less critical. But it still needs tightening.**

Story 1, Tier 1-A:
> "Built a MILP-based staffing optimization engine across 3,700+ branches, formulating a multi-component objective (product value, outreach opportunity, transition costs) under demand, capacity, utilization, and policy constraints across 3 role types, 4 product categories, and 16 customer cohorts"

This is 44 words and technically dense. The parenthetical "(product value, outreach opportunity, transition costs)" is good for human readers but ATS parsers may struggle with comma-separated noun phrases in parentheses. Consider whether this level of formulation detail belongs in the resume bullet or in an interview answer.

**2. Acronyms without expansion on first use**

- "MILP" — not universally parsed. Should appear as "Mixed-Integer Linear Programming (MILP)" at least once, then MILP thereafter.
- "ABME," "ARB," "BSOT," "BAR," "ATLAS" — all internal Chase acronyms. ATS systems won't know what these are. The agent rules handle ATLAS/BAR naming well, but ABME and ARB appear in bullets without context.
- "FTE" — common enough that most ATS systems recognize it, but "full-time employees (FTEs)" on first use is safer.
- "DiD" — should be "difference-in-differences (DiD)" on first use.

**3. Em-dashes and special characters**

The approved bullets use em-dashes (—) extensively. Some ATS parsers strip these and concatenate adjacent words, creating nonsense tokens. Use a colon or semicolon instead where possible. The bullet "a specification failure invisible to the operator — (ArXiv: 2605.21827)" would parse as "operatorArXiv" after stripping.

**4. Parenthetical stacking**

Several bullets have nested or sequential parentheticals:
> "Designed A/B/C experiment and event-study DiD framework for a national role launch across ~1,200 branches and 10k employees with staggered adoption; identified +8-15% outreach lift and +5-12% account opening volume increase, securing CEO approval for nationwide expansion (role now deployed in every branch)"

The "(role now deployed in every branch)" parenthetical is strong human context but gets lost in ATS parsing. Move it to the main clause or drop it for ATS-targeted versions.

**5. Tilde (~) in numbers**

"~1,200 branches," "~10k employees," "~2,000 evaluations" — tildes are good for intellectual honesty but some parsers strip them. Not a major issue, but be aware.

---

## Tailoring Assessment

### Generic vs. Targeted

The story library is well-structured for tailoring — the A/B/C/D/E variant system is the right approach. But there are execution gaps.

**Well-tailored sections:**
- Story 1 (ATLAS system) has genuinely distinct variants for OR vs. Product DS vs. MLE. The [A] and [E] variants are substantively different, not just reworded.
- Story 4 (ABME DiD) has strong tailoring — the [B] experimentation variant and [C] product DS variant read differently and hit different JD signals.
- Story 14 (AI detection) has the best tailoring in the library — the [A] applied scientist framing, [B] experimentation framing, and [E] MLE framing are genuinely different angles on the same work.

**Under-tailored sections:**
- Story 2 (Impact) — the variants are nearly identical across role types. The $9B number doesn't change; the framing barely changes. For a product DS role the framing should lead with "replaced manual workflows and drove organizational adoption" not just the dollar figure. For an OR role it should lead with "validated net-neutral reallocation at scale." Currently all five variants lead with "$9B projected."
- Story 5 (ARB) — the variants are essentially the same bullet with minor word swaps. The [E] variant adds "propensity models" but the rest are nearly identical. This story is weak enough that it probably shouldn't appear on a one-page resume at all.
- Story 9 (SwagUp A/B) — the variants are strong but all lead with the same dollar figure. The [B] statistical emphasis variant is the most differentiated and should be the default for experimentation roles.

**The dream-tier gap is real and needs addressing:**

For OpenAI/Anthropic/DeepMind, the current approved bullets do not communicate "AI researcher." They communicate "strong applied DS who touched AI." The difference:

| Current framing | Dream-tier framing needed |
|----------------|--------------------------|
| "Built end-to-end experiment infrastructure (Streamlit, Supabase, Anthropic API)" | "Designed behavioral measurement framework for LLM alignment failure modes in tool-use settings" |
| "Found judges identify warned writers as human at p=0.000243" | "Identified a systematic specification failure in natural-language-to-action interfaces" |

The agent rules for Story 16 actually nail this framing — "this is alignment research, not NLP with a sticker" — but the approved bullets don't fully execute it. The [A] Tier 1 bullet is the closest but still leads with "Built an autonomous scenario planner" rather than the research finding.

---

## Missing Keywords / Themes

### Standard JD Themes That Are Underrepresented or Absent

**1. Production systems / MLOps**
Danny built production infrastructure (Snowflake pipelines, Streamlit, automated scoring, result caching) but the approved bullets rarely use production ML vocabulary: "deployed," "productionized," "monitoring," "inference pipeline," "model serving." The Story 3 [E] bullets get close but are marked as supplementary. For Google/Apple/Stripe MLE-adjacent roles, production credibility needs to be more visible.

**2. Cross-functional leadership**
"7+ cross-functional teams" appears in bullets but the actual leadership signal is weak. JDs at FAANG use phrases like "drove alignment across engineering, product, and finance," "partnered with stakeholders to define success metrics," "influenced without authority." Danny's story is actually strong here (CFO presentation, CEO steerco, field director alignment) but the bullets frame it as coordination, not leadership. The Story 1-C and 2-C bullets are better but still passive.

**3. Ambiguous problem scoping**
Top-tier DS JDs frequently ask for "experience defining problems from ambiguous requirements" or "translating business questions into analytical frameworks." Danny's ATLAS origin story (starting from an Excel solver, building the analytical foundations before touching the solver) is exactly this. But no approved bullet captures it. The closest is the Story 1 narrative but it doesn't appear in any bullet.

**4. Mentorship / technical leadership**
For Senior DS roles, JDs expect some signal of "technical leadership" or "mentoring." Danny has none of this in the approved bullets. Even if he hasn't formally mentored, the bus-factor-of-1 situation and the coordination across 7+ teams is a form of technical leadership. This theme is absent.

**5. Experimentation at scale / online experimentation**
Google, Stripe, and Shopify JDs frequently mention "online experimentation," "experiment infrastructure," or "experimentation platform." Danny's ABME work is offline experimentation (staggered rollout), not an online A/B platform. The SwagUp A/B test is online but small-scale. This gap is real and can't be papered over — but the Story 14 experiment infrastructure (two Streamlit apps, Supabase backend, 251 judges) is the closest thing to "built experiment infrastructure" and should be framed that way.

**6. "Impact" language specificity**
The $9B number is projected and Danny knows it. But every other bullet that doesn't have a dollar figure uses vague impact language: "informed decisions," "enabling coordinated scenario planning," "replaced manual workflows." Recruiters at top-tier companies want to see: "reduced X by Y%," "increased Z by W," "saved N hours per week." The pilot metrics were flagged as indefensible (correctly), which leaves a gap. The approved bullets need at least 2-3 concrete operational metrics that aren't the $9B projection. The "90% of recommendations within ±1 shift" and "30%+ branches unchanged" details from Story 2 are defensible and concrete — they should appear in at least one ATLAS bullet.

---

## Recruiter Quick-Scan

### What a Recruiter Sees in 3 Seconds

This depends entirely on assembly. Based on the approved bullets, here's the honest read:

**If assembled correctly (Story 1-B or 1-C as headline, Story 2-B for impact, Story 4-B for experimentation, Story 14-B or 16-B for AI research):**

> A senior DS at JPMorgan Chase who built a $9B-projected optimization platform solo across 3,700+ branches, designed causal experiments for 10k+ employee national rollouts, and published two solo ArXiv preprints on AI behavior. That's a rare combination.

**The value proposition IS clear — but only if the assembly is right.** The story library is rich enough that bad assembly would produce a generic "experienced DS at a bank" read. Good assembly produces a "must interview" signal.

**The 3-second scan problem:**

The current approved bullets are too long for a 3-second scan. A recruiter's eye goes to: (1) company name, (2) title, (3) first 8 words of the first bullet. If the first bullet of the JPMC section is 44 words of technical formulation, the recruiter reads "Built a MILP-based staffing optimization engine" and moves on. That's fine for OR roles. For product DS roles at Google or Stripe, "MILP-based staffing optimization" reads as "operations research specialist" — which may filter Danny out before they see the experimentation work.

**Recommendation:** The first bullet under JPMC should always be the impact bullet ($9B projected, CEO sign-off, 3,700+ branches) regardless of role type, with the technical system bullet second. Recruiters read top-to-bottom. Impact first, method second.

---

## Assembly Recommendations

*Concrete picks for each target role type. One page. ArXiv paper non-negotiable in Projects.*

### Section Order (Universal)

```
[Name / Contact]
[Education — MS Georgia Tech, Expected Dec 2026]
[Experience]
  JPMorgan Chase — Data Scientist (May 2024–Present)
  JPMorgan Chase — Data Scientist, FAST (Aug 2022–Apr 2024)
  SwagUp — Data Analyst (approx 2021–2022)
  [Consulting — only if needed for space/variety]
[Projects]
  AI/Human Detection Experiment (ArXiv: