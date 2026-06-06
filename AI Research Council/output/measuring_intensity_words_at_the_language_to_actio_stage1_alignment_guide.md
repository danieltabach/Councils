# Alignment Guide — stage1

# Alignment Guide Review

## Paper: "Measuring Intensity Words at the Language-to-Action Boundary"

---

### Stated Goals vs. Delivered Content

**Goal 1: Frame as a psycholinguistic measurement study, not a tool-calling paper.**

This is the most important framing test, and the paper mostly passes it — but with a persistent tension. The abstract, introduction, and conclusion all foreground the psycholinguistic question correctly: the subject is word interpretation, the tool call is the instrument. The phrase "language-to-action boundary" in the title and throughout the text does real work here.

However, the framing slips in several places. The Methods section describes the environment in terms that read more like a systems paper than a measurement study: "deterministic solver," "role has three task allocations," "structured tool." A reader arriving cold at Section 3.2 would not immediately know they are reading a psycholinguistics-adjacent measurement paper. The environment description is necessary, but it currently reads as though the environment is the object of study rather than the instrument. One sentence at the top of Section 3.2 — something like "The environment is described here as a measurement instrument; the object of study remains the word-to-number translation" — would anchor the framing.

The Discussion paragraph titled "Alignment framing" also partially re-frames the paper as an AI alignment piece. This is not wrong, but it introduces a third framing (after psycholinguistics and measurement) that is not established in the introduction. A reader tracking the paper's thesis may find this paragraph slightly disorienting.

**Goal 2: Establish priority and timestamp on experiment design and initial results.**

Fully delivered. The method is described with enough specificity (model version, run counts, temperature values, baseline grid, prompt templates) to establish priority. The "first measurement slice" framing appears explicitly in the conclusion. This goal is met.

**Goal 3: Three empirical questions answered.**

All three questions are answered, and the answers are clearly organized. The mapping is:
- Q1 → Section 4.1 (compression and coarse ordinality) ✓
- Q2 → Section 4.2 (context dominates word choice) ✓
- Q3 → Section 4.3 (boundary behavior: hedge, act, abstain) ✓

The four stated contributions in the introduction are all delivered by the results. The contribution list and the results are well-aligned.

---

### Scope Drift Analysis

**Section 4.4: Downstream Consequences.**

This section exists to show that linguistic differences "propagate into materially different outcomes." The dollar figures (~$250K spread) are specific to a synthetic environment and the paper explicitly acknowledges this. However, the section currently reads as though the downstream consequence is a finding rather than a demonstration. The paper's thesis is about the word-to-number translation, not about what happens after that translation. This section is not wrong, but it risks re-framing the contribution as "this matters for production systems" — a claim the paper explicitly disclaims elsewhere. The section should be shortened and its instrumental role made explicit: it exists to confirm that the measurement instrument has consequential outputs, not to claim real-world impact.

**Discussion: "Mechanistic Speculation" paragraph.**

This paragraph speculates about why the model hedges at 0.50 (training data frequency, RLHF effects, maximal non-commitment). These are interesting hypotheses, but they are not tested and not supported by data in this paper. The paragraph is appropriately flagged as speculation, but it introduces a mechanistic framing that is not part of the paper's stated scope. For a preprint, this is acceptable as a discussion element, but it should be clearly demarcated as outside the paper's empirical scope. Currently it is labeled "Mechanistic speculation" which is honest; consider adding a sentence that explicitly says this is outside the current study's scope.

**Discussion: "Alignment framing" paragraph.**

As noted above, this paragraph introduces a third framing (AI alignment) that is not established in the introduction. The paper's introduction uses the word "alignment" only in passing. If this framing is important, it should appear in the introduction. If it is not central, the paragraph should be shortened to a sentence or two.

---

### Redundant Sections

**Figures 2 and 2b (frequency map and medians bar chart).**

Both figures show the same no-context T=0.0 result. Figure 2 (frequency heatmap) shows the distribution; Figure 2b (bar chart) shows the medians. The bar chart adds the tier color coding and the explicit "ordinal violation" annotation, which are useful. But the two figures together take substantial space to convey what could be one figure. For a preprint this is acceptable, but if the paper is later submitted to a venue with page limits, one of these should move to an appendix. The frequency heatmap (Figure 2) carries more information; the bar chart is more readable. Consider whether both are necessary at this stage.

**Figures 3 and 4 (convergence line plot and delta heatmap).**

These two figures both show the context-conditioned results: Figure 3 shows absolute allocation by baseline, Figure 4 shows delta (change) by baseline. They are complementary rather than redundant — the delta view is important for the "differentiation funnel" argument — but the paper could more explicitly state why both are needed. The current text references both but does not explain the division of labor between them.

**Figure 4b (separation panel).**

This figure directly summarizes the differentiation gap already visible in Figure 4. It is a useful summary but is partially redundant with Figure 4. For a preprint, keeping it is fine; it makes the gap argument more legible for a general audience.

---

### Missing Sections

**1. No explicit statement of what the paper does NOT claim.**

The paper correctly scopes itself as a "first measurement slice" and lists limitations. However, there is no single location where the paper states clearly what it is NOT claiming. Given that the paper will be shared on LinkedIn and in conference pitches, a brief "Scope and Non-Claims" note — either as a paragraph in the introduction or as the first paragraph of the limitations section — would prevent misreading. Specifically, the paper should state explicitly: (a) no claim about production system behavior, (b) no claim that the model is performing worse than humans, (c) no claim that these results generalize beyond Claude Haiku. These are all implied by the limitations section but are scattered rather than consolidated.

**2. The Quirk taxonomy framing needs one more sentence of explicit distance-setting in the introduction.**

The introduction says the 10 words "span Quirk's categorical range" and that only three appear in Quirk's explicit lists. This is honest. But the paper does not yet say, in the introduction, what the consequence of this is for interpreting the results. The footnote in the Methods section (Table 1) handles this for the methods, but a reader of the introduction who does not read footnotes carefully may over-interpret the Quirk connection. One sentence in the introduction — "The tier assignments are researcher-constructed and should be read as a hypothesis about ordering, not as a validated psycholinguistic instrument" — would close this gap at the point where the reader first encounters the taxonomy claim.

**3. No description of the prompt templates beyond paraphrase.**

The paper describes the no-context prompt as "Architects should spend [WORD] more time on innovation" and the context-conditioned prompt as "The current innovation allocation is b%. I would like to [WORD] increase innovation." These are paraphrases. For a paper whose central claim is about how word choice affects model output, the exact prompt templates should appear somewhere — either in the Methods section or in an appendix. A reader who wants to replicate or extend this work cannot do so from paraphrases alone. This is the most significant reproducibility gap in the current draft.

**4. No explicit statement of what "abstention" means operationally in the no-context condition.**

The paper defines abstention as "a non-error run that produces zero tool calls" in the context-conditioned condition. It is not stated whether abstention was observed in the no-context condition, or whether abstention is even possible in that condition. Since the no-context condition does not supply a current allocation, the model may behave differently. This should be clarified.

---

### Structural Recommendations

**1. Add a "Scope" sentence to the abstract.**

The abstract is strong but does not explicitly state that this is a single-model, single-domain, single-direction study. One sentence — "Results are specific to one model (Claude Haiku), one synthetic domain, and increase-only instructions; generalization is a question for follow-on work" — would prevent the abstract from being read as a broader claim than it is. This is especially important given that the abstract will be the primary text read on ArXiv and LinkedIn.

**2. Move the Quirk taxonomy qualification forward.**

Currently the main qualification of the Quirk taxonomy appears in Table 1's caption and in the Methods section footnote. The introduction mentions it but briefly. For a paper whose framing depends on the Quirk connection, the qualification should appear in the introduction at the point where Quirk is first invoked — not only in the methods.

**3. Consolidate the limitations.**

The paper has limitations scattered across three locations: the Methods section (footnote about human validation), the Discussion section (a "Limitations" paragraph), and the Future Work section (which re-states most of the same limitations as planned extensions). For a preprint, this is acceptable. For a cleaner read, consider consolidating all limitations into one paragraph in the Discussion and having the Future Work section focus only on what is planned, not on re-stating what is missing.

**4. The Results section uses two different organizational schemes.**

The introduction states three empirical questions. The Results section has five subsections (4.1–4.5). The mapping is: Q1→4.1, Q2→4.2+4.3, Q3→4.4 (boundary), with 4.5 (downstream consequences) and 4.6 (temperature robustness) as additional findings not tied to the three stated questions. This mismatch is minor but creates a small coherence gap. Either reframe the introduction to list five findings rather than three questions, or add a sentence at the start of Section 4 mapping the five subsections to the three questions.

**5. The "Downstream Consequences" subsection should be explicitly framed as a validity check.**

Currently it reads as a fourth finding. It should be framed as confirming that the measurement instrument has real stakes — i.e., it validates that the numeric allocation differences are not trivial. This re-framing keeps the paper's thesis on word interpretation and prevents the dollar figures from being read as the paper's main claim.

---

### Title and Abstract Accuracy

**Title: "Measuring Intensity Words at the Language-to-Action Boundary"**

The title is accurate and well-chosen. "Measuring" correctly signals a measurement study rather than a model-building or optimization paper. "Intensity words" correctly identifies the subject. "Language-to-action boundary" correctly identifies the construct. The title does not over-claim. It is appropriately scoped for a preprint.

One minor note: the title does not signal that this is an LLM study. A reader browsing ArXiv might read this as a psycholinguistics paper about human subjects. This is not necessarily wrong — the paper wants to be read as psycholinguistics-adjacent — but it may affect discoverability in CS/ML venues. This is a judgment call, not a flaw.

**Abstract accuracy:**

The abstract accurately represents the paper's content. The three patterns (compression, state dominance, boundary modes) match the three empirical questions and the three main results sections. The specific statistics cited (Spearman ρ = 0.845, ε² values, the 10:1 ratio) are all present in the paper. The final sentence ("Vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries") is an accurate summary of the findings.

One gap: the abstract does not mention that the word scale is researcher-constructed rather than validated. A reader of the abstract alone may assume the 10-word scale has psycholinguistic validation. Adding "using a researcher-constructed 10-word scale informed by Quirk et al.'s degree-modifier taxonomy" would be accurate and would set the right expectation.

---

### Special Attention: Author's Three Concerns

**Concern 1: Quirk Taxonomy Honesty**

The current framing is adequate for a preprint but has one gap. The paper is honest in three places: the introduction, Table 1's caption, and the Future Work section. However, these qualifications are not co-located with the paper's strongest uses of the Quirk framing. Specifically, the abstract says the paper "tests 10 intensity words spanning six hypothesized tiers of the Quirk et al. degree-modifier taxonomy" without immediately noting that the mapping is by analogy. The word "hypothesized" does some work here, but it is subtle. For a preprint, the current framing is defensible. To make it bulletproof, add "by analogy rather than direct inclusion" or equivalent language in the abstract itself, and ensure the introduction's qualification appears before the first substantive use of the tier structure.

The footnote approach (Table 1) is appropriate for the methods. The introduction qualification is appropriate for context-setting. The gap is only in the abstract, which is the most-read section.

**Concern 2: Statistical Rigor**

The paper's acknowledgment of its statistical limitations is adequate for a preprint with the stated scope. Specifically:

- The absence of multiple-comparison correction is acknowledged implicitly through the "first measurement slice" framing and the limitations paragraph. However, it is not stated explicitly. For a preprint, adding one sentence — "No multiple-comparison correction is applied; the tests are treated as exploratory rather than confirmatory" — in the statistical methods paragraph would make this explicit rather than implicit.

- The absence of a human baseline is acknowledged clearly in the limitations section and the future work section. The paper correctly does not frame compression as "model failure" without a human comparison. This is well-handled.

- The researcher-hypothesized ordinality is acknowledged in Table 1, the introduction, and the future work section. This is sufficient.

- The ε² values for the no-context condition (ε² = 0.969) are very large and may attract scrutiny. The paper does not note that this high value is partly a consequence of the near-zero variance in the lower-tier words (all 30 runs at exactly 0.50), which makes the between-group variance almost mechanical. This is not a flaw in the analysis, but noting it would preempt a reviewer objection.

- The claims are not oversold given the scope. The paper consistently uses hedged language ("the model compresses," "these effects persist," "this suggests") rather than causal or universal language. The statistical claims match the statistical evidence.

**Concern 3: Clarity and Flow**

The five-block results structure works. The paper reads coherently front-to-back with one exception: the transition from Section 4.3 (boundary behavior) to Section 4.4 (downstream consequences) is abrupt. Section 4.4 introduces a different type of evidence (dollar values) without a bridging sentence explaining why this section follows from the previous one. A one-sentence transition — "Having documented how words map to allocations, I now confirm that these differences produce materially different downstream outcomes" — would smooth this.

The limitations are clearly stated and not understated. The Future Work section is appropriately scoped: it lists specific, concrete extensions rather than vague gestures toward "more research." The round-number anchoring observation in the Discussion is correctly flagged as preliminary and visual rather than statistical.

The one flow issue worth flagging: the paper introduces the "differentiation funnel" concept in Section 4.2 but does not use this term in the abstract or introduction. If this is a key conceptual contribution, it should be seeded earlier. If it is a descriptive label, it can stay where it is.

---

### Summary for ArXiv Readiness

The paper is ready for ArXiv with minor revisions. The core alignment between stated goals and delivered content is strong. The three empirical questions are answered, the four contributions are delivered, and the "first measurement slice" framing is consistently maintained. The two most important pre-submission fixes are: (1) add the researcher-constructed scale qualification to the abstract, and (2) add exact prompt templates in an appendix for reproducibility. Everything else identified above is either already handled adequately for a preprint or is a refinement rather than a gap.