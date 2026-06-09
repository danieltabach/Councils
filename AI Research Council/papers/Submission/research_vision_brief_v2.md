# Research Vision + Foundation Brief — For Council Deliberation (v2)

**Author:** Danny Tabach
**Companion artifact:** "Does Slightly Mean Somewhat? Measuring Vague Intensity Words in LLM Numeric Actions" (arXiv, May 2026). Paper one. The published study summarized in §3 below.
**Status:** Vision-stage, now anchored to a real result.
**Two-part ask of the Council:**
1. **Vet the bet.** Is the field I'm describing (§1–2) real and unclaimed, or a rebrand of existing work?
2. **Stress the cornerstone.** Can paper one (§3) actually serve as the founding instrument of that field (§4–5), or am I retrofitting a grand narrative onto a solid-but-modest first study? If it can bear the weight, how do I sequence and align myself to build on it? (§6)

I want adversarial deliberation, not synthesis. Assign at least one agent to argue the field is derivative and one to argue the paper cannot carry it. Their job is to break this here.

---

## 1. The one-sentence bet

AI safety is currently a **lab-internal** science: measure the model in isolation — weights, neurons, benchmark behavior, scheming under contrived pressure. I'm betting safety must *also* become a **deployment-external** science: the empirical, measured study of what happens at the interface where an AI system meets a human meets a real decision with real stakes.

Not "is the model safe in a vial." But: "what does the human+AI+system *unit* do when wired into something that matters, and where does that unit *silently* fail?"

---

## 2. The shape of the field

**Best analogy — clinical safety science.** Pharmacology asks if a compound works in the lab (current alignment research). But a drug safe in a vial still kills through interaction effects, dosing errors, doctor-patient miscommunication, bad handoffs. So medicine built an empirical discipline on top of the chemistry — adverse-event reporting, human-factors trials, surgical checklists, M&M conferences. That discipline is a *measurement science*, not an ethics seminar, and it generates the evidence base regulation stands on. It didn't exist until people started dying in hospitals and someone decided to measure it. **I want to build the equivalent for AI deployment.**

**Supporting analogies.** The *ruler* (we have inches because shared measurement enables coordination; human↔AI interaction has no agreed units yet). The *road line* (an interface convention — not a property of the car, not a law in a book — empirically refined to let two systems share dangerous space).

**What it is NOT:** not interpretability (don't care about the neurons here); not benchmark alignment (not scoring a held-out set); not "AI ethics/policy" (that sits above and usually has no data underneath — I want to *produce the substrate* policy later codifies); not robotics (could be a subfield, isn't the thing).

**The core scientific bet:** failure modes *rhyme across domains.* A doctor over-trusting a diagnostic suggestion and a branch manager over-trusting an ATLAS output are the same measurable phenomenon in different clothes. If true → I can build rulers. If false → I have anecdotes. **Proving the rhyme is the contribution.**

**The distinction I keep losing and need held:** *active vs. passive failure.* The field mostly studies AI failing actively — scheming, blackmail, refusal (e.g. Lynch et al. 2025, agentic misalignment: the model's villainy under pressure). I want to study AI failing *passively* — a confident, plausible, wrong-for-the-human output produced because intent got silently mistranslated in the loop, and nobody registers anything went wrong. Passive failure is more dangerous because it doesn't trip alarms; it looks like the system working.

---

## 3. What paper one actually establishes (the empirical substrate)

A controlled environment: human-language instruction → Claude Haiku → numeric tool call → deterministic backend → measurable outcome. The model is the only stochastic component; the backend is a measuring instrument, not the object of study. 6,620 runs across T=0.0 and T=0.7. Findings:

- **Compression / expressivity gap.** 10 intensity words collapse to ~5 distinct outputs. Four lower-tier words (*slightly, marginally, somewhat, mildly*) all map to a 0.50 median with zero variance; *drastically/dramatically* lock to 0.70. Spearman ρ ≈ 0.845 — coarse ordinality preserved, fine distinctions destroyed. The interface accepts more linguistic distinction than the model expresses.
- **The 0.50 hedge.** Weak words default to the midpoint rather than a small positive move. Open mechanism: training-data frequency, RLHF rewarding noncommittal responses, or 0.50 as maximally noncommittal under magnitude-uncertainty.
- **Ordinal anomalies.** *moderately* maps *below* *slightly* (restraint heuristic — "keep it moderate" — not magnitude). Within-tier instability (*considerably* > *substantially*).
- **State dominates word.** With context supplied, baseline allocation explains ~10× more rank variance than word choice (ε² 0.782 vs 0.079). But the 10:1 masks an **inversion**: at low baselines (b≤25%) the *word* drives output (~5:1 word-over-context); at mid-high baselines the *context* drives it (~14:1 context-over-word). Same word, opposite regime.
- **Differentiation funnel.** Weak–strong gap ≈0.40 at low baseline → 0.00 at 75% (all words converge to 0.80). Ordinal faithfulness ρ>0.91 at low baseline → ~0 near capacity. The model only honors word ordering when it has headroom.
- **Boundary modes — hedge / act / abstain.** At 89% baseline, 121/300 runs abstain entirely, and it's sharply word-dependent: weak words always act (small adjustments); *considerably/substantially/significantly* abstain 100%; *dramatically* 29/30; *drastically* abstains only 2/30 and pushes to the ceiling (0.912) — it reads as "as much as possible." A one-word swap (*drastically*→*dramatically*) flips the system from acting to refusing in the same state.
- **Downstream consequence.** Word choice alone moves the objective ~$250K (−$424K for *moderately* to −$675K for *drastically/dramatically*) in the synthetic environment. Vague language controlling a tool propagates into materially different outcomes.
- **Temperature-robust.** T=0.7 broadens dispersion (cells with >1 value: 24%→69%) but preserves every structural pattern (ρ 0.834 vs 0.845; ε² ratio ~10:1). Stochasticity does not restore a clean scale.
- **Preliminary anchoring signal (visual only).** Round baselines → round outputs; irregular baselines → irregular outputs (deltas like 0.164, 0.136, 0.094). Flagged in the paper as needing a denser grid for a formal test.

The paper's own alignment framing is deliberately *narrow*: not "does the model share human values," but "does a model-mediated action interface preserve the operator's intended semantics." Answer: mixed — coarse regimes captured, fine distinctions compressed, heavy state-anchoring, discontinuity at boundaries.

---

## 4. The directions this opens — paper one as a generator

Two buckets. **Bucket A** = extensions the paper already names (low-risk, credibility-building, closes its own gaps). **Bucket B** = the field-defining moves that the vision adds (higher-risk, higher-ceiling). The strategic question is the *mix and order*, not either/or.

**Bucket A — already in the paper's future work:**
- *Human baseline survey* (IRB in prep at Georgia Tech). Closes ordinality-validation AND human-comparison in one instrument. If humans also compress, the effect reflects English, not a model flaw — which itself becomes a finding about where the human's assumption diverges from reality.
- *Cross-model* (GPT-4o, Gemini Flash, etc.). Is compression/state-dominance/three-mode policy universal or Claude-specific? Divergence = a finding about how training shapes vague-language interpretation.
- *Denser baseline grid + T=1.0* (collected). Locates exact transition points; enables a formal test of the anchoring signal.
- *Decrease instructions* (asymmetry near the 0% floor).
- *Partial-context (Tier 3)* — does state-dependence come from prompt grounding or the model reading system state itself? Clean mechanistic isolation.
- *No-word control* — distinguishes "0.50 = hedge" from "0.50 = default to any increase request." Sharpens the central claim at minimal cost.

**Bucket B — the field-defining additions (our ideas):**
- *Valence framing (paper two candidate).* Inject the **identical** intensity word into an allocation task, but vary only the consequence framing in a 2×2: valence (gain/loss) × stakes domain (human/economic). Grounded in prospect theory and the reflection effect (Kahneman & Tversky 1979; Tversky & Kahneman 1981 — the "200 saved vs 400 die" framing flip; humans turn risk-seeking under loss, risk-averse under gain). The open question: does the model inherit this framing asymmetry, and does it leak into continuous numeric allocation through the vague word? **The headline finding is the *direction*** — if the model does NOT get risk-seeking under loss framing the way the human on the other end assumes it will, that gap *is* the silent interface failure the whole field is about. Note: existing work (e.g. CogBias 2026) maps K&T biases onto LLM *choice* tasks; the unclaimed slot is framing-effect-via-intensity-word into *continuous allocation*.
- *Stakes magnitude axis.* Hold the allocation skeleton identical, move only the stakes label across domains (ad budget → branch staffing → triage). Tests whether the model is *stake-insensitive* — exactly as cavalier allocating ICU beds as ad budget. Lab benchmarks can't surface this; it only appears at the language-meets-stakes interface.
- *The anchoring finding, promoted but controlled.* The round/irregular-number effect is its own paper (numeric-format contamination at the interface). In paper two it must be *controlled* (one fixed baseline grid across all cells) so it doesn't confound valence — and forward-referenced. Earns its keep without expanding scope.
- *Cross-domain transfer (the keystone).* The move that turns a pile of studies into a *field*: take ONE instrument and show it produces comparable, calibratable numbers across genuinely different domains. This is where "the rhyme" is proven or falsified.

---

## 5. The cornerstone question, stated honestly

There is a real tension the Council must adjudicate, and I don't want it smoothed over:

**The paper is epistemically humble. The vision is expansive.** Paper one is careful, narrow, hedged — "one model, one domain, one direction, descriptive claim, not a human baseline, should not be framed as model failure." The field vision wants to call it the founding instrument of a new applied safety science. Those two postures are in tension. Possible verdicts:

- **(a) Legitimate elevation.** The paper genuinely is a domain-general measurement instrument; its narrowness is *appropriate scope discipline*, not smallness, and the field is the honest extrapolation. Build on it directly.
- **(b) Retrofit / grandiosity.** The paper is a fine niche linguistics-meets-LLM result, and draping a "new field" over it is exactly my known failure mode — narrative inflation that a reviewer or a serious researcher would see through. Keep the paper modest; build the field claim only after 3–4 transferable instruments exist.
- **(c) Something between** — the instrument generalizes but the "new field" branding is premature; pursue the program, mute the manifesto.

I genuinely don't know which is true. I lean (a) on good nights and fear (b) on honest ones. **Tell me which, and why.**

---

## 6. How I'm asking to be aligned (the questions that matter most)

1. **Is the field real and unclaimed?** Where exactly does it overlap human-factors / HCI / responsible-AI / sociotechnical-systems work, and what is the *specific* slice that is genuinely open? If there's no open slice, say so plainly.

2. **Cornerstone verdict:** (a), (b), or (c) from §5 — and the reasoning.

3. **The wedge.** Of everything in §4, what is the *single* highest-leverage next instrument — the one whose existence most makes the rest inevitable? My current lean is the valence 2×2 as paper two. Argue me off it or onto it.

4. **A-vs-B mix.** How much Bucket-A credibility-building (human baseline, cross-model) do I need *before* a Bucket-B field-defining move lands without getting dismissed? What's the right sequence over the next 3 papers?

5. **The vision's failure mode** (not the experiment's). What's the most likely way this becomes five years of effort that produces nothing a lab, company, or regulator can use?

6. **Audience.** Workshops (NeurIPS/EMNLP/ACL)? Lab safety teams? Eventual standards bodies? The choice redefines "rigor" and "impact"; I need to pick, not drift.

7. **Alignment to my actual position.** I'm a working data scientist (not a lab researcher), self-funding on Haiku-scale budgets, finishing a master's, prepping a fellowship. Given *that* reality, what is the honest highest-return path to becoming a recognized voice in this area — and what am I structurally unable to do alone that I should stop pretending I can?

8. **What am I not seeing?** I built this from inside one optimization system and one conviction that it matters. Name the obvious blind spot.

---

## 7. The trap — license to call it on me

My known failure: I get intoxicated by the size of the vision and try to make one paper *be* the field, cramming every finding (compression, anchoring, context-inversion, boundary modes, valence) into a single swing. That turns a study into a manifesto with no data — the exact "ethics/policy" thing I said I don't want to be. The backlog is a *sequencing* asset I keep misreading as a *fitting* problem.

**If you catch me doing this mid-deliberation — expanding scope because expansion feels like progress — stop me and say so.** A good outcome from this council *narrows* me. If eight agents enthusiastically help me add directions, they've fallen into the same vein I did.

---

## 8. The conviction, plainly

One day this tech will run through hospitals, finance, courts, logistics, daily decisions — and it will need rulers, lane lines, and a settled empirical practice for how humans and AI share consequential space. We have almost none of that, because everything moves too fast to settle. The study of real human↔AI interactions — what works, what silently fails, how to standardize the difference — is a field waiting to be named. Paper one is either its first brick or a good standalone result I'm over-reading. I'd rather find out which from you than in year three.

If I'm wrong about the size of it, I'm still not wrong that the measurements don't exist yet and someone should take them.

---

*Prepared for adversarial Council deliberation. Break the bet and the cornerstone here. Narrow me.*
