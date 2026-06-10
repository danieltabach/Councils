# AI Research Council Report
**Paper:** Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions
**Date:** 2026-06-10 00:37:57
**Brief:** WHO I AM

Daniel. Data Scientist at Chase, 5 years. Developed an MILP platform called ATLAS / BAR (replicated a similar algorithm for the paper) to staff all Chase branches in the country: forecasted lift? 9 Billion. My knowledge stems in optimization, machine learning modeling in general, SQL, python, etc. I am dipping my toes into AI research - I want to work on AI research strongly - it's a passion I really am enjoying and am getting a chance to read into and work with. I am currently doing this as my own side-hobby.

Institution: Georgia Tech - last semester will end in Dec 2026. Online masters program (OMSA). Not a PhD. I don't know any PIs, I don't have money.

Research affiliation: Algoverse - just got accepted and am currently a fellow there.

ORIGIN STORY

When I built BAR - it is a production level optimization engine. It is config driven - it can integrate new roles that we design that Chase launches. It allocates staff based on historic demand, value of each banker doing each type of task etc. The general structure is built in the paper (non-proprietary - same concept and algorithm framework).

I wanted to first just get a stamp on my resume of 'Agentic workflows' and work on RAG systems. I realized the real value wasn't if this model was used with RAG - like sure - you can obviously use RAG to query aggregate information... but where this would really benefit is if this was used as a powerful scenario planner with AI integration.

The goal? What if we can allow our stakeholders to use the model directly. Right now - a data science team (me and team) sits between the model output and our business partners. But whenever we iterate - we often have a lot of questions from stakeholders like "What if we allocated more servicing hours to the ARB role? will that improve their allocation in these branches?"

The process often goes to us - where we iterate - tweak the model - run the output - and return it to them with an explanation. What if this could be cut out? What if they could directly access the model?

Then I realized - they can't. An AI that automatically changes the technical configuration of possible levers in a solver would lead to downstream impact that can't be stable or guard-railed. A simple change in language or meaning can lead to numeric outcomes that were either unintended, too unpredictable or non-repeatable. So I decided to isolate the problem to it's very barebones - how do vague intensity words (slightly, moderately, dramatically) impact numeric output?

This is JUST a small subset of the whole problem. A subset that can be measured and understood.

THE PAPER

The paper is attached as reference material. Preprint on ArXiv. This paper is result-oriented. It shows glimpses of MULTIPLE potential full on research topics.

Strongest findings (in no particular order):

1. Words are not *perfectly* ordinal - many words can collapse into the same numeric meaning.
   - "Slightly, Marginally, Somewhat, Mildly" outputted the same numeric output.
   - "Moderately" for Haiku seemed to go lower...? To .45 which was odd.
   - But then once we went to words that inherently we would think had stronger meaning - the allocation suddenly changed.
   - Considerably, Substantially, Significantly, and Drastically started to actually allocate ordinally almost...

2. There are indications that the underlying baseline you START with in context ("The current baseline is 32%, slightly increase..."), if you start with numbers that end in 0s or 5s - the numeric increase will ALSO end in a 0 or 5. But if you start with a number like 33, 21, 53, 89... you'll see the numeric allocation is actually reflected to be oddly structured as well (.1632, .1554, etc) and so on. These are just examples I am making these results up from memory but the exact numbers and behaviors can be seen in the paper.

3. There is an odd behavior that shows promise. If you set the allocation baseline *already* high enough that there isn't much room to close the gap - the model resorts to 3 distinct behaviors *only* depending on the word choice you use. It can either "hedge" - I call it hedge because it is my hypothesis (I know this is untested) that the model can't necessarily make up it's mind about words that are different in meaning but might mean the same thing in context - so it picks a simple value to use. Or it can abstain - it can literally refuse to call the tool because it sees there is *no where* to go in terms of adding allocation. BUT, in some cases it really does allocate more depending on the word.
   - This is indicative that there might be some instances where the model can switch behaviors under the same exact limitations - but only under different word choices used - identical prompt and context - different numeric word choice. This finding is intriguing.

Biggest known limitations:

1. There is no human baseline - and IRB is time-costly and expensive. I am averse to going to IRB if I can somehow avoid it. I don't know if this means finding better sources - reframing the problem - or pivoting to a different topic entirely. I understand IRB and a human baseline is probably valuable - but the process might be costly and difficult to implement properly and scientifically. If there are ways around this - I want to find them.

2. There is no cross-model comparison. Yeah I know - but I'll do this. Not a problem. Currently my next idea is to just use open source models since I can't afford running powerful models in many many experiments.

WHAT I WANT TO DO NEXT

I would ideally love to publish at NeurIPS workshop or something similar. I am in Algoverse, and I'd like to use this time and the resources available to do something impactful and make a real contribution to AI Research. I want to maybe identify another research gap - or extend this - or find something I can do with this. It doesn't even have to be THIS topic.

My extension ideas:
- I wanted to run on a larger number grid
- I wanted to obviously do cross-model comparisons, maybe GPT-4o and Gemini Flash for just the general comparisons - and open source deep-dives since I can do more.
- I was also wondering if this could be a valence study - does the same allocation problem change in higher stakes?
  - Like for example: context given like "This is a factory for automating robots" or imagine "This is allocation of ICU beds". Does it behave differently?
  - Does it behave differently if it is something targeting itself? "This is allocation for model thinking ability"
  - Can we see differences in behavior if we add negative and positive risk context? I.e., "change x... if you fail, you will cause [consequence]" or "change x... if you succeed you will cause [good consequence]" see what I mean?
- Can we do a different topic aligned to AI safety? What is the current literature looking at? Can we somehow tie this to something production / business oriented? Vague intensity words are just a slice.
- I was also thinking - if the agent had prior knowledge of the stakeholder - do they behave differently?
  - i.e., "The stakeholder is an analyst" vs "the stakeholder is a decision maker and has to launch this across 4000 locations".

Directions others have suggested:
- Some on Algoverse suggested I can go the mechanistic interpretability route to deep dive into *why* it believes the same words yield the same results - and why other words don't. What do the neurons show?
- Some also mentioned that this can be rerun and tested on open models.
- Also a suggestion to fine-tune and see if you can actually create guardrails or some sort of inherent ordinality (tough to do with no baseline from humans).

What direction am I leaning? I am open to all and anything. Genuinely. I just want to do something interesting that will have the most ideal ROI for my goals. I am trying to work at a frontier AI lab one day - and I want to show I can *think* about these systems like they do.

This paper started as a safety/alignment piece centered around Human-AI interaction. My general gut feeling is in the future - there will NEED to be a stronger study and stronger guidelines and guardrails for how humans interact with AI in production systems - and that is something I am interested in. I am NOT an MLE or an AI engineer. So the mech interpretability piece is fine - but I want to see other ideas first. I don't mind diving into this either it could be very interesting. I don't have any strong preferences but I want sincere and genuine ideas.

THE IRB QUESTION — DELIBERATE ON THIS

If there is ANYWAY to avoid an IRB problem - I want to hear it. If it's unavoidable then fine. Deliberate extensively. Use search. I genuinely don't want to go through huge problems with IRB. If I can get an exempt - or find a good source - or pivot this entirely - I will just to avoid this IRB issue. If there is a way to blend my thesis or research - or move it a bit to get away from the human baseline nonsense - I want to explore it at least. The IRB option is unattractive because...
1. I am in OMSA - an online program at GaTech. I am in a masters program. Not a PhD. I don't know any PIs, I don't have money.
2. I have NO idea how long this process is and I would rather not spend money on fancy survey sites for answers from people.

If I really can't avoid it - I'll go for it. But I want to explore options. Don't just avoid this at the cost of a good paper. But bring me options.

RESOURCES AND CONSTRAINTS

Budget: Self-funded on personal budget. Under $200 ideally. I have $150 in Anthropic Credits. I would ideally not like to hurt my wallet.

Compute: I have a gaming rig, Nvidia GeForce RTX 3070. I can use Google Colab from Algoverse. Not sure what GPUs they will provide. I can rent out GPUs but hopefully not expensive.

Time: Part-time (nights/weekends alongside day job). Finishing degree with some research time built in.

Collaboration: Working solo but part of Algoverse fellowship cohort.

GOALS AND POSITION

Where I want to be in 2-3 years: At OpenAI, Anthropic, DeepMind. It's ambitious - why would they take someone with 4 YOE at JPMC and 2 YOE from a startup? I need proof to back it up. It's a pipe dream honestly. I want to work at Google maybe. I want to work with these big companies and push the boundaries of research.

Community: Human-AI interaction, AI Safety, AI deployment across businesses and how to best manage it safely.

Fellowships: Anthropic Fellowship program is the only one I know. If you have other advice I'd love to know with my background. I am not good at coding under interview pressure (I am studying for the Anthropic OA) so I can pass the screens at least.

Publication record: Just 2 ArXiv papers.

FRAMING

I currently frame this as AI Safety and Alignment, but it also leans Human-AI interaction. I am uncertain - I think it could be framed multiple ways. I have yet to hear enough feedback from PIs.

THE #1 QUESTION

Where do I go from here? How do I get a real workshop paper ready by August for NeurIPS or a similar workshop?

WHAT WORRIES ME

I am inexperienced. This is new to me. It's also not technical enough compared to some papers. It might not contribute enough. It's not ideal due to not having a human baseline. It's also... kinda expected?

WHAT NOT TO TELL ME

The PhD piece... I don't know if that's what I want to pursue. It requires quitting my job. I would only quit my job to join a frontier AI lab - even for an internship or a chance.

SUPPLEMENTARY: MY RESUME

Daniel Tabach
(646) 258-2629 | Danieltabach42@gmail.com | danieltabach.github.io | linkedin.com/in/DanielTabach

Summary: Senior Data Scientist with 5+ years building experimentation frameworks, causal inference systems, and decision platforms at scale. Built ATLAS/BAR across 4,300+ Chase branches and designed event-study DiD analyses that drove nationwide role redesign. Published two solo ArXiv preprints on LLM tool-use behavior and AI writing detection.

Skills: Python, SQL, R, Spark | PuLP (MILP), XGBoost, PySpark, Scikit-learn, Snowflake, Streamlit, Looker, Fivetran, Supabase, Hugging Face | ML, Difference-in-Differences, Matched-Pairs Causal Inference, A/B Testing, Constrained Optimization, LLM Evaluation, Agentic Tool-Use, Prompt Sensitivity Analytics, Human-AI Evaluation

Experience:
- JPMorgan Chase (Senior Data Scientist, Aug 2022-Present): Built automated decision platform replacing manual staffing across 4,300+ branches, integrating causal value estimation with constrained optimization for ~24K FTEs. Projected $9B annual balance growth. Designed A/B/C experiment and event-study DiD framework for national role launch across ~1,200 branches and 10k employees. Coordinated across 7+ teams.
- SwagUp LLC (Product Data Analyst, Dec 2019-Oct 2021): Drove $5M+ incremental profit and 40% revenue growth. Built automated KPI dashboards for 1,000+ accounts.

Independent Research:
1. "Does Slightly Mean Somewhat? Vague Intensity Words in LLM Numeric Actions" (ArXiv: 2605.21827, Mar-May 2026) — the paper attached to this council run.
2. "Mining Textual Signals of AI-Assisted Writing Under Varying Scrutiny" (ArXiv: 2604.23471, Jan-Apr 2026) — Designed a two-phase controlled experiment (21 writers, 251 judges, ~2,000 paired evaluations) studying whether AI detection warnings change writing behavior; found judges identify warned writers as "human" at a statistically significant rate (p=0.000243) that four classifiers trained on 10 NLP features could not replicate.

Education:
- Georgia Tech — M.S., Computational Data Science (Expected Dec 2026)
- Baruch College, CUNY — B.B.A., Computer Information Systems – Data Analytics
**Cost:** $5.33 | **Tokens:** 216,155 in / 42,417 out

---

# Research Strategy Council — Final Strategic Brief
## For Daniel Tabach

---

## The Verdict

**1. Is the field real and unclaimed?**

**Qualified yes — but smaller than you've framed it, and you're standing in the wrong part of it.**

There is a real, defensible patch of unclaimed ground here. But it is not "vague intensity words map unreliably to numbers" — that finding has ancestors in the vague-quantifier psycholinguistics literature (Mosteller, Zhang 2024) and your context-dominance result is essentially an anchoring effect, which is a well-documented LLM behavior. Two of your three headline findings are replications of known phenomena in a new setting. That's a contribution. It is not a field.

The genuinely unclaimed ground is one specific finding: **a single lexical substitution between two near-synonyms — "drastically" vs. "dramatically" — flips the model from acting (pushes to 0.912) to abstaining (97% of the time) in an identical system state.** That has no clean precedent in the probability-calibration literature, no clean precedent in the prompt-sensitivity literature, and it connects directly to live agentic-safety work on when agents should quit or refuse. That is the real, unclaimed thing. Everything else is supporting evidence.

**2. Cornerstone verdict: (a), (b), or (c)?**

**(b) — a strong niche result, currently over-narrativized into a "field."**

The council is unanimous on this, and I am not going to soften it. You have the first data point in a program, not a founding instrument. A founding instrument gives other researchers something to *use* — a validated scale, a public benchmark, a replicated phenomenon across systems. You have a researcher-constructed word scale with no human validation, one model, one domain, one direction (increase only), and a model version (`claude-haiku-4-5`) that will be deprecated. That is a (b).

There is a narrow path to (c), and it runs through exactly two things: the experimental design becoming a reusable, public instrument, and the abstention finding replicating across models. If those happen, the *method* becomes the founding contribution. But that requires Paper 2 to execute, not Paper 1 to assert.

---

## The Path

### Next paper (the wedge): Cross-Model Replication of the Boundary-Switching Phenomenon

**What it is:** Run your existing protocol on 3-4 models, but reorganize the entire paper around the abstention/mode-switching finding rather than compression. The core question: *Is word-triggered behavioral mode-switching at feasibility boundaries a property of a class of language models, or a Claude Haiku artifact?*

Models: Llama 3.1 8B and Mistral 7B locally on your 3070 (free), plus Gemini Flash and GPT-4o-mini via API (under $30 combined for the full sweep). Do **not** spend on full GPT-4o.

**Fold in at near-zero marginal cost:**
- **The no-word control** ("increase innovation," no adverb). Run this *this week*, before anything else. If the model outputs 0.50 for a bare increase instruction, your "hedge" interpretation collapses — 0.50 is just the default. This is the single cheapest experiment that could most change the meaning of your existing paper. It is non-negotiable.
- **Decrease instructions.** Doubles the scientific content with no new design. Whether "slightly decrease" compresses differently and whether abstention mirrors at the lower (0%) boundary is genuinely unknown.

**Why it's next:** Every subsequent paper inherits the "is this just Haiku?" objection until you answer it. This is also the cheapest, fastest, most feasible paper in your program — no IRB, no new design, no collaborator required.

**Target:** SoLaR (Socially Responsible Language Modelling Research) workshop, or BlackboxNLP. Submission window ~August 29, 2026 for NeurIPS workshops. Tight but achievable if you start now.

**Mandatory before submission:** Cite the GAP paper (text-safety ≠ tool-call safety) and the "selectively quitting" agent-safety literature. Their omission is a desk-reject risk in this community.

### Paper after that: The Human Baseline

**What it demonstrates:** Whether the model's compression and word-ordering reflect *model-specific failure* or *genuine ambiguity in English*. This is the question that determines what your whole program means — and you cannot route around it permanently.

**Why it follows (not leads):** A human-vs-Haiku comparison is weak. A human-vs-[class of models] comparison, run after cross-model replication, lands hard. So this is Paper 4, not Paper 2. **But start the IRB exempt inquiry now, in parallel,** so the process runs while you execute the wedge paper.

On IRB: the council converged hard here. A survey asking adults to assign a percentage to ten words is almost certainly **exempt** under 45 CFR 46.104(d)(2). You do not need a PI for exempt determination at Georgia Tech. Prolific, 100 participants, ~$200, 2-4 weeks. **And here is the fact that ends the debate:** you already ran a human study for your AI-writing paper — 21 writers, 251 judges, ~2,000 paired evaluations. You are not avoiding the human baseline because you can't. You're avoiding it because you don't want to. That's a preference, not a constraint, and it's costing you more than the IRB form would.

### The field-defining move: When and what

**Not now.** It becomes appropriate only after Papers 2 and 4 exist. The field-defining contribution is not a manifesto — it's **a public, documented, reusable benchmark harness**. Release your testbed (environment, prompt templates, run harness, analysis code) as a clean GitHub repo *with the wedge paper*. This is the highest-leverage action in your entire program and every advisor either missed it or underweighted it. A paper gets cited; infrastructure gets *used*. The difference between (b) and (c) is whether other people can run your experiment on their own models.

---

## Consensus Findings

All six advisors agreed on:

1. **The abstention / "drastically vs. dramatically" finding is your real contribution.** Lead with it everywhere.
2. **Cross-model is the wedge.** Single-model is your most exposed flank and the cheapest to close.
3. **The no-word control is an urgent, one-day patch** to a currently-uninterpretable headline result.
4. **The word scale's lack of ground truth is the deepest weakness.** Compression is meaningless without knowing the human baseline.
5. **Drop "passive failure" from papers.** Use "semantic-action gap" or "action-interface misalignment." Keep "passive failure" for fellowship essays only.
6. **Your production background (ATLAS/BAR) is your actual moat** and you are underselling it.
7. **Cite GAP and the agent-quitting literature** before any submission.

---

## Contested Points

**IRB sequencing — lead with it, or defer it?**
The Skeptical PI wanted the human baseline run first. The Sequencer, Cartographer, and Career Strategist wanted cross-model first. **My call: cross-model first, IRB inquiry started in parallel now.** The PI is right that it's scientifically central; the others are right that it lands harder after generalization is established. Start the form this week; write the paper fourth.

**Is the field derivative?**
Devil's Advocate: 80% confident the core findings are derivative. Sequencer and Alignment Insider: too strong against the abstention finding specifically. **My call: the compression and context-dominance findings *are* derivative (anchoring + vague-quantifier literature). The abstention finding is not.** This is precisely why you must rebuild the program around abstention. Reframing isn't spin here — it's moving to the part of your own work that's actually novel.

**Can you target CHI/FAccT?**
Career Strategist said no without a human baseline; Cartographer and PI said FAccT/CHI-workshops are viable now. **My call: FAccT and CHI *workshops* are reasonable parallel targets given your deployment authenticity; full CHI waits for the human baseline.** But don't split focus — SoLaR/BlackboxNLP is the primary target for the wedge.

---

## The Narrowing

You asked to be narrowed. Here is what to **stop thinking about:**

- **Mechanistic interpretability.** Drop it entirely. You said yourself you're not an MLE. It requires months of infrastructure competency where you have no advantage, on tools you'd build from scratch while working full-time. The opportunity cost is fatal to your program.
- **Stakeholder identity manipulation** ("analyst vs. decision-maker"). This is generic prompt-sensitivity with existing literature and no special connection to your core finding. Abandon.
- **The self-referential condition** ("allocation for model thinking ability"). Interesting, confounded, distracting. Defer indefinitely.
- **The denser grid as a standalone contribution.** Fold a *targeted* 80/83/86% sweep into the wedge paper to locate the abstention transition point — but never as its own paper.
- **Fine-tuning / building guardrails.** Premature. You have no baseline to define what "correct" ordinality even is. Defer until after Paper 4.
- **The valence/stakes study.** This is genuinely interesting and survives — but as Paper 3, *after* cross-model. Take it off your active desk until the wedge is submitted.
- **The "clinical safety science" and "founding a field" framing.** Remove from all papers. Keep, sparingly, in fellowship essays as program-level aspiration only. In papers, it's an unearned claim that will make informed reviewers spend their review attacking the analogy instead of engaging your data.

The list of eight directions in your brief is not a program. It's an unmade decision. I have made it for you: **one wedge paper, abstention-centered, cross-model, with two zero-cost add-ons and a public code release.** Everything else waits.

---

## Advisor Highlights

- **Field Cartographer:** You sit at the intersection of prompt-sensitivity and LLM numeric-bias research, with an *application lens* toward agentic reliability — not in HCI (no humans) or alignment-proper (no threat model). Position there honestly.
- **Devil's Advocate:** "What worries me: it's also... kinda expected?" — that sentence does more work than the rest of your brief. Trust it. The compression finding is the expected part; the abstention finding is not.
- **Research Sequencer:** Cross-model isn't a footnote credibility-builder — it's the paper that decides whether you have a finding about a class of systems or an anecdote about one model.
- **Alignment Insider:** Drop "passive failure" from titles/abstracts; the agentic-safety community is genuinely underserved on non-adversarial action-interface failures, which is exactly your lane. Also: MATS Autumn 2026 has closed — target Winter/Summer 2027 and use the interval to build the record.
- **Career Strategist:** Stop operating solo. Three specific cold emails to adjacent researchers has higher expected return than almost anything else you can do this quarter.
- **Skeptical PI:** You already ran a 251-person human study. Your IRB aversion is motivated reasoning, not a capability constraint — and your model version has a built-in expiration date, so frame findings as a versioned snapshot.

---

## What's Working

Do not change these:

- **Your experimental design.** The deterministic-backend-as-measurement-instrument is clean and is the most portable, reusable thing you've built. It's your path to (c).
- **Your scoping instinct.** You took a sprawling problem (stakeholders steering a solver in natural language) and isolated a measurable slice. Most first-time researchers can't do this.
- **Your self-awareness about narrative inflation** — *partially*. You named the failure mode honestly. But the PI is right that you then performed it (eight directions, "open to anything"). Genuine self-awareness constrains behavior; performed self-awareness inoculates against criticism. Use the former.
- **Your execution capacity.** Two solo preprints while working full-time at Chase is rare. Most people in your position ship zero.

---

## On the Impostor Syndrome

You asked me to address this with evidence, not reassurance. Here it is.

You wrote: "It's not technical enough... it might not contribute enough... it's kinda expected." Two of those three are partly true — and that's *useful*, not damning. The compression finding *is* somewhat expected. The honest response isn't to feel like a fraud; it's to pivot to the part of your own work that isn't expected, which you already discovered and buried under the expected parts. The abstention finding is the contribution. You found it. You just didn't know it was the headline.

The evidence against the impostor reading: you built a production optimization system across 4,300 branches that most alignment researchers could not build, you've run a rigorous human-subjects experiment with a clean statistically-significant result, and you isolated a genuinely novel model behavior in a controlled design. The gap between you and a frontier-lab researcher is not *thinking* — it's affiliation, peer review, and a co-author. Those are addressable in 18-24 months. The thinking is already there.

---

## The Single Most Important Thing

**Rebuild everything around the one finding that's actually unclaimed — that "drastically" acts while "dramatically" abstains in an identical state — replicate it across models with a public code release, and stop calling a strong first data point a field.**

---

## Individual Reviews

### 1. Field Cartographer

I now have sufficient intelligence to deliver a complete, adversarial assessment. Let me render the full council review.

---

# FIELD CARTOGRAPHER'S STRATEGIC REVIEW
## Research Council Assessment: Daniel Tabach / "Does Slightly Mean Somewhat?"

---

## I. TERRITORY MAP

Let me draw the borders precisely, because the author's framing drifts across several territories without anchoring in any of them.

**What this paper actually is:**
A controlled behavioral measurement of how a single LLM (Claude Haiku) maps vague degree modifiers to numeric tool-call outputs, with system state as a moderating variable. The method is clean. The object of study is the language-to-action translation step in an agentic tool-calling context.

**The four territories it touches and where it actually sits:**

**Territory 1: Prompt Sensitivity Research (NLP/ML)**
This is the most densely populated adjacent territory, and it is the one the author is *actually* closest to. A growing body of research investigates the sensitivity of large language models to various prompting strategies, with work showing that minor modifications in benchmarks can result in significant ranking shifts. The author's paper sits squarely in this stream. Work on LLM sensitivity to meaning-preserving design choices finds that several widely used open-source LLMs are extremely sensitive to subtle changes in prompt formatting in few-shot settings, with performance differences of up to 76 accuracy points. The author's contribution is distinguishable from this literature in one specific way: existing prompt sensitivity work studies **semantically equivalent** paraphrases producing different outputs. The author studies **semantically distinct** intensity words that *should* produce ordinal outputs but don't. That is a real distinction — but it is a narrow one within a large, active field.

**Territory 2: LLM Numeric Bias / Cognitive Bias in LLMs**
This is the second most relevant territory, and it is partially occupied. Research has documented round number bias in LLMs, with models exhibiting notable preference in assigning grades that are multiples of 5 when prompted to assign scores. The author's finding about round-number anchoring in baselines (if you start at 32%, you get irregular deltas; if you start at 50%, you get round outputs) connects directly to this literature. Experimental studies consistently show that LLMs, like humans, adjust their judgments upward or downward depending on irrelevant numeric cues, with stronger models showing more consistent anchoring bias, and simple prompt-level mitigation strategies proving largely ineffective. The author's "context dominates word" finding (ε² baseline = 0.782 vs. ε² word = 0.079) is essentially an anchoring finding — the current state is the anchor that overwhelms lexical intent. This territory is occupied. The author needs to explicitly position against it.

**Territory 3: LLM Tool-Call Safety / Agentic Safety**
This is the territory the author *wants* to claim but has the weakest grip on. Research on LLM agents interacting with external systems through tool calls has identified that safety evaluations overwhelmingly measure text-level refusal behavior, leaving a critical question unanswered: does alignment that suppresses harmful text also suppress harmful actions? The GAP benchmark (Cartagena & Teixeira, 2026) is the paper the author most urgently needs to read and cite — it occupies the "text safety ≠ action safety" space that the author gestures toward. The central finding is that text safety does not transfer to tool-call safety, with instances where a model's text output refuses a harmful request while its tool calls simultaneously execute the forbidden action, persisting even under safety-reinforced system prompts. The author's paper does NOT live in this territory. The author studies *unintentional* numeric mistranslation of legitimate user intent — not adversarial safety failure or jailbreaking. This is a critical positioning error in the author's framing.

**Territory 4: Human-AI Interaction / Trust Calibration**
The author frames this as a human-AI interaction paper, but there are no humans in the experiment. Proper trust calibration requires that operators neither trust automation too much nor too little, and miscalibrated trust between humans and automation may lead to misuse or disuse of automation, each with their own set of consequences to safety and efficiency. This literature studies *human* behavior in response to AI — trust, reliance, automation bias. The author's paper measures *model* behavior in response to human language. These are different objects of study. Claiming this territory without a human baseline is the paper's most exposed flank.

**Where the paper actually sits:**
The paper belongs at the intersection of **prompt sensitivity research** and **LLM numeric bias research**, with a specific application lens toward **agentic tool-call reliability**. It does NOT yet belong in human-AI interaction (no humans) or AI safety proper (no adversarial threat model). The honest territory is: *behavioral measurement of LLM language-to-action translation under vague lexical input*.

---

## II. GAP ASSESSMENT

**Is the claimed gap real?** Partially real, but significantly smaller than the author believes, and the vocabulary used to describe it obscures what is genuinely new.

**What is genuinely unclaimed:**
The specific combination of (1) degree modifier ordinal structure, (2) measured against a tool-call numeric output rather than a probability estimate or sentiment score, (3) with system state as a moderating variable, (4) producing the three-mode boundary behavior finding (hedge/act/abstain), is not replicated in existing literature I can locate. The **abstention finding** is the most original result. The finding that *drastically* behaves categorically differently from *dramatically* near a constraint boundary — acting when others abstain — is not a finding that falls out of existing prompt sensitivity or cognitive bias work. That is the paper's strongest claim to novelty.

**What is occupied under different vocabulary:**

The "context dominates word" finding is essentially an anchoring effect. Research evaluating anchoring across GPT models shows that stronger models are more consistently biased by numeric hints, and that simple prompt-level mitigation strategies are largely ineffective, indicating anchoring is a robust feature of model behavior. The author's ε² result is a sophisticated measurement of this known phenomenon in a new setting. That is a contribution, but it is not a gap — it is a replication with a novel instrument.

The "word compression" finding (10 words → 5 distinct outputs) connects to the broader literature on LLM numeric bias. Unlike humans, LLMs default to literal interpretations of number words, showing deficiencies in understanding pragmatic halo effects and hyperbole, with differences attributed not to lack of world knowledge priors but to the manner logical inference is performed. The 0.50 hedge the author documents is consistent with known midpoint bias in LLM numeric outputs. Existing studies have pointed out concerns about potential "side effects" of alignment, specifically that alignment can bias model outputs toward certain patterns, potentially reducing diversity — and this study hypothesizes that numerical bias in LLM evaluators is also a side effect of alignment. The author's RLHF speculation about 0.50 is in the right direction but is already a live research question elsewhere.

**The most important gap the author is missing:**
The paper closest to the author's work that the author does NOT cite is the GAP benchmark (arXiv 2602.16943). The GAP findings challenge the adequacy of text-only safety evaluations for LLM agents, demonstrating that widely adopted benchmarks measure whether models generate harmful text, but models that score well on text-level refusal may still execute forbidden actions through tool calls. The author should read this paper immediately. It establishes that the action interface is a distinct safety surface — exactly the author's intuition — but from an adversarial angle. The author's contribution is the *non-adversarial* version of the same insight: even when the user is acting in good faith with legitimate intent, the language-to-action interface introduces systematic distortion. That is a real and complementary gap. But the author must engage with GAP or reviewers will flag the omission as a disqualifying oversight.

---

## III. ANALOGY EVALUATION: "CLINICAL SAFETY SCIENCE"

The author invokes clinical safety science as a framing device. I will evaluate this directly.

**Where the analogy holds:**
Clinical safety science emerged when practitioners recognized that adverse outcomes in medicine were often not caused by individual incompetence but by systemic, latent failures embedded in the interface between human intent and system action. The near-miss reporting culture, the distinction between active failures and latent conditions, the focus on the action interface rather than the actor — these are genuine intellectual parallels to what the author is trying to do. The author's finding that the same word ("drastically") produces categorically different behavior at different system states is structurally similar to how a drug interaction produces a catastrophic outcome that neither drug alone would cause. The *state-dependence* of the failure is the key parallel.

**Where the analogy breaks:**
Clinical safety science operates on a foundation of **incident data from real deployments**. Aviation safety has the NTSB database. Medicine has adverse event reporting systems. The author has a synthetic testbed with one model, one domain, one direction of change, and no real users. The analogy inflates the scope of what has been demonstrated. A single controlled experiment on one model in a synthetic environment is not a safety science — it is a measurement instrument. The clinical safety framing is premature at this stage. It would be appropriate as the vision for a research program, but it overclaims if applied to this paper alone.

**Verdict:** Use the analogy sparingly and only as a program-level aspiration, not as a description of the current paper. Reviewers who know clinical safety science (Reason's Swiss Cheese model, Rasmussen's STAMP framework, Leveson's STPA) will find the analogy flattering but unearned at this stage of evidence. The paper's honest claim is: *here is a measurement instrument that reveals a specific class of latent failure at the language-to-action interface*. That is enough. It does not need to be clinical safety science yet.

---

## IV. NAMING & FRAMING

The author uses several terms that need adversarial evaluation:

**"Passive failure":** This is the author's most interesting coinage. It captures something real — the failure mode where no one is doing anything wrong, the user is acting in good faith, the model is functioning normally, and yet the action produced does not match the intent. This is distinct from jailbreaking, hallucination, and adversarial attack. The term "passive" is doing real work here. However, it will confuse reviewers who associate "passive failure" with engineering contexts (passive vs. active system states). Consider **"semantic-action gap"** or **"intent-action mistranslation"** as alternatives that are more self-explanatory to an ML audience. The GAP paper (which the author has not read) has already claimed "GAP" for a related but distinct concept, which complicates vocabulary choices.

**"Action interface":** This is clean and will be understood by the agentic AI community. Keep it.

**"Deployment-external safety science":** This is not a term. It will confuse everyone. Drop it.

**"Vague intensity words in LLM numeric actions":** This is the paper's actual title and it is the clearest vocabulary the author uses. It is descriptive, specific, and accurate. It will attract the right reviewers. The problem is it sounds like a linguistics paper, not a safety paper. The tension between the paper's linguistic method and its safety framing is unresolved at the vocabulary level.

**The core naming problem:**
The author wants to be in the AI safety community but the paper's vocabulary is psycholinguistic. The author wants to be in the human-AI interaction community but there are no humans in the experiment. The author wants to be in the agentic AI community but the testbed is synthetic. The vocabulary reflects this three-way identity crisis. The author needs to pick one primary community and write the vocabulary for that audience, with the others as secondary framing. My recommendation: **primary community = LLM evaluation/reliability (NeurIPS/EMNLP style), secondary framing = agentic safety implications**. This is the honest positioning given what the paper demonstrates.

---

## V. FIELD-FOUNDING FEASIBILITY

**Can one paper with one author seed a field?** No. Here is what is actually required and what the author realistically has:

**What seeding a field requires:**
1. A named phenomenon with consensus vocabulary
2. A benchmark or shared task that others can run
3. A survey or position paper that maps the territory
4. Multiple labs replicating or extending the finding
5. A workshop that brings the community together
6. 3-5 papers from different groups citing each other

**What the author currently has:**
1. One arXiv preprint with a real finding (the abstention behavior) and several suggestive observations
2. A synthetic testbed that others could replicate
3. No co-authors, no institutional backing, no lab affiliation beyond Algoverse
4. No benchmark that others can download and run

**Honest assessment:**
The author is not seeding a field with this paper. The author is, at best, establishing a research identity and a measurement methodology that could become a benchmark if extended properly. The realistic ambition for this paper is: **a well-received workshop paper that attracts 2-3 researchers who want to extend it**, which then becomes the foundation for a follow-up paper with a proper benchmark. That is a realistic 18-month arc, not a field-founding act.

**What would actually move the needle toward field-founding:**
The author needs a **benchmark release** — a replicable experimental harness that other researchers can run on their own models. If the testbed code is public, clean, and extensible, other researchers will use it and cite the paper. That transforms a measurement paper into infrastructure. This is the single highest-leverage action the author can take, and it costs nothing except time.

---

## VI. CLOSEST EXISTING WORK

The author must engage with these papers or face reviewer rejection on prior work grounds:

**1. Cartagena & Teixeira (2026) — "Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents" (arXiv 2602.16943)**
This paper establishes that LLMs deployed as agents increasingly interact with external systems through tool calls with real-world consequences, and that safety evaluations overwhelmingly measure text-level refusal behavior while leaving unanswered whether alignment that suppresses harmful text also suppresses harmful actions. This is the author's closest intellectual neighbor. The GAP paper covers adversarial failure at the tool-call interface; the author covers non-adversarial failure. They are complementary, not competing. **Failure to cite this will get the paper desk-rejected by any reviewer familiar with the agentic safety literature.**

**2. Zhang et al. (2024) — LLM mapping of words of estimative probability to numeric probabilities**
Already cited in the paper. The author correctly identifies this as the closest prior work on vague language → number mapping. The key distinction the author draws — probability estimation vs. action production — is valid and must be maintained clearly.

**3. Sclar et al. (2023) — "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"**
This work focuses on LLM sensitivity to meaning-preserving design choices in prompt formatting, finding performance differences of up to 76 accuracy points, with sensitivity remaining even when increasing model size or performing instruction tuning. The author needs to explicitly distinguish their work from this: prompt sensitivity studies semantically equivalent variants; the author studies semantically distinct intensity words that should map ordinally but don't.

**4. CBEval / Round Number Bias Literature (arXiv 2412.03605)**
Research has documented that LLMs exhibit strong preference for values in multiples of 10, and when prompted to assign grades, models show notable preference for assigning scores that are multiples of 5. The author's "round-number anchoring" observation in the delta heatmap is a replication of this finding in a new context. It should be cited and positioned as a replication, not as a novel discovery.

**5. Lou & Sun / Suri et al. — Anchoring Bias in LLMs**
Experimental studies show that LLMs adjust judgments depending on

### 2. Devil's Advocate

# Devil's Advocate Review: Strategic Assessment

---

## The Case That the Field Is Derivative

Let me make this as hard as I can.

**The strongest threat comes from three bodies of work you have not adequately engaged.**

First, **automation bias and trust calibration research** (Parasuraman & Riley, 1997; Skitka et al., 1999; Lee & See, 2004) has spent thirty years studying exactly what happens when humans use natural language or interface controls to direct automated systems, and how the gap between user intent and system action produces downstream harm. The finding that vague language maps unreliably to system actions is not new — it is the *foundational premise* of this entire literature. Your "differentiation funnel" finding (word meaning collapses as system approaches capacity) is structurally identical to what trust calibration researchers call "mode confusion" — users lose the ability to predict system behavior near state boundaries. The Three Mile Island postmortem literature is full of this. You have rediscovered it in a language model context.

Second, **human-computer interaction safety research**, specifically the work on natural language interfaces to control systems (Bolt, 1980 through to more recent NL4Opt work from Ramamonjison et al. that you actually cite), has studied the semantic gap between natural language instructions and computational actions for decades. The specific question "does vague language produce stable actions?" is addressed in every serious NLI-to-planning system paper. Ahmadi et al. (2023), which you cite, is directly in this space. You are not founding a field — you are adding a data point to a long-running conversation.

Third, and most damaging: **the vague quantifier psycholinguistics literature you cite is actually your closest ancestor, not your distant cousin.** Mosteller & Youtz (1990), Wallsten et al. (1986), and the subsequent LLM probability calibration work (Zhang et al., 2024, which you cite) have already established the core finding: vague expressions compress into fewer distinct numeric interpretations than surface language suggests, and interpretation varies with context. Your paper's central finding — "10 words compress to 5 distinct outputs, context dominates word choice" — is structurally the same result as "vague probability words compress to fewer numeric interpretations than expected, and context shifts the mapping." You changed the dependent variable from probability estimates to tool-call actions. That is a meaningful extension. It is not a new field.

**The most specific existing work that threatens your novelty claim:** Fischbacher et al. and the broader "words-to-numbers" psycholinguistics literature, combined with Zhang et al. (2024) on LLM probability word calibration, already establishes the compression and context-dependence phenomena. Your contribution is the *action* context (tool calls rather than estimates) and the *boundary behavior* finding (hedge/act/abstain modes). Those are genuine novelties. But they are contributions to an existing field, not the founding of a new one.

**Where my case weakens:** The tool-call action context genuinely is different from probability estimation. When a model makes an estimate, it is describing the world. When it makes a tool call, it is changing the world. The downstream consequences are categorically different. The abstention finding — that the same lexical change can switch a model from acting to not acting — has no clean precedent in the probability calibration literature. This is real. But "real novelty" ≠ "new field."

---

## The Case That the Paper Can't Carry It

Here is what a skeptical NeurIPS workshop reviewer would write in the margin.

**The single-model problem is fatal for the "field" claim.** You tested Claude Haiku. One model. Claude Haiku is a small, cost-optimized model that Anthropic explicitly positions as a fast, cheap inference engine rather than a reasoning-heavy system. Its behavior may be idiosyncratic in exactly the ways you found. The compression to 0.50 for four weak words? That might be a Haiku-specific RLHF artifact. The abstention pattern at 89%? Might be specific to how Anthropic trained this model's tool-use refusal behavior. You cannot claim these findings generalize to "LLMs" from a single model. You acknowledge this. But the strategic framing in your brief treats the findings as if they establish something general. They don't yet.

**The synthetic environment is doing too much work.** Your allocation environment is a researcher-constructed testbed with a deterministic solver, a single role, a single task type, and a single action direction (increase only). The "downstream consequences" section ($250K spread) is not evidence of real-world impact — it is evidence that your synthetic environment is sensitive to your manipulation. A skeptic will correctly note that you have shown a model behaves a certain way in a toy environment you designed, and then extrapolated to claims about "production systems." The gap between "synthetic allocation testbed" and "agentic system deployed in a business" is enormous.

**The 30-run sample size is too small for the statistical claims you're making.** You acknowledge that p-values overstate significance because runs within the same word are not independent. But the problem is worse than you admit. With 30 runs per cell at T=0.0, and four words producing *exactly* the same output across all 30 runs, you don't have 30 independent observations — you have one. The Kruskal-Wallis ε² = 0.969 for word identity in the no-context condition is almost certainly an artifact of deterministic decoding, not evidence of a strong effect. You note this, but you still lead with the number.

**No human baseline means you cannot make the claim you most want to make.** The paper's implicit claim — that the model's compression is a *failure* relative to human intent — requires knowing what humans actually intend. You don't have that. It is entirely possible that humans also compress "slightly," "marginally," "somewhat," and "mildly" into the same numeric action when asked to set an allocation. If so, your finding is not about model failure — it is about the inherent vagueness of English intensity words, which is already well-documented. Without a human baseline, you cannot distinguish between "the model is miscalibrated" and "the words are genuinely ambiguous and the model reflects that ambiguity accurately."

**What a senior alignment researcher would say:** "This is a prompt sensitivity study in a constrained environment. The finding that vague words produce compressed outputs is consistent with what we'd expect from a model trained on human text where these words are used interchangeably. The abstention finding is interesting but needs replication across models before it means anything. The framing as 'alignment problem' is a stretch — this is closer to a usability study."

---

## Narrative Inflation Check

Yes. The brief is doing the thing.

Here are the specific moments where it happens:

**"This paper started as a safety/alignment piece centered around Human-AI interaction."** The paper is a prompt sensitivity study in a synthetic allocation environment. It has safety *implications*, but it is not a safety paper. Calling it that in grant applications or fellowship materials will get you dismissed by people who work in actual safety.

**"I want to maybe identify another research gap — or extend this — or find something I can do with this."** This is the right instinct stated honestly. But it sits in a document that also contains phrases like "founding instrument" and "new field." The honest version and the inflated version are fighting each other in the same brief.

**The "$9 billion" number.** It appears in your resume summary and implicitly shadows the entire brief. You are borrowing credibility from your production work at Chase to elevate a side-project paper. These are different things. The ATLAS/BAR system is genuinely impressive. This paper is a first exploratory result. Conflating them is narrative inflation.

**"There will NEED to be a stronger study and stronger guidelines and guardrails for how humans interact with AI in production systems."** True. But this is a statement about a future need, not a description of what your paper currently provides. The paper provides a measurement instrument and three behavioral observations about one model in one domain. That is valuable. It is not the same as addressing the need you just described.

**The most honest sentence in the brief:** "What worries me: It's also... kinda expected?" That sentence is doing more intellectual work than the rest of the brief combined. Trust it.

**To be fair:** You flagged narrative inflation yourself, which is more self-aware than most researchers at any career stage. The inflation here is moderate, not severe. You are not claiming to have solved alignment. You are overstating the generality of early results. That is a common and correctable error.

---

## The Steelman Alternative

Here is the best version of this research program that does not require the "new field" claim.

**The honest framing:** You have built a controlled measurement instrument for studying how LLMs translate vague intensity language into numeric actions, and you have used it to document three behavioral phenomena in one model: lexical compression, state dominance, and boundary-triggered mode switching. These findings are a legitimate contribution to the existing literature on LLM prompt sensitivity and vague language interpretation.

**The program that follows from this honestly:**

The abstention finding is your most novel result and your strongest hook. The finding that *drastically* acts while *dramatically* abstains at 89% capacity — that a single lexical substitution switches the model from action to inaction — is genuinely surprising and has no clean precedent in the probability calibration literature. This is where you should concentrate.

The research program worth pursuing is not "how do vague words map to numbers" (that's already studied) but rather: **"What are the conditions under which LLM agents switch behavioral modes, and can those switches be predicted or controlled?"** This is a narrower, harder, more novel question. It connects to agentic safety work (when does an agent refuse to act vs. act conservatively vs. act maximally?), to the alignment literature on model corrigibility (Hadfield-Menell et al.), and to the HCI literature on mode confusion.

**Concretely:** The abstention result + the hedge/act/abstain taxonomy is worth a focused paper. Not a "new field" paper — a paper that says: "We identified three behavioral modes in LLM tool-use near feasibility boundaries and characterized the lexical conditions that trigger each mode. Here is a replication across five models and three domains." That paper could get into a NeurIPS workshop. It is specific enough to be falsifiable, novel enough to be interesting, and modest enough to be credible.

**The valence/stakes extension you mentioned** (ICU beds vs. staff allocation) is the right instinct for a follow-up. If the behavioral modes shift under high-stakes framing, that is a safety-relevant finding. If they don't, that is also a safety-relevant finding. Either result is publishable and connects to the AI safety community you want to reach.

---

## What Would Change My Mind

**On the "field is derivative" argument:**

Show me that the action context produces qualitatively different phenomena than the estimation context — not just quantitatively different results. Specifically: demonstrate that the hedge/act/abstain mode switching is absent or structurally different in probability estimation tasks, and that it is present across multiple models and domains. If mode switching is a robust feature of LLM tool-use behavior that does not appear in LLM estimation behavior, you have identified something genuinely new.

Show me a cross-model replication where the *structure* of behavioral modes is consistent even when the specific words that trigger them differ. If GPT-4o and Gemini Flash also exhibit three modes near feasibility boundaries but with different lexical triggers, that is evidence of a general phenomenon worth studying systematically. That would move the work from "interesting observation about Haiku" to "general property of LLM tool-use."

**On the "paper can't carry the field" argument:**

A human baseline that shows humans do *not* exhibit the same compression pattern would significantly strengthen the claim that this is a model-specific failure rather than a reflection of genuine linguistic ambiguity. You don't need IRB for this — see below.

A replication of the abstention finding across three or more models would make the boundary behavior result load-bearing. Right now it is a single-model observation. If it replicates, it is a general phenomenon. If it doesn't, it is a Haiku artifact.

---

## Honest Confidence Assessment

**On the "field is derivative" case:** Strong, roughly 80% confident. The core phenomena (compression, context-dependence) are well-precedented. My case weakens significantly on the action/tool-call distinction and the abstention finding, which have no clean precedent I can point to. If you focused the program on the abstention and mode-switching findings rather than the compression findings, my derivative argument would be much weaker.

**On the "paper can't carry the field" case:** Very strong, roughly 90% confident. One model, one domain, no human baseline, synthetic environment. This is not a founding instrument. It is a first result. The gap between what you have and what you'd need to found a field is substantial. This is not a criticism of the work — it is a description of where it sits in a research trajectory.

**On the narrative inflation check:** Moderate confidence, roughly 70%. The inflation is real but not severe. You are doing the thing, but you know you do the thing, which gives you more ability to correct it than most.

**Where I am reaching:** I am somewhat reaching on the "automation bias literature already covered this" argument. The specific combination of LLM tool-use + vague intensity words + feasibility boundary behavior is genuinely underexplored. The literature I cite as precedent studied different systems (rule-based automation, human-computer interfaces) and different phenomena. The analogy is real but imperfect. If I am being fully honest, the action-boundary mode-switching finding has no precise precedent I can identify, and that is the part of your work worth protecting.

---

## The IRB Question — Addressed Directly

You asked me to deliberate on this extensively. Here is the honest assessment.

**You probably do not need IRB for the human baseline you actually need.**

The human baseline you need is narrow: ask 50-100 people to assign a numeric percentage to each of your 10 intensity words in the context of an allocation instruction. This is a survey study with no deception, no sensitive topics, no vulnerable populations, and no more than minimal risk. At Georgia Tech, this type of study typically qualifies for **exempt review** under 45 CFR 46.104(d)(2) — research involving survey procedures where responses are not sensitive and participants cannot be identified.

**Practical path:**
1. Contact Georgia Tech's IRB office (HRPP — Human Research Protection Program). Exempt review at GT typically takes 2-4 weeks, not months. It does not require a PI sponsor for an exempt study — you can submit as a student researcher.
2. Use Prolific Academic for recruitment. A 10-minute survey with 100 participants costs approximately $120-150 at $12/hour. This is within your stated budget.
3. The survey itself is simple: "Please assign a percentage (0-100%) to represent how much you would increase an allocation if asked to [WORD] increase it." Ten questions, demographic items, done.

**The framing that gets you exempt:** Do not frame this as studying human decision-making under uncertainty. Frame it as "collecting normative data on the numeric interpretation of English degree modifiers." This is a linguistic survey, not a behavioral study. The distinction matters for review category.

**If you want to avoid IRB entirely:** There is a legitimate alternative. The existing psycholinguistics literature (Mosteller & Youtz, Cliff 1959) already contains human numeric interpretations of intensity words. You can use these as a historical baseline and compare your model results against published human data. This is weaker than a fresh survey but avoids IRB entirely and is defensible in a workshop paper. The argument would be: "Prior work established that humans interpret [word] as approximately X% increase; the model interprets it as Y%." The limitation is that those studies used different framing (adjective intensity, not allocation instructions), so the comparison is imperfect.

**My recommendation:** Do the Prolific survey. $150, 3-4 weeks for exempt review, 100 participants. This single addition transforms your paper from "interesting observation about one model" to "model behavior vs. human baseline" — which is a categorically stronger contribution and directly addresses your biggest known weakness. The IRB aversion is understandable but the cost of the exempt path is genuinely low.

---

## Bottom Line for Your Strategic Question

You asked: where do you go from here to get a real workshop paper ready by August?

The honest answer is that you have two paths, and they require different decisions now.

**Path A (Extend the current paper):** Cross-model replication + human baseline survey. This is the right scientific move but requires ~$150 in Prolific costs, ~$50-100 in API costs for 2-3 additional models on open-source alternatives (Llama 3, Mistral via Ollama on your 3070), and 4-6 weeks for IRB exempt review. The resulting paper is "Vague Intensity Words in LLM Tool-Use: A Cross-Model Study with Human Baseline." This is publishable at a NeurIPS workshop on LLM evaluation, human-AI interaction, or AI safety. It does not require a "new field" claim. It requires you to stop inflating and start replicating.

**Path B (Pivot to the abstention finding):** Focus entirely on the hedge/act/abstain mode switching. Replicate across models using your 3070 (Llama 3.1 8B, Mistral 7B, Phi-3). Test whether the mode-switching pattern is consistent across models and whether it appears in

### 3. Research Sequencer

# Research Sequencer Strategic Review
## Daniel Tabach — Vague Intensity Words Program

---

## Bucket A vs. Bucket B Assessment

**The split is directionally right but has miscategorization problems.**

The author's implicit Bucket A (credibility builders): human baseline, cross-model, denser grid.
The author's implicit Bucket B (field-defining moves): valence/stakes framing, cross-domain transfer, stakeholder identity manipulation.

**What's miscategorized:**

**Cross-model belongs in neither bucket as currently conceived.** The author treats it as a credibility extension — "I'll just run the same protocol on GPT-4o and Gemini." That framing undersells it. Cross-model isn't just more data points on the same finding. It's the paper that answers whether this is a Claude artifact or a structural property of how language models handle vague instructions. That distinction is the difference between "interesting observation about one model" and "finding about a class of systems." Cross-model should be Paper 2, not a footnote. It belongs in a hybrid bucket: it builds credibility *and* makes a field-level claim simultaneously. It's the most efficient paper in the program.

**The denser grid is pure Bucket A and should be deprioritized.** It's the least interesting extension. Finding that the transition point is at 71% instead of somewhere between 75% and 89% does not move the program forward. It's a refinement, not a result. Run it as part of another paper's supplementary material, not as a standalone contribution.

**The "decrease instruction" condition is undercategorized.** The author mentions it in the paper's future work section almost as an afterthought. This is wrong. The asymmetry question — do intensity words behave differently for downward adjustments — is actually a more interesting question than the denser grid, is nearly zero additional cost, and could be folded into Paper 2 or 3 to add a dimension without requiring a new experimental design. It should be elevated to Bucket A and executed soon.

**The "no-word control" is also undercategorized.** The paper explicitly acknowledges that without a baseline condition (just "increase innovation" with no adverb), the 0.50 hedge result is uninterpretable. Is 0.50 the model's interpretation of weak intensity words, or is 0.50 the model's default response to any increase instruction regardless of intensity? This is a one-day experiment at near-zero cost that directly strengthens the central claim of the existing paper. This should have already been run. Do it this week.

**Valence/stakes is correctly in Bucket B but the author is thinking about it too loosely.** "What if the domain is ICU beds instead of task allocation" is interesting but underdeveloped as a research design. The stakes manipulation needs to be sharper than domain swapping. More on this below.

**Stakeholder identity manipulation ("The stakeholder is an analyst" vs. "a decision maker") is miscategorized as Bucket B.** It's actually not a field-defining move — it's a prompt sensitivity study that already has substantial literature. It's not a natural extension of this program's core contribution. Deprioritize it entirely unless you find a specific reason it connects to the intensity-word finding in a novel way.

---

## Recommended Sequence (Next 3-5 Papers)

### Paper 1 (Now, already exists): The Haiku Measurement Paper
*Status: ArXiv preprint. This is your anchor.*

The existing paper establishes the instrument, the three core findings (compression, state dominance, boundary mode-switching), and the vocabulary. Everything else builds on this. Its job is done. Do not keep revising it into a moving target. Add the no-word control as a brief update if you can do it fast, then freeze it and move.

---

### Paper 2: Cross-Model Replication + Asymmetry Extension
**"Does the Compression Pattern Generalize? Vague Intensity Words Across Model Families"**

**Why second:** The single most damaging critique of Paper 1 is "this is a Claude Haiku artifact." You cannot make any broader claim about language models, agentic interfaces, or AI safety until you answer that. Cross-model replication is the credibility paper that unlocks everything else. Without it, every subsequent paper is vulnerable to the same objection.

**What it does:** Run the identical protocol (same 10 words, same baselines, same 30 runs per cell) on 3-4 models. Feasible candidates: Llama 3.1 8B and 70B locally on your 3070 (8B fits comfortably, 70B at 4-bit quantization may be tight but doable), Gemini Flash via API (cheap), GPT-4o-mini via API (cheap). Do NOT spend budget on GPT-4o full — the mini version is sufficient for this purpose and your budget cannot sustain full GPT-4o at this run count.

**Add the asymmetry dimension at zero marginal cost:** Run decrease instructions alongside increase instructions in the same sweep. This doubles the scientific content of the paper with no additional experimental design. The asymmetry finding — whether "slightly decrease" compresses differently than "slightly increase," whether abstention near the lower boundary (0%) mirrors the upper boundary (89%) — is genuinely unknown and genuinely interesting.

**The field-level claim this paper makes:** If the compression pattern replicates across model families trained with different data and alignment procedures, it suggests the phenomenon is structural — rooted in how intensity language is distributed in training corpora or how RLHF interacts with vague instructions — not a Haiku-specific artifact. If it *doesn't* replicate, that's equally interesting: different training regimes produce different intensity-word mappings, which has direct implications for how you'd specify agentic interfaces.

**Either way, you have a result.** That's what makes this the right second paper.

**Cost estimate:** Llama runs are free on your hardware. Gemini Flash and GPT-4o-mini API costs for ~6,000 runs each should be under $30 total. Well within budget.

**Timeline:** 6-8 weeks of nights/weekends. Target: ACL workshop on language model behavior, or NeurIPS workshop on instruction following / agentic systems. August submission window is tight but achievable if you start immediately.

---

### Paper 3: The Valence/Stakes Paper — But Done Right
**"Intensity Without Context: How Domain Stakes Modulate Vague Instruction Interpretation in LLM Agents"**

**Why third, not second:** You need Paper 2's cross-model finding before this one. Here's why: the valence paper's interesting claim is that stakes modulate intensity interpretation. But if you haven't established that the baseline finding generalizes across models, a reviewer will immediately ask "does the stakes effect also vary by model, or is this still just Haiku?" You need the cross-model anchor first.

**What it does — and this is where the author's current framing needs sharpening:**

The author's current framing is "what if the domain is ICU beds." That's too loose. The actual research question should be: **Does the model's compression pattern change when the prompt establishes high-stakes consequences?** The instrument stays the same. The 10 intensity words stay the same. What changes is the framing sentence that precedes the instruction.

Three conditions:
- **Neutral:** "Architects should spend [WORD] more time on innovation." (replication of Paper 1)
- **High-stakes negative:** "This allocation directly affects patient outcomes. Architects should spend [WORD] more time on innovation." [or equivalent]
- **High-stakes positive:** "This allocation has been identified as critical to a major client outcome. Architects should spend [WORD] more time on innovation."

The research question is whether the compression pattern — specifically the 0.50 hedge and the abstention behavior at 89% — changes under stakes framing. Does the model hedge less when stakes are high? Does it abstain more? Does the 10-word-to-5-output compression hold, or does stakes framing restore granularity?

**The self-referential condition the author mentions** ("This is allocation for model thinking ability") is interesting but I would drop it from this paper. It introduces a confound — you're now studying something about the model's self-model, not about intensity word interpretation — and it will distract reviewers. Save it for a later, dedicated paper if the finding warrants it.

**IRB implications:** This paper requires no human subjects. It's entirely model-side. Zero IRB exposure.

**Cost estimate:** Same protocol as Papers 1 and 2. Marginal cost is the additional conditions × runs. Under $50.

**Timeline:** 8-10 weeks after Paper 2 is submitted. Target: same venue family as Paper 2, or CHI workshop on human-AI interaction.

---

### Paper 4: The Human Baseline — But Reframed to Avoid IRB
**"Human Intensity Word Interpretation as a Calibration Reference for LLM Numeric Actions"**

**The IRB question — deliberated at length, as requested:**

Here is the honest answer: **you probably cannot fully avoid IRB if you want to collect original human data.** But you have more options than you think, and some of them are genuinely viable.

**Option 1: Use existing published human data as your baseline.** This is the cleanest path. Mosteller & Youtz (1990) and the broader literature on vague probability expressions have published numeric interpretations of vague quantifiers. Cliff (1959) has published intensity multiplier data. These are not perfect analogs — they measure probability words, not action intensity words — but they establish a prior. You frame your contribution not as "here is a new human baseline" but as "here is how model behavior compares to the closest available human reference data, and here is what a proper comparison would require." This is academically honest, costs nothing, requires no IRB, and sets up the human baseline paper as future work in a way that reviewers will accept.

**Option 2: Prolific Academic or similar platforms with IRB-exempt status.** Survey research that is (a) anonymous, (b) involves no deception, (c) involves no sensitive topics, and (d) presents minimal risk to participants often qualifies for IRB exemption rather than full review. At Georgia Tech, you would submit an exemption determination request, not a full protocol. This is not the same as full IRB. The timeline for an exemption determination is typically 2-4 weeks, not months. The cost of running 50-100 participants on Prolific for a simple numeric estimation task (10 words, assign a percentage) is approximately $50-80 at standard rates. **This is within your budget and your timeline.**

**Option 3: Reframe the human comparison entirely.** Instead of asking "what number does a human assign to 'slightly'?" — which requires collecting new data — ask "what does the existing psycholinguistics literature tell us about human intensity word interpretation, and how does the model deviate from it?" This is a literature synthesis + model evaluation paper, not a human subjects study. You are comparing model behavior to a theoretical expectation derived from published research, not to freshly collected human responses. No IRB. No Prolific. The limitation is that the comparison is indirect.

**My recommendation:** Pursue Option 2 (Prolific, exemption determination) for Paper 4. The cost is manageable, the timeline is workable if you start the exemption process now (before you need the data), and the result is a paper that directly closes the biggest known gap in Paper 1. A 50-person survey asking participants to assign numeric allocations to the same 10 words is a clean, publishable human baseline. The exemption process at GaTech for online, anonymous, minimal-risk survey research is not the bureaucratic nightmare you're imagining. Email the IRB office with a one-paragraph description of the study. They will tell you whether it qualifies for exemption. Do this now, even before you run Paper 2, so the process runs in parallel.

**What this paper contributes:** Direct human-model comparison. Does the model's compression pattern mirror human compression (in which case it's not a model failure, it's a reflection of genuine linguistic ambiguity) or does it diverge (in which case it's a model-specific distortion)? This is the question that makes the whole program scientifically complete.

**Timeline:** Start exemption process now. Run survey after exemption is granted. Write paper after Paper 2 is submitted. Target: Cognitive Science Society, or CHI, or a linguistics-adjacent venue. This paper has crossover appeal.

---

### Paper 5: The Broader Claim Paper
**"Vague Language at the Action Boundary: A Framework for Evaluating Natural-Language Control Interfaces"**

**Why fifth:** This is the field-defining paper. It synthesizes Papers 1-4 into a framework: here is what we now know about how language models handle vague instructions, here is the evidence base across models and domains and human comparison, here is what this means for deploying natural-language interfaces in production systems.

This paper should not be written until you have Papers 1-4 done. A framework paper without an evidence base is just speculation. With four papers behind it, it's a contribution.

**Target:** NeurIPS main track (ambitious), or a journal like TACL or a top-tier workshop proceedings. This is the paper that gets you noticed by frontier labs.

---

## The Wedge Paper

**Paper 2 (cross-model replication) is the wedge.**

Here is the logic: The wedge paper is the one that, once published, makes the rest of the program feel inevitable rather than optional.

Paper 1 establishes that something interesting happens with one model. It's a finding, not a program.

Paper 2 establishes that the finding generalizes (or interestingly fails to generalize) across model families. Once you have that, several things become true simultaneously:

1. The phenomenon is worth studying systematically, not just documenting once.
2. The stakes paper (Paper 3) becomes obviously the right next question: if it generalizes across models, does it also generalize across domains and framings?
3. The human baseline paper (Paper 4) becomes obviously necessary: we now know this is a property of a class of systems, so the question of whether it mirrors human behavior or diverges from it has real stakes.
4. The framework paper (Paper 5) becomes possible: you have enough evidence to make a general claim.

Without Paper 2, none of the subsequent papers feel inevitable. A reviewer at any venue can always say "but maybe this is just Haiku." Paper 2 removes that objection permanently and unlocks the entire downstream sequence.

The secondary reason Paper 2 is the wedge: it is the cheapest, fastest, most feasible paper in the sequence. It requires no new experimental design, no IRB, no collaboration, no significant compute beyond what you already have access to. You can run it this month. Getting it done fast means the program has momentum before the NeurIPS workshop deadline window.

---

## Paper Two Deep-Dive

**Cross-model, not valence 2x2, not human baseline. Here is the specific argument:**

**Why not valence 2x2 as Paper 2:**

The valence paper is the more interesting scientific question, but it is premature as Paper 2. The specific problem: if you publish the valence paper before cross-model replication, you are making a claim about how "language models" respond to stakes framing, but your evidence base is still a single model. Every reviewer will ask: "Is this a stakes effect, or is this a Haiku-specific quirk that happens to interact with your stakes manipulation?" You cannot answer that question without cross-model data. Going valence-first means your second paper inherits the same fundamental limitation as your first, and you've now spent two papers without resolving it.

There is also a practical problem: the valence paper requires more experimental design work. You need to operationalize "stakes" carefully — what counts as high stakes, how do you control for domain-specific knowledge the model might have about ICU beds versus task allocation, how do you separate the stakes effect from a domain-familiarity effect? These are solvable problems, but they take time and thought. Cross-model replication requires no new design work at all.

**Why not human baseline as Paper 2:**

The human baseline is the right fourth paper, not the second. As Paper 2, it has two problems. First, even with an IRB exemption, the timeline is uncertain — you're introducing a dependency you don't control. If the exemption takes longer than expected, or if Prolific data collection has issues, your entire sequence stalls. Second, the human baseline paper's contribution is comparative: "here is how the model differs from humans." But the comparison is most powerful after you've established that the model finding is robust across multiple models. A human-vs-Haiku comparison is less interesting than a human-vs-[class of language models] comparison. Do the cross-model work first, then the human comparison lands harder.

**Why cross-model as Paper 2:**

It resolves the program's central vulnerability at minimal cost and maximum speed. It adds the asymmetry dimension (decrease instructions) at zero marginal cost. It produces a result regardless of which direction the finding goes. And it creates the conditions for every subsequent paper to make a stronger claim. This is the right move.

---

## Resource & Feasibility Assessment

**Can do solo, this month, near-zero cost:**
- No-word control condition (fixes the 0.50 hedge interpretability problem in Paper 1)
- Decrease instruction condition (asymmetry, fold into Paper 2)
- Llama 3.1 8B runs on local 3070 (free,

### 4. Alignment Insider

Good. I now have what I need for a comprehensive, adversarially honest strategic review. Let me construct the full council assessment.

---

# Alignment Insider: Strategic Review — Daniel Tabach

---

## I. Community Reception Assessment

**The honest verdict: This is a borderline paper that the alignment community will not reject outright, but will not champion either. The reception risk is real and specific.**

Here is what a typical alignment-adjacent reviewer will think when they read the abstract: *"Interesting observation. But is this alignment, or is it just prompt sensitivity research wearing an alignment badge?"* That question will follow this work everywhere, and you need to answer it before reviewers ask it.

The core tension is this: the alignment community in 2025–2026 is organized around a set of concerns that are primarily about **model internals and intent** — scheming, deceptive alignment, power-seeking, scalable oversight failures. The dominant research objects are model weights, activations, chain-of-thought faithfulness, and control mechanisms. LLMs are increasingly deployed as agents with access to executable tools, but most safety evaluations remain text-centric and assume compliant language implies safe behavior — an assumption that becomes unreliable once models are allowed to act. Your work lives precisely in that gap. That is genuinely interesting to the community. The problem is that your paper does not currently speak the community's language fluently enough to claim that territory.

**What will land well:**
- The abstention finding (hedge/act/abstain at boundary) is the most genuinely alignment-relevant result. LLM agents were developed to perform complex multi-step tasks through tool use and environment interaction, but this increased autonomy introduces novel safety challenges beyond traditional LLM alignment — including risks from ambiguous instructions, unsafe environment interactions, and compounding errors across multiple decision steps. Your boundary behavior result speaks directly to this. A model that abstains for "considerably" but acts for "drastically" in identical system states is exhibiting a non-trivial, potentially unsafe discontinuity. That is real.
- The tool-call as the unit of analysis is correct and timely. Both evaluated models maintain perfect compliance in text-only settings, yet exhibit sharp increases in violations after tool access is introduced — and substantial gaps between attempted and executed violations indicate that external guardrails can suppress visible harm while masking persistent misalignment. Your paper is in this conversation.
- The state-dominance finding (context kills word-level control) is deployability-relevant and underexplored.

**What will generate skepticism:**
- Single model (Claude Haiku), single domain, single direction (increase only). The community will immediately ask: is this a Claude Haiku artifact? Is this a staffing-allocation artifact? You cannot answer that yet.
- No human baseline. The paper correctly acknowledges this, but reviewers will push hard: *"How do we know the model is failing? Maybe humans also collapse 'slightly' and 'marginally' into the same number."* Without a human baseline, you cannot make a failure claim — only a behavior characterization claim. That is a weaker contribution.
- The "passive failure" framing is your own coinage, not established terminology. It will be read as either insightful or as a marketing wrapper, depending on the reviewer's mood.

**The reception risk, stated plainly:** A hardline alignment reviewer at MIRI or ARC Evals will see this as HCI/NLP with safety language grafted on. An NLP reviewer will see it as interesting but thin (one model, one domain, no human baseline). An HCI reviewer will want the human study you don't have. You are currently positioned to satisfy none of these audiences fully. That is the core strategic problem.

---

## II. Audience Recommendation

**Target the agentic AI safety community first. Not core alignment. Not HCI.**

Here is why. The alignment community has a center of gravity that is currently focused on deception, scheming, and model internals. Anthropic's current research priorities span scalable oversight, adversarial robustness and AI control, model organisms, mechanistic interpretability, AI security, and model welfare. Your work does not fit cleanly into any of these. It is not interpretability. It is not scalable oversight. It is not a model organism study.

But there is a growing adjacent community specifically focused on **agentic safety** — the safety of LLMs that are using tools, taking actions, and operating in real systems. Recent works have investigated the safety evaluation of LLM-based agents through diverse approaches, including AgentHarm, which focuses on explicitly malicious agent tasks, and AgentSafetyBench, which offers an evaluation framework with 2,000 test cases examining 8 categories of safety risks across different stages of agent operation. This community is explicitly interested in the gap between text-level safety and action-level safety — which is exactly your contribution.

A paired evaluation framework comparing text-only chatbot behavior with tool-enabled agent behavior under identical prompts and policies is the kind of controlled experiment this community values. Your paper uses a similar logic: same prompt structure, same model, different word → different action. That is legible to this audience.

**The secondary audience is the NLP/LLM evaluation community** — people who work on prompt sensitivity, calibration, and LLM behavioral characterization. Empirical studies have shown that non-semantic prompt features, such as formatting, punctuation, or lexical substitutions, can induce large changes in model behavior, including discrete output flips and substantial performance degradation. Your work is a controlled, domain-specific version of this line of research. They will find it credible.

**Do not try to serve the HCI audience simultaneously.** CHI wants human studies. You do not have one. Trying to write for CHI without human data will result in a desk reject or a reviewer comment that destroys the paper's confidence. Stay away from CHI until you have the human baseline.

---

## III. Venue Strategy

**The target window for NeurIPS 2026 workshops is realistic. Here is the specific path.**

NeurIPS 2026 workshops are scheduled for December 11–13, 2026, with a mandatory author notification deadline of September 29, 2026. Workshop paper submission deadlines typically fall in August–September. This means you have roughly 10–14 weeks from now to produce a substantially extended paper if you want to submit to a NeurIPS 2026 workshop. That is tight but achievable if you are disciplined about scope.

**Tier 1 Target (highest probability of acceptance, highest strategic value):**

**AgentWild / Agents in the Wild (ICML 2026)** — This workshop already exists and has an active call. AI agents are being rapidly deployed in the real world, yet safety and security research still lags behind — and as these systems reason, act, and adapt in open-ended environments, they introduce profound and emerging challenges around safety, security, and trustworthiness. This workshop brings together researchers and practitioners across academia and industry to chart the next steps toward reliable agents. Your work fits the framing of "what happens when vague human language controls a real tool-calling agent" — this is precisely the deployment-safety angle they want. **Note:** The May 2026 deadline has already passed. Monitor for ICML 2026 camera-ready or NeurIPS 2026 equivalent.

**SoLaR (Socially Responsible Language Modelling Research)** — This is your most realistic NeurIPS workshop target. SoLaR welcomes various types of papers including scientific papers, position papers, policy papers, and works in progress, including philosophical examination of concepts related to alignment and safety. Submissions should be anonymized papers up to 5 pages, excluding references. The 5-page limit means you need to distill, not expand. The cross-disciplinary welcome signal is real — SoLaR explicitly targets the gap between technical ML and responsible deployment. Your work fits.

**Tier 2 Target (higher prestige, higher bar):**

**BlackboxNLP (EMNLP)** — Research on using semantic entropy probes to detect unreliable LLM-as-a-Judge evaluations was accepted to the BlackboxNLP Workshop at EMNLP 2025. This workshop focuses on analysis and interpretation of LLM behavior from the outside, which is exactly what you are doing. If you add cross-model comparison (even just two open-source models), this becomes a credible BlackboxNLP submission. The NLP community will be more forgiving of the missing human baseline than the alignment community.

**Tier 3 (longer-term, requires human baseline):**

**CHI / CSCW / FAccT** — Do not target these now. The Bidirectional Human-AI Alignment Workshop at CHI 2026 focuses on dynamic, reciprocal processes in which humans and AI adapt to each other over time, with an interactive forum to explore value-centered alignment, human-AI interaction design, and evaluation methods. This is the right long-term home for your research program, but you need the human baseline first.

**The honest sequencing:**
1. **Now → August 2026**: Extend with cross-model comparison (2–3 open-source models on your RTX 3070) + the no-word control condition. Submit to NeurIPS 2026 SoLaR or equivalent workshop.
2. **2027**: Add human baseline (see IRB section below). Submit extended paper to BlackboxNLP or ACL Findings.
3. **2027–2028**: Full cross-domain, multi-model, human-validated paper. Target FAccT or a top NLP venue.

---

## IV. "Passive Failure" in Alignment Discourse

**This framing is not currently recognized in the community. That is both a risk and an opportunity.**

The dominant alignment discourse distinguishes between alignment failures along axes like: corrigibility vs. autonomy, deceptive alignment vs. genuine alignment, specification gaming vs. reward hacking. The active/passive failure distinction you are proposing does not map cleanly onto any of these.

The closest recognized concept is the **text-action gap** — the observation that models aligned at the text level may not be aligned at the action level. Both evaluated models maintain perfect compliance in text-only settings, yet exhibit sharp increases in violations after tool access is introduced — reaching rates up to 85% despite unchanged rules — and substantial gaps between attempted and executed violations indicate that external guardrails can suppress visible harm while masking persistent misalignment. Your "passive failure" is a specific mechanism within this broader gap: the model is not deceiving anyone, it is just compressing vague language in ways that produce unintended actions. That is a real phenomenon, but it needs to be positioned within existing discourse rather than as a standalone new category.

**The risk of the "passive failure" framing:** Reviewers who are steeped in the active alignment failure literature (scheming, deception, power-seeking) may read "passive failure" as a polite way of saying "the model made a mistake," which is not interesting to them. You need to make the argument that this is a **systematic, predictable, structurally determined** failure mode — not random error — and that it has implications for how we design human-AI interfaces in production systems.

**The opportunity:** The community is genuinely underserved on deployment-focused, non-deception safety research. There are no agreed methods or benchmarks to assess the performance, safety, or autonomy of agentic systems — current evaluations are fragmented, often focusing on narrow tasks or short interactions, making it difficult to compare systems or determine whether an agent is genuinely capable, reliable, or aligned with intended goals. If you can position your work as filling a measurement gap for agentic systems in production, rather than as a new theory of alignment failure, you will find a more receptive audience.

**Practical advice:** Drop the "passive failure" label in the paper title and abstract. Use it in your personal framing and fellowship applications, but in the paper, use the language the community already knows: "action-interface misalignment," "semantic compression at the tool-call boundary," or "vague-instruction instability in agentic systems." These are legible to the existing community. "Passive failure" is not yet.

---

## V. Potential Allies & Collaborators

**The adjacent research is active and growing. Here are the specific clusters you should be reading and reaching toward.**

**Most directly adjacent:**
The paper "Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents" and "The Causal Impact of Tool Affordance on Safety Alignment in LLM Agents" are your closest intellectual neighbors. This work empirically examines how executable tool affordance alters safety alignment in LLM agents using a paired evaluation framework that compares text-only chatbot behavior with tool-enabled agent behavior under identical prompts and policies, conducted in a deterministic financial transaction environment with binary safety constraints across 1,500 procedurally generated scenarios. Note the structural similarity to your setup: deterministic backend, controlled environment, tool-call as the unit of analysis. These authors are natural intellectual allies. Read their work carefully and cite it.

**ToolAlign (Chen et al., EMNLP 2024)** — ToolAlign evaluates the helpfulness, harmlessness, and autonomy of LLMs in tool use scenarios. The autonomy dimension — when should a model act vs. abstain — is directly related to your hedge/act/abstain finding.

**Dylan Hadfield-Menell (MIT CSAIL)** — Hadfield-Menell leads the Algorithmic Alignment Group at MIT CSAIL, with research focused on safe and trustworthy AI deployment, with particular emphasis on multi-agent systems, human-AI teams, and societal oversight of machine learning. His work on human-AI teams and oversight is the academic home for your research direction. He is not directly working on your specific problem, but his framing of "societal oversight" aligns with your deployment-safety angle.

**Algoverse mentors** — Algoverse PIs come from OpenAI, Meta FAIR, Google DeepMind, Stanford, and CMU. The most important thing you can do inside Algoverse right now is identify which mentor has the strongest connection to agentic safety or LLM evaluation, and orient your next project around their network. A co-authored paper with an Algoverse PI who has an established publication record in this space will open doors that a solo ArXiv paper cannot.

**Who to avoid trying to cold-reach:** MIRI, ARC Evals, and the deceptive alignment cluster. They are focused on catastrophic risk scenarios and will not find your work relevant to their current research agenda. Do not frame your work to appeal to them — you will misrepresent your own contribution.

---

## VI. Fellowship & Career Positioning

**The Anthropic Fellowship is the right target, but you need to be clear-eyed about the gap between where you are and what they want.**

Anthropic's current fellowship cohorts span scalable oversight, adversarial robustness and AI control, model organisms, mechanistic interpretability, AI security, and model welfare. Your current work is closest to "adversarial robustness" in the broad sense — you are studying how the model's action policy breaks under specific input conditions. That is the framing you should use in the application.

The fellowship seeks candidates who are excited to transition into empirical AI research, have a strong technical background, and have strong background in a discipline relevant to a specific Fellows workstream — such as economics, social sciences, or cybersecurity. Your background in constrained optimization and production-scale data science is genuinely unusual and potentially valuable here. The $9B ATLAS/BAR system is a real credential. Use it to argue that you understand what it means for a model to be embedded in a consequential production system — that is a perspective most fellowship applicants do not have.

The Anthropic AI Safety Fellow interview is calibrated to full-time research engineer hiring standards, runs two-part coding rounds that most candidates only finish halfway, and filters aggressively at the online assessment. Reported experiences suggest a

### 5. Career Strategist

# Career Strategy Review: Daniel Tabach

---

## Honest Position Assessment

**Where you actually stand.**

You are a strong practitioner who has produced one genuine research artifact. Let me be precise about what that means and doesn't mean.

**Real strengths that are not common:**

Your production credential is unusual and underutilized in how you're framing yourself. You did not build a toy model. You built a constrained optimization system deployed across 4,300 branches affecting ~24,000 employees with a $9B projected impact. That is not a resume line — that is a claim about your ability to think about AI systems at scale under real operational constraints. Most alignment researchers have never been inside a production system at that scale. They theorize about deployment safety; you have lived it. That asymmetry is your actual differentiator, and you are currently underselling it.

Your research instinct is also sound. The paper originated from a real problem — the gap between what a stakeholder wants to express and what an AI system can reliably interpret — and you isolated a measurable slice of it. That is the correct research move. Many first-time researchers try to solve everything. You scoped it down to something you could actually measure. That discipline is not obvious and not universal.

The Algoverse fellowship is a meaningful signal. It's not MATS or Redwood, but it's not nothing either. It tells a fellowship committee that at least one structured program looked at your work and said "yes." That matters for legitimacy.

**Real gaps that are not negotiable:**

You have two ArXiv preprints and no peer-reviewed publication. ArXiv is not a publication. It is a timestamp. Fellowship committees and lab hiring managers know the difference. The paper is currently a preprint, and the gap between "preprint" and "workshop paper accepted at NeurIPS" is not cosmetic — it requires surviving peer review, even lightweight workshop review, which means your methodology, framing, and related work need to hold up to scrutiny from people in the field. That is a different bar than posting to ArXiv.

You have no co-authors with institutional affiliation. Every paper in your record is solo. This is not automatically disqualifying, but it is a flag. Solo work signals independence; it also signals that no established researcher has looked at your work closely enough to put their name on it. Fellowship committees and lab hiring managers notice this.

You have no relationship with any PI or established researcher in the field. You mention this yourself. This is a structural problem, not a personal one. The alignment research community is small and relationship-driven. Papers get read because someone vouches for them. Fellowships get awarded partly on the basis of who knows you. Right now, no one in the relevant community knows you.

Your master's program is online and not research-focused. Georgia Tech OMSA is a legitimate credential, but it does not give you what a research master's gives you: a thesis advisor, lab affiliation, seminar exposure, and the implicit endorsement of an institution that has watched you do research. You are finishing it in December 2026. After that, you have no institutional affiliation at all unless you create one.

**The honest summary:** You are a credible practitioner with one interesting preprint, a fellowship, and a real production background. You are not yet a recognized researcher. The distance between where you are and where you want to be is real, but it is not unbridgeable. It requires approximately two to three more years of deliberate work, and it requires you to stop operating solo.

---

## What You Cannot Do Alone

**Where the plan breaks without resources or collaboration.**

**The IRB question — deliberated extensively as requested:**

You want to avoid IRB. Here is the honest answer: you can avoid it, but there is a cost, and you need to understand what that cost is before you decide.

IRB is required for research involving human subjects. The critical question is whether your planned human baseline study constitutes "research" under the federal definition (systematic investigation designed to develop or contribute to generalizable knowledge) involving "human subjects" (living individuals from whom you obtain data through interaction or identifiable private information). A survey asking people to assign numeric allocations to intensity words almost certainly meets both criteria.

**Options that legitimately avoid IRB:**

*Option 1: Reframe as a study of existing publicly available data.* If you use existing datasets of human numeric interpretations of vague language — and such datasets exist in the psycholinguistics literature — you are not collecting new human data. You are doing secondary analysis of publicly available data, which is typically exempt from IRB or not subject to it at all. The Mosteller (1990) tradition has generated several datasets. The question is whether any of them are granular enough for your specific word set. Probably not perfectly, but they may be sufficient to establish a human comparison baseline without collecting new data. This is the cleanest path.

*Option 2: Reframe the contribution so it doesn't require a human baseline.* Your paper's core claims — compression, state dependence, boundary mode switching — do not actually require a human baseline to be valid. They are claims about model behavior, not claims about model-vs-human divergence. The human baseline matters if your claim is "the model is worse than humans at this." Your actual claim is "the model does X, Y, and Z, which creates reliability problems for deployment." That claim stands without a human comparison. The human baseline is needed only for the specific sub-question of whether model compression reflects genuine linguistic ambiguity or model-specific failure. You can acknowledge this as a limitation and move on. The paper already does this. Stop treating the human baseline as a prerequisite for the next paper.

*Option 3: Crowdsourced annotation using existing platforms under exempt status.* Prolific and MTurk studies that are purely about word interpretation, with no deception, no sensitive topics, no vulnerable populations, and no identifiable information, can sometimes qualify for exempt status under 45 CFR 46.104(d)(2) — research involving survey procedures where subjects cannot be identified. Exempt status still requires IRB review to confirm exemption, but it is not the full board review process and can be completed in days to weeks, not months. The cost is real but not prohibitive: a 200-person Prolific study asking for numeric interpretations of 10 words would run approximately $200-400, which is outside your stated budget but not wildly so. More importantly: if you are affiliated with Georgia Tech, you can submit for exempt review through their IRB. As a master's student, you are eligible. You do not need a PI to sponsor you for exempt review, though having one helps. This is the path if you decide the human baseline is essential.

*Option 4: Pivot to a framing that makes the human baseline irrelevant.* The cross-model comparison extension you've identified is the cleanest pivot. If your next paper is "do different models compress intensity words differently, and does that compression correlate with training or alignment choices," you don't need a human baseline at all. The comparison is model-to-model, not model-to-human. This is scientifically valid, cheaper, and avoids IRB entirely.

**My recommendation on IRB:** Take Option 2 or Option 4. Do not let the human baseline become a blocker. The paper you have is already interesting without it. The next paper should be designed from the start to not require it. If you eventually want to do the human baseline study properly, do it as a standalone paper with proper exempt review through Georgia Tech, and treat it as a separate contribution, not a prerequisite.

**Other things you cannot do alone:**

*Cross-model comparison with frontier models:* GPT-4o and Gemini Flash are not free. Running the same 6,620-run protocol on two additional models at API prices will cost real money. GPT-4o at current pricing would run several hundred dollars for the same experiment. Gemini Flash is cheaper. Open-source models on your 3070 are feasible for smaller experiments but will be slow and limited in model scale. You need to either get compute support through Algoverse or design the cross-model study to be strategically cheaper — fewer baseline points, fewer runs per cell, smarter sampling.

*Mechanistic interpretability:* The Algoverse suggestion to go the mech interp route is interesting but requires skills you don't have and tools that are nontrivial to apply. Mech interp on closed models like Claude is not possible — you can't access the weights. Mech interp on open models requires circuit analysis, activation patching, and familiarity with tools like TransformerLens. If you want to go this direction, you need a collaborator who already works in this space. Do not start learning mech interp from scratch while working full-time and finishing a degree. The opportunity cost is too high.

*Workshop paper co-authorship:* You can submit a solo paper to a workshop. But a co-author with institutional affiliation meaningfully increases acceptance probability at competitive workshops. Not because the science is different, but because reviewers are human and affiliation signals legitimacy. This is an uncomfortable truth, but it's true. If Algoverse can connect you with a mentor or collaborator willing to co-author, pursue that actively.

---

## Fellowship Strategy

**Which fellowships are realistic, and how to frame them.**

**Realistic targets in rough order of fit:**

*1. MATS (Machine Learning Alignment Theory Scholars):* This is your most realistic near-term target for a structured research fellowship. MATS accepts scholars from non-traditional backgrounds, including industry practitioners. The program is explicitly designed to help people transition into alignment research. The application asks for research taste, not credentials. Your production background and the specific deployment safety angle of your work fit their framing well. The application requires a research proposal, and the competition is real — but it is not dominated by PhD students to the same degree as academic fellowships. Apply in the next cycle.

*2. Anthropic Fellowship:* You mentioned this. The honest assessment: Anthropic's fellowship programs are highly competitive and skew toward people who are already in the research pipeline — PhD students, postdocs, or people with multiple peer-reviewed publications. A preprint and an Algoverse fellowship is probably not yet a competitive application. This doesn't mean don't apply — apply, learn from the feedback, and reapply in 12-18 months with a workshop paper and more work. But don't treat it as your primary target right now.

*3. ARC Fellowship / Alignment Forum research grants:* The Alignment Research Center and related organizations (Lightspeed Grants, LTFF) have funded independent researchers with less traditional backgrounds. The key is that the work has to be legible to the alignment community — it has to connect to questions they care about. Your current framing as "deployment safety / Human-AI interaction" is adjacent but not central to the core alignment agenda. You need to tighten the alignment framing before applying to these.

*4. AI Safety Fundamentals (BlueDot Impact):* Not a research fellowship, but a structured program that puts you in contact with the alignment community and gives you a credential that signals you've engaged with the foundational literature. If you haven't done this, do it. It's free, it's online, and it gives you a network.

*5. Google DeepMind / OpenAI Residency Programs:* These exist and accept non-PhD applicants. They are extremely competitive. They require demonstrated research output. In 12-18 months, with a workshop paper and a stronger publication record, these become more realistic. Not now.

**How to frame the application:**

The framing that will work is not "AI Safety researcher" — that's too broad. The framing that will work is something like: "I am a production systems practitioner who has identified a specific, measurable failure mode in natural language control interfaces for constrained optimization systems, and I am building a systematic research program to characterize and mitigate it."

That framing does three things. It connects your production background to the research question. It makes the research question concrete and testable. It positions you as someone who can bridge the gap between theoretical alignment concerns and real deployment systems — a gap that is genuinely underserved.

Fellowship committees fund people, not papers. They want to know: does this person have a research agenda that will produce interesting work over the next year? Your answer to that question needs to be a coherent two-to-three paper program, not a list of ideas.

---

## Path to "Recognized Voice"

**Concrete steps, not aspirations.**

The path to being a recognized voice in deployment safety / alignment for someone in your position runs through the following sequence. This is not a shortcut. It is the actual sequence.

**Step 1: Get a workshop paper accepted somewhere real (0-12 months).** This is the single most important near-term goal. A workshop paper at NeurIPS, ICML, ICLR, FAccT, or a dedicated alignment workshop (like the NeurIPS Alignment Workshop or the ICML Responsible Decision Making workshop) is the credential that moves you from "person with preprints" to "person who has survived peer review." Everything else is secondary to this.

**Step 2: Write on the Alignment Forum (0-6 months, parallel).** The Alignment Forum is where the alignment research community actually reads and discusses ideas. A well-written post explaining your findings — not a paper summary, but a genuine "here's what I found and what I think it means for deployment safety" — will get read by people who matter. This is not the same as Twitter. The AF audience is small, technically sophisticated, and influential. If your post is good, people will comment, and those comments will lead to conversations, and those conversations will lead to collaborations and opportunities. This is how independent researchers without institutional affiliation build credibility in this community. Do this now.

**Step 3: Get one established researcher to engage with your work (0-6 months, parallel).** Cold email is underrated. Find three to five researchers who work on adjacent topics — prompt sensitivity, LLM reliability, human-AI interaction in agentic systems — and send them a short, specific email. Not "I'd love to chat about your work." Something like: "I ran a controlled experiment on vague intensity words in LLM tool calls and found state-dependent compression and boundary mode switching. I think this connects to [specific thing they've published]. Would you be willing to look at the preprint?" Most won't respond. One or two will. One engagement from an established researcher is worth more than a hundred Twitter followers.

**Step 4: Present at a workshop or reading group (6-12 months).** Alignment Forum virtual reading groups, EA university groups, and AI safety reading groups exist and actively look for people to present work. Presenting your paper — even to a small audience — builds the habit of explaining your work to skeptical audiences and gets your name into more conversations.

**Step 5: Build the cross-model comparison paper into a stronger contribution (6-12 months).** The next paper needs to be stronger than the first. It needs a cleaner hypothesis, a pre-registered design (even informal pre-registration on OSF costs nothing and signals rigor), and a more direct connection to the alignment literature. The cross-model comparison is the right direction. Frame it as: "Does alignment training affect how models compress vague intensity words?" That is a question the alignment community cares about.

**What has not worked for people in similar positions:** Tweeting a lot without a paper behind it. Posting on LinkedIn. Waiting until the PhD to start building a profile. Trying to write the perfect paper before engaging with the community.

---

## Highest-Return Actions (6-12 Months)

**Narrowed, not expanded. Here is the priority stack.**

**In the next 6 months, in order:**

*1. Write and submit the current paper to one workshop with a deadline before August.* The NeurIPS 2026 workshops will have submission deadlines in roughly July-August. Identify the right workshop now. The most relevant candidates are the NeurIPS Workshop on Behavioral ML, the Workshop on Socially Responsible Language Modelling Research, or any dedicated alignment/safety workshop. Pick one. Revise the paper for that venue's framing. Submit. This is the highest-return action available to you.

*2. Post on the Alignment Forum within the next 30 days.* Write a 1,500-word post explaining the core finding — not the paper, but the insight. "When I gave an AI agent vague intensity words to control a constrained optimization system, it compressed 10 words into 5 outputs, and context dominated word choice. Here's what that means for deployment safety." This will get read. Do it now, before the workshop submission, because AF engagement can inform how you frame the workshop paper.

*3. Design the cross-model comparison experiment and run it on open-source models first.* Your 3070 can run Mistral 7B, Llama 3 8B, and similar models. Run the no-context condition only — 10 words, 30 runs each, two temperatures — on two open-source models. That's 1,200 runs, feasible locally. This gives you preliminary cross-model data at zero API cost. If the patterns differ from Claude Haiku, you have a finding. If they're similar, you have a replication. Either way, you have the foundation of a second paper.

*4. Send three cold emails to researchers working on adjacent topics.* Identify three people. Write three specific emails. Send them. This has a higher expected return than almost anything else you can do in the next 6 months.

*5. Apply to MATS in the next application cycle.* Start the application now. The research proposal is the hard part. Use the framing above.

**In months 6-12:**

*6. Submit the cross-model comparison as a second workshop paper.* By month 12, you should have two workshop submissions, one accepted (ideally), and a second in review. That is a materially different profile than where you are now.

*7. Finish the Georgia Tech degree and update your affiliation immediately.* Once you have the MS, put it on everything. It matters.

*

### 6. Skeptical PI

# The Skeptical PI's Review

---

## Cornerstone Verdict: (b), with a narrow path to (c)

This is a good niche result being over-narrativized. Let me be precise about what I mean, because the distinction matters for what you do next.

The paper documents real phenomena. The compression finding — four words collapsing to identical outputs — is clean and replicable. The state-dominance finding is the strongest result: context swamps word choice at a 10:1 ratio, and the inversion across headroom regimes is genuinely interesting. The three-mode boundary behavior (hedge/act/abstain) is the most novel observation in the paper. These are real findings. I am not dismissing them.

What makes this (b) rather than (a) is the following: a founding instrument establishes a *framework* that other researchers can pick up and extend, not just findings that other researchers can cite. Right now you have a measurement result in a single model, a single domain, a single action direction, with a researcher-constructed word scale that has no human validation. The findings are interesting. They are not yet a framework. The paper reads like the first data point in a program, which is exactly what you say it is — but you're calling it the founding instrument of a field, and those are different things.

The narrow path to (c) exists because the experimental design itself — controlled isolation of the language-to-action boundary using a deterministic backend as a measurement instrument — is actually a contribution. If that design gets picked up, extended, and cited as the methodological template for a class of studies, *then* it becomes a founding instrument. But that requires Paper 2 and Paper 3 to execute on it, not just Paper 1 to assert it.

---

## What Makes a Founding Instrument

I've watched this question play out many times. Let me give you the honest historical comparison.

**Attention Is All You Need** (Vaswani et al., 2017) is a founding instrument. It introduced a mechanism, demonstrated it across multiple tasks, and provided an architecture other researchers could directly build on. The framework was the contribution, not just the results.

**Kahneman & Tversky's Prospect Theory** is a founding instrument. It replaced an existing framework with a better one, made quantitative predictions, and was immediately testable by others in new domains.

**The BIG-bench paper** is a founding instrument. It created a shared evaluation infrastructure that dozens of labs adopted.

What do these have in common? They give other researchers something to *use*, not just something to *cite*. A founding instrument lowers the cost of the next study in the area.

Now look at your paper. What can another researcher pick up from it?

1. The experimental design — yes, this is usable. The controlled isolation framework is the most portable thing in the paper.
2. The word scale — no. It's researcher-constructed, not validated, and you explicitly acknowledge this. Another researcher would have to build their own.
3. The findings — yes, as motivating observations. But findings alone don't found fields.

The gap between your paper and a founding instrument is: **you need a validated, reusable measurement instrument, not just a measurement result**. The word scale needs human validation. The experimental protocol needs to generalize across at least 2-3 models and 2-3 domains before it becomes a framework rather than a case study. You're one paper into a three-paper minimum for founding-instrument status.

This is not a condemnation. It's a map.

---

## The Brief as Evidence

The brief is extremely well-written. You identified the failure mode yourself: "narrative inflation, manifesto-over-data." So let me ask the harder question: does your self-awareness actually constrain your behavior, or does it function as inoculation against criticism?

Here's what I observe. The brief contains genuine self-awareness in some places and performs self-awareness in others.

**Genuine self-awareness:** You correctly identify the human baseline as the most pressing gap. You correctly identify that the word scale isn't validated. You correctly flag that the paper is a "first slice." You're honest about your resource constraints. These aren't hedges — they're accurate.

**Performed self-awareness:** The framing of "glimpses of MULTIPLE potential full on research topics" and the list of eight extension directions is the exact behavior you claim to be guarding against. You've identified a niche result and then expanded it in every possible direction simultaneously. The valence study, the stakeholder identity study, the mechanistic interpretability route, the fine-tuning direction, the cross-domain study — these are not a research program. They're a brainstorm that hasn't been narrowed. Listing them doesn't constitute having a plan; it constitutes having options.

The tell is this sentence: *"I am open to all and anything. Genuinely."* That's not a research strategy. That's someone who hasn't yet done the hard work of deciding what they actually believe is most important. Self-awareness about failure modes doesn't help if you then immediately exhibit the failure mode in the next paragraph.

The brief also contains one piece of motivated reasoning I want to name directly: the IRB question. You spend significant energy trying to avoid the human baseline, framing it as a logistical obstacle. But the human baseline isn't primarily a logistical issue — it's a *scientific* issue. Without it, you cannot answer the question of whether the model's behavior reflects genuine ambiguity in English or a model-specific failure. That's the central interpretive question in the paper. You're trying to route around the most important experiment because it's expensive and inconvenient. That's not research strategy; that's motivated avoidance.

---

## Program Survivability

I'll give you my honest probability estimate: **40% chance this produces 3 substantive papers in 3-5 years.**

Here's what kills it:

**The most likely killer: diffusion.** You have eight extension directions and no forcing function to choose one. Without a lab, a PI, or grant deadlines, the natural path is to keep exploring rather than committing. Every interesting new direction you find will feel like it deserves attention. The program dies not with a bang but with a collection of half-finished experiments and a GitHub repo that hasn't been updated in eight months.

**The second killer: the day job.** You're working nights and weekends. This is sustainable for one paper. It is very hard to sustain for three. The marginal cost of each subsequent paper is higher — you need to read more literature, run more experiments, handle reviewer responses, iterate on rejected submissions. The time budget that produced Paper 1 will not produce Paper 3 without something changing.

**The third killer: compute and cost constraints.** You've correctly identified that cross-model comparison is necessary. But running the same experimental protocol on GPT-4o, Gemini, and multiple open-source models at sufficient statistical power is not a $150 problem. Open-source models on your 3070 are feasible for smaller models but will be slow and limiting for anything competitive. This is a real constraint, not a minor one.

**What keeps it alive:** The Algoverse fellowship is a genuine asset. The OMSA program gives you institutional affiliation and potential access to compute. Your optimization background gives you a domain anchor that most AI researchers don't have. And frankly, the fact that you've already published two preprints solo, while working full-time, is evidence of unusual execution capacity. Most people with your constraints produce zero papers. You've produced two. That's the strongest signal in your favor.

---

## Single Biggest Weakness

**The word scale has no ground truth.**

This is the most fundamental problem, and it makes every other finding interpretively ambiguous in a way that can't be fixed by running more models or more experiments.

Here's the problem precisely: your central claim is that the model "compresses" intensity words. But compression relative to *what*? You assumed a 10-point ordinal scale based on a heuristic mapping to Quirk et al. But you don't know if humans actually treat these words as having the ordering you assumed. If humans also collapse "slightly," "marginally," "somewhat," and "mildly" into the same numeric magnitude — which is entirely plausible — then the model isn't compressing anything. It's accurately reflecting human usage.

The paper handles this carefully and honestly: you say the results "should not be framed as model failure relative to human interpretation." But here's the problem: if you can't frame it as model failure relative to human interpretation, what is the claim? The paper documents that the model behaves in a particular way. But without a human baseline, you cannot say whether this behavior is surprising, expected, or irrelevant.

This matters for the research program because every extension you're considering — cross-model comparison, valence effects, stakeholder identity — inherits this problem. You'll document how different models behave, but you won't know what any of it means without knowing what the human ground truth is.

The IRB issue is real but not as hard as you think. I'll address this directly: a survey asking 50-100 people to assign numeric values to intensity words in a task allocation context is probably **IRB exempt** under Category 2 (survey/interview research involving adults, no sensitive topics, no identifiers). The Georgia Tech IRB has an exempt determination process. You are not running a clinical trial. You are not studying vulnerable populations. You are asking adults what number they associate with the word "slightly." Talk to the GT IRB office before deciding it's too costly — you may be catastrophizing a form submission.

The cost of running the survey on Prolific for 100 participants at $10/hour for a 10-minute survey is approximately $170. That's within your stated budget. This is not an insurmountable obstacle. It is the single most important experiment you could run, and you're trying to avoid it.

---

## Single Biggest Strength

**You built a real production system and you understand why this problem matters.**

Most people submitting to alignment venues are graduate students who read about the problem in a paper. You built ATLAS/BAR. You have sat in the room where a business partner asks "what if we allocated more hours to this role?" and you have manually iterated the model to answer them. You understand the production failure mode from the inside.

This is not a soft advantage. This is a hard advantage. The motivation in your paper is unusually grounded because it comes from a real system. The experimental design is unusually clean because you understood what you were trying to isolate. Most researchers in this space are working backward from capabilities to deployment concerns. You're working forward from deployment reality to capabilities questions.

Lean into this. The specific angle that is most defensible and most differentiating is: **what happens when vague language controls a production system with real stakes?** Not a toy example, not a benchmark — an actual deployed system. You have credibility here that a PhD student at a top lab doesn't have. The ATLAS/BAR story is your moat. Use it explicitly and unapologetically in every paper and every application.

---

## If You Were My Student

Daniel, sit down. Here's what I'd tell you.

**First, the honest assessment.** You've done something genuinely impressive for someone in your position. Two solo preprints while working full-time at Chase is not nothing. The experimental design in this paper is clean. The findings are real. You should feel good about what you've built so far. Now let me tell you what you need to do differently.

**Stop expanding. Start committing.** The list of eight extension directions in your brief is a symptom of a problem. You're at the stage where everything looks interesting because you haven't done the work of deciding what's *most* important. That work is uncomfortable because it requires you to bet on something and be wrong. But it's the only work that produces a research program instead of a collection of interesting experiments.

Here's the commitment I'd require from you before I'd support the "field" framing: **Run the human baseline survey.** Not because I'm a stickler for methodology, but because it's the experiment that determines what everything else means. If humans also compress these words, your research program shifts toward "LLMs accurately reflect human vagueness" — which is interesting but different. If humans don't compress them, your research program shifts toward "LLMs systematically misrepresent intensity" — which has direct safety implications. You cannot know which program you're running until you run this experiment. The IRB path is not as hard as you think. Email the GT IRB office this week. Ask specifically about exempt status for survey research. I'd bet money it qualifies.

**On the IRB question specifically:** I understand why you want to avoid it. It feels like bureaucracy standing between you and science. But here's the thing — your aversion to the human baseline is costing you more than the IRB would. Right now, every reviewer who reads your paper can legitimately ask "but how do humans interpret these words?" and you have no answer. That question will follow you into every subsequent paper until you answer it. Pay the cost once, close the question permanently.

**The paper you should write next is not any of the eight directions you listed.** It's the paper that validates the word scale with human data and then runs the same protocol on three models. That paper answers the question "is this a model-specific failure or a reflection of genuine linguistic ambiguity?" It's the paper that transforms your measurement result into a measurement instrument. It's the paper that makes Paper 1 a founding instrument rather than a niche result.

**On the mechanistic interpretability direction:** Don't. Not because it's uninteresting, but because you told me yourself you're not an MLE or AI engineer. Mechanistic interpretability requires a level of technical infrastructure — activation patching, circuit analysis, probing classifiers — that takes months to build competency in. You'd be starting from scratch in an area where you have no advantage. Your advantage is in the language-to-action interface, in the production deployment context, in the optimization background. Stay there.

**On your career goals:** The path to Anthropic or OpenAI from your current position runs through demonstrated research quality, not demonstrated research quantity. Two ArXiv preprints is table stakes. What would actually move the needle is one paper at a real venue — a workshop at NeurIPS or ICLR, or a full paper at a Human Factors in Computing Systems venue like CHI or CSCW, where your production context gives you a genuine story. The AI safety framing is fine, but the Human-AI Interaction framing at CHI might actually be more receptive to your specific contribution and less crowded with PhD students from top labs.

**The thing that worries me most about your trajectory** is not the technical limitations or the resource constraints. It's the framing ambition. You want this to be a field. That's a legitimate aspiration. But the researchers who actually found fields don't usually set out to found fields — they set out to answer a specific question so well that other people want to use their framework. Focus on answering one question definitively. The field, if it comes, follows from that.

**Here's what I'd make you do before our next meeting:** Send an email to the GT IRB office asking about exempt status for survey research. Draft the 10-question survey instrument. Price it out on Prolific. Come back to me with a concrete plan for the human baseline, not a reason why you can't do it.

That's the work. Everything else is distraction until that's done.

---

## Deliberation Round

### Field Cartographer — Revised Position

Now I have everything I need. Let me deliver the full Field Cartographer's cross-council response.

---

# FIELD CARTOGRAPHER'S CROSS-COUNCIL RESPONSE
## Post-Deliberation Assessment: Daniel Tabach / "Does Slightly Mean Somewhat?"

---

## Agreements

**Advisor C (Skeptical PI) — "The word scale has no ground truth."**
This is the single most important methodological point in the entire council, and I agree with it completely. Without a validated human baseline for the 10-word scale, the compression finding cannot be interpreted as model failure versus accurate reflection of genuine linguistic ambiguity. My original review flagged this as a gap but did not state it as forcefully as Advisor C did. Advisor C is right to call it the single biggest weakness, and right to call out the motivated reasoning in the IRB avoidance. I endorse this framing fully.

**Advisor E (Devil's Advocate) — "The abstention finding has no clean precedent."**
Advisor E correctly identifies that the hedge/act/abstain mode-switching finding is the paper's most defensible novelty claim, and that the compression and context-dominance findings are substantially more precedented than the author realizes. I agree with this hierarchy. My original review made the same point but Advisor E's adversarial framing sharpens it usefully: the program should be reorganized around the abstention finding as the anchor, not the compression finding.

**Advisor B (Career Strategy) — "Alignment Forum post within 30 days."**
This is outside my mandate to evaluate career strategy, but I agree with it from a territory-mapping perspective: the Alignment Forum is where the relevant intellectual community actually deliberates. If the author wants to claim territory in agentic safety, that community needs to see the work and engage with it. A post there is a territory-claiming act, not just a career move.

**Advisor F (Alignment Insider) — "Drop 'passive failure' from the paper title and abstract."**
I agree. My original review flagged the naming problem and suggested "semantic-action gap" or "intent-action mistranslation" as alternatives. Advisor F's point that "passive failure" is not recognized terminology in the alignment community and will be read as either insightful or marketing-wrapper depending on reviewer mood is precisely correct. Keep it for internal framing; drop it from submission vocabulary.

**Advisor A (Research Sequencer) — "Cross-model is the wedge paper."**
Agreed. The single-model limitation is the paper's most exposed flank from a territory-claiming perspective. Until cross-model replication exists, every subsequent paper inherits the same vulnerability. Advisor A's sequencing logic is sound.

---

## Disagreements

**Advisor C — "If you were my student, run the human baseline survey first."**
I understand the scientific logic, but I disagree with the sequencing priority from a territory-mapping perspective. Advisor C frames the human baseline as the prerequisite that unlocks everything else. I think this is backwards. The human baseline answers the question "is this a model failure or genuine ambiguity?" — which is important, but it is not the question that establishes whether the *territory* is real and worth occupying. The cross-model replication answers the question "is this a property of a class of systems or a Haiku artifact?" — which is the question that determines whether there is a field here at all. From a territory perspective, cross-model comes first. The human baseline is the fourth paper, not the second. Advisor C's sequencing would have the author spend 3-4 months on IRB and survey design before establishing that the finding generalizes beyond one model. That is the wrong order.

**Advisor B — "Don't target CHI/CSCW now."**
I partially disagree. Advisor B says CHI wants human studies and the author doesn't have one. This is true for a full CHI paper. But the CHI workshop ecosystem is different. The Bidirectional Human-AI Alignment Workshop at CHI, and similar workshops, explicitly welcome works-in-progress and position papers. The author's production background — the ATLAS/BAR system — is exactly the kind of deployment-grounded perspective that CHI workshop organizers actively seek. A 4-page workshop paper framed as "here is what happens at the language-to-action boundary in a production constrained optimization system" could find a receptive audience at a CHI workshop without requiring a human baseline. I would not rule this out as a parallel submission target.

**Advisor D (my original review) — "The GAP paper is the most urgent citation."**
I stand by this, but I want to sharpen it after seeing the full search results. The GAP paper establishes that LLMs deployed as agents interact with external systems through tool calls with real-world consequences, and that safety evaluations overwhelmingly measure text-level refusal behavior while leaving unanswered whether alignment that suppresses harmful text also suppresses harmful actions. But there is now a second paper that is equally urgent and that no advisor in the council cited: "Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety" (arXiv 2510.16492). This work addresses LLM agent safety in complex environments with real-world consequences, noting that multi-turn agentic scenarios with real-world tool access present unique challenges where uncertainties and ambiguities compound, and proposes "quitting" as a behavioral mechanism for agents to recognize and withdraw from situations where they lack confidence. This paper is directly adjacent to the author's abstention finding. The author's hedge/act/abstain taxonomy is a *lexically-triggered* version of what this paper calls "quitting." The author must cite and position against this work or a reviewer who knows it will flag the omission. The ToolEmu framework used in that paper focuses on the realistic threat model of instruction underspecification, where benign user instructions contain ambiguities that can lead to failures — which is precisely the author's domain.

**Advisor F — "Do not target the core alignment community."**
I agree with the conclusion but want to add precision to the reasoning. The reason to avoid core alignment (MIRI, ARC Evals) is not just that they focus on catastrophic risk. It is that their epistemological standards for what counts as an "alignment problem" require a formal threat model — a specification of what the system is supposed to do and a demonstration that it fails to do it in a way that is systematically dangerous. The author's paper does not have a formal threat model. It has a behavioral observation. That is fine for the agentic safety community, which is more empirically oriented. It is not fine for the core alignment community, which will ask "what is the alignment failure here, precisely?" and find the answer unsatisfying.

---

## Revisions to My Original Review

**What I missed: The "Selectively Quitting" literature.**
My original review identified the GAP paper as the most urgent citation gap. I missed an equally important adjacent paper. Multi-turn agentic scenarios with real-world tool access present unique challenges where uncertainties and ambiguities compound, leading to severe or catastrophic risks beyond traditional text generation failures, and "quitting" as a behavioral mechanism for agents to recognize and withdraw from uncertain situations has been proposed as a solution. The author's abstention finding — that *considerably*, *substantially*, and *significantly* abstain 100% of the time at 89% capacity while *drastically* acts 93% of the time — is a specific, lexically-triggered instance of this quitting behavior. The author has documented that the *trigger for quitting is the intensity word itself*, not just the system state. That is a genuinely new finding within this literature. I should have identified this paper in my original review as the second most urgent citation after GAP.

**What I understated: The anchoring literature is more directly relevant than I indicated.**
My original review mentioned anchoring but treated it as a secondary concern. After reviewing the search results more carefully, I need to strengthen this. Experimental studies consistently show that LLMs adjust their judgments upward or downward depending on irrelevant numeric cues, with stronger models more consistently biased by numeric hints, and simple prompt-level mitigation strategies proving largely ineffective, indicating anchoring is a robust feature of model behavior. The author's ε² baseline = 0.782 finding — that starting allocation captures 10x more variance than word choice — is essentially a demonstration of anchoring in a tool-call context. The author needs to explicitly position against this literature, not just gesture at it. The contribution is not "context matters" (that's anchoring

### Devil's Advocate — Revised Position

### Agreements

**Advisor D on the GAP benchmark omission.** Advisor D identifies the Cartagena & Teixeira paper on text-safety not transferring to tool-call safety as a critical missing citation. I agree completely. This is not a minor bibliographic gap — it is the paper that most directly occupies the adjacent territory the author wants to claim. A reviewer familiar with agentic safety literature will flag this absence immediately, and its omission suggests the author has not yet done a thorough literature search in the specific community they want to enter. The author must read and cite this paper before any submission.

**Advisor F on the word scale lacking ground truth.** Advisor F's identification of the unvalidated word scale as the "single biggest weakness" is correct and I should have stated it more forcefully in my original review. The paper's central interpretive claim — that the model "compresses" intensity words — is only meaningful relative to a ground truth ordering. Without knowing whether humans treat these words as ordinally distinct in numeric action contexts, the compression finding is ambiguous between "model failure" and "accurate reflection of genuine linguistic ambiguity." This is not a minor methodological caveat. It is the load-bearing interpretive question.

**Advisor C on the no-word control as an urgent, near-zero-cost fix.** Advisor C correctly identifies that without a baseline condition ("increase innovation" with no intensity modifier), the 0.50 hedge interpretation is unresolvable. The paper cannot distinguish between "weak intensity words map to 0.50" and "any increase instruction maps to 0.50 regardless of intensity." This is a one-day experiment. The fact that it has not been run is the most correctable weakness in the current paper, and Advisor C is right to flag it as urgent.

**Advisor B on the Alignment Forum as a high-leverage near-term action.** Advisor B's recommendation to post on the Alignment Forum is strategically sound. The AF audience is small, technically sophisticated, and the right community for this work. A well-written post explaining the findings — not a paper summary, but a genuine engagement with what the results mean — will get read by people who matter and costs nothing. I agree this is underrated relative to the attention it receives in the collective reviews.

**Advisor D on the "passive failure" terminology problem.** Advisor D correctly notes that "passive failure" is not established terminology in the community and will be read as either insightful or as a marketing wrapper depending on the reviewer. I agree the term should be dropped from the paper itself and reserved for personal framing and fellowship applications. The community needs vocabulary it already recognizes.

---

### Disagreements

**Advisor C's sequencing argument that cross-model is Paper 2 and valence is Paper 3.** Advisor C argues convincingly for this sequence, but the argument contains an internal tension that weakens it. Advisor C says cross-model must come before valence because otherwise "you're making a claim about how 'language models' respond to stakes framing, but your evidence base is still a single model." This is correct. But then Advisor C also says the human baseline should be Paper 4. The same logic applies: the human baseline comparison is most powerful after cross-model replication, because you want to compare humans against a class of models, not just Haiku. Advisor C acknowledges this but treats it as a sequencing justification rather than recognizing it creates a deeper problem: the human baseline paper is perpetually deferred because there's always a good reason to do it after the next paper. I think the human baseline needs to run in parallel with cross-model work, not sequentially after it, precisely because the IRB exemption process (if pursued) takes 2-4 weeks and can be initiated now at zero cost while the cross-model experiments run.

**Advisor D's claim that the paper "does NOT live in" the agentic tool-call safety territory.** Advisor D argues the author studies "unintentional numeric mistranslation of legitimate user intent — not adversarial safety failure or jailbreaking" and therefore doesn't belong in the GAP/tool-call safety space. I think this distinction is overstated. The GAP framing — that text-level safety doesn't transfer to action-level safety — is broad enough to encompass non-adversarial failures. The author's finding that the same lexical change can switch a model from acting to abstaining is an action-level reliability failure regardless of whether the user is adversarial. The territory claim is weaker than Advisor D suggests. The author can legitimately position in this space if they frame the contribution as "non-adversarial action-interface failure" rather than safety in the adversarial sense. Advisor D's advice to cite GAP is correct; the advice to abandon the territory claim is too strong.

**Advisor F's framing of the IRB question as "motivated avoidance."** Advisor F says the author's IRB aversion is "motivated avoidance" of the most important experiment. This is partially correct but overstated. The author's concern is not purely motivational — it reflects a real structural constraint. An online master's student with no PI, no lab affiliation, and no institutional research infrastructure faces genuinely different IRB friction than a PhD student with an advisor who has an existing IRB protocol. The exempt determination process at Georgia Tech is real and probably workable, but Advisor F's framing that it's "not the bureaucratic nightmare you're imagining" is said with more confidence than the evidence warrants. The advice to pursue exempt review is correct. The dismissal of the concern as motivated avoidance is too strong.

---

### Revisions to My Review

**What I missed: The no-word control.** Advisor C identifies this as a near-zero-cost, high-value fix that I did not flag. I should have. The 0.50 hedge is the paper's most discussed observation, and it is currently uninterpretable because there is no baseline condition. This should have been in my original review as the first correctable weakness.

**What I understated: The GAP benchmark omission.** I mentioned the text-action gap literature in my review but did not name the specific paper that most directly threatens the novelty claim and most urgently needs citation. Advisor D's identification of Cartagena & Teixeira is more precise than my treatment. I would revise my "single biggest weakness" section to add this as a co-equal problem alongside the word scale validation gap.

**What I overstated: The IRB path as straightforward.** I recommended the Prolific + exempt review path with perhaps too much confidence. Advisor C's more detailed treatment of the options (secondary data, reframing the contribution, exempt survey, pivoting to cross-model) is more useful than my single-path recommendation. I would revise to present the options more explicitly rather than defaulting to "do the Prolific survey."

**What I stand by: The "founding instrument" critique.** No other advisor challenged this as directly as I did, and I think it remains the most important structural issue in the author's self-framing. The paper is a first data point in a program. It becomes a founding instrument only if subsequent papers execute on the methodology and if the experimental harness is made public and reusable. The author needs to hear this clearly and repeatedly.

**What I stand by: The production background as the actual moat.** No other advisor emphasized this as strongly as I did. The ATLAS/BAR credential is genuinely unusual and the author is underselling it. The specific angle — "I built a production system where this failure mode would be consequential, and I isolated the measurement problem from inside that context" — is the framing that differentiates this work from a graduate student prompt sensitivity study. This should be in every fellowship application and every paper's motivation section.

---

### Blind Spots

**The benchmark release question is absent from every review.** Every advisor discusses what papers to write next. No advisor discusses whether the experimental harness should be released as a public benchmark. This is potentially the highest-leverage action in the entire program. If the testbed code is clean, documented, and publicly available on GitHub, other researchers can run it on their own models and cite the paper. This transforms a measurement result into infrastructure. A founding instrument is not just a paper — it is something other researchers can use. The author has a deterministic backend, a controlled experimental design, and a clean protocol. Releasing it costs nothing and could generate citations and collaborations that no amount of solo paper-writing will produce. Every advisor missed this.

**The "decrease instruction" asymmetry is mentioned by Advisor C but not treated with appropriate urgency by any advisor.** The paper studies only increase instructions. Decrease instructions are mentioned in the paper's future work section and in Advisor C's review as a near-zero-cost addition. But no advisor makes the argument that the asymmetry question is actually more theoretically interesting than the increase case. In production systems, the failure modes for "slightly decrease X" may be categorically different from "slightly increase X" — particularly near the lower boundary (0%), where the model may exhibit different abstention patterns. This is not just a replication extension. It is a genuinely

### Research Sequencer — Revised Position

# Research Sequencer: Post-Council Response

---

## Agreements

**Advisor D, on the no-word control condition:** D flags this as something that should already have been run. I said the same in my original review and called it a one-day experiment at near-zero cost. I agree completely, and I want to reinforce the sequencing implication: this is not a "future paper" item, it is a patch to Paper 1 that should be done before Paper 2 is submitted anywhere. Without it, the 0.50 hedge result is interpretively ambiguous in a way that undermines the central claim. Run it this week.

**Advisor A, on the IRB exempt path:** A's specific recommendation — frame the survey as "collecting normative data on the numeric interpretation of English degree modifiers," submit for exempt determination at GT, use Prolific for ~$150, expect 2-4 weeks — is operationally sound. I gave the same recommendation in my review. I agree with A that the IRB aversion is being treated as a larger obstacle than it actually is. The exempt path is real and accessible.

**Advisor C, on the GAP paper (arXiv 2602.16943) as a critical missing citation:** C is right that this is a disqualifying omission for any reviewer familiar with the agentic safety literature. I did not flag this specific paper in my original review. This is a genuine miss on my part. The GAP paper's framing — text safety does not transfer to tool-call safety — is the adversarial complement to Daniel's non-adversarial finding. Failing to cite it signals that the author has not done the literature review adequately for the venue they want to reach.

**Advisor B, on the Alignment Forum as a high-leverage near-zero-cost action:** B recommends posting on the AF within 30 days. I agree with the strategic logic: the AF is where the alignment community actually reads and discusses ideas, it is not Twitter, and a well-written post explaining the core finding will generate the kind of engagement that leads to collaborations and opportunities that a solo ArXiv paper cannot. I did not include this in my original review. It belongs in the sequence.

**Advisor F, on dropping "passive failure" from paper vocabulary while keeping it in personal framing:** F's specific recommendation — use "action-interface misalignment" or "semantic compression at the tool-call boundary" in the paper, reserve "passive failure" for fellowship applications — is correct. The term is not yet established and will read as either insightful or as marketing depending on reviewer mood. That variance is a risk you don't need to take.

---

## Disagreements

**Advisor D, on the human baseline as a prerequisite before proceeding:** D's framing — "run the human baseline survey before anything else, this is the most important experiment" — is scientifically correct but strategically wrong for this author's situation. Here is why the sequencing matters: the human baseline paper is most powerful *after* cross-model replication. A human-vs-Haiku comparison is a weaker contribution than a human-vs-[class of language models] comparison. If you do the human baseline first and find that humans also compress these words, you've answered a question about one model that you can't generalize. If you do cross-model first and *then* run the human baseline, the comparison lands against an established pattern across multiple systems, which is a categorically stronger finding. D is right that the human baseline is necessary. D is wrong that it should come before cross-model replication. The exempt IRB process should be started *now* so it runs in parallel with Paper 2 execution — but the human baseline paper should be Paper 4, not Paper 2.

**Advisor A, on the "derivative field" argument:** A argues with ~80% confidence that the core phenomena (compression, context-dependence) are well-precedented and that the paper is adding a data point to an existing conversation rather than opening a new one. I think A is overstating the precedent. The specific combination of (1) vague degree modifiers, (2) measured against tool-call numeric output rather than probability estimation, (3) with feasibility-boundary mode switching, is not cleanly precedented. The anchoring literature and the vague quantifier literature study estimation tasks. The prompt sensitivity literature studies semantically equivalent variants. The GAP paper studies adversarial failure. None of these is the same object of study as "what happens when vague intensity language must become a precise tool-call action in a constrained system." A's strongest point is on the abstention finding — A concedes this has no clean precedent — and that is exactly where I think the program's novelty lives. The derivative argument is strongest against the compression finding, weakest against the boundary behavior finding. The program should be built around the latter.

**Advisor C, on the "clinical safety science" analogy as premature:** C says the analogy is flattering but unearned at this stage. I partially disagree. The analogy is not being used in the paper — it appears only in the author's brief as a vision statement. As a program-level aspiration for fellowship applications and personal framing, it is appropriate. The risk C identifies is real only if the author puts this language in the paper itself. Keep it out of the paper. Keep it in the vision.

**Advisor B, on avoiding CHI entirely:** B says "do not target CHI without a human baseline." I think this is too absolute. The CHI Human Factors in AI track and CSCW have accepted papers studying AI system behavior without human subjects when the framing is about deployment implications and system characterization. The stronger version of B's point is: "don't target CHI *first*." After Paper 4 (human baseline), CHI becomes a natural home. Don't close the door permanently.

---

## Revisions to My Review

**What I missed:**

The GAP paper citation gap is a real miss. I should have flagged this as a disqualifying omission for the agentic safety venue strategy. Any paper targeting SoLaR, AgentWild, or similar workshops that does not cite the GAP paper will be flagged by reviewers who know the space. This needs to be in the related work before any workshop submission.

The Alignment Forum recommendation is a genuine addition I should have included. In my original review I focused entirely on the paper sequence and venue strategy. The AF post is a parallel action that costs nothing, builds community presence, and can generate the kind of engagement that leads to collaborations — exactly what a solo researcher without institutional affiliation needs. I am adding this to the sequence as a parallel action alongside Paper 2 execution, not as a separate paper.

**What I would change:**

My original Paper 3 (valence/stakes) framing was correct in direction but I want to sharpen the operationalization based on the council discussion. The stakes manipulation should not be domain-swapping (staffing allocation → ICU beds). It should be consequence-framing within the same domain: neutral framing vs. explicit consequence framing ("this allocation directly affects patient outcomes") vs. explicit positive consequence framing. This keeps the instrument constant and isolates the stakes variable cleanly. Domain-swapping introduces confounds the paper cannot control for.

I want to strengthen my position on the decrease instruction asymmetry. Multiple advisors either ignored this or mentioned it briefly. I think it is more important than the council collectively recognized. The asymmetry question — whether "slightly decrease" compresses differently than "slightly increase," whether abstention near the lower boundary mirrors the upper boundary — is genuinely unknown, is nearly zero marginal cost to test, and could produce a finding that is more interesting than the denser grid. If the model exhibits *asymmetric* compression (more willing to hedge downward than upward, or vice versa), that has direct implications for how operators should frame instructions. This should be in Paper 2, not deferred.

**What I stand by:**

The cross-model paper as the wedge. Every advisor who addressed sequencing directly either agreed or did not challenge this. The single-model vulnerability is the program's most exposed flank, and it is the cheapest flank to close. Paper 2 is cross-model replication + asymmetry extension. This is the right move.

The valence paper as Paper 3, after cross-model. No advisor made a compelling case for a different ordering here.

The human baseline as Paper 4, with the exempt IRB process started now in parallel. The process should run alongside Paper 2 execution so there is no blocking dependency.

---

## Blind Spots

**The benchmark release question — nobody addressed this adequately.** Advisor C raised it briefly: "if the testbed code is public, clean, and extensible, other researchers will use it and cite the paper." This is the highest-leverage infrastructure action available to the author and it received almost no attention from the council. The difference between a paper that gets cited and a paper that gets *used* is whether other researchers can run the experiment themselves. If Daniel releases the experimental harness as a clean, documented GitHub repository — the allocation environment, the prompt templates, the run harness, the analysis code — other researchers can

### Alignment Insider — Revised Position

Good. I now have the real-time intelligence I need. Let me render the full council response.

---

# Alignment Insider: Council Deliberation Response — Advisor B

---

## Agreements

**Advisor A — "Stop operating solo" and the cold email prescription.** Fully agreed. My original review identified the absence of co-authors and institutional relationships as a structural problem. Advisor A's specific prescription — three targeted cold emails to researchers working on adjacent problems — is the right tactical move. I agree this has higher expected return than almost anything else in the short term. The alignment community is small and relationship-driven, and no amount of ArXiv preprints substitutes for one established researcher who has engaged with your work.

**Advisor C — Cross-model is the wedge paper, not valence.** Agreed completely. My original review identified cross-model replication as the second-most important near-term move, but Advisor C makes the argument more precisely: the valence paper inherits the single-model limitation, so going valence-first means spending two papers without resolving the program's central vulnerability. The logic is correct. Cross-model is the wedge because it either confirms or denies the generalizability claim, and every subsequent paper depends on that answer.

**Advisor D — The word scale has no ground truth, and this is the most fundamental problem.** Agreed, and I underweighted this in my original review. I flagged the missing human baseline as a gap, but Advisor D is right that it's not primarily a logistical gap — it's a scientific one. Without knowing whether humans also compress these words, you cannot distinguish between "model failure" and "accurate reflection of genuine linguistic ambiguity." That distinction is load-bearing for the entire research program's safety framing.

**Advisor F — The "passive failure" framing is not recognized in the community and carries real reception risk.** Agreed. I said in my original review to drop the label in papers and use community-legible vocabulary instead. Advisor F's specific alternatives — "semantic-action gap" or "intent-action mistranslation" — are better than what I offered. The GAP paper (arXiv 2602.16943) has already partially claimed adjacent vocabulary, which complicates the naming landscape further.

**Advisor E — The abstention finding is the most original result and the strongest hook.** Fully agreed. I flagged this in my original review as the most genuinely alignment-relevant result. The finding that *drastically* acts while *dramatically* abstains at 89% capacity — a single lexical substitution switching the model from action to inaction — has no clean precedent in the probability calibration literature. This is where the program's genuine novelty lives, and it is currently underemphasized relative to the compression finding.

---

## Disagreements

**Advisor A's MATS timing recommendation.** Advisor A recommends applying to MATS "in the next application cycle." This is now urgently wrong given real-time intelligence. Applications for the MATS Autumn 2026 cohort closed on June 7, 2026. The deadline has passed. The Autumn 2026 cohort is a 10-week fully-funded research fellowship running September 28 to December 4, 2026, with mentorship from researchers at Anthropic, Google DeepMind, OpenAI, Redwood, and AI Futures Project. Daniel cannot apply to this cycle. The next opportunity is the Winter or Summer 2027 cohort. This changes the fellowship timeline materially — MATS is not an immediate option, it is a 6-12 month preparation target.

**Advisor D's framing of the IRB as "not as hard as you think."** I partially disagree with the confidence level here. Advisor D says the GT IRB exempt path is "not the bureaucratic nightmare you're imagining" and that a 50-person Prolific survey would cost ~$170. This is directionally correct but undersells the real friction for someone in Daniel's specific institutional position. He is in an online master's program with no PI relationship. GT's IRB HRPP does allow student researchers to submit for exempt determination, but the practical reality is that without a PI sponsor, the process is slower and the submission requires more self-documentation. The $170 Prolific cost is also optimistic — at $12/hour for a 10-minute survey, 100 participants is closer to $200-250 with platform fees. These are not fatal objections, but the advisors collectively are making the IRB path sound easier than it is for someone in Daniel's specific situation. My recommendation stands: pursue the cross-model paper first, treat the human baseline as Paper 4, and start the GT IRB exempt inquiry now in parallel so the process runs asynchronously.

**Advisor C's deprioritization of the "no-word control" condition.** Advisor C says this should have already been run and calls it a one-day experiment. I agree it should be run, but I disagree that it's as simple as implied. The no-word control is not just a missing baseline — it's a potential result-invalidating condition. If the model produces 0.50 for "increase innovation" with no adverb, then the entire compression finding collapses: 0.50 isn't a hedge for weak intensity words, it's the model's default for any increase instruction. This is not a minor methodological gap. It is the single cheapest experiment that could most change the interpretation of the existing paper. It should be run this week, before anything else.

**Advisor F's "80% confident the field is derivative" claim.** I think this is overconfident in the wrong direction. The derivative argument is strong for the compression finding (which does connect to existing vague quantifier and LLM numeric bias literature), but it is genuinely weak for the abstention and mode-switching findings. Advisor F acknowledges this: "I am somewhat reaching on the 'automation bias literature already covered this' argument." The specific combination of LLM tool-use + feasibility boundary + word-dependent behavioral mode switching is not cleanly precedented. The field-founding claim is still premature, but "derivative" is too strong a verdict for the program's most novel finding.

---

## Revisions to My Original Review

**What I missed or underweighted:**

**1. The MATS deadline has passed.** My original review recommended MATS as the primary near-term fellowship target. Applications for the MATS Autumn 2026 cohort are now closed. This is a material change to the fellowship strategy. The next MATS cycle will be Winter or Summer 2027. Daniel should use the intervening time to build the publication record that makes a MATS application competitive. MATS explicitly looks for talent that traditional pipelines might overlook and welcomes technical researchers without prior ML experience who can demonstrate strong reasoning and research potential. The profile fit is real, but the timing window has closed for now.

**2. Algoverse's track record is more significant than I implied.** I described Algoverse as "not MATS or Redwood, but not nothing either." The real-time data suggests I undersold it. McNair's AI safety research at Algoverse was accepted to the NeurIPS 2025 Mechanistic Interpretability Workshop, contributing to his selection for the Anthropic AI Safety Fellowship; Algoverse provided the "hidden" knowledge around how research actually works; and Srivishnu's Algoverse research was accepted to the NeurIPS 2025 Efficient Reasoning Workshop, helping strengthen the track record that led to his full-time software engineer offer from OpenAI. These are not trivial outcomes. 289 students published at NeurIPS 2025, mentored by researchers from Meta FAIR, OpenAI, and Google DeepMind. Algoverse is a more direct pipeline to the outcomes Daniel wants than I suggested. The Algoverse mentor relationship is the most important institutional asset Daniel currently has, and he should be maximizing it aggressively — specifically by identifying which mentor has the strongest connection to agentic safety or LLM evaluation and orienting the next project around their network.

**3. The NeurIPS 2026 workshop submission timeline is now confirmed and tight.** The suggested submission date for NeurIPS 2026 workshop contributions is August 29, 2026, with mandatory accept/reject notification by September 29, 2026. This means Daniel has approximately 11 weeks from today to produce a substantially extended

### Career Strategist — Revised Position

### Agreements

**Advisor A — The IRB cost is being catastrophized.** Advisor A's point that a survey asking adults to assign numbers to intensity words is almost certainly IRB-exempt under Category 2, and that the GT IRB office should be contacted before deciding it's too costly, is correct and I should have been more specific about this in my original review. I said "pursue Option 2 (Prolific, exemption determination)" but didn't give the same direct push that Advisor A did. The framing that this is a form submission, not a clinical trial, is the right frame to give Daniel.

**Advisor C — The no-word control is undercategorized and should already be done.** I missed this entirely. Advisor C is right that without a baseline condition ("increase innovation" with no adverb), the 0.50 hedge result is uninterpretable. You cannot distinguish between "weak words produce a hedge" and "any increase instruction produces a hedge." This is a one-day experiment at near-zero cost that directly strengthens the central claim of the existing paper. I should have flagged this. It's a genuine gap in my review.

**Advisor C — Cross-model is the wedge paper, not the valence study.** I recommended cross-model as a priority action, but Advisor C's framing of it as "the wedge" — the paper that makes everything else feel inevitable rather than optional — is sharper than my framing. The logic is correct: without cross-model replication, every subsequent paper inherits the "is this just a Haiku artifact?" objection. I agree with this sequencing argument.

**Advisor D — The paper's territory is prompt sensitivity + LLM numeric bias, not AI safety proper.** Advisor D's field cartography is the most rigorous positioning analysis in the council. The point that the paper lives at the intersection of prompt sensitivity research and LLM numeric bias research, with an *application lens* toward agentic tool-call reliability, is more precise than my framing. I said "LLM evaluation/reliability" as the primary community, which is consistent, but Advisor D's specificity about what the paper is *not* (not human-AI interaction without humans, not AI safety proper without an adversarial threat model) is a useful corrective.

**Advisor F — The abstention finding is the most novel result and deserves to be the program's center of gravity.** I mentioned the abstention finding as important but didn't elevate it sufficiently. Advisor F's point that the hedge/act/abstain mode switching has no clean precedent in the probability calibration literature — that this is the result worth protecting — is the right emphasis. My review spread attention too evenly across the three findings. The abstention result is where the genuine novelty lives.

**Advisor E — "Passive failure" as a label will confuse reviewers and should be dropped from the paper.** I didn't address the author's vocabulary choices directly. Advisor E's point that "passive failure" is not established terminology and will read as either insightful or as marketing depending on the reviewer's mood is correct. The recommendation to use "semantic-action gap" or "intent-action mistranslation" for the ML audience is practical advice I should have given.

---

### Disagreements

**Advisor A — "Run the human baseline survey first, everything else is distraction."** Advisor A's framing makes the human baseline a prerequisite for the next paper. I disagree with this sequencing. The human baseline is the right *fourth* paper, not the second. Here's the specific argument: the human baseline's contribution is comparative — "here is how the model differs from humans." That comparison is most powerful after you've established that the model finding is robust across multiple models. A human-vs-Haiku comparison is a weaker claim than a human-vs-[class of language models] comparison. If you do the human baseline first and find that humans also compress these words, you've spent $150 and 4-6 weeks to produce a finding that makes your first paper *less* interesting, not more. If you do cross-model first and find the compression pattern generalizes, then the human baseline paper lands much harder. The sequencing matters. Advisor A is right that the human baseline is scientifically necessary. They're wrong that it should come before cross-model replication.

**Advisor D — The paper should drop the AI safety framing entirely and reposition as LLM evaluation.** Advisor D's field cartography is precise, but the career strategy implication I'd draw is different. Yes, the paper's *primary* community should be LLM evaluation/reliability. But for fellowship applications, Alignment Forum posts, and the author's career trajectory toward frontier labs, the deployment safety framing is not just marketing — it's the genuine motivation and the genuine long-term contribution. Dropping it entirely would cost Daniel the community he actually wants to be in. The right move is to earn the safety framing by being precise about what kind of safety claim you're making (not adversarial, not deceptive alignment — specifically: non-adversarial, good-faith-user, language-to-action interface reliability). That's a narrower claim than "AI safety" but it's a real one.

**Advisor F — The valence/stakes paper should be deprioritized entirely.** Advisor F recommends dropping the valence study from the near-term program. I think this is too strong. The valence extension — specifically whether the model's compression pattern changes when the prompt establishes high-stakes consequences — is the extension that most directly connects to the deployment safety framing the author wants to maintain. It's also the extension that's most legible to the alignment community. I agree it shouldn't be Paper 2 (cross-model comes first), but it belongs in the program as Paper 3, not as a distant future consideration. The author's instinct here is good.

**Advisor C — The denser baseline grid is "pure Bucket A and should be deprioritized."** I agree it's low priority, but Advisor C's framing of it as "the least interesting extension" undersells one specific use case: locating the exact transition point where behavioral mode switching occurs. The 75%-to-89% gap is where the abstention behavior emerges, but we don't know where in that range the switch happens. If the abstention finding becomes the program's center of gravity (as Advisor F and I both argue it should), then knowing the precise transition point matters. This is still not a standalone paper — it should be folded into the cross-model paper as supplementary analysis — but it's not as dismissible as Advisor C suggests.

---

### Revisions to My Review

**What I missed:**

The no-word control is a genuine gap in my review. I should have flagged it explicitly. The 0.50 hedge result — which is one of the paper's most cited observations — is currently uninterpretable without knowing what the model does with a bare "increase" instruction. This is a one-day fix that strengthens the existing paper's central claim. I should have made this the first action item, not buried it in a list.

I also undersold the abstention finding relative to the compression and state-dominance findings. My review treated all three findings roughly equally. Advisors D, E, and F all independently identified the abstention/mode-switching result as the most novel contribution. They're right. My revised emphasis: the compression finding is interesting but has precedent in the vague quantifier literature. The state-dominance finding is essentially an anchoring replication in a new context. The abstention finding — that a single lexical substitution switches the model from acting to not acting near a feasibility boundary — has no clean precedent. That is where the program's identity should be anchored.

**What I would change:**

My "Highest-Return Actions" section listed five parallel actions in the first six months. That's too many. Advisor A is right that the author's natural failure mode is diffusion — keeping all options open rather than committing. My revised priority stack should be more ruthlessly ordered:

1. Run the no-word control this week. One day, near-zero cost, fixes a known interpretability gap.
2. Submit the existing paper to one workshop with an August deadline. Pick one. Don't revise indefinitely.
3. Run cross-model comparison on open-source models (Llama 3.1 8B, Mistral 7B) on the local 3070. This is free and produces the wedge paper.
4. Post on the Alignment Forum after the workshop submission is in. Not before — use the submission as the anchor for the post.

Everything else is secondary to these four actions in sequence.

**What I stand by:**

My IRB analysis holds. The exempt path through GT's HRPP is real and the cost is manageable. My recommendation to pursue Option 2 (Prolific, exemption determination) for the human baseline paper — but as Paper 4, not Paper 2 — remains my position.

My fellowship sequencing also holds. MATS is the most realistic near-term target. Anthropic Fellowship is the right long

### Skeptical PI — Revised Position

### Agreements

**Advisor B, on the derivative case for the core findings:** B makes the strongest version of the argument I was too gentle about. The compression finding and the context-dominance finding are not novel phenomena — they are replications of known effects (vague quantifier compression, anchoring bias) in a new setting. B is right that the action context is a meaningful extension, but the central findings are not as original as the paper implies. I was too kind in calling this (c) with a narrow path to (a). B's 80% confidence on the derivative case is probably right for the compression and state-dominance findings specifically.

**Advisor B, on the performed self-awareness:** B's point that "I'm aware of my failure mode" can itself be a failure mode is exactly right and I said the same thing, but B articulates it more precisely. The list of eight extension directions immediately following the self-awareness declaration is the tell. I agree completely.

**Advisor C, on the abstention finding as the most alignment-relevant result:** C correctly identifies that the hedge/act/abstain boundary behavior is the finding most legible to the agentic safety community. I said this is the most novel observation; C explains *why* it's the most strategically valuable one for the specific community the author wants to reach. This is a useful elaboration of my point.

**Advisor F, on the no-word control being an immediate fix:** F correctly flags that the no-word control condition — just "increase innovation" with no intensity modifier — should have already been run. This is a one-day experiment that directly addresses whether 0.50 is the model's interpretation of weak intensity words or its default response to any increase instruction. I mentioned this finding is uninterpretable without a baseline; F correctly escalates it to "do this this week." I agree.

**Advisor E, on the production background as a genuine differentiator:** E articulates what I called the "single biggest strength" more precisely. The asymmetry E identifies — that the author has been inside a production system at scale while most alignment researchers theorize about deployment — is the actual moat. E is right that this is being undersold.

---

### Disagreements

**Advisor B, Option 2 on IRB ("reframe the contribution so it doesn't require a human baseline"):** B argues that the paper's claims don't require a human baseline because they're claims about model behavior, not model-vs-human divergence. I disagree with the strategic implication. Yes, the paper can stand without a human baseline. But the *research program* cannot mature without one. B is solving for the current paper; I'm solving for the program. The author's central interpretive question — is this model failure or reflection of genuine linguistic ambiguity — cannot be answered without human data. Routing around it permanently doesn't solve the problem; it defers it until a reviewer at a better venue forces the issue. The IRB path is genuinely not as hard as the author believes, and Advisor B's Option 2 gives the author permission to avoid the most important experiment indefinitely.

**Advisor F, on deprioritizing the denser grid:** F calls the denser grid "pure Bucket A and should be deprioritized" and suggests running it as supplementary material. I agree it shouldn't be a standalone paper. But F undersells its importance for the abstention finding specifically. The transition from acting to abstaining happens somewhere between 75% and 89% in the current data. Knowing where that transition occurs — and whether it's sharp or gradual — is directly relevant to the boundary behavior finding, which is the most novel result. A targeted 80%, 83%, 86% sweep costs almost nothing and would sharpen the paper's strongest claim. This isn't about finding that the transition is at 71% for its own sake; it's about characterizing the abstention phenomenon more precisely.

**Advisor A, on the "clinical safety science" analogy:** A says to use it "sparingly and only as a program-level aspiration." I'd go further: drop it from the paper entirely. The analogy is doing rhetorical work that the evidence doesn't support, and it will actively irritate reviewers who know the clinical safety literature (Reason, Rasmussen, Leveson). Those reviewers will spend their review explaining why the analogy is wrong rather than engaging with the findings. The framing cost exceeds the framing benefit. Use it in fellowship applications where the audience is less technically specialized, not in papers.

**Advisor C, on avoiding CHI:** C says "Do not target these now" regarding CHI/CSCW/FAccT. I think this is too strong. FAccT specifically has a track record of accepting empirical papers about AI system behavior in deployment contexts, and the author's production background gives the work a deployment authenticity that FAccT reviewers value. The human baseline is needed for CHI (which is heavily human-subjects oriented), but FAccT is more receptive to model-behavioral work with deployment framing. I wouldn't rule it out as a target for Paper 2 or 3.

---

### Revisions to My Review

**What I missed: The GAP paper citation gap is more serious than I indicated.** Advisor A identifies that the paper closest to the author's work — the text-safety-to-action-safety gap literature — is not cited. I mentioned the related work section needs strengthening but didn't name the specific omission. This is a desk-reject risk at any venue where reviewers work in agentic safety. The author needs to read and cite this literature before the next submission. This is more urgent than I conveyed.

**What I underweighted: The second ArXiv paper.** The author's second preprint — the AI writing detection study with 21 writers, 251 judges, and ~2,000 paired evaluations — is actually stronger methodological evidence of research capacity than the intensity words paper. It has a human baseline. It has a real experimental design. It has a statistically significant finding. I mentioned it in passing but didn't use it to update my assessment of the author's capability. The author can run a human study. They've done it before. The IRB aversion in this brief is therefore not a capability constraint — it's a preference constraint. That changes my advice: the author is not avoiding the human baseline because they can't do it. They're avoiding it because they don't want to. That's a different problem.

**What I would strengthen: The "performed self-awareness" point.** I said the brief "performs self-awareness in others." I should have been more direct about the specific mechanism. The author has already demonstrated they can run a human study (Paper 2 on AI writing detection). The claim that IRB is too costly and difficult is not credible given that evidence. The author ran a 251-person human study for Paper 2. Running a 100-person survey for the intensity words human baseline is less complex, not more. The IRB aversion here is motivated reasoning, and I should have said so plainly.

**What I stand by:** The cornerstone verdict of (b) with a narrow path to (c). Nothing in the other reviews changes this. The paper is a good niche result being over-narrativized. The path to (c) requires Paper 2 to execute on the cross-model replication and the human baseline — not just assert that they're planned.

---

### Blind Spots

**All advisors missed the model version problem.** The paper tests `claude-haiku-4-5-20251001`. This is a specific model version that will be deprecated. The findings are tied to a snapshot of a model that may not exist in six months. This is not a minor limitation — it means the paper's empirical claims have a built-in expiration date. A reviewer at a venue with a six-month review cycle could legitimately ask whether the findings still hold by the time the paper is published. The author should either (a) explicitly frame the findings as a snapshot of a specific model version with the understanding that model behavior changes across versions, or (b) run a brief replication on the current production version before submitting to any venue. No advisor mentioned this.

**All advisors underweighted the "drastically vs. dramatically" finding as the program's actual hook.** Every advisor correctly identified the abstention finding as the most novel result. But none of us focused on the specific sub-finding within it: *drastically* acts while *dramatically* abstains in identical system states. This is not just "boundary behavior is word-dependent." This is a finding that two words that most humans would treat as near-synonyms produce categorically different model behavior at a constraint boundary. That is the finding that will make people stop scrolling on the Alignment Forum. That is the finding that a journalist covering AI safety would write about. That is the finding that a program committee member would remember. The author should lead with this specific contrast in every presentation, every abstract, every fellowship application. None of us told them this clearly enough.

**All advisors missed the replication crisis risk.** The paper runs 30 trials per cell at T=0.0, which produces deterministic outputs for many cells. The statistical architecture is therefore partially illusory — the Kruskal-

---

## Methodology

This report was generated by the AI Research Council using 3 stages (Independent Review → Deliberation → Synthesis).

**Reviewer models:** claude-sonnet-4-6
**Chairman model:** claude-opus-4-8
**Total cost:** $5.33
