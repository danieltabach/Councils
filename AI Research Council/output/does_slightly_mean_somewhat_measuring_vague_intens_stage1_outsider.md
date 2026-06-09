# Outsider / Red Team — stage1

# Outsider Review: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"

---

## First Impressions

This paper asks a genuinely interesting question: when you tell an AI system to "slightly increase" something versus "drastically increase" something, does the word choice actually matter in a predictable way? The answer turns out to be: sort of, but not as cleanly as you'd hope, and the current state of the system matters more than the word you chose.

My gut reaction after a first read is that this is careful, honest, small-scope empirical work. The author is unusually transparent about limitations — flagging inflated statistics, non-pre-registered analysis choices, and missing controls. That transparency is refreshing and, paradoxically, makes the work more credible. The core findings are legible and the figures are genuinely useful.

However, I came away with a nagging concern: the paper studies one AI system, in one synthetic environment, using one direction of change (always "increase"), with a word scale the author invented, against a human baseline that doesn't exist yet. The findings are real but their generalizability is essentially unknown. The author knows this — it's all in the limitations — but the framing sometimes reaches further than the data supports.

On the author's specific question about whether this paper can serve as the "cornerstone" of a larger field: I have significant doubts, which I'll detail. But I want to be clear that doubting the cornerstone claim is not the same as doubting the paper's value. These are separable questions.

---

## Accessibility Assessment

**What works well:** The paper is structured logically. The experimental design figure (Figure 1) is excellent — I understood the setup immediately. The plain-language descriptions of findings are clear. The author explains *why* they used nonparametric statistics rather than just deploying them.

**Where it loses me:**

The word scale construction is the first place I got confused. The author says the 10 words are "informed by the Quirk et al. degree-modifier taxonomy" but then says only 3 of the 10 words actually appear in Quirk's lists. The remaining 7 were "chosen heuristically." This means the ordering of words into tiers is the author's judgment. The paper then measures whether the AI preserves this ordering — but the ordering itself was never validated. The paper acknowledges this, but the acknowledgment comes in a footnote and in the limitations section, not prominently in the introduction where it would change how a reader interprets everything that follows.

The ε² statistic is explained, but the explanation ("proportion of rank-based variance explained") is technical enough that I had to re-read it several times. More importantly, the paper is careful to say the two ε² values (0.782 and 0.079) come from *separate tests* and can't be added together — but then immediately uses the ratio "10 times more" as if they can be compared directly. Even if this comparison is technically defensible, it feels like having it both ways.

The "deterministic backend" is described as a measuring instrument, but I never fully understood what it is. It converts allocations into an "objective value" measured in dollars. Where do the dollars come from? What is being optimized? The paper says this is a "synthetic constrained resource-allocation environment" but the description of what that means in practice is thin. I understand *why* the paper doesn't want to make this the focus — the backend is deliberately just a measurement instrument — but I needed more to follow the downstream consequences section.

---

## Logical Gaps

**Gap 1: The word scale is the thing being tested, but it was constructed by the researcher.**

The paper asks "does the model preserve the ordinal ranking of intensity words?" But the ordinal ranking is the author's. If the model puts "moderately" below "slightly," the paper calls this an "ordinal anomaly." But how do we know it's anomalous rather than correct? Without a human baseline, the researcher's intuition *is* the ground truth. The paper acknowledges this but doesn't fully reckon with the implication: the Spearman ρ = 0.845 measures agreement between the model and the author's judgment, not agreement between the model and some validated human standard.

**Gap 2: The 0.50 "hedge" interpretation is asserted without a control.**

The paper's most interesting interpretive claim is that 0.50 functions as a "hedge" — the model defaults to the midpoint when uncertain about magnitude. But without a no-word control (the author acknowledges this gap), we can't distinguish "0.50 is what the model does when it hears a weak intensity word" from "0.50 is what the model does when asked to increase anything." If someone just typed "increase innovation" with no intensity word and got 0.50, the hedge interpretation would be weakened considerably. The paper lists this as future work, but the hedge interpretation is used as an explanatory concept throughout the paper.

**Gap 3: The jump from "compression" to "alignment problem."**

The paper moves from the empirical finding (words compress to fewer outputs) to the claim that this represents an "alignment problem" — specifically, that the model fails to preserve operator intent. But this requires an unstated assumption: that the operator's intent was that these words should produce *different* numeric outputs. What if "slightly" and "marginally" genuinely mean the same thing to most people? What if 0.50 is actually the right answer for a weak increase with no context? The paper cannot answer this without the human baseline, yet it frames the compression as a failure rather than as a potentially accurate reflection of genuine linguistic ambiguity.

**Gap 4: The "drastically vs. dramatically" discontinuity is striking but underexplained.**

The paper calls this a "genuine, slightly unsettling result" (in the author's brief) and it is — at 89% allocation, "drastically" acts (pushes to ceiling) while "dramatically" abstains 97% of the time. But the paper's explanation is brief: "drastically" functions as "as much as possible," which remains satisfiable even near a constraint. This is plausible but it's a post-hoc interpretation. The paper doesn't show the model's actual text responses in these cases, which would be the most direct evidence for or against this interpretation. I wanted to see what the model actually *said* when it abstained with "dramatically" versus when it acted with "drastically."

**Gap 5: The $250K downstream consequence figure.**

This is presented as evidence that "different interpretations propagate into materially different outcomes." But the dollar figure comes from a synthetic environment with parameters the author set. The paper says "the exact dollar scale is specific to the synthetic environment." This is honest, but it means the $250K is not a finding — it's an illustration. The way it's presented in the abstract and results section, a reader could easily mistake it for a real-world consequence.

---

## Undefined Jargon

- **RLHF (Reinforcement Learning from Human Feedback)**: Used without definition; explained in a parenthetical only when it appears as a possible explanation for the 0.50 hedge.
- **Tool call / structured tool call**: Used throughout without explaining what this means mechanically. I inferred it means the AI outputs a formatted command rather than free text, but this was never stated.
- **Kruskal-Wallis H test**: Explained as "analogous to ANOVA," which helps, but "ANOVA" is also jargon for many readers.
- **IQR (interquartile range)**: Used in Table 1 without definition.
- **Spearman's ρ**: Explained reasonably well, but the explanation is embedded in a methods subsection that readers might skip.
- **Degree modifiers / amplifiers / downtoners / boosters / diminishers**: Quirk's taxonomy terms are used as organizational scaffolding but the distinctions between them are never explained. I couldn't tell from reading the paper what makes a "booster" different from an "amplifier."
- **Frontier models**: Used in future work section without definition.
- **Temperature (T=0.0, T=0.7)**: Explained briefly as stochastic sampling, but a non-expert would not understand what this parameter actually does to the model's behavior or why it matters.
- **ε² (epsilon-squared)**: Defined as "proportion of rank-based variance explained" but this phrasing is itself technical.

---

## Unconvincing Arguments

**1. The "alignment framing" in the discussion feels retrofitted.**

The paper's discussion section includes a paragraph titled "Alignment framing" that states the findings fit "a narrow but important version of an alignment problem." This paragraph reads like it was added to elevate the paper's significance rather than because the data directly supports an alignment interpretation. The paper studied whether words map stably to numbers in a synthetic allocation task. The leap to "model-mediated action interface fails to preserve operator's intended semantics" requires several unstated assumptions about what the operator intended, what they would have expected, and whether the model's behavior deviates from that expectation. The paper cannot demonstrate this without the human baseline.

**2. The temperature robustness section is presented as a positive finding but could be read as a negative one.**

The paper says temperature is "structurally non-corrective but behaviorally consequential." This means: raising temperature doesn't fix the compression problem, it just adds noise. This is framed as confirming robustness of the main findings, which is true — but it also means there's no easy fix. The paper presents this somewhat neutrally when it could be a more pointed finding.

**3. The "differentiation funnel" is an evocative name for a phenomenon that might be trivially expected.**

When a system is near its maximum capacity, any instruction to increase it will produce a small increase regardless of the word used — because there's no room to increase more. The paper treats the convergence of word interpretations near 89% as a finding, but this might follow directly from the constraint structure of the environment. If "drastically increase" when you're at 89% can only mean "go to ~91%," and "slightly increase" also means "go to ~91%," then the convergence is a mathematical consequence of the constraint, not a finding about language interpretation. The paper doesn't fully address this alternative explanation.

**4. The mechanistic speculation section is hand-wavy.**

The paper offers three possible explanations for the 0.50 hedge: training data frequency, RLHF reward for moderate responses, or genuine uncertainty. It then says "I do not resolve this question here." This is honest but unsatisfying — the paper raises the most interesting question about *why* the model behaves this way and then declines to pursue it. For a paper that claims to be measuring something important about AI systems, leaving the mechanism entirely open feels like a significant gap.

---

## What I Still Don't Understand

1. **What does the synthetic allocation environment actually represent?** I understand it's a "role" with "three task allocations that sum to 100%." But what is the role? What are the tasks? Why does the objective value come out in dollars? The paper says the environment is a "measurement instrument rather than the object of study," but I needed more detail to assess whether the environment might be introducing artifacts.

2. **Why were these specific 10 words chosen?** The paper says they were chosen to "fill categorical gaps using terms natural to operational instructions." But why these 10 and not others? Why not "greatly," "enormously," "a bit," "a little"? The choice of words shapes every finding in the paper, and the rationale for this specific list is thin.

3. **What does the model actually output when it abstains?** The paper says the model "produces a text response acknowledging the request but declines to invoke the allocation tool, typically citing the constraint that allocations must sum to 100%." I wanted to see examples of these responses. The difference between "drastically" (acts) and "dramatically" (abstains) is one of the paper's most interesting findings, and the model's actual language in these cases would be the most direct evidence for the author's interpretation.

4. **What is a "fresh session" in this context?** The paper says each prompt cell is run "with a fresh session, deep-copied state, no memory between calls." I understand the intent (prevent runs from influencing each other), but I don't know whether this is technically meaningful given how these APIs work.

5. **Why 30 runs per cell?** The paper says this "balances statistical power for nonparametric tests with API cost constraints." But if the model at T=0.0 produces the same output 30/30 times for many words, the 30 runs are providing zero additional information for those cells. The sample size justification feels like it was written before the results were known.

6. **How do the results change with decrease instructions?** The paper studies only "increase" instructions. But the symmetry (or lack thereof) between increase and decrease behavior seems directly relevant to the practical implications. The paper lists this as future work but doesn't explain why it was excluded from the current study beyond implying it was a scope decision.

---

## On the Author's Specific Questions (from the brief)

The author asked me to pay attention to whether this paper can serve as the "cornerstone" of a larger field, and whether the field framing is legitimate or inflated. Here is my honest outsider assessment:

**On the cornerstone question:** The paper is a solid first empirical study with clearly documented limitations and honest statistical practice. It is *not* currently a cornerstone. A cornerstone needs to demonstrate that it measures something general, not just something specific to one model, one domain, and one researcher-constructed word scale. Right now, the paper measures Claude Haiku's behavior in a synthetic staffing allocation task using 10 words Daniel Tabach picked. That's a starting point, not a foundation. The cross-model comparison and human baseline survey aren't optional extensions — they are the minimum required before the core claims can be taken seriously as general findings about language models.

**On the field framing:** The "deployment-external safety science" framing in the author's brief is genuinely interesting and I can see why it's compelling. But the paper as written doesn't establish this field — it establishes that one model behaves inconsistently with one researcher's word-ordering intuitions in one synthetic domain. The gap between what the paper demonstrates and what the field framing claims is large. The author's own trap-warning in the brief ("I get intoxicated by the size of the vision and try to make one paper be the field") is apt. This paper is not the field. It's a data point that could, with extensions, become part of the field.

**The most honest verdict:** Option (c) from the author's own list — "pursue the program, mute the manifesto." The paper is real work. The findings are real. The safety-relevant observation about the drastically/dramatically discontinuity is genuinely interesting. But the paper cannot bear the weight of the field framing as currently written, and trying to make it do so risks making the actual findings look weaker by association with overclaiming.

**The single highest-leverage next step:** The human baseline survey. Not because it's the most exciting extension, but because without it, the paper's central interpretive claim — that the model's compression is a *failure* rather than an *accurate reflection of human ambiguity* — is unfalsified. Every other extension builds on this foundation. If humans also compress these 10 words into 5 clusters, the paper's framing needs to change substantially.