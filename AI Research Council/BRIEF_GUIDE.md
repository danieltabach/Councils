# How to Write an Effective Review Brief

Your **brief** is the single most important input to the council besides your paper.
It tells all 6 reviewers what you need, so they calibrate their depth, focus, and
tone to your actual situation — instead of giving you a generic review you can't act on.

## The Golden Rule

**Every dollar you spend on a council run is only as good as your brief.**
A vague brief ("review my paper") gets vague output. A specific brief gets
specific, actionable feedback you can take directly into a revision session.

---

## Recommended Structure

You don't need to fill every field. Use what's relevant. But the more context
you give, the sharper the output.

```
REVIEW TYPE: [What kind of review do you need?]
TARGET: [Where is this going? ArXiv preprint, NeurIPS, ICML, journal, internal report?]
STAGE: [Early draft, pre-submission, post-rejection revision, camera-ready?]
GOALS: [What are you trying to achieve with this paper?]
CONCERNS: [What specifically worries you? What do you want extra attention on?]
CONTEXT: [Any background the reviewers should know that isn't in the paper?]
```

### Example Briefs

**Quick ArXiv readiness check:**
```
REVIEW TYPE: Preprint readiness check
TARGET: ArXiv preprint, no formal peer review
STAGE: Near-final draft
GOALS: Get this out quickly as a position piece to establish priority
CONCERNS: Are there any embarrassing errors or unsupported claims that would
undermine credibility? Is the abstract accurate?
```

**Full peer review for a top venue:**
```
REVIEW TYPE: Full peer review simulating NeurIPS standards
TARGET: NeurIPS 2026
STAGE: Pre-submission, have 2 weeks to revise
GOALS: Acceptance. This is our strongest result this year.
CONCERNS: Reviewer 2 at ICML said our baselines were unfair — we've added
new comparisons but want to know if they're sufficient. Also worried about
the clarity of Section 4 (theoretical analysis).
```

**Framing/positioning help:**
```
REVIEW TYPE: Framing and positioning review
TARGET: Nature Machine Intelligence
STAGE: Early draft, structure is not final
GOALS: We want to frame this as an AI Safety contribution, but the core
work is a capability result. How do we bridge that gap?
CONCERNS: Does the safety framing feel forced? Is the related work section
missing key AI Safety references? Would a safety-focused reviewer buy our argument?
```

**Methodology-focused review:**
```
REVIEW TYPE: Methodology audit
TARGET: JMLR
STAGE: Post-rejection, reviewer flagged statistical issues
GOALS: Fix the methodology concerns from the first round of reviews
CONCERNS: Previous reviewer said our significance tests were inappropriate
for non-i.i.d. data. We've switched to a permutation test — is this the
right call? Also, are our ablations sufficient?
CONTEXT: The rejection review is pasted at the end of the .tex file as a comment.
```

**Revision guidance:**
```
REVIEW TYPE: Revision alignment check
TARGET: AAAI 2026 (resubmission)
STAGE: Revised draft after major revisions
GOALS: We got a "revise and resubmit" — need to verify we've addressed all
the concerns adequately
CONCERNS: The main criticism was lack of real-world evaluation. We've added
a case study in Section 6 — is it convincing? Did we over-correct by making
the paper too long?
CONTEXT: Original reviews are in Appendix D of the paper.
```

---

## Length Guidelines

| Brief Length | Tokens | Effect on Cost | Recommendation |
|-------------|--------|----------------|----------------|
| 1-2 sentences | ~50 | Negligible | Too short. You'll get generic feedback. |
| **1 paragraph** | **~100-200** | **Negligible** | **Minimum viable brief.** |
| **Structured (recommended)** | **~200-500** | **< $0.01 extra** | **Best bang for buck.** |
| Full page | ~500-1000 | ~$0.02 extra | Fine if you have a lot of context. |
| Multiple pages | 1000+ | $0.05+ extra | Diminishing returns. Keep it focused. |

The brief adds almost nothing to cost — it's included once per reviewer prompt.
The paper itself (10,000-20,000+ tokens) dominates the token budget. So write
a thorough brief without worrying about cost.

**However:** don't dump raw data, full literature reviews, or entire email
threads into the brief. This doesn't help — it dilutes the signal. The brief
should be YOUR synthesis of what you need, not a data dump for the model to sort through.

---

## What to Include

- **Your actual goal.** "Get into NeurIPS" and "establish priority on ArXiv"
  demand very different reviews.
- **Your specific worries.** If you know Section 3 is weak, say so. The reviewers
  will spend more time there.
- **Previous feedback.** If you've been rejected before, tell the council what
  the reviewers said. They'll check whether you've addressed it.
- **Target audience.** Who will read this? ML researchers? Policymakers?
  Practitioners? This changes how the Outsider and Peer Reviewer evaluate clarity.
- **Constraints.** Page limits, formatting requirements, submission deadlines.
  The Alignment Guide uses these to judge what to cut.

## What NOT to Include

- **Raw experimental data.** The paper should contain this, not the brief.
- **Full literature reviews.** Don't paste 50 paper summaries. If specific papers
  are relevant, mention them by name.
- **Entire email threads or review histories.** Summarize the key points yourself.
- **Implementation details.** Unless the paper is about the implementation,
  code-level details belong elsewhere.
- **Requests for the model to "be harsh" or "be nice."** The reviewers have fixed
  mandates. They'll be thorough regardless.

---

## How the Brief Flows Into Each Reviewer

Every reviewer sees your brief appended to their system prompt. Here's how each
persona uses it:

| Reviewer | How they use your brief |
|----------|----------------------|
| Source Auditor | Focuses fact-checking on claims related to your concerns |
| Methodologist | Gives extra scrutiny to methodology areas you flagged |
| Peer Reviewer | Evaluates against the standards of your target venue |
| Domain Expert | Positions the work relative to your stated goals |
| Outsider | Reads with your target audience in mind |
| Alignment Guide | Checks whether the paper delivers on YOUR stated goals |

---

## Quick-Start Templates

Copy-paste one of these and fill in the blanks:

**Template A — Standard Review:**
```
Full peer review for [VENUE]. This is a [early draft / near-final / revision].
Main contribution: [one sentence]. I'm most worried about [specific concern].
```

**Template B — Specific Ask:**
```
I need help with [specific aspect]. Target: [venue/purpose].
Background: [why this is tricky]. Please focus on [sections/claims].
```

**Template C — Post-Rejection:**
```
Resubmission to [venue] after [accept/reject/R&R].
Previous reviewer concerns: [list them]. Changes made: [list them].
Question: Have we adequately addressed the feedback?
```
