# Bullet Surgeon — stage1

# Bullet Surgeon Report: Danny Tabach

---

## Prefatory Note on Scope

This library contains 16 stories, 100+ bullet variants, and 5+ tiers of approved selections. My mandate is bullet-level craft — verb choice, structure, conciseness, impact clarity. I will not assemble the resume or make story selection calls (that's strategic positioning work outside my lane), but I will flag where bullet quality varies by tier and variant so Danny can make informed picks. Where the brief explicitly asks me to evaluate defensibility or AI positioning *at the bullet level*, I'll address it.

---

## Bullet-by-Bullet Assessment

I'll work through the Approved Agent-Selectable Bullets, which are the decision-relevant set. Historic variants are mostly superseded — I'll call out the few worth salvaging.

---

### STORY 1: ATLAS / BAR — The System

#### Tier 1 Bullets

**[A — OR / Applied Scientist]**
> Built a MILP-based staffing optimization engine across 3,700+ branches, formulating a multi-component objective (product value, outreach opportunity, transition costs) under demand, capacity, utilization, and policy constraints across 3 role types, 4 product categories, and 16 customer cohorts

**What works:** Verb is strong ("built"). The parenthetical is doing real work — it communicates technical sophistication in compressed form. The constraint enumeration at the end (3 role types, 4 product categories, 16 customer cohorts) is specific and defensible.

**What doesn't:** No result. This bullet describes the system but never tells the reader what it *did*. For OR/Applied Scientist roles, the formulation IS the point — but even a one-clause result ("enabling budget-neutral reallocation across ~24K FTEs") would close the loop. The phrase "multi-component objective" is slightly academic — "six-component objective" is both more precise and more impressive.

**Verdict:** Strong structure, missing result clause. Fix: add ", enabling [result]" at the end.

---

**[B — Decision Scientist]**
> Built an automated decision platform that replaced manual staffing workflows across 3,700+ branches, integrating causal value estimation (matched-pairs balance growth analysis) with constrained optimization to drive budget-neutral allocation decisions for ~24K FTEs

**What works:** Strong verb. "Replaced manual staffing workflows" is concrete and shows what existed before. The parenthetical "(matched-pairs balance growth analysis)" is specific and defensible. "Budget-neutral" is a meaningful qualifier — it tells the reader the system created value without additional spend.

**What doesn't:** "Integrating causal value estimation...with constrained optimization" is slightly dense. The reader has to parse two technical concepts connected by "with" before landing on the result. The result ("budget-neutral allocation decisions for ~24K FTEs") is solid but doesn't include a dollar figure — for a Decision Scientist role, the $9B or $5-15M/month number belongs here.

**Verdict:** Best Tier 1 bullet overall. Tighten the middle clause, add a dollar figure. This is the one to use for most applications.

---

**[C — Product DS]**
> Built and deployed an automated decision platform across 3,700+ locations, coordinating with 7+ cross-functional teams (Workforce Planning, Finance, regional leadership) and presenting to C-suite executives to secure enterprise-wide rollout

**What works:** "Built and deployed" shows full lifecycle. The team enumeration is specific. "Presenting to C-suite to secure enterprise-wide rollout" is outcome-oriented.

**What doesn't:** This bullet buries the technical work entirely. A Product DS role still needs to see that Danny built something technically sophisticated — this reads like a PM bullet. "Coordinating with 7+ cross-functional teams...and presenting to C-suite" is the *how*, not the *what*. The system itself (MILP, optimization, causal modeling) disappears. Also: "enterprise-wide rollout" is slightly inflated given that Danny confirmed it's still in phased pilot — this is a defensibility flag.

**Verdict:** Weakest Tier 1 bullet. The cross-functional and C-suite details belong in a Tier 2 supporting bullet, not the headline. Recommend replacing with a version that leads with the technical system and ends with the stakeholder outcome.

---

**[D — Senior Data Analyst]**
> Built an automated staffing system serving 3,700+ branches by consolidating CRM task-hour data, outreach volumes, and account-level value metrics into a single optimization engine that replaced subjective field-based allocation decisions

**What works:** "Replaced subjective field-based allocation decisions" is a strong before/after contrast. The data sources listed (CRM task-hour data, outreach volumes, account-level value metrics) are specific and show data fluency.

**What doesn't:** "Consolidating...into a single optimization engine" undersells the work significantly. The system isn't a consolidation project — it's a MILP solver with causal value estimation. For a Senior DA role, this framing is appropriate in scope but loses the differentiation. No result.

**Verdict:** Appropriate for the tier. Would benefit from a result clause.

---

**[E — MLE / Analytics Engineering]**
> Built a production decision system (ATLAS) across 3,700+ branches using a modular, config-driven architecture where role definitions, constraints, and objective terms derive dynamically from a central registry; integrated an XGBoost revenue-lift model as binary scenario variables within the MILP solver

**What works:** "Config-driven architecture where role definitions, constraints, and objective terms derive dynamically from a central registry" — this is excellent. It's specific, defensible (code-confirmed), and signals systems-thinking rather than just modeling. The XGBoost integration detail is precise.

**What doesn't:** No result. For an MLE role, the production deployment details (solve time, scale, infra) matter — "production decision system" is asserted but not proven. The solve-time reduction (8-12 hours → 1.5 hours) from Story 3 belongs here or in a supporting bullet. Also: "binary scenario variables within the MILP solver" is correct but will confuse non-OR readers — fine for a targeted MLE application.

**Verdict:** Strong for MLE. Add a result. Consider pairing with the solve-time bullet from Story 3[E].

---

#### Tier 2 Bullets

**[A — Formulation depth]**
> Designed MILP formulation maximizing net value across product openings, outreach opportunity, and revenue-lift scenarios, subject to demand fulfillment, capacity, utilization floors, staffing policy, and pool-level budget constraints; integrated an XGBoost model as binary scenario selection (±2 headcount) per branch

**What works:** Technically precise. The constraint list is comprehensive and defensible. "±2 headcount" is a specific detail that makes the formulation concrete.

**What doesn't:** "Designed MILP formulation" is correct but passive-adjacent — the reader has to do work to understand what this produced. The verb "designed" is fine but "formulated" or "built" would be stronger. No result. This bullet is interview prep on paper — it's what Danny says when asked "walk me through the formulation," not what goes on the resume.

**Verdict:** Too dense for a resume bullet. Best used as a talking point. If it must appear, cut the constraint list to the 3 most distinctive items and add a result.

---

**[B — Causal + optimization blend]**
> Unified causal value estimation (matched-pairs analysis across banker roles and customer segments), demand modeling, and constrained optimization into a single config-driven system coordinating 7+ teams

**What works:** "Unified...into a single config-driven system" is strong — it implies that these three things existed separately before Danny combined them. The parenthetical is specific.

**What doesn't:** "Coordinating 7+ teams" is tacked on and doesn't flow grammatically from "unified...into a single system." These are two different claims that should be two different bullets or joined with a result. No result.

**Verdict:** Good bones, weak ending. Cut "coordinating 7+ teams" (it belongs in [C]) and replace with a result.

---

**[C — Cross-functional / stakeholder]**
> Coordinated across Workforce Planning, Finance, Divisional Directors, and Market Expansion teams to align solver recommendations with field-level staffing policies; CFO endorsed projections and CEO approved phased rollout

**What works:** Specific team names. "CFO endorsed projections and CEO approved phased rollout" is a strong credibility signal.

**What doesn't:** Leads with "Coordinated" — a weak verb that positions Danny as a facilitator rather than a builder. The technical work is invisible. This bullet, if it appears at all, should be a supporting bullet after a technical headline, not a standalone claim.

**Verdict:** Never use as a standalone bullet. Acceptable as a second or third bullet in a section where the technical work is already established.

---

**[D — Data infrastructure]**
> Consolidated CRM task-hour data, outreach funnel metrics, servicing costs, and account-level value data across Snowflake pipelines into a single branch-level dataset feeding the optimization engine

**What works:** Specific data sources. "Feeding the optimization engine" connects the infrastructure to the system.

**What doesn't:** "Consolidated...into a single branch-level dataset" is the least impressive framing of what Danny built. This is a data engineering bullet, not a data science bullet. No result.

**Verdict:** Bench bullet only. Use for analytics engineering roles that specifically ask about data pipeline experience.

---

**[E — System design]**
> Architected config-driven system where adding a new banker role requires only a registry entry — solver variables, constraints, objective terms, preprocessing, and output columns all adapt automatically; built iterative demand buffer algorithm to handle incomplete CRM data

**What works:** The "adding a new banker role requires only a registry entry" is an excellent concrete illustration of what "config-driven" actually means. This is the best explanation of the architecture in the entire library. The demand buffer algorithm is specific and defensible.

**What doesn't:** Two separate claims in one bullet — the config-driven architecture AND the demand buffer algorithm. These should be separate bullets or one should be cut. "Architected" is a slightly inflated verb given that Danny built this solo as a DS, not as a software architect — though it's defensible. No result for either claim.

**Verdict:** Split into two bullets or cut one. The config-driven illustration is the best in the library — keep that half.

---

#### Tier 3 Bullets

**[A/B — Outreach ceiling methodology]**
> Designed double-regression methodology to estimate per-branch outreach maximums: regressed branch features against call volumes to identify high-performing branches, then derived contact-rate functions across 16 customer cohorts from those upper-residual branches to set network-wide outreach ceilings

**What works:** Technically precise and genuinely interesting. "Upper-residual branches" is specific. The two-stage logic is clear.

**What doesn't:** This is a methodology description, not a result. It reads like a methods section of a paper. For a resume, the reader needs to know what this produced — "enabling the solver to set network-wide outreach targets based on empirically observed best-performing branches" or similar. Also: "set network-wide outreach ceilings" is the output but not the business impact.

**Verdict:** Strong for OR/Applied Scientist interviews. Too dense for a resume bullet without a result clause. Use only when the JD explicitly mentions regression methodology or capacity modeling.

---

**[B — Value estimation methodology]**
> Built role-by-product value dictionary using matched-pairs causal analysis: isolated customers with identical features opened by different banker roles and measured 12-month balance growth to estimate the incremental value of each role-product-customer combination

**What works:** "Isolated customers with identical features opened by different banker roles" is a clean, jargon-light explanation of matched pairs. "12-month balance growth" is specific. This is the clearest methodology bullet in the library.

**What doesn't:** No result. "Estimate the incremental value of each role-product-customer combination" is the output of the analysis, not the business impact. Also: "role-by-product value dictionary" is a slightly awkward construction.

**Verdict:** Best methodology bullet in the library. Add a result: "...producing the value coefficients that drive $9B in projected balance growth optimization."

---

**[A — Disruption cost calibration]**
> Calibrated disruption cost parameters through grid search over representative regions, targeting field acceptance criteria: 30%+ branches unchanged, 90%+ within ±1 net headcount, preserving minimum licensed banker thresholds per branch

**What works:** Extremely specific. The acceptance criteria (30%+ unchanged, 90%+ within ±1) are defensible and show Danny thought about operationalizability, not just mathematical optimality.

**What doesn't:** "Calibrated disruption cost parameters through grid search" will read as jargon to most readers. The business insight — that the solver's recommendations had to be constrained to what the field would actually accept — is buried. Verb "calibrated" is weak.

**Verdict:** Strong interview talking point, weak resume bullet. Use only for OR roles. Reframe to lead with the business insight: "Constrained solver recommendations to field-acceptable shifts (90%+ within ±1 headcount) by tuning disruption cost parameters through grid search across representative regions."

---

**[E — Demand buffer engineering]**
> Built iterative demand buffer algorithm to address systematic CRM undercounting of branch utilization, converging on a multiplier that fully allocates all role pools while maintaining outreach opportunity utilization within a 65-80% target range

**What works:** Specific. "Systematic CRM undercounting" explains the problem. "Converging on a multiplier" shows algorithmic thinking. The 65-80% range is defensible.

**What doesn't:** "Converging on a multiplier that fully allocates all role pools while maintaining outreach opportunity utilization within a 65-80% target range" is a complex clause that requires domain knowledge to parse. No business impact stated.

**Verdict:** Excellent for MLE/engineering roles. Pair with the solve-time bullet from Story 3.

---

**[C/D — Stakeholder translation]**
> Translated solver outputs into scenario planning dashboards and automated reports comparing current vs. optimized allocation, showing revenue-lift calculations per variable to enable decision-making by Workforce Planning and regional leadership

**What works:** "Comparing current vs. optimized allocation" is a clear before/after. "Revenue-lift calculations per variable" is specific and shows explainability thinking.

**What doesn't:** "Translated solver outputs" is a weak verb construction. "Enable decision-making" is vague. No quantification of the dashboards' impact.

**Verdict:** Acceptable supporting bullet for Product DS roles. Strengthen the verb and add adoption metrics if available.

---

### STORY 2: ATLAS — Impact & Scale

#### $9B Headline Bullets

**[A — OR / Applied Scientist]**
> Projected $9B in annual balance growth through net-neutral headcount reallocation across 4,300+ branches; ~90% of recommendations within ±1 person shifts — secured CEO sign-off for phased market rollouts

**What works:** "Projected" qualifier is correct. "Net-neutral headcount" is a meaningful differentiator. The "~90% within ±1 person shifts" detail makes the $9B credible — it shows the recommendations are actionable. "Secured CEO sign-off" is a strong outcome.

**What doesn't:** The semicolon construction creates two separate claims that don't flow naturally. "~90% of recommendations within ±1 person shifts" is a methodology detail that interrupts the impact story. The sentence structure is: [impact] — [methodology detail] — [stakeholder outcome]. Consider restructuring.

**Verdict:** Strong content, awkward structure. Restructure: "Projected $9B in annual balance growth through net-neutral reallocation across 4,300+ branches, with 90%+ of recommendations within ±1 headcount shift; presented to CFO and secured CEO sign-off for phased rollout."

---

**[B — Decision Scientist]**
> Projected $9B in annual balance growth ($750M/month) by modeling optimal staff-to-opportunity allocation with net-neutral headcount; CFO endorsed projections, CEO approved phased rollout

**What works:** The parenthetical "$750M/month" is helpful — it makes the annual figure more tangible. "Modeling optimal staff-to-opportunity allocation" is clean. The stakeholder outcomes are specific.

**What doesn't:** "Staff-to-opportunity allocation" is slightly jargony. The CFO/CEO endorsement is strong but feels appended rather than earned by the bullet's logic.

**Verdict:** Best $9B bullet. Minor polish needed on the middle clause.

---

**[C — Product DS]**
> Projected $9B in annual balance growth through budget-neutral staffing reallocation; presented financial analysis to CFO of Community Banking and contributed to CEO steerco securing enterprise rollout approval

**What works:** "Budget-neutral" is cleaner than "net-neutral." The CFO/CEO specificity is strong.

**What doesn't:** "Contributed to CEO steerco" is hedging language — "contributed to" implies Danny was a minor participant.