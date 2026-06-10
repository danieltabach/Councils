# Alignment Insider — stage1

This is a comprehensive brief and I have everything I need. Let me now deliver the full strategic council review.

---

# ALIGNMENT INSIDER COUNCIL REVIEW: DANIEL TABACH

---

## SECTION 1: HOW THE COMMUNITY WILL RECEIVE THIS WORK

**The honest read: this is a legitimate empirical finding wrapped in an undersold framing.**

The three core findings — lexical compression to coarse regimes, state dominance over word choice, and the three-mode boundary policy (hedge/act/abstain) — are genuinely interesting to the right audience. The hedge/act/abstain finding in particular is the kind of clean, surprising behavioral result that gets attention at workshops. The convergence funnel (10:1 ratio of baseline variance to word variance) is a well-documented, well-visualized result.

Here's the reception problem you need to know about: **the alignment and safety community will not receive this as an alignment paper without significant reframing.** The current framing — "vague instructions may not map to stable numeric actions" — sounds like a UX or prompt engineering concern. The community that cares about alignment wants to know: *does this create a failure mode that matters for safety?* You have the seed of that argument (the downstream dollar consequences, the boundary discontinuity), but you haven't made it the spine of the paper.

The **LLM evaluation community** (NeurIPS Datasets & Benchmarks, BIG-bench-style work, the evals crowd at Anthropic/ARC Evals) will find this more immediately legible. They're used to "we ran X prompts, found Y behavioral pattern." Your methodology fits that mold cleanly.

The **HCI / CSCW community** (CHI, CSCW, IUI) would find the operator-facing framing extremely compelling — *how do business users reliably communicate intent to AI systems?* — but you're not in that community yet and their review standards differ.

**The community is hungry for this right now.** Agentic systems and tool-use safety are among the hottest topics in 2025-2026. The specific gap you're studying — what happens when vague human language must become a precise machine action — is real and under-measured. You are not behind the curve. You are approximately at the right moment.

**What will get you dismissed:** The single-model limitation is the reviewers' first objection. They will ask "is this Claude Haiku or is this a real phenomenon?" You need cross-model comparison before a strong venue submission. This is fixable and you know it. The lack of a human baseline is the second objection — but I'll address this in the IRB section with a path around it.

---

## SECTION 2: FRAMING — WHAT TO LEAD WITH AND WHAT TO BURY

**Do not lead with "AI Safety and Alignment."** That label in the alignment community means something specific: deceptive alignment, reward hacking, corrigibility, interpretability of goals. Your paper is about a narrower, more operational problem. If you walk into the alignment track calling this an alignment paper, technically sophisticated reviewers will penalize you for overclaiming.

**The frame that will land hardest** in the current moment is: **"Agentic tool-use reliability and the language-to-action boundary."** This is precise, it's hot, and it maps exactly to what you measured. The safety framing is still there — boundary discontinuities in agentic systems are a real safety concern — but you're not overclaiming.

**Secondary frames that work:**
- *LLM evaluation / behavioral characterization* — for NeurIPS evaluation workshops
- *Human-AI interaction for operational systems* — for CHI/CSCW/IUI
- *Prompt sensitivity in tool-calling agents* — for NLP venues (EMNLP, ACL workshops)

**What to bury:** The optimization/MILP origin story. It's compelling to you personally, but reviewers will see it as domain-specific scaffolding and worry the findings don't generalize. The testbed should be described as "a controlled synthetic allocation environment used as a measurement instrument" — which is exactly how you wrote it in the paper. Keep that framing. Don't let the Chase backstory bleed into the research narrative.

---

## SECTION 3: THE IRB QUESTION — DELIBERATE ANALYSIS

This is the section you asked me to spend the most time on. Here is the full picture.

**The key legal/institutional fact:** IRB review is required for "research involving human subjects" under the Common Rule (45 CFR 46). The critical question is whether your planned human baseline survey constitutes "research involving human subjects" under that definition — and whether it qualifies for **exempt status**, which is fast and cheap.

### Path 1: Avoid the Human Baseline Entirely (Strongest Near-Term Option)

Your paper as currently written is a **pure behavioral study of a language model**. No human subjects are involved. The model is the subject. This requires **zero IRB involvement** whatsoever. You can extend the paper significantly — more models, more domains, more word sets, denser grids — without ever touching IRB. This is the path of least resistance and it is scientifically defensible.

The reframe: instead of framing the missing human baseline as a *limitation*, frame it as a *deliberate design choice* that isolates model behavior from human variability. You're not measuring whether humans agree with these words; you're measuring what the model does with them. That's a complete scientific question on its own. Many published behavioral characterization papers at NeurIPS and EMNLP workshops take exactly this approach.

**The community cost:** You cannot make comparative claims like "the model is worse than humans at this." You can only say "the model compresses these words; whether humans do too is an open question." That is a legitimate limitation, but it is not fatal. Papers at the venues you're targeting routinely make this trade.

### Path 2: Exempt Determination (If You Want the Human Baseline)

If you want to include a human comparison, the good news is that your study design would almost certainly qualify for **IRB Exempt Category 2** under the Common Rule. Exempt Category 2 covers research involving educational tests, survey or interview procedures, or observation of public behavior. Your planned study — asking adults to assign numeric values to vague intensity words in an online survey — fits this category cleanly. Benign behavioral interventions are defined as brief in duration, harmless, painless, not physically invasive, not likely to have a significant adverse lasting impact on the subjects, and examples include having subjects play an online game, solve puzzles, or decide how to allocate a nominal amount of cash. A numeric word-rating task is squarely in this territory.

**The Georgia Tech process:** As a registered student at Georgia Tech (OMSA), you have access to GT's IRB office. Exempt determinations are made by designated staff and IRB members; investigators are not permitted to make their own determinations of exemption. Requests should be submitted in the IRB system, and subject participation or data collection cannot start until investigators have received approval that the research is determined as exempt. The exempt determination process at most universities is significantly faster than full IRB review — often 2-4 weeks rather than months. You are not looking at a full board review. You are looking at a form submission and a staff determination.

**The cost question — it's cheaper than you think.** Prolific recommends paying participants at least $12.00 per hour, with a minimum of $8.00 per hour. The platform fee is 33.3% for academic or non-profit customers. A 5-minute numeric rating survey (10 words, assign a percentage to each) at $1.00 per participant (equivalent to $12/hr) plus 33% fee = ~$1.33 per response. **100 participants = ~$133 total.** That is within your $200 budget. You don't need fancy survey sites. You need a Google Form linked to Prolific, and a GT email to get the academic rate.

**The strategic recommendation on IRB:** Do not do the human baseline for the NeurIPS 2026 workshop submission. The timeline is too tight. Do the exempt determination this fall (September–October 2026), run the Prolific survey in November, and include the human baseline in a **revised extended version** you target for a full-length venue (EMNLP 2026 workshops, or a journal submission) in early 2027. This is the correct sequencing: publish the model-only version now, add the human comparison in the follow-up.

---

## SECTION 4: VENUE STRATEGY — WHERE TO SUBMIT AND WHEN

### Primary Target: NeurIPS 2026 Workshop

The NeurIPS 2026 suggested submission date for workshop contributions is August 29, 2026, with mandatory accept/reject notification by September 29, 2026. The conference runs December 6th through 12th, 2026. This is your primary target. You have approximately 11 weeks from today (June 10) to get a submission-ready paper.

**Specific workshops to target (in priority order):**

1. **NeurIPS 2026 Workshop on Multi-Turn Interactions in LLMs** — This is your best fit. The workshop explicitly addresses multi-turn RL learning for agentic tasks, maintaining alignment over extended interactions, and human-AI interaction ensuring models adapt to user goals without compromising safety. Your paper on language-to-action reliability in tool-using agents fits the "agentic tool use" and "alignment over interactions" themes directly. The 2025 edition accepted 4 or 8-page papers (non-archival, double-blind) with a submission deadline of August 22. Expect the 2026 version to have a similar deadline around August 22–29.

2. **NeurIPS 2026 LLM Evaluation Workshop** — There is a dedicated LLM Evaluation workshop track at NeurIPS. Your paper is fundamentally a behavioral characterization / evaluation paper. This is a natural fit and the bar is slightly more accessible than the main alignment workshops.

3. **NeurIPS 2026 Constrained Optimization for ML Workshop** — A surprising but real fit. This workshop focuses on AI systems deployed in safety-critical domains and the demand to ensure fairness, safety, robustness, and interpretability. Your paper's origin in constrained optimization and its findings about solver-integrated language interfaces could resonate here.

### Secondary Target: EMNLP 2026 Workshops

EMNLP 2026 runs October 22–26 in Budapest, Hungary. The ARR submission deadline was May 25, 2026, with EMNLP commitment deadline August 2, 2026.

**Specific EMNLP workshops:**

- **UncertaiNLP @ EMNLP 2026** — The Third Workshop on Uncertainty-Aware NLP. Your finding that the model collapses 10 words into 5 output regimes is fundamentally a story about how models handle lexical uncertainty in action contexts. This is a direct fit.

- **REALM (Research on Agent Language Models) @ EMNLP 2026** — REALM covers tool use, safety and security, and the challenge of turning promising agent capabilities into dependable systems — agents must become more reliable on long-horizon tasks and interact safely with external environments. Your paper is exactly about reliability at the language-to-action boundary.

### Tertiary Target: ACL 2026 Workshops (Already Happened, But Note for Future)

The EvalEval workshop was in-person at ACL 2026 in San Diego. ACL 2027 will be your next shot at this venue. File this for future planning.

### Realistic Assessment

The strongest student papers at NeurIPS workshops asked specific questions and answered them thoroughly. Papers that tried to tackle broad problems without narrowing to a concrete, testable claim struggled in review, while papers that asked focused questions consistently performed better. Your paper already does this well — the three empirical questions are specific and answered. The gap is cross-model comparison. Add even two open-source models before submission and you substantially close the main reviewer objection.

---

## SECTION 5: THE EXTENSION STRATEGY — WHAT TO BUILD NEXT

You asked what direction has the best ROI. Here is my ranking, with reasoning:

### Tier 1 (Do This): Cross-Model Comparison on Open-Source Models

This is the single highest-ROI extension. Run the exact same protocol on Llama 3.1 (8B and 70B), Mistral, and Qwen2.5 on your RTX 3070. You don't need API credits. The core question — does the compression pattern and three-mode boundary behavior generalize? — is what every reviewer will ask. If it does generalize, you have a finding about how language models in general handle vague intensity words. If it doesn't, you have an equally interesting finding about how training and RLHF procedures shape this behavior differently.

Your RTX 3070 can run 7B-13B models locally via Ollama or llama.cpp. Colab from Algoverse can handle 70B models with quantization. This is a $0 extension.

### Tier 2 (Do This for the Follow-Up Paper): Domain Valence Study

Your idea about varying the stakes context ("This is allocation of ICU beds" vs. "This is allocation of innovation hours") is genuinely interesting and connects directly to safety-relevant deployment scenarios. The alignment community specifically cares about whether models behave differently when the stakes are high. This is the kind of extension that moves the paper from "interesting behavioral observation" to "safety-relevant finding." Design this as a separate study — it's a clean paper on its own.

**Frame it as:** "Does the language-to-action boundary shift under high-stakes framing?" That's a question Anthropic's safety team, DeepMind's safety team, and ARC Evals would find directly relevant.

### Tier 3 (Consider Carefully): Mechanistic Interpretability

Your Algoverse colleagues suggested mech interp. I'll be honest with you about the community dynamics here: mech interp is extremely competitive, dominated by a small number of researchers (Neel Nanda, Chris Olah's group, Anthropic's interp team), and the bar for what counts as a real mech interp finding has risen sharply. Identifying which circuits activate for "drastically" vs. "considerably" is technically interesting, but the field will ask: what does this tell us about the mechanism that we couldn't infer from the behavioral data? That's a hard question to answer.

The mech interp path is valuable for **career positioning** — the Anthropic Fellows Program specifically lists mechanistic interpretability as a priority area — but it requires more technical depth than your current skill set suggests is immediately accessible. If you want to go this direction, I'd recommend starting with Neel Nanda's TransformerLens tutorials on open-source models first, before committing to it as a paper direction.

### Tier 4 (Skip for Now): Fine-Tuning for Ordinality

Your idea about fine-tuning to create guardrails is interesting but requires a human baseline (which you don't have yet) and significant compute. It's a 2027 project, not a 2026 project.

### The Stakeholder Persona Extension

Your idea about varying the stakeholder description ("The stakeholder is an analyst" vs. "the stakeholder is a decision-maker launching across 4,000 locations") is clever and connects to personalization and alignment. This is lightweight to implement — it's just a prompt variation — and could be folded into the current paper as an additional condition. It directly addresses the question of whether the model's action policy is sensitive to the described authority level of the requester, which is a safety-relevant finding about how models weight user context.

---

## SECTION 6: FELLOWSHIP AND CAREER POSITIONING

### Fellowships You Should Know About

**1. OpenAI Safety Fellowship** — This is new and directly relevant to your goals. OpenAI has announced a Safety Fellowship for external researchers, engineers, and practitioners to pursue rigorous, high-impact research on the safety and alignment of advanced AI systems, running from September 14, 2026 through February 5, 2027. They are looking for applicants interested in safety questions that matter for existing and future systems. Priority areas include safety evaluation, ethics, robustness, scalable mitigations, privacy