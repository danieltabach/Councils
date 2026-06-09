# Alignment Guide — stage2

# Alignment Guide — Council Response

## Agreements

**Reviewer B, W1 (no-word control as structural gap):** Agreed, and I flagged this in my Missing Sections. But Reviewer B sharpens the point in a way I didn't: the hedge interpretation is used as *settled language* in the Discussion while being flagged as unconfirmed in Future Work. That's an internal inconsistency between sections, which is squarely my mandate. I noted it but didn't name it as an internal inconsistency explicitly. I should have.

**Reviewer D, "Conclusions vs. Evidence" section on the "discontinuous" claim:** Reviewer D correctly identifies that a single boundary point (89%) cannot establish discontinuity versus a steep continuous function. From an alignment perspective, this means the paper's third stated research question — "does the model switch into qualitatively different behavior?" — is answered with less evidence than the paper implies. The conclusion section states the mode-switching finding as established; the evidence only supports "consistent with mode-switching at one tested boundary." This is a promise-delivery gap I underweighted.

**Reviewer F, "differentiation funnel may be trivially expected" (Logical Gap 3):** This is the most important point I missed entirely. If the convergence near 89% follows mathematically from the constraint structure (there's simply less room to move), then the "differentiation funnel" is not a finding about language interpretation — it's a finding about arithmetic. The paper does not address this alternative explanation. From my mandate: the paper claims to deliver evidence about how the model handles vague language near boundaries, but the boundary convergence finding may be explained by the environment's design rather than by the model's linguistic behavior. This is a gap between what's promised (a finding about language-to-action translation) and what's delivered (a finding that may be partially about constraint geometry).

**Reviewer A, on the drastically/dramatically discontinuity being underanalyzed:** I flagged this as a missing section — the paper's most alignment-relevant finding gets one paragraph. Reviewer A adds that the model's text responses during abstention are data the author has but hasn't analyzed. That's a concrete missing section I should have named explicitly rather than just noting the finding is underemphasized.

**Reviewer E (myself), on the inversion finding not appearing in the abstract:** All other reviewers who touched on the 10:1 ratio noted the caveat about separate tests, but none flagged the abstract-level omission of the inversion as prominently as I did. I stand by this as the highest-priority alignment fix: the abstract implies a stable dominance relationship; the paper shows it completely reverses. That's a direct abstract-to-content misalignment.

---

## Disagreements

**Reviewer A and B, framing the no-word control as primarily a statistical/methodological gap:** Both reviewers treat this as a technical weakness. From my mandate, it's an alignment problem: the paper's Discussion uses "hedge" as a settled interpretive concept, but the paper's own Future Work section says the hedge interpretation is unconfirmed. That's not a missing experiment — it's a section of the paper (Discussion) making a claim that another section of the same paper (Future Work) explicitly says is unsupported. The fix isn't just running the control; it's aligning the Discussion's language with the paper's actual epistemic state. This distinction matters for the revision brief.

**Reviewer D, on the "compression" construct conflating two phenomena:** Reviewer D argues the paper conflates "model cannot distinguish words" with "model maps words to same output because task context doesn't require finer granularity." This is a valid technical point, but from an alignment perspective, the paper's stated contribution is specifically about whether the interface is "less expressive than it appears" — which is the operator-facing version of the same question regardless of mechanism. The paper doesn't promise to resolve the mechanism; it promises to measure the expressivity gap. On that narrower claim, the paper delivers. I'd push back on framing this as a contribution failure; it's a mechanistic gap the paper doesn't claim to close.

**Reviewer F, cornerstone verdict leaning toward (b):** Reviewer F concludes the paper leans toward "fine niche result with inflated framing." From a pure alignment perspective — does the paper do what it says it will do — the paper is actually well-aligned internally. The overreach is in the Discussion's alignment framing paragraph and in the author's vision brief, not in the paper's stated contributions. The paper's four stated contributions are all delivered. The cornerstone question is about the vision, not the paper. A paper can be well-aligned internally while being insufficient for a larger program. These are separable verdicts and I think Reviewer F conflates them.

---

## Revisions to My Review

**What I missed:**

**1. The differentiation funnel's alternative explanation (Reviewer F's Logical Gap 3).** This is a genuine alignment issue I failed to catch. The paper promises to deliver evidence about how the model handles vague language near operational boundaries. But the convergence finding at high baselines may be partially or fully explained by the constraint geometry of the environment rather than by the model's linguistic behavior. The paper does not acknowledge this alternative. This belongs in my Scope Drift Analysis: the paper frames the convergence as a finding about language interpretation when it may be a finding about the environment's design. I would add this to my Missing Sections as: "An acknowledgment that boundary convergence may reflect constraint geometry rather than linguistic behavior — the paper should distinguish these or acknowledge it cannot."

**2. The internal inconsistency between Discussion and Future Work on the hedge interpretation.** I noted this in Missing Sections as "soften hedge language," but I should have named it explicitly as an internal alignment failure: two sections of the paper make contradictory epistemic claims about the same finding. This is the clearest instance of the paper not doing what it says — the Discussion presents the hedge as an established finding while Future Work correctly treats it as a hypothesis. I would elevate this from a structural recommendation to a Stated Goals vs. Delivered Content flag.

**3. The abstention text responses as missing content.** I noted the boundary behavior finding is underanalyzed, but I didn't identify the specific missing content: the model's actual text outputs during abstention are data the paper has collected but not reported. For a paper that claims to document "word-dependent abstention," the absence of any example of what the model says when it abstains is a gap between the claim ("the model produces a text response acknowledging the request but declines to invoke the allocation tool, typically citing the constraint") and the evidence (no examples shown). "Typically" is doing work that should be done by data.

**What I stand by:**

My core finding — that the paper delivers on all four stated contributions and three research questions — stands. The alignment failures I identified (inversion finding absent from abstract, hedge language inconsistency, three-failure synthesis missing from conclusion) remain the highest-priority structural fixes. The differentiation funnel alternative explanation is an addition, not a replacement.

---

## Blind Spots

These are points absent from all six reviews that fall within my alignment mandate:

**1. The paper's title promises a comparison ("Does Slightly Mean Somewhat?") that the paper never directly makes.**

The title frames the paper as a comparison between two specific words. The paper's findings address this implicitly — both map to 0.50 — but the paper never presents a direct "slightly vs. somewhat" comparison as a named finding. The title sets up an expectation the paper satisfies only incidentally. No reviewer flagged this. The title is accurate in spirit but creates a specific expectation (a pairwise comparison) that the paper's structure doesn't deliver. A reader who comes to the paper expecting a focused slightly-vs-somewhat analysis will find a broader study. This is a minor but real abstract-to-content misalignment.

**2. The three research questions in the introduction are answered in a different order than they are asked.**

The introduction lists: (1) ordinal ranking, (2) word vs. state variance, (3) near-limit behavior. The results sections deliver: 4.1 ordinal ranking ✓, 4.2 word vs. state ✓, 4.3 boundary behavior ✓. This is fine. But the conclusion reverses the emphasis: it leads with state dominance, then compression, then boundary behavior. The introduction's framing sets up boundary behavior as the third, least-prominent question; the conclusion and the author's own framing brief treat it as the most important finding. No reviewer flagged this ordering inconsistency. It's a structural alignment issue: the paper's introduction undersells its most important finding by placing it third, and the conclusion doesn't correct this by reordering the emphasis.

**3. The "ongoing study" framing in the conclusion creates an alignment problem the paper doesn't resolve.**

The conclusion states: "This is a preprint documenting the first slice of an ongoing study." This framing implies the paper's claims are provisional pending future slices. But the abstract and introduction make no such qualification — they present the findings as complete contributions. A reader who