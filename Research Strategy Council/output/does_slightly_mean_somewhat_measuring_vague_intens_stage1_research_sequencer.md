# Research Sequencer — stage1

# Research Sequencer Advisory: Strategic Review

## Bucket A vs. Bucket B Assessment

The author's split is approximately right but has two miscategorizations worth correcting.

**The split is correct in spirit.** Bucket A (human baseline, cross-model, denser grid) builds the empirical foundation. Bucket B (valence framing, stakes magnitude, cross-domain transfer) stakes claims about what the phenomenon means. You cannot credibly stake claims without the foundation. The instinct to separate them is sound.

**Miscategorization 1: Cross-model belongs in Bucket B, not Bucket A.**

This is the most important correction. Cross-model comparison feels like a credibility move because it looks like replication — "does this hold across models?" But strategically, it functions differently. If you find that GPT-4o and Gemini Flash show the *same* compression pattern, you've made a claim about the universality of the phenomenon, which is a field-defining move. If you find they differ, you've made a claim about how training and alignment shape vague-language interpretation — also field-defining. Cross-model is not a replication study; it's a theoretical claim about whether this is a property of the model class or a property of the language-action interface itself. Running it second, before you have a human baseline, means you're comparing models to each other without an anchor. That's a weaker paper than it could be.

Cross-model should be Paper 3, after the human baseline establishes the anchor.

**Miscategorization 2: The denser baseline grid is not Bucket A credibility — it's infrastructure.**

The denser grid isn't a publishable paper on its own. It's data collection that enables other papers. Treat it as a resource investment that runs in the background, not as a paper in the sequence. If you collect it while executing Paper 2, you have it available for Paper 3 without it consuming a publication slot.

**Miscategorization 3: The valence 2x2 is not cleanly Bucket B.**

The author frames valence (increase vs. decrease) as a field-defining move. I'd push back. Testing decrease instructions is a direct, obvious extension of Paper 1 — the paper itself flags it as a limitation. Asymmetry between increase and decrease is a credibility-building result, not a field-defining claim. It belongs in Bucket A. The *framing* of valence as a safety-relevant phenomenon is Bucket B, but the empirical test itself is Bucket A.

**Revised Bucket Structure:**

- **Bucket A (credibility):** Human baseline survey, valence asymmetry (increase vs. decrease), denser grid (as infrastructure), no-word control
- **Bucket B (field-defining):** Cross-model comparison (after human anchor), cross-domain transfer, stakes magnitude framing
- **Reclassified:** Cross-model moves from A to B; valence moves from B to A

---

## Recommended Sequence (Next 3-5 Papers)

### Paper 2: Human Baseline + Valence Asymmetry (Combined Study)

**Why first:** The paper's single most damaging limitation is the absence of a human comparison. Every reviewer who reads Paper 1 will ask: "But do humans do the same thing?" You cannot answer the question "is this model failure or genuine linguistic ambiguity?" without this data. Until you answer it, every subsequent paper is built on an unstable foundation.

The strategic move is to combine the human baseline with the valence extension (decrease instructions) in a single study. Here's why combining is correct: both require the same word scale, the same task framing, and the same statistical apparatus. Running them separately wastes a publication slot on what would be a thin paper. Together, they produce a paper with two genuine contributions: (1) the human-model comparison that closes the ordinality validation gap, and (2) the asymmetry result that extends the phenomenon to a new action direction. This is a paper that can stand on its own.

The human baseline also does something strategically critical: it reframes the entire research program. If humans show the same compression, the story becomes "this is a fundamental property of vague language, and models inherit it." If humans show finer discrimination, the story becomes "models are worse than humans at this specific task." Either result is interesting, but you cannot make the claim without the data. Getting this data in Paper 2 means every subsequent paper can speak to the human-model gap rather than hedging around it.

**What this paper needs to demonstrate:** That the human ordinal structure is measurable, that it differs from the model's compression in at least one meaningful way, and that the decrease direction produces a different pattern than increase.

**What it creates for Paper 3:** An anchor. You now have a human ground truth against which cross-model results can be compared. Instead of "Model A vs. Model B," Paper 3 becomes "Model A vs. Model B vs. Human Baseline" — a much stronger framing.

### Paper 3: Cross-Model Comparison (with Human Anchor)

**Why third:** With the human baseline established, cross-model becomes a test of a real theoretical question: do different training procedures and alignment methods produce different language-to-action mappings, and how do those mappings relate to human interpretation? This is no longer a replication study — it's a study of how model design choices shape the language-action interface.

The specific theoretical question worth asking: does the compression pattern correlate with model size, RLHF intensity, or training data composition? You won't be able to answer this definitively, but you can generate hypotheses. A finding that instruction-tuned models show more compression than base models (or vice versa) would be genuinely interesting to the alignment community.

**Resource note:** This is the first paper in the sequence that has real API cost. Running the full protocol across GPT-4o, Gemini Flash, and one other frontier model at the same scale as Paper 1 could run $500-1500 depending on current pricing. This is manageable on a self-funded budget but requires planning. Haiku-equivalent tiers of each model family are the right target — you're studying the phenomenon at the deployment tier, not the frontier tier.

**What this paper needs to demonstrate:** That the compression pattern varies across models in ways that are interpretable, and that the human baseline from Paper 2 provides a meaningful reference point for evaluating model behavior.

**What it creates for Paper 4:** A cross-model result means you can now speak to the phenomenon at the level of the model class, not just one model. This is the foundation for the field-defining move.

### Paper 4: The Field-Defining Move — Passive Failure at the Action Interface

**Why fourth:** This is the paper that makes the claim. By Paper 4, you have: (1) the original phenomenon documented across 6,620 runs, (2) a human baseline that characterizes the linguistic ground truth, (3) evidence that the phenomenon varies across models in interpretable ways, and (4) a valence asymmetry result that shows the phenomenon generalizes across action directions. You now have enough empirical ground to stake the claim that this is a systematic property of language-action interfaces, not an artifact of one model or one domain.

The paper's core argument: vague intensity words are a broken control interface for autonomous systems. The failure mode is passive — the model isn't refusing or hallucinating; it's silently mistranslating intent. The human-model gap quantifies the cost of this mistranslation. The cross-model variation suggests it's tractable — some training procedures produce better-calibrated interfaces than others.

**What this paper needs to demonstrate:** A theoretical framework, not just more data. This is where "passive failure at the action interface" gets defined, operationalized, and connected to existing alignment literature. The empirical foundation is already built; this paper synthesizes it.

**Venue target:** This is the paper that aims at a workshop at NeurIPS or ICLR — specifically the alignment or safety workshops. Algoverse's track record at these venues is the relevant asset here.

### Paper 5 (Optional/Conditional): Cross-Domain Transfer

**Why fifth and conditional:** Cross-domain transfer (healthcare dosing language, financial risk language, logistics scheduling language) is the paper that makes the program genuinely important rather than a niche result about resource allocation. But it requires either (a) domain expertise you don't have, (b) collaborators who do, or (c) synthetic environments you'd need to build from scratch. This paper is only worth pursuing if Paper 4 lands and creates pull — if reviewers and readers ask "does this hold in healthcare?" you have a natural next move. If Paper 4 doesn't land, this paper is premature.

**Conditional trigger:** Pursue Paper 5 only if Paper 4 gets accepted at a workshop or generates significant community interest. Otherwise, the program has sufficient depth at four papers.

---

## The Wedge Paper

**The wedge is Paper 2: the human baseline.**

Here's why this is the highest-leverage single result: every other paper in the sequence depends on knowing whether the model's compression reflects genuine linguistic ambiguity or model-specific failure. Without the human baseline, you're always hedging. With it, you can make claims.

The wedge paper creates three specific conditions that make the rest inevitable:

1. **It closes the ordinality validation gap.** The word scale is currently researcher-constructed. Once you have human data, it's validated. Every subsequent paper that uses the scale is now on firmer ground.

2. **It reframes the research question.** "Does the model compress vague intensity words?" becomes "Does the model compress vague intensity words *more than humans do*?" The second question is more interesting, more publishable, and more directly relevant to alignment. You cannot ask the second question without the first study.

3. **It creates a reference point for cross-model comparison.** Without a human anchor, cross-model comparison is just "Model A vs. Model B." With it, you can ask "which model is closest to human calibration?" — a question with direct deployment relevance.

The human baseline is also the paper that most credibly answers the "so what?" question. Right now, the "so what?" is "the model compresses words." After the human baseline, the "so what?" is "the model compresses words in ways humans don't, and here's the quantified gap." That's a stronger claim, and it's the one that makes downstream papers feel necessary rather than incremental.

One additional strategic point: the human baseline is the paper that most directly addresses the "is this model failure or linguistic ambiguity?" objection — which is the single most likely dismissal of Paper 1. Getting this data early means you're not defending against that objection for the rest of the program.

---

## Paper Two Deep-Dive

**The recommendation is human baseline + valence asymmetry as a combined study. Here is the argument against each alternative.**

**Against valence alone as Paper 2:**

Valence alone (increase vs. decrease) is a thin paper. The finding would almost certainly be "yes, there's asymmetry" — which is interesting but not surprising. More importantly, it doesn't close any of the major open questions from Paper 1. Reviewers who read Paper 1 will not be satisfied by a paper that adds one new condition without addressing the human comparison gap. Valence alone as Paper 2 looks like salami-slicing.

**Against cross-model as Paper 2:**

Cross-model without a human anchor is a comparison without a reference point. You'd be saying "Model A compresses differently than Model B" — but differently relative to what? Relative to each other, yes, but that's a weak claim. The interesting claim is "Model A is closer to human calibration than Model B" — and you can't make that claim without the human data. Running cross-model second means you've spent significant API budget on a result that will be immediately weakened by the absence of a human baseline.

There's also a strategic sequencing problem: if you run cross-model second and the results are interesting, you'll want to add the human baseline to the paper anyway. You'll either have to run the survey after the fact (making the paper feel retrofitted) or publish without it (making the paper feel incomplete). Better to get the human baseline first.

**Against human baseline alone as Paper 2:**

A pure human baseline survey — "here's what humans say these words mean numerically" — is a psycholinguistics paper, not an AI paper. It's publishable, but it doesn't advance the research program as efficiently as a combined study. The human baseline is most valuable as a comparison point against the model, not as a standalone result.

**For the combined study:**

Human baseline + valence asymmetry in a single paper does three things: (1) validates the word scale, (2) provides the human-model comparison that closes the main gap from Paper 1, and (3) extends the phenomenon to decrease instructions. The valence component also makes the IRB protocol more efficient — you're running participants through a richer task rather than a minimal one, which is better use of participant time and your effort.

**The one risk:** Combined studies can feel unfocused. The solution is a clear framing that ties the two components together. The framing is: "We characterize human interpretation of these words (baseline) and then test whether the asymmetry between increase and decrease instructions — which humans likely show — is preserved or distorted in the model." That's a coherent paper with two contributions.

---

## Resource & Feasibility Assessment

**What can be done solo:**

- **Valence extension (decrease instructions):** Fully solo. Same harness, same API, same analysis. Marginal cost relative to Paper 1. Can be collected in a weekend.
- **Denser baseline grid:** Solo. API cost is the only constraint. At Haiku pricing, a full 0-100 grid at 30 runs per cell × 10 words × 2 temperatures = 60,000 runs. At current Haiku pricing this is probably $50-150. Collect it as infrastructure while executing other work.
- **No-word control:** Solo. Trivial addition to the existing harness. Should have been in Paper 1; include it in Paper 2.
- **T=1.0 analysis:** Solo. Already collected per the paper. Analyze and include in Paper 2 or as a supplement.

**What requires collaboration or IRB:**

- **Human baseline survey:** Requires IRB review at Georgia Tech. The paper already notes this is in preparation. The IRB process at GT typically takes 4-8 weeks for minimal-risk studies; a survey study with no deception and no sensitive data is minimal risk. This is the primary blocking dependency for the sequence. Start the IRB application now — it runs in parallel with other work.
- **Cross-domain transfer:** Requires domain expertise you don't have. Healthcare dosing language, financial risk language — you need a collaborator with domain knowledge to validate that the synthetic environment is realistic. This is where Algoverse becomes critical.

**What requires significant compute:**

- **Mechanistic interpretability:** The author asks about this. The honest answer: mechanistic interpretability of the compression phenomenon would require activation patching, attention analysis, and potentially training probes on intermediate representations. This is not Haiku-scale API work — it requires model weights, which means either open-source models (Llama, Mistral) or significant collaboration. This is the right question eventually but the wrong move now. It pulls you away from the deployment-facing empirical work and into a different research community with different norms. Defer.
- **Cross-model at scale:** Running the full protocol across 3-4 models is feasible solo but requires budget planning. Estimate $500-1500 for Paper 3. Not a blocker, but requires conscious resource allocation.

**Algoverse leverage:**

The fellowship is most valuable for two specific things: (1) access to PIs who can co-author or advise on the field-defining paper (Paper 4), and (2) access to collaborators who can provide domain expertise for cross-domain transfer (Paper 5). The credibility papers (2 and 3) can be executed largely solo with mentorship. The field-defining paper benefits from having a more senior co-author who can vouch for the framing and help target the right venue. Bring Paper 4's framing to your PI now — not for execution, but for feedback on whether the "passive failure at the action interface" framing is the right one for the venues you're targeting.

**What to stop pretending you can do alone:**

Cross-domain transfer with real domain validity. You can build synthetic healthcare or finance environments, but without a domain expert co-author, reviewers will correctly note that the environments may not capture how vague instructions actually function in those domains. This paper requires collaboration. Do not attempt it solo.

---

## Timeline & Venue Strategy

### Paper 2: Human Baseline + Valence Asymmetry
- **Execution time:** 3-4 months (dominated by IRB timeline, not data collection)
- **IRB application:** Start immediately; 4-8 weeks for approval
- **Survey data collection:** 2-3 weeks after IRB approval (Prolific or MTurk, ~200 participants, ~$400-600 in participant costs)
- **Valence data collection:** 1-2 weeks (solo, API-based)
- **Analysis and writing:** 4-6 weeks
- **Target venue:** *Cognitive Science* (if the human comparison finding is strong), or a computational linguistics venue like *ACL Findings* or *EMNLP*. Alternatively, an AI safety workshop at NeurIPS or ICLR if the human-model gap is large and interpretable. The venue choice depends on the finding: if humans show the same compression, the story is linguistic and belongs at a linguistics venue; if humans show finer discrimination, the story is about model failure and belongs at an AI venue.
- **What it needs to demonstrate:** A measurable human ordinal structure, a