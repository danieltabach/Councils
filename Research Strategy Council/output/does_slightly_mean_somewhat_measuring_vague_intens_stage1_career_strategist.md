# Career Strategist — stage1

# Career Strategy Review: Daniel Tabach

---

## 1. Honest Profile Assessment

Let me tell you what your profile actually looks like before we talk about where to go.

**What a hiring manager at a frontier lab sees right now:**

A senior DS at a major financial institution who built something genuinely impressive at scale — ATLAS/BAR is not a toy project, and $9B projected lift across 4,300 branches is the kind of number that gets attention. You have two ArXiv preprints, one of which (the AI writing detection paper) already demonstrates you can design a real controlled experiment with human subjects. You're in a legitimate fellowship. You're finishing a GT master's.

That's a non-trivial profile for someone with no PhD and no institutional research home. Don't undersell it.

**What the same hiring manager also sees:**

No publications in peer-reviewed venues. No co-authored work with known researchers. No conference presence. No citations. The ArXiv papers exist in a vacuum — they demonstrate effort and some methodological competence, but they haven't been stress-tested by peer review, and frontier labs know that. Your research community doesn't know your name yet.

**The honest gap:** You're not far from being taken seriously as an independent researcher. You're not yet at the point where a cold application to Anthropic's research team gets past a screener. The path from here to there is real but requires specific actions, not just more papers.

---

## 2. The IRB Question — Extended Deliberation

You asked me to deliberate on this extensively, so here it is.

**The short answer:** You can probably avoid IRB for the next paper if you make one strategic pivot, and you almost certainly should.

**Why IRB is genuinely painful in your situation:**

Georgia Tech's IRB process for online masters students is not impossible, but it is bureaucratically oriented toward PhD students with faculty sponsors. Without a PI, you would be the PI of record — which GT does allow for graduate students, but which puts the administrative burden entirely on you. The process typically takes 4–12 weeks for expedited review (which is what a low-risk survey would qualify for), costs nothing in fees, but requires completing CITI training, writing a full protocol, and navigating a system designed for people who do this regularly. For a part-time researcher working nights and weekends targeting an August workshop deadline, this is a real timeline risk.

Beyond timeline: even if you get IRB approval and run a survey, a 100-person Mechanical Turk study of word interpretation is not going to dramatically strengthen a workshop paper. It would help, but it's not the difference between acceptance and rejection at a NeurIPS workshop.

**The actual IRB question you should be asking:**

The human baseline you're missing isn't necessary to make your current paper stronger. It's necessary to answer the question "do humans also compress these words?" That's a legitimate scientific question, but it's a *separate* paper — a follow-up, not a prerequisite.

**Paths that avoid IRB entirely:**

*Path 1: Reframe the human baseline as future work (you've already done this).* Your paper already footnotes the human survey as planned future work. This is acceptable for a workshop paper. Reviewers at a workshop like HCOMP or a NeurIPS Human-AI Interaction workshop will not reject you for lacking a human baseline if you've clearly articulated why it's future work and what it would show. They will flag it, but they won't kill the paper.

*Path 2: Use existing human data as a proxy.* The psycholinguistics literature already has human numeric interpretations of intensity words. Cliff (1959), Mosteller (1990), and more recent work provide human scalar judgments for many of these terms. You don't need to run a new survey if you can map your word set onto existing validated scales and compare model behavior to the published human distributions. This is methodologically defensible and requires zero IRB. It's not perfect — the task contexts differ — but for a workshop paper it's more than sufficient, and it's actually a cleaner intellectual move than running your own survey.

*Path 3: Pivot the framing away from human comparison entirely.* If you reframe the paper as a study of LLM action consistency rather than a study of LLM-human alignment, the human baseline becomes less central. The question becomes: "Are these models internally consistent and reliable as action-taking agents?" not "Do these models match human intuition?" This is arguably a more important question for AI safety and deployment anyway. Under this framing, the missing human baseline isn't a gap — it's a deliberate scope choice.

**My recommendation:** Take Path 2 or Path 3. Path 2 is stronger academically; Path 3 is faster. For an August NeurIPS workshop deadline, I'd do Path 3 for this paper and save Path 2 for the extended journal version. Do not start an IRB process for an August deadline. The math doesn't work.

---

## 3. Which Direction Has the Best ROI for Your Goals

You said you want to work at OpenAI, Anthropic, or DeepMind. That goal requires a specific type of evidence: that you can think rigorously about AI systems, that you have a research identity someone can describe in a sentence, and that people in the relevant communities have heard your name.

Here's my honest ranking of your extension ideas by ROI for that goal:

**Tier 1 — Do These**

**Cross-model comparison (open-source focus).** This is the single highest-ROI extension available to you right now. Your current paper is a one-model study. A cross-model comparison — even just Llama 3, Mistral, and one other open-source model — transforms your finding from "here's what Haiku does" to "here's a structural property of how language models handle vague intensity words." That's a generalizable claim. It's publishable at a different level. Your 3070 can run 7B and 13B models locally with Ollama or llama.cpp. This costs you essentially nothing and is the fastest path to a stronger paper.

**Valence/stakes manipulation.** Your ICU beds idea is genuinely interesting and directly relevant to AI safety. The question "does the model interpret 'slightly increase' differently when the stakes framing changes?" is a clean, testable hypothesis with real implications for deployment. This doesn't require IRB because you're not studying human subjects — you're studying model behavior under different prompt conditions. This is cheap to run and would add a meaningful dimension to your paper.

**Decrease instructions.** You noted this yourself. It's cheap, it closes an obvious gap reviewers will flag, and asymmetric behavior between increase and decrease would be a real finding.

**Tier 2 — Do These After August**

**Denser baseline grid / round-number anchoring.** The observation about round numbers is interesting and worth formalizing, but it's a refinement finding, not a headline finding. Save it for the extended version.

**Stakeholder persona manipulation ("The stakeholder is an analyst" vs. "a decision maker").** This is interesting but it's a different paper. It starts to touch on role-playing and persona effects in LLMs, which is a separate literature. Don't dilute your current framing.

**Tier 3 — Think Carefully Before Committing**

**Mechanistic interpretability.** I'll be direct: this is the suggestion from your Algoverse colleagues that sounds exciting but may not be the right move for you right now. Mech interp is technically demanding, requires deep familiarity with transformer internals, and the community has high methodological standards. A surface-level mech interp analysis on Haiku (a closed model you can't fully inspect) would likely be weaker than your behavioral work, not stronger. If you want to go this direction eventually, it's worth learning — but don't bolt it onto this paper as a quick extension. It would take months to do properly.

**Fine-tuning for guardrails.** This requires a human baseline to have a target, requires significant compute, and is a different research project entirely. Tabling this.

---

## 4. The Realistic Path to an August NeurIPS Workshop Paper

**Which workshop?** Let me be specific, because "NeurIPS workshop" is not one thing.

Your most realistic targets for August 2025 submission:

- **NeurIPS 2025 Workshop on Behavioral ML / Human-AI Interaction** — if one runs this year (check the NeurIPS workshop list when announced, typically July)
- **NeurIPS 2025 Workshop on Foundation Models for Decision Making** — directly relevant to your work
- **NeurIPS 2025 Workshop on Socially Responsible Language Modelling Research (SoLaR)** — safety framing fits
- **EMNLP 2025 workshops** (if NeurIPS timing doesn't work) — more NLP-oriented but your linguistics angle fits

**Backup targets if August doesn't work:**
- ICLR 2026 workshops (January submission)
- AAAI 2026 workshops
- HCOMP 2025 (the dedicated Human Computation conference — this is actually a strong fit for your work and has a shorter paper track)

**The honest timeline assessment:**

NeurIPS 2025 main conference deadline has already passed (May 2025). Workshop deadlines are typically late August to early September for a December conference. That gives you roughly 8-10 weeks from now.

What you can realistically do in 8-10 weeks, working nights and weekends:

- Cross-model comparison on 2-3 open-source models: 3-4 weeks of work
- Valence/stakes manipulation: 2-3 weeks
- Decrease instruction baseline: 1 week
- Rewriting and reframing the paper: 2 weeks

This is tight but achievable. The key constraint is that you should not try to do all of these. Pick cross-model comparison and one of the following: valence manipulation OR decrease instructions. That's a paper. Three models, two new conditions, and you've tripled the scope of what's currently on ArXiv.

**What will make or break workshop acceptance:**

Workshop papers are accepted on interestingness of finding + clarity of contribution + relevance to workshop theme. Your core finding — that vague intensity words collapse into discrete behavioral modes, that context dominates word choice, and that boundary behavior is discontinuous — is genuinely interesting. The weakness is the single-model scope. Fix that and you have a submittable workshop paper.

---

## 5. Framing for Maximum Impact

**Current framing: AI Safety and Alignment.** This is defensible but vague. "AI Safety" is a big tent and your work sits in a specific corner of it.

**Recommended framing: Reliable Language-to-Action Interfaces / Agentic System Reliability**

This framing is more precise and more timely. The question you're actually studying is: *when humans use natural language to control AI agents that take real-world actions, how reliably does that language map to intended actions?* This sits squarely in the agentic AI literature, which is currently one of the hottest areas in the field. Anthropic, OpenAI, and DeepMind are all actively building and deploying agentic systems. Your work speaks directly to a deployment risk they care about.

The safety angle is real but should be secondary framing, not primary. Lead with: "vague language in agentic systems produces unreliable and state-dependent actions." Then say: "this has safety implications." Don't lead with safety — lead with the concrete, measurable problem.

**For your resume and LinkedIn:** "Independent research on prompt sensitivity and language-to-action reliability in agentic LLM systems." This is more specific than "AI Safety" and more searchable.

---

## 6. Fellowships and Career Pathways Realistic for Your Profile

**Fellowships you should know about:**

- **Anthropic's Residency / Research Engineer roles:** You mentioned the fellowship. Be aware that Anthropic also hires Research Engineers who are not PhDs — this is actually your more realistic entry point than a research scientist role. Your MILP/optimization background is genuinely differentiated.
- **ML Collective:** Free, open research community. Good for collaboration and mentorship.
- **EleutherAI:** Open-source AI research community. Very accessible to non-traditional researchers, has produced real papers.
- **Apart Research:** AI safety sprints and fellowships. Accessible, no PhD required, directly relevant to your framing.
- **SERI MATS (ML Alignment Theory Scholars):** Competitive but accepts non-PhDs with strong research track records. Worth applying in 1-2 years once you have a workshop paper.
- **Redwood Research:** Has hired non-traditional researchers. Long shot currently but worth watching.
- **AI safety camps (AISF, ARENA):** Technical AI safety programs that can build credentials and connections.

**The realistic 2-3 year path to a frontier lab:**

Year 1 (now): Publish workshop paper. Build cross-model study. Get active in ML Collective or EleutherAI. Start engaging on Twitter/X with researchers in your area — reply to papers, share your work.

Year 2: Use Algoverse and any workshop connections to co-author with someone who has institutional affiliation. One co-authored paper with a known researcher is worth more than three solo ArXiv papers for your purposes. This is the key unlock you need.

Year 3: Apply to Research Engineer roles at Anthropic, Google DeepMind, and similar. By then you'll have: GT master's, Algoverse fellowship, workshop publication, 3-4 ArXiv papers, and ideally one co-authored paper. That's a competitive profile for a non-PhD research engineering role.

**The co-authorship problem is your biggest structural gap.** You cannot get to a frontier lab on solo work alone. Your Algoverse cohort is the most accessible path to collaboration right now. Identify one person in your cohort whose interests overlap with yours and propose a joint project explicitly. Don't wait for it to happen organically.

---

## 7. Addressing What's Worrying You

**"It's not technical enough."**

Define technical. Your paper uses appropriate nonparametric statistics for the data structure, runs 6,620 trials, and produces clean quantitative findings. It's not a methods paper and shouldn't be. The behavioral findings are the contribution. Workshop papers at NeurIPS are routinely less "technical" than this. What you need is not more math — it's more breadth (cross-model) and tighter framing.

**"It might not contribute enough."**

The three-mode boundary behavior finding (hedge/act/abstain) is genuinely novel as far as I'm aware. The context-dominance finding (baseline explains 10x more variance than word choice) is clean and counterintuitive. These are real contributions. The weakness is scope, not depth.

**"It's kinda expected."**

This is the most legitimate concern. The finding that LLMs don't perfectly preserve ordinal word meaning is not shocking. What makes it publishable is the *mechanism* you've identified (compression into discrete regimes, state dependence, boundary mode-switching) and the *context* (agentic tool-use, not just text generation). Frame it as a measurement study that documents specific failure modes in a deployment-relevant setting, not as a surprising discovery. That's an honest framing and a defensible one.

**"I'm inexperienced."**

You're inexperienced at academic publishing. You're not inexperienced at research. You built a production optimization system that allocates 24,000 people across 4,300 locations. You understand what it means for a system to behave reliably under constraints. That's more relevant experience than most first-year PhD students have. The impostor syndrome here is partially warranted (you are new to this community) and partially not (your underlying skills are real). Treat the academic publication process as a new domain to learn, not evidence that you don't belong.

---

## 8. The One Thing You Should Do This Week

Before anything else: run your existing experimental setup on two open-source models — Llama 3.1 8B and Mistral 7B via Ollama on your 3070. Just the no-context condition, 30 runs each, same 10 words. This costs you nothing, takes maybe a weekend to set up, and tells you immediately whether the compression pattern is specific to Haiku or generalizes.

If it generalizes: your paper just became significantly stronger and you have a clear extension path.

If it doesn't generalize: that's also a finding, and arguably a more interesting one — it means something about Haiku's training specifically is producing this behavior, which opens the mechanistic question in a principled way.

Either outcome is good for you. Do this first.