# Skeptical PI — stage2

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