# Hiring Manager — stage1

# Hiring Manager Review: Danny Tabach — Full Story Library Assessment

---

## First Impression (6-Second Scan)

What registers immediately: **a builder who ships at scale inside a major institution, with two solo ArXiv preprints and a genuine AI research thread.** The ATLAS/BAR story is immediately legible as a flagship — $9B projected, 3,700+ branches, sole DS, C-suite sign-off. That's a headline.

What's confusing: **the story library is 16 stories deep for a one-page resume.** The abundance creates a selection problem, not a quality problem. The risk is a resume that tries to say too much and ends up saying nothing clearly in 6 seconds.

The headline takeaway: **Danny is a rare hybrid — production optimization engineer, rigorous experimentalist, and emerging AI researcher, all in one person.** The resume's job is to make that unmistakable in the first 6 seconds. Right now, the story library has the raw material. The assembly is the work.

---

## Callback Assessment

### Story 1 + 2 + 3: ATLAS/BAR System, Impact, Architecture
**Verdict: CALLBACK — but only with the right bullet selection**

This is the anchor. A sole-DS MILP system across 3,700+ branches with C-suite sign-off is genuinely rare. I've seen hundreds of "optimization model" bullets. Almost none of them have: (a) 24K FTEs in scope, (b) a multi-component objective function the candidate can defend line by line, (c) a config-driven architecture the candidate built alone, and (d) a CEO who approved the rollout. The combination earns a call.

**What works:** The Tier 1-A bullet (OR/Applied Scientist framing) is the strongest single bullet in the library. It's specific, defensible, and signals genuine technical depth. The "6-component objective" detail and the "16 customer cohorts" aren't resume filler — they're proof that the candidate actually formulated this.

**What doesn't work:** The $9B number. Not because it's wrong — the CFO's quote is actually the most credible framing imaginable — but because "$9B projected" on a resume reads as either a typo or a stretch. Every hiring manager's first instinct is "that's a big number, is it real?" The answer is yes, but the resume can't explain it. The $9B needs to be earned with context, not dropped as a headline.

**My recommendation:** Lead with the system, not the impact. The system is defensible and impressive on its own. The $9B can appear as a supporting detail with the "projected" qualifier and the "net-neutral headcount" context — that framing is actually *more* impressive than the raw number because it shows the mechanism.

**Defensibility check:** The Gurobi landmine is real and documented. If Danny uses "MILP solver" or "PuLP" he's fine. If he ever says Gurobi in an interview at a company that cares about solvers, he's exposed. The "patent pending" landmine is also real — the paper exists but hasn't been filed. Don't use it.

**The "bus factor of 1" framing** is powerful for senior roles and should be explicit. "Sole data scientist" undersells it slightly — "built and owned end-to-end as sole DS" is the right construction.

---

### Story 4: ABME — Staggered DiD / National Experimentation
**Verdict: CALLBACK**

This is the strongest experimentation story in the library, and it's genuinely differentiated. A staggered DiD event-study across 10K employees, validated parallel trends, a three-arm design, and a result that drove permanent organizational change (the AB role is gone nationwide) — that's not a resume bullet, that's a career story.

**What works:** The "role now deployed in every branch" punchline is devastating in the best way. Most DS experimentation stories end with "informed a decision." This one ended with the original role being eliminated nationwide. That's the callback moment.

**What doesn't work:** The old pilot metrics (15%, 3-8%, 4%) are confirmed fabrications. They're documented as "I threw a number." If any of those appear on the resume and an interviewer probes them, it's a failed interview. The approved bullets correctly use the confirmed ranges (+8-15% outreach, +5-12% openings, +6-8% conversion). Use only those.

**The blog post (danieltabach.github.io)** is a genuine differentiator. A published methodology walkthrough with Python code is something most candidates don't have. It should be referenced on the resume — either as a URL in the header or as a note in the experimentation bullet.

**Defensibility check:** The "27% underestimation" finding from the blog is strong for decision science roles. The three-arm design and the C-arm "informed a no" decision shows experiment design maturity. Both are defensible.

---

### Story 5: ARB — Matched-Pairs Pilot
**Verdict: MAYBE**

Solid methodology story, but it's clearly the weaker sibling to ABME. The 150-branch matched-pairs result (10-20 hours/week freed) is defensible but the hours discrepancy (weekly vs. monthly) is unresolved and the propensity modeling angle is confirmed as "fluff." The outcome (5% lift in accounts, negligible otherwise) is underwhelming for a resume bullet.

**My recommendation:** Use this only if the resume needs a second experimentation bullet AND the JD specifically mentions matched-pairs, propensity modeling, or small-sample causal design. Otherwise, ABME carries the experimentation story alone.

**The hours number must be resolved before this story goes on any resume.** "10-20 hours/week" and "~20 hours/month" are 4-5x apart. That's not a rounding difference — that's a defensibility failure waiting to happen.

---

### Story 6: FAST — Propensity-to-Pay Model
**Verdict: MAYBE**

1M+ customers, logistic regression, AUC ~88-90%, drove a product launch. Solid but not differentiated. Every DS at a bank has a customer scoring story. The "flexible loan program for at-risk clients" angle has social impact resonance that could matter for mission-driven companies.

**My recommendation:** Include only if the resume needs a FAST bullet for breadth AND the JD values customer-level modeling or financial products. The ROC curve tuning detail (adjusting FPR/TPR thresholds) is the most technically interesting part — that's the detail worth surfacing if this story is used.

---

### Story 7: FAST — Next-Best-Product XGBoost
**Verdict: CALLBACK (as a supporting bullet)**

This is the strongest FAST story. 5M+ customers, XGBoost with SHAP, PySpark productionization, 8% lift in business account openings within 6-8 months — that's a complete ML story. The "finding future entrepreneurs before they become business customers" framing is genuinely interesting and shows product thinking.

**What works:** PySpark at 5M+ scale signals production ML competency. SHAP for feature importance shows model explainability awareness. The 8% lift is defensible (within 6-8 months, from the target population).

**What doesn't work:** Danny doesn't own the MLOps piece — it was handed off. The bullet should say "engineered and productionized" (which is true) without implying he maintained it in production. The 400+ features detail is impressive but can't fit in a bullet — save for interviews.

**My recommendation:** Use as a FAST supporting bullet alongside Story 6 when the JD values production ML, XGBoost, or customer segmentation. This is the FAST story that should lead if only one FAST bullet fits.

---

### Story 8: FAST — Household Acquisition Analysis
**Verdict: PASS**

Dropped from resumes after #7 for good reason. The "40M by 2030 forecast" is a company target, not Danny's result. There's no methodology, no model, no quantified contribution. This story doesn't belong on a competitive DS resume. Remove from rotation permanently.

---

### Story 9: SwagUp — A/B Test & Pricing
**Verdict: CALLBACK**

$5M+ incremental profit and 40% revenue growth for SMB clients from a pricing experiment that overturned a company-wide assumption and changed policy. That's a clean, compelling story with a clear hypothesis, measurable outcome, and business impact.

**What works:** The "overturned legacy sales assumptions" framing is the narrative hook. The policy change is the business impact. The 40% first-order revenue growth for the treatment group is the number. All three are defensible.

**What doesn't work:** The rigor was limited (3-month run, basic t-test, no power analysis). Danny should not claim statistical rigor he doesn't have. The approved bullets correctly frame this as "designed and executed" without overclaiming methodology. That's the right call.

**The refund rate story (12% → ~1%)** is actually more impressive than the 40% revenue number and is currently underused. A 12-percentage-point reduction in refund rates is a concrete, defensible outcome that shows Danny understood the full customer lifecycle, not just top-line conversion.

**My recommendation:** Lead with $5M+ or 40% revenue growth. Add refund rate reduction as supporting context if SwagUp gets 2+ bullets. This story always makes the resume when SwagUp appears.

---

### Story 10: SwagUp — Product Catalog & Self-Serve Pricing
**Verdict: MAYBE**

The ~5% add-to-cart lift and ~20% self-serve conversion are real but approximate, and the methodology was "we launched it because it seemed like a good idea" with no A/B test. The actual product was a recommendation engine ("Businesses like you ordered...") that Danny built the underlying data for — that's more interesting than how it's currently framed.

**What works:** "Identified zero pricing visibility as a conversion bottleneck" shows product sense and problem identification. That's the differentiator for product DS roles.

**What doesn't work:** The numbers (~5%, ~20%) are approximate and the improvement methodology is weak. If an interviewer asks "how did you measure the 5% lift?" the answer is "general trends, no A/B test." That's a credibility risk.

**My recommendation:** Use for product DS roles where the JD values product intuition and conversion optimization. Reframe around the recommendation engine angle (it's more technically interesting than "self-serve catalog"). Keep the tilde on the numbers. Don't lead with the metrics — lead with the problem identification.

---

### Story 11: SwagUp — Churn Prediction Model
**Verdict: MAYBE**

Production churn model that triggered automated sales outreach — that's the right structure for an MLE story. But the honest version is: rule-based RFM table first, then a logistic regression enriched with Clearbit firmographics, outputting a CSV to Salesforce. It's a real production system, but it's not sophisticated ML.

**What works:** "Monthly scoring pipeline triggering automated sales outreach" is the production proof point. It ran in production and drove real actions. That's more than most junior DS stories.

**What doesn't work:** No quantified retention impact. The mechanism is there but the result isn't. "Improving retention" without a number is weak on a competitive resume.

**My recommendation:** Use only when the JD specifically mentions churn modeling, retention analytics, or production ML pipelines. Pair with Story 9 (A/B test) to show SwagUp breadth. Don't use as a standalone bullet — it needs Story 9 to carry the impact.

---

### Story 12: SwagUp — Analytics Infrastructure & Dashboards
**Verdict: MAYBE (strong for analytics engineering roles)**

Fivetran + DBT + Looker on GCP, consolidating Salesforce + QuickBooks + billing for 1,000+ accounts, reducing weekly manual pulls to daily self-serve monitoring — that's a complete analytics engineering story. The tool stack is legitimate (Danny confirms Fivetran, DBT, Looker, GCP).

**What works:** The "weekly manual → daily self-serve" transformation is the before/after that makes this concrete. Four teams served (sales, finance, product, ops) shows breadth of impact.

**What doesn't work:** Danny's specific role vs. the data engineer's role needs to be clearer. He hired the engineer and built the dashboards; the engineer handled scheduling and data contracts. The bullet should reflect Danny's actual contribution without overclaiming the infrastructure build.

**My recommendation:** Use for analytics engineering or BI-heavy roles. The Fivetran/DBT/Looker stack variant is the strongest version. The "1,000+ accounts" context gives scale. This competes with Story 10 for SwagUp space — for analyst/AE roles, prefer this one.

---

### Story 13: Georgia Tech — Drift Detection Project
**Verdict: MAYBE (MLE roles only)**

Five algorithms benchmarked, detection latency vs. false positive tradeoffs evaluated, Windowed CUSUM and ADWIN as winners — it's a legitimate comparative study. But it's academic coursework, not production, and it competes directly with Story 14 (ArXiv paper) for the Projects section slot.

**My recommendation:** Story 14 wins the Projects slot for almost every target role. Use Story 13 only for MLE/ML monitoring roles where drift detection is explicitly mentioned in the JD AND Story 14 is already placed. Never use both — one-page constraint.

---

### Story 14: Georgia Tech — AI/Human Detection (ArXiv 2604.23471)
**Verdict: CALLBACK — non-negotiable Projects slot**

Published solo-authored ArXiv preprint. Two-phase controlled experiment. 251 judges, ~2,000 paired evaluations. p=0.000243. Four classifiers trained on 10 NLP features couldn't beat chance; human judges could. Self-funded, self-recruited, self-built (two Streamlit apps, Supabase backend, Anthropic API). 

This is research-grade work done independently by someone without a PhD. That's the signal. For AI labs (Anthropic, OpenAI, DeepMind), this is the bullet that gets the resume read. For Google, Stripe, and FAANG-adjacent companies, it's the differentiator that separates Danny from the 500 other applicants with JPMC experience.

**What works:** Everything about this story is defensible and impressive. The counter-intuitive finding (warning didn't moderate AI use, it polarized it) is the kind of result that makes researchers want to talk to you. The "humans beat classifiers" finding is directly relevant to AI safety and LLM evaluation. The full-stack build (two apps, backend, automated testing, bot dry-runs) shows engineering competency.

**What doesn't work:** The Tier 1-B bullet (Decision Scientist framing) is the strongest for most target roles. The Tier 1-E (MLE/NLP) buries the lead by starting with feature engineering rather than the finding. Lead with the finding, not the methodology.

**My recommendation:** This story MUST be in the Projects section. Use the Tier 1-B or Tier 1-A bullet depending on the role. Always include "(ArXiv: 2604.23471)." This is Danny's AI research credential — it needs to be unmissable.

---

### Story 15: Consulting — Cohort Analytics & NLP Pipeline
**Verdict: PASS for most roles**

TF-IDF + cosine similarity for customer name deduplication and automated Excel reporting. It's real work but it's the weakest story in the library. Use only if the JD specifically mentions entity resolution, record linkage, or RFM analysis AND the resume has space after all other stories are placed. In practice, this never makes the cut for the target roles.

---

### Story 16: LLM Behavioral Measurement — Vague Intensity Words (ArXiv 2605.21827)
**Verdict: CALLBACK — critical for AI lab positioning**

This is the story that could get Danny into Anthropic. Not because of the paper alone — because of the origin. He built the production optimization system, wanted to bolt an LLM agent onto it, realized it couldn't be trusted, and measured why. That's the intellectual trajectory of someone who should be doing AI safety research.

The findings are genuinely interesting: 10 intensity words compress into ~5 distinct outputs, system state dominates word choice 10:1, and the model mode-switches near constraint boundaries rather than degrading smoothly. For agentic AI, alignment research, and AI product roles, this is directly relevant work.

**What works:** The Tier 1-A bullet (Applied Scientist/Alignment framing) is the right lead for AI lab applications. The "specification failure invisible to the operator" framing is the punchline. The $250K downstream propagation makes it concrete. The origin story (builder who questioned his own system) is the differentiator.

**What doesn't work:** The Tier 1-E bullet (MLE/AI Engineering) buries the finding in infrastructure details. The infrastructure is impressive but secondary. Lead with the problem and the finding.

**My recommendation:** Pair with Story 14 in the Projects section when targeting AI labs. Together, two solo ArXiv preprints demonstrate a real research practice. For