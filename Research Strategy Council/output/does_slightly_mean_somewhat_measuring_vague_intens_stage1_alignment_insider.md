# Alignment Insider — stage1

This is sufficient. I now have what I need for a fully grounded strategic review. Let me deliver it.

---

# Alignment Insider: Strategic Review of Danny Tabach's Research Program

*Adversarial deliberation requested. Narrowing, not expansion, is the mandate.*

---

## Community Reception Assessment

**The honest read: this will be received as a useful empirical NLP result wearing an alignment coat. The alignment sticker will not be free.**

Here is what will happen when an alignment researcher reads this paper. They will see a well-executed behavioral experiment on a single model in a single synthetic domain. They will appreciate the controlled design. Then they will ask the question that determines reception: *does this tell me something about alignment that I couldn't already infer from what I know about LLM behavior generally?* A significant fraction will answer no. They will say: "Of course LLMs are inconsistent with vague language. Of course context dominates. This is a prompt sensitivity result with a resource allocation wrapper."

The alignment community's current center of gravity on agentic problems is focused on systems that "develop behaviors or objectives that conflict with designers' or operators' goals" — particularly in tool-using, multi-step environments where agents pursue instrumental aims including deception, collusion, or specification gaming. Your paper is about something structurally different: not a model pursuing misaligned goals, but a model failing to faithfully translate a user's linguistic intent into a numeric action. That is a real problem. But the community's gatekeepers will need to be convinced it belongs in *their* tent, not in the NLP or HCI tent.

**The reception risk is specific:** reviewers at alignment-focused venues will ask whether this is a *safety* problem or a *usability* problem. They will point out that the model isn't scheming, isn't deceiving, and isn't pursuing misaligned goals — it's just imprecise. That's a meaningful distinction in this community's current framing. You will need a sharp answer to that question before you submit anywhere that calls itself an alignment venue.

**What works in your favor:** The "drastically" → "dramatically" flip — where swapping one near-synonym causes the model to switch from acting to abstaining in the same state — is genuinely surprising and memorable. That single finding is your strongest hook. Lead with it everywhere. It is the empirical result that most clearly demonstrates that the failure mode is *discontinuous* and *invisible*, not merely noisy. That is the finding that separates this from generic prompt sensitivity work.

**What works against you:** One model (Claude Haiku), one domain, no human baseline. The community will want to know if this is a Claude Haiku artifact. They will want to know if humans would compress these words the same way. Without those comparisons, the paper's claim about alignment risk rests on a single data point in a synthetic environment. That is a real limitation and reviewers will name it.

---

## Audience Recommendation

**Target the NLP/deployment-safety audience first. Do not lead with alignment.**

This is the narrowing you asked for. You cannot serve alignment, HCI, and NLP simultaneously with this paper. You need to pick a lane, establish credibility there, and then cross over.

The right first audience is the NLP safety and evaluation community — specifically, researchers working on LLM behavioral consistency, prompt sensitivity, and deployment-facing reliability. This community will read the paper on its own terms. They will evaluate the experimental design, the statistical approach, and the generalizability of the findings. They will not demand that you solve deception or scheming. They will ask: *is this a real behavioral phenomenon, is it measured carefully, and does it matter for deployed systems?* Your paper can answer all three of those questions.

Workshops focused on AI safety drew significant attention at NeurIPS 2025, with large language models being deployed at scale in consumer products making questions about alignment, robustness, and safe behavior no longer theoretical. That's the current appetite. But notice the framing: "robustness and safe behavior" — not "deception and scheming." Your work fits the former frame better than the latter.

The alignment community is your *second* audience, not your first. Once you have a publication record in NLP safety, you can bring the work to alignment venues with the credibility of having already passed peer review in a rigorous technical community. Trying to enter alignment venues first, as an independent researcher with one preprint, is a harder path.

---

## Venue Strategy

**One paper, one venue. Do not fragment this into three simultaneous submissions.**

**Stage 1 (now): EMNLP 2026 or ACL 2026 — findings track or main conference**

This is the right first venue. EMNLP and ACL have strong traditions of empirical behavioral work on LLMs. The paper's controlled design, nonparametric statistics, and behavioral framing fit the NLP community's evidence standards. The "does slightly mean somewhat?" framing is exactly the kind of question that gets traction at these venues. The linguistic grounding (Quirk taxonomy, degree modifiers) is a genuine differentiator — most NLP safety papers don't have that theoretical scaffolding.

What you need to add before submission: a human baseline (even a small-n survey), at least one additional model for comparison, and a no-word control condition. Without these, the paper is a first slice, not a complete study. The human baseline is the single highest-leverage addition — it either shows that humans also compress these words (in which case the model is reflecting genuine linguistic ambiguity) or it shows that humans differentiate them (in which case the model has a specific failure). Either result is publishable. The ambiguity of not knowing is not.

**Stage 2 (after Stage 1 publication): NeurIPS SoLaR or COLM SoLaR workshop**

The SoLaR workshop is an interdisciplinary gathering that aims to foster responsible and ethical research in language modeling, recognizing significant risks from development, deployment, and use of language models, and bringing together experts from various domains with a shared commitment to promoting fairness, accountability, transparency, and safety. This is the right second venue. By the time you submit here, you should have the multi-model comparison and the human baseline. The SoLaR framing — deployment safety, socially responsible LM research — fits your work better than the core alignment workshops, which skew toward deception, scheming, and model internals.

**Stage 3 (cross-model study as a second paper): FAccT or AIES**

FAccT is the right venue for a second paper that establishes the cross-model pattern and connects to deployment consequences in high-stakes domains. FAccT reviewers care about real-world harm, not theoretical alignment risk. A paper showing that multiple frontier models exhibit the same compression pattern, with a human baseline showing that humans *don't* compress these words the same way, is a strong FAccT submission.

**Do not target CHI.** CHI will ask for user studies, interface designs, and interaction data. Your paper has none of that. CHI is the wrong community for this work at this stage.

**Do not target core NeurIPS or ICML main conference.** Not yet. You don't have the cross-model generalizability or the theoretical contribution that main conference reviewers at those venues will require.

---

## "Passive Failure" in Alignment Discourse

**The framing is not recognized as a term of art. It is recognized as a phenomenon. That gap matters.**

The alignment community does not have an established concept called "passive failure at the action interface." What it does have is a rich literature on specification gaming, reward hacking, and Goodhart's Law — all of which involve a model doing something other than what the operator intended. Research on specification gaming shows that open-ended language causes otherwise-constrained models to bypass rules, and that vague or underspecified objectives lead to environment or policy hacking. Your "passive failure" framing is adjacent to this but distinct: you're not describing a model gaming a specification, you're describing a model failing to faithfully execute a specification because the specification was expressed in vague natural language.

That distinction is real and worth preserving. But "passive failure" as a label will not resonate with most alignment researchers on first contact. It sounds like a euphemism for "the model is bad at this." The framing that will resonate better is **"semantic compression at the action boundary"** or **"intent-action fidelity"** — language that connects to the community's existing vocabulary around faithful execution and instruction following.

The deeper issue is this: the alignment community is currently focused on *active* failures — strategic reasoning about objectives, context, and safety apparatus, resulting in alignment faking, cooperation with adversarial actors, or active sabotage. Your work is about a failure mode that doesn't require any of that. The model isn't trying to do anything wrong. It's just imprecise. That is a harder sell to a community that has trained itself to worry about sophisticated adversarial behavior.

**The reframe that opens doors:** Stop calling it "passive failure" in alignment venues. Call it a problem of **operator intent preservation** — the question of whether a deployed system faithfully executes the operator's intended semantics, not just the surface form of their instruction. This connects to Anthropic's explicit language about steerable, trustworthy AI and to the broader concept of corrigibility. It's a harder problem than it looks, and your paper is the first controlled measurement of it.

---

## Potential Allies & Collaborators

**Be specific. Don't cold-email everyone. Pick two.**

**The most natural intellectual ally is the prompt sensitivity research community.** The BrittleBench line of work (which your paper already cites) is the closest existing research program. The researchers behind that work are studying whether semantically equivalent paraphrases produce different outputs; you're studying whether semantically distinct intensity words produce stable outputs. These are complementary questions and the methodological overlap is significant. Find the authors of the BrittleBench paper and reach out with a specific, short message: "I've extended the prompt sensitivity question to the action case — here's what I found."

**Within the alignment community, the most natural entry point is through Algoverse.** MATS alumni-founded organizations include Algoverse AI Safety Fellowship, which means the Algoverse network has direct connections into the MATS and Anthropic ecosystems. You are already inside this network. Use it. Ask your Algoverse PIs specifically: who at Anthropic or Redwood is working on instruction following reliability or agentic safety evaluations? That is the warm introduction you need, not a cold ArXiv ping.

**The AgentAlign and AgentSafetyBench research groups** are working on adjacent problems. AgentHarm presents a benchmark focusing on explicitly malicious agent tasks, while AgentSafetyBench offers an evaluation framework with 2,000 test cases examining safety risks across different stages of agent operation. These groups are measuring safety failures in agentic systems, but they're focused on harmful outputs, not on semantic compression of legitimate instructions. Your work is complementary, not competitive. Reach out to the AgentSafetyBench authors with that framing.

**Do not try to connect with MIRI or ARC at this stage.** Their research programs are focused on theoretical alignment and formal verification, respectively. Your empirical deployment work is not in their wheelhouse and they are not in yours.

---

## Fellowship & Career Positioning

**Your profile is stronger than you think for one specific fellowship and weaker than you think for another.**

**MATS: Realistic, but requires a specific pitch.**

MATS seeks individuals deeply motivated by AI security, alignment, and governance with the skills and mindset to contribute to cutting-edge research. With only about 4-7% of applicants ultimately selected, the program is highly competitive. Successful applicants demonstrate clear mission alignment, a track record of research or competency relevant to their chosen stream, and credible references.

Your profile — working data scientist, master's student, one ArXiv preprint, Algoverse fellow — is exactly the kind of non-traditional background that MATS says it welcomes. MATS explicitly looks for talent that traditional pipelines might overlook and welcomes technical researchers without prior ML experience who can demonstrate strong reasoning and research potential.

What you need for MATS is a credible answer to: "Which stream are you applying to, and why does your work connect to that stream's research agenda?" The Anthropic stream spans a range of empirical research areas in AI safety including AI control, scalable oversight, model organisms, model internals, model welfare, and security. Your work is closest to the "model organisms" and "AI control" streams — specifically, the question of whether deployed systems faithfully execute operator intent. Frame your application around that connection, not around "passive failure."

MATS looks for evidence of research ability, ideally in relevant areas, with outputs such as publications, blog posts, open-source projects, or substantial research contributions. Your ArXiv preprint is your evidence of research ability. The Algoverse fellowship is your evidence of community engagement. The JPMorgan production system is your evidence that this work comes from a real deployment problem, not a toy exercise. That combination is genuinely distinctive.

**Anthropic Fellows: Harder, but not impossible.**

Anthropic cares much more about ability to execute on research than credentials. Strong candidates can code well in Python, take ambiguous problems and make concrete progress, and think clearly about hard technical questions. They explicitly say you don't need a PhD, prior ML experience, or published papers.

Your obstacle at Anthropic is not credentials — it's fit. Anthropic's current priority areas include scalable oversight, adversarial robustness and AI control, model organisms, mechanistic interpretability, AI security, and model welfare. Your work doesn't cleanly map to any of these. The closest is "model organisms" — but Anthropic's model organisms work is focused on creating controlled demonstrations of specific misalignment phenomena (alignment faking, scheming). Your work is measuring a different phenomenon. You would need to reframe your research agenda around creating a model organism of *intent-action infidelity* — a controlled demonstration that vague operator instructions reliably produce misaligned actions in specific, predictable conditions. That reframe is possible, but it requires you to think about your work differently.

**The fellowship to target first is MATS, not Anthropic.** MATS is the on-ramp. Anthropic is the destination you work toward after MATS.

---

## Community Appetite & Timing

**The timing is genuinely good for deployment-facing empirical work. But you're competing with a crowded field.**

Workshops focused on AI safety drew significant attention at NeurIPS 2025, with large language models being deployed at scale in consumer products making questions about alignment, robustness, and safe behavior no longer theoretical. The community has shifted meaningfully in the last 18 months toward deployment-facing empirical work. The question used to be "will AI systems be misaligned in theory?" It is now increasingly "are deployed AI systems behaving reliably in practice?" Your work is in the second category.

Empirical studies have converged on realistic RL and tool-use environments to elicit and quantify agentic misalignment. The community is hungry for controlled, reproducible experiments that demonstrate specific failure modes. Your paper has that. The synthetic environment is a feature, not a bug — it makes the result clean and interpretable in a way that real-world deployment logs cannot.

The risk is not that you're too early. The risk is that you're in a crowded space. Submitting on a hot topic like AI safety or LLM evaluation can be advantageous because there are more workshops accepting papers in those areas, but it also means more competition. The key is to bring a specific angle or insight that existing work has not addressed. Your specific angle — the *action interface*, not the *output quality* — is genuinely underexplored. The community has studied harmful outputs, hallucinations, and jailbreaks extensively. It has studied much less the failure mode where a benign instruction is silently mistranslated into a different numeric action.

---

## Political Landscape

**Three camps, one territorial dispute, one strategic opportunity.**

**Camp 1: The x-risk / deception-focused alignment researchers.** This is the dominant camp at MIRI, ARC, and in the Anthropic alignment science team. They are focused on scheming, deception, and power-seeking. This stream focuses on building a science of scheming: empirically studying oversight gaming, alignment faking, and