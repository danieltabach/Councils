# Devil's Advocate — stage2

# Advisor B — Post-Council Response

---

## Agreements

**Advisor E (Skeptical PI) — "You're underselling one thing and overselling another."**
This is the most precise diagnosis in the entire council. E correctly identifies that the boundary abstention finding is the genuine contribution and the compression finding is the expected one. I made this point but less sharply. E's framing — "the compression stuff is context; the boundary behavior is the finding" — is the clearest single sentence in all six reviews and Daniel should tattoo it somewhere visible.

**Advisor C (Research Sequencing) — Three-paper arc structure.**
The sequencing logic is sound. Paper 2 = cross-model replication, Paper 3 = domain/stakes sensitivity. I agree with this ordering and the reasoning behind it. Don't build the stakes study before you've established the phenomenon generalizes. C is right.

**Advisor F (Field Cartographer) — "The action/estimation distinction is the moat."**
F correctly identifies that the critical differentiator from the verbal probability literature (Zhang 2024, Mosteller 1990) is that Daniel is measuring *action execution* not *probability estimation*. This is the claim that needs to be defended aggressively and explicitly in every submission. I mentioned it but F articulates it more precisely.

**Advisors A, C, D, E (unanimous) — Cross-model comparison is the highest-priority next step.**
The council is unanimous here. I agree. This is not a controversial call.

**Advisor D — Prolific cost estimate (~$133 for 100 participants).**
D did the actual math on Prolific costs. I said "cheap" without quantifying it. D's specific numbers ($1/participant + 33% fee = ~$1.33, 100 participants = ~$133) are useful and within Daniel's stated budget. This is a concrete correction to my vague treatment of the IRB cost question.

---

## Disagreements

**Advisor A — "Your most realistic targets for August 2025 submission."**
A's timeline is confused. The paper is dated May 2026. The author is targeting NeurIPS 2026 workshops, not 2025. A's entire venue section references 2025 deadlines that have already passed. This is a significant error in a strategic review. D correctly identifies NeurIPS 2026 with an August 29, 2026 suggested deadline. Daniel should use D's timeline, not A's.

**Advisor C — "Do NOT target NeurIPS main track yet. Workshop is the right bar for this stage."**
I agree with the conclusion but C states this without acknowledging that NeurIPS workshops have also become substantially more competitive in 2024-2026. Several NeurIPS workshops now have acceptance rates in the 25-35% range with hundreds of submissions. "Workshop" is not a soft landing. Daniel needs to know this going in, not discover it at rejection.

**Advisor D — OpenAI Safety Fellowship framing.**
D references an OpenAI Safety Fellowship running "September 14, 2026 through February 5, 2027." I cannot verify this program exists as described, and D's citation pattern in this section is suspiciously specific in ways that suggest hallucination risk. Daniel should independently verify any fellowship program before investing application time. Do not take D's fellowship list at face value without checking primary sources.

**Advisors A and C — Recommending GPT-4o-mini and Gemini Flash as "cheap frontier models."**
Both advisors recommend these for cross-model comparison. I'd push back harder: GPT-4o-mini and Gemini Flash are not the same class of model as Claude Haiku. Comparing a small Anthropic model to a small OpenAI model and a small Google model gives you cross-vendor comparison, but it confounds model size, training data, RLHF procedure, and architecture simultaneously. You can't isolate what's driving differences. The cleaner scientific move is to compare within a model family (Haiku vs. Sonnet vs. Opus, or Llama 8B vs. 70B) to isolate scale effects, AND across families (Llama vs. Mistral vs. Haiku) to test generalization. The council is treating "cross-model" as monolithic when it's actually two different experiments with different inferential value.

**Advisor E — "Do NOT pursue the valence/stakes manipulation, the stakeholder persona manipulation, or the mechanistic interpretability route right now."**
E is right about mech interp. E is wrong about the valence study. The stakes/domain manipulation is not just "a different paper" — it's the paper that makes this work safety-relevant rather than just behaviorally interesting. If Daniel's goal is to reach frontier AI labs, a paper that shows "the model's action policy changes when the stakes framing invokes human welfare" is directly relevant to Anthropic's safety team in a way that "here's the cross-model replication" is not. E's conservatism here is appropriate for academic sequencing but suboptimal for career positioning.

---

## Revisions to My Review

**What I missed: The ε² ratio is partially a design artifact, and I didn't push hard enough on this.**

I said the state-dominance finding (ε²_baseline = 0.782 vs. ε²_word = 0.079) is "a consequence of your experimental design, not a discovery about language models" because including an 89% ceiling condition mechanically forces convergence. I stand by this challenge, but I understated the correct response to it.

The correct response is not to remove the 89% condition — it's to report the split-range analysis (which Daniel already has in the paper: word dominates at low baselines 5:1, context dominates at high baselines 14:1) as the *primary* result, and the aggregate 10:1 ratio as a summary statistic. The split-range inversion is the more interesting and defensible finding. The aggregate ratio is the one that's vulnerable to the design-artifact critique. I should have been clearer about which number to lead with.

**What I missed: The no-word control is more important than I indicated.**

I mentioned it briefly. Advisor E correctly elevates it. Without a no-word control ("increase innovation" with no intensity modifier), you cannot distinguish "the model hedges at 0.50 because weak words mean 0.50" from "the model defaults to 0.50 for any increase instruction." This is not a minor gap — it's a threat to the central interpretive claim about what the 0.50 hedge means. This is a $2-3 API cost fix that closes a major hole. I should have led with it.

**What I missed: The drastically/dramatically divergence is your single most citable finding.**

I identified the three-mode behavior as the strongest finding. But I didn't sharpen it to its most pointed form: *drastically* and *dramatically* are near-synonyms by any standard linguistic analysis, yet they produce categorically different behavior (7% abstention vs. 97% abstention) at identical system states. This is not a compression finding — it's an anti-compression finding. The model is making a categorical distinction that humans would not reliably make. That's a more surprising and publishable result than anything else in the paper. Every submission should lead with this specific contrast, not the general three-mode framework.

**What I would change in my original framing of IRB:**

I was too aggressive in pushing Path 3 (reframe to avoid human comparison entirely) and not concrete enough about the Prolific cost. D's specific numbers ($133 for 100 participants) and the exempt determination pathway are more actionable than my general "reframe it." I'd now recommend: do Path 3 for the NeurIPS workshop submission, simultaneously submit an exempt determination request to GT IRB (20-minute task), and if exempt status comes through before submission, add a small Prolific study as a supplementary result. Don't wait for IRB to submit; use it to strengthen the follow-up version.

---

## Blind Spots

**All advisors missed: The replication crisis problem specific to this paper.**

Daniel's paper runs 30 trials per cell at T=0.0 and T=0.7. The paper itself acknowledges that p-values "overstate significance" because runs within the same word are not independent. No advisor pushed hard enough on what this means for the cross-model comparison paper. When you run the same 30-trial protocol on Llama 3.1 8B and find "similar compression patterns," how do you know the similarity is real and not an artifact of the discrete output space both models share? If both models are constrained to output values like 0.50, 0.60, 0.65, 0.70 because those are the natural round-number anchors in the training data, you'll see "similar compression" regardless of whether the underlying mechanism is the same. The cross-