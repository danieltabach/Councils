# Domain Expert — stage1

### Technical Assessment

**Core Contribution Soundness**

The experimental design is internally coherent and the core measurement logic is sound. The key insight — using a deterministic backend as a measuring instrument to isolate the language-to-action translation step — is methodologically clean and well-executed. The author correctly identifies that the backend is not the object of study; it is a signal amplifier. This is a legitimate and underused experimental paradigm.

The statistical choices are appropriate for the data structure. Nonparametric tests (Kruskal-Wallis H, Spearman ρ, ε²) are the right tools when outputs are discrete, heavily concentrated on a small number of values, and not plausibly normally distributed. The author does not misuse these tools.

**Where the Technical Account Has Gaps**

The most significant technical gap is the treatment of the no-context condition's absolute allocation values (0.50, 0.60, 0.65, 0.70) as if they are purely semantic outputs of the intensity words. They are not — they are also outputs of the prompt's implicit framing, the tool schema, any system prompt present, and the model's prior about what a "reasonable" allocation for an "innovation" task looks like. The paper acknowledges that 0.50 may reflect training data frequency or RLHF effects, but this is treated as speculation in Discussion rather than as a confound to be controlled. The no-context condition cannot cleanly separate "what does *slightly* mean to the model" from "what does the model think a reasonable innovation allocation is, adjusted slightly." These two things are entangled, and the paper does not fully reckon with this.

A related gap: the paper reports that at T=0.0, 4 of 10 words produce more than one distinct value across 30 runs. This is buried in a single sentence at the end of Section 4.5. This is actually a notable result — greedy decoding at temperature 0 should be deterministic given identical inputs. If it is not, either (a) the API is not truly T=0 greedy, (b) there is session-level variation the author did not fully control, or (c) there is something about the prompt construction that introduces variation. The author should investigate and explain this more carefully, as it bears on the reliability of the T=0.0 as a "deterministic baseline."

The Spearman ρ calculation in the no-context condition uses the researcher-hypothesized tier as the ordinal predictor. Since ρ = 0.845 is computed against the researcher's own ordering, it is not an independent validation of that ordering — it is a measure of how well the model's outputs are *consistent with* the researcher's hypothesis. This is fine as a descriptive statistic but should be stated more precisely. The paper partially acknowledges this but does not make the circularity fully explicit.

---

### Addressing the Author's Specific Concerns

**Concern 1: Quirk Taxonomy Honesty**

The current framing is adequate for a preprint at this stated scope. The paper acknowledges in three places (Introduction, Table 1 caption, Section 3.3) that only 3 of 10 words appear in Quirk's explicit lists, that the remaining 7 were heuristically chosen, and that the scale is researcher-constructed. This is honest and sufficient for ArXiv.

However, there is a subtle framing inconsistency that should be fixed. The paper uses the word "tier" throughout as if tiers are a property of the words themselves, but they are a property of the researcher's hypothesis. When the paper says "words in tiers 1--3 always act" or "booster-class words abstain," it is using the researcher's categorization as if it were established. This is fine as shorthand, but one sentence in the Results section should remind the reader that tier assignments are hypothesized, not validated — especially when tier-based groupings are used analytically (e.g., the weak/strong split in Figure 4b). The current footnote in Section 3.3 does this for the word scale, but the reminder does not carry into Results where the tier labels are used most heavily.

The more substantive issue is that *moderately* is placed in Tier 3 as a "moderate/compromising term," but it produces the lowest allocation of any word (0.45 median, below all Tier 1 and 2 words). The paper correctly identifies this as an "ordinal violation" and offers a plausible interpretation (restraint heuristic vs. magnitude heuristic). This interpretation is linguistically reasonable — "moderate" can function as a policy word ("keep things moderate") rather than a quantity word ("increase by a moderate amount"). But the paper should note that this ambiguity is a known issue in degree-modifier semantics and is not merely a quirk of this experiment. The word "moderately" is genuinely ambiguous between an instructional reading and a quantity reading in this context, and that ambiguity is not a failure of the model — it may be a correct response to genuine lexical ambiguity. The paper should say this more directly rather than treating it primarily as an anomaly.

**Concern 2: Statistical Rigor**

The statistical claims are not oversold given the stated scope. The acknowledgments of limitations are present and appropriately placed. Specific assessments:

*Multiple comparison correction*: The paper runs multiple Kruskal-Wallis tests and multiple Spearman correlations across conditions and baseline values. No correction (Bonferroni, Benjamini-Hochberg) is applied. For a preprint framed as a "first measurement slice," this is defensible, but the paper should add one sentence explicitly noting this: "No correction for multiple comparisons was applied; reported p-values should be interpreted as descriptive rather than confirmatory." The current text says "these limitations are acknowledged" but does not say this directly in the statistical methods section. The current acknowledgment is in the Limitations paragraph of Discussion, which is too late and too buried. Add it to Section 3.6.

*The ε² decomposition*: The 10:1 ratio (ε²_baseline = 0.782 vs. ε²_word = 0.079) is reported as if the two effect sizes are directly comparable and sum to a meaningful total. They do not — they come from separate Kruskal-Wallis tests on different grouping variables, not from a joint variance decomposition. Two separate KW tests cannot be interpreted as a partition of variance. The paper should say "two separate Kruskal-Wallis tests were run, one grouping by word and one by baseline; the ε² values from these tests are not additive but suggest that baseline grouping captures far more rank-based structure than word grouping." The current language ("starting allocation explains roughly 10 times more variance than word choice") implies a joint decomposition that the analysis does not perform. This needs to be corrected — it is the most technically imprecise claim in the paper.

*Ordinality validation circularity*: As noted above, Spearman ρ against researcher-hypothesized tiers is not an independent test of ordinality. The paper should state explicitly: "This is a measure of consistency with the hypothesized ordering, not an independent validation of it."

*The split-range variance decomposition* (low vs. mid-to-high baselines) is a post-hoc analysis with a researcher-chosen split point. The paper should flag this as exploratory. The finding is plausible and the direction is clear from the figures, but the specific numbers (65.3%, 12.5%, 88.0%, 6.5%) should not be presented without noting that the split at 25%/32% was chosen after seeing the data.

**Concern 3: Clarity and Flow**

The five-block structure under two empirical questions works. The paper reads coherently front-to-back. The figures are high quality and the captions are informative. The limitations section is clearly stated. The future work section is appropriately scoped for a first preprint — it is ambitious but not overclaiming.

One structural issue: the paper promises in the Introduction that it will answer three empirical questions, but the Results section is organized into five blocks that do not map cleanly onto those three questions. The reader has to do work to connect "Boundary Behavior: Hedge, Act, Abstain" to Question 3 and "Downstream Consequences" to... none of the three questions explicitly. Either restructure the Results headers to match the three questions, or change the Introduction to not promise a three-question structure.

---

### Positioning in the Field

**Related Work Coverage**

The related work section is adequate for a preprint. The three paragraphs cover the right territory: degree modifiers from linguistics, vague quantifiers and probability expressions, and LLM prompt sensitivity. The citations are appropriate.

**Missing Related Work**

The paper is missing engagement with several lines of work that are directly relevant:

1. **Scalar implicature and pragmatic scales**: The finding that the model compresses 10 words into 5 regimes is directly related to Horn scales and scalar implicature in formal pragmatics (Horn 1972, Levinson 2000). The model's behavior — treating *slightly*, *marginally*, *somewhat*, and *mildly* as equivalent — may reflect the pragmatic structure of these scales rather than model failure. The paper should at minimum acknowledge this literature and note that the compression pattern may be linguistically principled rather than a model artifact.

2. **Vague predicates and degree semantics in formal linguistics**: Kennedy & McNally (2005) on gradable adjectives and degree scales, and subsequent work on vagueness in degree modification, would strengthen the theoretical framing. The paper uses "degree modifiers" as a technical term but does not engage with the formal semantic literature on what degree modification means.

3. **LLM calibration on numeric outputs**: The paper cites Zhang (2024) on probability words, but misses Kadavath et al. (2022) on calibration and Xiong et al. (2024) on LLM uncertainty expression. These are relevant because the compression finding can be framed as a calibration issue.

4. **Instruction following and grounding**: The context-dominance finding connects to work on grounding in instruction following (Misra et al. 2023, Andreas et al. 2022). The model's tendency to anchor on the stated current state rather than the instruction word is a grounding phenomenon.

5. **Anchoring effects in LLMs**: The round-number anchoring observation in the Discussion connects to a growing literature on numeric anchoring in LLMs (Zhao et al. 2021 on calibration, various prompt-sensitivity papers). The paper treats this as a preliminary observation but it is actually a well-studied phenomenon.

**Is the Framing as a Psycholinguistic Measurement Study Working?**

Mostly yes, but with one persistent leak. The paper frames tool calling as the instrument and word interpretation as the subject, which is the right framing. However, several passages slip back into framing the results as findings *about the tool-calling interface* rather than findings *about word interpretation*. The sentence "Vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries" (abstract) is about the interface, not about word interpretation. Reframe as: "The model's numeric interpretation of vague intensity words is compressed, state-dependent, and discontinuous near operational boundaries." This is a small but important distinction for the framing the author wants.

---

### Alternative Approaches

**What I Would Have Done Differently**

1. **Prompt the model to explain its reasoning before acting.** A chain-of-thought or "explain your choice" condition would reveal whether the model has an explicit numeric interpretation of the word or is choosing based on some other heuristic. This would be low-cost to add and would substantially strengthen the mechanistic claims.

2. **Include a symmetric decrease condition in the initial design.** The paper acknowledges this as future work, but the asymmetry between increase and decrease instructions is a known phenomenon in human cognition (loss aversion, asymmetric framing effects) and would be a natural within-experiment control. The cost is a 2× experiment, which is significant but not prohibitive.

3. **Use a minimal context condition that doesn't state the current allocation explicitly but implies it.** The paper plans this as "Tier 3" future work, but it would have been more informative as part of the initial design. The distinction between "the model reads context it is given" and "the model infers context from the tool state" is important for the alignment framing.

4. **Treat the word scale as a continuous variable rather than a categorical one.** The paper assigns tier numbers (1–6) to words and uses these as the ordinal predictor for Spearman ρ. An alternative is to use human-elicited numeric ratings of the words as the predictor — even a small pilot survey of 10–20 participants would provide a continuous scale and would simultaneously address the human baseline gap.

5. **Test the same words in a different domain (e.g., temperature, speed, budget) to assess domain generalization.** The current results are specific to resource allocation with percentage values. Whether the compression pattern is specific to this domain or reflects something general about how the model interprets these words is an open question that a second domain would partially address.

---

### Baselines and Comparisons

The paper does not claim to be a comparative study, which is appropriate for a first measurement slice. However, the absence of any baseline raises a specific technical concern that goes beyond the acknowledged "no human baseline" limitation.

**The no-context condition lacks a null baseline.** The paper shows that *slightly* maps to 0.50 and *drastically* maps to 0.70. But what does the model output when given no intensity word at all — just "Architects should spend more time on innovation"? If the null instruction also produces 0.50, then the lower-tier words are not functioning as intensity modifiers at all; they are producing the same output as no modifier. If the null produces something else, the comparison is informative. This is a one-cell addition to the experiment and should be added. It would sharpen the claim that lower-tier words "hedge at 0.50" versus "produce the same output as no instruction."

**The exact-number controls are mentioned but not analyzed.** The paper says they "reproduced the requested values exactly, validating that the harness correctly transmits and applies numeric requests." This is fine as a sanity check, but the controls could be used more analytically — for example, to establish what the model outputs when given a precise numeric instruction, providing a reference point for how much precision is lost in the vague-word condition.

---

### Impact Assessment

If the claims hold and generalize, the contribution is modest but legitimate. The specific findings — compression, context dominance, and boundary mode-switching — are not surprising to practitioners who work with LLM agents, but they have not been carefully documented in a controlled setting. The value is in the measurement methodology and the clean experimental design, not in the surprise of the findings.

The most impactful finding is the abstention pattern at the boundary, specifically the *drastically*/*dramatically* asymmetry. This is genuinely unexpected and is the most novel result in the paper. The interpretation (drastically = "as much as possible" vs. dramatically = "a large specific amount") is speculative but interesting and testable.

The context-dominance finding (10:1 ratio) is the most practically important but also the most constrained by the single-model, single-domain design. The claim that "the same word cannot be treated as having a context-invariant numeric meaning" is important for agent design, but its generalizability across models and domains is unknown.

For the stated purpose — ArXiv preprint, portfolio piece, priority establishment, research pitch — this is appropriate and ready. For a conference submission, it would need the human baseline, cross-model comparison, and the multiple-comparison correction.

---

### Technical Red Flags

**Flag 1 (Moderate): The ε² additivity claim.**
As noted above, comparing ε²_baseline = 0.782 and ε²_word = 0.079 from two separate KW tests as if they are components of a joint variance decomposition is technically incorrect. The "10:1 ratio" language implies a partition that the analysis does not perform. This needs to be reworded in the abstract, the Results section, and the contributions list. The underlying finding (baseline explains more rank-based structure than word) is correct; the framing as a variance ratio is not.

**Flag 2 (Minor): T=0.0 non-determinism.**
Four of 10 words produce more than one distinct value at T=0.0 across 30 runs. This is either a real phenomenon (the API is not truly greedy at T=0) or an artifact of experimental procedure. The paper mentions it briefly but does not investigate it. For a paper making claims about deterministic behavior at T=0.0, this deserves a more explicit explanation. The author should check whether the Anthropic API guarantees deterministic output at T=0 and report this.

**Flag 3 (Minor): The convergence figure (Fig. 3) shows non-monotonic behavior for *drastically*.**
The *drastically* line in Figure 3 drops sharply at b=18% and then rises again at b=25%, creating a V-shape that is inconsistent with a smooth state-dependent policy. This is not discussed in the text. It may be an artifact of the 30-run median with discrete outputs at a specific baseline, or it may reflect something interesting about how the model handles the number 18 specifically. The paper should at minimum note this non-monotonicity.

**Flag 4 (Moderate): The "three-mode policy" claim is presented more confidently than the data support.**
The hedge/act/abstain taxonomy is a post-hoc description of the observed pattern at one specific baseline (89