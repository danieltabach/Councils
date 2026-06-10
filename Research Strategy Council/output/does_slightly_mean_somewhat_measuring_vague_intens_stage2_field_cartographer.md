# Field Cartographer — stage2

Now I have everything I need to deliver a fully grounded, updated Field Cartographer review. Let me synthesize.

---

# Field Cartographer's Council Response
## Advisor E — Revised Position After Full Deliberation

---

## AGREEMENTS

**Advisor A — The boundary behavior finding is the headline.** I agree completely. Advisor A's framing that the hedge/act/abstain discontinuity is "the finding" while compression is "the context" is the most important reordering any advisor made. My original review said the same thing but did not state it as forcefully. The three-mode boundary behavior — particularly the *drastically* vs. *dramatically* divergence at 89% — is the only result in this paper that would make a safety researcher sit up. Everything else is measurement scaffolding.

**Advisor A — The ground truth problem is the single biggest weakness.** I flagged this in my original review but Advisor A names it more precisely: the ordinal anomaly with "moderately" could mean the model is wrong *or* that the tier assignment was wrong. Without a human baseline, you cannot distinguish these. This is a threat to the core claim, not just a limitation.

**Advisor B — The framing "AI Safety and Alignment" will misfire.** Advisor B is correct that this label means something specific in the alignment community (deceptive alignment, reward hacking, corrigibility) and your paper doesn't touch those. I agree with the reframe toward "agentic tool-use reliability." This is more precise and more defensible.

**Advisor C — The state-dominance finding is partly a design artifact.** This is the most important adversarial point in the entire council. Including an 89% ceiling condition mechanically forces convergence. The ε² ratio of 10:1 is real, but its magnitude is inflated by the experimental design. I did not flag this clearly enough in my original review. Advisor C is right.

**Advisor D — The no-word control is the cheapest, highest-value experiment not yet done.** I mentioned this in my original review but Advisor D makes the point more actionably: without a baseline of "increase innovation" (no intensity modifier), you cannot distinguish "the model hedges at 0.50 because weak words mean 0.50" from "the model defaults to 0.50 for any increase instruction." This costs almost nothing and closes a major interpretive hole.

**Advisor F — The co-authorship gap is the biggest structural problem for career goals.** Advisor F is correct that solo ArXiv papers, even at workshop venues, are insufficient to get to a frontier lab. One co-authored paper with a known researcher is worth more than three solo preprints. I did not address this at all in my original review. It belongs in the field map.

---

## DISAGREEMENTS

**Advisor B on the OpenAI Safety Fellowship.** Advisor B's review was cut off mid-sentence while describing this fellowship. I want to flag this as a gap in that review — the fellowship details were incomplete and Daniel should not rely on that section for planning.

**Advisor C on NeurIPS being the wrong target.** Advisor C argues that NeurIPS is "the most competitive venue and the least aligned with your topic" and recommends EMNLP, ACL workshops, or FAccT instead. I partially disagree. The framing matters more than the venue brand. The NeurIPS 2026 suggested submission date for workshop contributions is August 29, 2026, with mandatory accept/reject notification by September 29, 2026. This is a real, achievable target. More importantly, the agentic tool-use reliability framing fits NeurIPS's current appetite — the field has moved heavily toward agents and deployment reliability. The question is not "is NeurIPS the right venue for linguistics work?" (it isn't) but "is NeurIPS the right venue for agentic systems reliability work?" (it is). The framing determines the fit, not the topic label.

**Advisor D on using existing psycholinguistic data as a human baseline proxy.** Advisor D recommends anchoring to Vogel et al. (2022) and Cliff (1959) as a substitute for original human data. I flagged this same path in my original review, and I still think it is the right move — but I want to be more precise about its limits. To ground linguistic hedges in established human interpretations, researchers have adopted the verbal-numerical probability correspondences summarised in the meta-analysis by Vogel et al. (2022), showing averaged mean values and 95% confidence intervals for 35 commonly used expressions arranged approximately linearly from "impossible" to "definite." The critical limitation: Vogel et al. covers *probability* hedges ("likely," "probably"), not *intensity action modifiers* ("slightly increase," "drastically raise"). The overlap is partial at best. A reviewer will correctly note this. You can use it as a reference for ordinal structure, but you cannot use it as a direct human baseline for your specific words in your specific action context. Frame it as "external validation of ordinal structure" not "human comparison."

**Advisor F on mechanistic interpretability being a distraction.** I agree it is not the right primary direction for Daniel right now, but I want to add a more precise reason than "it requires skills you don't have." The deeper problem is that mech interp on Claude Haiku is impossible — you do not have access to model weights. LLMs rely entirely on the text descriptions of tools to decide which ones to use — a process that is surprisingly fragile. Any mech interp work would require switching to open-source models, which changes your experimental setup and introduces a confound. If you want to go this direction, you must first replicate your core findings on an open-source model, then do the interpretability work on that model. That is a two-step project, not a bolt-on extension.

---

## REVISIONS TO MY ORIGINAL REVIEW

**What I missed: The "Tool Preferences in Agentic LLMs are Unreliable" paper (arXiv 2505.18135) is a near-neighbor you must engage with.** LLMs rely entirely on the text descriptions of tools to decide which ones to use — a process that is surprisingly fragile. Through controlled experiments, tools with properly edited descriptions receive over 10 times more usage from GPT-4.1 and Qwen2.5-7B than tools with original descriptions. This paper studies how *tool description wording* affects tool selection. Your paper studies how *instruction intensity wording* affects tool parameter values. These are adjacent but distinct: they study which tool gets called; you study what numeric argument the tool receives. You need to cite this paper and explicitly position against it. The delta is: they study tool selection sensitivity; you study numeric argument sensitivity. Both are about language-to-action reliability in agentic systems, but at different points in the pipeline.

**What I missed: The IRB PI requirement at Georgia Tech is a harder constraint than I stated.** My original review said you could submit as PI on an exempt study. This was imprecise. Students may not be PIs on protocols and should be listed based on their role as either co-investigators, study staff, or student. Only faculty can be listed as PI and Co-PI. This means you genuinely need a faculty PI to submit any IRB protocol at Georgia Tech, including exempt determinations. This is a real obstacle for an online OMSA student without a known advisor. The path through Algoverse (finding an affiliated faculty member to serve as PI) is your most realistic route if you want the human baseline. My original recommendation stands — avoid IRB for the current paper — but I was wrong to suggest the exempt route was straightforward for you specifically.

**What I understated: The venue landscape for this paper.** I identified EMNLP as the best fit but did not name specific workshops. Now I can be precise. The LUHME 2026 workshop on Language Understanding in the Human-Machine Era at EMNLP 2026 covers AI-mediated communication in high-stakes domains (law, health, finance, governance), effects and risks of language misunderstanding, and human vs. machine language understanding. This is a direct fit for your work — "effects and risks of language misunderstanding" and "AI-mediated communication in high-stakes domains" map exactly to your findings. The third UncertaiNLP workshop at EMNLP