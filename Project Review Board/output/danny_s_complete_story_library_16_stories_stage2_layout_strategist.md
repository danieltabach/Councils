# Layout Strategist — stage2

# Reviewer G Response: Layout Strategist

---

## Agreements

**Reviewer A — ATS/Recruiter: Skills section as standalone keyword block**

Reviewer A flags that "Python" and "SQL" don't appear as explicit tokens in any approved bullet, and recommends a dedicated Skills section. I agree completely and should have been more specific about this in my original review. My section order recommendation included "SKILLS" as a section but I didn't specify what it must contain or why it's structurally critical. Reviewer A is right that ATS systems parse standalone keyword tokens differently from keywords embedded in prose. A two-line Skills row is not optional — it's load-bearing infrastructure for ATS passage. I'll address this in my revisions.

**Reviewer B — Hiring Manager: Impact before method in bullet ordering**

Reviewer B recommends leading with the impact bullet ($9B, CEO sign-off) before the system description bullet. I disagree with this for most targets (see Disagreements), but I agree with the underlying principle: the system description bullet must not be so technically dense that a recruiter bounces before reaching the impact. Reviewer B's point that "MILP-based staffing optimization" reads as "operations research specialist" to a product DS recruiter is a real layout risk I underweighted.

**Reviewer C — Story Architect: The ATLAS-to-LLM-paper connection is invisible**

Reviewer C identifies that the connection between ATLAS/BAR (Stories 1-3) and the LLM behavioral paper (Story 16) — that Story 16 was *born from* the production system — is the most compelling narrative thread Danny has, and it's currently invisible on the resume. I agree, and this is a layout problem, not just a narrative problem. If the Projects section is formatted as two disconnected paper entries with no link to the Experience section, the reader never makes the connection. The fix is structural: the Story 16 bullet must explicitly reference "production-grade constrained optimization system" so the reader who just finished reading about ATLAS immediately recognizes the origin. This is a one-phrase layout intervention that changes how the whole page reads.

**Reviewer F — Skeptical Interviewer: "Enterprise-wide rollout" is a defensibility risk in the Tier 1-C bullet**

Reviewer F flags that the Story 1-C bullet's phrase "enterprise-wide rollout" is inflated given the actual deployment state (phased pilots, surgical decision support). I flagged the Tier 1-C bullet as the weakest Tier 1 bullet but didn't specifically call out this phrase. Reviewer F is right that this is a live landmine. I'll incorporate this into my role-specific layout recommendations.

**Reviewer H — Market Benchmarker: "Independent AI Research" as a Projects section header**

Reviewer H recommends framing the two ArXiv papers under a single "Independent AI Research" header rather than as two separate project entries. This is a layout insight I missed. A shared header signals intentionality — it tells the reader these two papers are part of a research practice, not two unrelated one-off projects. This changes the visual hierarchy of the Projects section significantly and I should have caught it.

**Reviewer D — Assembly Strategist: Story 5 (ARB) should be retired**

Reviewer D recommends retiring Story 5 from active rotation. I included it as a conditional story ("include only if JD specifically mentions matched-pairs"). Reviewer D, Reviewer C, and Reviewer F all independently reach the same conclusion: the hours discrepancy is unresolved, the propensity modeling claim is confirmed as fluff, and the results were negligible by Danny's own description. Three independent reviewers agreeing on a cut is strong signal. I should have been more decisive: Story 5 is cut, not conditional.

---

## Disagreements

**Reviewer B — Hiring Manager: "Lead with impact, not the system"**

Reviewer B recommends that the first bullet under JPMC should always be the impact bullet ($9B projected, CEO sign-off) regardless of role type, with the technical system bullet second. I disagree with this as a universal rule, and I think it creates a specific layout problem for technical roles.

For OR/Applied Scientist targets (OpenAI, Anthropic, Google research), the $9B number appearing before the reader knows what the system IS will read as either a typo or a stretch. The reader's first question will be "what generated $9B?" and the answer is in the second bullet. That's a bad reading experience — the reader has to work backward. For technical audiences, the system description earns the impact claim. Impact-first works when the reader already has context; it doesn't work on a cold read for a number this large.

For product DS and decision science targets, Reviewer B's recommendation is correct. But it shouldn't be universal.

**My position:** The system bullet leads for OR/Applied Scientist/MLE targets. The impact bullet leads for product DS, decision science, and analyst targets. This is a role-specific layout decision, not a universal one, and my original review was right to frame it that way.

**Reviewer A — ATS/Recruiter: Em-dashes are an ATS parsing risk**

Reviewer A recommends replacing em-dashes with colons or semicolons because some ATS parsers strip em-dashes and concatenate adjacent words. This is technically accurate but I think it's overweighted as a concern for Danny's specific target companies. OpenAI, Anthropic, Google, Stripe, and Shopify all use modern ATS systems (Greenhouse, Lever, Workday) that handle Unicode characters correctly. The em-dash parsing failure is a real issue for legacy systems at mid-market companies, but Danny's Tier 1-2 targets are not running legacy ATS. Replacing em-dashes across the board would make the bullets less readable for human reviewers, which is the higher-stakes concern. I'd keep em-dashes in the Projects section (where the bullets are longer and more complex) and use semicolons in the Experience section bullets where the structure is tighter.

**Reviewer D — Assembly Strategist: Removing Consulting as a standalone Experience entry**

Reviewer D recommends removing Consulting as a separate Experience entry entirely and folding the NLP work into Skills or omitting it. I partially agree — Consulting is low priority and Story 15 is weak. But there's a layout reason to keep a minimal Consulting entry: it fills a potential gap in the timeline. If Danny's resume shows JPMC (May 2024-present), SwagUp (2021-2022), and FAST (Aug 2022-Apr 2024) with nothing else, the timeline is actually clean. But if there's any gap that needs covering, a one-line Consulting entry ("Independent Consultant | 2024-2025 | NLP pipeline for client CRM integration") costs one line and closes the gap. Whether this matters depends on the actual timeline — I don't have enough information to be definitive. My recommendation: keep Consulting as a one-line entry with no bullets if there's a timeline gap; remove it entirely if the timeline is clean without it.

---

## Revisions to My Review

### Addition 1: Skills Section Must Be Specific

My original review listed Skills as a section in the recommended order but didn't specify content. Based on Reviewer A's ATS analysis, the Skills section must explicitly include these tokens as standalone words:

```
Languages: Python, SQL
Tools: PuLP, XGBoost, Scikit-learn, PySpark, Snowflake, Streamlit, Tableau, Looker, Fivetran
Methods: MILP, Difference-in-Differences, Matched-Pairs, A/B Testing, Causal Inference
APIs/Infra: Anthropic API, Supabase, GitHub
```

This should be formatted as 2-3 compact lines, not a categorized table that consumes 6+ lines. The goal is keyword token coverage, not comprehensiveness.

### Addition 2: "Independent AI Research" as Projects Header

I missed this. The Projects section should be headed "Independent AI Research" rather than just "Projects." This single-word change signals intentionality to AI lab reviewers. The two papers then appear as entries under that header:

```
INDEPENDENT AI RESEARCH
─────────────────────────────────────────────────────────────────────
Vague Intensity Words in LLM Tool-Use Actions | Solo-authored | ArXiv: 2605.21827
[one-sentence finding]

AI Detection Warning Effects on Writing Behavior | Solo-authored | ArXiv: 2604.23471  
[one-sentence finding]
```

Note the ordering: Story 16 (LLM behavioral measurement) leads because it's more directly relevant to agentic AI and alignment — the primary differentiator for dream-tier targets. Story 14 (AI detection) follows. For Tier 2 targets where Story 14 is more relevant