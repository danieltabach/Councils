# Peer Reviewer — stage1

# Peer Review: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"

---

## Summary

This paper investigates how a language model (Claude Haiku) translates vague English intensity words (e.g., *slightly*, *substantially*, *drastically*) into numeric tool-call actions within a controlled synthetic resource-allocation environment. Across 6,620 runs at two temperature settings, the author documents three primary findings: (1) lexical compression — 10 words collapse to approximately 5 distinct output values; (2) state dominance — starting allocation explains ~10× more rank-based variance than word choice when context is provided; and (3) boundary discontinuity — near feasibility limits, the model switches among three behavioral modes (hedge, act, abstain) in a word-dependent manner. The paper frames these findings as evidence that natural-language control interfaces are less expressive and less stable than they appear to operators.

---

## Strengths

1. **Clean experimental isolation.** The core methodological contribution is the deterministic backend design — by ensuring the solver is noise-free, the author correctly isolates the model as the sole stochastic component. This is a genuine design insight, not a trivial choice, and it substantially strengthens causal attribution of the observed variance to the language-to-action translation step. The figure (Fig. 1) communicates this architecture clearly.

2. **The boundary behavior finding is genuinely interesting.** The hedge/act/abstain trichotomy at the 89% baseline is the paper's most striking result. The *drastically* vs. *dramatically* discontinuity — two near-synonyms producing categorically different action policies in identical system states — is not an obvious or expected finding. It has real implications for agentic system design and is the kind of result that earns citations. Fig. 5 communicates this crisply.

3. **Commendable statistical honesty.** The author explicitly flags that (a) the $\varepsilon^2 = 0.969$ effect size is inflated by deterministic decoding, (b) p-values overstate significance because within-word runs are not independent, and (c) the split-range analysis was not pre-registered. This level of self-disclosure is unusual in empirical ML papers and reflects genuine research integrity. It also partially preempts the most obvious methodological criticisms.

4. **The differentiation funnel is a well-executed secondary finding.** The complete inversion of explanatory power — from word-dominant at low baselines to state-dominant at high baselines — is a substantive result that goes beyond a simple "context matters" observation. The quantification (5:1 to 14:1 inversion) is concrete and the figures (Figs. 3, 4, 4b, 3b) present it coherently as a progression.

5. **Figures are generally high quality.** The frequency heatmaps (Figs. 2, 6) and the convergence plot (Fig. 3) are well-designed for their purpose. The delta heatmap (Fig. 4) is particularly effective at showing the joint word-state structure in a single glance. Captions are appropriately informative without being redundant with the text.

6. **Transparent scope-setting.** The paper is clear that it studies one model, one domain, one action direction, and one language. The limitations section is substantive and identifies the right gaps (human baseline, cross-model, no-word control). This is honest positioning that makes the paper more trustworthy, not less.

---

## Weaknesses

### Major Weaknesses

**W1. The absence of a no-word control is a structural gap that the paper itself identifies but does not resolve.**
The 0.50 "hedge" interpretation is the paper's central mechanistic claim for the lower-tier words. But without a condition where the model receives an increase instruction with no intensity modifier (e.g., "Architects should spend more time on innovation"), the reader cannot distinguish between two explanations: (a) weak words activate a hedging heuristic that produces 0.50, or (b) 0.50 is simply the model's default response to *any* increase request, and the words are doing nothing. The author acknowledges this in the Future Work section, but this is not a nice-to-have extension — it is the falsification condition for the paper's most prominent interpretive claim. At 30 runs × 2 temperatures = 60 API calls, the cost is negligible. Its absence from the current study is a meaningful weakness.

**W2. Single-model scope limits the strength of claims about "language-to-action interfaces."**
The paper's framing — and its alignment-adjacent implications — implicitly suggests that the findings say something about how LLMs in general handle vague intensity words. But with only Claude Haiku tested, every observed pattern could be an artifact of Anthropic's specific training pipeline, RLHF procedure, or this model's particular tokenization of these words. The paper does hedge this ("In this model and domain...") but the Discussion and Conclusion sections repeatedly slide toward broader language about "agents, copilots, and natural-language control systems" without the cross-model evidence to support that generalization. The author knows this is the next step; the issue is that the current framing slightly outruns the evidence.

**W3. The word scale is under-validated and this creates interpretive fragility.**
The researcher-constructed six-tier scale is the measurement instrument against which ordinal faithfulness ($\rho = 0.845$) is assessed. But the scale is acknowledged to be heuristic — only 3 of 10 words appear in Quirk's explicit lists. This creates a circularity problem: if the model's ordering diverges from the hypothesized scale (as it does for *moderately*), the author cannot determine whether (a) the model is wrong about *moderately*, or (b) the researcher's tier assignment for *moderately* is wrong. The paper handles this gracefully by framing the scale as a "researcher-constructed ordering" rather than a ground truth, but this simultaneously weakens the $\rho$ statistic as a meaningful measure of ordinal faithfulness. The planned human survey is the right fix, but in its absence, Spearman's $\rho$ against an unvalidated scale is a less powerful result than it appears.

**W4. The downstream consequence framing ($250K spread) is rhetorically overloaded relative to the evidence.**
The ~$250K objective-value spread is presented as evidence that "different interpretations propagate into materially different outcomes from production systems." But the dollar figure is explicitly synthetic, domain-specific, and not calibrated to any real system. Using a concrete dollar amount from a made-up environment to motivate real-world concern is a rhetorical move that may invite skepticism from reviewers. The point the author actually wants to make — that the action-level differences are non-trivial in magnitude — could be made more defensibly by staying in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars.

### Moderate Weaknesses

**W5. The "moderately" anomaly deserves more rigorous treatment.**
The finding that *moderately* maps below *slightly* (0.45 vs. 0.50) is presented as an ordinal anomaly and interpreted speculatively as a "restraint heuristic." This is actually one of the more theoretically interesting findings in the paper — it suggests the model may be reading the word's connotation ("keep things moderate") rather than its intensity magnitude. But it receives only a paragraph of treatment. A closer look at what text the model generates when it produces 0.45 vs. 0.50 (even qualitative inspection of model outputs) would substantially strengthen this interpretation.

**W6. The split-range analysis is post-hoc and the split point is researcher-chosen.**
The author discloses this ("the split point was chosen by the researcher based on observed convergence behavior, not pre-registered"), which is good. But the 5:1 to 14:1 inversion figures are then cited as though they are independent evidence. They are not — they were derived from a split chosen to maximize the contrast. The overall 10:1 ratio from the pre-specified analysis is the defensible number; the split-range figures are illustrative at best.

**W7. The paper does not show the model's text outputs, only its numeric actions.**
For several findings — especially the abstention behavior and the *moderately* anomaly — the author makes claims about what the model is "thinking" (e.g., "the model produces a text response acknowledging the request but declines to invoke the allocation tool, typically citing the constraint that allocations must sum to 100%"). This is stated as a factual description of model behavior, but the actual text responses are never shown. Including even a representative example or two (in an appendix if space is tight) would ground these claims considerably.

---

## Questions for Authors

1. **No-word control:** Why was the no-word control not included in the current study given its low cost and its centrality to the 0.50 hedge interpretation? If you ran it subsequently, what did it show?

2. **Moderately's text output:** What does the model actually say when it produces 0.45 for *moderately*? Does it use language consistent with a "restraint" interpretation (e.g., "I'll keep this moderate" vs. "I'll increase this by a moderate amount")? Even 5 examples would be informative.

3. **The 0.50 anchor in context-conditioned runs:** In the context-conditioned condition at low baselines (e.g., b=0%), weak words produce outputs of 0.10 (not 0.50 as in the no-context condition). Does this suggest the 0.50 "hedge" in the no-context condition is specifically a response to the *absence of a reference point* rather than a property of the words themselves? If so, this seems like an important clarification of the mechanism.

4. **Abstention at other baselines:** The paper focuses abstention analysis on the 89% baseline. Were there any abstentions at lower baselines (e.g., 75%)? If abstention begins earlier for some words, the transition point would be informative.

5. **The $\rho$ computation:** Spearman's $\rho$ is computed "over all individual run observations" pairing each run's tier with its output. At T=0.0, where within-word variance is near zero for most words, this computation is effectively equivalent to computing $\rho$ over the 10 word-medians. Is this correct? If so, the n=300 framing overstates the effective sample size considerably, and it would be cleaner to present $\rho$ over the 10 medians directly.

6. **The 75% convergence point:** All 10 words converge to 0.80 at the 75% baseline. Is 0.80 a round-number anchor (the next 5% increment above 75%), or is it the maximum feasible given the three-task constraint? Understanding which would help distinguish a rounding/anchoring effect from a constraint-satisfaction effect.

7. **Prompt text:** The paper describes the prompts but does not reproduce them verbatim. Can the exact system prompt and user prompt templates be provided (in an appendix or supplementary material)? For reproducibility and to assess whether the prompt structure itself might be inducing some of the observed behavior.

---

## Minor Issues

1. **Section 4.1, paragraph 2:** "Figure~\ref{fig:medians} shows the same pattern as Figure~\ref{fig:frequency}" — this sentence is redundant; both figures are described as showing the same thing. Consider either merging the figures or differentiating what each contributes.

2. **Section 3.4:** The phrase "don't assume any underlying distributions" should be "do not assume any underlying distributions" for formal register consistency.

3. **Section 4.2:** "the context of a 'current allocation' (our baseline variable)" — the parenthetical is unnecessary; "baseline" has been defined earlier.

4. **Table 1 caption:** The note that "only three of the 10 words appear in Quirk's explicit lists" is important and should arguably be in the main text rather than only in the caption and a footnote, given how much interpretive weight the Quirk framing carries.

5. **Section 4.4, dollar figures:** The negative sign on the objective-value deltas (−$424K, −$675K) is confusing without explanation. If higher allocation produces a more negative delta (i.e., the objective is a cost), this should be stated explicitly. The reader cannot tell from context whether negative is better or worse.

6. **Figure 3 (fig3_convergence.pdf):** The *drastically* line is visually noisy relative to other words (large oscillations at low baselines), making it hard to read in the context of the other 9 lines. A brief note in the caption or text explaining why *drastically* behaves erratically at low baselines (rather than just at the high boundary) would help.

7. **Section 5, "A preliminary observation on numeric format sensitivity":** This is a genuinely interesting observation but is buried in the Discussion. Given the paper's emphasis on state dependence, this could be elevated — or alternatively flagged more clearly as a secondary, informal observation requiring future confirmation.

8. **Abstract:** The abstract is well-written and accurate, but the phrase "informed by the Quirk et al. degree-modifier taxonomy" should note that the mapping is heuristic/partial, as the paper itself emphasizes throughout. The abstract currently implies more systematic grounding in Quirk than the paper delivers.

---

## Recommendation

**Weak Accept** (for a workshop venue or empirical findings track; **Borderline** for a full conference main track)

### Rationale

This is a carefully executed, honestly reported empirical study with a clean methodological core and at least one genuinely interesting finding (the hedge/act/abstain boundary behavior). The author demonstrates real experimental instincts: isolating the stochastic component, reporting effect size inflation, flagging non-independence. These are not common in first papers.

The weaknesses are real but not fatal. The absence of the no-word control is the most significant gap — it is cheap to fix and important to the central claim. The single-model scope is a limitation the paper acknowledges but does not always honor in its framing. The unvalidated word scale creates interpretive fragility around the Spearman $\rho$ result.

**Addressing the author's specific ask directly:** The cornerstone question the author poses — is this paper (a) a domain-general measurement instrument, (b) a fine niche result with inflated framing, or (c) something between — the honest answer is **(c), leaning toward (b) in its current form, with a clear path to (a)**. The paper is a solid first measurement slice. The boundary behavior finding and the differentiation funnel are real contributions. But the single-model scope, the unvalidated scale, and the missing no-word control mean it cannot yet bear the weight of the broader "alignment/deployment safety" framing the author wants to place on it. The path to (a) runs through: (1) the no-word control (cheap, do it now), (2) the human survey (closes the ordinality gap), and (3) one cross-model replication (GPT-4o or Gemini Flash). With those three additions, the paper becomes a substantially stronger instrument. Without them, it is an interesting and honest single-model observation — valuable, but not yet the cornerstone the author envisions.

The field framing in the author's vision brief is legitimate and the bet is reasonable, but the paper as currently written should be positioned as "first measurement slice" (which it already calls itself) rather than as evidence for the broader program. The vision is larger than the paper, and that gap is currently visible in the Discussion section's occasional overreach. Narrowing the claims to what the data actually supports would strengthen, not weaken, the paper's reception.

---

## Confidence

**4/5** — I have read the paper carefully including all figures, the methodology is clear enough to evaluate, and the statistical approach is transparent. I am not a specialist in degree-modifier linguistics and cannot assess the Quirk taxonomy framing at depth; a linguist reviewer would add value here. My confidence in the experimental design evaluation and the alignment/safety framing assessment is high.