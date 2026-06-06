# Source Auditor — stage2

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