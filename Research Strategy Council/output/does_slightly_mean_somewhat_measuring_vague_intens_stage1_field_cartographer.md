# Field Cartographer — stage1

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