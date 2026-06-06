# Peer Reviewer — stage2

## Agreements

**Reviewer B — ε² additivity claim (Technical Flag 1)**
I agree this is the most technically imprecise claim in the paper. I flagged the 10:1 ratio as a key finding but did not adequately scrutinize whether two separate Kruskal-Wallis tests can be compared as a ratio implying joint variance decomposition. Reviewer B is right that the language "explains roughly 10 times more variance" implies a partition that the analysis does not perform. My original review noted the inversion across baseline ranges but did not flag the underlying methodological imprecision in how the ratio is presented. This needs correction in the abstract, results, and contributions list.

**Reviewer B — null baseline missing (Baselines section)**
Reviewer B correctly identifies that the no-context condition lacks a null/no-word control. If the model produces 0.50 for "Architects should spend more time on innovation" (no intensity word), then the lower-tier words are not functioning as intensity modifiers at all. I mentioned the 0.50 hedge finding as interesting but did not flag the absence of a null control as a confound. This is a genuine gap I missed.

**Reviewer C — prompt framing confound (Internal Validity)**
Reviewer C correctly notes that the no-context and context-conditioned prompts use different syntactic frames ("spend [WORD] more time" vs. "I would like to [WORD] increase"). I did not flag this. The word modifies a noun phrase in one condition and a verb phrase in another, which is a genuine confound that the paper does not acknowledge. For a measurement study claiming to isolate the word as the variable, this matters.

**Reviewer C — system prompt and tool schema missing (Reproducibility)**
I flagged the absence of exact prompt templates as a reproducibility gap, but Reviewer C goes further and correctly identifies the system prompt and tool schema as the most critical missing pieces. Tool-calling behavior in Claude is highly sensitive to both. I should have been more specific about what "prompt templates" means in this context.

**Reviewer F — "ordinal violation" label is problematic**
Reviewer F and Reviewer C both flag this, and I agree. I noted the *moderately* anomaly as underexplained, but I did not catch that labeling it an "ordinal violation" presupposes the researcher's ordering is ground truth. If the tier ordering is researcher-hypothesized, *moderately* mapping below *slightly* is evidence the ordering may be wrong for that word, not that the model violated a validated scale. The label should be "ordinal anomaly" or "unexpected ordering."

**Reviewer A — downstream consequences section should be reframed as validity check**
I called this the weakest section and recommended shortening it. Reviewer A makes the more precise point that it should be explicitly framed as confirming the instrument has consequential outputs — a validity check, not a fourth finding. This is a better framing than my recommendation to simply shorten it.

**Reviewer D (myself) — the drastically/dramatically asymmetry is the most novel finding**
All reviewers converge on this. I stand by this assessment and note it is consistently underexplained relative to its novelty.

---

## Disagreements

**Reviewer F — "the psycholinguistics framing has not landed"**
Reviewer F states the paper "reads as a behavioral study of an AI system" and that the psycholinguistics framing is not realized. I partially disagree. The framing does land at the level of abstract and introduction — the paper correctly situates itself relative to Cliff (1959), Quirk (1985), and vague quantifier literature, and the "language-to-action boundary" framing is coherent and consistent. What Reviewer F is really identifying is that the word "psycholinguistics" never appears in the paper, and that the framing could be made more explicit. That is a fair point about execution, not a fundamental failure of framing. The paper does not need to be a human-subjects study to be psycholinguistics-adjacent; it is studying the same construct (how intensity words map to magnitudes) using a different instrument. The framing is present but could be made more explicit — I would call this a refinement needed, not a framing failure.

**Reviewer B — missing citations (scalar implicature, Kennedy & McNally)**
Reviewer B flags the absence of Horn scales, scalar implicature literature, and Kennedy & McNally (2005) on gradable adjectives as significant gaps. I think this is a valid observation for a conference submission but is overcalibrated for an ArXiv preprint by a first-time author. The paper's stated scope is a measurement study, not a formal semantics paper. Adding these citations would strengthen the theoretical grounding but their absence does not undermine the empirical contribution. For ArXiv readiness, the current related work is adequate. For a venue submission, Reviewer B is right.

**Reviewer C — the three-task constraint as a hidden variable**
Reviewer C flags that the sum-to-100% constraint may be a confound because the model might be reasoning about disruption to other tasks. This is theoretically possible, but the paper's design (single tool call, single target task) makes this less likely to be a dominant confound than Reviewer C implies. The model is asked to set one allocation; whether it reasons about the other two tasks is speculative. I would flag this as worth acknowledging but not as a critical confound.

**Reviewer F — T=1.0 data collected but not included**
Reviewer F says "if it's collected, why not include it?" I think this is slightly unfair to the stated scope. The author explicitly frames this as a "first measurement slice" and notes the T=1.0 analysis will appear in a subsequent revision. Including partially analyzed data to satisfy a reviewer's expectation could weaken the paper if the analysis is not yet complete. The mention of collected data is a transparency signal, not a gap. That said, Reviewer F's point that it reads oddly in a preprint is fair — the sentence could be removed or moved to a footnote.

---

## Revisions to My Review

**What I missed:**

1. **The ε² additivity issue is more serious than I indicated.** I noted the 10:1 ratio as a well-reported finding and flagged the inversion across baseline ranges. But I did not identify that the ratio itself is methodologically imprecise — two separate KW tests cannot be compared as components of a variance partition. This should have been in my weaknesses list, not just a question for authors. I would now elevate this to a moderate weakness requiring correction before ArXiv submission.

2. **The null/no-word control is a genuine confound I missed entirely.** The paper cannot cleanly claim lower-tier words "hedge at 0.50" without showing that the no-word baseline produces something different. This is a one-cell addition that would substantially sharpen the paper's central claim about compression. I would add this to my Questions for Authors.

3. **The syntactic frame confound between conditions.** I noted the two conditions have different prompts but did not identify the specific syntactic difference (noun phrase vs. verb phrase modification) as a confound. This should be acknowledged in the paper's limitations.

4. **The "ordinal violation" label.** I noted *moderately* as underexplained but did not catch the labeling problem. I would add this to my minor issues.

5. **The Spearman ρ computation ambiguity.** Reviewer C correctly identifies that the paper does not specify whether ρ is computed over 10 medians or 300 individual observations. These produce different values and different p-values. I should have flagged this. I would add it to Questions for Authors.

**What I stand by:**

- My overall recommendation of Weak Accept for ArXiv remains appropriate. The additional issues raised by other reviewers are real but do not change the fundamental assessment: this is a competent first preprint with genuine empirical contributions that needs targeted fixes, not a fundamental redesign.
- My identification of the downstream consequences section as the weakest section is confirmed by multiple reviewers.
- My assessment that the boundary behavior finding (hedge/act/abstain) is the paper's most novel contribution is confirmed by all reviewers.
- My identification of the Quirk taxonomy framing as adequate-but-needing-one-more-sentence is confirmed by Reviewers A, B, and C.

**Revised weakness list additions:**
- The ε² ratio language implies a joint variance decomposition that the analysis does not perform (moderate weakness, requires correction)
- No null/no-word control in the no-context condition (genuine confound, should be acknowledged)
- Syntactic frame differs between conditions (confound not acknowledged in limitations)
- Spearman ρ computation method not specified (ambiguity in primary statistic)

---

## Blind Spots

Several issues appear in no review or only tangentially:

**1. The convergence figure (Fig. 3) non-monotonicity