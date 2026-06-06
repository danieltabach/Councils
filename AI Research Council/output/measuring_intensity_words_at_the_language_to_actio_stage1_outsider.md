# Outsider / Red Team — stage1

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