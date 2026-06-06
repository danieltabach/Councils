# Brief Guide — Project Review Board

The **brief** is the single most important input besides the project description itself. It tells all 6 reviewers what kind of feedback you need. Without it, they give a generic review. With it, every dollar spent produces targeted, actionable output.

## What the brief should contain

- **Review type**: What kind of review? (Feasibility check, full evaluation, scope audit, market validation, technical review)
- **Stage**: Napkin idea, early concept, have a prototype, ready to launch, post-launch pivot?
- **Goals**: What are you trying to figure out?
- **Concerns**: What specifically worries you? What needs extra attention?
- **Constraints**: Budget, timeline, team size, skill gaps, dependencies
- **Context**: Background not in the description (prior feedback, failed attempts, etc.)

## Brief length guidelines

- 1-2 sentences: too short, gets generic output
- **1 structured paragraph (100-500 tokens): ideal** — costs < $0.01 extra
- Multiple pages: diminishing returns, dilutes focus

## Example briefs

### "Should I build this?"
> REVIEW TYPE: Feasibility and market check. STAGE: Early idea, no code yet. GOALS: Determine if this is worth investing 3 months of evenings. CONCERNS: Not sure if anyone else needs this. Worried the technical complexity is beyond my skill level (intermediate Python developer). CONSTRAINTS: Solo developer, $500 budget, no ML experience.

### "Is my MVP scoped right?"
> REVIEW TYPE: Scope and priority review. STAGE: Have a rough spec, starting to build. GOALS: Ship something useful in 6 weeks. CONCERNS: Feature list feels too long — what should I cut? Am I building the right thing first? CONSTRAINTS: 2-person team, both part-time.

### "Ready to launch?"
> REVIEW TYPE: Pre-launch readiness. STAGE: Working prototype, 50 beta users. GOALS: Go public next month. CONCERNS: Onboarding flow is clunky. Not sure about pricing. Beta users like it but I don't know if it'll grow. CONTEXT: Competitors X and Y exist but target enterprise — I'm going consumer.

### "Technical architecture review"
> REVIEW TYPE: Technical deep-dive. STAGE: Early prototype, architecture decisions still flexible. GOALS: Make sure I'm not painting myself into a corner. CONCERNS: Database choice (Postgres vs. Mongo), whether to use a queue, and if my auth approach will scale. CONSTRAINTS: AWS credits, need to stay under $50/month hosting.

### "Post-pivot evaluation"
> REVIEW TYPE: Full evaluation after pivot. STAGE: Rebuilt core product around new use case. GOALS: Validate the new direction makes more sense than the old one. CONCERNS: Previous version failed because of poor retention — is this version better? CONTEXT: Original product was a task manager for teams, pivoted to personal knowledge base after user interviews showed solo users were the most engaged.

## What NOT to put in the brief

- Full codebases or raw data (summarize the relevant parts)
- Entire email threads (pull out the key points)
- Requests to "be harsh" or "be nice" (reviewers have fixed mandates)
- Long literature reviews or market research (mention specific competitors by name)
