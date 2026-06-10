# Devil's Advocate — stage1

# Devil's Advocate Strategic Review: Daniel Tabach

---

## LEAD CHALLENGE: What You Actually Have vs. What You Think You Have

Before addressing your specific questions, I need to name the central problem with your current strategic position, because everything else flows from it.

You have documented **one model's prompt-response behavior in one synthetic domain at one point in time.** The findings — compression, state dominance, boundary abstention — are real. They're clean. The paper is competent. But you are at risk of mistaking a measurement artifact for a generalizable phenomenon, and building a research program on top of that mistake.

Here is the adversarial reading of your strongest findings:

**Finding 1 (compression):** You showed that Claude Haiku maps 10 words to 5 numeric outputs in a constrained allocation task. The alternative explanation is trivial: the model was trained on enormous amounts of text where "slightly," "marginally," "somewhat," and "mildly" co-occur in nearly identical contexts and carry nearly identical pragmatic force. Of course it collapses them. This is not a discovery about LLM action interfaces — it may be a rediscovery of well-documented near-synonymy in English. The linguistics literature on hedges and approximators (Lakoff 1973, Hyland 1998) already knows these words cluster. You've confirmed a model trained on that corpus reflects that clustering. That's not nothing, but it's much smaller than "vague instructions don't map to stable numeric actions."

**Finding 2 (state dominance):** Context dominates word choice when you give the model explicit numeric context. This is… expected? If I tell you "the allocation is currently 89%, please slightly increase it," any rational agent — human or model — will be constrained by that ceiling. The ε² ratio of 10:1 is a consequence of your experimental design, not a discovery about language models. You chose to include an 89% ceiling condition, which mechanically forces convergence. Remove that condition and your ratio changes substantially. A reviewer at a serious venue will make this argument.

**Finding 3 (boundary abstention):** This is your genuinely interesting finding. The three-mode behavior (hedge/act/abstain) that is word-dependent at the same system state — this is not obvious. This is the thing worth building on.

The danger is that you're treating all three findings as equally strong when they have very different levels of novelty. Your research strategy should be built around Finding 3, not Finding 1 or 2.

---

## SECTION 1: THE NEURIPS WORKSHOP QUESTION

**Can you get a workshop paper ready by August for NeurIPS?**

Let me be honest about the math here. NeurIPS 2025 workshops have submission deadlines typically in August-September. You're writing in mid-2026 based on your paper date, so you're likely targeting NeurIPS 2026 workshops, with deadlines probably in July-September 2026.

**The adversarial case against your current path to NeurIPS:**

Your paper as it stands has the following profile when reviewed by a NeurIPS workshop PC member:
- Single model (Claude Haiku — a *small* model, not frontier)
- Single domain (synthetic allocation)
- No human baseline
- No cross-model comparison
- Researcher-constructed word scale, not validated
- 30 runs per cell (defensible but thin)
- Statistical approach that the paper itself acknowledges overstates significance

A workshop reviewer will ask: *Is this a finding about LLMs, or a finding about Claude Haiku's RLHF training specifically?* You cannot answer that question. That's a fatal gap for a workshop that attracts serious researchers.

**What would change my mind:** If you run the same protocol on 3-4 models (including at least one open-source model you can run locally) and find that the compression pattern and three-mode boundary behavior are consistent across model families, you have a cross-model finding. That's publishable at a workshop. If the patterns diverge across models, *that's also publishable* — it tells you something about how different training regimes handle vague language.

**Realistic timeline assessment:** You have a gaming rig with an RTX 3070. You can run Llama 3.1 8B, Mistral 7B, Phi-3, and Gemma 2 9B locally. These are small models, but running your exact protocol on 4 models (including Haiku) gives you a cross-model comparison paper. That's achievable in 2-3 months of nights and weekends. The cross-model extension is your fastest path to a publishable workshop paper, not any of the more exotic directions you're considering.

**The workshop targeting question:** I'd push back on NeurIPS as your primary target. Consider:
- **EMNLP workshops** (particularly the Workshop on Insights from Negative Results in NLP, or workshops on LLM evaluation) — your work fits the evaluation/behavioral framing better than NeurIPS's ML-heavy culture
- **ACL workshops** on human-computer interaction or language grounding
- **FAccT** — your work has a direct connection to reliability and accountability in AI systems
- **AAAI workshops** on human-AI interaction

NeurIPS is the most competitive venue and the least aligned with your topic. Chasing it because of brand recognition is a strategic mistake for someone building a publication record.

---

## SECTION 2: THE IRB QUESTION — DELIBERATED EXTENSIVELY

This is where I'll give you the most direct answer, because you asked for it.

**The core IRB question for your work:** Do you need IRB approval to collect a human baseline?

**The honest answer is: probably not, and here's why.**

IRB review is required for research involving human subjects when the purpose is to generate generalizable knowledge AND the data collection involves interaction with living individuals. The key regulatory framework in the US is the Common Rule (45 CFR 46).

**Path 1: Exempt determination (most likely applicable)**

Under the revised Common Rule (effective 2018), research that involves only surveys/interviews and poses no more than minimal risk, with no sensitive topics, is often **exempt** (Category 2). A survey asking people "if you were allocating resources and wanted to slightly increase something, what percentage would you choose?" is:
- Minimal risk (no sensitive information, no deception, no vulnerable populations)
- Anonymous or easily anonymizable
- Not involving any intervention or manipulation that could harm participants

**At Georgia Tech specifically:** GaTech has an IRB office that processes exempt determinations. The process for an exempt determination is typically 2-4 weeks, not months. You fill out a form, describe your study, and the IRB confirms it's exempt. You don't need a PI to sponsor an exempt determination — graduate students can submit. You *do* need to submit, but you don't need full board review.

**The practical path:** Email GaTech's IRB office (irb@gatech.edu) and describe your study in one paragraph. Ask if it qualifies for exempt determination. This is a 20-minute task. They will tell you. Do not skip this step — publishing a paper that should have had IRB review and didn't is a career-ending mistake, not a minor oversight.

**Path 2: Use existing validated data (avoids IRB entirely)**

Here's the option you haven't considered: **you don't need to run your own human study.** 

The psycholinguistics literature already has data on how humans interpret degree modifiers numerically. Specifically:
- Mosteller & Youtz (1990) on probability words — you cite this
- Budescu & Wallsten (1985, 1995) on vague quantifiers
- Moxey & Sanford (2000) on quantifier interpretation
- More recently, Wallsten et al. have published numeric elicitation data for hedging terms

The problem is these studies used *probability* words ("likely," "probable") not *degree modifiers* ("slightly," "considerably"). But there's a closer match: **Cliff (1959)**, which you also cite, actually collected numeric multiplier data for adverbs including some of your words. His data is in the paper. You can use it as a historical human baseline.

**The adversarial challenge to this path:** A reviewer will correctly note that Cliff's data is from 1959, collected in a different task context (adjective modification, not resource allocation), and may not generalize. This is a real limitation. But it gives you *something* to compare against without IRB, and you can frame it as "historical human calibration" rather than a direct baseline.

**Path 3: Reframe the paper to not need a human baseline**

This is the cleanest option strategically. Your paper's central contribution is **not** "models differ from humans in how they interpret intensity words." Your paper's central contribution is **"LLM action interfaces exhibit compression, state dependence, and boundary mode-switching that creates operational unpredictability."** 

That claim does not require a human baseline. It requires only that you demonstrate the behavior is (a) consistent across models, (b) consequential for real systems, and (c) not fixed by obvious interventions (like changing temperature).

**Reframe the paper:** Drop the implicit human comparison. Make the paper explicitly about *characterizing LLM action interface behavior* rather than *comparing LLM behavior to human norms*. The human baseline becomes future work (which you already have in the paper), not a current gap. This reframe makes IRB irrelevant to the current paper.

**My recommendation:** Do Path 3 for the current paper (reframe, remove implicit human comparison framing), simultaneously submit an exempt determination request to GaTech IRB for a simple survey, and if you get exempt status, run a cheap Prolific study (Prolific.ac, ~$100 for 50-100 participants on a simple survey) for the follow-up paper. Prolific is far cheaper than you think — a 5-minute survey at $12/hour pays ~$1/participant, so 100 participants costs $100-150 including Prolific's fee. That's within your budget.

**What would make IRB unavoidable:** If you want to make the claim "LLMs interpret these words differently from humans" as a central finding, you need a human baseline, and you need IRB. There's no way around this. But you can choose not to make that claim.

---

## SECTION 3: THE RESEARCH DIRECTION QUESTION

You asked where to go next. I'll evaluate each direction you mentioned adversarially.

### Direction A: Cross-model comparison
**My assessment: Do this first. It's your highest-ROI next step.**

Not because it's the most intellectually interesting, but because it's the fastest path to a defensible paper. Without cross-model comparison, every finding you have is "Claude Haiku did this." That's a product evaluation, not research.

**The adversarial case against this direction:** Cross-model comparisons are often shallow. "GPT-4o compresses words differently than Haiku" is a finding, but it doesn't explain *why*, and it doesn't tell you what to do about it. You risk producing a paper that is descriptively richer but not analytically deeper.

**What would make it strong:** Don't just compare compression patterns. Test whether the three-mode boundary behavior (hedge/act/abstain) is universal or model-specific. If it's universal, you have a finding about LLM action interfaces in general. If it's model-specific, you have a finding about training procedures.

**Compute budget:** Your RTX 3070 can run 7-8B parameter models in 4-bit quantization. Llama 3.1 8B, Mistral 7B Instruct, Phi-3 Mini, Gemma 2 9B — all runnable locally. This costs you electricity, not money. For GPT-4o and Gemini Flash, use their APIs sparingly — run only the no-context condition and the 89% boundary condition to minimize cost. That's 60 runs × 2 conditions × 2 models = 240 API calls, probably under $5.

### Direction B: Mechanistic interpretability
**My assessment: Don't pursue this as your primary direction.**

I'll be direct: mech interp is a specialized subfield with its own community, tools, and norms. Doing it well requires deep familiarity with activation patching, attention head analysis, and circuit-level analysis. Doing it poorly produces papers that the mech interp community dismisses as "we already knew this" or "this doesn't actually tell us about the mechanism."

More importantly, mech interp on closed models (Claude Haiku) is impossible — you don't have weights. You'd need to run on open models, which changes your experimental setup. And the question "why does the model map 'slightly' and 'marginally' to the same value" has a boring mech interp answer: their token embeddings are close in the representation space, and the instruction-following fine-tuning didn't separate them. You'd spend 3 months confirming something that a 10-minute embedding similarity analysis would suggest.

**What would change my mind:** If you found that the three-mode boundary behavior (hedge/act/abstain) has a mechanistic signature — specific attention heads or circuits that activate differently for "drastically" vs. "considerably" at high baseline states — that would be genuinely interesting. But this requires expertise you don't currently have, and it's a 6-12 month project minimum.

### Direction C: Valence/stakes manipulation
**My assessment: This is your most interesting idea, but it's a different paper.**

"Does the same allocation problem change in higher stakes?" — ICU beds vs. factory robots vs. branch staffing — is actually a fascinating question. It touches on something real: do LLMs apply different interpretive norms when the stakes of the action are higher? Do they become more conservative? Do they abstain more?

This is adjacent to work on LLM risk sensitivity and moral reasoning under uncertainty. It connects to AI safety in a more direct way than your current paper.

**The adversarial case:** This is a much harder experiment to design cleanly. You need to control for domain familiarity (the model knows more about hospitals than about abstract allocation), emotional valence (ICU beds carry emotional weight that branch staffing doesn't), and the specificity of the constraint (medical resource allocation has real-world norms the model may have learned). Confounds multiply.

**The steelman for this direction:** If you find that the three-mode behavior (hedge/act/abstain) is *amplified* in high-stakes domains — that models abstain more when the stakes are higher — that's a safety-relevant finding. It suggests models have some implicit risk-sensitivity in their action policies. That's publishable at an AI safety venue.

**My recommendation:** File this idea. Don't pursue it now. Finish the cross-model comparison first.

### Direction D: Stakeholder identity manipulation
**My assessment: Interesting but methodologically treacherous.**

"The stakeholder is an analyst" vs. "The stakeholder is a decision maker launching across 4,000 locations" — does this change model behavior? This is actually a question about LLM sycophancy and authority sensitivity, which is a studied phenomenon (Perez et al. 2022, Sharma et al. 2023 on sycophancy). You'd be adding to an existing literature rather than opening a new one.

**The adversarial case:** This direction is well-trodden. Sycophancy in LLMs is documented. Authority-sensitivity is documented. You'd need a very clean experimental design to say something new here, and your allocation framework may not be the right vehicle for it.

### Direction E: Fine-tuning for ordinality
**My assessment: Way out of scope for your resources.**

Fine-tuning to create inherent ordinality in intensity word interpretation requires: a human baseline (IRB), a training dataset, compute for fine-tuning (your 3070 can fine-tune small models but not frontier models), and evaluation methodology. This is a 12-18 month project. Don't touch it now.

---

## SECTION 4: THE FRAMING QUESTION

You're uncertain whether this is AI Safety, Alignment, or Human-AI Interaction. Here's the adversarial take on each framing:

**AI Safety framing:** Your work is relevant to safety in the narrow sense that unpredictable LLM action interfaces create operational risk. But "safety" in the AI safety community means something more specific — it's about catastrophic risk, value alignment, corrigibility, deceptive alignment. Your paper doesn't touch these. Framing it as "AI safety" will get you dismissed by the safety community as not engaging with the real safety problems, and it will confuse reviewers who expect safety-relevant threat models.

**Alignment framing:** Closer, but still not quite right. Alignment is about whether models pursue intended goals. Your paper is about whether models *interpret instructions correctly*, which is a precondition for alignment but not alignment itself. The framing "alignment of vague instructions with numeric actions" works, but it's a stretch.

**Human-AI Interaction (HCI) framing:** This is your strongest framing, and I'd argue you should lean into it. Your paper is fundamentally about the usability and reliability of natural language interfaces to computational systems. The HCI community (CHI, CSCW, IUI) cares deeply about this. Your production motivation — stakeholders trying to interact with optimization systems — is exactly the kind of real-world deployment context HCI researchers value.

**The reframe I'd suggest:** Stop calling this "AI Safety and Alignment." Call it **"Reliability of Natural Language Interfaces to Agentic Systems"** or **"Prompt Semantics in LLM Tool-Use."**