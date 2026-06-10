# Research Sequencer — stage1

# Strategic Review: Daniel Tabach — Research Sequencing Council

---

## SITUATION ASSESSMENT

You have something real. The paper establishes a measurement framework, produces three distinct empirical patterns, and is already on ArXiv. That's your foundation. The honest assessment: as a standalone result it's a credibility-builder, not a claim-staker. One model, one domain, no human baseline, no cross-model comparison. Reviewers will say exactly that. Your job now is to use this paper as *the first brick* — it establishes the measurement apparatus and the vocabulary (compression, state dominance, hedge/act/abstain). Everything you build next should reference it as the originating instrument.

The good news: you don't need to defend this paper. You need to extend it in a direction that makes the next paper land harder.

---

## THE IRB QUESTION — DELIBERATED EXTENSIVELY

This is your most important structural constraint, so I'm addressing it first and in full.

**The core question: do you actually need IRB for your next paper?**

Short answer: probably not, if you reframe correctly. Here's the full reasoning.

IRB review is triggered when you conduct research *involving human subjects* — meaning you are collecting data *from* people (surveys, behavioral studies, interviews, physiological data). The key distinction is whether humans are your *subjects* or your *instruments*.

**Paths that avoid IRB entirely:**

**Path A: Stay purely in the LLM behavioral space.** Your current paper has zero IRB exposure because you studied model behavior, not humans. The cross-model comparison paper, the denser baseline grid paper, the open-source model paper — none of these require IRB. You can publish multiple papers in this lineage without ever touching a human subject. This is the cleanest path given your constraints.

**Path B: Use existing validated human data as your baseline.** Instead of running your own human survey, anchor to *published psycholinguistic data* on degree modifier interpretation. The Mosteller & Youtz (1990) probability word study, the Cliff (1959) adverb multiplier data, and more recent work like Wallsten et al. on verbal probability expressions give you numeric distributions for how humans interpret these words. You can compare your model outputs to *published human distributions* without collecting a single new data point. No IRB. No money. This is actually a stronger scientific move than a small bespoke survey anyway — you're comparing against established literature rather than 50 Prolific participants.

**Path C: Reframe the human comparison as a theoretical claim, not an empirical one.** Instead of "here is how humans interpret these words vs. the model," your claim becomes "here is how the model's compression pattern diverges from the ordinal structure documented in the psycholinguistics literature." You're citing prior work, not generating new human data. This is intellectually honest and sidesteps the entire IRB machinery.

**Path D: If you genuinely want human data, pursue IRB exempt status.** Georgia Tech IRB has an exempt category for research involving "educational tests, survey procedures, interview procedures" where subjects cannot be identified and disclosure would not place them at risk. A simple online survey asking participants to assign numeric values to 10 intensity words in a resource-allocation scenario almost certainly qualifies for exempt status, not full review. Exempt status at GT can be processed in 2-4 weeks, not months. The cost is your time filling out the form, not money. You do not need a PI sponsor for exempt studies at GT — you can submit as the principal investigator on an OMSA thesis-adjacent study. The Algoverse affiliation strengthens your institutional standing here.

**My recommendation: Use Path B as your primary strategy.** Anchor to published psycholinguistics data for the human comparison claim. This is scientifically stronger, costs nothing, requires no IRB, and lets you write "we compare model behavior against established human interpretation norms from Cliff (1959) and Mosteller & Youtz (1990)" rather than "we ran a small survey." If a reviewer pushes for original human data, you can note it as future work — which you already do in the paper.

**What not to do:** Don't let IRB anxiety make you avoid the human comparison framing entirely. The framing "does the model's behavior match human interpretation?" is one of your strongest hooks. You can make that claim using existing literature without collecting new data.

---

## SEQUENCING: THE THREE-PAPER ARC

Given your constraints (part-time, ~$200 budget, RTX 3070, Algoverse compute, no collaborators), here is the optimal sequence. Each paper creates the conditions for the next.

---

### Paper 2: The Cross-Model Replication + Generalization Study
**Target: NeurIPS 2025 workshop or EMNLP 2025 workshop (Human-Centered NLP, or Safety/Alignment tracks)**
**Timeline: Submit August 2025 for NeurIPS workshops**
**Budget: ~$50-80 in API costs + open source models on your rig**

**What this paper does:**
Takes your existing experimental protocol and runs it on 3-4 additional models. This is the paper that transforms your result from "one model's quirk" to "a behavioral pattern across language models." That's the leap from interesting observation to publishable finding.

**Model selection strategy (given your budget):**
- GPT-4o-mini (cheap, widely cited, ~$10-15 for your protocol)
- Gemini Flash (cheap Google model, different training lineage)
- Llama 3.1 8B or Mistral 7B on your RTX 3070 (free, open weights, lets you do more runs)
- Optionally: one larger open model on Algoverse compute (Llama 3.1 70B via quantization)

**Do NOT spend credits on GPT-4o full or Claude Sonnet for the bulk runs.** Use the cheap frontier models for comparability and open models for depth. Reserve your Anthropic credits for targeted follow-up experiments.

**The central claim this paper can make:**
Compression is not a Claude-specific artifact. If you find it in GPT-4o-mini AND Gemini Flash AND Llama, you have a cross-architecture behavioral regularity. That's a publishable finding. If you find differences (e.g., GPT-4o-mini has less compression, or different abstention patterns), that's equally interesting — it becomes a paper about how training and alignment procedures shape vague-language interpretation.

**Add two low-cost extensions from your current setup:**
1. The **no-word control** (you flagged this in your own future work — it costs 10 extra runs per model and sharpens your hedge interpretation)
2. The **decrease direction** (same protocol, "slightly decrease" instead of "slightly increase" — tests asymmetry, adds a full new dimension for minimal cost)

**Anchor to published human data** (Cliff 1959, Mosteller 1990) for the "human comparison" framing. No IRB needed.

**Why this paper first:** It's the highest-leverage move for your NeurIPS August deadline. It reuses your existing codebase, your existing experimental design, and your existing analysis pipeline. You're not building something new — you're running the same machine on different inputs and asking what varies. It's achievable part-time in 3-4 months. And it directly addresses the biggest weakness reviewers will cite in your current paper.

---

### Paper 3: The Context Framing / Stakes Sensitivity Study
**Target: FAccT, CHI, or AAAI 2026 workshop**
**Timeline: 6-12 months after Paper 2**
**Budget: ~$50-100 in API costs**

**What this paper does:**
This is where your valence and stakes ideas become a focused study. The central question: *does the semantic domain of the allocation task change the model's intensity word interpretation?*

Your instinct about "ICU beds vs. factory robots vs. innovation hours" is the right instinct, but you need to sharpen it into a testable hypothesis. Here's the framing I'd recommend:

**The claim:** The model's numeric interpretation of vague intensity words is not domain-neutral. High-stakes or morally-weighted contexts shift the compression pattern, the hedge point, and the abstention threshold.

**The design:**
- Keep your 10-word scale and baseline grid
- Vary the *domain framing* of the allocation task across 4-5 conditions:
  - Neutral (your current "innovation hours" framing)
  - High-stakes human welfare (ICU bed allocation, emergency resource distribution)
  - Financial/economic (budget allocation, investment weighting)
  - Self-referential (model's own processing allocation — your "targeting itself" idea)
  - Negative-risk framing ("if you fail, [consequence]")
- Run on 2-3 models (open source + one frontier)

**Why this is Paper 3, not Paper 2:**
It requires building a new experimental design, new domain framings, and new analysis. It's more conceptually ambitious. You need the credibility from Paper 2 (cross-model replication) before you make claims about domain sensitivity — otherwise reviewers will say "you haven't even established this is a general phenomenon yet."

**The self-referential condition** ("allocate model thinking capacity") is genuinely novel and has AI safety relevance. I'd include it specifically because it's the condition most likely to produce anomalous behavior that generates attention. But don't lead with it — bury it as one condition among several and let the data speak.

**The stakeholder identity extension** ("the stakeholder is an analyst" vs. "a decision-maker responsible for 4,000 locations") fits here too. It tests whether the model's compression pattern changes with perceived authority or consequence. This is directly relevant to your JPMC background and gives you a production-systems angle that differentiates you from pure NLP researchers.

**IRB situation for Paper 3:** Still no IRB needed. You're studying model behavior across prompt conditions. No humans as subjects.

---

### Paper 4 (Optional / Longer Horizon): The Guardrail Design Paper
**Target: ICLR 2027 or NeurIPS 2026 main track**
**Timeline: 18-24 months out**

This is the paper that stakes a claim rather than just building credibility. Given your findings, the natural question is: *can you design a prompt-level or system-level intervention that restores ordinal faithfulness?*

This is where your MILP/optimization background becomes genuinely differentiating. You're not just an NLP person studying model behavior — you're someone who has built production constraint systems who is asking: "given that vague language produces unstable actions, what's the engineering fix?"

Potential framing: a calibration layer between natural language input and numeric action that uses your compression/state-dependence findings to correct for known distortions. You don't need to fine-tune anything. You could design a prompting strategy or a post-processing normalization scheme.

This paper requires more compute, more time, and possibly collaboration. Don't start it until Papers 2 and 3 are done. But keep it in mind as the destination.

---

## YOUR SINGLE HIGHEST-LEVERAGE MOVE IN THE NEXT 6 MONTHS

**Run the cross-model replication study and submit to a NeurIPS 2025 workshop.**

Here's exactly what to do:

1. **In the next 2 weeks:** Identify which NeurIPS 2025 workshops are relevant. Look specifically for: "Behavioral ML," "Human-Centered AI," "Safety and Alignment," "Evaluation of Language Models," "Socially Responsible Language Modelling." NeurIPS workshop submission deadlines are typically August-September. Confirm the exact dates now.

2. **In the next 4-6 weeks:** Port your experimental harness to run on Llama 3.1 8B locally (your RTX 3070 can handle this with 4-bit quantization via llama.cpp or Ollama — it's free). Run your full protocol. This costs you nothing but time.

3. **In parallel:** Run GPT-4o-mini and Gemini Flash on your existing protocol. Estimated API cost: $30-50 total. Add the no-word control and decrease direction at the same time — marginal cost, significant analytical value.

4. **Weeks 6-10:** Analyze, write. The paper structure is already built — you're adding a cross-model comparison section and updating your claims from "Claude Haiku shows X" to "across N models, we observe X, with variation in Y."

5. **Weeks 10-14:** Submit to target workshop.

The reason this is highest-leverage: NeurIPS workshop acceptance gives you a venue, a community, and a line on your CV that says "NeurIPS workshop" rather than "ArXiv preprint." For your goal of getting to a frontier lab, that's a meaningful signal. Workshop papers also get you into the room — the hallway conversations at NeurIPS are where you meet the people who matter.

---

## EVALUATION OF YOUR EXTENSION IDEAS

Let me go through each one directly.

**Larger number grid:** Low priority as a standalone paper. High value as an addition to Paper 2 at minimal cost. Add a denser sweep (every 5%) for one model only, and use it to formally test the round-number anchoring effect. Don't make this the center of a paper.

**Cross-model comparisons (GPT-4o, Gemini Flash, open source):** This is Paper 2. Do it. It's your highest-leverage next move. Prioritize open-source models for depth (more runs, no cost) and cheap frontier models for comparability (GPT-4o-mini, Gemini Flash, not the expensive versions).

**Valence/stakes study (ICU beds, factory robots, self-referential):** This is Paper 3. Good instinct. Don't do it before Paper 2 — it requires new experimental design and you want the cross-model replication to land first.

**Negative/positive risk framing ("if you fail/succeed"):** Include this as one condition in Paper 3, not a standalone paper. It's an interesting manipulation but not enough on its own.

**Stakeholder identity ("analyst" vs. "decision-maker"):** Include in Paper 3. It's a natural extension of the stakes framing and directly connects to your production background.

**Mechanistic interpretability:** This is a distraction given your resources and goals. Mech interp requires significant ML engineering depth, access to model weights, and specialized tools (TransformerLens, activation patching). It's a different research community with different norms. You said yourself you're not an MLE. Don't let Algoverse colleagues push you toward a direction that doesn't play to your strengths. Your strength is behavioral measurement with production-systems intuition. Stay there.

**Fine-tuning for guardrails:** Too resource-intensive for your current stage. This is Paper 4 territory, minimum. Fine-tuning a model to restore ordinal faithfulness requires training data, compute, and evaluation infrastructure you don't have yet. Don't touch this until you have at least two published papers establishing the phenomenon you're trying to fix.

---

## VENUE STRATEGY

**For Paper 2 (cross-model replication):**
- Primary target: NeurIPS 2025 workshop (Safety/Alignment, Behavioral ML, or Human-Centered AI tracks)
- Backup: EMNLP 2025 workshop (Human-Centered NLP, or Evaluation tracks)
- Do NOT target NeurIPS main track yet. Workshop is the right bar for this stage.
- The workshop venue gets you into the room and onto the program. That matters more than the acceptance rate right now.

**For Paper 3 (stakes/domain sensitivity):**
- Primary target: FAccT 2026 or CHI 2026 (both have strong human-AI interaction tracks and care about deployment safety)
- Backup: AAAI 2026 workshop
- These venues care about production consequences and real-world deployment — your JPMC background is an asset here, not a liability.

**On the "is it technical enough" worry:**
Stop worrying about this. Behavioral measurement papers are a legitimate and important genre. The question isn't "is this technically complex" but "does this tell us something we didn't know before?" Your three findings (compression, state dominance, hedge/act/abstain) are empirically clean and practically consequential. That's enough. The cross-model replication makes it more robust. The stakes study makes it more general. Neither requires new mathematical machinery.

---

## ON YOUR GOAL OF REACHING A FRONTIER LAB

I want to be direct about this because it shapes how you should prioritize.

The path from where you are to OpenAI/Anthropic/DeepMind research roles is not primarily through publications — it's through demonstrated research thinking that someone at those labs can vouch for. Publications help, but a NeurIPS workshop paper won't get you hired at Anthropic directly. What it does is:

1. Give you something concrete to discuss in interviews and applications
2. Signal that you can complete a research project end-to-end
3. Get you into communities where you meet people who can advocate for you

The Algoverse fellowship is actually more valuable than you're treating it. Use it aggressively. Go to every meeting. Ask for feedback from fellows who have connections to frontier labs. Ask directly: "Do you know anyone at Anthropic/OpenAI who works on evaluation or alignment who might be willing to do a 20-minute call?" One warm introduction from someone in the Algoverse network is worth more than three