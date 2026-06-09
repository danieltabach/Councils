# Source Auditor — stage2

Now I have confirmed the key facts I need. Let me produce the full cross-council response.

---

# Reviewer F — Cross-Council Response

## Agreements

**Reviewer A — The ε² comparison structural problem.** I agree fully. Reviewer A correctly identifies that the 10:1 ratio is the paper's central quantitative claim and that it rests on two *separate* Kruskal-Wallis tests rather than a joint model. My original audit flagged this, but Reviewer A articulates the precise statistical remedy (a two-way Kruskal-Wallis or mixed-effects model with an interaction term) more crisply than I did. The interaction *is* the story, and the current framing doesn't test it. This is a genuine structural gap, not a disclosure issue.

**Reviewer A — The drastically/dramatically discontinuity is underanalyzed.** Reviewer A notes this is the paper's most alignment-relevant finding and gets one paragraph. I agree. My original audit flagged that the "as much as possible" interpretation for *drastically* is a post-hoc, untested claim. Reviewer A goes further by noting the model's actual text responses during abstention are available data that the author hasn't analyzed. This is correct and important: the abstention text is the most direct evidence for or against the proposed mechanism, and its absence is a reproducibility and evidentiary gap I should have flagged more prominently.

**Reviewer B — The no-word control is a structural gap, not a nice-to-have.** Reviewer B's framing is sharper than mine: this is not a "hole to patch" but the falsification condition for the paper's most prominent interpretive claim. I agree. At 30 runs × 2 temperatures = 60 API calls, its absence is hard to justify on cost grounds. My original audit noted this gap but understated its centrality to the hedge interpretation.

**Reviewer B — The $250K figure is rhetorically overloaded.** I agree with Reviewer B's specific suggestion: the point about propagation could be made more defensibly by staying in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars. The dollar figure will be extracted from context by non-technical readers and cited as a real-world consequence. My original audit flagged this but did not offer the cleaner alternative framing Reviewer B provides.

**Reviewer C — The inversion finding (5:1 → 14:1) is buried and should be in the abstract.** This is correct and I missed it entirely. Reviewer C identifies that the complete reversal of word-vs-state dominance across the allocation range is arguably more operationally important than the overall 10:1 ratio, yet it appears only in Section 4.2 and not in the abstract or conclusion. This is a genuine alignment gap between what the paper delivers and what it advertises. I should have caught this.

**Reviewer C — The "hedge" language in Discussion is inconsistent with Future Work's epistemic honesty.** Reviewer C correctly notes that the Discussion uses "hedge" as settled language while Future Work correctly flags it as unconfirmed. This is an internal consistency issue I flagged in my original audit, but Reviewer C's proposed fix — "appears to function as a hedge" rather than "functions as a hedge" — is the right one-word correction.

**Reviewer D — The abstention operationalization conflates two distinct behaviors.** Reviewer D identifies that "zero tool calls" could mean constraint-aware refusal *or* other non-action behaviors, and the paper uses "typically" to characterize the abstention responses without coding them. This is a construct validity issue I did not raise and should have. It directly affects the interpretability of the 121/300 abstention figure at 89%.

**Reviewer D — The independence violation is more serious than acknowledged.** Reviewer D correctly notes that at T=0.0, four words produce the *exact same value* across all 30 runs — these are not 30 independent observations but one observation repeated 30 times. The effective sample size for the no-context T=0.0 Spearman ρ is closer to 10 (one median per word) than 300. My original audit flagged the independence issue but did not quantify how severely it affects the no-context ρ specifically.

**Reviewer E — The "ordinal anomaly" framing for *moderately* is epistemically fragile.** Reviewer E correctly notes that calling *moderately* an "anomaly" presupposes the researcher's tier assignment is correct. The model's behavior (0.45) might be the accurate reflection of how humans use the word. Without the human baseline, "anomaly" is the wrong word. My original audit made this point but Reviewer E's framing — "the model's output for *moderately* falls below the researcher's hypothesized position" — is more precise and less loaded.

---

## Disagreements

**Reviewer A — "The paper should either not report [ε² = 0.969] or replace it with a more appropriate measure."** I partially disagree. The paper already explicitly flags the inflation ("This effect size is partly inflated by the deterministic decoding condition") and explains why. Removing the statistic would lose information; replacing it with only the count of distinct medians (which the paper also reports as 5) would be less informative about the degree of between-group separation. The better fix is to keep the statistic but move the inflation caveat from a parenthetical to a more prominent position — perhaps immediately after the number rather than two sentences later. Suppression is not the right remedy for a disclosed limitation.

**Reviewer A — Recommending the decrease condition be included in this paper rather than future work.** Reviewer A argues this is a "missed opportunity that reviewers will notice." I disagree that this rises to a paper-level deficiency. The paper is explicitly scoped as a "first measurement slice." Adding a decrease condition without a clear a priori hypothesis about asymmetry would expand scope without proportionate gain. The paper's existing scope is coherent; the decrease condition belongs in a second study where asymmetry can be the primary research question, not an afterthought appended to this one.

**Reviewer B — "Weak Accept" for a workshop venue.** My assessment is slightly more conservative. The missing no-word control and the unvalidated word scale together mean the paper's central interpretive claim (compression as a meaningful failure, not a default) is currently unfalsified. For a workshop venue focused on empirical findings, this is acceptable with revision; for a main track, it is not. I would rate this "Conditional Accept for workshop, Revise and Resubmit for main track," which is functionally similar to Reviewer B's verdict but with a stronger emphasis on the no-word control as a pre-acceptance requirement rather than a post-acceptance extension.

**Reviewer E — "The differentiation funnel may be trivially expected from the constraint structure."** Reviewer E argues that convergence near 89% might simply follow mathematically from the constraint: if you're at 89%, any increase instruction can only go to ~91% regardless of word. This is a fair alternative explanation for the *convergence* finding, but it does not explain the *abstention* finding — which is the more striking result. The model doesn't just produce small increases near 89%; it *refuses to act at all* for some words while acting for others. That word-dependent categorical switching is not a mathematical consequence of the constraint. Reviewer E's critique applies to the differentiation funnel but not to the boundary mode-switching finding, and the paper should be clearer about which claim each piece of evidence supports.

---

## Revisions to My Review

**What I missed and would add:**

**1. The Mosteller & Youtz page range issue is more complex than I stated.** My original audit flagged the bibliography entry as truncating the page range (pp. 2–12 rather than 2–34). The search results now confirm this is genuinely ambiguous: the Project Euclid canonical record lists the article as 5(1): 2-12, while the Stanford-hosted PDF and the Harvard repository both cite the volume as 1990, Vol. 5, No. 1, 2-34. The discrepancy appears to reflect the difference between the article itself (pp. 2–12) and the full issue section including comments and rejoinder (pp. 2–34). The comments run from pp. 13–30 and the rejoinder from pp. 31–34. The paper's bibliography entry of "pp. 2–12" is therefore *correct* for the article itself, and my original citation issue flag was wrong. I retract it.

**2. The Mosteller & Youtz "high variance