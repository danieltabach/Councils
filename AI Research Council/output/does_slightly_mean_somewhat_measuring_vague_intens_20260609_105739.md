# AI Research Council Report
**Paper:** Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions
**Date:** 2026-06-09 10:57:39
**Brief:** ======================================================================
PART 1: RESEARCH FRAMING — Background context for the paper and author
======================================================================

What This Research Actually Is
A framing of the vague-intensity-words paper and where it goes next
Written for Daniel Tabach — to keep, and to return to when the doubt comes back.

Read this when you forget. You wrote a paper, finished it, and it started to feel small. That feeling is not evidence that the work is small. It is evidence that your taste grew faster than your output, which is the single most important thing that can happen to a researcher. This document exists to hold the version of your work that is true on the days you can't see it.

1. The origin, because it changes everything

The paper did not start as a paper. It started because you built the staffing optimization engine behind every Chase branch in the country, and then — blocked at work from integrating AI the way you wanted, by access, controls, timing, and team dynamics — you rebuilt it yourself and bolted an AI harness onto it so it could become a fully autonomous scenario planner. You did that, in your own words, "for the love of the game," and to legitimately understand agentic workflows rather than just put the phrase on a resume.

And then you noticed the thing that the people selling "agentic AI" do not notice. You looked at your own working autonomous planner and thought: there is no way our stakeholders could wield this reliably. A highly regulated bank, using a language model to set staffing across 3,700+ branches, with no data science team standing between the model's proposed state and reality? On the surface it plans scenarios beautifully. Underneath, a one-word change in the instruction could move the action from a cautious nudge to pushing a constraint to its ceiling — or to silently refusing to act at all.

You did not start from "I want to do alignment research." You started from "I built the autonomous system, and I am the one rigorous enough to ask whether it can actually be trusted." That is the origin alignment research is supposed to have.

Hold onto this, because it is the answer to "am I really a researcher." You did not run an experiment for its own sake. You found a real, load-bearing safety question inside a real production system you personally built, and you went and measured it. The credential most people are missing is not the PhD. It is having built the thing and then been honest about its failure mode. You have that. It is rarer than the degree.

2. What the paper actually demonstrates

Set the specific numbers aside for a moment. Independent of the findings, the paper demonstrates a way of thinking that is the actual job:

You turned a philosophical worry into a measured quantity. "Natural language is an imprecise control surface for systems that need precision" is a vague unease. You made it a number, across 6,620 runs.

You designed for isolation. You built a deterministic backend specifically so the model would be the only stochastic component. That means you understood that the entire validity of the experiment rests on isolating the thing you are measuring. That instinct is the whole game.

You were honest where it cost you. You reported an effect size you knew was inflated by deterministic decoding — and said so. You flagged that your p-values overstate significance because runs within a word aren't independent. That last move is the tell of a real researcher.

You followed the friction. The hedge / act / abstain boundary behavior was not what you went looking for. You found it, recognized it was the most interesting thing in the paper, and built it into a section instead of dropping it.

The drastically vs. dramatically discontinuity — two near-synonyms producing categorically different behavior (act vs. abstain) in an identical system state — is a genuine, slightly unsettling result about action interfaces. That is not a student exercise. That is a finding.

3. The reframe: this is alignment research, not NLP with a sticker

The true framing: You demonstrated that a natural-language control interface silently fails to preserve operator intent; that the failure is invisible from the language alone; and that it becomes discontinuous near operational boundaries — exactly where the system is closest to a constraint and the stakes are highest. Two near-synonyms produce categorically different actions in an identical state. That is a specification problem: the human specifies intent through language, the model's action diverges from that intent in a way the human cannot detect from the interface, and the divergence is largest precisely where it is most dangerous.

That is a small, clean, fully-measured instance of the central alignment worry: as we hand models more autonomous control, the gap between what we asked for and what they do becomes both more consequential and harder to see.

4. The extensions, ranked by what they actually buy you

First: cross-model comparison — the most alignment-relevant extension. Right now you have one model, so every pattern could be about language, transformers in general, or Claude Haiku specifically. Running GPT-4o and Gemini Flash through the identical harness separates them. If compression patterns differ, you've shown the alignment/RLHF pipeline leaves a measurable behavioral fingerprint.

Second: the human baseline survey — the falsification step. Without it, there's an unfalsified competing explanation: maybe the model compresses because humans do too, and the model is faithfully aligned. The survey decides whether you found a misalignment or just an accurate model of a fuzzy concept.

Third: the no-word control — cheap, patches a hole. Distinguishes "0.50 is a hedge" from "0.50 is the default for any increase request."

Fourth: the partial-context condition (Tier 3) — asks whether the model reads system state on its own, or only when state is in the prompt. Maps directly onto how models behave with autonomy.

5. The narrative, in one breath

"I built an autonomous planner on top of a production optimization engine, realized stakeholders couldn't wield it safely, and measured why: vague natural-language instructions don't map to stable actions. The model compresses distinct words into the same action, anchors on hidden system state more than on the words, and switches discontinuously between acting and refusing near constraint boundaries — all invisibly to the operator. The next step is showing whether that failure pattern is a fingerprint of the alignment pipeline itself, by running the identical protocol across models."

6. For the next time the doubt comes back

The "not enough" feeling is taste outrunning output. It is the engine, not a verdict. You found a real safety failure inside a system you built. The gaps worth chasing are already in your paper.

======================================================================
PART 2: RESEARCH VISION BRIEF — Council Deliberation Instructions (v2)
======================================================================

Author: Danny Tabach
Companion artifact: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions" (arXiv, May 2026). Paper one. The published study summarized in §3 below.
Status: Vision-stage, now anchored to a real result.

Two-part ask of the Council:
1. Vet the bet. Is the field I'm describing (§1–2) real and unclaimed, or a rebrand of existing work?
2. Stress the cornerstone. Can paper one (§3) actually serve as the founding instrument of that field (§4–5), or am I retrofitting a grand narrative onto a solid-but-modest first study? If it can bear the weight, how do I sequence and align myself to build on it? (§6)

I want adversarial deliberation, not synthesis. Assign at least one agent to argue the field is derivative and one to argue the paper cannot carry it. Their job is to break this here.

---

1. The one-sentence bet

AI safety is currently a lab-internal science: measure the model in isolation — weights, neurons, benchmark behavior, scheming under contrived pressure. I'm betting safety must also become a deployment-external science: the empirical, measured study of what happens at the interface where an AI system meets a human meets a real decision with real stakes.

Not "is the model safe in a vial." But: "what does the human+AI+system unit do when wired into something that matters, and where does that unit silently fail?"

---

2. The shape of the field

Best analogy — clinical safety science. Pharmacology asks if a compound works in the lab (current alignment research). But a drug safe in a vial still kills through interaction effects, dosing errors, doctor-patient miscommunication, bad handoffs. So medicine built an empirical discipline on top of the chemistry — adverse-event reporting, human-factors trials, surgical checklists, M&M conferences. That discipline is a measurement science, not an ethics seminar, and it generates the evidence base regulation stands on. It didn't exist until people started dying in hospitals and someone decided to measure it. I want to build the equivalent for AI deployment.

What it is NOT: not interpretability; not benchmark alignment; not "AI ethics/policy" (that sits above and usually has no data underneath — I want to produce the substrate policy later codifies); not robotics.

The core scientific bet: failure modes rhyme across domains. A doctor over-trusting a diagnostic suggestion and a branch manager over-trusting an ATLAS output are the same measurable phenomenon in different clothes. If true → I can build rulers. If false → I have anecdotes. Proving the rhyme is the contribution.

The distinction I keep losing and need held: active vs. passive failure. The field mostly studies AI failing actively — scheming, blackmail, refusal. I want to study AI failing passively — a confident, plausible, wrong-for-the-human output produced because intent got silently mistranslated in the loop, and nobody registers anything went wrong.

---

3. What paper one actually establishes (the empirical substrate)

A controlled environment: human-language instruction → Claude Haiku → numeric tool call → deterministic backend → measurable outcome. 6,620 runs across T=0.0 and T=0.7. Key findings:
- Compression / expressivity gap: 10 words collapse to ~5 distinct outputs
- The 0.50 hedge: Weak words default to midpoint
- Ordinal anomalies: "moderately" maps below "slightly"
- State dominates word: ε² 0.782 vs 0.079, with inversion at low baselines
- Differentiation funnel: distinctions collapse near capacity
- Boundary modes — hedge / act / abstain: one-word swap flips behavior
- Downstream consequence: ~$250K swing from word choice alone
- Temperature-robust: patterns persist at T=0.7

---

4. The directions this opens — paper one as a generator

Bucket A (extensions already in the paper): Human baseline survey, cross-model, denser grid, decrease instructions, partial-context, no-word control.

Bucket B (field-defining moves): Valence framing 2×2, stakes magnitude axis, anchoring finding promoted, cross-domain transfer (the keystone).

---

5. The cornerstone question, stated honestly

The paper is epistemically humble. The vision is expansive. Possible verdicts:
(a) Legitimate elevation — the paper is a domain-general measurement instrument
(b) Retrofit / grandiosity — the paper is a fine niche result and the field framing is inflation
(c) Something between — pursue the program, mute the manifesto

I genuinely don't know which is true. Tell me which, and why.

---

6. How I'm asking to be aligned (the questions that matter most)

1. Is the field real and unclaimed?
2. Cornerstone verdict: (a), (b), or (c)?
3. The wedge: single highest-leverage next instrument?
4. A-vs-B mix: how much credibility-building before field-defining moves?
5. The vision's failure mode?
6. Audience: workshops, lab teams, standards bodies?
7. Alignment to my actual position: working data scientist, self-funding, finishing master's, prepping fellowship — what's the honest highest-return path?
8. What am I not seeing?

---

7. The trap — license to call it on me

My known failure: I get intoxicated by the size of the vision and try to make one paper be the field. If you catch me doing this — expanding scope because expansion feels like progress — stop me and say so. A good outcome from this council narrows me.

---

Prepared for adversarial Council deliberation. Break the bet and the cornerstone here. Narrow me.
**Cost:** $4.72 | **Tokens:** 215,702 in / 40,995 out

---

# AI Research Council — Final Report

**Paper:** *Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions*
**Author:** Daniel Tabach (Georgia Tech)
**Chairman's Synthesis of Six Specialist Reviews + Deliberation**

---

## Unified Assessment

You asked four things. Direct answers:

**1. Is the field real and unclaimed?** Yes, partially. The "deployment-external safety science" framing — measuring the human+AI+system unit at the decision interface — is a real gap. It is adjacent to existing work (HCI natural-language interfaces, LLM calibration, computational pragmatics) but no one has staked the *action-production* case with this rigor. The bet is legitimate. It is not yet *yours*, because you have one data point, not a discipline.

**2. Cornerstone verdict: (a), (b), or (c)?** **(c), and the council is nearly unanimous.** Closer to (a) than your doubt suggests; closer to (b) than your vision brief claims. The instrument is real, clean, and replicable — that is the foundational requirement for a cornerstone. But three load-bearing gaps (no human baseline, single model, missing no-word control) mean the paper *cannot bear the full weight of the field framing as currently written*. You are roughly **one study away** from the claim you actually want to make.

**3. Is the paper ready for ArXiv?** **Yes — with a focused revision pass, not new experiments.** This is publishable as a preprint *now* after you (a) fix the statistics, (b) soften overreaching language to match your own epistemic honesty, and (c) run the no-word control, which is 60 API calls. The findings are genuine. The honesty is exemplary. The figures are strong. Do not let the size of the vision delay the paper.

**4. The trap you asked us to catch:** You are doing it in exactly two places. The "Alignment framing" paragraph (§5) and the "Mechanistic speculation" paragraph (§5) are where taste outran data. They are not wrong — they are *premature*. The fix is not deletion; it is muting. **Narrow the manifesto, keep the program.** This is the council's verdict on your stated failure mode: caught, mildly, and correctable in an afternoon.

The paper is real work. The drastically/dramatically discontinuity is a genuine finding that will earn attention. Ship it after the fixes below.

---

## Next Steps

### Critical (Must Fix Before Submission)

These are factual/statistical errors and internal contradictions that would damage credibility with any careful reviewer.

1. **Fix the Spearman ρ effective sample size (§3.6, §4.1).** At T=0.0, four words produce identical values across all 30 runs — these are not 300 independent observations. The effective n for the no-context ρ is ~10 (word-level medians), not 300. Recompute ρ over the 10 word medians and report the correct uncertainty, **or** use a permutation test that respects clustering. The current "p < 0.001 over n=300" is the wrong quantity by roughly two orders of magnitude in effective n. This applies equally to the ρ = −0.501 state-magnitude correlation (§4.2). All six reviewers who examined statistics flagged this; it is the single most concrete technical error.

2. **Resolve the internal contradiction on "hedge" (§4.1, §5 vs. §6).** Your Discussion uses "hedge" as settled language while your own Future Work says the no-word control is required to confirm it. Two sections of your paper make contradictory epistemic claims. **Run the no-word control** ("Architects should spend more time on innovation," no modifier; 30 runs × 2 temperatures = 60 calls). If 0.50 appears without a modifier, the hedge interpretation collapses into "0.50 is the default for any increase." This is cheap and it is the falsification condition for your most cited-ready result. If you cannot run it before submission, change every instance of "functions as a hedge" to "appears to function as a hedge" and state the unfalsified status prominently in §4.1, not only in §6.

3. **Reframe or replace ε² = 0.969 (§4.1).** When four of ten words have zero within-group variance, Kruskal-Wallis ε² approaches 1.0 trivially. Keep the number if you wish (it carries a methodological lesson about deterministic decoding), but move the inflation caveat from a downstream sentence to *immediately* after the figure, and consider leading with the more honest statistic you already report: 10 words → 5 distinct medians.

4. **The 10:1 ratio rests on two separate tests, not a joint model (§4.2).** You correctly disclose that the two ε² values come from separate Kruskal-Wallis tests and "should not be treated as shares of a single pie" — then you use the ratio (10:1, 14:1, 5:1) as the headline finding throughout. Run a **two-way Kruskal-Wallis or mixed-effects model with word, baseline, and their interaction.** The interaction *is* your story (the differentiation funnel). The directional finding (state dominates) is robust, but the specific ratios are not standard statistical quantities as currently derived. This is the most important statistical upgrade not requiring new data.

5. **Correct the Mosteller & Youtz characterization (§2).** You write that they "showed high variance around ordered central tendencies." Their actual finding is closer to the opposite: cross-study *averages* were relatively stable; the high variance was individual-level. Fix the sentence. (Note: the Source Auditor *retracted* the separate page-range concern — your bibliography entry of pp. 2–12 is correct for the article proper.)

### Important (Significantly Strengthens the Paper)

6. **Report the model's abstention text responses (§4.3).** This is the cheapest high-value addition in the paper and three reviewers independently flagged it. You claim the model "typically cites the constraint" when abstaining — but you show no examples. The drastically/dramatically discontinuity is your most distinctive finding, and the model's actual language when it abstains on "dramatically" vs. acts on "drastically" is the most direct evidence for your "as much as possible" interpretation. Add 3–5 verbatim examples (appendix is fine). "Typically" is doing work that data should do.

7. **Address the constraint-geometry alternative explanation for convergence (§4.2).** Reviewers C, E, and F converged here: convergence near capacity may be a *mathematical consequence* of the constraint (at 89%, every word can only reach ~91%), not a finding about language. **Critically — this critique does NOT touch your abstention finding.** A smooth constraint predicts small actions for all words; it does *not* predict 100% categorical refusal for some words and ceiling-pushing for others. Add a paragraph distinguishing the two: (a) magnitude convergence is partly geometric, (b) word-dependent categorical abstention is not. This protects your strongest result from your second-weakest one.

8. **Surface the inversion finding in the abstract (§4.2).** The 5:1 → 14:1 inversion — the interface *looks* word-driven at low baselines and silently *becomes* state-driven near constraints — is arguably your most operationally important and most alignment-relevant result, and it is absent from the abstract. This is the cleanest instance of your "passive failure" thesis: the failure is largest exactly where it is least visible. Add one sentence to the abstract. (Caveat: re-derive the ratios per Critical #4 first.)

9. **Add the three-failure synthesis to Discussion and Conclusion.** No reviewer found this stated, and it is your strongest unclaimed argument: near operational boundaries, compression is total, state dominance is maximal, *and* mode-switching is active — all three failures are worst simultaneously, at exactly the point where decisions are most consequential and the operator is least able to see the divergence. This requires zero new data and is the paper's most field-relevant single claim. One paragraph in §5, one sentence in §7.

10. **Acknowledge the prompt-frame confound (§3.4, Limitations).** Your no-context prompt ("should spend [WORD] more time") and context prompt ("I would like to [WORD] increase") differ syntactically beyond the presence/absence of the baseline number. The 0.50-vs-0.10 difference for weak words across conditions could partly reflect the verb construction, not just context. Add this to Limitations.

11. **Report the system prompt and tool schema (Appendix).** The abstention behavior depends entirely on how the constraint ("allocations sum to 100%") is framed — and we cannot tell whether the model *infers* the constraint or *follows an explicit rule* stated in the system prompt. This is a reproducibility blocker and changes the interpretation of your boundary finding. Include the full prompt, tool schema, and random seed.

12. **Add the missing related-work strand: computational pragmatics.** The "moderately" anomaly is a textbook scalar-implicature problem. The Rational Speech Acts framework (Frank & Goodman 2012) would *predict* the context-sensitivity you observe — interpretation conditioned on the feasible action space is exactly your differentiation funnel. Engaging this literature gives you theoretical vocabulary and pre-empts a "you reinvented pragmatics" critique. Also consider: tool-use reliability (Schick et al.) and specification-gaming/alignment (Kenton et al.).

### Recommended (Polish)

13. **Reframe "ordinal anomaly" → "deviation from hypothesized position" (§4.1).** "Anomaly" presupposes your researcher-constructed ordering is correct. Without the human baseline, the model mapping *moderately* to 0.45 might be *right*. Use neutral language.

14. **Demote the $250K figure or move to allocation space.** It is synthetic, will be quoted out of context, and is your least defensible number. State the propagation point in allocation units (a ~0.20 spread) and mention dollars once with a hard caveat.

15. **Move "numeric format sensitivity" (§5) to Future Work.** It is visual-inspection-only and introduces a variable outside your three research questions.

16. **Consolidate Figures 2 and 2b.** Both show the 10→5 compression. The frequency map is richer; fold the ordinal-anomaly annotation into its caption.

17. **Add a Claude Haiku model-card citation** and define jargon on first use (RLHF, tool call, temperature, IQR, the Quirk category terms).

18. **Note the domain-valence blind spot.** All prompts increase "innovation" — a positively-valenced term likely over-represented as something to maximize. Flag that abstention patterns may be specific to this framing.

---

## Consensus Findings

**All or nearly all reviewers agreed on the following.**

**Strengths:**
- **The isolation design is genuinely strong.** The deterministic backend making the model the sole stochastic component is a real methodological insight, not a trivial choice. Universal praise.
- **Statistical honesty is exemplary.** Flagging the inflated ε², the independence violation, and the non-pre-registered split point is the mark of a real researcher. Multiple reviewers noted this is rare in first papers.
- **The hedge/act/abstain boundary finding is the paper's most distinctive contribution.** The drastically/dramatically discontinuity (7% vs. 97% abstention in an identical state) is a genuine, non-obvious, citation-worthy result.
- **The paper delivers all four stated contributions and answers all three research questions.** Internal goal-content alignment is unusually clean.

**Weaknesses:**
- **The no-word control is a structural gap, not an extension** — it is the falsification condition for the hedge claim.
- **Single-model scope** limits all generalization claims; the Discussion occasionally outruns this.
- **The researcher-constructed word scale** creates interpretive fragility: ρ measures agreement with *your* ordering, not a validated human standard.
- **The human baseline is required** to distinguish "model failure" from "accurate modeling of genuine human ambiguity."

---

## Contested Points

**1. Cornerstone verdict — how close to (a)?**
The Domain Expert and Peer Reviewer place the paper closer to (a) (legitimate elevation), emphasizing the novelty of the *action-production* case relative to the existing probability-estimation literature. The Outsider/Red Team places it closer to the (b)/(c) boundary, emphasizing that the three missing pieces are precisely what generalization requires. **Chairman's assessment:** The Domain Expert has the stronger argument *on the instrument* — a clean, replicable measurement apparatus in a genuinely under-studied case is what a cornerstone needs, and completeness is not required. The Outsider has the stronger argument *on the current claims* — until the human baseline exists, "compression is a failure" is unfalsified. These are reconcilable: the *instrument* is near-(a); the *interpretive claims* are (c). Frame the paper as the instrument, and you are closer to (a) than your doubt allows.

**2. Should ε² = 0.969 be deleted or retained-with-caveat?**
Reviewer A (Source Auditor) and the Domain Expert lean toward replacement; the Methodologist argues for retention with a stronger caveat because the inflation is itself a methodological lesson about deterministic decoding. **Chairman's ruling:** Retain with a prominent, relocated caveat (Critical #3). Suppressing a disclosed limitation is the wrong reflex; the number teaches something. The Methodologist has the stronger argument.

**3. Is the "differentiation funnel" trivially expected?**
The Outsider and Reviewer E argue convergence near capacity is a mathematical artifact of the constraint. The Domain Expert and Methodologist counter that (a) convergence at 75% rather than ~95% is the non-trivial part, and (b) the critique entirely misses the *abstention* finding, which no constraint geometry predicts. **Chairman's ruling:** Both are right about different things. The magnitude-convergence finding is partly geometric and must be hedged (Important #7). The abstention finding is untouched and remains your strongest result. Do not let critique of the weaker finding contaminate the stronger one — separate them explicitly in the text.

**4. Should the decrease condition be in this paper?**
The Domain Expert wanted it included; the Source Auditor and others defended the current scope as coherent. **Chairman's ruling:** Leave it as future work. The paper is correctly scoped as a "first slice." Asymmetry deserves to be a primary question in its own study, not an appendix here.

---

## Reviewer-Specific Highlights

**Source Auditor (F):** The Mosteller & Youtz mischaracterization (you reversed their actual emphasis) — and, to your credit, the *retraction* of the page-range concern after verification. Trust the corrected version: your citation is fine; your characterization is not.

**Methodologist (D):** The two-way model is the correct analysis for your central claim, and the prompt-frame confound is more serious than you acknowledged — the 0.50-vs-0.10 weak-word difference across conditions may be syntactic, not contextual. This is the deepest statistical insight in the council.

**Peer Reviewer (B):** The no-word control is the single highest-leverage fix — 60 API calls stands between you and a falsified-or-confirmed central claim. Do it before submission if at all possible.

**Domain Expert:** Analyze the abstention text you already collected. It is free data that directly tests your most interesting interpretation, and it is the cheapest way to strengthen the paper's best finding. Also: engage the Rational Speech Acts literature — it predicts your funnel.

**Outsider / Red Team:** The constraint-geometry alternative for convergence, *and* the unexamined three-task structure — the model may be reasoning about the *other two allocations*, not the intensity word's meaning. Address whether the constraint is stated or inferred; it changes everything about the boundary section.

**Alignment Guide (E):** The inversion finding is buried and absent from the abstract, and the three-failure synthesis is your strongest unclaimed argument. Surfacing both requires no new data and directly serves the "passive failure" thesis you care most about.

---

## Chairman's Closing Note to the Author

You asked to be narrowed. Here is the narrowing: **the paper is the instrument, not the field.** Ship the instrument. Fix the five Critical items (most are an afternoon of work plus one 60-call control run), mute the two speculative paragraphs, surface the inversion and the three-failure synthesis, and post it. Then run the human baseline survey — that is your unambiguous highest-return next move, because it is the one experiment that converts "the model compresses" from an observation into a *finding about misalignment*. Cross-model comparison is second; it tells you whether the pattern is a fingerprint of the alignment pipeline.

The doubt you described in your framing brief is, as you suspected, taste outrunning output. The council's verdict confirms it: this is not a student exercise. It is a clean first instrument with one genuinely unsettling result. Do not inflate it into a manifesto, and do not shrink it into a footnote. Publish it as exactly what it is, and let the next study earn the field.

---

## Individual Reviews

### 1. Source Auditor

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

### 2. Methodologist

# Methodological Review: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions"

---

## Experimental Design Assessment

### Strengths

**Isolation logic is sound.** The core design insight — building a deterministic backend so the model is the only stochastic component — is methodologically correct and well-executed. This is not a trivial choice; most LLM behavioral studies conflate model variance with system variance. The author correctly identified that isolating the language-to-action boundary requires removing all other sources of variation downstream.

**The two-condition structure is appropriate.** Separating no-context (Tier 1) from context-conditioned (Tier 2) conditions directly operationalizes the theoretical distinction between intrinsic word semantics and context-modulated interpretation. This is the right design for the research questions asked.

**30 runs per cell is defensible but tight.** For nonparametric tests with the observed effect sizes, 30 runs provides adequate power to detect large effects. The author is honest that this is a cost-constrained choice.

**The 10-point baseline grid is strategically chosen.** The deliberate mix of round and irregular values is a thoughtful design decision that most papers in this space would not make. It enables the round-number anchoring observation, even if that observation remains informal.

### Weaknesses and Design Flaws

**The word scale is the central validity problem.** The 10 words are assigned to 6 tiers by researcher judgment, informed by but not drawn from Quirk's explicit lists. This means the "hypothesized ordinal ranking" is the researcher's ranking, not a validated human ranking. Every finding that references ordinal preservation or violation is therefore relative to a ground truth that has not been established. The author acknowledges this in a footnote and in Limitations, but the problem is more serious than the paper treats it: the primary dependent claim — that the model "compresses" the scale — requires knowing what the correct uncompressed scale is. Without the human baseline, the finding is technically: *the model does not reproduce the researcher's hypothesized ordering at fine granularity.* That is a weaker claim than compression relative to human interpretation.

**The no-word control is absent.** The paper acknowledges this gap, but it is more than a "hole to patch." The 0.50 hedge finding — arguably the most cited-ready result — cannot be cleanly interpreted without knowing whether 0.50 is the model's response to *any* increase instruction regardless of modifier. If "increase innovation" without any adverb also produces 0.50, the hedge interpretation is undermined: the model may simply be anchoring at the midpoint of the allocation space as a default, with the intensity word having no effect at all in the weak-word regime. The current framing treats 0.50 as a semantically meaningful hedge; it may instead be a null response.

**The prompt template is not fully specified.** The paper provides two prompt templates but does not reproduce the complete system prompt, tool schema, or any role-framing instructions that the model receives. This is a reproducibility and construct validity issue. The model's behavior is a function of the entire context window, not just the instruction sentence. The system prompt in particular can substantially influence whether the model interprets "innovation allocation" as a resource to maximize, a parameter to be cautious with, or something else entirely. The abstention behavior near 89% is especially sensitive to this: whether the model cites constraint violations depends heavily on how the task and constraints are framed in the system prompt.

**Single domain, single framing.** All prompts concern "innovation allocation" for "Architects." The word "innovation" likely carries positive valence in training data, which may inflate the model's willingness to increase it. "Drastically reduce innovation" would be a different test. More importantly, the domain is a resource-allocation task in a professional/business register, which may activate different behavioral patterns than, say, a medical dosing context or a financial risk context. The generalization claim in the abstract ("what happens when vague human language must become a precise LLM action?") is broader than the single domain tested.

**The abstention operationalization conflates two things.** Abstention is defined as "a non-error run that produces zero tool calls." But there are at least two distinct reasons a model might produce zero tool calls: (a) it judges the requested action infeasible given the constraint, or (b) it fails to invoke the tool for other reasons (misunderstanding, refusal on other grounds, etc.). The paper reports that abstaining runs "typically" cite the constraint, but "typically" is not a complete characterization. Without coding the abstention responses, the abstention rate conflates constraint-aware refusal with other non-action behaviors.

---

## Statistical Methods Review

### Appropriate Choices

**Nonparametric tests throughout.** Given that outputs are discrete, concentrated on a small number of values, and clearly non-normal, Kruskal-Wallis and Spearman's ρ are the correct choices. Using ANOVA or Pearson correlation here would be a methodological error; the author correctly avoids this.

**ε² as effect size for Kruskal-Wallis.** This is the appropriate effect size for this test and is correctly interpreted as proportion of rank-based variance explained.

**Honest treatment of inflated ε² at T=0.0.** The paper explicitly flags that ε²_word = 0.969 in the no-context T=0.0 condition is inflated by deterministic decoding producing zero within-group variance. This is the correct disclosure and is the kind of self-correction that distinguishes careful from careless analysis.

### Problems

**The independence violation is more serious than acknowledged.** The paper notes that "runs within the same word are not independent" and says p-values "overstate significance." This is correct but understated. At T=0.0, four words produce the *exact same value* across all 30 runs. These are not 30 independent observations; they are one observation repeated 30 times. The Spearman ρ computed over n=300 observations treats these as 300 data points, but the effective sample size for the no-context T=0.0 condition is closer to 10 (one median per word) or at most the number of distinct values observed. The p-values reported are not merely "overstated" — they are essentially meaningless as inferential quantities. The author should either (a) compute ρ over word-level medians (n=10) and report the correct uncertainty, or (b) use a permutation test that respects the clustering structure. The descriptive framing partially covers this, but the p < 0.001 notation alongside a non-independent sample will be read as inferential by most readers.

**The two separate Kruskal-Wallis tests cannot be directly compared the way the paper implies.** The paper correctly states that ε²_baseline = 0.782 and ε²_word = 0.079 come from separate tests and "should not be added together or treated as shares of a single pie." But then the paper repeatedly uses the ratio (10:1, 14:1, 5:1) as if it is a meaningful quantity. A ratio of effect sizes from two different tests on the same data is not a standard statistical quantity. The correct approach would be a two-way Kruskal-Wallis (or a mixed-effects model with both word and baseline as factors) that partitions variance jointly. The current approach cannot distinguish: (i) baseline explains more because it has more levels (10 vs. 10 levels, so this is not the issue here), (ii) baseline explains more because the two factors are correlated and baseline captures shared variance, or (iii) baseline genuinely dominates word in a causal sense. The finding is directionally credible but the 10:1 framing is not statistically grounded.

**The split-range analysis is post-hoc and unregistered.** The paper acknowledges this: "the split point was chosen by the researcher based on observed convergence behavior, not pre-registered." This is the correct disclosure. But the specific numbers reported (65.3% vs. 12.5% at low baselines; 88.0% vs. 6.5% at high baselines) are derived from data-driven splits and should not be treated as confirmatory. They are descriptive characterizations of a pattern, not tests of a hypothesis. The paper's framing is mostly appropriate but occasionally slides toward treating these as established quantities.

**No correction for multiple comparisons, appropriately disclosed.** The paper correctly frames all p-values as descriptive. This is the right call for an exploratory study, but it should be stated more prominently — ideally in the Methods section rather than only at the end of the statistical approach paragraph.

**The Spearman ρ = -0.501 (p < 0.001) for the relationship between starting allocation and magnitude of change** has the same independence problem as the no-context ρ. Each data point is a (baseline, output) pair, but there are 30 runs per (word × baseline) cell, so the effective n for this correlation is at most 100 (10 words × 10 baselines), not 3,000. The p-value is meaningless at n=3,000 with clustered data.

---

## Threats to Validity

### Internal Validity

**Construct validity of the word scale.** The tiers are researcher-assigned. The finding that the model "violates ordinal ordering" for *moderately* depends entirely on the researcher having correctly placed *moderately* above the tier-1 and tier-2 words. The model's behavior (mapping *moderately* to 0.45) might be correct relative to actual human interpretation — *moderately* may genuinely mean "keep things moderate" rather than "increase by a moderate amount" in this context. Without the human baseline, the anomaly finding cannot be distinguished from a researcher miscategorization.

**Prompt confound.** The no-context prompt ("Architects should spend [WORD] more time on innovation") and the context prompt ("I would like to [WORD] increase innovation") have different syntactic structures beyond just the presence/absence of the baseline number. The no-context prompt uses "spend more time" while the context prompt uses "increase." These are not equivalent framings. Any difference between conditions could partially reflect the different verb constructions, not just the presence of context.

**The system prompt / tool schema is an uncontrolled variable.** As noted above, the complete prompt context is not reported. This is a significant internal validity threat because the model's calibration of "feasibility" — which drives the abstention behavior — is sensitive to how constraints are framed.

**Single model version.** The model is identified as `claude-haiku-4-5-20251001`. Model behavior can change with updates. The results are specific to this checkpoint.

### External Validity

**Single model.** All findings are specific to Claude Haiku. The paper correctly acknowledges this but the abstract's framing ("In this model and domain") is appropriate — the concern is whether the Discussion section occasionally generalizes beyond this. The "alignment framing" paragraph in Discussion, for example, makes claims about "model-mediated action interfaces" that go beyond what a single-model study supports.

**Single domain, single direction, single task structure.** Increase-only instructions in a resource-allocation task with a professional framing. The generalization to other domains (medical, financial, creative) is entirely unvalidated.

**Synthetic environment.** The allocation task is purpose-built. Whether the patterns hold in real deployed systems with richer prompts, multi-turn context, and more complex tool schemas is unknown.

**English only.** The findings are specific to English intensity words. Cross-linguistic behavior is entirely untested.

### Statistical Conclusion Validity

**The main risk is Type I error inflation** from the independence violation described above. The large effect sizes (ε² = 0.78, 0.97) are robust to this concern — these are not borderline findings that p-values are carrying. But the specific p-values reported should be understood as descriptive only.

**The $250K downstream consequence figure** is specific to the synthetic environment's objective function. The paper correctly notes this, but the number will be read as more general than it is. The finding that word choice propagates into outcome differences is valid; the specific dollar figure is not.

### Construct Validity

**"Compression" as a construct.** The paper uses "compression" to mean "multiple words map to the same output." This is a reasonable operationalization, but it conflates two distinct phenomena: (a) the model genuinely cannot distinguish the words, and (b) the model distinguishes the words but maps them to the same output because the task context doesn't require finer granularity. These have different implications. The first is a limitation of the model's semantic representation; the second is appropriate context-sensitivity. The paper does not separate these.

**"Abstention" as a construct.** As noted above, zero tool calls conflates constraint-aware refusal with other non-action behaviors.

---

## Reproducibility Assessment

### What Is Provided
- Model identifier (specific version string): ✓
- Temperature values: ✓
- Number of runs per cell: ✓
- Word list: ✓
- Baseline values: ✓
- High-level prompt templates: ✓
- Statistical tests used: ✓

### What Is Missing

**Critical gaps:**

1. **Complete prompt text.** The system prompt, tool schema definition (field names, types, constraints, descriptions), and any role-framing instructions are not provided. A replicator cannot reproduce the study without these. This is the single most important reproducibility gap. The model's behavior — especially the abstention pattern — is highly sensitive to how the tool and constraints are described.

2. **Random seed.** "Same synthetic data seed" is mentioned but the seed value is not reported.

3. **The deterministic backend specification.** The paper describes the backend as a "deterministic solver" that evaluates configurations, but the objective function is not specified. The $250K figure requires knowing the objective function. A replicator cannot verify or extend the downstream consequence analysis.

4. **Session initialization details.** "Fresh session, deep-copied state, no memory between calls" — what does this mean concretely for API calls? Are these single-turn calls? Is there a system prompt that persists across the 30 runs for a given cell?

5. **Abstention coding procedure.** How were abstentions identified? Was this automated (checking for empty tool_calls list) or manual? What happened to runs that produced tool calls with invalid values?

**Secondary gaps:**

6. The T=1.0 data is mentioned as collected but not analyzed. Its absence is noted but the reason (future revision) means the paper is incomplete as submitted.

7. The exact-number control results are mentioned but not reported in detail. These are the validation check for the harness; readers should be able to see them.

---

## Conclusions vs. Evidence

### Claims That Are Well-Supported

**"The model compresses 10 intensity words into 5 distinct median outputs."** Directly supported by Figure 2. This is a descriptive finding about this model in this condition, and it is stated accurately.

**"Grouping by starting allocation captures far more rank-based variance than grouping by word."** Supported by the two Kruskal-Wallis tests, with appropriate caveats about their separateness. The directional finding is credible even if the 10:1 ratio is not a standard statistical quantity.

**"Near feasibility limits the model exhibits three behavioral modes."** The abstention data at 89% is striking and well-documented. The characterization of three modes (hedge/act/abstain) is a reasonable description of the observed pattern.

**"These patterns persist across temperature."** The temperature comparison is appropriately modest — the paper correctly characterizes higher temperature as broadening distributions rather than restoring granular distinctions.

### Claims That Outrun the Evidence

**"The model's numeric interpretation of vague intensity words is compressed, state-dependent, and discontinuous near operational boundaries."** The first two are supported. "Discontinuous" is the strongest word here — the abstention finding is consistent with discontinuity but the paper tests only one near-boundary point (89%). A single boundary point cannot establish discontinuity versus a very steep continuous function. The paper would need at least 85%, 87%, 89%, 91%, 93% to characterize the transition.

**The "ordinal anomaly" framing for *moderately*.** This is presented as evidence that the model is behaving unexpectedly, but as noted above, it could be that the researcher's tier assignment is wrong. The word "anomaly" implies a deviation from a known correct ordering. The correct framing is: "the model's output for *moderately* falls below the researcher's hypothesized position for this word."

**The $250K consequence figure.** The paper correctly notes this is environment-specific, but the Discussion section's "alignment framing" paragraph uses language ("a narrow but important version of an alignment problem") that implicitly generalizes. The finding that word choice propagates into outcome differences is valid; the alignment framing requires the additional premise that users cannot detect or correct these differences, which is not tested.

**"Vague instructions should not be assumed to map to stable numeric actions."** This is the paper's practical conclusion, and it is stated in the Conclusion section. As a finding about Claude Haiku in a synthetic allocation task with increase-only instructions, the evidence supports it. As a general claim about LLM action interfaces, it overreaches — a single model, domain, and direction is insufficient basis for a general prescription.

**The Discussion's mechanistic speculation paragraph** (RLHF rewards moderate responses, 50% overrepresented in training data) is framed as "possibilities worth noting" rather than supported claims, which is appropriate. However, the paper should be clearer

### 3. Peer Reviewer

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

### 4. Domain Expert

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

### 5. Outsider / Red Team

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

### 6. Alignment Guide

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

---

## Deliberation Round

### Source Auditor — Revised Position

Now I have confirmed the key facts I need. Let me produce the full cross-council response.

---

# Reviewer F — Cross-Council Response

## Agreements

**Reviewer A — The ε² comparison structural problem.** I agree fully. Reviewer A correctly identifies that the 10:1 ratio is the paper's central quantitative claim and that it rests on two *separate* Kruskal-Wallis tests rather than a joint model. My original audit flagged this, but Reviewer A articulates the precise statistical remedy (a two-way Kruskal-Wallis or mixed-effects model with an interaction term) more crisply than I did. The interaction *is* the story, and the current framing doesn't test it. This is a genuine structural gap, not a disclosure issue.

**Reviewer A — The drastically/dramatically discontinuity is underanalyzed.** Reviewer A notes this is the paper's most alignment-relevant finding and gets one paragraph. I agree. My original audit flagged that the "as much as possible" interpretation for *drastically* is a post-hoc, untested claim. Reviewer A goes further by noting the model's actual text responses during abstention are available data that the author hasn't analyzed. This is correct and important: the abstention text is the most direct evidence for or against the proposed mechanism, and its absence is a reproducibility and evidentiary gap I should have flagged more prominently.

**Reviewer B — The no-word control is a structural gap, not a nice-to-have.** Reviewer B's framing is sharper than mine: this is not a "hole to patch" but the falsification condition for the paper's most prominent interpretive claim. I agree. At 30 runs × 2 temperatures = 60 API calls, its absence is hard to justify on cost grounds. My original audit noted this gap but understated its centrality to the hedge interpretation.

**Reviewer B — The $250K figure is rhetorically overloaded.** I agree with Reviewer B's specific suggestion: the point about propagation could be made more defensibly by staying in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars. The dollar figure will be extracted from context by non-technical readers and cited as a real-world consequence. My original audit flagged this but did not offer the cleaner alternative framing Reviewer B provides.

**Reviewer C — The inversion finding (5:1 → 14:1) is buried and should be in the abstract.** This is correct and I missed it entirely. Reviewer C identifies that the complete reversal of word-vs-state dominance across the allocation range is arguably more operationally important than the overall 10:1 ratio, yet it appears only in Section 4.2 and not in the abstract or conclusion. This is a genuine alignment gap between what the paper delivers and what it advertises. I should have caught this.

**Reviewer C — The "hedge" language in Discussion is inconsistent with Future Work's epistemic honesty.** Reviewer C correctly notes that the Discussion uses "hedge" as settled language while Future Work correctly flags it as unconfirmed. This is an internal consistency issue I flagged in my original audit, but Reviewer C's proposed fix — "appears to function as a hedge" rather than "functions as a hedge" — is the right one-word correction.

**Reviewer D — The abstention operationalization conflates two distinct behaviors.** Reviewer D identifies that "zero tool calls" could mean constraint-aware refusal *or* other non-action behaviors, and the paper uses "typically" to characterize the abstention responses without coding them. This is a construct validity issue I did not raise and should have. It directly affects the interpretability of the 121/300 abstention figure at 89%.

**Reviewer D — The independence violation is more serious than acknowledged.** Reviewer D correctly notes that at T=0.0, four words produce the *exact same value* across all 30 runs — these are not 30 independent observations but one observation repeated 30 times. The effective sample size for the no-context T=0.0 Spearman ρ is closer to 10 (one median per word) than 300. My original audit flagged the independence issue but did not quantify how severely it affects the no-context ρ specifically.

**Reviewer E — The "ordinal anomaly" framing for *moderately* is epistemically fragile.** Reviewer E correctly notes that calling *moderately* an "anomaly" presupposes the researcher's tier assignment is correct. The model's behavior (0.45) might be the accurate reflection of how humans use the word. Without the human baseline, "anomaly" is the wrong word. My original audit made this point but Reviewer E's framing — "the model's output for *moderately* falls below the researcher's hypothesized position" — is more precise and less loaded.

---

## Disagreements

**Reviewer A — "The paper should either not report [ε² = 0.969] or replace it with a more appropriate measure."** I partially disagree. The paper already explicitly flags the inflation ("This effect size is partly inflated by the deterministic decoding condition") and explains why. Removing the statistic would lose information; replacing it with only the count of distinct medians (which the paper also reports as 5) would be less informative about the degree of between-group separation. The better fix is to keep the statistic but move the inflation caveat from a parenthetical to a more prominent position — perhaps immediately after the number rather than two sentences later. Suppression is not the right remedy for a disclosed limitation.

**Reviewer A — Recommending the decrease condition be included in this paper rather than future work.** Reviewer A argues this is a "missed opportunity that reviewers will notice." I disagree that this rises to a paper-level deficiency. The paper is explicitly scoped as a "first measurement slice." Adding a decrease condition without a clear a priori hypothesis about asymmetry would expand scope without proportionate gain. The paper's existing scope is coherent; the decrease condition belongs in a second study where asymmetry can be the primary research question, not an afterthought appended to this one.

**Reviewer B — "Weak Accept" for a workshop venue.** My assessment is slightly more conservative. The missing no-word control and the unvalidated word scale together mean the paper's central interpretive claim (compression as a meaningful failure, not a default) is currently unfalsified. For a workshop venue focused on empirical findings, this is acceptable with revision; for a main track, it is not. I would rate this "Conditional Accept for workshop, Revise and Resubmit for main track," which is functionally similar to Reviewer B's verdict but with a stronger emphasis on the no-word control as a pre-acceptance requirement rather than a post-acceptance extension.

**Reviewer E — "The differentiation funnel may be trivially expected from the constraint structure."** Reviewer E argues that convergence near 89% might simply follow mathematically from the constraint: if you're at 89%, any increase instruction can only go to ~91% regardless of word. This is a fair alternative explanation for the *convergence* finding, but it does not explain the *abstention* finding — which is the more striking result. The model doesn't just produce small increases near 89%; it *refuses to act at all* for some words while acting for others. That word-dependent categorical switching is not a mathematical consequence of the constraint. Reviewer E's critique applies to the differentiation funnel but not to the boundary mode-switching finding, and the paper should be clearer about which claim each piece of evidence supports.

---

## Revisions to My Review

**What I missed and would add:**

**1. The Mosteller & Youtz page range issue is more complex than I stated.** My original audit flagged the bibliography entry as truncating the page range (pp. 2–12 rather than 2–34). The search results now confirm this is genuinely ambiguous: the Project Euclid canonical record lists the article as 5(1): 2-12, while the Stanford-hosted PDF and the Harvard repository both cite the volume as 1990, Vol. 5, No. 1, 2-34. The discrepancy appears to reflect the difference between the article itself (pp. 2–12) and the full issue section including comments and rejoinder (pp. 2–34). The comments run from pp. 13–30 and the rejoinder from pp. 31–34. The paper's bibliography entry of "pp. 2–12" is therefore *correct* for the article itself, and my original citation issue flag was wrong. I retract it.

**2. The Mosteller & Youtz "high variance

### Methodologist — Revised Position

# Methodologist's Response to Council Reviews

---

## Agreements

**Reviewer A — The two-way analysis gap**
Reviewer A correctly identifies that the correct analysis for the word × baseline interaction is a two-way model, not two separate Kruskal-Wallis tests. I raised this in my original review, but Reviewer A articulates the specific consequence more precisely: without a joint model, you cannot distinguish whether baseline captures more variance because it genuinely dominates, or because the two factors are correlated and baseline absorbs shared variance. This is the right framing and I endorse it fully.

**Reviewer A — The ε² = 0.969 inflation problem**
Reviewer A goes further than I did on this point, correctly noting that when within-group variance is exactly zero for four of ten words at T=0.0, the statistic approaches 1.0 trivially and "reporting ε² = 0.969 as a meaningful statistic is misleading." I flagged inflation but understated how severe it is. Reviewer A's recommendation to either drop the number or replace it with the count of distinct medians (already reported as 5) is the right fix.

**Reviewer C — The no-word control is not a nice-to-have**
Reviewer C frames this more forcefully than I did: "it is the falsification condition for the paper's most prominent interpretive claim." I agree. My original review called it a "structural gap"; Reviewer C's language better captures the epistemic severity. The hedge interpretation is not merely unconfirmed — it is unfalsified within the paper.

**Reviewer C — The split-range analysis ratios are post-hoc descriptive, not confirmatory**
Reviewer C and I agree on this. The 5:1 and 14:1 figures are derived from a researcher-chosen split point and should not be treated as established quantities. The paper's disclosure is honest but the framing occasionally treats these as independent evidence.

**Reviewer E — The convergence near capacity may be mathematically trivial**
Reviewer E raises a point I did not: "when a system is near its maximum capacity, any instruction to increase it will produce a small increase regardless of the word used — because there's no room to increase more." This is a genuine alternative explanation for the differentiation funnel that the paper does not address. The convergence finding may be a mathematical consequence of the constraint structure rather than a finding about language interpretation. I should have caught this.

**Reviewer F — The inversion finding is undersurfaced**
Reviewer F identifies that the 5:1 → 14:1 inversion is the paper's most operationally important result and it is absent from the abstract. I agree. The abstract reports the overall 10:1 ratio, which is an average that masks the directional reversal. The inversion is the finding that most directly supports the "passive failure" framing: the interface appears word-driven at low baselines and becomes state-driven at high baselines, invisibly to the operator.

**Reviewer B — Mosteller & Youtz mischaracterization**
Reviewer B flags that the paper describes Mosteller & Youtz as showing "high variance around ordered central tendencies" when the actual finding is closer to the opposite: cross-study averages were relatively stable, with high individual-level variance. This is a real mischaracterization that I missed entirely. It is minor in terms of the paper's argument but is a citation accuracy issue.

---

## Disagreements

**Reviewer A — "The paper should either not report this number or replace it with a more appropriate measure"**
Reviewer A recommends dropping ε² = 0.969 or replacing it. I partially disagree. The number should stay with a stronger caveat, not be dropped. Removing it would obscure the methodological lesson: deterministic decoding produces trivially inflated effect sizes, which is itself a finding about how to design and interpret these experiments. The paper's current disclosure is too brief; it should be expanded into a methodological note, not resolved by deletion.

**Reviewer C — "Weak Accept for workshop; Borderline for full conference main track"**
This is a venue recommendation rather than a methodological judgment, which is outside my mandate. I note only that the methodological gaps I identified — missing no-word control, unvalidated word scale, independence violation in ρ computation, incomplete prompt specification — are the factors that should drive venue decisions, and those gaps are real regardless of where the paper is submitted.

**Reviewer E — "The differentiation funnel is an evocative name for a phenomenon that might be trivially expected"**
Reviewer E argues the convergence near capacity "might follow directly from the constraint structure." I agree this is a valid alternative explanation, but I would not characterize it as "trivially expected." The non-trivial finding is not that all words converge near capacity — that is indeed mathematically expected — but that the convergence happens at 75% rather than, say, 95%, and that the transition is sharp rather than gradual. The paper does not characterize the transition point or its sharpness, which is the actual gap. The finding is not trivial; it is underspecified.

**Reviewer A — "Run the human survey first, or concurrently"**
Reviewer A recommends the human survey should have been the first instrument. I understand the argument but disagree methodologically. The controlled measurement instrument (the LLM harness) is the contribution; the human survey is the validation. Running the survey first would have required pre-specifying the word scale and task framing without knowing whether the harness would produce interesting variation. The sequencing is defensible. The problem is not the order but the absence of the survey from this paper, which leaves the ordinal claims unanchored.

---

## Revisions to My Review

**Addition: The convergence-as-mathematical-artifact problem (from Reviewer E)**
I should have raised the alternative explanation that convergence near capacity is a mathematical consequence of the constraint, not a behavioral finding. The paper needs to address this directly. The relevant test would be: does convergence happen at the mathematically expected point (near 100%), or does it happen earlier? The data shows convergence at 75%, which is not the mathematical ceiling — this is the finding. But the paper does not frame it this way, and without this framing, the convergence result is vulnerable to the "trivially expected" critique.

**Strengthening: The Spearman ρ effective sample size problem**
I raised the independence violation but did not fully specify the consequence. At T=0.0, where four words produce identical outputs across all 30 runs, the effective sample size for the no-context ρ is not 300 — it is closer to 10 (one observation per word). The correct computation is ρ over the 10 word-level medians with n=10, not ρ over 300 individual runs. The p-value at n=300 with clustered data is not merely overstated; it is the wrong quantity. The paper should report ρ over medians with the correct uncertainty, or use a permutation test that respects the clustering. I stated this in my original review but should have been more explicit that this affects the primary ordinal faithfulness claim, not just the significance level.

**Addition: The prompt template confound is more serious than I acknowledged**
I flagged the syntactic frame difference between no-context ("should spend [WORD] more time") and context ("I would like to [WORD] increase") as a confound. Reviewing the figures more carefully, I note that the no-context condition produces 0.50 for four weak words while the context condition at b=0% produces approximately 0.10 for the same words (visible in Figure 4). This is a large difference that could reflect the syntactic frame difference as much as the presence of context. The paper attributes this difference to the presence of context, but the prompt structure changed simultaneously. This is a more serious internal validity threat than I originally stated, and it is not acknowledged in the Limitations section.

**Addition: The abstention operationalization conflates two phenomena — and the 89% baseline is the only boundary tested**
I raised both of these in my original review, but I want to strengthen the second point. The paper claims the model "switches into qualitatively different behavior" near feasibility limits. But "near feasibility limits" is operationalized with a single data point: 89%. The paper cannot establish that this is a boundary effect rather than a high-baseline effect without testing intermediate points (85%, 87%, 91%, 93%). The transition point and its sharpness are the empirically interesting quantities, and they are entirely uncharacterized. This is a significant gap in the boundary behavior section that no other reviewer emphasized sufficiently.

**Retraction: I overstated the severity of the two-ε² comparison problem**
In my original review, I said the ratio comparison "cannot distinguish" between three possible explanations. On reflection, the directional finding (baseline explains more than word) is robust to the methodological limitation, even if the specific ratio is not a standard statistical quantity. The paper

### Peer Reviewer — Revised Position

### Agreements

**Reviewer A — Statistical structure of the ε² comparison (W1 equivalent):**
Reviewer A's point that the correct analysis is a two-way Kruskal-Wallis or mixed-effects model with word and baseline as factors is exactly right, and I understated this in my own review. I flagged the two-test independence issue (W3 in my review) but framed it as "moderate" rather than "structural." Reviewer A is correct that this is the paper's central quantitative claim and the framing has a structural problem that the current caveats don't fully resolve. I should have been more forceful here.

**Reviewer B — Prompt confound between no-context and context conditions:**
Reviewer B's W5 observation that the two prompt templates use different syntactic frames ("should spend [WORD] more time" vs. "I would like to [WORD] increase") is a confound I missed entirely. This is a legitimate internal validity threat: any difference between conditions could partially reflect the different verb constructions, not just the presence of context. I should have caught this.

**Reviewer C — The "differentiation funnel" may be trivially expected:**
Reviewer C's Gap 3 is sharp: when a system is near maximum capacity, any increase instruction will produce a small increase regardless of word, because there is no room to increase more. The convergence near 89% may be a mathematical consequence of the constraint structure rather than a finding about language interpretation. I noted the convergence finding as a strength (Strength 4) without adequately interrogating whether it is surprising given the task design. Reviewer C is right to push on this.

**Reviewer E — The inversion finding is underemphasized:**
Reviewer F (the alignment guide reviewer) makes this point most forcefully, but Reviewer E's source audit implicitly supports it. The complete inversion of explanatory power (5:1 word-dominant at low baselines → 14:1 state-dominant at high baselines) is arguably the most operationally important finding in the paper and is absent from the abstract. I noted the differentiation funnel as a strength but did not flag the inversion's absence from the abstract as a weakness. This is a gap in my review.

**Reviewer D (my own) — No-word control as structural gap:**
Reviewers A, B, C, and F all independently converge on this point. My W1 was correct and appropriately prioritized. The convergence across reviewers strengthens my confidence that this is the paper's most important fixable gap.

**Reviewer F — "Hedge" language should be softened in Discussion:**
My W1 noted the hedge interpretation is unfalsified, but Reviewer F makes the sharper point that the Discussion uses "hedge" as settled language while Future Work correctly flags it as unconfirmed. This is an internal inconsistency I identified but didn't frame as precisely. Reviewer F's framing is better: the fix is a single word change ("appears to function as a hedge"), not a new experiment.

---

### Disagreements

**Reviewer A — Cornerstone verdict closer to (b) than (a):**
Reviewer A concludes the paper is "closer to (b) than the author's framing suggests." I think this is too harsh. The boundary behavior finding (hedge/act/abstain) and the differentiation funnel inversion are genuinely novel empirical contributions that go beyond what the existing calibration or pragmatics literature has documented in the action case. The paper is (c), but I would place it closer to (a) than Reviewer A does — specifically because the measurement instrument is clean and replicable, which is the foundational requirement for a cornerstone. A cornerstone doesn't need to be complete; it needs to be reproducible and extensible. This one is.

**Reviewer C — The alignment framing is "retrofitted":**
Reviewer C argues the alignment framing "reads like it was added to elevate the paper's significance." I disagree. The finding that a one-word swap between near-synonyms (*drastically* vs. *dramatically*) produces categorically different action policies at the most constrained boundary is a genuine alignment-relevant result, not a rhetorical move. The framing may be underdeveloped, but it is not manufactured. The issue is that the paper needs the human baseline to distinguish "model failure" from "accurate modeling of human ambiguity" — but the alignment framing is not wrong, it is premature. That's a different critique.

**Reviewer B — Abstention operationalization conflates two things:**
Reviewer B argues that zero tool calls conflates constraint-aware refusal with other non-action behaviors. This is technically correct, but the paper reports that abstaining runs "typically cite the constraint that allocations must sum to 100%." The word "typically" is imprecise, but if the author has the text responses, this is a characterization issue, not a fundamental operationalization failure. I would frame this as a documentation gap (show the text responses) rather than a construct validity problem. Reviewer B overstates the severity here.

**Reviewer E — Mosteller & Youtz "high variance" mischaracterization:**
Reviewer E flags that the paper says Mosteller & Youtz "showed high variance around ordered central tendencies" when the actual finding is that cross-study averages were relatively stable. This is a real discrepancy, but it is minor in context: the paper uses Mosteller & Youtz to motivate the general point that numeric interpretation of vague language varies, which is consistent with the source even if the specific characterization is imprecise. Reviewer E is correct to flag it, but it does not affect any finding in the paper.

---

### Revisions to My Review

**What I missed and would add:**

1. **The prompt confound (Reviewer B's W5).** I should have flagged that the no-context and context prompts use different syntactic frames. This belongs in my Weaknesses section as a moderate weakness. It doesn't invalidate the conditions comparison, but it should be acknowledged as a limitation.

2. **The trivial-convergence alternative explanation (Reviewer C's Gap 3).** I should have noted that convergence near capacity may follow from the constraint structure rather than from anything interesting about language interpretation. This is a competing explanation for the differentiation funnel that the paper does not address. I would add this to my Questions for Authors.

3. **The inversion finding's absence from the abstract.** I noted the differentiation funnel as a strength but did not flag the abstract's failure to surface the inversion. Reviewer F is right that this is the most operationally important result and its absence from the abstract is a gap between what the paper delivers and what the abstract promises. I would add this to my Minor Issues or elevate it to a Moderate Weakness.

4. **The Spearman ρ computation over n=300 vs. n=10.** I raised this in Question 5, but Reviewer B makes the stronger point that at T=0.0 with near-zero within-word variance, the effective sample size for the no-context ρ is closer to 10 than 300. I should have flagged this more forcefully in my Weaknesses rather than only in Questions.

5. **Missing citations: scalar implicature / RSA literature.** Reviewer A's point about the Rational Speech Acts framework is one I should have raised. The *moderately* anomaly is a textbook scalar implicature problem, and the paper's failure to engage with Frank & Goodman (2012) or the computational pragmatics literature is a genuine related-work gap. I would add this to my Weaknesses.

**What I stand by:**

- The boundary behavior finding (hedge/act/abstain) as the paper's most distinctive contribution. No reviewer disputes this.
- The no-word control as the single most important missing condition. All reviewers converge.
- The Weak Accept recommendation for workshop/findings track, Borderline for main conference. The consensus across reviewers supports this positioning.
- The cornerstone verdict as (c), leaning toward (a) with extensions. I maintain my disagreement with Reviewer A's more pessimistic placement.

**Revised recommendation language:** I would add to my recommendation: "The abstract should be revised to surface the word-dominance inversion finding (5:1 → 14:1 flip across baselines), which is the paper's most operationally significant result and is currently absent from the abstract. The Discussion should soften 'functions as a hedge' to 'appears to function as a hedge' to match the epistemic status acknowledged in Future Work. The prompt confound between conditions should be acknowledged as a limitation."

---

### Blind Spots

Points that no reviewer (including myself) adequately addressed:

**1. The three-failure-compound problem near operational boundaries.**
Every reviewer noted the individual findings (compression, state dominance, boundary mode-switching) but no reviewer explicitly stated that these three failures are simultaneously worst at the same point in the allocation space — near capacity, where the system is most const

### Domain Expert — Revised Position

## Agreements

**Reviewer A — Gap 2 (no-word control as central, not peripheral):** Reviewer A correctly identifies that the no-word control is not a "nice-to-have extension" but a falsification condition for the paper's central interpretive claim. I flagged this in my original review, but Reviewer A's framing is sharper: the hedge interpretation is the paper's most cited-ready result, and it is currently unfalsified within the paper. I agree this should be elevated from Future Work to a genuine limitation of the current claims.

**Reviewer C — The inversion finding is underemphasized relative to its importance:** Reviewer C identifies that the 5:1 → 14:1 inversion is arguably more important than the overall 10:1 ratio and is currently buried in Section 4.2. I agree completely. The inversion is the most operationally dangerous pattern — the interface *looks* word-driven at low baselines and *becomes* state-driven at high baselines, invisibly to the operator. This belongs in the abstract. I mentioned the interaction structure in my original review but did not flag the abstract-level absence as a specific correctable problem.

**Reviewer C — The three failure modes compound simultaneously near boundaries:** Reviewer C identifies that the paper never explicitly states that compression, state dominance, and mode-switching are all worst simultaneously at the most constrained operating point. This synthesis is the paper's strongest single claim and it is currently implicit. I missed this entirely in my original review. It is a genuine gap.

**Reviewer E — The independence violation is more serious than acknowledged:** Reviewer E is correct that at T=0.0, four words produce the exact same value across all 30 runs, making those 30 runs effectively one observation repeated. The effective sample size for the no-context Spearman ρ is closer to 10 than 300. I flagged the independence issue in my original review but understated its severity. Reviewer E's point that the p-values are "essentially meaningless as inferential quantities" in this regime is technically correct. The right fix is computing ρ over word-level medians (n=10) with appropriate uncertainty, not over all 300 runs.

**Reviewer F — The $250K figure is rhetorically overloaded:** Reviewer F correctly identifies that using a concrete dollar amount from a synthetic environment to motivate real-world concern is a rhetorical move that invites skepticism. I flagged this as a technical red flag in my original review. Reviewer F's suggested fix — stay in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars — is the right prescription.

**Reviewer E — The prompt confound between conditions:** Reviewer E identifies that the no-context prompt ("should spend [WORD] more time on innovation") and the context prompt ("I would like to [WORD] increase innovation") use different syntactic frames beyond just the presence/absence of the baseline number. I flagged this in my original review as a confound worth acknowledging. Reviewer E correctly notes this is a construct validity issue, not just a minor limitation.

**Reviewer D — Mosteller & Youtz mischaracterization:** Reviewer D identifies that the paper describes Mosteller & Youtz as showing "high variance around ordered central tendencies" when the actual finding is that cross-study averages were relatively *stable* — almost the opposite emphasis. I did not catch this in my original review. This is a real bibliographic accuracy issue.

---

## Disagreements

**Reviewer A — Cornerstone verdict leaning toward (b):** Reviewer A concludes the paper is "closer to (b) than the author's framing suggests." I disagree with this weighting. The paper's measurement instrument is genuinely novel in the action-production context. The distinction between probability estimation (Zhang 2024, Mosteller 1990) and action production is real and under-studied. The boundary behavior finding (hedge/act/abstain) is not a finding you would predict from the prior literature, and the drastically/dramatically discontinuity is a genuine empirical surprise. These are not characteristics of a "fine niche result with inflated framing." The paper is (c), but I would place it closer to (a) than Reviewer A does, conditional on the human survey and one cross-model replication. Reviewer A's verdict seems to discount the novelty of the action-production framing relative to the existing probability-estimation literature.

**Reviewer A — "The differentiation funnel might be trivially expected":** Reviewer A argues that convergence near 89% might follow directly from the constraint structure — if there's no room to increase, all words produce the same small increase. This is partially correct but misses the most important part of the finding: the *abstention* behavior. The convergence of *action magnitudes* near capacity is indeed somewhat expected. What is not expected — and what the paper documents — is that some words trigger *complete abstention* (zero tool calls) while others continue to act. The constraint explanation predicts small actions for all words; it does not predict categorical refusal for some words and ceiling-pushing for others. Reviewer A's critique applies to the convergence finding but not to the mode-switching finding, and the paper's most important boundary result is the mode-switching, not the convergence.

**Reviewer F — "Weak Accept" recommendation:** Reviewer F recommends Weak Accept for a workshop venue. I think this is slightly too conservative given the boundary behavior finding. The drastically/dramatically discontinuity — two near-synonyms producing categorically different action policies in identical system states — is a result that would be interesting to the NeurIPS alignment workshop or the ACL workshop on human-AI interaction regardless of the single-model limitation. The paper's methodological transparency (flagging inflated statistics, non-pre-registered splits, independence violations) is itself a contribution to norms in this space. I would recommend Accept for a workshop venue and Borderline for a full conference findings track, which is slightly more optimistic than Reviewer F.

**Reviewer E — "Discontinuous" is too strong a claim:** Reviewer E argues that a single boundary point (89%) cannot establish discontinuity versus a very steep continuous function. This is technically correct and I agree the paper should hedge this language. However, I think Reviewer E understates how informative the 89% data is. The *categorical* nature of the abstention — 100% abstention for considerably/substantially/significantly, 0% for tiers 1-3, 7% for drastically — is not consistent with a smooth function. A smooth function would produce graded abstention rates across words. The all-or-nothing pattern within words is itself evidence of a categorical decision process, even from a single boundary point. The paper should say "consistent with discontinuity" rather than "discontinuous," but the finding is stronger than Reviewer E implies.

---

## Revisions to My Review

**What I missed:**

**1. The synthesis gap (Reviewer C's most important point).** I identified the three findings individually but never noted that the paper fails to state their simultaneous worst-case at the operational boundary. This is the paper's most important unclaimed result and it requires zero additional data. I would add this to my Technical Red Flags section: the paper has a finding it hasn't made.

**2. The abstract-level absence of the inversion finding.** I discussed the inversion in my original review but did not flag that it is absent from the abstract. Given that the abstract is what gets read and cited, this is a more serious omission than I originally treated it. I would add this to my Baselines and Comparisons section as a framing issue.

**3. The severity of the independence violation at T=0.0.** I flagged the independence issue but Reviewer E's analysis is sharper than mine: at T=0.0, the effective sample size for the no-context Spearman ρ is ~10, not 300. The p < 0.001 notation is not just "overstated" — it is misleading by approximately two orders of magnitude in effective n. I would strengthen my Technical Red Flags section accordingly and recommend the author compute ρ over word-level medians with a permutation test.

**4. The Mosteller & Youtz mischaracterization.** I did not catch this. The paper describes "high variance around ordered central tendencies" when the source actually found relatively stable cross-study averages. This should be corrected.

**What I stand by:**

My core assessment — that the paper is (c) leaning toward (a) with the human survey and cross-model replication — is unchanged and is consistent with the strongest reviewers (B, C, E, F). My identification of the two-way Kruskal-Wallis as the correct statistical approach for the word × baseline interaction remains the most important statistical fix not flagged by other reviewers. My recommendation that the drastically/dramatically abstention text responses be analyzed (the model's actual language during abstention is data the author has but hasn't used) was not picked up by other reviewers and remains the cheapest high-value addition to the

### Outsider / Red Team — Revised Position

### Agreements

**Reviewer B — The inversion finding deserves abstract-level visibility.**
Reviewer B correctly identifies that the 5:1 to 14:1 inversion is arguably the most operationally important result and is currently buried. I flagged this as a logical gap (the paper doesn't fully reckon with what the inversion means for a user who can't see it happening), but Reviewer B makes the structural point more precisely: the abstract reports the overall 10:1 ratio but not the inversion. I agree this is a significant omission. The inversion is the finding that should alarm a practitioner — the interface *looks* word-driven when you're far from a constraint and *becomes* state-driven when you're near one, invisibly.

**Reviewer C — The "drastically vs. dramatically" finding is underanalyzed.**
Reviewer C flags that the model's actual text responses during abstention are data that exists but hasn't been analyzed. I made the same point in my review (under "What I Still Don't Understand" and "Logical Gaps"). Reviewer C adds the specific alternative explanation I didn't articulate: the difference might be about training data distribution (how each word appears in context) rather than the model's constraint reasoning. That's a sharper version of my concern and I agree with it.

**Reviewer D — The $250K figure is rhetorically overloaded.**
Reviewer D's point that the dollar figure will be extracted from context and read as a real-world consequence is exactly right. I flagged this as a logical gap, but Reviewer D adds the useful suggestion that the paper would be more defensible staying in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars. That's a concrete fix I didn't offer.

**Reviewer E — The independence violation is more serious than acknowledged.**
Reviewer E makes the technical point precisely: at T=0.0, four words produce the exact same value across all 30 runs. These are not 30 independent observations; they are one observation repeated 30 times. The p-values are not merely "overstated" — they are essentially meaningless as inferential quantities. I noted the independence problem in my review but didn't articulate how severe it is at T=0.0 specifically. Reviewer E is right that the Spearman ρ should be computed over word-level medians (n=10), not over all 300 individual runs.

**Reviewer A — The Mosteller & Youtz characterization is a partial mischaracterization.**
Reviewer A flags that the paper says Mosteller & Youtz "showed high variance around ordered central tendencies" when the actual finding is more nuanced — the variation of averages across studies was modest, not high. I didn't catch this. It's a real, if minor, mischaracterization.

---

### Disagreements

**Reviewer C — "Run the human survey first, or concurrently" as the primary design critique.**
Reviewer C says the entire interpretive framework depends on knowing what humans mean by these words and that running the experiment without this is "like measuring a thermometer's accuracy without a reference temperature." I understand this argument but I think it's too strong. The paper is measuring *what the model does*, not whether the model is right or wrong relative to humans. The compression finding — 10 words collapsing to 5 outputs — is a real finding about the model's behavior regardless of what humans would do. The human baseline is needed to *interpret* whether this is a failure, but it's not needed to establish that it *happens*. The thermometer analogy implies the paper is measuring accuracy against a known standard; it's actually measuring a behavior pattern. These are different things.

**Reviewer C — Verdict (c) "closer to (a) than the author's doubt suggests."**
Reviewer C says the paper is closer to (a) — legitimate elevation — than the author's doubt suggests. I think Reviewer C is being generous here. The single-model scope, the unvalidated word scale, and the missing no-word control are not minor gaps. They are the three things that would need to be true for the paper to function as a general measurement instrument. Without them, it's a careful single-model observation. I'd put it closer to the (b)/(c) boundary than Reviewer C does.

**Reviewer B — The "moderately" observation as "ordinal anomaly" framing.**
Reviewer B recommends softening the "ordinal anomaly" language. I agree with the direction but I think the more important point is that the "anomaly" framing assumes the researcher's tier assignment is correct. Reviewer B treats this as a framing issue; I think it's a validity issue. The word "anomaly" implies deviation from a known correct ordering. The paper doesn't have a known correct ordering — it has the author's ordering. Softening the language is necessary but not sufficient; the paper needs to acknowledge that "moderately" behaving differently might mean the tier assignment is wrong, not that the model is wrong.

---

### Revisions to My Review

**What I missed: The prompt template confound.**
Reviewer E correctly identifies that the no-context prompt ("should spend [WORD] more time on innovation") and the context prompt ("I would like to [WORD] increase innovation") use different syntactic frames beyond just the presence/absence of the baseline number. I didn't catch this. It's a real confound: any difference between conditions could partially reflect the different verb constructions. I would add this to my "Logical Gaps" section.

**What I missed: The abstention operationalization conflates two things.**
Reviewer E points out that "zero tool calls" conflates constraint-aware refusal with other non-action behaviors. I mentioned wanting to see the model's actual text responses, but I didn't frame this as an operationalization problem. That's a sharper and more useful critique. I would add this to my "Logical Gaps" section.

**What I would strengthen: The convergence-near-capacity finding.**
I raised the concern that convergence near 89% might be a mathematical consequence of the constraint structure rather than a finding about language interpretation. Reviewer E's point about the "differentiation funnel" being potentially trivially expected strengthens this. I would make this concern more prominent in my review — it's not just a caveat, it's an alternative explanation for one of the paper's three main findings.

**What I stand by: The "cornerstone" assessment.**
After reading all six reviews, I stand by my verdict that this paper cannot currently bear the weight of the field-building framing. Reviewers C and D both land near (c) with different emphases, and none of the other reviewers argue for (a). The consensus is that the paper is a solid first measurement slice that requires the human baseline and cross-model comparison before its claims generalize. I think my framing of this — "the paper is not the field; it's a data point that could, with extensions, become part of the field" — is accurate and I would not soften it.

---

### Blind Spots

**No reviewer examined the role of the specific domain framing.**
All prompts concern "innovation allocation" for "Architects." The word "innovation" has strong positive valence in professional/business contexts and is likely overrepresented in training data as something to be maximized. No reviewer asked: would the same compression and abstention patterns appear if the task were "reduce risk allocation" or "decrease safety budget"? The domain framing may be doing significant work in producing the observed patterns — particularly the abstention behavior, which might reflect the model's learned disposition toward "innovation" specifically rather than a general property of constraint-near behavior. This is a threat to external validity that none of the six reviews raised.

**No reviewer examined the three-task constraint structure as a potential artifact.**
The allocation environment requires three tasks to sum to 100%. This means increasing one task necessarily decreases others. No reviewer asked whether the model's behavior — particularly the 0.50 hedge and the abstention near 89% — might reflect the model reasoning about the *other two tasks* rather than just the target task. If the model is implicitly protecting the other allocations, the observed behavior is about multi-task constraint management, not about the intensity word's numeric meaning. This is a different mechanism than what the paper claims, and it's not addressed anywhere in the six reviews.

**No reviewer asked about the model's "knowledge" of the constraint.**
The paper says the model "typically cites the constraint that allocations must sum to 100%" when abstaining. But how does the model know about this constraint? It must be in the system prompt or tool schema — which are not reported. If the constraint is explicitly stated in the system prompt, the abstention behavior is the model following an explicit rule. If it's not stated and the model infers it, that's a different finding. This distinction matters enormously for interpreting the boundary behavior section, and none of the six reviews raised it.

**No reviewer examined the implications of the finding for the *user*, not the system.**
The paper frames its findings in terms of what the model does. But the practical implication is about

### Alignment Guide — Revised Position

# Alignment Guide — Council Response

## Agreements

**Reviewer B, W1 (no-word control as structural gap):** Agreed, and I flagged this in my Missing Sections. But Reviewer B sharpens the point in a way I didn't: the hedge interpretation is used as *settled language* in the Discussion while being flagged as unconfirmed in Future Work. That's an internal inconsistency between sections, which is squarely my mandate. I noted it but didn't name it as an internal inconsistency explicitly. I should have.

**Reviewer D, "Conclusions vs. Evidence" section on the "discontinuous" claim:** Reviewer D correctly identifies that a single boundary point (89%) cannot establish discontinuity versus a steep continuous function. From an alignment perspective, this means the paper's third stated research question — "does the model switch into qualitatively different behavior?" — is answered with less evidence than the paper implies. The conclusion section states the mode-switching finding as established; the evidence only supports "consistent with mode-switching at one tested boundary." This is a promise-delivery gap I underweighted.

**Reviewer F, "differentiation funnel may be trivially expected" (Logical Gap 3):** This is the most important point I missed entirely. If the convergence near 89% follows mathematically from the constraint structure (there's simply less room to move), then the "differentiation funnel" is not a finding about language interpretation — it's a finding about arithmetic. The paper does not address this alternative explanation. From my mandate: the paper claims to deliver evidence about how the model handles vague language near boundaries, but the boundary convergence finding may be explained by the environment's design rather than by the model's linguistic behavior. This is a gap between what's promised (a finding about language-to-action translation) and what's delivered (a finding that may be partially about constraint geometry).

**Reviewer A, on the drastically/dramatically discontinuity being underanalyzed:** I flagged this as a missing section — the paper's most alignment-relevant finding gets one paragraph. Reviewer A adds that the model's text responses during abstention are data the author has but hasn't analyzed. That's a concrete missing section I should have named explicitly rather than just noting the finding is underemphasized.

**Reviewer E (myself), on the inversion finding not appearing in the abstract:** All other reviewers who touched on the 10:1 ratio noted the caveat about separate tests, but none flagged the abstract-level omission of the inversion as prominently as I did. I stand by this as the highest-priority alignment fix: the abstract implies a stable dominance relationship; the paper shows it completely reverses. That's a direct abstract-to-content misalignment.

---

## Disagreements

**Reviewer A and B, framing the no-word control as primarily a statistical/methodological gap:** Both reviewers treat this as a technical weakness. From my mandate, it's an alignment problem: the paper's Discussion uses "hedge" as a settled interpretive concept, but the paper's own Future Work section says the hedge interpretation is unconfirmed. That's not a missing experiment — it's a section of the paper (Discussion) making a claim that another section of the same paper (Future Work) explicitly says is unsupported. The fix isn't just running the control; it's aligning the Discussion's language with the paper's actual epistemic state. This distinction matters for the revision brief.

**Reviewer D, on the "compression" construct conflating two phenomena:** Reviewer D argues the paper conflates "model cannot distinguish words" with "model maps words to same output because task context doesn't require finer granularity." This is a valid technical point, but from an alignment perspective, the paper's stated contribution is specifically about whether the interface is "less expressive than it appears" — which is the operator-facing version of the same question regardless of mechanism. The paper doesn't promise to resolve the mechanism; it promises to measure the expressivity gap. On that narrower claim, the paper delivers. I'd push back on framing this as a contribution failure; it's a mechanistic gap the paper doesn't claim to close.

**Reviewer F, cornerstone verdict leaning toward (b):** Reviewer F concludes the paper leans toward "fine niche result with inflated framing." From a pure alignment perspective — does the paper do what it says it will do — the paper is actually well-aligned internally. The overreach is in the Discussion's alignment framing paragraph and in the author's vision brief, not in the paper's stated contributions. The paper's four stated contributions are all delivered. The cornerstone question is about the vision, not the paper. A paper can be well-aligned internally while being insufficient for a larger program. These are separable verdicts and I think Reviewer F conflates them.

---

## Revisions to My Review

**What I missed:**

**1. The differentiation funnel's alternative explanation (Reviewer F's Logical Gap 3).** This is a genuine alignment issue I failed to catch. The paper promises to deliver evidence about how the model handles vague language near operational boundaries. But the convergence finding at high baselines may be partially or fully explained by the constraint geometry of the environment rather than by the model's linguistic behavior. The paper does not acknowledge this alternative. This belongs in my Scope Drift Analysis: the paper frames the convergence as a finding about language interpretation when it may be a finding about the environment's design. I would add this to my Missing Sections as: "An acknowledgment that boundary convergence may reflect constraint geometry rather than linguistic behavior — the paper should distinguish these or acknowledge it cannot."

**2. The internal inconsistency between Discussion and Future Work on the hedge interpretation.** I noted this in Missing Sections as "soften hedge language," but I should have named it explicitly as an internal alignment failure: two sections of the paper make contradictory epistemic claims about the same finding. This is the clearest instance of the paper not doing what it says — the Discussion presents the hedge as an established finding while Future Work correctly treats it as a hypothesis. I would elevate this from a structural recommendation to a Stated Goals vs. Delivered Content flag.

**3. The abstention text responses as missing content.** I noted the boundary behavior finding is underanalyzed, but I didn't identify the specific missing content: the model's actual text outputs during abstention are data the paper has collected but not reported. For a paper that claims to document "word-dependent abstention," the absence of any example of what the model says when it abstains is a gap between the claim ("the model produces a text response acknowledging the request but declines to invoke the allocation tool, typically citing the constraint") and the evidence (no examples shown). "Typically" is doing work that should be done by data.

**What I stand by:**

My core finding — that the paper delivers on all four stated contributions and three research questions — stands. The alignment failures I identified (inversion finding absent from abstract, hedge language inconsistency, three-failure synthesis missing from conclusion) remain the highest-priority structural fixes. The differentiation funnel alternative explanation is an addition, not a replacement.

---

## Blind Spots

These are points absent from all six reviews that fall within my alignment mandate:

**1. The paper's title promises a comparison ("Does Slightly Mean Somewhat?") that the paper never directly makes.**

The title frames the paper as a comparison between two specific words. The paper's findings address this implicitly — both map to 0.50 — but the paper never presents a direct "slightly vs. somewhat" comparison as a named finding. The title sets up an expectation the paper satisfies only incidentally. No reviewer flagged this. The title is accurate in spirit but creates a specific expectation (a pairwise comparison) that the paper's structure doesn't deliver. A reader who comes to the paper expecting a focused slightly-vs-somewhat analysis will find a broader study. This is a minor but real abstract-to-content misalignment.

**2. The three research questions in the introduction are answered in a different order than they are asked.**

The introduction lists: (1) ordinal ranking, (2) word vs. state variance, (3) near-limit behavior. The results sections deliver: 4.1 ordinal ranking ✓, 4.2 word vs. state ✓, 4.3 boundary behavior ✓. This is fine. But the conclusion reverses the emphasis: it leads with state dominance, then compression, then boundary behavior. The introduction's framing sets up boundary behavior as the third, least-prominent question; the conclusion and the author's own framing brief treat it as the most important finding. No reviewer flagged this ordering inconsistency. It's a structural alignment issue: the paper's introduction undersells its most important finding by placing it third, and the conclusion doesn't correct this by reordering the emphasis.

**3. The "ongoing study" framing in the conclusion creates an alignment problem the paper doesn't resolve.**

The conclusion states: "This is a preprint documenting the first slice of an ongoing study." This framing implies the paper's claims are provisional pending future slices. But the abstract and introduction make no such qualification — they present the findings as complete contributions. A reader who

---

## Methodology

This report was generated by the AI Research Council using 3 stages (Independent Review → Deliberation → Synthesis).

**Reviewer models:** claude-sonnet-4-6
**Chairman model:** claude-opus-4-8
**Total cost:** $4.72
