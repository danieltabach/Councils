# Devil's Advocate — stage1

# Devil's Advocate Review: Strategic Assessment

---

## The Case That the Field Is Derivative

Let me name the specific bodies of work that most directly threaten the novelty claim, because the author deserves precision here, not a vague gesture at "related work."

**The automation bias and trust calibration literature** has been studying the gap between human intent and AI action for thirty years. Parasuraman & Riley (1997) on automation bias, Lee & See (2004) on trust in automation, Cummings (2004) on human supervisory control — these establish the foundational claim that humans cannot reliably predict or control automated system behavior through natural language interfaces. The "passive failure" framing is a restatement of what this community calls *automation surprise*: the system did something the operator didn't expect because the operator's mental model of the system was wrong. The author's contribution is a measurement of *one mechanism* by which this surprise occurs. That is real. But it is not a new field — it is a new data point in a 30-year-old field.

**The vague quantifier and linguistic uncertainty literature** is even more directly threatening. Mosteller & Youtz (1990), which the author cites, already documents that vague probability expressions compress into fewer distinct numeric interpretations than the surface vocabulary implies. Wallsten, Budescu, and colleagues throughout the 1980s and 1990s showed that words like "likely" and "probable" map inconsistently to numbers across individuals and contexts. The author's finding — that 10 intensity words compress to 5 distinct outputs — is structurally identical to what this literature found about probability expressions decades ago. The novelty claim requires that the *action* context (tool call producing a consequential numeric output) is categorically different from the *estimation* context (reporting a probability). That argument is present in the paper but underdeveloped and unproven. It may be true. It isn't demonstrated.

**The HCI safety and natural language interfaces literature** covers the deployment gap directly. Work on natural language interfaces to databases (Androutsopoulos et al., 1995 and the subsequent decade of NLIDBs), voice interfaces in aviation (Cushing, 1994 — "Fatal Words"), and more recently conversational AI in clinical settings (Laranjo et al., 2018) all study what happens when vague human language must be translated into precise system actions with safety consequences. Cushing's work on aviation communication failures is particularly sharp: pilots issuing ambiguous altitude instructions and controllers interpreting them differently produced crashes. The author's "drastically → dramatically flips act to abstain" finding is a cleaner, more controlled version of what Cushing documented in the field. The author has the better measurement instrument. They do not have a new phenomenon.

**The prompt sensitivity / brittleness literature** is the most recent and direct threat. Mizrahi et al. (2023, "State of What Art?"), Webson & Pavlick (2022), and the BIG-Bench Hard evaluations all document that semantically similar prompts produce different model outputs. The author's paper is a controlled, domain-specific instance of this. The contribution is the *controlled measurement environment* — the deterministic backend that converts linguistic variation into measurable outcome variation. That is methodologically clean. It is not a new phenomenon.

**The strongest existing work that most directly threatens the novelty claim** is Fischler & Firschein's work on language grounding and, more recently, Bender et al. (2020) on the "meaning" problem in NLP — the argument that statistical language models don't have stable referents for words, so of course "slightly" and "marginally" produce the same output. The author's paper is an empirical confirmation of a theoretical prediction that has been in the literature for years.

**My honest assessment of this case:** The "new field" framing is not supported. The existing literature covers the phenomenon from multiple angles. What the author has that is genuinely novel is: (1) a clean measurement instrument that isolates the language-to-action translation step with a deterministic backend, and (2) the specific finding about boundary-dependent abstention behavior, which I have not seen documented in this form elsewhere. These are contributions to existing fields, not the foundation of a new one.

---

## The Case That the Paper Can't Carry It

Here is what a skeptical NeurIPS reviewer would write in the meta-review, and I am not softening it:

**One model.** The entire empirical edifice rests on Claude Haiku. Not Claude Sonnet. Not GPT-4o. Not Gemini. Not an open-weights model where the training data and RLHF procedure are at least partially known. Claude Haiku is a commercial, closed-weights model with undisclosed training data, undisclosed RLHF procedures, and undisclosed system prompt defaults. The author cannot tell you *why* "drastically" acts while "dramatically" abstains. They cannot tell you whether this is a stable property of the model class or an artifact of a specific fine-tuning run. They cannot tell you whether the 0.50 hedge reflects training data frequency, RLHF reward shaping, or something else. The paper documents a behavioral fingerprint of one commercial model version. Model versions change. The findings may not replicate on the next Haiku release.

**One domain.** Resource allocation with a sum-to-100% constraint. This is not just "one domain" in the sense of being narrow — it is a domain with a specific mathematical structure (simplex constraint) that may be driving the boundary behavior. The abstention at 89% may not be about the semantics of "considerably" — it may be about the model's learned behavior near simplex boundaries. The author cannot distinguish these explanations with the current design.

**No human baseline.** The author acknowledges this. I am emphasizing it because it is more damaging than the paper's framing suggests. Without a human baseline, you cannot make the claim that the model's compression is a *failure* rather than a *reflection of genuine linguistic ambiguity*. If humans also compress "slightly," "marginally," "somewhat," and "mildly" into the same numeric output — which the Mosteller & Youtz literature suggests they might — then the model is not failing. It is accurately representing the ambiguity in the language. The entire "passive failure" framing depends on a gap between human intent and model action that has not been measured.

**Synthetic environment.** The allocation environment is clean by design, but that cleanliness is also a limitation. Real production systems have noise, feedback loops, multiple agents, and users who adapt their language based on observed outcomes. The author's finding that word choice is dominated by context state is interesting in a clean environment. In a real system, users would learn to say "drastically" when they want a large move, regardless of state, because they've observed the model's behavior. The static, non-adaptive experimental design cannot capture this.

**30 runs per cell.** For a deterministic model at T=0.0, 30 runs per cell is adequate. For T=0.7 and the boundary behavior analysis, 30 runs is marginal. The abstention finding at 89% (121/300 total, but word-level counts as small as 0/30 vs. 30/30) is robust for the extreme cases but the intermediate cases (the "drastically" 7% abstention rate is 2/30 runs) are fragile.

**What a senior alignment researcher would say:** This paper measures a real phenomenon. It is not a safety paper. It documents that a model's numeric outputs are compressed and state-dependent — which is a behavioral characterization, not a mechanistic one, and not a safety intervention. The alignment relevance depends entirely on the "passive failure" framing, which requires the human baseline that doesn't exist. Without it, this is a psycholinguistics result about model behavior, not an alignment result.

**The founding instrument claim fails** on a simple criterion: a founding instrument needs to be generative — it needs to produce a research program that couldn't exist without it. The author's measurement instrument is clever, but the research program it enables (test more words, test more models, test more domains) is incremental, not generative. It does not open questions that couldn't be asked before. It provides cleaner answers to questions that were already being asked.

---

## Narrative Inflation Check

Yes. The brief is an instance of the failure mode the author identified.

Here is the specific evidence:

**The phrase "passive failure at the action interface"** is doing enormous work. The paper does not establish that there is a failure. It establishes that there is compression and state-dependence. Whether this constitutes failure depends on whether the model's output diverges from human intent — which requires the human baseline that doesn't exist. The author has named a phenomenon before demonstrating that the phenomenon is harmful.

**"I think this matters across domains (healthcare, finance, logistics)"** — this is the inflation move in real time. The paper tests one model, one domain, one action direction, two temperatures. The leap to "healthcare" is not supported by anything in the paper. It is a vision statement dressed as an empirical claim.

**"The failure modes rhyme across those domains"** — this is assertion, not evidence. The author has no data from healthcare, finance, or logistics. They have a metaphor.

**"I've been calling this 'passive failure'"** — naming a phenomenon before establishing it is a classic inflation move. The name implies a verdict (failure, passivity, interface as the locus) that the evidence does not yet support.

**The brief's framing of the paper as "opening a window into something bigger"** — this is the author's own language, and it is the inflation pattern exactly. The paper is a controlled measurement of one behavioral property of one model in one domain. That is not a window into something bigger. It is a result. The author is being asked to let it be a result.

**Where the brief is NOT inflating:** The origin story (production system, real stakes) is grounded. The acknowledgment of limitations is honest. The request for narrowing rather than expanding is self-aware. The author knows they do this. The question is whether knowing it is enough to stop it.

---

## The Steelman Alternative

Here is the best version of this research program that does not require the "new field" claim and does not require the brief's inflation:

**The actual contribution is a measurement instrument.** The author built a clean, reproducible method for measuring how a language model maps vague intensity language to numeric actions in a constrained environment. The deterministic backend is the key innovation — it converts a behavioral question into a measurement question. This is a methodological contribution to the empirical study of LLM behavior.

**The actual finding is the boundary behavior.** The compression result (10 words → 5 outputs) is interesting but not surprising given the existing literature. The boundary-dependent abstention is genuinely novel in its specificity: the finding that "drastically" acts by pushing to the ceiling while "dramatically" abstains in the same state is a crisp, falsifiable, surprising result. This is the paper's sharpest contribution. It belongs in the empirical NLP / model behavior literature, not in a new field.

**The right framing is "behavioral characterization of vague language in constrained action contexts."** This sits cleanly in the intersection of empirical NLP, human-computer interaction, and AI evaluation. It does not require a new field. It requires a second paper that either (a) adds the human baseline and establishes that there is actually a gap between human intent and model action, or (b) demonstrates the boundary behavior across multiple models and domains, establishing generality.

**The production origin is a genuine asset.** The fact that this came from a real system the author built gives it ecological validity that most academic benchmarks lack. The right way to use this is not to claim a new field, but to position the work as "empirically grounded in deployed systems" — which is a credibility claim, not a scope claim.

**The research program that succeeds without the new field claim:** Study 1 (existing paper): Behavioral characterization of intensity word compression in one model. Study 2: Human baseline + cross-model comparison, establishing whether the compression reflects model failure or linguistic ambiguity. Study 3: Boundary behavior replication across domains with different constraint structures, testing whether the abstention pattern generalizes. This is a three-paper arc that is publishable, credible, and does not require founding a field.

---

## What Would Change My Mind

I am arguing the field is derivative. Here is what would make me concede it is genuinely new:

**On the field claim:** Show me a body of work that specifically studies the *action* case — where vague language must produce a consequential numeric output through a tool call — as distinct from the *estimation* case (probability expressions) and the *classification* case (sentiment, intent). If that literature does not exist as a coherent body, then the author has identified a genuine gap. My current read is that the gap exists but is not large enough to constitute a new field — it is a new application domain within existing fields. To change my mind, I would need to see that the action context produces qualitatively different phenomena than the estimation context, not just quantitatively different ones. The boundary abstention behavior is a candidate for this — it is a categorical behavioral switch that doesn't have a direct analog in the probability expression literature. If Study 2 shows that humans do not exhibit analogous abstention behavior (i.e., humans would try to act even near boundaries), that would establish the action context as genuinely different.

**On the paper carrying the field:** Show me the result replicated across at least three models with different training procedures (one open-weights, one closed), across at least two domains with different constraint structures, with a human baseline showing a measurable gap between human intent and model action. That four-element package — multi-model, multi-domain, human baseline, demonstrated gap — would make the paper load-bearing. Any one of those elements alone would substantially strengthen the case.

**On the "passive failure" framing:** The framing becomes credible the moment you have a human baseline showing that humans would have acted differently. Right now, the failure is asserted. If humans also compress "slightly" and "marginally" into the same output, the model is not failing — it is accurately representing genuine ambiguity. If humans reliably distinguish these words and the model does not, you have a documented failure. Run the survey. That is the single most important next step, and it is cheap.

---

## Honest Confidence Assessment

**My case that the field is derivative: 7/10.** The existing literature is real and relevant. The author is not discovering a new phenomenon — they are measuring it more cleanly than it has been measured before. The "new field" framing is not supported. However, I am reaching slightly when I claim the boundary abstention behavior has direct precedents. I have not found a clean prior example of word-dependent categorical action switching in a constrained tool-use context. That specific finding may be genuinely novel at the mechanistic level, even if the broader phenomenon is not.

**My case that the paper can't carry the field: 9/10.** This is my strongest argument and I am not reaching. One model, one domain, no human baseline, synthetic environment — these are not minor limitations. They are structural constraints on what the paper can claim. The paper is a solid first result. It is not a founding instrument. The gap between "solid first result" and "founding instrument" is exactly the gap the author's inflation tendency fills with narrative.

**My case that the brief is already inflating: 8/10.** The evidence is in the author's own words. The "passive failure" naming, the domain-generalization claims, the "window into something bigger" framing — these are the inflation pattern in action. The author knows this. The brief's self-awareness is real. But self-awareness of a failure mode is not the same as not doing the thing.

**Where I am weakest:** I cannot fully evaluate the claim that the *action* context is categorically different from the *estimation* context without more data. If it turns out that boundary-dependent abstention is a robust, model-general, domain-general phenomenon that only appears when vague language must produce a *consequential action* (not an estimate), then the author has found something genuinely new. I am arguing against that claim because the current evidence doesn't support it — not because I am certain it is false.

**The honest summary:** The author has a clean methodological contribution and one genuinely sharp finding (the boundary abstention behavior). The inflation is in the framing, not the data. The data is real. The field claim is not. The path forward is to let the data be what it is — a controlled measurement of a specific behavioral property — and build the second paper that either establishes the human gap or establishes cross-model generality. Either of those would be a real contribution. Neither requires founding a field.