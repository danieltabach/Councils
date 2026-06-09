# Domain Expert — stage1

### Technical Assessment

**Core contribution is technically sound with important caveats.**

The experimental design is the paper's strongest feature. The author correctly identifies that isolating the language-to-action translation step requires a deterministic backend, and then builds one. This is the right instinct. The model is genuinely the only stochastic component, which means the variance you measure is attributable to the right thing. That's not trivial to achieve and many papers in this space don't bother.

The statistical choices are appropriate and honestly reported. Kruskal-Wallis with ε² for nonparametric effect size comparisons is correct given the discrete, concentrated output distributions. Spearman ρ for ordinality is correct. The author's own flagging of the independence violation (30 runs per word are not independent, so p-values overstate significance) is exactly the kind of epistemic honesty that distinguishes real measurement work from significance-farming.

**However, there are genuine technical gaps:**

**1. The ε² comparison is the paper's central quantitative claim and it has a structural problem.** The author acknowledges this — "they come from separate tests rather than a single model" — but then continues to use the 10:1 ratio as the headline finding. The correct analysis is a two-way Kruskal-Wallis or, better, a mixed-effects model with word and baseline as factors and their interaction. Without this, you cannot cleanly attribute variance to either factor because they are correlated in your design (the model's response to a word changes systematically with baseline, which is itself your finding). The interaction is the story, but the statistical framing doesn't capture it. This is fixable and should be fixed before the paper is submitted to a venue that will have a statistician reviewer.

**2. The no-word control is absent.** The author flags this in future work, but it's not a minor gap — it's a hole in the central claim. If "slightly increase" maps to 0.50 and "increase" (no modifier) also maps to 0.50, then 0.50 is the model's default for any increase request, not a hedge on the word "slightly." The compression finding stands, but the "hedge" interpretation of 0.50 is currently unfalsified. This is cheap to run and should be in the paper.

**3. The word scale is researcher-constructed and unvalidated.** The author is transparent about this, but it creates a circularity risk: you measure whether the model preserves ordinal structure relative to a tier assignment you made. If "moderately" is genuinely ambiguous in English (it may activate a "keep things moderate" reading rather than a "moderate increase" reading, as the author correctly speculates), then the "ordinal anomaly" finding might be a misclassification of the word's actual human semantics rather than a model failure. The human survey isn't just a nice-to-have — it's required to interpret the anomalies correctly. The paper should be more explicit that findings like the "moderately" inversion are uninterpretable without the human baseline.

**4. The drastically/dramatically discontinuity is the most interesting finding and the least analyzed.** Two words in the same tier, both tier 6, produce categorically different behavior at the 89% boundary (7% vs. 97% abstention). The paper notes this and offers the "as much as possible" interpretation for "drastically," which is plausible. But this deserves more: What does the model actually say when it abstains on "dramatically"? Is it citing the constraint? Does it say the increase would be too large? The text responses during abstention are data the author has but hasn't analyzed. This is the paper's most alignment-relevant finding — a one-word swap between near-synonyms produces a categorical action difference at the most consequential boundary — and it gets one paragraph.

---

### Positioning in the Field

**What the paper correctly cites:**
- Cliff (1959) on adverb multiplier effects — correct and relevant
- Quirk et al. (1985) taxonomy — appropriate scaffolding
- Mosteller (1990) on probability expression variance — right parallel
- Zhang (2024) on LLM probability word miscalibration — the closest prior work
- BrittleBench (2026) on prompt sensitivity — relevant

**What's missing:**

**Calibration and uncertainty quantification literature.** Kadous & Sammut, and more recently Kuhn et al. (2023) on semantic uncertainty in LLMs, are directly relevant. If the model compresses words into fewer outputs, this is related to the model's uncertainty representation. The paper is in conversation with this literature whether it knows it or not.

**Scalar implicature and pragmatics.** The finding that "moderately" may activate a restraint heuristic rather than a magnitude heuristic is a classic scalar implicature problem. Grice's maxims, and the computational pragmatics literature (Frank & Goodman 2012, RSA model) would give the author theoretical vocabulary for why "moderately" behaves differently — it may be that the model has learned pragmatic interpretations of these words that differ from their literal scalar meanings. This is a significant gap. The RSA (Rational Speech Acts) framework would predict exactly the kind of context-sensitivity you observe: the model's interpretation of a word is not fixed but is conditioned on the feasible action space, which is precisely what the differentiation funnel shows.

**Tool-use and function-calling literature.** There's a growing body of work on LLM tool use reliability (Schick et al. 2023 Toolformer, and subsequent work on tool-call accuracy) that the paper doesn't engage with. The abstention finding — the model declining to invoke the tool — is directly relevant to tool-use reliability literature.

**Instruction following and specification gaming.** Kenton et al. (2021) "Alignment of Language Agents" and related work on specification gaming would give the author better vocabulary for the alignment framing. The paper's alignment claim is currently informal; connecting it to the formal specification problem literature would strengthen it.

**Human-computer interaction literature on natural language interfaces.** There's substantial HCI work on vague language in command interfaces (going back to Bolt 1980, and more recently work on conversational agents) that the paper ignores entirely. This is relevant because the "alignment problem" framing may be reinventing wheels that HCI researchers built 20 years ago.

---

### Alternative Approaches

**What I would have done differently:**

**1. Run the human survey first, or concurrently.** The entire interpretive framework depends on knowing what humans mean by these words. Running the experiment without this is like measuring a thermometer's accuracy without a reference temperature. The author has a planned survey — it should have been the first instrument, not the last. The paper would be twice as strong if it could say "humans assign these median values; the model assigns these; here is the gap."

**2. Use a factorial design with interaction terms.** Word × baseline is a 10 × 10 design. The author has 3,000 context-conditioned runs. A proper two-way analysis would let you test the word × baseline interaction directly, which is the mechanistic claim underlying the differentiation funnel. The current analysis describes the interaction visually but doesn't test it.

**3. Analyze the abstention text responses.** When the model abstains, it produces text. That text is data. What does the model say when it abstains on "considerably" but not on "drastically"? Does it cite the constraint? Does it express uncertainty? This would let you distinguish "the model understood the request but judged it infeasible" from "the model misunderstood the request." This is cheap and would significantly strengthen the boundary behavior section.

**4. Include a "decrease" condition in this paper, not as future work.** The asymmetry hypothesis (increase vs. decrease may behave differently) is directly testable with the existing harness. Leaving it as future work when you could run it for the cost of ~3,000 more API calls is a missed opportunity that reviewers will notice.

**5. Test the prompt framing more carefully.** The no-context prompt is "should spend [WORD] more time on innovation." The context prompt is "I would like to [WORD] increase innovation." These are different syntactic frames (adverbial modifier vs. adverb modifying a verb), which could contribute to the observed differences beyond the presence/absence of context. This is a confound worth acknowledging.

---

### Baselines and Comparisons

The paper doesn't have baselines in the traditional ML sense — it's a measurement study, not a comparative study. This is appropriate given the research question. However:

**The no-word control is the one missing baseline that matters.** Without it, the compression finding is solid but the hedge interpretation is not. This is the single most important missing condition.

**The exact-number control is good** — it validates the harness. This is the right sanity check.

**The temperature comparison is handled well.** Running T=0.0 and T=0.7 and showing structural persistence is the right robustness check for this type of study.

**What's missing as a comparison:** The paper would be significantly stronger with even one other model. Not because one model is insufficient for the measurement study, but because the author's own vision document identifies cross-model comparison as the alignment-relevant extension. If GPT-4o shows different compression patterns, that's a finding about training pipelines. If it shows the same patterns, that's a finding about language itself. Running even a single comparison model on the no-context condition (300 runs × 2 temperatures = 600 calls) would transform the paper's scope claim.

---

### Impact Assessment

**Honest assessment: this is a solid empirical first paper with a genuine finding, but the cornerstone verdict is (c), not (a).**

The author asked for a verdict between (a) legitimate elevation, (b) retrofit/grandiosity, and (c) something between. It's (c), but closer to (a) than the author's doubt suggests and closer to (b) than the author's framing suggests.

**What the paper actually establishes that is durable:**
- A clean measurement instrument for language-to-action translation
- The compression finding (10 words → 5 outputs) is real and replicable
- The state-dominance finding is real and has direct deployment implications
- The three-mode boundary behavior (hedge/act/abstain) is the most novel finding and is genuinely interesting

**What the paper does not establish:**
- That this is a model failure rather than accurate modeling of human ambiguity (requires the human survey)
- That the patterns are general rather than Claude Haiku-specific (requires cross-model)
- That the "alignment problem" framing is the right frame rather than "calibration problem" or "pragmatics problem"

**If the claims hold and the extensions are run:** This program has genuine impact potential. The deployment-external safety science framing is real and underdeveloped. The closest existing work is in HCI (natural language interfaces) and calibration (probability word studies), but neither has focused on the action case with the rigor this paper brings. The clinical safety analogy in the vision document is apt and the field gap is real.

**Where to publish this paper:** Not a top ML venue in current form. The right venues are: NLP4Science workshops, the ACL/EMNLP workshop on human evaluation of NLP systems, or the AAAI/ACL workshop on NLP for human-AI interaction. A stronger version with the human survey and one cross-model comparison could reach ACL or EMNLP findings. The alignment framing could get it into the NeurIPS alignment workshop track.

---

### Technical Red Flags

**1. The ε² = 0.969 in the no-context condition is explicitly flagged as inflated, but the inflation is larger than acknowledged.** When T=0.0 and four of ten words produce identical outputs across all 30 runs, the within-group variance for those four words is exactly zero. Kruskal-Wallis ε² in this situation will approach 1.0 trivially. This doesn't invalidate the finding (the compression is real), but reporting ε² = 0.969 as a meaningful statistic is misleading. The paper should either not report this number or replace it with a more appropriate measure of discrimination (e.g., the number of distinct median values, which is already reported as 5).

**2. The split-range analysis (the 5:1 / 14:1 inversion) was not pre-registered.** The author correctly flags this: "the split point was chosen by the researcher based on observed convergence behavior, not pre-registered." This is honest but it means the specific ratios are exploratory and should not be treated as confirmatory. The inversion is visible in the figures and is real; the specific numbers are post-hoc and should be presented as descriptive.

**3. The $250K downstream consequence figure is the only number that will get quoted in non-technical contexts, and it's the least defensible.** It's specific to a synthetic environment with synthetic data. The paper correctly notes this, but the number is prominent enough that it will be extracted from context. Consider either removing it or adding a stronger caveat that the magnitude is entirely an artifact of the synthetic parameterization.

**4. The "drastically" finding is presented as the paper's most striking result, but the mechanism is unexamined.** The interpretation ("as much as possible") is plausible but untested. An alternative explanation: "drastically" may have a different distributional context in the training data — it may appear more often in contexts where extreme action is taken regardless of constraints (e.g., "the company drastically cut costs"), while "dramatically" may appear more often in contexts where the action is described as dramatic but constrained. If this is true, the finding is about training data distribution, not about the model's constraint reasoning. The paper should acknowledge this alternative.

**5. The no-context condition uses a different syntactic frame than the context condition.** "Should spend [WORD] more time" vs. "I would like to [WORD] increase." This is a confound that could contribute to the observed differences between conditions independent of the presence or absence of numerical context. It's not fatal but it should be acknowledged as a limitation.

**Direct answer to the author's cornerstone question:** The paper can bear weight, but not the full weight of the vision as currently framed. The instrument is real. The measurement is clean. The findings are genuine. But the "deployment-external safety science" framing requires the human baseline to be load-bearing, and it isn't in this paper yet. The correct sequencing is: run the human survey (which closes the ordinality validation gap and enables the human-model comparison simultaneously), then run cross-model comparison, then make the field-defining claim. In the current form, the paper is a strong first instrument paper that gestures toward a larger program. That's valuable. It's not the cornerstone yet. It becomes the cornerstone when you can say: "humans interpret these words this way; the model interprets them that way; here is the gap; here is whether the gap is model-specific or universal." You're one study away from that claim.