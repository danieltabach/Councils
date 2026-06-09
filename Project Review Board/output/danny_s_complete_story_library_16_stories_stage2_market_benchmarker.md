# Market Benchmarker — stage2

## Agreements

**Reviewer A (Layout Strategist) — Section ordering and JPMC space allocation:**
Agree entirely that Experience must lead, Education follows, and the top third of the page must hit ATLAS within 3 seconds. The "impact-first vs. system-first" debate Reviewer A raises is real — I recommended leading with the system bullet and treating impact as supporting, while Reviewer A notes the recruiter's eye goes to the first 8 words. We're actually aligned: the system bullet should be written so its first 8 words ARE the impact signal. "Built an automated decision platform replacing manual staffing workflows across 3,700+ branches" accomplishes both — it's a system description that reads as impact.

**Reviewer B (Bullet Surgeon) — Tier 1-C is the weakest ATLAS bullet:**
Agree completely. The current Tier 1-C buries the technical work and reads as a PM bullet. I flagged this as a positioning gap; Reviewer B correctly identifies it as a structural problem at the bullet level. The fix is the same: open with what the system IS, close with the cross-functional proof.

**Reviewer D (Skeptical Interviewer) — ARB is a liability:**
Agree strongly. Danny's own words ("the lift was negligible," "this really shipped due to cost savings — not innovation") are disqualifying for a featured bullet. The hours discrepancy (10-20/week vs. ~20/month) is a 4-5x gap that will surface in any competent behavioral screen. I recommended dropping this story; Reviewer D provides the specific interview failure mode that confirms why. This story should be retired, not compressed.

**Reviewer D — The fabricated pilot metrics must never appear:**
Agree absolutely. 15%, 3-8%, 4% — Danny confirmed these were thrown in. If these appear on a resume submitted to Google or Anthropic, they will be probed, and the interview ends. The approved bullets correctly retire them. This is a hard rule, not a preference.

**Reviewer E (Story Architect) — The ATLAS-to-LLM-paper origin story is the superpower:**
Agree, and this is the most important strategic insight in the entire board review. The connection between building the production system and then questioning whether it could be trusted is the narrative thread that turns two separate credentials into a single arc. I flagged this as a positioning gap; Reviewer E correctly identifies it as the brand itself. The resume currently presents these as unrelated line items. They are cause and effect.

**Reviewer F (Assembly Strategist) — Story 5 (ARB) should be retired from active rotation:**
Agree. Reviewer F and I reach the same conclusion from different angles — I from competitive positioning, Reviewer F from assembly logic. The story adds nothing that ABME doesn't cover better, and its defensibility problems make it a net negative.

**Reviewer G (Hiring Manager) — The "AB role eliminated nationwide" punchline is the most undersold line in the library:**
Agree completely, and I flagged this as an undersold strength. "Your analysis eliminated a job title" is organizational impact at a scale most senior DS candidates never see. The approved bullets gesture at it; none of them land the punch. This needs to be the explicit closing clause of the ABME bullet, not a parenthetical.

**Reviewer C (Recruiter/ATS) — SQL and Python are absent from approved bullets:**
Agree this is a real ATS gap. I flagged the missing Skills section as a positioning gap; Reviewer C correctly identifies the specific tokens that are missing. "Python" and "SQL" are among the most-filtered keywords in DS JDs and neither appears explicitly in the JPMC approved bullets. This is fixable with a compact Skills row.

---

## Disagreements

**Reviewer A — "Do not put a Summary/Objective section":**
I agree for most targets, but I'd carve out an exception for Dream Tier (Anthropic Fellowship specifically). A one-line research statement — "Research interests: agentic AI safety, LLM behavioral measurement, constrained optimization" — under Education signals intent in a way that a recruiter scanning for "alignment researcher" will respond to. This is not a traditional objective statement; it's a positioning signal for a specific audience. For Tier 1-2 targets, Reviewer A is correct. For Anthropic Fellowship, I'd reconsider.

**Reviewer B — "Impact-first construction works only when the reader already has context":**
Reviewer B argues the system description must precede the impact claim on a first-read cold resume. I partially disagree. The correct construction is: impact clause that implies the system, not impact clause that requires prior knowledge of the system. "Built an automated decision platform projected to unlock $9B in annual balance growth through net-neutral reallocation across 4,300+ branches" leads with impact AND describes the system in the same sentence. The reader doesn't need prior context — the sentence provides it. The failure mode Reviewer B identifies (dropping $9B before explaining what ATLAS is) is real, but the solution isn't always "system first, impact second." It's "write a sentence that does both."

**Reviewer C — Recommending "Mixed-Integer Linear Programming (MILP)" spelled out on first use:**
This is technically correct ATS advice but practically wrong for the target audience. At Google, Anthropic, and Stripe, a recruiter or hiring manager who sees "Mixed-Integer Linear Programming (MILP)" will recognize it as a candidate who doesn't assume the reader knows what MILP is — which is fine. But the parenthetical expansion costs space on a one-page resume and signals a level of explanation that senior technical audiences don't need. "MILP-based" is sufficient for the target companies. The ATS concern is real but secondary to the human reader experience at this level.

**Reviewer F — "SwagUp disappears entirely for Role Type A (OR/Applied Scientist)":**
I'd keep one SwagUp bullet even for OR/Applied Scientist targets. The reason is competitive positioning, not content quality. A resume with only JPMC and Georgia Tech projects reads as someone who has only ever worked in one environment. The SwagUp A/B test ($5M+, 40% revenue growth, policy change) demonstrates that Danny can identify and solve problems outside of a structured enterprise context. For Anthropic and OpenAI, intellectual range matters. One SwagUp bullet — the A/B test, tightly written — signals that range without consuming significant real estate. I'd drop it to one bullet, not zero.

**Reviewer G — "Currently a long shot, not a no" for Dream Tier:**
I'd push back slightly on the framing. "Long shot" implies the probability is low enough that Danny should deprioritize these applications. I'd say "reach, not a no" — and more importantly, the Anthropic Fellowship specifically is worth a dedicated application strategy, not just a resume submission. The Fellowship is explicitly designed for people who are building toward alignment research from non-traditional paths. Danny's profile — production system builder who questioned his own system and published the measurement — is closer to the Fellowship's stated intent than a typical PhD applicant who has only studied LLMs from the outside. The resume alone may be a long shot; a resume plus a strong research statement plus the ArXiv papers is a different conversation.

---

## Revisions to My Review

**Addition: The autonomous planner gap is more critical than I stated.**

Reviewer E identifies that the connection between ATLAS and the LLM paper is the brand, but neither Reviewer E nor I fully addressed the missing story: Danny *rebuilt ATLAS as an autonomous LLM agent* before writing the paper. This is not in any approved bullet. For AI lab targets, "built an autonomous resource-allocation agent on top of a production MILP system, then measured why natural-language control interfaces silently fail" is a single sentence that does more work than any two separate bullets about ATLAS and the LLM paper. This should be the Projects section framing for Story 16 — not "built a synthetic environment inspired by production expertise" but "rebuilt my production optimization system as an autonomous agent, then measured its failure modes."

**Addition: The Skills section gap is more severe than I originally stated.**

Reviewer C's audit reveals that Python and SQL — two of the most-filtered keywords in DS JDs — do not appear in any JPMC approved bullet. I flagged the missing Skills section as a positioning gap, but I understated the severity. This is not a nice-to-have; it's a potential ATS filter failure that could prevent the resume from reaching human eyes at all. The fix is a compact two-line Skills section: one line for languages/tools (Python, SQL, PuLP, XGBoost, PySpark, Streamlit, Snowflake, Looker, Fivetran), one line for methods (MILP, DiD, matched-pairs causal inference, A/B testing, propensity modeling, NLP). This section should appear between Experience and Projects.

**Revision: I underst