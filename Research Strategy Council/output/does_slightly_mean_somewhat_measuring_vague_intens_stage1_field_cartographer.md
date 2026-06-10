# Field Cartographer — stage1

I now have sufficient research to provide a thorough strategic review. Let me synthesize everything into a comprehensive field map.

---

# Field Cartographer's Strategic Review
## Daniel Tabach | "Does Slightly Mean Somewhat?" | June 2026

---

## SECTION 1: WHERE YOUR WORK ACTUALLY SITS — THE PRECISE MAP

Let me draw the borders clearly, because you're currently standing at the intersection of four research territories and you need to know exactly which one to plant your flag in.

**Territory 1: Prompt Sensitivity / LLM Robustness**
The closest existing work to yours is the prompt sensitivity literature. An interesting behavior in LLMs is prompt sensitivity — when provided with different but semantically equivalent versions of the same prompt, models may produce very different distributions of answers, suggesting that the uncertainty reflected in a model's output for one prompt may not reflect the model's uncertainty about the meaning of the prompt. Key papers here include BrittleBench (Romanou et al., 2026, which you already cite), Errica et al. (2025) "What Did I Do Wrong?", and ProSA (Zhuo et al., 2024). Empirical studies show that non-semantic prompt features, such as formatting, punctuation, or lexical substitutions, can induce large changes in model behavior, including discrete output flips and substantial performance degradation.

**The critical delta:** All of that work studies *semantically equivalent* paraphrases producing different outputs — it's about robustness to noise. Your paper studies *semantically distinct* intensity words producing outputs that should differ but sometimes don't. This is the inverse problem. You're measuring expressivity collapse, not robustness failure. That's a genuine distinction and you should lean into it hard.

**Territory 2: Vague Quantifiers / Verbal Probability**
The second closest territory is the vague quantifier and verbal probability literature. Researchers investigate whether LLMs conform to predictions from models of distributional semantics in the domain of quantifiers, finding that LLMs' performance on vague quantifiers is consistently worse than their performance on exact quantifiers. There is also a parallel paper — "Prospect Theory Fails for LLMs" (2025) — that is uncomfortably close to your work. Epistemic markers are inherently vague and context-sensitive, yet they often substitute for precise numerical probabilities in practice. For LLMs, the ability to interpret epistemic markers consistently and meaningfully is critical if they are used as decision-support tools. However, there is little empirical understanding of how LLMs map epistemic markers to numerical probabilities, and whether this mapping is coherent across different models or aligned with human intuition.

**The critical delta:** That paper uses epistemic probability markers ("likely," "certainly") in a *decision* context (lottery choices), not intensity modifiers in an *action* context (tool calls). Your construct is different: you're not asking the model to estimate a probability — you're asking it to *execute an action* with a constrained numeric parameter. The action/estimation distinction is the moat. Defend it explicitly and aggressively in your next paper.

**Territory 3: LLM Number Representation**
There is a growing literature on how LLMs internally represent numbers. Number representations have recently been studied within pretrained language models using techniques from mechanistic interpretability. Zhu et al. (2025) devised a dataset of addition problems to show that LLMs encode the value of numbers linearly in that context. Likewise, circuit analysis has been adopted to characterize how smaller language models compute "greater than" and basic arithmetic operations. Your round-number anchoring finding (outputs cluster at round values when baselines are round) connects directly to this literature. The training paradigm encourages LLMs to prioritize surface-level statistical patterns rather than numerically grounded reasoning, and LLMs treat numbers as discrete tokens rather than continuous magnitudes, inherently limiting their ability to understand exact numerical semantics. This is a strong mechanistic hook you're not yet exploiting.

**Territory 4: Human-AI Interaction / Agentic Systems Safety**
This is where you *want* to be positioned, and it's where the work is most consequential. Although current AI technologies can incorporate human feedback, they are not inherently designed to optimize the overall efficiency of socio-technical systems composed of technical artifacts, human beings, institutions, and rules, implying that current applications of AI cannot fully leverage human-AI interaction, calling for new advancements in scientific research. Your paper's practical contribution — that vague language in natural-language control interfaces is unreliable — fits squarely here.

---

## SECTION 2: NOVELTY ASSESSMENT — HONEST ACCOUNTING

**What is genuinely new:**
1. The *action boundary* framing. Prior work measures probability estimation or quantifier judgment. You measure what happens when vague language must produce a constrained tool-call parameter. This is a different and underexplored construct.
2. The three-mode boundary behavior (hedge/act/abstain) is your most original finding. No paper I can find has documented this specific categorical switching near feasibility limits, and it has direct safety implications.
3. The state-dominance finding (ε²_baseline = 0.782 vs. ε²_word = 0.079) is a clean, quantified result. The 10:1 ratio is memorable and citable.
4. The round-number anchoring observation is preliminary but genuinely interesting — it connects to the number-as-token literature in a novel way.

**What is expected / needs stronger positioning:**
The compression finding (10 words → 5 clusters) is the most expected result. Any reviewer familiar with the verbal probability literature will not be surprised that LLMs compress fine-grained lexical distinctions. The ordinal anomaly with "moderately" is interesting but needs a mechanistic story. The temperature robustness finding is confirmatory, not novel.

**The core risk:** Your paper is currently a *measurement* paper without a *mechanism* paper to follow it. Measurement papers are publishable, but they're more compelling when they point toward a mechanism. Your mechanistic speculation section is good but it's speculation. The round-number anchoring and the hedge/act/abstain switching are the two findings most likely to lead somewhere mechanistically interesting.

---

## SECTION 3: FRAMING ASSESSMENT

**Current framing: AI Safety and Alignment**
This framing is *partially correct* but *too broad* for the work you've done. "AI Safety" as a label at NeurIPS or ACL will put you in competition with alignment papers about value learning, RLHF, and constitutional AI. Your paper is not about those things. You will be reviewed by people expecting something different.

**Better framing: "Language-to-Action Fidelity in Agentic Systems"**
This is your actual contribution. The question is not "is this AI safe?" but "when a human uses natural language to steer an AI agent, does the agent's action faithfully represent the human's intent?" This is a *specification* problem, not a value-alignment problem. It sits at the intersection of:
- LLM evaluation (does the model do what the prompt says?)
- Human-computer interaction (does the interface express what the user means?)
- Agentic systems reliability (can you trust the agent's interpretation of vague instructions?)

This framing is more precise, more defensible, and more likely to land with reviewers at NeurIPS workshops, EMNLP, or CHI.

**Alternative framing: "Semantic Grounding Failure in Tool-Use Agents"**
If you go the NLP route (EMNLP, ACL), this framing connects to the grounding literature. The claim becomes: intensity adverbs are not reliably grounded in numeric action space, and the grounding is state-dependent. EMNLP 2026 explicitly welcomes work going beyond static leaderboards, including real-world impact, trustworthiness, robustness, and longitudinal behavior; and asks how system-level research on agentic workflows, tool use, and multi-model orchestration interfaces with human experiences. This is a direct fit.

---

## SECTION 4: THE IRB QUESTION — DELIBERATED EXTENSIVELY

This is the most important strategic question in your brief, so I'm giving it the most space. Here is the honest map of your options, from most to least attractive.

### Option A: Avoid IRB Entirely — Reframe the Human Baseline as a Model Comparison Study (RECOMMENDED FIRST)

The cleanest path is to reframe what the "human baseline" actually needs to accomplish. Ask yourself: *what scientific question does a human baseline answer?* It answers: "Does the model's compression of intensity words reflect genuine ambiguity in human language, or is it a model-specific failure?"

You can answer this question without collecting new human data. Here's how:

**Use existing published psycholinguistic data.** Cliff (1959), Mosteller & Youtz (1990), and the Vogel et al. (2022) meta-analysis (which compiled numeric mappings for 35 verbal expressions) already provide human numeric interpretations of hedging and intensity language. To ground linguistic hedges in established human interpretations, researchers have adopted the verbal-numerical probability correspondences summarised in the meta-analysis by Vogel et al. (2022), showing averaged mean values and 95% confidence intervals for 35 commonly used expressions arranged approximately linearly from "impossible" to "definite." You can compare your model's output ordering against the human ordering documented in these papers — no new data collection required, no IRB.

This is a legitimate scientific move. If the Vogel et al. ordering matches your model's tier ordering for overlapping words, you have evidence that the model's coarse compression reflects real human ambiguity. If it doesn't, you have evidence of model-specific distortion. Either result is publishable.

**The limitation you must acknowledge:** Vogel et al. covers probability hedges, not intensity action modifiers. The overlap is partial. But this limitation is manageable — you frame it as a cross-domain comparison and note that a direct action-domain human study is future work.

### Option B: Use Multi-LLM Comparison as a Partial Proxy

Research comparing LLMs with human judgements finds that LLMs' performance on vague quantifiers is consistently worse than their performance on exact quantifiers. If you run your protocol on 4-5 models and find that compression patterns differ across models (e.g., GPT-4o shows less compression than Haiku, Llama-3 shows different tier boundaries), this is itself evidence that the behavior is not a fixed property of language — it's model-specific. This doesn't replace a human baseline, but it reframes the paper from "model vs. human" to "model behavior characterization," which is a defensible scope for a workshop paper.

### Option C: The IRB Exempt Route — If You Must Go This Way

If a reviewer or venue specifically demands a human comparison, here is the least painful path. Your survey would be a simple online questionnaire: "Given the task of increasing a parameter, what numeric value (0-100) would you assign to each of these 10 instructions?" No deception, no sensitive data, no risk to participants.

Research that only includes interactions involving educational tests, survey procedures, interview procedures, or observation of public behavior qualifies for exemption if the information obtained is recorded such that the identity of human subjects cannot readily be ascertained, and any disclosure of responses would not place subjects at risk of criminal or civil liability or be damaging to subjects' financial standing, employability, or reputation. This is Exempt Category 2 under the Common Rule. Your survey would almost certainly qualify.

**The Georgia Tech-specific complication:** At Georgia Tech, Principal Investigators and Co-Principal Investigators must be members of the GT faculty. Students may not be PIs on protocols and should be listed as co-investigators, study staff, or students. This means you *need a faculty PI*. As an online OMSA student without a known advisor, this is a real obstacle. However:

- Algoverse may have affiliated faculty who can serve as PI. Ask them directly.
- Georgia Tech OMSA has faculty advisors for capstone projects. Email your program coordinator and explain you need a faculty PI for an exempt IRB submission.
- The revised 2018 Common Rule broadens the types of research that may be determined to be exempt from IRB review. Starting January 21, 2019, benign behavioral interventions conducted with adults may be determined to be exempt. The process for exempt review is lighter than full review.

**Cost estimate for the human study:** A 5-minute survey on Prolific for 100 participants. Prolific's platform fee is 33.3% for academic or non-profit customers, and they recommend paying participants at least $12.00 per hour. At $12/hour for 5 minutes = $1/participant + 33% fee = ~$1.33/participant × 100 participants = **~$133 total**. This is within your $200 budget. The survey itself can be built free on Google Forms or Qualtrics (free tier).

### Option D: Use Other LLMs as "Silicon Respondents" — The Riskiest Option

There is a growing literature on using LLMs as synthetic survey respondents. Recent work has treated LLM-as-respondent as a low-cost proxy for real human sampling in surveys and lab studies. Argyle et al. (2023) simulate demographic subpopulations by conditioning GPT-3 on rich backstories and compare the resulting LLM-generated silicon samples to human survey distributions. However, sampling by ChatGPT is not reliable for statistical inference: there is less variation in responses than in real surveys, and regression coefficients often differ significantly from equivalent estimates. The distribution of synthetic responses varies with minor changes in prompt wording, and the same prompt yields significantly different results over a 3-month period.

**My recommendation: Do not use this approach as a human baseline substitute.** It will invite reviewer criticism that you're using one LLM to validate another. It's circular. Use it only as an additional model comparison, not as a human proxy.

### My Verdict on IRB

**Do Option A first.** Reframe the human baseline gap as a comparison against Vogel et al. (2022) and Cliff (1959) for the current paper. Add a cross-model comparison (Option B). If a reviewer demands more, note that a direct human survey is planned future work. For a workshop paper, this is sufficient. If you want to publish a full journal paper later, do Option C with a faculty PI from Algoverse.

---

## SECTION 5: WHERE TO PUBLISH — SPECIFIC TARGETS FOR AUGUST 2026

NeurIPS 2025 has already passed. NeurIPS 2025 had a paper submission deadline of May 15, 2025, with the conference running November 30 – December 7, 2025. You are targeting **NeurIPS 2026**, which will be held in Vancouver in December 2026. Workshop submission deadlines for NeurIPS 2026 workshops typically fall in **August–September 2026** — you are on track.

**Tier 1 Target: NeurIPS 2026 Workshop**
Look specifically for workshops on:
- Human-AI Interaction (the MTI-LLM workshop at NeurIPS 2025 covered multi-turn RL for agentic tasks, maintaining alignment over extended interactions, and human-AI interaction ensuring models adapt to user goals without compromising safety or fairness — a direct fit for your work)
- Trustworthy ML / Robustness
- Language Grounding and Agents

**Tier 2 Target: EMNLP 2026 (October 24-29, Budapest)**
EMNLP 2026 will be held as a hybrid conference in Budapest, Hungary from October 24-29, 2026. This is actually your *best* venue for a strengthened version of this paper. EMNLP 2026 explicitly asks how system-level research on agentic workflows, tool use, and multi-model orchestration interfaces with human experiences,