# AI Research Council Report
**Paper:** Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions
**Date:** 2026-06-09 14:27:47
**Brief:** Who I am:
Danny Tabach. Working data scientist (JPMorgan Chase — built the staffing optimization engine behind every Chase branch). Finishing a master's at Georgia Tech. AI Safety Research Fellow at Algoverse AI Research — a selective AI safety fellowship where I work with other researchers and PIs on safety research. Algoverse has mentored researchers to publish at top venues (NeurIPS, etc.) and gives me access to collaborators and mentorship I wouldn't have solo.

What I have:
A preprint on ArXiv: "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions." The paper is attached as reference material. In short: I built a controlled environment where a language model receives a vague intensity word ("slightly," "drastically," etc.), produces a numeric action through a tool call, and a deterministic backend measures the outcome. Across 6,620 runs, the model compresses 10 words into ~5 distinct outputs, anchors heavily on system state over word choice, and exhibits discontinuous behavior near operational boundaries — including a case where swapping one near-synonym for another ("drastically" → "dramatically") flips the system from acting to refusing in the same state.

The origin story matters: this came from a real production system I built. I looked at my own autonomous planner and realized stakeholders couldn't wield it safely — a one-word change in the instruction could silently move the action from a cautious nudge to pushing a constraint to its ceiling.

What I believe (but need tested):
I think this paper opens a window into something bigger. The finding isn't just about intensity words — it's about what happens at the interface where human language meets AI numeric action in consequential settings. I've been calling this "passive failure" — the model isn't scheming or refusing maliciously, it's just silently mistranslating intent in ways nobody notices. I think this matters across domains (healthcare, finance, logistics — anywhere a human gives a vague instruction and an AI turns it into a number), and I think the failure modes rhyme across those domains.

But I might be wrong about how big this is. I might be inflating a solid niche result into something it's not. My known failure mode is narrative inflation — falling in love with the vision and trying to make one paper be an entire field. Call me on it if you see it.

The productive question:
I need to extend this paper into a second study. Not "someday" — this is the immediate next step. I need a concrete, feasible direction that builds on what this paper established and produces a publishable result. What is the strongest next experiment I can run? What would make the biggest contribution given what I've already shown? I'm not looking for a wishlist — I'm looking for the one or two moves that turn a single preprint into a research trajectory.

What I want from this council:
I'm standing at a fork with many paths. The paper is done. It's on ArXiv. Now what?

I have my own ideas about extensions, but I don't want to anchor you with them. I want YOUR independent read on where this result points. Treat this like a peer collaboration — you've read my paper, you know my position and resources, now tell me:

1. What do you see through this window? What directions does this paper open that I might not be seeing from inside it? Think broadly — not just "run more words" but what research programs, what questions, what fields does this result speak to?

2. Which direction has the highest leverage? If I can only pursue one thread for the next year, which one builds the most — for the research, for my credibility, and for the community?

3. Is the "passive failure at the action interface" framing the right frame? Or is there a better way to position what this paper actually demonstrates? Would a different framing open more doors?

4. Some people have suggested mechanistic interpretability — looking inside the model to understand WHY the compression happens, why the boundary behavior is discontinuous, why "drastically" acts while "dramatically" abstains. Is that the right move, or does it pull me away from the deployment-facing empirical work that's the paper's actual contribution?

5. How does Algoverse factor in? I'm a fellow in an AI safety research program with access to PIs, collaborators, and mentorship infrastructure. How should I be leveraging that for this research program? What should I be bringing to my collaborators and mentors?

6. What's the honest read on my position? Working data scientist, master's student, one preprint, AI safety research fellow at Algoverse. What does this profile actually afford me and what does it not? Where should I aim and what should I stop pretending I can do alone?

7. What am I not seeing? I built this from inside one system and one conviction. Name the blind spot.

I want adversarial honesty, not encouragement. Narrow me — don't expand me. If six advisors each add a direction, that's a failure. If six advisors converge on one path, that's the outcome I need.
**Cost:** $5.08 | **Tokens:** 216,155 in / 41,938 out

---

# RESEARCH STRATEGY COUNCIL — FINAL STRATEGIC BRIEF

**For:** Danny Tabach
**Re:** "Does Slightly Mean Somewhat?" — what comes next
**From:** The Research Director, synthesizing six advisors across two rounds

---

## The Verdict

**1. Is the field real and unclaimed?**

**Qualified yes — but you are misnaming it.** There is a genuine, unclaimed coordinate: the controlled measurement of how *semantically distinct* vague intensity language maps to *consequential numeric actions* via tool calls, with attention to the word×state interaction and boundary behavior. The Field Cartographer confirms no one occupies this specific spot, and the 2026 GAP benchmark (text-safety vs. tool-call-safety divergence) actually *strengthens* your claim — two independent research programs are converging on the text-action boundary, which is evidence the territory is real, not derivative.

But the Devil's Advocate is correct on the larger point: this is **a real gap inside existing fields, not a new field.** The compression finding is anticipated by Mosteller & Youtz. State-dominance is close to what "grounding" already predicts. What is genuinely yours — and unclaimed at the mechanistic level — is the **boundary abstention behavior**: the drastically→dramatically flip, where one near-synonym swap changes the system from acting to refusing in the same state. That finding has no clean precedent. That is your real estate.

A gap is not a field. Fields require communities, taxonomies, and infrastructure you don't have. Stop trying to name the field. Name the *phenomenon* precisely and let the community name the field if it forms.

**2. Cornerstone verdict: (a), (b), or (c)?**

**(c) — and you don't yet have the evidence to know whether it can become (b).** The council is unanimous on this. The Skeptical PI's framing is the one to internalize: your paper becomes a load-bearing instrument **if and only if** the human baseline shows that humans *do* differentiate these words where the model does not. Without that result, you have a clean behavioral characterization — a contribution to existing fields, publishable, credible, but not foundational. With it, you have a demonstrated gap between human intent and machine action, which is the thing the "passive failure" framing has been *asserting* without earning.

The verdict is not yours to declare. It is contingent on one experiment. Run it.

---

## The Path

### Next paper (the wedge): The Human Baseline Study

**What it is:** Administer your 10-word scale to 50–100 human participants under the same task framing, asking them to assign numeric allocations. Compare the human ordinal/numeric structure directly to Claude Haiku's.

**Why it's next:** This is the single highest-leverage move and the council converged on it across both rounds. It closes the gap that destabilizes everything else. Right now you cannot distinguish "model failure" from "genuine linguistic ambiguity" — which means your entire framing rests on an unmeasured assumption. Every downstream paper is built on sand until this is resolved. It also validates your researcher-constructed word scale, which is currently a vulnerability (only 3 of 10 words come from Quirk's explicit lists).

**Critical sequencing (this is non-negotiable):**
- **File the Georgia Tech IRB application THIS WEEK.** Multiple advisors flagged this as the most time-sensitive dependency in your entire program. Your IRB access closes when your master's affiliation ends. Miss this window and the study delays by years or requires an institutional sponsor you don't yet have. The IRB runs in parallel with everything else — it is not a future-work item, it is a closing door.
- **Before IRB even clears, run the Skeptical PI's informal pilot:** 10–15 participants on Prolific, no IRB needed for a non-sensitive, non-deceptive, non-identifying survey. Cost: ~$50–100, two weeks. This tells you *immediately* which world you're in. If humans also compress, you revise the framing before investing months. If they don't, you have confirmation the full study is worth it. Do the pilot first.

**Target venue:** Contingent on the result. If humans differentiate and the model doesn't → AI venue (EMNLP/ACL Findings, or SoLaR workshop). If humans also compress → the story is linguistic; still publishable but reframed.

**Feasibility:** High. The methodology (numeric adverb scaling) is decades old and well-established. Survey cost ~$400–600 for the full study. This is the cheapest, most decisive experiment available to you.

### Paper after that: Cross-Model Replication (with the human anchor)

**What it demonstrates:** Run the same protocol on GPT-4o, Gemini Flash, and **at least one open-weights model (Llama or Mistral).** With the human baseline established, this becomes "which models are closest to human calibration?" — a far stronger question than "Model A vs. Model B."

**Why it follows:** Two reasons. First, it tells you whether the phenomenon is a Claude Haiku artifact or a model-class property. Second — and the council surfaced this as an underweighted risk — **model deprecation.** Claude Haiku (`claude-haiku-4-5-20251001`) is a versioned commercial model that will be deprecated. Your entire empirical foundation is time-stamped. The open-weights model is your insurance: a stable baseline that survives even when the commercial models shift. Run this *while Haiku still exists.*

**Feasibility:** Solo-executable. Budget $500–1,500 in API costs. Plan it explicitly.

### The field-defining move: "Intent–Action Fidelity at the Boundary"

**When it becomes appropriate:** Only after the human baseline and cross-model studies are done. By then you have: the original phenomenon, a human anchor, and cross-model generality. *Then* you can synthesize — and only then.

**What it requires:** A senior co-author. This is where Algoverse becomes load-bearing. The synthesis paper benefits enormously from a PI who can vouch for the framing and target the right venue (NeurIPS/ICLR safety workshop, or FAccT). Bring the framing to your PI *now* for feedback — not for execution, but to pressure-test whether it lands.

**One framing instruction:** Build this paper around the *class* of behavior (boundary-dependent categorical mode-switching), not around the single drastically/dramatically pair. The flip is your motivating example and your hook in every abstract. It is not the organizing unit of a paper.

---

## Consensus Findings

All or most advisors agreed:

1. **The human baseline is the load-bearing next step.** Unanimous. It determines whether your framing survives.
2. **The IRB clock is the binding constraint.** File now. It closes with your degree.
3. **The drastically→dramatically flip is your sharpest, most defensible finding.** Lead with it everywhere.
4. **"Passive failure" is overreaching as currently used.** It names a verdict the evidence hasn't earned, and it's technically imprecise (engineers read "passive failure" as failure-to-act; your model *does* act). Use it as a research-program label, not as a description of what the paper shows.
5. **Do NOT pursue mechanistic interpretability now.** Wrong resources, wrong community, pulls you from your actual advantage. Defer it as a possible *later collaboration*, not a solo move.
6. **Target NLP/deployment-safety venues before alignment venues.** Establish credibility where the work is evaluated on its own terms first.
7. **The production-system origin is your genuine differentiator.** Lean into it.

---

## Contested Points

**Combine human baseline + valence (decrease instructions) into one paper?**
- *Research Sequencer:* yes — same apparatus, efficient, two contributions.
- *Alignment Insider & Career Strategist:* no — the human baseline should stand alone, clean and focused; combining adds IRB complexity and risks a "two thin contributions stapled together" review.
- **My call: Keep them separate. The human baseline is too important to dilute, and the IRB protocol is simpler for a pure survey.** Collect the valence data in parallel (it's solo, cheap, one weekend) but publish it separately or fold it into the cross-model paper. The decrease asymmetry is the cheapest extension you have — run it this week regardless.

**How derivative is the field — 7/10 or 5/10?**
- *Devil's Advocate:* 7/10 derivative.
- *Field Cartographer & Skeptical PI:* closer to 5/10 once you isolate the boundary behavior.
- **My call: 5/10.** The Devil's Advocate's own analysis concedes the boundary abstention has no clean precedent. "Contribution to existing fields that extends them in a new direction" is not "derivative." But it is also not "new field." Hold both truths.

**Is cross-model credibility-building or field-defining?**
- *Research Sequencer:* field-defining (Bucket B), comes after human anchor.
- *Career Strategist & Skeptical PI:* basic scientific hygiene / credibility-building.
- **My call: It's hygiene with a hedge function.** For someone with one preprint, cross-model is the minimum required to make *any* general claim — not a theoretical flourish. But the Sequencer is right that it's stronger *after* the human anchor. Sequence: human baseline first, cross-model second. The labels matter less than the order.

---

## The Narrowing

You asked to be narrowed. Here is what to **stop**:

- **STOP trying to name a field.** "Passive failure at the action interface," "deployment-external safety science" — drop these as field-founding claims. Name the phenomenon, ship the results, let the field name itself.
- **STOP the cross-domain ambition (healthcare, finance, logistics).** This is the inflation, named by the Devil's Advocate in real time. You have *one* domain you understand deeply. Stay there until you've exhausted it. Cross-domain requires domain co-authors you don't have and is a Paper 5 *only if* Paper 4 lands.
- **STOP considering mechanistic interpretability.** Not now, not solo. Five advisors said this independently.
- **STOP running multiple extensions simultaneously.** Your future-work section lists six directions. That's a wishlist, not a program. Pick the human baseline. Finish it.
- **STOP treating self-awareness as a defense.** The Skeptical PI's sharpest observation: naming "narrative inflation" in your brief can function as pre-emptive inoculation rather than behavioral constraint. The test is your next paper. If it's a clean human-baseline replication with no new theoretical superstructure, your self-awareness is real. If it introduces a new domain + new construct + new framing all at once, it was decorative.
- **DEFER, don't abandon:** valence asymmetry (collect now, publish later), denser baseline grid (background infrastructure, not a paper), no-word control (add it to the next study — it resolves the 0.50-hedge ambiguity cheaply).

---

## Advisor Highlights

- **Field Cartographer:** Engage the GAP benchmark (Cartagena & Teixeira, 2026) and Feng et al. (EMNLP 2025) — both are direct, recent neighbors your paper doesn't cite. GAP studies harmful-action leakage; you study magnitude-fidelity. Position yourself as the complement.
- **Devil's Advocate:** Your framing asserts a "failure" that requires a counterfactual you don't have. The word "failure" presupposes the conclusion. Earn it with the human baseline or drop it.
- **Research Sequencer:** The no-word control is cheap, fast, and resolves whether 0.50 is a "hedge" or just the model's default response to *any* increase request. It should have been in Paper 1. Put it in Paper 2.
- **Alignment Insider:** The MATS Autumn 2026 window is closed; next meaningful cycle is ~Summer 2027. You have 6–9 months to land a workshop paper as a prerequisite. The Algoverse→workshop→fellowship pipeline is documented and real — use your PI as a reference.
- **Career Strategist:** The "recognized voice" path is shorter than the research path. Write one Alignment Forum post around the drastically/dramatically finding *in the next two weeks*, framed as a question to the community. It costs nothing and tests your framing faster than peer review.
- **Skeptical PI:** Run the informal Prolific pilot before the full IRB study. Two weeks, $100, and it tells you which world you're in before you invest months.

---

## What's Working

Do not change these:

- **The experimental design.** The deterministic backend as a measurement instrument is genuinely clever and reusable. It is your real methodological contribution.
- **The production-system origin.** Ecological validity most researchers lack. Anchor every paper in "what would a practitioner building a real system need to know?"
- **Your honesty in the paper.** The limitations section is clean, the statistics are appropriately hedged, you don't overclaim *in the paper itself.* The inflation lives in the brief, not the work.
- **The self-diagnosis.** You named your failure mode precisely. That's rare. Now make it behavioral.

---

## The Single Most Important Thing

**File the IRB this week and run the human-baseline pilot before anything else — because until you know whether humans differentiate these words, you don't know whether you've found a failure or just described a feature of language, and that single answer determines whether your entire research program is a real contribution or a beautifully-measured tautology.**

---

## Individual Reviews

### 1. Field Cartographer

Good. I now have sufficient material to render a complete, adversarially honest strategic review. Let me construct it.

---

# FIELD CARTOGRAPHER'S STRATEGIC REVIEW
## Research Vision Brief: Danny Tabach / "Does Slightly Mean Somewhat?"

---

## I. TERRITORY MAP: Where Does This Sit?

The paper occupies a specific coordinate that sits at the intersection of four fields, but is not fully claimed by any of them. Let me draw the borders precisely.

**HCI / Natural Language Interfaces.** This field studies how humans communicate intent to computational systems. Natural Language Interfaces represent a fundamental reimagining of the human-computational relationship, placing the burden of translation on machines rather than humans. HCI work on NLIs focuses extensively on the *user experience* of this translation — does the user feel understood? Can they recover from errors? What mental models do users form? What HCI does **not** routinely do is instrument the *output side* of the translation with a deterministic measurement harness and ask: what number did the machine actually choose, and how does that number vary as a function of input semantics? The paper's contribution is on the output side. HCI sits at the border but does not occupy the interior.

**Prompt Sensitivity Research.** This is the nearest occupied territory. Subtle changes in prompt phrasing can lead to significant shifts in LLM behavior, even when model outputs appear accurate. However, the dominant framing in prompt sensitivity research studies *semantically equivalent* paraphrases — does the model give the same answer when you ask the same question differently? Much of the prompt sensitivity research stems from heuristic evaluation methods that overlook semantically correct responses expressed through alternative phrasings. Tabach's paper studies the *opposite* problem: **semantically distinct** intensity words that a user *intends* to be different — and measures whether the model preserves that intended distinction in a numeric action. This is a different construct, not a rebranding. The border with prompt sensitivity is real but the interior is distinct.

**LLM Agent / Tool-Calling Reliability.** A fundamental reliability question remains under-explored in LLM agents with tool-calling capabilities: does the same agent behave the same way twice? Recent work presents systematic empirical studies of behavioral consistency in multi-step tool-calling agents. This is the closest adjacent territory to emerge in 2025-2026. Unlike prior work on consistency in ReAct-style agents (search-only, free-text actions), newer work studies the richer setting of structured tool-calling interfaces with typed parameters and consequential side effects. The Yagubyan (2026) paper on behavioral reproducibility and the Mehta et al. (2026) work on agent self-disagreement are the most direct neighbors. However, these papers ask: *given identical inputs, does the agent produce identical outputs?* Tabach asks: *given semantically graduated inputs (a word scale), does the agent produce ordinally graduated outputs?* The framing is different: consistency vs. semantic fidelity. The territory is adjacent but the specific question is not occupied.

**Automation Bias / Trust Calibration.** Automation bias results in making both omission and commission errors when decision aids are imperfect; it occurs in both naive and expert participants, cannot be prevented by training or instructions, and can affect decision making in individuals as well as in teams. This literature — Parasuraman & Manzey (2010), Mosier et al. (1998), Skitka et al. (1999) — studies the *human* side of the failure: users over-rely on automation and fail to catch its errors. Safety and efficiency of human-AI collaboration often depend on how humans appropriately calibrate trust; over-trusting the autonomous system sometimes causes serious safety issues. What this literature does **not** do is measure the *pre-human* failure mode: what the model actually outputs before any human gets the chance to over-trust it. Tabach's "passive failure" is upstream of automation bias. The territory is adjacent but the interior is different.

**AI Alignment / Safety.** Alignment research focuses on whether models pursue intended objectives, with emphasis on deceptive or misaligned goal-directed behavior. Tabach's contribution is explicitly *not* about scheming or refusal — it is about silent mistranslation of vague intent into numeric action. This sits closer to what alignment researchers call *specification gaming* or *reward misspecification*, but framed empirically and at the deployment layer rather than at the training objective layer. The alignment community will recognize the concern but will not recognize the methodology as theirs.

**The Unclaimed Coordinate.** The specific unclaimed space is: *empirical, controlled measurement of how vague scalar language maps to numeric actions in tool-calling agents, with attention to the interaction between lexical semantics and system state at operational boundaries.* No existing research program has staked this exact claim with this exact methodology. The space exists. Whether it is large enough to be a field is a separate question (addressed below).

---

## II. GAP ASSESSMENT: Real, Partially Occupied, or Fully Occupied?

**The gap is real but partially occupied on the periphery.** Here is the precise accounting:

**Fully occupied by others:**
- Prompt sensitivity for *semantically equivalent* inputs → extensive literature
- Automation bias in human-AI teaming → Parasuraman, Mosier, Skitka lineage
- Trust calibration → well-developed empirical program
- LLM agent behavioral consistency (identical inputs, repeated runs) → Mehta 2026, Yagubyan 2026

**Partially occupied:**
- Vague quantifier interpretation by LLMs → Zhang et al. (2024) on probability expressions is the closest prior work the paper correctly cites. That work studies probability words ("likely," "probable") mapping to numeric probabilities. Tabach studies *intensity* words ("slightly," "drastically") mapping to numeric *actions* via tool calls. The distinction matters: probability estimation is a reporting task; action selection is a consequential output task. The gap between them is real but narrow. Reviewers will push on this.
- Systematic empirical work on behavioral consistency in multi-step tool-calling agents is emerging, measuring whether agents select the same tools, in the same order, with the same arguments, across repeated identical invocations. This work is about *consistency* of behavior, not about *semantic fidelity* of graduated language. The overlap is structural (same measurement apparatus) but the research question is different.

**Genuinely unclaimed:**
- The *interaction* between word semantics and system state in determining numeric output — the "differentiation funnel" finding — has no direct prior art that I can locate. The finding that word choice dominates at low baselines but state dominates at high baselines, and that this relationship inverts completely, is not documented elsewhere.
- The *three-mode boundary behavior* (hedge, act, abstain) at operational limits, and the finding that near-synonyms ("drastically" vs. "dramatically") produce categorically different behaviors at the same state, is not documented in any adjacent literature.
- The *action-specific* framing — not "what does the model think this word means" but "what number does the model put in a tool call" — is genuinely distinct from prior NLP work on vague language.

**Verdict:** The gap is real. It is not a virgin continent — there is significant adjacent work the author must engage — but the specific coordinate (vague intensity words × numeric tool-call actions × system-state interaction × boundary behavior) is not occupied. The author is not rebranding existing work. They are measuring something that has not been measured.

---

## III. ANALOGY EVALUATION: Does "Clinical Safety Science" Hold?

The clinical safety science analogy is the paper's most seductive and most dangerous framing device. Let me stress-test it.

**Where it holds:**
Both medicine and aviation involve high-stakes decision-making often under uncertainty, and medicine has borrowed from aviation: the origins of surgical checklists, safety time-outs, the "just culture" of incident reporting can all be traced back to flight safety. The analogy to *near-miss reporting* is legitimate. AI issues (or AI flaws) are system conditions that, once exposed to an external environment, become prerequisites for incidents, while incidents are events that could have caused harm (near misses) or did cause harm. Tabach's paper documents a class of *pre-incident conditions* — systematic mistranslation that is invisible to users — which maps coherently onto the near-miss concept.

The analogy also holds at the methodological level: clinical safety science developed *controlled measurement instruments* (standardized checklists, dosage protocols, outcome tracking) precisely because uncontrolled observation of failures is insufficient. Tabach's controlled harness — deterministic backend, isolated variables, repeated runs — is structurally analogous to a clinical measurement instrument.

**Where it breaks:**

*Scale and stakes.* Clinical safety science emerged from catastrophic, visible, countable failures: wrong-site surgeries, medication overdoses, anesthesia deaths. The failures are discrete, attributable, and legally consequential. Tabach's documented failures are diffuse, invisible, and currently consequential only in synthetic environments. The analogy inflates the urgency of the finding by borrowing the gravity of a field built on body counts. The paper has not yet demonstrated that these failures cause harm in production systems at a meaningful rate. That is not a disqualifying limitation — it is exactly what a research program would need to establish — but the analogy presupposes the conclusion.

*The absence of a counterfactual human baseline.* Clinical safety science always compares against a human performance baseline: how often do *humans* make this error without the system? Tabach's paper explicitly acknowledges the absence of a human survey. This is the most important gap for the analogy. Without it, you cannot say whether the model's compression of intensity words is worse than, equal to, or better than how humans would interpret those same words. Healthcare systems have mainly attempted to learn from errors and near-miss events through incident reporting systems inspired by aviation; the most powerful ambition was that healthcare would learn from failures the way aviation does — but this aspiration has not yet been realized, partly due to key principles being lost when adapted from aviation. The lesson here is pointed: analogies from safety science are productive when the structural parallels are maintained, and the most important structural parallel is the *comparison to baseline human performance*. Without that, the analogy is decorative.

*The "passive" framing is doing too much work.* "Passive failure" is a useful intuition — the model isn't refusing or scheming, it's silently mistranslating. But in clinical safety science, "passive failure" has a specific meaning: failure of a system to perform an expected protective function (e.g., a safety interlock that doesn't trigger). Tabach's usage is different: the model *does* act, but acts differently than the user intended. This is closer to a *commission error* (acting incorrectly) than a passive failure (failing to act). The vocabulary is evocative but imprecise.

**Verdict:** The analogy is productive as a motivating frame but dangerous as a field-founding claim. Use it to explain *why this matters* to non-specialist audiences. Do not use it to claim the paper has established a new safety science. The analogy needs the human baseline study to become defensible.

---

## IV. NAMING & FRAMING: Does the Vocabulary Work?

**"Passive failure"** — Evocative, memorable, but technically imprecise (see above). The word "passive" will confuse engineers who use it in a specific sense (fail-safe vs. fail-dangerous). More importantly, it implies the model is inert when the paper shows the model is *actively* doing something — it's just doing it wrong. Consider: *silent mistranslation*, *semantic opacity*, or *lexical-action gap* as alternatives. None of these are perfect, but they are more precise.

**"Action interface"** — This is the strongest piece of vocabulary in the author's framing. It cleanly distinguishes the paper's contribution from probability estimation (a cognitive task) and from prompt sensitivity (a consistency task). The "language-to-action boundary" framing in the paper's Figure 1 is the best visual articulation of the concept. Keep this.

**"Deployment-external safety science"** — This phrase will confuse reviewers. "External" to what? The paper studies behavior *within* a deployment harness. The intended meaning seems to be "safety science conducted outside the model's training and alignment pipeline, by third-party researchers, in deployment-realistic conditions." If that's the meaning, say that. The phrase as stated is opaque.

**"Vague intensity words in LLM numeric actions"** — This is the paper's actual title framing, and it is the most precise and defensible. It will attract the right reviewers: NLP researchers who work on vague language, HCI researchers who work on natural language interfaces, and AI safety researchers who care about agentic action reliability. It is not glamorous, but it is accurate. For a first paper, accurate is better than glamorous.

**The naming problem in aggregate:** The author is trying to name a field before the field has enough papers to name itself. This is premature. The right move is to name the *phenomenon* precisely (the paper does this adequately) and let the field name emerge from the community of researchers who cite the work. Forcing the field name now risks either being ignored (if the name doesn't catch on) or being absorbed (if someone with more institutional weight adopts the concept and renames it). Focus on the phenomenon, not the field.

---

## V. FIELD-FOUNDING FEASIBILITY: Can One Paper Do This?

**No. And the author already knows this.**

The author's self-diagnosis of "narrative inflation" is correct and important. Here is the honest map of what one paper can and cannot do:

**What this paper has done:**
- Established a controlled measurement methodology for a previously unmeasured phenomenon
- Produced three specific, replicable findings (compression, state dominance, boundary behavior)
- Identified a research question that is not occupied by existing literature
- Demonstrated that the phenomenon has consequential downstream effects (the $250K spread)

**What this paper cannot do alone:**
- Establish generalizability (one model, one domain, no human baseline)
- Claim the phenomenon is a "failure" rather than a feature (without human comparison)
- Found a field (fields require a community, not a paper)

The parallels between safety-critical domains have long been recognized; both involve high-stakes decision-making often under uncertainty. The fields that Tabach is analogizing to — clinical safety science, aviation safety — were founded not by single papers but by *incident taxonomies*, *reporting infrastructures*, and *regulatory mandates* that created institutional demand for the research. Tabach has none of these. What he has is a measurement methodology and three findings. That is the right starting point, but it is a starting point.

**What would actually seed a field:**
1. A human baseline study (the most urgent gap — the paper's own future work section identifies this correctly)
2. A cross-model replication (does this pattern hold for GPT-4o, Gemini Flash, Llama?)
3. A domain replication (does the pattern hold for medical dosing language, financial instruction language?)
4. A workshop at a venue like FAccT, AIES, or the ACL Safety workshop that convenes researchers around the phenomenon
5. A benchmark or shared task that operationalizes the measurement harness for community use

One person cannot do all of this. The Algoverse fellowship is the right vehicle for items 2 and 3. The workshop requires co-authors with institutional weight. The benchmark is the highest-leverage single artifact.

---

## VI. CLOSEST EXISTING WORK: The 10 Papers That Must Be Engaged

The author must engage the following work, in order of proximity to the claimed contribution:

**1. Zhang et al. (2024) — "Words of Estimative Probability in LLMs"**
The closest direct predecessor. Studies how LLMs map probability words ("likely," "probably") to numeric probabilities. The delta from Tabach's work: probability estimation vs. action selection, and no system-state interaction. This paper must be cited, and the distinction must be made explicit.

**2. Mehta, Ramesh & Singla (2026) — "When Agents Disagree With Themselves"**
This work studied behavioral consistency in ReAct-style agents on HotpotQA, finding that agents produce 2.0–4.2 distinct action sequences per 10 runs and that inconsistency predicts failure — but it is limited to search-only actions in a question-answering setting. Tabach's work is complementary: not consistency of identical inputs, but ordinal fidelity of graduated inputs.

**3. Yagubyan (2026) — "How Consistent Are LLM Agents?"**

### 2. Devil's Advocate

# Devil's Advocate Review: Strategic Assessment

---

## The Case That the Field Is Derivative

Let me name the specific bodies of work that most directly threaten the novelty claim, because the author deserves precision here, not a vague gesture at "related work."

**The automation bias and trust calibration literature** has been studying the gap between human intent and AI action for thirty years. Parasuraman & Riley (1997) on automation bias, Lee & See (2004) on trust in automation, Cummings (2004) on human supervisory control — these establish the foundational claim that humans cannot reliably predict or control automated system behavior through natural language interfaces. The "passive failure" framing is a restatement of what this community calls *automation surprise*: the system did something the operator didn't expect because the operator's mental model of the system was wrong. The author's contribution is a measurement of *one mechanism* by which this surprise occurs. That is real. But it is not a new field — it is a new data point in a 30-year-old field.

**The vague quantifier and linguistic uncertainty literature** is even more directly threatening. Mosteller & Youtz (1990), which the author cites, already documents that vague probability expressions compress into fewer distinct numeric interpretations than the surface vocabulary implies. Wallsten, Budescu, and colleagues throughout the 1980s and 1990s showed that words like "likely" and "probable" map inconsistently to numbers across individuals and contexts. The author's finding — that 10 intensity words compress to 5 distinct outputs — is structurally identical to what this literature found about probability expressions decades ago. The novelty claim requires that the *action* context (tool call producing a consequential numeric output) is categorically different from the *estimation* context (reporting a probability). That argument is present in the paper but underdeveloped and unproven. It may be true. It isn't demonstrated.

**The HCI safety and natural language interfaces literature** covers the deployment gap directly. Work on natural language interfaces to databases (Androutsopoulos et al., 1995 and the subsequent decade of NLIDBs), voice interfaces in aviation (Cushing, 1994 — "Fatal Words"), and more recently conversational AI in clinical settings (Laranjo et al., 2018) all study what happens when vague human language must be translated into precise system actions with safety consequences. Cushing's work on aviation communication failures is particularly sharp: pilots issuing ambiguous altitude instructions and controllers interpreting them differently produced crashes. The author's "drastically → dramatically flips act to abstain" finding is a cleaner, more controlled version of what Cushing documented in the field. The author has the better measurement instrument. They do not have a new phenomenon.

**The prompt sensitivity / brittleness literature** is the most recent and direct threat. Mizrahi et al. (2023, "State of What Art?"), Webson & Pavlick (2022), and the BIG-Bench Hard evaluations all document that semantically similar prompts produce different model outputs. The author's paper is a controlled, domain-specific instance of this. The contribution is the *controlled measurement environment* — the deterministic backend that converts linguistic variation into measurable outcome variation. That is methodologically clean. It is not a new phenomenon.

**The strongest existing work that most directly threatens the novelty claim** is Fischler & Firschein's work on language grounding and, more recently, Bender et al. (2020) on the "meaning" problem in NLP — the argument that statistical language models don't have stable referents for words, so of course "slightly" and "marginally" produce the same output. The author's paper is an empirical confirmation of a theoretical prediction that has been in the literature for years.

**My honest assessment of this case:** The "new field" framing is not supported. The existing literature covers the phenomenon from multiple angles. What the author has that is genuinely novel is: (1) a clean measurement instrument that isolates the language-to-action translation step with a deterministic backend, and (2) the specific finding about boundary-dependent abstention behavior, which I have not seen documented in this form elsewhere. These are contributions to existing fields, not the foundation of a new one.

---

## The Case That the Paper Can't Carry It

Here is what a skeptical NeurIPS reviewer would write in the meta-review, and I am not softening it:

**One model.** The entire empirical edifice rests on Claude Haiku. Not Claude Sonnet. Not GPT-4o. Not Gemini. Not an open-weights model where the training data and RLHF procedure are at least partially known. Claude Haiku is a commercial, closed-weights model with undisclosed training data, undisclosed RLHF procedures, and undisclosed system prompt defaults. The author cannot tell you *why* "drastically" acts while "dramatically" abstains. They cannot tell you whether this is a stable property of the model class or an artifact of a specific fine-tuning run. They cannot tell you whether the 0.50 hedge reflects training data frequency, RLHF reward shaping, or something else. The paper documents a behavioral fingerprint of one commercial model version. Model versions change. The findings may not replicate on the next Haiku release.

**One domain.** Resource allocation with a sum-to-100% constraint. This is not just "one domain" in the sense of being narrow — it is a domain with a specific mathematical structure (simplex constraint) that may be driving the boundary behavior. The abstention at 89% may not be about the semantics of "considerably" — it may be about the model's learned behavior near simplex boundaries. The author cannot distinguish these explanations with the current design.

**No human baseline.** The author acknowledges this. I am emphasizing it because it is more damaging than the paper's framing suggests. Without a human baseline, you cannot make the claim that the model's compression is a *failure* rather than a *reflection of genuine linguistic ambiguity*. If humans also compress "slightly," "marginally," "somewhat," and "mildly" into the same numeric output — which the Mosteller & Youtz literature suggests they might — then the model is not failing. It is accurately representing the ambiguity in the language. The entire "passive failure" framing depends on a gap between human intent and model action that has not been measured.

**Synthetic environment.** The allocation environment is clean by design, but that cleanliness is also a limitation. Real production systems have noise, feedback loops, multiple agents, and users who adapt their language based on observed outcomes. The author's finding that word choice is dominated by context state is interesting in a clean environment. In a real system, users would learn to say "drastically" when they want a large move, regardless of state, because they've observed the model's behavior. The static, non-adaptive experimental design cannot capture this.

**30 runs per cell.** For a deterministic model at T=0.0, 30 runs per cell is adequate. For T=0.7 and the boundary behavior analysis, 30 runs is marginal. The abstention finding at 89% (121/300 total, but word-level counts as small as 0/30 vs. 30/30) is robust for the extreme cases but the intermediate cases (the "drastically" 7% abstention rate is 2/30 runs) are fragile.

**What a senior alignment researcher would say:** This paper measures a real phenomenon. It is not a safety paper. It documents that a model's numeric outputs are compressed and state-dependent — which is a behavioral characterization, not a mechanistic one, and not a safety intervention. The alignment relevance depends entirely on the "passive failure" framing, which requires the human baseline that doesn't exist. Without it, this is a psycholinguistics result about model behavior, not an alignment result.

**The founding instrument claim fails** on a simple criterion: a founding instrument needs to be generative — it needs to produce a research program that couldn't exist without it. The author's measurement instrument is clever, but the research program it enables (test more words, test more models, test more domains) is incremental, not generative. It does not open questions that couldn't be asked before. It provides cleaner answers to questions that were already being asked.

---

## Narrative Inflation Check

Yes. The brief is an instance of the failure mode the author identified.

Here is the specific evidence:

**The phrase "passive failure at the action interface"** is doing enormous work. The paper does not establish that there is a failure. It establishes that there is compression and state-dependence. Whether this constitutes failure depends on whether the model's output diverges from human intent — which requires the human baseline that doesn't exist. The author has named a phenomenon before demonstrating that the phenomenon is harmful.

**"I think this matters across domains (healthcare, finance, logistics)"** — this is the inflation move in real time. The paper tests one model, one domain, one action direction, two temperatures. The leap to "healthcare" is not supported by anything in the paper. It is a vision statement dressed as an empirical claim.

**"The failure modes rhyme across those domains"** — this is assertion, not evidence. The author has no data from healthcare, finance, or logistics. They have a metaphor.

**"I've been calling this 'passive failure'"** — naming a phenomenon before establishing it is a classic inflation move. The name implies a verdict (failure, passivity, interface as the locus) that the evidence does not yet support.

**The brief's framing of the paper as "opening a window into something bigger"** — this is the author's own language, and it is the inflation pattern exactly. The paper is a controlled measurement of one behavioral property of one model in one domain. That is not a window into something bigger. It is a result. The author is being asked to let it be a result.

**Where the brief is NOT inflating:** The origin story (production system, real stakes) is grounded. The acknowledgment of limitations is honest. The request for narrowing rather than expanding is self-aware. The author knows they do this. The question is whether knowing it is enough to stop it.

---

## The Steelman Alternative

Here is the best version of this research program that does not require the "new field" claim and does not require the brief's inflation:

**The actual contribution is a measurement instrument.** The author built a clean, reproducible method for measuring how a language model maps vague intensity language to numeric actions in a constrained environment. The deterministic backend is the key innovation — it converts a behavioral question into a measurement question. This is a methodological contribution to the empirical study of LLM behavior.

**The actual finding is the boundary behavior.** The compression result (10 words → 5 outputs) is interesting but not surprising given the existing literature. The boundary-dependent abstention is genuinely novel in its specificity: the finding that "drastically" acts by pushing to the ceiling while "dramatically" abstains in the same state is a crisp, falsifiable, surprising result. This is the paper's sharpest contribution. It belongs in the empirical NLP / model behavior literature, not in a new field.

**The right framing is "behavioral characterization of vague language in constrained action contexts."** This sits cleanly in the intersection of empirical NLP, human-computer interaction, and AI evaluation. It does not require a new field. It requires a second paper that either (a) adds the human baseline and establishes that there is actually a gap between human intent and model action, or (b) demonstrates the boundary behavior across multiple models and domains, establishing generality.

**The production origin is a genuine asset.** The fact that this came from a real system the author built gives it ecological validity that most academic benchmarks lack. The right way to use this is not to claim a new field, but to position the work as "empirically grounded in deployed systems" — which is a credibility claim, not a scope claim.

**The research program that succeeds without the new field claim:** Study 1 (existing paper): Behavioral characterization of intensity word compression in one model. Study 2: Human baseline + cross-model comparison, establishing whether the compression reflects model failure or linguistic ambiguity. Study 3: Boundary behavior replication across domains with different constraint structures, testing whether the abstention pattern generalizes. This is a three-paper arc that is publishable, credible, and does not require founding a field.

---

## What Would Change My Mind

I am arguing the field is derivative. Here is what would make me concede it is genuinely new:

**On the field claim:** Show me a body of work that specifically studies the *action* case — where vague language must produce a consequential numeric output through a tool call — as distinct from the *estimation* case (probability expressions) and the *classification* case (sentiment, intent). If that literature does not exist as a coherent body, then the author has identified a genuine gap. My current read is that the gap exists but is not large enough to constitute a new field — it is a new application domain within existing fields. To change my mind, I would need to see that the action context produces qualitatively different phenomena than the estimation context, not just quantitatively different ones. The boundary abstention behavior is a candidate for this — it is a categorical behavioral switch that doesn't have a direct analog in the probability expression literature. If Study 2 shows that humans do not exhibit analogous abstention behavior (i.e., humans would try to act even near boundaries), that would establish the action context as genuinely different.

**On the paper carrying the field:** Show me the result replicated across at least three models with different training procedures (one open-weights, one closed), across at least two domains with different constraint structures, with a human baseline showing a measurable gap between human intent and model action. That four-element package — multi-model, multi-domain, human baseline, demonstrated gap — would make the paper load-bearing. Any one of those elements alone would substantially strengthen the case.

**On the "passive failure" framing:** The framing becomes credible the moment you have a human baseline showing that humans would have acted differently. Right now, the failure is asserted. If humans also compress "slightly" and "marginally" into the same output, the model is not failing — it is accurately representing genuine ambiguity. If humans reliably distinguish these words and the model does not, you have a documented failure. Run the survey. That is the single most important next step, and it is cheap.

---

## Honest Confidence Assessment

**My case that the field is derivative: 7/10.** The existing literature is real and relevant. The author is not discovering a new phenomenon — they are measuring it more cleanly than it has been measured before. The "new field" framing is not supported. However, I am reaching slightly when I claim the boundary abstention behavior has direct precedents. I have not found a clean prior example of word-dependent categorical action switching in a constrained tool-use context. That specific finding may be genuinely novel at the mechanistic level, even if the broader phenomenon is not.

**My case that the paper can't carry the field: 9/10.** This is my strongest argument and I am not reaching. One model, one domain, no human baseline, synthetic environment — these are not minor limitations. They are structural constraints on what the paper can claim. The paper is a solid first result. It is not a founding instrument. The gap between "solid first result" and "founding instrument" is exactly the gap the author's inflation tendency fills with narrative.

**My case that the brief is already inflating: 8/10.** The evidence is in the author's own words. The "passive failure" naming, the domain-generalization claims, the "window into something bigger" framing — these are the inflation pattern in action. The author knows this. The brief's self-awareness is real. But self-awareness of a failure mode is not the same as not doing the thing.

**Where I am weakest:** I cannot fully evaluate the claim that the *action* context is categorically different from the *estimation* context without more data. If it turns out that boundary-dependent abstention is a robust, model-general, domain-general phenomenon that only appears when vague language must produce a *consequential action* (not an estimate), then the author has found something genuinely new. I am arguing against that claim because the current evidence doesn't support it — not because I am certain it is false.

**The honest summary:** The author has a clean methodological contribution and one genuinely sharp finding (the boundary abstention behavior). The inflation is in the framing, not the data. The data is real. The field claim is not. The path forward is to let the data be what it is — a controlled measurement of a specific behavioral property — and build the second paper that either establishes the human gap or establishes cross-model generality. Either of those would be a real contribution. Neither requires founding a field.

### 3. Research Sequencer

# Research Sequencer Advisory: Strategic Review

## Bucket A vs. Bucket B Assessment

The author's split is approximately right but has two miscategorizations worth correcting.

**The split is correct in spirit.** Bucket A (human baseline, cross-model, denser grid) builds the empirical foundation. Bucket B (valence framing, stakes magnitude, cross-domain transfer) stakes claims about what the phenomenon means. You cannot credibly stake claims without the foundation. The instinct to separate them is sound.

**Miscategorization 1: Cross-model belongs in Bucket B, not Bucket A.**

This is the most important correction. Cross-model comparison feels like a credibility move because it looks like replication — "does this hold across models?" But strategically, it functions differently. If you find that GPT-4o and Gemini Flash show the *same* compression pattern, you've made a claim about the universality of the phenomenon, which is a field-defining move. If you find they differ, you've made a claim about how training and alignment shape vague-language interpretation — also field-defining. Cross-model is not a replication study; it's a theoretical claim about whether this is a property of the model class or a property of the language-action interface itself. Running it second, before you have a human baseline, means you're comparing models to each other without an anchor. That's a weaker paper than it could be.

Cross-model should be Paper 3, after the human baseline establishes the anchor.

**Miscategorization 2: The denser baseline grid is not Bucket A credibility — it's infrastructure.**

The denser grid isn't a publishable paper on its own. It's data collection that enables other papers. Treat it as a resource investment that runs in the background, not as a paper in the sequence. If you collect it while executing Paper 2, you have it available for Paper 3 without it consuming a publication slot.

**Miscategorization 3: The valence 2x2 is not cleanly Bucket B.**

The author frames valence (increase vs. decrease) as a field-defining move. I'd push back. Testing decrease instructions is a direct, obvious extension of Paper 1 — the paper itself flags it as a limitation. Asymmetry between increase and decrease is a credibility-building result, not a field-defining claim. It belongs in Bucket A. The *framing* of valence as a safety-relevant phenomenon is Bucket B, but the empirical test itself is Bucket A.

**Revised Bucket Structure:**

- **Bucket A (credibility):** Human baseline survey, valence asymmetry (increase vs. decrease), denser grid (as infrastructure), no-word control
- **Bucket B (field-defining):** Cross-model comparison (after human anchor), cross-domain transfer, stakes magnitude framing
- **Reclassified:** Cross-model moves from A to B; valence moves from B to A

---

## Recommended Sequence (Next 3-5 Papers)

### Paper 2: Human Baseline + Valence Asymmetry (Combined Study)

**Why first:** The paper's single most damaging limitation is the absence of a human comparison. Every reviewer who reads Paper 1 will ask: "But do humans do the same thing?" You cannot answer the question "is this model failure or genuine linguistic ambiguity?" without this data. Until you answer it, every subsequent paper is built on an unstable foundation.

The strategic move is to combine the human baseline with the valence extension (decrease instructions) in a single study. Here's why combining is correct: both require the same word scale, the same task framing, and the same statistical apparatus. Running them separately wastes a publication slot on what would be a thin paper. Together, they produce a paper with two genuine contributions: (1) the human-model comparison that closes the ordinality validation gap, and (2) the asymmetry result that extends the phenomenon to a new action direction. This is a paper that can stand on its own.

The human baseline also does something strategically critical: it reframes the entire research program. If humans show the same compression, the story becomes "this is a fundamental property of vague language, and models inherit it." If humans show finer discrimination, the story becomes "models are worse than humans at this specific task." Either result is interesting, but you cannot make the claim without the data. Getting this data in Paper 2 means every subsequent paper can speak to the human-model gap rather than hedging around it.

**What this paper needs to demonstrate:** That the human ordinal structure is measurable, that it differs from the model's compression in at least one meaningful way, and that the decrease direction produces a different pattern than increase.

**What it creates for Paper 3:** An anchor. You now have a human ground truth against which cross-model results can be compared. Instead of "Model A vs. Model B," Paper 3 becomes "Model A vs. Model B vs. Human Baseline" — a much stronger framing.

### Paper 3: Cross-Model Comparison (with Human Anchor)

**Why third:** With the human baseline established, cross-model becomes a test of a real theoretical question: do different training procedures and alignment methods produce different language-to-action mappings, and how do those mappings relate to human interpretation? This is no longer a replication study — it's a study of how model design choices shape the language-action interface.

The specific theoretical question worth asking: does the compression pattern correlate with model size, RLHF intensity, or training data composition? You won't be able to answer this definitively, but you can generate hypotheses. A finding that instruction-tuned models show more compression than base models (or vice versa) would be genuinely interesting to the alignment community.

**Resource note:** This is the first paper in the sequence that has real API cost. Running the full protocol across GPT-4o, Gemini Flash, and one other frontier model at the same scale as Paper 1 could run $500-1500 depending on current pricing. This is manageable on a self-funded budget but requires planning. Haiku-equivalent tiers of each model family are the right target — you're studying the phenomenon at the deployment tier, not the frontier tier.

**What this paper needs to demonstrate:** That the compression pattern varies across models in ways that are interpretable, and that the human baseline from Paper 2 provides a meaningful reference point for evaluating model behavior.

**What it creates for Paper 4:** A cross-model result means you can now speak to the phenomenon at the level of the model class, not just one model. This is the foundation for the field-defining move.

### Paper 4: The Field-Defining Move — Passive Failure at the Action Interface

**Why fourth:** This is the paper that makes the claim. By Paper 4, you have: (1) the original phenomenon documented across 6,620 runs, (2) a human baseline that characterizes the linguistic ground truth, (3) evidence that the phenomenon varies across models in interpretable ways, and (4) a valence asymmetry result that shows the phenomenon generalizes across action directions. You now have enough empirical ground to stake the claim that this is a systematic property of language-action interfaces, not an artifact of one model or one domain.

The paper's core argument: vague intensity words are a broken control interface for autonomous systems. The failure mode is passive — the model isn't refusing or hallucinating; it's silently mistranslating intent. The human-model gap quantifies the cost of this mistranslation. The cross-model variation suggests it's tractable — some training procedures produce better-calibrated interfaces than others.

**What this paper needs to demonstrate:** A theoretical framework, not just more data. This is where "passive failure at the action interface" gets defined, operationalized, and connected to existing alignment literature. The empirical foundation is already built; this paper synthesizes it.

**Venue target:** This is the paper that aims at a workshop at NeurIPS or ICLR — specifically the alignment or safety workshops. Algoverse's track record at these venues is the relevant asset here.

### Paper 5 (Optional/Conditional): Cross-Domain Transfer

**Why fifth and conditional:** Cross-domain transfer (healthcare dosing language, financial risk language, logistics scheduling language) is the paper that makes the program genuinely important rather than a niche result about resource allocation. But it requires either (a) domain expertise you don't have, (b) collaborators who do, or (c) synthetic environments you'd need to build from scratch. This paper is only worth pursuing if Paper 4 lands and creates pull — if reviewers and readers ask "does this hold in healthcare?" you have a natural next move. If Paper 4 doesn't land, this paper is premature.

**Conditional trigger:** Pursue Paper 5 only if Paper 4 gets accepted at a workshop or generates significant community interest. Otherwise, the program has sufficient depth at four papers.

---

## The Wedge Paper

**The wedge is Paper 2: the human baseline.**

Here's why this is the highest-leverage single result: every other paper in the sequence depends on knowing whether the model's compression reflects genuine linguistic ambiguity or model-specific failure. Without the human baseline, you're always hedging. With it, you can make claims.

The wedge paper creates three specific conditions that make the rest inevitable:

1. **It closes the ordinality validation gap.** The word scale is currently researcher-constructed. Once you have human data, it's validated. Every subsequent paper that uses the scale is now on firmer ground.

2. **It reframes the research question.** "Does the model compress vague intensity words?" becomes "Does the model compress vague intensity words *more than humans do*?" The second question is more interesting, more publishable, and more directly relevant to alignment. You cannot ask the second question without the first study.

3. **It creates a reference point for cross-model comparison.** Without a human anchor, cross-model comparison is just "Model A vs. Model B." With it, you can ask "which model is closest to human calibration?" — a question with direct deployment relevance.

The human baseline is also the paper that most credibly answers the "so what?" question. Right now, the "so what?" is "the model compresses words." After the human baseline, the "so what?" is "the model compresses words in ways humans don't, and here's the quantified gap." That's a stronger claim, and it's the one that makes downstream papers feel necessary rather than incremental.

One additional strategic point: the human baseline is the paper that most directly addresses the "is this model failure or linguistic ambiguity?" objection — which is the single most likely dismissal of Paper 1. Getting this data early means you're not defending against that objection for the rest of the program.

---

## Paper Two Deep-Dive

**The recommendation is human baseline + valence asymmetry as a combined study. Here is the argument against each alternative.**

**Against valence alone as Paper 2:**

Valence alone (increase vs. decrease) is a thin paper. The finding would almost certainly be "yes, there's asymmetry" — which is interesting but not surprising. More importantly, it doesn't close any of the major open questions from Paper 1. Reviewers who read Paper 1 will not be satisfied by a paper that adds one new condition without addressing the human comparison gap. Valence alone as Paper 2 looks like salami-slicing.

**Against cross-model as Paper 2:**

Cross-model without a human anchor is a comparison without a reference point. You'd be saying "Model A compresses differently than Model B" — but differently relative to what? Relative to each other, yes, but that's a weak claim. The interesting claim is "Model A is closer to human calibration than Model B" — and you can't make that claim without the human data. Running cross-model second means you've spent significant API budget on a result that will be immediately weakened by the absence of a human baseline.

There's also a strategic sequencing problem: if you run cross-model second and the results are interesting, you'll want to add the human baseline to the paper anyway. You'll either have to run the survey after the fact (making the paper feel retrofitted) or publish without it (making the paper feel incomplete). Better to get the human baseline first.

**Against human baseline alone as Paper 2:**

A pure human baseline survey — "here's what humans say these words mean numerically" — is a psycholinguistics paper, not an AI paper. It's publishable, but it doesn't advance the research program as efficiently as a combined study. The human baseline is most valuable as a comparison point against the model, not as a standalone result.

**For the combined study:**

Human baseline + valence asymmetry in a single paper does three things: (1) validates the word scale, (2) provides the human-model comparison that closes the main gap from Paper 1, and (3) extends the phenomenon to decrease instructions. The valence component also makes the IRB protocol more efficient — you're running participants through a richer task rather than a minimal one, which is better use of participant time and your effort.

**The one risk:** Combined studies can feel unfocused. The solution is a clear framing that ties the two components together. The framing is: "We characterize human interpretation of these words (baseline) and then test whether the asymmetry between increase and decrease instructions — which humans likely show — is preserved or distorted in the model." That's a coherent paper with two contributions.

---

## Resource & Feasibility Assessment

**What can be done solo:**

- **Valence extension (decrease instructions):** Fully solo. Same harness, same API, same analysis. Marginal cost relative to Paper 1. Can be collected in a weekend.
- **Denser baseline grid:** Solo. API cost is the only constraint. At Haiku pricing, a full 0-100 grid at 30 runs per cell × 10 words × 2 temperatures = 60,000 runs. At current Haiku pricing this is probably $50-150. Collect it as infrastructure while executing other work.
- **No-word control:** Solo. Trivial addition to the existing harness. Should have been in Paper 1; include it in Paper 2.
- **T=1.0 analysis:** Solo. Already collected per the paper. Analyze and include in Paper 2 or as a supplement.

**What requires collaboration or IRB:**

- **Human baseline survey:** Requires IRB review at Georgia Tech. The paper already notes this is in preparation. The IRB process at GT typically takes 4-8 weeks for minimal-risk studies; a survey study with no deception and no sensitive data is minimal risk. This is the primary blocking dependency for the sequence. Start the IRB application now — it runs in parallel with other work.
- **Cross-domain transfer:** Requires domain expertise you don't have. Healthcare dosing language, financial risk language — you need a collaborator with domain knowledge to validate that the synthetic environment is realistic. This is where Algoverse becomes critical.

**What requires significant compute:**

- **Mechanistic interpretability:** The author asks about this. The honest answer: mechanistic interpretability of the compression phenomenon would require activation patching, attention analysis, and potentially training probes on intermediate representations. This is not Haiku-scale API work — it requires model weights, which means either open-source models (Llama, Mistral) or significant collaboration. This is the right question eventually but the wrong move now. It pulls you away from the deployment-facing empirical work and into a different research community with different norms. Defer.
- **Cross-model at scale:** Running the full protocol across 3-4 models is feasible solo but requires budget planning. Estimate $500-1500 for Paper 3. Not a blocker, but requires conscious resource allocation.

**Algoverse leverage:**

The fellowship is most valuable for two specific things: (1) access to PIs who can co-author or advise on the field-defining paper (Paper 4), and (2) access to collaborators who can provide domain expertise for cross-domain transfer (Paper 5). The credibility papers (2 and 3) can be executed largely solo with mentorship. The field-defining paper benefits from having a more senior co-author who can vouch for the framing and help target the right venue. Bring Paper 4's framing to your PI now — not for execution, but for feedback on whether the "passive failure at the action interface" framing is the right one for the venues you're targeting.

**What to stop pretending you can do alone:**

Cross-domain transfer with real domain validity. You can build synthetic healthcare or finance environments, but without a domain expert co-author, reviewers will correctly note that the environments may not capture how vague instructions actually function in those domains. This paper requires collaboration. Do not attempt it solo.

---

## Timeline & Venue Strategy

### Paper 2: Human Baseline + Valence Asymmetry
- **Execution time:** 3-4 months (dominated by IRB timeline, not data collection)
- **IRB application:** Start immediately; 4-8 weeks for approval
- **Survey data collection:** 2-3 weeks after IRB approval (Prolific or MTurk, ~200 participants, ~$400-600 in participant costs)
- **Valence data collection:** 1-2 weeks (solo, API-based)
- **Analysis and writing:** 4-6 weeks
- **Target venue:** *Cognitive Science* (if the human comparison finding is strong), or a computational linguistics venue like *ACL Findings* or *EMNLP*. Alternatively, an AI safety workshop at NeurIPS or ICLR if the human-model gap is large and interpretable. The venue choice depends on the finding: if humans show the same compression, the story is linguistic and belongs at a linguistics venue; if humans show finer discrimination, the story is about model failure and belongs at an AI venue.
- **What it needs to demonstrate:** A measurable human ordinal structure, a

### 4. Alignment Insider

This is sufficient. I now have what I need for a fully grounded strategic review. Let me deliver it.

---

# Alignment Insider: Strategic Review of Danny Tabach's Research Program

*Adversarial deliberation requested. Narrowing, not expansion, is the mandate.*

---

## Community Reception Assessment

**The honest read: this will be received as a useful empirical NLP result wearing an alignment coat. The alignment sticker will not be free.**

Here is what will happen when an alignment researcher reads this paper. They will see a well-executed behavioral experiment on a single model in a single synthetic domain. They will appreciate the controlled design. Then they will ask the question that determines reception: *does this tell me something about alignment that I couldn't already infer from what I know about LLM behavior generally?* A significant fraction will answer no. They will say: "Of course LLMs are inconsistent with vague language. Of course context dominates. This is a prompt sensitivity result with a resource allocation wrapper."

The alignment community's current center of gravity on agentic problems is focused on systems that "develop behaviors or objectives that conflict with designers' or operators' goals" — particularly in tool-using, multi-step environments where agents pursue instrumental aims including deception, collusion, or specification gaming. Your paper is about something structurally different: not a model pursuing misaligned goals, but a model failing to faithfully translate a user's linguistic intent into a numeric action. That is a real problem. But the community's gatekeepers will need to be convinced it belongs in *their* tent, not in the NLP or HCI tent.

**The reception risk is specific:** reviewers at alignment-focused venues will ask whether this is a *safety* problem or a *usability* problem. They will point out that the model isn't scheming, isn't deceiving, and isn't pursuing misaligned goals — it's just imprecise. That's a meaningful distinction in this community's current framing. You will need a sharp answer to that question before you submit anywhere that calls itself an alignment venue.

**What works in your favor:** The "drastically" → "dramatically" flip — where swapping one near-synonym causes the model to switch from acting to abstaining in the same state — is genuinely surprising and memorable. That single finding is your strongest hook. Lead with it everywhere. It is the empirical result that most clearly demonstrates that the failure mode is *discontinuous* and *invisible*, not merely noisy. That is the finding that separates this from generic prompt sensitivity work.

**What works against you:** One model (Claude Haiku), one domain, no human baseline. The community will want to know if this is a Claude Haiku artifact. They will want to know if humans would compress these words the same way. Without those comparisons, the paper's claim about alignment risk rests on a single data point in a synthetic environment. That is a real limitation and reviewers will name it.

---

## Audience Recommendation

**Target the NLP/deployment-safety audience first. Do not lead with alignment.**

This is the narrowing you asked for. You cannot serve alignment, HCI, and NLP simultaneously with this paper. You need to pick a lane, establish credibility there, and then cross over.

The right first audience is the NLP safety and evaluation community — specifically, researchers working on LLM behavioral consistency, prompt sensitivity, and deployment-facing reliability. This community will read the paper on its own terms. They will evaluate the experimental design, the statistical approach, and the generalizability of the findings. They will not demand that you solve deception or scheming. They will ask: *is this a real behavioral phenomenon, is it measured carefully, and does it matter for deployed systems?* Your paper can answer all three of those questions.

Workshops focused on AI safety drew significant attention at NeurIPS 2025, with large language models being deployed at scale in consumer products making questions about alignment, robustness, and safe behavior no longer theoretical. That's the current appetite. But notice the framing: "robustness and safe behavior" — not "deception and scheming." Your work fits the former frame better than the latter.

The alignment community is your *second* audience, not your first. Once you have a publication record in NLP safety, you can bring the work to alignment venues with the credibility of having already passed peer review in a rigorous technical community. Trying to enter alignment venues first, as an independent researcher with one preprint, is a harder path.

---

## Venue Strategy

**One paper, one venue. Do not fragment this into three simultaneous submissions.**

**Stage 1 (now): EMNLP 2026 or ACL 2026 — findings track or main conference**

This is the right first venue. EMNLP and ACL have strong traditions of empirical behavioral work on LLMs. The paper's controlled design, nonparametric statistics, and behavioral framing fit the NLP community's evidence standards. The "does slightly mean somewhat?" framing is exactly the kind of question that gets traction at these venues. The linguistic grounding (Quirk taxonomy, degree modifiers) is a genuine differentiator — most NLP safety papers don't have that theoretical scaffolding.

What you need to add before submission: a human baseline (even a small-n survey), at least one additional model for comparison, and a no-word control condition. Without these, the paper is a first slice, not a complete study. The human baseline is the single highest-leverage addition — it either shows that humans also compress these words (in which case the model is reflecting genuine linguistic ambiguity) or it shows that humans differentiate them (in which case the model has a specific failure). Either result is publishable. The ambiguity of not knowing is not.

**Stage 2 (after Stage 1 publication): NeurIPS SoLaR or COLM SoLaR workshop**

The SoLaR workshop is an interdisciplinary gathering that aims to foster responsible and ethical research in language modeling, recognizing significant risks from development, deployment, and use of language models, and bringing together experts from various domains with a shared commitment to promoting fairness, accountability, transparency, and safety. This is the right second venue. By the time you submit here, you should have the multi-model comparison and the human baseline. The SoLaR framing — deployment safety, socially responsible LM research — fits your work better than the core alignment workshops, which skew toward deception, scheming, and model internals.

**Stage 3 (cross-model study as a second paper): FAccT or AIES**

FAccT is the right venue for a second paper that establishes the cross-model pattern and connects to deployment consequences in high-stakes domains. FAccT reviewers care about real-world harm, not theoretical alignment risk. A paper showing that multiple frontier models exhibit the same compression pattern, with a human baseline showing that humans *don't* compress these words the same way, is a strong FAccT submission.

**Do not target CHI.** CHI will ask for user studies, interface designs, and interaction data. Your paper has none of that. CHI is the wrong community for this work at this stage.

**Do not target core NeurIPS or ICML main conference.** Not yet. You don't have the cross-model generalizability or the theoretical contribution that main conference reviewers at those venues will require.

---

## "Passive Failure" in Alignment Discourse

**The framing is not recognized as a term of art. It is recognized as a phenomenon. That gap matters.**

The alignment community does not have an established concept called "passive failure at the action interface." What it does have is a rich literature on specification gaming, reward hacking, and Goodhart's Law — all of which involve a model doing something other than what the operator intended. Research on specification gaming shows that open-ended language causes otherwise-constrained models to bypass rules, and that vague or underspecified objectives lead to environment or policy hacking. Your "passive failure" framing is adjacent to this but distinct: you're not describing a model gaming a specification, you're describing a model failing to faithfully execute a specification because the specification was expressed in vague natural language.

That distinction is real and worth preserving. But "passive failure" as a label will not resonate with most alignment researchers on first contact. It sounds like a euphemism for "the model is bad at this." The framing that will resonate better is **"semantic compression at the action boundary"** or **"intent-action fidelity"** — language that connects to the community's existing vocabulary around faithful execution and instruction following.

The deeper issue is this: the alignment community is currently focused on *active* failures — strategic reasoning about objectives, context, and safety apparatus, resulting in alignment faking, cooperation with adversarial actors, or active sabotage. Your work is about a failure mode that doesn't require any of that. The model isn't trying to do anything wrong. It's just imprecise. That is a harder sell to a community that has trained itself to worry about sophisticated adversarial behavior.

**The reframe that opens doors:** Stop calling it "passive failure" in alignment venues. Call it a problem of **operator intent preservation** — the question of whether a deployed system faithfully executes the operator's intended semantics, not just the surface form of their instruction. This connects to Anthropic's explicit language about steerable, trustworthy AI and to the broader concept of corrigibility. It's a harder problem than it looks, and your paper is the first controlled measurement of it.

---

## Potential Allies & Collaborators

**Be specific. Don't cold-email everyone. Pick two.**

**The most natural intellectual ally is the prompt sensitivity research community.** The BrittleBench line of work (which your paper already cites) is the closest existing research program. The researchers behind that work are studying whether semantically equivalent paraphrases produce different outputs; you're studying whether semantically distinct intensity words produce stable outputs. These are complementary questions and the methodological overlap is significant. Find the authors of the BrittleBench paper and reach out with a specific, short message: "I've extended the prompt sensitivity question to the action case — here's what I found."

**Within the alignment community, the most natural entry point is through Algoverse.** MATS alumni-founded organizations include Algoverse AI Safety Fellowship, which means the Algoverse network has direct connections into the MATS and Anthropic ecosystems. You are already inside this network. Use it. Ask your Algoverse PIs specifically: who at Anthropic or Redwood is working on instruction following reliability or agentic safety evaluations? That is the warm introduction you need, not a cold ArXiv ping.

**The AgentAlign and AgentSafetyBench research groups** are working on adjacent problems. AgentHarm presents a benchmark focusing on explicitly malicious agent tasks, while AgentSafetyBench offers an evaluation framework with 2,000 test cases examining safety risks across different stages of agent operation. These groups are measuring safety failures in agentic systems, but they're focused on harmful outputs, not on semantic compression of legitimate instructions. Your work is complementary, not competitive. Reach out to the AgentSafetyBench authors with that framing.

**Do not try to connect with MIRI or ARC at this stage.** Their research programs are focused on theoretical alignment and formal verification, respectively. Your empirical deployment work is not in their wheelhouse and they are not in yours.

---

## Fellowship & Career Positioning

**Your profile is stronger than you think for one specific fellowship and weaker than you think for another.**

**MATS: Realistic, but requires a specific pitch.**

MATS seeks individuals deeply motivated by AI security, alignment, and governance with the skills and mindset to contribute to cutting-edge research. With only about 4-7% of applicants ultimately selected, the program is highly competitive. Successful applicants demonstrate clear mission alignment, a track record of research or competency relevant to their chosen stream, and credible references.

Your profile — working data scientist, master's student, one ArXiv preprint, Algoverse fellow — is exactly the kind of non-traditional background that MATS says it welcomes. MATS explicitly looks for talent that traditional pipelines might overlook and welcomes technical researchers without prior ML experience who can demonstrate strong reasoning and research potential.

What you need for MATS is a credible answer to: "Which stream are you applying to, and why does your work connect to that stream's research agenda?" The Anthropic stream spans a range of empirical research areas in AI safety including AI control, scalable oversight, model organisms, model internals, model welfare, and security. Your work is closest to the "model organisms" and "AI control" streams — specifically, the question of whether deployed systems faithfully execute operator intent. Frame your application around that connection, not around "passive failure."

MATS looks for evidence of research ability, ideally in relevant areas, with outputs such as publications, blog posts, open-source projects, or substantial research contributions. Your ArXiv preprint is your evidence of research ability. The Algoverse fellowship is your evidence of community engagement. The JPMorgan production system is your evidence that this work comes from a real deployment problem, not a toy exercise. That combination is genuinely distinctive.

**Anthropic Fellows: Harder, but not impossible.**

Anthropic cares much more about ability to execute on research than credentials. Strong candidates can code well in Python, take ambiguous problems and make concrete progress, and think clearly about hard technical questions. They explicitly say you don't need a PhD, prior ML experience, or published papers.

Your obstacle at Anthropic is not credentials — it's fit. Anthropic's current priority areas include scalable oversight, adversarial robustness and AI control, model organisms, mechanistic interpretability, AI security, and model welfare. Your work doesn't cleanly map to any of these. The closest is "model organisms" — but Anthropic's model organisms work is focused on creating controlled demonstrations of specific misalignment phenomena (alignment faking, scheming). Your work is measuring a different phenomenon. You would need to reframe your research agenda around creating a model organism of *intent-action infidelity* — a controlled demonstration that vague operator instructions reliably produce misaligned actions in specific, predictable conditions. That reframe is possible, but it requires you to think about your work differently.

**The fellowship to target first is MATS, not Anthropic.** MATS is the on-ramp. Anthropic is the destination you work toward after MATS.

---

## Community Appetite & Timing

**The timing is genuinely good for deployment-facing empirical work. But you're competing with a crowded field.**

Workshops focused on AI safety drew significant attention at NeurIPS 2025, with large language models being deployed at scale in consumer products making questions about alignment, robustness, and safe behavior no longer theoretical. The community has shifted meaningfully in the last 18 months toward deployment-facing empirical work. The question used to be "will AI systems be misaligned in theory?" It is now increasingly "are deployed AI systems behaving reliably in practice?" Your work is in the second category.

Empirical studies have converged on realistic RL and tool-use environments to elicit and quantify agentic misalignment. The community is hungry for controlled, reproducible experiments that demonstrate specific failure modes. Your paper has that. The synthetic environment is a feature, not a bug — it makes the result clean and interpretable in a way that real-world deployment logs cannot.

The risk is not that you're too early. The risk is that you're in a crowded space. Submitting on a hot topic like AI safety or LLM evaluation can be advantageous because there are more workshops accepting papers in those areas, but it also means more competition. The key is to bring a specific angle or insight that existing work has not addressed. Your specific angle — the *action interface*, not the *output quality* — is genuinely underexplored. The community has studied harmful outputs, hallucinations, and jailbreaks extensively. It has studied much less the failure mode where a benign instruction is silently mistranslated into a different numeric action.

---

## Political Landscape

**Three camps, one territorial dispute, one strategic opportunity.**

**Camp 1: The x-risk / deception-focused alignment researchers.** This is the dominant camp at MIRI, ARC, and in the Anthropic alignment science team. They are focused on scheming, deception, and power-seeking. This stream focuses on building a science of scheming: empirically studying oversight gaming, alignment faking, and

### 5. Career Strategist

# Career Strategy Review: Danny Tabach

---

## Honest Position Assessment

**Where you actually stand:**

You are a non-traditional researcher with a stronger profile than you probably believe and more significant gaps than you're comfortable admitting. Let me be precise about both.

**What's working in your favor:**

Your profile has a coherent story that most early-stage researchers lack. You built a production system, noticed a real failure mode in it, designed a controlled experiment to measure that failure mode, and produced a preprint with clean empirical results. That origin story — practitioner-to-researcher, motivated by a real deployment problem — is genuinely differentiated. Most alignment researchers come from ML or philosophy backgrounds and theorize about deployment problems they've never encountered. You've encountered one. That's not nothing.

The Algoverse fellowship is real signal. It's selective, it has a track record of mentoring researchers to top venues, and it gives you something most independent researchers lack: a named institutional affiliation, access to PIs, and a collaborative infrastructure. When a fellowship committee looks at your CV, "AI Safety Research Fellow at Algoverse" reads better than "independent researcher." Don't underestimate this.

Your JPMorgan work is also real signal, but it's double-edged. It demonstrates you can build systems that matter at scale. It also raises the question in an academic committee's mind: *is this person a researcher or a practitioner writing papers?* The answer to that question is not yet settled by your profile.

**The gaps — stated directly:**

One preprint is not a research trajectory. It's a starting point. Fellowship committees funding research programs want to see evidence that you can sustain a research direction across multiple papers, not just execute one well-designed study. You don't have that yet. This is your most significant gap, and it's the one you can actually close in the next 12 months.

Your paper is single-model, single-domain, single-action-direction. These are acknowledged limitations, but they matter more than you may realize for how the work is received. The findings are real, but their generalizability is genuinely unknown. A reviewer who wants to dismiss the work can do so by pointing at Claude Haiku and a synthetic allocation environment. Your next paper needs to make that dismissal harder.

You have no co-authors, no citations from others, and no evidence of engagement from the community you're trying to enter. The paper is on ArXiv but has not yet been tested by peer review or community response. You don't yet know if the people whose opinion matters think this work is interesting. That's information you need.

Your master's is finishing, which is both an asset (you'll have the credential) and a transition risk (you'll lose your Georgia Tech affiliation unless you're careful about timing). Plan for this.

---

## What You Cannot Do Alone

Be honest with yourself about which parts of the planned program require things you don't have:

**The human baseline survey requires IRB approval.** You acknowledge this in the paper. This is not a minor procedural step — IRB review at Georgia Tech takes time, requires proper protocol design, and must be completed while you still have institutional affiliation. If you're finishing your master's in the near term, the window for doing this under Georgia Tech's IRB may be shorter than you think. This is the single most time-sensitive dependency in your entire research program. Miss this window and the human comparison study either gets delayed by years or requires finding a new institutional sponsor.

**Cross-model comparison requires API budget you may not have.** Running the same 6,620-run protocol on GPT-4o, Gemini Flash, and other frontier models multiplies your API costs by the number of models. This is manageable but not free. Budget this explicitly before committing to it as the next study.

**Mechanistic interpretability requires compute and expertise you don't have.** If you pursue the mechanistic interp direction — looking inside the model to understand why compression happens — you need either GPU access for activation analysis or collaboration with someone who has it. You cannot do serious mechanistic work on API calls alone. This isn't a direction you can pursue solo with your current resources. This is the honest answer to your question about whether to pursue it.

**Getting the work into a peer-reviewed venue requires navigating a process you haven't navigated yet.** ArXiv is not publication. The gap between a preprint and a workshop paper, and between a workshop paper and a full venue paper, is real. Algoverse mentors can help here, but you need to actively use them for this.

**Building a "recognized voice" requires community engagement you haven't started.** Visibility doesn't happen from ArXiv alone. It requires showing up — at workshops, on forums, in conversations. This takes time that competes with research time.

---

## Fellowship Strategy

**Which fellowships are realistic targets:**

Given your profile — master's finishing, one preprint, Algoverse fellowship, industry background — the realistic near-term targets are:

*Strong fits:*
- **Open Philanthropy AI Fellowship / LTFF grants** — These fund independent and non-traditional researchers explicitly. Your practitioner background is a feature, not a bug, for funders who care about deployment-facing safety research. The framing of your work as deployment safety rather than theoretical alignment is well-suited here.
- **Anthropic's academic programs** — You're studying their model. This is not a coincidence you should ignore. Anthropic has expressed interest in deployment safety research. A well-framed application that builds on the Claude Haiku findings and proposes cross-model extension is a natural fit.
- **MATS (ML Alignment Theory Scholars)** — Selective but accessible to non-traditional researchers with demonstrated research output. One preprint may be sufficient if the application is strong.
- **Redwood Research / ARC** — Less structured fellowship programs but open to researchers with empirical deployment safety work.

*Stretch targets that become realistic with a second paper:*
- NSF Graduate Research Fellowship (if you're still a student — check eligibility carefully given master's completion timeline)
- Any fellowship requiring demonstrated research trajectory rather than a single paper

**What fellowship applications need to demonstrate:**

Fellowship committees funding deployment safety research want to see three things you currently have in partial form:

1. **A coherent research question that matters.** You have this. The language-to-action interface question is real, deployment-relevant, and understudied. Don't let narrative inflation obscure it — the question is good enough without overselling it.

2. **Evidence you can execute.** You have one paper. You need two. The second paper doesn't need to be published before you apply — it needs to be in progress, described concretely, and plausibly completable.

3. **A reason to bet on you specifically.** This is where your practitioner background matters. You're not competing with PhD students on theoretical depth. You're competing on the claim that deployment safety research done by someone who has actually deployed systems will ask different questions and produce more practically relevant findings. Make that case explicitly.

**How to frame the application:**

Do not frame this as "I am studying vague intensity words in LLMs." Frame it as: "I am building a measurement framework for language-to-action translation failures in deployed AI systems, motivated by a real production failure I encountered, and I have initial empirical evidence that these failures are systematic, state-dependent, and invisible to operators." That's a research program. The first is a paper.

---

## Path to "Recognized Voice"

**What actually works for someone in your position:**

The path to being a recognized voice in deployment safety is not the same as the path to being a recognized academic researcher. They overlap but are distinct. Be clear about which one you're pursuing, because the tactics differ.

For deployment safety specifically, the community is small enough that direct engagement matters more than publication count. Here is what has worked for others in similar positions:

**The highest-leverage single action is getting a response from someone who matters.** Email Anthropic's alignment team about your findings on Claude Haiku. Not to ask for anything — to share a result that's directly about their model. If one person at Anthropic reads your paper and finds it interesting, that's worth more for your trajectory than 500 ArXiv downloads. Do this. Do it now. The paper is already on ArXiv.

**Write one non-academic piece that makes the core finding accessible.** Not a Twitter thread. A 1,500-word essay on the LessWrong / Alignment Forum that presents the finding in plain language, explains why it matters for deployment, and invites pushback. The alignment community reads these forums. This is where ideas get stress-tested before they become research programs. If your framing is right, you'll get engagement. If it's wrong, you'll find out faster than you would through peer review.

**Present at one workshop in the next 12 months.** NeurIPS, ICML, and ICLR all have safety and alignment workshops with lower acceptance bars than main tracks. A workshop paper or poster is a legitimate venue for your current work and puts you in a room with the people you want to know. Algoverse mentors can advise on which workshops are appropriate targets.

**Don't build a Twitter presence yet.** You don't have enough output to sustain it without diluting your signal. The researchers who built influence through Twitter did so after they had a body of work to point to. One preprint is not a body of work. Build the work first.

---

## Highest-Return Actions (6-12 Months)

I'm giving you a ranked list, not a menu. Do these in order.

**1. Complete the IRB application before you lose Georgia Tech affiliation (immediate, non-negotiable).**

This is the most time-sensitive action in your entire research program and the one most people in your position procrastinate on. The human baseline study is the single most important extension of your current paper. It closes the most significant gap in the work (no human comparison), it's methodologically cheap (a survey is low-cost relative to API runs), and it produces a result that either validates your framing or forces you to revise it. You need to know which. But you need IRB approval to do it, and you need institutional affiliation to get IRB approval. Do this now.

**2. Run the cross-model comparison study (months 1-3).**

This is the highest-leverage research extension given your resources. Same protocol, multiple models (GPT-4o at minimum, Gemini Flash if budget allows). The API costs are real but manageable. The payoff is substantial: if the compression and state-dominance patterns replicate across models, you've shown something about language-to-action translation that isn't Claude-specific. If they don't replicate, that divergence is itself a finding about how different training and alignment procedures shape vague-language interpretation. Either result is publishable. This is the study that turns one paper into a research trajectory.

**3. Submit the current paper to one workshop (months 2-4).**

Identify the most appropriate safety/alignment workshop at a major venue and submit. Your Algoverse mentors should help you identify the right target. The goal is not prestige — it's peer review, community exposure, and a line on your CV that says "peer-reviewed." A workshop acceptance is meaningful at your stage.

**4. Write the Alignment Forum post (month 1-2, can run parallel to above).**

One post presenting the core finding in plain language. Frame it as a question to the community, not a declaration. Ask: does this pattern generalize? Has anyone seen similar behavior in their deployments? You're not just broadcasting — you're gathering signal about whether the community thinks this is interesting and where they think it points.

**5. Email three people at AI labs whose work intersects yours (month 1).**

Anthropic (obviously, given the model), DeepMind's safety team, and one academic researcher whose work on LLM behavior you've cited or should have cited. Keep the email short: "I have a preprint on Claude Haiku's behavior at the language-to-action boundary. Given your work on [X], I thought you might find the boundary abstention findings interesting. Happy to discuss." You will get responses from some of these. Those responses are the beginning of a network.

**What not to do in the next 6 months:**

Do not pursue mechanistic interpretability. It requires resources and expertise you don't have, it pulls you away from the empirical deployment-facing work that is your actual contribution, and it would be a detour from building a research trajectory in the area where you have genuine advantage. The mechanistic questions are interesting. They are not your questions to answer right now.

Do not try to expand the "passive failure" framing into a grand theory. You identified this risk yourself. The framing is useful for motivation, but the next paper should be narrower and more decisive, not broader. Compression of the word scale and state-dominance of interpretation are empirical findings. Let them stand on their own before you build a theoretical superstructure.

Do not start the decrease-instructions study, the partial-context condition, and the denser baseline grid simultaneously. Pick one extension (the cross-model comparison) and complete it. Breadth at this stage is the enemy of publication.

---

## Unrealistic Assumptions

**You are assuming the "passive failure" framing will resonate with the alignment community as stated.**

It might not. The alignment community has specific priors about what constitutes an alignment problem, and "the model silently mistranslates vague intensity words" may read to some reviewers as a usability problem or an NLP problem rather than an alignment problem. This doesn't mean the framing is wrong — it means you need to test it before building your research program around it. The Alignment Forum post will tell you quickly whether the framing lands.

**You are assuming Algoverse gives you more than it does.**

Algoverse is a real asset, but it is not a substitute for institutional affiliation with a PhD program or a lab. It gives you mentorship, collaborators, and a named fellowship — all valuable. It does not give you IRB access (Georgia Tech does), compute (you still pay for API calls), or the kind of credentialing that comes from a PhD program. Be clear about what Algoverse provides and what it doesn't. Use it for what it's good for: mentorship on research direction, feedback on papers, introductions to collaborators, and advice on the fellowship application process.

**You are assuming one strong paper is enough to demonstrate a research trajectory.**

It isn't. Fellowship committees and lab hiring managers want to see that you can sustain a direction. Two papers with a coherent through-line are categorically different from one paper. The cross-model comparison study, if executed well, gives you that second paper. Until you have it, your profile reads as "promising start" rather than "researcher with a program."

**You are assuming the IRB timeline is flexible.**

It isn't. If you're finishing your master's in the near term, your window to conduct IRB-approved human subjects research under Georgia Tech's umbrella is closing. The human baseline study is the most important methodological gap in your current work. If you miss the IRB window, you either delay this study by years or find an institutional sponsor willing to cover you — which requires exactly the kind of network you're still building. Treat the IRB application as a hard deadline, not a future work item.

---

## The Impostor Syndrome Question

Here is the honest assessment you asked for.

Your work sits at a legitimate entry point to the deployment safety research community. It is not yet at the level of work that gets cited heavily or changes the field's direction. That's appropriate — it's a first paper from a non-traditional researcher without a PhD. The bar for entry is not "change the field." The bar for entry is "produce a controlled empirical result on a real question that the community hasn't answered." You've done that.

What you have that most early-stage researchers don't: a real deployment motivation, a clean experimental design, and a result that's empirically unambiguous within its scope. The paper doesn't overclaim. The limitations section is honest. The methodology is reproducible. These are not small things. Many first papers from PhD students at top programs are worse on these dimensions.

What you're still missing: generalizability evidence, peer review, community engagement, and a second paper. These are not permanent gaps — they're next-step gaps. The difference between where you are and where you need to be is 12 months of focused execution, not years of credential-building.

The impostor syndrome question has a specific answer in your case: you are not an impostor, but you are also not yet what you want to become. The gap is real and closeable. The path is narrow — cross-model replication, human baseline, workshop submission, community engagement — and it requires you to resist the narrative inflation you correctly identified as your failure mode.

The vision of "passive failure at the action interface" as a research program is not inflation. It's a legitimate framing of a real problem. The inflation risk is in trying to make *this paper* carry that entire vision. It can't. Your job for the next 12 months is to build the empirical foundation that makes the vision credible, not to argue for the vision before the foundation exists.

Do the cross-model study. File the IRB application. Submit to one workshop. Write one Alignment Forum post. Email three people. Everything else is secondary.

### 6. Skeptical PI

### Cornerstone Verdict: (c) — Something Between, Closer to (b) Than (a)

Let me be direct: this is a well-executed niche result that contains one genuinely interesting finding, dressed in framing that is reaching toward (a) but hasn't earned it yet.

Here's my actual read of what you have. You have three empirical observations. First, LLMs compress intensity vocabulary when mapping to numeric actions — coarse ordinality holds, fine distinctions collapse. Second, system state dominates word choice when context is present, by roughly 10:1. Third, near operational boundaries, the model switches behavioral modes discontinuously, and the drastically/dramatically flip is your sharpest example. These are real findings. They're clean. They replicate across temperature. The experimental design is genuinely clever — using a deterministic backend as a measuring instrument is the right move.

But here's where I pump the brakes on the "founding instrument" claim. None of these three findings is surprising to someone who has been in this space. Compression of vague language by LLMs is documented. Context dominance over lexical cues is expected — it's basically what grounding means. The boundary behavior is the most interesting finding and the one that's actually novel, but even there, the mechanism is unresolved and the generality is unestablished. What you've done is measure these phenomena cleanly in a controlled setting. That's a contribution. It's not a field.

The "passive failure at the action interface" framing is your attempt to elevate three behavioral observations into a theoretical construct. Right now, that construct is doing more work in the abstract than the data can support. The data shows compression, state-dominance, and mode-switching in one model, one domain, one action direction. The framing claims something about a general failure mode in human-AI action interfaces. That gap between what the data shows and what the framing claims is exactly the inflation you're worried about.

---

### What Makes a Founding Instrument

I've watched founding papers get made. Let me be specific about what they look like versus what you have.

Attention Is All You Need introduced a mechanism that was architecturally novel and showed it worked better than alternatives across multiple tasks. The founding claim was load-bearing because the mechanism itself was new. Reward Hacking and Goodhart's Law papers in alignment weren't single experiments — they were conceptual frameworks with enough theoretical structure that other researchers could derive predictions from them. Grice's original work on implicature wasn't an empirical paper at all — it was a theoretical framework so precise that it generated decades of testable predictions. Sparks of AGI from the Microsoft team was a founding instrument of a different kind — it was a systematic, multi-domain phenomenological survey that established a new object of study by sheer breadth of documentation.

What do these have in common? They either introduce a new mechanism, propose a theoretical framework with predictive power, or establish a new phenomenon with enough breadth and rigor that the community accepts it as a stable object of study.

What do you have? You have a well-controlled measurement of known phenomena in a specific setting. The experimental design is the contribution, not the finding per se. That's closer to a methods paper than a founding paper. A founding paper for "passive failure at the action interface" would need to do one of the following: establish that this failure mode is distinct from existing constructs (prompt sensitivity, miscalibration, grounding), show it across enough domains and models that it's recognizable as a stable phenomenon, or propose a theoretical account of why it happens that generates testable predictions. You have none of these yet. You have the first measurement slice, as you correctly say in the paper. That's honest. But the brief is reaching further than the paper.

---

### The Brief as Evidence

I want to say something careful here, because this is the most important thing I'll tell you.

Your brief is extremely well-written. The self-awareness is real — I can tell because it's specific. You name your failure mode precisely ("narrative inflation"), you pre-register your uncertainty ("I might be wrong about how big this is"), and you ask to be narrowed rather than expanded. That's not performative. Most people who come to me with inflated framings don't know they're inflating — they're genuinely convinced. You're not convinced, which is a good sign.

But here's the trap. Self-awareness can function as pre-emptive inoculation. By naming the failure mode in advance, you've made it harder for advisors to call it out — because you've already called it out yourself. The question is whether the self-awareness actually changes your behavior or just changes how you present. I can't fully answer that from a brief. But I notice that even after flagging narrative inflation as your failure mode, you still use phrases like "opens a window into something bigger," "failure modes rhyme across domains," and "passive failure at the action interface." Those are the moves of someone who is still, at some level, building the manifesto.

The test of genuine self-awareness is whether it constrains your next move. If the next paper you write is a cross-model replication with a human baseline and no new theoretical framing, that's evidence the self-awareness is load-bearing. If the next paper introduces a new domain, a new theoretical construct, and a new framing — all at once — that's evidence the self-awareness was decorative.

I'm not accusing you of bad faith. I'm saying: the brief is evidence that you understand the failure mode intellectually. Whether you've internalized it behaviorally is what the next twelve months will reveal.

---

### Program Survivability

I'll give you my honest probability estimate and then explain it.

My estimate: 40% chance this produces three or more papers in five years. That's not low enough to walk away, but it's not high enough to plan around.

Here's what kills it. The first threat is the single-model problem. You ran everything on Claude Haiku. That model will be deprecated. The next paper you write will either need to re-run on a new model (which means your baseline shifts) or explain why the results transfer. Either way, you're fighting a moving target. AI research timelines are brutal for empirical work that depends on specific model behavior — the model you studied may not exist in recognizable form by the time your third paper is under review.

The second threat is the domain trap. Your testbed is synthetic and clever, but it's one domain. The "passive failure" framing claims generality across healthcare, finance, logistics. Establishing that generality requires running the same protocol in multiple domains, which requires domain access, domain expertise, or collaborators who have both. You have one domain — the one you built at JPMorgan. Getting into healthcare or clinical settings requires IRB, clinical collaborators, and a much longer timeline than a year.

The third threat is the energy problem. You're a working data scientist finishing a master's degree. Research programs die when the researcher runs out of time, money, or motivation. The Algoverse fellowship gives you structure and mentorship, which helps. But I've watched people in your position produce one strong preprint and then get absorbed back into their day job. The question isn't whether you have the intellectual capacity — you clearly do. The question is whether you have the sustained protected time. What's your plan for that?

The fourth threat is the human baseline gap. You flagged it yourself, and it's real. Without knowing whether humans also compress these words, you can't distinguish "model failure" from "the words are genuinely ambiguous." That distinction matters enormously for the alignment framing. If humans show the same compression, your finding is about language, not about LLMs. That's still interesting, but it's a different paper with a different audience.

What keeps it alive: the production system origin is real, the experimental design is reusable, and the finding is clean enough to build on. If you stay disciplined and resist the temptation to expand the frame before you've deepened the foundation, this can sustain.

---

### Single Biggest Weakness

Not the most fixable one. The most fundamental one.

**You don't have a human baseline, which means you don't know what you're measuring.**

This is the issue that, if unresolved, makes the rest of the program interpretively unstable. Your central claim is that the model silently mistranslates vague intensity words — that there's a gap between what the user intends and what the model does. But you have no measurement of what users actually intend. You have a researcher-constructed word scale informed by Quirk et al., but Quirk describes linguistic taxonomy, not numeric intent.

Here's the problem in concrete terms. You find that "slightly" and "mildly" both map to 0.50 in the no-context condition. Is that compression? Or is it accurate? If you ran the same experiment with 50 human participants and they also both mapped "slightly" and "mildly" to roughly 50%, then the model is doing what humans do, and the finding is about language ambiguity, not model failure. If humans spread these words across a range (say, "slightly" → 10-20%, "mildly" → 25-35%), then you have evidence of genuine compression. You don't know which world you're in.

Everything downstream of this — the "passive failure" framing, the alignment implications, the claim that users can't wield these systems safely — depends on the answer. Without a human baseline, you're measuring the model against an assumed human intent that you haven't actually measured. That's a load-bearing assumption that the paper doesn't validate.

I know you flagged this as future work. I know you said IRB is in preparation. Do it first. Before the next experiment. Before the cross-model study. Before anything. The human baseline isn't just a gap to fill — it's the foundation the entire interpretive structure rests on.

---

### Single Biggest Strength

**You built the system you're studying, and you can see the failure mode from the inside.**

This is rarer than it sounds. Most alignment researchers study hypothetical failure modes or construct synthetic scenarios that approximate deployment. You looked at your own production system — a staffing optimization engine behind every Chase branch — and saw a real problem: a one-word change in a stakeholder instruction could silently move an action from cautious to maximal. That's not a constructed scenario. That's a deployed system with real consequences.

This gives you two things most people in this space don't have. First, you have genuine ecological validity. Your testbed is synthetic, but it's synthetic in the right way — it abstracts a real problem you actually encountered. When reviewers ask "does this matter in practice," you have a concrete answer that isn't speculative. Second, you have a practitioner's intuition about what the failure modes actually look like, which means you're less likely to study the wrong thing. Academic researchers often study failure modes that are theoretically interesting but practically rare. You're studying one you tripped over in production.

Lean into this. Hard. Every paper in this program should be anchored in the question: "what would a practitioner building a real system need to know?" That framing is your differentiator. It's also what makes this work legible to a broader audience — not just alignment researchers, but HCI people, software engineers, and the practitioners who are actually building these systems.

---

### If You Were My Student

Sit down. Here's what I'd tell you.

You've done something genuinely good. The paper is clean, the design is clever, and the production system origin gives it a credibility that most first papers lack. You should feel good about it. Now stop feeling good about it, because the next twelve months are where this either becomes something or doesn't.

Here's what I'd make you do before I'd support the "field" framing.

**First, run the human baseline study.** This is not optional. Get your IRB approved at Georgia Tech — you said it's in preparation, so finish that preparation. Design the survey carefully. Give the same 10 words to 50-100 participants in the same task framing. Ask them to assign a numeric allocation. Analyze whether humans show the same compression pattern you observed in the model. This single study either validates your framing or fundamentally changes it. Either outcome is publishable. Either outcome makes the next paper stronger. Do this before you run another model experiment.

**Second, stay in one domain.** I know you're tempted by healthcare and finance and logistics. Don't go there yet. You have one domain that you understand deeply — workforce allocation. Stay there until you've exhausted it. The cross-domain generalization claim is something you earn after three papers, not something you assert in the first one.

**Third, pick one extension, not five.** Your future work section lists six directions. That's a wishlist, not a research program. If I were your advisor, I'd make you pick one and defend why it's the most important. My vote: the human baseline plus a cross-model replication in the same domain, combined into a single paper. That's the paper that turns this from a single preprint into a research program. It closes the biggest weakness, extends the empirical base, and positions you to make the "passive failure" framing with actual evidence behind it.

**Fourth, be honest about what the drastically/dramatically finding actually is.** That finding — where swapping one near-synonym flips the system from acting to refusing — is your sharpest result. It's the one that's hardest to explain away. It's the one that practitioners will immediately recognize as a real problem. Lead with it. Build the next paper around it. Don't bury it in the boundary behavior section.

**Fifth, use Algoverse for what it's actually good for.** You have access to PIs and collaborators. Use them to pressure-test your framing, not to expand your scope. Bring your human baseline design to your PI before you run it. Ask them to tell you what's wrong with it. Ask them to name the paper that already did this. If they can name it, you need to know about it. If they can't, that's evidence you're in novel territory.

**On the "passive failure at the action interface" framing:** I don't hate it. It's evocative and it points at something real. But right now it's a hypothesis, not a finding. You can use it as a research program label — the thing you're building toward — but you shouldn't use it as the description of what you've already shown. What you've shown is three specific behavioral patterns in one model in one domain. The framing should follow the evidence, not precede it.

**On mechanistic interpretability:** Don't go there. Not because it's wrong, but because it pulls you away from your actual advantage, which is the deployment-facing empirical work. You're not a mechanistic interpretability researcher. You don't have the infrastructure, the collaborators, or the training for it. More importantly, the question you're asking — what happens at the interface where vague language meets numeric action — is answerable without opening the model. Stay outside the box.

**On your profile:** Working data scientist, master's student, one preprint, Algoverse fellow. Here's what that affords you. It affords you credibility with practitioners, which most alignment researchers don't have. It affords you a real production system as a source of research questions. It affords you the Algoverse network, which is real mentorship infrastructure. What it doesn't afford you: the ability to run large-scale multi-domain studies solo, the ability to pursue mechanistic interpretability without significant upskilling, or the ability to claim a new field on the basis of one paper. Aim at the venues where deployment-facing empirical work is valued — not just alignment venues, but HCI venues like CHI and CSCW, and applied ML venues that care about real-system behavior. Your practitioner background is a credential there in a way it isn't at pure theory venues.

**The single question I'd leave you with:** If the human baseline study shows that humans also compress these words — that "slightly" and "mildly" really do mean roughly the same thing to most people — what does your research program become? If you have a good answer to that question, you have a robust research program. If the answer is "I don't know," then the program is more fragile than you think.

You're not wrong about the window. I just want you to look through it carefully before you tell everyone it's a new room.

---

## Deliberation Round

### Field Cartographer — Revised Position

Good. I now have the additional landscape intelligence I need. The search results reveal two critical pieces of new information that sharpen my review considerably:

1. **The GAP benchmark** (Cartagena & Teixeira, February 2026) is a direct and very recent neighbor — it studies text-safety vs. tool-call-safety divergence across six frontier models and six domains. This is the closest existing work to Tabach's paper and was published *after* the paper was written. It must be engaged.

2. **Feng et al. EMNLP 2025** ("Noise, Adaptation, and Strategy") studies LLM fidelity in numeric decision-making tasks (auction, newsvendor) — a direct methodological parallel that Tabach's related work section missed entirely.

3. **Shivade et al. BioNLP 2016** on gradable terms in clinical text is a real prior art thread that none of the advisors named — it shows the "action domain" concern exists in clinical NLP and directly threatens the cross-domain generalization claim.

Now I can deliver my full deliberation response.

---

# FIELD CARTOGRAPHER'S DELIBERATION RESPONSE

---

## Agreements

**Advisor B — "The human baseline is the single most important next step."**
I agree completely, and I want to strengthen the argument with a piece of evidence none of us cited in the first round. Research on adverb quantification has shown that people can attribute numerical values to adverbs on intensity scales, and this procedure has been used to transform ordinal scales into interval scales for measuring behavioral patterns. This literature — going back to Thurstone-style scaling studies — means the human baseline study is not methodologically novel or difficult. It is a known, cheap, executable procedure. The fact that it hasn't been done *for this specific word set in an action context* is the gap. Advisor B is right that this is the load-bearing dependency for everything else, and I agree it should be Paper 2's primary contribution.

**Advisor D — "The boundary abstention behavior is the sharpest finding and the one hardest to explain away."**
I agree, and I want to add precision to why. The GAP benchmark (Cartagena & Teixeira, 2026) — which was published *after* Tabach's paper and which none of us cited in the first round — finds that text safety does not transfer to tool-call safety, with instances where the model's text output refuses a harmful request while its tool calls simultaneously execute the forbidden action. Tabach's boundary behavior finding is structurally *inverse* to this: his model's text acknowledges the request but the tool call is suppressed. These are complementary failure modes at the same text-action interface. The GAP paper is the most important new neighbor in the territory, and Tabach must engage it explicitly. Advisor D's instinct to lead with the boundary behavior is correct precisely because it connects to this emerging literature.

**Advisor C — "The IRB window is time-sensitive and must be treated as a hard deadline."**
I agree and want to reinforce this from a territory perspective. The human baseline study is not just methodologically important — it is the *only* thing that lets the author make a claim about the *action context* being categorically different from the *estimation context*. Gradable adjectives are inherently vague and are used by clinicians to document medical interpretations, and a comprehensive study of gradable adjectives in the clinical domain shows they have a substantial presence in clinical text. This Shivade et al. (BioNLP 2016) work — which none of the advisors cited — shows that the "gradable terms in action contexts" problem has been studied in clinical NLP for a decade. Without a human baseline, Tabach cannot distinguish his contribution from that lineage. The IRB deadline is therefore not just a logistical concern; it is the prerequisite for the territorial claim.

**Advisor E — "Cross-model belongs in Bucket B, not Bucket A."**
I agree with the reclassification but want to add the territorial reason. LLMs are increasingly used in social science simulations, and while their performance on reasoning and optimization tasks has been extensively evaluated, less attention has been paid to their ability to simulate human decision-making's variability and adaptability. Feng et al. (EMNLP 2025) — another paper none of us cited in the first round — runs a directly analogous study: LLMs in constrained numeric decision tasks (newsvendor problem, auction), with a human comparison. LLMs by default converge on stable and conservative strategies that diverge from observed human behaviors, and risk-framed instructions impact LLM behavior predictably but do not replicate human-like diversity. This paper is Tabach's closest methodological neighbor in the published literature. Cross-model comparison without engaging Feng et al.'s framework would be a missed opportunity; with it, cross-model becomes a field-defining move. Advisor E is right that it belongs after the human anchor.

**Advisor A — "Target the NLP/deployment-safety audience first."**
I agree with the venue sequencing. Growing evidence reveals that model performance can be highly sensitive to prompt wording, and questions remain about how well benchmark accuracy translates to real-world reliability. The instruction-following reliability literature at EMNLP is the right first home for this work. The alignment framing is a second-order move.

---

## Disagreements

**Advisor D — "The field is derivative at 7/10 confidence."**
I disagree with the confidence level, not the direction. Advisor D's case rests on the claim that the action context is not categorically different from the estimation context. But the new evidence changes this assessment. Large language models deployed as agents increasingly interact with external systems through tool calls — actions with real-world consequences that text outputs alone do not carry. Safety evaluations, however, overwhelmingly measure text-level refusal behavior, leaving a critical question unanswered: does alignment that suppresses harmful text also suppress harmful actions? The GAP benchmark (2026) establishes, from a completely independent research direction, that the text-action boundary is a real, distinct, and underexplored safety surface. Tabach's paper is measuring a different failure mode at the same boundary — not harmful actions, but semantically miscalibrated actions. The convergence of two independent research programs on the same boundary is evidence that the territory is real. I would revise Advisor D's confidence from 7/10 to 5/10. The field is partially derivative, but the specific coordinate is less occupied than Advisor D claims.

**Advisor B — "The founding instrument claim fails on the generativity criterion."**
I partially disagree. Advisor B's criterion — a founding instrument must enable questions that couldn't be asked before — is too strong. Tabach's measurement harness (deterministic backend + isolated language variable + repeated runs) is a reusable methodology. When faced with user prompts expressing similar intent but differing subtly in phrasing, contextual framing, or task instantiation, one model may generalize appropriately while the other fails. The instruction-following reliability literature has been asking this question without a clean measurement instrument. Tabach's harness provides one. That is generative in the methodological sense, even if the phenomenon was previously suspected. The founding instrument claim is premature for a *field*, but it is not premature for a *methodology*. Advisor B conflates these two claims.

**Advisor F (myself, first round) — I understated the urgency of one specific new neighbor.**
The GAP benchmark (Cartagena & Teixeira, February 2026) was not in my original review. The GAP benchmark is a systematic evaluation framework that measures divergence between text-level safety and tool-call-level safety in LLM agents, testing six frontier models across six regulated domains. This paper is structurally complementary to Tabach's work in a way that is strategically important: GAP studies *harmful* instructions where text refuses but tool calls execute; Tabach studies *benign* instructions where the tool call executes but with semantically wrong magnitude. Together, they map two failure modes at the same text-action boundary. Tabach should cite GAP, position his work as the *magnitude fidelity* complement to

### Devil's Advocate — Revised Position

### Agreements

**Advisor F, "Single Biggest Weakness":** Fully agree, and I want to sharpen why. Advisor F frames the human baseline gap as "you don't know what you're measuring." That's correct but understates the structural problem. Without the human baseline, the entire "passive failure" framing is unfalsifiable as stated. The paper cannot distinguish between three interpretations: (1) the model is failing relative to human intent, (2) the model is accurately reflecting genuine linguistic ambiguity, or (3) the model is doing something idiosyncratic that neither confirms nor disconfirms human intent. All three are consistent with the current data. The framing presupposes interpretation (1) while the evidence is silent on it. This isn't a gap to fill — it's a load-bearing assumption that the entire research program rests on.

**Advisor F, "Narrative Inflation Check" equivalent (the "inoculation" observation):** Advisor F makes the sharpest point in the entire council when they note that self-awareness of a failure mode can function as pre-emptive inoculation rather than behavioral constraint. I flagged the inflation in my original review, but I didn't identify the mechanism. Advisor F did. The author named the trap, which makes it harder for advisors to spring it — and may not actually prevent the author from falling into it. This is the most psychologically precise observation in any review.

**Advisor E, "What You Cannot Do Alone" — IRB timing:** Advisor E correctly identifies the IRB window as the most time-sensitive dependency and the one most likely to be treated as a future work item rather than an immediate constraint. I mentioned the human baseline as critical but didn't flag the institutional clock. If the author is finishing their master's, the window for conducting IRB-approved human subjects research under Georgia Tech's umbrella is closing. This is a hard deadline masquerading as a soft one.

**Advisor B, "The Unclaimed Coordinate":** Advisor B's field cartography is the most rigorous treatment of the novelty question in the council. Their specific identification of what is and isn't occupied — particularly the distinction between the *consistency* question (do identical inputs produce identical outputs?) and the *semantic fidelity* question (do semantically graduated inputs produce ordinally graduated outputs?) — is the clearest articulation of where the genuine gap lies. I agree that this specific coordinate is not occupied, and I should have been more precise about this in my original review rather than gesturing at "adjacent literature."

---

### Disagreements

**Advisor A, "Cross-model belongs in Bucket B, not Bucket A":** Advisor A argues that cross-model comparison is a field-defining move rather than a credibility move, and should therefore come after the human baseline. I disagree with the sequencing logic, though not the underlying point. The argument is: without a human anchor, cross-model comparison is just "Model A vs. Model B," which is weaker than "Model A vs. Model B vs. Human Baseline." This is true. But it proves too much. By this logic, nothing should happen before the human baseline, because everything is stronger with it. The practical question is: what can be executed in parallel with the IRB process, which takes 4-8 weeks? Cross-model comparison can be collected during that window at minimal additional cost. The human baseline doesn't need to be published first — it needs to be collected first. Running cross-model data collection while IRB is pending is not sequencing error; it's efficient use of a bottleneck period. Advisor A's bucket logic is sound; the execution timeline implication is wrong.

**Advisor D, "Target the NLP/deployment-safety audience first. Do not lead with alignment":** Advisor D recommends leading with NLP safety venues (EMNLP, ACL) and treating alignment as a second audience. I partially disagree. The recommendation is strategically sound for publication, but it may be wrong for fellowship positioning. The author is an Algoverse AI Safety Research Fellow. Their credibility infrastructure is in the alignment community, not the NLP community. Submitting to EMNLP as a first move optimizes for one audience while potentially signaling to the fellowship community that the work isn't really safety research. The author needs to decide which community they're building toward, because the optimal first venue differs depending on the answer. Advisor D treats this as a pure publication strategy question; it's also a community identity question.

**Advisor B, "The Steelman Alternative" — framing as "behavioral characterization of vague language in constrained action contexts":** Advisor B's steelman is accurate but undersells the boundary abstention finding. They write that the right framing is "behavioral characterization" and that the research program "does not require a new field." I agree it doesn't require a new field. But "behavioral characterization" is too flat a frame for the abstention finding specifically. The drastically/dramatically flip — where swapping one near-synonym causes categorical behavioral switching in the same state — is not adequately captured by "behavioral characterization." It's a discontinuity finding with direct safety implications: a user cannot predict, from the surface language alone, whether their instruction will produce action or abstention. That's a reliability claim, not just a characterization claim. The steelman should preserve this.

**Advisor E, "Do not try to connect with MIRI or ARC at this stage":** Agree with the conclusion but the reasoning is wrong. Advisor E says MIRI and ARC are focused on theoretical alignment and formal verification, which is true. But the actual reason to avoid them is simpler: they are not hiring or fellowshipping empirical deployment researchers right now, and cold outreach to them has near-zero expected value regardless of the work's quality. The framing matters because it implies the work is misaligned with their research programs, when the real issue is just that the author has no warm path in and the expected return on the time investment is negative.

---

### Revisions to My Review

**What I missed: The IRB clock.** My original review identified the human baseline as the most important next step but treated it as a research priority rather than an institutional timing constraint. Advisor E's point about the master's completion timeline and the IRB window is correct and I should have flagged it. The human baseline isn't just the most important study — it's the study with the hardest external deadline. I revise my priority ordering: the IRB application is not "first step in the research program," it's "the thing that must happen before the master's ends, full stop."

**What I understated: The boundary abstention finding is doing more work than I gave it credit for.** My original review treated the three findings (compression, state dominance, boundary behavior) as roughly equal in novelty. Reviewing the other advisors' treatments, I think I was wrong. The compression finding is the least novel — it's consistent with what the vague quantifier literature would predict. The state dominance finding is interesting but arguably expected. The boundary abstention finding — specifically the drastically/dramatically categorical flip — is the finding that has no clean prior art and the most direct safety implication. I should have led with it as the paper's sharpest contribution rather than treating it as one of three parallel findings.

**What I should strengthen: The "inoculation" mechanism.** I identified narrative inflation in the brief but didn't explain the mechanism by which self-awareness fails to prevent it. Advisor F's framing is better than mine. I would now add to my Narrative Inflation Check: the author's self-awareness is real but may be functioning as a permission structure rather than a constraint. Naming the failure mode in the brief signals sophistication to advisors and may reduce the pressure they apply — which is exactly the wrong outcome if the goal is genuine stress-testing.

**What I stand by: The "passive failure" framing is doing more work than the evidence supports.** No other advisor challenged this as directly as I did, and the council's overall response suggests some softening of the adversarial position. I maintain it. The framing names a verdict (failure, passivity, interface as locus) that requires the human baseline to be defensible. Until that data exists, "passive failure" is a hypothesis dressed as a finding. The author should use it as a research program label, not as a description of what the current paper demonstrates.

---

### Blind Spots

**The model deprecation problem, and what it means for the research program's durability.** Advisor F mentions it briefly, but no advisor develops it. Claude Haiku (`claude-haiku-4-5-20251001`) is a specific model version. Anthropic releases new versions regularly. The behavioral fingerprint documented in this paper — the specific compression pattern, the 0.50 hedge, the drastically/dramatically flip — may not replicate on the next Haiku release. This is not a minor limitation. It means the paper's empirical foundation is time-stamped in a way that most empirical research is not. A physics experiment from 2024 still holds in 2026. A behavioral experiment on a commercial model version may not. The research program needs a strategy for this: either (a) establish the phenomenon on open-

### Research Sequencer — Revised Position

### Agreements

**Advisor F (Cornerstone Verdict) on the human baseline as the load-bearing gap:** F's framing is the sharpest version of what I said. The specific formulation — "you don't know what you're measuring" without a human baseline — is more precise than my version. I said the human baseline is the wedge paper; F explains *why* with more force: without it, you cannot distinguish model failure from linguistic ambiguity, which means the entire "passive failure" framing is built on an unvalidated assumption. I agree completely and wish I had said it this cleanly.

**Advisor D (Devil's Advocate) on the boundary abstention finding as the paper's sharpest contribution:** D identifies the drastically/dramatically flip as the one finding that is genuinely hard to explain away and doesn't have a clean precedent in adjacent literature. I agree. My review treated the human baseline as the wedge; D's point reinforces why the boundary behavior is what makes this work worth defending — it's the finding that most clearly demonstrates the failure mode is *discontinuous and invisible*, not just noisy. The sequence implication: Paper 2 should be designed to test whether this boundary behavior generalizes, not just to add a human comparison.

**Advisor C on the IRB timeline as the most time-sensitive dependency:** C names this explicitly and correctly. I mentioned IRB as a dependency but didn't flag it as a hard deadline tied to institutional affiliation. C is right that finishing the master's creates a closing window for Georgia Tech IRB access. This is a sequencing constraint I underweighted.

**Advisor E on targeting NLP/deployment-safety venues before alignment venues:** E's argument that the paper should establish credibility in the NLP safety community before attempting alignment venues is sound sequencing advice. I implicitly assumed alignment venues were the right target; E makes a better case for why the NLP empirical community is the right first audience and the alignment community is the second.

**Advisor A on the "action case" being genuinely distinct from the "estimation case":** A's point that the paper's novelty claim requires demonstrating that the action context produces qualitatively different phenomena — not just quantitatively different ones — is correct. The boundary abstention behavior is the candidate for this distinction. My review didn't make this argument explicitly enough.

---

### Disagreements

**Advisor B (my own review) on cross-model belonging in Bucket B:** I stand by this reclassification but want to sharpen the argument in response to what other advisors said. Advisors C and E both treat cross-model as a credibility move. I think they're wrong about the *sequencing* even if they're right about the *function*. Cross-model without a human anchor produces a comparison without a reference point. The interesting question isn't "does GPT-4o compress differently than Haiku?" — it's "which model is closest to human calibration?" You can only ask the second question after Paper 2. Running cross-model second wastes the result.

**Advisor D on the "new field" claim being unsupportable:** D argues the field is derivative at 7/10 confidence. I think D is correct that the "new field" framing is premature, but I think D underweights the genuine novelty of the boundary abstention finding. D acknowledges this at the end of the review but then doesn't revise the overall verdict. The boundary behavior — where swapping near-synonyms produces categorical action switches — is not documented in the vague quantifier literature, the prompt sensitivity literature, or the automation bias literature in this specific form. That finding alone is sufficient to justify a research program even if the broader "passive failure" framing is overreach. D's 7/10 confidence on derivativeness is too high; I'd put it at 5/10 once you isolate the boundary behavior as the core contribution.

**Advisor F on mechanistic interpretability being off-limits:** F says "don't go there" for resource and expertise reasons. I agree with the resource argument but think F dismisses it too quickly on strategic grounds. The right answer isn't "never" — it's "not now, and not solo." If Paper 3 (cross-model) shows that different models produce different boundary abstention patterns, the natural next question is *why* — and that question points toward mechanistic work. The path is: establish the behavioral phenomenon across models first, then bring in a collaborator with mechanistic expertise for a later paper. F treats it as a permanent detour; I'd treat it as a deferred collaboration.

---

### Revisions to My Review

**What I missed: The IRB as a sequencing constraint, not just a resource constraint.** I flagged IRB as a dependency but treated it as a planning item. Advisors C and F both make clear it's actually a hard deadline tied to institutional affiliation. This changes the sequencing logic: the IRB application isn't something you do when you're ready to run the human baseline study — it's something you file *now*, in parallel with everything else, because the window may close when the master's degree completes. I would revise my Paper 2 recommendation to add: "File the IRB application before you do anything else. It runs in parallel. Do not treat it as a future work item."

**What I missed: The drastically/dramatically finding as the organizing center of the research program.** My review treated the human baseline as the wedge because it closes the most significant methodological gap. But Advisors D and F both point to the boundary abstention behavior as the finding that is hardest to explain away and most clearly demonstrates something genuinely novel. I should have made this the organizing center of the sequence, not just a finding to replicate. Revised framing: the research program is fundamentally about *discontinuous behavior at operational boundaries* — the human baseline and cross-model studies are in service of establishing whether this discontinuity is a model artifact or a general property of language-action interfaces. That's a sharper program than "measuring vague intensity words."

**What I missed: The venue strategy needs more specificity.** Advisor E provides a more detailed venue roadmap than I did. I said "EMNLP or ACL" without specifying what the paper needs to demonstrate to succeed there. E's point that the paper needs a human baseline before EMNLP submission is correct and I should have said it explicitly.

**What I would not change:** The core sequencing recommendation — human baseline first, cross-model third, field-defining synthesis fourth — stands. The other advisors' reviews don't provide a compelling argument for a different order. D's devil's advocate review actually strengthens the case for getting the human baseline before anything else, since D's strongest objection is that the paper can't distinguish model failure from linguistic ambiguity without it.

---

### Blind Spots

**The model deprecation problem is underaddressed by all advisors.** Advisor D mentions it briefly in the "program survivability" section, but no advisor addresses the strategic implication: Claude Haiku (specifically `claude-haiku-4-5-20251001`) will be deprecated. When it is, the baseline for the entire research program shifts. This is not a minor concern — it means the cross-model paper needs to be run while Haiku is still available, and the human baseline study needs to be completed before the model changes. The sequence has a hidden time pressure that none of the advisors named explicitly: the window to run comparative studies against the *same* model version that Paper 1 used is closing, not just the IRB window.

**No advisor addressed the "no-word control" as a sequencing priority.** The paper itself flags this as a limitation: without a condition where the model receives an increase instruction with no intensity modifier, the 0.50 hedge interpretation is ambiguous — it might be the model's response to any increase request, not specifically to weak intensity words. This is a cheap, fast, solo-executable addition that would sharpen the central interpretive claim of Paper 1. It should be collected immediately, before Paper 2, and either added to Paper 1 as a revision or incorporated into Paper 2's design. No advisor mentioned it despite the paper flagging it explicitly.

**The benchmark/shared task opportunity is mentioned by Advisor A but not developed by anyone.** A notes that a benchmark or shared task is the highest-leverage single artifact for seeding a research community. No advisor develops what this would look like or how to pursue it. For a self-funded researcher, a well-designed benchmark that other researchers can run against their own models is a force multiplier — it generates citations, creates community, and establishes the measurement instrument as a standard rather than a one-off. The harness already exists. Packaging it as a reproducible benchmark with a leaderboard is a concrete action that no advisor recommended but that could have outsized impact relative to cost.

**The decrease instruction asymmetry is underweighted as a near-term result.** Multiple advisors mention it, but none flag that it's the cheapest possible extension — same harness, same API, same analysis, just flip the direction — and it directly addresses one of the paper's stated limitations. It should be collected *this week*, not treated as a future paper.

### Alignment Insider — Revised Position

Good. I now have current data on MATS, Algoverse, and SoLaR. Let me render the full deliberation response.

---

# Alignment Insider: Post-Deliberation Response

*Advisor E — Responding to the Full Council*

---

## Agreements

**Advisor D on the human baseline as the single most important gap.** Advisor D states it most sharply: "You don't have a human baseline, which means you don't know what you're measuring." I agree completely, and I said the same in my original review. But Advisor D earns credit for the specific formulation: without knowing whether humans also compress these words, the "passive failure" framing is not just weakened — it is *interpretively unresolvable*. The failure might be the model's. It might be the language's. You cannot tell. Every other paper in the sequence rests on this distinction. I stand by my original position and Advisor D's formulation strengthens it.

**Advisor C on the "passive failure" label being technically imprecise.** Advisor C notes that in engineering and safety science, "passive failure" has a specific meaning — a system failing to perform an expected protective function — and that Tabach's usage is different: the model *does* act, but acts incorrectly. This is a real terminological problem I flagged but didn't develop as precisely. Advisor C is right that the label will confuse engineers and safety scientists who encounter it. The suggested alternatives — *semantic opacity*, *lexical-action gap* — are more defensible, though none are yet better than the paper's own phrase "language-to-action boundary," which is the clearest framing in the entire document.

**Advisor A on cross-model belonging in a later paper, not Paper 2.** Advisor A argues that cross-model comparison without a human anchor is a comparison without a reference point — you're comparing models to each other rather than to human intent. I agree with the logic. In my original review I said to target the NLP/deployment-safety audience first and build toward alignment venues; Advisor A's sequencing argument is the methodological version of the same point. Cross-model before human baseline produces a weaker paper than cross-model after.

**Advisor F on the IRB window being time-sensitive.** Advisor F identifies this as a hard deadline risk that others treat as a soft future-work item. Algoverse's track record shows that NeurIPS workshop acceptance can contribute to Anthropic fellowship selection, which means the institutional pipeline is real — but only if the foundational empirical work gets done while institutional affiliation is still active. Advisor F is correct that the IRB window is the most time-sensitive dependency in the entire program, and it is the one most likely to be procrastinated on. I should have been more emphatic about this in my original review.

**Advisor B on the "differentiation funnel" finding being genuinely unclaimed territory.** Advisor B identifies the specific interaction between word semantics and system state — the complete inversion from word-dominates at low baselines to state-dominates at high baselines — as having no direct prior art. I agree. This is the finding that most clearly distinguishes the paper from generic prompt sensitivity work, and it is the finding that should anchor the research program's identity claim. I noted the boundary abstention behavior as the sharpest result; Advisor B's identification of the differentiation funnel as equally novel is a useful addition.

---

## Disagreements

**Advisor A on combining human baseline + valence asymmetry as Paper 2.** Advisor A recommends combining the human baseline survey with the decrease-instructions (valence) study into a single paper. I disagree with this on strategic grounds. The IRB protocol for a human survey and the API-based valence extension are methodologically distinct. Combining them creates a paper with two separate empirical components that reviewers will evaluate independently — and if either component is weak, it weakens the whole paper. More importantly, the human baseline study is the *foundational* result. It should stand on its own, cleanly, without being diluted by a second study that is methodologically straightforward but thematically adjacent. A clean, focused paper that establishes the human-model comparison is more publishable and more citable than a combined paper that does two things adequately. Run them in parallel if you want, but publish them separately.

**Advisor C on the founding instrument claim failing on a "generativity" criterion.** Advisor C argues that a founding instrument needs to be generative — it needs to produce a research program that couldn't exist without it — and that Tabach's measurement harness fails this test because the research program it enables (test more words, test more models, test more domains) is incremental. I think this is too strict a criterion and it's applied inconsistently. The Mosteller & Youtz (1990) probability expression work that Advisor C cites as a predecessor was itself incremental — it extended existing psycholinguistics methodology to a new domain. The question isn't whether the instrument enables entirely new questions; it's whether it enables *cleaner answers* to questions that were previously unanswerable with precision. The deterministic backend is genuinely novel as a measurement device. No prior work in the vague quantifier or prompt sensitivity literature has a backend that converts linguistic variation into measurable consequential outcomes with zero noise. That is a methodological contribution that enables more precise answers to existing questions. Advisor C's generativity criterion would disqualify most methodological papers in empirical science.

**Advisor B on the "deployment-external safety science" framing being worth preserving.** Advisor B dismisses this phrase as opaque and recommends dropping it. I agree it's opaque as stated, but I think Advisor B is dismissing the underlying concept too quickly. The concept — safety science conducted by third-party researchers in deployment-realistic conditions, outside the model's training pipeline — is a real and important positioning claim. It distinguishes this work from both internal alignment research (which has access to model weights and training data) and from purely theoretical safety work. The phrase needs to be rewritten, not abandoned. Something like "deployment-facing empirical safety research" or "third-party behavioral characterization" captures the same concept more clearly.

**Advisor D on the "drastically/dramatically" flip being the paper's sharpest result and the one to lead with everywhere.** Advisor D says: "Lead with it. Build the next paper around it." I partially agree — it is the sharpest, most memorable result, and it should be the hook in every abstract and talk. But I disagree that the next paper should be *built around* it specifically. The flip is a single data point within the boundary behavior finding. Building a paper around one near-synonym pair risks producing a paper that is more interesting as a demonstration than as a generalizable result. The next paper should be built around the *class* of behavior the flip exemplifies — boundary-dependent categorical mode switching — and the flip should be the motivating example, not the organizing unit. The distinction matters for how the paper is framed and what claims it can make.

---

## Revisions to My Review

**What I missed: The Algoverse-to-MATS pipeline is more direct than I stated.**

MATS alumni-founded organizations explicitly include Algoverse AI Safety Fellowship, which means the Algoverse network has a documented institutional relationship with MATS, not just a general connection to the safety community. Algoverse research accepted to the NeurIPS 2025 Mechanistic Interpretability Workshop contributed to one fellow's selection for the Anthropic AI Safety Fellowship. This is a concrete, recent example of the Algoverse → workshop paper → fellowship pipeline working. Tabach is already inside this pipeline. My original review treated Algoverse as a general asset; I should have been more specific that the pipeline to MATS and Anthropic fellowships runs directly through Algoverse's workshop publication track record.

**What I missed: The MATS Autumn 2026 application window has already closed.**

Applications for the Autumn 2026 MATS cohort are now closed. This is a concrete, immediate consequence for fellowship strategy. The next MATS cycle will be Summer 2027 (approximately). This means Tabach has roughly 6-9 months to build the empirical foundation — specifically, to get a workshop paper accepted — before the next meaningful MATS application window opens. This changes the urgency calculus: the workshop submission isn't just a credibility move, it's a prerequisite for the next fellowship cycle. My original review said "submit to one workshop in the next 12 months" without this specific deadline pressure. The pressure is real and immediate.

**What I should strengthen: The SoLaR workshop is the specific right target, not a generic "safety workshop."**



### Career Strategist — Revised Position

# Advisor D — Response to Full Council Deliberation

---

## Agreements

**Advisor B, on the human baseline being more damaging than the paper acknowledges.** Advisor B makes the point precisely: without a human baseline, you cannot distinguish "model failure" from "genuine linguistic ambiguity." I flagged this in my original review, but Advisor B sharpens it in a way I didn't: if Mosteller & Youtz already showed that humans compress probability expressions into fewer distinct numeric interpretations, the prior probability that humans *also* compress intensity words is non-trivial. The "passive failure" framing may be asserting a failure that doesn't exist relative to human performance. I agree this is more structurally damaging than I originally stated.

**Advisor C, on the IRB window being a hard deadline, not a future work item.** I said this in my review, but Advisor C frames it with more precision: the IRB process runs in parallel with other work, and the window closes when Georgia Tech affiliation ends. I agree completely, and I should have been more emphatic about the timeline risk. This is the single most time-sensitive dependency in the entire program, and it is the one most likely to be treated as a background task rather than an immediate action.

**Advisor E, on the drastically/dramatically flip being the sharpest finding.** Advisor E says: "Lead with it everywhere. It is the empirical result that most clearly demonstrates that the failure mode is discontinuous and invisible." I agree. My original review mentioned the boundary behavior but didn't elevate it sufficiently. The flip is the finding that is hardest to explain away, most memorable, and most directly relevant to deployment safety. It should be the paper's lead, not its third result.

**Advisor F, on targeting NLP/deployment-safety venues before alignment venues.** I said "target MATS first, not Anthropic" — Advisor F makes the same point at the venue level: establish credibility in the NLP safety community before trying to enter alignment venues. The reasoning is the same: the alignment community will ask whether this is a safety problem or a usability problem, and you don't yet have a sharp answer. I agree with this sequencing.

**Advisor B, on the "narrative inflation" self-diagnosis being real and present in the brief.** Advisor B notes that self-awareness of a failure mode is not the same as not doing the thing. The brief uses "opens a window into something bigger," "failure modes rhyme across domains," and "passive failure at the action interface" — all of which are the inflation pattern in action. I flagged this in my review but Advisor B names it more precisely: the self-awareness may be functioning as pre-emptive inoculation rather than behavioral constraint. I agree.

---

## Disagreements

**Advisor C's recommendation to combine human baseline + valence asymmetry as Paper 2.** Advisor C argues this is more efficient than running them separately. I disagree on strategic grounds. The human baseline study is the single most important next step and deserves to be its own paper, not a combined study. Here's why: combining them risks producing a paper that feels unfocused to reviewers, and more importantly, it delays the human baseline by adding the complexity of valence design to an already IRB-constrained timeline. The IRB application for a pure survey study is simpler and faster than one that includes a valence manipulation. Get the human baseline approved and executed first. The valence extension can be Paper 3. The efficiency gain from combining is real but smaller than the risk of the combined study taking longer or being reviewed as two thin contributions stapled together.

**Advisor C's reclassification of cross-model comparison as "Bucket B" (field-defining rather than credibility-building).** Advisor C argues that cross-model comparison is a theoretical claim about universality, not a replication. I think this is wrong at the current stage. For a researcher with one preprint and no peer-reviewed publications, cross-model comparison is a credibility move, not a field-defining move. The field-defining framing requires institutional weight that the author doesn't yet have. Running the same protocol on GPT-4o and finding the same compression pattern is a replication result that strengthens the empirical foundation. It becomes field-defining only after you have the human baseline anchor. Advisor C's sequencing (human baseline → cross-model) is right; the labeling of cross-model as inherently field-defining is wrong.

**Advisor A's framing of the "unclaimed coordinate" as sufficient to constitute a new field.** Advisor A maps the territory carefully and concludes that the specific coordinate (vague intensity words × numeric tool-call actions × system-state interaction × boundary behavior) is "not occupied." I agree it's not occupied. I disagree that an unoccupied coordinate is sufficient to constitute a field. Fields require communities, not coordinates. Advisor A's map is accurate; the conclusion it's asked to support is too strong. This is a gap in the literature, not a new field. The distinction matters for how the author frames fellowship applications and community engagement.

**Advisor F's recommendation to avoid CHI entirely.** Advisor F says "do not target CHI — CHI will ask for user studies, interface designs, and interaction data." This is correct for the current paper. But it's too categorical as a career-level recommendation. If the human baseline study produces strong results showing a measurable gap between human intent and model action, a CHI submission framed around the design implications of that gap is entirely appropriate. CHI has a strong tradition of empirical studies that inform interface design without requiring a deployed interface. Don't close this door permanently — close it for Paper 1.

---

## Revisions to My Review

**What I missed: the model deprecation risk.** Advisor E raises this and I didn't. Claude Haiku is a commercial model that will be deprecated. The findings are a behavioral fingerprint of one model version. If the next paper runs on a new Haiku release and the results shift, the research program has a continuity problem. The mitigation is to run cross-model comparison early — not because it's field-defining, but because it insulates the program against the moving-target problem. I would add this to my "What You Cannot Do Alone" section: you cannot control the model you're studying, which means you need to establish the pattern across multiple models before the baseline model disappears.

**What I understated: the Algoverse leverage for the fellowship application specifically.** I said Algoverse is "real signal" and gave it appropriate weight. But Advisor F's point about the MATS application is sharper than mine: MATS explicitly looks for non-traditional researchers, and the Algoverse fellowship is exactly the kind of structured research environment that MATS treats as evidence of research ability. I should have been more specific: use your Algoverse PI as a reference for MATS. A letter from an Algoverse PI who has mentored researchers to NeurIPS carries more weight than a letter from a Georgia Tech thesis advisor who supervised a master's project. This is a concrete action I didn't name.

**What I should have been more direct about: the "recognized voice" goal has a shorter path than the research program.** The author wants to be a recognized voice in deployment safety. My review treated this as downstream of the research program. It isn't. The Alignment Forum post I recommended in my "Highest-Return Actions" section can happen in the next two weeks, before any new data is collected, before any IRB is filed, before any new paper is written. The drastically/dramatically finding is the hook. Write the post around that finding, frame it as a question to the community, and you have begun the "recognized voice" path independent of the research program timeline. I should have separated these more clearly.

**What I would strengthen: the fellowship framing advice.** I said "frame the application as a research program, not a paper." I stand by this but would add a specific instruction: the fellowship application should name the human baseline study as the immediate next step, describe it concretely (survey design, participant count, IRB status), and frame it as the pivot point that either validates or revises the current framing. Fellowship committees fund research programs with clear next steps, not visions. The human baseline is the clearest, most concrete, most fundable next step in the program. Make it the centerpiece of any fellowship application.

---

## Blind Spots

**No advisor addressed the model deprecation problem as a strategic risk to the research program.** Advisor E mentioned it briefly. No one addressed it as a planning constraint. The author is building a research program on behavioral findings from a specific commercial model version. That model will change. The findings may not transfer. The mitigation — run cross-model comparison early, include at least one open-weights model where the weights are stable — is not just a scientific choice, it's a program survival choice. An open-weights model (Llama 3, Mistral) as one of the comparison models in Paper 2 or 3 means the baseline is stable even if Claude Haiku is deprecated. No advisor recommended this specifically.

**No advisor addressed the question of what happens if the

### Skeptical PI — Revised Position

### Agreements

**Advisor B on the human baseline being more damaging than the paper acknowledges.** B makes the point precisely: without a human comparison, you cannot distinguish "model failure" from "accurate reflection of genuine linguistic ambiguity." I said this was the single biggest weakness, but B sharpens it further — the Mosteller & Youtz literature already shows that humans compress probability expressions into fewer distinct numeric interpretations than the surface vocabulary implies. If that pattern holds for intensity words too, the compression finding evaporates as a model-specific claim. B is right that this isn't just a gap to fill; it's a gap that destabilizes the interpretive foundation of everything else.

**Advisor B on the "passive failure" framing doing too much work before the evidence supports it.** B's specific charge — that the author has named a phenomenon before demonstrating that the phenomenon is harmful — is correct. I made this point but B makes it more precisely: "passive failure" implies a verdict (failure, passivity, interface as the locus) that the data does not yet support. The word "failure" requires a counterfactual. You don't have one.

**Advisor D (my own review) on the boundary abstention finding being the sharpest result.** I stand by this. The drastically/dramatically flip is the finding that is hardest to explain away, most surprising to practitioners, and most clearly demonstrates that the failure mode is discontinuous rather than merely noisy. Every other advisor who touches on this agrees it's the paper's strongest hook. The convergence is meaningful.

**Advisor F on targeting NLP/deployment-safety venues before alignment venues.** F's point that the alignment community will ask "is this a safety problem or a usability problem?" is correct and important. I didn't address venue strategy directly (outside my mandate), but the underlying diagnostic is right: the paper needs to establish itself in a community that evaluates it on its own terms before it tries to claim alignment relevance. The NLP safety and evaluation community will read the experimental design charitably. Alignment venues will demand the human baseline and cross-model generalizability before accepting the safety framing.

**Advisor C on the boundary abstention finding being genuinely unclaimed territory.** C's field cartography is careful, and the specific claim — that the *three-mode boundary behavior* (hedge, act, abstain) and the near-synonym flip have no direct prior art — is the most important thing C contributes. This is where I'd push back on Advisor B's more dismissive read. B is right that the broader phenomenon isn't new. C is right that this specific finding is. These are compatible claims.

---

### Disagreements

**Advisor A on cross-model comparison belonging in "Bucket B" (field-defining moves) rather than "Bucket A" (credibility building).** A argues that cross-model is a theoretical claim about universality, not a replication study, and should come after the human baseline. I disagree with the sequencing logic, though not the underlying point. The human baseline and cross-model comparison are both necessary to establish the paper's basic claims, and they're not cleanly separable. Here's why: the human baseline tells you whether the compression is a model artifact or a linguistic reality. Cross-model tells you whether the compression is a Claude Haiku artifact or a model-class property. These are two different questions, and you need both answers before you can claim anything general. A's framing treats them as sequential when they're actually parallel dependencies. The practical implication: run them together, not in sequence.

More importantly, A's "Bucket B" framing implies cross-model is a field-defining move. It isn't. It's basic scientific hygiene. A finding that holds in one model is a finding about that model. A finding that holds across three models with different training procedures is a finding about the phenomenon. Cross-model is not a theoretical claim — it's the minimum required to make any claim at all.

**Advisor B's overall confidence level on "the field is derivative."** B rates this 7/10 and I think that's too high. B's case rests on the claim that the existing literature covers the phenomenon from multiple angles. But B's own analysis concedes the boundary abstention behavior has no direct precedent. A finding that is genuinely novel at the mechanistic level, even if the broader phenomenon is not, is not derivative — it's a contribution to existing fields that extends them in a new direction. That's not the same as founding a new field (I agree with B there), but it's also not "derivative." The right framing is: the paper makes a real contribution to existing fields, not a new field. B's framing slides toward dismissiveness in a way that undersells the actual finding.

**Advisor E on the IRB timeline being the most time-sensitive action.** E is right that IRB is time-sensitive and that the window closes when the master's ends. But E frames this as the single most urgent action, which I think is wrong about the ordering. The most urgent action is determining whether the human baseline study is even necessary before investing in IRB. Here's the test: run a quick informal pilot — 10-15 participants on Prolific, no IRB required for a non-sensitive survey that doesn't involve deception and collects no identifying information beyond demographic screening. This is not a substitute for a proper IRB-approved study, but it will tell you within two weeks whether humans show the same compression pattern. If they do, the entire "passive failure" framing needs revision before you invest in a full IRB study. If they don't, you have confirmation that the IRB study is worth pursuing. The informal pilot costs $50-100 and two weeks. The IRB study costs months and institutional resources. Do the pilot first.

---

### Revisions to My Review

**What I missed: the model deprecation problem is more acute than I stated.**

I mentioned the single-model problem as a survivability threat, but I understated how specifically damaging it is for this paper. The paper studies `claude-haiku-4-5-20251001` — a specific model version with a specific release date in the name. Model versions change. The next Haiku release may produce entirely different compression patterns, different abstention behavior, different boundary modes. If that happens before the paper is published in a peer-reviewed venue, the paper's empirical claims are about a model that no longer exists in the form studied. This is not a hypothetical risk — it's a near-certainty over a 2-3 year research program timeline.

The practical implication I didn't state clearly enough: the cross-model comparison is not just scientifically important, it's a hedge against model deprecation. If the same patterns hold in GPT-4o and Gemini Flash, the paper's claims survive even if Claude Haiku is deprecated. If the patterns are Claude-specific, you need to know that now, not after you've built a research program on them.

**What I understated: the no-word control is more important than I indicated.**

I mentioned the no-word control in passing. I should have been more direct: without a baseline condition where the model receives "increase innovation" with no intensity modifier, you cannot interpret the 0.50 hedge. The paper speculates that 0.50 is a hedge — the model recognizes a request for change but lacks confidence about magnitude. But it might equally be the model's default response to any increase request, regardless of the word. These are different interpretations with different implications. The no-word control is cheap, takes one afternoon to run, and resolves a genuine ambiguity in the paper's central interpretive claim. It should have been in Paper 1. It must be in Paper 2.

**What I would change about my "founding instrument" verdict:**

I said this is closer to (b) than (a). I stand by that verdict, but I want to be more precise about what would move it toward (a). The paper becomes a founding instrument if and only if the human baseline shows that humans *do* differentiate these words in ways the model does not. That result — a demonstrated gap between human intent and model action, measured directly — would establish that there is a real failure to explain, not just a behavioral characterization to describe. Without that result, the paper is a contribution to existing fields. With it, the paper has a claim to founding something. The human baseline isn't just the most important next step. It's the step that determines whether the "founding instrument" question is even worth asking.

---

### Blind Spots

**All advisors treated the word scale as fixed. Nobody asked whether the word scale is the right instrument.**

The paper tests 10 words chosen by the researcher based on Quirk's taxonomy, with only 3 of 10 appearing in Quirk's explicit lists. The remaining 7 were chosen heuristically. This means the "compression" finding — 10 words collapse to 5 outputs — is partly a function of which 10 words were chosen. If you chose 10 words that humans also treat as 5 distinct categories, the compression is not compression at all. If you chose 10 words that humans treat as 8 distinct categories, the compression is real but smaller than reported. Nobody asked: what would

---

## Methodology

This report was generated by the AI Research Council using 3 stages (Independent Review → Deliberation → Synthesis).

**Reviewer models:** claude-sonnet-4-6
**Chairman model:** claude-opus-4-8
**Total cost:** $5.08
