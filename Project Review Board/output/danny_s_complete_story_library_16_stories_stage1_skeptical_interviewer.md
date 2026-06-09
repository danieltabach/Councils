# Skeptical Interviewer — stage1

# Skeptical Interviewer's Full Review: Danny's Story Library

---

## OPENING ASSESSMENT

Danny has real, substantive work. The ATLAS/BAR system is genuinely impressive — a sole-authored, production-grade MILP system at scale is rare. The two ArXiv preprints are real differentiators in the 2026 market. The ABME experimentation story is clean and defensible. The SwagUp A/B test has a real business impact number.

But this library has serious landmines. Several bullets will invite questions Danny cannot answer cleanly. The $9B number is the biggest risk on the page — it will be the first thing every interviewer asks about, and the answer is shakier than it looks. The pilot metrics (15%, 3-8%, 4%) are fabricated by Danny's own admission and must never appear again. Story 5 (ARB) has a hours discrepancy that is 4-5x and unresolved. Story 10 (self-serve catalog) was not A/B tested. Story 11 (churn model) is a rule-based system dressed as ML.

The AI positioning (Stories 14 and 16) is the right move for Danny's target market but is currently buried. It needs to lead, not trail.

What follows is the most rigorous read I can give this library.

---

## DEFENSIBILITY ASSESSMENT (PER STORY)

---

### Story 1: ATLAS/BAR — The System

**Defensibility: HIGH — with specific exceptions**

The core build is real. Bus factor of 1 is confirmed. The MILP formulation is code-confirmed. The six-component objective function, constraint families, and config-driven architecture are all verifiable. Danny can walk through every piece of this in detail because he built it.

**What holds up under pressure:**
- "Sole data scientist" — fully defensible. He can describe what that means operationally: no engineering support, personal GitHub, Streamlit dashboards, Snowflake pipelines built himself.
- The MILP formulation — he can name the objective terms, constraint families, and solver (PuLP/CBC). He knows why he chose CBC (access constraints at JPMC, not a free choice).
- The config-driven architecture — he can explain what "config-driven" means in practice (role_definitions.py, capability flags, zero code changes to add a role). This is a strong engineering story.
- The double-regression outreach methodology — he can walk through both phases in detail. This is sophisticated and real.
- The matched-pairs value estimation — he can describe the matched-pairs process, the 12-month balance growth window, and the role-by-product-by-affluence dictionary.
- The demand buffer algorithm — he can explain the CRM undercounting problem, the iterative scaling approach, and the 65-80% target range.
- The BSOT integration — he can describe the 5 binary variables per branch, the exactly-one constraint, and why this was the key to condensing the recommendation swings.
- The disruption cost grid search — he can name the acceptance criteria (30%+ unchanged, 90%+ within ±1 net shift) and explain why a grid search was necessary.

**What will get probed and how to handle it:**

*"What solver did you use?"* — Answer: PuLP/CBC. Do NOT say Gurobi. If asked why not Gurobi: "Access constraints at a large bank. CBC is open-source and available through PuLP. For our problem size — 150-250 branches per region — CBC with tight constraints and warm starts gets us to 1.5 hours for the full network, which is acceptable for a monthly planning cycle." This is honest and defensible.

*"Is this in production?"* — This is the hardest question. The honest answer: "BAR is deployed as decision support. Workforce Planning and Finance use it as a gut check and scenario planner. Full automated rollout is in phased market pilots — 5-10 branch clusters. The system is live and informing real decisions; a complete network-wide automated rollout is a multi-year political and operational lift at this scale." That's a real and honest answer. Don't overclaim "fully deployed."

*"You said you built the XGBoost model — did you?"* — No. BSOT is another team's model. The defensible claim is "integrated an existing XGBoost revenue-lift model." Danny knows how XGBoost works and can speak to it, but he should not claim he built BSOT.

*"What does 'config-driven' mean in practice? Can a non-technical user run this?"* — Honest answer: the architecture supports it, a Streamlit app exists, but WFP doesn't have access yet due to risk controls. This is fine — it shows thoughtfulness about productionization, not failure.

**Landmines in the approved bullets:**

Tier 1-E says "built a production decision system (ATLAS)." The word "production" is aggressive given the actual deployment state. Interviewers at Google/Anthropic will ask "what does production mean here?" Danny needs to be ready: "Production in the sense that it runs on real data, produces real recommendations used by Workforce Planning and Finance, and is the authoritative source for staffing decisions in pilot markets. Full automated network rollout is in progress."

---

### Story 2: ATLAS — Impact & Scale

**Defensibility: MEDIUM — the $9B is the biggest interview risk in the entire library**

This is where Danny is most exposed. Every interviewer will ask about $9B. It will be the first question in every phone screen. The number is real in the sense that it came from a legitimate analytical process and the CFO endorsed it. But it is projected, not realized, and the assumptions are significant.

**The $9B stress test:**

The calculation is: matched-pairs value estimation × optimized task allocation → projected monthly balance growth of $750M → $9B annually. The CFO's own framing ("even if we're wrong by 50%") signals that leadership treats this as a directional estimate, not a precise forecast.

Under pressure, Danny's answer needs to be: "We built the $9B projection by taking our matched-pairs role-by-product value dictionary and modeling what the optimized allocation would generate in balance growth relative to today's allocation, split across banking and investment products. It's a net-neutral projection — no new headcount, just better placement. The CFO endorsed the methodology and said 'even if we're wrong by 50%, this delivers $4.5B.' It's a projection, not a realized result. We're in phased market pilots now to validate the directional assumptions."

That answer is defensible. What is NOT defensible: claiming $9B was "delivered" or "generated." The approved bullets correctly use "projected." This must be maintained absolutely.

**The $150M problem:**

Multiple old bullets use $150M in inconsistent ways. Danny's own input says "calculations changed over time." The approved bullets correctly retire $150M in favor of $750M/month balance growth and $5-15M/month cost savings. These should never be mixed. Pick one framing per resume and stick to it.

**The pilot metrics that must never appear:**

15% reduction in mis-staffed hours, 3-8% task utilization improvement, 4% account conversion lift — Danny confirmed these were estimates he "threw in." These are fabricated numbers on a resume for a company like Google or Anthropic. If these appear in any bullet Danny submits, they will be probed and he will not be able to defend them. The Story 2 agent rules correctly ban these. Enforce this absolutely.

**What IS defensible in Story 2:**

- $9B projected annual balance growth (with "projected" qualifier, with the assumption walkthrough ready)
- $5-15M/month cost savings from role-mix reallocation (mechanism is clear and explainable)
- 90% of recommendations within ±1 net shift (from grid search acceptance criteria — defensible)
- 30%+ branches unchanged (same source — defensible)
- CEO approved phased rollout (confirmed)
- CFO quote (confirmed)
- System informing surgical staffing decisions today (confirmed — WFP and Finance use it)

---

### Story 3: ATLAS — Technical Architecture

**Defensibility: HIGH for MLE/OR roles, MEDIUM for product roles**

The technical depth here is real and code-confirmed. Danny can walk through:
- Solve-time optimization: overnight → 1.5 hours through warm starts and constraint engineering
- Region-level partitioning: 150-250 branches, why this works for the business case
- Data contracts and pre-flight validation
- The Streamlit scenario planner

**One risk:** The "production infrastructure" framing. Danny's honest description is: personal GitHub, Snowflake pipelines, Streamlit dashboards, scheduler still in progress. For MLE roles at Google or Anthropic, "production infrastructure" implies CI/CD, containerization, MLflow or similar. Danny's setup is more "sophisticated analyst infrastructure" than "ML engineering production." He should be ready to explain the constraints: "JPMC's access controls limit what tools I can use. I built what I could within those constraints — Snowflake pipelines, automated scripts, Streamlit dashboards, version control. The formal MLOps layer is on the roadmap but requires a platform team lift I don't control."

That's honest and actually shows maturity — he understands the gap and can articulate why it exists.

**The Gurobi trap:** Story 3's fact sheet still lists "Gurobi solver" in the confirmed column, which contradicts Story 1's agent rules. This is a documentation error in the library. The solver is PuLP/CBC. This must never appear on a resume.

---

### Story 4: ABME — Staggered DiD / National Experimentation

**Defensibility: HIGH — Danny's cleanest story**

This is the most defensible story in the library. The methodology is published at danieltabach.github.io. The results are statistically significant. The business outcome is permanent and verifiable (the AB role is gone nationwide). Danny can walk through every piece of this.

**What holds up:**
- Event-study DiD with staggered adoption — Danny can walk through the time-normalization logic. The blog post is the backup.
- A/B/C design — three arms with clear hypotheses, C-arm informed a "no" decision (sophisticated)
- +8-15% outreach lift, +5-12% account opening volume — statistically significant, Danny confirmed
- +6-8% servicing-to-account-opening conversion — statistically significant
- Parallel trends validated — confirmed
- CEO presentation (2 slides), nationwide expansion — confirmed

**What will get probed:**

*"Walk me through the DiD methodology."* — Danny's answer: "The challenge was staggered adoption — branches onboarded at different calendar months. I normalized all branches to relative event time, defining the adoption window (first to last trainee completing licensing within each branch) as 'period 0' — too noisy to measure due to training disruption. I then compared pre-period to post-period across branches, controlling for branch size by grouping similar branches together. I validated parallel trends in the pre-period. This is the Callaway-Sant'Anna approach to staggered DiD." Clean and defensible.

*"Why not use a synthetic control?"* — "Sample was limited enough that synthetic control would have been unstable. DiD with size controls and parallel trend validation was the right call for this population size."

*"Did you run placebo tests?"* — Danny admitted he didn't know what placebo tests were when asked. This is a gap. He should know: a placebo test assigns fake treatment dates to control units and checks whether the estimated effect disappears. If an interviewer at Google asks this, Danny needs an answer. Recommend he learn this before interviews.

*"How did you handle the 6-month reversion issue?"* — "Post-rollout, some ABs reverted to servicing/teller habits. This was a coaching and management issue, not an experiment flaw — the experiment measured the entitlement effect under normal conditions. We addressed it with scorecards and floor-presence requirements. It's an important caveat about sustained behavioral change requiring management reinforcement."

**The one metric to never use again:**
The "+17% outreach" number from Resume #3 is fabricated. The real number is +8-15%. The "+4% client meetings" secondary metric couldn't be powered to significance. These must not appear.

---

### Story 5: ARB — Matched-Pairs Pilot

**Defensibility: LOW-MEDIUM — significant problems**

This story has three problems that will surface in interviews:

**Problem 1: The hours discrepancy.** "10-20 hours/week" vs "~20 hours/month" — these are 4-5x apart. Danny has not resolved this. Under interview pressure: "How did you calculate 10-20 hours per week per location?" Danny's answer will be unclear because the number evolved across resumes without a clean source. **Recommendation: Drop the specific hours number entirely.** Say "freed significant senior banker capacity per location for high-value outreach" and let the interviewer ask for specifics. If pushed, Danny needs to reconstruct the calculation from first principles.

**Problem 2: The propensity model is "fluff" by Danny's own admission.** Story 5's agent rules include a propensity modeling angle. Danny said: "One propensity model was seeing the propensity for an account to be opened by an ARB. Truthfully I didnt work on this much this story is more like fluff." If this appears on a resume and an interviewer asks "walk me through the propensity model you built for ARB," Danny will not be able to. **Do not use the propensity modeling bullet for ARB.**

**Problem 3: The impact was modest.** Danny's own input: "the lift was.. negligible. The unfortunate part is this really shipped due to cost savings - not innovation on a role." If an interviewer asks "what were the results of the ARB pilot?" and Danny says "about 5% measurable lift in accounts opened," that's a weak result for a 150-branch experiment. The real story is "we validated a cost-saving role substitution" — which is honest but less impressive than the bullet framing suggests.

**What IS defensible:**
- Matched-pairs methodology across 150 branches — real
- Colorado pilot, then expansion — real
- Two treatment arms (add vs. swap) — real
- Senior banker capacity freed — real, just without a defensible specific number

**Recommendation:** Use this story only when you need a second experimentation bullet and the JD specifically asks for matched-pairs or small-sample experiment design. Lead with ABME. If ARB appears, drop the hours number and the propensity model claim.

---

### Story 6: FAST — Propensity-to-Pay Model

**Defensibility: MEDIUM**

This is a real model with a real outcome (loan program launched). Danny can walk through the feature engineering (balance sizes, overdraft frequency, deposit consistency, autopay indicators, lagging deposit trends) and the ROC curve tuning. AUC ~88-90% is credible for a logistic regression with good feature engineering.

**What will get probed:**

*"What was your role vs. the team's?"* — Danny's answer: "I was responsible for the feature engineering and the ROC curve calibration. The loan program design was a separate team's work — I provided the scoring." This is honest and fine.

*"How did you choose the threshold?"* — "I adjusted the operating point on the ROC curve to balance false positives (unnecessary intervention cost) against false negatives (missed at-risk customers). The goal was to capture the customers who were genuinely at risk of overdraft or late payment while keeping the intervention pool manageable." Clean answer.

*"Is the model still running?"* — "It was handed off to another team after validation. I don't know the current status." Honest.

**No major landmines here.** This is a bench story — use it when the JD needs customer-level modeling or financial products experience.

---

### Story 7: FAST — Next-Best-Product XGBoost

**Defensibility: MEDIUM — with one important caveat**

The model is real. 400+ features, SHAP for importance, clustering for targeting, PySpark productionization, 8% lift in business account openings. Danny can speak to the business problem (identify future entrepreneurs before they go to a competitor) and the feature engineering approach (transaction signals, brand interactions, money flow patterns).

**The important caveat:** Danny said "No one is going to check source code. Use XGBoost if need be almost for a keyword ATS search." This is a yellow flag. Danny built the feature engineering and worked on the model, but the MLOps was handled by the tech team after handoff. If an interviewer asks "walk me through the XGBoost training pipeline — how did you handle class imbalance? What was your CV strategy? What was the evaluation metric?" Danny's answer will be thin. He remembers SHAP and clustering but not the training details.

**Recommendation:** Frame as "engineered features for and productionized an XGBoost customer segmentation model" — which is defensible — rather than "built an XGBoost model" which implies full ownership of training and evaluation. The PySpark productionization is the real differentiator here.

*"8% lift — how was that measured?"* — "We compared the business account opening rate in our target population (customers scored as high-propensity by the model) against the historical base rate for that population. Within 6-8