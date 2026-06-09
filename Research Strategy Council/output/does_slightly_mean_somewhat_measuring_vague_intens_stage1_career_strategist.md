# Career Strategist — stage1

# Career Strategy Review: Danny Tabach

---

## Honest Position Assessment

**Where you actually stand:**

You are a non-traditional researcher with a stronger profile than you probably believe and more significant gaps than you're comfortable admitting. Let me be precise about both.

**What's working in your favor:**

Your profile has a coherent story that most early-stage researchers lack. You built a production system, noticed a real failure mode in it, designed a controlled experiment to measure that failure mode, and produced a preprint with clean empirical results. That origin story — practitioner-to-researcher, motivated by a real deployment problem — is genuinely differentiated. Most alignment researchers come from ML or philosophy backgrounds and theorize about deployment problems they've never encountered. You've encountered one. That's not nothing.

The Algoverse fellowship is real signal. It's selective, it has a track record of mentoring researchers to top venues, and it gives you something most independent researchers lack: a named institutional affiliation, access to PIs, and a collaborative infrastructure. When a fellowship committee looks at your CV, "AI Safety Research Fellow at Algoverse" reads better than "independent researcher." Don't underestimate this.

Your JPMorgan work is also real signal, but it's double-edged. It demonstrates you can build systems that matter at scale. It also raises the question in an academic committee's mind: *is this person a researcher or a practitioner writing papers?* The answer to that question is not yet settled by your profile.

**The gaps — stated directly:**

One preprint is not a research trajectory. It's a starting point. Fellowship committees funding research programs want to see evidence that you can sustain a research direction across multiple papers, not just execute one well-designed study. You don't have that yet. This is your most significant gap, and it's the one you can actually close in the next 12 months.

Your paper is single-model, single-domain, single-action-direction. These are acknowledged limitations, but they matter more than you may realize for how the work is received. The findings are real, but their generalizability is genuinely unknown. A reviewer who wants to dismiss the work can do so by pointing at Claude Haiku and a synthetic allocation environment. Your next paper needs to make that dismissal harder.

You have no co-authors, no citations from others, and no evidence of engagement from the community you're trying to enter. The paper is on ArXiv but has not yet been tested by peer review or community response. You don't yet know if the people whose opinion matters think this work is interesting. That's information you need.

Your master's is finishing, which is both an asset (you'll have the credential) and a transition risk (you'll lose your Georgia Tech affiliation unless you're careful about timing). Plan for this.

---

## What You Cannot Do Alone

Be honest with yourself about which parts of the planned program require things you don't have:

**The human baseline survey requires IRB approval.** You acknowledge this in the paper. This is not a minor procedural step — IRB review at Georgia Tech takes time, requires proper protocol design, and must be completed while you still have institutional affiliation. If you're finishing your master's in the near term, the window for doing this under Georgia Tech's IRB may be shorter than you think. This is the single most time-sensitive dependency in your entire research program. Miss this window and the human comparison study either gets delayed by years or requires finding a new institutional sponsor.

**Cross-model comparison requires API budget you may not have.** Running the same 6,620-run protocol on GPT-4o, Gemini Flash, and other frontier models multiplies your API costs by the number of models. This is manageable but not free. Budget this explicitly before committing to it as the next study.

**Mechanistic interpretability requires compute and expertise you don't have.** If you pursue the mechanistic interp direction — looking inside the model to understand why compression happens — you need either GPU access for activation analysis or collaboration with someone who has it. You cannot do serious mechanistic work on API calls alone. This isn't a direction you can pursue solo with your current resources. This is the honest answer to your question about whether to pursue it.

**Getting the work into a peer-reviewed venue requires navigating a process you haven't navigated yet.** ArXiv is not publication. The gap between a preprint and a workshop paper, and between a workshop paper and a full venue paper, is real. Algoverse mentors can help here, but you need to actively use them for this.

**Building a "recognized voice" requires community engagement you haven't started.** Visibility doesn't happen from ArXiv alone. It requires showing up — at workshops, on forums, in conversations. This takes time that competes with research time.

---

## Fellowship Strategy

**Which fellowships are realistic targets:**

Given your profile — master's finishing, one preprint, Algoverse fellowship, industry background — the realistic near-term targets are:

*Strong fits:*
- **Open Philanthropy AI Fellowship / LTFF grants** — These fund independent and non-traditional researchers explicitly. Your practitioner background is a feature, not a bug, for funders who care about deployment-facing safety research. The framing of your work as deployment safety rather than theoretical alignment is well-suited here.
- **Anthropic's academic programs** — You're studying their model. This is not a coincidence you should ignore. Anthropic has expressed interest in deployment safety research. A well-framed application that builds on the Claude Haiku findings and proposes cross-model extension is a natural fit.
- **MATS (ML Alignment Theory Scholars)** — Selective but accessible to non-traditional researchers with demonstrated research output. One preprint may be sufficient if the application is strong.
- **Redwood Research / ARC** — Less structured fellowship programs but open to researchers with empirical deployment safety work.

*Stretch targets that become realistic with a second paper:*
- NSF Graduate Research Fellowship (if you're still a student — check eligibility carefully given master's completion timeline)
- Any fellowship requiring demonstrated research trajectory rather than a single paper

**What fellowship applications need to demonstrate:**

Fellowship committees funding deployment safety research want to see three things you currently have in partial form:

1. **A coherent research question that matters.** You have this. The language-to-action interface question is real, deployment-relevant, and understudied. Don't let narrative inflation obscure it — the question is good enough without overselling it.

2. **Evidence you can execute.** You have one paper. You need two. The second paper doesn't need to be published before you apply — it needs to be in progress, described concretely, and plausibly completable.

3. **A reason to bet on you specifically.** This is where your practitioner background matters. You're not competing with PhD students on theoretical depth. You're competing on the claim that deployment safety research done by someone who has actually deployed systems will ask different questions and produce more practically relevant findings. Make that case explicitly.

**How to frame the application:**

Do not frame this as "I am studying vague intensity words in LLMs." Frame it as: "I am building a measurement framework for language-to-action translation failures in deployed AI systems, motivated by a real production failure I encountered, and I have initial empirical evidence that these failures are systematic, state-dependent, and invisible to operators." That's a research program. The first is a paper.

---

## Path to "Recognized Voice"

**What actually works for someone in your position:**

The path to being a recognized voice in deployment safety is not the same as the path to being a recognized academic researcher. They overlap but are distinct. Be clear about which one you're pursuing, because the tactics differ.

For deployment safety specifically, the community is small enough that direct engagement matters more than publication count. Here is what has worked for others in similar positions:

**The highest-leverage single action is getting a response from someone who matters.** Email Anthropic's alignment team about your findings on Claude Haiku. Not to ask for anything — to share a result that's directly about their model. If one person at Anthropic reads your paper and finds it interesting, that's worth more for your trajectory than 500 ArXiv downloads. Do this. Do it now. The paper is already on ArXiv.

**Write one non-academic piece that makes the core finding accessible.** Not a Twitter thread. A 1,500-word essay on the LessWrong / Alignment Forum that presents the finding in plain language, explains why it matters for deployment, and invites pushback. The alignment community reads these forums. This is where ideas get stress-tested before they become research programs. If your framing is right, you'll get engagement. If it's wrong, you'll find out faster than you would through peer review.

**Present at one workshop in the next 12 months.** NeurIPS, ICML, and ICLR all have safety and alignment workshops with lower acceptance bars than main tracks. A workshop paper or poster is a legitimate venue for your current work and puts you in a room with the people you want to know. Algoverse mentors can advise on which workshops are appropriate targets.

**Don't build a Twitter presence yet.** You don't have enough output to sustain it without diluting your signal. The researchers who built influence through Twitter did so after they had a body of work to point to. One preprint is not a body of work. Build the work first.

---

## Highest-Return Actions (6-12 Months)

I'm giving you a ranked list, not a menu. Do these in order.

**1. Complete the IRB application before you lose Georgia Tech affiliation (immediate, non-negotiable).**

This is the most time-sensitive action in your entire research program and the one most people in your position procrastinate on. The human baseline study is the single most important extension of your current paper. It closes the most significant gap in the work (no human comparison), it's methodologically cheap (a survey is low-cost relative to API runs), and it produces a result that either validates your framing or forces you to revise it. You need to know which. But you need IRB approval to do it, and you need institutional affiliation to get IRB approval. Do this now.

**2. Run the cross-model comparison study (months 1-3).**

This is the highest-leverage research extension given your resources. Same protocol, multiple models (GPT-4o at minimum, Gemini Flash if budget allows). The API costs are real but manageable. The payoff is substantial: if the compression and state-dominance patterns replicate across models, you've shown something about language-to-action translation that isn't Claude-specific. If they don't replicate, that divergence is itself a finding about how different training and alignment procedures shape vague-language interpretation. Either result is publishable. This is the study that turns one paper into a research trajectory.

**3. Submit the current paper to one workshop (months 2-4).**

Identify the most appropriate safety/alignment workshop at a major venue and submit. Your Algoverse mentors should help you identify the right target. The goal is not prestige — it's peer review, community exposure, and a line on your CV that says "peer-reviewed." A workshop acceptance is meaningful at your stage.

**4. Write the Alignment Forum post (month 1-2, can run parallel to above).**

One post presenting the core finding in plain language. Frame it as a question to the community, not a declaration. Ask: does this pattern generalize? Has anyone seen similar behavior in their deployments? You're not just broadcasting — you're gathering signal about whether the community thinks this is interesting and where they think it points.

**5. Email three people at AI labs whose work intersects yours (month 1).**

Anthropic (obviously, given the model), DeepMind's safety team, and one academic researcher whose work on LLM behavior you've cited or should have cited. Keep the email short: "I have a preprint on Claude Haiku's behavior at the language-to-action boundary. Given your work on [X], I thought you might find the boundary abstention findings interesting. Happy to discuss." You will get responses from some of these. Those responses are the beginning of a network.

**What not to do in the next 6 months:**

Do not pursue mechanistic interpretability. It requires resources and expertise you don't have, it pulls you away from the empirical deployment-facing work that is your actual contribution, and it would be a detour from building a research trajectory in the area where you have genuine advantage. The mechanistic questions are interesting. They are not your questions to answer right now.

Do not try to expand the "passive failure" framing into a grand theory. You identified this risk yourself. The framing is useful for motivation, but the next paper should be narrower and more decisive, not broader. Compression of the word scale and state-dominance of interpretation are empirical findings. Let them stand on their own before you build a theoretical superstructure.

Do not start the decrease-instructions study, the partial-context condition, and the denser baseline grid simultaneously. Pick one extension (the cross-model comparison) and complete it. Breadth at this stage is the enemy of publication.

---

## Unrealistic Assumptions

**You are assuming the "passive failure" framing will resonate with the alignment community as stated.**

It might not. The alignment community has specific priors about what constitutes an alignment problem, and "the model silently mistranslates vague intensity words" may read to some reviewers as a usability problem or an NLP problem rather than an alignment problem. This doesn't mean the framing is wrong — it means you need to test it before building your research program around it. The Alignment Forum post will tell you quickly whether the framing lands.

**You are assuming Algoverse gives you more than it does.**

Algoverse is a real asset, but it is not a substitute for institutional affiliation with a PhD program or a lab. It gives you mentorship, collaborators, and a named fellowship — all valuable. It does not give you IRB access (Georgia Tech does), compute (you still pay for API calls), or the kind of credentialing that comes from a PhD program. Be clear about what Algoverse provides and what it doesn't. Use it for what it's good for: mentorship on research direction, feedback on papers, introductions to collaborators, and advice on the fellowship application process.

**You are assuming one strong paper is enough to demonstrate a research trajectory.**

It isn't. Fellowship committees and lab hiring managers want to see that you can sustain a direction. Two papers with a coherent through-line are categorically different from one paper. The cross-model comparison study, if executed well, gives you that second paper. Until you have it, your profile reads as "promising start" rather than "researcher with a program."

**You are assuming the IRB timeline is flexible.**

It isn't. If you're finishing your master's in the near term, your window to conduct IRB-approved human subjects research under Georgia Tech's umbrella is closing. The human baseline study is the most important methodological gap in your current work. If you miss the IRB window, you either delay this study by years or find an institutional sponsor willing to cover you — which requires exactly the kind of network you're still building. Treat the IRB application as a hard deadline, not a future work item.

---

## The Impostor Syndrome Question

Here is the honest assessment you asked for.

Your work sits at a legitimate entry point to the deployment safety research community. It is not yet at the level of work that gets cited heavily or changes the field's direction. That's appropriate — it's a first paper from a non-traditional researcher without a PhD. The bar for entry is not "change the field." The bar for entry is "produce a controlled empirical result on a real question that the community hasn't answered." You've done that.

What you have that most early-stage researchers don't: a real deployment motivation, a clean experimental design, and a result that's empirically unambiguous within its scope. The paper doesn't overclaim. The limitations section is honest. The methodology is reproducible. These are not small things. Many first papers from PhD students at top programs are worse on these dimensions.

What you're still missing: generalizability evidence, peer review, community engagement, and a second paper. These are not permanent gaps — they're next-step gaps. The difference between where you are and where you need to be is 12 months of focused execution, not years of credential-building.

The impostor syndrome question has a specific answer in your case: you are not an impostor, but you are also not yet what you want to become. The gap is real and closeable. The path is narrow — cross-model replication, human baseline, workshop submission, community engagement — and it requires you to resist the narrative inflation you correctly identified as your failure mode.

The vision of "passive failure at the action interface" as a research program is not inflation. It's a legitimate framing of a real problem. The inflation risk is in trying to make *this paper* carry that entire vision. It can't. Your job for the next 12 months is to build the empirical foundation that makes the vision credible, not to argue for the vision before the foundation exists.

Do the cross-model study. File the IRB application. Submit to one workshop. Write one Alignment Forum post. Email three people. Everything else is secondary.