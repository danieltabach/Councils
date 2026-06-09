# Assembly Strategist — stage1

# Assembly Strategist Review: Danny Tabach Resume Content System

---

## Preliminary System Assessment

Before diving into role-by-role recommendations, a few structural observations that affect every assembly decision:

**The anchor is clear.** ATLAS/BAR (Stories 1-3) is the strongest technical story in the library and should headline every resume variant. No debate here.

**The AI research pivot is real but thin.** Stories 14 and 16 are genuine research — two solo ArXiv preprints is not nothing, and the origin story for Story 16 (builder who questioned his own system) is legitimately differentiated. But the library has no story showing Danny *working on* AI systems at scale. He studied AI behavior; he hasn't trained models or shipped AI products in production. This gap matters for Dream Tier (OpenAI, Anthropic) and should be managed honestly.

**The experimentation portfolio is strong but redundant.** Stories 4 and 5 both show experimentation at JPMC. Story 9 shows experimentation at SwagUp. Three experimentation stories competing for two slots on a one-page resume means one gets cut in every variant. The redundancy report below handles this.

**Story 5 (ARB) is the weakest story in the library.** Danny's own input reveals the propensity modeling claim was "fluff," the results were "negligible," and the role was essentially a cost-cutting rebranding exercise. It should be retired from active rotation.

**Story 8 (Household Acquisition) and Story 15 (Consulting NLP) are bench-only.** Neither makes the cut for any target role type.

---

## Story Portfolio Recommendations

### Role Type A — Operations Research / Applied Scientist
*Target companies: OpenAI (research), Anthropic, DeepMind, Google (optimization/ML roles)*

**Include:** Stories 1, 2, 3, 4, 14, 16
**Order on resume:**
1. ATLAS system (Story 1, Tier 1-A)
2. ATLAS impact (Story 2, $9B framing)
3. ATLAS technical architecture (Story 3, one supporting bullet only)
4. ABME experimentation (Story 4, Tier 1-A)
5. ArXiv preprints in Projects section (Stories 14 + 16)

**Drop:** Stories 5, 6, 7, 8, 9, 10, 11, 12, 13, 15. SwagUp disappears entirely for this role type — the OR/Applied Scientist audience cares about formulation depth, not startup A/B tests.

**Rationale:** This audience needs to see mathematical rigor (MILP formulation, constraint families, objective components), causal methodology (event-study DiD), and genuine research output (two ArXiv preprints). The $9B number signals real-world scale. The research papers signal intellectual curiosity beyond the day job.

---

### Role Type B — Decision Scientist
*Target companies: Google, Stripe, Intuit, PayPal*

**Include:** Stories 1, 2, 4, 9, 14 or 16
**Order on resume:**
1. ATLAS system (Story 1, Tier 1-B)
2. ATLAS impact (Story 2, $9B framing)
3. ABME experimentation (Story 4, Tier 1-B)
4. SwagUp A/B test (Story 9, primary bullet)
5. ArXiv paper in Projects (Story 14 preferred)

**Drop:** Stories 3, 5, 6, 7, 8, 10, 11, 12, 13, 15. Story 3 (technical architecture) is too MLE-flavored for this audience. Story 5 (ARB) is redundant with Story 4.

**Rationale:** Decision science roles want to see experiment design maturity, causal inference, and business impact. The ABME story (staggered DiD, north star + guardrail metrics framework, CEO sign-off, role now nationwide) is the strongest experimentation credential in the library. SwagUp's A/B test shows Danny can do this at a startup too — range matters. The ArXiv paper shows he thinks about measurement problems independently.

---

### Role Type C — Product Data Scientist
*Target companies: Shopify, Stripe (product), Apple, Google (product analytics)*

**Include:** Stories 1, 2, 4, 9, 10 or 11
**Order on resume:**
1. ATLAS system (Story 1, Tier 1-C)
2. ATLAS impact (Story 2, $9B framing, C-variant)
3. ABME experimentation (Story 4, Tier 1-C)
4. SwagUp A/B test (Story 9, C-variant)
5. SwagUp product catalog (Story 10) OR churn model (Story 11) — pick based on JD
6. ArXiv paper in Projects (Story 14)

**Drop:** Stories 3, 5, 6, 7, 8, 12, 13, 15, 16. Story 12 (dashboards) is weaker than Story 10 for product roles. Story 16 (LLM research) is too research-oriented for most product DS JDs.

**Rationale:** Product DS roles want to see product sense (Story 10 — identified a gap, proposed a solution, shipped it), experimentation (Stories 4 and 9), and cross-functional delivery (Story 1-C with the 7+ teams framing). The ATLAS story needs the stakeholder framing (C-variant) more than the formulation depth framing here.

---

### Role Type D — Senior Data Analyst
*Target companies: Tier 2-3 companies, fintech, growth analytics*

**Include:** Stories 1, 2, 4, 9, 12, 7
**Order on resume:**
1. ATLAS system (Story 1, Tier 1-D)
2. ATLAS impact (Story 2, D-variant)
3. ABME experimentation (Story 4, Tier 1-D)
4. SwagUp A/B test (Story 9, D-variant)
5. SwagUp dashboards (Story 12, D-variant)
6. FAST XGBoost model (Story 7, D-variant)

**Drop:** Stories 3, 5, 6, 8, 10, 11, 13, 14, 15, 16. Story 6 (propensity-to-pay) is weaker than Story 7 for analyst roles. Stories 14/16 are too research-heavy.

**Rationale:** Analyst roles want breadth — SQL, dashboards, experimentation, ML familiarity. Story 12 shows infrastructure chops. Story 7 shows production ML at scale (5M customers, PySpark). This is the most "full-page" variant.

---

### Role Type E — MLE / Analytics Engineering
*Target companies: Google (MLE), Apple (MLE), Stripe (data engineering)*

**Include:** Stories 1, 3, 7, 4, 13 or 14
**Order on resume:**
1. ATLAS system (Story 1, Tier 1-E)
2. ATLAS architecture (Story 3, E-variant, solve-time optimization bullet)
3. FAST XGBoost / PySpark (Story 7, E-variant)
4. ABME experimentation (Story 4, Tier 1-E)
5. Drift detection (Story 13) OR AI detection (Story 14) in Projects

**Drop:** Stories 2, 5, 6, 8, 9, 10, 11, 12, 15, 16. Story 2 (impact) gets absorbed into Story 1's framing for MLE roles. Story 9 (SwagUp A/B) is less relevant than the ML stories.

**Rationale:** MLE roles need to see production system design (config-driven architecture, solve-time optimization), scale (5M customers, PySpark), and ML monitoring awareness (drift detection). Story 3's E-variants are the most technically specific bullets in the entire library — use them here.

---

## Specific Bullet Selections

### Story 1 (ATLAS System) — Tier 1 Selections

**Role A (OR/Applied Scientist):** Use Tier 1-A exactly as written. It leads with MILP, lists the objective components, and names the constraint families. This is the right level of specificity for an OR audience. Do NOT add the 24K FTE number — technical audiences don't need scale padding.

**Role B (Decision Science):** Use Tier 1-B. The "replaced manual staffing workflows" framing is strong, and the matched-pairs reference signals causal sophistication. Keep the "~24K FTEs" — enterprise scale matters to this audience.

**Role C (Product DS):** Use Tier 1-C. The 7+ teams and C-suite framing is correct for this audience. However, the current Tier 1-C bullet is the weakest of the five — it buries the technical work and leads with coordination. Recommend a hybrid: open with what it IS ("built an automated decision platform replacing manual staffing workflows across 3,700+ branches"), then close with the cross-functional proof ("coordinating 7+ teams and presenting to C-suite to secure enterprise rollout"). See Variant Gap section.

**Role D (Analyst):** Use Tier 1-D. Clean, accessible, shows data consolidation and impact without requiring OR knowledge.

**Role E (MLE):** Use Tier 1-E. Config-driven architecture with the dynamic registry is the right technical hook for this audience. "Production decision system (ATLAS)" framing is correct.

### Story 1 — Tier 2 Selections

**Role A:** Use Tier 2-A (formulation depth). This is the only role type that should get a Tier 2 ATLAS bullet — formulation specifics are interview depth for OR roles, not filler.

**Role B:** Use Tier 2-B (causal + optimization blend). The "unified causal value estimation... demand modeling... and constrained optimization" framing signals methodological range.

**Role C:** Skip Tier 2 for this role type. The C-suite endorsement detail (CFO quote, CEO sign-off) should appear in Story 2's C-variant instead.

**Role D:** Skip Tier 2. One ATLAS bullet is sufficient for analyst roles.

**Role E:** Use Tier 2-E (system design) — specifically the config-driven architecture bullet. This pairs naturally with Tier 1-E and gives the architecture depth that MLE interviewers probe.

### Story 1 — Tier 3 Selections

**Role A only:** Use Tier 3-A (disruption cost calibration) IF the JD mentions "mathematical modeling," "solver tuning," or "parameter estimation." Otherwise skip. No other role type should see a Tier 3 ATLAS bullet — one-page constraint is non-negotiable.

**All other roles:** Skip Tier 3 entirely.

### Story 2 (ATLAS Impact) — Bullet Selections

**All roles:** Use the $9B headline variant matched to role type. Always include the "~90% within ±1 person shifts" qualifier — it makes the $9B credible and shows the recommendations are actionable, not theoretical.

**Critical:** NEVER use the $150M framing going forward. The $9B/$750M-per-month framing is cleaner and more defensible. The $150M has three different definitions across resumes and will invite confusion in interviews.

**Role A:** Use Tier 1-A variant of Story 2: "$9B in annual balance growth... ~90% within ±1 person shifts — secured CEO sign-off."

**Role B:** Use Tier 1-B variant: "$9B ($750M/month)... CFO endorsed... CEO approved phased rollout." The dual endorsement signals Danny can influence at the executive level.

**Role C:** Use Tier 1-C variant. Add the CFO quote if space allows: "CFO: 'Even if we're wrong by 50%, this delivers $4.5B.'" That quote is gold for product roles that value business impact.

**Role D:** Use Tier 1-D variant. Keep it simple — "$9B projected, presented to CFO, contributed to CEO sign-off."

**Role E:** Use Tier 1-E variant with the cost savings framing. MLE audiences care about operational impact more than balance sheet projections.

### Story 3 (Technical Architecture) — Bullet Selections

**Role A only:** Use Tier 3-A (BSOT integration): "Integrated an existing XGBoost revenue-lift model into the MILP formulation as binary scenario selection variables (±2, ±1, unchanged per branch)..." This is technically elegant and interview-ready.

**Role E only:** Use Tier 2-E (solve-time optimization): "Cut full-network solve time from 8-12 hours to 1.5 hours through warm starts, tighter constraint engineering, and region-level parallelization." This is the most impressive single technical fact in the entire Story 3 library — it shows Danny thinks about production performance, not just correctness.

**All other roles:** Story 3 does not appear as a standalone bullet. Its content gets absorbed into the Tier 2 selections from Story 1.

### Story 4 (ABME DiD) — Bullet Selections

**Role A:** Use Tier 1-A. Lead with the quantified results (+8-15% outreach, +5-12% accounts), mention the event-study methodology, and close with the nationwide outcome.

**Role B:** Use Tier 1-B exactly as written. This is the strongest bullet in the entire experimentation library. The specific numbers (8-15%, 5-12%, 6-8%), the methodology (event-study DiD, staggered adoption, parallel trends), and the outcome (role now in every branch, AB role eliminated) are all defensible and impressive.

**Role C:** Use Tier 1-C. The north star + guardrail metrics framework detail is the differentiator for product roles — it shows Danny thinks about experiment design holistically, not just top-line lift.

**Role D:** Use Tier 1-D. Keep it accessible — staggered DiD, statistically significant results, CEO approval, nationwide expansion.

**Role E:** Use Tier 1-E. The "pipeline" framing (time-normalization, fixed effects, parallel trend validation) signals engineering rigor.

**For all roles:** Include the Tier 2 "business outcome" bullet — "Results drove permanent organizational change: the original Associate Banker role was eliminated nationwide" — if SwagUp is being dropped to make room. This punchline is too good to leave on the floor.

**Tier 2 methodology depth (danieltabach.github.io):** Include for Role B only, as a parenthetical in the primary bullet or as a second bullet if space allows. The blog post is a live work sample — it's a differentiator.

### Story 9 (SwagUp A/B Test) — Bullet Selections

**Roles B, C, D:** Use the B/C primary variant: "Drove $5M+ incremental profit and 40% revenue growth for SMB clients by designing an A/B test on premium sample kits, analyzing retention and refund rates to overturn legacy pricing assumptions and reshape company strategy."

**Do NOT use "spearheaded"** — it's on the banned verb list and appears in multiple historic variants. Several approved bullets are clean; use those.

**Do NOT use the "statistically significant" framing** — Danny confirmed the test was run without proper power analysis and used only basic t-tests. Claiming statistical significance here invites trouble. The business impact numbers ($5M, 40%) are strong enough without the statistics claim.

### Story 14 (AI/Human Detection) — Bullet Selections

**All roles (Projects section):** Use Tier 1-B for most roles: "Designed and ran a two-phase controlled experiment (21 writers, 251 judges, ~2,000 paired evaluations)... p=0.000243... four classifiers trained on 10 NLP features could not replicate (ArXiv: 2604.23471)."

**Role A (Applied Scientist):** Use Tier 1-A instead. The non-behavioral priming citation and the "polarized behavior without changing measurable text features" finding signals research sophistication.

**Role E (MLE):** Use Tier 1-E. The infrastructure depth (Streamlit, Supabase, Anthropic API, 29 automated tests) is the hook for this audience.

**Always include the ArXiv number.** It's published. It's real. It's a differentiator.

### Story 16 (LLM Vague Intensity Words) — Bullet Selections

**Role A (Applied Scientist/Alignment):** Use Tier 1-A. The origin story (built the production system, then questioned whether it could be trusted) is the correct framing for alignment-adjacent roles. The $250K downstream propagation makes it concrete.

**Role B (Decision Scientist):** Use Tier 1-B. The controlled experiment framing (6,620 runs, 10 words