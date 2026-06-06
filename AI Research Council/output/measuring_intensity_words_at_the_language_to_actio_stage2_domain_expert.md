# Domain Expert — stage2

## Agreements

**Reviewer A — System prompt and tool schema absence (Critical reproducibility gap)**
I agree strongly. Reviewer A correctly identifies this as the most significant reproducibility concern. My original review flagged the confound between prompt phrasing and word choice, but I understated the severity of the missing system prompt and tool schema. In a tool-calling context, the tool description is part of the model's effective input. Without it, the experiment cannot be replicated. This is more critical than I initially emphasized.

**Reviewer A — The "ordinal violation" label for *moderately***
I agree with Reviewer A's suggestion to replace "ordinal violation" with "ordinal anomaly" or "unexpected ordering." My original review made the same point but less directly. The label implies the researcher's ordering is ground truth, which it is not. This is a framing fix that costs nothing.

**Reviewer C — The 0.50 hedge interpretation is asserted, not demonstrated**
Reviewer C correctly identifies that 0.50 could be the model's prior for a balanced equal-split allocation (33%/33%/34% default) rather than a hedge. My original review noted the "hedge" framing as speculative but did not articulate this specific alternative as clearly. The null/no-word control that Reviewer B (myself) recommended would directly test this, but Reviewer C's framing of the alternative hypothesis is sharper than mine.

**Reviewer C — Gap 2: variance ratio does not imply context-invariant word meaning is unstable**
This is a genuine logical gap I missed. The 10:1 variance ratio is consistent with the word having a *stable relative meaning* (e.g., "add X% of available headroom") rather than an unstable absolute meaning. The paper conflates these two interpretations. The finding could reflect sensible context-sensitive behavior rather than semantic instability.

**Reviewer D — BrittleBench (2026) citation is unverifiable**
I did not flag this in my original review. Reviewer D is correct that a 2026 citation with no full bibliographic entry cannot be verified. For a preprint, this is a credibility issue.

**Reviewer E — ε² = 0.969 caveat needed**
I agree with Reviewer E's point that the near-zero within-word variance at T=0.0 mechanically inflates ε². When many groups have zero variance, between-group variance dominates trivially. My original review flagged the ε² additivity claim as the primary technical error but did not separately address this inflation issue. Both problems need fixing.

**Reviewer F — Downstream consequences section should be framed as validity check, not finding**
I agree. My original review called this section "the weakest section" but did not articulate the correct reframing. Reviewer F's suggestion — frame it as confirming the instrument has consequential outputs — is the right fix.

---

## Disagreements

**Reviewer E — "Weak Accept for ArXiv" framing**
Reviewer E gives a "Weak Accept" and describes the paper as "ready for ArXiv with minor revisions." I think this understates the severity of two issues. First, the ε² additivity problem (comparing two separate KW test outputs as if they partition variance) is not a minor revision — it affects the abstract, the contributions list, and the headline finding. The "10:1 ratio" language as currently written is technically incorrect as a variance decomposition claim, not merely imprecise. Second, the missing system prompt and tool schema are not minor omissions for a paper whose central claim is about how word choice affects model output. These are the two most significant technical gaps, and calling them "minor" undersells the work needed.

**Reviewer C — "The framing as psycholinguistics has not landed"**
Reviewer C argues the paper reads as a behavioral study of an AI system, not a psycholinguistics paper. I partially disagree. The framing question is whether the paper reads as studying *word interpretation* (psycholinguistics-adjacent) versus *system behavior* (AI systems). I think the paper mostly succeeds at the former — the abstract, introduction, and conclusion consistently foreground the word-interpretation question. The Methods section does slip into systems language, but this is a localized problem, not a global framing failure. Reviewer C's critique is valid for the Methods section specifically but overstated as a global assessment.

**Reviewer A — "Confound: prompt phrasing is not isolated from word choice"**
Reviewer A flags that the no-context prompt uses the word as a noun modifier ("more time on innovation") while the context prompt uses it as a verb modifier ("increase innovation"). This is a real confound, but I think Reviewer A overstates its severity. The paper is not claiming that the syntactic frame is held constant — it is claiming that the word is the only variable *within each condition*. The two conditions are explicitly different measurement regimes, not two instances of the same measurement. The confound would matter if the paper were claiming to isolate word semantics from syntactic context across conditions, but it is not making that cross-condition comparison as a primary claim. This should be acknowledged but is not a fatal flaw.

**Reviewer D — Round-number anchoring observation is "consistent with the data shown"**
Reviewer D accepts the round-number anchoring observation as visually consistent with Figure 4. Looking at the delta heatmap more carefully: at b=18%, the deltas for booster-class words are 0.164 (not round); at b=32%, they are 0.138 (not round); at b=53%, they are 0.094 (not round). But at b=25%, *drastically* shows 0.250 (round), and at b=50%, the deltas are 0.100 (round). The pattern is mixed. The observation is weaker than the paper implies, and Reviewer D's endorsement of it as "consistent" is slightly too generous. The paper's own hedge ("preliminary, visual inspection") is appropriate, but the observation should not be cited as even a preliminary finding without more systematic analysis.

---

## Revisions to My Review

**Strengthening the ε² additivity point (Flag 1)**
My original review correctly identified this as the most technically imprecise claim. After seeing other reviews, I want to be more specific about what the fix requires. The paper needs to change three locations: (1) the abstract ("starting allocation explains roughly 10 times more variance than word choice" → "two separate Kruskal-Wallis tests show that baseline grouping captures far more rank-based structure than word grouping, with ε² values of 0.782 and 0.079 respectively"); (2) the contributions list (same reframing); (3) the results section (add explicit statement that these are not additive components of a joint decomposition). This is not cosmetic — it is the paper's primary quantitative claim and it is currently stated in a way that implies a statistical procedure that was not performed.

**Adding the logical gap Reviewer C identified**
I missed the distinction between "word meaning is unstable" and "word meaning is stably relative." The paper's interpretation of the 10:1 ratio as evidence that "the same word cannot be treated as having a context-invariant numeric meaning" is not the only interpretation. A word that means "add X% of available headroom" has a context-invariant meaning that produces context-variant outputs. The paper should acknowledge this alternative interpretation explicitly.

**Elevating the no-word control recommendation**
My original review recommended a null/no-word control as a missing baseline. After seeing Reviewer B's (my own) and Reviewer C's convergent concern about the 0.50 hedge interpretation, I want to elevate this from a recommendation to a near-requirement for the paper's central interpretive claim. The hedge interpretation is the paper's main mechanistic story for the no-context compression finding, and it is entirely untested. Without a null control, the paper cannot distinguish "0.50 is the hedge value" from "0.50 is the model's default allocation for this task regardless of instruction."

**Revising the impact assessment**
My original review called the abstention finding "the most impactful" result. I stand by this, but I want to add: the *drastically*/*dramatically* asymmetry at the boundary is also the finding most vulnerable to being a model-specific artifact. Two words that humans might treat as near-synonyms diverging completely at one boundary value is striking, but it could reflect something idiosyncratic about how Claude Haiku was trained rather than a general property of LLM word interpretation. The paper should flag this more explicitly.

**On the T=0.0 non-determinism**
My original Flag 2 noted this. After reviewing Figure 6 (the temperature comparison heatmap), I can see that at T=0.0, *considerably* splits 11/19 between 0.60 and 0.65, *substantially* splits 20/10, and *significantly* splits 5/