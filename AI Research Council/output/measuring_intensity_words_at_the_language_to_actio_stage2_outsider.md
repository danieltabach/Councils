# Outsider / Red Team — stage2

# Reviewer A — Council Response

---

## Agreements

**Reviewer B (Experimental Design Assessment) — Confound: Prompt phrasing differs between conditions.**
Reviewer B correctly identifies that the no-context prompt ("Architects should spend [WORD] more time on innovation") and the context-conditioned prompt ("I would like to [WORD] increase innovation") are not the same syntactic frame. I flagged the no-context condition as underspecified but missed this specific confound. The word modifies a noun phrase in one condition and a verb phrase in the other. This is a genuine internal validity threat that I should have caught.

**Reviewer B — System prompt and tool schema not reported.**
I flagged this as a reproducibility gap but Reviewer B articulates it more precisely: tool-calling behavior in Claude is highly sensitive to system prompt content and tool schema definitions. This is the most critical reproducibility gap, and I agree it is more serious than I initially conveyed. My review mentioned it but understated its centrality.

**Reviewer C (Strengths #5) — The hedge/act/abstain finding is the paper's most novel contribution.**
I agree. The *drastically*/*dramatically* asymmetry at 89% is genuinely surprising and the paper's most defensible claim to novelty. I said this in my review but Reviewer C articulates it more cleanly.

**Reviewer C (Weakness #6) — ε² = 0.969 requires a caveat about near-zero within-word variance.**
I did not flag this specifically. Reviewer C is right: when many words produce identical outputs across all 30 runs, between-group variance dominates mechanically. The 0.969 figure is partly a design artifact, not purely a semantic finding. This is a real gap in my review.

**Reviewer D (Citation Issues) — BrittleBench (2026) is unverifiable.**
I did not examine citations at this level of detail. Reviewer D is correct that a 2026 reference with no full bibliographic entry cannot be verified by readers. This is a concrete ArXiv-readiness issue I missed.

**Reviewer E (Missing Sections #3) — Exact prompt templates must appear somewhere.**
I flagged that the no-context condition was underspecified, but Reviewer E makes the stronger and more actionable point: the exact prompt templates should appear in the paper or an appendix, not just paraphrases. This is the right framing of the reproducibility problem.

**Reviewer F (Technical Red Flag #1) — The ε² additivity claim is technically incorrect.**
This is the most important technical flag in all six reviews, and I missed it entirely. Reviewer F correctly identifies that comparing ε²_baseline = 0.782 and ε²_word = 0.079 from two *separate* Kruskal-Wallis tests as if they partition a joint variance is technically wrong. The "10:1 ratio" language implies a decomposition the analysis does not perform. This is a moderate-severity error that appears in the abstract, contributions list, and results section. I should have caught this.

**Reviewer F (Missing Related Work) — Scalar implicature and Horn scales.**
Reviewer F correctly notes that the compression finding (10 words collapsing to 5 regimes) connects directly to Horn scales and scalar implicature in formal pragmatics. The model treating *slightly*, *marginally*, *somewhat*, and *mildly* as equivalent may reflect linguistically principled scale structure rather than model failure. This is an important framing gap I missed entirely.

---

## Disagreements

**Reviewer C (Recommendation: Weak Accept) — I would rate this more cautiously.**
Reviewer C gives a "Weak Accept" and says the psycholinguistic framing "mostly" succeeds. I think the framing success is more partial than Reviewer C credits. The paper never uses the word "psycholinguistics." The introduction situates the work relative to psycholinguistic literature, but the Methods section reads as a systems paper and the Discussion introduces a third framing (AI alignment) that is not established in the introduction. For a paper whose stated goal is to be read as a psycholinguistic measurement study, this is a more significant framing failure than "mostly successful." I would say the framing is "partially successful in the abstract and introduction, but leaks in the methods and discussion." This doesn't change my ArXiv readiness verdict (I also think it's ready with minor revisions), but the framing assessment differs.

**Reviewer B (Weakness: Single-direction design) — Framed as "significant constraint" but not a blocking issue.**
Reviewer B calls the increase-only design "a significant constraint" and says the paper should be careful not to imply generality of the mode-switching finding. I agree with the substance but not the severity framing. The paper explicitly acknowledges this limitation in both the Limitations and Future Work sections. For a stated "first measurement slice," an increase-only design is a reasonable scope constraint, not a flaw. Reviewer B's concern is valid but I think the paper's existing acknowledgment is adequate for a preprint.

**Reviewer F (Alternative Approaches — chain-of-thought condition) — Valuable but not a gap for this paper.**
Reviewer F suggests the author should have prompted the model to explain its reasoning before acting. This would be informative, but it changes the experimental condition: a model that must articulate its reasoning may behave differently from one that acts directly. For a paper measuring the action output specifically, adding a reasoning step is a different experiment, not a missing control. I'd frame this as future work rather than a design gap.

---

## Revisions to My Review

**Addition 1: The ε² additivity problem (from Reviewer F).**
This is the most significant thing I missed. My original review flagged the multiple-comparison issue but did not identify that the "10:1 variance ratio" framing is technically imprecise. Two separate Kruskal-Wallis tests do not produce additive ε² values that partition a joint variance. The paper should reword this throughout: instead of "starting allocation explains roughly 10 times more variance than word choice," it should say something like "a Kruskal-Wallis test grouping by baseline yields ε² = 0.782; a separate test grouping by word yields ε² = 0.079; these are not additive but suggest baseline grouping captures far more rank-based structure." This is a moderate fix, not a minor one, and it affects the abstract, the contributions list, and the results section.

**Addition 2: Scalar implicature connection (from Reviewer F).**
I flagged undefined jargon from linguistics but missed the substantive theoretical gap: the compression finding may reflect Horn scale structure rather than model limitation. The paper should acknowledge this in Related Work or Discussion. Without it, the paper risks presenting as a "model failure" something that may be a linguistically principled behavior.

**Addition 3: The syntactic frame confound (from Reviewer B).**
I noted the no-context condition was underspecified but missed that the two conditions use different syntactic frames. This should be added to my Logical Gaps section. The word modifies "more time" (noun phrase) in the no-context condition and "increase" (verb) in the context condition. This is a genuine confound that the paper does not acknowledge.

**Revision to my Unconvincing Arguments #5 (multiple comparisons):**
I said the issue was "more serious than acknowledged" but did not specify where the most serious instance is. Based on Reviewer F and Reviewer C's more precise analyses, the split-range variance decomposition (the 65.3%/12.5%/88.0%/6.5% figures) is the most problematic: it is a post-hoc analysis with a researcher-chosen split point, and the specific numbers are presented without flagging their exploratory nature. My original review was correct in direction but insufficiently specific.

**Strengthening my Gap 1 (the 0.50 hedge):**
Reviewer F adds a point I missed: the paper does not test a null/no-word control. If the model produces 0.50 even with no intensity word at all, then the lower-tier words are not functioning as intensity modifiers — they are producing the same output as no instruction. This is a one-cell addition that would sharpen the hedge interpretation substantially. I should have caught this as a missing control.

**Standing by my Gap 2 (the variance ratio framing):**
My original concern — that the 10:1 ratio could reflect sensible context-sensitive behavior rather than instability — is confirmed and strengthened by Reviewer F's technical flag. The paper does not distinguish between "the word means different things" and "the word means the same thing but that meaning is inherently relative to context." This remains an unresolved logical gap.

---

## Blind Spots

After reviewing all six reviews, I believe the following points are absent from all reviews, including my own:

**1