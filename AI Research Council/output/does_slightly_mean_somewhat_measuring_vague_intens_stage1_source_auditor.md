# Source Auditor — stage1

Now I have sufficient information to produce a thorough, structured Source Audit. Let me compile the full review.

---

# Source Audit: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"

---

## Verified Claims

### Cliff (1959) — Core Citation

The paper cites Cliff (1959) for the claim that "adverbs such as *slightly* and *extremely* can behave as stable multipliers of perceived adjective intensity." Cliff's 1959 paper "Adverbs as multipliers" (*Psychological Review*, 66, 27–44) tested an equation with nine intensive adverbs and 15 evaluative adjectives. The paper's characterization of the finding — that adverbs act as multipliers of adjective intensity — is consistent with what the source demonstrates. Subsequent work confirmed the stability of the multiplying values of intensive adverbs across different rating dimensions, supporting the multiplicative function proposed by Cliff (1959).

**Flag:** The paper's specific claim that Cliff showed adverbs "can behave as stable multipliers" is essentially correct, but the paper does not note that Cliff's study used *evaluative* adjectives in a rating paradigm, not action-production contexts. The parallel to the present study is motivational, not structural. This is a legitimate use of the citation, but the construct gap is worth noting.

---

### Mosteller & Youtz (1990) — Core Citation

The paper characterizes Mosteller & Youtz (1990) as having "compiled numeric interpretations of probability expressions and showed high variance around ordered central tendencies." Mosteller and Youtz (1990) tabulated numerical averages of opinions on quantitative meanings of 52 qualitative probabilistic expressions across 20 different studies. In spite of variety in populations, format, instructions, and context, the variation of the averages for most expressions was modest, though one exception was *possible*, which had distinctly different meanings for different people.

**Flag — Partial Mischaracterization:** The paper says Mosteller & Youtz "showed high variance around ordered central tendencies." The actual finding is more nuanced: the variation of the averages for most expressions was *modest*, suggesting they might be useful for codification. The paper's description of "high variance" is an overstatement of the source. What Mosteller & Youtz found was high *individual-level* variance but relatively stable *cross-study averages* — almost the opposite emphasis. This is a minor but real mischaracterization.

---

### Ramotowska et al. (2024) — Core Citation

Ramotowska et al. (2024) investigate, by means of a computational model, how individuals map quantifiers onto numbers and how they order quantifiers on a mental line, selecting five English quantifiers (*few*, *fewer than half*, *many*, *more than half*, and *most*). The paper's claim that this work studies "human interpretation of vague quantifiers such as 'many' and 'most'" is accurate. The paper's broader claim that "ordinal ranking tends to be preserved even when numeric interpretation varies across individuals" is also consistent with the literature, though it is stated as a general finding drawn from multiple sources (Cliff, Mosteller, Ramotowska), not from Ramotowska alone. That attribution is reasonable.

---

### Brittlebench (2026) — Core Citation

The paper cites Brittlebench (2026) for the claim that "model outputs can vary with semantically small wording changes." Brittlebench addresses how existing evaluation methods fail to capture the noise and variability inherent in real-world user inputs, including how language models face queries containing mistakes, typos, or alternative ways of phrasing the same question, and introduces a framework for quantifying model sensitivity to prompt variants. Using this framework, model performance was observed to degrade as much as 12% under semantics-preserving perturbations.

**Flag — Construct Mismatch:** The paper uses Brittlebench to establish that "semantically equivalent paraphrases produce different outputs," then distinguishes its own study as examining "semantically *distinct* intensity words." This is a legitimate and well-drawn contrast. However, the paper should note that Brittlebench applies semantics-*preserving* perturbations (i.e., same meaning, different form), whereas the present study's words are not semantically equivalent — they differ in intensity. The distinction the paper draws is correct; the citation use is appropriate.

---

### Ramamonjison (2022) and Ahmadi (2023) — Background Citations

The paper cites these for the claim that "natural-language interfaces to optimization and planning systems typically assume that the user request is sufficiently specified before solving begins." The most common approach to integrating LLMs with optimization is autoformulation, and the NL4Opt Competition investigated how natural language processing can produce optimization formulations from text (Ramamonjison et al. 2022, 2023). AhmadiTeshnizi et al. (2023) developed a modular system (OptiMUS) for complex descriptions. These citations support the general framing of NL-to-optimization work. The specific claim that these systems "assume the request is sufficiently specified" is a reasonable inference from the autoformulation paradigm, though it is not a direct quote or finding from either source. This is a mild extrapolation, not a misattribution.

---

### Quirk et al. (1985) — Taxonomy Citation

The paper is notably careful here. It states explicitly that "only three of the 10 words appear in Quirk's explicit lists; the remaining seven were chosen heuristically to fill categorical gaps." This is an honest and important disclosure. Quirk et al.'s *Comprehensive Grammar of the English Language* (1985) covers degree modifiers in Chapter 8, "The semantics and grammar of adverbials." The paper's reference to "sections 8.104–8.115" is specific and plausible for the degree-modifier taxonomy, though this reviewer cannot independently verify the exact section numbers from available sources. This is flagged below as unverifiable from text alone.

---

### Zhang et al. (2024) — LLM Probability Calibration

The paper cites Zhang et al. (2024) for the finding that "model interpretations are prone to diverge from human calibration" when mapping words of estimative probability to numeric probabilities. This characterization is broadly consistent with the literature on LLM probability calibration. RLHF fine-tuned LLMs are generally found to be poorly calibrated. The specific "Zhang et al. 2024" citation is used in the paper's arXiv version and appears to refer to work on verbalized probability calibration in LLMs. This citation could not be fully verified against a specific paper with that exact author-year combination; this is flagged below.

---

### Kruskal-Wallis ε² Usage

The paper uses ε² as the effect size for Kruskal-Wallis tests and interprets values of 0.782 and 0.079 as capturing proportions of "rank-based variance." Epsilon-squared (ε²) is an effect size measure for the Kruskal-Wallis nonparametric test, analogous to eta-squared in ANOVA, and is computed as ε² = H / (n − 1), where H is the Kruskal-Wallis statistic and n is the total sample size. The paper's description of ε² as capturing "rank-based variance" is accurate. The paper's explicit warning that the two ε² values "come from separate tests rather than a single model" and "should not be added together or treated as shares of a single pie" reflects a sophisticated and correct understanding of the statistic's interpretation.

---

## Unsupported or Weakly Supported Claims

### 1. "Prior work shows that humans often preserve ordinal structure across vague expressions even when numeric interpretation varies"

This is cited to Cliff (1959), Mosteller & Youtz (1990), and Ramotowska et al. (2024). The claim is directionally correct for the Cliff and Ramotowska literature, which does show ordinal stability. However, as noted above, Mosteller & Youtz (1990) is about *probability* expressions, not degree modifiers, and the paper itself acknowledges this is "a related but distinct mapping." Treating Mosteller & Youtz as evidence for ordinal preservation of *intensity* adverbs is a stretch; the ordinal-preservation finding is better anchored in Cliff (1959) alone for intensity adverbs specifically.

### 2. The 0.50 "hedge" interpretation and its mechanistic explanations

The paper offers three mechanistic explanations for why the model defaults to 0.50: training data frequency, RLHF effects rewarding moderate responses, and maximal non-commitment. These are presented as "possibilities worth noting" without citations. This is honest framing, but all three remain entirely speculative and unverifiable from the experimental design. The paper acknowledges this explicitly ("I do not resolve this question here"), so this is not a flaw in presentation — but it is a significant gap in the evidentiary chain.

### 3. "A highly regulated bank, using a language model to set staffing across 3,700+ branches" (Author's Brief, not in paper)

This claim appears only in the author's research framing brief, not in the paper itself. No source or verification is provided. It is not a claim in the paper and therefore falls outside the formal audit scope, but is noted for completeness.

### 4. Downstream consequence: "~$250K swing from word choice alone"

The paper states: "median objective-value deltas range from approximately −$424K for *moderately* to approximately −$675K for *dramatically* and *drastically*, a spread of about $250K driven entirely by word choice." This figure is presented as a descriptive result from the synthetic backend. The paper appropriately qualifies it: "The exact dollar scale is specific to the synthetic environment and the testbed." However, no description of the synthetic environment's parameterization is provided that would allow a reader to verify or reproduce the dollar figures. The claim that the spread is "attributable to the model's interpretation of the intensity word, not to system noise" is internally consistent given the deterministic backend design, but the dollar values themselves are **unverifiable from text alone** without access to the backend code and parameters.

### 5. "Even at T=0.0, the no-context condition is not perfectly deterministic: 4 of 10 words produce more than one distinct value across 30 runs"

This is stated as a factual claim in Section 4.5, but it appears inconsistent with the frequency map in Figure 2 (fig2_frequency.pdf), which shows all runs at T=0.0 landing on single values for all 10 words. This is flagged in detail under **Internal Consistency** below.

---

## Citation Issues

### Issue 1: Mosteller & Youtz (1990) — Page Range Discrepancy

The paper cites Mosteller & Youtz (1990) as *Statistical Science* pp. 2–12. The actual publication is "Quantifying Probabilistic Expressions," *Statistical Science* 5(1): 2–34. The paper's bibliography entry truncates the page range (pp. 2–12 rather than 2–34). This is a minor bibliographic error but worth correcting.

### Issue 2: Zhang et al. (2024) — Underspecified Reference

The paper cites "zhang2024" for the claim about LLM miscalibration of probability words. The arXiv version of the paper (found at arxiv.org/html/2605.21827) also uses this citation. No full title, journal, or venue is available in the text to allow independent verification. There are multiple Zhang et al. (2024) papers on LLM calibration (e.g., the "Calibrating Verbalized Probabilities" line of work). Without a full bibliographic entry visible in the submitted text, this citation is **partially unverifiable**. The general claim it supports is well-attested in the literature, but the specific attribution cannot be confirmed.

### Issue 3: Brittlebench (2026) — Citation Characterization

The paper describes Brittlebench as studying whether "semantically equivalent paraphrases produce different outputs." This is accurate. Brittlebench introduces a theoretical framework for quantifying model sensitivity to prompt variants, or brittleness, using semantics-preserving perturbations across a suite of popular benchmarks. The paper's use of this citation to establish a contrast with its own study (semantically *distinct* words) is valid and well-reasoned.

### Issue 4: Quirk et al. (1985) Section Numbers

The paper references "sections 8.104–8.115" of Quirk et al. for the degree-modifier taxonomy. The table of contents found confirms Chapter 8 covers "The semantics and grammar of adverbials," which is the correct chapter. The specific section numbers (8.104–8.115) are plausible for this coverage but **cannot be independently verified from available sources** without physical access to the text. This is flagged as unverifiable from text alone.

### Issue 5: Ahmadi (2023) Citation Key

The paper uses the citation key "ahmadi2023" and refers to a system for "natural-language interfaces to optimization." Search results confirm AhmadiTeshnizi et al. (2023/2024) developed OptiMUS, a multi-agent architecture for formulating and solving mixed-integer programs from natural language. Agentic methods included OptiMUS (AhmadiTeshnizi et al., 2023), a modular system for complex descriptions. However, the paper's claim that this work "assumes the user request is sufficiently specified before solving begins" is an inference, not a direct finding of that paper. The characterization is reasonable but not directly citable to the source.

---

## Missing Citations

### 1. The "0.50 as hedge" claim — No citation for the RLHF moderation hypothesis

The claim that RLHF fine-tuning "may reward moderate, noncommittal responses under uncertainty, pushing the model toward the midpoint" is a substantive mechanistic hypothesis with no citation. There is a body of literature on RLHF reward-hacking and overconfidence/underconfidence effects that could be cited here. The absence is not a flaw in the result, but it weakens the mechanistic discussion.

### 2. Spearman's ρ as a measure of ordinal faithfulness — No methodological citation

The paper uses Spearman's ρ throughout as its primary measure of ordinal consistency. No citation is provided for the use of this statistic in this context. While Spearman's ρ is standard, a citation to a methodological reference for its use in measuring rank-order preservation in psycholinguistic or behavioral studies would be appropriate given the paper's interdisciplinary audience.

### 3. The "no-word control" gap acknowledgment

The paper correctly identifies the absence of a no-word control as a limitation. However, it does not cite any precedent for the use of null-modifier baselines in similar studies, which would strengthen the argument for why this gap matters.

### 4. Claude Haiku model card or technical report

The model under test is identified as `claude-haiku-4-5-20251001` accessed through the Anthropic API. No citation to an Anthropic technical report or model card is provided. For reproducibility and for readers who want to understand the model's training, a citation to available Anthropic documentation is expected by convention.

### 5. The "differentiation funnel" label

The paper introduces "differentiation funnel" as a descriptive concept. This appears to be an original coinage by the author. No prior use is cited, which is fine if it is original — but if the author intends it as a general concept applicable across models, a brief note clarifying it is a term introduced in this paper would be appropriate.

---

## Internal Consistency

### ⚠️ Critical Inconsistency: T=0.0 Determinism Claim vs. Figure 2

**Section 4.5 states:** "Even at T=0.0, the no-context condition is not perfectly deterministic: 