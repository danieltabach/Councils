# Story Architect — stage1

# Story Architect Review: Danny Tabach

---

## Personal Brand Assessment

**What brand do these stories collectively communicate?**

At their best, these stories communicate: *a builder who ships production systems at enterprise scale, then turns around and questions whether those systems can be trusted.* That's a genuinely rare combination. Most candidates are one or the other — operators who ship, or researchers who question. Danny is both, and the two ArXiv papers are the proof.

**Is it clear and consistent?**

No, and this is the core problem. The brand fractures across three competing identities:

1. **Enterprise optimization engineer** (ATLAS/BAR, ABME, ARB)
2. **Startup product analyst** (SwagUp A/B test, churn model, dashboards)
3. **Independent AI researcher** (ArXiv 2604.23471, ArXiv 2605.21827)

These three identities are not mutually exclusive — the best version of Danny's brand synthesizes them — but on a resume, they read as three different candidates competing for space. The AI researcher identity, which is the most differentiated and most relevant to dream-tier targets, is currently the weakest in terms of real estate and positioning. The optimization engineer gets 3 stories and ~60% of the bullet space. The AI researcher gets 2 projects buried at the bottom.

**The brand gap:** Dream-tier targets (OpenAI, Anthropic, DeepMind) are not hiring "enterprise DS who also published." They're hiring "researcher who happens to have shipped production systems." The current story ordering tells the wrong version of Danny's story for those targets. For Tier 1-2 targets (Google, Stripe, Intuit), the brand is closer to right but still needs tightening.

---

## The Superpower

**What is Danny's unique differentiator?**

Danny's superpower is this: **he builds the system, then measures whether the system can be trusted.**

This is not a common combination. Most enterprise DS build systems and hand them off. Most researchers study systems they didn't build. Danny built a $9B-projected staffing optimization engine, then — blocked from integrating AI the way he wanted at a bank — rebuilt it himself as an autonomous agent, noticed it couldn't be trusted with vague human instructions, and published a paper measuring exactly why. That origin story is the differentiator. It's not "I do both applied and research." It's "I built the thing that made me ask the research question."

**Is it visible enough?**

No. It is almost completely invisible on the current resume.

The connection between ATLAS/BAR (Stories 1-3) and the LLM paper (Story 16) — that Story 16 was *born from* the production system in Stories 1-3 — is the most compelling narrative thread Danny has. It turns two separate credentials into a single arc. Right now, that thread exists only in Story 16's canonical narrative, which no recruiter will ever read. On the resume itself, ATLAS and the LLM paper appear in separate sections with no visible connection. A recruiter scanning in 6 seconds sees "optimization engineer" and "AI paper" as unrelated line items, not as cause and effect.

**What needs to happen:** The LLM paper bullet must explicitly reference that the synthetic environment was "built from production expertise in constrained staffing optimization." That one phrase connects the two credentials and communicates the superpower without additional space.

---

## Narrative Coherence (Per Story)

### ATLAS/BAR (Stories 1-3)

**Arc coherence: Strong, but over-allocated.**

The narrative arc is genuinely excellent: Danny arrived with a weekend notebook, pitched himself into a role that didn't exist, spent 6 months building the analytical foundations before touching the solver, then spent months "cramming a dying star" into field-acceptable constraints. That's a complete story with a beginning (manual gut-feel staffing), middle (6 months of foundational analytics + solver design + BSOT integration + disruption cost calibration), and end ($9B projected, CEO sign-off, surgical decisions being made today).

The problem is that Stories 1, 2, and 3 are the same story told three times. Story 1 is the system. Story 2 is the impact. Story 3 is the architecture. On a resume, these collapse into 2-3 bullets maximum. The story bank has done excellent work separating them for targeting purposes, but the agent rules already acknowledge this: "Never use more than 3 ATLAS bullets on a single resume."

**Narrative gaps:**
- The "dying star" compression arc — the most compelling part of the build — is not surfaced in any approved bullet. Every bullet describes what the system IS. None of them captures the *journey* of getting it to work. This matters because the journey is what makes the story memorable in an interview, and the resume should hint at it.
- The "bus factor of 1" detail is powerful (sole DS, no handoff possible, owns it all) but is only in agent rules, not in any approved bullet. It should be surfaced.

**Defensibility:**
- The $9B "projected" qualifier is correctly enforced throughout. The agent rules are tight here.
- The Gurobi ban is correctly enforced.
- The patent ban is correctly enforced.
- The old pilot metrics (15%, 3-8%, 4%) are correctly retired.
- **One remaining risk:** The "$5-15M/month cost savings" range is wide enough that an interviewer will probe it. Danny's explanation (role-mix reallocation → senior bankers shift to outreach → ABs absorb more servicing) is defensible but requires a 90-second verbal explanation. The bullet should include the mechanism, not just the number, so Danny can point to it in an interview.

### ABME — Staggered DiD (Story 4)

**Arc coherence: Strong. This is the best experimentation story.**

Beginning: Walk-in account openings were being lost because ABs had no entitlement to open accounts, and senior bankers were too busy. Middle: Danny designed a three-arm staggered national rollout with an event-study DiD framework, validated parallel trends, controlled for branch size, and built a comprehensive metrics framework (north star + secondary + guardrails). End: +8-15% outreach lift, +5-12% account opening volume, CEO approval, AB role eliminated nationwide.

The arc is complete. The "C-arm informed a 'no' decision" detail is excellent — it shows experiment design maturity, not just "we ran a test and it worked." The nationwide permanent organizational change (AB role gone) is the ultimate punchline and it's correctly flagged in agent rules.

**Defensibility:**
- The range approach (+8-15%, +5-12%) is correctly adopted after Danny confirmed the single numbers were wrong.
- The decision NOT to use "-4% demand constraint" and "+4% client meetings" is correct — Danny couldn't confirm these as statistically significant.
- The blog post (danieltabach.github.io) is a genuine public work sample and should always be linked.
- **One risk:** The sample size concern. 21 writers in Story 14 is small; ~1,200 branches in Story 4 is large. But Danny acknowledged the matching constraints limited the sample, and parallel trends held. The event-study framework is the methodological defense. This is fine.

### ARB — Matched-Pairs Pilot (Story 5)

**Arc coherence: Weak. This story has defensibility problems that make it a liability.**

The "10-20 hours/week freed" vs. "~20 hours/month" discrepancy is unresolved. These are 4-5x apart. Danny's input on this story reveals that the ARB pilot was "very long and iterative and slow," the add/swap arms had unclear results, the 5% lift in accounts opened was "negligible" by Danny's own description, and the role was primarily a cost-savings/rebranding exercise. Danny also said the propensity model angle was "more like fluff."

**Recommendation: Drop this story from the active rotation.** It doesn't add to the brand, the numbers are unresolved, and Danny's own characterization ("the lift was negligible," "this really shipped due to cost savings — not innovation") undermines the bullet's credibility. If an interviewer asks about it, Danny would be in a difficult position. The space is better used for Story 14 or Story 16.

The one defensible element — "matched-pairs causal methodology" — is already demonstrated more powerfully in Story 4 (ABME) and in the value estimation methodology within ATLAS (Story 1). There is no unique methodological contribution from ARB that isn't covered elsewhere.

### FAST — Propensity-to-Pay (Story 6)

**Arc coherence: Adequate but thin.**

Beginning: 1M+ customers at risk of overdraft. Middle: behavioral feature engineering (balance sizes, overdraft frequency, deposit consistency, autopay indicators) + logistic regression with ROC curve tuning. End: flexible loan program launched, AUC ~88-90%.

The arc is complete but the story is undersold. The ROC curve tuning detail — Danny adjusted the decision threshold to optimize the tradeoff between catching at-risk customers and false positives — is actually a meaningful methodological choice that most candidates don't mention. The "non-interest $50-100 loan preventing delinquency" outcome is a concrete, human story. Neither of these details appears in the approved bullets.

**Recommendation:** Keep as a bench story. Upgrade the approved bullet to include the AUC (~88-90%) and the ROC threshold tuning detail if space permits.

### FAST — Next-Best-Product XGBoost (Story 7)

**Arc coherence: Adequate, with an undersold finding.**

The most interesting part of this story — Danny was trying to identify *future* business customers before they became business customers, based on behavioral signals — is not in any approved bullet. The 8% lift in business account openings within 6-8 months is a real result. The SHAP feature importance and clustering work adds methodological depth.

**Recommendation:** Keep as a bench story for MLE/ML roles. The approved bullets are functional. The "predicting future business customers before they self-identify" framing is more compelling than "customer segmentation model" and should be the lead.

### FAST — Household Acquisition (Story 8)

**Arc coherence: Incomplete. Danny didn't answer any of the questions.**

This story was correctly dropped after Resume #7. The "40M by 2030" forecast is a forward-looking number with no mechanism explained, no Danny-specific contribution clear, and no defensible result. 

**Recommendation: Remove permanently from the rotation.** It adds nothing that Stories 6 or 7 don't cover better.

### SwagUp — A/B Test & Pricing (Story 9)

**Arc coherence: Strong. This is Danny's best startup story.**

Beginning: Legacy assumption that premium samples were enterprise-only. Middle: Danny identified the gap (SMBs with samples never had refunds, came back with larger orders), designed a 50/50 coin-flip A/B test in Salesforce, shipped cheap SwagUp-branded sample packs. End: $5M+ incremental profit in 6 months, 40% first-order revenue growth, refund rate dropped to ~1%, company-wide policy change.

The arc is complete and the mechanism is clear. The "overturned legacy assumption" narrative hook is strong. The policy change is the punchline.

**Defensibility concerns:**
- Danny acknowledged the test lacked statistical rigor (no power analysis, basic t-test). This is fine — he was 21 in his first data job. The results are strong enough that the methodology critique is survivable. But he should not claim "statistically significant improvements" in the bullet unless he's comfortable defending that in an interview. The Stripe/Perplexity variant does claim this — that variant should be retired.
- The $5M calculation is post-launch trend comparison, not a controlled measurement. "Drove $5M+ incremental profit" is a stronger claim than the methodology supports. "Contributed to $5M+ incremental profit" or "analysis drove a policy change that generated $5M+ incremental profit" is more defensible.
- The 40% first-order revenue growth is clean: treatment vs. control, first orders were larger. This is the most defensible number.

### SwagUp — Product Catalog (Story 10)

**Arc coherence: Weak as currently written. The canonical narrative is better than the bullets.**

The actual story is interesting: Danny noticed cart dropoffs, investigated why, built a "Businesses like you ordered..." recommendation engine (similar to Amazon's "customers also bought"), and shipped a preset catalog that let SMBs see packages before engaging a sales rep. That's a product sense story with a real mechanism.

But the approved bullets say "identified zero pricing visibility as a conversion bottleneck and launched a self-serve product catalog with dynamic bulk pricing." That's not quite what happened — it was more like a recommendation/preset system than a pricing catalog. The "dynamic bulk pricing" framing doesn't match Danny's description of what he actually built.

**Recommendation:** Rewrite the bullet to match the actual story: "Identified cart abandonment as a conversion bottleneck, built a recommendation engine surfacing preset packages by budget and company size ('businesses like you ordered...'), reducing sales rep dependency for ~20% of conversions." This is more accurate and more interesting.

The ~5% add-to-cart lift is based on general trends with no A/B test. Keep the tilde. Don't claim statistical significance.

### SwagUp — Churn Prediction (Story 11)

**Arc coherence: Weak. The story is significantly oversold.**

The canonical narrative says "production churn prediction model" and "monthly scoring pipeline." Danny's input reveals: first version was a rule-based RFM table in Excel. Second version was a rudimentary logistic regression with Clearbit data, running via "a simple Python script to a CSV with labels → pushed to a Salesforce table." The "automated sales outreach" was sales reps looking at a monthly table.

This is not a production ML pipeline. It's a monthly batch scoring script feeding a Salesforce table. That's defensible and useful — but calling it a "production churn prediction model" with a "monthly scoring pipeline" invites questions Danny can't fully answer (what's the AUC? what were the features? how was it validated?).

**Recommendation:** Reframe honestly: "Built a monthly churn scoring model combining RFM analysis with firmographic enrichment (Clearbit) to flag at-risk accounts; automated monthly scoring to a Salesforce table triggering proactive sales outreach." This is accurate, defensible, and still shows real initiative. Drop "production" — it's overselling.

### SwagUp — Analytics Infrastructure (Story 12)

**Arc coherence: Adequate. The tool stack confusion is the main problem.**

Danny confirmed: Fivetran, DBT, Looker, Google Cloud. The stack is now clear. The "weekly manual → daily self-serve" transformation story is the strongest framing. The "I helped hire a data engineer and then built the infrastructure together" detail shows leadership and initiative.

**Recommendation:** Use the GCP/Fivetran/Looker/DBT variant going forward. Retire the Tableau variants — they're from before Danny confirmed the actual stack.

### Georgia Tech — Drift Detection (Story 13)

**Arc coherence: Thin. This is a class project with limited depth.**

Danny didn't answer any of the enrichment questions (concrete results, algorithm selection rationale, team size). The approved bullets are functional but the story has no "so what" beyond "I know these five algorithms exist." Without specific numbers (CUSUM detected drift in X data points vs. Y for PELT), the bullet is a list of algorithm names, not a finding.

**Recommendation:** This story competes with Story 14 (AI detection) for the project slot in MLE resumes. Story 14 is significantly stronger — it has a published paper, specific results, and a compelling finding. Drop Story 13 from the active rotation for all targets except pure MLE/ML monitoring roles where drift detection is explicitly mentioned in the JD. Even then, it should be a secondary bullet at best.

### Georgia Tech — AI/Human Detection (Story 14)

**Arc coherence: Strong. This is Danny's best research story.**

Beginning: Do AI detection warnings change how people write with AI? Middle: Two-phase controlled experiment, 21 writers, 251 judges, ~2,000 paired evaluations, four classifiers on 10 NLP features. End: p=0.000243, judges detect something classifiers cannot, warning polarizes behavior rather than moderating it.

The arc is complete. The counter-intuitive finding (warning didn't reduce AI use — it polarized it) is the hook. The "humans beat classifiers" finding is the punchline for AI/ML audiences. The full-stack solo build (two Streamlit apps, Supabase, Anthropic API, 29 automated tests, self-funded) is the engineering punchline.

**Published on ArXiv (2604.23471).** This is now a real credential.

**Defensibility:** The small writer sample (21) is the obvious attack vector. Danny's defense is correct: the per-document analysis (15/23 treatment docs above 50%, 5/18 control docs), the sensitivity analysis (effect strengthens under stricter filtering), and the large judge sample (251, ~2,000 evaluations) all hold up. The effect is distributed, not driven by outliers. This is defensible.

### Consulting — NLP Pipeline (Story 15)

**Arc coherence: Thin.