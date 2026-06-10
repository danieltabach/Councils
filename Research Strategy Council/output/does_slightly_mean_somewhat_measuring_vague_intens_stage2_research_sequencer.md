# Research Sequencer — stage2

## Agreements

**Advisor A — "Finding 3 is your genuinely interesting finding"**
Completely agree. Advisor A is the most direct about this and I should have been equally blunt in my original review. The compression finding is expected; the three-mode boundary behavior is not. I said this but buried it. Advisor A made it the lead. That's the right call.

**Advisor B — "The action/estimation distinction is the moat"**
Agree strongly. The distinction between measuring probability *estimation* (what prior work does) and measuring constrained *action execution* (what this paper does) is the core novelty claim. Advisor B articulates this more precisely than I did. Daniel should be able to state this distinction in one sentence in every abstract and introduction he writes going forward.

**Advisor C — "The feasibility-regime inversion is underplayed"**
Agree. Advisor C correctly identifies that the split-range analysis result — word dominates at low baselines, context dominates at high baselines — is a *regime change* in the model's action policy, not just "context matters." I mentioned this but didn't name it forcefully enough. That framing is stronger and more publishable.

**Advisor D — "Do not lead with AI Safety and Alignment"**
Agree completely. "Agentic tool-use reliability" or "language-to-action fidelity" is more precise, more timely, and less likely to invite the wrong reviewers. I said something similar but Advisor D's specific framing is better.

**Advisor F — "The co-authorship problem is your biggest structural gap"**
Agree, and I underweighted this. Solo ArXiv papers don't move the needle at frontier labs the way one co-authored paper with a known researcher does. This is a career constraint, not just a research quality issue.

---

## Disagreements

**Advisor A — "Don't pursue mechanistic interpretability"**
I agree mech interp is a distraction *right now*, but Advisor A's dismissal is too categorical. The specific argument — "their token embeddings are close in representation space, boring result" — is actually not guaranteed. The *boundary switching* behavior (why does *drastically* push to ceiling while *dramatically* abstains?) is not obviously explained by embedding proximity. If Daniel develops the behavioral map first across multiple models and finds consistent boundary switching, *then* a targeted mech interp question about that specific discontinuity becomes tractable and interesting. The sequencing matters. Mech interp is wrong for Paper 2; it might be right for Paper 4.

**Advisor B — "EMNLP 2026 is your best venue"**
I think this overstates the fit. EMNLP is primarily an NLP venue and the linguistics framing of this work is its weakest dimension. The paper's strength is the *agentic systems* framing, not the linguistics framing. Venues like NeurIPS workshops on agents/safety or FAccT are better fits than EMNLP main. EMNLP workshops are fine but I wouldn't call it the best venue.

**Advisor D — "OpenAI Safety Fellowship running September 2026 through February 2027"**
I can't verify this specific fellowship exists as described, and presenting unverified fellowship details as concrete advice is risky. Daniel should verify independently before planning around it. The broader point — that fellowships exist beyond Anthropic — is correct and useful.

**Advisor F — "The valence/stakes study is Paper 3"**
I agree with the sequencing but want to push back on one thing: Advisor F frames the valence study as primarily about whether models behave differently under high-stakes framing. The more interesting version of that question, which nobody has fully articulated, is whether the *three-mode boundary behavior* (hedge/act/abstain) is amplified or suppressed under high-stakes framing. That's a tighter, more testable hypothesis than "does the model behave differently?" and it directly extends the most novel finding from Paper 1.

---

## Revisions to My Review

**What I missed: The no-word control is more important than I signaled.**

Multiple advisors flagged this but I listed it as a secondary addition. It's actually a prerequisite for the central interpretive claim. If "increase innovation" with no intensity word also produces 0.50, then the entire "hedge" interpretation collapses — 0.50 is just the model's default for any increase instruction, and the compression finding loses its meaning. This is a $2-3 API cost experiment that should be run *before* the cross-model study, not alongside it. I would revise my sequencing: run the no-word control first (one weekend), confirm the hedge interpretation holds, then proceed to cross-model replication.

**What I underweighted: The production systems angle as a differentiator.**

Advisor F makes this point and I made it briefly, but I should have been more aggressive about it. Daniel's JPMC background is not just backstory — it is construct validity that most academic researchers cannot claim. The reason the allocation environment is a credible measurement instrument is that Daniel has actually built one at scale. That should be in the abstract, not buried in the introduction. "We study this problem using a synthetic environment modeled on production-scale constrained optimization systems" is a stronger opening than the current framing.

**What I should revise on IRB:** My Path 3 recommendation (reframe to avoid human comparison) was correct but I didn't give enough weight to Advisor B's specific suggestion about Vogel et al. (2022) and Cliff (1959) as existing human data sources. Using published psycholinguistic distributions as a reference baseline is methodologically cleaner than I implied — it's not a workaround, it's a legitimate scientific move. I'd revise my recommendation to: use Cliff (1959) and Mosteller & Youtz (1990) for the ordinal validation claim in the current paper, and treat the direct human comparison as a clean follow-up study rather than a gap.

---

## Blind Spots

**All advisors missed: The decrease direction is not just a robustness check — it's a different paper.**

Every advisor who mentions decrease instructions treats it as a minor extension ("add it at minimal cost"). But asymmetric boundary behavior between increase and decrease directions would be a *substantive finding* about how LLMs handle directional constraints. Near the lower boundary (0-10% allocation), does *drastically decrease* push to the floor the way *drastically increase* pushes to the ceiling? Or does it abstain? Does the hedge/act/abstain structure mirror or invert? If the behavior is asymmetric, that tells you something about how the model represents feasibility constraints directionally — which has direct implications for any agentic system with both upper and lower bounds. This deserves its own experimental design, not a footnote.

**All advisors missed: The Algoverse fellowship is underutilized as a peer review mechanism.**

Every advisor treats Algoverse as a resource for compute and connections. Nobody suggests using it as a pre-submission review venue. Daniel should be presenting his cross-model results to the Algoverse cohort before submission — not for validation, but to stress-test the framing and find the holes reviewers will find. The mech interp suggestion came from Algoverse colleagues; that means there are people in that cohort who think carefully about these systems. Use them as adversarial reviewers, not just supporters.

**All advisors missed: The round-number anchoring finding needs a formal test, not just a mention.**

Every advisor treats the round-number anchoring observation as a preliminary note. But this finding — that the model's output format mirrors the input format (round baselines produce round outputs, irregular baselines produce irregular outputs) — connects to a specific and testable claim about how LLMs process numeric tokens. A denser baseline grid (every 5%, which is achievable on open-source models at zero cost) would let Daniel run a formal test: do outputs cluster at round values significantly more often when baselines are round? If yes, that's a publishable finding about numeric representation in LLMs that is orthogonal to the intensity word question and could anchor a separate short paper.

**All advisors missed: The submission timing for NeurIPS 2026 workshops requires knowing which workshops exist.**

Every advisor says "target NeurIPS 2026 workshops" but NeurIPS 2026 workshop proposals are typically submitted and accepted in spring, with the final workshop list announced in summer. Daniel cannot submit to a workshop that hasn't been announced yet. The practical advice is: (1) check the NeurIPS 2026 workshop list when announced (typically June-July), (2) have a submission-ready paper by then, (3) identify 2-3 target workshops from the announced list. The backup plan if no suitable workshop exists is EMNLP 2026 workshops (October) or ICLR 2027 workshops. Daniel needs a contingency plan,