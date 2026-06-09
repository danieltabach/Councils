# Methodologist — stage1

# Methodological Review: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"

---

## Experimental Design Assessment

### Strengths

**Isolation logic is sound.** The core design insight — building a deterministic backend so the model is the only stochastic component — is methodologically correct and well-executed. This is not a trivial choice; most LLM behavioral studies conflate model variance with system variance. The author correctly identified that isolating the language-to-action boundary requires removing all other sources of variation downstream.

**The two-condition structure is appropriate.** Separating no-context (Tier 1) from context-conditioned (Tier 2) conditions directly operationalizes the theoretical distinction between intrinsic word semantics and context-modulated interpretation. This is the right design for the research questions asked.

**30 runs per cell is defensible but tight.** For nonparametric tests with the observed effect sizes, 30 runs provides adequate power to detect large effects. The author is honest that this is a cost-constrained choice.

**The 10-point baseline grid is strategically chosen.** The deliberate mix of round and irregular values is a thoughtful design decision that most papers in this space would not make. It enables the round-number anchoring observation, even if that observation remains informal.

### Weaknesses and Design Flaws

**The word scale is the central validity problem.** The 10 words are assigned to 6 tiers by researcher judgment, informed by but not drawn from Quirk's explicit lists. This means the "hypothesized ordinal ranking" is the researcher's ranking, not a validated human ranking. Every finding that references ordinal preservation or violation is therefore relative to a ground truth that has not been established. The author acknowledges this in a footnote and in Limitations, but the problem is more serious than the paper treats it: the primary dependent claim — that the model "compresses" the scale — requires knowing what the correct uncompressed scale is. Without the human baseline, the finding is technically: *the model does not reproduce the researcher's hypothesized ordering at fine granularity.* That is a weaker claim than compression relative to human interpretation.

**The no-word control is absent.** The paper acknowledges this gap, but it is more than a "hole to patch." The 0.50 hedge finding — arguably the most cited-ready result — cannot be cleanly interpreted without knowing whether 0.50 is the model's response to *any* increase instruction regardless of modifier. If "increase innovation" without any adverb also produces 0.50, the hedge interpretation is undermined: the model may simply be anchoring at the midpoint of the allocation space as a default, with the intensity word having no effect at all in the weak-word regime. The current framing treats 0.50 as a semantically meaningful hedge; it may instead be a null response.

**The prompt template is not fully specified.** The paper provides two prompt templates but does not reproduce the complete system prompt, tool schema, or any role-framing instructions that the model receives. This is a reproducibility and construct validity issue. The model's behavior is a function of the entire context window, not just the instruction sentence. The system prompt in particular can substantially influence whether the model interprets "innovation allocation" as a resource to maximize, a parameter to be cautious with, or something else entirely. The abstention behavior near 89% is especially sensitive to this: whether the model cites constraint violations depends heavily on how the task and constraints are framed in the system prompt.

**Single domain, single framing.** All prompts concern "innovation allocation" for "Architects." The word "innovation" likely carries positive valence in training data, which may inflate the model's willingness to increase it. "Drastically reduce innovation" would be a different test. More importantly, the domain is a resource-allocation task in a professional/business register, which may activate different behavioral patterns than, say, a medical dosing context or a financial risk context. The generalization claim in the abstract ("what happens when vague human language must become a precise LLM action?") is broader than the single domain tested.

**The abstention operationalization conflates two things.** Abstention is defined as "a non-error run that produces zero tool calls." But there are at least two distinct reasons a model might produce zero tool calls: (a) it judges the requested action infeasible given the constraint, or (b) it fails to invoke the tool for other reasons (misunderstanding, refusal on other grounds, etc.). The paper reports that abstaining runs "typically" cite the constraint, but "typically" is not a complete characterization. Without coding the abstention responses, the abstention rate conflates constraint-aware refusal with other non-action behaviors.

---

## Statistical Methods Review

### Appropriate Choices

**Nonparametric tests throughout.** Given that outputs are discrete, concentrated on a small number of values, and clearly non-normal, Kruskal-Wallis and Spearman's ρ are the correct choices. Using ANOVA or Pearson correlation here would be a methodological error; the author correctly avoids this.

**ε² as effect size for Kruskal-Wallis.** This is the appropriate effect size for this test and is correctly interpreted as proportion of rank-based variance explained.

**Honest treatment of inflated ε² at T=0.0.** The paper explicitly flags that ε²_word = 0.969 in the no-context T=0.0 condition is inflated by deterministic decoding producing zero within-group variance. This is the correct disclosure and is the kind of self-correction that distinguishes careful from careless analysis.

### Problems

**The independence violation is more serious than acknowledged.** The paper notes that "runs within the same word are not independent" and says p-values "overstate significance." This is correct but understated. At T=0.0, four words produce the *exact same value* across all 30 runs. These are not 30 independent observations; they are one observation repeated 30 times. The Spearman ρ computed over n=300 observations treats these as 300 data points, but the effective sample size for the no-context T=0.0 condition is closer to 10 (one median per word) or at most the number of distinct values observed. The p-values reported are not merely "overstated" — they are essentially meaningless as inferential quantities. The author should either (a) compute ρ over word-level medians (n=10) and report the correct uncertainty, or (b) use a permutation test that respects the clustering structure. The descriptive framing partially covers this, but the p < 0.001 notation alongside a non-independent sample will be read as inferential by most readers.

**The two separate Kruskal-Wallis tests cannot be directly compared the way the paper implies.** The paper correctly states that ε²_baseline = 0.782 and ε²_word = 0.079 come from separate tests and "should not be added together or treated as shares of a single pie." But then the paper repeatedly uses the ratio (10:1, 14:1, 5:1) as if it is a meaningful quantity. A ratio of effect sizes from two different tests on the same data is not a standard statistical quantity. The correct approach would be a two-way Kruskal-Wallis (or a mixed-effects model with both word and baseline as factors) that partitions variance jointly. The current approach cannot distinguish: (i) baseline explains more because it has more levels (10 vs. 10 levels, so this is not the issue here), (ii) baseline explains more because the two factors are correlated and baseline captures shared variance, or (iii) baseline genuinely dominates word in a causal sense. The finding is directionally credible but the 10:1 framing is not statistically grounded.

**The split-range analysis is post-hoc and unregistered.** The paper acknowledges this: "the split point was chosen by the researcher based on observed convergence behavior, not pre-registered." This is the correct disclosure. But the specific numbers reported (65.3% vs. 12.5% at low baselines; 88.0% vs. 6.5% at high baselines) are derived from data-driven splits and should not be treated as confirmatory. They are descriptive characterizations of a pattern, not tests of a hypothesis. The paper's framing is mostly appropriate but occasionally slides toward treating these as established quantities.

**No correction for multiple comparisons, appropriately disclosed.** The paper correctly frames all p-values as descriptive. This is the right call for an exploratory study, but it should be stated more prominently — ideally in the Methods section rather than only at the end of the statistical approach paragraph.

**The Spearman ρ = -0.501 (p < 0.001) for the relationship between starting allocation and magnitude of change** has the same independence problem as the no-context ρ. Each data point is a (baseline, output) pair, but there are 30 runs per (word × baseline) cell, so the effective n for this correlation is at most 100 (10 words × 10 baselines), not 3,000. The p-value is meaningless at n=3,000 with clustered data.

---

## Threats to Validity

### Internal Validity

**Construct validity of the word scale.** The tiers are researcher-assigned. The finding that the model "violates ordinal ordering" for *moderately* depends entirely on the researcher having correctly placed *moderately* above the tier-1 and tier-2 words. The model's behavior (mapping *moderately* to 0.45) might be correct relative to actual human interpretation — *moderately* may genuinely mean "keep things moderate" rather than "increase by a moderate amount" in this context. Without the human baseline, the anomaly finding cannot be distinguished from a researcher miscategorization.

**Prompt confound.** The no-context prompt ("Architects should spend [WORD] more time on innovation") and the context prompt ("I would like to [WORD] increase innovation") have different syntactic structures beyond just the presence/absence of the baseline number. The no-context prompt uses "spend more time" while the context prompt uses "increase." These are not equivalent framings. Any difference between conditions could partially reflect the different verb constructions, not just the presence of context.

**The system prompt / tool schema is an uncontrolled variable.** As noted above, the complete prompt context is not reported. This is a significant internal validity threat because the model's calibration of "feasibility" — which drives the abstention behavior — is sensitive to how constraints are framed.

**Single model version.** The model is identified as `claude-haiku-4-5-20251001`. Model behavior can change with updates. The results are specific to this checkpoint.

### External Validity

**Single model.** All findings are specific to Claude Haiku. The paper correctly acknowledges this but the abstract's framing ("In this model and domain") is appropriate — the concern is whether the Discussion section occasionally generalizes beyond this. The "alignment framing" paragraph in Discussion, for example, makes claims about "model-mediated action interfaces" that go beyond what a single-model study supports.

**Single domain, single direction, single task structure.** Increase-only instructions in a resource-allocation task with a professional framing. The generalization to other domains (medical, financial, creative) is entirely unvalidated.

**Synthetic environment.** The allocation task is purpose-built. Whether the patterns hold in real deployed systems with richer prompts, multi-turn context, and more complex tool schemas is unknown.

**English only.** The findings are specific to English intensity words. Cross-linguistic behavior is entirely untested.

### Statistical Conclusion Validity

**The main risk is Type I error inflation** from the independence violation described above. The large effect sizes (ε² = 0.78, 0.97) are robust to this concern — these are not borderline findings that p-values are carrying. But the specific p-values reported should be understood as descriptive only.

**The $250K downstream consequence figure** is specific to the synthetic environment's objective function. The paper correctly notes this, but the number will be read as more general than it is. The finding that word choice propagates into outcome differences is valid; the specific dollar figure is not.

### Construct Validity

**"Compression" as a construct.** The paper uses "compression" to mean "multiple words map to the same output." This is a reasonable operationalization, but it conflates two distinct phenomena: (a) the model genuinely cannot distinguish the words, and (b) the model distinguishes the words but maps them to the same output because the task context doesn't require finer granularity. These have different implications. The first is a limitation of the model's semantic representation; the second is appropriate context-sensitivity. The paper does not separate these.

**"Abstention" as a construct.** As noted above, zero tool calls conflates constraint-aware refusal with other non-action behaviors.

---

## Reproducibility Assessment

### What Is Provided
- Model identifier (specific version string): ✓
- Temperature values: ✓
- Number of runs per cell: ✓
- Word list: ✓
- Baseline values: ✓
- High-level prompt templates: ✓
- Statistical tests used: ✓

### What Is Missing

**Critical gaps:**

1. **Complete prompt text.** The system prompt, tool schema definition (field names, types, constraints, descriptions), and any role-framing instructions are not provided. A replicator cannot reproduce the study without these. This is the single most important reproducibility gap. The model's behavior — especially the abstention pattern — is highly sensitive to how the tool and constraints are described.

2. **Random seed.** "Same synthetic data seed" is mentioned but the seed value is not reported.

3. **The deterministic backend specification.** The paper describes the backend as a "deterministic solver" that evaluates configurations, but the objective function is not specified. The $250K figure requires knowing the objective function. A replicator cannot verify or extend the downstream consequence analysis.

4. **Session initialization details.** "Fresh session, deep-copied state, no memory between calls" — what does this mean concretely for API calls? Are these single-turn calls? Is there a system prompt that persists across the 30 runs for a given cell?

5. **Abstention coding procedure.** How were abstentions identified? Was this automated (checking for empty tool_calls list) or manual? What happened to runs that produced tool calls with invalid values?

**Secondary gaps:**

6. The T=1.0 data is mentioned as collected but not analyzed. Its absence is noted but the reason (future revision) means the paper is incomplete as submitted.

7. The exact-number control results are mentioned but not reported in detail. These are the validation check for the harness; readers should be able to see them.

---

## Conclusions vs. Evidence

### Claims That Are Well-Supported

**"The model compresses 10 intensity words into 5 distinct median outputs."** Directly supported by Figure 2. This is a descriptive finding about this model in this condition, and it is stated accurately.

**"Grouping by starting allocation captures far more rank-based variance than grouping by word."** Supported by the two Kruskal-Wallis tests, with appropriate caveats about their separateness. The directional finding is credible even if the 10:1 ratio is not a standard statistical quantity.

**"Near feasibility limits the model exhibits three behavioral modes."** The abstention data at 89% is striking and well-documented. The characterization of three modes (hedge/act/abstain) is a reasonable description of the observed pattern.

**"These patterns persist across temperature."** The temperature comparison is appropriately modest — the paper correctly characterizes higher temperature as broadening distributions rather than restoring granular distinctions.

### Claims That Outrun the Evidence

**"The model's numeric interpretation of vague intensity words is compressed, state-dependent, and discontinuous near operational boundaries."** The first two are supported. "Discontinuous" is the strongest word here — the abstention finding is consistent with discontinuity but the paper tests only one near-boundary point (89%). A single boundary point cannot establish discontinuity versus a very steep continuous function. The paper would need at least 85%, 87%, 89%, 91%, 93% to characterize the transition.

**The "ordinal anomaly" framing for *moderately*.** This is presented as evidence that the model is behaving unexpectedly, but as noted above, it could be that the researcher's tier assignment is wrong. The word "anomaly" implies a deviation from a known correct ordering. The correct framing is: "the model's output for *moderately* falls below the researcher's hypothesized position for this word."

**The $250K consequence figure.** The paper correctly notes this is environment-specific, but the Discussion section's "alignment framing" paragraph uses language ("a narrow but important version of an alignment problem") that implicitly generalizes. The finding that word choice propagates into outcome differences is valid; the alignment framing requires the additional premise that users cannot detect or correct these differences, which is not tested.

**"Vague instructions should not be assumed to map to stable numeric actions."** This is the paper's practical conclusion, and it is stated in the Conclusion section. As a finding about Claude Haiku in a synthetic allocation task with increase-only instructions, the evidence supports it. As a general claim about LLM action interfaces, it overreaches — a single model, domain, and direction is insufficient basis for a general prescription.

**The Discussion's mechanistic speculation paragraph** (RLHF rewards moderate responses, 50% overrepresented in training data) is framed as "possibilities worth noting" rather than supported claims, which is appropriate. However, the paper should be clearer