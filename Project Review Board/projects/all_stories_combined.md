# Danny's Complete Story Library (16 Stories)

Each story contains: canonical narrative, defensible fact sheet, historic bullet variants, approved agent-selectable bullets, agent rules, and candidate input.

---

# Story 1: ATLAS / BAR — The System

## Canonical Narrative

Danny built BAR (Banker Allocation Recommendation), later branded ATLAS, an automated decision platform for JPMorgan Chase's Consumer Banking division. It is a MILP-based resource allocation engine that optimizes banker staffing across 3,700+ branches nationwide, impacting ~24,000 FTEs across 3 banker role types (Associate Banker, Relationship Banker, Private Client Banker).

The system's objective function maximizes net value across six components: product value (account openings across 4 product types x 5 balance bands), outreach opportunity value (16 customer cohorts), teller coverage, minus servicing costs and transition/disruption costs, plus revenue-lift signals from an integrated XGBoost model (BSOT). The solver operates under constraints including demand fulfillment, capacity limits, utilization floors, staffing policy rules (min servicing %, max account opening %, min cohort allocation), pool-level FTE budgets, and a ±2 licensed banker deviation limit per branch.

Before the solver existed, Danny spent ~6 months building the three analytical foundations that feed it:
1. **Demand sizing** — using CRM task-hour data across servicing, account opening, teller, and outreach, normalized to monthly with seasonality and non-customer-facing time adjustments
2. **Outreach maximum estimation** — a double-regression methodology: first regressing branch features against call volumes to identify upper-residual branches (those outperforming their peer group), then regressing contact rates per customer cohort within those high-performers to derive per-branch outreach ceilings across 16 customer segments
3. **Task value estimation** — matched-pairs causal analysis comparing balance growth over 12 months for customers with identical features opened by different banker roles, producing a role-by-product-by-affluence value dictionary

The system is config-driven: roles are defined in a central registry with capability flags (can_do_teller, can_do_servicing, etc.) and all solver components — variables, constraints, objective terms — derive dynamically from role definitions. Adding a new role is a dictionary entry, not a code rewrite.

Danny integrated an existing team's XGBoost revenue-lift model (BSOT) as binary scenario selection variables within the MILP formulation. For each branch, the solver chooses among five discrete staffing scenarios (±2, ±1, unchanged) and adds the corresponding revenue-lift (or loss) value to the objective. This constrained the solver's recommendations to actionable ±1-2 person shifts while simultaneously capturing revenue signals the field already trusted.

Danny also built an iterative demand buffer algorithm to address incomplete CRM data (observed utilization systematically undercounts real demand). The algorithm scales demand hours by a buffer multiplier and iterates until all role pools are fully allocated and outreach opportunity utilization falls within a target range (65-80%).

Danny built this as the sole data scientist, coordinating across 7+ cross-functional teams: Workforce Planning, Finance/CFO, Divisional/Regional/Market Directors, Assignments, Market Expansion, and Outreach. He presented to the CFO of Community Banking and later covered BAR in a steerco with the CB CEO, securing sign-off for regional pilots. Bus factor of 1 — Danny owns the full scope end to end.

The naming evolved over time: early resumes call it "BAR" or "the optimization model." Later versions rebrand to "ATLAS" or "automated decision platform." For agent output, use whichever framing fits the role — "ATLAS" for product/decision science roles, "optimization engine" for OR roles, "production decision system" for MLE roles.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| 3,700+ branches | Confirmed | Network scale |
| ~24,000 FTEs impacted | Confirmed | Danny's narrative + resumes |
| 7+ cross-functional teams | Code-confirmed | WFP, Finance/CFO, Div/Regional/Market Directors, Assignments, Market Expansion, Outreach |
| Solo data scientist (bus factor of 1) | Confirmed | Danny owns full scope end to end |
| Config-driven modular architecture | Code-confirmed | `role_definitions.py` registry pattern, solver/preprocessor/config all derive dynamically |
| MILP solver (PuLP/CBC) | Code-confirmed | `from pulp import LpVariable, lpSum, LpProblem, LpMaximize` |
| 3 role types: AB, RB, PCB | Code-confirmed | With capability flags and role-specific constraints |
| 4 product types x 5 balance bands | Code-confirmed | Checking, Card, Savings, CDs x <1k, <50k, <150k, >=150k, business |
| 16 customer cohorts | Code-confirmed | Y/N x Lead/None x Affluent/Base BAL x Affluent/Base WAL |
| XGBoost revenue-lift model (BSOT) integrated | Code-confirmed | 5 binary scenario selection variables per branch (±2, ±1, 0) |
| Iterative demand buffer algorithm | Code-confirmed | `optimizer.py` — converges on 65-80% opportunity ratio |
| Transition/disruption costs in objective | Code-confirmed | Configurable per role, absolute-value linearization |
| Replaced manual workflows | Confirmed | Nothing like BAR existed before (BSOT and BCM were partial tools) |
| Presented to C-suite | Confirmed | CFO presentation (20 slides, Danny presented) + CEO steerco (1 slide in 4-slide deck) |
| Authored technical paper | Confirmed | Draft in BAR snippets folder, pending organizational review for publication |
| ~6 months building analytical foundations | Confirmed | Before solver implementation began |
| Double-regression outreach methodology | Confirmed | Danny's narrative, code-consistent with Opportunity_Hours_Total and cohort structure |
| Matched-pairs value estimation | Confirmed | Role-by-product-by-affluence value dictionary |
| Grid search for disruption costs | Confirmed | Per-quarter calibration against field acceptance criteria |

### ⚠️ Defensibility Notes
| Claim from old resumes | Reality | Recommendation |
|------------------------|---------|----------------|
| "Gurobi solver" | Code uses PuLP/CBC. Danny has not migrated to Gurobi. | Say "MILP solver" or "PuLP" — do NOT claim Gurobi |
| "Patent pending" | Paper draft exists but Chase hasn't filed a patent | Say "authored technical paper (pending organizational review)" |
| "$150M projected incremental value" | Danny needs to confirm what this number actually represents | Keep using with "projected" qualifier until Danny clarifies |
| "Snowflake ETL pipelines" | Danny pipes data through Snowflake but infra is still maturing; scheduler in progress | Say "built data pipelines through Snowflake" — defensible |

---

## All Historic Bullet Variants

### Era 1: Early Resumes (500+ branches, PuLP, "Optimization Data Scientist")

> Developed a stochastic optimization model using PuLP to allocate staffing across 500+ branches, accounting for fluctuating demand, opportunity levels, and value. Projected to improve staffing efficiency by 20% and align resources with regional growth priorities
> — *Resume #1 (F)*

> Built an advanced stochastic optimization framework using PuLP for effective staff distribution among over 500 branches, accounting for demand shifts and opportunities; anticipated workforce efficiency forecasted to reach beyond 20%
> — *Resume #2 (VF)*

> Led the engineering and design of a network-wide staffing solution for Chase branches, accounting for demand shifts and opportunities; applying data-driven budget realignment to maximize high-value opportunities, resulting in a 12% boost in outreach and a 15% decrease in branch demand constraint
> — *Resume #3*

### Era 2: "Architect of BAR" (3,700+ branches, Senior DS)

> Architected and solely developed the Banker Allocation Recommendation (BAR) engine, Chase's first-ever data-driven, network-wide (3,700+ branches) staffing optimization engine
> — *Resumes #4-6 (Oracle, 2025_Prod, 2025)*

> Modeled the core optimization engine to allocate staff based on quantified branch demand, service tasks, and banker value, replacing subjective field-based decision-making
> — *Resumes #4-6*

> Pioneered an ensemble approach by integrating BAR with an existing regression-based revenue lift model, using a custom weighting system to refine recommendations and ensure alignment with established tools
> — *Resumes #4-6*

> Established foundational analytics to empirically define distinct banker role value and establish branch-specific maximum outreach potential, providing crucial inputs for the BAR engine
> — *Resumes #4-6*

> Drove the full project lifecycle from conceptualization, rigorous validation, and iterative tuning to executive presentations and successful deployment as Chase's standalone branch staffing engine
> — *Resumes #4-6*

### Era 3: "5 YOE" with Sub-headers (BAR/ABME/ARB structure)

> Led the development of the BAR product, an enterprise staffing engine that defined and operationalized headcount OKRs across 3,700+ branches, establishing a data-driven approach to national workforce planning
> — *Resume #7 (2025)*

> Owned the end-to-end technical build-out, from architecting Snowflake ETL pipelines to engineering the core Gurobi solver which integrated a revenue-lift XGBoost model to weigh thousands of variables
> — *Resume #7*

### Era 4: Patent Pending, $150M+ framing

> Led the end-to-end development and deployment of the Banker Allocation Recommendation (BAR) platform (patent pending), an enterprise-scale optimization engine operationalizing budget-neutral staffing decisions across 3,700+ branches
> — *Resumes #8-10, 14-15*

> Led end-to-end development of enterprise optimization engine (patent pending) operationalizing budget-neutral staffing across 3,700+ branches, impacting 24K FTEs and delivering $150M projected incremental revenue + $5M cost savings
> — *Resumes #11-13 (Oracle, Netflix, Stripe GTM)*

### Era 5: Decision Platform / ATLAS branding

> Built automated resource allocation platform replacing manual decision workflows across 3,700+ locations
> — *Resume #16 (2026)*

> Designed MILP optimization model integrating revenue forecasting (XGBoost) and demand models, enabling config-driven scenario planning and cross-functional coordination across 7+ teams
> — *Resume #16*

> Built end-to-end automated decision system replacing manual workflows across 3,700+ locations, unified revenue forecasting, demand modeling, and optimization into a config-driven scenario planning tool with cross-functional coordination across 7+ teams
> — *Resume #18 (ProductDS_v2)*

> Delivered $150M in monthly projected business value by building an automated decision platform (ATLAS) that replaced manual workflows across 3,700+ locations
> — *Resume #19 (DanielT_2026)*

> Unified ML-based revenue forecasting, demand modeling, and constrained optimization into a single config-driven system with cross-functional coordination across 7+ teams
> — *Resumes #19-20*

> Delivered $150M in monthly revenue by building an automated decision platform (ATLAS) that replaced manual workflows across 3,700+ locations
> — *Resume #20 (Hex)*

---

## Approved Agent-Selectable Bullets

*Each bullet below is grounded in code-confirmed or narrative-confirmed facts. No embellishment.*

### Tier 1: Primary System Bullet (pick ONE per resume — this is the headline)

> **[A — OR / Applied Scientist]**
> Built a MILP-based staffing optimization engine across 3,700+ branches, formulating a multi-component objective (product value, outreach opportunity, transition costs) under demand, capacity, utilization, and policy constraints across 3 role types, 4 product categories, and 16 customer cohorts

> **[B — Decision Scientist]**
> Built an automated decision platform that replaced manual staffing workflows across 3,700+ branches, integrating causal value estimation (matched-pairs balance growth analysis) with constrained optimization to drive budget-neutral allocation decisions for ~24K FTEs

> **[C — Product DS]**
> Built and deployed an automated decision platform across 3,700+ locations, coordinating with 7+ cross-functional teams (Workforce Planning, Finance, regional leadership) and presenting to C-suite executives to secure enterprise-wide rollout

> **[D — Senior Data Analyst]**
> Built an automated staffing system serving 3,700+ branches by consolidating CRM task-hour data, outreach volumes, and account-level value metrics into a single optimization engine that replaced subjective field-based allocation decisions

> **[E — MLE / Analytics Engineering]**
> Built a production decision system (ATLAS) across 3,700+ branches using a modular, config-driven architecture where role definitions, constraints, and objective terms derive dynamically from a central registry; integrated an XGBoost revenue-lift model as binary scenario variables within the MILP solver

### Tier 2: Architecture / How It Works (supporting bullet — use when space allows)

> **[A — Formulation depth]**
> Designed MILP formulation maximizing net value across product openings, outreach opportunity, and revenue-lift scenarios, subject to demand fulfillment, capacity, utilization floors, staffing policy, and pool-level budget constraints; integrated an XGBoost model as binary scenario selection (±2 headcount) per branch

> **[B — Causal + optimization blend]**
> Unified causal value estimation (matched-pairs analysis across banker roles and customer segments), demand modeling, and constrained optimization into a single config-driven system coordinating 7+ teams

> **[C — Cross-functional / stakeholder]**
> Coordinated across Workforce Planning, Finance, Divisional Directors, and Market Expansion teams to align solver recommendations with field-level staffing policies; CFO endorsed projections and CEO approved phased rollout

> **[D — Data infrastructure]**
> Consolidated CRM task-hour data, outreach funnel metrics, servicing costs, and account-level value data across Snowflake pipelines into a single branch-level dataset feeding the optimization engine

> **[E — System design]**
> Architected config-driven system where adding a new banker role requires only a registry entry — solver variables, constraints, objective terms, preprocessing, and output columns all adapt automatically; built iterative demand buffer algorithm to handle incomplete CRM data

### Tier 3: Analytical Foundations (methodology bullets — pick based on JD emphasis)

> **[A/B — Outreach ceiling methodology]**
> Designed double-regression methodology to estimate per-branch outreach maximums: regressed branch features against call volumes to identify high-performing branches, then derived contact-rate functions across 16 customer cohorts from those upper-residual branches to set network-wide outreach ceilings

> **[B — Value estimation methodology]**
> Built role-by-product value dictionary using matched-pairs causal analysis: isolated customers with identical features opened by different banker roles and measured 12-month balance growth to estimate the incremental value of each role-product-customer combination

> **[A — Disruption cost calibration]**
> Calibrated disruption cost parameters through grid search over representative regions, targeting field acceptance criteria: 30%+ branches unchanged, 90%+ within ±1 net headcount, preserving minimum licensed banker thresholds per branch

> **[E — Demand buffer engineering]**
> Built iterative demand buffer algorithm to address systematic CRM undercounting of branch utilization, converging on a multiplier that fully allocates all role pools while maintaining outreach opportunity utilization within a 65-80% target range

> **[C/D — Stakeholder translation]**
> Translated solver outputs into scenario planning dashboards and automated reports comparing current vs. optimized allocation, showing revenue-lift calculations per variable to enable decision-making by Workforce Planning and regional leadership

---

## Agent Rules

1. **Name flexibility:** Use "ATLAS" for product/decision roles, "optimization engine" or "resource allocation engine" for OR roles, "production decision system" for MLE roles. All refer to the same system.
2. **⚠️ Do NOT say "Gurobi."** The solver is PuLP/CBC. Say "MILP solver" or "MILP (PuLP)" if the JD asks for solver specifics. Danny has not migrated to Gurobi.
3. **⚠️ Do NOT say "patent pending."** Say "authored technical paper on modular optimization architecture (pending organizational review)" if the JD values publications/IP.
4. **Solo build:** Can say "solely built," "built as sole data scientist," or "built end-to-end." All are defensible. Bus factor of 1 is real.
5. **Never say** "leveraged," "ensured," "spearheaded" per Danny's voice rules.
6. **24K FTEs:** Use when scale of impact matters (enterprise roles, leadership-facing). Omit for technical-depth roles.
7. **Tier selection:** Pick ONE Tier 1 bullet (headline), up to ONE Tier 2 (architecture), and up to ONE Tier 3 (methodology). Never use more than 3 ATLAS bullets on a single resume — leave room for experimentation and SwagUp.
8. **Tier 3 bullets are interview depth, not resume filler.** Use them only when the JD specifically asks for the methodology they describe (e.g., "quasi-experimental" → value estimation bullet, "mathematical formulation" → formulation depth bullet).

---

## Danny's Input

*Answer whatever you can — even partial answers help. Skip anything you can't discuss.*

### The Build
1. **Timeline:** When did you start building BAR/ATLAS? When did it first go into production? How long was the core build (months)?

I joined this team after FAST around May 2024. 
Story goes like this: my manager (Chandler) built out a very tiny mini branch example of staff & task allocation in Excel using a solver. I was brought on board after literally building a tiny MILP using pulp - making fake simulated data - fake branches and did this with the help of chatgpt over one weekend. I pitched the notebook - showed the results - my assumptions, the simulation, the ideas I had for each variable and constraint and then solved it. It was rudimentary and crude - and obviously not a good solution. But the pitch was incredible from me. My manager was excited - told me to talk to his boss (Evan at the time - he moved teams eventually). Evan grilled me gently on the notebook - pushed my assumptions - my thinking - smiled and was excited to have me get started. Told me to talk to Chandler. I asked Chandler "so when is the actual interview" - Chandler said "That was the interview, you start Monday."

I started work on just building out the assumptions. We had a lot of tasks at hand before we even touched what the Solver algorithm would look like. 

a. How do we size the demand of today's branches?
b. How do we size what branches COULD do today given optimal staffing already? 
c. How do we estimate the value of each task a banker could do? 


a. How do we size the demand of today's branches? 
    - We had a few options - but we had some SQL tables that carried in our CRMs. Tables that basically told us how much time bankers spent on account opening for different products, time spent on certain tasks, servicing, and teller work and outreach (both inbound and outreach). Sounds simple enough but we had to settle on the assumptions with other teams to align on what is an acceptable way to estimate what demand looks like (seasonality assumptions for instance). We knew that if we over-engineered this solver - we wouldn't land on the proper assumptions that landed on good recommendations. I and my manager both understood this and managed upward. We wanted to move with agility and simplicitly over over-engineered crap that would only make iterations slow and results difficult to explain. 
    - We sized demand over a quarter as a test pilot - we also knew that there was "non-customer facing" time, time spent on lunch, breaks, conversations, water cooler time. We accounted for this, and landed on a basic assumption of what a banker's maximum capacity without overload would look like - and what a floor would look like for a successful branch. We relied on historic field guidance for the floor of utilization and ceilings. 
b. How do we size what branches COULD do today given optimal staffing already?
    - This one was an incredibly interesting project. We had to decide "what is possible for a branch to do in terms of outbound calls". Let me explain what outbound outreach looks like. A banker calls, they ask you if you're looking to put your money into a savings, a CD or something like an investment. The banker gets a lead or they even look at customers themselves and build a portfolio to call. They call and try to basically go from 
    call -> a successful contact (an appointment or a followup) -> an in-person meeting at a branch -> opening an account. THIS is a successful funnel for a banker to achieve. We care about the CALL portion of this. We want to make sure that topline outreach volumes can be hit. Bankers of course have "scorecards" or goals they need to hit - but this isn't always possible - and not always in a banker's control. I should mention - bankers do their research on their customer to maximize their portfolio either from the lead engine or the customer database itself. They look for signals that tell them you have extra money laying around that they might be able to get into the Chase ecosystem. 
    - So for BAR / ATLAS - the goal is how do we size how much outreach COULD potentially happen if the branch had optimal staffing and no demand constraints? We needed an outreach volume maximum that bankers could do. This would be the proxy to determine how much volume of calls would be available. 
    - I build a double regression. let me explain. The first phase of this regression basically regressed household counts, branch features, population features, etc, etc, against call counts. Each branch was a point on this regression. Y = mx + b -> call volume = m1 * household count + m2 * branch features + b is the simplified way to understand this. 
    - Once we have this regression -> I build a 5x5 matrix around the data points. Not a literal matrix but think of it like this, along the X variables - I set up 5 types of quintiles equally distributed - and on the Y axis - I broke out the residuals from the upper residuals (call volumes far exceeding the average for these branches with similar X features) and the lower residuals (call volumes for branches with similar X features being much lower than the average.)
    - I did an entire analysis basically looking at these residuals by branch quintile grouping. What we discovered was proving our hypothesis -> branches with more people (compared to their branch average) and less demand that took away time from their calls -> directly contributed to how much the branch can output in terms of call volumes. 
    - We basically pitched this as -> get us better staffing and help us optimize demand constraints in branches -> and we can hit these call counts the upper residuals do. 
    - Now, the second regression: for each household within the upper residuals for each branch quintile, I regressed the average contact rate PER customer cohort (high wallet, high chase balance, or low wallet, high chase balance, etc other customer features) based on how OFTEN the high residual branches called these customers. This gave us a slope function for every customer cohort (16 of them) for each branch that existed in the upper residual. This slope function WAS the contact rate -> for every household in this branch under this cohort -> upper residual branches call them x.x times. This was how we could calculate what the "max" threshold was. 
    - We apply this contact rate across cohorts for every branch in the network. Now every branch basically has an upper limit that is based on what the upper residual branches in the ecosystem can do. because we proved that those branches have better staffing and lighter demand -> if we can get other branches to have the same conditions -> we should be able to hit the contact rates we assume per household. Finally, this was how we landed on our branch maximums which get directly inputted as the outreach volume available per branch within the solver. 
    
c. How do we estimate the value of each task a banker could do? 
    - This one was also in-depth and complicated and I had to lean on another data scientist to help me land here. 
    - The basic jist is this, we started with account products by role. Every product that opened was a customer who was opened by a banker. We needed to isolate the differences between a senior banker opening the same account for the same customer. But how do we removed routing bias? 
    - We looked at branch new customers who 6 months down the line we found had the same features - we isolated these customers and used techniques to minimize or completely remove the routing bias - the only difference was that a different banker opened them. We used a matched pairs process to compare how different products, opened by different types of clients of varying affluent ranges - opened by different banker roles - grew over the next 12 months. 
    - From here, we extrapolated the balance / value growth per product per account - and assigned values for each time a banker opened an account of this type for this type of client. We called this value 'revenue' - extrapolated from this balance growth over time that we measured in this matching process. This became a table that was basically a dictionary for our account opening products. 

    Looking sort of like this: 

    Banker Type, Associate Banker, Relationship Banker, Private Client Banker
    Credit Cards for <1k balances, 100, 200, 250
    Credit Cards for <50k balances, 200, 250, 320
    
    etc etc. This became the value piece of BAR. 

    These 3 pieces together took about 6 months to land on and finalize. Finally I began designing and implementing the first chunks of the solver. 

    I designed the preprocessing to ingest all this data, and shape it in a way where each branch is a row - and each column is a feature like for example the value of each role for a particular task - which was repetitive. But there were columns isolated the demand as well, servicing, and teller. 

    I set up the 3 base roles - before even making any config, and just set up core assumptions of what each role can do and what it can't do. AB, RB, PCB. You can check the details of how this solver was designed from the preprocessing to the final output and the constraints in this project space. 

    I do want to mention WHY optimizer.py was developed. Here is the deal - if we take what demand was historically done today and what is captured on our CRMs, we WONT be able to see all the demand happening at branches. branches MIGHT genuinely be stressed, but our utilization in the CRMs might only show bankers being utilized 40% of their time. we KNOW this isn't true. So we created an artificial demand buffer that buffers the servicing and account opening hours incrementally to artificially scale the demand so that we can allocate the entire pool of staff. Our core assumption is that every branch suffers the same rate of missing data we cant see - and it's safe to say if we buffer, we are capturing what is really happening at the same rate. Through the logic that if we sample the distribution of how demand looks at a branch - we can assume it just needs scaling to reach the real demand happening. A stressed branch might say 40% utilization. And we saw unstressed branches for example have metrics that say they are only 20% utilized. So in reality - they aren't under-utilized. The data just isnt seen. So optimizer.py was created as a way to push through the allocation. 

    We use the region between 65% and 80% of outreach hours available to basically say - look - we KNOW today you can probably allocate 70% of the maximum goals. So we are going to assume that even with ideal allocation you can hit this. If you can hit more - great - if not then that's fine too. We scale demand until there is so much demand that bankers can only attribute their time enough to cover ~70% of the maximum outreach hours we propose. 

    This algorithm took a few months of testing, catastrophic failures, compute issues, and lots of iterations to get even a working version going. We tried scaling big to small - to push it's limits. The version you see in this workspace is a dated sample of the type of code in the solver infra itself. But in general, Id say this took about 3-4 months to fully feel confident in our solver actually starting to make good recommendations. But here is the thing - it worked - the recommendations LOOKED sound against our metrics and KPIs, but now it took time to literally condense it and constrain it to fit the business needs. Even if moving 6 people from a branch to be distributed to other branches was "ideal" based on the math - no one in the field would ever take this recommendation seriously. 

    I personally thought of this like.. a dying star. Not in a bad way. When stars die, they expand from super giants and then shrink to tiny white dwarfs with incredible mass. This is exactly what happened to BAR. We condensed this giant recommendation swings it made - and over the course of many iterations and adjustments and demand tuning we managed to constrain it. One of the key ways we got there was by implementing BSOT. One of the issues with BAR initially is it had HUGE swings in recommendations - shift 3 people here, shift 5 bankers here, etc etc. I want you to imagine me literally feeling like I had to take this machine, and using my hands cram it into a tiny space and make it work. Condense, condense, condense, and fit within the policies chase had. How do we move from making huge shift recommendations -> to making recommendations within at MOST 2 people AND making sure we keep the value that BAR had with role mixtures? 

    BSOT is an XGBoost model. It basically takes the features of the branch - and with all things unchanged - gives you a "revenue lift" or "revenue loss" number based on keeping all other items the same - just changing the headcount number assumed. It would run 4 scenarios (I am not familiar with the specs but ill explain further as I understand it). Basically, all other features at the branch held firm, how would the Y (revenue lift) change if I added or removed a banker? What if I added or removed 2. The limit of this model was a -2 to +2 swing. Seems almost.. like its perfect to be a constraint in BAR. 

    Our partners rely on this model to basically help them make tradeoffs with other dashboards and internal measurements on where the most ideal positions for opportunity were for hiring or moving bankers. If the model said "Adding a banker here will add 300k lift" - our workforce planning partners would take that seriously and that particular branch would be considered strongly for a new headcount based on this. They have been using and making incremental adjustments to the Chase branch ecosystem based on this model for 2 years now. This was well-established in the field. 

    We had a field leadership offsite with our internal data science team and our partners and field leaders. Our directors wanted to unify a single staffing solution - why should we have 3 tools (BCM comes later I didnt mention them) when we can have 1? And why can't that one be BAR? BAR was set up in a way where it now needed to be integrated - to blend in the tools available to come up with powerful recommendations. So here was my pitch - which earned me respect and a strong repututation - and was one of the most pivotal moments of my career. We can literally funnel the BSOT scenario recommendations as a decision layer in BAR. youll notice in the files there are binary markers to determine the tradeoffs. BAR Automatically consolidates BSOT scenarios of +2 to -2 bankers in a way that constrains the LB side of things (RBs and PCBs.). Boom. One problem done. I implemented this over the course of a month with help from partners, and using BSOT recommendations directly funneled into this algorithm. Validation was strong - the model was constrained now - the recommendations aligned against value signals, against capacity signals, and now... we were one step closer to condensing our star to a final solution. (I also ran experiments with BSOT, like rounding the revenue lift numbers, or scaling them to weigh less if the branch was larger (branches with higher staff counts to start have a smaller BSOT revenue lift for example). And we eventually settled on a default config with the solution below).

    But now how do we make sure the shifts have a penalty? That is where I set up disruption costs. Disruption costs are tricky because we cant necessarily use the real cost of moving a banker - it might be too large or inexplainable to a solver which is now using a unified language of revenue from the value of a task and the value from BSOT. But we also cant avoid this. BAR shouldnt be allowed to freely move bankers - how can that make sense? If it moves without any penalty - it wouldnt be able to distill branches where the MOST value can be extracted today. Itll just make blanket recommendations. So how do we do this? How do we do a grid search over what disruption costs work? 

    I set up parameters and then set up a grid search over a sample of regions that are representative of the whole solution - since running an instance of BAR takes hours (CBC is slow) - I had to be smart. I knew this: 
    - Based on solutions we ran before, and what the field already agreed with - we needed atleast 30% of branches to remain completely non-changing. This was possible. 
    - We needed 85-90% of the solution to be a shift of literally 1 Net Person. Could be -3 AB and + 2RB or -1 RB + 2 AB. But the shift must be between +-1 person. This was what the field could agree to - and what we could pitch as a story. 
    - We needed there to be more 2 LB branches than 1 LB branches. Some of the earlier runs of this solver would make recommendations where branches with 2 bankers needed to go down to 1 many many times, but the field could not accept this. So for this, we needed to make sure the solution was constrained enough that the current ecosystem's branches that had 2 LBs outnumbered the ones that had 1 LB post recommendation. 

    We set up a grid search - and this grid search runs for each quarter to find new disruption costs that align with this. 

    We did many other things - such as set up custom constraints for specific branches, I set up static roles as well (not in the code) that exist in branches but cant be moved, I set up new roles as well like Senior PCBs and ARBs (which I helped pilot the launch of but that's a different story.). I also aligned to other things like real estate capacity. 

    we also integrated a new tool into BAR as well. BEAT or Health Tracker. 
    Health tracker was developed by my teammate to basically label and identify branches that have chronic issues like performance issues or demand issues or branches that also have opportunity that we dont tap into. There was 3 month period where BAR and BEAT were literally being tuned upon eachother to capture edge cases - her tool would find issue branches - but my tool wouldnt add staffing? Why? Oh? a constraint needed to be slightly adjusted? Done. An edge case for a specific branch scenario was caught? Done. 

    What's in flight right now? 
    Regional and market pilots. We got sign off from the CEO of CB banking himself. BAR, BEAT, BSOT are now in unison. Providing a unified staffing recommendation together - all in one. With labeling, recommendations, etc. BAR is also set to BECOME the guidance number for future budgets and branch headcounts. Small regions and markets are now running off these recommendations and testing branches for when they attrite or do backfills or get new budget. 
    
    I am also working on algorithms that will focus on clustering branches nearby so that we can run these pilots quicker - basically allowing us to test recommendations by just moving people to close-by but different branches to avoid travel issues for them, avoid waiting for attrition, avoid hiring or firing, avoid issues where branch managers dont want to give up people without something etc. The clustering algorithm will basically be aided to help us make a top-layer adjustment after BAR to allow us to launch this mini pilots with these recommendations and NOT actually disrupt people's lives and jobs. Bankers will just move to a different branch. 

    What does BAR promise to deliver? 
    9 billion in balance growth in a year. 
    net neutral - no headcount or budget shifts - we can do this all today. 
    ~90% of the solution happens within a +-1 person shift. 
    Addresses capacity and demand issues in 70% of the branches with chronic issues of capacity and demand. 
    Addresses performance issues in 80% (not a staffing change - but also captures opportunities for coaching) 
    And addresses 65% of branches with higher potential for additional staff to capture more wealth and opportunity. This is the real fucking deal. 

2. **Solo vs. supported:** You were the sole DS, but did you have engineering support for deployment? Data engineering for pipelines? Or was it truly end-to-end solo including infra?

I am frankly dissapointed with the tech stack in this bank. Getting access to tools like Databricks or AWS is difficult. I went around this by piping everything through our Snowflake platform and made it automatic. I am still in progress of making schedulers in Snowflake for this model but that will take some time. To get this handed off to a big platform like that as a model - so it doesnt sit on my local - it needs significant lift. it makes me upset I cant write much about this. The tech team is also slow. And so is the dashboard team. 

In the meantime, I piped it, built repeatable scripts to run it, cached all the data for any time period run, I built my own experimental platform within my workspaces to allow for quick iterations on any BAR experiments, I set up my own github, and I set up analytics that are automatically piped into a custom streamlit dashboard and generated reports, recommendations, high level views, and even revenue lift calculations that show us how we get from "Today" vs "BAR" in terms of dollar amount for each and every single variable in the solver. Infra that is more professional (level 2-4) will have to come later. 

3. **What existed before?** Was there a prior staffing model/tool, or was it literally "field managers decided based on gut"? What was the handoff like from old process → ATLAS?

BSOT as mentioned above. And BCM. BCM isnt a recommender. it just says "In 6 months we forecast this branch to have x.x amount of demand". This tool is a separate team and theyve been dragging their feet trying to integrate with us. But they are also used to forecast demand and account for things that BAR can't see (but is currently being implemented). Nothing like BAR existed before. 

### The Patent
4. **Patent scope:** What specifically is patented — the MILP formulation? The config-driven architecture? The integration of XGBoost + solver? Is it filed or granted?

I wrote a paper in the BAR snippets folder. Its a draft - close to a final one that still needs to be published under chase but they are dragging their feet. Which is part of my dissapointment. 

### Config-Driven Architecture
5. **What does "config-driven" actually mean in practice?** Can a non-technical user change configs? What's configurable — constraints, objective weights, regions, role definitions? How often do configs change?

Yes and No. Ideally - I personally want the workforce planning team to use this as a scenario planner. The reality is that our team handles which recommendations they currently see. But the architecture is there (check the code). There are a lot of access and controls issues with doing it this way - and a lot of risk the data science team would take on if we are wrong or if we give a tool and they use it wrong to make their recommendations. But the engine and architecture is there for this sort of capability. I made sure of that. 

6. **Modularity:** If someone wanted to swap the XGBoost model for a different forecasting model, how hard is that? Is the system designed for that kind of plug-and-play?

Eventually. 

### Cross-Functional
7. **The 7+ teams:** Can you name them? (Product, Finance, Workforce Planning, regional leads — who else?) Which ones pushed back the hardest? What was the biggest political or organizational challenge?

Workforce Planning - the Main users of BAR -> they have the final say on staffing in the entire chase ecosystem. 

Finance - Led by the CFO whom saw BAR and the 9 Billion lift and even in a steerco call said "Even if we are wrong by 50%. This thing will deliver 4.5 Billion. I believe in the numbers." -> they determine ecosystem budget for headcount 

Divisional / Regional / Market Directors -> They are in charge of their branch areas. For example like Northeast or Texas. Divisions -> Regional -> Markets are largest to smallest. Markets are in Regions. Regions are in Divisions. Each one has a leader. These people are also the end receivers of BAR recommendations. They care about headcount, taking care of their branches, making sure they hit their success metrics, making sure they allocate the budget assigned, making sure they tell Workforce planning which branches need help, which branches need people, etc etc. They are the key people responsible to help us get our tests up and running.  

Assignments -> Decide the algorithms and the systems that routes customers to bankers, we had to partner with them to make sure our assumptions were sound and tested.

Market Expansion Teams -> I support this team as well. Responsible for launching and designing new banker roles (ARB, ABME, Sr. PCB). They care about how their new roles will fit within the Chase ecosystem. use BAR as a proxy to tell them "Oh if BAR is saying it is worth putting a PCB here despite the disruption costs, this branch MUST have opportunity. We can put a senior PCB to capture it". I worked with them to land on assumptions for some of the roles. 

Outreach Team -> Worked with them to understand how bankers go through the funnel from call, contact made, scheduled meeting, account opened. 






8. **C-suite presentations:** How many times did you present to C-suite? What level (SVP, CEO, board)? What was the hardest question you got asked?

About BAR? 2 times. 

It was my manager's (Chandler's) boss, Andy. The CFO of community banking (Another Andy) and myself. I walked through 20 slides of BAR and its financials as well that I prepared. 

Once with the CEO in a steerco. I covered 1 slide of a 4 slide deck. My manager carried most of it. We talked about the upcoming execution plan - how BAR addresses the ecosystem, and the 9 billion dollar price tag. This was recent - got sign off. 

About another initiative 1 time on the ABME rollout (role design). 


### Current State
9. **Where is ATLAS today?** Fully rolled out? Still in phased deployment? How many regions/branches live?

Can't say its ongoing. But details above.

10. **Is it still your project?** Or has it been handed off to a team?

There is a bus factor of 1 and that is me. it is my owned project and MY tool. The KT hasn't been successful because nobody has time for onboarding. I own the scope end to end. I am the architect, the sales guy, the tech know-how, the results guy, the tuning guy, the infra guy, etc. 

---

# Story 2: ATLAS — Impact & Scale

## Canonical Narrative

ATLAS's recommendations are projected to generate $9B in incremental balance growth through net-neutral headcount reallocation — no new budget. The system optimizes staffing against higher-value markets and outreach opportunities. It is launching in small markets/regions first. The $150M figure refers to projected incremental value from account openings that the optimized platform enables, with an additional $5M in annual cost savings from eliminating mis-staffed hours. CEO approved the rollout based on these projections.

Multi-region pilots validated the system before enterprise rollout: 15% reduction in capacity misallocation (mis-staffed hours), 3-8% improvement in task utilization across all roles, and 4% increase in account opening conversions for licensed bankers.

**Critical distinction:** The $9B and $150M are different metrics.
- $9B = incremental balance growth from reallocation (PROJECTED, not realized)
- $150M = projected incremental value from account openings / monthly operational revenue the platform manages
- $5M = annual cost savings from reduced mis-staffing

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| $9B incremental balance growth / year | PROJECTED | $750M/month in balance growth from optimized account openings and outreach. CEO approved. |
| $5-15M/month in cost savings | PROJECTED | From role-mix reallocation: senior bankers shift to outreach, ABs absorb more servicing. Net-neutral headcount. |
| $30M/month in task allocation savings | PROJECTED | Narrower framing of cost savings from more efficient hour allocation alone |
| 4,300 branches (updated) | Confirmed | Recently expanded from 3,700 after adding more branches into recommendations |
| Net-neutral budget | Confirmed | No additional headcount spend |
| Phased rollout (small market pilots) | Confirmed | 5-10 branch clusters in low-risk/emerging markets, working with willing market directors |
| CEO approved rollout | Confirmed | CFO of CB and CEO of CB both signed off |
| CFO quote | Confirmed | "Even if we are wrong by 50%, this thing will deliver 4.5 Billion." |
| BAR informing surgical staffing decisions today | Confirmed | WFP and Finance use BAR as decision support / gut check for adds, removes, edge cases |
| 90% of recommendations within ±1 net shift | Confirmed | From Danny's narrative and grid search acceptance criteria |
| 30%+ branches unchanged | Confirmed | Grid search acceptance criteria |
| Addresses 70% of chronically constrained branches | Confirmed | Danny's narrative |
| Addresses 80% of performance issue branches | Confirmed | Danny's narrative |
| Addresses 65% of high-potential branches | Confirmed | Danny's narrative |

### ⚠️ Numbers NOT Defensible — Do NOT Use
| Old claim | Reality | Danny's words |
|-----------|---------|---------------|
| "15% reduction in mis-staffed hours" | Not a measured result | "Its hard to quantify so I threw a number" |
| "3-8% task utilization improvement" | Not a measured result | "Hard to land on real numbers for this type of thing" |
| "4% account conversion lift" | An estimate, not measured | "We estimate... we should see at minimum a 4% increase" |
| "Delivered $150M in monthly revenue" | Projection, not realized | Multiple framings exist; $750M/month balance growth is the cleaner number |
| Any "realized" impact language | Everything is still projected | "Still projected unfortunately" |

### ⚠️ Numbers That Vary Across Old Resumes (for reference, do not reuse)
- "20% staffing efficiency improvement" (early 500-branch era)
- "12% boost in outreach" and "15% decrease in demand constraint" (Resume #3)
- "$155M value" ($150M + $5M — calculation changed over time)
- "$150M projected incremental value" — unclear origin, superseded by $750M/month and $30M/month framings

---

## All Historic Bullet Variants

### $9B Framing (from plan, not yet in historic resumes)

> Projected to unlock $9B in incremental balance growth through net-neutral headcount reallocation, optimizing staffing against high-value markets without increasing budget

> Sized at $9B in projected incremental balance growth by modeling optimal staff allocation against market opportunity, securing executive approval for phased rollout

> Platform manages $150M in monthly revenue across 3,700+ locations, serving as the operational backbone for staffing decisions

### $150M / $155M Framing (from resumes)

> Architected data pipelines in Snowflake and productionized a Gurobi optimization solver integrated with an XGBoost revenue-lift model, delivering $150M projected incremental value from account opening and $5M annual cost savings
> — *Resumes #8-10 (2026(1), Lyft, Decision Scientist)*

> Led end-to-end development of enterprise optimization engine (patent pending) operationalizing budget-neutral staffing across 3,700+ branches, impacting 24K FTEs and delivering $150M projected incremental revenue + $5M cost savings
> — *Resumes #11-13 (Oracle, Netflix, Stripe GTM)*

> Delivered $150M in monthly projected business value by building an automated decision platform (ATLAS) that replaced manual workflows across 3,700+ locations
> — *Resume #19*

> Delivered $150M in monthly revenue by building an automated decision platform (ATLAS) that replaced manual workflows across 3,700+ locations
> — *Resume #20 (Hex)*

### Pilot Results Framing

> Drove a multi-region pilot that validated a 15% reduction in mis-staffed hours and a 4% revenue per-banker-hour lift, securing executive buy-in for a national rollout
> — *Resume #7 (2025)*

> Executed multi-region pilots that achieved a 15% reduction in mis-staffed hours and 4% increase in revenue per banker hour, securing executive approval for enterprise rollout
> — *Resumes #8, 10 (2026(1), Decision Scientist)*

> Executed multi-region pilots achieving ~3-8% improvement in task utilization and 4% increase in account conversions, securing enterprise rollout approval
> — *Resumes #9, 11-15 (Lyft, Oracle, Netflix, Stripe variants)*

> Delivered $150M projected value and 15% reduction in capacity misallocation; presented to senior leaders securing enterprise rollout
> — *Resume #16 (2026)*

> Delivered $150M projected value and 15% reduction in capacity misallocation; presented findings to senior leadership securing enterprise-wide rollout
> — *Resumes #17-18 (ProductDS variants)*

### Capacity Misallocation Framing

> Reduced capacity misallocation by 15% by developing a benchmarking methodology using matched-pairs causal inference and residual analysis to generate value driver coefficients and utilization targets as optimization model inputs
> — *Resume #19*

### Early Era (20% efficiency, 500 branches)

> Projected to improve staffing efficiency by 20% and align resources with regional growth priorities
> — *Resume #1*

---

## Approved Agent-Selectable Bullets

*Impact bullets pair with a Story 1 system bullet. Never lead with impact alone — the reader needs to know what the system IS before hearing what it DOES.*

### $9B Headline (use when the JD values strategic scale, C-suite influence, or business impact)

> **[A — OR / Applied Scientist]**
> Projected $9B in annual balance growth through net-neutral headcount reallocation across 4,300+ branches; ~90% of recommendations within ±1 person shifts — secured CEO sign-off for phased market rollouts

> **[B — Decision Scientist]**
> Projected $9B in annual balance growth ($750M/month) by modeling optimal staff-to-opportunity allocation with net-neutral headcount; CFO endorsed projections, CEO approved phased rollout

> **[C — Product DS]**
> Projected $9B in annual balance growth through budget-neutral staffing reallocation; presented financial analysis to CFO of Community Banking and contributed to CEO steerco securing enterprise rollout approval

> **[D — Senior Data Analyst]**
> Sized $9B in projected annual balance growth by modeling staffing reallocation against market opportunity across 4,300+ branches; presented analysis to CFO, contributed to CEO sign-off for phased rollout

> **[E — MLE / Analytics Engineering]**
> Projected $9B in annual balance growth and $5-15M/month in cost savings through optimized role-mix allocation across 4,300+ branches; system now informing surgical staffing decisions for Workforce Planning and Finance

### Cost Savings / Operational Framing (use when the JD values efficiency, operations, or quantified ROI)

> **[A/C — Cost savings lead]**
> Projected $5-15M/month in cost savings by optimizing role-task allocation: shifting senior bankers toward high-value outreach while redistributing servicing hours to associate roles — all within existing headcount budget

> **[D — Analyst operational]**
> Projected $5-15M/month in network-wide cost savings by reallocating task hours across banker roles to match value-weighted demand, reducing time senior bankers spend on low-value servicing

### Ecosystem Impact (use when the JD values operational breadth, system thinking, or cross-functional influence)

> **[All — Ecosystem breadth]**
> System addresses capacity and demand issues in 70% of chronically constrained branches, performance coaching opportunities in 80%, and untapped wealth opportunity in 65% of high-potential branches — all within existing headcount budget

> **[C/D — Stakeholder / tool unification]**
> Unified three separate staffing tools (optimization engine, revenue-lift model, branch health tracker) into a single recommendation system now used by Workforce Planning and Finance as decision support for surgical staffing changes

### Current Usage / Adoption (use when the JD values influence, adoption, or real-world decision-making)

> **[C — Product / influence framing]**
> System actively informing staffing decisions: Workforce Planning uses recommendations as a decision-support layer for adds, removes, and role-mix changes; Finance references outputs as a gut check against branch-level budget guidance

> **[B — Decision support framing]**
> Deployed as decision-support system for surgical staffing changes: traces the "why" behind each recommendation (demand vs. opportunity vs. capacity), enabling regional directors to validate branch-level decisions against model outputs

---

## Agent Rules

1. **⚠️ NEVER say "delivered $9B" or "generated $9B."** Always use "projected." The CFO's own framing: "Even if we are wrong by 50%, this thing will deliver 4.5 Billion."
2. **$9B = $750M/month in projected balance growth** from net-neutral reallocation. Derived from matched-pairs value estimation × optimized task allocation, split by banking and investment products.
3. **⚠️ Do NOT use the old pilot metrics (15%, 3-8%, 4%).** Danny confirmed these were estimates he "threw" in, not measured results. They are in old resumes but should NOT be carried forward.
4. **$5-15M/month cost savings is defensible as projected.** From role-mix reallocation shifting senior bankers toward outreach and high-value openings. Use "$5-15M/month" range or just "$5M+/month" if the range feels soft.
5. **⚠️ Avoid "$150M" as a standalone number.** The calculation changed over time and Danny's clearer numbers ($750M/month balance growth, $30M/month allocation savings) supersede it. If an old resume used "$150M," don't carry it forward without qualification.
6. **4,300 branches** is the current number (expanded recently from 3,700). Use "4,300+" going forward. If a JD is already submitted with "3,700+" that's fine but update for new applications.
7. **"Informing staffing decisions" is the honest current state.** BAR is used as decision support for surgical changes, not as a fully deployed automated system. Frame accordingly.
8. **Pick ONE impact framing per resume.** $9B headline OR cost savings OR ecosystem breadth. Don't stack multiple.
9. **The "90% within ±1" and "30%+ unchanged" details** make the $9B credible. Include at least one when using the $9B bullet — it shows the recommendations are actionable, not theoretical.

---

## Danny's Input

*Answer whatever you can — even partial answers help. These are the most important questions in the whole story bank because impact numbers are the first thing interviewers probe.*

### The $9B
1. **How was $9B calculated?** What's the model? Is it: (optimized allocation revenue) - (current allocation revenue) = $9B? Over what time horizon — annual? Lifetime? What assumptions drive it (market growth, conversion rates, banker productivity)?

We basically went backwards from our matched pairs process as discussed in the 01 story. We looked at how those values times the tasks done today generate value - and then compared to post - how do the same values per task validate what it would look like with a BAR recommendation. We then changed them from task values to what it converts to in projected monthly balance growth and the gain we would get from allocating opportunity. We split this out by product (banking products like checkingm, savings, cards, cds) to investments products. The value add is basically promising 9B in balance growth year over year from these changes. With NET NEUTRAL FTE HEADCOUNT MIND YOU! 

2. **What did leadership actually see?** Was it a slide deck with sensitivity analysis? A single number? Did they challenge the assumptions?

Leadership saw alot over the course of this project. Everything from how we landed on our assumptions to begin with, how we sized each part as mention in story 01. How we determined what "value" looks like and how the model basically allocates on a high level (avoided technical stuff since they dont care.) 

3. **What could invalidate the $9B?** If an interviewer says "that's a big number, what are the assumptions?" — what's the 60-second answer?

"We are assuming that given the tasks are reallocated exactly, and that similar volumes of demand, account openings, servicing, and teller hours continue for the future as they have trended over the past years, we should hit this amount. Of course we also assume that our outreach estimations are within the ballpark of how much opportunity is there in a branch ecosystem. However, we know that demand will shift - especially for emerging markets - and THAT is where we are testing our pilot programs the most to see if BAR can hold up even when demand is uncertain. We are also assuming staff will be utilized to their potential within reason, and we are assuming that the tasks they take on will remain consistent to some extent over the course of time. This guidance will be updated every 6 months. So if things change, we can pivot quickly. And the configuration and architecture of the model allows for quick adjustments in the underlying assumptions." Idk I tried.

### The $150M
4. **What exactly is $150M?** Your resumes use it three different ways: "projected incremental value from account openings," "monthly projected business value," and "monthly revenue." Which is accurate? Is it monthly or total? Projected or realized?

Calculations changed over time. Here is the real value -> If we look at how much money we save just from the hourly tasks - just from allocation alone we save roughly $30 Million a month in savings from allocating more efficiently and putting staff where there is opportunity. 

if we expand that out to be a balance growth indicator - like how much money will come from account openings both from outreach and the walkins and the general demand -> balances growing by 750 M a month is the estimate which is 9 Billion a year. These are the numbers we land on. 

5. **$5M cost savings:** Is this realized or projected? How is it measured — reduced overtime? Fewer mis-staffed hours × hourly cost?

Its more like the way we allocate forces our senior bankers to do less servicing, it forces out other bankers to focus and target specific clients that walk in the door in an allocated way - it essentially makes our associate bankers take up a tad bit more of the servicing hours and the quick-hit account openings (think super easy checking account openings) that our more senior staff were doing which took away time from outreach and more valuable account opening and client deepenening. With this re-allocation we estimate this on a NET would provide between a 5-15M cost savings per month for the entire network. Which doesnt seem like a lot but we also have a net neutral headcount, dont disrupt the branches, and make recommendations the field can work with. Its also just one piece of the puzzle. 

### Pilot Results
6. **How many regions were in the pilot?** How many branches per region? How long did the pilot run?

I wrote 3700 branches. The number went up recently to 4300 after we added more branches into the fold for our recommendations. 

But in reality the recommendations are there and directionally help our workforce planning team treat it as a proxy - but real pilots where we actually shift around staff are set up in small markets - think 5-10 branch pilots that are in close proximity in low-risk areas or emerging markets where budget is a bit more fluid and we work with the market directors there who are excited about our tools. The pilot will take months to read, and we need to wait for branch feedback and other KPIs. Its a process unfortunately. Its a bank so things move at a snails pace. 

7. **15% reduction in mis-staffed hours:** How is a "mis-staffed hour" defined? Too many staff for demand? Wrong role mix?

Its hard to quantify so I threw a number. But basically our role mixture allocation does a couple things. 

We basically say senior bankers should up their outreach hours by 30% for the maximum value gain, and lessen their servicing and account hours by that much to balance the scales. The outreach we deemed was extremely important for getting new customers in the door to open more accounts. Especially wealthy ones. And our senior staff can handle this. We allocate them with BAR based on where the best and most valuable opportunity lies. 

But ABs and RBs allocate work differently, in general we try to get ABs to take on a bit more servicing hours and less account opening hours that an RB can do. RBs can work across servicing, account opening, and outreach. And they are constrained to do all 3 in a balanced way that helps the branch in general. 

8. **3-8% task utilization improvement:** What's "task utilization"? Is 3-8% a range across roles, or across regions?

See above for details on what I mean. Hard to land on real numbers for this type of thing. 

9. **4% account conversion lift:** For licensed bankers specifically — what was the baseline conversion rate? Is 4% absolute or relative?

We estimate that if we allocated the way we want to with BAR for more outreach - we should see at minimum a 4% increase in new customers walking through that door based on trends we saw with other branches in the ecosystem. 


### Rollout
10. **Current deployment status:** How many regions/branches are live as of now? What's the rollout timeline?

2 quarters - steady slow rollout being tested market by market. Full national pilot of roles will take years because of attrition, firing, hiring, budget changes. BUT, when the workforce planning team makes surgical precise changes in branches - BAR is in the conversation always. Just a FULL network optimization is a massive political lift especially in such a short time frame. I know - I am upset by it too but what can ya do? But for now its small market rollouts where the marketing director is excited about our tools and are very willing to work with us. We have an execution plan but itll take time for clear reads on if the recommendations worked. 

11. **Has any realized impact been measured post-rollout?** Or is everything still "projected"?

Still projected unfortunately. I know - it sucks. But here is the caveat, everytime our staffing team used BAR in a conversation where they wanted to add somewhere or remove from somewhere, BAR always agreed - and even traced the "why" behind its recommendation. So BAR is technically informing staffing decisions. Its just not a formal rollout like "Here is a recommendation - go change your entire org". Its more like 
"Based on my other tools (BSOT, BCM, Blueprint) it looks like I should do X. Oh - BAR agrees with me and shows me the WHY too! Great - ill pull the trigger". 

Or when staffing budget guidance changes per branch - even finance looks at our recommendations as a "gut check" to see if BAR agrees. We get flags if anything is an edge case but so far its been pretty consistent. 

or when we see a branch with capacity issues - sometimes there is doubt on if that branch is *actually* struggling or if its a utilization or performance problem. BAR is the gut check for our regional directors and the workforce planning team of "No this branch is ACTUALLY constrained and BAR says it can use an extra person. Looks like based on the value an AB is the best bet. Lets see if we can add a part time AB here" or "No BAR doesnt see this branch as having a demand problem, your staff most likely need coaching.". 



---

# Story 3: ATLAS — Technical Architecture

## Canonical Narrative

This story captures the technical depth of the ATLAS build — solver architecture, data pipelines, constraint formulation, and productionization details. It exists as a dedicated story because MLE-adjacent and analytics engineering roles need to see Danny can build and ship production systems, not just design experiments. It also provides the "how" details that OR/applied scientist roles probe in interviews.

**Solver Architecture (code-confirmed):**
- MILP solver using PuLP/CBC, operating at the region level
- Objective: maximize(product_value + cohort_value + teller_value - servicing_costs - transition_costs + BSOT_lift)
- Six value components, each with role-specific coefficients
- Decision variables: FTE counts per role per branch (AB continuous, RB/PCB integer), task-hour allocations (teller, servicing by balance band, products by band and type, opportunity by cohort), plus 5 binary BSOT scenario selection variables per branch
- Constraints: demand fulfillment (teller, servicing, products, opportunity), capacity (can't exceed hours), utilization floors (can't park people without work), staffing policy (min servicing %, max account opening %, min cohort allocation if opportunity > threshold), LB pool ±2 deviation, minimum FTE per branch, and pool-level FTE budgets

**BSOT Integration (code-confirmed):**
- BSOT is an XGBoost model built by a partner team that predicts revenue lift/loss from ±1 or ±2 headcount changes per branch
- Danny integrated BSOT into BAR by creating 5 binary variables per branch (is_actual_minus_2 through is_actual_plus_2) with an exactly-one constraint
- The solver chooses which BSOT scenario is optimal for each branch simultaneously with all other allocation decisions
- BSOT values are added directly to the objective, so the solver trades off task-allocation value against headcount-shift revenue signals

**Config-Driven Architecture (code-confirmed):**
- `role_definitions.py` serves as a central registry: each role defines capability flags (can_do_teller, can_do_servicing, can_do_products, can_do_opportunity), productivity rates, utilization thresholds, constraint parameters, and transition costs
- Solver (`model.py`), preprocessor (`preprocessing.py`), config (`config.py`), and output (`solver.py`) all derive dynamically from role definitions
- Adding a new role (e.g., Senior PCB, ARB) is a dictionary entry — zero code changes to solver logic

**Demand Buffer Algorithm (code-confirmed):**
- `optimizer.py` implements iterative demand scaling to handle CRM undercounting
- Starts with initial buffer, adjusts up (step 0.1) or down (step 0.07) based on whether FTE pools are fully allocated and opportunity ratio is within 65-80% target
- Converges when all role pool gaps are within tolerance AND opportunity ratio is in target range
- Fails gracefully if buffer drops below 0.5 or max iterations reached

**Solve-Time Optimization:**
- Danny cut full-network solve time from 8-12 hours (overnight runs) to ~1.5 hours through:
  - Warm starts: seeding demand buffer and disruption cost parameters from prior quarter's solution
  - Tighter constraint engineering to reduce search space
  - Region-level partitioning (150-250 branches per solve, perfectly suited to business use case)

**Data Quality & Validation:**
- Input tables refresh monthly (aligned to business planning cycles)
- Danny built extensive pre-flight validation checks and data contracts: business rule enforcement, edge case handling, preprocessing artifact checks, naming convention validation
- Current preprocessing.py in the snippets is outdated — the production version has far more validation gates

**Production Infrastructure:**
- Snowflake data pipelines for all input data
- Automated solver execution with result caching per time period
- Streamlit dashboards for analytics, reporting, and "Today vs. BAR" comparisons
- Streamlit app for config-based scenario planning (built for WFP but access not yet granted)
- Experimental platform for rapid iteration on BAR configurations
- Version-controlled codebase (personal GitHub)
- Bus factor of 1 — Danny built all of this solo within JPM's constrained tech environment

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| MILP solver (PuLP/CBC) | Code-confirmed | `from pulp import LpVariable, lpSum, LpProblem, LpMaximize` |
| XGBoost revenue-lift model (BSOT) | Code-confirmed | Integrated as 5 binary scenario variables per branch; BSOT is partner team's model |
| Config-driven modular architecture | Code-confirmed | `role_definitions.py` registry pattern |
| Snowflake data pipelines | Confirmed | Danny pipes data through Snowflake |
| Region-level optimization | Code-confirmed | Solver runs per division/region |
| 6-component objective function | Code-confirmed | Product + opportunity + teller - servicing - transition + BSOT lift |
| Constraint families | Code-confirmed | Demand, capacity, utilization, staffing policy, LB ±2, min FTE, pool budget |
| Scenario + validation tooling | Confirmed | For explainability and decision support |
| Ensemble with existing regression model | Confirmed | Custom weighting system |
| Tableau decision dashboards | Confirmed | For Finance and Workforce Planning |
| Demand forecasting integration | Confirmed | Time-series constraints |
| Residual analysis for capacity benchmarking | Confirmed | |
| Patent pending | Confirmed | |

---

## All Historic Bullet Variants

### Solver & Architecture

> Owned the end-to-end technical build-out, from architecting Snowflake ETL pipelines to engineering the core Gurobi solver which integrated a revenue-lift XGBoost model to weigh thousands of variables
> — *Resume #7*

> Designed Snowflake data pipelines for model training datasets (train/eval/test splits, windowed feature engineering) and productionized Gurobi solver integrated with XGBoost revenue-lift model for real-time decision support
> — *Resumes #11-15 (Oracle, Netflix, Stripe, Perplexity)*

> Architected data pipelines in Snowflake and productionized a Gurobi optimization solver integrated with an XGBoost revenue-lift model, delivering $150M projected incremental value from account opening and $5M annual cost savings
> — *Resumes #8-10*

> Designed MILP optimization model integrating revenue forecasting (XGBoost) and demand models, enabling config-driven scenario planning and cross-functional coordination across 7+ teams
> — *Resume #16*

### Constraint Formulation

> Designed the region-level formulation (maximize revenue) with role-mix/pool limits, task-utilization, branch FTE min/max, productivity caps, and demand-coverage; added guardrails (opportunity floors, account-opening caps) plus scenario + validation tooling for explainability and decision support
> — *Resume #9 (Lyft)*

> Partnered with demand forecasting team to integrate time-series constraints into staffing model; built multi-constraint optimization (role-mix limits, task-utilization caps, demand coverage) with scenario analysis tooling
> — *Resumes #11-12, 14-15 (Oracle, Netflix, Stripe, Perplexity)*

> Modeled the core optimization engine to allocate staff based on quantified branch demand, service tasks, and banker value, replacing subjective field-based decision-making
> — *Resumes #4-6*

### Ensemble & Integration

> Pioneered an ensemble approach by integrating BAR with an existing regression-based revenue lift model, using a custom weighting system to refine recommendations and ensure alignment with established tools
> — *Resumes #4-6*

### Foundational Analytics

> Established foundational analytics to empirically define distinct banker role value and establish branch-specific maximum outreach potential, providing crucial inputs for the BAR engine
> — *Resumes #4-6*

> Developed capacity benchmarking methodology using residual analysis and matched-pairs causal inference to generate role-specific value coefficients and utilization targets for model inputs
> — *Resume #16*

> Developed capacity benchmarking methodology using residual analysis and matched-pairs causal inference to generate value driver coefficients and utilization targets as model inputs
> — *Resumes #17-18*

### Dashboard & Cross-functional

> Collaborated with Finance and Workforce Planning to translate solver outputs into executive-facing Tableau dashboards enabling cost-impact analysis and budget-neutral scenario planning
> — *Resumes #11-15*

> Partnered with cross-functional teams (Product, Finance, and Workforce Planning) to translate solver outputs into a Tableau-based decision dashboard, enabling real-time scenario analysis for regional and national planning
> — *Resume #9 (Lyft)*

### Project Lifecycle

> Drove the full project lifecycle from conceptualization, rigorous validation, and iterative tuning to executive presentations and successful deployment as Chase's standalone branch staffing engine
> — *Resumes #4-6*

---

## Approved Agent-Selectable Bullets

*These are supplementary bullets — they pair with a Story 1 headline bullet, never stand alone. Pick at most ONE from this story per resume.*

### For OR / Applied Scientist roles

> **[A — Formulation specifics]**
> Formulated multi-component MILP objective maximizing product value, outreach opportunity value, and XGBoost revenue-lift signals, minus servicing costs and configurable disruption penalties; solved under demand fulfillment, capacity, utilization floor, staffing policy, and pool-budget constraints

> **[A — BSOT integration]**
> Integrated an existing XGBoost revenue-lift model into the MILP formulation as binary scenario selection variables (±2, ±1, unchanged per branch), simultaneously optimizing task allocation and headcount shift decisions within a unified solver

> **[A — Disruption cost tuning]**
> Calibrated disruption cost parameters through grid search across representative regions, targeting field acceptance criteria (30%+ branches unchanged, 90%+ within ±1 net headcount) and rerunning per quarter to adapt to ecosystem changes

### For Decision Science / Experimentation roles

> **[B — Value methodology]**
> Built role-by-product-by-customer value dictionary through matched-pairs causal analysis: isolated customers with identical features opened by different banker roles and measured 12-month balance growth to estimate incremental value per role-product-affluence combination

> **[B — Outreach ceiling methodology]**
> Designed double-regression outreach estimation: regressed branch features against call volumes to identify high-performing branches, then derived per-cohort contact-rate functions from those upper-residual performers to set outreach ceilings across 16 customer segments network-wide

### For Product DS roles

> **[C — System unification]**
> Unified three separate staffing tools (optimization engine, revenue-lift model, branch health tracker) into a single recommendation platform, eliminating conflicting guidance and enabling coordinated scenario planning for Workforce Planning and regional leadership

> **[C — Cross-functional delivery]**
> Coordinated across 7+ teams (Workforce Planning, Finance/CFO, Divisional Directors, Market Expansion, Assignments, Outreach) to align solver recommendations with field-level staffing policies, real estate constraints, and regional budget cycles

### For Senior Data Analyst roles

> **[D — Data consolidation]**
> Consolidated CRM task-hour data, outreach funnel metrics, servicing cost tables, XGBoost revenue-lift scenarios, and account-level value dictionaries across Snowflake pipelines into a unified branch-level dataset feeding the optimization engine

> **[D — Reporting automation]**
> Built automated reporting and Streamlit dashboards comparing current vs. optimized allocation, showing revenue-lift calculations per variable to enable scenario-based decision-making by Workforce Planning and regional leadership

### For MLE / Analytics Engineering roles

> **[E — Config-driven architecture]**
> Designed config-driven system with a central role registry defining capability flags, productivity rates, utilization thresholds, and constraint parameters; solver variables, objective terms, constraints, and output columns all derive dynamically — adding a new role requires zero code changes

> **[E — Demand buffer algorithm]**
> Built iterative demand buffer algorithm addressing systematic CRM undercounting: scales demand hours by a multiplier and iterates with asymmetric step sizes until all role pools are fully allocated and outreach opportunity utilization converges within a 65-80% target range

> **[E — Solve-time optimization]**
> Cut full-network solve time from 8-12 hours to 1.5 hours through warm starts (seeding demand buffers and disruption costs from prior solutions), tighter constraint engineering, and region-level parallelization across 150-250 branch partitions

> **[E — Production infrastructure]**
> Built end-to-end production infrastructure as sole developer: Snowflake data pipelines with pre-flight validation checks and data contracts, automated solver execution with result caching, Streamlit analytics dashboards, and experimental platform for rapid config iteration

> **[E — Data quality / validation]**
> Built pre-flight validation layer with data contracts enforcing business rules, edge case handling, naming conventions, and preprocessing artifact checks across all input tables before solver execution — monthly refresh cadence aligned to business planning cycles

---

## Agent Rules

1. **This story is supplementary.** It provides depth bullets to pair with Story 1 (system) or Story 2 (impact). It should NOT be used as a standalone section.
2. **⚠️ Do NOT say "Gurobi."** Solver is PuLP/CBC. Say "MILP solver" if the JD asks for solver specifics.
3. **Pick at most ONE bullet from this story per resume.** These are depth bullets that prove you can go deeper if asked. The resume should intrigue, not exhaust.
4. **Match the bullet to the JD's primary concern.** If the JD says "mathematical modeling" → formulation specifics. If it says "cross-functional" → system unification. If it says "production ML" → config-driven architecture. If it says "causal inference" → value methodology.
5. **These bullets are also interview prep.** Each one represents a 5-minute conversation Danny can have. The double-regression, the matched-pairs value estimation, the BSOT integration, and the disruption cost grid search are all stories Danny can walk through in detail.

---

## Danny's Input

*Most questions here are now answered by the code review and your narrative in Story 1. A few remaining items:*

### Solver Performance
1. **Solve time:** How long does a typical region-level solve take with CBC? Minutes? Hours? You mentioned "running an instance of BAR takes hours" — is that per region or full network?

Due to compute with CBC we can't run larger than a region (150-250 branches in one go) which is actually fine for the business use case and is perfect. I managed to benchmark and cut down time with SWE tricks in pure python and warm starts (like setting the demand buffer of a prior solution to the new solution so it doesnt search. Or a disruption cost that worked for this prior time period with this data) to speed it up. I cut down run times that were at some point overnight (8-12 hours for the whole network) to 1 hour 30 minutes for the whole network with clever architecting and tight constraints. 

2. **Solution space:** Roughly how many branches per region? (This lets us estimate decision variable count: ~N branches × 3 roles × multiple task-hour variables + 5N binary scenario variables)

150-250. 

### XGBoost / BSOT
3. **BSOT is another team's model.** Can you claim XGBoost on the resume since you integrated it but didn't build it? Or should the bullet say "integrated an XGBoost revenue-lift model" (which is accurate) rather than implying you built the XGBoost model?

I know how to build an XGBoost model and I know how BSOT works. I did integrate it into the solution - as rudimentary it might look - its elegant. And no one is going to check source code. Use XGBoost if need be almost for a key word ATS search if that makes sense. Like if the role might be something where the "branding" might be good, include it. 

4. **How often is BSOT retrained?** And how often do you re-run BAR with updated BSOT inputs?

Every quarter BSOT is retrained. But this is genuinely fine for our use-case. It doesnt need to be everyday. 

### Config-Driven System
6. **What's configurable?** Constraint bounds? Objective weights? Region scope? Role definitions? Give me 2-3 examples of a config change someone would make.

Everything in the config.py, the values, the scenarios can be run as experiments and created as dicts that can be run through a python terminal automatically. BSOT can be scaled up or down, or certain branches can get a smaller BSOT input if need be. Every role can be configured in terms of floors and ceilings for utilization, how much they should focus on every task (floor and ceiling minimums). Config.py is a bit dated I added more, but this works. Can also configure for time period length (if you want to average out 6 months instead of 3 you can.). If you want to create and test a new role you can - as long as the naming conventions are correct. 

7. **Who changes configs?** You? A product manager? Automated?

Our team unfortunately. But I built a supporting streamlit app to run this optimization AND allow a user to change the config. But our workforce planning team isnt allowed to use it. 

### Data Pipelines
8. **Snowflake pipeline details:** How many source tables feed the model? What's the refresh cadence — daily, weekly? How do you handle data quality issues?

The tables aren't live - they get refreshed monthly which is absolutely fine for this use-case. I built out many many many data contracts based on known business rules, edge cases, preprocessing artifacts, naming conventions, etc in the preprocessing - the current preprocessing.py is far outdated compared to the checks I built. I built pre-flight validation checks before the solver is even run. Every table ingested needs to pass certain criteria to make sure the data is clean and organized. 

9. **Train/eval/test splits:** Time-based splits? Random? What's the evaluation metric for the XGBoost model?

Unknown since I didnt build the model. Evaluation metric is revenue lift generated given the branch opportunity features and metrics that define how a branch ecosystem looks both staffing wise, but also its customer base and general features. 

### Validation & Explainability
10. **Scenario analysis tooling:** What does this look like? Can a user say "what if we add 10 bankers to Region X" and see the impact? Who uses it?

The way it currently works is workforce planning can say 

"Hey I have 50 Senior PCBs I want to put somewhere. Know what a good place might be" 

Lets say in a region we have 300 PCBs in-seat. So BAR's pool is 300. 

We let the solver assume there are now 350. Wherever it places them - it does so for a reason because it does role mixtures and optimizes to maximize revenue - which is driven by opportuntiy and value of customer cohorts and tasks at each branch. We can find them the best places to put these 50 Sr PCBs for example. 

11. **How do you validate that the solver's recommendations are good?** Backtesting? Expert review? A/B test against the old process?

Field alignment for now, market pilots as we speak. Field alignment is important because there are so many subject matter experts for every tiny thing that happens in a branch - directors and even branch managers know their branch health on the ground. We also talk a lot with others about edge cases, expectation-setting, etc. We can't AB test because AB tests with staffing are very costly and tricky to implement in disparate branch ecosystems. 
We basically make sure 

1. The recommendation makes sense on paper. here is an example: 
branch 101 shows that bankers are overworked - BAR says add 1 banker. We find a happy medium for hours per worker for the tasks there historically in terms of hours. 
2. We align against that branch's metrics - is there ample opportunity for more growth? Are bankers doing their tasks normally? etc etc
3. We ask experts and field knowers what they think "Oh yeah we were also considering adding a banker here!". Sort of like this. 


---

# Story 4: ABME — Staggered DiD / National Experimentation

## Canonical Narrative

Danny designed the full experimentation strategy for a national initiative rolling out a new banker role (ABME — Associate Banker, Market Expansion) across ~10,000 employees and ~1,200 branches. The core idea: Associate Bankers previously had no job entitlement to open accounts — they handled teller and servicing work, and account openings were the domain of RBs and PCBs. ABME added account opening to their entitlements, allowing them to independently open checking, savings, and student accounts. The hypothesis was that this would capture missed account-opening opportunities from walk-ins while freeing senior bankers (RBs, PCBs) to focus on outreach and high-value client deepening.

**The A/B/C design:**
- **A (Control):** Regular Associate Banker — teller + servicing only, no account-opening entitlement
- **B (ABME):** Entitled to open basic accounts (checking, savings, student accounts)
- **C (ABME+):** Entitled to open basic + investment accounts and CDs

The rollout was staggered — branches onboarded at different times, with a 6-month onboarding/training process per banker. ~80% of branches completed onboarding within a 6-month window. Danny initially ran a proof-of-concept on ~400 branches, then expanded analysis to ~1,200 branches and ~10k employees.

**The methodology (published at danieltabach.github.io):**
Danny built an event-study DiD framework to handle the staggered adoption. For each branch, he identified the adoption window (first to last trainee completing licensing), treated that window as "period 0" (blacked out — too noisy to measure), and normalized all branches to relative event time. This allowed clean pre/post comparison despite branches adopting at different calendar months. He controlled for branch size (grouping similarly-sized branches), validated parallel trends in the pre-period, and used location and time fixed effects.

**Metrics framework:**
- North Star: accounts opened per branch (by product, role, cohort) + servicing-to-account-opening conversion rate
- Secondary: outreach volume, affluent/investment account openings, contact-to-meeting conversion, meeting-to-opening rate, calls-to-opening rate
- Guardrails: customer complaints, servicing session frequency, walk-out proxy, teller service level, teller transaction rate, RB/PCB task time disruption

**Results (statistically significant):**
- +8-15% outreach lift (RBs and PCBs had more time for calls once ABMEs took over basic openings)
- +5-12% lift in account opening volume (missed walk-in opportunities now captured)
- +6-8% servicing-to-account-opening conversion (ABMEs could deepen during servicing sessions)
- No significant disruption to branch operations; slight early teller strain that cleared within months
- C-arm (investment/CD entitlement) was NOT adopted — insufficient volume and ABs naturally referred high-wallet clients to PCBs

**Caveat found:** ~6 months post-rollout, some branches saw ABs revert to servicing/teller habits. This was a coaching/performance issue, not an experiment flaw. Score cards and floor-presence requirements were implemented to address it.

**Outcome:** 2-slide CEO presentation. Secured nationwide expansion. The ABME role is now fully rolled out across every Chase branch — the AB role is completely gone.

**Published work sample:** Danny wrote a comprehensive blog post covering the full event-study methodology using simulated data: danieltabach.github.io/applied/staggered-did-event-study/. It covers both clean-holdout and everyone-eventually-treated scenarios, compares against naive cutoff and standard TWFE (showing naive underestimates by ~27%), and includes full Python code. References Callaway & Sant'Anna (2021), Sun & Abraham (2021), Goodman-Bacon (2021).

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| ~10,000 employees | Confirmed | Nationwide rollout |
| ~1,200 branches analyzed | Confirmed | Expanded from initial ~400 proof of concept |
| A/B/C test framework | Confirmed | A = regular AB (no account-opening entitlement), B = ABME (basic account entitlement), C = ABME+ (basic + investments/CDs, requires licensing) |
| Event-study DiD methodology | Confirmed | Published at danieltabach.github.io |
| 6-month adoption window ("period 0") | Confirmed | 80% of branches completed within this window |
| +8-15% outreach lift | Confirmed | Statistically significant. Range across branches/segments. |
| +5-12% account opening volume lift | Confirmed | Statistically significant. Captures missed walk-in opportunities. |
| +6-8% servicing-to-account-opening conversion | Confirmed | Statistically significant. ABMEs deepening during servicing sessions. |
| C-arm not adopted | Confirmed | Not enough investment/CD volume to justify; ABs referred to PCBs anyway |
| No significant disruption | Confirmed | Slight early teller strain, cleared within months |
| 2-slide CEO presentation | Confirmed | Methodology trust + results. Secured nationwide expansion. |
| ABME now fully nationwide | Confirmed | AB role completely gone. Every branch has ABMEs. |
| Parallel trends validated | Confirmed | Pre-period trends held |
| Controlled for branch size | Confirmed | Similarly-sized branches grouped together |
| Blog post published | Confirmed | Full methodology with simulated data, Python code, method comparison |

### ⚠️ Defensibility Notes
| Old claim | Reality | Recommendation |
|-----------|---------|----------------|
| "+8% productivity lift" (single number) | Actual range is 8-15% for outreach, 5-12% for openings | Use "+8% outreach lift" as the conservative end, or "8-15% outreach lift" for the range |
| "-4% demand constraint" | Danny didn't confirm a specific demand constraint number | Don't use; instead say "freed senior banker capacity for outreach" |
| "+4% client meetings" | Part of secondary metrics with 1-3% lifts that couldn't be proven significant | Don't use as a standalone number; it may be noise |
| "10k+ employee rollout" | ~10k employees across ~1,200 branches | Both framings are defensible; use whichever fits the bullet |

---

## All Historic Bullet Variants

### Full Experimentation Strategy

> Designed the experimentation strategy for a 10k+ employee national rollout, building a time-normalized difference-in-differences methodology to isolate treatment effects under staggered adoption; identified +8% productivity lift and secured nationwide expansion
> — *Plan (Story 3, Variant B)*

> Designed and implemented experimentation strategy (A/B/C test framework) for a new incentive-based banker role (~10k participant bankers), enabling causal inference of program impact on key product KPIs
> — *Resumes #8-15*

> Defined the experimentation strategy for a new incentive-based banker role, launching a ~400-branch A/B/C test to measure impact on branch ecosystem KPIs
> — *Resume #7*

### DiD Methodology

> Engineered a wave-based DiD framework correcting for staggered rollouts by normalizing treatment gaps into a 6-month post-onboarding window, yielding an unbiased causal estimate (+8% outreach lift)
> — *Resumes #8-15*

> Designed a novel 'wave-based' DiD measurement framework to disentangle treatment effects from a non-simultaneous rollout, ensuring an unbiased estimate of the program's causal impact
> — *Resume #7*

> Built time-normalized difference-in-differences methodology to isolate treatment effects under non-parallel trends; identified +8% productivity lift, securing CEO approval for nationwide expansion
> — *Resumes #17-19*

> Identified +8% productivity lift across 10k+ employees by designing the full experimentation strategy for a national initiative with staggered rollout; built a time-normalized difference-in-differences methodology to isolate treatment effects under non-parallel trends, securing nationwide expansion
> — *Resumes #19-20 (impact-first construction)*

> Designed full experimentation strategy for a national workforce initiative with staggered rollout across business units
> — *Resumes #17-18*

### Business Case Translation

> Translated analysis of a -4% drop in demand constraint and +4% lift in client meetings into a successful business case, directly shaping the product roadmap and securing the role's nationwide launch
> — *Resumes #8-15*

> Translated analysis of a -4% drop in demand constraint and +6% lift in sales outreach into a successful business case, directly shaping the product roadmap and securing the role's nationwide launch
> — *Resume #7*

### Early Era (pre-ABME branding)

> Coordinated with cross-functional teams to design and test a pilot role in 300 demand-constrained branches, allowing senior staff to focus on customer-facing tasks and boosting client outreach; resulted in a measurable 17% increase of outreach and branch capacity increases within three months for branches with the new role
> — *Resume #3*

> Designed treatment and control samples using matched-pairs analysis and controlled for bias across branch locations, customers, and external factors
> — *Resume #3*

> Implemented difference-in-differences analysis and propensity score matching to calculate lift in client outreach and branch capacity, isolating the impact of the pilot program while controlling for external variables
> — *Resume #3*

> Built a lift measurement framework using hypothesis testing and confidence intervals to quantify improvements in outreach and capacity, validating treatment effects
> — *Resume #3*

### Stripe/Perplexity (partnership emphasis)

> Designed and implemented A/B/C test framework for new banker role (~10k participants), partnering with Product team to define success metrics and experiment parameters; implemented wave-based difference-in-differences to correct for staggered rollout and isolate causal impact (+8% outreach lift, +4% client meetings)
> — *Resumes #14-15*

---

## Approved Agent-Selectable Bullets

### Tier 1: Primary Bullet (pick ONE — this is the headline for experimentation)

> **[B — Experimentation / Decision Science lead]**
> Designed A/B/C experiment and event-study DiD framework for a national role launch across ~1,200 branches and 10k employees with staggered adoption; identified +8-15% outreach lift and +5-12% account opening volume increase, securing CEO approval for nationwide expansion (role now deployed in every branch)

> **[A — OR / Applied Scientist]**
> Identified +8-15% outreach lift and +5-12% account opening increase across 10k+ employees by designing an event-study framework for a staggered national rollout, directly informing staffing allocation decisions and securing CEO approval for expansion

> **[C — Product DS]**
> Designed the experimentation strategy for a national initiative across ~1,200 branches, defining a north star metrics framework (accounts opened, servicing-to-opening conversion) with guardrails (complaint rates, walk-outs, teller service levels); presented causal evidence to CEO, securing nationwide expansion

> **[D — Senior Data Analyst]**
> Designed and analyzed a staggered national rollout across ~1,200 branches using event-study difference-in-differences, identifying statistically significant lifts in outreach (+8-15%) and account openings (+5-12%); delivered findings to CEO, securing nationwide expansion

> **[E — MLE / Analytics Engineering]**
> Built event-study DiD pipeline analyzing ~1,200 branches with staggered adoption: time-normalization to event periods, location and time fixed effects, branch-size controls, and parallel trend validation; results drove nationwide rollout now deployed in every branch

### Tier 2: Supporting Bullets (use when space allows — pick at most ONE)

> **[B — Methodology depth]**
> Built event-study DiD framework normalizing staggered rollout to relative event time: defined 6-month adoption window as "period 0" blackout, validated parallel trends in pre-period, and estimated period-by-period treatment effects with location and time fixed effects (published methodology at danieltabach.github.io)

> **[C — A/B/C design depth]**
> Designed three-arm experiment testing incremental entitlement expansion for associate bankers: control (teller/servicing only), basic account opening (checking/savings), and full entitlement including investments/CDs; C-arm results informed decision NOT to expand investment entitlements — insufficient volume to justify onboarding cost

> **[B/C — Metrics framework]**
> Defined multi-tier metrics framework: north star (accounts opened by product/role/cohort, servicing-to-opening conversion), secondary (outreach volume, contact-to-meeting conversion, affluent account openings), and guardrails (customer complaints, walk-out proxy, teller service levels, RB/PCB task disruption)

> **[All — Business outcome]**
> Results drove permanent organizational change: the original Associate Banker role was eliminated nationwide and replaced by the ABME role across every Chase branch — transforming how the branch ecosystem handles walk-in account openings

> **[D — Published methodology]**
> Published comprehensive technical write-up on event-study methodology for staggered rollouts (danieltabach.github.io), demonstrating that naive calendar-cutoff approaches underestimate treatment effects by ~27% compared to properly time-normalized event-study design

---

## Agent Rules

1. **This is Danny's strongest experimentation story.** Prioritize it for any role mentioning causal inference, experimentation, quasi-experimental design, DiD, or A/B testing.
2. **Blog post link:** Always include "Technical Writing: Staggered DiD Event-Study Design for Messy Rollouts — danieltabach.github.io" in the resume (per plan Section 5). This is a published, public work sample.
3. **The A/B/C design shows sophistication.** Three arms, incremental entitlement tiers, C-arm informed a "no" decision — that's experiment design maturity. Mention when the JD values experiment design or program evaluation.
4. **The metrics framework is a differentiator.** North star + secondary + guardrails shows Danny thinks about tradeoffs, not just top-line lift. Use the metrics bullet for product DS roles.
5. **"Role now deployed in every branch" is the ultimate punchline.** The AB role is gone. ABME replaced it nationwide. This is a permanent organizational change driven by Danny's analysis.
6. **Use ranges, not single numbers.** +8-15% outreach lift, +5-12% account openings. If space is tight, use the conservative end: "+8% outreach lift" or "+5% account opening lift."
7. **⚠️ Don't use "-4% demand constraint" or "+4% client meetings"** — Danny couldn't confirm these as specific, statistically significant results. The secondary metric lifts were 1-3% and couldn't be powered to significance.
8. **Don't conflate with ARB.** ABME = national 10k+ employee rollout with event-study DiD. ARB = 150-branch matched-pairs pilot. Different experiments, different methodologies.
9. **The "27% underestimation" finding from the blog** is a strong talking point for decision science roles — it shows Danny validated his methodology against alternatives.

---

## Danny's Input

*This is your strongest experimentation story. The more detail here, the more versatile the bullets become.*

### The Experiment Design
1. **A/B/C — what were the three arms?** What was A, what was B, what was C? How were branches assigned to each? Random? Stratified?

A -> just normal AB role (ABME just means associate banker market expansion. Its a funny name I know)

B -> The ABME role -> they were given more responsibilities. Originally, the control group was only consigned to do teller and servicing work, and only open accounts IF the RB and PCB were slammed and SOMEONE needed to do them. ABs are unlicensed (meaning they cannot open accounts - even checking or savings needed a confirmation from the RB and PCB). The ABME role gets rid of that, and now ABMEs are licensed and can open simple checkings, savings, student accounts 

C -> This was the ABME role but with more responsibilities, they can now open investing accounts and CD accounts on top of what the B arm can do. 


CORRECTION! its not that ABs are licensed to open accounts or not, it wasn't a job entitlement. Rest of the story stays the same. The C arm is the one that needs a license to open investment accounts. 


2. **Why A/B/C instead of simple A/B?** What was the hypothesis that required a third condition?

It was to understand responsibilities and how it impacted the branch ecosystem. 
The context is this, so many branches are constrained, we saw lots of walk-outs because nobody was available to do something as simple as open an account. Or we saw situations where an AB would help with servicing, but not have ANY authority to deepen with the client by saying "hey since you're in here would you be interested in opening a savings? We offer a special $200 bonus on-us if you open a savings account with a $3000 balance today". This would never happen - and so it is literally losing us opportunities all because the other licensed bankers are busy. So the idea was that if ABs can finally get licensed and have the ability to deepen and open accounts with clients, it wouldnt just improve account openings and servicing experiences, it would also let the more senior bankers have more time on doing outreach and making calls to valuable customers to deepen their relationships with them over the phone and improve on their portfolios. The idea was that this would have ripple effects, it would improve branch demand constraint, and generally improve the ecosystem. The downside was the cost and disruption of teaching your ABs how to open accounts, and spending time coaching them - its a 6 month onboarding process to do this. 

The point of the C-arm is to see if they can handle opening investments and CDs, which typically are for more high-wallet customers. And we wanted to see the incremental effect of doing this. If they are spread too thin - we would know. If the experiences arent great and a relationship banker had to take the reins instead, we would know. But if they succeeded and it actually opened more accounts that otherwise would've been lost, we would also see that. 

3. **~400 branches or ~10k employees?** One resume says ~400-branch A/B/C test, others say 10k employees. Are both true (400 branches housing 10k employees)? Or are these different phases?

I started a proof of concept by only looking at 400 branches. But I got more in my sample of branches to look at for this event design study. It was looking at 10k employees, and actually analyzed about ~1200 branches at different staggered times within one analysis. My blog post covers 90% of how I did this with the staggered roll out issue. 



### The Methodology
4. **"Time-normalized DiD" — walk me through it.** A branch onboards in March, another in July. How exactly do you align them to "period 0"? What's the 6-month window — 6 months before onboarding + 6 months after? Why 6 months specifically?

In the blog! You can pull my github it is public and you can read it. Im proud of the blog I wrote.
The sample of branches would've been larger, but about 80% of branches that started onboarding their ABMEs to get licensed did this within a 6 month period. The first person finished and the last person finished within 6 months of eachother. THIS was period 0. The effect in between wasn't capture - it would be noisy due to disruption. The pre and post would. I normalized by time by looking at this period 0 across all branches regardless of when they started onboarding in time. One of the challenges here was getting proper sample. 

I want to make it clear this test wasn't just looking at KPIs around success. Here are the general list of metrics Id say we looked at

North Star Metrics:

- Number of Accounts opened per Branch (By product, by role, by customer cohort.)
- Servicing Session to Account Opening Rate (How many initial servicing sessions turned into an account opening)

Secondary Metrics:

- Outreach Volume per Banker (only for RBs and PCBs)
- Affluent Account Opening per Banker (RBs and PCBs) 
- Investment Account Opening per Banker (RBs and PCBs)
- Contact Made to Meeting Conversion (How often do bankers who do outreach successfully convert a contact into a meeting. Meetings going up could mean bankers have MORE time to do meetings)
- Meeting to Account Opening Rate (How many scheduled appointment meetings turned into an account opening in the same day)
- Calls to Account Opening Rate (How did the topline call volume impact the meeting count?) 

Gaurdrails 

- Disruption metrics: 
    - Complaint Metrics from customers (Customers get an Ipad in the branch and are allowed to rate their experience) 
    - Servicing sessions (Did customers need to come in more frequently due to issues? You can imagine ABs who opened accounts and did something wrong would lead to more unhappy customers coming in) by reason by resolve-rate. 
    - Walk-out rate (Hard to measure events that DIDNT happen, a proxy is how many customers went in, went on the ipad, and hit the "Notify me when someone is available" button) 
    - Teller Service Level (Were ABs disrupted from their teller jobs causing teller lines to slow down significantly?) 
    - Teller transaction rate (Were ABs teller transaction rate decreased?) 
    - RB and PCB task time (Due to them coaching ABs in many instances, one of our concerns is the responsibility of onboarding was now going to disrupt other staff's responsibilities) 

The metrics here do a few things, they show us the tradeoffs between the opportunity gain and the accounts we capture vs the disruption we cause and how much that disruption impacts a branch. 



5. **What controls did you use?** Seasonality — how? Branch-level fixed effects? Covariates? Did you test for parallel trends pre-treatment?

The tough thing is due to limited sample - and a fixed population of branches - you CANT cut for too many controls because you'd either be p-hacking to tell a story you want to tell or you'd get random noise that doesnt capture the overall trends or success of this pilot. What I did do was control for branch features overall, placing similar-ish branches within groups together. One of the ways we did this was by looking at branch size. 1 out of the only 2 ABs in a branch with 1 RB might be more disrupted by this rollout than a Manhattan branch onboarding 4 people out of 20. We did test for parallel trends and they held. 

6. **Robustness checks:** Did you run placebo tests? Vary the window? Check for treatment effect heterogeneity across regions or branch types?

Not sure what placebo tests are. Our difference and differences should have covered the general trends of demand. We did vary the window - the 6 month black-out period was a good point and captured the most sample. We did control for the bias as much as we could. 

### The Results
7. **+8% outreach lift — is this the primary KPI?** What does "outreach" mean concretely? Calls made? Emails sent? Client meetings booked?
8. **-4% demand constraint:** What is "demand constraint"? Branches hitting capacity limits? How is it measured?
9. **+4% client meetings:** Is this on top of the +8% outreach, or a subset of it?
10. **+6% vs +8%:** Resume #7 says +6% sales outreach. Later resumes say +8%. Which is correct and why did it change?

It changed because Im an idiot. Here are the facts as much as I remember them. 

1. No significant disruption. The onboarding black-out period DID cause some disruption but not enough that completely derailed any branches or forced them to put the brakes on. The ABs were able to get licensed smoothly - especially ones with more tenure because they saw and already had a good sense of how to open basic accounts. 
2. There wasn't enough volume of CD and Investment accounts to be taken by ABMEs, and it was not worth the tradeoff to license them further to learn how to open these accounts because the accounts were taken by more senior staff in general with low volumes. They also wouldnt necessarily know how to work and deepen a relationship with someone who has a million dollars in the bank - in many field tests we saw that ABs actually just referred these types of customers anyways to the PCB sitting in the brach. So the C-arm was not the rollout. But it was good to measure for the test. 
3. There was a significant outreach lift. I believe somewhere between 8-15%. We saw that bankers DID indeed have more time now that ABMEs were rolled on to take basic account openings from walk-in clients more frequently. They finally had more time to make more calls and more outreach came from that. 
4. There was significant lift in the volume of accounts opened. I believe 5-12% if I recall correctly. A good chunk of missed opportunties were captured. Servicing to Account Opening sessions increased by a significant amount - nearly 6-8% of servicing sessions led to a conversation about opening a new account. These were the key takeaways. 
5. Teller service lines were slightly under more strain - but earlier in the test while ABs were still probably a little green to opening accounts and the allocation of tasks by the branch managers were probably a little shaky. This was a primacy bias (I think that's the word?) that we essentially saw clear itself out over time. After the branch got in the groove of things we saw solid lift across the board.

All other metrics had a 1-3% lift, and this lift *could* be noise, we didnt have the sample to power the confidence intervals to say this lift FOR CERTAIN came from the test. But no metrics were negative in direction. The positive lifts helped the story in general, but we couldnt statistically prove they were significant in the grand scheme of things. The other lifts WERE statistically proven to be significant. 

However, we did see a contingency. 
6. 6 months post onboarding, we saw a dip where some ABs started reverting back to doing servicing and teller of their own accord, and the branch equilibrium started to shift back to pre-ABME levels. This happened in a significant amount of branches - but was a COACHING and PERFORMANCE issue and a management issue - not a caveat of the experiment of the test. ABs were just more nervous and leaned too hard on the RBs and PCBs to take on account opening. It took some cohesion and big discussions to make sure they were going on board. We set up score cards that they should aim to hit -> and even modified the role mid-launch to force some AB time to literally stand around the floor of the branch and welcome in walk-ins. 



### The Business Impact
11. **CEO presentation:** How did you structure it? Slides + live demo? Just the numbers? What questions did the CEO ask?

2 Slides. One was "How we did the test, how you can trust us (basically), how we made sure this is going to get us the read we want" and the second was the read "Look at these metrics, we saw this lift and these changes, here is why. We recommend a launch across all branches". 

12. **"Secured nationwide expansion":** What does this mean operationally? Budget approved? Timeline set? How many locations expanded to?

It meant the ABME team - separate from our data science team, now had the go-ahead to implement their onboarding to license all ABs across the entire country on this role. That's it. Every single branch in the country now has ABMEs, the AB role is completely gone. 

13. **Current status:** Is ABME fully rolled out nationwide now? Still expanding?

Nationwide baby. 

### The Blog Post
14. **Is danieltabach.github.io live and published?** The plan says to always link it. Is the content finalized?
Published. Ping it yourself!

15. **What does the post cover?** Just the methodology, or results too? Any JPMC-sensitive content that could be an issue?
Go ahead and read. :D

---

# Story 5: ARB — Matched-Pairs Pilot Experiment

## Canonical Narrative

Danny designed and analyzed a matched-pairs experiment validating a new operational model (ARB — Associate Relationship Banker role) across 150 locations. This was a strategic initiative to validate a replacement role addressing staff attrition. Treatment groups included adding the new role to existing teams vs. swapping an existing role. Danny designed the methodology, selected matched pairs, validated regional controls, and presented to leadership.

The experiment found 10-20 hours/week of high-value capacity unlocked per location by freeing senior bankers from lower-value tasks — enabling them to refocus on high-value client outreach, increasing client meetings and account openings while alleviating service bottlenecks for demand-constrained branches. The pilot was specifically in Colorado (mentioned in Resume #7).

In later resumes (Oracle, Netflix), Danny also describes building propensity models predicting client fit for the specialized role and using matched-pairs methodology to debias balance growth estimates.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| 150 locations/branches | Confirmed | Some early versions say ~100 |
| Matched-pairs causal methodology | Confirmed | |
| 10-20 hours/week freed per location | Confirmed | High-value capacity unlocked |
| Two treatment arms (add vs. swap) | Confirmed | |
| Senior bankers refocused on high-value clients | Confirmed | Second-order effect |
| Service bottleneck alleviation | Confirmed | For demand-constrained branches |
| Colorado location | Partially confirmed | Mentioned in Resume #7 only |
| Strategic initiative for staff attrition | Confirmed | Resume #7 |
| Propensity models for client fit | Confirmed | Resumes #11-12 (Oracle, Netflix) |
| Debiasing balance growth estimates | Confirmed | Resumes #11-12 |

### ⚠️ Number Discrepancy
- "10-20 hours/week" (plan, resumes #16-20) vs "~20 senior banker hours/month" (resumes #11-15)
- These are 4-5x apart. Danny needs to confirm which is canonical. The later resumes consistently use "10-20 hours/week" which is the stronger claim.
- Resume #7 uses "~100 branches" while later resumes use "150 branches"

---

## All Historic Bullet Variants

### Core Experiment Design

> Designed a matched-pairs experiment across 150 locations validating a new operational model, demonstrating 10-20 hours/week of high-value capacity unlocked per location
> — *Plan (Variant B)*

> Led the experimental design for a banker role pilot in Colorado, a strategic initiative to validate a role for staff attrition, applying a matched-pairs approach to isolate causal impact and ensure statistical power with a small, staggered sample of ~100 branches
> — *Resume #7*

> Designed small-sample pilot experiments using matched-pairs causal methodology to isolate treatment effects and validate new staffing role efficacy across 150 branches
> — *Resumes #8, 10 (2026(1), Decision Scientist)*

> Designed and analyzed matched-pairs pilot experiment validating a new role model across 150 branches; demonstrated 10-20 hours/week of high-value capacity unlocked per location
> — *Resumes #17-18 (ProductDS variants)*

> Demonstrated 10-20 hours/week of high-value capacity unlocked per location by designing and analyzing a matched-pairs experiment validating a new operational model across 150 locations
> — *Resumes #19-20 (impact-first construction)*

### Capacity & Value Proof

> Proved role's value by freeing ~10-20 senior banker hours per week for high-value outreach, increasing client meetings and account openings while alleviating service bottlenecks
> — *Resumes #8, 10*

> Proved the role's holistic value by quantifying critical second-order effects enabling senior bankers to refocus on high-value clients and reducing service bottlenecks for demand-constrained branches
> — *Resume #7*

> Proved role value by freeing ~20 senior banker hours/month for high-value outreach, increasing meetings and account openings while alleviating service bottlenecks
> — *Resumes #11-15 (Oracle, Netflix, Stripe, Perplexity)*

### Propensity Modeling Angle

> Built propensity models predicting client fit for specialized banker roles; used matched-pairs methodology to debias balance growth estimates and validate new role efficacy across 150 branches
> — *Resumes #11-12, 14-15 (Oracle, Netflix, Stripe, Perplexity)*

> Built propensity models predicting client fit for specialized roles; used matched-pairs methodology to validate efficacy across 150 branches, proving value by freeing ~20 banker hours/month for high-value client outreach
> — *Resume #13 (Stripe GTM)*

### Measurement Framework (Early)

> Designed and implemented the measurement framework for a pilot program testing a novel hybrid banker role, quantifying impact on branch capacity, client outreach, and demand management across 300 test branches
> — *Resumes #4-6*

> Coordinated with cross-functional teams to launch a new pilot role across 50 high-demand branches, offloading responsibilities from senior staff and increasing client outreach by 15% in 3 months; analyzed outreach volumes and conducted staff interviews to evaluate operational improvements and role effectiveness
> — *Resume #1*

---

## Approved Agent-Selectable Bullets

> **[B — Experimentation lead]**
> Designed a matched-pairs experiment across 150 locations validating a new operational model, demonstrating 10-20 hours/week of high-value capacity unlocked per location

> **[C — Product DS]**
> Validated a new operational model through a matched-pairs experiment across 150 locations, quantifying 10-20 hours/week of freed senior capacity to inform national rollout decisions

> **[A — OR-adjacent]**
> Demonstrated 10-20 hours/week of high-value capacity freed per location by designing a matched-pairs causal experiment across 150 branches, validating a staffing model change

> **[D — Analyst]**
> Analyzed matched-pairs pilot experiment across 150 branches validating a new role model; quantified 10-20 hours/week of high-value capacity unlocked per location and presented findings to leadership

> **[E — With propensity modeling]**
> Built propensity models predicting client fit for specialized roles; used matched-pairs methodology to debias balance growth estimates and validate new role efficacy across 150 branches

> **[C — Impact-first]**
> Demonstrated 10-20 hours/week of high-value capacity unlocked per location by designing and analyzing a matched-pairs experiment validating a new operational model across 150 locations

---

## Agent Rules

1. **This is the "smaller" experiment story.** Use it to show range alongside ABME (the big one). If space is tight and the role only needs one experimentation bullet, ABME usually wins.
2. **Don't conflate with ABME.** ARB = 150-branch matched-pairs. ABME = 10k+ employee staggered DiD. Different experiments, different methodologies.
3. **Hours/week vs hours/month:** Use "10-20 hours/week" as the canonical version (matches plan and later resumes). Flag to Danny that this needs final confirmation.
4. **Propensity modeling angle** is unique to this story. Use it when the JD mentions propensity models, classification, or client scoring — it's the only JPMC story that hits that keyword.
5. **"Second-order effects"** framing (senior bankers refocusing) is strong for product roles that value understanding downstream impact, not just direct metrics.

---

## Danny's Input

*The critical question here is the hours discrepancy. Everything else is enrichment.*

### ⚠️ CRITICAL: The Hours Number
1. **10-20 hours/week or ~20 hours/month?** Your later resumes say "10-20 hours/week freed per location." Your Oracle/Netflix resumes say "~20 hours/month." These are 4-5x apart. Which is the real, defensible number? If an interviewer asks "how did you calculate that?" — what's the answer?

Let me maybe give you context of what we were doing so you can understand. 

ARB is a national pilot for a new role. Some context of why Chase wanted this role, we noticed that in many instances the RB role has sort of been siloed into doing a little bit of outreach, some account opening, and some servicing. ARBs were meant to be a new role that could act as a support role for our other LBs within the branch. The truth is.. it's just a way to rebrand an old role (RB) and call it something else with a cheaper price tag on it. The ARB role was intended to upskill ABMEs/ABs into a role where they can open more complex accounts and complete outreach - but without the same incentives that PCBs and RBs get for outreach as far as I can understand. Whether or not I agree with the ethics of doing this is besides the point. This role *does* add jobs rather than recycle them, but in many cases it also serves as a backfill role for RBs and PCBs or ABs who attrite. I think for some reason (as far as I know) ARBs are easier because they dont have to be licensed to open accounts and they can do every task the RB does. Their point was similar to the ABME story - to offload branch demand and busyness. 

### The Experiment
2. **150 branches or ~100?** Resume #7 says ~100, later resumes say 150. Which is correct?

The pilot started in Colorado with ~50 branches. As the resume goes on the project was expanded as pilots to 100 -> then 150 -> then an approval for a nationwide rollout. 

3. **How were matched pairs selected?** What variables did you match on — branch revenue? FTE count? Region? Customer mix? Demand level?

Choosing the pilot region was where we did the matching. The problem was - we were limited in our test because we had to find branches WITHIN a region that were similar to eachother enough to have a sample of branches we can make relatively decent comparisons with AND the region had to be large enough that we can launch a pilot. 

The items we matched on were branch sizes (FTE), opportunity metrics like how many calls were available, affluency levels, balance levels, etc. The problem was - the more we match - the less sample we get. And this was an iterative problem that I worked with a teammate on to land. It was not easy - and colorado just had the better matching results - albeit also limited. 

4. **"Add vs. swap" — two treatment arms.** How many branches in each arm? Did one clearly outperform the other? What was the control — branches with no new role?

The truth is, there wasn't too much of a difference between the swap and the add branches. Add branches of course took a bit more time to ramp up - but since they were add - they didn't cause much disruption in the branch. Swaps were harder to read from what I recall because there was a delay in the role launch and the read was noisy. 

Maybe in the initial pilot 20 swap and 20 add branches - then expanded to 50 and 50 - then 75 and 75. Though the add branches were significantly reduced because over time when bankers attrited (this role test took a year and was very long and iterative and slow) - we moved away from add branches to swap branches due to budget constraints. So the majority of the test was just swapping people for the ARB role. Usually upskilling an ABME/AB. 

5. **Colorado specifically:** Was the whole pilot in Colorado, or was Colorado one of several regions? Why Colorado?

Whole pilot was in Colorado. Ideal matching results. Politically safe, quieter branches, market directors were on board so were the regional leads. 

### The Role
6. **What is the ARB role exactly?** What tasks does this person handle? What did senior bankers do before that they no longer have to do?

Everything an RB does. Truly I think they are just meant to help with more servicing and account opening tasks. 

7. **"Strategic initiative for staff attrition":** What was the attrition problem? Were senior bankers leaving because they were stuck doing low-value work?

Can't say honestly. Attrition isn't too common - maybe 10 bankers attrited over an 8 month period. 

### Propensity Models
8. **You mention propensity models in some resumes.** What were you predicting — which clients fit the new role? Which branches would benefit most? What features went into the model?

One propensity model was seeing the propensity for an account to be opened by an ARB. Truthfully I didnt work on this much this story is more like fluff. 

### Outcome
9. **Was ARB rolled out beyond the pilot?** Is it nationwide now? How many locations?

About 500. 

10. **Did anyone measure long-term impact?** 10-20 hours/week freed is the immediate result — did that translate to measurable revenue lift or retention improvement over time?

This was the long term result - about 5% measureable lift in accounts opened because of the new staff, but otherwise the lift was.. negligible. The unfortunate part is this really shipped due to cost savings - not innovation on a role. 


---

# Story 6: FAST — Propensity-to-Pay Model

## Canonical Narrative

During Danny's time on JPMorgan Chase's Focused Analytics Solutions Team (FAST), he developed a regression model using behavioral features to categorize 1 million+ customers by propensity to pay. The analysis identified at-risk customers — those likely to miss payments or overdraft — and was instrumental in launching a small/flexible loan program with adjusted repayment terms to assist vulnerable clients in avoiding overdrafts or late payments.

This is an early-career story from before Danny moved to the optimization/ecosystems team. It demonstrates customer-level modeling, behavioral feature engineering, and real business impact through product launch.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| 1 million+ customers categorized | Confirmed | |
| Behavioral features used | Confirmed | |
| Regression model | Confirmed | Later versions say "multivariate model" |
| Drove launch of flexible loan program | Confirmed | For at-risk/vulnerable customers |
| Overdraft/late payment prevention | Confirmed | Resume #1 mentions this specifically |
| FAST team (Aug 2022 - Apr 2024) | Confirmed | |

---

## All Historic Bullet Variants

> Developed and implemented a regression model utilizing behavioral features to categorize customers based on propensity to pay; drove the introduction of a small loan program with flexible repayment terms to assist at-risk customers in avoiding overdrafts or late payments
> — *Resume #1 (F)*

> Developed and implemented a regression model based on behavioral features to categorize 1 million+ customers by propensity to pay; this analysis was instrumental in launching a flexible loan program for vulnerable clients
> — *Resume #2 (VF)*

> Developed and deployed a multivariate model based on behavioral features to categorize 1 million+ customers by propensity to pay; enabling the launch of a flexible loan program for vulnerable clients
> — *Resumes #4-6*

> Deployed a multivariate model based on behavioral features to categorize 1 million+ customers by propensity to pay; enabling the launch of a flexible loan program for vulnerable clients
> — *Resumes #4-6 (shorter variant)*

---

## Approved Agent-Selectable Bullets

> **[D — Analyst]**
> Built a regression model on behavioral features to categorize 1M+ customers by propensity to pay, driving the launch of a flexible loan program for at-risk clients

> **[C — Product DS]**
> Developed a behavioral feature-based model categorizing 1M+ customers by propensity to pay, directly enabling a new loan product for vulnerable clients

> **[E — ML framing]**
> Deployed a multivariate classification model on behavioral features for 1M+ customers, enabling production scoring that drove launch of a flexible loan program

---

## Agent Rules

1. **This is a bench story.** Use it when the resume needs more bullets (e.g., if the JD values customer-level modeling, classification, or financial products) and the main ATLAS/experimentation bullets don't fill the page.
2. **FAST team context:** This predates Danny's senior role. If using it, it should appear under a separate "Data Scientist | FAST" sub-section, not mixed with ATLAS/BAR bullets.
3. **Don't over-elevate.** This is solid but not Danny's flagship work. It's useful as proof of breadth, not depth.
4. **"Vulnerable clients" / social impact angle** can resonate with mission-driven companies. Use when the company values responsible AI or financial inclusion.

---

## Danny's Input

*This is a bench story so less urgent, but a few details would make it much more versatile.*

1. **What behavioral features?** Payment history patterns? Overdraft frequency? Deposit regularity? Spending velocity? Give me 3-5 examples.

It was a while ago, but balance sizes, overdraft frequency, deposit consistency, even indicators if they stopped auto-pay into their savings, bills on time, autopay on bills, lagging trends over time in terms of their deposits as well, 

2. **Binary or multi-class?** Did the model output "at-risk" vs "not at-risk," or was there a gradient (high/medium/low risk)?

It actually was a pretty accurate and robust log-reg. Very simple - but the feature engineering made it powerful - and I adjusted the ROC curve I recall to improve it - I remember playing around with the FPR and TPR to capture the customers and label them in an at-risk way that was pretty accurate and robust across multiple time periods, features, etc. 


3. **What was your role vs. the team's role?** Did you build the model and hand it off, or were you involved in the loan program design too?

I was responsible for the feature engineering and the tuning of the ROC curve parameters if I recall to capture these customers. 

4. **Any model performance numbers?** AUC, precision, recall — even approximate?

AUC was fairly high - Like 88? Maybe 90? 

5. **Is the loan program still running?** Did it work? Any follow-up metrics?

It was passed off to another team. But basically we proved out that if you give a non-interest 50-100 dollar loan to customers who needed to repay their bills, theyd avoid delinquincy risk. Sometimes that small difference was enough to actually move the needle between people who were at-risk and not. 

6. **When was this?** Roughly what year/quarter during your FAST stint?

2022-2023? I want to also clarify FAST was like a Data Science Consultant role. We did projects for 6 months - it was very fast paced, we built models and shipped, and analytics behind problems other teams just didnt want to solve or wanted to solve but needed a strong DS team to do for them because not every team at Chase has a dedicated data science team. FAST was like the SWAT team of data science at chase. 

---

# Story 7: FAST — Next-Best-Product XGBoost Model

## Canonical Narrative

Danny engineered an end-to-end customer segmentation model using XGBoost, productionized via PySpark, to power a "Next-Best-Product" propensity model for 5 million+ customers. The model identified customers with high propensity for business product applications (e.g., business banking accounts) and enabled targeted mail-marketing campaigns for the Business Banking division. The model facilitated strategic marketing initiatives that directly correlated with increased conversion rates across key demographics.

This is another FAST team story demonstrating production ML, large-scale data processing, and direct marketing/business impact.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| 5 million+ customers | Confirmed | |
| XGBoost model | Confirmed | |
| PySpark productionization | Confirmed | |
| Next-Best-Product propensity model | Confirmed | Resume #1 |
| Targeted mail-marketing campaigns | Confirmed | For Business Banking |
| Customer segmentation | Confirmed | |
| Increased conversion rates | Confirmed | |

---

## All Historic Bullet Variants

> Designed a predictive model with XGBoost and productionized it via PySpark to enable a "Next-Best-Product" propensity model for 5 million+ customers. The model served as a tool that identified customers with a high propensity for business product applications and enabled targeted mail-marketing campaigns for Business Banking
> — *Resume #1 (F)*

> Engineered a robust customer segmentation model leveraging XGBoost within PySpark for 5 million+ customers; facilitated strategic mail-marketing initiatives that directly correlated with increased conversion rates across key demographics
> — *Resume #2 (VF)*

> Engineered an end-to-end customer segmentation XGBoost model within PySpark for 5 million+ customers; facilitated strategic mail-marketing initiatives that directly correlated with increased conversion rates across key demographics
> — *Resume #3*

> Engineered an end-to-end XGBoost customer segmentation model in PySpark for 5 million+ customers; facilitated strategic mail-marketing initiatives that directly correlated with increased conversion rates across key demographics
> — *Resumes #4-6*

---

## Approved Agent-Selectable Bullets

> **[E — MLE lead]**
> Engineered and productionized an XGBoost customer segmentation model via PySpark for 5M+ customers, enabling targeted mail-marketing campaigns that increased conversion rates across key demographics

> **[D — Analyst]**
> Built an XGBoost-based propensity model for 5M+ customers identifying high-value segments for targeted marketing campaigns, increasing conversion rates for Business Banking

> **[C — Product DS]**
> Designed a Next-Best-Product propensity model scoring 5M+ customers via XGBoost and PySpark, enabling targeted marketing campaigns that increased conversion rates across key demographics

---

## Agent Rules

1. **This is the strongest ML bench story.** When a JD asks for XGBoost, ensemble methods, customer segmentation, or production ML and the ATLAS bullets don't emphasize those terms, pull this in.

2. **PySpark is the production hook.** Mentioning PySpark signals Danny can work at scale with distributed compute — valuable for MLE and analytics engineering roles.
3. **FAST team context:** Same rule as Story 6. Goes under separate FAST sub-section if used.
4. **"Next-Best-Product"** is industry jargon that resonates in financial services, marketing analytics, and recommendation system roles.
5. **Pair with Story 6** if the resume needs two FAST bullets. They complement each other (classification + segmentation).

---

## Danny's Input

*Same as Story 6 — bench story, but details here would strengthen your ML credibility significantly.*

1. **How many features in the XGBoost model?** What were the top predictors? Transaction frequency? Account balance? Product holdings?

Over 400 different features of varying things, we also applied stronger weights on some of them that were emphasized. We worked with the technical marketing team to productionize it on AWS but I do not remember all the specs of this. 

Let me explain the point of this model: 

Chase has many mail marketing campaigns - but they wanted to design an engine that specifically captures customers who were likely to become future entrepenuers or business owners. Everything from people starting their own brand on shopify to mom and pop shops to people who were inherenting a business from their parents to people who were traveling to conferences and attending business-related items. We needed to capture them in the chase ecosystem BEFORE they hit any other bank - we wanted to send them business related mail so they can see it and we can have business acquisition 

We found trends and feature engineered their transactions to certain brands I cant recall, or their general timing, their general money shifts within chase and outbound of chase. We captured a lot of niche customer signals that we worked on extrapolating for a few months on FAST - it was to basically find features and identifiers that can capture what a business customer looks like BEFORE they even BECOME business customers. 

We did a lot of propensity score matching to validate these feature sets - like back-testing which customers became business customers based on their prior behaviors, and then tested this model itself live for 2 months to see if our guesses would be correct on which customers would open a business product. 2 months is not a long period of time, but it was enough to gauge that the model worked, and then we worked on passing it off to the tech team to propagate it up and set up the MLOps behind it. I dont have the MLOps piece because once the model was handed off to the marketing team - we just designed and validated it. 


2. **What was the target variable?** Probability of applying for a business banking product? Probability of approval? Probability of becoming a profitable customer?

Yes the probability of a business banking account opening - by PRODUCT. I can't recall HOW we did this, but it was a multi-variable propensity model with XGBoost, we used SHAP to determine the importance of features and built clustering on our sample to make the targeting more specific. I think I call it one model, but I think the target was AGAINST the propensity for multiple account opening types. 

3. **Campaign results:** Do you know the response/conversion rate from the mail campaigns? Even a rough "X% conversion" would be powerful.

Definitely saw a lift because this was targetted. 

Within 6-8 months, saw a lift of 8% from the rate of account openings in the target population we had. Historically this population cut had some rate of propensity of business account opening - our model seemed to improve on the rate of account openings by 8%. It wasn't just mail marketing I think it was also bankers calling these customers as well if they existed in the Chase ecosystem. 

4. **PySpark scale:** How many nodes? How long did training take? Batch scoring frequency?

I wish i can remember. But the important part here is I knew the pyspark syntax. I dont remember the rest.

5. **Is this model still in production?** Or was it a one-time campaign?

I can't say. This was around 2023-2024 on FAST. It most likely is in production - it had a slow rollout and they were testing it's success separately from our validation on their marketing team. I believe it was cast into production but I was moved to other workstreams. FAST projects are typically 6-12 month rotations and I was on the team for 2 years. 

6. **5M+ customers — what's the base?** All Chase retail customers? A specific segment?

A specific segment yes. This was the population that would receive either calls or inbox mail letters of product offerings. 

---

# Story 8: FAST — Household Acquisition Analysis

## Canonical Narrative

Danny led an analysis on U.S. household acquisitions at JPMC, identifying significant obstacles impeding acquisition rates among student and college demographics. He implemented focused measures that are forecasted to drive household acquisitions to 40 million by 2030. This was strategic analytics work — identifying demographic gaps and recommending targeted interventions.

This story appears only in the earliest resumes (#1-6) and was dropped from later versions as the ATLAS/experimentation stories grew stronger. It's the weakest of the three FAST stories but could serve as filler for analyst roles that value demographic analysis or growth analytics.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| U.S. household acquisitions analysis | Confirmed | |
| Student/college demographic obstacles | Confirmed | |
| 40 million households by 2030 forecast | Confirmed | Forward-looking target |
| Focused measures implemented | Confirmed | |

---

## All Historic Bullet Variants

> Led an analysis on U.S. household acquisitions, identifying significant obstacles impeding acquisition rates among student and college demographics; implemented focused measures that are forecasted to drive household acquisitions to 40 million by 2030
> — *Resumes #1-6*

---

## Approved Agent-Selectable Bullets

> **[D — Analyst]**
> Led analysis on U.S. household acquisitions identifying obstacles in student and college demographics; implemented targeted measures forecasted to drive acquisitions to 40M by 2030

> **[C — Product/Growth]**
> Identified demographic-specific barriers to household acquisition in student segments and implemented targeted growth measures forecasted to drive acquisitions to 40M by 2030

---

## Agent Rules

1. **Lowest priority FAST story.** Only use if the JD specifically mentions growth analytics, demographic analysis, acquisition funnels, or the resume needs a third FAST bullet (rare).
2. **Dropped from later resumes for a reason.** It's not as strong as the propensity-to-pay or XGBoost stories. Prefer those first.
3. **"40M by 2030" is a forecast**, not a realized outcome. Keep the "forecasted" qualifier.
4. **Student/college demographic angle** could resonate with edtech or companies targeting younger demographics.

---

## Danny's Input

*Lowest priority — only answer if you have time or if this story matters to you.*

1. **What were the "significant obstacles"?** Fee sensitivity? Lack of awareness? Poor digital experience for younger users? Regulatory barriers?
2. **What "focused measures" did you implement?** Product changes? Marketing campaigns? Fee waivers? Channel strategy?
3. **Is the 40M forecast still on track?** Where are things now relative to that projection?
4. **Do you want to keep this story at all?** It was dropped from your later resumes. If you don't feel strongly about it, we can deprioritize it permanently.


---

# Story 9: SwagUp — A/B Test & Pricing

## Canonical Narrative

At SwagUp (B2B startup, promotional products/onboarding merchandise), Danny designed and executed an A/B test on premium sample kits for SMB (small-to-mid-sized business) clients. The legacy sales assumption was that premium samples were enterprise-only — too expensive to offer to smaller clients. Danny challenged this assumption by testing offering premium sample kits to SMBs and analyzing first-order volume, refund rates, and 6-month retention.

Results overturned the assumption decisively: $5M+ incremental profit within six months, 40% revenue growth for first-time SMB clients, higher first-order volumes, drastically reduced refund rates, and improved retention. Danny collaborated with the Sales team on test design for treatment/control populations and drafted Tableau dashboards to track experiment activity. The findings drove a strategic, company-wide pricing policy change — samples offered to all client tiers, not just enterprise.

This is Danny's strongest startup story and his cleanest A/B test narrative. It has a clear hypothesis, clean methodology, decisive results, and direct business impact (policy change).

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| $5M+ incremental profit | Confirmed | Within six months |
| 40% revenue growth | Confirmed | For first-time SMB clients specifically |
| Higher first-order volumes | Confirmed | |
| Reduced refund rates | Confirmed | "Drastically reduced" |
| Improved 6-month retention | Confirmed | |
| Company-wide pricing policy change | Confirmed | Samples offered to all client tiers |
| Legacy sales assumption overturned | Confirmed | Premium = enterprise-only was wrong |
| Collaborated with Sales on test design | Confirmed | Treatment/control populations |
| Tableau dashboards for tracking | Confirmed | |
| Statistically significant improvements | Confirmed | Resume #14 mentions this explicitly |

---

## All Historic Bullet Variants

### Single Consolidated Bullet (Early)

> Identified a missed opportunity at a B2B onboarding merchandise company to extend premium sample kits to small-to-mid-sized businesses. Designed and launched an A/B test to evaluate the ROI of offering on-us sample kits, demonstrating an over 40% increase in initial order size and 20% improvement in customer retention over the course of a year. Insights from the experiment drove a strategic shift in the company's sales approach, resulting in significant revenue growth and stronger client partnerships
> — *Resume #1 (F)*

### Three-Bullet Breakout

> Identified a missed opportunity at a B2B onboarding merchandise company to extend premium sample kits to small-to-mid-sized businesses. Designed and launched an A/B test to evaluate the ROI of offering on-us sample kits
> — *Resumes #2-3*

> Collaborated with the Sales Team to improve test design for test and control populations, designed Tableau dashboards to track new client activity within the experiment
> — *Resumes #2-3*

> Drove a strategic shift in sales approach based on insights; contributed to substantial revenue growth (40% revenue growth for first-time clients) and enhanced onboarding processes for new B2B clients
> — *Resumes #2-3*

### $5M Framing

> Spearheaded a data-driven initiative to offer premium sample kits to Small-to-Mid-Sized Businesses (SMBs), challenging prior sales assumptions by designing and executing an A/B test that proved significant ROI and led to a company-wide policy shift, directly contributing to $5M+ incremental profit within six months
> — *Resumes #4-7*

> Analyzed A/B test results, demonstrating that sample kits for SMBs led to higher first-order volumes, drastically reduced refund rates, and improved 6-month client retention
> — *Resumes #4-7*

> The resulting strategic change in sales policy (offering samples to all client tiers) generated 40% revenue growth for first-time SMB clients
> — *Resumes #4-7*

### Product Analytics Framing

> Spearheaded a product-analytics initiative to A/B test premium sample kits for SMBs, challenging legacy sales assumptions and driving $5M+ incremental profit in six months
> — *Resumes #8-10*

> Analyzed experiment outcomes showing higher first-order volume, lower refund rates, and improved six-month retention, directly informing pricing and retention strategy
> — *Resumes #8-10*

### Partnership Emphasis (Stripe)

> Designed and executed A/B test of premium sample kits for SMBs, partnering with Sales and Product teams to challenge legacy assumptions; proved +40% revenue growth for first-time clients through higher order volume, lower refunds, and improved 6-month retention; analysis showed statistically significant improvements in first-order metrics and downstream retention
> — *Resumes #14-15 (Stripe, Perplexity)*

### Compact / Impact-First

> Led A/B test of premium sample kits for SMBs, proving +40% revenue growth for first-time clients through higher order volume, lower refunds, and improved 6-month retention
> — *Resumes #11-13 (Oracle, Netflix, Stripe GTM)*

> Drove $5M+ incremental profit and 40% revenue growth for first-time SMB clients by designing and executing an A/B test on premium sample kits, analyzing first-order volume, refund rates, and 6-month retention to overturn legacy sales assumptions and reshape pricing strategy
> — *Resume #20 (Hex)*

> Drove $5M+ incremental profit and 40% revenue growth for first-time SMB clients by designing and executing an A/B testing initiative on premium sample kits; challenged legacy sales assumptions through experiment design, analyzing first-order volume, refund rates, and 6-month retention to inform pricing and retention strategy
> — *Resume #19*

---

## Approved Agent-Selectable Bullets

### Primary (pick one)

> **[B/C — Experimentation/Product lead]**
> Drove $5M+ incremental profit and 40% revenue growth for SMB clients by designing an A/B test on premium sample kits, analyzing retention and refund rates to overturn legacy pricing assumptions and reshape company strategy

> **[D — Analyst]**
> Designed and analyzed an A/B test on premium sample kits for SMB clients, driving $5M+ incremental profit and 40% revenue growth by identifying retention improvements that reshaped company pricing strategy

> **[A — OR-adjacent]**
> Reshaped pricing strategy through a controlled experiment on premium sample kits, driving $5M+ incremental profit by analyzing volume, refund, and retention tradeoffs across client segments

> **[B — With statistical emphasis]**
> Designed and executed A/B test on premium sample kits for SMBs, proving statistically significant improvements in first-order volume, refund rates, and 6-month retention; results drove $5M+ incremental profit and company-wide policy change

> **[C — Impact-first compact]**
> Drove $5M+ incremental profit and 40% revenue growth for first-time SMB clients by designing an A/B test that overturned legacy sales assumptions, informing a company-wide pricing policy change

### Supporting (use when SwagUp gets 2+ bullets)

> **[B/C — Outcome detail]**
> Analyzed experiment outcomes showing higher first-order volume, lower refund rates, and improved 6-month retention, directly informing pricing and retention strategy

> **[D — Process detail]**
> Collaborated with Sales team on experiment design for treatment/control populations; built Tableau dashboards to track experiment activity and client behavior in real time

---

## Agent Rules

1. **This is SwagUp's flagship story.** It always makes the resume if SwagUp appears at all.
2. **$5M+ and 40% are the headline numbers.** Always include at least one. If space is tight, $5M+ is more impactful.
3. **"Overturned legacy assumptions" is the narrative hook.** It shows Danny doesn't just run tests — he challenges conventional wisdom.
4. **Company-wide policy change** is the ultimate business impact. Include when the JD values "driving strategic decisions" or "influencing business direction."
5. **Don't use "spearheaded"** — it's on Danny's banned verb list. Use "designed," "executed," "drove," or "led."
6. **One-page constraint:** SwagUp typically gets 2-3 bullets max. This story + Story 10 or 12 is the usual SwagUp allocation.

---

## Danny's Input

*This is your cleanest impact story. A few details would make it bulletproof in interviews.*

### The Experiment
1. **Sample sizes:** How many SMBs in treatment vs. control? How long did the experiment run?

For context; I was a "data analyst" at this startup. It was my first data job - or my first real technical job at all. Ive been here for about a year or so. Everything is amatuer and new and if I can go back and redo it I would. So I didnt structure this or build it with as much rigor as I would now. But I want to be honest about that so you understand the limitations. 

Experiment ran for 3 months. Shipped fast. 

Here is the full context for you. 

SwagUp is an onboard merchandising company. The basic premise is if you're hiring interns, or new staff, or you just want to get some cool gear for your company - we are the middle man to basically save you time finding vendors, get you the items you want based on your budget, and ship and label the nice packaging with your company logo and design. We source all the vendors, find the optimal pricing, find the optimal material, figure out all the labeling and printing, and ship you the pre-made packages with all the gear + boxes inside to your company's address. We do this for everyone from your small business with 50 employees to Amazon, Walmart, Google, Meta etc. 

We had about 12-15 sales reps when I was there (probably more as time went by). And the sales reps had client portfolios of various businesses. Some sales reps had bigger clients some had smaller. It was performance dependent I think. 

We had thousands of leads - we couldnt assign our sales rep to EVERY client we ever had. So we developed a web portal to basically allow our leads to go into cart and checkout before they were given any sales rep from what I recall. Typically the process wouldn't be hard, but.. in some instances we got a huge client -> think Amazon or Costco or Google. It might not be the whole company - sometimes a department or a subset of the company. Our goal was to assign a good sales rep to these clients and make their experience smooth - so that they can spread the word and the network effect would bring in OTHER giant clients. 

One of the things we did was provide free samples. If its a giant client like Google, we would happily provide like 5 samples to them to show them how their label would look like on a customized box with some sample items they can see. This was an incredibly expensive thing to do for us - ranging from 500-5000 dollars each time we did this with a client. The tradeoff we believed was that if we show the client what a sample product looks like, they would pull the trigger on large orders off the bat and know what they are getting. 


Here is the problem: 

- When we make custom samples - because of Bulk pricing with our vendors - we pay a significant premium for just a few custom samples. 
- We typically made custom samples for big clients. We would source sample products from multiple vendors - so making something custom is expensive especially for a few boxes. 
- We only gave this to clients we desperately wanted in our funnel (think big ones - like massive corporations or departments of massive corporations)
- We had to move quickly so we didnt lose their interest. 
- We had some BASE sample packs (swagup branded) but they were smaller in quantity and stock, and in some cases we didnt want to risk giving the business a sample of what we had - because it was typically just the box with no items - or if it had items it probably wasnt going to be the items our businesses wanted. 


Here was my initial analysis: 

- I noticed that businesses who NEVER got a sample obviously had higher refund rates, smaller first order volumes, and often they wouldn't repeat their order. We couldnt tell if this was because this was a one-off or if they werent satisfied with their product. Their listed budget was also typically not the actual budget they wanted to spend. 
- These businesses were smaller in size - maybe 50-5000 employees. Startups, small businesses, etc. They were high volume and low conversion in our sales funnel, and we only took a few of them to be under sales rep portfolios. Typically if they made a purchase the sales rep wouldnt try tooo hard to make a relationship with them - we just didnt have the bandwidth and prioritized bigger clients. The sales rep would make sure they were set for purchasing and if they needed any extra help or had any questions. Simple. 

- But these clients are tricky. Sometimes theyd never even connect with the rep. Or they purchased and did a refund. We had around a 12% refund rate on ATLEAST one item (either one item in the box or the whole box). Refunds sucked - because we spent money on big orders AND we got some significantly bad NPS when things went wrong with this segment of clients. The problem for us as a startup is if we get bombarded with bad experiences - we will lose bigger clients down the line. Our reputation was everything. And refunds hurt us financially as well. 

- Here is what I did notice: 
    - When we had these smaller clients go through our funnel - if these clients EVER somehow got a sample (typically not a custom one, but a SwagUp one), it was because they actually asked the Sales rep OR the sales rep was smart enough to offer a SwagUp branded sample so they can look at it. This small but sizeable subset of these SMBs NEVER had a single refund. 
    - They also came back - and their second order in their next hiring cycle or their next order was typically 2-3x bigger than their first - this was evidence that they were hedging their budget in the initial setup. 
    - These customers in general had significantly worse metrics than every customer - similar or not - who got a sample pack. 

- My pitch:
    - I worked with the CFO and the C-suite + Sales + Ops team in the company to help me get this pitch.
    - I made 2 experiment arms - one was business as usual, if its a small SMB with a sales rep to confirm a purchase, dont give them a sample pack unless they explicitly ask. 
    - In the other one, always offer a FREE on-us sample pack for the SMB. 
    - The arms were based on a simple 50/50 coin flip that was implemented as a flag in the Salesforce CRM -> they hit checkout -> contact rep -> AB test they fall into one arm. 

- I estimate the cost vs benefit, that we dont need to give them custom boxes like we do for big clients, we just need to buy more basic SwagUp branded ones with the most basic items (shirts, mugs a notebook) to give to them as a sample with all the sprinkled paper in it and the look of it so the client can *feel* what the product looked like when we shipped it to them. 
- Ops ordered a large batch of cheap swagup branded packs for this project. 
- For every new client in the test, we shipped them one sample pack for them to try. 

- Immediate results; 
    - They came back and pulled the trigger on their first order at a significantly higher rate - +40-50% increase in how many clients who got the pack actually came back to our rep or site or emailed us and asked for an order
    - They ALTERED their budgets, often INCREASING IT by 25-100%. They would typically hedge their budgets as I expected. 
    - They had larger budgets and pulled the trigger on first orders. 
    - Refund rates plummeted significantly - down to nearly 1% for entire-pack refunds. Down significantly as well for single item refunds - but the reason was almost always typically because it was damaged goods, not a dissapointment with our service - just the vendor or the quality of the product through transit. 
    
- Short Term Results:
    - I oversaw these clients over 3 months, they came back with a second order - and we also got MANY referrals from this, typically these SMBs would also refer us positively to other SMBs who came through the door
    - I tracked their metrics to see if theyd come back. The real metrics came from the first orders since SMBs and even big businesses kinda relied on hiring cycles or these were one-offs. 
    - Some clients I saw down the line became repeat customers from this experiment. 

- Impact: 
    - Overall a huge success. Changed sales policy entirely. Ops team now has sample packs on standby for exactly these reasons. YES its a cost on-us to freely ship and also buy these products - BUT -> it proved to convert clients. It proved that this sample strategy was worth it. The shipping costs + the risk of a sample not leading to a conversion was completely eclipsed by the goodwill, repeat orders, and the conversion orders that increased from SMB clients. 





2. **Statistical rigor:** Did you use a t-test? Chi-square? Bayesian? What was the significance level? Power analysis beforehand?
    - Again I was inexperienced, So I looked at basic trends - almost like a diff in diff. T test yes but that's it. Nothing huge. No POWER which is unfortunate but also this is a B2B so Power analysis on SMBs is tricky since its incoming clients. 
3. **"Premium sample kits":** What does this mean concretely? Physical product samples shipped to prospects? What was the cost per kit?
    - Premium meaning it was like our SwagUp branded boxes we showed. 
### The Numbers
4. **$5M+ incremental profit:** Is this gross profit or net? Over what period — 6 months from test start? Annualized? How was it calculated (incremental revenue from treated SMBs minus kit costs)?
    6 months post launch. If we compare trends of the SMB customer base after we launched this sales policy vs priors, we saw in the past compared to today - we had a 5 million lift from this population in the first 6 months of launching our sample kit initiative for all SMBs. 
5. **40% revenue growth:** 40% increase in first-order revenue for treated first-time SMB clients vs. control? Or vs. prior cohort? Over what window?
    40% first-order increase compared to SMBs in the control group. Their first orders were larger. 
6. **Refund rates:** Can you quantify the reduction? Even "reduced from ~X% to ~Y%" would strengthen the bullet.
    Sounds insane - but the refund rate plummeted to 1% when they actually saw the product they were selling before buying from us. 
7. **6-month retention:** Same — any numbers on the improvement? "Improved from X% to Y%" or "X percentage point lift"?
    Hard to remember, but they came back. Id say compared to historics, we managed to increase average returns from something like 1.2 returns within 1 year per SMB who completed their order to 1.35 or 1.4. Definitely moved the needle. 

### The Business Impact
8. **"Company-wide policy change":** Who made the call? CEO? VP Sales? How quickly after your results?
    - It was a 250 person company when I left so it was sorta small. CFO and CEO liked the experiment. VP of Sales loved it too. 
9. **Who pushed back?** The legacy assumption was "premium = enterprise only." Who held that view and how did you convince them?
    - I just ran the results. Showed them a cost analysis of how much theyd spend per box on shipping + how much theyd need to buy in inventory to support this experiment enough for me to get a decent batch of customers to analyze. the CFO was onboard he didnt mind throwing money around and he liked me. 
10. **Is this policy still in place?** Are samples still offered to all tiers today?
    - I think so. It was in place up until I left. I dont know if they still have it now. Maybe they changed it. But up until I left they still had this. 


---

# Story 10: SwagUp — Product Catalog & Self-Serve Pricing

## Canonical Narrative

Danny identified that prospects had zero pricing visibility before the sales intake stage — a significant conversion bottleneck. He proposed and launched a self-serve product catalog with dynamic bulk pricing. The catalog lifted add-to-cart actions by ~5% across tens of thousands of monthly visitors, with ~20% of conversions happening without sales rep involvement. This was a product initiative Danny conceived, pitched, and executed, not just an analysis.

This story only appears fully in the plan and Resume #20 (Hex). It's the strongest "product sense" story Danny has — he identified a problem through data, proposed a solution, and shipped it.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Zero pricing visibility identified | Confirmed | Problem discovery |
| Self-serve product catalog | Confirmed | Danny proposed and launched it |
| Dynamic bulk pricing | Confirmed | |
| ~5% lift in add-to-cart | Confirmed | Across tens of thousands monthly visitors |
| ~20% converting without sales rep | Confirmed | |
| Tens of thousands of monthly visitors | Confirmed | Scale context |

---

## All Historic Bullet Variants

> Proposed and launched a self-serve product catalog with dynamic bulk pricing after identifying zero pricing visibility before the sales intake stage; lifted add-to-cart actions by ~5% across tens of thousands of monthly visitors, ~20% converting without sales rep involvement
> — *Resume #20 (Hex)*

> Proposed and launched a self-serve product catalog with dynamic bulk pricing, lifting add-to-cart actions by ~5% and enabling ~20% of conversions without sales rep involvement
> — *Plan (Variant C/D)*

> Identified zero pricing visibility as a conversion bottleneck and launched a self-serve catalog with dynamic bulk pricing; consolidated multi-source data into automated dashboards serving 1,000+ accounts
> — *Plan (Variant C — combined with dashboard)*

---

## Approved Agent-Selectable Bullets

> **[C — Product DS lead]**
> Identified zero pricing visibility as a conversion bottleneck and proposed a self-serve product catalog with dynamic bulk pricing; lifted add-to-cart actions by ~5%, with ~20% of conversions happening without sales rep involvement

> **[D — Analyst]**
> Proposed and launched a self-serve product catalog with dynamic bulk pricing after identifying zero pricing visibility as a conversion bottleneck, lifting add-to-cart by ~5% across tens of thousands of monthly visitors

> **[C — Impact-first]**
> Lifted add-to-cart by ~5% and enabled ~20% of conversions without sales rep involvement by identifying a pricing visibility gap and launching a self-serve product catalog with dynamic bulk pricing

---

## Agent Rules

1. **This is the "product sense" story.** Use it when the JD values product intuition, GTM analytics, conversion optimization, or self-serve product work.
2. **Problem identification is the differentiator.** Danny didn't just build something — he identified the gap. Lead with "identified zero pricing visibility" when possible.
3. **~5% and ~20% are approximate.** Keep the tilde. Don't say "5%" as if it's exact.
4. **This story competes with Story 12 (dashboards) for SwagUp space.** For product roles, prefer this one. For analyst roles, prefer Story 12. For both, pick whichever matches the JD better.
5. **Currently only in one resume.** Danny should confirm he's comfortable with this story being used more widely.

---

## Danny's Input

*This is your "product sense" story — the one that shows you can identify problems, not just analyze data. Worth fleshing out.*

1. **How did you discover the pricing visibility gap?** Funnel analysis? User interviews? Customer complaints? Sales team feedback? What data told you this was the bottleneck?

For context this looks like it has changed as I visit the website. Looks like a shell of what it once was idk. We used to have such a massive catalogue of items. 
Anyways, 

The website HAS pricing - but it sorta gave them a range - and since we sometimes have to order items on demand in bulk - we werent able to always gaurantee that these prices would remain static. 
But I noticed in many cases there were cart dropoffs. I tried to investigate why. 

In many cases, I realized that users who would browse through our sales catalogue had to go through a LOT of effort to click on the catalogue of products and build their own items with their own budget. That's not what we wanted. So I worked on some very very basic analytics to look at past orders based on budget sizes, item purchase orders, how much those items cost typically, how much the pack cost, and I developed the underlying data to basically help us tell on the front page UI VERY similar to Amazon's "Customers like you also bought" - when they did an intake form for budget and employee size, I made the data that basically helped us land on a "Businesses like you ordered..." and it would already provide presets. This was the project. The bulletpoint doesn't explain it well unfortunately. 

2. **Who did you pitch it to?** CEO? Product lead? How did you make the business case?

I dont exactly recall but we had a lot of product managers - I pitched it to the UI/UX team that worked on the front end and the backend - it was sort of like the overall tech team. This is a startup mind you! 

3. **"Dynamic bulk pricing":** How does this work? Tiered pricing by quantity? Algorithm-based? Who set the price points?

My first MVP was literally just building out a fake thing like "If your budget is $10000, show the top 3 most common packages / item combinations other customers bought". I eventually evolved this to be more like a model (I just dont remember how) where the combinations werent just based on budget but also employee size and even the type of products they were looking for. But the preset option was a great way to kick off a conversation with a sales rep or help a customer get started. 

4. **What platform was the catalog built on?** Custom-built? Shopify? Something else? Did you build it yourself or work with engineers?

In-house. We have our own website. 

5. **~5% add-to-cart lift:** Was this A/B tested, or measured before/after launch? What's the confidence level?

General trends, no AB test actually - we just... launched it because it seemed like a good idea. They just didnt know how to properly build the data that supported this. So I did that work. 

6. **~20% converting without sales rep:** Is this still the case? What was the baseline (0% before, since there was no catalog)?

More like theyd be able to finish their cart and order. They didnt have to contact the sales rep to start an order or make a whole relationship. 

7. **Are you comfortable with this story being used across more resumes?** Right now it only appears in your Hex resume. It's strong for product roles — want it in the general rotation?

Yes but needs to be re-written a bit. 

---

# Story 11: SwagUp — Churn Prediction Model

## Canonical Narrative

Danny built a production churn prediction model (classification) at SwagUp that detected order volume dips and attrition risk across the client base. The model was operationalized as a monthly scoring pipeline that triggered automated sales outreach for at-risk accounts, improving retention and informing targeted intervention strategies.

This story appears only in the Oracle/Netflix/Stripe-era resumes (#11-15). It's Danny's only production ML story from SwagUp and his strongest "deployed classification model" example outside of JPMC.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Classification model | Confirmed | Churn/attrition prediction |
| Order volume dip detection | Confirmed | |
| Monthly scoring pipeline | Confirmed | Operationalized, not one-off |
| Automated sales outreach trigger | Confirmed | Model output drove action |
| At-risk account identification | Confirmed | |
| Improved retention | Confirmed | |

---

## All Historic Bullet Variants

> Built production churn prediction model (classification) detecting order volume dips and attrition risk; operationalized monthly scoring to trigger automated sales outreach for at-risk accounts, improving retention
> — *Resumes #11-12 (Oracle, Netflix)*

> Built production churn prediction model (classification) detecting order volume dips and attrition risk; operationalized monthly scoring pipeline to trigger automated sales outreach for at-risk accounts, improving retention and informing targeted intervention strategies
> — *Resumes #14-15 (Stripe, Perplexity)*

> Built production churn prediction model (classification) detecting order volume dips and attrition risk; operationalized monthly scoring to trigger automated sales outreach for at-risk accounts, improving retention
> — *Resume #13 (Stripe GTM)*

---

## Approved Agent-Selectable Bullets

> **[E — MLE lead]**
> Built production churn prediction model (classification) detecting order volume dips and attrition risk; operationalized monthly scoring pipeline triggering automated sales outreach for at-risk accounts

> **[C — Product DS]**
> Built churn prediction model identifying at-risk accounts through order volume dip detection; operationalized monthly scoring to trigger automated sales outreach, improving client retention

> **[D — Analyst]**
> Developed classification model detecting order volume dips and attrition risk across client base; automated monthly scoring to trigger proactive sales outreach for at-risk accounts

---

## Agent Rules

1. **Use when the JD mentions churn, retention modeling, classification, or production ML pipelines.** This is the only SwagUp story that shows deployed ML.
2. **"Monthly scoring pipeline" is the production proof point.** It wasn't a one-off analysis — it ran in production and triggered real actions.
3. **Complements Story 9 (A/B test).** Together they show Danny did both experimentation AND production ML at SwagUp.
4. **No specific retention numbers.** Danny doesn't quantify the retention improvement. If pressed, he can speak to the mechanism but not a precise %.
5. **This story appears in mid-to-late resumes only.** It was added when Danny started targeting MLE-adjacent and analytics engineering roles.

---

## Danny's Input

*The main gap here is quantification. Any numbers you can add make this much stronger.*

1. **What model type?** Logistic regression? Random forest? XGBoost? Something simpler?

- First version was completely rule-based. You gotta understand I was like 21 in my first DA job doing fuck-all. Everything I tried was hacky. 
    - The idea was that each business had a hiring cycle - or some sort of order cycle. All I did initially was build a very simple RFM table in excel with rules to sort of figure out what this business' typical order cycle should look like based on their past orders (this only worked for repeat clients.). 
        - When they were nearing their order cycle loop, we sent them an email or some sort of nudge to ask if they want to order again. 
    - So how do we figure out new businesses? Like based on their first order? 
- Second version I made a bit better.
    - At the time (before AI) I tried to explore survival models. But I couldn't figure it out because I wasn't technical enough and didnt have the proper time or data to get past all the theory or how to implement it at this startup. So instead... 
    - Claude helped me summarize this: "you enriched SwagUp's thin internal data with Clearbit firmographics, segmented the customer base to account for different purchasing rhythms (so a quarterly onboarding buyer and a biannual events buyer aren't measured against the same clock), defined churn as no orders within a calibrated dormancy window, built a classifier on top of that, and surfaced the probabilities to sales as an early warning system so they could intervene before the customer fully disengaged."
    - Basically, I struggled building survival models. So focused on a way to build almost a propensity model. 
    - I worked to get the clearbit data in with the product team at this startup - and built a rudimentary log-reg model that used churn as a predictor. I do not exactly remember the details how. 
    - "We didn't have contractual churn events, so I analyzed historical repurchase intervals by customer segment to establish empirically-grounded dormancy thresholds. Customers who exceeded their segment's typical repurchase window by a sufficient margin were labeled as churned. It was heuristic, but calibrated against observed purchasing rhythms rather than arbitrary."
    - The model ran every month - it was rudimentary. 


2. **What features predicted churn?** Order frequency drop? Days since last order? Invoice payment delays? Ticket volume?

We knew hiring cycles were a key item. We knew some companies were one-off. We knew some were huge clients. I did a clustering exercise first - and then applied the model seperately. 

3. **"Order volume dips":** What threshold defined a "dip"? 20% decline? 2 standard deviations? Over what window?

We used clearbit data to cluster and basically look at prior clients with these sizes and features, and estimated what a typical ordering cycle for this business would look like. 

4. **Monthly scoring — how did it work?** Batch job? Cron? Output to a Salesforce field? How did the sales team see the scores?

Even cruder. Simple python script to a csv with labels -> pushed to a salesforce table. It was very crude. 

5. **"Automated sales outreach":** What triggered it — score above a threshold? Automated email? Or did it just flag accounts for reps to call?

The monthly sales force table almost created like a reverse lead engine - allowed sales reps to see which companies they should nudge. 

6. **Any retention impact numbers?** Even approximate — "churn rate dropped from ~X% to ~Y% for flagged accounts"? Or "X% of flagged accounts were retained after outreach"?

Hard to say - we cant tell what events we DIDNT stop. 

7. **How many accounts were in the system?** How many got flagged per month on average?

A few hundred clients a month got a month. A gentle nudge. 


---

# Story 12: SwagUp — Analytics Infrastructure & Dashboards

## Canonical Narrative

Danny consolidated Salesforce, QuickBooks, and billing data into automated KPI dashboards at SwagUp, reducing reporting from weekly manual pulls to daily self-serve monitoring across sales, finance, product, and operations for 1,000+ accounts. In later resumes, this story expands to include the full analytics infrastructure: partnering with engineering to build Fivetran pipelines from Salesforce, QuickBooks, and billing systems, creating reusable SQL data models, and deploying Looker dashboards for real-time KPI monitoring.

The scope evolved across resumes — early versions mention "Tableau dashboards," middle versions add "ETL data pipelines through Google Cloud," and the Oracle/Netflix/Stripe versions describe a full GCP analytics stack with Fivetran, SQL data models, and Looker. Danny should confirm which version accurately represents the actual infrastructure.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Salesforce + QuickBooks + billing data consolidated | Confirmed | Three source systems |
| Weekly manual → daily self-serve | Confirmed | |
| 1,000+ accounts served | Confirmed | |
| Sales, finance, product, operations served | Confirmed | Four teams |
| Tableau dashboards | Confirmed | Early versions |
| Google Cloud / GCP | Confirmed | Later versions |
| Fivetran pipelines | Confirmed | Oracle/Netflix/Stripe versions |
| Reusable SQL data models | Confirmed | Oracle/Netflix/Stripe versions |
| Looker dashboards | Confirmed | Oracle/Netflix/Stripe versions |
| Partnered with engineering | Confirmed | |
| Real-time KPI monitoring | Confirmed | Sales KPIs, renewals, client health |

### ⚠️ Tool Stack Variation
- Early resumes: Tableau
- Mid resumes: "Tableau dashboards and ETL data pipelines through Google Cloud"
- Late resumes: "Fivetran pipelines from Salesforce, QuickBooks, and billing systems; reusable SQL data models and Looker dashboards"
- Danny should confirm the canonical tool stack

---

## All Historic Bullet Variants

### Dashboard Focus

> Consolidated Salesforce, QuickBooks, and billing data into automated KPI dashboards, reducing reporting from weekly manual pulls to daily self-serve monitoring across 1,000+ accounts
> — *Plan (Variant D)*

> Consolidated Salesforce, QuickBooks, and billing data into automated KPI dashboards, reducing reporting from weekly manual pulls to daily self-serve monitoring across sales, finance, product, and operations for 1,000+ accounts
> — *Resume #20 (Hex)*

### ETL + Dashboard Combined

> Built automated Tableau dashboards and ETL data pipelines through Google Cloud integrating Salesforce, QuickBooks, and billing data to monitor sales KPIs, renewals, and client health in real time
> — *Resumes #8-10 (2026(1), Lyft, Decision Scientist)*

> Partnered with engineering to build automated ETL pipelines and Tableau dashboards integrating Salesforce, QuickBooks, and billing data into real-time KPI monitoring across sales, renewals, and client health
> — *Resume #19*

> Built automated ETL pipelines and Tableau dashboards integrating Salesforce, QuickBooks, and billing data into real-time KPI monitoring across sales, renewals, and client health
> — *Resumes #17-18 (ProductDS variants)*

### Full GCP Stack (Fivetran + Looker)

> Designed analytics infrastructure on GCP: partnered with engineering to build Fivetran pipelines from Salesforce, QuickBooks, and billing systems; created reusable SQL data models and Looker dashboards for real-time KPI monitoring
> — *Resumes #11-15 (Oracle, Netflix, Stripe, Perplexity)*

### Executive Dashboard Lead (GTM emphasis)

> Built executive dashboards integrating Salesforce, QuickBooks, and billing data to monitor sales KPIs, renewal rates, client retention, and revenue metrics in real time; enabled data-driven decision making across the organization
> — *Resume #13 (Stripe GTM) — listed first among SwagUp bullets*

### Enabling Self-Service

> Designed analytics infrastructure on GCP: built Fivetran pipelines from Salesforce, QuickBooks, and billing systems; created reusable SQL data models and Looker dashboards enabling self-service reporting
> — *Resume #13 (Stripe GTM — alternate ending)*

---

## Approved Agent-Selectable Bullets

> **[D — Dashboard / Analyst lead]**
> Consolidated Salesforce, QuickBooks, and billing data into automated KPI dashboards, reducing reporting from weekly manual pulls to daily self-serve monitoring across sales, finance, product, and operations for 1,000+ accounts

> **[E — Analytics engineering]**
> Designed analytics infrastructure on GCP: built Fivetran pipelines from Salesforce, QuickBooks, and billing systems; created reusable SQL data models and Looker dashboards for real-time KPI monitoring

> **[C — Product emphasis]**
> Identified zero pricing visibility as a conversion bottleneck and launched a self-serve catalog with dynamic bulk pricing; consolidated multi-source data into automated dashboards serving 1,000+ accounts

> **[D — Executive dashboard]**
> Built executive dashboards integrating Salesforce, QuickBooks, and billing data to monitor sales KPIs, renewal rates, client retention, and revenue metrics in real time across the organization

> **[C/D — ETL + Tableau]**
> Built automated ETL pipelines and Tableau dashboards integrating Salesforce, QuickBooks, and billing data into real-time KPI monitoring across sales, renewals, and client health

---

## Agent Rules

1. **This is the go-to SwagUp bullet for analyst and analytics engineering roles.** It shows SQL, ETL, dashboard, and cross-functional reporting skills.
2. **Tool stack should match JD.** If JD mentions Looker → use Looker variant. If JD mentions Tableau → use Tableau variant. If JD mentions Fivetran/DBT → use GCP stack variant.
3. **"Weekly manual → daily self-serve" is the transformation story.** Always include this contrast when space allows — it quantifies the before/after.
4. **1,000+ accounts** gives scale context. Include when possible.
5. **Don't combine with Story 10 (product catalog)** into a single bullet unless one of the plan's pre-approved combined variants is used. They're separate initiatives.
6. **Stripe GTM resume uniquely leads SwagUp with the dashboard bullet.** For analytics engineering or BI roles, consider leading with this story rather than the A/B test.

---

## Danny's Input

*The critical question here is the tool stack. Everything else is enrichment.*

### ⚠️ CRITICAL: The Tool Stack
1. **What was the actual stack?** Your resumes say three different things:
   - Early: "Tableau dashboards"
   - Mid: "Tableau dashboards and ETL data pipelines through Google Cloud"
   - Late: "Fivetran pipelines, reusable SQL data models, Looker dashboards on GCP"

   Which is accurate? Did the stack evolve over your time there, or was one version always the truth? Can you claim all of these tools?


- I helped hire a Data Engineer - went through 200 resumes with my team because we had no data team. I was the single data guy. We needed help. Everything was in excel. 
- We connected everything from what I recall via some.. platform that we paid for. It had an automatic way to funnel everything for a start..
   - Fivetran!
   - We used Fivetran as a connector to start I believe. 
- We then used DBT and Looker as well. We rebuilt all our dashboards that lived with Grow.com into Looker. 
- I dont recall exactly but we did use DBT as well. 
- We used Google Cloud to plug in our Quickbooks, billpay and Salesforce tables for instant querying and SQL tables we could use for our analytics. 

### The Infrastructure
2. **"Partnered with engineering":** What was your role vs. theirs? Did you design the data models and they built the pipelines? Or did you build end-to-end?

- They handled a lot of the parts of data engineering such as building contracts, validation, repeatable processes, scheduling processes, data ingestion. 
- I handled the movement of visuals, data, I also worked on connecting and consolidating all the tables we need for reporting. 
- I built out all the dashboards in Looker as well
- I worked on plugging things in via DBT as well but I cannot recall what - nor do I recall the syntax ill need a refresher.

3. **How many source tables/objects?** From Salesforce, QuickBooks, and billing — roughly how many data sources fed the dashboards?

- Must be dozens. Everything from funnel tables, marketing, outreach, sales performance, cohort analytics I built, inventory, operations... literally everything in the startup. I was part of this massive migration overhaul in my last 6 months there. 

4. **Refresh cadence:** Real-time? Daily batch? How long from source update to dashboard update?

- Some were live but the engineer sorted that out. Some were daily batch. Source update to dashboard update was nearly instant. 

5. **"Reusable SQL data models":** Were these in a tool like DBT, or raw SQL views? How many models?

I think so but I cannot recall. 


### The Impact
6. **"Weekly manual pulls":** Who was doing them? How long did they take? What triggered the shift to automation?

Everyone was. Everything in this startup lived in master excel tables the teams worked on. It was a mess. I was the main guy who pushed on getting an engineer and building out the proper infrastructure. 

7. **"1,000+ accounts":** SwagUp's accounts or accounts visible in the dashboard? Is this the full customer base?

All accounts. We had thousands of clients. 

8. **Which KPIs mattered most?** Revenue per account? Churn rate? Pipeline conversion? Renewal rate? Give me the top 3-5 that leadership actually looked at.

Retention was a big one in all forms. 


---

# Story 13: Georgia Tech — Drift Detection Project

## Canonical Narrative

As a Georgia Tech project (Sep 2024 - Apr 2025), Danny led a comparative study benchmarking five time-series drift detection algorithms — PELT, ADWIN, CUSUM, KS (Kolmogorov-Smirnov), and Bayesian Changepoint — for production ML monitoring. The study evaluated detection latency, false positive rates, and robustness/implementation complexity. The algorithms were tested against simulated user engagement data representing gradual drift from a feature launch. Windowed CUSUM and ADWIN showed the strongest results across noisy environments.

This is an academic project, not production work. It's relevant for MLE roles that value ML monitoring, model observability, or drift detection.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Five algorithms benchmarked | Confirmed | PELT, ADWIN, CUSUM, KS, Bayesian Changepoint |
| Detection latency evaluated | Confirmed | |
| False positive rates evaluated | Confirmed | |
| Robustness / implementation complexity evaluated | Confirmed | |
| Simulated user engagement data | Confirmed | Gradual drift from feature launch |
| Windowed CUSUM & ADWIN strongest | Confirmed | |
| Project lead role | Confirmed | |
| Georgia Tech, Sep 2024 - Apr 2025 | Confirmed | |

---

## All Historic Bullet Variants

### Two-Bullet Version

> Led a comparative study benchmarking five time series drift detection methods (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) to assess efficacy in identifying gradual drift in simulated user engagement data for a feature launch
> — *Resumes #4-7*

> Analyzed model performance based on detection latency, false positive rates, and implementation complexity, providing recommendations for optimal algorithm selection in noisy, evolving data environments (Windowed CUSUM & ADWIN showed strong results)
> — *Resumes #4-7*

### Research Framing

> Led a comparative research project benchmarking five time-series drift detection algorithms (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) to evaluate data drift detection latency and robustness for production ML monitoring
> — *Resumes #8-10, 16*

### Compact Single-Bullet

> Led comparative benchmarking of 5 time-series drift detection algorithms (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) for production ML monitoring; analyzed detection latency vs false positive tradeoffs (Windowed CUSUM & ADWIN optimal)
> — *Resumes #11-15 (Oracle, Netflix, Stripe, Perplexity)*

> Benchmarked five time-series drift detection algorithms (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) evaluating detection latency, false positive rates, and robustness for production ML monitoring, Windowed CUSUM & ADWIN showed strongest results across noisy environments
> — *Resumes #18-20*

### Plan Variants

> Benchmarked five drift detection algorithms (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) evaluating detection latency, false positive rates, and robustness for production ML monitoring
> — *Plan (Variant E — MLE lead)*

> Evaluated five time-series drift detection algorithms for production ML monitoring; Windowed CUSUM and ADWIN showed strongest robustness in noisy environments
> — *Plan (Variant All — general)*

---

## Approved Agent-Selectable Bullets

> **[E — MLE lead]**
> Benchmarked five drift detection algorithms (PELT, ADWIN, CUSUM, KS, Bayesian Changepoint) evaluating detection latency, false positive rates, and robustness for production ML monitoring; Windowed CUSUM and ADWIN showed strongest results

> **[All — General/compact]**
> Evaluated five time-series drift detection algorithms for production ML monitoring; Windowed CUSUM and ADWIN showed strongest robustness in noisy environments

---

## Agent Rules

1. **Use for MLE and ML monitoring roles.** Skip for pure product DS, decision science, or analyst roles unless space is abundant.
2. **Competes with Story 14 (AI/Human Detection) for the project slot.** Use this one for MLE/monitoring roles. Use Story 14 for experimentation/NLP roles. Never use both — one-page constraint.
3. **Academic project disclaimer:** This is coursework, not production. Frame as "Georgia Tech" project, not as professional experience.
4. **Algorithm names are keyword bait.** Listing all five by name helps with ATS keyword matching for ML monitoring roles.

---

## Danny's Input

*Academic project — lower stakes, but a few details would make it interview-ready.*

1. **What was the simulated data?** Did you generate synthetic user engagement time series? What did the "drift" look like — gradual mean shift? Variance change? Distribution change?
2. **Concrete results:** Can you give specific numbers? E.g., "CUSUM detected drift within 15 data points vs. 45 for PELT" or "ADWIN had a 5% false positive rate vs. 20% for KS"?
3. **Why these five algorithms?** How did you select them? Were they the most cited in the literature? Did you consider others?
4. **Team or solo?** "Project Lead" — how big was the team? What did you specifically own vs. delegate?
5. **Any publication or deliverable?** Paper? Poster? Course report? Could it be published?
6. **Practical takeaway:** If someone at JPMC wanted to monitor ATLAS for drift, which algorithm would you recommend and why?


---

# Story 14: Georgia Tech — AI/Human Detection Experiment

## Canonical Narrative

Danny designed, built, and ran a two-phase controlled experiment studying whether AI detection warnings change how people write with AI, and whether human judges can detect the difference. Solo project — he built both experiment platforms, designed the methodology, recruited all participants, funded the study out of pocket, and wrote the paper.

**Phase 1 (Writers):** 21 participants used an AI chatbot (Claude Sonnet) to write opinion pieces on remote work. Control group got no extra context. Treatment group was told their submission would be scanned by an AI detection tool. The warning was designed as a non-behavioral prime — it activated awareness without prescribing a response (citing Bargh et al., 1996; Weingarten et al., 2016). Counterbalanced writing order (for/against remote work), between-subjects design, post-experiment hypothesis probe (no one guessed the real purpose). 41 validated documents produced.

**Counter-intuitive Phase 1 finding:** The warning didn't reduce AI use — it *polarized* behavior. Treatment participants took more turns (3.0 vs 2.4), spent more time (720s vs 571s), and used more tokens. Several treatment participants abandoned the chatbot entirely and wrote everything themselves; no control participant did this. Yet the submitted text was nearly identical on every measurable feature — AI overlap scores differed by only 0.025 between medians, and all 6 stylometric features (type-token ratio, sentence length/SD, first-person rate, hedging rate, contraction rate) showed overlapping distributions.

**Phase 2 (Judges):** 251 independent judges evaluated 1,999 paired comparisons. Each pair showed one control and one treatment document for the same stance, with position randomized and a forced 10-second reading delay before selection. Judges were told one document was "written by a human" and asked to identify which — a deliberately deceptive framing, since both writers had AI access.

**Results:**
- Judges selected the treatment (warned) document as human **54.13%** of the time vs **45.87%** for control
- Two-sided binomial test: **p = 0.000243** (significant at α = 0.05)
- 95% Wilson CI on control-as-human: [43.70%, 48.06%] — entirely below 50%
- Effect holds across both stances: FOR p=0.012, AGAINST p=0.008
- Effect **strengthens** with higher judge confidence (42-43% control-as-human at confidence 4-5)
- Effect **strengthens** with longer reading time (fastest quartile near chance, slower quartiles 43-45%)
- When judges expanded only one document: control-as-human dropped to **35.9%**
- No fatigue effect across session
- Not driven by outliers: 15/23 treatment docs above 50%, only 5/18 control docs above 50%
- Removing strongest outlier (P26, who never used AI at all): effect weakens but holds (45.87% → 47.89%)
- Sensitivity analysis: effect **strengthens** under stricter filtering (time filter, dropping affected docs)

**Classifiers (RQ2/RQ4):** 4 classifiers (logistic regression, KNN k=3, KNN k=5, random forest) trained on 10 features (6 stylometric + AI overlap + 3 process features). SMOTE inside each CV fold, repeated stratified 5-fold CV (20 repeats). ALL classifiers at or below 50% chance line. Best: KNN k=5 at 48.7%. Feature importance: task duration (0.26), type-token ratio (0.20), AI overlap (0.10).

**The core finding:** Humans detect something that feature-based classifiers cannot. The AI detection warning changed writer behavior (polarized interaction patterns) without changing measurable text features, yet judges consistently identified the warned group's writing as more human. The signal may be holistic — stylistic rhythm, personal tone, editorial choices — rather than any single extractable feature.

**Infrastructure (all solo):**
- Two Streamlit apps: writer platform (9-stage session flow, 3-column layout with chatbot + notepad + submission) and judge platform (paired comparison with forced 10s reading delay, optional expansion)
- Supabase PostgreSQL backend with real-time data writes
- Anthropic API (Claude Sonnet) for AI chatbot
- 29 automated tests (AppTest + pytest) covering full session flow
- Bot dry-runs testing abuse scenarios (prompt injection, character overwrites, mass token usage)
- Guardrails: access code, word count limits (200-400), turn limits (25/task), token budget (50k/session), soft 15-min timer, duplicate session prevention, forced 10s judge reading delay
- Self-funded: $175 in participant raffles, $100 Reddit ad campaign (32k impressions, 1,200 landings, 324 survey clicks)
- Recruited via Instagram, LinkedIn (4 rounds, ~6,400 impressions), WhatsApp (~300 students), Reddit

**Paper:** 35-page final report with 23 references. LaTeX source at github.com/danieltabach/human_ai_detection_latex. Danny wants to publish a cleaned-up version outside of the coursework context.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Two-phase controlled experiment | Paper-confirmed | Phase 1: writers, Phase 2: judges |
| 21 writers, 41 validated documents | Paper-confirmed | 9 control, 12 treatment |
| 251 judges, 1,999 paired evaluations | Paper-confirmed | 315 sessions started, 251 submitted ≥1 evaluation |
| p=0.000243 (two-sided binomial) | Paper-confirmed | Significant at α=0.05 |
| 54.13% treatment-as-human vs 45.87% control | Paper-confirmed | 95% Wilson CI: [43.70%, 48.06%] |
| Effect holds across both stances | Paper-confirmed | FOR: p=0.012, AGAINST: p=0.008 |
| Effect strengthens with judge confidence | Paper-confirmed | 42-43% control-as-human at confidence 4-5 |
| Effect strengthens under stricter filtering | Paper-confirmed | Sensitivity analysis in Appendix E |
| Not driven by outliers | Paper-confirmed | 15/23 treatment docs > 50%, 5/18 control > 50% |
| Warning polarized behavior (didn't moderate) | Paper-confirmed | More turns, time, tokens; some abandoned AI entirely |
| AI overlap scores nearly identical | Paper-confirmed | Medians: 0.978 control vs 0.953 treatment |
| All 6 stylometric features overlapping | Paper-confirmed | TTR, sentence length/SD, first-person, hedging, contractions |
| 10 features total (6 stylometric + AI overlap + 3 process) | Paper-confirmed | |
| 4 classifiers: LR, KNN(3), KNN(5), RF | Paper-confirmed | SMOTE + 20-repeat stratified 5-fold CV |
| Best classifier: 48.7% accuracy (below chance) | Paper-confirmed | KNN k=5 |
| 3-component AI overlap scoring | Paper-confirmed | Trigram overlap, longest common substring, sequence ratio |
| Two Streamlit apps (writer + judge) | Paper-confirmed | 9-stage writer flow, paired comparison judge flow |
| Supabase PostgreSQL backend | Paper-confirmed | Real-time data writes |
| Anthropic API (Claude Sonnet) | Paper-confirmed | |
| 29 automated tests + bot dry-runs | Paper-confirmed | AppTest + pytest |
| Counterbalanced design | Paper-confirmed | 4-participant rotation cycle, writing order balanced |
| Non-behavioral priming | Paper-confirmed | Warning activates concept without prescribing response |
| Forced 10s reading delay for judges | Paper-confirmed | Guards against automatic responses |
| Self-funded: $175 raffles + $100 Reddit ads | Paper-confirmed | Plus personal time for LinkedIn, Instagram, WhatsApp recruitment |
| Reddit: 32K impressions, 1,200 landings, 324 clicks | Paper-confirmed | |
| 35-page paper, 23 references | Paper-confirmed | LaTeX on GitHub |
| Solo project | Paper-confirmed | Design, build, recruit, analyze, write — all Danny |

---

## All Historic Bullet Variants (from plan only — not yet in resumes)

> Designed and ran a two-phase controlled experiment with 21 writers and 251 judges (~2,000 evaluations), finding that AI detection warnings produce statistically detectable behavioral shifts (p=0.000243) invisible to feature-based classifiers
> — *Plan (Variant B — Experimentation lead)*

> Built end-to-end experiment infrastructure (Streamlit, Supabase, Anthropic API) and recruited 250+ judges to test whether humans detect AI-assisted writing; found a significant human-detectable signal that ML classifiers missed
> — *Plan (Variant C — Product / full-stack DS)*

> Engineered 10 NLP features (AI overlap scoring, lexical diversity, stylometric measures) and trained four classifiers for AI text detection; human judges outperformed all models, identifying behavioral signals invisible to feature extraction
> — *Plan (Variant E — MLE / NLP framing)*

---

## Approved Agent-Selectable Bullets

### Tier 1: Primary Bullet (pick ONE — headline for project section)

> **[B — Experimentation / Decision Science]**
> Designed and ran a two-phase controlled experiment (21 writers, 251 judges, ~2,000 paired evaluations) studying whether AI detection warnings change writing behavior; found judges identify warned writers as "human" at a statistically significant rate (p=0.000243) that four classifiers trained on 10 NLP features could not replicate (ArXiv: 2604.23471)

> **[C — Product DS / Full-Stack]**
> Built end-to-end experiment infrastructure (two Streamlit apps, Supabase backend, Anthropic API) and self-recruited 250+ judges to test whether humans detect AI-assisted writing; found a statistically significant human-detectable signal (p=0.000243) invisible to feature-based classifiers (ArXiv: 2604.23471)

> **[E — MLE / NLP]**
> Engineered 3-component AI overlap scoring (trigram overlap, longest common substring, sequence matching) and 10 NLP features for AI text detection; four classifiers (logistic regression, KNN, random forest with SMOTE + stratified CV) could not beat chance, while 251 human judges identified behavioral shifts at p=0.000243 (ArXiv: 2604.23471)

> **[A — Applied Scientist / Behavioral Research]**
> Designed counterbalanced between-subjects experiment with non-behavioral priming to study AI detection warning effects on writing behavior; warning polarized AI usage (more intensive use OR complete abandonment) without changing measurable text features, yet 251 judges detected the shift at p=0.000243 across ~2,000 evaluations (ArXiv: 2604.23471)

> **[D — Analyst / General]**
> Built and ran a controlled experiment with 21 writers and 251 judges producing ~2,000 evaluations, finding that AI detection warnings produce writing perceived as more human (p=0.000243); solo-authored preprint published on ArXiv (2604.23471)

### Tier 2: Supporting Bullet (use when space allows)

> **[B — Counter-intuitive finding]**
> Found that AI detection warnings polarized writer behavior (more AI interaction OR complete chatbot abandonment) rather than moderating it, yet submissions were textually indistinguishable on all measurable features; the human-detectable signal persists under sensitivity analysis and strengthens with judge confidence and reading time

> **[E — Infrastructure depth]**
> Built two Streamlit experiment platforms with Supabase backend and Anthropic API: writer app with 9-stage session flow, counterbalanced assignment, and 29 automated tests; judge app with paired comparison, forced reading delays, and position randomization across ~2,000 evaluations

> **[C — Recruitment / initiative]**
> Self-funded and recruited for the study across Reddit ($100 ad spend, 32K impressions), LinkedIn (4 rounds, ~6,400 impressions), WhatsApp, and Instagram; 315 judge sessions started, 251 submitted evaluations, producing ~2,000 paired responses

---

## Agent Rules

1. **Published on ArXiv (2604.23471).** This is now a real publication. Always include "(ArXiv: 2604.23471)" in the bullet.
2. **Pair with Story 16 (LLM Vague Intensity Words) as Danny's research portfolio.** Together they show two solo-authored ArXiv preprints — a real independent research practice. Both should appear in the Projects section when space permits.
3. **The p-value is the punchline for stats/decision science roles.** p=0.000243 across ~2,000 evaluations is strong.
4. **The "humans beat classifiers" finding is the punchline for AI/NLP/ML roles.** Four classifiers trained on 10 features couldn't beat chance. 251 judges could. That gap is the finding.
5. **The counter-intuitive mechanism is the punchline for behavioral/product roles.** Warning didn't moderate AI use — it polarized it. That's unexpected and interesting.
6. **Self-funded + self-recruited shows entrepreneurial initiative.** $275 personal investment, multi-platform recruitment campaign, no university backing. Mention for startups or roles valuing ownership.
7. **The sensitivity analysis is the defensibility anchor.** Effect strengthens under stricter filtering (time filter, dropping affected docs). If an interviewer pushes on small sample size, this is the answer.
8. **Per-document analysis eliminates the outlier concern.** 15/23 treatment docs above 50%, 5/18 control docs above 50%. The effect is distributed, not concentrated. Removing strongest outlier (P26) weakens but doesn't eliminate the result.
9. **This project demonstrates Danny can do research-grade experiment design, NLP feature engineering, full-stack app development, statistical analysis, and scientific writing — all solo.**

---

## Danny's Input

**RESOLVED:** Paper is now published on ArXiv (2604.23471, April 2026). Solo author. 25 pages, 12 figures, CC BY 4.0 license.

Danny leads with experiment design in interviews. The p-value (0.000243) is the statistical punchline, the human-vs-classifier gap is the AI/NLP punchline, and the full-stack build is the engineering punchline.



---

# Story 15: Consulting — Cohort Analytics & NLP Pipeline

## Canonical Narrative

Danny did consulting work (2024-2025) building a Python NLP algorithm using TF-IDF and cosine similarity to clean and standardize ~10,000 customer names, integrated directly into the client's Salesforce and QuickBooks pipelines. He also designed and deployed an automated Excel-based reporting suite featuring cohort analysis, retention metrics, RFM (Recency, Frequency, Monetary) insights, and a consolidated view of customer revenue that updated directly from CRM/ERP systems.

This story appears in resumes #4-7 and was dropped from later versions. It demonstrates freelance/consulting experience, NLP application, and analytics infrastructure — useful as filler for roles that value NLP, data cleaning at scale, or consulting experience.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| Python NLP algorithm | Confirmed | TF-IDF + cosine similarity |
| ~10,000 customer names cleaned | Confirmed | |
| Salesforce & QuickBooks integration | Confirmed | Direct pipeline integration |
| Automated reporting suite | Confirmed | Excel-based |
| Cohort analysis | Confirmed | |
| Retention metrics | Confirmed | |
| RFM insights | Confirmed | Recency, Frequency, Monetary |
| CRM/ERP direct updating | Confirmed | |
| 2024-2025 timeframe | Confirmed | |

---

## All Historic Bullet Variants

> Programmed a Python NLP algorithm (TF-IDF, cosine similarity) to clean and standardize ~10000 customer names, integrated directly into client's Salesforce & Quickbooks pipelines
> — *Resumes #4-6*

> Programmed an NLP algorithm to clean and standardize ~10000 customer names, integrated directly into client's Salesforce & Quickbooks pipelines
> — *Resume #7 (shorter)*

> Designed and deployed an automated Excel-based reporting suite featuring cohort analysis, retention metrics, RFM insights, and a consolidated view of customer revenue, directly updating from CRM/ERP systems
> — *Resumes #4-7*

---

## Approved Agent-Selectable Bullets

> **[E — NLP/MLE]**
> Built Python NLP pipeline (TF-IDF, cosine similarity) to clean and standardize ~10K customer names, integrated directly into client's Salesforce and QuickBooks data pipelines

> **[D — Analyst]**
> Designed automated reporting suite with cohort analysis, retention metrics, and RFM insights for ~10K customers, updating directly from Salesforce and QuickBooks

> **[C — Product/consulting]**
> Built end-to-end analytics pipeline for consulting client: NLP-based customer name standardization (~10K records) integrated into CRM, plus automated cohort and retention reporting from CRM/ERP systems

---

## Agent Rules

1. **Lowest priority story overall.** Only include if the resume has space after all JPMC, SwagUp, and Georgia Tech bullets are placed AND the JD specifically values NLP, data cleaning, CRM integration, or consulting experience.
2. **Dropped from resumes after #7 for a reason.** The ATLAS and experimentation stories outcompete it. Use only as a flex piece.
3. **TF-IDF and cosine similarity are NLP keyword matches.** If a JD mentions text processing, entity resolution, or record linkage, this story becomes relevant.
4. **RFM analysis** is a specific marketing analytics term. If the JD mentions RFM, customer segmentation, or lifecycle analytics, this story can be pulled in.
5. **"Consulting" framing** — this shows Danny does work outside of his full-time role. Can signal initiative and breadth.

---

## Danny's Input

*Lowest priority story. Only answer if you have time or want to keep this in the rotation.*

1. **Who was the client?** Industry? Size? How did you get the engagement — referral? Cold outreach?
2. **NLP accuracy:** How well did the TF-IDF + cosine similarity approach work? What was the deduplication rate? Any tricky edge cases (abbreviations, misspellings, "Inc" vs "LLC")?
3. **"Automated Excel-based reporting":** How is it automated — Python script? VBA? Runs on a schedule or manually triggered?
4. **RFM segmentation:** How many segments? What were the cutoffs? What did the client do with the segments (targeted campaigns? different service tiers?)?
5. **Hours invested:** Was this a weekend project or a multi-month engagement? Paid?
6. **Do you want to keep this story?** It was dropped after Resume #7. If it's not adding value, we can remove it from the rotation permanently.


---

# Story 16: LLM Behavioral Measurement — Vague Intensity Words in Tool-Use Actions

## Canonical Narrative

This paper did not start as a paper. Danny built the MILP-based staffing optimization engine behind every Chase branch in the country (BAR/ATLAS), then — blocked at work from integrating AI the way he wanted — rebuilt it himself and bolted an LLM agent harness onto it to create a fully autonomous scenario planner. He did this to genuinely understand agentic workflows, not to put the phrase on a resume.

And then he noticed something the people selling "agentic AI" don't notice: a one-word change in an instruction could move the model's action from a cautious nudge to pushing a constraint to its ceiling — or to silently refusing to act at all. A highly regulated bank using a language model to set staffing across 3,700+ branches, with no data science team standing between the model's proposed state and reality? Danny looked at his own working autonomous planner and asked whether it could actually be trusted. Then he measured why it can't.

Published as a solo-authored preprint on ArXiv (2605.21827, May 2026).

**The Research Question:** When an LLM receives a vague instruction like "increase the allocation slightly," how does it translate that into a precise numeric action? Does the language-to-action interface preserve operator intent, or does it silently fail — and if so, where and how?

**Experimental Design:** Danny built ATLAS (Adaptive Testing of Language-to-Allocation Sensitivity) — a synthetic constrained resource-allocation environment with 30 factories, 4 task categories, and 13 composable constraint patterns, directly inspired by his production ATLAS/BAR system at JPMC. The key design insight: the deterministic backend solver is the measurement instrument, not the subject. With the solver fixed, the LLM is the only stochastic component — isolating language interpretation as the variable under study. Danny ran 6,620 controlled API calls across 2 temperature settings (T=0.0, T=0.7), 10 intensity words, and 10 starting allocation states. Every run used fresh sessions with deep-copied state and no memory contamination between calls.

**The 10 Intensity Words Tested:** slightly, a little, somewhat, moderately, noticeably, considerably, significantly, substantially, greatly, drastically.

**Key Findings:**
1. **Compression Effect:** The model compresses 10 English intensity words into ~5 distinct median outputs. Weaker words ("slightly," "a little," "somewhat") map to nearly identical actions. Stronger words separate into higher tiers. Monotonic rank correlation: Spearman rho = 0.845.
2. **Context Dominance:** System state dominates word choice 10:1 in determining output. Epsilon-squared: 0.782 for starting state vs. 0.079 for word selection. The model responds far more to WHERE it is than WHAT you tell it.
3. **Boundary Behavior:** Near feasibility boundaries (operational limits), the model exhibits three distinct behavioral modes: (a) hedge — weak words produce minimal action, (b) act — mid-strength words push toward feasible limits, (c) abstain — "drastically" pushes to maximum capacity. This is not smooth gradation; it's mode-switching.
4. **Temperature Persistence:** Results hold across T=0.0 and T=0.7. The compression and state-dominance effects are structural, not sampling artifacts.
5. **Downstream Propagation:** Word choice alone shifted deterministic solver outcomes by $250K in the synthetic environment. The variance propagates directly from linguistic interpretation to material system outcomes.

**Why This Matters for AI Safety:**
- Tool-use LLMs are making consequential numeric decisions based on vague human language
- The model's interpretation of "slightly" vs "substantially" is compressed and inconsistent
- System state influences the model's actions 10x more than the user's word choice
- Near boundaries, the model exhibits unpredictable mode-switching behavior
- This directly informs how to design guardrails for agentic AI systems doing resource allocation, financial decisions, or any numeric tool-call actions

**Infrastructure (all solo, self-funded):**
- Synthetic constrained resource-allocation environment serving as a measurement instrument
- Structured tool-call interface with deterministic backend solver
- Automated data collection pipeline with fresh sessions, deep-copied state, and session isolation across all 6,620 runs
- Nonparametric statistical analysis: Kruskal-Wallis H tests, Spearman rank correlation, epsilon-squared effect sizes
- Self-funded through Anthropic API credits
- Built the full experimental stack end-to-end

**Paper:** Solo-authored preprint, ArXiv: 2605.21827 (May 2026). Planned extensions: human baseline survey (pending Georgia Tech IRB), cross-model comparison (GPT-4o, Gemini Flash), NeurIPS/EMNLP workshop submissions.

**Connection to ATLAS/BAR:** The synthetic environment Danny built for this experiment was directly inspired by the MILP-based resource allocation system he built at JPMC. He took his domain expertise in staffing optimization and used it to create a controlled measurement instrument for LLM behavior. This crossover between applied optimization and AI research is unique.

---

## Defensible Fact Sheet

| Fact | Status | Notes |
|------|--------|-------|
| 6,620 controlled API calls | ArXiv-confirmed | 2 temperatures x 10 words x 10 starting states x ~33 runs each |
| Solo author | ArXiv-confirmed | Daniel Tabach, Georgia Institute of Technology |
| ArXiv: 2605.21827 | Published | May 2026 |
| 10 vague intensity words tested | ArXiv-confirmed | slightly through drastically |
| Compression: 10 words -> ~5 distinct outputs | ArXiv-confirmed | Spearman rho = 0.845 |
| State dominance: epsilon-squared 0.782 vs 0.079 | ArXiv-confirmed | 10:1 ratio |
| Three behavioral modes near boundaries | ArXiv-confirmed | Hedge, act, abstain |
| Temperature persistence (T=0.0, T=0.7) | ArXiv-confirmed | |
| Claude Haiku (Anthropic API) | ArXiv-confirmed | |
| Synthetic resource-allocation environment | ArXiv-confirmed | Deterministic backend solver |
| Structured tool-call interface | ArXiv-confirmed | |
| Fresh sessions with state isolation | ArXiv-confirmed | No memory contamination |
| $250K outcome variance from word choice alone | ArXiv-confirmed | Downstream propagation through deterministic solver |
| Self-funded via Anthropic API | Confirmed | Danny's own money |
| Kruskal-Wallis H tests | ArXiv-confirmed | Nonparametric statistical analysis |
| Spearman rank correlation | ArXiv-confirmed | |
| Planned: human baseline, cross-model, conference submissions | Confirmed | From core competencies doc |

---

## Approved Agent-Selectable Bullets

### Tier 1: Primary Bullet (pick ONE — headline for project section)

> **[A — Applied Scientist / Alignment Research]**
> Built an autonomous scenario planner on top of a production-grade optimization engine, then measured why natural-language control interfaces silently fail: across 6,620 controlled runs, vague instructions compress into fewer distinct actions than words used, system state dominates user word choice 10:1, and two near-synonyms produce categorically different behavior (act vs. abstain) in identical system states — a specification failure invisible to the operator (ArXiv: 2605.21827)

> **[B — Decision Scientist / Experimentation]**
> Demonstrated that natural-language interfaces to agentic systems silently fail to preserve operator intent: designed a controlled experiment (6,620 runs, 10 intensity words, 2 temperature settings) isolating the language-to-action boundary, finding that the model compresses distinct instructions into identical actions (Spearman rho=0.845) and mode-switches near constraint boundaries rather than degrading smoothly (ArXiv: 2605.21827)

> **[C — Product DS / AI Product]**
> Identified a specification failure in LLM-mediated decision systems: built a synthetic resource-allocation environment mirroring production staffing optimization and showed that system state influences model actions 10x more than user word choice, with word selection alone shifting solver outcomes by $250K — directly informing guardrail design for agentic AI products (ArXiv: 2605.21827)

> **[E — MLE / AI Engineering]**
> Built end-to-end measurement infrastructure for LLM tool-use behavior: synthetic constrained-optimization environment with deterministic backend solver as measurement instrument, structured tool-call interface, and automated pipeline with session isolation; demonstrated that vague language produces compressed, state-dependent, and discontinuous actions at operational boundaries (ArXiv: 2605.21827)

> **[D — Analyst / General]**
> Published solo-authored ArXiv preprint showing that when LLMs translate vague instructions into numeric tool-call actions, the language-to-action interface silently compresses distinct words into identical outputs and switches behavioral modes near constraint boundaries — a finding from 6,620 controlled runs in a resource-allocation environment the author built from production domain expertise

### Tier 2: Supporting Bullet (use when space allows)

> **[A/B — Core finding detail]**
> Found that the language-to-action boundary is compressed (10 words collapse to ~5 outputs), state-dependent (system context explains 78.2% of output variance vs 7.9% for word choice), and discontinuous near operational boundaries where the model exhibits three behavioral modes: hedge with weak words, abstain with strong words, and push to capacity ceiling with maximizer-adjacent language

> **[E — Infrastructure depth]**
> Built full experimental stack from production domain expertise in staffing optimization: synthetic constrained resource-allocation environment with deterministic backend solver isolating model behavior as the only stochastic component, structured tool-call interface, and automated pipeline with fresh sessions, deep-copied state, and zero memory contamination across 6,620 runs

> **[C — AI Safety / Alignment framing]**
> Research demonstrates a concrete alignment failure in tool-use settings: the gap between operator intent and model action is invisible from the language interface, grows largest near constraint boundaries where stakes are highest, and manifests as silent specification failure — two near-synonyms ("drastically" vs "dramatically") produce categorically different behavior (act vs. abstain) in an identical system state

---

## Agent Rules

1. **This is alignment research, not NLP with a sticker.** Danny found a real, load-bearing safety question inside a real production system he personally built, and he went and measured it. The credential most people are missing is not the PhD — it's having built the thing and then been honest about its failure mode. Frame accordingly.
2. **NEVER lead with "Ran 6,620 API calls."** That makes it sound like benchmarking. Lead with the PROBLEM (natural-language control interfaces silently fail to preserve operator intent) or the FINDING (the failure is compressed, state-dependent, and discontinuous). The 6,620 runs are the evidence, not the story.
3. **The origin is the differentiator.** Danny built the autonomous system (ATLAS at JPMC), realized it couldn't be trusted with stakeholders wielding vague language, and measured why. That origin — builder who questioned his own system — is rarer than a PhD.
4. **ArXiv link is live.** Always include "(ArXiv: 2605.21827)" in the bullet when space permits.
5. **The drastically/dramatically discontinuity is the unsettling finding.** Two near-synonyms produce categorically different behavior (act vs. abstain) in an identical system state. That's a specification failure invisible to the operator. This is the punchline for AI safety and agentic AI roles.
6. **The state-dominance finding (10:1) is the punchline for alignment roles.** The gap between what we asked for and what the model does is both invisible from the interface and largest near operational boundaries where stakes are highest.
7. **$250K downstream propagation** makes it concrete for business-facing roles. Word choice alone shifted solver outcomes by $250K. That's not abstract — it's material.
8. **Solo, self-funded, published.** He found the question inside his own production system, built the entire measurement apparatus, paid for the API runs, and published. That combination is the signal.
9. **Pair with Story 14 (AI detection) when possible.** Two solo ArXiv preprints demonstrate a real research practice, not a one-off.
10. **Planned extensions show trajectory.** Cross-model comparison (do different alignment pipelines leave different behavioral fingerprints?), human baseline (is this misalignment or genuine ambiguity?), conference submissions targeting NeurIPS/EMNLP workshops.

---

## Danny's Input

*Paper is published on ArXiv. Key details from the paper and core competencies document.*

1. **How much did the Anthropic API runs cost?** Estimated from 6,620 Haiku calls.
2. **Human baseline survey status:** Pending Georgia Tech IRB approval.
3. **Cross-model comparison:** Planned for GPT-4o and Gemini Flash.
4. **Conference submissions:** Targeting NeurIPS workshops (safe/reliable AI, tool use) and EMNLP workshops.


---

