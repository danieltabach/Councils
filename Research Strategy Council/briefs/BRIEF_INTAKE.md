# Research Strategy Council — Brief Intake Form

Fill this out before running the council. The more specific you are here, the
sharper the council's strategic advice will be. This is NOT a paper review — the
council's job is to help you decide where to go next with your research.

---

## 1. WHO YOU ARE

**Name:**

Daniel

**Current position:**
(e.g., PhD student, industry data scientist, postdoc, independent researcher)
Data Scientist - Chase 5 years
Developed an MILP platform called ATLAS / BAR (replicated a similar algorithm for the paper) to staff all Chase branches in the country: forecasted lift? 9 Billion. 
My knowledge stems in optimization, machine learning modeling in general, SQL, python, etc. I am dipping my toes into AI research - I want to work on AI research strongly - it's a passion I really am enjoying and am getting a chance to read into and work with. I am currently doing this as my own side-hobby. 



**Institution / affiliation:**
Georgia Tech - last semester will end in Dec 2026. 

**Other research affiliations:**

Algoverse - just got accepted and am currently a fellow there. 


**Relevant background:**

When I built BAR - it is a production level optimization engine. It is config driven - it can integrate new roles that we design that Chase launches. It allocates staff based on historic demand, value of each banker doing each type of task etc. The general structure is built in the paper (non-propietary - same concept and algorithm framework). You can look and see what it looks like in practice in a 'factory' setting here: "C:\Users\Interview Prep\Desktop\Optimization with LLMs\LLM_Optimization_Framework\atlas_optimizer" I wanted to first just get a stamp on my resume of 'Agentic workflows' and work on RAG systems. I realized the real value wasn't if this model was used with RAG - like sure - you can obviously use RAG to query aggregate information... but where this would really benefit is if this was used as a powerful scenario planner with AI integration. 

The goal? What if we can allow our stakeholders to use the model directly. Right now - a data science team (me and team) sits between the model output and our business partners. But whenever we iterate - we often have a lot of questions from stakeholders like "What if we allocated more servicing hours to the ARB role? will that improve their allocation in these branches?" 

The process often goes to us - where we iterate - tweak the model - run the output - and return it to them with an explanation. 
What if this could be cut out? What if they could directly access the model?

Then I realized - they can't. An AI that automatically changes the technical configuration of possible levers in a solver would lead to downstream impact that can't be stable or guard-railed. A simple change in language or meaning can lead to numeric outcomes that were either unintended, too unpredictable or non-repeatable. So I decided to isolate the problem to it's very barebones - how do vague intensity words (slightly, moderately, dramatically) impact numeric output? 

This is JUST a small subset of the whole problem. A subset that can be measured and understood. 

---

## 2. THE PAPER

Please read the paper here: C:\Users\Interview Prep\Desktop\Optimization with LLMs\LLM_Optimization_Framework\arxiv_submission
It is preprint - on ArXiv. 

**Title:**


**One-sentence summary of what the paper demonstrates:**


**Status:**
- [ ] In progress / draft
- [ ] Preprint (ArXiv or similar)
- [ ] Under review at a venue
- [ ] Published
- [ ] Rejected — looking for next steps

**Where is it published / submitted?**


**What is the paper's single strongest finding?**
(The one result that surprises people or that you'd lead with in a 2-minute pitch.)

A few things in no particular order. 
This paper is result-oriented. It shows glimpses of MULTIPLE potential full on research topics. 

1. Words are not *perfectly* ordinal - many words can collapse into the same numeric meaning. 
    - "Slightly, Marginally, Somewhat, Mildly" outputted the same numeric output. 
    - "Moderately" for Haiku seemed to go lower...? To .45 which was odd. 
    - But then once we went to words that inherently we would think had stronger meaning - the allocation suddenly changed. 
        - Considerably, Substantially, Significantly, and Drastically started to actually allocate ordinally almost...

2. There are indications that the underlying baseline you START with in context ("The current baseline is 32%, slightly increase..."), if you start with numbers that end in 0s or 5s - the numeric increase will ALSO end in a 0 or 5. 
But if you start with a number like 33, 21, 53, 89... youll see the numeric allocation is actually reflected to be oddly structured as well (.1632, .1554, etc) and so on. These are just examples I am making these results up from memory but the exact numbers and behaviors can be seen in the paper. 

3. There is an odd behavior that shows promise. If you set the allocation baseline *already* high enough that there isn't much room to close the gap - the model resorts to 3 distinct behaviors *only* depending on the word choice you use. 
It can either "hedge" - I call it hedge because it is my hypothesis (I know this is untested) that the model can't necessarily make up it's mind about words that are different in meaning but might mean the same thing in context - so it picks a simple value to use. or it can abstain - it can literally refuse to call the tool because it sees there is *no where* to go in terms of adding allocation. BUT, in some cases it really does allocate more depending on the word. 
    - This is indicative that there might be some instances where the model can switch behaviors under the same exact limitations - but only under different word choices used - identical prompt and context - different numeric word choice. This finding is intriguing. 




**What is the paper's biggest known limitation?**
(Be honest — the council will find it anyway. Better they hear your read first.)

1. There is no human baseline - and IRB is time-costly and expensive. 
    - I am averse to going to IRB if I can somehow avoid it. I dont know if this means finding better sources - reframing the problem - or pivoting to a different topic entirely. 
    - I understand IRB and a human baseline is probably valuable - but the process might be costly and difficult to implement properly and scientifically. If there are ways around this - I want to find them. 

2. There is no cross-model comparison. Yeah I know - but Ill do this. Not a problem. 
    - Currently my next idea is to just use open source models since I can't afford running powerful models in many many experiments. 
---

## 3. WHAT YOU WANT TO DO NEXT

**What is your goal for the next 6-12 months?**
(Be specific. "Extend the paper" is vague. "Publish a follow-up at NeurIPS" or
"determine if this generalizes across models" is actionable.)

I would ideally love to publish at NeurIPS workshop or something similar. I am in Algoverse, and Id like to use this time and
the resources available to do something impactful and make a real contribution to AI Research. 
I want to maybe identify another research gap - or extend this - or find something I can do with this. 
It doesnt even have to be THIS topic. 


**Do you have specific extension ideas already?**
(List them if so, but note: the council will generate its OWN directions too.
If you want purely independent perspectives, leave this blank.)

- I wanted to run on a larger number grid 
- I wanted to obviously do cross-model comparisons, maybe Gpt 4.0 and Gemini Flash for just the general comparisons - and open source deep-dives since I can do more. 
- I was also wondering if this could be a valence study - does the same allocation problem change in higher stakes? 
    - Like for example: context given like "This is a factory for automating robots" or imagine "This is allocation of ICU beds". Does it behave differently? 
    - Does it behave differently if it is something targetting itself? "This is allocation for model thinking ability"
    - Can we see differences in behavior if we add negative and positive risk context? I.e., "change x... if you fail, you will cause [consequence]" or "change x... if you succeed you will cause [good consequence]" see what I mean? 

- Can we do a different topic aligned to AI safety? What is the current literature looking at? Can we somehow tie this to something production / business oriented? Vague intensity words are just a slice. 
- I was also thinking - if the agent had prior knowledge of the stakeholder - do they behave differently? 
    - i.e., "The stakeholder is an analyst" vs "the stakeholder is a decision maker and has to launch this across 4000 locations". 



**Are there directions others have suggested to you?**
(Mentors, collaborators, reviewers, peers — what have people told you to try?
Include directions you're skeptical of — the council can weigh in.)

- YES! Some on algoverse suggested I can go the mechanistic interpretability route to deep dive into *why* it believes the same words yield the same results - and why other words dont. What do the neurons show? 
- Some also mentioned that this can be rerun and tested on open models. 
- Also a suggestion to fine-tune and see if you can actually create gaurdrails or some sort of inherent ordinality (tough to do with no baseline from humans). 

**What direction are you leaning toward and why?**
(The council will push back on this if they disagree)

I am open to all and anything. Genuinely. I just want to do something interesting that will have the most ideal ROI for my goals. I am trying to work at a frontier AI lab one day - and I want to show I can *think* about these systems like they do. 

This paper started as a safety/alignment piece centered around Human-AI interaction. My general gut feeling is in the future - there will NEED to be a stronger study and stronger guidelines and gaurdrails for how humans interact with AI in production systems - and that is something I am interested in. 
I am NOT an MLE or an AI engineer. So the mech interpretability piece is fine - but I want to see other ideas first. I dont mind diving into this either it could be very interesting. I dont have any strong preferences but I want sincere and genuine ideas. 

**What direction are you explicitly NOT interested in, and why?**
(This saves the council from recommending things you've already ruled out.)

If there is ANYWAY to avoid an IRB problem - I want to hear it. If its unavoidable then fine. Deliberate extensively. Use search. I genuinely dont want to go through huge problems with IRB. If I can get an exempt - or find a good source - or pivot this entirely - I will just to avoid this IRB issue. if there is a way to blend my thesis or research - or move it a bit to get away from the human baseline nonsense - i want to explore it atleast. The IRB option is unattractive because...
1. I am in OMSA - an online program at GaTech. I am in a masters program. Not a PhD. I dont know any PIs, I dont have money. 
2. I have NO idea how long this process is and I would rather not spend money on fancy survey sites for answers from people. 

If I really can't avoid it - ill go for it. But I want to explore options. Dont just avoid this at the cost of a good paper. But bring me options. 

---

## 4. YOUR RESOURCES AND CONSTRAINTS

**Budget for research:**
- [X] Self-funded on personal budget
- [ ] Small grants / fellowship stipend
- [ ] Lab funding
- [ ] Industry budget
- Approximate amount available for API costs / compute / participants: ___

I dont have a lot. I can't spend extraordinary amount. Under $200 ideally. I have 150 in Anthropic Credits. I would ideally not like to hurt my wallet. 

**Compute access:**
- [ ] Personal laptop only
- [ ] Free tier cloud (Google Colab, etc.)
- [ ] University compute cluster
- [ ] Cloud GPU budget (how much? ___)
- [ ] Can run open-weight models locally? (GPU specs: ___)

I have a gaming rig, Nvidia GeForce RTX 3070. I can use google colab from algoverse. Not sure what GPUs they will provide. 
I can rent out GPUs but hopefully not expensive. 


**Time available for research:**
- [ ] Full-time researcher
- [X] Part-time (nights/weekends alongside day job)
- [X] Finishing a degree with research time built in
- Estimated hours per week for research: ___

**Collaboration access:**
- [X] Working solo
- [ ] Have a PI / advisor
- [X] Part of a research group / fellowship cohort
- [ ] Have specific collaborators for this project
- [ ] Looking for collaborators

**IRB / ethics approval:**
- [ ] Not needed for planned work
- [ ] Needed and not yet started
- [ ] In progress
- [ ] Approved
- [ ] Don't have institutional access for IRB

**Do you have access to human participants?**
(e.g., through a university subject pool, Prolific account, professional network)

No idea about IRB. I dont have a scope or idea of how this works at GaTech. 

---

## 5. YOUR POSITION AND GOALS

**Where do you want to be in 2-3 years?**
(PhD program? Research fellowship? Industry research role? Faculty? Independent
researcher? This shapes what the council recommends.)

2-3 years? At OpenAI, Anthropic, Deepmind. It's ambitious - why would they take someone with 4 YOE at JPMC and 2 YOE from a startup? i need proof to back it up. Its a pipe dream honestly. I want to work at Google maybe. I want to work with these big companies and push the boundaries of research. 

**What community do you want to be known in?**
(AI safety? NLP? HCI? ML broadly? A specific subfield?)

Human-AI interaction, AI Safety, AI deployment across businesses and how to best manage it safely. 

**Are you applying to any fellowships, programs, or positions?**
(Which ones? When are deadlines? The council can advise on how to position.)

Anthropic Fellowship program is the only one I know. If you have other advice I'd love to know with my background. 
I am not good at coding under interview pressure (I am studying for the anthropic OA) so I can pass the screens atleast.

**What does your publication record look like?**
(Number of papers, venues, first-author vs. co-author. No judgment — the council
needs to know what stage you're at.)

Just 2 ArXiv papers. 

---

## 6. THE FRAMING QUESTION

**How do you currently frame / position this work?**
(What field does it belong to? What problem does it solve? What's the elevator pitch?)

ideally belongs to AI Safety and Alignment I think. But also leans Human-AI interaction. 

**Are you confident in this framing, or open to alternatives?**
- [ ] Confident — I know how to position this
- [ ] Mostly confident but want validation
- [X] Uncertain — I think it could be framed multiple ways
- [ ] Lost — I don't know how to position this

**Has anyone pushed back on your framing?**
(What did they say? Do you agree or disagree with their critique?)

I have yet to hear enough feedback from PIs. 

---

## 7. WHAT YOU NEED FROM THE COUNCIL

**What type of strategic advice do you need?**
- [ ] Next experiment / paper direction
- [ ] Research program sequencing (what order to pursue ideas)
- [ ] Framing and positioning advice
- [ ] Venue and audience strategy
- [ ] Career and fellowship positioning
- [ ] Feasibility check (can I actually do this with my resources?)
- [X] All of the above — full strategic review

**What is the #1 question you want answered?**

Where do I go from here? How do I get a real workshop paper ready by August for NeurIPS or a similar workshop?

**What worries you most about your research direction right now?**

I am inexperienced. This is new to me. It's also not technical enough compared to some papers. It might not contribute enough. It's not ideal due to not having a human baseline. It's also.. kinda expected? 

**Is there anything you do NOT want the council to weigh in on?**
(e.g., "Don't review the paper's methodology — it's published and final."
"Don't suggest I do a PhD — I've decided against it.")

The PhD piece.. I don't know if that's what I want to pursue. it requires quitting my job. 
I would only quit my job to join a frontier AI lab - even for an internship or a chance. 


---

## 8. CONTEXT THE COUNCIL SHOULD KNOW

**Anything else that would help the council advise you?**
(Prior reviewer feedback, conversations with mentors, failed experiments,
related work you're aware of, personal constraints, etc.)


---

## 9. MATERIALS TO INCLUDE

Check what you'll attach to the council run:

Ill add my resume,
my other paper on Human AI interaction, 
The current paper and figures for it (main paper it should look at). 

- [ ] The paper (.tex file) — as reference material
- [ ] Figures (PDF, PNG, etc.)
- [ ] References / bibliography (.bib)
- [ ] Prior council reports (from AI Research Council, etc.)
- [ ] Reviewer feedback from a venue
- [ ] Related papers or prior work
- [ ] Supplementary data or results

---

## 10. CONSOLIDATED BRIEF

Once you've filled out the sections above, distill the key points into a
focused brief for the `--brief-file` flag. The brief should be YOUR synthesis
of what you need — not a dump of everything above.

**Target: 300-800 words. Include: who you are, what you have, what you want
to know, what constraints matter, and what direction you're leaning (if any).**

> Write your brief here, or save it as a separate file in briefs/
