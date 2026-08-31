# Weekly AI Agent Paper Report

**Generated:** 2026-08-31 17:06
**Period:** 2026-08-24 to 2026-08-30

## Summary

- **Total papers fetched:** 729
- **Papers matching keywords:** 163
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-08-24) | Change |
|--------|-----------|-----------|--------|
| Total matched | 163 | 142 | +21 |
| arxiv | 160 | 140 | +20 |
| biorxiv | 3 | 2 | +1 |
| medrxiv | 0 | 0 | +0 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. Self-organized Regulation of Group Size and Number in Natural and Artificial Collectives

- **Authors:** Zhang, T., Lee, S., Hamann, H.
- **Published:** 2026-08-28
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.25.746978](https://doi.org/10.64898/2026.08.25.746978)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

From animal societies to self-organizing multi-agent systems, collectives adapt their group structure to tasks and environments. However, how they determine appropriate group sizes and the number of subgroups to form remains unclear. We formulate the Group Size and Number Regulation Problem (GSNRP), which asks how individuals regulate group sizes and numbers using only local information. In a first step, we establish a graph-theoretic model demonstrating that simple following behavior suffices to form group structures that match theoretical expectations, but is insufficient for active regulation of group size and number. In a second step, we operationalize individual group-size preferences in a decentralized fission-fusion mechanism based on perceived group size. Through multi-agent simulations, we validate that this mechanism achieves stable convergence across three signaling regimes, from position-only sensing to continuous group-size communication. Using tracking data from wild white-nosed coatis (mammals in the raccoon family), we calibrate individual group-size preferences and show that the controller recovers selected group-size, subgroup-count, and transition statistics. This in-sample case study demonstrates descriptive consistency with natural fission-fusion dynamics without establishing the underlying behavioral mechanism. These results suggest that natural and engineered collectives may share local principles of perception, preference, and response for regulating group structure.

</details>


### 2. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-08-26
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

</details>


### 3. ASAREE: An Analytical Sandbox for Agentic AI Research, Engineering, and Experimentation

- **Authors:** Moran, J., Freda, P. J., Ghosh, A., Hernandez, M. E., Moore, J. H.
- **Published:** 2026-08-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.20.746074](https://doi.org/10.64898/2026.08.20.746074)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Summary: Agentic AI platforms enable the engineering of autonomous workflows but are not designed for experimentation and hypothesis testing. ASAREE (Analytical Sandbox for Agentic AI Research, Engineering, and Experimentation), is an open-source platform to address this gap. ASAREE creates agents, connects to MCP servers and tools, and designs factorial experiments through a visual interface or Python SDK. It records a full provenance trace for every run and routes all model calls through a provider-agnostic bridge that supports local deployments, ensuring data privacy. As a use-case, we use ASAREE to evaluate key design choices in a mutli-agent machine learning pipeline. Across a 2 x 2 x 2 factorial design, more advanced models, greater reasoning effort, and critic agent use significantly increased compute time, token use, cost, and feature count without improving predictive performance. The lowest-cost baseline, Claude Sonnet 5 with medium effort and no critic, achieved the highest mean PR AUC while Claude Opus 5 with extra high effort and a critic agent cost 15.5x more (USD) and ran 13.1x longer while performing worse on average. These findings highlight ASAREE as a robust framework for evaluating agentic system performance and resource efficiency.

</details>


---



## Arxiv (160 papers)


### 1. COVER: Identifiable Evaluation of Coalition Routing

- **Authors:** Raghul Sugumar, Amrit Gopinath
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28475v1](http://arxiv.org/abs/2608.28475v1)
- **PDF:** [https://arxiv.org/pdf/2608.28475v1](https://arxiv.org/pdf/2608.28475v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a multi-agent system changes its team, it also changes the messages and final answer it produces, so an end-to-end accuracy gap does not by itself identify a routing effect. We introduce method, an evaluation contract that fixes a public information boundary, downstream stack G, and finite legal team family before outcomes are generated. Complete coverage identifies exact finite-benchmark oracle regret conditional on that stack. For any finite collection of frozen policies, executing the union of their distinct selected teams is the minimal assumption-free support for every pairwise policy contrast, though not for absolute oracle regret. Two controlled tables with source-ID-disjoint splits test the instrument. On MuSiQue-12, a pre-specified privileged positive control improves regret from 0.532 to 0.402; a later public-interface control reaches 0.424 versus 0.554 but is retrospective. On HotpotQA-4, a pre-specified public direct scorer improves regret from 0.313 to 0.110. In fixed-stack Llama execution, verified route regret improves by 0.190, while the raw-answer gain is 0.010 with an interval crossing zero. A five-family ToolSandbox variant-shift validation exhaustively evaluates 16 declared teams on 14 untouched task variants (224/224 valid rows): the declared-family oracle reaches 0.768 safe-evidence completion, while the prospectively frozen router gets 0.637 (regret 0.131), failing the predeclared 0.10 criterion. A later retrospective comparator reaches 0.655, matching all-workers with 4.57 versus 5.00 workers on average. Thus COVER exposes selection headroom without manufacturing a routing win. A crossed-stack diagnostic shows absolute scores depend on G but finds no detectable router-by-finalizer interaction. COVER is an auditable measurement methodology, not a claim of stack-invariant or universal agent-routing superiority.

</details>


### 2. Learning to Use Tools: Reinforcement Learning for Tool-Integrated Mathematical Reasoning

- **Authors:** Minghui Xu, Zi Wang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28447v1](http://arxiv.org/abs/2608.28447v1)
- **PDF:** [https://arxiv.org/pdf/2608.28447v1](https://arxiv.org/pdf/2608.28447v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current large language models (LLMs) increasingly benefit from external tool integration, especially for tasks requiring reliable computation and verification. Motivated by this, we study calculator tool calling for improving mathematical reasoning on the Countdown task. We first analyze reasoning failures and find that calculation errors account for a substantial portion of incorrect responses. We then construct supervised fine-tuning datasets to teach the model useful tool-use patterns and how to interpret returned outputs. Building on this tool-formatted policy, we apply several on-policy reinforcement learning methods, including RLOO, RLOO++, GRPO, and DAPO, using automatically verifiable final-answer rewards. To enable a more reliable evaluation, we construct a fresh 1,024-problem held-out Countdown benchmark with no exact overlap with the training data. Our results show that calculator tool integration consistently improves both SFT and RL baselines, yielding roughly 10 percentage-point gains across pass@k. Among the RL methods, Tool-DAPO achieves the strongest performance, improving pass@1 from 35.8% for Tool-SFT to 66.0%. Further analysis shows that RL encourages more effective tool use even when only final-answer rewards are provided. These findings suggest that tool integration reduces arithmetic and verification errors, while RL increases the probability of correct reasoning traces.

</details>


### 3. Prove2Me: An Open Collaborative Platform for Scaling Math Formalization

- **Authors:** Shuze Chen, Kunal Marwaha, Xiaoyang Lu, Henry Yuen, Tianyi Peng
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28433v1](http://arxiv.org/abs/2608.28433v1)
- **PDF:** [https://arxiv.org/pdf/2608.28433v1](https://arxiv.org/pdf/2608.28433v1)
- **Categories:** cs.AI, cs.LO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Proof assistants such as Lean 4 promise the paradigm of formally verified mathematics, but large-scale formalization projects have faced major barriers to entry, including the need for expertise in formal verification (as well as the underlying mathematics) and the significant time required for writing formal proofs. AI coding agents have dramatically reduced these barriers; human users can now use natural language to prompt agents to write complex proofs in Lean. This opens up the intriguing possibility of internet-scale mathematical collaboration involving both humans and AI agents, where correctness is machine-checked.
  To realize this possibility, we introduce Prove2Me (https://prove2.me), an open collaborative platform for formalizing mathematics. Users launch formalization "missions", to which AI agents contribute formal proofs toward completion. We designed mechanisms and a specialized harness in Prove2Me that enable large-scale collaboration so that agents can build on one another's work and freely reuse existing results. In doing so, Prove2Me aims to turn math formalization into a scalable, crowd-sourced effort open to anyone with an agent.

</details>


### 4. EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses

- **Authors:** Tanmay Sah, Dolly Sah, Harshul Jain, Tanya Sah
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28363v1](http://arxiv.org/abs/2608.28363v1)
- **PDF:** [https://arxiv.org/pdf/2608.28363v1](https://arxiv.org/pdf/2608.28363v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime. Such self-evolution can improve capability, but a successful mutation may leave persistent effects that cannot be safely reversed in states different from the one in which it was created. We introduce EvoUndo, a framework for representing, synthesizing, diagnosing, and independently verifying recoverability of model-generated self-modifications across counterfactual states. Across 600 unseen one-shot self-evolution tasks, we identify 197 capability-improving mutations that fail recoverability verification. Under the original recovery representation, conventional repair strategies recover 0/197 of these natural failures. Deterministic oracle analysis recovers 48/197 under the original recovery language L0, while the extended recovery calculus increases empirical oracle recovery to 191/197. A protocol-locked 2x2 grounding-by-expressivity intervention then separates two bottlenecks: exact state-address grounding increases successful recovery from 0/48 to 38/48 (79.2%) when the original language is sufficient, while extending the recovery language enables recovery on 142/143 (99.3%) failures in the oracle-defined S1 stratum. On the primary gpt-oss-120b backbone, adding exact-address diagnostics to the richer language reduces recovery to 133/143 (93.0%); a Qwen3.8-27B replication preserves the grounding and expressivity effects but not this negative interaction, indicating that the latter is model-dependent. These results indicate that reliable agent self-evolution requires co-designing verification, state grounding, witness semantics, and recovery-language expressivity rather than relying on iterative prompting alone.

</details>


### 5. AGENT-O: A Semantic Agent Card Framework for Interoperable and Governed Healthcare AI Agents

- **Authors:** Pengze Li, Cui Tao
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28345v1](http://arxiv.org/abs/2608.28345v1)
- **PDF:** [https://arxiv.org/pdf/2608.28345v1](https://arxiv.org/pdf/2608.28345v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AGENT-O is a modular ontology framework that defines a semantic Agent Card for representing health-oriented AI agent systems and supports assessment of reporting completeness in scientific publications. AGENT-O was developed as an OWL 2/RDF ontology covering runtime, models, workflow, tools, clinical use, evaluation, provenance, governance, and reporting assessment. Evaluation included ontology inventory, OWL-RL reasoning, three SHACL suites, 12 SPARQL competency queries, three cases, and model-assisted reporting-completeness assessment of 279 papers across five dimensions. The ontology contained 1,962 RDF triples and 1,922 Protege axioms, with 252 active classes, 198 active object properties, and 51 datatype properties. All SHACL suites conformed on example graphs, all competency queries returned prespecified evidence, and all 279 papers were scored. Incomplete reporting was highest for runtime/architecture (84.6%), governance/safety (82.8%), and provenance/reproducibility (78.1%), compared with evaluation (25.8%) and benchmark-process alignment (29.8%). AGENT-O supported semantic Agent Card representation and reporting assessment while revealing an evaluation-specification gap: evaluation and benchmark procedures were reported more consistently than runtime architecture, governance, and reproducibility. AGENT-O provides a reusable ontology, semantic Agent Card profile, and reporting-completeness workflow for structured reporting and gap identification, but does not assess agent quality or deployment readiness.

</details>


### 6. Finding Where the Buck Stops: An Automated Failure Attribution-Based Reflection Framework for Multi-Agent Collaboration

- **Authors:** Xiaoqing Wang, Keman Huang, Bin Liang, Hongyu Li, Xiaoyong Du, Wuqiong Pan
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28264v1](http://arxiv.org/abs/2608.28264v1)
- **PDF:** [https://arxiv.org/pdf/2608.28264v1](https://arxiv.org/pdf/2608.28264v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) powered by large language models have shown promise for complex tasks but suffer from high failure rates. Current self-reflection methods for MAS require all agents to reflect upon failure, overlooking a critical reality: failures typically stem from a specific agent leading the task astray, namely the decisive error agent, while others merely fulfill their regular duties. Forcing regular-behaving agents to reflect contaminates their memory with wrong insights. Hence, we propose DoCtOR (Diagnose-then-Correct PPO-enhanced Reflection), a novel reflection framework that enhances multi-agent collaboration. DoCtOR first identifies the decisive error step and decisive error agent through automated failure attribution, then employs counterfactual reasoning to generate a corrected decisive error step, and finally engages only the decisive error agent to produce targeted reflections. Experimental results show DoCtOR achieves 22%, 26%, and 27% improvements over initial success rates on HotPotQA, ChartQAPro, and Mind2Web datasets, outperforming Reflexion, Retroformer, and COPPER. We further establish the generalizability of our diagnose-then-correct paradigm and demonstrate that in low-resource settings, focusing reflection on reasoning steps after the decisive error step achieves comparable quality to reflecting on the complete failure trajectory.

</details>


### 7. CrabOS: An Operating System for Human-AI Co-inhabitation

- **Authors:** Qi Yang, Yun Ma
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28165v1](http://arxiv.org/abs/2608.28165v1)
- **PDF:** [https://arxiv.org/pdf/2608.28165v1](https://arxiv.org/pdf/2608.28165v1)
- **Categories:** cs.AI, cs.HC, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are evolving into long-running computational entities that can invoke tools, maintain memory, and complete complex tasks across applications. In real-world settings, completing a task often requires humans and AI to take turns leading its execution. Such alternation depends on the seamless handoff of the work state of the task between humans and AI. Existing agent systems, however, provide humans and AI with separate work environments. AI agents must therefore rely on additional bridges to continue work: either developers build task-specific interfaces to access the work state, or users manually transfer relevant parts of it through screenshots or textual descriptions. Both approaches make handoffs costly and scale poorly.
  We propose Human-AI Co-inhabitation, a type of work environment that enables humans and AI to seamlessly take turns continuing work on the same task, and design and implement CrabOS to realize this concept. CrabOS represents the work state as natural-language-readable text objects shared by humans and AI, allowing both to access and manipulate it directly through the same auditable interface without bridges. Case studies show that CrabOS elevates support for complex tasks with alternating human and AI leadership from bridge-dependent application-level solutions to native operating-system capabilities, which provide a new foundation for developing and running AI agents.

</details>


### 8. VICT: Verifier-Instrumented Credit Tracing for Long-Horizon LLM Agent Reinforcement Learning

- **Authors:** Pengcheng Li, Zhengyang Zhang, Dongxu Zhang, Sui Huang, Shaohua Ma
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28128v1](http://arxiv.org/abs/2608.28128v1)
- **PDF:** [https://arxiv.org/pdf/2608.28128v1](https://arxiv.org/pdf/2608.28128v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Fine-grained credit assignment is a central challenge in reinforcement learning for long horizon LLM agents. Standard objectives often train from programmatically verifiable terminal rewards by broadcasting each sparse outcome to every action in a trajectory. Existing methods typically seek finer credit from the rollout side, constructing auxiliary trajectory signals or additional comparisons to estimate action importance. Although useful, these approaches still treat the verifier that judged success as a scalar reward, discarding its internal task structure. Our key insight is that many verifiable tasks already encode the relevant checks inside their terminal verifier. We propose VICT (VerifierInstrumented Credit Tracing), a training-time interface that exposes executable or evidence backed atoms and traces them back to actions through dependency-valid proof edges. VICT redistributes group-relative advantage only along those edges, shifting credit assignment from rollout-side inference to verifierside tracing. It preserves the original terminal reward, abstains when evidence is incomplete or ambiguous, and changes only the training-time advantage tensor, requiring no learned critic, process labels, branch rollouts, or inference-time verifier access. On ALFWorld and WebShop, VICT improves substantially over outcome-only training and achieves strong performance alongside recent fine-grained credit methods; ablations rule out dense atom rewards, final-commit credit, temporal proximity, and sparsity as sufficient explanations.

</details>


### 9. String: An Agentic OS Where Every App Is a Markdown File

- **Authors:** Jookyung Song, Nojun Kwak, Simyung Chang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28027v1](http://arxiv.org/abs/2608.28027v1)
- **PDF:** [https://arxiv.org/pdf/2608.28027v1](https://arxiv.org/pdf/2608.28027v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents have become a new class of software user, but every surface they work through was designed for someone else. Pages are built for human eyes, which can skim and ignore; tool schemas for programs, which pay nothing to carry definitions they never call. An agent has neither luxury: it re-reads, and pays again for, everything it is shown on every turn. We present String, an open-source runtime that gives this user an interface of its own and treats the job as an operating-systems problem. Tool knowledge moves out of the agent's context and into a common layer that renders it back one view at a time as Markdown. A single SFMD (String-Flavored Markdown) document declares an application's views, typed actions, navigation, and credentials, and the runtime handles discovery, validation, execution, state, and secrets behind two core verbs: /open to see and /act to do. Web and app turn out to be two renderings of one architecture: an SFMD site serves styled HTML to browsers and the raw document to agents, so one grammar reaches apps, files, shells, and the web, even legacy HTML, with no per-site integration. Views stay partial by design, and the staging is causal: disclosing one tier of detail a single turn too early costs up to 23 accuracy points, while proper staging drops wrong-action selection from 28% to 2%. Privilege follows provenance: a remote page may call HTTP but never the shell, and caller-supplied text never expands a stored secret. On an 87-task benchmark that pairs each task with curated skills, operationalizing those procedures as on-demand String apps yields comparable aggregate success across six models from frontier to small (+1.3pp) while using 33.5% fewer tokens among completed episodes, and the resident interface stays a constant 53 tokens at any catalog size. We report the design, the evaluation, and what three months of production use taught us.

</details>


### 10. Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents

- **Authors:** Yuxu Ge
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.28011v1](http://arxiv.org/abs/2608.28011v1)
- **PDF:** [https://arxiv.org/pdf/2608.28011v1](https://arxiv.org/pdf/2608.28011v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Trajectory-level credit assignment can localize which module of a tool-using LLM agent causes failures using only verifiable signals. We ask whether such failure credit should route a fixed zeroth-order/evolution-strategies (ZO/ES) perturbation budget. Across a synthetic environment and frozen Qwen2.5-1.5B/3B and SmolLM2-1.7B agents, three task families, six allocation schemes, a credit-noise sweep, paired seeds, and exact sign-flip tests, we find no statistically detectable improvement over uniform allocation in any on-pool comparison (no gain of at least 2 percentage points). The joint soft-plus-sigma scheme is equivalent to uniform within a +/- 0.02 AUC margin on 1.5B and 3B; concentrating the full budget on the credit argmax is marginally equivalent on 1.5B, where that module is the verified bottleneck, and significantly worse on 3B. Inverse-propensity debiasing does not rescue routing, and misrouting costs up to -0.074 AUC in-house and -0.118 end-to-end on the BFCL-derived family. Across six fixed-step schedules, loss is linear in bottleneck starvation rate (R^2 = 0.94, descriptive), and a preregistered credit-free coverage floor removes detected harm. Matched-budget burst and step-compensating catch-up schedules are consistent with harm arising from insufficient cumulative parameter movement rather than update frequency. Our primary estimand is optimization efficiency on a fixed task pool. On unseen BFCL functions, the study's one exception is that soft routing exceeds uniform on held-out endpoints (+0.047, p = 0.031, n = 6). A plausible but untested reading is that routing-favored caller improvements transfer while uniform's on-pool gains reflect a synthesizer behavior specific to our harness. We report this exception explicitly and document three failure modes that can silently invalidate ZO/ES experiments on frozen LLMs.

</details>


### 11. PhenoIntel: A Lifecycle-Aligned Multi-Agent Web Application for Verified, Accessible Plant Phenotype Analysis

- **Authors:** Narendren S, Soumyashree Kar
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27999v1](http://arxiv.org/abs/2608.27999v1)
- **PDF:** [https://arxiv.org/pdf/2608.27999v1](https://arxiv.org/pdf/2608.27999v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing conversational plant-phenotyping platforms are difficult for plant scientists to use and lack the reliability scientific research demands: failed analyses are reported as valid measurements rather than flagged as missing, statistical tests run without checking assumptions, predictions carry no uncertainty estimate, and specialised hardware limits accessibility. We present PhenoIntel, a lifecycle-aligned multi-agent web platform that turns the full machine-learning workflow into a reliable, user-friendly phenotyping system. Nine specialised agents divide the analysis into stages, from image collection through model selection, inference, and reporting, rather than handing the whole task to one AI manager. Independent checks separate these stages, and every agent reads from and writes to one shared, fixed-structure record, so an inconsistent output from one stage is caught before it reaches the next. Uncertainty is matched to each model family, conformal prediction, detection-confidence spread, or Monte Carlo Dropout, rather than applied uniformly, and quality thresholds adapt to crop and task instead of one global cutoff. When no suitable model exists, PhenoIntel can propose, validate, and integrate a new one on its own. The model repository spans ten trained models across five crops and four imaging modalities. Classification models reach Macro F1 of 0.78-0.996; object-detection models reach 0.96 mAP@50 with a 54% reduction in counting error over an unoptimised baseline; and a temporal model reaches held-out Macro F1 of 0.7050. PhenoIntel runs in a browser on standard hardware, requiring no GPU, and a 1,200-test automated suite confirms complete pipeline execution. Every result carries calibrated uncertainty, validated statistics, and FAIR-compliant provenance, a combination existing conversational phenotyping tools do not offer.

</details>


### 12. Automated Analysis Framework for Multilingual Climate-Health Literature Based on Multi-Agent Large Language Model

- **Authors:** Yuze Sun, Shihui Zhang, Jiancheng Pan, Yunjia Ye, Wentao Luo, Jiahao Li, Quan Zhang, Wenjia Cai, Xiaomeng Huang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27998v1](http://arxiv.org/abs/2608.27998v1)
- **PDF:** [https://arxiv.org/pdf/2608.27998v1](https://arxiv.org/pdf/2608.27998v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid proliferation of interdisciplinary and multilingual scientific literature has left traditional manual analysis and single-algorithm methods plagued by low efficiency, poor scalability, and insufficient domain adaptability. Targeting the literature analysis needs of the typical interdisciplinary climate-health field, this study proposes a multi-agent large language model automated analysis framework for multilingual scientific literature, which realizes full-process automation covering literature screening, structured information extraction, and standardized integration. With a central coordination module as the core, the framework deploys three dedicated agents for document evaluation, information extraction, and analytical review to mimic the literature analysis thinking of domain experts, and adopts a four-layer hallucination control strategy together with a manual verification procedure to ensure the accuracy and reliability of analytical outcomes. Validated on a bilingual Chinese-English corpus of 32,642 climate-health papers covering China from 1993 to 2023, the framework achieves an F1 score of 0.92 in core information extraction, and completes the extraction and standardization of 2,012 city-literature association pairs, offering effective technical support for large-scale evidence mining in the climate-health research domain.

</details>


### 13. CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?

- **Authors:** Zi Liang, Xiaoyu Xu, Yanyun Wang, Minxin Du, Qingqing Ye, Haibo Hu
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27990v1](http://arxiv.org/abs/2608.27990v1)
- **PDF:** [https://arxiv.org/pdf/2608.27990v1](https://arxiv.org/pdf/2608.27990v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompt injection attacks on Large Language Model (LLM) agents seek to introduce malicious instructions or content into external text sources retrieved by agents, forcing the underlying LLMs to execute harmful actions outside their benign scope. While current defenses effectively counter known injection attacks, deploying them in LLM agent environments remains challenging due to attack variants and emerging threats. Moreover, existing solutions typically suffer from an inherent trilemma, i.e., a constant trade-off among runtime efficiency, contextual precision, and adaptability. To bridge this gap, we propose Continuous Agents for Injection Threats via Lifelong Yielding Nexus (CAITLYN), an agent-agnostic defense middleware. CAITLYN integrates two systems. System I focuses on immediate defense against existing attacks using a two-tiered library: Tier-0 for rule-based detection scripts and Tier-1 for optimized LLM-based accurate inference. System II, in contrast, is deployed to monitor potential abnormal signals and attempt to synthesize new defenses. On standard benchmarks, CAITLYN matches the detection performance of state-of-the-art defenses at lower token overhead than LLM-as-a-judge baselines. On Emerging, our new delivery-aware benchmark featuring novel injection techniques, static baselines and the standalone System I configuration remain vulnerable. In contrast, System II autonomously synthesizes verified defense capabilities, substantially lowering the attack success rate across three diverse agent environments.

</details>


### 14. When Evidence Shapes Collaboration: Knowledge-Conditioned Topology Generation for Multi-Agent Systems

- **Authors:** Yangxiao Jiang, Jiarun Fan, Mingcong Xu, Yanxi Guo, Jiwen Feng, Shanqing Xu, Mengchen Qian, Wei Chen, Xiaojin Zhang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27984v1](http://arxiv.org/abs/2608.27984v1)
- **PDF:** [https://arxiv.org/pdf/2608.27984v1](https://arxiv.org/pdf/2608.27984v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Systems (MAS) have recently moved from static workflows toward dynamically generated collaboration topologies. However, existing topology generation methods rely primarily on the parametric knowledge of large language models, with external search or retrieval used only as a reactive tool rather than an explicit determinant of collaboration structure. This leads to structure-knowledge misalignment, where systems exhibit redundant interactions or insufficient verification in knowledge-intensive tasks. We propose K-GAT (Knowledge-Guided Agent Topology Generator), a neuro-symbolic framework that formulates collaboration topology design as a knowledge-conditioned structure learning problem, integrating external evidence directly into autoregressive graph generation. Extensive experiments on knowledge-intensive benchmarks demonstrate K-GAT's efficiency and effectiveness: notably on the expert-level GPQA dataset, K-GAT outperforms the LLM-Debate baseline by a substantial margin of +15.7% in accuracy, while consuming less than half the computational tokens.

</details>


### 15. openJiuwen: Beyond Static Harnesses for Long-Horizon Coding Agents

- **Authors:**  openJiuwen Team, Tao Yu, Xinyu Zhang, Qianqian Chen, Xiaoneng Xiang, Chia Kwangyang, Xingchen Huang, Ran Chen, Yangkai Ding, Zheng Wang, Yeo Boon Hong, Bingzheng Gan, Enrui Hu, Shuo Cheng, Deyang Li, Ruifeng Shi, Hongbo Wang, Qi Ye, Xuefeng Jin, Zhangchun Zhao
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27969v1](http://arxiv.org/abs/2608.27969v1)
- **PDF:** [https://arxiv.org/pdf/2608.27969v1](https://arxiv.org/pdf/2608.27969v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon coding agents operate over evolving repository states while increasingly relying on heterogeneous capabilities, delegated agents, and multi-agent coordination. These trends pose two complementary challenges for the agent harness. First, developers need to compose capabilities, reconfigure execution logic, and scale increasingly complex agent systems without repeatedly rebuilding orchestration. Second, complex coding tasks continuously produce new evidence---such as semantic diagnostics, execution outcomes, task progress, and changing context relevance---that should dynamically influence subsequent runtime decisions. We characterize these challenges as Structural Composability and Runtime Adaptivity. We present openJiuwen, an open-source harness designed for both developer composability and adaptive task execution. openJiuwen provides a shared execution substrate and Rail-based capability composition across single agents, delegated sub-agents, and Swarm Flow, enabling developers to construct sophisticated agent harnesses under common execution semantics. It further adapts framework-controlled runtime decisions around a fixed model policy, allowing evolving evidence to dynamically affect context, feedback, and task control toward successful completion. We systematically evaluate openJiuwen on SWE-bench Verified and Terminal-Bench 2.1, where it achieves 82.6% and 87.19%, respectively, exceeding the strongest selected official-leaderboard point estimates by 3.4 and 3.39 percentage points. These results show that openJiuwen achieves strong performance on complex coding tasks while providing a composable and adaptive harness design.

</details>


### 16. PCBnet: A Dataset and Automatic Construction of SPICE Netlists from Schematic Images

- **Authors:** Zhen Huang, Yuhao Gao, Yuzhi Liu, Daian Cheng, Chengyuan Shao, Yucheng Chen, Yongjian Jia, Futing Zhang, Yichen Shi, Wenhao Wang, Zuyan He, Yangbo Wei, Zhanfei Chen, Jinlong Yan, Yu Zhang, Haoying Wu, Ting-Jung Lin, Lei He
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27923v1](http://arxiv.org/abs/2608.27923v1)
- **PDF:** [https://arxiv.org/pdf/2608.27923v1](https://arxiv.org/pdf/2608.27923v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Printed circuit boards (PCBs) are fundamental to modern electronic systems, yet AI-driven PCB design automation remains constrained by the lack of large-scale paired schematic-netlist datasets. PCB schematics are particularly challenging due to diverse component types, complex wiring topologies, and noisy textual annotations. To address this gap, we present PCBnet, a large-scale PCB schematic dataset comprising over 300 real-world designs with annotated pins and paired SPICE netlists. It contains more than 50,000 component instances, 150,000 wires, 100,000 text regions, and 400,000 characters. We further develop an automated schematic-to-netlist pipeline that combines visual recognition, topology construction, and domain-knowledge-guided multi-agent correction. The proposed method achieves 94.54% component detection mAP, 98.57% text recognition accuracy, and 84.47% end-to-end connectivity accuracy. PCBnet provides a benchmark and data foundation for future AI-driven PCB design automation.

</details>


### 17. TACIT-Switch: Cost-Aware Model Escalation for LLM Agents from Censored Supervision

- **Authors:** Ji'an Lei, Jian Huang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27911v1](http://arxiv.org/abs/2608.27911v1)
- **PDF:** [https://arxiv.org/pdf/2608.27911v1](https://arxiv.org/pdf/2608.27911v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents with smaller language-model backbones are less expensive but can drift into persistent failure modes, whereas those with larger backbones are generally more reliable but more costly. This reliability-cost trade-off motivates routing methods that decide when to invoke an agent with a larger backbone: before execution, after a fixed trajectory prefix, or locally at individual steps. Our method, TACIT-SWITCH, learns permanent handoff policies from accumulated trajectory evidence and Teacher-Annotated Censored Intervention Times (TACIT). It represents each annotation as an interval-censored observation on a cumulative-risk scale. The resulting mixture-cure threshold model estimates the probability that the paired Strong rollout succeeds and, conditional on success, the handoff threshold; no teacher is required at deployment. In a mechanism-based multi-step simulation, TACIT-SWITCH improves success by 7.4-11.1 percentage points over task-level, step-level, and fixed-prefix routing baselines at comparable cost. Within that controlled simulation, ablations show that task features and cumulative trajectory risk provide complementary information. With operating points selected on development data, TACIT-SWITCH achieves the highest held-out success among learned policies on both ALFWorld (48.5% with 4B Cheap; 45.5% with 9B Cheap) and DABench (73.1%).

</details>


### 18. AI Alignment through a Game-theoretic Lens: A Survey

- **Authors:** Yanan Cai, Zhongrui Zhao, Zhigang Lu, Ickjai Lee, Wei Emma Zhang, Minhui Xue, Yihong Zhang, Shuchao Pang, Wei Xiang
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27910v1](http://arxiv.org/abs/2608.27910v1)
- **PDF:** [https://arxiv.org/pdf/2608.27910v1](https://arxiv.org/pdf/2608.27910v1)
- **Categories:** cs.AI, cs.CL, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models and increasingly capable AI agents are deployed in high-risk settings, aligning them with complex human values has become a central challenge. Existing alignment methods, while effective in improving helpfulness, harmlessness, and controllability, often struggle to capture real-world preferences that are context-dependent, non-transitive, and shaped by dynamic multi-party interactions. This survey reviews AI alignment through a game-theoretic lens. Specifically, it organizes recent progress around key game-theoretic elements and synthesizes the literature along three challenges: preference diversity, alignment priority, and temporal dynamics. This perspective clarifies where current alignment methods genuinely benefit from game-theoretic analysis, where the framework is looser, and what challenges remain in building robust, adaptive, and verifiable AI systems.

</details>


### 19. Low-Altitude Fluid Antenna Network with Multi-Agent Reinforcement Learning

- **Authors:** Tong Zhang, Yanfei Su, Shuai Wang, Wanli Ni, Chengzhong Xu, Huseyin Arslan
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27909v1](http://arxiv.org/abs/2608.27909v1)
- **PDF:** [https://arxiv.org/pdf/2608.27909v1](https://arxiv.org/pdf/2608.27909v1)
- **Categories:** cs.IT, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Low-altitude wireless networks (LAWNs) integrate terrestrial and aerial platforms to provide ubiquitous communication, sensing, and localization services for unmanned aerial vehicles (UAVs) and electric vertical takeoff and landing (eVTOL) aircraft. However, dynamic air-ground and air-air channels, abrupt blockages, and heterogeneous interference hinder the realization of this goal. Nevertheless, fluid antenna (FA), a cutting-edge multiple-input multiple-output (MIMO) technique, overcomes these challenges by reconfiguring antenna positions to unlock additional spatial degrees-of-freedom. In this paper, towards bringing low-altitude FA networks into reality, we study the fast and high-performance FA reconfiguration for low-altitude FA networks with multi-agent reinforcement learning (MARL). Specifically, we present an electromagnetic digital twin (EM-DT)-assisted MARL framework. To fill the sim-to-real gap, we introduce a two-stage transfer learning framework. Our case study shows that joint FA positions and beamforming optimization can enhance the system sum-rate by 118.5%, compared to the fixed position baseline. This gain comes from the dynamic millisecond timescale reconfiguration of FA arrays and the adaptive steering of beams toward aerial users with mobility.

</details>


### 20. Resource Constraints and Performance in Agentic AI Systems

- **Authors:** Amaz Salman, Malka Halgamuge, Teo Susnjak
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27886v1](http://arxiv.org/abs/2608.27886v1)
- **PDF:** [https://arxiv.org/pdf/2608.27886v1](https://arxiv.org/pdf/2608.27886v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Progress toward more autonomous AI increasingly depends on agentic systems that combine a language model with tools, memory, state management, and multi-step execution. These mechanisms shape both task capability and operational burden. We compare OpenClaw and NanoBot as complete agentic systems using a paired primary benchmark and a more detailed instrumented subset of paired prompts. In the primary benchmark, the rate of full task completion was 31% for OpenClaw and 25% for NanoBot, a six-percentage-point difference with a 95% task-bootstrap interval from -3 to 15 percentage points, providing no statistically established full-completion advantage for either system. In the instrumented layer, both systems achieved 26% full completion, while NanoBot reached at least partial completion on 43% of prompts compared with 26% for OpenClaw. OpenClaw took longer on 83% of prompts and had a higher recorded peak-memory value on every prompt, with geometric mean ratios of 2.98 for wall time and 19.44 for peak memory. Among the ten detailed-layer prompts on which at least one system achieved partial or full completion, NanoBot weakly dominated on eight; across all 23 prompts, however, ten of its eighteen dominance cases were cheaper joint failures. Outcome labels differ across the two evidence layers, showing why agent-system evaluation should connect capability and resource measurements to attempt-level execution and scoring provenance. These findings show that progress toward more autonomous AI should be evaluated through verified task completion, observed resource use and records linking each result to the execution that produced it.

</details>


### 21. FedEHR-Agents: Federated Agentic Optimization for Automated EHR Modeling

- **Authors:** Jun Bai, Ruilin Wang, Yue Li
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27856v1](http://arxiv.org/abs/2608.27856v1)
- **PDF:** [https://arxiv.org/pdf/2608.27856v1](https://arxiv.org/pdf/2608.27856v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models are enabling autonomous clinical agents to perform increasingly complex electronic health record (EHR) modeling workflows. However, agents deployed at individual hospitals remain constrained by institution-specific data and modeling environments, while direct cross-hospital collaboration is restricted by the sensitivity of patient-level EHR data. Although federated learning (FL) provides a natural foundation for privacy-preserving collaboration, existing approaches remain predominantly model-centric, limiting federation to prediction models or their updates while overlooking the richer modeling experience accumulated by autonomous agents. To address this limitation, we propose FedEHR-Agents, an experience-centric federated agentic optimization framework for automated EHR modeling. Each hospital deploys an autonomous clinical EHR agent that performs data preprocessing and model development while refining local clinical modeling experience through historical memory, task-specific evaluation, and TextGrad-based prompt refinement. The federated server performs evidence-guided experience aggregation to integrate reliable and complementary modeling experience across heterogeneous hospitals and distills the aggregated experience into global meta-prompts for subsequent local refinement. Extensive experiments on real-world multi-hospital EHR benchmarks demonstrate that FedEHR-Agents consistently outperforms local and federated baselines across diverse clinical prediction tasks and remains robust across different federation scales and LLM backbones. These results establish clinical modeling experience as a promising collaborative object beyond conventional parameter-centric FL and point toward federated autonomous clinical intelligence.

</details>


### 22. AcCoRD: Evaluating User-Agent Collaboration Under Realistic User Preference Dynamics

- **Authors:** Tejas Srinivasan, Shikib Mehri, Nandita Shankar Naik, Anirban Das, William M. Campbell, Jesse Thomason
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27818v1](http://arxiv.org/abs/2608.27818v1)
- **PDF:** [https://arxiv.org/pdf/2608.27818v1](https://arxiv.org/pdf/2608.27818v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

User preferences in user-agent collaboration are rarely static and fully-specified upfront: preferences are formed, revealed, adjusted, and relaxed during interaction. Existing benchmarks for evaluating user-agent collaboration focus almost exclusively on resolving underspecified preferences, thereby failing to capture the richer dynamics of real-world interaction. We introduce AcCoRD, a user-agent collaboration benchmark requiring agents to handle diverse user preference dynamics in two domains: online shopping and travel planning. We evaluate five frontier LLMs under two prompting strategies: vanilla ReAct, and an uncertainty-guided variant that prompts models to identify and resolve ambiguity about user preferences. Our results reveal that frontier models can handle underspecification but struggle to satisfy preferences that emerge or evolve mid-interaction and require more sophisticated uncertainty modeling. Further, prompting alone fails to elicit the required uncertainty recognition. We release AcCoRD as a resource for developing agents that can navigate the full complexity of real-world user preferences.

</details>


### 23. ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

- **Authors:** Yuqi Jia, Ruiqi Wang, Patrick Li, Yuepeng Hu, Peinian Li, Neil Gong
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27800v1](http://arxiv.org/abs/2608.27800v1)
- **PDF:** [https://arxiv.org/pdf/2608.27800v1](https://arxiv.org/pdf/2608.27800v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: (1) the agent selects the malicious tool for task execution, (2) the agent passes its runtime context as input arguments to the tool, and (3) the tool's implementation transmits these inputs to an attacker-controlled endpoint. Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration.
  In this work, we bridge this gap by developing ContextLeak, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

</details>


### 24. CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action

- **Authors:** Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27797v1](http://arxiv.org/abs/2608.27797v1)
- **PDF:** [https://arxiv.org/pdf/2608.27797v1](https://arxiv.org/pdf/2608.27797v1)
- **Categories:** cs.AI, cs.CL, cs.FL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Natural-language tasking of embodied agents is rarely just goal specification: users also impose constraints that must persist while the world changes. Code-generating LLM agents can produce plausible behaviors for such instructions, but their free-form programs provide no stable object to verify, compose with new constraints, or repair from a failing trace. We present CEDAR, a counterexample-guided framework that grounds instructions as regular languages over environment event traces. CEDAR uses a language model for semantic judgments and execution traces for correction, then represents both skills and specifications as deterministic finite automata. This turns constraints into executable finite-state objects: a learned skill can be intersected with a learned sleep at night or stay in this biome specification, yielding a controller that enforces the learned constraint by construction rather than by repeated prompting. In Minecraft, with the same simulator/API observations available to a program-generating baseline, CEDAR maintains temporal and spatial constraints that the baseline fails to preserve and amortizes reuse of learned skills, reducing cumulative LLM queries. These results suggest that regular languages offer a practical verification layer between natural-language instructions and embodied-agent policies.

</details>


### 25. ReToolSQL: Agentic Reinforcement Learning for Robust Text-to-SQL

- **Authors:** Pratik Kakkar, Chandra Dhir, Ravi Shankar, Pareekshit Reddy Gaddam, Anup Shirgaonkar
- **Published:** 2026-08-28
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27796v1](http://arxiv.org/abs/2608.27796v1)
- **PDF:** [https://arxiv.org/pdf/2608.27796v1](https://arxiv.org/pdf/2608.27796v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work has shown that reinforcement learning from execution feedback can substantially improve text-to-SQL performance, often enabling smaller models to match or exceed much larger systems. However, most existing approaches treat SQL generation as a single-turn task, limiting the model's ability to recover from errors through iterative refinement. We present ReToolSQL, a two-stage training framework for text-to-SQL that combines (i) a supervised warm-start on rejection-sampled reasoning traces with (ii) agentic reinforcement fine-tuning (RFT) over multi-turn tool-use trajectories. The key insight is that the two stages act on complementary axes, the supervised fine-tuning (SFT) on verified privileged-teacher traces expands the set of solvable questions (raising pass@k coverage on the hardest cases), while RFT converts that expanded capability into higher single-pass accuracy by teaching the model when to verify, what evidence to retrieve, and how to repair faulty SQL from execution feedback. Applied to Gemma 4 instruction-tuned (31B), RFT alone achieves 73.66% execution accuracy (EX) on the BIRD-SQL development benchmark (74.12% EX with self-consistency). Initializing RFT from the SFT checkpoint (SFT$\to$RFT) yields our strongest model at 74.32% EX single-pass and 74.77% EX with self-consistency. At the time of writing, this ranked first on the BIRD single-model development-set leaderboard. The approach uses composite rewards anchored on execution correctness, requires no human annotation beyond the benchmark itself, and operates within a single dense 31B model, showing that a properly designed SFT$\to$RFT pipeline over tool-use trajectories is a practical path toward robust enterprise-grade text-to-SQL.

</details>


### 26. The Calls are Coming from Inside the Model: Investigating Probe-based Detection of Tool-Calling Errors in LLMs

- **Authors:** Eric Yeats, Brendan Kennedy, Loc Truong, John Buckheit, Jung Lee, Jesse Friedbaum, John Emanuello, Henry Kvinge
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27750v1](http://arxiv.org/abs/2608.27750v1)
- **PDF:** [https://arxiv.org/pdf/2608.27750v1](https://arxiv.org/pdf/2608.27750v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The hidden states of large language models (LLMs) are known to capture rich information relating to model knowledge and behavior that can be hard to extract from examination of input and output alone. As LLM-based systems increasingly interface with the external world, one area of concern is detecting incorrect or improper use of tools. Motivated by this, we study the effectiveness of using linear probes to detect incorrect tool-calls, measuring probe efficacy across 18 tool-calling LLMs evaluated on the Berkeley Function Calling Leaderboard. Overall, we find that probing is an effective means to catch a range of different tool-calling errors, including errors arising from using an argument that has the wrong value but the correct type, which might not be recorded by standard logging frameworks. Important factors in success include model size, probing layer, and model post-training type. We also show that probes are capable of generalizing to novel types of errors, which is critical in real world deployments.

</details>


### 27. PCFBench: A Diagnostic Benchmark for Product Carbon Footprint Estimation

- **Authors:** Krishna Rao, Andrew Dumit, Shaena Ulissi, Jacob Feintzeig, P. James Joyce, Daniel Frank, Steven Watson, Jonathan Glidden, Gizem Ilayda Dinc, Travis M. Kwee
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27716v1](http://arxiv.org/abs/2608.27716v1)
- **PDF:** [https://arxiv.org/pdf/2608.27716v1](https://arxiv.org/pdf/2608.27716v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI systems are being deployed on high-stakes, domain-specific workflows that demand correctness not just in the final output, but at every intermediate step. One such workflow is estimating a product carbon footprint (PCF), the greenhouse-gas emissions attributable to a physical product. AI agents are increasingly being used to generate PCFs, but existing evaluations score either total emissions (hiding error sources and cancelling mistakes) or sub-tasks in isolation (missing compositional interactions). We introduce PCFBench, the first benchmark to carve PCF modeling into independently-evaluable tasks that require decomposition, retrieval, ontology matching, and numerical extraction. It comprises 614 expert-labelled items across six tasks. Together they probe reasoning under under-specification, conflicting context, and numerical constraints. Across eight frontier LLMs from four providers, no single model dominates. Although the strongest models estimate total product emissions within 2 times of declared totals on 77% of products, this rate drops to 37-58% when the PCF is generated step by step, with only 45-75% obeying mass conservation. These failures undermine the transparency practitioners need to compare products and drive decarbonization. We release the dataset and evaluation harness to support targeted progress.

</details>


### 28. Agents for Everyone: A Workshop Framework for Building Agentic AI Capabilities in a Distributed Curation Community

- **Authors:** Seth Carbon, Sierra Moxon, Kimberly Van Auken, Pascale Gaudet, Christopher J. Mungall
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27675v1](http://arxiv.org/abs/2608.27675v1)
- **PDF:** [https://arxiv.org/pdf/2608.27675v1](https://arxiv.org/pdf/2608.27675v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI has the potential to accelerate curation of biological databases and knowledge bases. However, uptake has been hindered by a number of challenges and obstacles, including access to agents and appropriate training. Here we describe how we have attempted to address and mitigate these challenges and obstacles through the deployment of a cloud-based agentic environment, and the development of an interactive training workshop for the Gene Ontology Consortium. Our cloud environment for agentic-assisted curation was based on the JupyterHub platform, and utilized Claude Code as a universal harness. This allows curators to interact with an agent session through a terminal running in the browser, and has additional benefits such as centralization of access through a single API gateway, removing the need for participants to manage subscriptions or install software locally. We created four training modules, walking participants through basic agentic tool use first and then working up to agentic biological pathway curation using the existing GO-CAM (GO Causal Activity Model) curation tool. Thirty-seven participants took part in the four-hour workshop. Our key takeaway from this workshop is that building community capability with agentic AI is primarily a problem of access, workflow design, and training. Removing technical barriers, introducing capabilities gradually, grounding exercises in familiar curation tasks, and giving curators direct experience evaluating agent output can provide a practical route toward building shared agentic AI capability in distributed scientific communities.

</details>


### 29. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

- **Authors:** Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27454v1](http://arxiv.org/abs/2608.27454v1)
- **PDF:** [https://arxiv.org/pdf/2608.27454v1](https://arxiv.org/pdf/2608.27454v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills package specialized knowledge and workflows into reusable resources that extend AI agent capabilities. Recent work automatically discovers such skills from agent experience, which enables agents to progressively adapt through interaction. However, the insights that guide skill development typically remain scattered across optimization histories, limiting their systematic reuse across iterations. We introduce WikiSkill, a framework that co-evolves agent skills with a persistent knowledge base (wiki). At a high level, WikiSkill separates raw execution experience, accumulated knowledge, and executable skills, while continuously consolidating experience into the wiki, which subsequent skill updates can build on. Across diverse benchmarks and models, WikiSkill consistently outperforms state-of-the-art skill-evolution methods and improves over no-skill baselines in most model-benchmark settings. We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them. We also find that evolved skills transfer effectively across models and model families, and skills evolved by other models can outperform self-evolved skills. Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution. These results demonstrate the benefits of systematically accumulating and refining agent experience for developing reusable and transferable skills.

</details>


### 30. Persona-Execution Separation: An Architecture Pattern for Evolving LLM Agents under Execution Audit

- **Authors:** Yisen Xi
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27427v1](http://arxiv.org/abs/2608.27427v1)
- **PDF:** [https://arxiv.org/pdf/2608.27427v1](https://arxiv.org/pdf/2608.27427v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents in governed organizations must let the persona (instructions, tone, self-presentation) evolve freely, while keeping execution (stateful, audited work) traceable. A single trust domain does not satisfy both cheaply. We present Persona-Execution Separation (PES): persona and execution reside in different trust domains, connected by a governed contract bridge. The persona is singly-homed and may drift; execution is faceless and audited. Status summaries may return; data bodies remain in the restrictive domain except a graded data-loss-prevention (DLP) exception; identity stays continuous. An approval matrix, DLP, and audit enforce the crossing. PES follows from three goals---free drift, execution traceability, and decoupling. Under LLM representational indistinguishability, any single-domain mechanism that meets all three must re-introduce typed change objects, an external gate, and a stable audit anchor: PES rebuilt at higher coupling cost. A development/pilot case in a regulated digital-employee platform records five decisions over one month, each with a rejected alternative. A mechanism check on the shipped implementation found no execution-side re-validation under persona perturbation (five model configurations) and no persona fingerprint on hard-asserted fields. A probe of a recovered pre-separation build found the governed execution path decoupled from the persona by omission, not by construction; a later wiring change could reverse that isolation, which PES makes an audited architectural rule. The pattern applies when multi-user deployment, execution audit, and expected persona churn hold jointly.

</details>


### 31. INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment

- **Authors:** Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, Xiaoping Zhang, Han Qiu
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27348v1](http://arxiv.org/abs/2608.27348v1)
- **PDF:** [https://arxiv.org/pdf/2608.27348v1](https://arxiv.org/pdf/2608.27348v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) are deployed as autonomous agents, safety failures increasingly involve consequential actions. We study agentic misalignment, where agents take harmful actions under goal conflicts and pressures. Using chain-of-thought (CoT) monitoring, we find that harmful execution is often preceded by intent signals in reasoning. However, post-hoc CoT labels are too coarse to show how intent changes during generation. We introduce INTENT-AS-A-TOOL, an approach that adds intent-targeted tools to give the model a dedicated channel for expressing commitment to a target behavior. The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior. Our results show that INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention. These findings suggest that action preferences are useful for tracking agentic misalignment during reasoning. Our code and data are accessible: https://github.com/RebeccaZhang22/intent-as-a-tool.

</details>


### 32. One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles

- **Authors:** Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, Xiyuan Yang, Chaosheng Dong, Haiyang Zhang, Hanghang Tong
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27338v1](http://arxiv.org/abs/2608.27338v1)
- **PDF:** [https://arxiv.org/pdf/2608.27338v1](https://arxiv.org/pdf/2608.27338v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Specializing Large Language Models (LLMs) toward distinct abilities underpins successes ranging from personalized assistants to multi-agent systems (MAS). Single-agent paradigms rely on pre-defined personas or steering vectors to induce specialization, yet they impose a single fixed specialization that fails to adapt to diverse queries. Conversely, MAS achieves dynamic multi-perspective problem solving by orchestrating agents with distinct text-based roles, but fusing these specializations requires multi-turn interactions that inflate context length and inference cost. To address these limitations, we propose Mixture of Roles (MoRe), which adaptively composes multiple specializations into a single steering vector for single-turn inference. Specifically, MoRe learns a diversified codeboox of steering vectors, each of which encodes a latent role. A query-aware router dynamically fuses the codebook into a steering vector that encompasses multiple roles. By steering the backbone LLM with the composed vector, MoRe enables multi-perspective specialization in a single-agent, single-turn inference process. The proposed MoRe can be efficiently trained via a three-stage SFT curriculum and GRPO post-training, while the backbone LLM remains frozen. Experiments across reasoning and personality benchmarks show that MoRe outperforms single-agent baselines by 2.2% on average, and achieves performance on par with MAS while reducing token cost by 20x.

</details>


### 33. Naive Prompt Optimization: Rethinking the Need for Complex Prompt Search

- **Authors:** Yuan Chang, Xiaoqi Chen
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27266v1](http://arxiv.org/abs/2608.27266v1)
- **PDF:** [https://arxiv.org/pdf/2608.27266v1](https://arxiv.org/pdf/2608.27266v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Efficiently improving autonomous agents across diverse tasks is central to accelerating recursive self-improvement (RSI) in agentic AI, with prompt optimization emerging as a promising approach capable of delivering performance gains comparable to those achieved by fine-tuning model weights, while reducing computational costs in both optimization and serving. However, recent developments increasingly favor unnecessarily complex prompt optimizers. We introduce Naive Prompt Optimization (NPO), a lightweight single-lineage method that iteratively revises prompts using a teacher model with rollout feedback. NPO achieves comparable or better performance than GEPA with fewer rollouts, and its advantage increases with stronger teacher models, suggesting that stronger teacher reasoning can partially substitute for optimizer-side search complexity. In interactive games, NPO remains broadly competitive with GEPA, while GRPO performs better on some tasks less amenable to prompt optimization. We also show that NPO-optimized prompts elicit similar performance improvements when applied verbatim to other student models, especially across models within the same family. Overall, our preliminary results show that simple, linear prompt optimization can rival substantially more sophisticated and complex search procedures.

</details>


### 34. What Makes Good Agentic Data? An ACE Lens on Data Generation for LLM Agents

- **Authors:** Xingshan Zeng, Zishan Xu, Boju Zhang, Yuzhou Wu, Lingzhi Wang, Jianghao Lin, Liangyou Li, Yasheng Wang, Lifeng Shang, Xin Jiang, Weinan Zhang, Yong Yu, Qun Liu, Weiwen Liu
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27260v1](http://arxiv.org/abs/2608.27260v1)
- **PDF:** [https://arxiv.org/pdf/2608.27260v1](https://arxiv.org/pdf/2608.27260v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on generated interaction data to learn how to interact with external environments. Agentic data generation must maintain consistency among environments, tasks, interactions, and success signals while producing experience that is useful rather than merely abundant. Existing work spans many agent domains, but domain-centered organization and heterogeneous evaluation often obscure common generation mechanisms and conflate candidate construction with verification and selection. This work develops a two-level framework for the field. First, we represent agentic data as a common factorized object $(E,q,τ,v)$, comprising an environment specification, task signal, interaction realization, and optional verifier. We organize generation paradigms by their primary anchor and dependency structure. Second, we formulate generation as constrained distribution design through the Accuracy-Complexity-divErsity (ACE) lens. Accuracy establishes the feasible support of grounded and internally consistent data. Within this support, Complexity places learning mass relative to the capability of a declared learner and execution configuration, while divErsity controls coverage and redundancy of data. Using this framework, we explore how prior work verifies generated experience, constructs and calibrates difficulty, and expands behavioral coverage. The literature reveals a shift toward execution-grounded accuracy, learner-relative complexity, and diversity beyond surface variation or dataset size. We further discuss broader directions and emerging trends in agentic data generation through the ACE lens, including their implications for scaling, data sources, training regimes and adaptive learning. Overall, the central challenge is not simply to generate more data, but to continually allocate valid, informative, and non-redundant experience as agents and environments evolve.

</details>


### 35. TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause Attribution

- **Authors:** Tommaso Bendinelli, Artur Dox, Christian Holz
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27182v1](http://arxiv.org/abs/2608.27182v1)
- **PDF:** [https://arxiv.org/pdf/2608.27182v1](https://arxiv.org/pdf/2608.27182v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly applied to anomaly detection and root-cause analysis in time-series observations collected from real-world systems; however, their performance on these tasks has not been systematically evaluated under controlled conditions. We introduce TraceBench, a simulation-based framework for generating controlled root-cause attribution tasks. In each generated task, an agent receives time-series observations produced by simulating a physical dynamical system and must determine whether a system parameter was altered during the simulation and, if so, which one. Using TraceBench, we generate tasks from three interpretable mechanical systems and systematically evaluate four LLM agents across controlled experimental conditions, yielding new insights into how these agents analyze time-series observations from dynamical systems. Our results show that agents benefit substantially from domain context and explore data primarily through numerical console output rather than visualizations. We also find that agents generally perform worse when required to produce a Python script that maps each time-series sample to a predicted root-cause label than when they submit predictions directly. We release our datasets, agent trajectories, experimental results, and a leaderboard on our website, tracebench.github.io.

</details>


### 36. Calibrated Enough to Know, Not Calibrated to Act: Fabricated Evidence Makes LLM Agents Commit to the Unknowable

- **Authors:** Pranav Aggarwal
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27167v1](http://arxiv.org/abs/2608.27167v1)
- **PDF:** [https://arxiv.org/pdf/2608.27167v1](https://arxiv.org/pdf/2608.27167v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent shown a professional-looking market panel commits to a directional call on a provably unpredictable question far more often than one asked the bare question: across 12 frontier models, commitment rises from 6.5% to 54.0% as evidence is escalated. It commits just as readily when every number on the panel is invented: fabricating the entire display, so nothing the model can see is true except the question itself, still lifts commitment from 24.5% to 36.8%, statistically indistinguishable from the 37.6% produced by genuine market data. What unlocks confident action is not information but the authority of its packaging. The failure is narrow and locatable. Incapacity is not the answer: on matched answerable questions attached to the same panels, the same models answer essentially always, at near-perfect accuracy. Nor is it belief - stated probabilities barely move across the gradient that swings action by 48 points, and score worse than a climatological baseline. Missing judgment isn't it either: asked to classify a question's knowability before acting, models call it irreducible 90% of the time and then commit on just 0.4% of those. The act/don't-act gate is what fails, and the effect is concentrated in a few models rather than universal. Because the gate is separable, it can be trained. Supervised fine-tuning of a 3B model on 540 synthetic cases, predominantly dice, coins, jars and timers, drives commitment to 0.0% on the original cases and transfers to three unseen domains. It does not survive everything: the gate holds exactly when the response format leaves room to reason, and rigid formats that remove that room leave the model confident and wrong on questions it otherwise answers correctly. The gate is trainable and context-fragile, and deployment needs both halves of that sentence.

</details>


### 37. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents

- **Authors:** Xiaokun Guo, Zhen Xu, Dongdong Huo, Yanqiu Zhang, Wei Wang, Qinfu Yang, Dongjin Yu, Yu Wang
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27146v1](http://arxiv.org/abs/2608.27146v1)
- **PDF:** [https://arxiv.org/pdf/2608.27146v1](https://arxiv.org/pdf/2608.27146v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-augmented LLM agents must rely on untrusted runtime Observations to complete open-ended tasks; however, when tool outputs no longer merely provide data but begin to specify concrete actions, they effectively become ``commands'' that can drive real-world side effects beyond user intent. We argue that this risk arises from conflating action induction with execution authorization. To address this distinction, we propose SARA, which treats action induction and execution authorization as distinct runtime roles and separates action provenance from execution authority. On the Observation side, a context-isolated Action Probe exposes action-inducing semantics and persistently records action-origin provenance across steps as a review signal; on the execution side, actual tool calls are authorized only against the user objective and audited evidence from authorized successful executions, while satisfying goal, execution-chain, and argument-level support. To preserve this separation across multi-step execution, SARA applies No-History-Promotion to prevent historical recurrence from laundering action origins into execution authority. Across AgentDojo and AgentDyn, SARA limits ASR to no more than \(0.63\%\) across four primary evaluation settings while maintaining competitive task utility, and consistently reduces ASR across additional Agent backbones.

</details>


### 38. GRAIN: Bridging Name and Narrative Shifts in Real-World Graph Reasoning through Invariance-Rewarded Agentic RL

- **Authors:** Zike Yuan, Han Zhang, Jianzhi Yan, Le Liu, Cai Ke, Huozhi Zhou, Jian Xie, Jiran Yin, Yukun Cao, Yue Yu, Hui Wang, Ming Liu, Bing Qin
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27142v1](http://arxiv.org/abs/2608.27142v1)
- **PDF:** [https://arxiv.org/pdf/2608.27142v1](https://arxiv.org/pdf/2608.27142v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite their potential in standardized graph tasks, Large Language Models (LLMs) remain brittle to real-world shifts in node identifiers and task formulation. While deterministic graph tools are invariant to such shifts, extracting topological structures from noisy text is highly fragile for LLMs, which often overfit to surface patterns. Moreover, mitigating these parsing failures via multi-agent systems incurs prohibitive latency. To address this, we propose GRAIN, a single-agent framework optimized via reinforcement learning. GRAIN models reasoning as a semantic parsing and tool-execution pipeline, guided by a Structure Invariance Reward. By validating extracted intermediate graphs against ground-truth topologies, this reward forces the LLM to learn robust text-to-structure mappings rather than memorizing linguistic artifacts. We also introduce GRIT, a benchmark evaluating sensitivity to such linguistic shifts. GRAIN outperforms multi-agent baselines by 16.45\% in accuracy with approximately 24\% lower latency. Furthermore, it demonstrates superior structural generalization, halving the out-of-distribution (OOD) gap of SFT models (from 15.77\% to 7.80\%) and maintaining robustness on large-scale graphs beyond the training distribution.

</details>


### 39. Safety Does Not Compose: Non-Decaying Loop State for Autonomous LLM Agents

- **Authors:** Chenhao Wu, Haoxuan Jia, Yang Liu, Yingguang Yang, Yuhan Lin, Chongyang Zhang, Hao Zheng, Yulin Huang, Jianshen Zhang, Yongzhi Qi, Shang Luo, Kefu Xu, Jifeng Zhu, Bin Chong
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27141v2](http://arxiv.org/abs/2608.27141v2)
- **PDF:** [https://arxiv.org/pdf/2608.27141v2](https://arxiv.org/pdf/2608.27141v2)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents are increasingly deployed as autonomous loops. Starting from one human goal, such a system repeatedly discovers work, plans, executes tool calls, verifies outcomes and persists state across many unattended iterations. The agent safeguards in wide use, however, are defined over a single trajectory, and their safety state is re-initialized when the next trajectory begins. We show that this is a failure of composition rather than an implementation detail. Our central result is a separation: against an attack whose evidence is fragmented across several iterations, every trajectory-scoped monitor has a true-positive rate equal to its false-positive rate, however expressive it is, because the evidence it would need never appears in the window it sees, whereas a monitor retaining cross-iteration state separates the two perfectly. We further show that the obvious repair of carrying a geometrically decaying risk score is insufficient, because the cooling-off period a patient adversary must wait is a constant that does not grow with the horizon $N$. We then present LoopHarness, which restores a persistent, non-decaying safety state at the loop level. Under mediated commits and an arbiter detection floor $δ_M$, it bounds the expected number of unauthorized irreversible actions by $B+m-1+m/δ_M$, a constant in $N$, of which the $B+m-1$ term is decided by a model-free rule and therefore survives a fully colluding verifier. We give a complete evaluation protocol on native Agent-SafetyBench tasks with paired clean and attacked episodes, an outer-state attack suite whose decisive evidence exists only across iterations, per-module ablations, and an adaptive white-box red team.

</details>


### 40. TransMeme: A Multi-Agent Framework for Cross-Cultural Meme Transcreation

- **Authors:** Jingyi Zheng, Yule Liu, Zifan Peng, Tianyi Hu, Yuemeng Zhao, Xinhu Zheng, Xinlei He
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27127v1](http://arxiv.org/abs/2608.27127v1)
- **PDF:** [https://arxiv.org/pdf/2608.27127v1](https://arxiv.org/pdf/2608.27127v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Internet memes are a pervasive form of multimodal online communication; however, such communication often involves users from diverse linguistic and cultural backgrounds. Therefore, adapting memes across cultures and languages is a central challenge for enabling mutual understanding in online communication. Unlike ordinary translation or standalone text rewriting, cross-cultural meme transcreation must jointly preserve communicative intent, adapt culture-dependent meaning for the target audience, and maintain coherence between text and image. In this work, we first provide an explicit task analysis of cross-cultural meme transcreation and identify three core challenges: culture-specific knowledge understanding, intent and tone preservation, and multimodal consistency. Based on this analysis, we propose a multi-agent framework with specialized agents that are coordinated to address these challenges through cultural adaptation, target text rewriting, revision, and conditional visual adjustment. The framework strengthens target text adaptation with coordinated feedback to handle difficult cases that require deeper cultural or visual intervention. We evaluate the framework on bidirectional Chinese-English meme transcreation using both human evaluation and LLM-as-a-Judge. Our method consistently outperforms all baselines across both evaluation settings. In human evaluation, it achieves the best performance on all four dimensions and delivers a 33.1% average improvement over the strongest baseline, while in LLM-as-a-Judge, it attains the highest Top-1 ranking rate (60% versus 26% for the second-best baseline). Further analysis indicates that each component contributes to the performance. Our error analysis suggests that the remaining bottlenecks lie in humor reconstruction and image-text alignment rather than simple cultural knowledge gaps, pointing to future work on humor transfer.

</details>


### 41. FaulT-Bench: Towards Benchmarking Network Troubleshooting LLM Agents under Unreliable User Tickets

- **Authors:** Kuan-Hao Tseng, Niruth Bogahawatta, Yasod Ginige, Kunjan Patel, Kosta Dakic, Suranga Seneviratne
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.27021v1](http://arxiv.org/abs/2608.27021v1)
- **PDF:** [https://arxiv.org/pdf/2608.27021v1](https://arxiv.org/pdf/2608.27021v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are increasingly proposed for network fault diagnosis, but existing benchmarks evaluate them only on accurate tickets and always assume a fault is present, conditions rarely met in practice. We present FaulT-Bench, a benchmark of 200 troubleshooting scenarios across eight network topologies, five reimplemented from public practitioner labs, spanning genuine faults, false fault reports, incorrect device attribution, and incorrect root-cause claims. To isolate how ticket wording affects diagnosis, we further rewrite 72 false-premise tickets into five reporter personas that vary reporter confidence and verifiable detail one factor at a time, holding the network state fixed. Our automated harness deploys each scenario in Kathará, lets agents interact through the NIKA tool interface, and scores free-text diagnoses with an LLM judge across outcome, fix, and reasoning quality. Evaluating SADE, ReAct, and Claude Code, we find all three are near-saturated on accurate tickets and robust to misdirection, yet degrade sharply when the network is healthy and the ticket is wrong, probing until a benign condition can be promoted to a root cause rather than concluding nothing is wrong. Persona rewrites show that how a ticket is written matters more than what it claims: a confidently wrong report is handled about as well as an accurate one, while a vague, underspecified report degrades performance sharply. The three agents also fail differently, from constant over-diagnosis to unanswered runs, at very different cost. These results position FaulT-Bench as a benchmark for developing agentic systems that can reason reliably over the noisy, unreliable tickets of real-world network troubleshooting.

</details>


### 42. DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research

- **Authors:** Linsen Zhu, Yi Shi
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26990v1](http://arxiv.org/abs/2608.26990v1)
- **PDF:** [https://arxiv.org/pdf/2608.26990v1](https://arxiv.org/pdf/2608.26990v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models can summarize financial information, but an operational stock-research system must first assemble heterogeneous evidence, expose unavailable data and model capabilities, and control how generated opinions affect a final report. We present DSA, an evidence-aware orchestration framework for multi-market stock research with large language model (LLM) agents. DSA organizes the workflow into evidence acquisition, structured context construction, model-routed analysis, optional role and Strategy Skill reasoning, and report generation with selected context and diagnostics. A default report profile and an optional agentic profile share evidence and model-routing services but use profile-specific output validation and risk safeguards. In the agentic profile, core role outputs are processed by role-specific parsers, whereas Strategy Skill opinions undergo an additional signal-eligibility partition before synthesis; disagreement is supplied explicitly to the decision agent, followed by a conservative risk override. The reference implementation includes six regional market paths, fifteen bundled Strategy Skills, hosted and local model routes, and multiple execution and delivery surfaces. At a frozen software snapshot, a selected manifest of 1,457 portable offline backend contract tests passed; 596 cases were retrospectively mapped to six contract families central to the reported LLM-agent architecture. This evidence establishes implementation conformance for the tested software contracts, not superior report quality, forecasting accuracy, or investment returns.

</details>


### 43. Dynamic Haven Selection for Multi-Agent Pickup and Delivery in Constrained Warehouses

- **Authors:** Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji, Itsuki Noda
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26939v1](http://arxiv.org/abs/2608.26939v1)
- **PDF:** [https://arxiv.org/pdf/2608.26939v1](https://arxiv.org/pdf/2608.26939v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Space-efficient warehouse layouts often contain single-agent-width aisles and dead-end workstations where robots have few places to wait without blocking others. In Multi-Agent Pickup and Delivery (MAPD) on such constrained layouts, robots must accept online pickup-delivery tasks while preserving protected waiting locations called Havens. The Safe HAven Retreat Planner (SHARP) introduced a mechanism that extends each committed task path with a validated retreat to the agent's dedicated initial Haven, but fixed-Haven commitments can send agents toward distant Havens after deliveries. We present A-sharp (Adaptive SHARP), which changes an agent's retreat target at task assignment time. A naive switch can cause two agents to rely on the same waiting location or let another committed path pass through a location that is still occupied or reserved. A-sharp prevents these failures with an availability test for candidate Havens and a pending-release rule that keeps the previous Haven protected until the agent departs. Under explicit Haven-structure and Safe Interval Path Planning (SIPP) assumptions, we prove invariant preservation and finite-release completeness: every task in any finite release sequence is delivered in finite time. Across 72,000 runs on 14,400 paired map-agent-count-rate-seed cases over four maps, both SHARP and A-sharp complete their respective 14,400 runs. For makespan (final delivery time), a prespecified paired comparison with Holm correction over all 138 configurations with more Havens than agents finds A-sharp significantly better in 107 configurations and never significantly worse than SHARP; on the tested tree map, the median reduction is 16.7%.

</details>


### 44. Counterfactual Bias Testing for Application Tracking System

- **Authors:** Sai Yashwant, Shruti Bansal, Anurag Dubey, Samaroha Chatterjee, Satyam Kumar, Shreyash Gupta, Gantala Thulsiram
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26899v1](http://arxiv.org/abs/2608.26899v1)
- **PDF:** [https://arxiv.org/pdf/2608.26899v1](https://arxiv.org/pdf/2608.26899v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated candidate-job matching systems are increasingly classified as high-risk AI under emerging regulation, yet auditing them for demographic bias is expensive: classical correspondence-audit studies require hand-crafted resumes and manual submission, which does not scale to fast pipeline retraining cycles. This paper presents a general, reusable methodology that (1) uses task-specialized LLM agents to synthesize identity-neutral base resumes and inject controlled demographic treatments across five protected-characteristic axes (sex/gender, age, residence, language, disability), producing a K x (1+N) correspondence-audit matrix; (2) qualitatively flags inferred protected characteristics per an EU AI Act-aligned prompt; (3) ranks candidates against a job description via a fine-tuned sentence-embedding model and cosine similarity; and (4) computes a nine-metric fairness suite spanning counterfactual (score delta, mean absolute rank change, flip rate), group-fairness (top-K retention, four-fifths/impact ratio), and merit-aware (Recall@K, nDCG@K, equal opportunity, equalized odds) families, each with bootstrap confidence intervals, significance tests, and Benjamini-Hochberg correction, culminating in an automated PASS/INVESTIGATE/FAIL report with a composite risk score. On an example corpus of 5 job orders, 100 base candidates, and 10 demographic treatments (90 metric x variant evaluations): score shifts, top-K retention, and merit-aware rate gaps stay within tolerance for every treatment, but a rank-stability metric (MARC) and nDCG@K each surface borderline findings - including one on the neutral baseline itself - that a score- or retention-only view would miss. The results argue for multi-metric, multi-family auditing over any single aggregate score, and for LLM-agent-generated audits as a practical, low-cost complement to human-curated audits for any candidate-job matching pipeline.

</details>


### 45. AI agents in Algorithmic Electricity Markets: On the Emergence of Tacit Collusion

- **Authors:** Jakub Seredyński, Georgios Tsaousoglou
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26896v1](http://arxiv.org/abs/2608.26896v1)
- **PDF:** [https://arxiv.org/pdf/2608.26896v1](https://arxiv.org/pdf/2608.26896v1)
- **Categories:** cs.AI, cs.GT, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

As electricity market participants increasingly adopt learning-based agents for their bidding strategies, electricity markets are becoming algorithmic. Evidence from algorithmic markets in other domains shows that tacit collusion can arise purely through independent learning. Moreover, electricity markets are typically oligopolistic and feature repeated interaction among a small number of participants, making them structurally susceptible to non-competitive behavior. In the face of these observations, this paper investigates the hypothesis that tacit collusion may emerge in electricity markets where participants' actions are controlled by autonomous learning-based algorithms. We model strategic bidding as a repeated game with imperfect public monitoring, and model the participants' emergent behavior using multi-agent reinforcement learning. We propose a multi-dimensional set of criteria (going beyond profit comparisons against Nash equilibria) to assess whether the resulting behavior constitutes tacit collusion. Our experimental results showcase that such a danger is realistic for electricity markets: there are cases where agents do learn to sustain supra-competitive outcomes that are supportive of tacit collusion indicators, even though the agents were never instructed to collude.

</details>


### 46. PLCBench: Can Autonomous LLM Agents Turn PLC Access into Sustained Physical Impact?

- **Authors:** Yitian Zhou, Jingyu Zheng, Qiliang Jiang, Linkang Du, Haoming Liu, Lichao Wu, Shiyi Zhao, Mengxiang Liu, Ruilong Deng
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26882v1](http://arxiv.org/abs/2608.26882v1)
- **PDF:** [https://arxiv.org/pdf/2608.26882v1](https://arxiv.org/pdf/2608.26882v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Industrial control systems (ICSs) rely on programmable logic controllers (PLCs) to connect networked computation with physical control. Tool-using large language model (LLM) agents represent an emerging attack threat: can an autonomous agent convert a network-reachable PLC into sustained adverse physical impact? However, existing evaluations focus on digital tasks or individual stages of PLC testing. In ICSs, evaluations that stop at software exploitation, an accepted write, or tool access may therefore mischaracterize physical risk.
  We present PLCBENCH, to our knowledge, the first real-PLC hardware-in-the-loop (HIL) framework for characterizing this cyber-to-physical capability and its boundaries. It combines vendor-native interaction, commercial PLC execution, closed-loop reduced-order process simulation, and independent outcome verification. A deterministic evaluator applies fixed rules to runner, communication, PLC-object, and process records to assign six hidden diagnostic flags, distinguishing usable PLC interaction, process-linked manipulation, and sustained physical impact. We instantiate PLCBENCH on four commercial PLCs crossed with four closed-loop workloads. Across five LLM families and 240 real-PLC episodes, 75 episodes (31.3%) sustain their respective physical objectives. Stagewise results show that 98 episodes stop before a valid native read, whereas 62 reach a process-linked write but do not sustain the final objective. Notably, richer process observation is associated with an increase in conditional objective attainment after a process-linked write from 44.2% to 64.0%. These measurements localize failure in configured PLC-process deployments and identify intervention points for future defense evaluation. To support reproducibility, we release the safely disclosable PLCBENCH code and a software-only reproduction pipeline through the accompanying artifact.

</details>


### 47. BekchiAI: Measuring, Observing, and Controlling LLM Agents in One Click

- **Authors:** Mesut Toruk
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26867v1](http://arxiv.org/abs/2608.26867v1)
- **PDF:** [https://arxiv.org/pdf/2608.26867v1](https://arxiv.org/pdf/2608.26867v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents reason, call tools, and act autonomously over many steps, but their agentic skills-correctly sequencing tools, planning under dependencies, judging untrusted inputs, and grounding generated arguments-are hard to measure with accuracy-only leaderboards. We present BekchiAI, which addresses both sides: a benchmark for measuring agentic skill and a platform for observing and controlling live agents. The BekchiAI-Benchmark, a suite of 13 tool-using ReAct agents across 7 task categories (arithmetic, structured/SQL, security detection, URL grounding, planning, orchestration, and tool-policy), totalling 2,057 deterministic, committed test tasks. Every task is verifier-checkable gold answers are computed by running canonical SQL against a real database, computing the exact schedule of a directed acyclic graph (DAG), or evaluating closed-form lambdas including adversarial security samples paired with deliberately imperfect signature scanners so a score reflects the model's own judgment, not the copying of an oracle. We define a small set of behavioral metrics beyond accuracy-tool-call adherence, URL hallucination and source-match, and per-model token cost and report a four-model comparison (Qwen3.7-Max, gemma-4-31B-it, gemma4:26b, gpt-oss-120b) whose story is in the per-family spread, not the aggregate. The benchmark runs are executed using the provided evaluation scripts. BekchiAI-Platform is a complementary web-based observability and control layer for deployed agents, providing full token and latency telemetry as well as remote run termination. The benchmark, evaluation tools, and platform are publicly released.

</details>


### 48. LiveSim: Simulating Environment-Shaped Users in Multi-Agent Live-Stream Ecosystems

- **Authors:** Jiaqi Xu, Yiran Qiao, Jing Chen, Qiwei Zhong, Xiang Ao, Xueqi Cheng
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26849v1](http://arxiv.org/abs/2608.26849v1)
- **PDF:** [https://arxiv.org/pdf/2608.26849v1](https://arxiv.org/pdf/2608.26849v1)
- **Categories:** cs.AI, cs.CY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

User behavior simulation with large language models~(LLMs) is increasingly used to support multi-agent ecosystem simulation. Existing simulators typically rely on static user profiles inferred from historical observations, which become inadequate in socially intensive environments such as live streaming where interaction dynamics continuously reshape user behavior. We propose \textbf{LiveSim}, an LLM-based framework for live-stream ecosystem simulation. It represents users as editable behavioral hypotheses and progressively refines them through trajectory-grounded interactions, where discrepancies between simulated and observed trajectories reveal missing environmental shaping effects. These signals are further extracted as transferable environment-behavior patterns and accumulated in a collective behavioral memory to improve user-level behavioral fidelity and support ecosystem-level simulation. Experiments on real-world live-stream risk-control data validate the effectiveness of LiveSim in improving user-level behavioral fidelity and enabling ecosystem-level analysis of risk evolution and platform intervention effects.

</details>


### 49. Decoupling Planning and Control for Instructable Agents

- **Authors:** Zineng Tang, Kelsey R. Allen, Sjoerd van Steenkiste, Ishita Dasgupta, Alane Suhr
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26788v1](http://arxiv.org/abs/2608.26788v1)
- **PDF:** [https://arxiv.org/pdf/2608.26788v1](https://arxiv.org/pdf/2608.26788v1)
- **Categories:** cs.AI, cs.CL, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work shows that pre-trained, instruction-tuned vision-language models (VLMs) perform well at mapping from instructions and observations to high-level plans, but struggle to realize such plans as reliable low-latency action sequences in unfamiliar environments. At the same time, world-model controllers excel at fast observation-to-action control, but lack open-ended task guidance. In this work, we combine these strengths into a single system, Instruct-to-Act, where we train a world-model controller to act autonomously at high frequency when conditioned on sparse, higher-latency, and high-level text instructions generated by a VLM planner. To train controllers to be language-instructable, we relabel segments of controller policy rollouts with synthetic instructions and jointly optimize a behavior-cloning objective along with existing reward-maximizing and world-modeling objectives. We evaluate our proposed approach across seven embodied environments, including three multi-agent environments where VLM planners coordinate through language while trained controllers serve as their actuators. Under matched observation and action spaces, our decoupled approach consistently outperforms controller-only and direct VLM action-generation variants, preserves fast control, and lets us swap in different pretrained VLM planners without fine-tuning, while remaining competitive with strong vision-language-action and multi-agent RL baselines on six of seven tasks.

</details>


### 50. Fixed-Haven Reservation for Online Multi-Agent Pickup and Delivery in Dense Warehouses

- **Authors:** Taisei Hirayama, Kohei Yoshida, Hiroki Sakaji, Itsuki Noda
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26759v1](http://arxiv.org/abs/2608.26759v1)
- **PDF:** [https://arxiv.org/pdf/2608.26759v1](https://arxiv.org/pdf/2608.26759v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Dense warehouses often contain single-lane aisles, dead ends, and tree-like guidepaths that leave little room for idle agents to wait without blocking others. Existing Multi-Agent Pickup and Delivery (MAPD) guarantees for completing all finitely released tasks typically rely on extra waiting endpoints that planned paths can avoid, or on biconnected topology; these assumptions may fail in such layouts. We study fixed-Haven reservation for online MAPD, where pickup-delivery tasks are released over time. Each agent owns a fixed Safe Haven (Haven for short), usually its start cell, that only the owner may occupy and that other agents treat as blocked. For finite task releases, we prove that this fixed-Haven contract completes all released tasks under Haven-Reachability and explicit planning/progress assumptions. We implement the contract in SHARP, a Safe-Haven Retreat Planner that keeps every busy or retreating agent on a collision-free reserved route ending at its Haven. We compare SHARP with representative TP and PIBT-family MAPD baselines: Token Passing (TP), Priority Inheritance with Backtracking (PIBT), and PIBT with Temporary Priority and Temporary Avoidance (PIBTTP-TA) for biconnected main areas with attached trees. In the robustness sweep, SHARP is the only method with 100% success on all tested configurations, at substantially higher centralized planning cost on tree-like layouts. A TP-style fixed-home-return counterfactual with full-route validation also recovers robustness on tested tree-like layouts, suggesting that fixed return is a central robustness mechanism there. A no-overwrite variant shows that disabling mid-retreat reassignment worsens service time (release-to-delivery latency) by 1.89 times and makespan by 1.53 times in the tested high-load tree condition.

</details>


### 51. Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research

- **Authors:** Lezhi Yu, Xiaogang Xu, Yuhua Zhou, Shuibing He, Aimin Pan
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26753v1](http://arxiv.org/abs/2608.26753v1)
- **PDF:** [https://arxiv.org/pdf/2608.26753v1](https://arxiv.org/pdf/2608.26753v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents used for scientific experimentation must do more than generate executable code: they must implement the reference method faithfully, design experiments that test the paper's claims, and provide evidence supporting those claims. We show that agents often produce methodological hallucinations: silently reducing datasets or training budgets, replacing failed learning or generative components with lookup or oracle functions, or drawing conclusions from resource-limited settings where a method's claimed advantage disappears. To detect these failures, we introduce ABE-Ralph, a reference-anchored auditing framework that represents claims, protocols, required components, baselines, and metrics as structured experimental constraints, guides implementation through an 8-step workflow, and performs quantitative, qualitative, and code-level verification. Across 30 long-horizon reproduction runs covering 12 machine learning domains, ABE-Ralph achieves a 93% robust execution rate and identifies five scientific failure modes. In 23 NatureBench discovery tasks, ABE-Ralph matches or exceeds state-of-the-art performance on 5 tasks. These results show that reliable evaluation of AI scientists must assess whether the experimental design faithfully tests the intended claim and whether the resulting evidence supports it, rather than treating code execution or plausible metrics as evidence of scientific success.

</details>


### 52. AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design

- **Authors:** Mingquan Liu, Jiangyu Chen, Hanqun Cao, Xujun Zhang, Pengsen Ma, Xiangru Tang, Shuting Jin, Zhuo Yang, Annie Zheng, Tianfan Fu, Fang Wu, Xiangxiang Zeng
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26747v2](http://arxiv.org/abs/2608.26747v2)
- **PDF:** [https://arxiv.org/pdf/2608.26747v2](https://arxiv.org/pdf/2608.26747v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific LLM agents have shown promise in literature reasoning, tool use, and experiment planning, but it remains unclear whether they can autonomously improve large, tightly coupled scientific machine-learning systems through executable code changes and computationally expensive validation. We study this question in protein folding, where progress requires coordinated architectural modifications, multi-objective evaluation, and domain-aware interpretation. We present AgentFold, a multi-agent framework that formulates folding-model development as a closed-loop search over executable code variants. Starting from ESMFold, AgentFold proposes hypotheses, implements and debugs code-level modifications, evaluates model variants, analyzes experimental outcomes, and stores both successful and failed interventions in structured memory. An MCTS-style policy allocates computational resources across high-scoring search branches. On an engineering-scale protein-folding codebase comprising more than 2,000 lines of code, AgentFold explores approximately 80 model variants using approximately 5,000 GPU-hours and 170 million LLM tokens. Under a matched computational budget, AgentFold improves the best lDDT by 7.5% over independent Codex proposals and outperforms a random-search control. Beyond model improvement, the resulting intervention traces reveal recurring empirical design patterns: stable gains tend to arise from early, soft, learnable priors and gated refinement, whereas direct geometric perturbations and geometry-conditioned feedback often destabilize training. The code and experimental resources are publicly available at https://github.com/lmqfly/AgentFold.

</details>


### 53. Knowing When Not to Reuse: Conditional Experience Transfer in Autonomous LLM Post-Training

- **Authors:** Tingyun Li, Wenfeng Feng, Weiqing Li, Abudukelimu Wuerkaixi, Guohua Liu, Yuewei Zhang
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26730v1](http://arxiv.org/abs/2608.26730v1)
- **PDF:** [https://arxiv.org/pdf/2608.26730v1](https://arxiv.org/pdf/2608.26730v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models offer broad capabilities, but adapting them to evolving domains, tools, and requirements often entails repeated post-training. Autonomous systems automate parts of this process by proposing updates, training candidates, and using evaluation feedback to select subsequent proposals. As evidence accumulates, a central problem emerges: which past update evidence remains actionable after subsequent training has changed the parent model? An update's effect depends on its parent, data, and training stage. Treating past success as context-free permission can waste compute. If the resulting child is promoted, it can also degrade the subsequent training trajectory. We formulate this problem as conditional experience transfer and introduce Boundary-Calibrated Intervention Transfer (BCIT), a method that authorizes experience reuse before weight-changing training. BCIT binds an observed effect to its source context, checks applicability conditions, vetoes candidates with named hard conflicts, and obtains current-state evidence through a bounded training trial when needed. Fully trained candidates still face a shared adoption rule, and only observed events extend memory. On one 4B model adapted across finance reasoning, text-to-SQL, and function calling, candidate updates exhibit heterogeneous target and retention effects across the evaluated contexts. Under matched candidates, evidence, and compute, BCIT authorizes fewer harmful updates and attains higher equal-budget final-model quality than the evaluated alternatives. These results support treating experience authorization as a distinct problem in autonomous post-training.

</details>


### 54. Accelerating Scientific Research with Gemini in the Real-World

- **Authors:** Samuel Schmidgall, Xiaokai Zhu, Marian Shaw, Lin Yang, Valentin Liévin, Jingyun Yang, Yuchen Zhuang, Tim Strother, Alex Bijamov, Min Woo Sun, Anil Palepu, Justin Chen, David Steiner, Jacqueline Shreibati, Wei-Hung Weng, Yilin Zhao, Xingjian Hu, Nicholas Zahn, Sadhya Garg, Julia Kirby, Yuxiang Gan, Jiaoli Li, Divy Thakkar, Shekoofeh Azizi, David Racz, Juraj Gottweis, Vivek Natarajan, Chenglin Wu, Tal Danino, Keran Rong, Haozhe Wang, Benoit Schillings, Yong Cheng, Quoc V. Le, Tao Tu
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26701v1](http://arxiv.org/abs/2608.26701v1)
- **PDF:** [https://arxiv.org/pdf/2608.26701v1](https://arxiv.org/pdf/2608.26701v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present an extension and comprehensive real-world validation of Co-Scientist, a Gemini-based multi-agent system designed to accelerate end-to-end scientific research across hypothesis generation, experimentation, and manuscript generation. Moving beyond in silico hypothesis generation, this specialized configuration transitions Co-Scientist into an execution-grounded research partner advancing closed-loop scientific workflows across materials science, biology, and computer science. In materials science, Co-Scientist interfaced with a semi-automated chemical vapor deposition reactor to design a safe precursor route for MXenes; experimental execution produced a lamellar 2D material sharing key structural similarities with the Ti3C2Tx MXene lattice, although further experiments are needed to confirm the atomic structure. Leveraging Gemini 3 Deep Think for rapid, lab-in-the-loop execution, it also tailored growth recipes to laboratory constraints in minutes, enabling single-attempt growth of monolayer MoS2, MoSe2, and WS2 semiconductors. In biology, Co-Scientist predicted emergent swarming phenotypes of engineered E. coli across inducer (IPTG) gradients from sparse imaging data, quantitatively matching unpublished wet-lab morphological measurements. In computer science, Co-Scientist autonomously discovered an inference-time scaling architecture that outperformed six frontier models on HealthBench (Hard and Professional) while reducing potential clinical harm under blinded physician evaluation. Finally, a double-blind study of end-to-end generated papers with 30 domain experts across 450 reviews demonstrates that Co-Scientist's reliability modules reduce hallucination and plagiarism while improving research safety. Together, these results demonstrate progress toward closed-loop multi-agent scientific AI systems capable of accelerating real-world scientific discovery.

</details>


### 55. Five Primitives for Governing Autonomous AI Agents at Runtime

- **Authors:** Jiten Oswal, John Cadeddu
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26696v1](http://arxiv.org/abs/2608.26696v1)
- **PDF:** [https://arxiv.org/pdf/2608.26696v1](https://arxiv.org/pdf/2608.26696v1)
- **Categories:** cs.AI, cs.CR, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise deployments of autonomous AI agents inherit a control model built for human users and long-lived services, and the fit fails in three specific ways: agent principals are ephemeral, appearing and vanishing faster than provisioning; their actions are selected by a model rather than programmed, so the set of things they may attempt is not known in advance; and the population is discovered rather than provisioned, because anyone who can call an API can create one. We argue that governing such agents is a runtime problem -- not a model-alignment problem and not a build-time problem -- and we derive five primitives from the questions that must be answered before an action takes effect and after it has: discovery, identity, governance, attestation, and supply chain. For each we state what fails if it is absent and why the others cannot structurally supply it. We describe an implementation in which an agent's action is mediated against policy before it takes effect, authorised against a per-tenant action vocabulary, and recorded in a hash-linked signed ledger a third party can verify with the vendor out of the loop. We report what the architecture costs: the enforcement point sits on the request's critical path, identity requires a sidecar per workload, and fail-closed mediation converts availability incidents into denial. We are explicit about implementation status: four primitives are built and running in private pilots, and the fifth is built as separate tooling and not yet integrated into the request path. We keep it in the set deliberately: a five-part decomposition that exactly matches what its authors happened to build is not a taxonomy but a description of a codebase.

</details>


### 56. SIGMA: Structured Noise-Effect-Aware Grouped Multi-Agent Aggregation

- **Authors:** Li Mingqian
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26683v1](http://arxiv.org/abs/2608.26683v1)
- **PDF:** [https://arxiv.org/pdf/2608.26683v1](https://arxiv.org/pdf/2608.26683v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) faces significant challenges in maintaining robust coordination under noisy observations. Although observation disturbances are often introduced independently across agents, their downstream effects on cooperative decision-making can become structured through underlying cooperation structures. We characterize this phenomenon as structured noise effects, where noise-induced decision effects exhibit local correlation among agents with stronger task-related dependencies while remaining globally heterogeneous across different agents and local structures. Existing robust MARL methods, however, rarely explicitly characterize or exploit such structure-dependent noise effects. To address this limitation, we propose SIGMA, a hierarchical collaboration framework that exploits cooperation structures to learn robust representations under noisy observations. SIGMA first organizes agents into adaptive local structures through density-based grouping and performs intra-group consensus aggregation to preserve shared task-relevant information while smoothing agent-specific representation deviations. Inter-group attention then adaptively integrates information across different groups to preserve global coordination while accommodating their heterogeneous contributions. Experiments on noisy-observation tasks in StarCraft II empirically validate the structured noise effects and demonstrate that SIGMA consistently improves robustness under observation noise while maintaining competitive performance in noise-free environments.

</details>


### 57. Risks and Controls for Multi-Agent Systems: an analytical framework for deployment of AI agents across organisational boundaries

- **Authors:** Alistair Reid, Simon O'Callaghan, Dustin Venini, Liam Carroll, Tiberio Caetano
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26626v1](http://arxiv.org/abs/2608.26626v1)
- **PDF:** [https://arxiv.org/pdf/2608.26626v1](https://arxiv.org/pdf/2608.26626v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This report presents a framework to help organisations, policymakers and researchers reason about the risks that emerge when AI agents interact with each other, how those risks change as interactions cross organisational boundaries, and the controls that may help address them.
  As organisations deploy AI agents, those agents will increasingly interact with each other: inside the organisation, with the agents of partners, customers and suppliers, and with unknown counterparties on the open internet. Failures can emerge from the interactions themselves, and once those interactions cross an organisation's perimeter, no single organisation can fully see, control or govern them.
  The report introduces three deployment tiers, defined by the minimum common governance binding any two interacting agents: singular governance, where one organisation governs every agent; federated governance, where multiple organisations deploy into a shared environment under agreed rules; and open environments, where agents operate with no central authority and shared standards are adopted voluntarily if at all.
  Within each tier, the report examines risk factors, failure modes and available controls. It identifies who is positioned to apply the controls, and where no actor is positioned to act, it characterises the gap and the collective action required to close it.

</details>


### 58. DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows

- **Authors:** Zechun Niu, Yukun Zhao, Jiaxin Zhang, Xu Shen, Jinhua Si, Han Tian, Can Xu, Yunfan Song, Jiaxin Mao, Yansong Gao, Yuchen Li, Jianmin Wu, Lingyong Yan, Shuaiqiang Wang, Dawei Yin
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26546v1](http://arxiv.org/abs/2608.26546v1)
- **PDF:** [https://arxiv.org/pdf/2608.26546v1](https://arxiv.org/pdf/2608.26546v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents are increasingly adopted to complete complex, multi-tool workflows in real-world settings. However, existing benchmarks typically separate tasks by application or capability and evaluate agents in environments that are cleaner and more stable than those encountered in practice. We introduce DuMateBench, a real-session benchmark reconstructed from anonymized and privacy-screened user sessions collected from a large-scale production agent platform. Each task preserves the relevant pre-solution interaction history, persistent configurations, and workspace state, and is then validated through human verification. The resulting benchmark comprises 200 tasks spanning 8 broad scenarios and 17 fine-grained capability categories, with most tasks requiring multiple capability coordination. We execute these tasks in isolated Docker containers injected with three forms of real-world environmental complexity: Insufficient, Unstable, and Noisy, and assess performance using a hybrid deterministic and LLM-as-Judge evaluation protocol. Experiments across five representative autonomous-agent frameworks paired with four state-of-the-art LLMs reveal substantial gaps in strict task completion. Complementary robustness, efficiency, and diagnostic analyses further show that performance under environmental perturbations is jointly shaped by the capabilities of the LLM and the surrounding agent framework. The code and data are publicly available at https://dumatebench.com/.

</details>


### 59. Zero-Shot Self-Orchestration with Ledger-Based Control for Improved LLM Coding Performance

- **Authors:** Victor Gao, Vida Khosrowshahi, Ali Khosrowshahi, Xihao Sun, Juhyun Lee,  Simon,  Lee
- **Published:** 2026-08-27
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26480v1](http://arxiv.org/abs/2608.26480v1)
- **PDF:** [https://arxiv.org/pdf/2608.26480v1](https://arxiv.org/pdf/2608.26480v1)
- **Categories:** cs.MA, cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent large language model systems are widely reported to beat single-model baselines, but the evidence is mixed, and comparisons are usually confounded: pipelines change token budgets, tool calls, and prompts simultaneously, so an aggregate gain rarely reveals what actually helped. We investigate the effect of introducing the manager-worker scaffold over a shared filesystem workspace, with no training and no per-benchmark tuning, measured against the same model answering in a single pass. Across nine models -- five open-weight, spanning 9B to ~2.8T parameters, and four frontier closed models -- on the 100 latest hard LiveCodeBench problems, the scaffold's benefit is real but conditional: large and statistically significant for some (Qwen3.8-27B +23.4, GPT-5.6-Luna +10.6 and GPT-5.6-Terra +8.0, each over five paired passes; Kimi-K3 +30.4 and Minimax-M3 +11.0 over five paired passes with reasoning off, both at $p < 10^{-4}$, and +42 and +12 in a single pass at a 128k cap) and null or negative for others (Qwen3.6-35B -1 to -9 with reasoning off). With the manager, Opus-5 achieves the highest score in the study at 91% in one pass. Running a manager roughly triples the token bill, but it buys accuracy more cheaply than moving to a larger model does: GPT-5.6-Terra with a manager nearly matches Fable 5's single-call accuracy (85.0 against 87.4, $p = 0.59$) at a fifth of the price (\$11.71 against \$61.11 per 100-problem pass, $p < 10^{-4}$), and the Qwen-27B arm does it for \$51.75 on weights anyone can self-host. Our transcript analysis finds several mechanisms behind the gains, of which two recur: context management, in which short worker calls and shared notes organize state and reduce truncation, and problem decomposition. Improvements are modest for large models with reasoning enabled, but larger for some models with reasoning disabled and for smaller models with reasoning enabled.

</details>


### 60. Don't Overthink, Don't Underthink: Toward Adaptive Reasoning in Agentic AI

- **Authors:** Md Jueal Mia, M. Hadi Amini
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26442v1](http://arxiv.org/abs/2608.26442v1)
- **PDF:** [https://arxiv.org/pdf/2608.26442v1](https://arxiv.org/pdf/2608.26442v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have shown that increased inference-time reasoning can improve performance on complex tasks. However, many existing approaches rely on fixed or preallocated reasoning controls, such as fixed token budgets, pre-execution difficulty estimates, or activation-space interventions, and are often evaluated on standalone reasoning benchmarks rather than full agentic workflows. These assumptions may not hold in agentic AI systems, where reasoning requirements evolve dynamically through planning, tool use, memory retrieval, and agent-to-agent interactions. Consequently, reasoning can become either excessive or insufficient, resulting in unnecessary computation, increased latency, planning drift, excessive tool use, or incomplete solutions. We argue that a major challenge for next-generation agentic AI is not merely how much reasoning a language model should perform, but how it should allocate reasoning according to evolving task demands. We characterize over-reasoning and under-reasoning as recurring failure modes of misallocated reasoning and evaluate them on MATH-500 and the GAIA public validation benchmark. Using tool-decision latency, token consumption, token-limit exhaustion, and answer correctness, our results suggest that cases classified as over-reasoning are associated with higher computational cost without proportional accuracy gains, whereas cases classified as under-reasoning are consistently associated with incorrect or incomplete solutions. These findings motivate future research on adaptive reasoning mechanisms for agentic AI.

</details>


### 61. Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives

- **Authors:** Zheyuan Liu, Weiliang Zhao, Xiangchi Yuan, Ningshan Ma, Yue Huang, Meng Jiang
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26372v1](http://arxiv.org/abs/2608.26372v1)
- **PDF:** [https://arxiv.org/pdf/2608.26372v1](https://arxiv.org/pdf/2608.26372v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as autonomous agents serving users on behalf of companies, placing them in settings where user and deployer interests can conflict. When an agent knows that a user is owed something its deployer would prefer to deny, does it remain honest? Answering this is difficult because false statements can reflect either ignorance or hallucination rather than deception. To address this challenge, we introduce KnownLieBench , a knowledge-verified benchmark that first confirms through a neutral probe that an agent knows a user's entitlement, and then evaluates whether it makes false claims once an incentive to deny that entitlement is introduced. Specifically, KnownLieBench covers eight customer-service domains and 112 grounded cases, conducts multi-round dialogues with a trust-tracking customer agent, and separates deception emerging from incentive alone from deception produced under explicit instruction. Across eighteen proprietary and open-weight models, emergent deception varies substantially across model families and domains. We further use the benchmark for post-training, finding that honesty-directed fine-tuning reduces deception under incentive, while deception-graded fine-tuning increases lie success on honest-control dialogues without increasing lie frequency under incentive. By verifying entitlement knowledge before scoring deceptive behavior, KnownLieBench reduces the confound between lying and not knowing and enables more rigorous auditing and steering of agent honesty.

</details>


### 62. Assessing mentalization in humans and large language models

- **Authors:** Aamir Sohail, Xintong Zhong, Arkady Konovalov, Patricia L. Lockwood, Lei Zhang
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26291v1](http://arxiv.org/abs/2608.26291v1)
- **PDF:** [https://arxiv.org/pdf/2608.26291v1](https://arxiv.org/pdf/2608.26291v1)
- **Categories:** cs.AI, q-bio.NC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mentalization - the ability to infer others' beliefs and intentions to guide one's own choices - is a key cognitive function underlying human social interactions. Large language models (LLMs) demonstrate behaviour consistent with humans on theory-of-mind tasks, yet whether these models can guide adaptive behaviour through mentalization is unknown. Here we use two economic games with cognitive computational modeling to uncover the latent strategies underlying mentalization in LLMs. We tested individual LLM agents across four model families, DeepSeek, GPT-4.1, GPT-5 and Gemini 2.0 Flash (N = 2,099), against opponents of varying sophistication and examined whether a prompting strategy designed to elicit strategic reasoning improved performance. We benchmarked results against human participants (N = 251) as a comparative measure. Across both games, LLMs showed clear behavioural and computational signatures of mentalizing that differed markedly by model provider and size. Strategic prompting generally improved performance by inducing more sophisticated reasoning, yet the extent of the benefit differed across the two tasks. Last, GPT-5 agents flexibly adapted their recursive depth of reasoning to increasingly sophisticated opponents, demonstrating superior performance to human participants. Collectively, we demonstrate different capacities for mentalization across LLMs, and highlight cognitive computational modeling as a formal method for assessing comparative intelligence across humans and machines.

</details>


### 63. SKILL.state: Scalable Long-Horizon Agent Skills

- **Authors:** Sanket Badhe, Priyanka Tiwari, Jonghyun Chung
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26263v2](http://arxiv.org/abs/2608.26263v2)
- **PDF:** [https://arxiv.org/pdf/2608.26263v2](https://arxiv.org/pdf/2608.26263v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) increasingly act as autonomous agents executing complex, long-running procedural skills. Existing agent runtimes maintain execution by continually appending observations, actions, and intermediate reasoning traces to an ever-growing conversation history, causing latency degradation and context-poisoning failures over long horizons. We present SKILL.state, a runtime architecture that replaces append-only conversational history with an explicit, mutable execution state. At each execution step, the model receives only the immutable skill specification, the current structured execution state, and the latest observation. Intermediate reasoning is discarded immediately after producing a validated state update, preventing prompt growth with execution history. Across diverse datasets, models, and execution environments, SKILL. state improves task accuracy while substantially reducing cumulative token consumption. Our results demonstrate that explicit execution state is an effective and architecture-agnostic abstraction for scalable long-horizon agent skills.

</details>


### 64. Agentic Autoresearch for Cell-Edge Power Control: Radically Redefining the Researcher's Role

- **Authors:** Ahmad Khan, Akram Bin Sediq, Sara Azadegi Naeini, Raviraj S. Adve
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26093v1](http://arxiv.org/abs/2608.26093v1)
- **PDF:** [https://arxiv.org/pdf/2608.26093v1](https://arxiv.org/pdf/2608.26093v1)
- **Categories:** cs.LG, cs.IT, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing machine learning algorithms for wireless resource management is labour-intensive: the architecture, the loss function and the training recipe are all specified by hand. We demonstrate that this design layer can be surrendered to an autonomous agent in its entirety. We adopt the autoresearch protocol, in which an AI coding agent edits a training script, runs a fixed-budget experiment, and retains or discards the change according to a single immutable metric. We grant the agent authority over the architecture family, the input representation, the output parameterization, the loss function and the task-sampling law, and set it a target chosen for its difficulty: sum-least-percentile-rate power control across a multicell network. The formulation targets cell-edge throughput and is non-convex, non-smooth and strongly NP-hard away from its max-min vertex. Safeguards render the results trustworthy: a hash-pinned evaluator, an enforced inference contract and a pre-registered falsifier per experiment. In eighty-one unattended experiments over twenty-six hours, the agent reached $99.5\%$ of a converged minorization-maximization reference in one fixed-cost inference pass, at roughly $600\times$ lower inference cost, closing $94\%$ of the gap from its first working architecture, with one parameter set serving every network size and percentile target. It recovered provable structure rather than tuned constants: the output parameterization it discovered reproduces the exact max-min-optimal allocation at the minimum percentile, for every value of the trained weights.

</details>


### 65. How Do LLM Agents Actually Get the Flag? Trace-Level Provenance for Agentic Offensive Security Evaluation

- **Authors:** Kimberly Milner, Minghao Shao, Nanda Rani, Haoran Xi, Venkata Sai Charan Putrevu, Meet Udeshi, Sandeep K. Shukla, Prashanth Krishnamurthy, Farshad Khorrami, Muhammad Shafique, Ramesh Karri
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26237v1](http://arxiv.org/abs/2608.26237v1)
- **PDF:** [https://arxiv.org/pdf/2608.26237v1](https://arxiv.org/pdf/2608.26237v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Capture-the-Flag (CTF) benchmarks are widely used to assess the offensive security capabilities of autonomous language-model agents. Evaluations rely on shallow binary judgments or aggregate scores, overlooking the agent's trajectory to the flag. Consequently actual exploitation is conflated with direct flag exposure, memorized recall, external lookup, guessing, and unsupported claims, potentially overstating the agent's cybersecurity capability. We introduce CTF-ABACUS, a trace-based agent auditing framework that reconstructs each run as an evidence-grounded solve profile. By decomposing agent actions into penetration-testing phases and categorical techniques, it identifies where exploitation occurs, where the flag first appears, and whether the recovered flag is supported by demonstrated behavior. Aggregating solve profiles across agents yields challenge signatures that reveal whether success was achieved via the intended exploit or via shortcut pathways. We apply CTF-ABACUS to 1,435 CTF attempts by six frontier and open-source models on 240 challenges, yielding 2,870 solve profiles under two judge lenses. Trace-verified exploits account for only 62-87% of recovered flags across benchmarks, while shortcut recoveries follow substantially shallower trajectories. These findings shift CTF evaluation from counting recovered flags to verifying demonstrated exploitation and provide a basis for designing benchmarks that better isolate the offensive capabilities.

</details>


### 66. SwarmWorld: Stigmergic technological evolution in societies of language-model agents

- **Authors:** Subhadeep Pal, Fiona Y. Wang, Markus J. Buehler
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26081v1](http://arxiv.org/abs/2608.26081v1)
- **PDF:** [https://arxiv.org/pdf/2608.26081v1](https://arxiv.org/pdf/2608.26081v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collective intelligence can emerge when individuals coordinate through a shared environment, allowing local actions to accumulate into durable social organization. Language-model agents offer a new substrate for this process, yet most multi-agent systems rely on direct conversation, predefined roles, or centralized workflows. It remains unclear whether decentralized agents can build functional technologies and outperform independent search. Here, initially homogeneous LLM agents in SwarmWorld self-organize without assigned roles or recipes into evolving technological societies. Agents explore a spatial environment, process resources, test materials, construct persistent artifacts, and write executable controllers evaluated by a deterministic simulator under unseen disturbances after the agents are removed. SwarmWorld splits cognition from consequence: agents propose architectures and controllers within fixed action and material schemas, while the simulated world determines function. Shared societies develop broader, more resilient technological portfolios than a strong best-of-N isolated-search baseline, although isolated search remains competitive for the strongest artifact. Agents differentiate into exploration, construction, maintenance, and coordination behaviors, transitioning as the world matures. Technologies accumulate through collaborative construction, executable inheritance, and persistent agent-artifact networks, with most reuse beginning through physical observation rather than communication. Explicit cultural mechanisms amplify collaboration and organization, but functional benefits depend on outcome and timescale. Physical stigmergy alone supports capable societies, while interaction drives persistent technological ecologies rather than universally superior individual inventions.

</details>


### 67. A Self-Evolving Multi-Agent Framework Defense against LLM Jailbreak Attacks

- **Authors:** Tongyan Hu, Bryan Hooi
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26008v1](http://arxiv.org/abs/2608.26008v1)
- **PDF:** [https://arxiv.org/pdf/2608.26008v1](https://arxiv.org/pdf/2608.26008v1)
- **Categories:** cs.CR, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) remain vulnerable to jailbreak attacks that exploit techniques such as role-playing, obfuscation, code transformation, and multi-step indirection to elicit harmful outputs. As jailbreak strategies keep emerging, defenses have proliferated in an ongoing cat-and-mouse game, yet most remain static: their safety behavior is fixed at deployment, so they cannot accumulate defensive experience or adapt to unseen strategies. We propose a self-evolving test-time defense built around a persistent, cross-interaction rule memory: when an attack succeeds, the framework abstracts that failure into a method-level rule capturing the structural attack wrapper rather than the harmful topic, and reuses it against future inputs. Because rules are method-level, one induced rule generalizes across an entire attack family, and the label space expands as novel wrappers appear. The mechanism operates entirely through external memory and prompting, with no parameter updates, and applies to both open-weight and black-box API models. We realize it as four cooperating modules, but the contribution is the memory-based adaptation mechanism, not the module decomposition. Across four black-box jailbreak families and multiple models, our method substantially reduces attack success rates while preserving benign utility, remains robust under an adaptive composite-wrapper attack, and does not increase over-refusal as the memory grows.

</details>


### 68. ProgRouter: Online Progress-Guided Orchestration for Multi-Agent LLM Workflows under Quality-Cost Tradeoffs

- **Authors:** Songyuan Li, Ahmed M. Abdelmoniem, Shiqiang Wang
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25992v1](http://arxiv.org/abs/2608.25992v1)
- **PDF:** [https://arxiv.org/pdf/2608.25992v1](https://arxiv.org/pdf/2608.25992v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent large language model (LLM) workflows have emerged as a powerful paradigm for solving complex, open-ended tasks through collaborative reasoning among specialized LLM agents, but they incur substantial operating costs due to repeated LLM invocations and long-horizon context accumulation. Existing cascade routing methods make one-shot, query-level decisions and cannot adapt to the dynamic, state-dependent nature of multi-step workflows, in which the right LLM at each step depends on evolving task progress, remaining task difficulty, and cost-efficiency requirements. We present ProgRouter, an online progress-guided routing framework that adaptively selects LLM agents across workflow steps to preserve task-solving quality while adhering to time and cost budgets. ProgRouter introduces a multi-view task progress scorer that combines coarse workflow outcome regimes with fine-grained signals on subtask completion, progress trends, and workflow state quality. Then, a dual-path task progress predictor and an adaptive meta-gating mechanism estimate the progress gain for each candidate routed LLM. ProgRouter makes online step-wise routing decisions that balance progress gain, task time budgets, and long-term operating cost efficiency. Experiments on HumanEval Plus, MBPP, MATH-500, and ASQA, spanning agentic code generation, mathematical reasoning, and retrieval-augmented long-form question answering, demonstrate that ProgRouter reduces the operating cost relative to key baselines while maintaining strong task-solving performance.

</details>


### 69. Spatial-Knowledge-Graph-Grounded LLM Agents for Neighborhood Livability Evaluation

- **Authors:** Haiyan Hao
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25952v1](http://arxiv.org/abs/2608.25952v1)
- **PDF:** [https://arxiv.org/pdf/2608.25952v1](https://arxiv.org/pdf/2608.25952v1)
- **Categories:** cs.CY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Neighborhood livability is commonly assessed with static built-environment indicators, such as facility proximity, street connectivity, and access to public space. These measures describe available opportunities but do not directly represent how residents with different mobility capacities, household roles, schedules, and care responsibilities experience the neighborhood. This paper presents a prototype framework that uses a spatial knowledge graph (KG) and large language models (LLMs) to generate and revise household schedules, followed by rule-based feasibility checking and GIS-based network materialization. The spatial KG integrates residents, residences, facilities, neighborhood context, and sampled road hubs; Graph-RAG retrieves each household's nearby spatial context, including candidate POIs and approximate walking times, for the scheduling LLM. The LLM produces structured household schedules, while rules are used for lightweight repairs and auditable feasibility checks. The LLM then revises schedules in response to identified feasibility issues. A routing module derives the actual travel paths, travel times, modes, and event histories from the road network. The resulting events support synthetic resident-agent interviews about daily convenience, travel burden, activity feasibility, and household coordination. A prototype demonstration in a Shenzhen neighborhood shows that nominal facility availability does not necessarily imply convenient access: residents with limited mobility and households with care responsibilities experience greater travel and coordination burdens. The framework offers an auditable way to connect spatial opportunity, household activity constraints, and resident-specific livability interpretation, while keeping simulated experience distinct from observed perception.

</details>


### 70. Candidate supply and answer selection shape the value of LLM judging in multi-agent systems

- **Authors:** Jia-Hao Ji, Sijie Li, Jiabei Cheng, Zixi She, Jin-Tai Yu, Zhiyuan Yuan
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25937v1](http://arxiv.org/abs/2608.25937v1)
- **PDF:** [https://arxiv.org/pdf/2608.25937v1](https://arxiv.org/pdf/2608.25937v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) sometimes already have the potential to answer correctly, but still report a wrong answer. Explaining this outcome is difficult because generation, communication and final answer-selection rules usually change simultaneously. We conceptualize multi-agent reasoning as an evolutionary pipeline of candidate generation, peer communication and terminal selection, wherein consensus without quality control can exhibit patterns of memetic drift. We study two questions: (1) when an LLM judge provides effective selection pressure by supplying a signal of answer correctness for candidates generated in a multi-agent system, and (2) when using that signal improves the reported answer. To map judge reliability, we analysed 15,336 questions from MMLU-Pro, GPQA, MedXpertQA and MuSR, with Humanity's Last Exam analysed separately. To test these rules, we replayed 81,390 fixed candidate pools drawn from 16,278 questions across five benchmarks. We report three findings. (1) A correct answer is often already present among the generated candidates, but the system can still converge on and report a wrong answer. (2) Judge reliability is not a fixed trait of the model, but varies with the task, the generator and how rare the correct answer is. (3) Combining answer frequency with the judge's evaluation changed only the final answer-selection rule and raised accuracy from 63.82% to 70.82-70.95%, primarily by rescuing correct answers that were outnumbered by popular errors. In the systems studied here, the value of generating more candidates depends on whether those extra samples make correct answers present, frequent or recognisable. By isolating generation, recognition and selection, these findings establish a diagnostic basis for designing multi-agent architectures that protect generated correct answers from being lost.

</details>


### 71. LLM Agents for Time-Series: A Survey

- **Authors:** Yilong Chen, Xiao Qin, Chenghao Liu, Liang Wu, Noelle I. Samia, Kaize Ding
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26226v1](http://arxiv.org/abs/2608.26226v1)
- **PDF:** [https://arxiv.org/pdf/2608.26226v1](https://arxiv.org/pdf/2608.26226v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are increasingly being developed for time-series problems, but their design choices vary substantially across task settings. This survey adopts a problem-driven taxonomy that organizes these systems by the time-series problems they address rather than by isolated technical components. We group existing systems into four categories: forecasting and reasoning, augmentation and synthesis, anomaly detection and diagnosis, and decision support. Within each category, we examine how task requirements shape agent architecture, tool use, and memory design. We further summarize representative datasets and environments, and compare reported model performance under shared or closely related settings. Overall, this survey offers a task-oriented guide to designing LLM-based agents for time-series problems and identifies open gaps for future work.

</details>


### 72. AI Agentic Selective Laser Sintering Process Optimization

- **Authors:** Peter Pak, Victor Alvarado, Amir Barati Farimani
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25928v1](http://arxiv.org/abs/2608.25928v1)
- **PDF:** [https://arxiv.org/pdf/2608.25928v1](https://arxiv.org/pdf/2608.25928v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic systems enable the intelligent automation of complex workflows, specific to additive manufacturing this is applicable for complex tasks such as process parameter optimization for mechanical properties. This work investigates the AI enabled agentic process optimization within Selective Laser Sintering (SLS) to iteratively improve the tensile and flexural properties of 3 different materials on the Inova Mk1. These materials include PA12 GF, PA11 Onyx, and PA12 Blend (volume mixture of 25% PA12 GF and 75% PA12 White) and with using knowledge from previous builds and minimal guidance from the user, the agentic system was able to optimize process parameters over a small number of iterations to achieve comparable TDS specified mechanical properties. This work showcases the ability for an agentic system to continually learn from updated data, enabling the intelligent automation of complex tasks such as process parameter optimization for selective laser sintering.

</details>


### 73. Agent Mesh: Reliability Primitives for Non-Idempotent Agent Delegation - Identity Adequacy and Evidence Adequacy

- **Authors:** Mazhar Shaikh, Anurag Rajkumar Bombarde, Harshal Pathak
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26225v1](http://arxiv.org/abs/2608.26225v1)
- **PDF:** [https://arxiv.org/pdf/2608.26225v1](https://arxiv.org/pdf/2608.26225v1)
- **Categories:** cs.AI, cs.DC, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents increasingly perform bounded software tasks under an orchestrator that retries, resumes, and budgets them. The machinery such orchestrators reach for is the service mesh's: retry, timeout, and error-rate circuit breaking. We report a failure study of a production agentic software-delivery platform over 147 numbered incidents spanning 81 runs, each with a measured cost and, in most cases, a mutation proof reproducing the failure. All three assumptions those primitives rest on are violated in practice, and we quantify the consequences: a loop of fifty-four consecutive successful tool calls no error-rate breaker could see; a progress signal constant by construction, guaranteeing a false trip on the third repair round and driving one run from six of six components to three; twenty-one events accumulated across six invocations of one delegation, making a correct, idempotent component unwinnable; a misrouted failure that woke five components for a two-component fault, leaving three bystanders regressing working code; and twelve incidents in which the enforcement layer blocked correct work, the most expensive costing 107 agent turns and zero accepted writes. We find one cross-cutting cause and its dual. Identity adequacy: in five separate subsystems an identity that failed to discriminate produced a confident wrong answer, and two of them derived the corrective rule independently. Evidence adequacy: a reliability decision may be taken only on evidence capable of moving, attributable to what it measures, and deterministic under identical conditions. From the findings we derive seven reliability primitives whose enforcement unit is the delegation rather than the message, and specify the controlled evaluation the study motivates but does not constitute.

</details>


### 74. Repair or Resample? Rethinking Failure Debugging in LLM Multi-Agent Systems

- **Authors:** Zhongwen Luan, Xiaoyu Zhang, Ming Hu, Yue Yang, Jiongchi Yu, Xiaohong Chen
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25920v1](http://arxiv.org/abs/2608.25920v1)
- **PDF:** [https://arxiv.org/pdf/2608.25920v1](https://arxiv.org/pdf/2608.25920v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language model (LLM)-based multi-agent systems (MASs) are increasingly applied to long-horizon complex tasks, their reliability has emerged as the core bottleneck hindering their real-world deployment. Existing MAS debugging and repair methods typically rely on rerunning and resampling the entire execution trajectory. However, a fundamental question remains to be answered: do these methods causally repair MAS failures or merely stochastically repair by leveraging the randomness of LLM sampling? To evaluate the effectiveness of MAS repair methods, we introduce SymTrace, a controlled evaluation framework that records the MAS execution trajectory and establishes intervention anchors. During replay, it effectively reconstructs the execution before the anchor using recorded logs and only regenerates the downstream trajectory, thereby enabling the reliable reproduction of MAS failures. We further construct the dataset SymFail, comprising 536 human-annotated failure trajectories with graph-linked locations, categories, and trace evidence. Based on these foundations, we conduct a large-scale empirical study across three mainstream MAS frameworks. Our findings reveal that existing unguided rerun methods are highly unreliable, exhibiting low failure reproduction and repair rates (only 67.97% and 6.90%, respectively). Building upon these findings, we further explore the effectiveness of a symptom-driven intervention method, which successfully repairs 20.15% of the failed cases (a 191.89% improvement to state-of-the-art repair methods). This study aims to provide actionable insights for MAS debugging and repair research, paving the way for the robust deployment of multi-agent systems.

</details>


### 75. Cooperative Multi-Agent Reinforcement Learning for Adaptive Aggregation in Semi-Supervised Federated Learning with non-IID Data

- **Authors:** Rene Glitza, Luca Becker, Rainer Martin
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25794v1](http://arxiv.org/abs/2608.25794v1)
- **PDF:** [https://arxiv.org/pdf/2608.25794v1](https://arxiv.org/pdf/2608.25794v1)
- **Categories:** cs.LG, cs.DC, cs.SD, eess.AS, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Federated Learning (FL) enables distributed training of machine learning models while preserving data privacy. However, FL struggles with heterogeneous, non-IID client data distributions, resulting in sub-optimal and biased global models. In this paper, we propose pFedMARL, a novel approach leveraging Multi-Agent Reinforcement Learning (MARL) with Twin Delayed Deep Deterministic Policy Gradient (TD3) to dynamically adapt aggregation strategies in FL settings. Our method employs a server-side agent adjusting client contributions to optimize global model robustness and client-side agents balancing global and local updates to personalize models effectively without pre-training. We demonstrate superior performance of pFedMARL for training a semi-supervised audio spectrogram transformer, matching or outperforming FedAvg, Ditto, and local training approaches across multiple non-IID scenarios and in the presence of adversarial clients. Our results indicate that pFedMARL actively improves accuracy, robustness, and fairness, making it suitable for real-world deployments.

</details>


### 76. LocalLSTC: A Long Short-Term Control Architecture for Locally Deployed GUI Agents

- **Authors:** Weiming Li, Helen Paik, Yulei Sui
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25777v1](http://arxiv.org/abs/2608.25777v1)
- **PDF:** [https://arxiv.org/pdf/2608.25777v1](https://arxiv.org/pdf/2608.25777v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern GUI-agent frameworks achieve strong desktop task performance with frontier API models, yet persistent control information often remains implicit in growing interaction trajectories. At each step, the planner reconstructs the active task stage, accumulated evidence, and runtime feedback before deciding the next action. This dependence becomes more pronounced under weaker local reasoning backbones. Across four representative state-of-the-art frameworks, replacing GPT-5 with Qwen3.5-9B reduces average OSWorld SR-100 from 60.9\% to 37.7\%. Trajectory annotation further identifies at least one control failure in 91.6\% of failed trajectories. To address this problem, we introduce LocalLSTC, a training-free architecture that organizes control by temporal scope, maintaining persistent cross-step state to guide short-term execution commitments. Long-Term Control maintains the active subgoal, subgoal-aligned evidence, and runtime feedback across interactions, while Short-Term Execution realizes bounded commitments for the current step. Long-to-Short Planning forms each commitment from persistent state, and Short-to-Long Control integrates execution outcomes back into that state for progress assessment, recovery, and termination. With Qwen3.6-27B, LocalLSTC reaches 64.7\% SR-100 on OSWorld and 65.3\% on WindowsAgentArena, outperforming the strongest prior local results on both benchmarks. Ablations further support contributions from mechanisms on both sides of execution. These findings identify temporal organization of control information as a distinct architectural dimension for locally deployed GUI agents.

</details>


### 77. Large Language Model Few-Shot Prompting with Dilemma Training Outperforms Human Surrogates in Predicting Patient Preferences

- **Authors:** Natasha Ureyang, Sebastian Porsdam Mann, Yuxin Liu, Zuriel Hassirim, Melanie Almonte, Wenhao Chen, Joyce Ng, Thant Nay Lin, Aung Thiha, Gerald CH Koh, Brian David Earp, Pin Sym Foong
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25771v1](http://arxiv.org/abs/2608.25771v1)
- **PDF:** [https://arxiv.org/pdf/2608.25771v1](https://arxiv.org/pdf/2608.25771v1)
- **Categories:** cs.HC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In serious illness, human surrogates often struggle to accurately predict patient preferences (68% accuracy), causing decision conflict. Personalized Patient Preference Predictor (P4) agents offer a potential solution, but prior prototypes treat values as static ratings, ignoring the contextual, situation-dependent nature of medical choices. Grounded in the 'logic of care', we present P4-DT (Dilemma Training), a P4 agent that constructs a patient decision policy by engaging users with varied medical dilemmas, eliciting individual preference reasoning through bi-directional training. In a study with 12 patient-surrogate dyads, P4-DT predicted patient treatment choices with 81.7% accuracy, significantly exceeding chance (OR = 5.61 [2.03, 15.51], p < .001) and outperforming both unassisted surrogates (55.0%; OR = 3.67 [1.59, 8.47], p = .002) and surrogates assisted by P4-DT (61.7%). Comparative prompt analyses showed that incorporating contextual scenario decisions and open-ended text improved accuracy by 15.0 percentage points over initial values ratings alone. We discuss implications for further testing and designing of context-aware AI agents that embody richer human experience to partner in complex decision-making.

</details>


### 78. HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning

- **Authors:** Ziqing Qian, Jiaying Lei, Yifang Wang, Nan Cao
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25770v1](http://arxiv.org/abs/2608.25770v1)
- **PDF:** [https://arxiv.org/pdf/2608.25770v1](https://arxiv.org/pdf/2608.25770v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have enabled AI scientist systems to automate scientific discovery, yet existing approaches most rely on static prompting or fixed workflows and fail to accumulate experience for continual improvement. We propose HypoForge, an experience-guided multi-agent framework that learns reusable scientific skills for automated hypothesis generation and hypothesis testing. HypoForge is built on the observation that these two stages involve different supervision signals. For hypothesis generation, where explicit feedback is unavailable, HypoForge adopts an adversarial generator--discriminator mechanism to improve reasoning through comparative critique. For hypothesis testing, where empirical feedback is available, HypoForge learns testing skills from execution outcomes and ground-truth results. By matching skill learning strategies with stage-specific supervision, HypoForge enables continual improvement without fine-tuning foundation models. Experiments on hypothesis generation and testing benchmarks show that HypoForge consistently outperforms existing AI scientist frameworks and skill-level variants. Further analysis demonstrates the effectiveness of the proposed stage-specific skill learning paradigms.

</details>


### 79. Beyond Scaling: Self-Evolving LLM Agents for Hardware Kernel Optimization via an Experience-Driven Workflow and Experience Graph Memory

- **Authors:** Siyuan Chen, Runlin Hou, Shenxiu Wu, Yansong Sun, Junming Cao, Yiyu Zhang, Shudi Shao, Junhao Qiu, Zhichao Lu, Qingfu Zhang
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25570v1](http://arxiv.org/abs/2608.25570v1)
- **PDF:** [https://arxiv.org/pdf/2608.25570v1](https://arxiv.org/pdf/2608.25570v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Hardware kernel optimization requires repeated compilation, correctness testing, profiling, and revision. LLM agents can automate parts of this process, and stronger foundation models, longer context windows, and longer execution horizons have improved optimization within individual tasks. These advances alone do not enable an agent to learn from completed optimization runs. Existing kernel-optimization agents seldom preserve a decision, its observed execution feedback, and the later decisions that use that evidence. Retaining every prior trajectory is also impractical because an expanding history competes with the current task for context. We present KOPE, an experience-driven framework for hardware kernel optimization. KOPE records optimization trajectories with correctness and performance feedback in Experience Graph Memory, then uses Active Context Management and Injection to retrieve relevant experience under a fixed token budget. The graph retains decision order, observed outcomes, and alternative branches, allowing evidence collected on the target hardware to inform later optimization steps and tasks. Under the same GLM-5.2 setting, the geometric mean of KOPE's per-operator speedups is $1.54\times$ that of CANNBot, the strongest competing baseline. In a complete 53-operator ablation, Active Context Management and Injection raises pass rate from 60.0\% to 84.6\%, increases the evaluator-reported positive-field geometric mean from 0.0382 to 0.0661, and reduces optimization token consumption from 15.9B to 1.113B tokens relative to passive agent-led context construction. Enabling Experience Graph Memory raises full-suite pass rate from 55.2\% to 84.6\% and yields a $1.43\times$ geometric-mean speedup on valid timing comparisons. These results support continual optimization through external experience while the foundation model remains fixed.

</details>


### 80. AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research

- **Authors:** Xintong Zhang, Xiaomeng Fan, Shilin Yan, Ekko He, Zicheng Liu, Zijian Zou, Guannan Zhang, Yuwei Wu, Zhi Gao, Hongwei Xue
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25559v1](http://arxiv.org/abs/2608.25559v1)
- **PDF:** [https://arxiv.org/pdf/2608.25559v1](https://arxiv.org/pdf/2608.25559v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Video deep research answers complex questions by jointly understanding video content and retrieving external knowledge from the open Web. However, diverse questions and videos require different tool-use strategies, and inappropriate tool calls can produce incorrect results. Uncertain grounding and retrieval also make unnecessary interactions costly and error-prone, increasing latency and reasoning errors. To address these challenges, we propose AdaVDR, an adaptive video deep research agent with adaptive tool invocation and reflection. AdaVDR selects tools according to the task and its capabilities, and backtracks only when unreliable intermediate results require correction. To enable these capabilities, we develop a video deep research data construction pipeline. We first discover retrieval-relevant events and entities in diverse videos and acquire detailed information through grounding and external retrieval to construct high-quality QA pairs. For each QA, task-specific prompts organize the information acquisition process into a tool-use trajectory, allowing different question and video types to follow different grounding and retrieval strategies. We further introduce model-conditioned tool necessity filtering, which evaluates tool calls against the target model's video understanding and internal knowledge, removing tools or tool chains the model can bypass. This yields trajectories tailored to the target model's video understanding capability and knowledge. Using this pipeline, we construct training data and VDR-EE, a benchmark covering entity-centric and event-centric questions. We perform supervised fine-tuning followed by reinforcement learning with a redundancy-aware reward to strengthen adaptive tool invocation and reflection. Experiments show that our method performs best among the evaluated open-source models on VDR-EE and substantially improves over its base models on VideoDR.

</details>


### 81. ClueWeaver: Reward-Guided Dual-Agent Evidence Reasoning for Compact LLMs on Literary Long Narratives

- **Authors:** Jihao Zhu, Zhiwei Yang, Wenxiao Zhang, Junqian Zhao, Qi You, Fangqi Wang, Zheyuan Deng, Hanzhe Yang, Yu Liu, Jin B. Hong
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25531v2](http://arxiv.org/abs/2608.25531v2)
- **PDF:** [https://arxiv.org/pdf/2608.25531v2](https://arxiv.org/pdf/2608.25531v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Humanities and social science research requires close reading of long narrative materials such as novels, scripts, archives, and case reports, yet many users have limited access to costly proprietary long-context models. Compact, locally deployable language models are a practical alternative, but directly feeding them an entire long context remains costly, hard to inspect, and prone to missing sparse evidence. We present ClueWeaver, an evidence-aware dual-agent framework for long-narrative question answering with compact local models. A Finder identifies passages containing answer-critical clues through retrieval-guided segmentation, while an Interpreter derives the answer from the selected evidence, produces rationales with paragraph-ID citations, and applies an internal self-calibration pass for high-risk questions. Both agents are optimized with reward-guided reinforcement learning: Finder rewards emphasize evidence retention and faithful paragraph-ID references, and Interpreter rewards emphasize correctness, grounding, and concise explanations. This decomposition makes evidence selection and reasoning more inspectable than end-to-end prompting. Experiments across multiple long-context narrative question answering and claim verification settings show that ClueWeaver substantially improves local end-to-end language models while providing evidence coverage and paragraph-referenced reasoning traces. Code is available at https://github.com/Ameame1/ClueWeaver.

</details>


### 82. TOPAS: Workflow-Aware Prefix-State Scheduling for Multi-Agent LLM Serving

- **Authors:** Hongqiu Ni, Han Tian, Chi Zhang, Guopeng Li, Haisheng Tan
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25523v1](http://arxiv.org/abs/2608.25523v1)
- **PDF:** [https://arxiv.org/pdf/2608.25523v1](https://arxiv.org/pdf/2608.25523v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prefix caching introduces a fundamental tradeoff in multi-agent large language model (LLM) serving: retaining a long system-prompt key-value (KV) cache for an agent accelerates future calls, yet it reduces the GPU memory available for batching concurrent requests. In multi-stage workflows, existing schedulers tend to prioritize either immediate prefix locality or overall workflow progress. However, under a shared KV cache budget, optimizing either objective in isolation can prolong tasklevel job completion time (JCT) through downstream delays or frequent prefix replacement. To strike a balance, we here propose TOPAS, a Task-Oriented Prefix-Aware Scheduler that jointly decides which agent prefixes to keep in the cache and which requests to schedule for execution. TOPAS scores candidate post-decision states by trading off the expected reduction in each task's longest remaining service path against the near-term benefit of downstream prefix reuse, accounting for the costs of prefix movement and preemption. A task-level aging mechanism is also incorporated to prevent starvation. We implement TOPAS within the SGLang framework and assess its performance on three synthetic DAGs and two MetaGPT software-development workflows. Compared with the best performing baseline for each workload and metric, TOPAS reduces the mean/p99 JCT by up to 39.8%/49.4% on the synthetic workloads, while lowering mean JCT by 9.8% on MetaGPT-SOP and mean/p99 JCT by 22.0%/26.6% on MetaGPT-TL.

</details>


### 83. AERIS: Offline Policy Improvement for Multi-UAV Integrated Sensing and Communication

- **Authors:** Ziyuan Wang, Yifan Sui, Wei Wei, Wenjie Xin, Zekai Zhang, Xiangwang Hou,  Xiao-Ping,  Zhang
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25477v1](http://arxiv.org/abs/2608.25477v1)
- **PDF:** [https://arxiv.org/pdf/2608.25477v1](https://arxiv.org/pdf/2608.25477v1)
- **Categories:** cs.NI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Unmanned aerial vehicle (UAV)-enabled integrated sensing and communication (ISAC) is a promising 6G paradigm, but dynamic multi-UAV ISAC control must jointly balance communication quality, sensing reliability, and flight safety under stochastic mobility. Existing optimization methods often require repeated global non-convex solving, while online reinforcement learning (RL) depends on risky trial-and-error flights that may cause sensing loss or collision-risk events.
  This paper proposes AERIS, an offline policy improvement framework for multi-UAV ISAC. AERIS learns from fixed flight logs under centralized training and decentralized execution, so each UAV acts from local histories while training uses logged global information to assess team-level effects. We further design STAR-CRDT, an offline multi-agent RL algorithm that performs support-aware local action rectification and distills only trusted improvements into the decentralized actor. We prove an offline-support policy improvement guarantee. Experiments show that STAR-CRDT improves the main ISAC objective return by 29.3% over the strongest baseline. It further improves communication sum rate, sensing pass rate, and sensing margin by 3.4%, 4.8%, and 69.1%, while reducing collision-risk events by 54.2%. On unseen real-road maps built from OpenStreetMap data, STAR-CRDT still obtains the best return.

</details>


### 84. MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration

- **Authors:** Miseon Yu, Jaehoon Choi, Younghan Lee, Yunheung Paek
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25457v2](http://arxiv.org/abs/2608.25457v2)
- **PDF:** [https://arxiv.org/pdf/2608.25457v2](https://arxiv.org/pdf/2608.25457v2)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite their strong ability to generate code, large language models often fail to produce secure code, as their outputs frequently contain security vulnerabilities. Secure code generation is inherently challenging because it requires solving a multi-objective problem: functional correctness and security. Existing approaches address this challenge by injecting external security knowledge or by using agentic feedback and iterative refinement. However, guideline retrieval often leaves the generator to translate generic advice into task-specific secure implementations, while shared-dialogue multi-agent feedback can blur role boundaries and suffer from context bloat.
  We present MACGen, a multi-agent framework that integrates planning, security analysis, code synthesis and refinement to jointly optimize security and functionality. A planner constructs a step-by-step plan to satisfy functional requirements. A security advisor identifies likely CWEs and synthesizes task-specific guidelines, a coder then generates code grounded in these artifacts, and a reviewer issues perspective-separated feedback. Rather than sharing full dialogue histories, each agent receives only structured artifacts from upstream stages, enforcing role specialization and reducing uncontrolled context growth. On CWEval and BaxBench, MACGen improves F&S@1 over direct prompting by 19.61 and 10.57 percentage points (pp) on average, respectively.

</details>


### 85. BVR Sim: An Open and High-Throughput Environment for Heterogeneous Air-Combat Reinforcement Learning

- **Authors:** Haocheng Sun, Mulai Tan
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25419v1](http://arxiv.org/abs/2608.25419v1)
- **PDF:** [https://arxiv.org/pdf/2608.25419v1](https://arxiv.org/pdf/2608.25419v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Beyond-visual-range (BVR) air combat is a challenging reinforcement-learning domain characterized by partial observability, long-horizon decision making, energy management, and limited weapons. We present BVR Sim, an open-source Gymnasium-style environment designed for heterogeneous air-combat reinforcement learning. BVR Sim supports multiple JSBSim aircraft models, including the F-15, F-16, F/A-18, and F-22, with configurable weapons, sensors, controllers, and opponents. A unified tactical action interface specifies desired heading, altitude, speed, and weapon release above aircraft-specific inner-loop controllers, enabling policies to operate across heterogeneous platforms. The environment provides interchangeable Python and accelerated C++ backends, entity-oriented observations, compositional rewards, scripted opponents, replay and visualization, and adapters for multi-agent learning frameworks. At a 0.4-s decision interval, the C++ backend achieves 104 simulated seconds per wall-clock second in 1-vs-1 and remains practical through 10-vs-10 scenarios. A policy trained only on the F-16 transfers without retraining to four unseen aircraft, reaching a 45.5% mean win rate with aircraft-specific controller adaptation. MAPPO and HAPPO experiments further verify end-to-end compatibility with standard multi-agent reinforcement-learning pipelines.

</details>


### 86. Can your AI agent be cheaper? Investigating the effects of task specifications on token spend in agentic coding tasks

- **Authors:** Jakub Smékal
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25399v1](http://arxiv.org/abs/2608.25399v1)
- **PDF:** [https://arxiv.org/pdf/2608.25399v1](https://arxiv.org/pdf/2608.25399v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic coding workflows are now widely deployed in real-world systems. With long-horizon reasoning and tool use, token usage has become an important consideration for both cost and efficiency. Two engineers using AI will solve the same problem differently. How the specification of a task shapes an agent's token spend, and whether that spend can be predicted in advance, are open questions. Here, we study the effects of different task specifications on agentic token spend with the Kimi K3 model at three thinking efforts. Across $2,700$ runs, we show that reducing a full task specification to a bare user story raises token spend by $29.7\%$, while run-to-run variance remains unaffected by any prompt changes. We show that prompt-sensitivity is task-dependent, running from $13\%$ to $115\%$. We fit a simple predictor that can price a full distribution of task specifications and thinking effort configurations from a single cheap probe on an unseen task within $36\%$, improving over prior work in predicting token spend. Our work provides initial results quantifying the effects of task specification on agentic token spend and introduces a method that can be used to systematically evaluate the cost of AI coding workflows.

</details>


### 87. BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks

- **Authors:** Zane Koch, Asmamaw T. Wassie, Javier Valdes-Aleman, Jason Lee, Michaela M. Hinks, Samuel G. Rodriques, Andrew D. White, Jon M. Laurent
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25286v1](http://arxiv.org/abs/2608.25286v1)
- **PDF:** [https://arxiv.org/pdf/2608.25286v1](https://arxiv.org/pdf/2608.25286v1)
- **Categories:** cs.AI, q-bio.QM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) promises to accelerate biological research by automating computational analyses. Yet the ability of AI agents to carry out computational biology at the scale of complete research studies has not been systematically evaluated. Here we introduce BixBench3, a benchmark that measures the capacity of AI agents to process raw biological data through to scientific results. We designed BixBench3 tasks to mirror the delegation of work from a scientist to an agent: the scientist chooses the research question and high-level methods, then delegates implementation of all analyses to the agent. In each task, an agent receives a research objective, methodological guidance, and raw data derived from a published scientific study, and must execute a sequence of analyses to achieve the research objective. The data artifacts resulting from these analyses - such as peak call matrices or differential expression tables - are programmatically graded against the corresponding artifacts generated and reported in the original study. Across 20 BixBench3 tasks encompassing the generation of 138 unique artifacts, we find that 13 frontier models achieve scores ranging from 0.00 for Gemini 3.1 Flash Lite to 0.48 for GPT 5.6 Sol. Agents perform worse on tasks with larger raw datasets (0.36 on tasks with <100 GB versus 0.10 on tasks with >100 GB) and on analyses requiring more sequential steps (0.36 at 1-2 steps vs 0.24 at 3+). On average, agents use 6.8 hours, 102 million tokens, and $43 to complete each task, with the longest attempts consuming 24 hours, 1.07 billion tokens, and $525. Notably, the highest-scoring agents used fewer tokens and were cheaper than less performant options. These results reveal that LLMs vary substantially in their ability to (1) execute multiple sequential analysis steps coherently, (2) manage large quantities of raw data, and (3) work across scientific domains.

</details>


### 88. Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation

- **Authors:** Pratyay Banerjee, Ankit Chadha
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25277v1](http://arxiv.org/abs/2608.25277v1)
- **PDF:** [https://arxiv.org/pdf/2608.25277v1](https://arxiv.org/pdf/2608.25277v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems coordinate through natural-language messages that consume 40--60\% of their token budget. Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning. We propose \textbf{Routed Graph Handoff}, where a lightweight LLM router (155 tokens, 0.15\% overhead) selects between a typed dependency graph and natural language for each delegation. On four benchmarks (1,050+ trajectories), the routed system matches or exceeds NL-only on every task: \textbf{+12.7\,pp} on $τ$-retail at 3.2$\times$ compression ($p{<}0.01$), \textbf{+8.7\,pp} on BrowseComp at 2.2$\times$ compression ($p{<}0.05$), and parity on BFCL and AppWorld. Without the router, graph-only delegation regresses 14.6\,pp on AppWorld; the router eliminates this at near-zero cost. A graph-aware executor prompt is required: the same schema without interpretation guidance yields no gain. An oracle analysis reveals 8.6\,pp of additional headroom, motivating execution-time adaptive routing as future work.

</details>


### 89. A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost after Coding-Agent Adoption

- **Authors:** Yegor Denisov-Blanch, Shyam Agarwal, Pavel Azaletskiy, Hao He, Rylan Schaeffer, Brando Miranda, Bogdan Vasilescu, Sanmi Koyejo
- **Published:** 2026-08-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25241v1](http://arxiv.org/abs/2608.25241v1)
- **PDF:** [https://arxiv.org/pdf/2608.25241v1](https://arxiv.org/pdf/2608.25241v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents increase development velocity but also technical debt. Prior work reports only average effects across adopters, hiding wide differences between teams. We introduce RAMP (Repository AI Maturity Profile), a four-level cumulative maturity model grounded in version-controlled artifacts that teams commit to configure AI tools. RAMP runs from behavioral rules and coding standards through named agent definitions to multi-agent orchestration, with observed practice concentrated in the first three levels. Across 441 repositories the levels behave as a cumulative scale, and independent human annotation reproduces RAMP's repository-level labels on 97% of a held-out sample. Adoption is cumulative, forward-only, and set-and-forget: 73.8% of artifacts are committed once and never modified. Re-estimating an existing agent-adoption panel within each stratum, agents accelerate development regardless of maturity (28-38% more commits), but quality diverges: among agent-first repositories, where the contrast is identified, those without committed AI configuration show roughly twice the increase in cognitive complexity (+53% versus +27%) and 1.7x the increase in static-analysis warnings. Because maturity is observational, correlated engineering discipline or model capability may explain part of the gap; we present these findings as hypothesis-generating and release RAMP as a reusable instrument.

</details>


### 90. SpecMine: A Large-Scale Corpus of Spec-Driven Development Artifacts

- **Authors:** Shyam Agarwal, Bogdan Vasilescu
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25202v2](http://arxiv.org/abs/2608.25202v2)
- **PDF:** [https://arxiv.org/pdf/2608.25202v2](https://arxiv.org/pdf/2608.25202v2)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spec-Driven Development (SDD) is a fast-emerging practice in which a structured natural-language specification, written by a developer, or (more often) drafted by an AI tool and then curated by the developer, drives an AI coding agent's implementation. A wave of tooling (GitHub Spec Kit [3], OpenSpec [4], AWS Kiro [5], and dozens of others) has appeared since 2025, yet the artifacts these tools produce have never been studied at scale. We present SpecMine, a corpus that captures SDD in public GitHub repositories through two censuses: a broad census of spec.md/specs.md files covering most tools (470,795 files across 73,030 repositories, attributed to 17 named tools), and a Kiro census of its distinct requirements/design/tasks layout (98,574 files across 12,910 repositories). Each spec is enriched with full repository metadata, complete commit history, and parsed document structure. How a spec becomes code is itself an open question, so for 11 tools we sweep every pull request that touches a spec in their repositories with at least ten stars, capturing 5,992 such PRs across 581 repositories with their changesets. That makes the simplest workflow, spec and implementation changing together in one PR, directly observable, and a census-wide index of 2,421,323 typed references (1.28M to code files, 863k to sibling documents, 152k to PRs, 62k refs, 43k branches, 22k issues) gives a second, independent link from spec to code. SpecMine lets the community study, for the first time, how software is specified in the age of AI agents.

</details>


### 91. Tunable Tool-Call Rates in LLM Agents via Representation Steering

- **Authors:** Yuqi Chen, Vincent Siu, Yang Liu, Dawn Song, Chenguang Wang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25198v1](http://arxiv.org/abs/2608.25198v1)
- **PDF:** [https://arxiv.org/pdf/2608.25198v1](https://arxiv.org/pdf/2608.25198v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deciding whether to call a tool is a core competence of an LLM agent, and a costly one to get wrong: needless calls add latency, accrue cost, and may trigger irreversible side effects, while missing calls leave the model confidently wrong on questions it could only answer through tool-calls. Models manage this balance poorly, both over-using and under-using tools. Existing methods such as post-training and prompt engineering are expensive and difficult to modify at inference time. We show that whether an instruction-tuned model calls a tool can be controlled by a single linear direction in its residual stream, extracted without any training from the model's own tool-use preference signal and turned into an inference-time intervention with no prompt change. Adding the direction with strength $α$ moves the call rate monotonically from near $0\% $ to over $90\%$ while keeping calls well-formed. The steering works in both directions: dialing it down suppresses calls, and dialing it up induces new calls that land precisely on the questions the model cannot answer from its own knowledge. We also show that the direction generalizes to unseen tools with strength comparable to each tool's own direction and without favoring any specific tool choice. With live tool execution, a single sweep of the steering traces a cost/accuracy Pareto frontier and nearly doubles open-domain QA accuracy ($0.29 \! \rightarrow \! 0.56$); the same recipe transfers across a diverse range of models spanning dense, MoE, and multimodal architectures, without any training. Our code is publicly available at https://github.com/YuqiChen4188/Steering-Tool-Use-Propensity.

</details>


### 92. Simulating Cognitive Smart Freight Corridors with Agent-Based Models and Reinforcement Learning

- **Authors:** Madelaine Martinez-Ferguson, Chun Wang, Mustafa Can Camur, Xueping Li
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25193v1](http://arxiv.org/abs/2608.25193v1)
- **PDF:** [https://arxiv.org/pdf/2608.25193v1](https://arxiv.org/pdf/2608.25193v1)
- **Categories:** cs.ET, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Smart freight corridors offer a practical pathway for connected and automated vehicle (CAV) deployment in freight transportation, but physical experimentation is expensive and existing approaches rely on predefined control policies that cannot capture adaptive behaviors. This paper presents an agent-based modeling (ABM) framework coupling a physical infrastructure layer, a connectivity layer (V2X), and a decision layer integrating reinforcement learning (RL) and multi-agent reinforcement learning (MARL) for platoon formation and charging coordination. We evaluate three scenarios (Baseline, Assisted, and Cognitive) using throughput, congestion, energy, emissions, and robustness metrics. Preliminary results indicate that the Cognitive scenario achieves higher throughput and lower congestion than the baseline, while the Assisted scenario delivers meaningful energy savings per kilometer through platooning. Sensitivity analysis shows that the throughput advantage of the smart corridor widens under conditions with high demand and that MARL coordination extracts greater utilization from fixed charging capacity than rule-based assignment.

</details>


### 93. Belief Cascades Drive Persuasion in LLM Agent Networks

- **Authors:** Haoyi Qiu, Genglin Liu, Pranav Narayanan Venkit, Kung-Hsiang Huang, Saadia Gabriel, Chien-Sheng Wu, Nanyun Peng
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25152v1](http://arxiv.org/abs/2608.25152v1)
- **PDF:** [https://arxiv.org/pdf/2608.25152v1](https://arxiv.org/pdf/2608.25152v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems increasingly debate answers, coordinate research, simulate users, and mediate information flows, making agent-to-agent persuasion a basic but undermeasured capability. We introduce a controlled testbed for studying how goal-directed persuaders shift elicited stances in networks of LLM agents grounded in real-world ego-network topologies. Across four LLM backbones, five graphs, and 55 policy statements, we find that persuasion dynamics depend on the interaction between topology, competition, topic, and model prior. Additionally, we show that direct exposure reliably predicts next-round stance change in competing runs, and peer relays carry smaller but measurable influence, showing that agents not assigned to persuade can still transmit persuasive force. Finally, analyzing post text alone misses important movement: planned strategies are only partly realized in executed messages, action choices can diverge from message content, and persuadees rarely state the stance shifts detected by probes. These results argue for evaluating multi-agent persuasion as a trajectory- and exposure-level process, using belief probes, exposure provenance, and action logs to identify who influenced whom and whether visible language reflects underlying stance movement.

</details>


### 94. SimVerity: When Does Simulated Agent Success Survive Physical Deployment?

- **Authors:** Zhonghao Zhan, Yefan Zhang, Krinos Li, Hamed Haddadi
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25067v1](http://arxiv.org/abs/2608.25067v1)
- **PDF:** [https://arxiv.org/pdf/2608.25067v1](https://arxiv.org/pdf/2608.25067v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulated evaluation is widely used to benchmark AI agents, yet how much evidence a simulated pass provides about physical deployment has not been systematically quantified. We present SimVerity, a verdict-transfer assurance framework: it replays matched scenarios on target smart home deployments and cross-validates agent execution against independently qualified physical witnesses. Our evaluation highlights that deployment success is a real-world process, not a static property in simulation: completion, reported state, observable effect, and settled outcome diverged within the same execution. Although an advanced simulator cleared all 240 light trials, a camera caught 42 sub-second failures invisible to settled-state checks. False clearance was predictable: a risk profile learned from measured trials and locked before evaluation predicted failures on a path it never physically measured, beating a property-blind baseline in all eleven held-out sessions across two cohorts. Agent auditability was also measurable: switching one agent loop's model-client/serving configuration raised its scenario-matching share from 52-88% to 100%. Finally, a second qualified simulator added no independent cross-check: it never disagreed on any overlapping case, and only physical measurement exposed their shared blind spots. SimVerity turns verdict transfer into an explicit decision: clear, abstain, or escalate before deployment.

</details>


### 95. LifePlanner: Evaluating LLM Agents for Geo-spatial Planning with Social Media Data

- **Authors:** Zhen Dong, Yuning Peng, Yutao Shi, Lei Zhong, Yongsen Mao, Yuan Liu, Haiping Wang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.25039v1](http://arxiv.org/abs/2608.25039v1)
- **PDF:** [https://arxiv.org/pdf/2608.25039v1](https://arxiv.org/pdf/2608.25039v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Geo-spatial planning, like trip design, is a realistic testbed for LLM agents because it requires grounded tool use, noisy evidence retrieval, and multi-constraint reasoning. Most benchmarks, however, only provide clean geospatial data and tools, missing the open-ended social signals that people use in daily planning. We introduce LifePlanner, a benchmark that enriches map data with large-scale local social media posts and provides access through an MCP toolset. LifePlanner provides an evaluation suite spanning four task categories and three difficulty levels. Experiments show frontier LLMs perform well on simple retrieval but degrade sharply on complex planning, with the Pass Rate dropping to 40.2%. Results show that failures mainly stem from incomplete evidence acquisition from such a large multimodal database, imprecise tool use, and weak constraint integration rather than model size or reasoning length, suggesting that future progress requires effective grounded planning instead of scaling alone.

</details>


### 96. SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL

- **Authors:** Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24870v1](http://arxiv.org/abs/2608.24870v1)
- **PDF:** [https://arxiv.org/pdf/2608.24870v1](https://arxiv.org/pdf/2608.24870v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before optimizing a token-mean actor loss. We show that trajectory centering generally does not center the token-weighted quantity consumed by the actor, and fix the mismatch by standardizing terminal-outcome advantages under the action-token measure. We additionally organize prompt evidence by the policy event that generated it rather than learner receipt order. Across matched runs on ALFWorld at two model scales and on Math-TIR, SPO++ improves online learning efficiency over SPO. A paired ablation identifies action-token-measure normalization as the strongest tested component.

</details>


### 97. Test-Time Collaborative Classification over Multi-Agent Networks

- **Authors:** Ping Hu, Mert Kayaalp, Ali H. Sayed
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24787v1](http://arxiv.org/abs/2608.24787v1)
- **PDF:** [https://arxiv.org/pdf/2608.24787v1](https://arxiv.org/pdf/2608.24787v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The increasing heterogeneity of multi-agent systems poses significant challenges for jointly training a global model across agents. At the same time, cooperative inference between agents has long been recognized as a powerful mechanism for distributed decision making over networks. Motivated by these observations, we propose a collaboration framework for distributed binary classification over multi-agent networks, where a set of independently trained agents, potentially differing in architecture, feature space, or modality, coordinate their actions during test time to form collective predictions. This coordination is achieved by exchanging local decision statistics through a distributed learning protocol. We develop a theoretical and experimental study of this independent training and cooperative inference paradigm, and examine its performance under different communication budgets and distributed learning rules. We establish classification error guarantees under sufficient, finite-round, and finite-precision communication, together with PAC-style generalization bounds. These results capture the influence of model heterogeneity, network topology, combination policy, and communication constraints on prediction accuracy. Taken together with the experimental results, they reveal both the price of independent training and the benefit of collective prediction for the proposed distributed decision making framework with models learned from data.

</details>


### 98. SkillForge: Evolving Verifiable Skills for Reinforcement Learning Agents

- **Authors:** Shidong Yang, Ziyu Ma, Tongwen Huang, Xucong Wang, Renda Li, Yiming Hu, Yong Wang, Xiangxiang Chu
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24747v1](http://arxiv.org/abs/2608.24747v1)
- **PDF:** [https://arxiv.org/pdf/2608.24747v1](https://arxiv.org/pdf/2608.24747v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are trained with reinforcement learning (RL) for complex decision-making tasks. However, most RL-trained agents remain episodic and cannot accumulate reusable knowledge across episodes. Recent skill-based approaches, such as SkillRL, attempt to address this issue by extracting skills from raw trajectories, but treat the skill bank as an append-only repository without verifying whether stored skills remain effective. In this paper, we propose SkillForge, a framework for continuous skill evolution that enables skills to be verified and refined through environment interaction. By making skill usage explicit during agent interaction, RL can directly optimize both environment actions and skill invocation decisions. SkillForge further introduces evidence-based skill verification and multi-pathway skill induction, allowing the skill bank to continuously grow while maintaining its quality. Extensive experiments on ALFWorld, WebShop, and AppWorld show that SkillForge consistently outperforms SkillRL, demonstrating the effectiveness of continuously verified skills in training stronger LLM agents.

</details>


### 99. Meta$^n$: Recursive Self-Improvement through Emergent Depth

- **Authors:** Zae Myung Kim, Young-Jun Lee, Seungyeon Jwa, Dongyeop Kang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24735v1](http://arxiv.org/abs/2608.24735v1)
- **PDF:** [https://arxiv.org/pdf/2608.24735v1](https://arxiv.org/pdf/2608.24735v1)
- **Categories:** cs.AI, cs.CL, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-improving LLM agents refine answers, not the process that produces those answers. Systems that add a meta-level hold that level fixed, and those that edit themselves must leave part of their own editing machinery untouched to stay stable, capping the meta-depth they realize at roughly two. We present Meta$^n$, which keeps the meta-operation fixed and recurses on its input instead. That operation, $Ω$, is applied repeatedly to its own products, reading the traces of the solver stack below together with the code that produced them, then writing the next layer as a strategic pre-process and a library of callable helpers. Because $Ω$ never changes, it cannot destabilize the system, and because its input strictly grows, each layer reasons from a higher vantage than the last. Depth is set by convergence rather than fixed in advance, and an evolutionary archive searches over layer chains. Across two backbones, Meta$^n$ outperforms prior self-improving agents on all eight benchmark families. The sharpest case is ARC-AGI-2, built to resist skill memorization, where it alone scores above zero. Ablations indicate that most of the gain from recursion comes from the conditioning each layer passes to the next, and distinct layer roles emerge with depth although no prompt prescribes them. Code available at https://github.com/minnesotanlp/meta-n

</details>


### 100. Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling

- **Authors:** Leonardo Liparulo, Francesco Pierri
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26199v1](http://arxiv.org/abs/2608.26199v1)
- **PDF:** [https://arxiv.org/pdf/2608.26199v1](https://arxiv.org/pdf/2608.26199v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

We ask whether AI agents powered by locally deployed large language models can reliably automate expert-defined hardware design workflows in an industry-realistic tool-calling setting. In these environments, engineers issue repetitive, dependency-ordered operations---such as creating components, adding ports, and wiring connections---through specialised tools. Confidentiality constraints on component specifications and naming conventions often preclude hosted proprietary APIs, motivating the use of locally deployed models. To study this setting, we build a Model Context Protocol (MCP) server that reproduces the state and dependency logic of a proprietary hardware design tool used in embedded system development and construct a benchmark covering single-operation edits, multi-step dependency chains, invalid requests, misspelled prompts, and multi-server tool contexts. We evaluate seven open-source models comparing pipeline choices including system prompts, tool-description detail, context scope, and single-agent versus multi-agent architectures. Results show that strong models can achieve near-complete expected-call coverage on the benchmarked workflows, but reliability depends strongly on both task structure and agent configuration. Comprehensive tool descriptions consistently reduce failures, few-shot prompting can cause severe inaction for some models, cumulative context harms constrained models, and multi-agent decomposition helps weak workers or long sessions at the cost of additional calls. These findings provide practical guidance for deploying local LLM agents in stateful hardware design environments.

</details>


### 101. Agentic AI for operating scientific instruments for nanoscale characterization

- **Authors:** Zahra Ayar, Marcos Penedo, Mahdi Mehdikhani, Nahid Hosseini, Prabhu Prasad Swain, Georg E. Fantner
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.26198v1](http://arxiv.org/abs/2608.26198v1)
- **PDF:** [https://arxiv.org/pdf/2608.26198v1](https://arxiv.org/pdf/2608.26198v1)
- **Categories:** cs.AI, physics.ins-det


> Summary unavailable.


<details>
<summary>Abstract</summary>

Operating a scientific instrument such as an atomic force microscope (AFM) requires continuous expert decision-making. A trained user defines the experimental intent, translates it into instrument commands, assesses incoming data, adjusts imaging parameters, and post-processes the final image. Existing automation usually addresses only parts of this workflow through hard-coded routines, task-specific controllers, or trained machine-learning models. Here we present an agentic-AI framework that operates the executable part of the AFM workflow using a general-purpose, tool-augmented large language model connected to instrument functions through the Model Context Protocol (MCP). The framework consists of 3 MCP-based agents: AFM Messenger converts natural-language instructions into checked instrument commands; AFM Pilot assesses image quality through a large language model (LLM) and, if necessary, adapts imaging parameters; and AFM Doctor diagnoses image artifacts and applies transparent post-processing from a pre-approved tool set. Because the language model performs image assessment rather than a fixed scalar objective or external optimizer, the same strategy can be applied across sample types and imaging modes without specific retraining. Safe hardware operation is enforced through an ambiguity check layer before execution. Benchmarking against fine-tuned and off-the-shelf tool-using models shows that this guarded execution layer, rather than model capability alone, reduces wrong-command execution to zero. In live experiments on different samples, AFM Pilot matched expert operators in image quality, iteration count, and tuning time, with no significant difference. These results demonstrate a safe route to agentic operation of scientific instruments, where experimental intent remains human-defined while command execution, image-based tuning, and post-processing are delegated to AI agents.

</details>


### 102. Pivot-and-Station Multi-Agent Path Finding: Solvability, Complexity, and Algorithms

- **Authors:** Andrea Di Nezza, Mihir Patel, Fabio Fagnani, Sara Bernardini
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24585v1](http://arxiv.org/abs/2608.24585v1)
- **PDF:** [https://arxiv.org/pdf/2608.24585v1](https://arxiv.org/pdf/2608.24585v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated high-density storage systems (warehouses, robotic parking, plant logistics, etc.) require fleets of agents to move through scarce task-critical resources and then park without obstructing future operations. We introduce Pivot-and-Station Multi-Agent Path Finding (PS-MAPF), a MAPF variant in which a subset of tasked agents must each visit one of a set of interchangeable pivots (e.g., workstations) before the entire fleet terminates at anonymous stations, one agent per station. We characterize solvability completely: every instance on a 2-edge-connected graph is solvable, and, on arbitrary connected graphs, a structural effective-distance measure relative to the number of unoccupied vertices gives a necessary and sufficient condition. We prove that minimizing station-makespan or station-flowtime is NP-hard already with a single pivot. We present three algorithms, a complete baseline, a SAT-based optimal solver, and Pivot-Prioritized Planning (PPP), the last solving 74-89% of benchmark instances with makespan and flowtime orders of magnitude below the baseline.

</details>


### 103. EviDx: Evidence-Aware Active Diagnosis with Scaffolded LLM Agents

- **Authors:** Lihang Zeng, Shaoting Zhang, Xiaofan Zhang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24570v1](http://arxiv.org/abs/2608.24570v1)
- **PDF:** [https://arxiv.org/pdf/2608.24570v1](https://arxiv.org/pdf/2608.24570v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical diagnosis is an active evidence-seeking process in which clinicians acquire evidence, update competing hypotheses, and decide when the available evidence is sufficient for diagnosis. Yet many medical diagnosis systems built around large language models (LLMs) still formulate diagnosis as static case-to-answer prediction, with limited support for evidence acquisition. Agentic LLMs offer a dynamic alternative through tool use and intermediate diagnostic trajectories, but existing systems often under-specify how patient evidence should be exposed, scaffolded, and controlled at runtime. We introduce EviDx, an evidence-aware active diagnosis framework that pairs patient-specific diagnostic environments with a clinical diagnostic scaffold and an observer-guided runtime harness. In EviDx, $\mathcal{E}$-Synthesis constructs interactive environments from raw clinical cases; the scaffold organizes role-specialized agents, evidence tools, and evolving evidence states; and the harness regulates diagnostic termination by tracking uncertainty and evidence coverage. A 3-level evaluation pyramid assesses execution robustness, reasoning dynamics, and diagnostic outcomes. Experiments show that EviDx improves diagnostic performance and process stability while revealing model-dependent capability boundaries.

</details>


### 104. When "Must" Becomes "Maybe": Constraint Weakening in LLM Agent Workflows

- **Authors:** Yiheng Sun, Huifei Wang, Yancheng Zhu, Zhenyu Li, Zebin Zhao, Yifan Yuan
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24569v1](http://arxiv.org/abs/2608.24569v1)
- **PDF:** [https://arxiv.org/pdf/2608.24569v1](https://arxiv.org/pdf/2608.24569v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents coordinate complex tasks through multi-role and multi-stage workflows. Upstream state is repeatedly transformed into intermediate language artifacts, such as summaries, plans, tickets, memories, and handoff notes, from which downstream components act. For action-constraining state, topical retention is insufficient: an artifact may mention an unresolved condition while changing it from a requirement that must be resolved before execution into information that may merely inform the next action. We study this action-binding role as operational state preservation. Safety blockers provide a controlled instance because each source state has an explicit prerequisite, authority, fallback, and execution consequence. We condition on correct upstream identification, vary the handoff transformation, and evaluate an executor restricted to the resulting artifact. Across 1,296 controlled synthetic episodes, direct-handoff controls preserve every blocker, whereas compression, plan assimilation, convergence, ownership deferral, and precedent substitution repeatedly turn binding state into caveats or non-binding considerations. Normal handoff compression produces 100.0% deactivation and 54.2% forbidden action. Restoring all four state fields raises preservation to 100.0% and reduces forbidden action to 0.0%. Fixed-artifact interventions further separate preservation from containment: downstream verification eliminates forbidden action while artifact deactivation remains 95.3%. These results identify a state-transmission failure between information extraction and action. Handoff transformations can retain state content while weakening its constraints on downstream action. Semantic availability does not guarantee operational preservation.

</details>


### 105. StrokeGuard: A Multi-Agent Guided System for Prehospital Stroke Assessment

- **Authors:** Wentao Yang, Zhenye Xu, Ruoyi Li, Musen Zhang, Yao Guo
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24555v1](http://arxiv.org/abs/2608.24555v1)
- **PDF:** [https://arxiv.org/pdf/2608.24555v1](https://arxiv.org/pdf/2608.24555v1)
- **Categories:** cs.HC, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prehospital stroke assessment aims to accurately identify stroke symptoms and make rapid decisions through standardized procedures within an extremely narrow time window, thereby saving valuable time for subsequent treatment. In clinical practice, FAST-based scales are widely used for prehospital stroke assessment by issuing instructions that guide subjects to perform specific actions to screen facial, arm, and speech functions. However, in home and community settings, non-clinical users often encounter challenges such as inaccurate descriptions, incomplete symptom observation, and difficult operational procedures, which may lead to inaccurate or biased assessment results. To address these challenges, this paper presents StrokeGuard: a multi-agent guided system designed for prehospital stroke assessment that makes mobile FAST screening more standardized and executable. Specifically, to overcome the limitations of traditional single-agent systems in terms of procedural fault tolerance and user guidance capability, StrokeGuard adopts a dual-channel agent mechanism that separates formal assessment (i.e., facial palsy, arm weakness, speech impairment) from procedural support (e.g., step prompts, error correction, and real-time feedback). It guides the assessment process through multi-agent collaboration, dual-channel interaction, state-machine control, and stage-local fallback recovery mechanisms. Stage-specific scoring is delegated to constrained pretrained video assessment modules, while evidence source records are integrated with structured report generation. The user evaluation uses MATES-9, an exploratory scale for measuring user experience in multistep AI-guided tasks. In a simulated prehospital scenario, StrokeGuard improves the MATES-9 total score over a paper FAST-style form by 10.83 points, corresponding to a 23.8% relative increase.

</details>


### 106. PeakBench: Benchmarking Resource-Aware Tool Invocation in LLM Agents

- **Authors:** Zhi-Kai Chen, Xu-Xiang Zhong, Song-Yan Li, De-Chuan Zhan, Han-Jia Ye
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24509v1](http://arxiv.org/abs/2608.24509v1)
- **PDF:** [https://arxiv.org/pdf/2608.24509v1](https://arxiv.org/pdf/2608.24509v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly solve tasks by invoking multiple tools, where parallel execution is essential for low latency but difficult to manage safely. Existing agent benchmarks primarily evaluate tool selection, argument generation, and end-to-end success under mostly serial execution, largely overlooking valid parallelization and resource-constrained scheduling. This missing scheduling dimension creates a practical failure mode: serial execution is safe but slow, while resource-agnostic parallel execution is fast but prone to avoidable resource overflows. To address this gap, we introduce PeakBench, a benchmark of executable multi-tool workflows with execution-grounded dependency annotations and measured resource profiles. A central challenge in evaluating such workflows is attribution: failures and inefficiencies may arise from incorrect dependency planning, poor resource-constrained scheduling, or both. PeakBench addresses this challenge with a two-part evaluation framework that disentangles logical planning from physical scheduling, with dedicated metrics for each dimension. Using this framework, we show that strong logical planning does not reliably translate into safe or efficient execution under resource constraints. We further show that exposing resource information can reduce avoidable overflows and improve resource utilization, making PeakBench a useful testbed for diagnosing resource-aware agent behavior. Code is available at https://github.com/Czzzk/Staggering-the-Peaks.

</details>


### 107. Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems

- **Authors:** Yarden Bakish, Amir Dudai, Roy Ganz, Oren Nuriel, Elad Ben Avraham, Mor Shpigel Nacson, Ron Litman
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24361v1](http://arxiv.org/abs/2608.24361v1)
- **PDF:** [https://arxiv.org/pdf/2608.24361v1](https://arxiv.org/pdf/2608.24361v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems are increasingly deployed in real-world applications, where failures can be costly and difficult to localize. Despite growing efforts to automate failure attribution, diagnosing failed runs still largely relies on human engineers. Yet engineers rarely debug complex systems by reading raw logs end to end. Instead, observability tools organize traces around components, actions, and dependencies to support targeted navigation. We hypothesize that modern LLMs can benefit from the same paradigm. To test this hypothesis, we introduce Adaptive Influence Graphs (AIGs), a two-stage agentic framework that first transforms a failed trace into a structured graph and then navigates it to identify the critical error. Across multiple models, we show that richer trace representations consistently improve failure attribution, with adaptive graph construction and agent-directed traversal yielding the strongest results. AIGs establish a new state of the art on Who&When, the standard benchmark for multi-agent failure attribution. This affirms our hypothesis that attribution depends not only on the diagnosing model, but also on how the trace is represented and explored.

</details>


### 108. The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents

- **Authors:** Roy Ganz, Mor Shpigel Nacson, Adi Kalyanpur, Ron Litman
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24358v1](http://arxiv.org/abs/2608.24358v1)
- **PDF:** [https://arxiv.org/pdf/2608.24358v1](https://arxiv.org/pdf/2608.24358v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents perform long-running tasks spanning dozens of model calls, tool uses, and code edits. As these runs unfold, users face a practical cost-quality trade-off: escalating to a stronger model when a cheaper one struggles, or downshifting once the hard reasoning is complete. Each switch requires the receiver to continue a non-native trajectory produced by another model. We study how this handoff affects quality and cost, and how varying the trajectory information inherited by the receiver changes the outcome. Using pairs of low-cost, low-capability (LC) and high-cost, high-capability (HC) models from the Claude and GPT families, we vary handoff direction, timing, and interface, comparing full-trajectory transfer, compaction, and trajectory removal while preserving the repository state. Across both model families, full-trajectory escalation recovers less than half of the LC-to-HC quality gap while incurring a substantial cost premium. We term this cost-quality penalty the handoff tax. By contrast, downshift offers a favorable cost-quality point. Interestingly, the preferred interface also reverses with direction: reducing LC-model trajectory information improves escalation quality, whereas removing the HC-model trajectory reduces downshift quality.

</details>


### 109. Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

- **Authors:** Eran Hirsch, David Wan, Han Wang, Elias Stengel-Eskin, Mohit Bansal, Ido Dagan
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24306v1](http://arxiv.org/abs/2608.24306v1)
- **PDF:** [https://arxiv.org/pdf/2608.24306v1](https://arxiv.org/pdf/2608.24306v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep research (DR) systems produce long-form cited reports by orchestrating multiple agents that search and synthesize information from the web. Citations are the primary mechanism for evaluating the faithfulness of these reports, yet current DR systems exhibit poor citation recall. Moreover, improving citation recall is challenging because DR systems are complex multi-agent architectures where information passes through agents like a telephone game, and both content and citations can get corrupted along the way. We propose an evaluation method that pinpoints which agent introduced each error by locally testing agent invocations for faithfulness and verifiability relative to their own inputs. Furthermore, we propose a four-type taxonomy to categorize the discovered errors: hallucination, uncited input reliance, uncited output, or insufficient citations. Applying our method to three top-ranked open-source DR systems, we obtain actionable diagnostics. Almost every agent makes a lot of mistakes with the exception being those that summarize a single document. We find that the dominant error type varies systematically across agents, where the orchestrator mistakes are mostly citation-related. We find that 84.7% of final-report errors in AI-Q originate at the orchestrator, roughly 31% of them hallucinations and the rest citation mistakes. Guided by these insights, we demonstrate that two simple interventions raise citation recall by 5% without degrading output quality.

</details>


### 110. ReproAgent: Contract-Guided Paper-to-Code Reproduction

- **Authors:** Xue Hu, Zewei Pan, Zhongyuan Wang, Zhou Liu, Zeli Su, Wentao Zhang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24291v1](http://arxiv.org/abs/2608.24291v1)
- **PDF:** [https://arxiv.org/pdf/2608.24291v1](https://arxiv.org/pdf/2608.24291v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Paper-to-code reproduction asks scientific AI agents to turn research papers into executable repositories that preserve the paper's method, protocol and artifacts. This is difficult because the specification is split: explicit paper content such as algorithms, metrics and artifacts is often lost across long agent trajectories, while implicit details such as framework defaults and conventions inherited from related work are absent from the paper. We introduce ReproAgent, a four-stage Prepare--Plan--Generate--Repair pipeline built around a persistent implementation contract with two channels: an implementation-requirement channel that turns paper snippets into code obligations, and a reference-evidence channel that retrieves content and structure evidence from related repositories. Both are bound to work packages, projected into file-level contracts, and consumed across generation and repair. On PaperBench Code-Dev, ReproAgent reaches the highest mean score among same-backbone scaffolds under both Claude-Sonnet-4.5 and Gemini-3-Flash. End-to-end channel ablations and per-paper cases support the contribution of both channels. Code and experimental artifacts are publicly available.

</details>


### 111. SA-Bench: Evaluating Semantic Alignment in LLM-Based Paper Reproduction

- **Authors:** Xue Hu, Zewei Pan, Zeli Su, Zhou Liu, Wentao Zhang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24252v1](http://arxiv.org/abs/2608.24252v1)
- **PDF:** [https://arxiv.org/pdf/2608.24252v1](https://arxiv.org/pdf/2608.24252v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can generate paper reproduction code, yet often produce scientifically unfaithful implementations. We define this failure mode as semantic drift, where generated code silently diverges from the paper's specifications. We introduce SemanticAlign-Bench(SA-Bench), a diagnostic benchmark covering 30 papers from ICLR, ICML and NeurIPS 2025. For each paper, we decompose its specifications into atomic and verifiable implementation claims, which we call Semantic Alignment Units (SAUs) and evaluate repositories along four diagnostic dimensions spanning numerical, methodological, protocol and ordering drift. In total, we construct 1,491 SAUs across five ML domains and evaluate 12 generator configurations (4 models $\times$ 3 scaffolds). Even the strongest configuration (Claude+PaperCoder) achieves a mean SAU score of only 0.301 out of 1.0, with an overall mean of 0.221 across 360 evaluations. A failure taxonomy reveals that agents attempt most requirements but implement them incorrectly, with implementation mismatch and stubs accounting for the majority of zero-scored claims. Our analysis further indicates that scaffolds optimized for executability provide limited leverage for scientific reproduction; narrowing the gap requires scaffolds that prioritize semantic specification verification. The benchmark, annotations and evaluation pipeline are publicly available.

</details>


### 112. STRIVE: Multi-Agent Structured Temporal Reasoning with Integrated Verification for Longitudinal Radiology Report Generation

- **Authors:** Junyeong Maeng, Eunsong Kang, Heung-Il Suk
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24237v1](http://arxiv.org/abs/2608.24237v1)
- **PDF:** [https://arxiv.org/pdf/2608.24237v1](https://arxiv.org/pdf/2608.24237v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Longitudinal radiology report generation (LRRG) requires identifying both current findings and their changes relative to a prior study. Existing methods jointly model diagnosis, attribute estimation, temporal comparison, and language generation within implicit representations, which can cause task interference, obscure the evidence underlying each decision, and limit error traceability. They also model progression states as independent labels, ignoring their ordered structure and thus treating missed changes and direction reversals equally. We present STRIVE, Multi-Agent Structured Temporal Reasoning with Integrated Verification for LRRG, which decomposes clinical reasoning into specialized Diagnosis, Attribute, and Temporal Change Agents that produce explicit intermediate evidence. In particular, the Temporal Change Agent is further post-trained using Progression-Aware GRPO, a verifiable, shaped reward that assigns partial credit to direction-preserving errors while scoring direction reversals lowest. STRIVE performs verification at two stages: a deterministic Consistency Gate reconciles the agent outputs before report generation, and a Validation Agent checks whether the generated report is supported by the aggregated clinical evidence. On Longitudinal-MIMIC, STRIVE attains the best clinical efficacy among recent methods and more than doubles Longitudinal Change Concordance (LCC), a measure of temporal agreement with the reference report, over the strongest baseline.

</details>


### 113. DeepRepoQA: Code Repository Question Answering with Deep Agent Exploration

- **Authors:** Weihan Peng, Yuling Shi, Yingwei Ma, Longfei Yun, Beijun Shen, Xiaodong Gu
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24221v1](http://arxiv.org/abs/2608.24221v1)
- **PDF:** [https://arxiv.org/pdf/2608.24221v1](https://arxiv.org/pdf/2608.24221v1)
- **Categories:** cs.SE, cs.CL, cs.PL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Answering developer questions about a software repository is a critical yet under-explored problem in software engineering. While existing repository understanding methods have advanced the field, they predominantly rely on surface-level code retrieval and lack the ability for deep reasoning over multiple files, complex software architectures, and grounding answers in long-range code dependencies. To address these limitations, we propose DeepRepoQA, a novel question answering (QA) framework for repository-level code understanding. DeepRepoQA builds on an agentic framework where LLM agents find answers through a systematic tree search over the repository structure. A Monte-Carlo Tree Search (MCTS) mechanism is employed to empower agents to dynamically search, navigate, and inspect code, enabling effective multi-hop reasoning over long-range code dependencies. Comprehensive experiments on the SWE-QA benchmark demonstrate substantial performance gains over strong baselines, validating the effectiveness of systematic MCTS-guided exploration for multi-hop repository reasoning.

</details>


### 114. Agentopia on a Consumer GPU: A Reduced-Scale Long-Horizon Port with an 8B Model

- **Authors:** Luo Huan
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24215v1](http://arxiv.org/abs/2608.24215v1)
- **PDF:** [https://arxiv.org/pdf/2608.24215v1](https://arxiv.org/pdf/2608.24215v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent social simulation has demonstrated compelling results, but Agentopia was evaluated with 100 agents over 10 simulated years using Qwen3.5-397B-A17B, leaving the behavior of reduced-scale deployments on consumer hardware unclear. In this paper, we implement and evaluate a reduced-scale Agentopia port on a single NVIDIA RTX 5070 Ti(12 GB VRAM) using Qwen3-8B-AWQ, a 4-bit quantized model. We introduce three structural adaptations for this setting: (1) system-managed layered memory compression, (2) four activity blocks per simulated day, and (3) explicit physical- and mental-health state variables. Across three independent stochastic runs, two runs completed 52 weeks and the third completed 50 weeks before reaching the context limit, totaling 154 system-weeks (770 agent-weeks). No agent died,and no threshold-based health warning was logged; activity records containing at least one NO_RESPONSE field occurred at rates of 10.15-10.29% across runs. A 52-week memory-off run tied L2/L3 artifact production to layered memory; a separate 10-week comparison associated four daily time blocks with 2.72 times more finalized records and lower lexical duplication, but a higher missing-field rate. These comparisons do not support causal behavioral claims. We release validated configurations, derived audits, analysis scripts, aggregate figure data, and our implementation changes in a public fork; raw runs and initial persona data are excluded because their redistribution provenance is not fully resolved.

</details>


### 115. AHEAD: Adaptive Hindsight with Environment-Augmented Distillation for Agentic RL

- **Authors:** Xiaolong Jin, Dingmin Wang, Vijay Lingam, Varun Kumar
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24114v1](http://arxiv.org/abs/2608.24114v1)
- **PDF:** [https://arxiv.org/pdf/2608.24114v1](https://arxiv.org/pdf/2608.24114v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training multi-turn LLM agents with reinforcement learning typically relies on trajectory-level rewards, which assign a uniform advantage to every step and cannot identify which decisions led to success or failure. Self-distillation methods can provide finer-grained supervision by augmenting RL with privileged information. However, existing approaches usually apply the same type of privileged information to every step in an indistinguishable manner, ignoring a key asymmetry: routine steps need little additional guidance, while critical error steps require corrective direction that environment feedback alone cannot provide. We propose AHEAD, a step-aware framework that matches different supervision sources to different step types. The teacher receives environment feedback on all steps as a grounded dense signal, and additionally receives LLM-generated corrective hints on error steps to supply the direction that environment feedback lacks. The method introduces minimal changes to the standard GRPO algorithm. Across ALFWorld, WebShop, and Search-based QA, and across three model scales, AHEAD raises task success (+13.3 points on ALFWorld and +11.0 on WebShop at 7B over GRPO), reaches a given success rate in fewer training steps, and solves tasks within tighter interaction budgets than outcome-only RL and prior self-distillation baselines.

</details>


### 116. Knowing When to Ask for Help: Bayesian Self-Escalation in Hierarchical LLM Agents

- **Authors:** Nadeem Shaikh
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24087v1](http://arxiv.org/abs/2608.24087v1)
- **PDF:** [https://arxiv.org/pdf/2608.24087v1](https://arxiv.org/pdf/2608.24087v1)
- **Categories:** cs.LG, cs.AI, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current LLM agent systems decide delegation before reasoning begins (a router picks a model) or after a response is complete (a verifier scores it and may retry). We study a third regime: an agent that recognises, during its own reasoning, that it is unlikely to succeed and transfers control to a stronger model. We formulate intra-generation delegation as a Bayesian optimal-stopping problem over a learned competence posterior -- an online estimate of the agent's eventual task success whose sufficient statistics are learned from labelled trajectories, not read off raw entropy. We derive the myopic escalation threshold in closed form, characterise the optimal policy via dynamic programming, and prove that the optimal policy is a time-varying threshold with no shape assumption on the raw signal. We further prove exponential separation of the oracle belief at the Chernoff-information rate of the signal, a regret bound governed by the calibration of the posterior, and a finite-sample guarantee: with n labelled calibration trajectories the deployed plug-in policy's regret decays as 1/sqrt(n). A controlled simulation study confirms each prediction of the theory, including the predicted 1/sqrt(n) rate. We additionally report a real-model validation on a Qwen2.5-Coder 1.5B->7B code cascade (MBPP, 257 tasks), confirming two of three pre-registered predictions: the escalation frontier dominates post-hoc routing at equal cost, and the cumulative competence belief's discrimination rises over generation.

</details>


### 117. AgentWorld: Personality-Aware Reliability Evaluation for Agentic Information Retrieval

- **Authors:** Gunja Agarwal, Arup Kumar Das, Arun Menon, Jitesh Chandra Mishra, Vignesh Divakaran
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24076v2](http://arxiv.org/abs/2608.24076v2)
- **PDF:** [https://arxiv.org/pdf/2608.24076v2](https://arxiv.org/pdf/2608.24076v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluation of agentic information retrieval remains limited to scripted interactions with uniform users, missing both natural personality diversity and adversarial brittleness. We present AgentWorld, a simulation framework combining (i)Big Five (OCEAN) personality-driven user populations with stateful tool-use environments; (ii)the pass$^k$ consistency metric with structured fault classification, partial-credit scoring, and dual-control handoff verification; (iii)score-thresholded training-data export in six fine-tuning formats; and (iv)an adversarial Risk Analyser that snapshots required-intermediate-state spines, branches Monte-Carlo rollouts under four task-aware perturbation types, and quantifies risk via $ΔP / ΔT$ scoring, Dempster--Shafer evidence fusion, and Shapley attack-category attribution. Three experiments demonstrate the framework: a conversational analytics agent across 10 OCEAN personas (240 evaluator judgments); a customer-support agent across 5 tasks $\times$ 4 persona variants; and adversarial stress-testing of 5 tasks revealing pre-existing trajectory brittleness ($V_{\min}=0.375$ without perturbation) and tool/infrastructure-layer attack dominance (Shapley: 46% system, 38% action). Personality variation surfaces failure modes uniform testing cannot expose---cross-domain leakage, contextual drift, a 0.27-point quality gap, and 50% vs. 100% pass-rate across personas on the same task---while the Risk Analyser quantifies trajectory-level brittleness that pass$^k$ alone cannot measure.

</details>


### 118. Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems

- **Authors:** CheolWon Na, Hao Ni, Lukasz Szpruch, Zhangyang Wang, Dhagash Mehta, Saurabh Nagrecha, Alejandro Lopez-Lira, Chanyeol Choi, Yongjae Lee, Jee-Hyong Lee
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24069v1](http://arxiv.org/abs/2608.24069v1)
- **PDF:** [https://arxiv.org/pdf/2608.24069v1](https://arxiv.org/pdf/2608.24069v1)
- **Categories:** cs.AI, cs.CE, cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent trading systems, in which specialized agents collaborate through structured communication to produce trading decisions, are moving rapidly from research prototypes to live deployments that control real assets. The same inter-agent communication that makes them effective also exposes them: a corrupted signal can propagate to the final decision and translate into realized financial loss. Unlike prior attacks that presume privileged access to system internals, we restrict the adversary to what is practically reachable---the source data and prompts agents consume---yielding a low-barrier, and thus democratized threat model instantiated as role-specific adversaries.
  We present the first systematic empirical study in the financial domain to characterize how an adversarial signal enters a multi-agent trading system and how far it survives toward the decision. Along the role axis, we decompose a widely-used trading pipeline into four functional roles---Analyst, Researcher, Trader, and Risk Manager---and pair each with an attack matched to its interface. Along the structural axis, we evaluate four communication topologies under data- and agent-level attacks, using the Adversarial Signal Preservation Score (APS) as a post-hoc lens on why some designs are more robust than others. We conduct experiments across five assets, two backbones, and two target directions. A central finding is that no architecture is inherently robust. These findings provide insights for the future design of safer and more robust agentic trading systems.

</details>


### 119. PinSieve: Production Selective VLM Serving and a Governed Memory Flywheel for Enterprise Content-Quality Triage

- **Authors:** Chuqing Gao, Yuanfang Song, Jonathan Zhang, Yifan Wu, Vishwakarma Singh, Qinglong Zeng, Andrey Gusev
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24040v1](http://arxiv.org/abs/2608.24040v1)
- **PDF:** [https://arxiv.org/pdf/2608.24040v1](https://arxiv.org/pdf/2608.24040v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI agents in production often need to be bounded, stateful, observable, and governable rather than fully autonomous. We present PinSieve, a production case study in a large-scale content-quality pipeline. Its deployed component is a selective vision-language-model (VLM) Serving Agent that operates only on the grey-zone slice left unresolved by lightweight upstream models, exposes a scalar routing score online, and preserves controlled human escalation. On this slice, the deployed system filters 2.05x more non-actionable items than the previous production module while slightly reducing estimated miss rate; after promotion, it improves review productivity by 25.7%, reduces normalized operating cost by 16.2%, and moves signal delivery from next-day to same-day. We then study maintenance through a governed memory flywheel under selective feedback, where escalated items are reviewed by default and auto-passed items are labeled mainly through audit sampling. Feedback Memory records routing traces, observation paths, audit propensities, and replay metadata for evaluation and debugging. The Data Curation Agent uses a bounded proposal-verifier loop over representative, uncertainty, recency, and fresh-review replay, with positive-rate and score-bin guardrails before batch acceptance. In chained monthly refresh over six months of production data, this design reduces average FNR@50% from 17.73% under representative random replay to 13.29%. A Reasoning Review Agent audits teacher-generated rationales and supports keep/repair/drop decisions. Production claims are attributed only to the deployed Serving Agent; replay and rationale-review results are offline or sampled-governance evidence. The same serving-agent recipe has been adopted to several additional internal signals, suggesting transferability beyond one task.

</details>


### 120. Design-to-Plan: A Large Language Model-Based Multi-Agent Framework for Manufacturing Process Planning from 3D CAD Models and 2D Engineering Drawings

- **Authors:** Muhammad Tayyab Khan, Lequn Chen, Wenhe Feng, Seung Ki Moon
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24039v1](http://arxiv.org/abs/2608.24039v1)
- **PDF:** [https://arxiv.org/pdf/2608.24039v1](https://arxiv.org/pdf/2608.24039v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Manufacturing process planning transforms heterogeneous design information into coherent manufacturing decisions. However, existing approaches focus on isolated subtasks, such as feature recognition, drawing interpretation, or tool selection, and struggle to support the full reasoning chain from design artifacts to process plans. This is critical when planning must interpret 3D CAD models, 2D engineering drawings, materials, and domain-specific rules. To address this gap, this paper presents Design-to-Plan, a large language model (LLM)-based multi-agent framework for end-to-end manufacturing process planning. An orchestrator coordinates specialized agents for 3D feature recognition, 2D drawing analysis, 2D-3D context fusion, knowledge retrieval, process sequencing, tool selection, and report generation. Rather than using LLMs as standalone text generators, the framework deploys them as reasoning agents that interact with deterministic modules and knowledge sources to produce consistent and traceable decisions. In this hybrid design, deterministic modules and specialized agents extract structured information from CAD and drawing inputs, while LLM agents perform context-aware reasoning, retrieve manufacturing rules, resolve conflicts, and generate planning outputs. The framework is evaluated using 300 benchmark cases across three downstream ReAct-enabled agents, plus separate evaluations of CAD feature recognition, drawing analysis, and 2D-3D context fusion. The parallel architecture achieves 100% success across downstream agents, Tool F1 scores of 95.9%-97.6%, 90% source detection accuracy in conflict analysis, and a 60%-68% reduction in token usage for key planning tasks. Results show that structured LLM-based multi-agent coordination can bridge design representations and manufacturing knowledge, enabling scalable, efficient, and traceable design-to-plan automation.

</details>


### 121. What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions

- **Authors:** Yichao Gao, Yumo Zhang, Yunhao Yao, Haohua Du, Puhan Luo, Ruiqi Li, Zhiqiang Wang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24022v1](http://arxiv.org/abs/2608.24022v1)
- **PDF:** [https://arxiv.org/pdf/2608.24022v1](https://arxiv.org/pdf/2608.24022v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents integrated with external resources gain complex task capabilities, yet the unified natural-language context channel makes them vulnerable to injection attacks: untrusted external data may be dynamically parsed as behavior-guiding instructions during LLM inference, thereby subverting the agent's decision. Existing defenses focus on static detection or isolation of malicious content at the input/output level, remains insufficient for detecting such dynamic inducements that arise during model reasoning. We propose Attnlocate, a runtime framework for fine-grained localization of context spans that genuinely influence tool-calling decisions, i.e., behavior-guiding instructions. Attnlocate casts this localization problem as an object detection task, aiming to detect the distinctive activation traces induced by behavior-guiding instructions within the attention matrix. Specifically, we design a multi-head, multi-layer attention aggregation scheme to construct a token-level feature space tailored for object detection. Then, a 1-D U-Net equipped with an anchor-free detection head is deployed to detect these spans. Finally, based on the authority of the provider from which the detected behavior-guiding spans originate, Attnlocate dynamically adjudicates malicious invocation attempts. We evaluate Attnlocate across ten agent configurations from five LLM families, covering scenarios involving indirect prompt injection and tool poisoning. Attnlocate achieves a mean IoU of 0.743, an average AUROC of 0.956, and a 0.934 true-positive rate at 0.067 false-positive rate. It also transfers effectively across unseen models and supports authority policy adaptation without retraining.

</details>


### 122. WebMCP-Phalanx: Enforcing and Characterizing Trust Boundaries for Browser-Integrated LLM Agents

- **Authors:** Lin-Fa Lee, YI-YU Chang, Kuo-Hui Yeh
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24017v1](http://arxiv.org/abs/2608.24017v1)
- **PDF:** [https://arxiv.org/pdf/2608.24017v1](https://arxiv.org/pdf/2608.24017v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The emerging W3C WebMCP proposal enables LLM agents to invoke tools exposed by web pages. In multi-party web environments, however, integrating agent execution into a browser security model centered on the Same-Origin Policy (SOP) leaves insufficient provenance and lifecycle guarantees for agent-accessible tools, creating three risks: subject-attribution spoofing, uncontrolled tool lifecycles, and semantic prompt injection. We propose WebMCP-Phalanx, a dual-layer agent runtime architecture. Its first layer provides a browser-native trust anchor that binds each tool to its registering principal through cryptographically protected capability credentials and propagates provenance labels throughout the tool lifecycle. Its second layer separates semantic inspection from privileged tool use. A Quarantine Agent (Q-LLM), without tool invocation authority, inspects tool metadata, outputs, and page-supplied content for prompt injection. Validated content is then forwarded to a Privileged Agent (P-LLM) for execution, while the Q-LLM's internal state remains hidden from page scripts. Empirical evaluation shows that the browser-native ownership mechanism reduces revocation and overwrite attack success from 100\% to 0\%. The dual-agent runtime blocks all 80 prompt-injection attempts embedded in tool descriptions and limits tool-return attacks to 2 successful cases out of 80. Across experiments, task utility remains statistically indistinguishable from the no-attack baseline. Under a white-box adaptive attacker, however, description-based filtering can be bypassed through malicious tool names invoked before inspection. This finding motivates a call-timing gate that delays tool invocation until all agent-visible tool metadata has been validated.

</details>


### 123. SAGE: From Direct Answering to Evidence-Grounded Inference for Chinese Ancient Document Understanding

- **Authors:** Yuchuan Wu, Xuan Luo, Yinglian Zhu, Meng Fang, Xiangyang Xue, Bin Li
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24011v1](http://arxiv.org/abs/2608.24011v1)
- **PDF:** [https://arxiv.org/pdf/2608.24011v1](https://arxiv.org/pdf/2608.24011v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chinese ancient document understanding demands complex visual, linguistic, and historical reasoning. Current Large Vision-Language Models (LVLMs) typically rely on an opaque, single-pass generation paradigm, often producing overconfident and weakly grounded responses. To address this, we propose SAGE, an evidence-grounded multi-agent framework that reformulates Chinese ancient document understanding as evidence-grounded inference rather than direct answer generation. SAGE coordinates specialized agents for task-aware planning, tool-mediated evidence acquisition, claim-level verification, and bounded replanning under a constrained shared-state runtime. This design supports bounded evidence seeking, answer revision, and abstention when grounding is insufficient. Experiments on the AncientDoc benchmark show that SAGE consistently outperforms matched direct-answering baselines across three LVLM backbones. Remarkably, SAGE with Qwen3.5-9B surpasses much larger monolithic LVLMs on most evaluated metrics, highlighting the importance of structured, evidence-grounded inference beyond model scaling.

</details>


### 124. AgentSpec: Speculative Decoding for Batch Inference of LLM Agents

- **Authors:** Xin Wang, Ziming Miao, Yi Zhu, Hui Shen, Zhongwei Wan, Fan Yang, Mi Zhang
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.24004v1](http://arxiv.org/abs/2608.24004v1)
- **PDF:** [https://arxiv.org/pdf/2608.24004v1](https://arxiv.org/pdf/2608.24004v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agent applications often incur high response time. Speculative decoding is a promising solution to improve the inference efficiency of LLM agents without impacting generation quality. However, state-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes, limiting their effectiveness to deploy in real-world agent applications. In this work, we first present a systematic analysis of speculative decoding for LLM agents and identify two dominant factors of speedup degradation: high rejection rate of speculative tokens, and under-utilization of dynamic token budgets.B ased on these observations, we propose AgentSpec, a speculative decoding algorithm that addresses the limitations of existing methods for LLM agents. AgentSpec incorporates structure-isolated drafting that constrains speculation to semantically coherent segments of the agent workflow, reducing the drafts of irrelevant semantic paths and achieving an extremely low rejection rate. Moreover, AgentSpec adopts redundancy-aware budget allocation that exploits agent-level information to better utilize the dynamically-free token budget during the agent inference. We implement and evaluate AgentSpec on five different workloads and four different models from four different LLM families in vLLM. Our results demonstrate the superiority of AgentSpec over state-of-the-arts.

</details>


### 125. The Empire, Long Divided, Must Unite: Architectural Convergence in Three LLM Agent Harnesses

- **Authors:** Dai Jiahong
- **Published:** 2026-08-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23953v1](http://arxiv.org/abs/2608.23953v1)
- **PDF:** [https://arxiv.org/pdf/2608.23953v1](https://arxiv.org/pdf/2608.23953v1)
- **Categories:** cs.SE, cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

An agent harness is what turns a language model into an autonomous agent: the surrounding code that builds the model's context, mediates its tools, runs the loop, and persists state across a long-horizon run. This layer, not the model it wraps, is increasingly the binding constraint on agent behaviour. We present a source-level, multi-case study of three open coding-agent harnesses built from deliberately opposing philosophies: LangChain's deepagents (batteries-included), Earendil's pi (radical minimalism), and DeepSeek's dsh (everything-is-a-plugin). Reading each at a pinned commit and following its commit history, we find that the two mature harnesses have travelled in opposite directions (deepagents subtracting authored scaffolding, pi accreting durable infrastructure), yet converged toward one architectural middle form of five recurring elements: a commoditised loop, an append-only replayable session record, model quirks kept as data, progressive disclosure of context, and explicit extension seams. A third harness, read afterward as a held-out check, exhibits all five, and in one seam reuses another's implementation outright. We therefore do not claim independent invention, and decompose the convergence into parallel discovery, diffusion, and literal reuse. Finally, one load-bearing dimension shows no convergence, and indeed no presence: external verifiability, a tamper-evident record an outside party can check without trusting the runtime. We read this absence not as an oversight but as a predictive gap, the next axis on which harnesses for provenance-sensitive domains will differ.

</details>


### 126. MARS: Multi-Specialist LLM Relay System for Competitive Programming

- **Authors:** Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23918v1](http://arxiv.org/abs/2608.23918v1)
- **PDF:** [https://arxiv.org/pdf/2608.23918v1](https://arxiv.org/pdf/2608.23918v1)
- **Categories:** cs.AI, cs.MA, cs.PL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models excel at code generation, yet competitive programming exposes a persistent failure mode: existing multi-agent pipelines distribute work over generic planner, coder, and debugger roles and delegate the choice of algorithmic technique to the backbone alone. We present MARS (Multi-Agent Relay of Specialized LLMs), a prompt-only framework in which each agent is a topic specialist---dynamic programming, graphs, strings, geometry, and so on---grounded by retrieval-augmented generation over an algorithm-theory corpus. Given a problem, retrieval selects a small team of relevant specialists; a starter writes an initial C++17 solution, and each subsequent turn runs the candidate against public examples in a sandbox, lets the active specialist keep, repair, or hand off the draft, and forwards a structured packet to the next specialist. A single infrastructure-fixer pass normalizes boilerplate at the end. On the CodeContests test split with Gemma 4, MARS reaches $0.624 \pm 0.006$ pass rate at $2.3$ recorded pipeline stages per task ($+14.4$ percentage points over direct prompting), closing most of the gap to CodeSIM ($0.731$) at $3.3{\times}$ lower wall-clock cost and substantially smaller variance in per-task token spend. The source code is available on GitHub: https://github.com/fckand/mars.

</details>


### 127. Retrieval-augmented generation vs. deterministic tax computation in multi-agent financial advisory: A 2x2 factorial experiment

- **Authors:** Aryan Brar, Justin Du, Avery Lor, Kylie Seto, Eric Taylor
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23908v1](http://arxiv.org/abs/2608.23908v1)
- **PDF:** [https://arxiv.org/pdf/2608.23908v1](https://arxiv.org/pdf/2608.23908v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tax-loss harvesting demonstrates consistent benefits to long-term portfolio growth; yet implementing it efficiently often involves complex considerations that are specific to the holdings within that portfolio and the individual who owns it. We introduce a custom capital gains calculation engine and a RAG-retrieved vector store of market advisory reports to provide context for a multi-agent trade recommendation system. We investigate the effects of each context provider on the quality of recommendations, measured by relative capital gains incurred during portfolio liquidation. A 2x2 repeated-measures ANOVA revealed a significant main effect of the tax optimization engine ($F(1,29) = 9.17$, $p = .005$, $η^2_p = .240$): enabling the engine reduced tax savings by approximately 55 percentage points relative to the no-engine conditions. The RAG main effect was not significant ($p = .841$), nor was the interaction ($p = .553$). The RAG-only condition achieved the highest descriptive mean tax savings (47.7%), and the baseline condition performed second-best (30.6%), suggesting that the pre-trained language model's internalized financial knowledge may be sufficient for competent tax-loss harvesting recommendations without explicit tooling. These results indicate that augmenting LLM agents with domain-specific computation engines does not guarantee improved performance and may introduce conflicting optimization signals.

</details>


### 128. Markets, Not Planners: Decentralized Orchestration of LLM Agents with Private Information

- **Authors:** Xiao Liu, Haoyang Li, Songwei Li, Hongbo Fang, Fengli Xu, Feng Shi, James Evans
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23867v1](http://arxiv.org/abs/2608.23867v1)
- **PDF:** [https://arxiv.org/pdf/2608.23867v1](https://arxiv.org/pdf/2608.23867v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents proliferate, built by different parties and with different capabilities and costs, orchestrating them is more like assembling labor across the economy than a computer calling a subroutine. Existing orchestration is typically centralized, with a single planner assigning every task, but this creates a bottleneck as agent pools grow, requires private information (e.g., agents' execution costs), and can easily be manipulated, such that a single inserted preference nearly doubles a favored agent's task share under a centralized LLM allocator. We introduce AgentLance, a repeated labor market in which agents bid on tasks using their private costs and self-maintained strategy notes, an allocator selects winners from bids and public reputation records, and a VCG-style payment rule rewards cost-aware bidding. Complex tasks are handled by hierarchical delegation: winning agents can decompose work and subcontract it through the same mechanism. Across mathematical reasoning, code generation, knowledge-intensive QA, and agentic tasks, AgentLance matches agents to their specializations, shifts work toward cheaper agents as cost sensitivity rises, and consistently outperforms single-model, centralized-orchestration, and market baselines. Diagnosing market failures, including inaccurate cost self-estimation and sub-optimal bidding, then correcting them in controlled experiments yields further gains, charting a path toward more efficient agent economies.

</details>


### 129. Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2)

- **Authors:** Avital Aviv, Parth A. Gandh, Ron Bitton, Asaf Shabtai
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23858v1](http://arxiv.org/abs/2608.23858v1)
- **PDF:** [https://arxiv.org/pdf/2608.23858v1](https://arxiv.org/pdf/2608.23858v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after signing. Agent interactions and external inputs that shape a transaction before authorization remain outside that protection, including Agent-to-Agent Protocol (A2A) messages and Model Context Protocol (MCP) tool calls. Prior work identified replay and prompt-injection attacks in AP2 v0.1. AP2 v0.2 addresses some of these issues but adds capabilities and deployment assumptions that require renewed analysis. We present a systematic security analysis of AP2 v0.2 based on its roles, transaction lifecycle, deployment architectures, and trust boundaries. We divide the lifecycle into five phases and identify five deployment architectures. Using MAESTRO (Multi-Agent Environment, Security, Threat, Risk, Outcome), we model four threat actors, eleven attack surfaces, eighteen adversary capabilities, and six attacker goals. The resulting catalog contains 48 threats spanning five attack families. We score these threats with the Artificial Intelligence Vulnerability Scoring System (AIVSS), identifying eight that reach the High band in at least one architecture. Because no complete public AP2 deployment was available, we build a testbed spanning all five architectures and develop five proof-of-concept demonstrations covering all eight High-risk threats and their mitigations. We also develop a deployment-aware scanner that maps applicable threats to static, cross-role consistency, and adversarial checks. Our analysis shows that valid mandate signatures alone do not ensure that an agent-mediated transaction reflects the user's intent when its pre-authorization context is manipulated.

</details>


### 130. Exploit More, Explore Smarter for Budget-Constrained Agentic Search

- **Authors:** Haoyang Fang, Bernie Wang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23848v1](http://arxiv.org/abs/2608.23848v1)
- **PDF:** [https://arxiv.org/pdf/2608.23848v1](https://arxiv.org/pdf/2608.23848v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Budget-constrained agentic search arises when an LLM agent must refine candidates under a small evaluation budget, because validation is expensive, generation requires multiple model calls, or both. In this regime, standard MCTS allocates budget poorly: exploration bonuses dominate at low visit counts, unpromising siblings are expanded before promising chains can deepen, and branching is independent of node quality. We introduce ExTS, a tree-search policy that treats expansion itself as a value-of-information decision. ExTS combines three mechanisms: discriminative reward shaping to separate candidates under narrow score distributions, a stochastic virtual child that estimates the value of creating a new branch from the parent's reward history, and quality-conditioned branching that expands only when a node's score justifies the budget cost. Across prompt optimization, code generation, molecular structure elucidation, and agentic workflow optimization, ExTS is competitive with or improves over task-specific tree-search baselines, with an average relative gain of +5.5% using a single fixed configuration. We further introduce pilot-run diagnostics that characterize what makes budget-constrained agentic search problems structurally different from one another, providing both understanding of the problem space and practical guidance for adaptation.

</details>


### 131. LUCAID: Agentic Multimodal AI for Lung Cancer Precision Pathology

- **Authors:** Marie-Lisa Eich, Kai Standvoss, Timo Milbich, Alexander Möllers, Miriam Hägele, Philipp Anders, Lars Tharun, Hanna Kontradiuk, Sebastian Kons, Nader Aldoj, Recepcan Adigüzel, Adam Narai, Lukas Hönig, Jonathan Striebel, Binru Yang, Mihnea P. Dragomir, Marvin Sextro, Philipp Keyl, Philipp Jurmeister, Rosemarie Krupar, Evelyn Ramberger, James Wells, Julika Ribbat-Idel, Andreas Kunft, Hussam Shuaib, Christian Grohé, Reinhard Büttner, David Horst, Klaus-Robert Müller, Lukas Ruff, Maximilian Alber, Frederick Klauschen, Simon Schallenberg
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23803v1](http://arxiv.org/abs/2608.23803v1)
- **PDF:** [https://arxiv.org/pdf/2608.23803v1](https://arxiv.org/pdf/2608.23803v1)
- **Categories:** cs.CV, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lung cancer tissue diagnostics is complex, as therapy decisions in precision oncology rely on the integration of histomorphological, immunohistochemical, and molecular features. Yet pathological assessment remains largely visual and semi-quantitative and shows interobserver variability, while existing artificial intelligence (AI) tools cover only selected tasks, rarely reach generalizable expert-level performance, and lack prospective clinical validation. To address these challenges, we developed and clinically validated LUCAID, an agentic AI system for precision lung cancer pathology. An integrative agent couples diagnostic reasoning with nine modules that cover the full routine workflow, from quality control, tumor detection and segmentation, histological subtyping, tumor microenvironment profiling, tumor cellularity quantification, and predictive biomarker scoring (PD-L1, MET, TROP-2) to automated structured report generation. LUCAID enables users to interactively query the module outputs and generate reports that contextualize the results. Against large-scale expert ground-truth annotations, the analysis modules achieved F1 scores of 0.82-0.95. In prospective clinical validation, LUCAID reached 93.0% concordance with an expert-panel adjudicated reference standard across clinically actionable decisions, compared with 68.3-81.1% for five experienced thoracic pathologists.

</details>


### 132. AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace

- **Authors:** Seonglae Cho, Donghyun Lee
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23740v1](http://arxiv.org/abs/2608.23740v1)
- **PDF:** [https://arxiv.org/pdf/2608.23740v1](https://arxiv.org/pdf/2608.23740v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool independent samples without coordination, and a single agent abandons up to half of hard tasks with a one-file stub-and-exit. AgentRoom is a realtime collaborative editing protocol for concurrent coding agents. Its runtime layer exposes file-level claim, status, and broadcast as MCP tools on a CRDT-merged shared filesystem. Five frontier coding-CLI models ran four backend coding tasks, with cross-language checks in Python DevBench and Rust+axum. For CLI-stable models, AgentRoom with 2 agents abandons fewer tasks than Solo and has less run-to-run variation. At matched-compute, one positive mean LLM-judge contrast puts AgentRoom over parallel-merge. The other contrast, a bundle probe, puts full AgentRoom above each partial case: an ordering rather than a percentage split. Coordination, not parallelism or CRDT-merge, bears the load.

</details>


### 133. Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment

- **Authors:** Stephen Chung, Wenyu Du, William J. Wesley
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23691v1](http://arxiv.org/abs/2608.23691v1)
- **PDF:** [https://arxiv.org/pdf/2608.23691v1](https://arxiv.org/pdf/2608.23691v1)
- **Categories:** cs.AI, cs.DM, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study autonomous mathematical discovery in the Station, an open-world multi-agent environment in which AI agents from different model families pursue a shared research goal without a central coordinator or scripted pipeline. Agents choose their own research directions, conduct experiments, collaborate, and build a shared scientific literature. Across 12 construction problems from the AlphaEvolve catalogue and two additional case studies, the Station obtained results novel relative to the prior literature on five problems: a new infinite family of finite-field Kakeya sets, new exact 604-point kissing configurations in dimension 11, new records for the discretized Kakeya needle and sign uncertainty problems, and a substantially improved lower bound for Erdős's minimum-overlap problem. Agents also discovered novel infinite families for Book Ramsey numbers. Importantly, the agents produced not only numerical constructions but also theorems and analyses explaining how those constructions work, making the results more interpretable and easier for mathematicians to build upon. We release all raw agent dialogues, proofs, and verification code, providing a transparent record of how these discoveries emerged.

</details>


### 134. Automata from Agent Traces: Failure and Next-Step Prediction

- **Authors:** Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed, Zekun Wu, Kleyton Da Costa, Ilham Wicaksono, Adriano Koshiyama
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23670v1](http://arxiv.org/abs/2608.23670v1)
- **PDF:** [https://arxiv.org/pdf/2608.23670v1](https://arxiv.org/pdf/2608.23670v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

</details>


### 135. The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams

- **Authors:** Summer Eunhyung Ann, Haokun Liu, Chenhao Tan
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23541v1](http://arxiv.org/abs/2608.23541v1)
- **PDF:** [https://arxiv.org/pdf/2608.23541v1](https://arxiv.org/pdf/2608.23541v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Does multi-agent LLM interaction help or hurt? Some work reports gains from debate (Du et al., 2024), critique loops (Chen et al., 2025), and mixture-of-agents synthesis (Wang et al., 2025), while other work finds that interaction adds cost without improving quality under equal budgets (Tran & Kiela, 2026; Xu et al., 2026; Jarrett et al., 2025), or that independent sampling already captures multi-agent gains (Li et al., 2024). We argue this contradiction partly reflects a missing distinction, because not all multi-agent communication is equal. Different model families find structurally different solutions, but when agents read each other's complete outputs, their proposals converge within one round, erasing the diversity that motivates using multiple models. We call this the interaction tax. We test 11 verifier-scored optimization tasks under matched budgets and find that full-solution interaction is a weak default. Independent proposal generation avoids this collapse. Full-solution interaction mainly makes agents stay close to the first solution they see instead of trying different approaches, and critique helps only if the violated rule is easy for the LLM to find and fix. These results suggest that multi-agent performance depends less on the number of agents than on the information they exchange, and interaction helps only when agents share the right information at the right time.

</details>


### 136. MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters

- **Authors:** ChengAo Shen, Wenchao Yu, Fangyu Wu, Dongjin Song, Hanghang Tong, Dongsheng Luo, Wei Cheng, Haifeng Chen, Jingchao Ni
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23473v1](http://arxiv.org/abs/2608.23473v1)
- **PDF:** [https://arxiv.org/pdf/2608.23473v1](https://arxiv.org/pdf/2608.23473v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecasters are more desirable. However, lightweight forecasters typically require substantial training data, limiting their use in domains with scarce, slowly accumulated, or privacy-sensitive time series. To address this dilemma, we investigate the challenging problem of few-shot learning for lightweight forecasters. We propose MetaCaster, a meta-harness-optimized multi-agent framework that uses agentic data generation to automatically train specialized lightweight forecasters from only a few examples and textual contexts. Our work highlights a new TSF paradigm in which agents act not as forecasters but as intermediary engineers that prepare efficient, task-specific forecasters for deployment. Experiments on 18 datasets, 23 state-of-the-art lightweight forecasters, and 14 baselines demonstrate that MetaCaster achieves both data efficiency and computational efficiency while maintaining high-quality TSF performance.

</details>


### 137. InjecMEM: Memory Injection Attack on LLM Agent Memory Systems

- **Authors:** Hanling Tian, Gengyu Zhang, Zeyang Sha, Jingying Wang, Yuhang Liu, Zhehao Huang, Kun Yang, Xiaolin Huang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23471v1](http://arxiv.org/abs/2608.23471v1)
- **PDF:** [https://arxiv.org/pdf/2608.23471v1](https://arxiv.org/pdf/2608.23471v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, we craft the injection with a retriever-agnostic anchor and an adversarial command. The anchor contains high-recall topical cues so that downstream retrieval consistently associates the record with the target topic. The command is a short sequence optimized to remain effective under uncertain fused contexts, variable placements, and long prompts so that it reliably steers outputs once retrieved. We learn the command via gradient-based coordinate search, averaging over synthetic prompt templates and insertion positions, and extend it to joint optimization across backbones to study transfer. Evaluated across multiple memory systems and backbone models, InjecMEM achieves reliable topic-conditioned retrieval and targeted generation, remains effective under memory drift, and leaves non-target queries unaffected. Our results underscore the need to harden memory systems and provide a reproducible framework for studying agent memory.

</details>


### 138. NetConfArena: An Executable Benchmark for LLM Agents in Closed-Loop Network Configuration

- **Authors:** Chang Liu, Xiaohui Xie, Xinyi Chen, Yong Cui
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23179v1](http://arxiv.org/abs/2608.23179v1)
- **PDF:** [https://arxiv.org/pdf/2608.23179v1](https://arxiv.org/pdf/2608.23179v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly attractive for automating network configuration, yet their reliability and failure patterns are poorly understood. An essential prerequisite is to assess such agents in a realistic but risk-free environment. Existing benchmarks, however, fall short: they often treat configuration as static command generation or rely on overly simplified settings. Such evaluations understate the core challenges of network configuration, where correctness requires reasoning about protocol complexity and topology dependence. We present NetConfArena, an executable benchmark for evaluating LLM agents in closed-loop network configuration. NetConfArena places agents in emulated multi-device networks, provides a standardized and compact action interface for task execution, and evaluates the resulting network behavior with hidden task-specific executable test cases. The benchmark relies on an LLM-assisted, emulation-grounded pipeline, which converts human-oriented network materials into reusable parameterized task templates. We evaluate representative LLM agents on 480 task instances instantiated from 96 protocol-focused task templates, yielding 3840 execution trajectories, and show that failures are not limited to command errors. The failures also reveal gaps in task-specification adherence and robust planning and execution. These findings suggest two future directions: using validated trajectories as supervision signals to improve foundation models, and designing harness mechanisms that make agent execution more reliable and accountable.

</details>


### 139. Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation

- **Authors:** Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23152v2](http://arxiv.org/abs/2608.23152v2)
- **PDF:** [https://arxiv.org/pdf/2608.23152v2](https://arxiv.org/pdf/2608.23152v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, stereotype, conspiracy, dehumanizing, non-factual), and then maps it to a targeted counterspeech style. To facilitate FIRE, we curate FactualCS, a novel dataset of $4,784$ instances that provides the annotations regarding hate categories, reasoning traces, and evidence mappings, which are critical elements for grounded generation that are missing in prior work. A comprehensive evaluation across $28$ baseline configurations demonstrates that FIRE significantly surpasses existing methods, despite using compact agents ($<$2B). FIRE achieves a $\sim$ $12 \%$ and $\sim$ $11 \%$ improvements in factual and category-specific accuracy respectively, while simultaneously reducing toxicity by $\sim$ $11 \%$ relative to the strongest baselines. Further human evaluation confirms that responses generated by FIRE are significantly preferred over the strongest baselines, underscoring its effectiveness for real-world deployment. These findings show that decomposing the underlying intent of hate speech is essential for generating safe, effective, and contextually precise counterspeech.

</details>


### 140. First Demonstration of Multi-Agent LLM System for Million-Scale Optical Link Management in Global Production AIDCs

- **Authors:** Jingyi Su, Yihao Zhang, Dianxuan Fu, Leiyan Fei, Juan Wang, Mengfan Dai, Qing Liu, Xiong Wu, Yufeng Jiang, Cheng Chen, Bowen Zhang, Peilong Wang, Xi Chen, Zonglong He, Hongchen Yu, Zhicheng Ye, Weisheng Hu, Qunbi Zhuge
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23145v1](http://arxiv.org/abs/2608.23145v1)
- **PDF:** [https://arxiv.org/pdf/2608.23145v1](https://arxiv.org/pdf/2608.23145v1)
- **Categories:** cs.MA, physics.optics


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present the first LLM-powered multi-agent system for autonomous fault management across millions of optical links in production AIDCs. Refined via SFT and continuous memory evolution, it achieves 97.7% F1 and over 60% fault-incident reduction, outperforming SOTA LLMs on a ten-week field data evaluation.

</details>


### 141. Beyond Executable Models: The Pufibara Agent Harness and the Modelica Agent Workflow Benchmark for Physical System Modeling

- **Authors:** Zizhe Wang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23653v1](http://arxiv.org/abs/2608.23653v1)
- **PDF:** [https://arxiv.org/pdf/2608.23653v1](https://arxiv.org/pdf/2608.23653v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly used for simulation-driven engineering. Physical system modeling presents different requirements from general-purpose code generation in software engineering, because correctness depends not only on syntax and executability but also on physical consistency and scenario-dependent behavior. We study this challenge in Modelica, an equation-based modeling language in which a model may compile and simulate while still violating its intended physics or engineering requirements. Across successive revisions, an agent may lose track of requirements or rely on simulation evidence produced by an outdated candidate.
  To address this challenge, we present Pufibara, an agent harness that maintains persistent engineering state across revisions, associates execution and simulation evidence with the candidate that produced it, and makes submission an explicit agent action. To evaluate end-to-end Modelica agent workflows, we also propose a source-grounded method for constructing realistic and independently evaluable tasks. We use this method to build the 232-task Modelica Agent Workflow Benchmark, spanning Model Repair, Model Generation, and Model Tuning. Each submitted candidate is scored by a benchmark-owned evaluator outside the agent loop.
  We compare Pufibara with Claude Code as complete harnesses under two matched large language model (LLM) backends. With DeepSeek v4 Flash, Pufibara passes 202 tasks, compared with 185 for Claude Code. With Claude Sonnet 5, Pufibara passes 202 tasks, compared with 187 for Claude Code. Under the repository-reported token accounting, Pufibara records 76.4%-82.5% lower logical-token totals. Its sequential runtime is 6.1%-58.4% lower. These findings show that, even under matched LLM backends, complete agent harnesses can differ substantially in both task success and resource use for physical system modeling.

</details>


### 142. Molecular LLM Agents: From Architectural Design to Scientific Autonomy

- **Authors:** Jiatong Li, Wengyu Zhang, Weida Wang, Yuxuan Ren, Wei Liu, Chenyang Mao, Yuqiang Li, Yatao Bian, Changmeng Zheng, Xiaoyong Wei, Qing Li
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23104v2](http://arxiv.org/abs/2608.23104v2)
- **PDF:** [https://arxiv.org/pdf/2608.23104v2](https://arxiv.org/pdf/2608.23104v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Molecular science represents an important frontier for LLM-based agents. Unlike general agents that mainly operate over natural language, code, or web environments, molecular LLM agents must perceive, reason about, and act upon chemical objects across symbolic strings, molecular graphs, 3D conformations, spectra, simulations, and wet-lab measurements. Their capabilities depend on chemically faithful molecular perception, an LLM-centered agent framework, domain-specific tool grounding, and computational or experimental feedback, in addition to planning and tool use. This work develops a conceptual framework for molecular LLM agents from two complementary perspectives. First, we introduce an architectural view of molecular-agent design, covering molecular representation and perception, the agent framework, domain-specific toolboxes, and learning and optimization. Second, we propose a scientific autonomy ladder inspired by staged autonomy in engineering systems, categorizing agents into four levels: L1 assistive or fixed workflows, L2 adaptive computational agents, L3 feedback-aware physical experiment agents, and L4 scientific-agenda agents. Together, these two perspectives establish a comprehensive framework for comparing existing molecular LLM agents, identifying missing capabilities and deployment risks, and guiding the design, evaluation, and deployment of future agents in molecular discovery workflows.

</details>


### 143. AgentWeave: Routing Before Reasoning for Efficient Function Calling in Tool-Rich Language Models

- **Authors:** Saurav Singla, Aarav Singla, Advik Gupta, Parnika Gupta
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23078v1](http://arxiv.org/abs/2608.23078v1)
- **PDF:** [https://arxiv.org/pdf/2608.23078v1](https://arxiv.org/pdf/2608.23078v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models increasingly operate over large collections of tools, functions, APIs, and specialized agents. As the candidate action space grows, a function-calling model must process more schemas, consume more prompt tokens, and distinguish among increasingly similar or irrelevant alternatives. We study a complementary systems strategy: reduce the candidate set before language-model inference while leaving the downstream model unchanged. We introduce AgentWeave, a deterministic pre-inference routing layer that constructs a bounded model-visible action space using eligibility, requirement, capability, and routing signals. We evaluate AgentWeave with a frozen BFCL-derived routing-pressure protocol using the public MadeAgents/Hammer2.1-1.5b model. On 48 fresh BFCL V4 multiple-function tasks, AgentWeave achieves 6/48 (12.5%) native BFCL successes, whereas all-tools, deterministic random top-8, and semantic top-8 baselines each achieve 0/48. The paired success difference is +12.5 percentage points with a 10,000-resample paired bootstrap 95% confidence interval of +4.17 to +22.92 points and exact McNemar p=0.03125. Relative to all-tools exposure, AgentWeave presents 70.18% fewer tools, uses 61.70% fewer input tokens, and exhibits 50.95% lower mean local-model latency. The result is deliberately narrow: this is a BFCL-derived routing-pressure study rather than an official full BFCL leaderboard score, and absolute task success remains low. The evidence nevertheless shows that candidate-space construction can materially affect a fixed model's function-calling behavior and motivates evaluating routing as a distinct stage before model reasoning.

</details>


### 144. From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation

- **Authors:** Xiangxin Zhang, Zhanwei Zhang, Zhihang Fu, Binbin Lin, Wenxiao Wang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23045v2](http://arxiv.org/abs/2608.23045v2)
- **PDF:** [https://arxiv.org/pdf/2608.23045v2](https://arxiv.org/pdf/2608.23045v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Web search agents powered by Large Language Models (LLMs) show strong promise, but deep research tasks expose a recurring failure mode: once an agent has produced a query, plan, or intermediate conclusion, it becomes less objective when later judging the consequences of that same action. We term this phenomenon inertia bias. To make it measurable, we introduce the IBIS benchmark, which controls the search observations while varying whether the model is evaluating the outcome of its own prior action. We find that models are substantially worse when they "own" the preceding search step, showing that self-authored action history can systematically distort subsequent judgment. We further show that this bias propagates into two forms of system-level degradation: search noise at the worker level and contextual noise at the manager level. To address this problem, we propose NIS-Agent, which applies context isolation at the two decision points most vulnerable to inertia bias: webpage triage and final-answer validation. Across GAIA, WebWalkerQA, BrowseComp, and BrowseComp-zh, NIS-Agent achieves competitive performance while reducing token cost by 33% compared to our baseline. We further train an 8B model to be intrinsically more resistant to inertia bias; under the same NIS-Agent framework, it attains average performance comparable to GPT-4o on deep research benchmarks. Our code is publicly available at https://github.com/PangSMPang/NIS-Agent.

</details>


### 145. AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces

- **Authors:** Sungho Park, Wonjoong Kim, Rongyuan Tan, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23041v1](http://arxiv.org/abs/2608.23041v1)
- **PDF:** [https://arxiv.org/pdf/2608.23041v1](https://arxiv.org/pdf/2608.23041v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning problem and iteratively updates the harness using failure signals from mini-batches. AutoSaddler combines failure-trace diagnosis, structured patch generation that treats the harness as code, and validation-based update selection. Experiments on GAIA2, SWE-Bench Pro, and Terminal-Bench 2.0 show that AutoSaddler substantially improves agent performance over the corresponding base harnesses, achieving gains of 9.0, 9.6, and 10.0 percentage points, respectively. Ablation studies further suggest that effective harness optimization benefits from three ingredients: deep debugging rather than shallow reflection, targeted modifications rather than unconstrained editing, and generalization-aware selection rather than trajectory-specific repair. Together, these results suggest that automatic harness optimization is a promising path toward more performant and reliable agent systems.

</details>


### 146. MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks

- **Authors:** Yi Zhu, Xiongwei Wu, Qiyi Wang, Tingyu Qu, Jiajun Liu, Sihan Cao, Long Chen, Weigao Sun, Feida Zhu, Yiran Zhong, Steven Hoi
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23035v2](http://arxiv.org/abs/2608.23035v2)
- **PDF:** [https://arxiv.org/pdf/2608.23035v2](https://arxiv.org/pdf/2608.23035v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints. To close this gap, we present \textbf{MobilePA-Bench}, an interactive, stateful, and tool-centric benchmark for evaluating the tool-calling and planning abilities of mobile planning agents. MobilePA-Bench runs on an executable sandbox that maintains live application databases and returns structured feedback, spanning $13$ functional domains and $212$ realistic mobile tools. Beyond basic tool use, it evaluates a central planning agent along three advanced dimensions: \emph{(1)~Sub-agent Collaboration}---decomposing a complex task and delegating specialized work to capable sub-agents; \emph{(2)~Memory Usage}---recalling stored memories, user profiles, and past preferences to resolve implicit requests; and \emph{(3)~Skill Usage}---invoking pre-packaged composite skills instead of planning every step from scratch. Extensive experiments show that current frontier LLMs remain unreliable in mobile settings: performance drops sharply under strict tool ordering, permission limits, and unexpected runtime errors. By pairing an interactive function-calling sandbox with evidence-based verification, MobilePA-Bench serves as both a practical diagnostic benchmark and an interactive foundation for agentic reinforcement learning---accelerating the development of dependable mobile agents.

</details>


### 147. Meta-Moderator: Empowering Multi-Agent Debate with Meta-Cognition

- **Authors:** Wentao Hu, Zhuoyue Wan, Jinhao Shen, Chen Jason Zhang, Xiaoyong Wei, Qing Li
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23029v1](http://arxiv.org/abs/2608.23029v1)
- **PDF:** [https://arxiv.org/pdf/2608.23029v1](https://arxiv.org/pdf/2608.23029v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent debate can improve large language model reasoning by eliciting diverse hypotheses and critiques, yet its performance is often constrained by weak moderation. Common pipelines rely on fixed budgets, agreement-based stopping, or untrained judges, leading to redundant deliberation and unreliable evidence aggregation. We cast moderation as a meta-cognitive process, monitoring debate utility, controlling deliberation, and adjudicating a final answer, and introduce Meta-Moderator, a learnable framework that dynamically regulates debate and decides when to finalize an answer. Meta-Moderator is trained independently of the debaters via outcome-driven policy optimization, making debate regulation an explicit capability rather than an incidental effect of prompting. Across five benchmarks, Meta-Moderator outperforms widely used decision layers and transfers across tasks and system configurations. Further analyses show that it allocates debate more selectively and reduces mis-aggregation after informative hypotheses appear.

</details>


### 148. Beyond Surface Cues: Disentangling Sociocultural Signals in Multilingual LLMs

- **Authors:** Yuanjun Feng, Tanzhou Liu, Stefan Feuerriegel, Yash Raj Shrestha
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23026v1](http://arxiv.org/abs/2608.23026v1)
- **PDF:** [https://arxiv.org/pdf/2608.23026v1](https://arxiv.org/pdf/2608.23026v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multilingual LLM outputs can vary across sociocultural contexts. However, evidence of cultural grounding can be misleading: identity labels may be inferred from explicit or indirect textual cues, while names and wording can reveal the source language. Treating all these signals as evidence of cultural grounding may obscure potential biases. We present a human-validated, multi-agent audit that separates three questions: whether outputs reproduce social biases, whether identity groups are represented differently, and whether outputs reflect cross-cultural patterns. The study analyzes 89,253 outputs from 12 LLMs in English, French, and Chinese, spanning 18 occupations and three task conditions.
  We find that bias representation varies systematically across languages and tasks. Removing direct identity cues sharply reduces identity-label prediction in English and Chinese, but has a much smaller effect in French. Across all language-genre settings, the cultural context associated with the source language receives the highest average relevance score, with moderate agreement between automated and human ratings. However, the ability to identify the source language drops substantially after translation and again after masking names. Without these controls, multilingual audits may mistake surface cues for cultural understanding, leading to misleading conclusions about cross-cultural variation and bias. Our audit offers a practical framework for separating such shortcuts from more meaningful cross-cultural patterns.

</details>


### 149. Toward Effective and Reliable LLM Agents via Dynamic Ontology

- **Authors:** Xiaohui Zhang, Zequn Sun, Chengyuan Yang, Yuanning Cui, Lingbing Guo, Wei Hu
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22974v1](http://arxiv.org/abs/2608.22974v1)
- **PDF:** [https://arxiv.org/pdf/2608.22974v1](https://arxiv.org/pdf/2608.22974v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents rely heavily on knowledge encoded in model parameters or presented as unstructured context. In domain-specific tasks, this leaves important semantic connections implicit. This often results in incomplete evidence use and brittle multi-step decisions. Ontologies offer a way to externalize domain concepts and relations as machine-interpretable structures, but constructing task-usable ontologies traditionally requires substantial effort from domain experts and is difficult to scale. Automatic construction is also challenging: an ontology that appears semantically plausible may not contain the relational structures needed for actual decision making. We present OaK, an ontology-as-a-kernel framework that dynamically constructs and refines task-oriented ontologies for LLM agents. Given task requirements and training data, OaK constructs an ontology and its knowledge graph, generates task-adaptation functions for graph reasoning, and uses judge feedback to iteratively refine both. By making relevant concepts and relations explicit, the ontology grounds knowledge retrieval and multi-step decision making. We evaluate OaK on TravelPlanner, CRMArenaPro, and ToolQA. Results show that OaK improves standard LLM agents, strengthens evidence grounding, and boosts the reliability of multi-step reasoning.

</details>


### 150. Buried in Textual Debt: Context Pruning with Visual Evidence Preservation for MLLM Agents

- **Authors:** Yuchen Huang, Sijia Li, Jun Zhang, Yi R. Fung
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22963v2](http://arxiv.org/abs/2608.22963v2)
- **PDF:** [https://arxiv.org/pdf/2608.22963v2](https://arxiv.org/pdf/2608.22963v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed as multi-step agents, where explicit reasoning supports task decomposition and tool coordination but also accumulates self-generated text. Over long trajectories, this text can dominate the context and suppress visual evidence, creating textual debt. We observe that reasoning becomes redundant once task-relevant visual evidence is grounded, while stale hypotheses can misguide later inference when grounding remains uncertain. Pruning must therefore remove redundant text without discarding visual evidence. We propose SPARE, a Kullback-Leibler (KL)-guided framework for pruning accumulated reasoning in multimodal tool-use agents. SPARE uses a compact task-state summary as privileged diagnostic context. For each candidate segment, it replays the same model under the original and summary-conditioned contexts. Reverse-KL divergence from on-policy self-distillation (OPSD) then tests whether the summary sufficiently covers the segment without disrupting future reasoning. We further fine-tune the summarizer with supervised fine-tuning (SFT), enabling more compact summaries, broader coverage, and more aggressive pruning. Across multi-step visual tool-use benchmarks, SPARE achieves the highest average accuracy among pruning methods while removing 37.89-64.58\% of reasoning tokens. This favorable accuracy-context trade-off shows that reducing textual dominance restores reliance on visual evidence and mitigates over-conditioning on self-generated language.

</details>


### 151. Concepts for Securing Agentic AI Coding and the Terok Environment

- **Authors:** Jiří Vyskočil, Franz Pöschel, Andreas Knüpfer
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22930v1](http://arxiv.org/abs/2608.22930v1)
- **PDF:** [https://arxiv.org/pdf/2608.22930v1](https://arxiv.org/pdf/2608.22930v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI is a fascinating new tool for software development. It is a huge step forward compared to "conventional" AI assisted coding, which in turn was a considerable breakthrough earlier. AI support through LLMs is a young and very fast-moving field. The "conventional" (non-agentic) flavor became useful and productive in early 2025 (around 18 months ago) and the agentic flavor followed in fall 2025 (approximately 9 months ago). Besides all its benefits and potential, it also carries some fundamental risks for IT security. And the agentic approach added very severe risks while making others much more dangerous.
  With all the motivation to explore this fascinating new tool we should not ignore the risks but actively address them. We present (I) an assessment of the IT security risks, (II) a concept for mitigating them without breaking its benefits, and (III) an overview about an implementation of our concept. In this very dynamic field this is likely not the final and once-and-for-all answer to the identified issues but still a substantial step forward in responsible usage of Agentic AI for software development. It should also be a contribution to the community to allow early and eager evaluation of the potential of agentic AI for software development without actually suffering from its implied IT security risks.

</details>


### 152. Minimal Local Simulation Foundations for LLM- and VLM-Driven Agents in 2D and 3D Environments

- **Authors:** Ryuki Hyodo
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22833v1](http://arxiv.org/abs/2608.22833v1)
- **PDF:** [https://arxiv.org/pdf/2608.22833v1](https://arxiv.org/pdf/2608.22833v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) and vision-language models (VLMs) are expanding the range of behaviors that can be represented in agent-based simulations, but many contemporary platforms are difficult to study, modify, or run on ordinary computers. We present two intentionally minimal simulation foundations for education and rapid prototyping. SD-AgentFoundry-2D provides a two-dimensional multi-agent environment in which locally hosted LLM agents move, communicate, respond to place occupancy, and encounter spatially localized fire events. SD-AgentFoundry-3D provides a three-dimensional digital-twin environment in which a locally hosted VLM receives first-person images and produces natural-language movement instructions. Both codebases are designed to run locally on macOS, Windows, and Linux and are deliberately left open to modification rather than developed as finished applications. Together, they offer accessible starting points for learning about generative social simulation and for building domain-specific extensions.

</details>


### 153. TRACE: A Self-Evolving Skill Bank for Consistent, Limit-Aware LLM Agents

- **Authors:** Wenhao Wu, Menghao Zhang, Xin Wang, Zhi Wang, Kun Shao, Jian Luan
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22793v1](http://arxiv.org/abs/2608.22793v1)
- **PDF:** [https://arxiv.org/pdf/2608.22793v1](https://arxiv.org/pdf/2608.22793v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reliable deployment of LLM agents in user-facing products depends not on raw task-solving ability but on consistency and limit-awareness: behaving the same way across repeated trials, and recognizing when a request cannot, or cannot yet, be safely fulfilled. CAR-bench exposes this reliability gap in the domain of in-car assistants: an LLM-simulated user issues incomplete or ambiguous requests, requiring the agent to resolve uncertainty through multi-turn dialogue and tool use while strictly adhering to domain policies. Even frontier models show a substantial gap between what they can solve at least once (Pass@3) and what they solve consistently across trials (Pass^k). We bridge this gap with TRACE (TRAjectory-Contrastive Evolution), which iteratively improves a skill-based agent's behavioral knowledge without modifying model weights. This knowledge is organized as a Skill Bank of modular, retrievable skills, each encoding a self-contained set of tool-use rules and behavioral guidelines. TRACE evolves this bank through an agentic self-evolution loop: after each evaluation round, it groups trajectories by the skills invoked and refines each skill by contrasting successful and failed behaviors. The updated bank then guides subsequent rounds, while during deployment the Actor performs state-conditioned skill orchestration at every turn. On GPT-5.5, TRACE improves consistency (Pass^3) by 34.6 points, from 59.9% to 94.5%, while shrinking the gap between potential and reliable performance to just 4.0 points. On the official hidden set, TRACE achieved first place using GPT-5.6-Sol, attaining a Pass^3 score of 70%-a 40% relative improvement over the baseline. These results show that TRACE converts high model potential into stable, consistent performance gain. Project homepage: https://darwin-agent.github.io/Car-bench-TRACE.

</details>


### 154. The Compaction Cliff in Long-Running AI Agent Memory

- **Authors:** Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22752v1](http://arxiv.org/abs/2608.22752v1)
- **PDF:** [https://arxiv.org/pdf/2608.22752v1](https://arxiv.org/pdf/2608.22752v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

A safety rule and an episodic log compete for the same tokens in an AI agent's context. When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable. On 20 production agent configurations, Claude Code's /compact prompt on Sonnet 4.6 preserves 53\% of safety rules after one compaction round and 10\% after five. We name this the Compaction Cliff. We address it with Knowledge Triage, a framework that classifies each line of an agent's knowledge base by type and routes each type through its own retention policy. Three deterministic operators implement this triage across the three context-management operations: TypeCompact rewrites items in place under per-type fidelity, TypeDecompose partitions a topic too large to compact safely, replicating in-scope safety rules across partitions, and TypeRetrieve fetches items from external storage with in-scope rules pinned ahead of relevance. On five public corpora, TypeCompact preserves 2--4$\times$ more safety rules than the strongest single-shot LLM compactor at every ratio, with 96\% recall over five rounds. TypeDecompose reaches 0\% locality violations against 93\% under uniform partitioning. TypeRetrieve reaches 100\% recall@50 against 73\% for the best single-shot LLM retriever. On three downstream behavioral benchmarks, we outperform the production Sonnet compactor on medical compliance (paired McNemar $p < 10^{-8}$ on preservation, $N = 200$), the full-policy and hierarchical baselines on retail task pass rate ($p < 0.01$, $N = 115$), and the hierarchical compaction on the airline domain ($p = 0.024$). We release AgentArtifactCorpus (396{,}934 agent configurations from 54{,}628 public GitHub repositories), the classifier, and the reference implementation.

</details>


### 155. AI Agents Push Humans Out of the Loop

- **Authors:** Margaret Mitchell, Avijit Ghosh, Samir Passi
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.23642v1](http://arxiv.org/abs/2608.23642v1)
- **PDF:** [https://arxiv.org/pdf/2608.23642v1](https://arxiv.org/pdf/2608.23642v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents pose significant risks as they are granted increasing autonomy. A commonly proposed solution is human oversight and keeping a ''human in the loop'', but this is not a simple solution: Not only do current approaches to AI agent design impede effective human oversight, but the cognitive capacities required for it are also themselves degraded by extended use of AI systems. This position paper argues that current approaches to the development and deployment of AI agent systems do not support effective human oversight -- they contribute to its degradation. To address this, a top priority in the advancement of AI agents should be supporting the situated goals and cognitive requirements of effective human oversight, treating the human needs of overseers at the same level of importance as AI agent capability. To put this idea into practice, we connect work on automation and human-computer interaction to AI agent processes, outlining design-level affordances and organizational protocols that (1) support overseers in exercising critical judgement and (2) counteract the skill atrophy that arises from extended use of automation. We urge developers and deployers to adopt these or similar approaches. Without explicit support for the cognitive demands of effective human-agent interaction, AI agent systems will continue to passively incentivize the degradation of the very human skills they rely on.

</details>


### 156. SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale

- **Authors:** Jiaqi Liu, Maolin Ran, Xiaoyang Lu, Jian Wang, Weiwen Liu, Jianghao Lin, Yong Yu, Weinan Zhang
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22725v1](http://arxiv.org/abs/2608.22725v1)
- **PDF:** [https://arxiv.org/pdf/2608.22725v1](https://arxiv.org/pdf/2608.22725v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory graph that repairs continuity entirely at the prompt-text layer by extracting a multi-dimensional state for every shot, retrieving only causally prior context over the resulting graph, filtering it selectively, and injecting the surviving constraints by natural-language prompt rewriting. We further release SEAM-Bench, a double-blind continuity storyboarding benchmark, on which SEAM raises cross-episode continuity recall from 0.700 to 0.946, generalizes across six mainstream text models, and yields consistent, though not yet significant, gains at the generated-image layer. Deployed as a mandatory stage in CreativeFitting's SEAM-Agent production pipeline over 201 shots, SEAM reaches a 96.5% director-acceptance rate with zero unsafe injections; a conservative counterfactual attributes at least 21.9 percentage points of that rate to its cross-episode memory.

</details>


### 157. Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf

- **Authors:** Davood Wadi, Yu Ma
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22697v2](http://arxiv.org/abs/2608.22697v2)
- **PDF:** [https://arxiv.org/pdf/2608.22697v2](https://arxiv.org/pdf/2608.22697v2)
- **Categories:** cs.AI, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are examined and bought more often. Consumers are now delegating search to AI agents that can ingest an entire results page at once. Randomizing the order of one hundred hotel listings across 5,000 AI agent sessions, we compare four large language models against human field data. AI agents search more deeply than humans and never decline to buy. Position still predicts which listings are inspected, but weakly and non-monotonically: the middle of a results page has the lowest probability of inspection, not the bottom. Position reaches the choice stage for some models and not others, a heterogeneity that tracks neither provider nor capability. All models nonetheless converge on the same undominated listing. For agentic search, the attributes displayed on a results page matter more than placement within it.

</details>


### 158. Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing

- **Authors:** Nazib Sorathiya, Daniel Zhang, Bardiya Akhbari
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22695v1](http://arxiv.org/abs/2608.22695v1)
- **PDF:** [https://arxiv.org/pdf/2608.22695v1](https://arxiv.org/pdf/2608.22695v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable profiles, and an online retrieve-then-rank pipeline that returns a ranked shortlist without invoking any candidates online. We show that from N=10 to 7,278 capabilities, in-context routing's top-1 accuracy (Match@1) collapses (0.85 to 0.12), while retrieve-then-rank degrades more gently (0.81 to 0.39) because its reranker still ranks the right capability first 0.70-0.87 of the time once retrieval finds it. In the Nova Micro sweep, the crossover is around N=500. We compare against two in-context baselines. Full-Ctx puts the whole registry in the prompt and asks the LLM to pick. Search&Pick gives the LLM a search tool to narrow candidates before it picks. At full scale the pipeline leads Search&Pick by 6.5 percentage points (pp) on Match@1 at about half the cost. It reduces cost 70x versus Full-Ctx. We use a fixed configuration (same enrichment, retriever, and scorer weights) across agent, tool, and skill registries. The pipeline runs in production as the default capability-discovery layer of a large-scale multi-agent platform.

</details>


### 159. Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses

- **Authors:** Jiachen Xu, Torben Bach Pedersen, Zhongming Yao, Xiaoyu Zhang, Yushuai Li
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22676v1](http://arxiv.org/abs/2608.22676v1)
- **PDF:** [https://arxiv.org/pdf/2608.22676v1](https://arxiv.org/pdf/2608.22676v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Robustness to a bad tool return means answering it in the way that return calls for, which depends on how the tool went wrong. A tool that has failed and a tool that returns a well-formed falsehood are different problems with different remedies. We ask whether the two already differ at the moment the return arrives. This is a qualitative pilot study: we score single decision points rather than running agents to completion. We inject controlled faults into a retail customer-service domain and read two channels off the model's log-probabilities: the likelihood of the returned content under the tool schema alone and under the whole trajectory, and its distribution over the legal actions, read for both shape and where the mass sits. An incomplete return is legible in every case, being improbable under the schema alone in a range no other condition enters, and it moves the mass toward the tools that re-read state wherever there is room to move. An inconsistent return leaves the schema channel untouched and registers in the likelihood comparison on the field whose true value the context already carries verbatim, not on the one whose contradiction runs through the domain policy. The action distribution gives each condition a distinct signature, but orders them by how far the return bears on the next action rather than by fault family. Recognition is therefore asymmetric: each condition is legible in some channel, and no channel is legible on all of them.

</details>


### 160. A-CPES: A Reference Framework for Agentic AI in Cyber-Physical Energy Systems

- **Authors:** Xiaoyu Zhang, Qiuye Sun, Jiachen Xu, Zhongming Yao, Yushuai Li
- **Published:** 2026-08-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2608.22672v1](http://arxiv.org/abs/2608.22672v1)
- **PDF:** [https://arxiv.org/pdf/2608.22672v1](https://arxiv.org/pdf/2608.22672v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Energy system operation contains a loop of work that automation has never taken over: posing the optimization problem the current cycle should solve, disposing of infeasibility, sequencing a solution into interlocked switching orders, assembling evidence no single model holds, negotiating adjustable capacity with many parties, and settling experience into practice. Licensed dispatchers carry all of it in person, and the rising share of variable renewable generation is making that loop turn faster than their number can grow. Agentic AI supplies the abilities it requires, but enters as the outer loop of control: it calls SCED and the other decision models rather than being called by them. We propose A-CPES, three nested rings, an authorization and accountability frame around an agentic control outer loop around a six-layer CPES core. We argue the loop is indivisible, tune where and how tightly it may close, state eight structural failure modes as falsifiable predictions, and specify six governance modules that rebuild the authorization frame until it covers the loop, before the loop starts turning.

</details>



## Biorxiv (3 papers)


### 1. Self-organized Regulation of Group Size and Number in Natural and Artificial Collectives

- **Authors:** Zhang, T., Lee, S., Hamann, H.
- **Published:** 2026-08-28
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.25.746978](https://doi.org/10.64898/2026.08.25.746978)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

From animal societies to self-organizing multi-agent systems, collectives adapt their group structure to tasks and environments. However, how they determine appropriate group sizes and the number of subgroups to form remains unclear. We formulate the Group Size and Number Regulation Problem (GSNRP), which asks how individuals regulate group sizes and numbers using only local information. In a first step, we establish a graph-theoretic model demonstrating that simple following behavior suffices to form group structures that match theoretical expectations, but is insufficient for active regulation of group size and number. In a second step, we operationalize individual group-size preferences in a decentralized fission-fusion mechanism based on perceived group size. Through multi-agent simulations, we validate that this mechanism achieves stable convergence across three signaling regimes, from position-only sensing to continuous group-size communication. Using tracking data from wild white-nosed coatis (mammals in the raccoon family), we calibrate individual group-size preferences and show that the controller recovers selected group-size, subgroup-count, and transition statistics. This in-sample case study demonstrates descriptive consistency with natural fission-fusion dynamics without establishing the underlying behavioral mechanism. These results suggest that natural and engineered collectives may share local principles of perception, preference, and response for regulating group structure.

</details>


### 2. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-08-26
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

</details>


### 3. ASAREE: An Analytical Sandbox for Agentic AI Research, Engineering, and Experimentation

- **Authors:** Moran, J., Freda, P. J., Ghosh, A., Hernandez, M. E., Moore, J. H.
- **Published:** 2026-08-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.20.746074](https://doi.org/10.64898/2026.08.20.746074)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Summary: Agentic AI platforms enable the engineering of autonomous workflows but are not designed for experimentation and hypothesis testing. ASAREE (Analytical Sandbox for Agentic AI Research, Engineering, and Experimentation), is an open-source platform to address this gap. ASAREE creates agents, connects to MCP servers and tools, and designs factorial experiments through a visual interface or Python SDK. It records a full provenance trace for every run and routes all model calls through a provider-agnostic bridge that supports local deployments, ensuring data privacy. As a use-case, we use ASAREE to evaluate key design choices in a mutli-agent machine learning pipeline. Across a 2 x 2 x 2 factorial design, more advanced models, greater reasoning effort, and critic agent use significantly increased compute time, token use, cost, and feature count without improving predictive performance. The lowest-cost baseline, Claude Sonnet 5 with medium effort and no critic, achieved the highest mean PR AUC while Claude Opus 5 with extra high effort and a critic agent cost 15.5x more (USD) and ran 13.1x longer while performing worse on average. These findings highlight ASAREE as a robust framework for evaluating agentic system performance and resource efficiency.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*