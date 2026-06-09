# Career Strategist — stage2

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