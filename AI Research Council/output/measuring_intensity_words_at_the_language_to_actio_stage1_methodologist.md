# Methodologist — stage1

# Methodological Review: "Measuring Intensity Words at the Language-to-Action Boundary"

---

## Experimental Design Assessment

### Overall Soundness

The core design is methodologically sound for its stated scope. The decision to use a deterministic backend as a measurement instrument rather than as the object of study is the paper's most important design choice, and it is the right one. It cleanly isolates the language-to-action translation step as the single stochastic element in the pipeline, which is exactly what the research questions require. The two-condition structure (no-context vs. context-conditioned) is well-motivated and maps directly onto the three empirical questions.

### Strengths

**Isolation logic is solid.** The deterministic solver means that all output variance is attributable to the model's interpretation, not to downstream noise. This is a meaningful methodological contribution for a measurement study — the instrument is well-designed.

**The no-context / context-conditioned split is appropriate.** These are genuinely different measurement regimes, and treating them as separate conditions rather than collapsing them is correct. The factorial structure (10 words × 10 baselines × 30 runs) is appropriate for the nonparametric decomposition that follows.

**Strategic baseline selection is defensible.** The mix of round and irregular values (0%, 5%, 10%, 18%, 25%, 32%, 50%, 53%, 75%, 89%) is explicitly motivated and the rationale is stated. This is better than a uniform grid for hypothesis-driven exploration and is honest about what it cannot test (transition points, round-number effects at full resolution). The paper correctly identifies the denser grid as future work.

**The exact-number control is good practice.** Validating that the harness transmits numeric requests correctly is a necessary sanity check that many papers omit. Its presence here is commendable.

**Temperature comparison is appropriately scoped.** Two temperatures is not a full sensitivity analysis, but it is enough to support the claim that the structural patterns are not temperature artifacts. The claim made — that temperature broadens distributions without restoring ordinal distinctions — is supported by what is shown.

### Weaknesses

**Single-direction design is a significant constraint.** All trials use increase instructions. This is acknowledged in the limitations and future work sections, but it is worth being explicit about what this means methodologically: the behavioral modes (hedge, act, abstain) and the compression patterns are documented only for the upward case. Whether these are symmetric is genuinely unknown, and the paper should be careful not to imply generality of the mode-switching finding to "near-boundary behavior" in general, since the lower boundary (0%) is untested.

**The 89% baseline is the only near-boundary observation.** The abstention finding is compelling, but it rests on a single baseline value. The paper does not know whether the transition to abstention behavior is sharp (occurring between 75% and 89%) or gradual. Given that this is one of the paper's most distinctive findings, the absence of intermediate data points (say, 80%, 85%) is a real gap. The paper acknowledges this, but readers should understand that the "three behavioral modes" finding is based on a single boundary observation.

**No-context condition has only one starting state.** The no-context condition measures the model's word-to-number mapping from the default state, but "default state" is not defined in the paper with sufficient precision for a reader to understand what the model is responding to. If the default state is, say, 33% (equal allocation across three tasks), then the no-context results are specific to that starting point. The paper does not report what the default state is, which is a reproducibility gap (addressed further below).

**The system prompt and tool schema are not reported.** The model's behavior in a tool-calling context is highly sensitive to how the tool is defined, what the system prompt says, and how the task is framed. None of these are provided. This is the most significant reproducibility concern in the paper.

---

## Statistical Methods Review

### Appropriateness of Nonparametric Tests

The choice of nonparametric methods throughout is correct and well-justified. The output distributions are discrete, concentrated on a small number of values, and clearly non-normal (30 runs all producing the same value is the extreme case). Kruskal-Wallis H and Spearman's ρ are appropriate. The epsilon-squared effect size is the correct companion to Kruskal-Wallis and is rarely used in ML papers; its inclusion here is a genuine methodological strength.

### Multiple Comparison Issue — The Author's Primary Concern

The paper runs multiple Kruskal-Wallis tests and multiple Spearman correlations across conditions and baseline splits without correction. This is the most significant statistical concern, and the paper's acknowledgment of it needs to be assessed carefully.

**What the paper currently says:** The limitations section states that multiple-comparison correction was not applied. This is present but brief.

**Is it adequate for a preprint?** Marginally, but it could be strengthened with minimal effort. The issue is not just that corrections are absent — it is that the paper makes several claims that depend on p-values from individual tests (e.g., Spearman ρ = 0.845, p < 0.001 in the no-context condition; the Kruskal-Wallis result for word identity). For the no-context condition, the concern is minor because the effect sizes are so large (ε² = 0.969) that no correction would change the conclusion. For the context-conditioned condition, where ε²_word = 0.079, the concern is more real. The split-range decomposition (reporting separate ε² values for low vs. high baselines) involves multiple tests on the same data, and the 65.3% / 12.5% / 88.0% / 6.5% figures are presented without acknowledging that these are post-hoc splits.

**Recommendation (see below):** Add one sentence to the limitations section explicitly noting that the split-range decomposition is exploratory and post-hoc, and that the reported variance proportions should be treated as descriptive rather than inferential. This is a small addition that substantially improves the honesty of the statistical framing.

### The Spearman ρ Computation — A Methodological Ambiguity

The paper reports Spearman ρ = 0.845 (p < 0.001) for the no-context condition. The paper says this is computed between "tier and output." There are two plausible ways to compute this:

1. Correlate the tier number (1–6) with the median output per word (10 data points).
2. Correlate the tier number with all individual run outputs (300 data points), treating each run as an observation.

These will produce different values and different p-values. With n = 10 (medians), the p-value computation is based on only 10 paired observations, which is a very small sample for a correlation. With n = 300, the p-value will be extremely small regardless of the actual correlation, because the sample size inflates significance. The paper does not specify which was used. This needs to be stated explicitly.

Similarly, the per-baseline Spearman ρ values in Figure 7 (ordinality across baselines) are computed with n = 10 words, meaning each individual ρ value has very low power and the p-values are not reported for these. The visual trend is compelling and the figure is appropriate for a descriptive claim, but the paper should not imply these individual correlations are statistically tested.

### Effect Size Reporting

The ε² values are the paper's strongest statistical contribution. The 10:1 variance ratio (ε²_baseline = 0.782 vs. ε²_word = 0.079) is a clear, interpretable finding. However, the paper should note that these two ε² values are not from the same test — they are from separate Kruskal-Wallis tests on the same data using different grouping variables. This is a valid approach, but it should be stated explicitly. A reader might wonder whether the two effects can simply be compared as a ratio, and the answer is "approximately yes, as descriptive quantities" but not "yes, as components of a single variance decomposition."

### The Abstention Statistic

The abstention finding (121/300 at 89%, with word-dependent patterns) is reported descriptively. No statistical test is applied to the word-by-abstention pattern. Given that several words show 0% abstention and others show 100%, a Fisher's exact test or chi-squared test would be straightforward and would support the claim that abstention rates differ by word. The current framing as a descriptive observation is defensible for a preprint, but the pattern is strong enough that a test would strengthen it.

### T=0.0 Non-Determinism

The paper notes that "4 of 10 words produce more than one distinct value across 30 runs" at T=0.0. This is an important observation that deserves slightly more attention. If the API is returning genuinely different outputs at temperature 0, either (a) the temperature parameter does not fully determinize the model, (b) there is randomness in the serving infrastructure, or (c) the prompt is hitting a boundary where the model's distribution is nearly flat between two tokens. The paper should acknowledge which of these it suspects, because this affects the interpretation of all T=0.0 results as "deterministic."

---

## Threats to Validity

### Internal Validity

**Confound: Prompt phrasing is not isolated from word choice.** The no-context prompt is "Architects should spend [WORD] more time on innovation." The context prompt is "The current innovation allocation is b%. I would like to [WORD] increase innovation." These are not the same syntactic frame. In the no-context condition, the word modifies a noun phrase ("more time"); in the context condition, it modifies a verb phrase ("increase"). It is possible that the model's behavior differs partly because of the syntactic context of the word, not just the presence or absence of the baseline number. This is a genuine confound that the paper does not acknowledge.

**Confound: "Architects" and "innovation" are semantically loaded.** The domain framing (architects, innovation, task allocation) is not neutral. The model may have domain-specific priors about what constitutes a "moderate" or "dramatic" change in innovation time for architects. A different domain framing (e.g., "server capacity," "budget allocation") might produce different compression patterns. The paper's framing as a measurement of "intensity words" is weakened if the results are domain-specific.

**Confound: The three-task constraint (sum to 100%) is implicit.** The model is operating under a constraint that allocations must sum to 100%, but the paper does not describe how this constraint is communicated to the model. If the model knows it is redistributing from other tasks, the intensity of its response may reflect not just the target word but also its model of how much disruption to other allocations is acceptable. This is a hidden variable.

### External Validity

**Single model.** All results are from Claude Haiku. The paper acknowledges this clearly and frames it as a first slice. The limitation is real: Claude Haiku is a smaller, cost-optimized model, and its compression patterns may not generalize to larger models, to models from other providers, or to fine-tuned variants. The paper should not say "vague language is compressed" as a general claim about LLMs — it should say "Claude Haiku compresses vague language in this context."

**Single domain.** The resource-allocation framing may produce results that are specific to the domain. The paper is appropriately cautious about this in the discussion, but the abstract's phrasing ("vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries") reads as a general claim. This should be qualified.

**Single action type.** Increase-only instructions. Already discussed above.

**API-accessed model, not open weights.** The model version is specified (claude-haiku-4-5-20251001), which is good. However, API-accessed models can change without notice. The results are timestamped to the experimental period, which is appropriate, but future readers cannot reproduce the exact model behavior.

### Construct Validity

**The Quirk taxonomy concern — the author's primary concern.**

The paper's framing of this issue is currently adequate for a preprint, but it could be tightened in one specific way. The current text says the tiers are "informed by Quirk et al.'s degree-modifier taxonomy" and that "only three of the 10 words appear in Quirk's explicit lists." This is honest. However, the paper then uses these tiers as the ordinal scale against which Spearman ρ is computed. This means the primary ordinal measure is circular in a subtle way: the researcher defines the ordering, then measures whether the model follows it.

This circularity is not fatal — it is the standard approach in psycholinguistic measurement when a ground truth ordering is not available — but it should be stated more explicitly. The current footnote ("A human validation survey using these 10 words is planned") addresses the gap but does not name the circularity. I recommend adding one sentence in the statistical methods section noting that the tier ordering is the researcher's hypothesis, not an empirical input, and that the Spearman ρ therefore measures agreement between the model's outputs and the researcher's prior ordering rather than agreement with a validated human scale.

**The "ordinal violation" label for *moderately*.**

The paper calls *moderately* an "ordinal violation" and annotates it as such in Figure 3. This framing has a subtle problem: if the tier ordering is researcher-hypothesized rather than validated, then *moderately* mapping below *slightly* is not a "violation" — it is evidence that the researcher's hypothesized ordering may be wrong for this word. The paper's interpretation (that *moderately* activates a "restraint heuristic") is plausible, but the label "ordinal violation" implies the researcher's ordering is the ground truth. Consider replacing "ordinal violation" with "ordinal anomaly" or "unexpected ordering" and making the interpretation more tentative.

**Abstention operationalization.**

Abstention is defined as "a non-error run that produces zero tool calls." This is operationally clear, but it conflates two possible behaviors: (a) the model decides not to act and says so, and (b) the model produces a response that does not include a tool call for other reasons (e.g., it produces a text response instead). The paper should state whether it distinguishes these cases and what the model's text response looked like in abstention cases. This matters for the "three behavioral modes" interpretation: if the model is explicitly reasoning "I cannot make a large increase because the allocation is already at 89%," that is a different finding than if it simply fails to invoke the tool.

### Statistical Conclusion Validity

**Multiple comparisons without correction.** Addressed above. The main concern is the split-range decomposition.

**Small n for per-baseline Spearman ρ.** Each per-baseline correlation is computed over 10 words, giving 10 paired observations. With n = 10, Spearman ρ has very limited power, and the individual p-values (if computed) would be unreliable. The figure is appropriate as a visualization of a trend, but the text should not imply these are statistically robust point estimates.

**The 10:1 ratio claim.** The claim that "starting allocation explains roughly 10 times more variance than word choice" is a clean, memorable finding. It is supported by the ε² values. However, the paper should note that this ratio is specific to the pooled context-conditioned condition and that the ratio inverts at low baselines (where word explains 5× more variance than baseline). The 10:1 figure is an average of two regimes that behave oppositely, and presenting only the average without prominent mention of the inversion could mislead readers about the nature of the effect.

---

## Reproducibility Assessment

### What Is Present (Good)

- Model identifier specified: `claude-haiku-4-5-20251001` ✓
- Two temperature values specified: T=0.0 and T=0.7 ✓
- Run count per cell: 30 ✓
- Total run count: 6,620 ✓
- Baseline values listed: {0, 5, 10, 18, 25, 32, 50, 53, 75, 89} ✓
- Session isolation described: fresh session, deep-copied state, no memory between calls ✓
- Synthetic data seed mentioned ✓
- Statistical tests named ✓

### What Is Missing (Critical)

**System prompt not provided.** The system prompt is the single most important missing piece. Tool-calling behavior in Claude is highly sensitive to system prompt content. Without it, another researcher cannot reproduce the experimental conditions.

**Tool schema not provided.** The `set_task_allocation` tool's schema (parameter names, types, ranges, descriptions) is not given. The model's behavior is sensitive to how the tool is described.

**Default state not defined.** The no-context condition uses a "default state," but the paper does not state what the default allocation values are. If the default is 33%/33%/34%, that is relevant context.

**The three tasks are not named.** The paper mentions "innovation" as the target task and "architects" as the role, but does not name the other two tasks or describe how they are described in the prompt. The model's behavior may depend on the relative framing of all three tasks.

**"Same synthetic data seed" is underspecified.** What data is seeded? Is there stochastic content in the environment that is being fixed? This needs clarification.

**No code or