# Alignment Guide — stage1

# Alignment Guide Review: "Does Slightly Mean Somewhat?"

---

## Stated Goals vs. Delivered Content

The paper makes four explicit contribution promises in the introduction. Here is the accounting:

**Contribution 1: A controlled method for measuring how a language model maps vague intensity words to numeric actions.**
✅ Delivered. The experimental design (Figure 1, Section 3) is clearly specified, the isolation logic is sound and explained, and the two-condition structure (no-context / context-conditioned) directly serves this methodological claim.

**Contribution 2: Evidence that the model preserves coarse intensity regimes while collapsing fine-grained distinctions.**
✅ Delivered. Sections 4.1 and the frequency map (Figure 2) directly support this. The 10→5 compression finding is the paper's cleanest result.

**Contribution 3: Evidence that context state dominates word choice (~10x variance ratio).**
✅ Delivered. Section 4.2, the differentiation funnel, and the split-range inversion (5:1 → 14:1) all serve this claim. The paper is appropriately careful about the independence caveat on the two ε² values.

**Contribution 4: Discovery of word-dependent abstention near feasibility boundaries (hedge/act/abstain).**
✅ Delivered. Section 4.3 and Figure 5 directly document this. The *drastically* vs. *dramatically* discontinuity is the paper's most distinctive and safety-relevant finding.

**Three empirical questions from the introduction:**
- Q1 (ordinal ranking preserved?) → Answered in 4.1. ✅
- Q2 (word or state explains more variance?) → Answered in 4.2. ✅
- Q3 (smooth scaling or mode-switching near limits?) → Answered in 4.3. ✅

**Overall verdict:** The paper does what it says it will do. The match between stated goals and delivered content is unusually clean for a first study. No major promises go unfulfilled.

---

## Scope Drift Analysis

The paper stays tightly on thesis with two minor drift zones worth flagging:

**Section 4.4 (Downstream Consequences) — mild drift, low risk.**
The $250K swing figure is compelling, but the paper already acknowledged in Section 3.2 that "the exact dollar scale is specific to the synthetic environment." The section does real work (demonstrating that the linguistic effects propagate into material outcomes), but it risks being read as a claim about the real-world stakes of *this specific environment*, which the paper explicitly disclaims. The section is short enough that it doesn't derail anything, but the framing should be tightened: the dollar figure is an illustration of *propagation*, not a finding about magnitude.

**Section 5 Discussion, "Mechanistic speculation" paragraph — moderate drift.**
This paragraph raises three possible explanations for the 0.50 hedge (training data frequency, RLHF reward shaping, maximal noncommittal hedging) and explicitly says "I do not resolve this question here." That's honest, but the paragraph ventures into mechanistic territory the paper has no data to address. It reads as intellectual throat-clearing. It doesn't damage the paper, but it introduces a framing (RLHF reward shaping) that belongs to a different kind of study. Given the author's stated concern about retrofitting grand narratives onto the paper, this paragraph is worth watching — it's the seed of scope inflation.

**Section 5 Discussion, "A preliminary observation on numeric format sensitivity" paragraph — moderate drift.**
This observation (round inputs → round outputs, irregular inputs → irregular outputs) is interesting, but it is explicitly flagged as "based on visual inspection" and "preliminary." It introduces a new variable (input format/precision) that was not part of the paper's three stated research questions. It belongs in Future Work, not Discussion. Leaving it in Discussion gives it more weight than the evidence warrants.

---

## Redundant Sections

**Figures 2 and 2b tell the same story twice.**
Figure 2 (frequency map) and Figure 2b (median bar chart) both show the 10→5 compression pattern. The frequency map is the richer visualization; the bar chart adds the ordinal anomaly annotation but could be integrated into the frequency map's caption or a single combined figure. As standalone figures, they create redundancy in the visual narrative of Section 4.1. One could be moved to an appendix without losing the finding.

**Section 4.5 (Robustness Across Temperature) is structurally sound but could be condensed.**
Table 1 and Figure 6 together with the section text repeat the same conclusion three times: temperature broadens distributions but doesn't restore ordinal structure. The section is doing real work (temperature robustness is a legitimate check), but the prose could be cut by half without losing anything. The key sentence is already in the abstract: "stochastic sampling broadening distributions but not restoring ordinal distinctions."

---

## Missing Sections

These are gaps between what the paper implies and what it delivers — not criticisms of the study's scope, but alignment issues between promise and content.

**The no-word control is absent, and the paper knows it.**
The Future Work section explicitly flags this: "Without this null baseline, the 0.50 'hedge' interpretation cannot be fully distinguished from the possibility that 0.50 is the model's default response to any increase request." This is a genuine hole in Contribution 2 and the hedge interpretation. The paper's central interpretive claim about the 0.50 value as a *hedge* (rather than a default) is currently unfalsified within the paper. The Discussion section uses "hedge" as settled language when it is actually a hypothesis. This should be softened in the Discussion to match the epistemic status acknowledged in Future Work.

**The split-range inversion finding (5:1 → 14:1) is underemphasized relative to its importance.**
The finding that the word-vs-state dominance relationship *completely inverts* depending on where you are in the allocation space is arguably more important than the overall 10:1 ratio. It means the same interface behaves fundamentally differently depending on system state — which is precisely the alignment-relevant finding. This result appears in Section 4.2 but is not surfaced in the abstract or conclusion. The abstract reports the overall 10:1 ratio; the inversion is buried in the body. Given that the inversion is the most operationally dangerous pattern (the interface *looks* word-driven at low baselines and *becomes* state-driven at high baselines, invisibly to the operator), it deserves abstract-level visibility.

**The connection between the three findings is not explicitly drawn.**
The paper documents three patterns (compression, state dominance, boundary mode-switching) as separate results. But the alignment-relevant insight — that these three failures compound near operational boundaries — is never stated as a unified claim. Near capacity: compression is total (all words → same output), state dominance is maximal (14:1), and mode-switching is active (hedge/act/abstain). The three failures are worst simultaneously, at exactly the point where the system is most constrained and decisions are most consequential. This synthesis belongs in the Discussion and Conclusion but is currently absent. It's the paper's strongest single claim and it's not made.

---

## Structural Recommendations

**1. Move "numeric format sensitivity" from Discussion to Future Work.**
The paragraph is a preliminary observation without analysis. It dilutes the Discussion's focus and introduces a variable not addressed by the paper's research questions. Moving it to Future Work (where a "denser baseline grid" is already planned) is a one-paragraph relocation that tightens the Discussion significantly.

**2. Soften "hedge" language in Discussion to match Future Work's epistemic honesty.**
The Discussion uses "hedge" as a settled interpretation; Future Work correctly flags that the no-word control is needed to confirm it. Align the Discussion's language: "what appears to function as a hedge" or "a pattern consistent with hedging" rather than "functions as a hedge."

**3. Add a synthesis paragraph to Discussion and Conclusion.**
State explicitly that the three failure modes (compression, state dominance, mode-switching) are worst simultaneously near operational boundaries. This is the paper's most important finding and it is currently implicit rather than stated. One paragraph in Discussion, one sentence in Conclusion.

**4. Surface the inversion finding (5:1 → 14:1) in the abstract.**
The abstract reports the overall 10:1 ratio but not the inversion. The inversion is the more alarming result for anyone deploying vague-language interfaces. A single sentence in the abstract — something like "this ratio masks a complete inversion: word choice dominates at low baselines while state dominates entirely at high baselines" — would accurately represent the paper's most operationally significant finding.

**5. Consolidate Figures 2 and 2b or move one to an appendix.**
Both show the same compression pattern. The frequency map (Fig 2) is the more informative visualization. The median bar chart (Fig 2b) adds the ordinal anomaly annotation, which could be incorporated into Fig 2's caption. Consolidating saves space and eliminates the impression that the same finding is being shown twice.

**6. Consider whether Section 4.4 (Downstream Consequences) earns its place as a standalone section.**
The $250K figure is a useful illustration of propagation, but the section is two short paragraphs and the finding is straightforwardly implied by the design. It could be folded into the Discussion's "alignment framing" paragraph as a single sentence: "In this environment, the compression documented above propagates into a ~$250K objective-value spread driven entirely by word choice." This would tighten the Results section without losing the point.

---

## Title and Abstract Accuracy

**Title: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"**

The title is accurate and appropriately scoped. It names the central question (do near-synonyms produce distinct outputs?), signals the measurement orientation, and correctly identifies the construct (vague intensity words) and the domain (LLM numeric actions). It does not overclaim. One minor note: the title foregrounds the compression finding (slightly vs. somewhat) but the paper's most distinctive finding is the boundary mode-switching (*drastically* vs. *dramatically* producing categorically different behavior). The title could hint at the action-mode finding without becoming unwieldy, but this is a low-priority concern — the current title is defensible.

**Abstract accuracy:**

The abstract accurately represents the three main findings and is appropriately hedged ("in this model and domain"). Two alignment issues:

- The abstract reports "separate Kruskal-Wallis tests show that grouping by starting allocation captures far more rank-based variance than grouping by word (ε²_baseline = 0.782 vs. ε²_word = 0.079)" — this is accurate and the independence caveat is correctly noted in the methods. ✅

- The abstract does not mention the inversion finding (5:1 → 14:1 flip). Given that the inversion is arguably the most operationally important result, its absence from the abstract is a gap between what the paper delivers and what the abstract promises. The abstract implies a stable 10:1 dominance relationship; the paper shows it completely reverses. This should be surfaced. ⚠️

- The abstract's three-pattern summary (compression, state dependence, boundary mode-switching) correctly maps to the paper's three research questions and three results sections. ✅

---

## Author's Brief: Direct Response to the Cornerstone Question

The author asked whether the paper can "bear the weight" of a larger field-building program, and requested narrowing if scope inflation is detected.

**On alignment between paper and vision:** The paper itself is well-aligned internally. The vision document is not the paper, and the council review of the vision is outside this mandate. What I can say from an alignment perspective is this: the paper's internal coherence is strong, but it currently undersells its most field-relevant finding. The inversion result — that the same natural-language interface is word-driven at low baselines and state-driven at high baselines, invisibly to the operator — is the finding that most directly instantiates the "passive failure" framing the author cares about. It is currently buried. Surfacing it (abstract, synthesis paragraph in Discussion, Conclusion) would make the paper a stronger cornerstone without adding a single new experiment. That is the highest-return structural move available before submission.

**The one thing the paper claims that isn't yet supported:** The "hedge" interpretation of 0.50 is used as settled language in the Discussion but is explicitly flagged as unconfirmed in Future Work. This is the paper's only internal inconsistency between what it claims and what it has evidence for. It is fixable with a single word change ("appears to function as a hedge" rather than "functions as a hedge") and does not require additional data.