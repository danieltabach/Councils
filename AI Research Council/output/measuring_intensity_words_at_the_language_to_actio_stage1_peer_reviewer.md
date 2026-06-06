# Peer Reviewer — stage1

### Summary

This paper presents a controlled measurement study examining how a large language model (Claude Haiku) translates vague English intensity words (e.g., *slightly*, *considerably*, *drastically*) into numeric actions within a synthetic constrained resource-allocation environment. The model receives natural-language instructions containing one of 10 degree modifiers and responds via a structured tool call; the numeric output of that call is the primary dependent variable. Across 6,620 runs at two temperatures, the paper documents three main findings: (1) the model compresses 10 words into ~5 distinct output regimes; (2) when current system state is provided as context, it explains ~10× more variance than word choice; and (3) near feasibility boundaries, the model exhibits qualitatively distinct behavioral modes (hedge, act, abstain) that are word-dependent. The paper is explicitly framed as a "first measurement slice" of a planned multi-experiment program.

---

### Strengths

1. **Clear and well-motivated research question.** The framing of the language-to-action boundary as a measurement target is genuinely useful and underexplored. The paper correctly identifies that prior work on vague quantifiers and probability expressions does not directly address the action case, and it carves out a defensible niche.

2. **Experimental design is clean and appropriate for its scope.** The separation of language input, model output, and deterministic backend is well-conceived. The two-condition structure (no-context vs. context-conditioned) isolates exactly the right variables for the questions asked. The exact-number control is a sensible sanity check.

3. **Figures are high quality and do real communicative work.** The frequency heatmap (Fig. 2), delta heatmap (Fig. 4), convergence plot (Fig. 3), and abstention bar chart (Fig. 5) are all well-designed and legible. The figures largely speak for themselves, which is a genuine strength in a measurement paper.

4. **Limitations are honestly and specifically stated.** The paper acknowledges single-model scope, absence of a human baseline, researcher-constructed word scale, one-directional instructions, and cost-constrained baseline grid. These are not buried — they appear in the Limitations section, in the footnote to Table 1, and are previewed in the introduction. This level of transparency is appropriate and commendable for a first preprint.

5. **The three-mode boundary finding (hedge/act/abstain) is the paper's most novel contribution.** The discovery that *drastically* behaves categorically differently from *dramatically* at the 89% boundary — acting by pushing to the ceiling rather than abstaining — is a genuinely surprising and well-documented result. Fig. 5 makes this vivid. This finding alone justifies the preprint.

6. **Psycholinguistic framing is mostly successful.** The paper reads as a measurement study of word interpretation, not a tool-calling paper. The introduction correctly situates the work relative to Cliff (1959), Quirk (1985), and vague quantifier literature. The framing succeeds at the level of abstract and introduction.

7. **The variance decomposition (10:1 context-over-word ratio) is well-reported.** The split-range decomposition in Section 4.2 — showing that the 10:1 ratio is an average masking a complete inversion between low and high baselines — is a more sophisticated presentation than the headline number alone, and it adds real interpretive value.

---

### Weaknesses

1. **The Quirk taxonomy framing creates an unresolved tension that the paper does not fully resolve.** This is the author's stated primary concern, and it deserves a direct verdict: the current framing is *adequate for a preprint but only just*. The footnote in Table 1 and the paragraph in Section 2 do acknowledge the heuristic nature of the mapping. However, the paper still uses "hypothesized tier" language throughout Results and Discussion as though the tier assignments carry more epistemic weight than they do. The specific problem: Spearman ρ = 0.845 is reported as confirming "the hypothesized intensity ordering," but the ordering is researcher-constructed, not validated. A reader could reasonably ask: if you had ordered the words differently, would ρ be higher? The paper should add one sentence explicitly acknowledging that the ρ value is sensitive to the assumed ordering, and that a different defensible ordering might yield a different correlation. This is a framing fix, not a statistical one.

2. **No multiple-comparison correction, and the paper does not adequately justify its absence.** The paper runs Kruskal-Wallis tests and Spearman correlations across multiple conditions (no-context, 10 baselines, two temperatures) without correction. For a preprint framed as a measurement study, this is acceptable *if explicitly justified*. The current Limitations section says "nonparametric tests throughout" but does not address the multiple-comparison issue at all. For ArXiv readiness, one sentence should be added: e.g., "No correction for multiple comparisons was applied; reported p-values should be interpreted as descriptive rather than confirmatory, consistent with the exploratory scope of this study." The primary concern is not false positives in the headline results (the effect sizes are enormous — ε² = 0.969 is not going to reverse under Bonferroni), but the absence of any acknowledgment looks like an oversight rather than a deliberate choice.

3. **The "moderately" ordinal violation is underexplained.** The paper notes that *moderately* maps below several lower-tier words and offers a "restraint heuristic" interpretation. This is the most linguistically interesting anomaly in the paper, and it gets two sentences in Results and one in Discussion. The interpretation — that *moderately* activates "keep things moderate" rather than "increase by a moderate amount" — is plausible and worth more development. What does this imply about the model's lexical representation of degree modifiers? Does it suggest that some words in this set are not functioning as degree modifiers at all in the operational context? This is worth a short additional paragraph, particularly because it speaks directly to the psycholinguistic framing.

4. **The no-context condition's relationship to the context-conditioned condition is not fully integrated.** The paper presents the two conditions somewhat sequentially without fully connecting them. In the no-context condition, the model produces 0.50 for four lower-tier words; in the context condition at b=50%, those same words also produce outputs near 0.50–0.55. Is the no-context condition behaving as though the model implicitly assumes a ~50% starting allocation? This would be a meaningful finding — the model may have an implicit prior over system state. The paper gestures at this in the "0.50 as hedge" discussion but does not develop the connection to the context-conditioned results. A single integrative paragraph would strengthen the paper considerably.

5. **The downstream consequences section (4.4) is the weakest section.** The dollar figures ($-424K to $-675K spread) are specific to a synthetic environment and the paper correctly notes this. But the section does not add much beyond "different words produce different outcomes, which matters." The section could be shortened to two sentences, or alternatively strengthened by showing how the spread varies across baselines (does the $250K spread persist at high baselines, or does it collapse like the allocation gap does?). As currently written, it reads like a justification for the experimental design rather than a result.

6. **The framing of ε² = 0.969 in the no-context condition requires a caveat.** An effect size of 0.969 for word identity in the no-context condition sounds very impressive, but it is partly a product of the experimental design: the model produces near-zero within-word variance at T=0.0 (many words produce the same value in all 30 runs), so between-word variance dominates trivially. The paper should note that this ε² is partly a consequence of the deterministic decoding condition rather than a substantive finding about word distinctiveness per se.

7. **The abstract's third finding is slightly misleading.** The abstract states "the word *drastically* pushes to the local ceiling." This is accurate but creates a slightly false impression that *drastically* is uniquely extreme across all conditions. In fact, at low baselines, *drastically* and *dramatically* both map to 0.70 in the no-context condition. The boundary behavior is what distinguishes them. The abstract could be more precise: "near feasibility limits, *drastically* pushes to the local ceiling while other strong words abstain."

---

### Questions for Authors

1. **On the Quirk ordering and ρ sensitivity:** If you re-ordered the 10 words using a plausible alternative ordering (e.g., swapping *moderately* and *mildly*, or placing *considerably* above *significantly*), how much does Spearman ρ change? Even a brief sensitivity analysis — or an acknowledgment that the ρ is conditional on the assumed ordering — would strengthen the statistical claims.

2. **On the 0.50 implicit prior:** In the no-context condition, the model defaults to 0.50 for four lower-tier words. In the context condition at b=50%, the same words produce outputs very close to 0.50–0.55. Does this suggest the model has an implicit ~50% prior over the starting state when no context is given? Have you examined whether the no-context outputs are consistent with the context-conditioned outputs at any particular implied baseline?

3. **On the ε² = 0.969 caveat:** The near-zero within-word variance at T=0.0 in the no-context condition means that between-word variance dominates mechanically. Do you agree that this inflates the ε² value relative to what would be observed with more within-word variance? If so, is there a way to report this more carefully?

4. **On the abstention mechanism:** When *considerably*, *substantially*, and *significantly* abstain at 89%, does the model produce a refusal message, a statement of infeasibility, or simply no tool call? Understanding the model's reasoning (if inspectable via chain-of-thought) would help distinguish between "the model recognizes a constraint violation" and "the model is uncertain about what to do." Is this information available from the API responses?

5. **On the context-conditioned condition at b=0%:** At a 0% starting allocation, the context condition should be close to the no-context condition (both start from a low/empty state). Do the outputs at b=0% match the no-context outputs for the same words? If they diverge substantially, that would suggest the framing of the context prompt (not just the baseline value) is changing behavior.

6. **On multiple comparisons:** Can you add an explicit statement that no correction for multiple comparisons was applied, and that this is appropriate given the exploratory scope? This is a one-sentence fix that would preempt a common reviewer objection.

---

### Minor Issues

1. **Section 4.1, paragraph 3:** "Figure~\ref{fig:medians} shows the same pattern as Figure~\ref{fig:frequency}" — this sentence is redundant given that the two figures are discussed consecutively. Consider replacing with a sentence that adds information (e.g., the specific median values for the booster tier).

2. **Section 3.5, Question 1 explanation:** The parenthetical "as tier increases, output tends to increase" is correct but the following sentence — "Cases where a higher-tier word produces a lower output than expected, are reported as descriptive observations rather than treated as evidence against the hypothesized ordering we framed in this study" — has an unnecessary comma after "expected" and is slightly circular in reasoning. Rephrase: "Ordinal violations are reported descriptively; the hypothesized ordering is treated as a reference frame, not a null hypothesis to be rejected."

3. **Section 4.2:** "When the context of a 'current allocation'(our baseline variable) is supplied" — missing space before the opening parenthesis.

4. **Section 4.2:** "roughly 10 times more variance than word choice ($\varepsilon^2_\text{baseline} = 0.782$ vs.\ $\varepsilon^2_\text{word} = 0.079$)" — 0.782/0.079 ≈ 9.9×, which rounds to "roughly 10 times." This is fine, but the Table 1 entry says "9.9×" while the text says "roughly 10 times." These are consistent but the slight discrepancy across text and table could confuse a casual reader. Consider using "approximately 10×" consistently.

5. **Introduction, contributions list, item 1:** "A controlled method for measuring how a language model maps vague intensity words to numeric actions" — this is a methodological contribution, but the method itself is fairly simple (it's essentially a prompt-and-measure design). Consider softening to "A controlled experimental setup" or "A measurement framework."

6. **Section 4.3:** "Lower words through *moderately* produce actions in all 30 runs" — "lower words through" is slightly awkward. Consider "Words in tiers 1–3 (including *moderately*) produce actions in all 30 runs."

7. **Figure 3 (convergence plot):** The lines for *considerably*, *substantially*, *significantly*, and *dramatically* are visually very similar in color (various shades of orange/red) and overlap substantially at mid-to-high baselines. Consider using line styles (dashed, dotted) in addition to color to distinguish these words, particularly for readers viewing in grayscale.

8. **Figure 4 (delta heatmap):** The two empty cells (Considerably and Substantially at 89%) presumably represent abstention. This should be noted explicitly in the caption — currently a reader might think the data is missing.

9. **Section 5, "Mechanistic speculation" paragraph:** The three explanations for the 0.50 hedge (training data frequency, RLHF, maximal non-commitment) are reasonable but are presented without any attempt to distinguish them. Even a brief note on what evidence would differentiate these hypotheses would strengthen the paragraph.

10. **Title:** "Measuring Intensity Words at the Language-to-Action Boundary" is clear and appropriate. No change needed.

11. **Abstract:** "Vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries" — this closing sentence is strong and memorable. Keep it.

---

### Recommendation

**Weak Accept** (for ArXiv)

This is a competent, well-framed first preprint that makes a genuine empirical contribution within its stated scope. The experimental design is clean, the figures are strong, the limitations are honestly stated, and the boundary-behavior finding (hedge/act/abstain) is novel and interesting. The paper successfully reads as a psycholinguistic measurement study rather than a tool-calling paper.

The weaknesses are real but appropriate to the stated stage: the Quirk taxonomy framing needs one additional sentence of qualification on ρ sensitivity; the absence of multiple-comparison acknowledgment should be addressed with a single sentence; and the downstream-consequences section should be tightened. None of these require new experiments. The paper is ready for ArXiv with minor revisions.

For the stated secondary purposes (LinkedIn, conference pitches, Algoverse mentorship), the paper is well-suited. The core findings are clearly stated, the figures are presentation-ready, and the "first slice" framing is appropriately humble without underselling the results.

**Not yet suitable for a top venue (NeurIPS/ICML/ICLR)** in its current form — the single-model scope, absence of human baseline, and researcher-constructed word scale would require the extensions described in Future Work before a competitive submission. But that is entirely consistent with the author's stated goals.

---

### Confidence

**4/5.** I have read the paper carefully, examined all figures, and engaged with the specific concerns raised in the author's brief. I am not auditing the raw statistical computations (per mandate), but the reported statistics are internally consistent and the effect sizes are large enough that minor computational errors would not change the qualitative conclusions. My confidence is slightly below 5 because I cannot verify the API behavior of Claude Haiku or the exact prompt text used, which are relevant to the abstention and compression findings.