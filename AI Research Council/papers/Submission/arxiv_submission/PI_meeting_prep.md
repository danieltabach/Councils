# PI Meeting Prep: Vague Intensity Words in LLM Numeric Actions

## The Core Read

This is already a legitimate research object. The current paper is strongest as an alignment / agent-safety / behavioral-evals paper: it measures whether a natural-language control interface preserves operator intent when vague language becomes a concrete tool action.

It is not yet a mechanistic interpretability paper, because the main result is behavioral and the tested model is closed. But it has a very good mechanistic-interp bridge: the surprising behavior is specific, reproducible, and has clean minimal pairs. That makes it a good candidate for asking what internal representation or causal pathway controls the action.

The best stance for the PI meeting is not "Should this be alignment or mech interp?" It is:

> I have a measured behavioral failure mode in language-to-action control. I want help deciding whether to mature it as an alignment/evals workshop paper, or convert it into a mechanistic-interp project by reproducing it in open models and studying the internal causes.

## One-Sentence Pitch

I measured how an LLM translates vague intensity words like "slightly," "substantially," and "dramatically" into numeric tool actions, and found that the model compresses fine word distinctions, lets current system state dominate word meaning, and switches discontinuously between acting and abstaining near constraint boundaries.

## 90-Second Pitch

I built an autonomous scenario-planning harness on top of a constrained resource-allocation optimizer. The practical worry was that stakeholders might control a precise system through vague language like "slightly increase" or "dramatically increase." So I isolated the language-to-action step: the model receives a natural-language instruction, emits a numeric tool call, and a deterministic backend evaluates the result.

Across 6,620 runs on Claude Haiku, three things happened. First, without context, 10 intensity words collapsed into only a few numeric regimes: several words that sound distinct to users produced the same allocation. Second, when I gave the current allocation, the starting state explained much more of the output than the word itself, so the same word did not have a stable operational meaning. Third, near the constraint boundary, the model stopped behaving like a smooth scalar controller and split into modes: weak words made small adjustments, several strong words abstained, and "drastically" pushed toward the ceiling.

My current question is how to take this from a preprint into a stronger research contribution. One path is alignment/evals: cross-model comparison, human baseline, no-word control, decrease instructions, and a denser state grid. The other path is mechanistic interpretability: reproduce the phenomenon in open-weight models, then use probing and causal interventions to ask where intensity, baseline state, and act-vs-abstain behavior are represented.

## What You Actually Did

You did not "just test words." You built a controlled measurement instrument for a real agentic failure mode.

The basic experimental logic:

1. Choose a set of vague intensity words.
2. Ask the model to convert each word into a numeric allocation through a structured tool call.
3. Keep the backend deterministic so output differences come from the model's language-to-action mapping.
4. Repeat across no-context prompts, context-conditioned prompts, temperatures, and starting allocations.
5. Measure whether word meaning is ordinal, stable under context, and smooth near constraints.

The actual research question:

> When language models are used as control surfaces for systems that need precise actions, do vague human instructions preserve their intended operational meaning?

## Main Findings in Plain English

Compression:
The model understands broad intensity, but not all fine distinctions. "Slightly," "marginally," "somewhat," and "mildly" can collapse to the same action. That means the natural-language interface appears more expressive than it really is.

State dominance:
Once the model sees the current allocation, the current state often matters more than the word. At low baselines, the words fan out. Near capacity, they converge. So the user is not controlling a stable word-to-number mapping; they are controlling a joint function of word and state.

Boundary mode switching:
Near the 89 percent boundary, the model does not merely shrink every increase. It changes mode. Weak words hedge, several strong words refuse to act, and "drastically" often pushes toward the local ceiling. The "dramatically" versus "drastically" contrast is the cleanest hook.

Why this matters:
The failure is invisible from the language alone. Two instructions that feel close to a human can produce categorically different action policies in the same state.

## Math Refresher

Median:
The middle output value. You used medians because the model outputs are discrete and clumpy, not smooth bell curves.

IQR:
The interquartile range, or the spread of the middle 50 percent of outputs. This shows how much variation appears inside a prompt cell, especially at higher temperature.

Spearman rho:
A rank-correlation statistic. It asks: as the word tier increases, does the output usually increase too? A value near 1 means the ordering is mostly preserved. A value near 0 means the ordering has collapsed. You used this because the question is ordinal, not linear.

Kruskal-Wallis H test:
A nonparametric group-comparison test. It asks whether different groups produce meaningfully different rank distributions. You used it because the outputs are not normally distributed.

Epsilon squared:
An effect size for Kruskal-Wallis. In your paper, the important comparison is that grouping by baseline explains much more rank-based structure than grouping by word in the context-conditioned condition. The two values come from separate tests, so they should not be added together like pieces of a pie.

Abstention:
A non-error run with zero tool calls. In your setup, that is not a backend failure. It is a model action-policy decision.

Downstream delta:
The deterministic change in objective value after the model's chosen allocation. This shows that word interpretation can propagate into material system outcomes.

## Current Weaknesses to Own Directly

One model:
Right now the results could be Claude-specific, training-pipeline-specific, or a general feature of language.

No human baseline:
You cannot yet say the model is misaligned relative to humans. Humans may compress some of these words too. The human survey decides whether this is model failure or faithful modeling of fuzzy human language.

No no-word control:
You need "increase innovation" without an intensity word to test whether 0.50 is a hedge caused by vague modifiers or just the default response to any increase request.

Researcher-defined word scale:
The ordering is plausible, but not validated. This is fine for exploratory work, but a stronger paper needs either human validation or a more systematic linguistic scale.

Closed model:
The current paper cannot directly support mechanistic claims because you do not have model internals.

Repeated runs:
Thirty runs per cell are useful, but runs inside the same prompt cell are not independent in the strongest statistical sense. You already handled this honestly by treating p-values as descriptive.

## Direction A: Strong Alignment / Agent-Safety Paper

This is the most direct route to a good workshop paper.

Minimum next experiments:

1. Add no-word control.
2. Add decrease instructions.
3. Run cross-model comparison across at least 3 model families.
4. Add a denser baseline grid near transition points, especially 75 to 95 percent.
5. Add a human baseline survey if feasible.

Stronger claim after these:

> Vague language in LLM-controlled tool interfaces produces systematic, model-dependent action policies that are compressed, state-sensitive, and discontinuous near constraints.

This fits agentic safety, failure-mode evaluation, calibration, human-AI interaction, and alignment workshops.

## Direction B: Mechanistic Interpretability Version

This is the right way to engage the PI if they are mech-interp oriented.

Core shift:

Move from "what does the model do?" to "what internal variables cause it to do that?"

Necessary first step:

Reproduce the behavioral phenomenon in open-weight models where activations are accessible, such as Llama, Qwen, or Mistral-class instruction models.

Possible mech-interp experiments:

1. Representation probing:
Train simple probes on residual stream activations to predict intended action magnitude, word tier, baseline value, or act-vs-abstain mode. Check where these signals appear.

2. Activation patching:
Hold the prompt fixed but patch activations from "slightly" into "dramatically" or from low-baseline prompts into high-baseline prompts. If the output changes, you have causal evidence about where the decision is represented.

3. Minimal-pair analysis:
Use "dramatically" versus "drastically" at 89 percent as the flagship pair. They are semantically close but behaviorally different. Ask whether the model internally routes one toward refusal / infeasibility and the other toward maximum feasible action.

4. Constraint-boundary features:
Look for features or directions associated with "cannot," "constraint," "sum to 100," "safe adjustment," or "maximum possible." If a sparse autoencoder setup is available, this could become especially interesting.

5. Word-state interaction:
Test whether baseline state and lexical intensity are represented independently, then combined, or whether one overwrites the other near the boundary.

Mechanistic version of the claim:

> The model's action policy is governed by separable internal representations of lexical intensity, available headroom, and feasibility/refusal mode; near constraints, the feasibility representation causally overrides lexical intensity except for maximizer-like words.

Important caveat:
Do not call the current paper mechanistic. Call it a behavioral finding that gives you clean targets for mechanistic study.

## Direction C: Human Alignment / HCI Version

This path asks how humans expect vague words to map to numeric actions and whether models preserve those expectations.

Best next step:

Run a human survey using the same prompts and baselines. Ask participants what allocation they expect, how confident they are, and whether the model's action would satisfy their intent.

Potential stronger claim:

> The safety problem is not vagueness itself; it is mismatch between user expectation and model operationalization.

This is valuable, but it is probably less tailored to a mechanistic-interp PI unless paired with model internals.

## Recommended Ask for the PI

Do not ask only, "What should I do with this paper?" That is too open.

Ask this:

> I see two plausible paths. The first is an alignment/evals paper where I strengthen the behavioral evidence with cross-models, human baselines, no-word controls, and decrease instructions. The second is a mechanistic-interp project where I reproduce the phenomenon in open models and study the internal cause of the compression and act/abstain switch. Given your taste, which path has the highest chance of becoming a real workshop paper by the end of AlgoVerse?

Then ask:

> If we pursued the mechanistic path, what would you consider the minimum credible mechanistic experiment? Would a clean activation-patching result on the dramatically/drastically boundary be enough to make this interesting?

## Good Questions to Bring

1. Is the current behavioral result interesting enough to mature as an alignment/evals workshop paper?
2. What experiment would make the work feel genuinely mechanistic rather than just behavioral plus probes?
3. Should I pivot from Claude to open-weight models first, even if the behavior changes?
4. Is the "dramatically" versus "drastically" boundary result the right flagship phenomenon?
5. Would you prioritize cross-model comparison, human baseline, or activation-level analysis first?
6. What would make this look novel to a workshop reviewer instead of like prompt sensitivity?
7. Is there a known mech-interp literature on numeric magnitude, scalar representations, refusal, or constraint handling that I should read first?
8. What is the smallest publishable unit for an 8 to 10 week program?

## How to Position Yourself

Say this plainly:

> I am a data scientist trying to pivot into AI research. I built the underlying optimization system in a real production context, then built the LLM harness myself because I wanted to understand agentic workflows. The paper came from noticing a safety failure in a system I had actually built, not from searching for a trendy topic.

That is a strength. You are bringing systems taste and a real-world failure mode. You do not need to apologize for not being a PhD student.

## Venue Notes As Of June 4, 2026

ICML 2026 has a Mechanistic Interpretability Workshop, but its call for papers is already closed and acceptance notifications are listed for June 12. It is useful as a signal of what the community currently values, not as a live target for this version.

ICML 2026 also has workshops that are conceptually close to this work, including Failure Modes in Agentic AI and Statistical Frameworks for Uncertainty in Agentic Systems. Their 2026 submission windows appear to be closed or limited, but they are good examples of venue fit.

NeurIPS 2026 workshop proposals are not finalized yet. The NeurIPS workshop call lists workshop acceptance notification on July 11, 2026, with a suggested submission date for workshop contributions of August 29, 2026 and mandatory accept/reject notifications on September 29, 2026. That makes NeurIPS workshops the likely near-term target once accepted workshops are announced.

Practical target:

1. Use the PI meeting to pick the research direction.
2. Spend the early AlgoVerse period producing one stronger experimental slice.
3. Aim for a NeurIPS 2026 workshop if a relevant workshop appears in July.
4. Otherwise aim for ICLR / ICML 2027 workshops or a longer-form arXiv revision.

## My Recommendation

Your best near-term path is a hybrid:

1. Keep the main framing as alignment / agent safety: vague natural-language control fails to preserve operator intent in stable ways.
2. Ask the PI to help define a mechanistic version using open-weight models.
3. Make the "dramatically" versus "drastically" boundary switch the flagship phenomenon.
4. Add the cheap behavioral patches immediately: no-word control, decrease direction, and denser near-boundary grid.
5. If open-model reproduction works, pursue activation patching or representation analysis. If it does not, the failure to reproduce is itself useful and the paper becomes a cross-model behavioral comparison.

The crossroads is real, but it is not a dead end. The behavioral alignment paper is the trunk. Mechanistic interpretability is the highest-upside branch.

