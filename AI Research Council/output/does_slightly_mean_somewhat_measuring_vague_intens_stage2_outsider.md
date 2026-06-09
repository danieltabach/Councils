# Outsider / Red Team — stage2

### Agreements

**Reviewer B — The inversion finding deserves abstract-level visibility.**
Reviewer B correctly identifies that the 5:1 to 14:1 inversion is arguably the most operationally important result and is currently buried. I flagged this as a logical gap (the paper doesn't fully reckon with what the inversion means for a user who can't see it happening), but Reviewer B makes the structural point more precisely: the abstract reports the overall 10:1 ratio but not the inversion. I agree this is a significant omission. The inversion is the finding that should alarm a practitioner — the interface *looks* word-driven when you're far from a constraint and *becomes* state-driven when you're near one, invisibly.

**Reviewer C — The "drastically vs. dramatically" finding is underanalyzed.**
Reviewer C flags that the model's actual text responses during abstention are data that exists but hasn't been analyzed. I made the same point in my review (under "What I Still Don't Understand" and "Logical Gaps"). Reviewer C adds the specific alternative explanation I didn't articulate: the difference might be about training data distribution (how each word appears in context) rather than the model's constraint reasoning. That's a sharper version of my concern and I agree with it.

**Reviewer D — The $250K figure is rhetorically overloaded.**
Reviewer D's point that the dollar figure will be extracted from context and read as a real-world consequence is exactly right. I flagged this as a logical gap, but Reviewer D adds the useful suggestion that the paper would be more defensible staying in the allocation space (a 0.20 allocation difference) rather than converting to synthetic dollars. That's a concrete fix I didn't offer.

**Reviewer E — The independence violation is more serious than acknowledged.**
Reviewer E makes the technical point precisely: at T=0.0, four words produce the exact same value across all 30 runs. These are not 30 independent observations; they are one observation repeated 30 times. The p-values are not merely "overstated" — they are essentially meaningless as inferential quantities. I noted the independence problem in my review but didn't articulate how severe it is at T=0.0 specifically. Reviewer E is right that the Spearman ρ should be computed over word-level medians (n=10), not over all 300 individual runs.

**Reviewer A — The Mosteller & Youtz characterization is a partial mischaracterization.**
Reviewer A flags that the paper says Mosteller & Youtz "showed high variance around ordered central tendencies" when the actual finding is more nuanced — the variation of averages across studies was modest, not high. I didn't catch this. It's a real, if minor, mischaracterization.

---

### Disagreements

**Reviewer C — "Run the human survey first, or concurrently" as the primary design critique.**
Reviewer C says the entire interpretive framework depends on knowing what humans mean by these words and that running the experiment without this is "like measuring a thermometer's accuracy without a reference temperature." I understand this argument but I think it's too strong. The paper is measuring *what the model does*, not whether the model is right or wrong relative to humans. The compression finding — 10 words collapsing to 5 outputs — is a real finding about the model's behavior regardless of what humans would do. The human baseline is needed to *interpret* whether this is a failure, but it's not needed to establish that it *happens*. The thermometer analogy implies the paper is measuring accuracy against a known standard; it's actually measuring a behavior pattern. These are different things.

**Reviewer C — Verdict (c) "closer to (a) than the author's doubt suggests."**
Reviewer C says the paper is closer to (a) — legitimate elevation — than the author's doubt suggests. I think Reviewer C is being generous here. The single-model scope, the unvalidated word scale, and the missing no-word control are not minor gaps. They are the three things that would need to be true for the paper to function as a general measurement instrument. Without them, it's a careful single-model observation. I'd put it closer to the (b)/(c) boundary than Reviewer C does.

**Reviewer B — The "moderately" observation as "ordinal anomaly" framing.**
Reviewer B recommends softening the "ordinal anomaly" language. I agree with the direction but I think the more important point is that the "anomaly" framing assumes the researcher's tier assignment is correct. Reviewer B treats this as a framing issue; I think it's a validity issue. The word "anomaly" implies deviation from a known correct ordering. The paper doesn't have a known correct ordering — it has the author's ordering. Softening the language is necessary but not sufficient; the paper needs to acknowledge that "moderately" behaving differently might mean the tier assignment is wrong, not that the model is wrong.

---

### Revisions to My Review

**What I missed: The prompt template confound.**
Reviewer E correctly identifies that the no-context prompt ("should spend [WORD] more time on innovation") and the context prompt ("I would like to [WORD] increase innovation") use different syntactic frames beyond just the presence/absence of the baseline number. I didn't catch this. It's a real confound: any difference between conditions could partially reflect the different verb constructions. I would add this to my "Logical Gaps" section.

**What I missed: The abstention operationalization conflates two things.**
Reviewer E points out that "zero tool calls" conflates constraint-aware refusal with other non-action behaviors. I mentioned wanting to see the model's actual text responses, but I didn't frame this as an operationalization problem. That's a sharper and more useful critique. I would add this to my "Logical Gaps" section.

**What I would strengthen: The convergence-near-capacity finding.**
I raised the concern that convergence near 89% might be a mathematical consequence of the constraint structure rather than a finding about language interpretation. Reviewer E's point about the "differentiation funnel" being potentially trivially expected strengthens this. I would make this concern more prominent in my review — it's not just a caveat, it's an alternative explanation for one of the paper's three main findings.

**What I stand by: The "cornerstone" assessment.**
After reading all six reviews, I stand by my verdict that this paper cannot currently bear the weight of the field-building framing. Reviewers C and D both land near (c) with different emphases, and none of the other reviewers argue for (a). The consensus is that the paper is a solid first measurement slice that requires the human baseline and cross-model comparison before its claims generalize. I think my framing of this — "the paper is not the field; it's a data point that could, with extensions, become part of the field" — is accurate and I would not soften it.

---

### Blind Spots

**No reviewer examined the role of the specific domain framing.**
All prompts concern "innovation allocation" for "Architects." The word "innovation" has strong positive valence in professional/business contexts and is likely overrepresented in training data as something to be maximized. No reviewer asked: would the same compression and abstention patterns appear if the task were "reduce risk allocation" or "decrease safety budget"? The domain framing may be doing significant work in producing the observed patterns — particularly the abstention behavior, which might reflect the model's learned disposition toward "innovation" specifically rather than a general property of constraint-near behavior. This is a threat to external validity that none of the six reviews raised.

**No reviewer examined the three-task constraint structure as a potential artifact.**
The allocation environment requires three tasks to sum to 100%. This means increasing one task necessarily decreases others. No reviewer asked whether the model's behavior — particularly the 0.50 hedge and the abstention near 89% — might reflect the model reasoning about the *other two tasks* rather than just the target task. If the model is implicitly protecting the other allocations, the observed behavior is about multi-task constraint management, not about the intensity word's numeric meaning. This is a different mechanism than what the paper claims, and it's not addressed anywhere in the six reviews.

**No reviewer asked about the model's "knowledge" of the constraint.**
The paper says the model "typically cites the constraint that allocations must sum to 100%" when abstaining. But how does the model know about this constraint? It must be in the system prompt or tool schema — which are not reported. If the constraint is explicitly stated in the system prompt, the abstention behavior is the model following an explicit rule. If it's not stated and the model infers it, that's a different finding. This distinction matters enormously for interpreting the boundary behavior section, and none of the six reviews raised it.

**No reviewer examined the implications of the finding for the *user*, not the system.**
The paper frames its findings in terms of what the model does. But the practical implication is about