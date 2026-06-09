# Methodologist — stage2

# Methodologist's Response to Council Reviews

---

## Agreements

**Reviewer A — The two-way analysis gap**
Reviewer A correctly identifies that the correct analysis for the word × baseline interaction is a two-way model, not two separate Kruskal-Wallis tests. I raised this in my original review, but Reviewer A articulates the specific consequence more precisely: without a joint model, you cannot distinguish whether baseline captures more variance because it genuinely dominates, or because the two factors are correlated and baseline absorbs shared variance. This is the right framing and I endorse it fully.

**Reviewer A — The ε² = 0.969 inflation problem**
Reviewer A goes further than I did on this point, correctly noting that when within-group variance is exactly zero for four of ten words at T=0.0, the statistic approaches 1.0 trivially and "reporting ε² = 0.969 as a meaningful statistic is misleading." I flagged inflation but understated how severe it is. Reviewer A's recommendation to either drop the number or replace it with the count of distinct medians (already reported as 5) is the right fix.

**Reviewer C — The no-word control is not a nice-to-have**
Reviewer C frames this more forcefully than I did: "it is the falsification condition for the paper's most prominent interpretive claim." I agree. My original review called it a "structural gap"; Reviewer C's language better captures the epistemic severity. The hedge interpretation is not merely unconfirmed — it is unfalsified within the paper.

**Reviewer C — The split-range analysis ratios are post-hoc descriptive, not confirmatory**
Reviewer C and I agree on this. The 5:1 and 14:1 figures are derived from a researcher-chosen split point and should not be treated as established quantities. The paper's disclosure is honest but the framing occasionally treats these as independent evidence.

**Reviewer E — The convergence near capacity may be mathematically trivial**
Reviewer E raises a point I did not: "when a system is near its maximum capacity, any instruction to increase it will produce a small increase regardless of the word used — because there's no room to increase more." This is a genuine alternative explanation for the differentiation funnel that the paper does not address. The convergence finding may be a mathematical consequence of the constraint structure rather than a finding about language interpretation. I should have caught this.

**Reviewer F — The inversion finding is undersurfaced**
Reviewer F identifies that the 5:1 → 14:1 inversion is the paper's most operationally important result and it is absent from the abstract. I agree. The abstract reports the overall 10:1 ratio, which is an average that masks the directional reversal. The inversion is the finding that most directly supports the "passive failure" framing: the interface appears word-driven at low baselines and becomes state-driven at high baselines, invisibly to the operator.

**Reviewer B — Mosteller & Youtz mischaracterization**
Reviewer B flags that the paper describes Mosteller & Youtz as showing "high variance around ordered central tendencies" when the actual finding is closer to the opposite: cross-study averages were relatively stable, with high individual-level variance. This is a real mischaracterization that I missed entirely. It is minor in terms of the paper's argument but is a citation accuracy issue.

---

## Disagreements

**Reviewer A — "The paper should either not report this number or replace it with a more appropriate measure"**
Reviewer A recommends dropping ε² = 0.969 or replacing it. I partially disagree. The number should stay with a stronger caveat, not be dropped. Removing it would obscure the methodological lesson: deterministic decoding produces trivially inflated effect sizes, which is itself a finding about how to design and interpret these experiments. The paper's current disclosure is too brief; it should be expanded into a methodological note, not resolved by deletion.

**Reviewer C — "Weak Accept for workshop; Borderline for full conference main track"**
This is a venue recommendation rather than a methodological judgment, which is outside my mandate. I note only that the methodological gaps I identified — missing no-word control, unvalidated word scale, independence violation in ρ computation, incomplete prompt specification — are the factors that should drive venue decisions, and those gaps are real regardless of where the paper is submitted.

**Reviewer E — "The differentiation funnel is an evocative name for a phenomenon that might be trivially expected"**
Reviewer E argues the convergence near capacity "might follow directly from the constraint structure." I agree this is a valid alternative explanation, but I would not characterize it as "trivially expected." The non-trivial finding is not that all words converge near capacity — that is indeed mathematically expected — but that the convergence happens at 75% rather than, say, 95%, and that the transition is sharp rather than gradual. The paper does not characterize the transition point or its sharpness, which is the actual gap. The finding is not trivial; it is underspecified.

**Reviewer A — "Run the human survey first, or concurrently"**
Reviewer A recommends the human survey should have been the first instrument. I understand the argument but disagree methodologically. The controlled measurement instrument (the LLM harness) is the contribution; the human survey is the validation. Running the survey first would have required pre-specifying the word scale and task framing without knowing whether the harness would produce interesting variation. The sequencing is defensible. The problem is not the order but the absence of the survey from this paper, which leaves the ordinal claims unanchored.

---

## Revisions to My Review

**Addition: The convergence-as-mathematical-artifact problem (from Reviewer E)**
I should have raised the alternative explanation that convergence near capacity is a mathematical consequence of the constraint, not a behavioral finding. The paper needs to address this directly. The relevant test would be: does convergence happen at the mathematically expected point (near 100%), or does it happen earlier? The data shows convergence at 75%, which is not the mathematical ceiling — this is the finding. But the paper does not frame it this way, and without this framing, the convergence result is vulnerable to the "trivially expected" critique.

**Strengthening: The Spearman ρ effective sample size problem**
I raised the independence violation but did not fully specify the consequence. At T=0.0, where four words produce identical outputs across all 30 runs, the effective sample size for the no-context ρ is not 300 — it is closer to 10 (one observation per word). The correct computation is ρ over the 10 word-level medians with n=10, not ρ over 300 individual runs. The p-value at n=300 with clustered data is not merely overstated; it is the wrong quantity. The paper should report ρ over medians with the correct uncertainty, or use a permutation test that respects the clustering. I stated this in my original review but should have been more explicit that this affects the primary ordinal faithfulness claim, not just the significance level.

**Addition: The prompt template confound is more serious than I acknowledged**
I flagged the syntactic frame difference between no-context ("should spend [WORD] more time") and context ("I would like to [WORD] increase") as a confound. Reviewing the figures more carefully, I note that the no-context condition produces 0.50 for four weak words while the context condition at b=0% produces approximately 0.10 for the same words (visible in Figure 4). This is a large difference that could reflect the syntactic frame difference as much as the presence of context. The paper attributes this difference to the presence of context, but the prompt structure changed simultaneously. This is a more serious internal validity threat than I originally stated, and it is not acknowledged in the Limitations section.

**Addition: The abstention operationalization conflates two phenomena — and the 89% baseline is the only boundary tested**
I raised both of these in my original review, but I want to strengthen the second point. The paper claims the model "switches into qualitatively different behavior" near feasibility limits. But "near feasibility limits" is operationalized with a single data point: 89%. The paper cannot establish that this is a boundary effect rather than a high-baseline effect without testing intermediate points (85%, 87%, 91%, 93%). The transition point and its sharpness are the empirically interesting quantities, and they are entirely uncharacterized. This is a significant gap in the boundary behavior section that no other reviewer emphasized sufficiently.

**Retraction: I overstated the severity of the two-ε² comparison problem**
In my original review, I said the ratio comparison "cannot distinguish" between three possible explanations. On reflection, the directional finding (baseline explains more than word) is robust to the methodological limitation, even if the specific ratio is not a standard statistical quantity. The paper