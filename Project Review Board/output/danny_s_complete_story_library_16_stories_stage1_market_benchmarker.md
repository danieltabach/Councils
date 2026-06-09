# Market Benchmarker — stage1

# Market Benchmarker Review: Danny Tabach

---

## Competitive Position

Danny is in the **top 10-15% of the applicant pool** for Tier 1 and Tier 2 DS roles, and potentially **top 5%** for the specific intersection of applied optimization + experimentation + AI research that he represents. Here's the honest breakdown by target tier:

**Dream tier (OpenAI, Anthropic, DeepMind):** Currently a **long shot, not a no.** The ArXiv preprints are real and the ATLAS build is genuinely impressive, but the research portfolio is two papers deep, both from 2026, with no conference publications, no co-authors with institutional credibility, and a methodology that behavioral/alignment researchers will probe hard (n=21 writers is the obvious target). The autonomous planner-to-research pipeline story is compelling and differentiated — but Anthropic Fellowship candidates typically have either a stronger publication record or a PhD-track signal. He should apply, especially for the Fellowship, but shouldn't anchor his strategy here.

**Tier 1 (Google, Apple):** **Strong candidate, not a lock.** Google DS roles at the L5-L6 level will see hundreds of applicants with FAANG experience, strong ML backgrounds, and often graduate degrees from top programs. Danny's ATLAS build — a production MILP system at this scale, built solo — is genuinely unusual. The experimentation depth (ABME staggered DiD, event-study methodology, published blog) is above average. The MS from Georgia Tech (completing Dec 2026) adds credibility. He should be getting interviews here.

**Tier 2 (Stripe, PayPal, Intuit, Shopify):** **Must-interview territory.** The combination of startup experience (SwagUp), production system ownership (ATLAS), experimentation rigor (ABME), and AI research (two ArXiv papers) is rare at this level. These companies will see his profile and want to talk.

**The core competitive problem:** Danny's resume history shows a pattern of inconsistent numbers, banned claims (Gurobi, patent pending, fabricated pilot metrics), and framing drift that could collapse an otherwise strong candidacy in a behavioral screen. The content is strong. The execution has been sloppy. That's fixable.

---

## Unique Edge

Danny has **three genuine differentiators** that most applicants at his level don't have. The problem is that only one of them is currently unmistakable on the resume.

**Differentiator 1 (Unmistakable): The ATLAS build.** A solo-built, production-grade MILP optimization system across 4,300+ branches impacting 24K FTEs, with CEO sign-off, is not something the other 99 resumes have. This is the anchor. It signals: can formulate complex problems mathematically, can ship production systems, can navigate enterprise politics, can translate technical work to C-suite. No one else in the pile has this.

**Differentiator 2 (Partially visible): The experimentation depth.** A staggered DiD event-study for a 10K-employee national rollout that permanently eliminated a role nationwide — that's not "ran an A/B test." The methodology is rigorous enough to publish (and he did publish the methodology). Combined with the ARB matched-pairs work and the SwagUp A/B test, Danny has a three-story experimentation portfolio spanning causal inference, quasi-experimental design, and controlled testing. This is above average for a DS with ~5 YOE.

**Differentiator 3 (Undersold): The AI research angle.** Two solo-authored ArXiv preprints in 2026, both on AI behavior, both self-funded, both built on production domain expertise — this is the bridge to AI labs and research-adjacent roles. The LLM behavioral measurement paper (2605.21827) in particular has a genuinely interesting finding (state dominance 10:1 over word choice, behavioral mode-switching near constraints) that is directly relevant to agentic AI safety. The story of "I built the autonomous planner, realized it couldn't be trusted, and measured why" is a research origin story that PhDs rarely have.

**What's NOT a differentiator:** The FAST stories (propensity models, XGBoost segmentation) are solid but table-stakes for a DS with 5 YOE at a major bank. The SwagUp churn model is junior-level work dressed up in production ML language. The consulting NLP pipeline is filler. These stories don't hurt, but they don't move the needle.

**Is the edge unmistakable on the resume?** For Differentiator 1: yes, if the right bullets are selected. For Differentiators 2 and 3: no. The experimentation depth is diluted by too many bullet variants that don't lead with the methodology. The AI research is buried in a Projects section that competes with other projects for space.

---

## Scale & Context

This is where Danny's resume history has the most problems, and where the approved bullets represent a significant improvement over the historic variants.

**ATLAS scale — properly contextualized:** "4,300+ branches, ~24K FTEs, CEO sign-off" is sufficient context. The $9B projection needs the "projected" qualifier every single time — the CFO's own framing ("even if we're wrong by 50%") is the right mental model. The approved bullets handle this correctly. The historic variants that say "delivered $150M in monthly revenue" (Resume #20) are a liability — that's a realized claim for a projected number, and it will get caught.

**ABME scale — undersold:** "10,000 employees" is mentioned but the weight of it isn't felt. This is a **national workforce restructuring that permanently eliminated a job title.** The AB role no longer exists. Every Chase branch in the country now runs on a role design that Danny's analysis validated. That's the context that's missing. The approved Tier 1-B bullet gets closest: "role now deployed in every branch" is the right punchline.

**ARB — scale is ambiguous and the story is weak:** The 150-branch number is fine, but Danny's own input reveals the propensity modeling angle is "fluff" and the measurable lift was "negligible." This story should be dropped or severely compressed. If it appears at all, it should be one line, not a featured bullet.

**SwagUp — scale needs startup context:** "B2B startup" is sufficient. The $5M+ number is strong for a startup context. The 40% revenue growth for first-time SMB clients is clean and defensible. The churn model story is a liability — it was rule-based, then a crude logistic regression, and Danny can't quantify retention impact. The approved bullets are honest about mechanism without fabricating numbers.

**FAST — scale is appropriate:** 1M+ customers for the propensity model and 5M+ for the XGBoost model are strong numbers. The AUC ~88-90% for the propensity model is worth including. The XGBoost model's 8% lift in business account opening rates is defensible and worth including.

**The AI papers — scale context is correct:** 6,620 controlled API calls, 251 judges, ~2,000 evaluations are specific and verifiable. The self-funded angle is unique and worth a brief mention.

---

## Seniority Calibration

Danny is targeting Senior DS, Applied Scientist, and Research roles. Here's the honest assessment:

**Where he presents at the right level:**
- ATLAS: The system architecture, cross-functional coordination, C-suite presentation, and solo ownership are senior-level signals. Building and owning a system of this complexity with no engineering support is above what most mid-level DS candidates can claim.
- ABME: Designing the full experimentation strategy, defining the metrics framework, and presenting to the CEO is senior-level work. The "I built the methodology and the CEO approved the expansion" narrative is credible.
- ArXiv papers: Solo-authored research published on ArXiv is a senior/research signal. The LLM behavioral paper in particular shows independent research capability.

**Where he presents below target level:**
- SwagUp churn model: A rule-based system that evolved into a logistic regression scored to a CSV and pushed to Salesforce is not a production ML system by the standards of Stripe or Google. The "operationalized monthly scoring pipeline" framing overstates it. Danny was 21 and doing his first data job — that's fine, but the framing needs to match the reality.
- ARB propensity models: Danny himself says this is "fluff." Don't claim it as a differentiator.
- Consulting NLP: TF-IDF + cosine similarity for name deduplication is junior-level work. Fine as filler, but don't feature it.
- The "5 YOE" framing is accurate but the experience is uneven — 3+ years of genuinely senior-level work (ATLAS, ABME) alongside some genuinely junior-level work (SwagUp churn, ARB propensity). The resume should lead with the senior work and treat the junior work as context, not as parallel evidence of capability.

**The MS completion (December 2026) gap:** This is a real credibility issue for research roles. Georgia Tech MS is strong, but it's not on the resume yet. For Anthropic Fellowship and research-adjacent roles, the degree completion date should be listed as "Expected December 2026" in the education section. This is not optional.

---

## Undersold Strengths

**1. The ABME permanent organizational change.** "The AB role is completely gone. Every Chase branch now has ABMEs." This is the most undersold line in the entire story library. Danny's analysis drove a permanent, nationwide restructuring of a job title across one of the largest branch networks in the country. The approved bullets gesture at this ("role now deployed in every branch") but don't land the punch. The headline should be: *your analysis eliminated a job title.* That's not an A/B test result — that's organizational impact at a scale most senior DS candidates never see.

**2. The ATLAS origin story.** Danny pitched a crude weekend MILP notebook and got hired on the spot. That story — "that was the interview, you start Monday" — is a signal of how he thinks and how he sells. It doesn't belong on the resume, but it's the kind of story that wins behavioral rounds, and Danny should know it's a strength.

**3. The LLM research origin.** "I built the autonomous planner, realized it couldn't be trusted with vague language, and measured why" is a research origin story that most alignment researchers don't have. They study LLM behavior from the outside. Danny studied it from inside a production system he built. That's the framing that should open every conversation about the paper.

**4. The solve-time optimization.** Cutting full-network solve time from 8-12 hours to 1.5 hours through warm starts and constraint engineering is a real engineering achievement that demonstrates production-grade thinking. It's buried in Story 3 as a Tier 2-E bullet. For MLE and analytics engineering roles, this should be featured.

**5. The blog post at danieltabach.github.io.** A published, detailed methodology write-up showing that naive calendar-cutoff approaches underestimate treatment effects by ~27% — with Python code, references to Callaway & Sant'Anna, Sun & Abraham, and Goodman-Bacon — is a strong public work sample. This is not just a blog post; it's a technical document that demonstrates graduate-level understanding of econometric methods. It should be linked prominently.

**6. The CFO quote.** "Even if we're wrong by 50%, this thing will deliver 4.5 billion. I believe in the numbers." That quote is not on the resume, but it's the kind of validation signal that interviewers remember. Danny should have it ready.

---

## Positioning Gaps

**Gap 1: No explicit AI/ML skills section that signals research capability.** The resume needs a skills section that includes: Python, SQL, PuLP/CBC (MILP), XGBoost, Scikit-learn, Streamlit, Supabase, Snowflake, Anthropic API, statistical methods (DiD, matched-pairs, nonparametric tests), and research methods. Right now, the technical stack is scattered across bullets and not visible at a glance. For AI lab roles, the Anthropic API and LLM tool-call experience should be front and center.

**Gap 2: The AI research is not positioned as a research practice.** Two solo-authored ArXiv preprints in the same year, both self-funded, both built on production domain expertise, with planned extensions and conference submissions — that's a research practice, not two one-off projects. The Projects section should frame them together: "Independent AI Research" as a header, with both papers listed, would signal to Anthropic and OpenAI reviewers that this is intentional, not accidental.

**Gap 3: No mention of the autonomous planner build.** Danny rebuilt ATLAS as an autonomous scenario planner with an LLM agent harness — that's the bridge between his optimization work and his AI research. This doesn't appear anywhere in the story library as a standalone bullet. For AI lab and agentic AI roles, "built an autonomous resource-allocation agent on top of a production MILP system" is a stronger signal than either story alone.

**Gap 4: The MS degree is absent.** Georgia Tech MS (Expected December 2026) must appear in the Education section. For research roles, the degree and institution are credibility signals that recruiters look for in the first 3 seconds.

**Gap 5: No cross-company experimentation signal.** Danny has run experiments at Chase (two major ones), SwagUp (A/B test), and Georgia Tech (AI detection). A recruiter reading the resume should immediately think "this person runs experiments everywhere." Right now, the experimentation depth is visible if you read carefully, but not if you skim. The summary/headline section (if it exists) should surface "experimentation" as a core identity.

**Gap 6: The "bus factor of 1" is undersold as an ownership signal.** At senior DS level, end-to-end ownership of a production system is a key differentiator. The approved bullets say "sole data scientist" and "built end-to-end" — that's correct. But the story behind it (no engineering support, no data engineering team, built Snowflake pipelines, Streamlit dashboards, automated execution, personal GitHub, all within JPM's constrained tech environment) is a stronger ownership signal than the bullet conveys. For MLE and analytics engineering roles, this infrastructure story needs to be more explicit.

---

## Story Selection & Assembly Recommendations

Given the one-page constraint and the target role types, here are my concrete picks:

### For AI Lab / Research Roles (Anthropic Fellowship, OpenAI, DeepMind)

**Lead with research, anchor with production depth.**

**JPMC Section (2 bullets max):**
- Story 1, Tier 1-A: The MILP formulation bullet — shows mathematical rigor
- Story 2, Tier 1-A: The $9B projected with "90% within ±1 shift" detail — shows scale and actionability

**SwagUp (1 bullet):**
- Story 9, primary B: The A/B test with statistical emphasis — shows experimentation rigor

**Projects Section (2 bullets — non-negotiable):**
- Story 16, Tier 1-A: The LLM behavioral measurement paper — this is the primary AI research signal
- Story 14, Tier 1-B: The AI detection experiment — secondary AI research signal

**Drop entirely:** ARB (Story 5), FAST household acquisition (Story 8), consulting (Story 15), churn model (Story 11), drift detection (Story 13), product catalog (Story 10), dashboards (Story 12)

---

### For Tier 1 DS / Applied Scientist (Google, Apple)

**Lead with scale and impact, show experimentation depth.**

**JPMC Section (3 bullets):**
- Story 1, Tier 1-B (Decision Scientist): The automated decision platform replacing manual workflows — accessible framing
- Story 2, Tier 1-B: The $9B projected with CFO/CEO endorsement
- Story 4, Tier 1-B: ABME event-study DiD — the experimentation flagship

**SwagUp Section (2 bullets):**
- Story 9, primary B/C: The $5M+ A/B test
- Story 7, MLE lead: The XGBoost 5M+ customer segmentation model — shows ML at scale

**Projects Section (2 bullets):**
- Story 14, Tier 1-B: AI detection experiment (ArXiv)
- Story 16, Tier 1-C: LLM behavioral measurement (ArXiv) — product DS framing

**Drop entirely:** ARB (Story 5), FAST household acquisition (Story 8), consulting (Story 15), churn model (Story 11), drift detection (Story 13)

---

### For Tier 2 / Product DS (Stripe, PayPal, Intuit, Shopify)

**Lead with business impact and experimentation, show product sense.**

**JPMC Section (3 bullets):**
- Story 1, Tier 1-C: The automated decision platform with 7+ team coordination
- Story 2, Tier 1-C: The $9B projected with CEO presentation framing
- Story 4, Tier 1-C: ABME with north star