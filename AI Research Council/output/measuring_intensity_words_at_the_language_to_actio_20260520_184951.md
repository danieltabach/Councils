# AI Research Council Report
**Paper:** Measuring Intensity Words at the Language-to-Action Boundary
**Date:** 2026-05-20 18:49:51
**Brief:** REVIEW TYPE: ArXiv readiness check with framing evaluation
TARGET: ArXiv preprint. This is the first published piece of a planned multi-model
research program. It will also be shared on LinkedIn, a personal blog, and used in
conference pitches and a research mentorship group (Algoverse). The paper explicitly
frames itself as a "first measurement slice," not a complete study.
STAGE: Near-final draft (v3). All statistics have been verified against raw data.
GOALS: (1) Establish priority and timestamp on the experiment design and initial
results — this is a portfolio piece to pitch and garner interest, not a final
conference submission. (2) Frame the paper as a psycholinguistic measurement study —
tool calling is the instrument, the optimizer is the testbed, the subject is word
interpretation. If the paper still reads like a "tool-calling paper," that framing
has failed.

CONCERNS — please give extra attention to:
1. QUIRK TAXONOMY HONESTY: The 10-word scale is organized by analogy to Quirk et al.'s
   (1985) degree-modifier taxonomy, but only 3 of the 10 words appear in Quirk's
   explicit lists. The remaining 7 were chosen to fill categorical gaps using terms
   natural to operational instructions. The paper already acknowledges this is a
   researcher-defined heuristic ordering, not an empirically validated scale. Is this
   framing currently sufficient for a preprint, or does it need further qualification?
2. STATISTICAL RIGOR: The paper uses nonparametric tests throughout (Kruskal-Wallis H,
   Spearman rho, epsilon-squared effect size) without multiple-comparison correction.
   There is no human baseline — ordinality is researcher-hypothesized. These limitations
   are acknowledged in the paper. Verify the acknowledgments are adequate and that
   statistical claims are not oversold given the stated scope.
3. CLARITY AND FLOW: Results are structured into 5 blocks under two empirical questions.
   Does this structure work? Does the paper read coherently front-to-back? Are the
   limitations clearly stated? Is the Future Work section appropriately scoped?

CONTEXT: This is a sole-author paper by a Georgia Tech ISyE student and Algoverse
research mentee. It is the author's first preprint. The paper uses first-person "I"
throughout. The experimental testbed is a synthetic constrained resource-allocation
environment — no production systems, no proprietary data, no deployment claims. The
goal is a sound preprint for ArXiv, not a polished NeurIPS submission. Known
limitations (single model, one direction, no human baseline, 10-point baseline grid)
are explicitly stated in the paper and scoped as future work.
**Cost:** $4.15 | **Tokens:** 25,503 in / 6,293 out

---

# AI Research Council — Final Report

## *Measuring Intensity Words at the Language-to-Action Boundary*

---

## Unified Assessment

**ArXiv readiness: YES, with targeted revisions.** The paper is sound, honest, and makes a genuine empirical contribution within its stated scope. The experimental design is clean, the figures are strong, and the boundary-behavior finding (hedge/act/abstain at 89%, particularly the *drastically*/*dramatically* asymmetry) is genuinely novel. All six reviewers converged on "ready for ArXiv with revisions" — none identified a fundamental flaw. The required revisions are concentrated in three areas: one technical claim that is currently stated incorrectly (the ε² ratio), one critical reproducibility gap (missing prompt/tool specifications), and a few framing tightenings. None require new experiments.

**Framing evaluation: PARTIALLY SUCCESSFUL.** The psycholinguistic measurement framing lands in the abstract, introduction, and conclusion. It leaks in two places: (1) the Methods section reads as a systems description without an anchoring sentence reminding the reader that the environment is the instrument, not the object; (2) the Discussion introduces an "alignment framing" paragraph that constitutes a third, unestablished frame. The paper successfully avoids reading as a "tool-calling paper" — that primary framing goal is met — but the word "psycholinguistic" never appears in the text, and the linguistic literature (Horn scales, scalar implicature, gradable adjectives) is absent. For the stated audience (ArXiv, LinkedIn, pitches, mentorship), the current framing is adequate. For a venue submission, the framing would need stronger linguistic grounding.

**On your three explicit concerns:**

1. **Quirk taxonomy honesty:** Adequate for a preprint, but the qualification needs to appear in the abstract (currently absent) and at the point of first analytic use in Section 4.1 (currently only in Methods footnote). One sentence each, no more.
2. **Statistical rigor:** Acknowledgments are mostly adequate, with one major exception — the "10× variance ratio" framing is technically incorrect, not just imprecise. This needs correction in three places (abstract, contributions, results). Two smaller fixes needed: explicit multiple-comparisons statement in Section 3.5, and caveat on ε² = 0.969 inflation.
3. **Clarity and flow:** The five-block structure works, but the mapping to the three empirical questions is not explicit. Add transition sentences. The "Downstream Consequences" section should be reframed as a validity check, not a fourth finding.

---

## Next Steps

### Critical (Must Fix Before Submission)

1. **Correct the ε² variance-ratio framing throughout the paper.** This is the single most important fix and was flagged independently by Methodologist, Domain Expert, Peer Reviewer, and Outsider. The claim "starting allocation explains roughly 10 times more variance than word choice (ε²_baseline = 0.782 vs. ε²_word = 0.079)" implies a joint variance decomposition that was not performed. These are ε² values from **two separate Kruskal-Wallis tests** on different grouping variables. They are not additive components of a single variance partition. Reword in three locations:
   - **Abstract:** Change "starting allocation explains roughly 10 times more variance than word choice" to something like "two separate Kruskal-Wallis tests show baseline grouping captures far more rank-based structure than word grouping (ε² = 0.782 vs. 0.079)."
   - **Contributions list (Introduction):** Same reframing.
   - **Section 4.2:** Add an explicit sentence: "These two ε² values come from separate Kruskal-Wallis tests with different grouping variables; they are not components of a joint variance decomposition, but their relative magnitudes indicate baseline grouping captures substantially more rank-based structure than word grouping."

2. **Add exact prompt templates, system prompt, and tool schema to an appendix.** Flagged by Source Auditor, Methodologist, Peer Reviewer, Domain Expert, Outsider, and Alignment Guide. The current paraphrased prompts ("Architects should spend [WORD] more time on innovation") cannot be reliably reproduced. Tool-calling behavior is highly sensitive to system prompt content and tool schema definitions. Add an appendix containing: (a) the exact user prompt strings for both conditions, (b) the system prompt (if any), (c) the full `set_task_allocation` tool schema, (d) the names of all three tasks and the default state values, (e) what the model "sees" about the sum-to-100% constraint.

3. **Fix the "Ordinal violation" label in Figure 2b and surrounding text.** Flagged by Methodologist, Domain Expert, Outsider, and Alignment Guide. Since the tier ordering is researcher-hypothesized, *moderately* mapping below *slightly* is not a "violation" — it is evidence the hypothesized ordering may be wrong for that word, or that *moderately* activates an instructional rather than quantitative reading. Replace "Ordinal violation" with "Ordinal anomaly" or "Unexpected ordering" in both Figure 2b and Section 4.1 text. Add one sentence acknowledging this could indicate miscategorization, not model error.

4. **Add explicit multiple-comparisons statement to Section 3.5.** Currently buried in Discussion limitations. Add one sentence: "No correction for multiple comparisons was applied; reported p-values should be interpreted as descriptive rather than confirmatory, consistent with the exploratory scope of this study." Additionally flag the split-range decomposition (65.3% / 12.5% / 88.0% / 6.5%) explicitly as post-hoc with a researcher-chosen split point.

5. **Provide complete bibliographic entry for BrittleBench (2026) and verify Zhang et al. (2024).** Flagged by Source Auditor. A 2026 citation with no full bibliographic entry cannot be verified by readers. Provide arXiv ID, authors, and date, or replace with a verifiable citation. Verify Zhang et al. (2024) is identifiable (specific venue, authors).

6. **Specify how Spearman ρ was computed.** Flagged by Methodologist and Peer Reviewer. The paper does not state whether ρ = 0.845 is computed over 10 word-level medians (n=10) or 300 individual run observations (n=300). These produce different statistics and different p-values; with n=300, observations are not independent (30 runs per word are highly correlated). State which was used and acknowledge the independence issue if n=300.

### Important (Significantly Improves the Paper)

1. **Add Quirk taxonomy qualification to the Abstract.** Currently absent from the most-read section. Add: "using a researcher-constructed 10-word scale informed by Quirk et al.'s degree-modifier taxonomy" or equivalent. Also add the same qualification to Section 4.1 at the point of first analytic use, not only in the Methods footnote.

2. **Add caveat on ε² = 0.969 in the no-context condition.** When four of ten words produce identical outputs across all 30 runs (zero within-word variance), between-group variance dominates mechanically. Add one sentence noting this effect size is partly a consequence of the deterministic decoding condition rather than a substantive finding about word distinctiveness per se.

3. **Reframe Section 4.4 (Downstream Consequences) as a validity check, not a finding.** The dollar figures should confirm that the measurement instrument has consequential outputs — not appear as a fourth finding. Shorten to a single paragraph and add a topic sentence: "Having documented how words map to allocations, this section confirms that these differences propagate into materially different downstream outcomes, validating the instrument's stakes."

4. **Add explicit Results-to-Questions mapping.** The Introduction promises three empirical questions; Results has five subsections. Either restructure the Results headers to match the three questions, or add one-sentence topic sentences linking each subsection to its question. The current mismatch creates a minor coherence gap.

5. **Clarify abstention operationalization.** Flagged by Methodologist, Peer Reviewer, Outsider. State explicitly whether abstaining runs produced (a) a refusal message, (b) a text response explaining infeasibility, or (c) silent non-invocation. This is important for interpreting whether the "three-mode policy" reflects principled reasoning or a different output failure.

6. **Acknowledge the syntactic frame confound between conditions.** Flagged by Methodologist and Outsider. The no-context prompt uses the word as a noun-phrase modifier ("[WORD] more time"); the context prompt uses it as a verb-phrase modifier ("[WORD] increase"). Add one sentence in Limitations acknowledging this is a confound that the design does not isolate.

7. **Address the alternative interpretation of the 10:1 ratio.** Flagged by Domain Expert and Outsider. The finding is consistent with two interpretations: (a) word meaning is unstable across contexts, or (b) word meaning is stably *relative* (e.g., "X% of available headroom"). The paper currently implies (a) without ruling out (b). Add one sentence in Discussion acknowledging this alternative.

8. **Add a scope sentence to the abstract.** Add: "Results are specific to one model (Claude Haiku), one synthetic domain, and increase-only instructions." This preempts overgeneralization on LinkedIn/ArXiv.

9. **Investigate or explicitly acknowledge T=0.0 non-determinism.** Flagged by Methodologist and Domain Expert. Four of ten words produce multiple distinct outputs at T=0.0. For a paper claiming T=0.0 as a deterministic baseline, this deserves more than a single sentence at the end of Section 4.5. Either investigate (API non-determinism vs. prompt boundary effects) or acknowledge openly that this is an unresolved methodological question.

### Recommended (Nice-to-Have Polish)

1. **Add one anchoring sentence at the top of Section 3.2** reminding the reader that the environment is the measurement instrument, not the object of study. This prevents the Methods section from reading as a systems paper.

2. **Add brief engagement with scalar implicature / Horn scales.** Flagged by Domain Expert and Outsider. The compression of *slightly*/*marginally*/*somewhat*/*mildly* into 0.50 may reflect linguistically principled scale structure (Horn 1972, Levinson 2000), not just model limitation. One paragraph in Related Work would strengthen the linguistic grounding for free.

3. **Soften the "alignment framing" paragraph in Discussion.** This paragraph introduces a frame not established in the Introduction. Either remove, shorten to one sentence, or seed in the Introduction.

4. **Note Figure 4 empty cells are abstentions in the caption.** A reader could interpret blank cells as missing data.

5. **Flag the non-monotonicity in Figure 3** for *drastically* at b=18% (V-shape). Currently undiscussed; one sentence would close the loop.

6. **Add citations for the RLHF and "50% overrepresented in training" speculation.** Either cite or label as informal speculation without empirical backing.

7. **Define jargon for outsider readers:** "tool call," "temperature," "fresh session," "IQR," "context cell," "feasibility boundary." Most readers will know these; for LinkedIn/blog/pitch audiences, brief inline definitions help.

8. **Remove or footnote the "T=1.0 has been collected" mention.** Reads oddly in a preprint if not yet analyzed.

9. **Consider line styles (in addition to color) in Figure 3** for grayscale readability.

10. **Tighten the abstract's closing sentence:** "vague language in action interfaces is compressed..." → "the model's numeric interpretation of vague intensity words is compressed..." This keeps the psycholinguistic framing on the construct (word interpretation), not the interface.

---

## Consensus Findings

**Strengths (all six reviewers agreed):**
- Experimental design is clean and well-motivated; the deterministic-backend-as-instrument logic is sound.
- The hedge/act/abstain finding at the 89% boundary — particularly the *drastically*/*dramatically* asymmetry — is the paper's most novel and defensible contribution.
- Figures (especially Figs. 2, 4, 5) do real communicative work.
- Limitations are honestly stated and the "first measurement slice" framing is appropriate.
- The paper successfully avoids reading as a tool-calling paper.

**Weaknesses (five or more reviewers agreed):**
- The ε² variance-ratio framing is technically incorrect as stated.
- Missing prompt templates, tool schema, and system prompt — critical reproducibility gap.
- The "Ordinal violation" label presupposes a researcher-constructed ordering is ground truth.
- The 0.50 "hedge" interpretation is asserted without a null/no-word control to rule out "0.50 is the model's default."
- The downstream consequences section is the weakest part of the paper.
- The Quirk qualification is honest but inconsistently placed (absent from abstract, present in methods footnote).

---

## Contested Points

**1. Is the psycholinguistic framing successful?**
- *Peer Reviewer & Alignment Guide:* Mostly successful; the framing lands in abstract/intro/conclusion.
- *Outsider:* Has not landed; the paper reads as a behavioral study of an AI system, and the word "psycholinguistics" never appears.
- *My assessment:* Both are right about different things. The framing succeeds at avoiding the "tool-calling paper" reading (the primary goal). It does not fully land as psycholinguistics because the linguistic literature is thin and the term itself is absent. For ArXiv readiness, this is acceptable. For LinkedIn/pitches, consider whether the framing needs to be more explicit in supplementary materials.

**2. How severe is the "ε² additivity" error?**
- *Peer Reviewer:* Moderate weakness; minor revision suffices.
- *Methodologist & Domain Expert:* This is the paper's most technically imprecise claim and requires correction in three places (abstract, contributions, results), making it a moderate revision.
- *My assessment:* The Methodologist and Domain Expert are correct. This is the paper's headline finding (the "10:1 ratio") and it appears in the most-read sections. Calling it a "minor" fix understates what's involved. The underlying empirical pattern (baseline matters more than word) is real; the framing as a variance ratio is the problem. This is Critical, not Important.

**3. Should a null/no-word control be added?**
- *Outsider, Methodologist, Domain Expert:* Yes, strongly recommended — without it, the "hedge at 0.50" interpretation cannot be distinguished from "0.50 is the model's default."
- *Peer Reviewer & Alignment Guide:* Flagged but not as a blocker.
- *My assessment:* For the stated preprint scope, adding this is *Important* but not *Critical* — the paper does label "hedge" as speculation. However, this is a one-cell experimental addition (10 words × 30 runs at one condition) that would substantially sharpen the paper's central interpretive claim. Strongly consider adding before submission if API budget allows.

**4. Is the related work sufficient?**
- *Peer Reviewer & Alignment Guide:* Adequate for stated scope.
- *Domain Expert & Outsider:* Missing scalar implicature, Horn scales, gradable adjectives literature.
- *My assessment:* Adequate for ArXiv as a "first measurement slice." A venue submission would require the broader linguistic grounding. For now, add one paragraph on Horn scales if framing as psycholinguistics matters; otherwise defer.

---

## Reviewer-Specific Highlights

- **Source Auditor:** The single most important catch is that **BrittleBench (2026) lacks a verifiable bibliographic entry** — a 2026 citation without authors/venue/arXiv ID is a credibility risk on ArXiv. Also: specify whether Spearman ρ is computed over n=10 medians or n=300 individual runs.

- **Methodologist:** The **ε² values come from two separate Kruskal-Wallis tests, not a joint variance decomposition** — the "10:1 ratio" framing is technically incorrect, and this is the most important methodological fix in the paper.

- **Peer Reviewer:** The **abstract's closing claim** ("vague language in action interfaces is compressed, state-dependent, and discontinuous") generalizes beyond the single model and single domain tested — soften by qualifying as model- and context-specific.

- **Domain Expert:** **The no-context condition cannot cleanly separate "what does *slightly* mean to the model" from "what does the model think a reasonable innovation allocation is, adjusted slightly"** — these are entangled, and the paper does not fully reckon with this. A null/no-word control would partially disentangle them.

- **Outsider / Red Team:** **The synthetic environment is never grounded for an outsider** — what does the solver solve? Why is 89% near-boundary? What are the other two tasks? An outsider cannot interpret the dollar figures or the abstention finding without this. Add one paragraph in Section 3.2.

- **Alignment Guide:** **The Quirk qualification is honest but unevenly placed** — present in Methods footnote, absent from the abstract. The single highest-leverage one-sentence addition would be qualifying the Quirk taxonomy claim in the abstract itself.

---

## Final Verdict

This is a competent, honest, and genuinely interesting first preprint. The boundary-behavior finding is novel enough to justify priority establishment on its own. The required revisions are concentrated and tractable — none require new experiments, and most are single-sentence additions or rewordings. The single most consequential fix is the ε² variance-ratio framing; the single most important reproducibility fix is providing the exact prompts and tool schema. Address the six Critical items, ideally most Important items, and the paper is ready for ArXiv. For your stated downstream uses (LinkedIn, pitches, mentorship), the paper communicates its findings effectively and its limitations honestly. Submit with confidence after revisions.

---

## Individual Reviews

### 1. Source Auditor

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

### 2. Methodologist

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

### 3. Peer Reviewer

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

### 4. Domain Expert

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

### 5. Outsider / Red Team

# Outsider Review: "Measuring Intensity Words at the Language-to-Action Boundary"

---

## First Impressions

This paper asks a genuinely interesting question: when you tell a computer system to "slightly" or "drastically" change something, does it actually treat those words differently in a consistent, ordered way? The answer — that it kind of does, but imperfectly and in ways that depend heavily on context — is intuitive once stated but apparently unmeasured before. The experimental setup is clever: use a controlled fake environment where you can isolate the word as the only variable, then see what number comes out.

My gut reaction is that this is a solid, honest piece of exploratory work. The author is careful about what they claim. The figures are clear and the results are striking (the complete abstention finding in particular is memorable). However, the paper has a framing tension it hasn't fully resolved, some statistical presentation issues that will raise eyebrows, and a few places where the logic jumps without adequate bridging. For a first preprint, it's genuinely impressive. For ArXiv readiness, it needs targeted fixes.

The psycholinguistics framing is **partially working but not fully landed**. I understood this as a paper about how an AI system behaves — it did not read to me primarily as a psycholinguistics measurement study until I was explicitly told that was the intent.

---

## Accessibility Assessment

**What works well:**
- The abstract is unusually readable. The three findings are stated plainly.
- The figures are excellent. Figure 2 (frequency heatmap) and Figure 5 (abstention bar chart) communicate their findings instantly without needing to read the surrounding text.
- The "hedge, act, abstain" framing in Section 4.3 is vivid and memorable.
- The author correctly defines most statistical terms inline (e.g., explaining Kruskal-Wallis as "analogous to ANOVA").

**Where it fails an outsider:**

The paper loses me in two specific places:

1. **The allocation numbers are never fully grounded.** The model outputs values like 0.50, 0.60, 0.70, 0.912. What do these represent physically? I understand there are "three task allocations that must sum to 100%," but I never learn what the tasks are, what the constraints are, why 89% is a "near-boundary" condition (is 100% the hard ceiling? Can you go to 100%?), or why the model would produce 0.912 rather than, say, 0.950 at the ceiling. The paper says the backend is a "deterministic solver" — what does it solve? The word "solver" implies optimization, but I don't know what's being optimized. This matters because the downstream dollar figures ($424K, $675K) appear with no grounding whatsoever.

2. **The "Tier 3" partial-context condition in Future Work** is described as if it's a third experimental tier, but it doesn't exist yet. This is fine, but it's confusing because Tiers 1 and 2 are used as condition labels in the Method section, making a reader expect Tier 3 to already exist.

---

## Logical Gaps

### Gap 1: The 0.50 "hedge" interpretation is asserted, not demonstrated

The paper says the model "defaults to the midpoint" and interprets this as a hedging behavior. Three explanations are offered (training data frequency, RLHF, genuine uncertainty), but none are tested or even ranked by plausibility. The problem is that 0.50 is also the *only value* that satisfies the constraint "sum to 100%" with three equal parts — it might simply be the model's prior for a balanced allocation, not a hedge at all. The paper doesn't rule this out. This is the paper's most interesting finding and the explanation is the weakest part.

**What's missing:** Even a brief acknowledgment that 0.50 could be the "default balanced state" rather than a hedge would strengthen this. The mechanistic speculation section raises but doesn't adjudicate between alternatives.

### Gap 2: The jump from "word choice explains less variance" to "context dominates word meaning"

The paper shows that starting allocation explains ~10x more variance than word choice in the context-conditioned condition. This is presented as evidence that "the same word cannot be treated as having a context-invariant numeric meaning." But this doesn't follow cleanly. It's possible that the word *does* have a stable meaning (e.g., "add 10% of available headroom") and the output varies with starting allocation *because* the word's meaning is stable and context-sensitive by design. The variance ratio could reflect sensible behavior, not instability. The paper doesn't distinguish between "the word means different things" and "the word means the same thing but that meaning is inherently relative."

### Gap 3: The ordinality claim relies entirely on the researcher's ordering

The Spearman correlation of 0.845 is between the model's outputs and the *researcher's hypothesized tier ordering*. If the tier ordering is wrong (e.g., if "moderately" really should sit below "slightly" in terms of implied increase magnitude), then the correlation is measuring agreement with a potentially incorrect baseline. The paper acknowledges this in footnotes and limitations, but the main text presents ρ = 0.845 as evidence of ordinal preservation without flagging this circularity prominently enough. The finding could be restated as "the model's outputs are broadly consistent with one plausible ordering of these words" — which is weaker but more defensible.

### Gap 4: Why does "drastically" behave differently from "dramatically"?

This is the most striking finding in the paper — drastically acts while dramatically abstains at 89% — and the explanation ("drastically functions as 'as much as possible'") is asserted without evidence. Both words are in the same tier. What would make one mean "push to ceiling" and the other mean "abstain if you can't do a lot"? This feels like the most important question raised by the paper, and it gets one sentence.

### Gap 5: The no-context condition is underspecified

The no-context prompt is: "Architects should spend [WORD] more time on innovation." But the model presumably still has *some* prior about what the current allocation is (maybe it assumes 33% as the default equal split?). The paper says the "target task starts from the default state" but doesn't say what that default is or whether the model is told this. If the model is reasoning from an implicit prior allocation, the no-context condition is not truly context-free — it's context-unknown, which is different.

---

## Undefined Jargon

The following terms are used without definition or with insufficient definition for an outsider:

1. **Tool call / structured tool call** — Used throughout. I infer this means a formatted function call the AI makes to interact with a system, but it's never defined. This is critical because the entire paper measures "tool calls."

2. **RLHF (Reinforcement Learning from Human Feedback)** — Expanded in parentheses once, but what it does and why it would cause midpoint-hedging is not explained.

3. **Temperature (T = 0.0, T = 0.7)** — The paper says "stochastic sampling" at higher temperature, but never explains what temperature *is* in this context. Why does 0.0 mean deterministic? Why 0.7? What would 1.0 do?

4. **Epsilon-squared (ε²)** — Introduced as "the proportion of rank-based variance explained" which is helpful, but the phrase "rank-based variance" itself is unexplained.

5. **IQR** — Used in Table 1 without definition.

6. **"Fresh session"** — Used in the methods. Does this mean the model has no memory of previous runs? This is important for experimental validity.

7. **"Deterministic solver"** — What does it solve? The paper never says.

8. **"Feasibility boundary" / "feasibility limits"** — Why is 89% a boundary? Is 100% the hard limit? Can allocations exceed 100%?

9. **"Degree modifiers" / "downtoners" / "amplifiers" / "maximizers" / "boosters"** — Quirk's taxonomy terms used without explanation. A reader unfamiliar with linguistics won't know what these mean.

10. **"Objective value delta"** — Appears in Section 4.4 without prior definition of what the "objective" is.

11. **"Context cell"** — Used in Table 1. I assume this means one (word × baseline) combination, but it's not defined.

---

## Unconvincing Arguments

### 1. The framing as a psycholinguistics paper

The author's brief states the paper should read as a "psycholinguistic measurement study." It doesn't, convincingly. The paper reads as a behavioral study of an AI system. Psycholinguistics typically involves human subjects and studies how humans process language. Using Quirk's taxonomy as organizational scaffolding doesn't make this psycholinguistics — it makes it a study of AI behavior *inspired by* psycholinguistic categories. This isn't a criticism of the science, but the framing claim is not realized in the text. The word "psycholinguistic" doesn't appear in the paper at all. If this framing matters for the target audience, it needs to be explicit.

### 2. The downstream dollar figures

Section 4.4 reports a spread of ~$250K between word choices. This is presented as evidence that "different interpretations propagate into materially different outcomes." But the dollar figures are from a *synthetic environment* with presumably synthetic numbers. The paper acknowledges this ("specific to the synthetic environment"), but the framing still implies real-world stakes. A reader might reasonably ask: what determines the dollar values in the synthetic environment? Are they calibrated to anything realistic? This section feels like it's trying to make the stakes feel higher than the evidence warrants.

### 3. "Temperature is structurally non-corrective but behaviorally consequential"

This phrase in Section 4.5 is pithy but I'm not sure what it means. If temperature doesn't change the structure but does change behavior, what distinguishes "structure" from "behavior"? The claim seems to be that higher temperature adds noise without restoring ordinal distinctions — which is a legitimate finding — but the phrasing obscures rather than clarifies.

### 4. The "local ordinal anomaly" for "moderately"

The paper notes that "moderately" maps below "slightly" and interprets this as the word activating a "restraint heuristic." This is plausible but entirely speculative. The alternative — that the researcher's tier ordering is simply wrong for this word — is mentioned but not taken seriously. If "moderately" means "keep things moderate" rather than "increase by a moderate amount," then the word was miscategorized in the scale, not anomalous. This distinction matters for whether the finding is about the model or about the scale.

### 5. The multiple comparisons issue

The paper runs many statistical tests across many word/baseline combinations without correcting for multiple comparisons. The author's brief acknowledges this, and the paper does too (briefly, in limitations). But the issue is more serious than acknowledged: when you run 10 × 10 = 100 comparisons and report the significant ones, some will be significant by chance. The paper doesn't quantify how many tests were run total or estimate how many false positives to expect. For a preprint, this is acceptable, but the limitations section should be more explicit about the magnitude of the problem, not just its existence.

---

## What I Still Don't Understand

After a careful read, I remain unclear on:

1. **What exactly is the synthetic environment?** I know there are "three task allocations summing to 100%" and one is "innovation." What are the other two? What does the solver optimize? Why does the allocation cap at some value below 100% (the model outputs 0.912 at 89% baseline — why not higher)?

2. **What does the model actually "see"?** I know the prompt text, but what else is in the model's context? Does it see the tool definition? Does it know the constraint that allocations sum to 100%? Does it know the current values of the *other* two tasks? This matters enormously for interpreting the abstention behavior.

3. **How is abstention defined operationally?** The paper says "a non-error run that produces zero tool calls." But what does the model *do* instead? Does it produce text saying "I can't do that"? Does it just respond with nothing? Does it explain why? This would help interpret whether abstention is principled (the model "knows" it can't comply) or a failure mode.

4. **Why are the specific allocation values what they are?** The model outputs 0.50, 0.60, 0.65, 0.70 in the no-context condition. These look like round numbers. Are these the only values the tool accepts? Or does the model happen to choose round numbers? If the tool accepts any value, why doesn't the model output 0.52 or 0.67?

5. **What is the "default state" in the no-context condition?** Is the model told anything about the current allocation? If not, what does it assume?

6. **Why 30 runs per cell specifically?** The paper says this "balances statistical power for nonparametric tests with API cost constraints" but doesn't show a power calculation or estimate. For a condition with zero variance (all 30 runs produce 0.50), 30 is trivially sufficient. For conditions with high variance, is 30 enough?

7. **What is the prompt system message?** The user-facing prompts are shown, but I don't know if there's a system prompt that establishes the model's role, the environment constraints, or other context that would affect interpretation.

---

## Specific Recommendations Addressing the Author's Brief

### On Quirk Taxonomy Honesty (Concern #1)

**Current framing: Adequate but buried.** The acknowledgment exists in a footnote in the word scale section and in the limitations. However, the main text presents the tier numbers (1–6) as if they're established categories, and the Spearman correlation is reported against these tiers without a prominent reminder that the tiers are researcher-constructed. 

**Recommendation:** Add one sentence in the Results section (Section 4.1) where ρ = 0.845 is first reported, explicitly noting that this correlation is against a researcher-defined ordering, not a validated human scale. Something like: "Note that this correlation measures agreement with the researcher-constructed tier ordering; whether humans would rank these words identically is untested." The current footnote in Section 3.3 is easy to miss.

### On Statistical Rigor (Concern #2)

**The limitations acknowledgment is present but underweighted.** The paper lists "no multiple-comparison correction" in the limitations paragraph, but this is one item in a list of six limitations. A reader skimming the results will see H = 290.02, p < 0.001, ε² = 0.969 and interpret these as strong evidence without registering the caveat buried later.

**Specific issues:**
- The ε² = 0.969 in the no-context condition is computed over a condition where many groups have zero variance (all 30 runs identical). This makes the effect size artificially inflated and potentially uninterpretable as a measure of explained variance. This should be flagged.
- The sentence "Cases where a higher-tier word produces a lower output than expected are reported as descriptive observations rather than treated as evidence against the hypothesized ordering" (Section 3.5) is methodologically problematic. You cannot define your hypothesis as unfalsifiable by pre-deciding that violations won't count against it. This needs to be reworded — perhaps as "anomalous cases are noted and discussed qualitatively" rather than implying they've been excluded from consideration.
- The Spearman ρ = 0.845 across the full no-context dataset pools 10 × 30 = 300 observations. But these are not independent — 30 runs per word are highly correlated (especially at T=0.0 where many are identical). The p-value is likely misleadingly small. Acknowledge this.

### On Clarity and Flow (Concern #3)

**The five-block structure works, but the transitions are weak.** The paper moves from Block 1 (no context) to Block 2 (context) to Block 3 (boundary) to Block 4 (downstream) to Block 5 (temperature) without clear signposting of how these blocks relate to the three empirical questions stated in the introduction. A reader tracking "which block answers which question" has to do this work themselves.

**Recommendation:** Add a one-sentence topic sentence to each results subsection that explicitly links back to the empirical question it addresses. E.g., "Turning to Question 1: does the model preserve ordinal ranking..."

**The Future Work section is appropriately scoped** — it reads as genuine extensions rather than padding, and the Tier 3 partial-context condition is a clever experimental design. However, mentioning that a T=1.0 sweep "has been collected and will be analyzed in a subsequent revision" is odd for a preprint — if it's collected, why not include it? Either include it or remove the mention.

**The framing as psycholinguistics has not landed.** The paper never uses the word "psycholinguistics." If this framing matters, it needs to appear — at minimum in the abstract and introduction. One sentence connecting this to psycholinguistic measurement traditions (e.g., "I use the tool-call environment as

### 6. Alignment Guide

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

---

## Deliberation Round

### Source Auditor — Revised Position

# Source Auditor Response — Council Review Round

---

## Agreements

**Reviewer B — Spearman ρ computation ambiguity.** Reviewer B correctly identifies that the paper does not specify whether the Spearman ρ = 0.845 is computed over 10 median values (one per word) or over all 300 individual run observations. I flagged this as internally consistent but did not flag the ambiguity in the computation method itself. This is a genuine source-integrity issue: the p-value and the interpretation of the correlation depend critically on which n is used. With n = 10, the correlation is computed over very few paired observations; with n = 300, the p-value is inflated by non-independence (30 runs per word are not independent draws). The paper presents "Spearman ρ = 0.845, p < 0.001" as a clean factual claim, but the factual basis of that claim is underspecified. I should have flagged this more explicitly.

**Reviewer B — ε² values from separate tests, not a joint decomposition.** Reviewer E raises this most sharply, but Reviewer B also identifies it. The paper states "starting allocation explains roughly 10 times more variance than word choice (ε²_baseline = 0.782 vs. ε²_word = 0.079)." These two ε² values come from two separate Kruskal-Wallis tests with different grouping variables on the same dataset. They are not components of a single variance partition. The ratio 0.782/0.079 = 9.9 is arithmetically correct, but the framing as a variance ratio implies a joint decomposition that the analysis does not perform. This is the most technically imprecise factual claim in the paper, and it appears in the abstract, the contributions list, and the results section. I noted the arithmetic was correct but did not flag the interpretive overreach. This is a source-integrity issue I should have caught.

**Reviewer B — System prompt and tool schema not provided.** I flagged BrittleBench (2026) and Zhang et al. (2024) as underspecified citations, but I did not flag the missing system prompt and tool schema as reproducibility gaps that affect factual verifiability. Reviewer B is correct that without these, the factual claim "the model receives a natural-language instruction and produces a numeric allocation" cannot be fully verified or reproduced. The exact prompt templates are paraphrased, not quoted. This is a source-integrity gap I missed.

**Reviewer D — ε² = 0.969 inflated by near-zero within-word variance.** Reviewer D correctly notes that ε² = 0.969 in the no-context condition is partly mechanical: when 4 of 10 words produce the same value in all 30 runs (zero within-word variance), between-word variance dominates trivially. I verified the arithmetic was correct but did not flag that the effect size is partially an artifact of the experimental design rather than a substantive finding. This is a factual framing issue.

**Reviewer F — Abstract does not disclose researcher-constructed scale.** I verified that the disclosure appears in Table 1's caption and in the introduction, but Reviewer F correctly notes it is absent from the abstract. The abstract states the paper "tests 10 intensity words spanning six hypothesized tiers of the Quirk et al. degree-modifier taxonomy" without noting that the mapping is by analogy and only 3 of 10 words appear in Quirk's lists. A reader of the abstract alone receives a stronger impression of Quirk grounding than is warranted. This is a factual framing issue I should have flagged.

---

## Disagreements

**Reviewer A — "The framing as a psycholinguistics paper" as a factual concern.** Reviewer A argues the paper does not read as psycholinguistics. This is outside my mandate as Source Auditor — I do not evaluate framing success or writing quality. I have no disagreement with the observation itself, but I note it is not a factual accuracy or citation integrity issue.

**Reviewer E — "The ε² additivity claim" as a "red flag."** Reviewer E labels this a "moderate" technical red flag and says the framing is "technically incorrect." I agree the framing is imprecise, but I would characterize it differently for source-integrity purposes: the underlying numbers are correct, the tests are correctly named, and the ratio is arithmetically accurate. The issue is that the language "explains roughly 10 times more variance" implies a joint decomposition. This is an interpretive overstatement, not a fabricated or miscited claim. The distinction matters for my mandate: I flag it as a factual framing issue requiring qualification, not as a false claim.

**Reviewer A — The 0.50 "hedge" as a logical gap.** Reviewer A argues the paper does not rule out that 0.50 is simply the equal-split default (33%/33%/34% → one task at 50% after redistribution). This is a valid interpretive concern, but it is outside my mandate. My role is to verify whether the hedge claim is presented as a tested finding or as speculation. The paper correctly labels it as speculation in the Discussion under "Mechanistic speculation." The claim is not oversold as a finding. I stand by my original assessment that this is appropriately hedged.

---

## Revisions to My Review

### Addition 1: Spearman ρ Computation — Flag as Unverifiable

I should have flagged the Spearman ρ = 0.845 (p < 0.001) claim more precisely. The paper does not state whether this is computed over n = 10 word-level medians or n = 300 individual observations. These yield different statistics and different p-values. The claim as stated is **unverifiable from text alone** because the unit of analysis is not specified. I add this to my Unsupported or Weakly Supported Claims section.

### Addition 2: ε² Ratio — Flag as Interpretive Overstatement

The claim "starting allocation explains roughly 10 times more variance than word choice (ε²_baseline = 0.782 vs. ε²_word = 0.079)" should be flagged. The arithmetic is correct (0.782/0.079 ≈ 9.9). The ε² values are correctly attributed to Kruskal-Wallis tests. However, the framing as a variance ratio implies these are components of a single decomposition, which they are not. This claim appears in the abstract, contributions list, and results section. I add this to my Unsupported or Weakly Supported Claims section as an interpretive overstatement requiring qualification.

### Addition 3: Missing Prompt Templates — Reproducibility Gap Affecting Factual Verifiability

The paper paraphrases its prompts rather than quoting them exactly. The no-context prompt is described as "Architects should spend [WORD] more time on innovation" and the context prompt as "The current innovation allocation is b%. I would like to [WORD] increase innovation." These may be exact quotes or paraphrases — the paper does not distinguish. Since the paper's central factual claims depend on what the model received as input, the absence of exact prompt text (including system prompt and tool schema) means the primary factual claims are **unverifiable from text alone**. I add this to my Missing Citations section as a reproducibility gap.

### Addition 4: Figure 4 Empty Cells — Confirmed Abstention, Caption Gap

I noted in my original review that the delta heatmap (Figure 4) has blank cells for *considerably*, *substantially*, and *significantly* at b = 89%, and that my review was cut off before completing this observation. Reviewing Figure 4 fully: the three blank cells for *considerably*, *substantially*, and *significantly* at 89% are consistent with the 100% abstention rates reported in Figure 5 and the text (121/300 total abstentions). The blank cells represent abstention, not missing data. However, the Figure 4 caption does not state this. A reader could interpret blank cells as missing data. This is an internal consistency gap between Figure 4 and Figure 5 that I should have flagged explicitly: the caption should note that blank cells indicate abstention.

### Addition 5: BrittleBench (2026) — Strengthen Flag

My original review flagged this citation as requiring a full bibliographic entry. Having reviewed all council feedback, no other reviewer identified this citation as verifiable. I strengthen my flag: this citation is **unverifiable from text alone** and may not exist in a form that readers can access. For a paper making claims about prompt sensitivity grounded in this citation, the absence of a verifiable reference is a source-integrity concern. The paper should provide authors, venue/arXiv ID, and date, or replace with a verifiable citation.

---

## Blind Spots

### Methodologist — Revised Position

## Agreements

**Reviewer B, Weakness #6 (ε² = 0.969 caveat):** I agree that the near-zero within-word variance at T=0.0 mechanically inflates ε² in the no-context condition. I raised this in my review but Reviewer B articulates it more cleanly: when many groups have zero internal variance, between-group variance dominates trivially, making the effect size partially an artifact of the deterministic decoding condition rather than a substantive finding about word distinctiveness. This needs a caveat in the text.

**Reviewer C, Flag 1 (ε² additivity):** I raised this as my most technically imprecise claim flag, and Reviewer C independently identifies the same issue with identical reasoning. Two separate Kruskal-Wallis tests cannot be interpreted as a joint variance partition. The "10:1 ratio" language implies a decomposition the analysis does not perform. This is the paper's most technically incorrect claim and both reviews converge on it. The fix is straightforward: reword to "two separate KW tests suggest baseline grouping captures far more rank-based structure than word grouping" rather than framing it as a variance ratio.

**Reviewer C, Flag 2 (T=0.0 non-determinism):** I flagged this as a technical red flag. Reviewer C independently raises it. The paper notes 4 of 10 words produce multiple distinct values at T=0.0 in a single sentence at the end of Section 4.5. For a paper making claims about deterministic baseline behavior, this deserves explicit investigation and explanation, not a brief mention.

**Reviewer B, Question 4 (abstention mechanism):** I raised the abstention operationalization as a construct validity concern — the paper conflates principled refusal with failure-to-invoke. Reviewer B asks the same question from a different angle: does the model produce a refusal message, or simply no tool call? This is important for interpreting whether the "three behavioral modes" finding reflects model reasoning or a different kind of output failure.

**Reviewer E, structural point on Results/Questions mismatch:** I did not raise this explicitly, but Reviewer E correctly identifies that the three empirical questions in the Introduction do not map cleanly onto the five Results subsections. The "Downstream Consequences" section answers none of the three stated questions. This is a coherence gap I should have flagged.

**Reviewer F, missing null/no-word control:** Reviewer C also raises this. The paper has no baseline condition where no intensity word is given. Without this, the claim that lower-tier words "hedge at 0.50" is untested — 0.50 may simply be the model's default output for this task regardless of word. This is a genuine experimental gap I underemphasized in my review.

---

## Disagreements

**Reviewer A, Gap 2 (variance ratio interpretation):** Reviewer A argues that the 10:1 variance ratio "doesn't follow cleanly" because the word might have a stable relative meaning (e.g., "add 10% of available headroom") that is inherently context-sensitive. I partially disagree with the framing of this as a logical gap. The paper's claim is not that words have unstable meanings in some absolute sense — it is that the *operational output* is primarily determined by state rather than word. Whether this reflects "sensible behavior" or "instability" is an interpretive question the paper correctly leaves open. The variance ratio finding is valid as a descriptive claim about what drives output variance; the paper does not need to adjudicate between the two interpretations Reviewer A raises. The paper should clarify the descriptive nature of the claim, but this is a framing fix, not a logical gap.

**Reviewer B, Weakness #3 (moderately underexplained):** Reviewer B says this is "the most linguistically interesting anomaly" and deserves more development. I agree it deserves more, but I think Reviewer C's framing is more precise: the issue is not just that the paper underexplains the anomaly, but that labeling it an "ordinal violation" presupposes the researcher's ordering is correct. The word may have been miscategorized, not the model's behavior anomalous. Reviewer B treats this as a model interpretation question; I think it is primarily a construct validity question about the word scale itself. The distinction matters for how the paper should address it.

**Reviewer B, Recommendation (Weak Accept):** I agree with the ArXiv readiness verdict but would characterize the ε² additivity issue as requiring more than a minor revision. The abstract, contributions list, and results section all use the "10:1 ratio" framing that implies a joint decomposition. This is not a one-sentence fix — it requires revising multiple passages to correctly characterize what the two separate KW tests actually show. I would call this a moderate revision rather than minor.

**Reviewer A, Gap 5 (no-context condition "not truly context-free"):** Reviewer A argues the no-context condition is "context-unknown, which is different" from context-free. This is correct as a philosophical point but I think it overstates the practical concern. The paper's claim is about what happens when no explicit current allocation is provided — the implicit prior is part of what is being measured. The paper should acknowledge the implicit prior exists, but calling this a "genuine confound" overstates it. It is a feature of the measurement condition, not a flaw.

---

## Revisions to My Review

**Addition: The null/no-word control gap is more serious than I indicated.** Reviewers C and F both raise this independently. I mentioned the no-context condition's relationship to the context-conditioned condition but did not flag the missing null baseline. Without a condition where no intensity word appears (just "Architects should spend more time on innovation"), the paper cannot distinguish between "the model hedges at 0.50 in response to weak words" and "the model outputs 0.50 as its default for this task regardless of word." This is a genuine experimental gap that weakens the "hedge" interpretation, which is one of the paper's most prominent interpretive claims. I would elevate this to a moderate concern rather than leaving it implicit.

**Addition: The split-range variance decomposition is post-hoc and should be flagged explicitly.** I mentioned this briefly but Reviewer C articulates it more precisely: the split at 25%/32% was chosen after seeing the data, and the specific percentages (65.3%, 12.5%, 88.0%, 6.5%) should be labeled as exploratory post-hoc analysis. I should have been more direct about this in my original review.

**Addition: The Spearman ρ computation method needs explicit specification.** I raised the circularity issue (ρ computed against researcher-hypothesized tiers) but did not flag the ambiguity in how ρ is computed — whether over 10 medians or 300 individual observations. Reviewer D (myself) missed this; it was raised by no other reviewer either, but it is a genuine ambiguity. With n=10 (medians), the p-value is based on 10 paired observations, which is a very small sample. With n=300, the p-value is inflated by non-independence (30 runs per word are correlated, especially at T=0.0 where many are identical). The paper should specify which was used and acknowledge the independence issue.

**Strengthening: The prompt syntactic frame confound.** I raised this as an internal validity concern (the no-context prompt uses "spend [WORD] more time" while the context prompt uses "[WORD] increase") but no other reviewer flagged it. I stand by this as a genuine confound. The model's behavior may differ partly because of the syntactic context of the word (modifying a noun phrase vs. a verb phrase), not just the presence or absence of the baseline number. This should be acknowledged in the limitations.

**Retraction/softening: I characterized the system prompt absence as "the single most important missing piece."** After reading Reviewer E's review, I think the exact prompt templates (user-facing) are equally critical. Both are needed for reproducibility. I would revise my reproducibility assessment to list both as equally critical missing pieces rather than privileging the system prompt.

---

## Blind Spots

**No reviewer adequately addressed the independence assumption in the Spearman ρ calculation.** The p-value for ρ = 0.845 assumes independent observations. At T=0.0, many words produce identical outputs across all 30 runs, meaning the 300 observations are not independent — they are 10 groups of 30 highly correlated (often identical) observations. The p-value is almost certainly misleadingly small regardless of whether ρ is computed over medians or raw observations. No reviewer stated this explicitly or recommended a correction (e.g., computing ρ over the 10 word-medians only, with n=10, and reporting the appropriate p-value

### Peer Reviewer — Revised Position

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

### Domain Expert — Revised Position

## Agreements

**Reviewer A — System prompt and tool schema absence (Critical reproducibility gap)**
I agree strongly. Reviewer A correctly identifies this as the most significant reproducibility concern. My original review flagged the confound between prompt phrasing and word choice, but I understated the severity of the missing system prompt and tool schema. In a tool-calling context, the tool description is part of the model's effective input. Without it, the experiment cannot be replicated. This is more critical than I initially emphasized.

**Reviewer A — The "ordinal violation" label for *moderately***
I agree with Reviewer A's suggestion to replace "ordinal violation" with "ordinal anomaly" or "unexpected ordering." My original review made the same point but less directly. The label implies the researcher's ordering is ground truth, which it is not. This is a framing fix that costs nothing.

**Reviewer C — The 0.50 hedge interpretation is asserted, not demonstrated**
Reviewer C correctly identifies that 0.50 could be the model's prior for a balanced equal-split allocation (33%/33%/34% default) rather than a hedge. My original review noted the "hedge" framing as speculative but did not articulate this specific alternative as clearly. The null/no-word control that Reviewer B (myself) recommended would directly test this, but Reviewer C's framing of the alternative hypothesis is sharper than mine.

**Reviewer C — Gap 2: variance ratio does not imply context-invariant word meaning is unstable**
This is a genuine logical gap I missed. The 10:1 variance ratio is consistent with the word having a *stable relative meaning* (e.g., "add X% of available headroom") rather than an unstable absolute meaning. The paper conflates these two interpretations. The finding could reflect sensible context-sensitive behavior rather than semantic instability.

**Reviewer D — BrittleBench (2026) citation is unverifiable**
I did not flag this in my original review. Reviewer D is correct that a 2026 citation with no full bibliographic entry cannot be verified. For a preprint, this is a credibility issue.

**Reviewer E — ε² = 0.969 caveat needed**
I agree with Reviewer E's point that the near-zero within-word variance at T=0.0 mechanically inflates ε². When many groups have zero variance, between-group variance dominates trivially. My original review flagged the ε² additivity claim as the primary technical error but did not separately address this inflation issue. Both problems need fixing.

**Reviewer F — Downstream consequences section should be framed as validity check, not finding**
I agree. My original review called this section "the weakest section" but did not articulate the correct reframing. Reviewer F's suggestion — frame it as confirming the instrument has consequential outputs — is the right fix.

---

## Disagreements

**Reviewer E — "Weak Accept for ArXiv" framing**
Reviewer E gives a "Weak Accept" and describes the paper as "ready for ArXiv with minor revisions." I think this understates the severity of two issues. First, the ε² additivity problem (comparing two separate KW test outputs as if they partition variance) is not a minor revision — it affects the abstract, the contributions list, and the headline finding. The "10:1 ratio" language as currently written is technically incorrect as a variance decomposition claim, not merely imprecise. Second, the missing system prompt and tool schema are not minor omissions for a paper whose central claim is about how word choice affects model output. These are the two most significant technical gaps, and calling them "minor" undersells the work needed.

**Reviewer C — "The framing as psycholinguistics has not landed"**
Reviewer C argues the paper reads as a behavioral study of an AI system, not a psycholinguistics paper. I partially disagree. The framing question is whether the paper reads as studying *word interpretation* (psycholinguistics-adjacent) versus *system behavior* (AI systems). I think the paper mostly succeeds at the former — the abstract, introduction, and conclusion consistently foreground the word-interpretation question. The Methods section does slip into systems language, but this is a localized problem, not a global framing failure. Reviewer C's critique is valid for the Methods section specifically but overstated as a global assessment.

**Reviewer A — "Confound: prompt phrasing is not isolated from word choice"**
Reviewer A flags that the no-context prompt uses the word as a noun modifier ("more time on innovation") while the context prompt uses it as a verb modifier ("increase innovation"). This is a real confound, but I think Reviewer A overstates its severity. The paper is not claiming that the syntactic frame is held constant — it is claiming that the word is the only variable *within each condition*. The two conditions are explicitly different measurement regimes, not two instances of the same measurement. The confound would matter if the paper were claiming to isolate word semantics from syntactic context across conditions, but it is not making that cross-condition comparison as a primary claim. This should be acknowledged but is not a fatal flaw.

**Reviewer D — Round-number anchoring observation is "consistent with the data shown"**
Reviewer D accepts the round-number anchoring observation as visually consistent with Figure 4. Looking at the delta heatmap more carefully: at b=18%, the deltas for booster-class words are 0.164 (not round); at b=32%, they are 0.138 (not round); at b=53%, they are 0.094 (not round). But at b=25%, *drastically* shows 0.250 (round), and at b=50%, the deltas are 0.100 (round). The pattern is mixed. The observation is weaker than the paper implies, and Reviewer D's endorsement of it as "consistent" is slightly too generous. The paper's own hedge ("preliminary, visual inspection") is appropriate, but the observation should not be cited as even a preliminary finding without more systematic analysis.

---

## Revisions to My Review

**Strengthening the ε² additivity point (Flag 1)**
My original review correctly identified this as the most technically imprecise claim. After seeing other reviews, I want to be more specific about what the fix requires. The paper needs to change three locations: (1) the abstract ("starting allocation explains roughly 10 times more variance than word choice" → "two separate Kruskal-Wallis tests show that baseline grouping captures far more rank-based structure than word grouping, with ε² values of 0.782 and 0.079 respectively"); (2) the contributions list (same reframing); (3) the results section (add explicit statement that these are not additive components of a joint decomposition). This is not cosmetic — it is the paper's primary quantitative claim and it is currently stated in a way that implies a statistical procedure that was not performed.

**Adding the logical gap Reviewer C identified**
I missed the distinction between "word meaning is unstable" and "word meaning is stably relative." The paper's interpretation of the 10:1 ratio as evidence that "the same word cannot be treated as having a context-invariant numeric meaning" is not the only interpretation. A word that means "add X% of available headroom" has a context-invariant meaning that produces context-variant outputs. The paper should acknowledge this alternative interpretation explicitly.

**Elevating the no-word control recommendation**
My original review recommended a null/no-word control as a missing baseline. After seeing Reviewer B's (my own) and Reviewer C's convergent concern about the 0.50 hedge interpretation, I want to elevate this from a recommendation to a near-requirement for the paper's central interpretive claim. The hedge interpretation is the paper's main mechanistic story for the no-context compression finding, and it is entirely untested. Without a null control, the paper cannot distinguish "0.50 is the hedge value" from "0.50 is the model's default allocation for this task regardless of instruction."

**Revising the impact assessment**
My original review called the abstention finding "the most impactful" result. I stand by this, but I want to add: the *drastically*/*dramatically* asymmetry at the boundary is also the finding most vulnerable to being a model-specific artifact. Two words that humans might treat as near-synonyms diverging completely at one boundary value is striking, but it could reflect something idiosyncratic about how Claude Haiku was trained rather than a general property of LLM word interpretation. The paper should flag this more explicitly.

**On the T=0.0 non-determinism**
My original Flag 2 noted this. After reviewing Figure 6 (the temperature comparison heatmap), I can see that at T=0.0, *considerably* splits 11/19 between 0.60 and 0.65, *substantially* splits 20/10, and *significantly* splits 5/

### Outsider / Red Team — Revised Position

# Reviewer A — Council Response

---

## Agreements

**Reviewer B (Experimental Design Assessment) — Confound: Prompt phrasing differs between conditions.**
Reviewer B correctly identifies that the no-context prompt ("Architects should spend [WORD] more time on innovation") and the context-conditioned prompt ("I would like to [WORD] increase innovation") are not the same syntactic frame. I flagged the no-context condition as underspecified but missed this specific confound. The word modifies a noun phrase in one condition and a verb phrase in the other. This is a genuine internal validity threat that I should have caught.

**Reviewer B — System prompt and tool schema not reported.**
I flagged this as a reproducibility gap but Reviewer B articulates it more precisely: tool-calling behavior in Claude is highly sensitive to system prompt content and tool schema definitions. This is the most critical reproducibility gap, and I agree it is more serious than I initially conveyed. My review mentioned it but understated its centrality.

**Reviewer C (Strengths #5) — The hedge/act/abstain finding is the paper's most novel contribution.**
I agree. The *drastically*/*dramatically* asymmetry at 89% is genuinely surprising and the paper's most defensible claim to novelty. I said this in my review but Reviewer C articulates it more cleanly.

**Reviewer C (Weakness #6) — ε² = 0.969 requires a caveat about near-zero within-word variance.**
I did not flag this specifically. Reviewer C is right: when many words produce identical outputs across all 30 runs, between-group variance dominates mechanically. The 0.969 figure is partly a design artifact, not purely a semantic finding. This is a real gap in my review.

**Reviewer D (Citation Issues) — BrittleBench (2026) is unverifiable.**
I did not examine citations at this level of detail. Reviewer D is correct that a 2026 reference with no full bibliographic entry cannot be verified by readers. This is a concrete ArXiv-readiness issue I missed.

**Reviewer E (Missing Sections #3) — Exact prompt templates must appear somewhere.**
I flagged that the no-context condition was underspecified, but Reviewer E makes the stronger and more actionable point: the exact prompt templates should appear in the paper or an appendix, not just paraphrases. This is the right framing of the reproducibility problem.

**Reviewer F (Technical Red Flag #1) — The ε² additivity claim is technically incorrect.**
This is the most important technical flag in all six reviews, and I missed it entirely. Reviewer F correctly identifies that comparing ε²_baseline = 0.782 and ε²_word = 0.079 from two *separate* Kruskal-Wallis tests as if they partition a joint variance is technically wrong. The "10:1 ratio" language implies a decomposition the analysis does not perform. This is a moderate-severity error that appears in the abstract, contributions list, and results section. I should have caught this.

**Reviewer F (Missing Related Work) — Scalar implicature and Horn scales.**
Reviewer F correctly notes that the compression finding (10 words collapsing to 5 regimes) connects directly to Horn scales and scalar implicature in formal pragmatics. The model treating *slightly*, *marginally*, *somewhat*, and *mildly* as equivalent may reflect linguistically principled scale structure rather than model failure. This is an important framing gap I missed entirely.

---

## Disagreements

**Reviewer C (Recommendation: Weak Accept) — I would rate this more cautiously.**
Reviewer C gives a "Weak Accept" and says the psycholinguistic framing "mostly" succeeds. I think the framing success is more partial than Reviewer C credits. The paper never uses the word "psycholinguistics." The introduction situates the work relative to psycholinguistic literature, but the Methods section reads as a systems paper and the Discussion introduces a third framing (AI alignment) that is not established in the introduction. For a paper whose stated goal is to be read as a psycholinguistic measurement study, this is a more significant framing failure than "mostly successful." I would say the framing is "partially successful in the abstract and introduction, but leaks in the methods and discussion." This doesn't change my ArXiv readiness verdict (I also think it's ready with minor revisions), but the framing assessment differs.

**Reviewer B (Weakness: Single-direction design) — Framed as "significant constraint" but not a blocking issue.**
Reviewer B calls the increase-only design "a significant constraint" and says the paper should be careful not to imply generality of the mode-switching finding. I agree with the substance but not the severity framing. The paper explicitly acknowledges this limitation in both the Limitations and Future Work sections. For a stated "first measurement slice," an increase-only design is a reasonable scope constraint, not a flaw. Reviewer B's concern is valid but I think the paper's existing acknowledgment is adequate for a preprint.

**Reviewer F (Alternative Approaches — chain-of-thought condition) — Valuable but not a gap for this paper.**
Reviewer F suggests the author should have prompted the model to explain its reasoning before acting. This would be informative, but it changes the experimental condition: a model that must articulate its reasoning may behave differently from one that acts directly. For a paper measuring the action output specifically, adding a reasoning step is a different experiment, not a missing control. I'd frame this as future work rather than a design gap.

---

## Revisions to My Review

**Addition 1: The ε² additivity problem (from Reviewer F).**
This is the most significant thing I missed. My original review flagged the multiple-comparison issue but did not identify that the "10:1 variance ratio" framing is technically imprecise. Two separate Kruskal-Wallis tests do not produce additive ε² values that partition a joint variance. The paper should reword this throughout: instead of "starting allocation explains roughly 10 times more variance than word choice," it should say something like "a Kruskal-Wallis test grouping by baseline yields ε² = 0.782; a separate test grouping by word yields ε² = 0.079; these are not additive but suggest baseline grouping captures far more rank-based structure." This is a moderate fix, not a minor one, and it affects the abstract, the contributions list, and the results section.

**Addition 2: Scalar implicature connection (from Reviewer F).**
I flagged undefined jargon from linguistics but missed the substantive theoretical gap: the compression finding may reflect Horn scale structure rather than model limitation. The paper should acknowledge this in Related Work or Discussion. Without it, the paper risks presenting as a "model failure" something that may be a linguistically principled behavior.

**Addition 3: The syntactic frame confound (from Reviewer B).**
I noted the no-context condition was underspecified but missed that the two conditions use different syntactic frames. This should be added to my Logical Gaps section. The word modifies "more time" (noun phrase) in the no-context condition and "increase" (verb) in the context condition. This is a genuine confound that the paper does not acknowledge.

**Revision to my Unconvincing Arguments #5 (multiple comparisons):**
I said the issue was "more serious than acknowledged" but did not specify where the most serious instance is. Based on Reviewer F and Reviewer C's more precise analyses, the split-range variance decomposition (the 65.3%/12.5%/88.0%/6.5% figures) is the most problematic: it is a post-hoc analysis with a researcher-chosen split point, and the specific numbers are presented without flagging their exploratory nature. My original review was correct in direction but insufficiently specific.

**Strengthening my Gap 1 (the 0.50 hedge):**
Reviewer F adds a point I missed: the paper does not test a null/no-word control. If the model produces 0.50 even with no intensity word at all, then the lower-tier words are not functioning as intensity modifiers — they are producing the same output as no instruction. This is a one-cell addition that would sharpen the hedge interpretation substantially. I should have caught this as a missing control.

**Standing by my Gap 2 (the variance ratio framing):**
My original concern — that the 10:1 ratio could reflect sensible context-sensitive behavior rather than instability — is confirmed and strengthened by Reviewer F's technical flag. The paper does not distinguish between "the word means different things" and "the word means the same thing but that meaning is inherently relative to context." This remains an unresolved logical gap.

---

## Blind Spots

After reviewing all six reviews, I believe the following points are absent from all reviews, including my own:

**1

### Alignment Guide — Revised Position

# Reviewer A — Council Response

## Agreements

**Reviewer B — ε² additivity claim (Technical Red Flag 1).** I agree this is more serious than I flagged it. I noted the issue briefly ("the two ε² values are not from the same test") but did not call it out as the paper's most technically imprecise claim. Reviewer B is right that the language "starting allocation explains roughly 10 times more variance than word choice" implies a joint variance decomposition that the analysis does not perform. This appears in the abstract, the contributions list, and the results section. My original review was too gentle here — I said the finding was "correct" while the framing was imprecise. The framing needs to be corrected in all three locations, not just noted as a caveat.

**Reviewer B — Spearman ρ circularity needs to be more explicit in Results (not just Methods).** I flagged this, but Reviewer B correctly identifies that the reminder needs to appear in Section 4.1 where ρ = 0.845 is first reported, not only in the Methods footnote. I agree the current placement is insufficient.

**Reviewer C — The "moderately" ordinal violation label is problematic.** I flagged this as scope drift in the Discussion but did not identify the deeper issue: labeling it an "ordinal violation" presupposes the researcher's ordering is ground truth. Reviewer C and Reviewer D both make this point more sharply than I did. The label should be "ordinal anomaly" or "unexpected ordering," and the interpretation should acknowledge that the researcher's tier placement of *moderately* may simply be wrong, not that the model is wrong.

**Reviewer D — Prompt templates and system prompt are missing (reproducibility gap).** I flagged this as the most significant reproducibility gap, and Reviewer D's systematic reproducibility assessment confirms and extends it. The tool schema, system prompt, default state definition, and the names of the other two tasks are all missing. I agree this is the single most important pre-submission fix beyond the statistical framing issues.

**Reviewer E — BrittleBench (2026) citation is unverifiable.** I did not flag this at all. Reviewer E is correct that a 2026 citation with no full bibliographic entry cannot be verified by readers. This needs a complete citation with arXiv ID or venue details.

**Reviewer F — ε² = 0.969 in no-context condition needs a caveat.** I mentioned this briefly ("the high value is partly a consequence of the near-zero variance in the lower-tier words") but did not recommend adding an explicit caveat in the text. Reviewer F correctly identifies this as a weakness in the statistical presentation that should be addressed directly.

**Reviewer F — Section 4.4 (Downstream Consequences) is the weakest section.** I flagged this as scope drift and recommended shortening. Reviewer F agrees and adds a useful suggestion: show whether the dollar spread varies across baselines. I endorse both the diagnosis and the suggested fix.

**Reviewer C — No null/no-word control.** I listed this under Missing Sections as "no explicit statement of what the paper does NOT claim," but I did not identify the specific missing cell: what does the model output with no intensity word at all? Reviewer C and Reviewer B both identify this as a meaningful gap that would sharpen the "hedge at 0.50" interpretation. I should have flagged this explicitly.

---

## Disagreements

**Reviewer B — Missing related work (scalar implicature, Kennedy & McNally, etc.).** Reviewer B argues the paper is missing engagement with Horn scales, scalar implicature, gradable adjectives (Kennedy & McNally 2005), and Bayesian pragmatics (Lassiter & Goodman 2017). I disagree that these omissions are within my mandate to evaluate, but more substantively: for a first preprint by a sole author at this stage, requiring engagement with formal semantics literature goes beyond what the paper promises. The paper frames itself as a measurement study informed by Quirk's taxonomy, not as a contribution to formal degree semantics. The Related Work section covers the three relevant areas it promises to cover. Expanding to scalar implicature would be appropriate for a journal version but is not a gap that prevents ArXiv readiness. I stand by my original assessment that the Related Work is adequate for the stated scope.

**Reviewer C — "The framing as a psycholinguistics paper has not landed."** Reviewer C argues the paper reads as a behavioral study of an AI system, not a psycholinguistic measurement study, and notes the word "psycholinguistics" never appears. I partially disagree. The paper's framing goal — as stated in the author's brief — is that tool calling is the instrument and word interpretation is the subject. This framing does land in the abstract and introduction. The absence of the word "psycholinguistics" is a deliberate choice, not a failure: the paper is psycholinguistics-adjacent, not a psycholinguistics paper proper (which would require human subjects). Reviewer C's point that the framing could be made more explicit is valid, but the claim that it has "not landed" overstates the problem. The paper successfully avoids reading as a tool-calling paper, which is the primary framing goal.

**Reviewer D — "The paper should not say 'vague language is compressed' as a general claim about LLMs."** Reviewer D argues the abstract's closing sentence ("Vague language in action interfaces is compressed, state-dependent, and discontinuous near operational boundaries") reads as a general claim. I partially disagree with the severity of this concern. The sentence uses "is" not "are generally" or "will be," and the paper's consistent single-model framing throughout provides adequate context. However, I agree with the direction: adding "in this model and context" or equivalent qualification to the abstract's closing sentence would be a small fix that preempts a legitimate objection. I should have flagged this more explicitly in my original review.

**Reviewer B — "The split-range decomposition is post-hoc with a researcher-chosen split point."** Reviewer B flags the 25%/32% split as chosen after seeing the data. I agree this is worth noting, but I disagree that it requires more than a one-sentence acknowledgment. The split is visually obvious from Figure 3 (the convergence is clearly non-linear with a transition around 25–32%), so calling it "post-hoc" is technically accurate but somewhat misleading — the split point is not arbitrary. The paper should note it as exploratory, which is a small addition.

---

## Revisions to My Review

**Addition: The ε² additivity issue is more serious than I stated.** My original review noted the issue but called it a "framing" problem. I should have flagged it as a technical precision problem that affects the abstract, the contributions list, and the results section simultaneously. The fix is not just rewording one sentence — it requires consistent correction across three locations. I revise my assessment: this is the highest-priority fix in the paper, equal to the prompt template reproducibility gap.

**Addition: The null/no-word control is a missing section I should have identified.** I listed "no explicit statement of what the paper does NOT claim" as a missing section, but I missed the more specific and actionable gap: there is no null condition (no intensity word). Without it, the "hedge at 0.50" interpretation cannot be distinguished from "0.50 is the model's default for this task regardless of instruction." This should be added to my Missing Sections list as a concrete gap.

**Addition: The "ordinal violation" label in Figure 2b.** I noted the *moderately* anomaly in my Scope Drift section but did not flag the specific label in the figure caption as problematic. The annotation "Ordinal violation" in Figure 2b presupposes the researcher's ordering is ground truth. This should be changed to "Ordinal anomaly" or "Unexpected ordering" in both the figure and the surrounding text.

**Strengthening: Multiple comparison acknowledgment.** My original review said the acknowledgment was "adequate for a preprint" but recommended adding one sentence to the statistical methods section. Reviewers B, C, D, and F all flag this independently. The convergence of four reviewers on this point suggests my original assessment was too lenient. I revise: the absence of an explicit multiple-comparison statement in Section 3.5 (not just in the Discussion limitations) is a gap that should be fixed before ArXiv submission, not after.

**Standing by: ArXiv readiness verdict.** Despite the additional issues raised by other reviewers, I maintain that the paper is ArXiv-ready with the fixes identified. The core alignment between stated goals and delivered content is strong. The issues raised are real but are all fixable without new experiments. My original verdict stands.

---

## Blind Spots

**All reviewers missed: The "Tier 3" partial-context condition naming creates a structural confusion that is never resolved.** The paper uses "

---

## Methodology

This report was generated by the AI Research Council using 3 stages (Independent Review → Deliberation → Synthesis).

**Reviewer models:** claude-sonnet-4-6
**Chairman model:** claude-opus-4-7
**Total cost:** $4.15
