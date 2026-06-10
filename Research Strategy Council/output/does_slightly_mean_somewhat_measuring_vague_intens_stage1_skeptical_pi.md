# Skeptical PI — stage1

# Skeptical PI Review: Daniel Tabach

---

## What I'd Tell You If You Were Sitting in My Office

Daniel, let me be direct with you. You've done something real here. It's not complete, it's not a landmark paper, but it's real — and I've seen far weaker work from people with far more institutional support. The fact that you built this from scratch, motivated by a genuine production problem, and executed a controlled experiment with coherent methodology puts you ahead of most first-time researchers I see. Now let me tell you where you actually stand and what you should do.

---

## Is the Work What You Think It Is?

**Mostly yes, but you're underselling one thing and overselling another.**

You're underselling the boundary behavior finding. The three-mode abstention result — hedge, act, abstain — where *drastically* and *dramatically* diverge at 89% is genuinely surprising and has real implications for agentic safety. That's not "a glimpse of a finding." That's the finding. A small lexical change flips the model from acting to abstaining in identical constraint contexts. That's a discontinuity in an action policy. That matters.

You're overselling the compression finding. "LLMs compress vague intensity words" is not surprising to the field. Anyone who has worked with these models expects this. What saves it is the *measurement* — you quantified it in a controlled action environment, which is different from prior probability-estimation work. But you need to be clear-eyed: the compression result alone would not get you into a NeurIPS workshop. The abstention discontinuity and the state-dominance inversion are what make this worth extending.

The state-dominance finding (ε²_baseline = 0.782 vs. ε²_word = 0.079) is solid and practically important. The inversion you found in the split-range analysis — word dominates at low baselines, context dominates at high baselines — is actually a more interesting result than you're treating it. That's not just "context matters." That's a regime change in the model's action policy as a function of feasibility. That's worth naming more forcefully.

**What you're missing:** You're treating this as a paper about words. It's actually a paper about how LLMs reason about feasibility under constraint. The words are just the instrument. The real contribution is the behavioral map of how an LLM navigates a constrained action space when instructed in natural language. If you reframe it that way, the work becomes more interesting and more connected to the agentic safety literature that actually has traction right now.

---

## The Single Biggest Weakness

**You have no ground truth for what the words *should* mean, and you're not being direct enough about what that costs you.**

Here's the problem: your entire ordinal analysis is benchmarked against a researcher-constructed scale informed by Quirk et al. You acknowledge this in the limitations, but you're not confronting what it means for your claims. When you say the model shows "compression" or "ordinal anomalies," you're implicitly assuming your 6-tier scale is the right reference. But is it? 

The *moderately* anomaly is the clearest example. You interpret it as the model activating a "restraint heuristic." That's a plausible story. But another equally plausible story is that *moderately* genuinely means something closer to the lower tier in the context of operational instructions, and your tier assignment was wrong. Without a human baseline, you cannot distinguish between "the model is wrong" and "the researcher's tier assignment was wrong." 

This isn't just a limitation — it's a threat to the core claim. A reviewer at a good workshop will ask: how do you know the model is compressing words that humans would distinguish, rather than correctly representing words that humans also treat as equivalent? You don't have an answer yet.

**This is the single most important thing to fix before you submit anywhere.**

---

## The Single Biggest Strength

**The abstention discontinuity at the boundary, combined with the feasibility-regime inversion, is a genuine empirical contribution.**

Nobody has cleanly documented this three-mode behavior (hedge/act/abstain) in a controlled agentic setting with a hard constraint. The fact that *drastically* behaves as "go to ceiling" while *dramatically* abstains — two words most people would treat as synonyms — is a result that would make a safety researcher sit up. This is directly relevant to anyone building natural-language interfaces to constrained systems, which is a growing and important problem.

Lean into this. This is your contribution. The compression stuff is context; the boundary behavior is the finding.

---

## The IRB Question — Deliberated Seriously

I'm going to give you the honest answer, not the comfortable one.

**You probably don't need IRB for the paper you should write next.**

Here's why: IRB is required for research involving human subjects. If you pivot — as I'll recommend below — toward a study that is purely about model behavior (comparing models, testing prompting strategies, probing mechanisms), you have no human subjects and no IRB issue. The human baseline question only becomes mandatory if you want to make claims about how *humans* interpret these words versus how the model does. 

**The pivot that avoids IRB entirely:** Stop framing this as "does the model match human interpretation?" and start framing it as "how do LLMs navigate constrained action spaces under vague instruction?" You don't need a human baseline to make that claim. The claim is about the model's behavior, not about the gap between model and human. The human baseline becomes interesting future work, not a prerequisite.

**If you still want a human baseline without IRB pain:** There are existing validated datasets. The Mosteller-Youtz (1990) probability-word scales, Wallsten et al.'s work on verbal probability expressions, and more recently Zhang et al. (2024) all provide human-derived numeric interpretations of vague quantifiers. You could use these as a proxy reference distribution for the ordinal structure of your word scale — not as a direct comparison to your experimental outputs, but as external validation that your tier assignments are reasonable. This is not a substitute for a direct human comparison, but it addresses the reviewer objection that your scale is arbitrary.

**The other option:** Georgia Tech's IRB process for online surveys that are anonymous, low-risk, and involve no deception is actually exempt-eligible in most cases. A simple Qualtrics survey asking "on a scale of 0-100, what numeric increase does 'slightly increase X' suggest to you?" across your 10 words, with 50-100 MTurk or Prolific participants, would likely qualify for exempt status. Total cost on Prolific at $12/hour for a 5-minute survey: roughly $50-80 for 50 participants. That's within your budget. The exempt determination at GT is typically a few weeks, not months. I would not let this stop you if you want the comparison — it's not the obstacle you think it is. But you don't need it for the paper I'd recommend you write.

**My recommendation:** Write the paper without the human baseline, but reframe so you don't need one. Then add it as a clean follow-up.

---

## Where to Go From Here: What I'd Actually Make You Do

**The paper you should write for August** is not an extension of this paper. It's a focused replication and deepening of the boundary behavior and feasibility-regime findings across multiple models.

Here's the specific program I'd recommend:

**Step 1: Run the same experiment on 3-4 open-source models on your 3070.** Llama 3.1 8B, Mistral 7B, and Qwen2.5 7B will all run on your hardware. This is free. The question is: do you see the same three-mode boundary behavior? Do you see the same state-dominance inversion? If the answer is yes across models, you have a general finding about how LLMs handle constrained action spaces under vague instruction. If the answer is no, you have an equally interesting finding about how alignment and training affect this behavior. Either way you win.

**Step 2: Add the no-word control condition.** This is the cheapest, highest-value experiment you haven't done. Right now you can't distinguish "the model hedges at 0.50 because weak words mean 0.50" from "the model defaults to 0.50 for any increase instruction." Run 30 trials of "increase innovation" with no intensity word. This costs you maybe $2-3 in API credits and closes a major interpretive hole.

**Step 3: Add decrease instructions.** "Slightly decrease" versus "drastically decrease" near the lower boundary (0%, 5%, 10%). Does the model show symmetric boundary behavior? Asymmetric? This is cheap, interesting, and rounds out the feasibility story.

**Step 4: Do NOT pursue the valence/stakes manipulation, the stakeholder persona manipulation, or the mechanistic interpretability route right now.** These are all interesting but they dilute your focus and none of them will be ready by August. The valence study (ICU beds vs. factory robots) is a completely different paper. The mech interp route requires skills you've said you don't have. Stakeholder persona is interesting but tangential. Pick one clear story and tell it well.

**The paper you write:** "Vague Intensity Words in Constrained LLM Action Spaces: Compression, State Dependence, and Boundary Discontinuities Across Models." Single-model results become the main study. Multi-model replication becomes the key extension. The abstention discontinuity is the headline finding. You frame it as a contribution to the agentic safety literature, not the linguistics literature.

---

## On the NeurIPS Workshop Target

This is achievable but tight. August submission means you have roughly 8-10 weeks from now. That's enough time to run the open-source model experiments (2-3 weeks), add the no-word control and decrease conditions (1 week), write the paper (3-4 weeks), and revise (1-2 weeks). You cannot do all of this and also pursue the valence study, the stakeholder study, and the mech interp work. You have to choose.

The workshops most aligned with your work: **ICLR workshops on LLM agents and safety** (if there's a late-breaking track), **NeurIPS workshops on robustness and reliability of LLMs**, and **the EMNLP or ACL workshops on human-computer interaction with NLP systems**. The ACL-affiliated venues are actually better fits for this work than NeurIPS, given the linguistic framing. Don't fixate on NeurIPS specifically.

One realistic concern: workshop papers at top venues are competitive and the bar has risen significantly in the last two years. A single-model ArXiv preprint extended with multi-model replication is a reasonable workshop submission, but it will not be a lock. The work needs to be framed tightly around a single clear contribution, not presented as "glimpses of multiple research topics." Your current framing is too exploratory for a competitive workshop submission.

---

## Reading the Brief as Evidence

You see your work clearly in most respects. Your self-assessment of the limitations is accurate. But I notice two things:

First, you're underselling your production experience as a *research* asset. The fact that you built ATLAS/BAR and understand why vague language is dangerous in production optimization systems is not just a backstory — it's a source of construct validity that most academic researchers don't have. You should be more aggressive about grounding your research questions in the real failure modes you've seen. That makes the work more compelling, not less rigorous.

Second, you're treating the IRB problem as bigger than it is, and the human baseline gap as smaller than it is. These are inverted. The IRB is solvable. The ground truth problem is the one that could undermine your core claims if a sharp reviewer goes after it. Address it by reframing, not by hoping reviewers don't notice.

---

## The Bottom Line

You have a real finding, a coherent methodology, and a genuine motivation from production experience. The work is not "kinda expected" — the boundary discontinuity is not expected, and the feasibility-regime inversion is well-documented. What you need is focus. Stop trying to find the next five papers in this one paper. Write the tight, multi-model version of the boundary behavior story, add the no-word control, and submit it to an appropriate workshop. That's a credible research contribution from someone in your position, and it's achievable by August.

The pipe dream isn't as far-fetched as you think, but it requires showing you can execute a focused research program, not just generate interesting observations. Show that.