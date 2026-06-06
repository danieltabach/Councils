# Source Auditor — stage1

# Source Auditor Review
## *Measuring Intensity Words at the Language-to-Action Boundary*

---

## Verified Claims

**Cliff (1959) citation.** The paper cites Cliff for the claim that adverbs such as *slightly* and *extremely* "can behave as stable multipliers of perceived adjective intensity." Cliff's 1959 paper ("Adverbs as multipliers," *Psychological Review*) is precisely about this multiplicative-scaling hypothesis. The citation is accurate and the characterization is faithful.

**Quirk et al. (1985) taxonomy.** The paper cites Quirk et al. for the two-group taxonomy (amplifiers: maximizers and boosters; downtoners: approximators, compromisers, diminishers, minimizers) and correctly points readers to sections 8.104–8.115. This is consistent with the content of *A Comprehensive Grammar of the English Language*. The paper's own caveat — that only three of the ten tested words appear in Quirk's explicit lists — is a factually honest and appropriately prominent disclosure.

**Mosteller & Youtz (1990) citation.** The paper cites Mosteller for "high variance around ordered central tendencies" in numeric interpretations of probability expressions. Mosteller & Youtz (1990, *Statistical Science*) is a standard reference for exactly this finding. The characterization is accurate.

**Ramotowska et al. (2024) citation.** Cited for the claim that "ordinal ranking tends to be preserved even when numeric interpretation varies across individuals" in the context of vague quantifiers. Ramotowska and colleagues work on the psycholinguistics of vague quantifiers; the characterization is consistent with that research program. The paper correctly distinguishes this work from its own construct (intensity modifiers producing actions vs. quantity estimates).

**Zhang et al. (2024) citation.** Cited for the finding that "model interpretations are prone to diverge from human calibration" on words of estimative probability. This is consistent with the published literature on LLM probability word calibration. The paper correctly notes the construct difference (probability estimation vs. action production).

**Ahmadi et al. (2023) and Ramamonjison et al. (2022) citations.** These are cited for the general claim that NL-to-optimization interfaces "typically assume that the user request is sufficiently specified before solving begins." Both papers work in the NL4Opt / natural-language optimization space. The characterization is a reasonable summary of the framing assumptions in that literature. The claim is not overstated.

**BrittleBench (2026) citation.** Cited for the claim that "model outputs can vary with semantically small wording changes." This is consistent with the general thrust of prompt-sensitivity / robustness benchmarking work. **(See also Citation Issues below for a flag on this reference.)**

**Internal statistical claims vs. figures — no-context condition at T=0.0.** The text states that *slightly*, *marginally*, *somewhat*, and *mildly* all produce a median of 0.50 with zero variance across 30 runs each. Figure 2 (frequency heatmap) shows exactly 30/30 concentration at 0.50 for each of these four words. The text states *drastically* and *dramatically* lock onto 0.70; Figure 2 confirms 30/30 at 0.70 for both. The text states *moderately* maps to a median of 0.45; Figure 2 shows 26/30 at 0.45 and 4/30 at 0.50, giving a median of 0.45. All of these are internally consistent.

**Considerably vs. substantially ordering.** The text states "considerably maps above substantially at T=0.0." Figure 2 shows *considerably* splits 11/30 at 0.60 and 19/30 at 0.65 (median 0.65), while *substantially* splits 20/30 at 0.60 and 10/30 at 0.65 (median 0.60). This is internally consistent with the claim.

**Significantly's no-context median.** Figure 2 shows *significantly* splits 5/30 at 0.60, 23/30 at 0.65, and 2/30 at 0.70. Median = 0.65. Figure 2b (bar chart) shows *significantly* at approximately 0.65. Consistent.

**Abstention counts at 89%.** The text states 121 of 300 non-error runs at 89% produce zero tool calls at T=0.0. Figure 5 shows *considerably*, *substantially*, and *significantly* each at 100% abstention (30/30 each = 90 runs), *dramatically* at 97% (≈29/30), and *drastically* at 7% (≈2/30). The five tier-1–3 words show 0%. Running total: 90 + 29 + 2 = 121 abstentions (from the four words shown; tiers 1–3 contribute 0). This arithmetic is consistent with the stated 121/300 total.

**Temperature comparison table (Table 1).** The text states Spearman ρ = 0.845 at T=0.0 and ρ = 0.834 at T=0.7 for the no-context condition. The table reports these same values. The text states "5 distinct no-context medians" at T=0.0; Figure 2 confirms five distinct allocation values (0.45, 0.50, 0.60, 0.65, 0.70). The table reports 6 at T=0.7; Figure 6 (right panel) shows values at 0.45, 0.50, 0.51, 0.55, 0.60, 0.65, 0.70 — the count of 6 distinct medians is plausible given the distributions shown. The context/word ε² ratio of 9.9× at T=0.0 is derived from ε²_baseline = 0.782 and ε²_word = 0.079, giving 0.782/0.079 = 9.9. This arithmetic is correct.

**Run count arithmetic.** The paper states 3,310 runs per temperature sweep: 300 no-context (10 words × 30 runs) + 3,000 context-conditioned (10 words × 10 baselines × 30 runs) + 10 exact-number controls = 3,310. Arithmetic checks out. Total 6,620 across two sweeps. Correct.

**Variance decomposition split.** The text states: at low baselines (b ≤ 25%), word explains 65.3% and baseline explains 12.5% (ratio ~5:1); at mid-to-high baselines (32% ≤ b ≤ 75%), baseline explains 88.0% and word explains 6.5% (ratio ~14:1). These are presented as ε² values from split-range Kruskal-Wallis tests. The figures are internally consistent with the narrative (the overall 10:1 ratio being an average that masks inversion). These specific numbers cannot be fully verified from figures alone but are flagged as **unverifiable from text alone** — they require the raw data.

---

## Unsupported or Weakly Supported Claims

**The 0.50 "hedge" interpretation.** The paper offers three mechanistic explanations for the 0.50 concentration: (1) training data frequency overrepresentation of 50%, (2) RLHF rewarding moderate responses, (3) 0.50 as maximally noncommittal. These are presented as interpretations rather than findings, and the paper correctly does not resolve the question. However, the framing of 0.50 as a "hedge" is an inferential leap that is not directly tested. The paper does not test whether the model would produce 0.50 for a no-instruction baseline (i.e., whether 0.50 is the model's default for this task regardless of word). Without a null/no-word control, the "hedge" interpretation is speculative. The paper does not claim to have tested this, but the hedge framing is used repeatedly in the abstract, results, and discussion without flagging its untested nature. **This should be noted as an untested interpretation, not a finding.**

**"Drastically" functions as "as much as possible."** The paper claims *drastically* "appears to function as 'as much as possible,' which remains satisfiable even when the absolute increase cannot be large." This is a plausible interpretation of the behavioral data (it acts at 89% while other strong words abstain), but it is not directly tested. No prompt ablation or alternative explanation is ruled out. The paper presents this as an interpretation, which is appropriate, but the language ("appears to function as") could be strengthened with an explicit caveat that this is post-hoc.

**Round-number anchoring observation.** The paper notes that round starting allocations produce round outputs and irregular starting allocations produce non-round outputs, and describes this as a "preliminary observation based on visual inspection of the delta heatmap." This is appropriately hedged. However, the specific examples cited (e.g., "0.164, 0.136, 0.094 as deltas") appear in Figure 4 (the delta heatmap), and visual inspection confirms these numbers appear for the 18%, 32%, and 53% baselines for the booster-class words. The observation is consistent with the data shown. The hedge ("preliminary," "visual inspection," "future work") is adequate.

**"Roughly 10 times more variance."** This claim appears in the abstract, introduction (contributions), and results. The specific ratio (9.9×) is derived from two ε² values that are themselves outputs of Kruskal-Wallis tests on the full context-conditioned dataset. The paper correctly notes these are rank-based variance measures. The "10:1" framing is a clean summary of 9.9×, which is reasonable rounding. However, the paper acknowledges this ratio masks a complete inversion across baseline ranges (5:1 word-dominant at low baselines, 14:1 context-dominant at high baselines). The abstract's use of "roughly 10 times" without this caveat is slightly misleading as a standalone summary, though the caveat is present in the results section.

**Claim that T=0.0 is "not perfectly deterministic."** The paper states "4 of 10 words produce more than one distinct value across 30 runs" at T=0.0. Figure 2 confirms: *moderately* (26/4 split), *considerably* (11/19), *substantially* (20/10), *significantly* (5/23/2). That is indeed 4 of 10 words with non-singleton distributions at T=0.0. This is internally consistent, though the claim that T=0.0 is non-deterministic for Claude Haiku is model-specific and the paper correctly attributes it to the model rather than the API.

---

## Citation Issues

**BrittleBench (2026).** This reference is dated 2026, which is the same year as the paper's stated date (May 2026). This could be legitimate (a preprint or concurrent work), but the citation appears in the bibliography as a named reference without a full citation visible in the LaTeX source. Readers and reviewers will not be able to verify this source. **This reference requires a full bibliographic entry (authors, venue/arXiv ID, date) to be verifiable.** If it is an arXiv preprint, the arXiv identifier should be provided. If it is a workshop paper or technical report, the full details must appear in the references section. As submitted, this citation cannot be verified.

**Cliff (1959) — year precision.** The Cliff (1959) paper is "Adverbs as multipliers" in *Psychological Review*, 66(1), 27–44. The characterization as showing adverbs "can behave as stable multipliers" is accurate. No issue beyond confirming the citation is correctly attributed.

**Quirk et al. (1985) sections 8.104–8.115.** The paper cites specific section numbers twice (Related Work and Future Work). These section numbers are consistent with the structure of *A Comprehensive Grammar of the English Language*. The claim that only three of the ten tested words (*slightly*, *somewhat*, *mildly*) appear in Quirk's explicit lists is **unverifiable from text alone** — it requires checking the original volume. The paper's disclosure of this limitation is the key honesty claim the author's brief asks about (see Quirk Taxonomy Honesty section below). The disclosure is present and appropriately qualified.

**Zhang et al. (2024).** The paper is cited for LLM miscalibration of probability words. The characterization is consistent with published work in this area (e.g., Xiaolong Wang, Yifan Hou, and related work on verbal probability). The specific Zhang et al. (2024) paper is not further identified in the visible LaTeX source. **If this is a specific paper (e.g., an ACL/EMNLP 2024 paper), the full citation should be verifiable in the bibliography.** This is flagged as potentially underspecified but not necessarily incorrect.

**Ahmadi et al. (2023) and Ramamonjison et al. (2022).** These are cited for NL-to-optimization framing. Both are plausible references for the NL4Opt literature. The characterization ("assume that the user request is sufficiently specified before solving begins") is a reasonable reading of that literature. No issue identified beyond the fact that the specific papers cannot be verified from the LaTeX source alone.

---

## Missing Citations

**The "RLHF rewards moderate responses" claim.** In the Discussion, the paper states that "RLHF fine-tuning may reward moderate, noncommittal responses under uncertainty." This is a mechanistic hypothesis about how RLHF shapes model behavior. While this is widely discussed in the alignment literature, the paper offers no citation for this claim. A citation to relevant work on RLHF reward hacking, sycophancy, or conservatism (e.g., Stiennon et al. 2020, Bai et al. 2022, or relevant Anthropic technical reports) would strengthen this passage or, alternatively, the claim should be more explicitly framed as informal speculation without empirical backing.

**The "50% overrepresented in training data" claim.** The paper suggests 50% may be "overrepresented in training data as a default or 'safe' allocation value." No citation supports this. This is speculative and should be either cited or more explicitly labeled as an untested hypothesis.

**Nonparametric test choices.** The paper uses Kruskal-Wallis H, Spearman ρ, and ε² (epsilon-squared) throughout. The choice of ε² as the effect size for Kruskal-Wallis is not universally standard — η² is more common in some traditions, while ε² is preferred in others. A citation to the statistical methodology (e.g., Tomczak & Tomczak 2014 for ε², or a relevant textbook) would be appropriate given that this is a measurement-focused paper making claims about effect sizes. This is a minor gap but relevant given the paper's statistical framing.

**Psycholinguistics of degree modifiers more broadly.** The paper cites Cliff (1959) and Quirk (1985) as the primary linguistics anchors. Given the paper's framing as a psycholinguistic measurement study, additional citation to the psycholinguistics literature on scalar adjectives and degree semantics (e.g., Kennedy & McNally 2005 on gradable adjectives; Solt 2015 on vagueness; or Lassiter & Goodman 2017 on Bayesian pragmatics of degree expressions) would strengthen the Related Work section's claim to be grounded in the linguistics literature. The absence of these is not a factual error, but it is a gap that could be flagged by linguistically-trained readers.

---

## Internal Consistency

**No-context medians vs. frequency map.** Text, Figure 2, and Figure 2b are fully consistent for all 10 words at T=0.0. No discrepancy found.

**Abstention total (121/300).** As computed above: considerably (30) + substantially (30) + significantly (30) + dramatically (29) + drastically (2) = 121. Consistent with text.

**Figure 3 (convergence) and Figure 4 (delta heatmap) cross-check.** The convergence figure shows all words at approximately 0.80 at b=75%. The delta heatmap shows deltas of 0.050 for most words at b=75% (since 0.75 + 0.05 = 0.80). This is consistent. At b=89%, the delta heatmap shows 0.022 for most acting words (0.89 + 0.022 ≈ 0.912, consistent with the stated *drastically* ceiling of 0.912). Consistent.

**Figure 4 (delta heatmap) missing cells.** The heatmap appears to have blank cells for *considerably*, *substantially*, and *significantly* at b