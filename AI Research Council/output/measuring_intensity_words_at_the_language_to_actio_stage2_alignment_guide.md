# Alignment Guide — stage2

# Reviewer A — Council Response

## Agreements

**Reviewer B — ε² additivity claim (Technical Red Flag 1).** I agree this is more serious than I flagged it. I noted the issue briefly ("the two ε² values are not from the same test") but did not call it out as the paper's most technically imprecise claim. Reviewer B is right that the language "starting allocation explains roughly 10 times more variance than word choice" implies a joint variance decomposition that the analysis does not perform. This appears in the abstract, the contributions list, and the results section. My original review was too gentle here — I said the finding was "correct" while the framing was imprecise. The framing needs to be corrected in all three locations, not just noted as a caveat.

**Reviewer B — Spearman ρ circularity needs to be more explicit in Results (not just Methods).** I flagged this, but Reviewer B correctly identifies that the reminder needs to appear in Section 4.1 where ρ = 0.845 is first reported, not only in the Methods footnote. I agree the current placement is insufficient.

**Reviewer C — The "moderately" ordinal violation label is problematic.** I flagged this as scope drift in the Discussion but did not identify the deeper issue: labeling it an "ordinal violation" presupposes the researcher's ordering is ground truth. Reviewer C and Reviewer D both make this point more sharply than I did. The label should be "ordinal anomaly" or "unexpected ordering," and the interpretation should acknowledge that the researcher's tier placement of *moderately* may simply be wrong, not that the model is wrong.

**Reviewer D — Prompt templates and system prompt are missing (reproducibility gap).** I flagged this as the most significant reproducibility gap, and Reviewer D's systematic reproducibility assessment confirms and extends it. The tool schema, system prompt, default state definition, and the names of the other two tasks are all missing. I agree this is the single most important pre-submission fix beyond the statistical framing issues.

**Reviewer E — BrittleBench (2026) citation is unverifiable.** I did not flag this at all. Reviewer E is correct that a 2026 citation with no full bibliographic entry cannot be verified by readers. This needs a complete citation with arXiv ID or venue details.

**Reviewer F — ε² = 0.969 in no-context condition needs a caveat.** I mentioned this briefly ("the high value is partly a consequence of the near-zero variance in the lower-tier words") but did not recommend adding an explicit caveat in the text. Reviewer F correctly identifies this as a weakness in the statistical presentation that should be addressed directly.

**Reviewer F — Section 4.4 (Downstream Consequences) is the weakest section.** I flagged this as scope drift and recommended shortening. Reviewer F agrees and adds a useful suggestion: show whether the dollar spread varies across baselines. I endorse both the diagnosis and the suggested fix.

**Reviewer C — No null/no-word control.** I listed this under Missing Sections as "no explicit statement of what the paper does NOT claim," but I did not identify the specific missing cell: what does the model output with no intensity word at all? Reviewer C and Reviewer B both identify this as a meaningful gap that would sharpen the "hedge at 0.50" interpretation. I should have flagged this explicitly.

---

## Disagreements

**Reviewer B — Missing related work (scalar implicature, Kennedy & McNally, etc.).** Reviewer B argues the paper is missing engagement with Horn scales, scalar implicature, gradable adjectives (Kennedy & McNally 2005), and Bayesian pragmatics (Lassiter & Goodman 2017). I disagree that these omissions are within my mandate to evaluate, but more substantively: for a first preprint by a sole author at this stage, requiring engagement with formal semantics literature goes beyond what the paper promises. The paper frames itself as a measurement study informed by Quirk's taxonomy, not as a contribution to formal degree semantics. The Related Work section covers the three relevant areas it promises to cover. Expanding to scalar implicature would be appropriate for a journal version but is not a gap that prevents ArXiv readiness. I stand by my original assessment that the Related Work is adequate for the stated scope.

**Reviewer C — "The framing as a psycholinguistics paper has not landed."** Reviewer C argues the paper reads as a behavioral study of an AI system, not a psycholinguistic measurement study, and notes the word "psycholinguistics" never appears. I partially disagree. The paper's framing goal — as stated in the author's brief — is that tool calling is the instrument and word interpretation is the subject. This framing does land in the abstract and introduction. The absence of the word "psycholinguistics" is a deliberate choice, not a failure: the paper is psycholinguistics-adjacent, not a psycholinguistics paper proper (which would require human subjects). Reviewer C's point that the framing could be made more explicit is valid, but the claim that it has "not landed" overstates the problem. The paper successfully avoids reading as a tool-calling paper, which is the primary framing goal.

**Reviewer D — "The paper should not say 'vague language is compressed' as a general claim about LLMs."** Reviewer D argues the abstract's closing sentence ("Vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries") reads as a general claim. I partially disagree with the severity of this concern. The sentence uses "is" not "are generally" or "will be," and the paper's consistent single-model framing throughout provides adequate context. However, I agree with the direction: adding "in this model and context" or equivalent qualification to the abstract's closing sentence would be a small fix that preempts a legitimate objection. I should have flagged this more explicitly in my original review.

**Reviewer B — "The split-range decomposition is post-hoc with a researcher-chosen split point."** Reviewer B flags the 25%/32% split as chosen after seeing the data. I agree this is worth noting, but I disagree that it requires more than a one-sentence acknowledgment. The split is visually obvious from Figure 3 (the convergence is clearly non-linear with a transition around 25–32%), so calling it "post-hoc" is technically accurate but somewhat misleading — the split point is not arbitrary. The paper should note it as exploratory, which is a small addition.

---

## Revisions to My Review

**Addition: The ε² additivity issue is more serious than I stated.** My original review noted the issue but called it a "framing" problem. I should have flagged it as a technical precision problem that affects the abstract, the contributions list, and the results section simultaneously. The fix is not just rewording one sentence — it requires consistent correction across three locations. I revise my assessment: this is the highest-priority fix in the paper, equal to the prompt template reproducibility gap.

**Addition: The null/no-word control is a missing section I should have identified.** I listed "no explicit statement of what the paper does NOT claim" as a missing section, but I missed the more specific and actionable gap: there is no null condition (no intensity word). Without it, the "hedge at 0.50" interpretation cannot be distinguished from "0.50 is the model's default for this task regardless of instruction." This should be added to my Missing Sections list as a concrete gap.

**Addition: The "ordinal violation" label in Figure 2b.** I noted the *moderately* anomaly in my Scope Drift section but did not flag the specific label in the figure caption as problematic. The annotation "Ordinal violation" in Figure 2b presupposes the researcher's ordering is ground truth. This should be changed to "Ordinal anomaly" or "Unexpected ordering" in both the figure and the surrounding text.

**Strengthening: Multiple comparison acknowledgment.** My original review said the acknowledgment was "adequate for a preprint" but recommended adding one sentence to the statistical methods section. Reviewers B, C, D, and F all flag this independently. The convergence of four reviewers on this point suggests my original assessment was too lenient. I revise: the absence of an explicit multiple-comparison statement in Section 3.5 (not just in the Discussion limitations) is a gap that should be fixed before ArXiv submission, not after.

**Standing by: ArXiv readiness verdict.** Despite the additional issues raised by other reviewers, I maintain that the paper is ArXiv-ready with the fixes identified. The core alignment between stated goals and delivered content is strong. The issues raised are real but are all fixable without new experiments. My original verdict stands.

---

## Blind Spots

**All reviewers missed: The "Tier 3" partial-context condition naming creates a structural confusion that is never resolved.** The paper uses "