# Peer Reviewer — stage2

### Agreements

**Reviewer A — Statistical structure of the ε² comparison (W1 equivalent):**
Reviewer A's point that the correct analysis is a two-way Kruskal-Wallis or mixed-effects model with word and baseline as factors is exactly right, and I understated this in my own review. I flagged the two-test independence issue (W3 in my review) but framed it as "moderate" rather than "structural." Reviewer A is correct that this is the paper's central quantitative claim and the framing has a structural problem that the current caveats don't fully resolve. I should have been more forceful here.

**Reviewer B — Prompt confound between no-context and context conditions:**
Reviewer B's W5 observation that the two prompt templates use different syntactic frames ("should spend [WORD] more time" vs. "I would like to [WORD] increase") is a confound I missed entirely. This is a legitimate internal validity threat: any difference between conditions could partially reflect the different verb constructions, not just the presence of context. I should have caught this.

**Reviewer C — The "differentiation funnel" may be trivially expected:**
Reviewer C's Gap 3 is sharp: when a system is near maximum capacity, any increase instruction will produce a small increase regardless of word, because there is no room to increase more. The convergence near 89% may be a mathematical consequence of the constraint structure rather than a finding about language interpretation. I noted the convergence finding as a strength (Strength 4) without adequately interrogating whether it is surprising given the task design. Reviewer C is right to push on this.

**Reviewer E — The inversion finding is underemphasized:**
Reviewer F (the alignment guide reviewer) makes this point most forcefully, but Reviewer E's source audit implicitly supports it. The complete inversion of explanatory power (5:1 word-dominant at low baselines → 14:1 state-dominant at high baselines) is arguably the most operationally important finding in the paper and is absent from the abstract. I noted the differentiation funnel as a strength but did not flag the inversion's absence from the abstract as a weakness. This is a gap in my review.

**Reviewer D (my own) — No-word control as structural gap:**
Reviewers A, B, C, and F all independently converge on this point. My W1 was correct and appropriately prioritized. The convergence across reviewers strengthens my confidence that this is the paper's most important fixable gap.

**Reviewer F — "Hedge" language should be softened in Discussion:**
My W1 noted the hedge interpretation is unfalsified, but Reviewer F makes the sharper point that the Discussion uses "hedge" as settled language while Future Work correctly flags it as unconfirmed. This is an internal inconsistency I identified but didn't frame as precisely. Reviewer F's framing is better: the fix is a single word change ("appears to function as a hedge"), not a new experiment.

---

### Disagreements

**Reviewer A — Cornerstone verdict closer to (b) than (a):**
Reviewer A concludes the paper is "closer to (b) than the author's framing suggests." I think this is too harsh. The boundary behavior finding (hedge/act/abstain) and the differentiation funnel inversion are genuinely novel empirical contributions that go beyond what the existing calibration or pragmatics literature has documented in the action case. The paper is (c), but I would place it closer to (a) than Reviewer A does — specifically because the measurement instrument is clean and replicable, which is the foundational requirement for a cornerstone. A cornerstone doesn't need to be complete; it needs to be reproducible and extensible. This one is.

**Reviewer C — The alignment framing is "retrofitted":**
Reviewer C argues the alignment framing "reads like it was added to elevate the paper's significance." I disagree. The finding that a one-word swap between near-synonyms (*drastically* vs. *dramatically*) produces categorically different action policies at the most constrained boundary is a genuine alignment-relevant result, not a rhetorical move. The framing may be underdeveloped, but it is not manufactured. The issue is that the paper needs the human baseline to distinguish "model failure" from "accurate modeling of human ambiguity" — but the alignment framing is not wrong, it is premature. That's a different critique.

**Reviewer B — Abstention operationalization conflates two things:**
Reviewer B argues that zero tool calls conflates constraint-aware refusal with other non-action behaviors. This is technically correct, but the paper reports that abstaining runs "typically cite the constraint that allocations must sum to 100%." The word "typically" is imprecise, but if the author has the text responses, this is a characterization issue, not a fundamental operationalization failure. I would frame this as a documentation gap (show the text responses) rather than a construct validity problem. Reviewer B overstates the severity here.

**Reviewer E — Mosteller & Youtz "high variance" mischaracterization:**
Reviewer E flags that the paper says Mosteller & Youtz "showed high variance around ordered central tendencies" when the actual finding is that cross-study averages were relatively stable. This is a real discrepancy, but it is minor in context: the paper uses Mosteller & Youtz to motivate the general point that numeric interpretation of vague language varies, which is consistent with the source even if the specific characterization is imprecise. Reviewer E is correct to flag it, but it does not affect any finding in the paper.

---

### Revisions to My Review

**What I missed and would add:**

1. **The prompt confound (Reviewer B's W5).** I should have flagged that the no-context and context prompts use different syntactic frames. This belongs in my Weaknesses section as a moderate weakness. It doesn't invalidate the conditions comparison, but it should be acknowledged as a limitation.

2. **The trivial-convergence alternative explanation (Reviewer C's Gap 3).** I should have noted that convergence near capacity may follow from the constraint structure rather than from anything interesting about language interpretation. This is a competing explanation for the differentiation funnel that the paper does not address. I would add this to my Questions for Authors.

3. **The inversion finding's absence from the abstract.** I noted the differentiation funnel as a strength but did not flag the abstract's failure to surface the inversion. Reviewer F is right that this is the most operationally important result and its absence from the abstract is a gap between what the paper delivers and what the abstract promises. I would add this to my Minor Issues or elevate it to a Moderate Weakness.

4. **The Spearman ρ computation over n=300 vs. n=10.** I raised this in Question 5, but Reviewer B makes the stronger point that at T=0.0 with near-zero within-word variance, the effective sample size for the no-context ρ is closer to 10 than 300. I should have flagged this more forcefully in my Weaknesses rather than only in Questions.

5. **Missing citations: scalar implicature / RSA literature.** Reviewer A's point about the Rational Speech Acts framework is one I should have raised. The *moderately* anomaly is a textbook scalar implicature problem, and the paper's failure to engage with Frank & Goodman (2012) or the computational pragmatics literature is a genuine related-work gap. I would add this to my Weaknesses.

**What I stand by:**

- The boundary behavior finding (hedge/act/abstain) as the paper's most distinctive contribution. No reviewer disputes this.
- The no-word control as the single most important missing condition. All reviewers converge.
- The Weak Accept recommendation for workshop/findings track, Borderline for main conference. The consensus across reviewers supports this positioning.
- The cornerstone verdict as (c), leaning toward (a) with extensions. I maintain my disagreement with Reviewer A's more pessimistic placement.

**Revised recommendation language:** I would add to my recommendation: "The abstract should be revised to surface the word-dominance inversion finding (5:1 → 14:1 flip across baselines), which is the paper's most operationally significant result and is currently absent from the abstract. The Discussion should soften 'functions as a hedge' to 'appears to function as a hedge' to match the epistemic status acknowledged in Future Work. The prompt confound between conditions should be acknowledged as a limitation."

---

### Blind Spots

Points that no reviewer (including myself) adequately addressed:

**1. The three-failure-compound problem near operational boundaries.**
Every reviewer noted the individual findings (compression, state dominance, boundary mode-switching) but no reviewer explicitly stated that these three failures are simultaneously worst at the same point in the allocation space — near capacity, where the system is most const