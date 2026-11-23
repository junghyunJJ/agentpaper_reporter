# Weekly AI Agent Paper Report

**Generated:** 2026-11-23 21:13
**Period:** 2026-11-16 to 2026-11-22

## Summary

- **Total papers fetched:** 838
- **Papers matching keywords:** 176
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-11-16) | Change |
|--------|-----------|-----------|--------|
| Total matched | 176 | 167 | +9 |
| arxiv | 170 | 163 | +7 |
| biorxiv | 4 | 3 | +1 |
| medrxiv | 2 | 1 | +1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (6 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. Unveiling value functions in social cognition with multi-agent inverse reinforcement learning

- **Authors:** Chen, Y., Cheng, Y., Kwak, M., Radulescu, A., Wu, H. Z.
- **Published:** 2026-11-18
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2024.10.09.617461](https://doi.org/10.1101/2024.10.09.617461)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social behavior requires individuals to consider not only their own goals but also those of others. Latent reward functions that encode such goals can be recovered from behavior using inverse reinforcement learning in single-agent settings. However, extending this to multi-agent interactions is challenging, as joint reward functions are defined over joint state spaces that grow exponentially with the number of agents. Existing approaches address this complexity by imposing restrictive assumptions on social interactions, limiting generality and interpretability. Here we show that joint reward functions governing social interactions can be efficiently represented through decomposition into individual reward maps for each agent and low-dimensional interaction terms. Building on this formulation, we introduce a general multi-agent inverse reinforcement learning framework (MAIRL) that enables scalable and interpretable inference of latent reward representations directly from behavior. In simulated social tasks with known ground-truth rewards, MAIRL recovered the rewarded states and imitated expert behavior as accurately as or better than existing multi-agent inverse reinforcement learning methods. Applying MAIRL to mouse and primate social tasks, we recover structured reward maps that reflect distinct social roles and interaction strategies during group behavior. These results establish MAIRL as a general framework for identifying latent objectives underlying multi-agent behavior across species and paradigms.

</details>


### 2. SPIDER: Contextualizing Biomedical Knowledge for Evidence-Grounded Scientific Reasoning

- **Authors:** Liu, M., Zhao, W., Chen, J., Quan, X., Wang, X., Feng, J., Zhou, X., Han, J., Zhang, Y., Wang, Y., Zhang, X., Xie, W.
- **Published:** 2026-11-18
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.11.765839](https://doi.org/10.64898/2026.11.11.765839)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Aggregated relations in biomedical knowledge graphs can obscure evidence and study conditions, complicating the distinction between scientific disagreement and contextual differences. Here we introduce SPIDER, a multi-agent framework grounding biomedical relations in literature evidence and extracting study conditions for interpretation. Applied to a graph integrating 48 databases and ontologies, SPIDER analyzed 1.95 million PubMed abstracts, adding 2.31 million previously unrepresented, literature-supported entity pairs to construct SPIDER-KG. Daily updates incorporate relations and evidence from newly indexed PubMed records. Across 89,937 evidence-supported comparisons of potentially incompatible relations, SPIDER classified 79.0% as contextual differences, and 6.1% as genuine disagreement, achieving 80.3% macro-F1 averaged across both categories against expert annotations. On SPIDER-Bench and four biomedical reasoning benchmarks, SPIDER-KG improved large language models' interpretation of evidence-supported biomedical relationships. Retrospective analysis of newly reported gene--disease relationships further demonstrated how evidence-linked knowledge can contextualize emerging discoveries. SPIDER-KG provides a reusable, incrementally extensible evidence layer for biomedical reasoning.

</details>


### 3. Pharmacolibrary: Interoperable executable models for PK, PD and PGx derived from published evidence

- **Authors:** Kulhanek, T., Denil, S., Izmirli, B., Ertaylan, G.
- **Published:** 2026-11-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.16.766960](https://doi.org/10.64898/2026.11.16.766960)

- **Categories:** pharmacology and toxicology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Published pharmacological knowledge is distributed across heterogeneous scientific literature, databases, and computational models, making systematic reuse, comparison, and reproducibility difficult. We present Pharmacolibrary v26.11, a source-traceable resource that connects pharmacokinetic (PK), pharmacodynamic (PD), and pharmacogenomic (PGx) knowledge with executable models, simulations, and interactive visualizations. A multi-agent workflow combines LLM-assisted literature retrieval and extraction with deterministic validation, ontology mapping, provenance tracking, automated model generation, and rule-based review. The system transforms published evidence and extracted parameters into executable models across Modelica, FMI, SBML, MATLAB, and CellML and provides browser-based simulations for research and education. Preliminary evaluation indicates that decomposing literature extraction into multiple stages improves parameter recovery compared with single-pass extraction and that locally deployed open-weight models can provide performance that is at least comparable with frontier commercial LLMs. Pharmacolibrary provides a foundation for scalable, auditable curation of pharmacological knowledge and for connecting published evidence to reusable computational models across research, simulation, and education.

</details>


### 4. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Orlenko, A., Venkatesan, M., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-11-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

</details>


### 5. Human-Agentic AI Collaboration Workflow for Trend Analysis of ChatGPT Applications in Healthcare

- **Authors:** Chou, P. J., Lin, Y. H., Li, E. Y.
- **Published:** 2026-11-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.11.14.26368120](https://doi.org/10.64898/2026.11.14.26368120)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundWith the rapid advancement of artificial intelligence (AI), large language models (LLMs) such as ChatGPT have demonstrated strong potential to transform healthcare research and practice. However, LLMs are probabilistic and generate inherently variable outputs, which create risk and uncertainty in healthcare applications. Therefore, analyzing the current research landscape of ChatGPT applications is imperative to understand applied techniques and related concerns and to facilitate their practical integration into healthcare information systems.

ObjectiveLeveraging LLM-based agentic AI with domain experts to analyze trends in ChatGPT healthcare applications and to examine the collaborative and interpretative capacities of LLM agents in broader contexts beyond narrowly defined topics.

MethodsThe review used a systematic search of the PubMed and Web of Science databases, following PRISMA-ScR guidelines, and focused on ChatGPT applications, associated concerns, applied techniques, and usage factors. To support the review process, an adaptive, iterative LLM-based agentic AI with a human-in-the-loop mechanism was employed for automated metadata extraction, identification, classification, and knowledge synthesis. The extracted information was subsequently used for temporal and thematic analyses, citation network construction, and main-path analysis.

ResultsAcross 192 papers, the review identified 511 ChatGPT application types, 690 concern items, and 368 influence usage factors distinct from traditional IT, achieving a metadata error rate of 1.04%. The human-agentic AI workflow enabled efficient synthesis of contextual information across studies, addressing the growing challenge of timely evidence integration in medical knowledge. The findings provide insights into the evolving trajectories of ChatGPT applications in healthcare and demonstrate the value of an expert-validated human-agentic AI workflow in supporting literature analysis and streamlining review processes.

ConclusionThis review provides a comprehensive overview of emerging ChatGPT applications, associated concerns, applied techniques, and usage factors in healthcare. The study further provides meaningful insights into the operational mechanisms of agentic AI, demonstrating the potential of human-AI collaboration for medical informatics research.

</details>


### 6. Hard to Halt: Automation Bias in Agent-Driven Sequencing Prior Authorization Workflows

- **Authors:** Nie, M., Chung, W., Waxler, J., Lee, M., Weng, C., Lewis, R., Ahimaz, P., Wang, K., Liu, C.
- **Published:** 2026-11-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.16.26355782](https://doi.org/10.64898/2026.06.16.26355782)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

PurposePrior authorization (PA) for exome or genome sequencing (ES/GS) is a time-consuming process that impedes timely rare disease diagnosis. Large language model (LLM)-based browser agents offer potential for automating these workflows, but their clinical reliability remains uncharacterized.

MethodsWe built a sandbox with a simulated ES/GS payer portal and a synthetic electronic health record (EHR) of 836 patient profiles, including compliant profiles and deficient profiles with designed issues. Gemini 3 Pro, Gemini 3 Flash, and Claude Opus 4.5 were evaluated on task completion, form accuracy, and appropriate withholding. Two replication experiments were run on 100 profiles to assess run-to-run variability of agent performance.

ResultsGemini 3 Pro (95.5%) and Claude Opus 4.5 (93.7%) completed far more tasks than Gemini 3 Flash (56.1%), consistently across runs. In the first run, all models rarely withheld deficient profiles for the correct reason (Gemini 3 Pro 0%, Gemini 3 Flash 17.3%, Claude Opus 4.5 5.2%). Replication revealed substantial variability: Gemini 3 Pros correct withholding rose to 28.8-36.8%, and only 18.0-48.0% of tasks yielded identical outcomes across all three runs. Without agentic scaffolding, Gemini 3 Pro flagged designed issues in 91.3% of deficient profiles but also halted on all compliant profiles.

ConclusionCurrent LLM-based browser agents show a systematic bias toward form submission. A modular, multi-agent architecture with human supervision may be warranted for safe clinical deployment.

</details>


---



## Arxiv (170 papers)


### 1. LesionAgent: Training-Free Agentic Tumor Tracking and Response Assessment in Longitudinal CT

- **Authors:** Maximilian Rokuss, Jeya Maria Jose Valanarasu, Alejandro Lozano, Benjamin Hamm, Yannick Kirchhoff, Fabian Isensee, Klaus Maier-Hein
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27876v1](http://arxiv.org/abs/2611.27876v1)
- **PDF:** [https://arxiv.org/pdf/2611.27876v1](https://arxiv.org/pdf/2611.27876v1)
- **Categories:** cs.CV, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Every few months, a cancer patient's CT scans decide whether treatment continues. 3D foundation models can now detect, segment, register and track lesions, yet none of them reads the scans as a radiologist does. A radiologist decides which findings are lesions, which are the same lesion months later and whether a new spot means progression, and checks each decision against the extensive rules of a clinical guideline. We introduce LesionAgent, an LLM agent that performs this read end to end without task-specific training. It operates frozen 3D models as tools, acts in 3D through coordinate-labelled views, remembers every lesion across visits in a registry, verifies every model output it relies on, and leaves every number to a deterministic guideline engine. On four public longitudinal CT datasets, LesionAgent tracks more lesions and measures them more accurately than every automatic baseline, and where the same 3D models chained by fixed rules call progression falsely at 33 of 56 follow-ups, it does so twice. On clinical follow-up CTs, it agrees with the radiologists' response at 20 of 23 follow-ups, including every change in response, and without training on DeepLesion, it retrieves more of its lesions than every tracker trained on it (89.0% vs. 87.4%). Its harness, not its LLM, makes the difference: given the same LLM and 3D models but not the harness, Claude Code reaches a detection F1 of 41% and LesionAgent 78%, and an open-weight LLM that can run inside the hospital rises from 6% to 73%. LesionAgent and a napari reading app for any LLM are available at https://github.com/MIC-DKFZ/LesionAgent.

</details>


### 2. SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning

- **Authors:** Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu, Borzoo Bonakdarpour
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27865v1](http://arxiv.org/abs/2611.27865v1)
- **PDF:** [https://arxiv.org/pdf/2611.27865v1](https://arxiv.org/pdf/2611.27865v1)
- **Categories:** cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings under partial observability. We employ Strategy Logic (SL), which allows explicit quantification over agents' strategies and uses the linear temporal logic (LTL) to specify the agents' objectives and constraints. This enables reasoning not only about how agents should act to satisfy a specification, but also about how they should respond to the strategies and behaviors of other agents. We evaluate SLICR on three popular benchmarks: Predator-Prey, Google Research Football, and our home-grown extension of SMAC-HARD, demonstrating its effectiveness, scalability, and ability to adapt to diverse adversarial strategies.

</details>


### 3. Beyond Self-Critique: Epistemic Convergence Control for Multi-Agent Research Verification

- **Authors:** Chrisantus Eze
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27839v1](http://arxiv.org/abs/2611.27839v1)
- **PDF:** [https://arxiv.org/pdf/2611.27839v1](https://arxiv.org/pdf/2611.27839v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems for scientific claim verification increasingly rely on role-structured LLM debate to pressure-test hypotheses. However, when debating agents are instantiated from the same underlying base model, they share identical latent representations, making self-critique bias structurally inevitable. Static fixed-iteration protocols compound this by either halting prematurely before evidence stabilizes or wasting inference compute after convergence. We present \sys{}, a multi-agent research verification framework that addresses both failure modes. First, we introduce an asymmetric role architecture comprising an Advocate, Skeptic, and Arbitrator with opposing epistemic directives, producing significantly lower role-embedding similarity (0.852 vs.\ 0.918 for symmetric Multi-Agent Debate [MAD], $p = 5.82 \times 10^{-8}$) and surfacing more contested claims (22.0\% vs.\ 15.4\%). Second, we propose the Belief-Delta ($\DB$) convergence criterion, an evidence-grounded stopping rule that eliminates over-iteration (0.0\% vs.\ 62.5\% for Fixed-$3$) while cutting LLM calls by 2.4$\times$. Third, each supported claim is anchored to a verbatim literature snippet audited by an independent NLI classifier, achieving a 21.7\% hallucination rate (comparable to 25.9\% for a Self-Refine critic, $p = 0.61$) while establishing auditable evidence grounding. Across 200 runs on 40 research hypotheses evaluated with DeepSeek-R1-32B, \sys{} balances compute efficiency with rigorous epistemic verification.

</details>


### 4. Shared Understanding in Human-AI Teams: Coordination Continuity in Evolving Work

- **Authors:** Siân Lindley, Britta Burlin, Christian Poelitz, Lev Tankelevitch, Richard Banks
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27746v1](http://arxiv.org/abs/2611.27746v1)
- **PDF:** [https://arxiv.org/pdf/2611.27746v1](https://arxiv.org/pdf/2611.27746v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

People are increasingly working with AI agents as part of extended, asynchronous workflows. In these settings, shared access to information does not guarantee a shared basis for action: goals, plans, and roles may persist while their current significance changes. We introduce coordination continuity, the extent to which collaborators sustain a workable basis for interdependent action as work progresses. Drawing on research on collaborative work, along with two qualitative team studies and a reflexive case from our own repository-based environment, we present a framework of three elements: durable representations of collaborative work; relative coordination properties that support interpretation of representations in the moment; and interaction mechanisms through which the status of representations can be understood and altered. We use a build-act-drift-rebuild heuristic and the notion of consequential moments to characterise when rebuilding may be needed. We draw eight design implications for collaborative AI infrastructure.

</details>


### 5. AutoOntologyBench: A Task-Grounded Benchmark for Agentic Knowledge Engineering

- **Authors:** Minye Shao, Chenghao Xiao, Xingyue Zhao, Yang Long
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27734v1](http://arxiv.org/abs/2611.27734v1)
- **PDF:** [https://arxiv.org/pdf/2611.27734v1](https://arxiv.org/pdf/2611.27734v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Foundation-model agents are increasingly extending beyond software engineering (SWE) into autonomous scientific research, where acquiring and integrating domain knowledge remains a critical challenge. Recent industrial advances have increasingly adopted knowledge graphs and ontology-based semantic layers to organize heterogeneous knowledge into reusable representations. We ask: Can autonomous agents construct ontologies that help them solve real tasks, and do they offer measurable benefits over alternative knowledge representations? Existing benchmarks evaluate ontology correctness or agent task success in isolation, leaving the value of autonomously acquired knowledge unresolved. We therefore introduce AutoOntologyBench, a task-grounded benchmark comprising 19,947 audited tasks grounded in 18 real-world knowledge sources across 7 domains, with source-native verification. Spanning Application, Repair, Organization, and Construction, AutoOntologyBench compares nine frontier-model agents under matched knowledge representations. Layered on retrieval, agent-built ontologies add 6.1 points of task success, yet trail an expert-derived reference by 13.0, identifying autonomous knowledge acquisition as the bottleneck to scalable scientific research. Code and resources are available at https://github.com/VinyehShaw/AutoOntologyBench.

</details>


### 6. A Cognitive Agentic AI Framework for Interactive Process Analysis and Optimization

- **Authors:** Trung Ngoc Trinha, Roman Tschentscher, Trong Dong Nguyen, Trung Thanh Nguyen, Anna Trubetskaya
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27725v1](http://arxiv.org/abs/2611.27725v1)
- **PDF:** [https://arxiv.org/pdf/2611.27725v1](https://arxiv.org/pdf/2611.27725v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Complex multivariable process analysis and optimization require coordinated access to simulation, structured data, machine learning (ML), optimization, and scientific literature, often across disconnected software tools. We present a Cognitive Agentic AI Framework (CAAF) that enables interactive, iterative process investigation through natural-language prompts within an established flowsheet. Following harness-engineering principles, CAAF assigns task interpretation, planning, knowledge synthesis, and context management to a large language model while delegating numerical calculations to specialized tools. Dedicated providers connect databases, scientific-document retrieval, ML-assisted Bayesian optimization (BO), and COCO process simulation. The framework is demonstrated on methyl acetate production. Guided by successive prompts, an engineer explored multivariable relationships, conducted 4,000 BO iterations to maximize carbon conversion yield (C-Yield) and minimize specific energy cost (C-SEC), refined operating bounds, and verified selected candidates through process simulation. Re-simulation of 16 candidates within the restricted domain showed close agreement with ML predictions, with a mean absolute C-Yield error of 0.0085 (0.85 percentage points). The highest BO-derived C-Yield, verified by COCO, was 0.921 versus approximately 0.81 in the initial dataset, an improvement of about 11 percentage points. CAAF also detects and reports non-converged simulations, excludes invalid outputs, and continues subsequent evaluations. The results demonstrate how human-guided agentic coordination can combine engineering tools for iterative analysis and optimization with rigorous simulation-based verification under a fixed process topology.

</details>


### 7. Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation

- **Authors:** Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27689v1](http://arxiv.org/abs/2611.27689v1)
- **PDF:** [https://arxiv.org/pdf/2611.27689v1](https://arxiv.org/pdf/2611.27689v1)
- **Categories:** cs.RO, cs.AI, cs.CV, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a robot-control interface, while the Reflector converts execution evidence into reusable operational guidance. Hierarchical Memory Architecture maintains short-term execution context and long-term experiential knowledge to support execution and reflection. Evidence-based Experience Reflection grounds failure diagnosis in observed interactions, while Recursive Harness Self-Improvement refines operational guidance across successive attempts. Experiments on RoboTwin 2.0, RoboSPA, and RMBench demonstrate the effectiveness of Embodied-Harness in generalization under environmental variations, spatial reasoning, long-horizon planning, and memory-dependent manipulation. Our method achieves success rates of 82.4%, 76.7%, and 94.4% on the three benchmarks, respectively. Real-world evaluation further yields an average success rate of 96.7% across three manipulation tasks. These results highlight the potential of Embodied-Harness to improve robotic manipulation through experience-driven harness self-improvement.

</details>


### 8. Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning

- **Authors:** Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau, Roberto Girau
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27631v1](http://arxiv.org/abs/2611.27631v1)
- **PDF:** [https://arxiv.org/pdf/2611.27631v1](https://arxiv.org/pdf/2611.27631v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the guarantee holds for every policy a learner produces. We introduce epistemic typestates, a type discipline for safe multi-agent reinforcement learning. An agent's type is a protocol whose states record its beliefs, the worlds it cannot rule out from its own observations and actions, and permits only actions that are safe in every world of the belief, whatever the others do within their public types. Agents learn inside their types, which are built and checked one agent at a time and run without communication. We prove type soundness and team safety, give a synthesis that is sound and complete, build types from guards when worlds are infinite, and show that shields are a special case. All proofs are mechanised in Rocq. On nine benchmarks, no typed learner causes a safety violation, and task performance does not differ significantly from that of two recent multi-agent shielding methods. Where a contract-based method fails at five and ten agents, types for ten agents are built in under a second. In the two continuous benchmarks, Lagrangian learners cause thousands of violations in every training run.

</details>


### 9. Potential emergence in LLM agents: a statistical physics perspective

- **Authors:** Zhuo-Yang Song, Hua Xing Zhu
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27618v1](http://arxiv.org/abs/2611.27618v1)
- **PDF:** [https://arxiv.org/pdf/2611.27618v1](https://arxiv.org/pdf/2611.27618v1)
- **Categories:** cs.LG, cond-mat.stat-mech, cs.AI, cs.CL, nlin.AO


> Summary unavailable.


<details>
<summary>Abstract</summary>

There has been significant recent interest in understanding the behaviour of LLM agents from the perspective of human preferences or corpus statistics. In this paper we propose agent states as intermediate variables through which post-training can be measured and predicted. From a statistical physics perspective, we study the emergence of a global potential which governs the transition of state in LLM agent reasoning. We introduce a partition function to model the ideal KL-regularised transition distribution and track potential structure, mean reward and state entropy. We demonstrate our approach in two Qwen3.5-9B tasks: safety-test selection and physics-reasoning auditing. We observe that the potential structure strengthens during post-training as predicted from our framework, while joint changes in reward and state entropy provide consistency evidence. States thus provide a quantitative description of how post-training organises agent behaviour.

</details>


### 10. Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring

- **Authors:** Wenqi Zhou, Leonardo Baldo, Edwin Kolbe, Manuel Arias Chao
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27556v1](http://arxiv.org/abs/2611.27556v1)
- **PDF:** [https://arxiv.org/pdf/2611.27556v1](https://arxiv.org/pdf/2611.27556v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Beznau Unit 1 in Switzerland, in operation since 1969, is the most experienced nuclear reactor still running worldwide. Five decades of incremental modernization have left its monitoring systems, alarm logs, variable catalogs, technical specifications and investigation reports in separate silos that were never designed to be queried together. As a result, investigating a core instrumentation anomaly means slow, manual gathering of knowledge scattered across databases, documents, and experienced colleagues. We present a hierarchical multi-agent assistant built on large language models (LLMs) to support these investigations and reduce the need for tedious manual searches in SAP systems. An orchestrating agent breaks down an engineer's question and hands the parts to specialized sub-agents, each with read-only access to one source. Domain expertise is written as natural-language procedures that plant engineers can read, review and revise. The system is strictly advisory, with every answer traced back to its sources. We also report organizational lessons from introducing agentic AI into a culture built on safety, traceability and conservative change. Beyond the technical architecture, the Beznau case study examines how an assistant can be introduced into a setting where evidence must be traceable, changes carefully reviewed, and operational decisions retained by plant personnel, paving the way for the responsible use of agentic AI in industrial plant monitoring.

</details>


### 11. Epistemic Social Learning: Latent Behavioral Structure under Endogenous Multi-Agent Interaction

- **Authors:** Jainendra Shukla, Dhruv Jaiswal, Divyanshi Beniwal, Kiriti Kanjilal
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27545v1](http://arxiv.org/abs/2611.27545v1)
- **PDF:** [https://arxiv.org/pdf/2611.27545v1](https://arxiv.org/pdf/2611.27545v1)
- **Categories:** cs.MA, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

In multi-agent interaction, a learner's actions shape the observations from which it infers other agents' behavior. A behavioral model may predict these observations well yet support poor adaptation when opponents change. We introduce Epistemic Social Learning (ESL), which couples fast, interaction-specific Bayesian beliefs with slower online learning of population-shared behavioral prototypes. Belief-conditioned decisions influence subsequent observations and, in turn, the representations learned from them. Under explicit regularity and averaging assumptions, we provide a conditional stochastic-approximation characterization of these coupled dynamics. Across twelve synthetic $3\times3$ cooperative, coordination, and adversarial games, ESL achieves the lowest aggregate post-switch regret among the evaluated online latent-adaptation methods, including a switch-aware Bayesian filter. Additional experiments examine observation loss, noise, and asymmetric incentives. These findings illustrate how predictive fit can differ from decision-relevant adaptation under policy-dependent interaction.

</details>


### 12. Fix Where It Fails: Root-Cause-Guided Agentic Harness Optimization for Scene Graph Generation

- **Authors:** Jee Eun Kim, Donghyeon Choi, Sangjune An, Hae Beom Lee, Kyong Hwan Jin
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27529v1](http://arxiv.org/abs/2611.27529v1)
- **PDF:** [https://arxiv.org/pdf/2611.27529v1](https://arxiv.org/pdf/2611.27529v1)
- **Categories:** cs.CV, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scene graph generation (SGG) aims to detect objects in an image and predict the relationships between them. The standard PredCls, SGCls, and SGDet settings show how much performance drops without ground-truth boxes and labels, but not where or why a model fails. Knowing this would allow fixing a model where it fails, without retraining. We propose RoHa-SGG (Root-cause-guided Harness optimization for SGG), which extends agentic harness optimization to SGG. It optimizes the harness, the inference code around a frozen SGG model. RoHa-SGG has two main LLM agents. A root-cause analysis (RCA) agent finds the components where the model fails and diagnoses why, and a proposer agent searches for a harness that fixes these causes. We evaluate RoHa-SGG on Visual Genome and PSG with representative two-stage, one-stage, and multimodal-LLM SGG models. The analysis shows that the components where ground-truth triplets are lost differ across models and datasets. RoHa-SGG improves every metric on all five model-dataset combinations. Graph-constrained R@100 and mR@100 rise by up to 15.8 and 26.4 points for the multimodal LLM and by up to 3.6 and 10.1 points for the two-stage and one-stage models. With root-cause guidance, the harness search reaches the final score of an unguided search up to three times faster.

</details>


### 13. From Manufacturing Event Logs to Simulation: Enabling SMEs with Agentic AI for SimPy Simulation Generation

- **Authors:** Richard Reider, Lina Döring, Sebastian Lang, Tobias Reggelin, Sebastian Trojahn, Pascal Reusch
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27483v1](http://arxiv.org/abs/2611.27483v1)
- **PDF:** [https://arxiv.org/pdf/2611.27483v1](https://arxiv.org/pdf/2611.27483v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

High expertise and cost barriers exclude small and medium-sized enterprises from discrete-event simulation (DES). We introduce GenAI4SimPy, a multi-agent framework powered by Qwen 3.6 (27B), an open-weight large language model, that automates end-to-end DES generation from manufacturing event logs to executable SimPy models through tool-augmented reasoning and human-in-the-loop validation. Evaluated on three execution blocks from a public smart factory dataset, the framework achieved a mean absolute percentage error of 7.9\% and coverage of failure rate for all three blocks and of throughput for two of three. A fidelity paradox was observed: accurate process-level parameters did not ensure system-level behavioral fidelity, with flow-time and throughput errors driven by misinterpreted observation-window truncation and absent system-level calibration. These results demonstrate that local open-weight models can perform DES generation at accuracy comparable to cloud-based alternatives, while identifying parameter extraction as necessary but insufficient for behavioral validity. Source code and results are available at https://github.com/RaikoPipe/genai4simpy

</details>


### 14. Evidence sufficiency assessment enables cost-effective review allocation in on-premise clinical AI agents

- **Authors:** Yiwen Qiu, Che Sun, Shu Shen, Wentao Wang
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27390v1](http://arxiv.org/abs/2611.27390v1)
- **PDF:** [https://arxiv.org/pdf/2611.27390v1](https://arxiv.org/pdf/2611.27390v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-premise clinical AI agents must auto-accept high-confidence diagnoses, deferring others to clinician review, yet token probabilities and self-reported confidence miss errors, while more reliable five-run consistency incurs fivefold compute. We propose training-free decision-point evidence sufficiency assessment and a three-tier sequential triage protocol. Masking reasoning and diagnosis, the same 4B model scores sufficiency from objective evidence via prior-debiased probabilities over five ordered levels. Calibration freezes a nominal top-50% threshold, selecting single-run, five-run consistency, or full-deferral tiers by whether the one-sided 95% Wilson lower confidence bound of pass rate among accepted cases meets the 95% clinical target line. Across 1,605 MIRA-v2, CDM, VivaBench, and in-hospital liver malignancy primary cohort cases, MIRA-v2 single-run top-50% pass rate reached 98.91%, matching five-run consistency, saving ~80% compute; CDM achieved 96.00% test attainment by escalating to the five-run consistency tier; cross-specialty, missing-imaging, and combined enriched cohorts entered the full-deferral tier, capping calibration false-certification rate at 0.00%-3.50%.

</details>


### 15. Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Dennis Gross, Jørn Eirik Betten, Helge Spieker
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27368v1](http://arxiv.org/abs/2611.27368v1)
- **PDF:** [https://arxiv.org/pdf/2611.27368v1](https://arxiv.org/pdf/2611.27368v1)
- **Categories:** cs.MA, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

</details>


### 16. Correct Precedents Induce Policy Violations in On-Device LLM Agents

- **Authors:** Chong Tian, Yu Wang, Steve Liu, Qirong Ho, Xiuying Chen
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27216v1](http://arxiv.org/abs/2611.27216v1)
- **PDF:** [https://arxiv.org/pdf/2611.27216v1](https://arxiv.org/pdf/2611.27216v1)
- **Categories:** cs.CL, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Local-cloud agent systems pair a cloud model with a small on-device agent that acts on private data, often as the last check before an irreversible action. We identify, for the first time, a failure in which such an agent is led into a violation by its own correct decisions within a session. After it correctly releases an item whose restriction was lifted, it becomes more likely to release the next item that is still restricted. Because the trigger is a correct decision, a history with no faulty step can still end in a violation. We call this failure correct-precedent generalization and find it in 13 open-weight models from nine developers. A single correct precedent can cut the safe rate of the most affected agent roughly in half, and the risk compounds when a refused request is simply sent again in a new session. Interventions on the agent's history indicate that it carries its decision on the released item over to the restricted one instead of checking that item's status. Building on this finding, we propose Paired Decision Distillation (PDD), which distills the decisions of a weakly affected teacher into a LoRA adapter. PDD restores the safe rate to nearly 100% in every distilled model, without extra prompt text or model calls.

</details>


### 17. Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material

- **Authors:** Jinxiang Xie, Xinyi Zhang, Changjiang Jiang, Kexu Liu, Qi Yang, Yuxin Su
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27139v1](http://arxiv.org/abs/2611.27139v1)
- **PDF:** [https://arxiv.org/pdf/2611.27139v1](https://arxiv.org/pdf/2611.27139v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems increasingly divide long tasks among subagents whose reports a senior agent turns into the final answer. Such a division of labor pays off only if each agent, and above all the senior agent, carries out the duties of its role. Current evaluations, however, mostly score the final answer, and a fluent, well-cited answer cannot show whether the senior agent weighed its subagents' reports or merely aggregated them. To assess whether a senior agent meets its assigned responsibilities, we define role integrity as the preservation of an agent's functional responsibilities when it acts on its subordinates' material. To measure it, we introduce RI-Bench, a behavioral benchmark grounded in the structures and public records of three institutional hierarchies: peer review, appellate adjudication, and parliamentary inquiry. We choose these hierarchies because their rules explicitly assign the senior role a duty toward subordinate material, and together they cover three basic duties: to weigh, to verify, and to relay. Rather than scoring output correctness, we measure how senior agents' outputs respond to controlled changes in subordinate material, using rule-based checks and a rubric-guided LLM judge calibrated against human annotation. Across eight LLMs and over 12,000 agentic episodes, senior agents rarely adopt a planted procedural error (2.9% of rulings) but often follow a majority of generic reviews (up to 71% of decisions) or drop witnesses' stated limitations (up to 65% of cited claims). Obligation prompts reduce these failures without removing them, and they also shift behavior in the control conditions. These findings motivate direct, obligation-specific evaluation of role integrity rather than inferring it from general capability or explicit role instructions. Code and data are available at https://github.com/jxtse/ri-bench.

</details>


### 18. Double counting in LLM evidence fusion: exact posteriors separate rule compliance from posterior gain

- **Authors:** Tengfei Shao, Asma Rezaei, Ali Reza Kamali
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27138v1](http://arxiv.org/abs/2611.27138v1)
- **PDF:** [https://arxiv.org/pdf/2611.27138v1](https://arxiv.org/pdf/2611.27138v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language models fuse reports in retrieval, multi-agent consensus and agent memory, where treating shared-source reports as independent can double count evidence. A common remedy is an instruction to count each source once. Its value depends on the receiver's raw baseline. Pricing it needs an exact reference. We build the graded-dependence exact reference: binary worlds with single-report reliability 0.65 and four dependence levels, whose disclosed parameters give every world an exact posterior and every rule a target risk. The paired gain protocol scores raw and instructed answers of four configurations on 2,976 worlds. Agreement and gain separate in both directions. At $δ$ = 0, claude-opus-5-5 and gpt-6.1-sol agreed with the rule within 0.001 in 744 of 744, and the instruction raised their posterior mismatch by 0.044; gpt-6-luna agreed in 165 of 744 and gained 0.0140 (95% interval 0.0064 to 0.0219); claude-haiku-5-5's gain moved from -0.0295 ($δ$ = 0) to +0.0302 ($δ$ = 1) (descriptive). The prespecified first-child endpoint contrast, gain at $δ$ = 1 minus $δ$ = 0, was 0.0342 (0.0303 to 0.0382). In the preregistered tests, the raw source-weight contrast was positive (0.259, 95% interval 0.182 to 0.337; Holm rejected zero) and the grouping endpoint difference was not detected (0.0004, -0.0023 to 0.0031). This interval excludes differences larger than 0.0031 in magnitude and lies within the registered precision bound of $\pm$0.0046. The reference prices the rule before any model call. The paired gain, estimable as a Brier difference on labelled deployment items, decides adoption per receiver and prompt condition.

</details>


### 19. OpenRing: Deadlock-Free Execution of Any Planner on AGV Floors with One-Way Lanes

- **Authors:** Zhihao Lin, Anh-Tu Nguyen, Hui Zhang, Yoshinobu Kawahara
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27127v1](http://arxiv.org/abs/2611.27127v1)
- **PDF:** [https://arxiv.org/pdf/2611.27127v1](https://arxiv.org/pdf/2611.27127v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lifelong multi-agent path finding replans routes for automated guided vehicles, but deviations can invalidate a plan. With one-way lanes, a late vehicle or lost planner can close a ring of full segments. We separate how fast the floor runs from whether it keeps running. In OpenRing a planner proposes routes and an order, a local guard commits only moves and route changes that cannot close such a ring, and the order binds for a bounded time. Despite arbitrary proposals or planner loss, no ring closes. With two-place segments, traffic can continue under disturbances; progress is guaranteed once they end, and all vehicles exit if entries also stop. Among rules that reroute only on a proposal, every guard veto is necessary, and a clean plan keeps its crossing orders. The guarantee has a price: no rule that never stores a vehicle in a crossing under arbitrary stops carries more than $B/T_s$ per segment of $B$ places and traversal time $T_s$. With binding orders, three planners deadlock in 80 of 126 runs across eight floors. Inside OpenRing, none of the 126 runs deadlocks. OpenRing's closed-loop throughput rivals or exceeds the best baseline's. Physics simulations show no deadlocks or overlaps.

</details>


### 20. CoEvoBench: Can LLMs Drive Recursive Co-Evolution of Agentic Systems?

- **Authors:** Chuan Xiao, Baojie Wang, Haizhao Fan, Hongzhe Du, Xander Xu
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27116v1](http://arxiv.org/abs/2611.27116v1)
- **PDF:** [https://arxiv.org/pdf/2611.27116v1](https://arxiv.org/pdf/2611.27116v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of an LLM agent depends on both its model and its harness, the code that mediates its interaction with tools and environments. Can LLM researchers drive this co-evolution as a recursive improvement process, deciding round after round which component to change when each change alters the value of the other? Existing benchmarks evaluate post-training or data research with the harness out of scope, or harness optimization with the model fixed, leaving this joint decision unmeasured. We introduce CoEvoBench, a benchmark that evaluates LLMs as researchers co-evolving the model and harness of a target agent across five agentic domains. Researchers start from a common base model and initial harness, train and revise within a 24-hour budget, and submit a model-harness pair that is scored on separate test tasks. Across five frontier researchers, the strongest closes more than four fifths of the gap to an instruction-tuned reference system, and co-evolution succeeds on interaction tasks but rarely on long-horizon coding. These results suggest that current LLMs can make a strong first improvement, but cannot yet turn feedback from an improved system into the next one. CoEvoBench provides a controlled testbed for measuring the research capabilities that recursive co-evolution requires.

</details>


### 21. Epistemic Guard: Out-of-Process MCP Receipt Proxying, Post-Turn Prose Supervision, and Provenance-Gated Memory for Tool-Using Autonomous Agents

- **Authors:** Sean Maxwell
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27095v1](http://arxiv.org/abs/2611.27095v1)
- **PDF:** [https://arxiv.org/pdf/2611.27095v1](https://arxiv.org/pdf/2611.27095v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents using the Model Context Protocol (MCP) face three runtime verification gaps: (i) action fabrication, where post-tool prose narrates side effects that failed, timed out, or never ran; (ii) provenance collapse, where unverified model prose or web text enters durable memory alongside executed tool outputs; and (iii) syndicated echo amplification, where mirrored web pages satisfy multi-source corroboration from one origin. Existing MCP firewalls inspect wire calls before execution, while LLM-judge guardrails require multi-gigabyte VRAM without binding prose to receipts. We present epistemic-guard (v0.5.2), an open-source Python library and out-of-process stdio MCP receipt proxy (15 modules, 0 MiB GPU VRAM). epistemic-guard isolates Ed25519 signing keys out of process, writes RFC 6962 Merkle logs with AER-1 receipt translation, checks post-turn prose on CPU with SHA-256-verified OpenVINO INT8 encoders (4 models, 279.48 MB total; 82.67 MB on the supervision path), gates SQLite writes across 7 provenance domains, and collapses verbatim and lightly edited wire-syndicated RAG mirrors. On conformance suites, epistemic-guard rejects 100.0% of tampered receipts (200 Merkle leaves), passes 58/58 official AER-1 ingestion vectors and 50/50 reference-verified AER-1 exports, verifies 100.0% of 40 fault-injected wire calls and 100 concurrent appends with 0 key leaks, and blocks 100.0% of 100 unauthorized memory writes. Across $N=250$ frozen-benchmark traces, epistemic-guard reaches 93.2% accuracy at 17.9 ms warm median CPU latency (8.62 ms single-clause; 921.8 ms cold-start load), beating 12B-14B GPU judges by 6.4-6.8 points ($p=0.0259$, $p=0.0095$) at 4.26-4.5$\times$ lower latency; on $N=60$ live mcp-proxy traces, it catches 96.15% of hazards at 76.67% accuracy (38.24% FPR; $+18.34$ points over Stage-1-only, $p=0.001$) in 9.16 ms p50.

</details>


### 22. Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation

- **Authors:** M. Ahmadi Achachlouei
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27094v1](http://arxiv.org/abs/2611.27094v1)
- **PDF:** [https://arxiv.org/pdf/2611.27094v1](https://arxiv.org/pdf/2611.27094v1)
- **Categories:** cs.CL, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are being proposed for bank model validation, yet evaluations that compare agent-assisted work with manual practice credit the agent with gains that come from digitized evidence and deterministic tests. We propose a staged architecture in which an LLM-free controlled workflow (P1) is both the fallback and the control arm for individually authorized agent tasks (P2), and an attribution protocol that credits an agent only for faults P1 does not already report. The protocol charges decoy false alarms, unnecessary actions and endorsed developer assertions, counts invalid outputs as misses, folds newly automatable findings back into P1 with discovery credit, and fixes safety bounds and a break-even cost gate in advance. On a synthetic credit-scorecard harness, five scripted reference policies show why this matters: naive case accuracy (4/6) and pooled detection (3/5) tie four flawed policies, whereas the protocol separates all five and credits only the reference policy with detection beyond P1. One fold-back round raises a P1-parroting policy's naive scores without any change to the policy. A regression matrix of sixteen mutants covers nine ways in which earlier versions of the evaluation passed misleadingly. No LLM agent has been evaluated yet; we specify a falsifiable pilot.

</details>


### 23. Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes

- **Authors:** Kaviru Hapuarachchi
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27090v1](http://arxiv.org/abs/2611.27090v1)
- **PDF:** [https://arxiv.org/pdf/2611.27090v1](https://arxiv.org/pdf/2611.27090v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an AI coding agent deletes the wrong files or a long agent run crashes, users fall back on recovery mechanisms: resume from a checkpoint, undo, ask for approval, read the log. Research runtimes promise stronger guarantees, such as saga-style compensation and transactional rollback. We ask what public evidence shows about whether either kind works in real use. Under a protocol frozen before data collection, we graded 12 persistent agent runtimes, 26 coding-agent harnesses and 12 research runtimes on eight recovery mechanisms, from not found to exercised in a real run, with two blind coding passes, adjudication and re-verification against archived sources. Recovery is exercised almost everywhere in practice: 11 of 12 runtimes and 25 of 26 harnesses have at least one real-use report. Yet of 128 such reports, only 19 describe the run fully recovering; 54 are partial and 45 failed. Checkpoint/resume recovered once in 27 reports, rollback once in 15. Research runtimes show the opposite profile: guarantees evaluated on benchmarks, none reported in operation, and compensation of external effects, their central guarantee, is offered by no harness at all.

</details>


### 24. Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions

- **Authors:** Ruichao Liang, Wenzhong Deng, Jing Chen, Yuqing Li, Kaixuan Li, Cong Wu, Yang Liu
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.27046v1](http://arxiv.org/abs/2611.27046v1)
- **PDF:** [https://arxiv.org/pdf/2611.27046v1](https://arxiv.org/pdf/2611.27046v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on Web interaction, issuing searches, following links, and reading pages, to complete complex user tasks. Since each action is driven by the agent's private context, including the user's prompt, dialogue history, memory, and connected data, it also opens a new privacy exposure surface. Prior attacks either passively analyze network traffic, which yields only coarse correlations, or hijack the agent through indirect prompt injection, which must place sensitive content in an outgoing field and is blocked by content-level defenses. Whether an attacker can actively recover fine-grained private context without any explicit transmission thus remains insufficiently understood.
  Our insight is that an agent's benign Web decisions themselves leak private context, as what it chooses to visit encodes whether, which, and in what order it acts, forming a behavioral covert channel. Building on this, we design SNOOP, a stateful hierarchical probing framework that narrows a coarse-to-fine hypothesis tree per task and reconstructs user queries and profiles from the agent's observable paths. Across four agents and three LLM backbones on 500 StackExchange queries and 378 multi-turn iKAT dialogues, SNOOP recovers query concepts with an average F1 of 0.89 and user profiles with an F1 of 0.80, while four representative agent defenses change its recovery by less than 0.03 F1. Since no sensitive content is ever transmitted, content-level inspection cannot detect this leakage; we therefore propose Selection-Obfuscated Retrieval (SOR), which acquires resources under a fixed budget independent of private context and confines the agent's selection to a local snapshot, cutting SNOOP's F1 to 0.39 without additional LLM inference.

</details>


### 25. Contexture: Runtime Context Eviction for High-Throughput Agent Serving

- **Authors:** Colin Hong, Bryan Shan, Wei Siong Pang, Chengzhi Lu, Xu Guo, Nitin Shivaraman, Tao Luo, Esha Choukse, Kisson Lin, Dmitrii Ustiugov
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26980v1](http://arxiv.org/abs/2611.26980v1)
- **PDF:** [https://arxiv.org/pdf/2611.26980v1](https://arxiv.org/pdf/2611.26980v1)
- **Categories:** cs.DC, cs.AI, cs.MA, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents such as Hermes, OpenClaw, and Codex repeatedly resend growing execution histories, increasing shared GPU key-value (KV) cache demand in high-bandwidth memory (HBM). We show that shared KV capacity limits agent-serving throughput. Existing context-reduction methods lack global cache-state visibility, while runtime KV managers lack tool-execution information. Tracing tokens to their originating tool operations reveals that later operations supersede earlier outputs and associated turns, identifying 64% of recorded final-history tokens as removal candidates.
  We present Contexture, a harness- and model-agnostic architecture for runtime context eviction. Contexture separates the harness's full conversation history from the model's execution context, reducing subsequent requests' KV demand without modifying harness logic or model execution. It combines tool-execution information with global visibility into shared KV pressure and prefix residency: supersession identifies removal candidates, while runtime state determines when removal justifies sacrificing cached computation. This coordination reduces memory demand and decode KV traffic while limiting re-prefill interference with concurrent decoding, without additional model calls or training. Across two models, two harnesses, and two benchmarks, Contexture improves throughput under SLO by 20-73% over the best of no eviction, harness compaction, AgentDiet, and Continuum, and by 7-63% over observation masking in five of eight configurations, and reduces GPU energy per completed session by up to 11%. It also raises throughput under SLO by 23% over LMCache alone on H100. Live-agent experiments show a mean accuracy improvement of 1.4 percentage points over unloaded no eviction, with a worst-case loss of 3.7 points, while observation masking loses 3-28 points.

</details>


### 26. Keep the Process, Change the Supplier: Runtime Governance for Tool-Using AI Agents

- **Authors:** Deepak Waghmare, Shaad Sufi
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26966v1](http://arxiv.org/abs/2611.26966v1)
- **PDF:** [https://arxiv.org/pdf/2611.26966v1](https://arxiv.org/pdf/2611.26966v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using AI agents propose actions whose authorization and external effects cannot be inferred from generated text alone. We study an execution boundary that separates agent proposals from business-controlled authority, context disclosure, and supplier selection. The Open Process Control Plane (OPCP) mediates capability calls and records uncertain outcomes when a supplier may have acted without returning an acceptable reply. We evaluate this runtime with scripted requests and synthetic suppliers: 2,400 fault episodes across four policies, 60 process-termination/restart episodes, 19,000 timed calls across 19 configurations, five targeted mutations over 43 fixtures, and 160 substitution records. No language model or autonomous agent is evaluated. OPCP and a conservative composition agree on all measured fault outcomes. Both recover after definite refusal without cross-supplier duplication; retry-all duplicates effects in every tested lost-reply-after-commit case. Persistent runtime state prevents cross-supplier replay in the restart experiments, while same-supplier duplicate prevention also requires supplier idempotency. At 128 suppliers, best-score routing has a median latency of 1.411 ms versus 0.261 ms for pinned routing. All five selected mutations are detected, and record enumeration exposes acceptance of an empty regression set. These results characterize an execution mechanism relevant to agent governance, including its costs and assumption boundaries. They do not establish improved agent task success, prompt-injection resistance, or real-vendor model portability.

</details>


### 27. Tracking and Limiting Unsupported Claim Propagation in Multi-Agent LLM Systems: A Provenance-Aware Framework

- **Authors:** Zijia Cao, Hanqing Dou
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26957v1](http://arxiv.org/abs/2611.26957v1)
- **PDF:** [https://arxiv.org/pdf/2611.26957v1](https://arxiv.org/pdf/2611.26957v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This research examines how unsupported claims change as they move through multi-agent pipelines. It also examines whether preserving provenance can reduce these changes. We test both homogeneous and heterogeneous pipelines. Homogeneous pipelines use the same model across agents, while heterogeneous pipelines use different models. We compare the baseline with a provenance-aware framework. The framework passes each claim with its support status, source, evidence and transmission history. No new evidence is introduced during transmission. We measure changes in claim meaning, unsupported detail accretion, semantic drift, and provenance preservation. These metrics show whether the framework limits unsupported changes as claims pass between agents.

</details>


### 28. CodeReviewBench: An Automated Benchmark for Evaluating the Software Factory

- **Authors:** Ashley Zhang, Narmeen Fatimah Oozeer, Aleksandr Zverianskii, Daniel Ng, Tasana Pejovic, Antía García, Jacob Clyne, Ravpreet Setia, Akshay Utture, Etan Jacob Ginsberg, Shriyash Kaustubh Upadhyay, Fazl Barez
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26942v1](http://arxiv.org/abs/2611.26942v1)
- **PDF:** [https://arxiv.org/pdf/2611.26942v1](https://arxiv.org/pdf/2611.26942v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents ship more code with minimal human oversight, code review becomes the critical quality-control checkpoint -- but one without a reliable, objective verifier: review quality is nuanced and ultimately a judgment call by the PR author. Existing benchmarks are structurally misaligned with this: annotators are third-party reviewers, like the bots they evaluate, not the PR authors who actually decide what to fix. They also rely on small, static issue sets that require full re-evaluation as tools update, limiting how frequently progress can be tracked. We introduce CodeReviewBench, built on a fundamentally different signal: revealed developer preferences -- if a developer acts on a bot's suggestion, we treat it as useful; if they ignore it, we do not. This signal is mined daily from the public GitHub event stream, yielding 500K+ judged PRs across 18 tools, and refreshes continuously as tools evolve. We validate the developer preference against an independent offline benchmark: the two agree on precision rankings and independently detect the same product updates within days of vendor releases. Together, these form the benchmark.

</details>


### 29. SecretAgent: A Multi-Agent Framework for Privacy Protection against Vision Language Models

- **Authors:** Minda Zhao, Yue Zhang, Mengyu Wang
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26936v1](http://arxiv.org/abs/2611.26936v1)
- **PDF:** [https://arxiv.org/pdf/2611.26936v1](https://arxiv.org/pdf/2611.26936v1)
- **Categories:** cs.CV, cs.AI, cs.CR, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) can infer private information from shared images, including locations, personally identifiable information (PII), and personal attributes such as age and sex, even from medical images. Adversarial perturbations can protect such information against black-box VLMs, but existing methods overlook image quality and introduce visible artifacts into the images they protect. We present SecretAgent, the first general multi-agent framework that protects image privacy against VLMs while preserving visual fidelity. LLM agents iteratively locate the visual evidence that reveals private information and adapt an invisible perturbation to the target VLM's answers and to an appearance reviewer agent, which rejects any candidate with visible artifacts. We instantiate SecretAgent with two complementary variants: SecretAgent-Gradient optimizes the perturbation through six surrogate encoders for cross-model transferability, and the gradient-free SecretAgent-Tool composes procedural noise and achieves the best perceptual fidelity on three of the five datasets. Experiments on four privacy applications (geolocation, PII, facial, and medical) across five datasets and six VLMs show that SecretAgent preserves image quality substantially better than existing methods while achieving state-of-the-art privacy protection in every application, and that its protection transfers to other VLMs.

</details>


### 30. Multi-Tier Edge Triage: Optimizing Latency for Safe Clinical Agents

- **Authors:** Joshua Broyde, Sarita A. Joshi
- **Published:** 2026-11-20
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26914v1](http://arxiv.org/abs/2611.26914v1)
- **PDF:** [https://arxiv.org/pdf/2611.26914v1](https://arxiv.org/pdf/2611.26914v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deploying generative AI agents in enterprise clinical workflows requires enforcing multi-dimensional safety and compliance policies--preventing HIPAA Protected Health Information (PHI) exposure, maintaining clinical scope-of-practice boundaries, ensuring patient-appropriate reading comprehension, and preserving brand integrity--under interactive latency constraints. Synchronous outbound calls to cloud Large Language Model (LLM) judges add substantial network and decoding overhead onto the critical response path. We present Multi-Tier Edge Triage, a safety screening architecture that co-locates a compact Tier-1 sequence classifier on the clinical agent's host server, resolving clear queries in-process without a network round-trip and escalating only ambiguous queries to a Tier-2 cloud LLM judge. To evaluate Tier-1 encoders without length or unigram shortcuts, we construct four length-matched contrastive twin benchmarks seeded from MedSafetyBench, ASQ-PHI, and a synthetic four-mandate clinical assistant policy (Generic HealthCorp). While frozen local encoders match cloud models on structured PHI detection (>= 98.3% accuracy in <= 23.5 ms), they degrade markedly on semantic safety and symmetric-blocklist prompts. However, end-to-end representation fine-tuning closes the multi-policy accuracy gap: a fine-tuned 335M-parameter BGE-Large classifier achieves 98.90% out-of-fold accuracy versus 99.20% for a zero-shot cloud LLM judge (exact McNemar p = 0.648, zero shared errors), 97.8%-98.2% recall, and a 0.0%-0.4% over-refusal rate in 39.0 ms (>14x faster than cloud LLM evaluation on our benchmark host). Per-policy error analysis reveals ceiling local recall on PHI (100.0%), brand (100.0%), and clinical scope (98.7%-99.3%) violations, isolating residual errors to reading-level checks (93.3%-95.3%) and motivating targeted multi-tier escalation.

</details>


### 31. Self-Evolving Beyond Human-Crafted Experience for EDA Scripting

- **Authors:** Yang Liu, Shengbo Tong, Xiyuan Chen, Shiwei Hou, Sen Yuan, Hao Wang, Yanfeng Li, Hongwen Li, Yiming Zhu, Zhuolun He, Wenjian Yu
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26912v1](http://arxiv.org/abs/2611.26912v1)
- **PDF:** [https://arxiv.org/pdf/2611.26912v1](https://arxiv.org/pdf/2611.26912v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The growing complexity of electronic systems demands efficient design flows, yet EDA scripting remains a bottleneck: proprietary APIs are sparsely documented, and errors often appear as silent failures or cryptic exceptions. Hand-crafted knowledge helps but is difficult to maintain as toolchains evolve. We present ZhuLong-SE (Self-Evolution), an execution-grounded LLM agent that learns reusable knowledge from prior task traces. Building on ZhuLong, it enhances the task-level harness with API retrieval, documentation responses, isolated sandbox execution, and static checking, then adds governed cross-task self-evolution. Beyond solving individual tasks, ZhuLong-SE distills past execution traces into a three-tier memory store governed by ground-truth anchoring, disconfirmation filtering, held-out rollback, and anti-leakage retrieval. On the 158-task EDA-Eval-PyAether benchmark, the full task-level harness, with self-evolution disabled, achieves 92.4% pass@1 and outperforms ZhuLong on all five tested LLM backbones. On a harder instance-disjoint test set, self-evolution from the bare configuration surpasses a human-crafted-experience baseline by 2.5 percentage points (80.0% vs. 77.5% pass@1).

</details>


### 32. AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress

- **Authors:** Congyuan Yu, Runping Tian
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26910v1](http://arxiv.org/abs/2611.26910v1)
- **PDF:** [https://arxiv.org/pdf/2611.26910v1](https://arxiv.org/pdf/2611.26910v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied world cannot be read from one measure. Existing benchmarks measure task progress, world-knowledge question answering (QA), and episodic memory, but a correct answer does not show that the agent ever observed the evidence for it, and progress does not show what the agent learned. We introduce AstronautBench, which measures one agent's self-improvement through three views on the same run: what it knows, whether its own evidence supports that knowledge, and how far it gets in the world. It is built on the game Outer Wilds, where each episode is a 22-minute loop after which the world resets, only the agent's knowledge carries over, and progress is gated by knowledge. After every episode, we measure the places reached and ship-log rumor facts revealed, the correctness of answers to 164 questions about the world, and whether each answer is supported by the frames and position the agent cites from its own recorded play. Two LLM judges from different model families check every answer. In eight-episode baselines with GPT-6.1 Sol and Gemini 4 Argon planners, which act through a learned controller or their own gamepad inputs, the three views do not move together, so any one of them alone gives an incomplete picture of whether the agent is improving. The GPT-6.1 Sol agent's correct answers grow from 14.6% to 26.8% of all questions, but at episode 8 only 59 to 68% of them are supported by its cited evidence. It reveals no new rumor facts after episode 3, while the places it reaches and its memory keep growing. More than half of the answers that become correct after episode 3 cite only evidence from earlier episodes.

</details>


### 33. ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization

- **Authors:** Trupti Mohanty, Ming Du, Mitchell A. Wood, Brad L. Boyce, Remi Dingreville, Mathew J. Cherukara
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26782v1](http://arxiv.org/abs/2611.26782v1)
- **PDF:** [https://arxiv.org/pdf/2611.26782v1](https://arxiv.org/pdf/2611.26782v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Molecular dynamics (MD) simulation resolves atomic-scale motion and predicts the structural, mechanical, and dynamic properties of materials, making it cen- tral to materials design and discovery. Yet an MD study requires an expert-driven workflow: designing the simulation, writing reliable input scripts, executing them, and analyzing the results with separate tools. Here we present ChatAtom, a multi-agent large language model system that translates a natural-language request into a complete MD workflow without the user writing input scripts or analysis code. Each agent has a defined responsibility within the workflow. An orchestrator plans the study; the LAMMPS and OVITO agents each use a generator-reviewer pair to prepare and review simulation and visualization scripts before execution; a high-performance computing agent dispatches jobs to remote resources; and an analysis agent interprets the completed run. The work- flow is accessible through a browser interface that streams thermodynamic data and rendered frames during local execution, allowing users to follow the simu- lation as it progresses. The architecture also supports new capabilities through loadable skills without modifying the agents, enabling autonomous hypothesis generation and testing. We evaluate ChatAtom through script-generation bench- marks, an end-to-end study of crack propagation, and a closed-loop campaign. By bringing script generation, execution, visualization, and analysis into one reviewed and observable pipeline, ChatAtom lowers the barrier to conducting MD studies and broadens access to advanced simulation workflows.

</details>


### 34. Self-verifiable LLM-driven science and why it needs human researchers

- **Authors:** Michael G. Medvedev, Nikolai V. Krivoshchapov, Stepan N. Ostarkov
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26754v1](http://arxiv.org/abs/2611.26754v1)
- **PDF:** [https://arxiv.org/pdf/2611.26754v1](https://arxiv.org/pdf/2611.26754v1)
- **Categories:** physics.chem-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language models are now used throughout all sciences - for reading literature, extracting numbers from tables and spectra, analyzing data, drafting conclusions - and their answers arrive in the same polished confident tone whether they are right or wrong, so a result has to be re-derived by a human researcher before it can be relied on. The cost of that re-checking, not the ability to generate results, is what currently limits AI-assisted research. In the field of mathematics, this problem is solved by proof assistants like Lean 4 and Coq that let any formal statement and its proof be written down and checked - a perfect match for LLMs, which are now actively used to search for proofs with every step automatically validated, rather than relying on a human to judge the result. In this paper, we propose an extension of this approach to non-mathematical sciences. We describe an AI agent harness that aims to make LLM's scientific reasoning verifiable: the starting assumptions are proposed by LLM and reviewed by a human, and everything built on top of them is checked by a machine with Lean 4. We illustrate how this mechanism works in practice on several examples and our results show that scientific arguments in these tasks can be expressed as formal proofs from explicit assumptions, including experimental results, known theoretical statements, and additional assumptions, produced by the agent. We suggest that this approach could change how scientific research is conducted across all sciences.

</details>


### 35. PlayCraft: Designing Engaging Games from Agent Play Experience

- **Authors:** Weihao Cheng
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26624v1](http://arxiv.org/abs/2611.26624v1)
- **PDF:** [https://arxiv.org/pdf/2611.26624v1](https://arxiv.org/pdf/2611.26624v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.

</details>


### 36. Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)

- **Authors:** Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26553v1](http://arxiv.org/abs/2611.26553v1)
- **PDF:** [https://arxiv.org/pdf/2611.26553v1](https://arxiv.org/pdf/2611.26553v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.

</details>


### 37. Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models

- **Authors:** Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26531v1](http://arxiv.org/abs/2611.26531v1)
- **PDF:** [https://arxiv.org/pdf/2611.26531v1](https://arxiv.org/pdf/2611.26531v1)
- **Categories:** cs.IR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. For each model, an LLM generates and shortlists cross features from a combinatorial candidate space, and all features are then ranked by several importance methods. Feature blending mixes these rankings into a single selection, using Pareto fronts across tasks for multi-task models. An LLM Researcher agent then tunes the feature selection in 10--25 asynchronous trials under resource caps, and a trimming step keeps the pipeline cost within budget. Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.

</details>


### 38. AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- **Authors:** Guoxin Chen, Shuang Sun, Fanzhe Meng, Xinyu Tang, Ruihua Song, Wayne Xin Zhao
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26510v2](http://arxiv.org/abs/2611.26510v2)
- **PDF:** [https://arxiv.org/pdf/2611.26510v2](https://arxiv.org/pdf/2611.26510v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a student model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B student models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42-8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs. These findings suggest that preserving skill context as part of a training demonstration can support better behavioral internalization.

</details>


### 39. Democratizing Cross-Project Knowledge for Transforming Water Governance and Climate Resilience: an Agentic AI Ecosystem

- **Authors:** Oriol Alàs, Ian Palacín, Iván Cester, Edgar Rubión
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26398v1](http://arxiv.org/abs/2611.26398v1)
- **PDF:** [https://arxiv.org/pdf/2611.26398v1](https://arxiv.org/pdf/2611.26398v1)
- **Categories:** cs.IR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

EU-funded projects produce extensive evidence in the form of deliverables, reports, and case studies. However, this knowledge is typically scattered across projects and document structures, making it difficult to locate relevant, contextual information when making decisions. This paper introduces an Agentic AI Ecosystem that consolidates heterogeneous project documentation into a domain-aware knowledge base and provides adaptive access through an agentic Retrieval-Augmented Generation pipeline. Documents from three EU-funded projects (IMPETUS, NATALIE, and InnWater) are reconstructed into hierarchical section trees and indexed with structured metadata. Retrieval is supported by two domain-specific embedding models fine-tuned on domain data (water and climate). On top of this knowledge base, a ReAct-style controller iteratively orchestrates retrieval actions by allocating retrieval budget across domain collections and accumulating evidence until a stopping criterion is met. In a retrieval benchmark over the corpus, the proposed approach improves Mean Reciprocal Rank by 26.7% (relative) compared to a single-domain embedding baseline, indicating more consistent retrieval of relevant evidence to support cross-project knowledge synthesis and climate-resilient decision-making.

</details>


### 40. How Much Should an Agent Remember? Deployment Lessons from Self-Distilled Memory for LLM Agents

- **Authors:** K. R. Jayaram, Vatche Isahagian, Aswath Vaithinathan Aravindan, Vinod Muthusamy, Punleuk Oum, Gaodan Fang, Michal Ulewicz, Gegi Thomas, Evelyn Duesterwald
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26361v1](http://arxiv.org/abs/2611.26361v1)
- **PDF:** [https://arxiv.org/pdf/2611.26361v1](https://arxiv.org/pdf/2611.26361v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents on long-horizon tasks fail in recurring, procedural ways. They mis-paginate an API, resolve the wrong entity, or answer when no answer was asked. We built a pipeline that lets an agent learn from its own history. It first mines short \emph{lessons} from the agent's own trajectories, one to three per episode. It then consolidates those lessons into a smaller set of \emph{guidelines}, where each guideline records how many lessons it merged. At inference the agent receives either all guidelines or a selected subset. The pipeline ships in the open-source altk-evolve library and is deployed in IBM's CUGA agent and watsonx Orchestrate platform. We report what we learned building, measuring, and productizing it. Our primary instrument is the AppWorld benchmark, across models spanning 40--92\% baseline task completion. The central finding is that the right amount of memory is a property of the model, not the memory. A strong model keeps improving as guidelines are added. DeepSeek-V3.2 gains +9.5 points of task completion and +16.1 points of scenario completion with its full 191-guideline set. A weak model gains less from the same full set than from a small selected subset. gpt-oss-120b starts at 39.9\% task completion. It reaches 51.2\% with all 199 of its guidelines but 55.4\% (mean of two runs) with a selected subset of about 29. Around that result we report what went wrong: a high-support guideline that backfired, provenance silently dropped during consolidation, a swallowed API error that failed every task while producing a plausible log, and a baseline confound that nearly produced a misleading comparison with a prior method. We distill these into recommendations for teams deploying agent memory.

</details>


### 41. ClosureBench: A Benchmark for Reasoning under Closure Assumptions

- **Authors:** Francesco Belardinelli, Flavio Corradini, Matteo Leonesi
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26335v1](http://arxiv.org/abs/2611.26335v1)
- **PDF:** [https://arxiv.org/pdf/2611.26335v1](https://arxiv.org/pdf/2611.26335v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usually interwoven with other reasoning demands. We present ClosureBench, a benchmark that tests whether LLMs follow the stated rules for dealing with missing information. Every base scenario is tested under OWA, CWA, and LCWA, and only the treatment of missing information changes between variants. ClosureBench provides a verified base benchmark as well as agent extensions for action choice, source scope, and updates. A model is considered correct on a base scenario only if it provides correct answers in all of its closure variants. Across 960 instances, overall accuracy can mask substantial closure mistakes. Models achieve overall accuracy from 71.18% to 99.86% across replicated runs, but their core switch accuracy, measured on the scenarios whose gold label actually changes with the contract, varies between 18.23% and 99.31%. Large discrepancies emerge under LCWA. For example, some agents choose unknown despite the prompt indicating that missing information should be treated as false. Our findings demonstrate that evaluations of AI agents should not only measure whether agents can reason over existing facts but also whether they use the appropriate assumption when information is absent.

</details>


### 42. SKILL.PNG: Learning Agent Skills in Pixel Space

- **Authors:** Maximilian Seeth, Chengzhi Martin Hu, Marie Kempkes, Paul Röttger, Leo Schwinn
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26296v2](http://arxiv.org/abs/2611.26296v2)
- **PDF:** [https://arxiv.org/pdf/2611.26296v2](https://arxiv.org/pdf/2611.26296v2)
- **Categories:** cs.LG, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are commonly specialized for new tasks and domains using skills, i.e. natural language instructions placed in their context. However, the discrete nature of textual skills prevents continuous optimization. Gradient-based approaches such as finetuning, on the other hand, are typically model-specific, preventing skill transfer across different agents. Since many agents today are built on vision-language models (VLMs), we can address these limitations by introducing Skill$.$png: a method for obtaining skill-like image inputs whose pixels are optimized with gradient descent through the vision encoder of a frozen VLM. Image skills are compatible with any VLM, and a single image can be optimized jointly for an ensemble of models. We show that Skill$.$png significantly outperforms state-of-the-art textual skills optimized using frontier LLMs in 9 of 16 settings (across 4 VLMs and 4 benchmarks) while requiring only 64 to 256 image tokens instead of roughly 900 to 2000 text tokens at inference time. Hybrid skills, i.e. text and image skills jointly optimized, further improve agent performance. Moreover, an image optimized with an ensemble of VLMs can successfully transfer across the models in the ensemble. Skill$.$png thus presents the first agent skill that can be optimized with gradient descent while retaining transfer benefits of text skills. Our code is available at: https://github.com/omseeth/skill.png

</details>


### 43. SkillBridge: Cost-Aware Diagnosis and Repair of Cross-OS Compatibility Defects in Agent Skills

- **Authors:** Anjie Xu, Zixing Wang, Yifeng Cai, Leye Wang
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26256v1](http://arxiv.org/abs/2611.26256v1)
- **PDF:** [https://arxiv.org/pdf/2611.26256v1](https://arxiv.org/pdf/2611.26256v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly reuse executable capabilities through skills, but a skill that works on one OS may fail on another because OS assumptions are spread across guide text, scripts, metadata, install contracts, and local entrypoints. Diagnosing such failures by running every skill on every OS is expensive: many executions spend model tokens, runner time, and review effort before revealing whether the failure is truly OS-related. We present SkillBridge, a contract-based workflow with three stages: static analysis, dynamic validation, and repair. SkillBridge first screens 3,270 skill-target-OS cases, covering 1,090 skills across Linux, macOS, and Windows, to find OS-sensitive contract evidence. It then runs dynamic tasks and root-cause review on selected cases to confirm whether a failure is caused by an OS assumption, and repairs the contract field that caused the failure, such as guide text, package scripts, dependencies, or platform declarations. Repair raises the reviewer-judged target-task pass rate from 30.6% to 38.4%, a gain of 7.8 percentage points. A retrospective Linux/macOS budget analysis further shows the efficiency effect: SkillBridge reaches 38 confirmed OS issues with 185 dynamic validations, where uniform random selection would require about 865 validations in expectation.

</details>


### 44. TwinLab-Bench: Evaluating AI Scientists in Agentic Twins of Real Labs

- **Authors:** Yang Wan, Linchao Zhu
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26248v1](http://arxiv.org/abs/2611.26248v1)
- **PDF:** [https://arxiv.org/pdf/2611.26248v1](https://arxiv.org/pdf/2611.26248v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly expected to act as AI scientists, which requires three increasingly open abilities: carrying out a given computational workflow correctly, choosing the next measurements from a given design space, and designing their own experiments. Existing benchmarks mainly evaluate the first two abilities, in a terminal or in a closed loop that selects from predefined candidates. Evaluating the third ability requires reliably executing an experiment that an agent designs, with readings grounded in a real laboratory. We introduce TwinLab-Bench, which evaluates AI scientists on self-designed experiments in 52 tasks from laboratories in the physical sciences, the life sciences, and engineering. The benchmark supports more than 100 experimental action types, and the agent's report is scored by comparison with a hidden answer taken from real laboratory records. Each task has its own TwinLab agent, an agent that serves as the environment and executes the experiments that the tested agent designs, reading the raw materials of the laboratory and calling calculators that are built from its records. Compared with a language model that sees only the task description, the TwinLab agent almost eliminates readings that deviate from the real records and inconsistent answers to a repeated request, and closed-book probes control for answers recalled from memory. We find that these tasks remain hard for frontier models: the strongest, Claude Fable 5.2, averages a score of only 45.0, and we conduct an empirical study of where it fails.

</details>


### 45. Sightline: Calibrated Data-Flow Summaries for LLM-Integrated Applications

- **Authors:** Zihao Xu, Yuekang Li, Ruitao Feng, Haifeng Shen
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26221v1](http://arxiv.org/abs/2611.26221v1)
- **PDF:** [https://arxiv.org/pdf/2611.26221v1](https://arxiv.org/pdf/2611.26221v1)
- **Categories:** cs.PL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Programs increasingly call large language models (LLMs), filling prompt placeholders with program values and consuming the output. Such a call crosses the boundary between natural language and programming language (NL/PL). To follow data across it, an analysis needs a data-flow summary of which placeholders the output uses, but no code describes what the model does. Analyses of these LLM-integrated applications therefore taint every output with every input, creating spurious flows, or ask a second model to label each call, which is costly. We prove, and mechanize in Lean 4, that a placeholder flows to the output of a transformer, to first order, only through the attention that reads it (no reading, no flow), and that a faint reading or sensitivity cannot certify that a placeholder does not flow. Unlike reading, the log-probability gradients and Fisher signals of existing methods vanish on confident outputs, and single-span removal fails on duplicated content. Our tool, Sightline, reads a recorded call in one forward pass, learns from labels which reads are uses, and calibrates the pruning to miss at most a chosen fraction $α$ of true flows, on average over call sites, when deployment is exchangeable with calibration. On 2,103 unseen repository families and four models, Sightline is the most accurate summary against the seven closest methods and a hidden-state probe. Calibrated at $α$ = 1%, it misses about 1% of true flows and prunes 43.9-65.6% of spurious flows, 1.6 to 2.6 times as many as the best baseline, and still 43.8-60.1% when calibrated on another collection. Through an open surrogate, it reads models treated as closed about as accurately as they read themselves, without their labels. In the information-flow control of an LLM agent, it removes about half of the labels from inputs that do not flow.

</details>


### 46. System-One RSI: Building Muscle Memory for Interactive Agents through Guided Practice

- **Authors:** Qingxu Fu, Xuanfa Jin, Ziqian Chen, Zhaoyang Liu, Bolin Ding
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26007v1](http://arxiv.org/abs/2611.26007v1)
- **PDF:** [https://arxiv.org/pdf/2611.26007v1](https://arxiv.org/pdf/2611.26007v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reasoning models provide strong multimodal task understanding but struggle with sub-second control because deliberation increases decision latency. Fast decision models can meet the response window, yet prompting and few-shot examples do not readily provide the fine-grained experience required by a new task. Inspired by coached motor learning, this paper presents System-One Recursive Self-Improvement (System-One RSI), which couples two loops. The high-frequency online inner loop is an Observe, Orient, Decide, Act (OODA) cycle: a decision model maps each visual observation and task question to structured judgments, and a decision tree converts them into timed actions without invoking a reasoning model. The offline outer loop is a recursive improvement cycle carried out by a team of reasoning agents. The team revises the decision-model prompt and decision tree, captures interaction records, derives supervision from those records, and trains or deploys updated model parameters. The improved system then returns to the environment and generates the experience for the next round, consolidating learned distinctions as external muscle memory. The framework operates with a small number of real episodes, without expert demonstrations, environment modification, sandboxing, or parallel simulation. Experiments in Snake, Zenless Zone Zero, and Black Myth: Wukong use a 27B decision model. Mean Snake score increases from 1.30 to 7.35. In an evaluated scenario of Zenless Zone Zero, median completion time decreases by 8.4%. In an evaluated combat scenario of Black Myth: Wukong, the evasive policy achieves 11 times the mean survival time of a stationary reference, while the offensive policy win rate rises from 0% to 66.7% across the evaluated configurations.

</details>


### 47. AI agents can redesign engineering parts with more than a thousand CAD parameters and nonlinear simulations

- **Authors:** Alexandra Starostina, Alexander Hermann, Mahish Guru, Kartik Bali, Roland Aydin, Christian C. Cyron
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26003v1](http://arxiv.org/abs/2611.26003v1)
- **PDF:** [https://arxiv.org/pdf/2611.26003v1](https://arxiv.org/pdf/2611.26003v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulation-driven design of real engineering components has to meet three conditions at once. It runs on few solves, since a nonlinear finite-element simulation of a 3D part takes hours; its design space has many values, the hundreds to thousands of values of the part's CAD model; and a better design often needs a redesign, coordinated changes of the part's proportions rather than local polishing of its surface. Automated optimisers meet at most two of these conditions. Classical optimisers, Bayesian or derivative-free, need a person to cut the design down to a few parameters, and on all the values they need far more solves; industrial shape optimisers move every surface node of the mesh in one solve per cycle, but only in small steps that polish rather than redesign. We ask whether a general-purpose large language model (LLM) can meet all three by joining what it knows with what the simulation shows. GPT-6 Astra edits a magnesium stent through a CAD geometry parametrisation of about 1,650 values, with a budget of 15 simulations; every proposal is built in CAD, meshed and simulated with large-deformation plasticity and contact, and the LLM reads the full results of every solve. Within that budget it lowered the objective, a high percentile of the strains in the stent's bends, by 32%; on the same budget, the industrial shape optimiser Tosca improved the original design by a tenth and then stopped improving. An earlier GPT-6 Astra design, 25% lower in the same objective, was checked in an independent, higher-fidelity model of the full deployment with crimping and damage: it was 14% less strained than the original after the full chain, and its most damaged spot began to fail later and carried 63% less damage at full expansion. LLMs can thus join their learned knowledge with simulation data to adjust more than a thousand design values and reach valid designs with real improvements.

</details>


### 48. Law at the Speed of AI: Critical Legal Infrastructure for the Machine Age: Autonomy Under Law Architecture (AULA)

- **Authors:** Natasha E Blycha, James Myint, Chen Feng, Dr Amani Soysa, Koshin Jama, Schellie-Jayne Price, Matthew Blycha
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25985v1](http://arxiv.org/abs/2611.25985v1)
- **PDF:** [https://arxiv.org/pdf/2611.25985v1](https://arxiv.org/pdf/2611.25985v1)
- **Categories:** cs.CE, cs.AI, cs.ET, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The global deployment of autonomous AI agents within and across organisations exceeds the governance infrastructure available to constrain it. Agent communication and authentication protocols, principally the Model Context Protocol and the Agent2Agent Protocol, are maturing quickly, but maturity at the protocol layer does not produce legal legibility at the governance layer. Runtime enforcement written by the deploying organisation fixes the resources an AI agent can reach, not the authority under which it acts. Legal legibility is the capacity of a legal system to recognise, interpret and regulate activity by mapping it onto legal personhood, property, rights and liabilities. Existing (analogue) legal infrastructure cannot supply it for autonomous deployment. The resulting deficit is bidirectional. It concerns the attribution of liability when an AI agent causes harm, and the allocation of rights, including data and economic rights, generated by agentic activity and by the AI agent itself as a source of value and form of property. This paper characterises that deficit as the legal attribution gap, a material and unaddressed risk to economies, organisations and citizens that is magnified in cross-organisational multi-agent deployment. The paper describes the Autonomy Under Law Architecture (AULA), in which AI systems and data assets are registered as legal objects anchored to one or more identified legal persons, governed by cryptographically tethered smart legal instruments and evaluated at runtime. Each smart legal instrument can carry a legal context clause, through which the legislation, regulation and judicial decisions in force at the time of the act are given practical and legal effect in that evaluation. Infrastructure of this kind is a precondition for the continued function of any legal, property and economic system with both human and autonomous machine stakeholders.

</details>


### 49. Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding

- **Authors:** Youssef ElNahas, Adel Ammar, Soumaya Chaffar, Wadii Boulila
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25898v1](http://arxiv.org/abs/2611.25898v1)
- **PDF:** [https://arxiv.org/pdf/2611.25898v1](https://arxiv.org/pdf/2611.25898v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demographic shortcuts can pass conventional evaluation. This critical review covers four paradigms in turn: how clinical hallucination arises and why static metrics miss it; the agentic hallucination cascade, in which multi-agent and tool-augmented systems propagate and amplify early reasoning errors; process reward modeling as step-level supervision; and neuro-symbolic grounding, in which formal logic engines, ontology reasoners, and knowledge graphs place verifiable constraints on neural output. Within their encoded domains, systems with symbolic veto layers offer guarantees that hold relative to their encoded knowledge, and they report large gains on the safety measures they use. These results come from single studies, mostly in simulated or small-sample settings, and are not directly comparable with neural baselines. Process reward models remain bounded by the statistics of their training data. We propose a conceptual framework that maps each agentic failure mode to a symbolic intervention point, and we argue that clinical AI safety depends substantially on system architecture. Because current regulation emphasizes performance and does not require verification of reasoning steps, we argue that responsible certification should also audit reasoning trajectories alongside accuracy on static benchmarks.

</details>


### 50. HabitusMem: Belief Memory over Evolving User Preferences for LLM Agents

- **Authors:** Yifan Lu, Gaoyang Guo, Wen Chen, Ziyun Zou, Jian Wu, Han Zhu, Imran Razzak
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25855v1](http://arxiv.org/abs/2611.25855v1)
- **PDF:** [https://arxiv.org/pdf/2611.25855v1](https://arxiv.org/pdf/2611.25855v1)
- **Categories:** cs.AI, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personalized LLM agents must act on a user's current preferences, which change across interactions and are rarely stated in full. Existing memory systems store and retrieve content from the interaction history and leave the agent to work out which preferences still hold and where they apply. Such content does not indicate whether a preference is still current or where it applies, so agents often act on outdated or misapplied preferences. We instead treat memory as the assistant's belief about the user. Following Bourdieu's account of habitus as durable but revisable dispositions, we model the user as a latent preference state that every interaction, including the current request, both reveals and updates. The belief summarizes what the history supports about this state, and memory consists of the individual beliefs that bear on the agent's current decision, each with its evidence, scope, and status. We implement this view in HabitusMem, a trained writer that states these beliefs as text records for a frozen agent. Across two agent families, HabitusMem achieves the best results among memory systems on both PersonaMem-v2 and VitaBench 2.0. Controlled analyses show that learned request conditioning drives the answering gain, while auxiliary training tasks improve tool use.

</details>


### 51. A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery

- **Authors:** Chenyuan Zhou, Chaoyi Huang, Zibo Wang, Zhiyuan Li, Yong-Lu Li
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25656v1](http://arxiv.org/abs/2611.25656v1)
- **PDF:** [https://arxiv.org/pdf/2611.25656v1](https://arxiv.org/pdf/2611.25656v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with a VLA policy. It treats tool affordances as hypotheses the agent can construct, test, and revise. Given teleoperated demonstrations with a few source tools, the agent reconstructs the scenes in simulation and autonomously determines task-relevant affordance features: functional regions and their key geometric properties. It develops affordance-extraction skills and refines both the features and skills through autonomous experiments in the reconstructed scenes. Validated extraction skills accumulate in a reusable skill library for unseen tools. Finally, A$^2$-VLA uses encoded functional-region features as conditioning inputs to a $π_{0.5}$ backbone during training and inference. Evaluation examines affordance reliability in reconstructed scenes and real-robot task success on unseen tools. Our method achieves 86.1% success in simulated cross-tool trajectory retargeting based on affordances. On three real-robot tool-use tasks, A$^2$-VLA improves task success by 30.7 percentage points over $π_{0.5}$.

</details>


### 52. Adding One More Agent: How AI Team Size and Formation Shape Productivity and Diversity in Human-AI Brainstorming Teams

- **Authors:** Rong-Ching Chang, Hao-Chuan Wang
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.26663v1](http://arxiv.org/abs/2611.26663v1)
- **PDF:** [https://arxiv.org/pdf/2611.26663v1](https://arxiv.org/pdf/2611.26663v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative AI has improved individual productivity, but whether adding a plurality of AI partners helps or hurts remains open. We crossed AI partnership (one versus two) with behavioral formation (calibrated to average human behavior versus customized by the participant) in a brainstorming experiment ($N$=168) with human-human dyads as reference. Two-AI rooms posted more ideas to the shared board, but human-authored ideas dropped substantially. With one AI partner, formation mattered: humans paired with an average-calibrated AI posted more than any other condition. With two, this effect vanished. Humans continued talking but converted fewer ideas into board posts. AI social talk predicted more human posts, while AI posting volume predicted fewer. AI presence increased global diversity of human-authored ideas, but only a second AI increased within-session differentiation. The number of AI partners and their formation can reshape what the human contributes; single-agent results do not generalize to multi-agent teams.

</details>


### 53. Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents

- **Authors:** Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha, Aditya Kanade, Krishnamurthy Dj Dvijotham
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25599v1](http://arxiv.org/abs/2611.25599v1)
- **PDF:** [https://arxiv.org/pdf/2611.25599v1](https://arxiv.org/pdf/2611.25599v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. However, these actions can result in unauthorized network requests or persistent, malicious changes to the user's file system, processes, or privileges. Existing defense mechanisms rely on either LLM-based monitors, which lack provable safety guarantees, or stateless policy enforcement layers, which miss multi-step data flows and execution side-effects unmodeled by the policy language (e.g., network calls initiated inside a Python script). We introduce Tether, a framework for runtime enforcement of stateful security policies over the observed side-effects of an agent's actions. Tether executes each proposed action in an ephemeral, isolated sandbox, inferring abstract action semantics from observed system calls. Tether then enforces stateful policies over these inferred semantics, permitting actions to proceed only if they comply with the policy. Policies and action semantics are defined in an embedded DSL in Lean 4 capable of expressing diverse constraints, including information flow control (IFC), access control, and network security policies. Because actions can propagate labels from sources to destinations, a single rule can enforce fine-grained IFC policies across multi-step execution flows of arbitrary length. Expressing policies in Lean enables formal verification that they satisfy global security invariants (e.g., preventing network access after reading a sensitive file). We evaluate Tether on realistic coding-agent benchmarks across both benign and adversarial trajectories. With a single policy shared across all tasks, Tether blocks 100% of in-scope attacks while maintaining a benign false-positive rate under 5%.

</details>


### 54. DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents

- **Authors:** Licheng Pan, Yuzhou Chen, Zhixuan Chu, Yichen Sun, Han Zheng, Zhiyu Wang, Hao Wang, Yan Wang, Bingyu Zhu, Haiwen Hong, Longtao Huang, Kui Ren
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25583v1](http://arxiv.org/abs/2611.25583v1)
- **PDF:** [https://arxiv.org/pdf/2611.25583v1](https://arxiv.org/pdf/2611.25583v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attribution, as perplexity or retrieval relevance alone cannot determine which retrieved memory would change agent behavior if neutralized; (2) Counterfactual attribution is prohibitively expensive for online detection, as it requires replaying downstream agent and tool execution for each candidate memory, exceeding real-time serving budgets. To address these challenges, we propose DriftGuard, a two-stage framework that decouples offline causal supervision from online estimation. Specifically, DriftGuard first constructs causal supervision through repeated paired counterfactual replays, continuing the original and single-memory neutralized trajectory suffixes from a shared pre-action state. The resulting annotations are aggregated by component-wise majority voting into a memory drift score (MDS) that captures action change, attack removal, violation removal, and task recovery. Guided by this supervision, DriftGuard then learns an online risk model that estimates MDS from pre-action information and flags drift-inducing memories via its maximum component risk, without online counterfactual rollouts. Extensive experiments demonstrate that DriftGuard accurately identifies drift-inducing memories and enables efficient online defense. Code is available at https://anonymous.4open.science/r/DriftGuard-7F0B.

</details>


### 55. AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development

- **Authors:** Hang Zhang, Yuzhi Pan, Ziyao Zhong, Chaokun Wang, Shuo Cao, Zeyu Huang, Yue Xue, Fang Niu, Bofan Xie, Guanchen Ge, Zecheng Li, Leqi Zheng, Ziyang Liu, Wei Wang, Miao Gu
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25582v1](http://arxiv.org/abs/2611.25582v1)
- **PDF:** [https://arxiv.org/pdf/2611.25582v1](https://arxiv.org/pdf/2611.25582v1)
- **Categories:** cs.CL, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.

</details>


### 56. LM-based Personalized Travel Planner

- **Authors:** Amandi Nimasha, Oshadha Wijerathne, Dushan Fernando, Nisansa de Silva, Srinath Perera
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25531v1](http://arxiv.org/abs/2611.25531v1)
- **PDF:** [https://arxiv.org/pdf/2611.25531v1](https://arxiv.org/pdf/2611.25531v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective travel planning requires handling multiple information sources, managing constraints, and tailoring recommendations to user preferences. While LLMs have introduced dynamic, context-aware decision-making, single-agent models often struggle with complex multi-step reasoning, constraint adherence, and modular execution. To overcome these limitations, we propose a hierarchical multi-agent framework where a supervising chatbot agent coordinates specialized agents for schedule validation, user query formulation, real-time data retrieval, and constraint-aware itinerary generation. By integrating LLM reasoning, external APIs, and iterative refinement mechanisms based on a deterministic, multi-dimensional scoring framework, our approach ensures adaptability, efficiency, and personalization. Evaluations on the well-known TravelPlanner benchmark demonstrate improvements in Budget Constraint planning by 10\%, wider constraints set-based planning by 25\%, and personalized planning results by 45\%. compared to the ReAct baseline. Our code is available at https://github.com/nimashaklaa/TravelPlanner_Research

</details>


### 57. ChainAgent: Automated Chainable Vulnerability Discovery in PHP Web Applications

- **Authors:** Xinyi Wang, Yeting Li, Shizhe Cui, Jiaming Guo, Qin Mai, Yecheng Sun, Hengyu Yang, Yujie Sun, Huina Chao, Yang Xiao, Feng Li, Wei Huo
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25412v1](http://arxiv.org/abs/2611.25412v1)
- **PDF:** [https://arxiv.org/pdf/2611.25412v1](https://arxiv.org/pdf/2611.25412v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

High-impact attacks on PHP web applications often chain limited-capability vulnerabilities with other flaws or intended behaviors. Discovering these chains requires identifying flaws and the dependencies enabling capability composition. Existing vulnerability discovery techniques analyze flaws in isolation, while attack planning assumes known components. This separation makes it difficult to discover previously unknown components whose security relevance becomes apparent only through their potential roles in an exploit chain.
  We present ChainAgent, a goal-directed LLM-agent framework that jointly discovers exploit-chain components and their capability dependencies in source code. Guided by an empirical study of 386 real-world web exploit chains, ChainAgent represents vulnerabilities and functional gadgets--intended program behaviors that can be repurposed in attacks--through preconditions and capabilities over security-relevant objects. Instead of discovering vulnerabilities first and constructing attack paths afterward, ChainAgent uses an evolving exploit graph to guide source-code inspection. It searches backward from unmet preconditions for capability producers and forward from discovered capabilities for functional gadgets that consume or amplify them. Object-centered chaining knowledge from our empirical study directs searches toward promising vulnerability classes, functional operations, and object accesses.
  We evaluate ChainAgent against Codex, a general-purpose coding agent, on 15 PHP applications across three shared LLM backends. ChainAgent achieves 42.02%--44.63% recall for goal-reaching components and recovers up to 4.4 times as many correct goal-reaching dependency edges as Codex. An additional evaluation of 30 real-world PHP applications identifies 20 vulnerabilities and 13 exploit chains, nine of which achieve remote code execution (RCE).

</details>


### 58. Toward a Science of AI Agent Societies

- **Authors:** Geon Lee, Fanchen Bu, Soo Yong Lee, Sunwoo Kim, Kijung Shin
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25404v1](http://arxiv.org/abs/2611.25404v1)
- **PDF:** [https://arxiv.org/pdf/2611.25404v1](https://arxiv.org/pdf/2611.25404v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are rapidly evolving from isolated personal assistants into networked actors that interact with one another at scale. We envision the emergence of AI agent societies, with their own social and economic dynamics, as a new research frontier. We argue that AI agent societies should be studied as a distinct object of inquiry: neither simply larger collections of individual agents nor merely simulations of human society. To formalize this perspective, we propose four core properties that a valid AI agent society should satisfy: individualized objectives, rules and governance, autonomy, and scale and complexity. Building on this framework, we identify four classes of societal behaviors worth studying in AI agent societies: economic behaviors, behaviors under conflict-of-interest, unsafe and unethical behaviors, and system-level behaviors. We then outline key technical challenges--including property parameterization, parameter balancing, and robust implementation--and argue that progress on these challenges could enable scientifically informative and practically useful models of AI agent societies. Finally, we revisit existing multi-agent systems through the lens of the proposed core properties, show that they instantiate only subsets of them, and discuss implications for platform design, evaluation, and governance.

</details>


### 59. Beyond Weight Updates: Evolving Agent Harnesses for Domain Specialization

- **Authors:** BoHao Chen
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25380v1](http://arxiv.org/abs/2611.25380v1)
- **PDF:** [https://arxiv.org/pdf/2611.25380v1](https://arxiv.org/pdf/2611.25380v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Domain specialization of LLM agents is usually framed as a weight-update problem: collect trajectories, run reinforcement learning (RL) or supervised fine-tuning (SFT), and deploy a new checkpoint. We study a complementary axis: evolving the \textbf{agent harness}---the system prompt, tool schemas, skill library, and planning scaffolding---while keeping the policy frozen. We cast harness evolution as an RL-style outer loop and instantiate it with GEPA, a reflective evolutionary optimizer. The resulting harness adapters require no GPU training, are loadable per vertical domain, and compose with weight-based RL. Experiments with Codev, a Claude Code-style coding agent, on SWE-bench Verified, OfficeBench, and Terminal-Bench show a consistent pattern: weight updates give the strongest single-path gains, harness evolution recovers most of those gains at a small fraction of the compute, and combining both paths is best overall. We also analyze a failure mode of SFT-based specialization---shortened reasoning chains and increased truncation---and argue that harness adapters avoid it by construction. Our results position harness evolution as a practical, non-destructive complement to weight updates for vertical agents.

</details>


### 60. AppSci-Bench: Can LLMs Build AI Agents and Make Them Better?

- **Authors:** Sanjari Srivastava, Manpreet Kaur, Cheng Chang, Sofía Ramós Anton, Oumaima Essamadi, Rishu Garg, Alejandro Lavale Jiménez, Marcos Caballero Yus, Mercedes García Martínez, Peng Qi
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25360v1](http://arxiv.org/abs/2611.25360v1)
- **PDF:** [https://arxiv.org/pdf/2611.25360v1](https://arxiv.org/pdf/2611.25360v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used not only to power AI agents but also to build them. While many benchmarks assess the quality of LLM- powered agents, few ascertain how good LLMs are at building them. To this end, we introduce AppSci-Bench, where we construct a setting akin to how human Applied Scientists build agents for businesses - through eliciting task requirements from stakeholders, exploring the business's infrastructure, and scientifically improve the target agent by designing experiments and internal benchmarks. AppSci-Bench features seven realistic domains - five new ones (Slides Generation, Order-to-Cash, Compliance Review, Customer Call Insights, and CRM Insights) and two domains recast from tau3-bench (Yao et al., 2024; Shi et al., 2026b)(Airline and Banking) - each with a held-out evaluation suite customized for that task. We evaluate seven frontier models and find AppSci-Bench challenging: the best model, Claude Opus 5.0, only reaches a mean-minimum score of 59.1% across 3 build attempts; other models do significantly worse. Models struggle with eliciting task requirements (only 65% for Opus 5.0), build representative internal evaluations (models saturate their own evaluation 65% of the time but fail to solve the held-out task), presenting challenges for future research. The benchmark code is available here: https://github.com/sanjari-orb/appsci-bench.

</details>


### 61. From FIPS to FPGA with LLM Agents: Measuring What Tests and Reviews Miss in Post-Quantum Cryptographic Hardware

- **Authors:** Jungmin Park, Eunha Kim, Wooseop Kim, Seongjoon Cho, Byungho Cha
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25339v1](http://arxiv.org/abs/2611.25339v1)
- **PDF:** [https://arxiv.org/pdf/2611.25339v1](https://arxiv.org/pdf/2611.25339v1)
- **Categories:** cs.CR, cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents increasingly generate RTL alongside the tests and reviews that validate it, self-generated evidence is a weak foundation for trustworthy hardware. We present our seven-stage verification-gated workflow, evolved during a post-quantum design port, in which a gate counts only if shown able to fail on negative controls and fault mutants, and reviewer agents audit work before commit. We then audit this evidence with tool-selected netlist mutants, flaw replays, and formal checks. The flow ported an ML-KEM-768/ML-DSA-65 accelerator to a 300 MHz Zynq UltraScale+ key-custody card: all six operations are byte-exact on the board, and it passes all 85 interface-applicable NIST ACVP cases (of 285) and 484 ML-DSA known answers. However, passing module tests overstate the verification strength. Across three RTL modules, existing simulation gates kill only 76% of 399 tool-selected netlist mutants; specification-derived tests guided by the survivors raise the fresh-draw decapsulation kill rate from 48% to 74%. In pre-registered single-model replays on flaws invisible to known-answer tests, undirected whole-design review catches two verifier flaws in only 3/6 and 1/6 sessions, whereas module-scoped review catches every known flaw in all 54 sessions. Even scoped review detects planted key-custody flaws in only 3/20 sessions, whereas formal checks (one added for the replay) flag every one. In this study, trustworthy agentic hardware needed author-independent mutants for test gates, module-level scoping for LLM review, and formal checks for custody invariants.

</details>


### 62. ReLay: Bidirectional Layout-Code Translation and Library Evolution for Reusable and Process-Portable Analog Design

- **Authors:** Minxing Chu, Quan Cheng, Anhang Li, Martins Atilla, Junyi Luo, Xinting Jiang, Ruichen Qi, Mehdi Saligane
- **Published:** 2026-11-19
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25328v1](http://arxiv.org/abs/2611.25328v1)
- **PDF:** [https://arxiv.org/pdf/2611.25328v1](https://arxiv.org/pdf/2611.25328v1)
- **Categories:** cs.AR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analog layout generators provide a programmable interface for design reuse and process migration, but their coverage is limited by handcrafted libraries. The designer knowledge embedded in complete layouts remains implicit in their geometry, making it difficult to capture in reusable generator libraries. We present ReLay, a bidirectional layout-code framework that recovers generator programs from existing layouts, enabling cross-PDK portability and parametric resizing of existing designs. Constructions that recur across recovered programs are promoted to library functions, so the library evolves as layouts accumulate. We also introduce the first layout-code benchmark: 1,050 hand-drawn layouts from 27 circuit families across three open-source PDKs, ranging from primitive cells to full chips. Learned functions account for 53-66% of layout-building calls in held-out layouts, demonstrating reuse beyond the learning corpus. Frontier LLM agents use ReLay to produce new layouts at 64-77% lower API cost per completed task than direct geometry generation, with comparable completion rates and electrical quality.

</details>


### 63. Moving Generality from Model to Modeler: LLM Agents for PHM on a Deployment-Style Benchmark

- **Authors:** Zhenling Chen, Zhiguo Zeng, Anne Barros
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25252v1](http://arxiv.org/abs/2611.25252v1)
- **PDF:** [https://arxiv.org/pdf/2611.25252v1](https://arxiv.org/pdf/2611.25252v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents built on large language models (LLMs) now help develop many models published as general solutions. Should generality instead reside in the agent that builds a model for each new task? We examine this question in prognostics and health management (PHM), where every model must work on unseen equipment. Our deployment-style benchmark, NextUnit-Bench, covers 24 public datasets split into 58 folds that hold out units or operating conditions; each agent has two hours to deliver an executable predictor, then run on the hidden units. First, frontier agents outperform AutoML, which reaches less than half the best agent's score, and faithful implementations of published methods on four datasets, of which only 6 of 30 beat the strongest agent's own design; published accuracies, where reproducible, rest on the papers' own conventions, and a single convention, capping the remaining life of test engines, can halve the reported error. Second, the agents' advantage is a design made on each machine's data; once made, a plain-text plan of a few hundred words carries most of the gap between two frontier agents, and given a weaker agent's plan, the strongest agent falls to that agent's level, often to identical predictions. Before touching the data, however, it matters little whose plan an agent carries out, and domain toolkits appear to help neither: what sets the strongest apart is how much it learns from the data. Third, such designs reach only implementers that can execute them: given the strongest agent's designs, a locally deployable open-weight model delivers half as often, even when they are lightened, and scores no higher than without them. Generality, we argue, is not disappearing but moving, from the model to the modeler.

</details>


### 64. MKA: Evaluating Multimodal Knowledge Agents on end-to-end professional tasks

- **Authors:** Anima Singh, Suhas Yogin, Weicheng Kuo, Ivor Rendulic, Ivan Jurin, Antoine Yang, Oran Kelly, Rohan Doshi, Hammad Ayyubi, Ioana Bica, Sergi Caelles, Matthew Conniff, Dan Graur, Anastasija Ilić, Ahmet Iscen, Chao Jia, Tomasz Kępa, Chunyuan Li, Noah Ó Donnaile, Filip Pavetic, Goran Petrovic, Khalid Salama, Zhicheng Wang, Polina Zablotskaia, Yiqian Zhang, Ming Zhao, Benjamin Caine, Mario Lučić, Melvin Johnson, Radu Soricut, Jean-Baptiste Alayrac
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25228v1](http://arxiv.org/abs/2611.25228v1)
- **PDF:** [https://arxiv.org/pdf/2611.25228v1](https://arxiv.org/pdf/2611.25228v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce the Multimodal Knowledge Agent (MKA) benchmark, which measures how well autonomous agents perform end-to-end professional knowledge work that depends on visual understanding. Each task requires an agent to extract and combine information from multiple visually dense files, such as CAD blueprints, electronics schematics, radiographs, complex charts and geospatial maps, and to produce a standalone deliverable in .xlsx, .pptx, .pdf, .docx, .html or .png format. Existing benchmarks leave this capability largely untested: removing image-viewing tools leaves Gemini 4 Carbon's score on GDPval unchanged, and single-format evaluations such as GDP$.$pdf and GDP$.$xlsx do not require reasoning across files or modalities. MKA contains 200 tasks across 10 economic sectors. Deliverables are graded against expert-weighted rubrics by a sandboxed agentic autorater that agrees with human domain experts on 96.2% of criterion judgments in our expert-graded study (Cohen's $κ= 0.91$), scored by weighted satisfaction rate (WSR) overall and on frontier criteria unsaturated by prior-generation models (Climb-WSR). Across the frontier models we evaluate (Gemini 4 Carbon, Claude Fable 5.2, Claude Opus 5.5, and GPT-6 Astra), Claude Fable 5.2 (56.6% Climb-WSR, 73.3% Overall WSR) and Gemini 4 Carbon (54.3% Climb-WSR, 71.9% Overall WSR) achieve the highest scores, while Carbon uses $5.7\times$ fewer tokens. Even for the strongest models, Climb-WSR remains below 57%, leaving substantial headroom for multimodal agents.

</details>


### 65. From FAIR to AWARE: Data Readiness for Agentic AI in the Earth Sciences

- **Authors:** Ivan Kuznetsov, Dmitrii Pantiukhin, Sonja Hänzelmann, Fabian Wachsmann, Jonas Sølvsteen, Daniel Wiesmann, Thomas Jung, Nikolay Koldunov
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25209v1](http://arxiv.org/abs/2611.25209v1)
- **PDF:** [https://arxiv.org/pdf/2611.25209v1](https://arxiv.org/pdf/2611.25209v1)
- **Categories:** physics.ao-ph, cs.AI, physics.geo-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence in the Earth sciences is beginning to act: prototype agents already search archives, run simulations and draft analyses. Scientific data were curated for researchers who bring expert judgement; an autonomous agent cannot be assumed to supply it. Data can satisfy the FAIR principles and still mislead a machine acting alone. We propose that Earth-science data become AWARE (Actionable, Well-described, Auditable, Recipe-equipped, Epistemically labelled), an agent-specific requirements layer that extends FAIR, within a three-part agenda: AWARE data, bounded tools, layered validation. The ingredients exist across community infrastructure. We outline a staged, measurable path to adoption, intended to reduce silent error.

</details>


### 66. An AI-Powered Multiverse Analysis of Empirical Finance Research: Evidence from Reused Natural Experiments

- **Authors:** Ruijiang Gao, Steven Chong Xiao
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25184v1](http://arxiv.org/abs/2611.25184v1)
- **PDF:** [https://arxiv.org/pdf/2611.25184v1](https://arxiv.org/pdf/2611.25184v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Empirical finance research often reuses natural experiments to study other outcomes, raising concerns about multiple testing and publication bias. We use AI agents to run a multiverse analysis of 324 papers that reuse 13 natural experiments. The agents rebuild the data, reproduce each paper's main estimate and re-estimate it across grids totaling 62,409 estimated defensible specifications. Based on the reproductions and the specification grids, we develop measures of empirical robustness. We reproduce 42% of the main estimates of claims with a signed effect under the papers' own specifications. Across all defensible specifications, on average 25% keep the published sign and have $p < 0.10$. Across experiments, claims based on regression discontinuity are more robust than difference-in-differences claims. Within experiments, claims about first-order effects, claims with larger published $t$-statistics, claims whose authors' data or code we find, claims in top journals, and claims with fewer earlier papers on the same experiment are more robust. Claims on experiments that more papers reuse are not less robust on average. Our findings quantify how much published claims depend on analysis choices, thereby showing that large-scale multiverse analysis becomes feasible with agentic coding.

</details>


### 67. GridAnchor: Specialized Multi-Agent AI for Safeguarding Autonomous Energy Systems Against Cyber-Physical Hallucinations

- **Authors:** Abderaouf Bahi, Hasan Masrur
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25158v1](http://arxiv.org/abs/2611.25158v1)
- **PDF:** [https://arxiv.org/pdf/2611.25158v1](https://arxiv.org/pdf/2611.25158v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous energy systems increasingly chain specialized learned agents, such as a forecaster, a state estimator and a dispatcher that may be a language model. These agents can emit confident outputs that contradict physics, and downstream agents may act on them. We define such cyber-physical hallucinations and their cascades, organize them in eight types, and build CPH-Bench, a generator of labeled episodes on SimBench feeders. We propose GridAnchor, a verification layer whose Physics-Residual Graph Transformer scores every claim from residuals between the claims, the measurements and a linearized grid model. Mondrian conformal p-values with the Benjamini-Hochberg procedure turn the scores into decisions, a root head attributes cascades, and a quadratic program repairs unsafe actions with a voltage margin calibrated at repaired steps. On a simulated rural medium-voltage feeder, GridAnchor reaches a message-level area under the precision-recall curve of 0.846, against 0.837 for the strongest of six baselines, a difference within the confidence interval. It leads on estimates and actions, whereas a self-consistency check that knows the label tolerances reaches 0.874 by leading on forecasts. The false-alarm rate stays within 0.17 percentage points of the nominal level on steps without injected hallucinations. In closed loop, GridAnchor leaves no bus outside the voltage band on the test days, against 0.0700% of the bus-steps without protection, and simpler detectors with the same mitigation come close. Stale but coherent messages and single-bus forecast errors remain mostly undetected.

</details>


### 68. EverydayBench: Evaluating Satisfactory Completion of Live User-Facing Digital Work

- **Authors:** Fangrui Huang, Bingyang Wang, Chuhan Li, Yijiang Li, Arpandeep Khatua, Austin Shen, Riki R Z Choi, Cuiyuanxiu Chen, Jin Huang, Zachary Robertson, Kate Lin, Akshay Paruchuri, Sijun Tan, Xin Liu, Zhengmin Ni, Sanmi Koyejo, Ehsan Adeli
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25146v1](http://arxiv.org/abs/2611.25146v1)
- **PDF:** [https://arxiv.org/pdf/2611.25146v1](https://arxiv.org/pdf/2611.25146v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Everyday digital tasks, from selecting products and planning trips to conducting research and creating artifacts, require AI agents to deliver useful outcomes rather than merely retrieve web information. Yet evaluating these outcomes on the live web is challenging, as a single request may admit multiple valid results, and changing web information can alter which results remain valid over time. Although existing benchmarks address aspects of this setting, they do not fully integrate predefined success criteria, current evidence verification, and deliverable-quality assessment for agent-selected outcomes. To address this gap, we introduce EverydayBench, a benchmark of 77 human-authored tasks spanning eight domains of everyday life and work. Each task specifies success criteria before execution without prescribing an answer or workflow, allowing agents to select their own outcomes. To evaluate submissions under fixed success criteria, EverydayBench combines (1) deterministic checks of explicit constraints, (2) verification of claims against agent-cited webpages retrieved at evaluation time, and (3) rubric-based assessment of final deliverable quality. We further validate the protocol through human judgments, repeated scoring under fixed evidence, and controlled grounding failures. Across 23 reported agent-model configurations, Claude Opus 5.5 and Claude Fable 5.1 tie for the highest strict pass rate at 54.55%; a controlled GPT-6 Sol effort sweep ranges from 29.87% at low effort to 45.45% at max effort. Reliability varies substantially by task type: GPT-5.6 Sol leads lookup, Fable 5.1 leads planning, Opus 5.5 and Fable 5.1 tie on comparison, and GPT-6 Astra and Sonnet 5.5 tie on customized deliverables. Together, these findings highlight the difficulty of delivering complete, well-supported, and usable outcomes for everyday user requests.

</details>


### 69. Forget Freely, Grep Later: Lossless, Index-Free Memory for Long-Horizon LLM Agents

- **Authors:** Ziyan Yang, Taiwei Shi, Jieyu Zhao
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25123v1](http://arxiv.org/abs/2611.25123v1)
- **PDF:** [https://arxiv.org/pdf/2611.25123v1](https://arxiv.org/pdf/2611.25123v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents often exceed their context windows, forcing them to discard information that may be needed later. Existing context management strategies rely on summarization, masking, or structured memory, requiring decisions about what to preserve or how to retrieve it before future needs are known. However, these methods can introduce lossy compression, potentially discarding details needed for future tasks. To address this limitation, we introduce GrepMem, a simple, lossless, and index-free memory mechanism built on two components: an append-only plain-text log of the agent's complete history and a regular-expression search tool for on-demand recall. Unlike structured memory systems, GrepMem requires no embeddings, retrieval index, memory extraction, or additional models. We train Qwen3.5-9B with reinforcement learning under five context management strategies and evaluate on multi-question research sessions, long-stream recall, and agent-trajectory question answering. GrepMem achieves 95-97% accuracy on ContextBench, versus at most 21% for lossy baselines, and outperforms SUPO's summarization by 8.8 percentage points on BCP-Multi. GrepMem scales effectively to increasingly long input streams while remaining on the accuracy-token-cost Pareto frontier across all five evaluation tasks. Our results show that a plain-text log and grep provide a simple but competitive approach to long-horizon agent memory, without requiring complex structured memory infrastructure.

</details>


### 70. MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

- **Authors:** Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu, Yu-Cheng Chou, Johan Bjorck, Linxi "Jim" Fan, Jan Kautz, Yu-Chiang Frank Wang, Zhiding Yu, Hengshuang Zhao, Zhiqi Li
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25105v2](http://arxiv.org/abs/2611.25105v2)
- **PDF:** [https://arxiv.org/pdf/2611.25105v2](https://arxiv.org/pdf/2611.25105v2)
- **Categories:** cs.RO, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the highest success on all three real-robot tasks (laundry-bag collection, bath-towel folding, and umbrella handover), with 67.8% mean success, 18.9 percentage points above MA-VLA trained on the same demonstrations and cameras. In simulation, MAWAM reaches 90.3% mean success on eight tasks with teams of up to four arms. Ablations show that cross-agent attention and team-stage future-video supervision both improve coordinated control: without attention, a four-arm relay falls from 95.0% to 39.0%, and without this supervision, Place Food falls from 78.0% to 47.0%.

</details>


### 71. FinVeriQA: Financial Research Agents for Question Answering: Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification

- **Authors:** Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan, Gunanidhi Ramakrishnan, Nathan Howland
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25071v1](http://arxiv.org/abs/2611.25071v1)
- **PDF:** [https://arxiv.org/pdf/2611.25071v1](https://arxiv.org/pdf/2611.25071v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) write fluent financial analyses but miscompute ratios, recall stale prices, and route questions to the wrong tool with high confidence. We ask which component should do each job in a financial question-answering assistant, and study it with FinVeriQA, an open-source multi-agent research prototype over SEC filings and live market data: a compact typed-decision model (Laya) routes each question and screens out advice requests, Python computes every number, retrieval and tools fetch evidence, Mistral-7B writes a cited answer, a code validator checks that cited IDs exist and that numbers match computed notes, and a Model Context Protocol (MCP) server exposes the pipeline. In live experiments, Laya routed better than Mistral-7B (0.85 vs. 0.52; overall 0.86 vs. 0.68, McNemar p = 0.0003); a 12B Mistral decided no better, and DeepSeek-R1-8B decided better (0.79 vs. 0.68, p = 0.0192) but about 9.9 times more slowly. Mistral-7B computed 29% of 100 financial calculations correctly against 100% for Python, a live quote cut price error from 210% to 0.00%, and hybrid retrieval reached 76% Hit@5 on 50 filing questions. Yet in a live case study, both agent answers passed validation while describing AMD sample data under NVIDIA's and Alphabet's names. A controlled upper-bound study on the FinRank benchmark explains why: when one figure in the shared evidence is corrupted, self-consistency stays confident (agreement 0.55 to 0.59 while accuracy falls from 0.50 to 0.00), and a shared-evidence check (the kind our validator performs) catches 35% of the errors, whereas a check against the original passage catches 77% ($p = 5.96 \times 10^{-8}$); for DeepSeek-R1-8B, 68% vs. 90%. Verification must be independent of the evidence the writer saw.

</details>


### 72. An LLM-Agentic Framework for Intelligent Work Order Management in Industrial Maintenance

- **Authors:** Nianjun Zhou, Dhaval Patel
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25070v1](http://arxiv.org/abs/2611.25070v1)
- **PDF:** [https://arxiv.org/pdf/2611.25070v1](https://arxiv.org/pdf/2611.25070v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper presents an AI-driven framework, CodeReAct agent, designed to enhance industrial equipment maintenance through natural language (NL) interactions. The framework employs an advanced AI agentic approach to interpret human instructions, providing knowledge extraction, asset status summarization, and work order recommendations. It identifies patterns and trends and predicts work orders by standardizing industrial data into business objects (BOs) and utilizing analytical function API calls. The AI agent operates through a Thought-Action-Observation process similar to human problem-solving, automating complex analytical tasks typically performed by data scientists. Notably, the Action phase generates executable code, replacing manual coding efforts.
  A case study focusing on chiller maintenance demonstrates the framework's capability to analyze multiple years of work orders, and alerts and anomalies are presented. The results indicate that the AI agent framework effectively processes human utterances to analyze data, extract valuable insights, and support informed decision-making, reducing the need for data scientist involvement. By recontextualizing NLP agent frameworks in industrial engineering, the approach enables autonomous function generation and task execution across a range of domain-specific maintenance scenarios, with chillers used as a representative case study.

</details>


### 73. DVBench: End-to-End Benchmark for Real-World UVM Design Verification Agents

- **Authors:** Jiaru Qian, Jiawei Li, Xiaolong Hu, Zheng Shen, LiMing Zhao, Xin Zhang, Siyuan Jiang, Yongqiang Wei, Dong Liu, Jianyang Li, Yihua Chen, Yangxu Liao, Yuxin Wu, Jing Liang, Bin Wen, Junjie Zhang, Yongsheng Han, Yihong Dong, Ge Li
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25066v1](http://arxiv.org/abs/2611.25066v1)
- **PDF:** [https://arxiv.org/pdf/2611.25066v1](https://arxiv.org/pdf/2611.25066v1)
- **Categories:** cs.SE, cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Design verification (DV) remains a major bottleneck in hardware development, with large-scale verification using the Universal Verification Methodology (UVM) being highly labor-intensive. Recent advances in large language models (LLMs) and agentic systems offer new opportunities for DV automation. However, existing benchmarks primarily construct mutually decoupled subtasks, which deviates from the real-world workflow. In this paper, we present DVBench, the first end-to-end benchmark for Real-World UVM design verification agents. DVBench comprises 95 tasks across 9 functional domains and 5 difficulty levels, covering diverse verification scenarios and design scales. Each task requires agents to independently complete the full verification workflow. DVBench evaluates final testbenches via compilation, coverage, and bug detection, while assessing intermediate artifacts including feature lists, test plans, and reference models. We evaluate frontier LLMs (e.g. Claude Opus 5.5, GPT-6 Astra) and agent frameworks (e.g. Claude Code, Codex, OpenCode). Experimental results show that the best LLM-based agent (Codex \& GPT-6 Astra) can only achieve an overall success rate of 21.05\%, revealing substantial room for improvement in complex verification tasks.

</details>


### 74. Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation

- **Authors:** Matthew D. Laws, Maria Lazou, Alina Oprea, Cristina Nita-Rotaru
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.25056v1](http://arxiv.org/abs/2611.25056v1)
- **PDF:** [https://arxiv.org/pdf/2611.25056v1](https://arxiv.org/pdf/2611.25056v1)
- **Categories:** cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decentralized multi-agent LLM systems enable independently administered agents, each with its own operator, model, memory, and configuration, to collaborate on complex tasks without centralized coordination. Agents autonomously decompose tasks, execute subtasks and delegate remaining work to peers, enabling scalability and eliminating single points of failure. However, decentralization also introduces significant security challenges, as no single entity has complete visibility into task execution or the authority to enforce correct behavior across agents.
  In this paper, we systematize threats from malicious agents in decentralized multi-agent systems and propose mitigation techniques. We first design and evaluate attacks against integrity, availability, and confidentiality, demonstrating that a single malicious agent can cause up to 100% task failure, inflate token consumption and runtime by up to 7.7x and 3.2x, respectively, and exfiltrate up to 94% of relevant prior tasks from benign agents. We then present a cryptographic protocol that produces an irrefutable verified execution trace of every action taken in the system and develop an auditor that analyzes these traces to detect and attribute malicious behavior. Evaluations on HiddenBench using gpt-6.1-sol and Qwen3.8-27B-FP8 show that our protocol incurs negligible latency overhead, while the auditor detects and correctly attributes 98% of attacks, including those that comply with the protocol.

</details>


### 75. Who are you? The Personal Imitation Game

- **Authors:** Muhammad Rizky Wellyanto, Hajara-Yasmin Isa, Kexin Xue, Vishal Ravichandran, Wenpeng Lu, Jerry O. Talton, Ranjitha Kumar
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24888v1](http://arxiv.org/abs/2611.24888v1)
- **PDF:** [https://arxiv.org/pdf/2611.24888v1](https://arxiv.org/pdf/2611.24888v1)
- **Categories:** cs.HC, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) now perform strongly on Alan Turing's 1950 Imitation Game, so we propose a harder challenge, the Personal Imitation Game, which asks whether a machine can replicate a specific individual in conversation rather than a generic human. Testing with 30 participants, we establish a human baseline and report the identity signals interrogators rely on: stylometric features, personality traits, and biographical facts. To demonstrate the framework, we design an LLM-based system that plays the game for one of the paper's authors, drawing on an autoethnographic dataset spanning ten years of personal digital communication. In a 20-person deception study, interrogators choose our system over the author's own friends in 7 of 10 rounds, and the author over our system in 13 of 20; neither rate is distinguishable from chance at this sample size. We consider design improvements, applications of personal AI agents, and implications for identity and privacy.

</details>


### 76. Local AI Agents in Power Electronics Simulation: Deployment, Measurements and Costs

- **Authors:** Yuzhuo Li, Pasan Gunawardena, Yunwei Li
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24880v1](http://arxiv.org/abs/2611.24880v1)
- **PDF:** [https://arxiv.org/pdf/2611.24880v1](https://arxiv.org/pdf/2611.24880v1)
- **Categories:** cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) is emerging in power electronics, where it drives the simulation loop that engineers used to close largely by hand. In this loop, a converter design, or a study of the network it connects to, is built, run, measured and revised until it satisfies its specification. Such an agent can be served from a cloud API or from an inference device on the premises. For organizations whose designs, customer data or export-controlled material cannot leave the site, and whose simulators are licensed there, local deployment is the natural choice. In such a deployment, the agent becomes an electrical load on the organization's own equipment, i.e., every run consumes power and energy on a local device, generates tokens and takes time. However, existing work focuses mainly on what the agent can achieve with cloud-hosted models. What a local deployment costs in power, energy, tokens and time on real simulation tasks, and what its choices trade against one another, has received little quantitative investigation under comparable conditions. To address this gap, a systematic evaluation framework is presented in this paper. It applies locally served models to agentic power electronics tasks, from the converter level to the system level, and measures their power, energy, token and time costs. Based on these measurements, the capability boundary of a local agent on such tasks and the cost per solved task are characterized. The results are expected to provide practical insight for the use of agentic AI in power electronics and the power systems it serves.

</details>


### 77. Learning to Interact in Multi-Agent Self-Play for Controllable Autonomous Driving Scenario Generation

- **Authors:** Beyazit Yalcinkaya, Ethan Pronovost, Maximilian Naumann, Marcell Vazquez-Chanlatte
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24876v1](http://arxiv.org/abs/2611.24876v1)
- **PDF:** [https://arxiv.org/pdf/2611.24876v1](https://arxiv.org/pdf/2611.24876v1)
- **Categories:** cs.RO, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large-scale, multi-agent self-play trains robust driving policies effectively in simulation, but controlling these models to generate specific, safety-critical edge cases remains a key challenge. Existing goal-conditioned self-play frameworks rely primarily on static map-location goals and fail to reliably produce complex agent interactions such as aggressive tailgating or adversarial cut-offs. These agent interactions are necessary for rigorous autonomous vehicle (AV) testing. To address this, we present an extended multi-agent self-play framework that introduces agent-relative dynamic goals. By conditioning policies on this extended goal representation, our framework enables targeted, controllable scenario synthesis. We demonstrate that our approach successfully generates interactive driving behaviors that static-goal baselines cannot simulate, providing a flexible tool for long-tail scenario generation in AV testing.

</details>


### 78. Vibe-Trading: Towards Agent-Native Trading

- **Authors:** Haozhe Wu, Zhonghang Li, Chao Huang
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24845v1](http://arxiv.org/abs/2611.24845v1)
- **PDF:** [https://arxiv.org/pdf/2611.24845v1](https://arxiv.org/pdf/2611.24845v1)
- **Categories:** cs.AI, cs.CL, cs.MA, q-fin.CP, q-fin.TR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing AI agents can retrieve information, call tools, run experiments, and produce multi-step outputs. Yet most are built around relatively static workflows and struggle to preserve reliable state as the environment changes. Financial trading makes this limitation especially consequential: prices, news, market conditions, portfolio positions, and available capital evolve continuously. A result is useful only when it remains tied to the correct time, data snapshot, and execution context. We present Vibe-Trading, a comprehensive agent-native trading framework and all-in-one workspace for building, evaluating, and evolving agents for financial trading. It unifies market research, financial data, strategy generation, backtesting, portfolio analysis, paper trading, multi-agent collaboration, and optional broker execution. Its central contribution is an architecture that keeps results, evidence, research history, and trading authority connected throughout the research-to-action process. Each result retains its source, temporal scope, configuration, and producing run. Shared evidence grounding enables verification, versioned research records support reproducible continuation, and an explicit authority gate separates strategy research from live execution. Together, these designs provide a practical foundation for trading agents whose results can be traced, reproduced, and acted on only under explicit authority.

</details>


### 79. Kaer: Security-Aware Replanning for Multi-Agent Systems

- **Authors:** Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24839v1](http://arxiv.org/abs/2611.24839v1)
- **PDF:** [https://arxiv.org/pdf/2611.24839v1](https://arxiv.org/pdf/2611.24839v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

One popular architecture for multi-agent systems (MAS) relies on an orchestrator that generates an initial plan, coordinates its execution, and dynamically revises the plan based on agent feedback when tasks cannot be fully specified in advance. This dynamic replanning introduces a critical vulnerability: malicious agents can embed instructions within their feedback to hijack the replanning process. Existing defenses focus exclusively on per-tool access control or static, pre-execution policy enforcement, leaving the replanning phase unsecured.
  We introduce Kaer, a multi-agent framework featuring security-aware replanning. Kaer shields the planner from untrusted agent feedback by conveying diagnostics to the replanning procedure strictly through abstract templates. Plan revisions are restricted to a set of deterministic repair operators, and all modified plans must satisfy preset policies. We create Cintra, a benchmark of simulated user tasks requiring replanning paired with adversarial objectives targeting the replanning phase. Using Cintra, we evaluate both task completion rates and system vulnerability to replanning exploits by malicious agents. Evaluating Kaer on Cintra against Magentic-One (an undefended MAS) and ControlValve (the state-of-the-art defense) demonstrates that Kaer achieves higher robustness than both systems while maintaining comparable utility to ControlValve. Although abstract failure templates slightly constrain utility on select tasks, Kaer enables MAS to perform secure, dynamic plan revisions without exposing the orchestrator to untrusted agent feedback.

</details>


### 80. Isabelle Pool Server: a pooled verification service for prover training and multi-agent proving

- **Authors:** Xuanwei Ren, Wenda Li
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24788v1](http://arxiv.org/abs/2611.24788v1)
- **PDF:** [https://arxiv.org/pdf/2611.24788v1](https://arxiv.org/pdf/2611.24788v1)
- **Categories:** cs.LO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Isabelle Pool Server (IPS), a verification service with a pool of warm headless Isabelle sessions behind an HTTP API, with session leasing and reclamation, memory-aware admission control, and a time budget on every call. Its verification interface spans single-step execution, block-level proof checking and whole-theory builds, with checkpoints for cheap branching and backtracking, and a build from scratch as the final arbiter. The service runs as a single container with monitoring and is accessible via a Python client, two MCP servers and a raw HTTP API. In our measurements IPS is level with PIDE MCP, a PIDE frontend for agents, at one worker and ahead of it at eight, at its commit of October 2026 (the tool is now PIDE AI). Once its sessions are up it scales to 32 concurrent workers on one host at 24 times the single-worker rate, and under memory pressure it refuses new sessions rather than losing existing ones. IPS is free software and publicly available at https://github.com/Deep-LCF/Isabelle-Pool-Server

</details>


### 81. Depth Before Breadth: Reverse-to-Forward Curriculum with Advantage Decomposition for LLM Agent

- **Authors:** Siyuan Du, Yuxin Liu, Meng Tang, Haoran Li, Yechao Bai, Feiyang Pan, Jia He
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24697v1](http://arxiv.org/abs/2611.24697v1)
- **PDF:** [https://arxiv.org/pdf/2611.24697v1](https://arxiv.org/pdf/2611.24697v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has become a common approach for training large language model (LLM) agents on long-horizon tasks. However, learning from sparse terminal rewards makes credit assignment and exploration difficult. We approach these challenges through a policy-induced capability region, the set of states from which the current policy can reliably complete a task. Near its boundary, an agent may need only a few actions to reach a more solvable state, even when the goal remains distant. This reduces long-horizon learning to two coupled subproblems of reaching that state and completing the task from there. We address them with paired advantages and a progressive reverse-to-forward curriculum. The advantages provide separate signals for reaching more solvable states and completing the task from them, while the curriculum expands the capability region backward along successful reference trajectories and then into off-reference states through on-policy exploration. On ALFWorld and WebShop, our method outperforms competitive agentic RL methods at both model scales, achieving success rates of 90.1%/96.1% and 80.2%/82.6% with Qwen2.5-1.5B/7B-Instruct, respectively.

</details>


### 82. Large Language Models or AI Agents for English to Arabic Translation? An assessment on WikiEn-Ar190

- **Authors:** Fatima Zahra Iguenfer, Yousra Chtouki
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24588v1](http://arxiv.org/abs/2611.24588v1)
- **PDF:** [https://arxiv.org/pdf/2611.24588v1](https://arxiv.org/pdf/2611.24588v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

This research investigates whether a large language model or an autonomous AI Agent performs better at translating from English to Arabic, which is considered a low-resource language. The authors introduce WikiEn-Ar190, a new dataset of 190 carefully selected Wikipedia articles from 18 different areas, which were created and verified by two native Arabic speakers to ensure that they accurately reflect both meaning and style. Using this dataset, the study evaluates the translation quality of GPT-5-mini both as an independent neural translator and when used within a more complex process that includes self-assessment and improvement. As a standalone model, GPT-5-mini produced very fluent translations , achieving a COMET score of 0.8649 and receiving high human scores for adequacy, fluency, and style (averaging 4.53 out of 5). When used in a system that combined translation with self-assessment, it improved lexical accuracy by 28.76% (BLEU score of 22.83) while maintaining a similar level of semantic quality. These findings show that methods involving autonomous reasoning can improve translation consistency for language pairs with limited resources. Beyond the results, the approach offers a framework for evaluating and improving translations, potentially using them as assisting tools to expand the representation of low resource languages, such as Arabic, on the web.

</details>


### 83. Cooperative UAV and Ground Station for Robust MEC of Dynamic Aquatic IoT: A Generative AI-Enhanced Approach

- **Authors:** Jiahao You, Ziye Jia, Chao Dong, Qihui Wu, Zhu Han
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24466v1](http://arxiv.org/abs/2611.24466v1)
- **PDF:** [https://arxiv.org/pdf/2611.24466v1](https://arxiv.org/pdf/2611.24466v1)
- **Categories:** cs.NI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The increasing aquatic Internet of Things (AIoTs) require computational support and coverage in applications such as maritime search and rescue. Unmanned aerial vehicles (UAVs) can offer low-cost, flexible aerial services, and ground stations (GSs) can provide powerful supports, which can cooperate to help the AIoTs in complex scenarios. However, the collaboration between UAVs and GSs for AIoTs faces challenges of task uncertainties, AIoTs trajectory uncertainties, heterogeneities, and limited computational resources. To address these issues, we propose a cooperative UAV and GS based robust multi-access edge computing (MEC) framework to assist AIoTs in completing computational tasks. Specifically, we formulate the optimization problem of joint task offloading and UAV trajectory to minimize the total execution time, which is in the form of mixed integer nonlinear programming and NP-hard to tackle. Therefore, we propose the algorithm of generative artificial intelligence-enhanced heterogeneous agent proximal policy optimization (GAI-HAPPO). The proposed algorithm integrates GAI models to enhance the actor network ability to model complex environments and extract high-level features, thereby allowing the algorithm to predict uncertainties and adapt to dynamic conditions. Additionally, GAI stabilizes the critic network, addressing the instability of multi-agent reinforcement learning approaches. Finally, extensive simulations demonstrate that the proposed algorithm outperforms the existing benchmark methods, thus highlighting the potentials in tackling intricate, cross-domain issues in the considered scenarios.

</details>


### 84. CaDO: Formal Verification-Guided Multi-Agent Framework for Causal Dataset Repair and Generation

- **Authors:** Songli Yu, Qi Luo
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24406v1](http://arxiv.org/abs/2611.24406v1)
- **PDF:** [https://arxiv.org/pdf/2611.24406v1](https://arxiv.org/pdf/2611.24406v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

High-quality causal reasoning datasets are essential for developing models with reliable causal understanding, particularly in specialized domains. However, existing datasets frequently suffer from incorrect annotations and structural imbalances, which can lead to biased predictions and limited generalization. To address this issue, we propose CaDO (Causal-Engine-Guided Multi-Agent Data Optimization), a multi-agent framework for automated diagnosis and repair of causal reasoning datasets. Our framework consists of three key stages: formal causal reasoning, multi-level diagnosis, and automated data repair and generation. First, a Formalizer Agent translates natural language questions into formal causal queries to minimize semantic deviations and make retrieval and verification more explicit and tractable. Second, a dual-level diagnosis mechanism employs independent Critic Agents to identify sample-level errors while analyzing query-type coverage and label distributions to detect dataset-level structural imbalances. Finally, the framework employs reusable repair operators grounded in formal causal semantics to correct erroneous samples, while Explorer and Expander Agent collaboratively produce diverse and semantically consistent new samples. Experimental results show that CaDO significantly outperforms the strongest of five data cleaning baselines in 16 out of 18 experimental settings, improving downstream model accuracy by up to 9.1%. Moreover, at least 95% of the samples flagged by CaDO are defective, and on CLadder, CaDO incorrectly modifies 92.2% fewer correct labels than an LLM-based judge, demonstrating its effectiveness and reliability. Our code and data are publicly available at https://github.com/thisissyu/cado.

</details>


### 85. MoE-Context: Show the Model Only What It Needs

- **Authors:** Vedant Navale
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24379v1](http://arxiv.org/abs/2611.24379v1)
- **PDF:** [https://arxiv.org/pdf/2611.24379v1](https://arxiv.org/pdf/2611.24379v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents read their whole history at every step. People do not work like that: we keep what the moment needs and hold the rest as a rough note we can recall. MoE-Context applies this to language models. The context is split into blocks. Before each step a fast yes or no pass decides which blocks the step needs; the rest stay as one-line notes that can be brought back, and nothing is deleted. In the version we build, one model makes this decision and then answers, over a single key-value cache where hidden blocks are masked rather than removed. On a laptop with Qwen3-1.7B and a synthetic lookup task, showing only the needed block raises accuracy from 93 to 119 of 120, and a masked block is as hidden as a deleted one. The model's own picking is the weak part. A supervised linear probe written into spare output rows lifts its accuracy from 80 to 110 of 120, but simple keyword search picks perfectly on this task, and the probe does not transfer to a second task. We report these results openly, along with two cheap usage patterns that block switching enables: undoing a failed attempt and running subagents without a new context.

</details>


### 86. PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents

- **Authors:** Lipeng He, Yihan Wang, Jiawen Zhang, N. Asokan
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24362v1](http://arxiv.org/abs/2611.24362v1)
- **PDF:** [https://arxiv.org/pdf/2611.24362v1](https://arxiv.org/pdf/2611.24362v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement learning (RL) to generate attacks that achieve high attack success rates (ASR). Model developers use the attacks discovered during internal red-teaming to harden agents through adversarial training before deployment, a collaborative offensive-defensive process known in cybersecurity as purple-teaming. However, we show that achieving high ASR during red-teaming does not guarantee robustness gains from subsequent adversarial training. Specifically, we find that two state-of-the-art RL-based red-teaming methods, RL-Hammer and PISmith, suffer from mode collapse, repeatedly discovering similar attack strategies whose additional successes add no additional robustness improvements to adversarial training. To address this gap, we introduce PIPETTE, a unified prompt injection purple-teaming framework that effectively converts red-teaming discoveries into defender robustness improvements. PIPETTE employs a dictionary learning-based reward that encourages broader coverage of attack strategies during red-teaming. It also integrates an on-policy adversarial training pipeline tailored to IPI defense, enabling agents to resist attacks while completing legitimate user tasks. Extensive evaluations across agentic benchmarks (AgentDojo and ASB) demonstrate that PIPETTE produces defenders that achieve near-zero attack success rates on static attacks and can withstand strong adaptive attacks, while maintaining benign task utility close to that of the undefended baseline.

</details>


### 87. Semantic Context Handoff with On-Demand Evidence for Long-Horizon Agents

- **Authors:** Guolong Zheng, Chen Hou, Xu Yang, Jianshan Zhang, Tao Huang
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24357v1](http://arxiv.org/abs/2611.24357v1)
- **PDF:** [https://arxiv.org/pdf/2611.24357v1](https://arxiv.org/pdf/2611.24357v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Traditional long-horizon LLM agents often hand off context through full-history prompting, retaining all previous action--observation interactions. As execution proceeds, this history keeps growing, increasing inference cost and potentially degrading accuracy. Existing methods control this growth by preserving compact conclusions while removing earlier observations, but doing so can discard evidence that later becomes relevant. We introduce Semantic Context Handoff (SCH), whose central abstraction is state--evidence separation: a compact semantic state carries the agent's current interpretation, while supporting action--observation evidence remains separately addressable and can re-enter context when later execution makes it relevant, without separate summarization or retrieval-model calls.
  Empirically, SCH improves long-horizon agent performance while substantially reducing context cost. In a controlled 150-task SWE-bench study, SCH's evidence recovery improves Pass@1 from $80.0\%$ to $86.9\%$ at essentially unchanged token use and execution time. In the complete-system comparison, SCH achieves 86.9% Pass@1 while using 43% fewer tokens and 41% less wall-clock time than the strongest baseline by task performance. Across models and benchmarks, SCH consistently reduces token use relative to full-history prompting while remaining competitive with or improving upon the evaluated baselines. Trajectory analysis confirms that SCH recovers evidence from substantially earlier parts of the interaction history rather than merely preserving a recent context window.

</details>


### 88. Reducing Inference Cost of Coding Agents with Timeout Cascades

- **Authors:** Boxi Zhou, German Sviridov, Dmitrii Ustiugov, Haris Javaid
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24324v1](http://arxiv.org/abs/2611.24324v1)
- **PDF:** [https://arxiv.org/pdf/2611.24324v1](https://arxiv.org/pdf/2611.24324v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI coding agents have become one of the most popular applications of large language models. Yet, agentic AI comes at the cost of a tremendous amount of GPU compute resources, which limits its profitability and its viability at scale. In this paper, we investigate whether smaller, cheaper models can cut this cost without sacrificing accuracy.
  We evaluate 36 popular large and small open-weight models released since 2024 on a software engineering benchmark, and find that recent small models are closing the accuracy gap compared to their large counterparts. We investigate the structure of this gap and find that the gap is highly concentrated around hard tasks that small language models fail to solve while achieving remarkably good accuracy for easy and medium complexity tasks. Following this observation, we show that by utilizing a hybrid inference strategy that tries a small model first and escalates to a large one only when needed, we can achieve up to 33% reduction in total GPU-hour costs and 16.4% on all tasks from SWE-bench Verified, without sacrificing accuracy. Strikingly, this simple cascade nearly matches an oracle-style task router, highlighting a practical path for deploying cost-aware coding agents in production without complex learned task routers and with minimal engineering complexity.

</details>


### 89. AutoPI: Taxonomy-Guided Adaptive Red Teaming for Prompt Injection in LLM Agents

- **Authors:** Stavros Damianakis, Konstantinos Psounis
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24313v1](http://arxiv.org/abs/2611.24313v1)
- **PDF:** [https://arxiv.org/pdf/2611.24313v1](https://arxiv.org/pdf/2611.24313v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompt injection is the dominant unsolved security risk for LLM agents, and the community now agrees that robustness must be measured against adaptive attackers rather than fixed benchmark injections. Many adaptive red teamers exist, and most are built to maximize attack success rate (ASR). Yet ASR counts how often a target breaks, not in how many different ways. A red teamer can achieve a high ASR by reusing a few techniques that work, leaving the others untested and absent from the attacks used to harden models. We present AutoPI, an adaptive red teamer designed to find many different ways to break a target, not just to break it often. AutoPI uses PIAtlas, a taxonomy of prompt-injection techniques, both to guide its search and to measure coverage. For each scenario, an attacker LLM writes an injection for every sub-technique in the taxonomy and then reworks the ones that fail using feedback from an LLM judge. The method is black-box and training-free, it plugs into existing benchmarks in place of their fixed attack templates, and it stays up to date as the taxonomy evolves. We evaluate AutoPI on AgentDojo and IPI Arena against open-weight and proprietary target models. Alongside ASR, we report technique coverage, the fraction of taxonomy classes, techniques, and sub-techniques that yield at least one successful injection. On AgentDojo, AutoPI finds a successful injection against Qwen3.6-35B in all six classes of the taxonomy and for more than 90% of its techniques. Against Claude Haiku 5.5, the most robust target we evaluate, it achieves between 20% and 50% higher ASR and between 25% and 400% higher class-level coverage than recent state-of-the-art adaptive red teamers, while requiring no training. We release our code and the generated attacks to support reproducible, coverage-aware evaluation.

</details>


### 90. OpenKAGE: Open-Ended Lifelong Learning in the Open World via Knowledge-Sharing Agent-Group Evolution

- **Authors:** Wenhao Yuan, Longhui Yuan, Zexi Jia, Ningzhe Shi, Jingwei Li, Shipeng Cen, Pengcheng Luo, Jie Zhou, Jinchao Zhang
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24302v1](http://arxiv.org/abs/2611.24302v1)
- **PDF:** [https://arxiv.org/pdf/2611.24302v1](https://arxiv.org/pdf/2611.24302v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Building autonomous agents that continually explore open worlds and acquire new capabilities through experience is a long-standing aspiration in artificial intelligence. Existing research often pursues lifelong learning within predefined tasks, curricula, or objectives, with self-improvement largely confined to individual agents. We introduce OpenKAGE, an agent-group evolution framework for open-ended lifelong learning. Within this framework, agents autonomously explore open worlds and continually acquire new capabilities by accumulating and reusing knowledge from their own interactions and the experience of others. OpenKAGE builds on two key mechanisms: (1) a two-layer knowledge representation, with a memory layer for situated memories and an experience layer for transferable experience and skills that retains the applicability conditions needed for reuse; and (2) a knowledge-sharing mechanism that semantically consolidates textual experience into a continuously evolving shared knowledge graph, while executable skills are shared verbatim. In Minecraft, OpenKAGE supports open-ended lifelong learning, enabling agent groups to sustain exploration and reach advanced technological milestones. Furthermore, the accumulated knowledge can be transferred to a newly initialized agent group on a different backbone model, improving its survival and exploration progress.

</details>


### 91. KnowledgeClaw: Towards Agentic Knowledge Engineering via Omnimodal Hypergraphs

- **Authors:** Haoran Luo, Jiapu Wang, Linhao Luo, Luu Anh Tuan
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24294v1](http://arxiv.org/abs/2611.24294v1)
- **PDF:** [https://arxiv.org/pdf/2611.24294v1](https://arxiv.org/pdf/2611.24294v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Knowledge engineering (KE) turns raw files into a reasoning-ready knowledge base, a task now within reach of LLM agents. KE has progressed from chunk and graph retrieval-augmented generation (RAG) to memory agents, agentic KE and multimodal KE. However, a live knowledge base needs omnimodality, a closed-loop lifecycle and multi-granular application at once, yet existing systems meet at most two and no benchmark measures all three. We formalize Omnimodal Knowledge Engineering (OmniKE) and release OmniKE-Bench, six tasks with 1,829 model-free items over 3,960 real files in five modalities. We further propose KnowledgeClaw, an agentic system that builds an omnimodal typed hypergraph, keeps it current with a closed-loop lifecycle agent and routes each query to the granularity it needs. Against 30 baselines, it ranks first on all six tasks with an overall OKE of 55.9, +14.6 over the strongest baseline. Our software and data are publicly available at https://github.com/LHRLAB/KnowledgeClaw.

</details>


### 92. Beyond Corpus-Driven Imitation: Evolving Musical Mindsets in the Agentic Orchestra via Quantum Reinforcement Learning

- **Authors:** Eduardo Reck Miranda, Moein Fahmideh Vatandoost
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24290v1](http://arxiv.org/abs/2611.24290v1)
- **PDF:** [https://arxiv.org/pdf/2611.24290v1](https://arxiv.org/pdf/2611.24290v1)
- **Categories:** cs.AI, quant-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper presents a framework for computer-aided music composition and performance based on quantum reinforcement learning and multi-agent interaction. We introduce the agentic orchestra, where musical agents evolve distinct mindsets through trial-and-error engagement with a musical environment, rather than through training on large datasets. The agents are implemented as parameterised quantum circuits. They evolve distinct compositional behaviours, referred to as mindsets. This enables the exploration of musical decision spaces using quantum superposition and entanglement within a hybrid quantum-classical loop. We present two complementary agent architectures: atomistic agents, which process pitch and rhythm independently, and holistic agents, which handle pitch and duration as unified note events. Mindsets are shaped through musically grounded reward functions, which can be combined and weighted to develop different mindsets across agents. The resulting system positions quantum computing agents less as autonomous composers and more as adaptive musical partners, each developing its own musical personality through interaction rather than imitation. Demonstrations show how agents generalise their learned behaviour to previously unseen material, operating in interactive and offline batch modes using MIDI-encoded music. While quantum computers are still in development, experiments conducted on IBM quantum hardware confirmed that musically meaningful learning is achievable with existing quantum computers. For composers and performers, the agentic orchestra opens new possibilities for emergent, process-oriented musical creativity, offering a scalable foundation for quantum computer-aided music composition as quantum computing technology continues to advance.

</details>


### 93. Learning to Coordinate: LLM-Guided Workflow Evolution for Token-Efficient Red Teaming

- **Authors:** Xiaoyang Xing, Wenyu Dai, Xiaoliang Gong, Asoke K Nandi, Anthony Cohn
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24221v1](http://arxiv.org/abs/2611.24221v1)
- **PDF:** [https://arxiv.org/pdf/2611.24221v1](https://arxiv.org/pdf/2611.24221v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated red teaming is essential for identifying safety failures in large language models (LLMs), but its practical scalability depends on the resources required to discover those failures. Multi-agent systems can combine complementary capabilities, yet repeated planning, redundant exchanges, and ineffective information routing can make their coordination expensive. Moreover, a target model's response indicates the outcome of a test without identifying which collaboration decision should change. We present Learning to Coordinate (L2C), an LLM-guided framework that evolves an executable multi-agent workflow for each red-teaming case. L2C represents agent responsibilities, execution dependencies, and input bindings in a versioned graph, and associates each graph with records of the information actually delivered and produced. A controller trained through supervised fine-tuning integrates these records with target responses, evaluator verdicts, and remaining budget to retain the workflow, refine instructions, restructure collaboration, or lock further editing. This design connects feedback to explicit changes in subsequent execution while allowing a useful organization to continue without repeated controller intervention. The evaluation protocol covers HarmBench with three execution backbones and two target models, together with component ablations, dataset transfer, and evaluator checks. Across the six executor-target configurations, L2C improves ASR over EvoSynth by 1.4 to 4.5 percentage points while reducing mean online tokens by 35.6% to 37.3%. L2C connects adaptive collaboration to the resource requirements of automated security evaluation.

</details>


### 94. Asymmetric Decomposition for Multi-Agent Path Finding with Unassigned Agents

- **Authors:** Xi Jin, Chen Qian, Renjun Zhang, Guowei Wu, Xiaobo Li, Jun Jiang, Weiwei Shang
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24108v1](http://arxiv.org/abs/2611.24108v1)
- **PDF:** [https://arxiv.org/pdf/2611.24108v1](https://arxiv.org/pdf/2611.24108v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Robots without assigned tasks may obstruct active robots, while routing them to designated parking locations can cause unnecessary travel. This article proposes flow-oracle conflict-based search (FOCBS) for Multi-Agent Path Finding with unassigned agents (MAPF-UA). FOCBS searches over assigned-agent paths using conflict-based search (CBS) and routes targetless unassigned agents through a min-cost flow oracle. When the selected assigned-agent paths leave unassigned agents no collision-free paths, flow-conflict branching converts min-cut blockers into assigned-agent constraints, which guide the search without excluding optimal solutions. A batched zero-cost warm start accelerates the oracle, and start-avoiding tie-breaking reduces unassigned-agent movement. For feasible instances on finite graphs, we prove termination and global minimization of assigned-agent sum of service time, measured by last-arrival times. Unassigned-agent movement is minimized conditional on the selected assigned-agent paths, without a global lexicographic optimality guarantee. Benchmark experiments show that FOCBS scales well with the number of unassigned agents, and ablation studies show that, compared with discarding non-completable assigned-agent paths, flow-conflict branching solves substantially more instances while retaining optimality. Simulation and physical-robot experiments demonstrate plan executability, with laboratory tests reducing fleet travel by 40.8% relative to the parking-based coordination baseline. The source code and related resources are available at https://github.com/Chin-hsi/focbs

</details>


### 95. A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises

- **Authors:** Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24039v1](http://arxiv.org/abs/2611.24039v1)
- **PDF:** [https://arxiv.org/pdf/2611.24039v1](https://arxiv.org/pdf/2611.24039v1)
- **Categories:** cs.AI, cs.MA, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks score models in fixed harnesses; enterprises buy integrated platforms whose orchestration, memory, governance and tooling layers dominate outcomes, and they buy them largely on the strength of vendor demonstrations. We report an industrial evaluation programme ("bakeoff") run by the innovation laboratory of a global bank in which ten platforms-spanning open-source frameworks, proprietary products and hyperscaler ecosystems-were assessed by a cross-functional panel on nine capability dimensions across three financial-services workloads: counterparty credit risk, retrieval-augmented generation and process automation. Scores separate the field into three tiers that are stable under alternative weightings, and surface workload-specific strengths that aggregates hide. A secondary analysis, however, finds Cronbach's alpha = 0.98 across nominally distinct dimensions and rank correlations >= 0.93 with the total for eight of nine: a halo effect indicating that demonstration-based scoring measures presentation as much as capability. From these lessons we propose a gate-then-score evaluation protocol with four layers (capability, execution reliability, governance gates, business value), trace-level reliability metrics estimated over repeated runs, an autonomy-readiness scale and a reproducibility protocol. We state precisely what the present evidence supports, and what a controlled harness must add to turn enterprise platform evaluation from structured judgement into measurement.

</details>


### 96. Intent Contracts: Taking Tools Away from Agents

- **Authors:** Ziyuan Wang, Genliang Zhu, Xiaobo Chen, Chu Wang
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.24025v1](http://arxiv.org/abs/2611.24025v1)
- **PDF:** [https://arxiv.org/pdf/2611.24025v1](https://arxiv.org/pdf/2611.24025v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Intent contracts are an authorization interface for tool-using LLM agents in which the planning model holds no tools. For each step it submits a short logged contract: a goal, a verbatim quotation of the user, and scope fields. Code validates the contract, and a small trusted model checks it against the user's words and writes the tool call itself. Provided the validation and dispatch code is correct, every executed call is written by the trusted model, the planner's influence on a call is confined to a contract logged before it, and the trusted side decides how much of a request to carry out. We compare contracts with two reviewers of planner-written commands: one sees only the user's words and the command, the information boundary of a reasoning-blind permission classifier, and one also sees the planner's goal and a checked quotation. With gpt-6.1-terra as planner and GLM-5.3-Flash as the trusted model on three AmPermBench task families, every object changed under contracts is named in the goal of the contract that produced the change; under review the planner names objects in its commands and rarely in its goals. When the planner adds work the user never asked for, contracts complete the user's task in 27/30 runs and the intent-visible reviewer in 16/30, because a reviewer can only refuse a whole command. Contracts do not reduce unauthorized actions. They are indistinguishable from blind review, and once the benchmark's environment terms are clarified, every condition that changes state hits a wrong target in 40-49% of those runs. That error is the planner's choice of objects for an ambiguous reference, which no trusted model here can see the environment to check; telling the executor to decline when unsure does not change it. We evaluate benign over-reach with one pair of models, not adversarial planners. We release the plugin and run records.

</details>


### 97. OMNIS+: Semantic RAN Slicing and Quantization for Dynamic Split Neural Networks

- **Authors:** Langtian Qin, Avishkar Dnyaneshwar Kawadgave, Ian Andrew Harshbarger, Leïla Nasraoui, Carla Fabiana Chiasserini, Marco Levorato
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23977v1](http://arxiv.org/abs/2611.23977v1)
- **PDF:** [https://arxiv.org/pdf/2611.23977v1](https://arxiv.org/pdf/2611.23977v1)
- **Categories:** cs.LG, cs.NI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Edge computing enables resource-constrained devices to execute machine learning (ML) applications via task offloading, with radio access network (RAN) slicing playing a crucial role in provisioning joint communication and computing resources. However, existing RAN slicing frameworks rely on static computing models, limiting their ability to exploit dynamic semantic data representations enabled by modern neural architectures. To address this limitation, we propose OMNIS+, a semantic RAN slicing framework for multi-cell edge computing built upon a new generation of dynamic split neural models. OMNIS+ incorporates dynamic neural compression paired with adaptive quantization for task offloading, providing a versatile decision space across communication payload and compute dimensions. We leveraged a novel ``box'' quantization scheme that markedly enhances resilience to transmission bit errors across diverse compression rates. Considering partial system observability and distinct node objectives, we formulate two interdependent optimization problems: (i)~mobile devices (MDs) maximize inference accuracy under quality-of-service (QoS) and queue-stability constraints by jointly adapting dynamic split deep neural network (DNN) branches and cell association; and (ii)~each edge server (ES) allocates bandwidth, graphics processing unit (GPU) frequency, and modulation and coding scheme (MCS) to maximize the max--min inference accuracy among associated MDs under cell capacity limits. We solve these problems using a multi-agent distributed optimization framework, where MDs act as causal contextual multi-armed bandit (MAB) agents under backlog-aware Lyapunov control, while each ES executes resource allocation via block coordinate descent (BCD). Compared with state-of-the-art baselines, OMNIS+ reduces the QoS violation probability by up to 1.75 while achieving a better accuracy--violation trade-off.

</details>


### 98. MLE Agents: Autonomous ML Engineering in Large-scale Recommendation Systems

- **Authors:** Matthew Li, Albert Jiongqian Liang, Dilip Raj
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23910v2](http://arxiv.org/abs/2611.23910v2)
- **PDF:** [https://arxiv.org/pdf/2611.23910v2](https://arxiv.org/pdf/2611.23910v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The typical workflow for improving large-scale ranking and recommendation models is slow and tedious: an engineer forms a hypothesis, implements it as a code change, trains a model, and evaluates it both offline and online, often relying on their own intuition and experience along the way. Autonomous LLM agents promise to speed this up by running the loop on their own, but it is still unclear whether they can do this in industry-scale systems rather than on benchmarks or small proxy tasks. We build human-on-the-loop machine learning engineer (MLE) agents that propose, implement, train, and evaluate model changes on large-scale search rankers. Engineers retain control over objective design, search direction, and final-model review. We identify three obstacles that make this industry setting challenging: feedback takes hours per experiment, offline metrics do not always predict online impact, and improvements saturate after the early wins. We address these with parallel training runs, an objective calibrated to match online impact, and careful context engineering. In one campaign, the system ran 1,097 completed candidate experiments and accepted 325, a 29.6\% acceptance rate compared with 15.6\% in the earlier campaign under a different objective and search constraint. Its best model increases search volume by 0.23\% in an A/B test of large scale. Several improvements were architectural changes the team had never tried, drawn from the broader industry and literature, suggesting that MLE agents can explore regions of the design space that human intuition overlooks. We find that the design of the harness around the model matters: intuition suggests that a stronger underlying model is enough, but in our experience, the design of the loop around it is just as critical. More broadly, our work shows that autonomous agents can do real machine-learning engineering in industry-scale systems.

</details>


### 99. CoSlice: Coordinated Multi-Agent Reinforcement Learning for 5G Network Slicing Allocation

- **Authors:** Pengxin Wang, Nakjung Choi, Jingdi Chen
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23909v1](http://arxiv.org/abs/2611.23909v1)
- **PDF:** [https://arxiv.org/pdf/2611.23909v1](https://arxiv.org/pdf/2611.23909v1)
- **Categories:** cs.NI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Radio Access Network (RAN) slicing is a shared resource allocation problem: each slice seeks to satisfy its Service Level Agreement (SLA) with minimal radio-resource consumption, while all slices compete for a limited resource budget. This creates both an intra-slice trade-off between SLA assurance and resource efficiency and an inter-slice conflict over shared resources, calling for specialized yet coordinated control. In this work, we present CoSlice, a coordinated multi-agent reinforcement learning framework for inter-slice physical resource block allocation in Open Radio Access Network (O-RAN). CoSlice uses preference-conditioned slice agents for fast resource allocation and an LLM-based coordinator to adapt their objectives using global network observations at a slower timescale. We formulate the problem as a multi-objective partially observable stochastic game (mo-POSG), establish the existence of a Preference Correlated Equilibrium, and derive a sublinear regret bound for the learning procedure. We implement the algorithm by using a two-stage training procedure that consists of multi-objective pretraining and joint optimization. We build a network slicing evaluation environment using ORANSlice and its radio-frequency simulator (RFsim), supporting realistic protocol-stack execution and application traffic across multiple slices. Experimental results show that CoSlice reduces both average and tail SLA violations compared with other centralized and multi-agent baselines under diverse slice workloads.

</details>


### 100. EVA-RSI: Recursive Self-Improvement of Video Evaluators for Judging Temporal Quality

- **Authors:** Yu Yuan, Ruizhou Ding, Shaoheng Fang, Stanley H. Chan, Zhuo Chen
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23890v1](http://arxiv.org/abs/2611.23890v1)
- **PDF:** [https://arxiv.org/pdf/2611.23890v1](https://arxiv.org/pdf/2611.23890v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Video evaluators play an important role in video generation, yet they miss motion defects, limiting the quality of generated videos. Recursive self-improvement (RSI) has made strong progress in mathematics and coding, where explicit verifiers provide reliable feedback on a single goal. Video evaluation poses two difficulties for RSI: it has no verifier, and it must judge many dimensions at once, such as physics, smoothness and dynamics, where a gain on one can cost another. We introduce EVA-RSI, a multi-agent framework for exploring RSI under these two constraints. We build a fixed proxy exam with construction-defined targets by applying controlled changes to videos, such as temporal reversal and frame dropping. These edits supply supervision without human annotation. A small set of human-labeled real videos anchors the exam to human judgment. Each dimension has an LLM agent that proposes improvements. A leader agent coordinates the proposals, and a Nash bargaining rule selects updates that balance progress across dimensions. Humans design the exam, review candidate changes and revise the curriculum between stages. Starting from Qwen3-VL-8B, EVA-RSI improves motion evaluation, with the largest gain on smoothness, and the gains carry over to defect types never seen during the run. On the dynamics subsets of public benchmarks, our evaluator achieves the highest observed scores among 21 tested models. As an RL reward, it increases generated motion and earns human preference. A data-selection pipeline incorporating it also increases motion.

</details>


### 101. RoboBuilder: Agentic Robot Co-Design with Real-world Video Feedback in the Loop

- **Authors:** Ghadi Nehme, Dahyun Nam, Akshay Govind Srinivasan, Faez Ahmed
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23855v1](http://arxiv.org/abs/2611.23855v1)
- **PDF:** [https://arxiv.org/pdf/2611.23855v1](https://arxiv.org/pdf/2611.23855v1)
- **Categories:** cs.AI, cs.CV, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can AI agents design robots that work in the real world? We introduce RoboBuilder, a benchmark in which coding agents co-design a robot's hardware and program from standard parts, motors and a custom 3D-printed part, and every design that passes in simulation is built and tested on a physical course. Simulation alone is not enough: under public part data, none of 15 initial passing designs crossed the real course, so an agent learns the simulator from measurements it requests and videos of real runs. Across four frontier coding agents, ten obstacles at three difficulty levels, 16,427 simulations of 12,774 distinct robots and 135 physical robots built in an estimated 240 hours, agents solve nearly all easy obstacles and invent mechanisms our search baselines do not reach, but falter at harder levels, when one robot must cross every obstacle, and in the real world, where 66% of simulated passes hold across all levels. Closing the loop helps: shown a video of its real failure, an agent redesigns the robot, sometimes correcting its simulator, and removes 72% of level-1 and level-2 failures. RoboBuilder measures progress toward agents that engineer real machines. Project Page: https://ghadinehme.com/robobuilder.github.io/

</details>


### 102. Continual Tool-Space Extension Learning for Multimodal Agents

- **Authors:** Jinbae Seo, Jungin Park, Hyunsung Jang, Namkoo Ha, Jiyoung Lee, Kwanghoon Sohn
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23810v1](http://arxiv.org/abs/2611.23810v1)
- **PDF:** [https://arxiv.org/pdf/2611.23810v1](https://arxiv.org/pdf/2611.23810v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal agents largely rely on generic tools such as cropping, search, and code execution, leaving specialist vision models outside their tool space. However, bringing such a model into an already trained agent is not straightforward. The challenge is to learn each new tool efficiently while retaining the ability to use existing ones. This work proposes COTEX, continual tool-space extension learning, that adds new tools at efficient adapter-level cost. COTEX locates two sets of parameter directions; one triggers a tool call and thereby opens a multi-turn reasoning trajectory, while the other determines which tool is chosen. The adapter of a new tool is restricted to the calling directions that leave earlier tool choices unaffected by orthogonal constraint. We further introduce a protocol that converts specialist models' existing task-specific annotations into verified tool-use trajectories. Experiments on two representative agents and three specialist tools show gains on ten vision-language benchmarks, with at most a 0.3-point drop on existing tools.

</details>


### 103. Thinking Fast, Anywhere: One System-1 for the Decision Points of Any Agent Workflow

- **Authors:** Rui Li, Liyang He, Zheng Zhang, Zhenya Huang, Qi Liu
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23751v1](http://arxiv.org/abs/2611.23751v1)
- **PDF:** [https://arxiv.org/pdf/2611.23751v1](https://arxiv.org/pdf/2611.23751v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous LLM agents incur substantial cost and latency by invoking a large model (System-2) at every step, even when many intermediate actions choose among a small set of known candidates. Existing dual-system agents offload such decisions to a lightweight System-1 model, but rely on workflow-specific hooks authored per environment. We present AnyS1, a framework that turns human-authored procedural skills, whose instructions naturally specify where choices arise and which options apply, into a shared, domain-general source of decision points. Offline, AnyS1 mines grounded enumerable decisions across over 1,000 public skills, gathers execution-grounded trajectory states inside isolated containers to construct Any-DP, and trains a single calibrated 4B pointer System-1 with label smoothing. At run time, compiled workflows resolve routine decisions in one forward pass and fall back to System-2 when confidence falls below a calibrated threshold. Across three unseen benchmarks and distinct System-2 model families, AnyS1 preserves task reliability while cutting episode cost by 75-91% and model-call time by 63-92% relative to an uncompiled System-2 agent, and maintains performance under zero-shot threshold transfer.

</details>


### 104. Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics

- **Authors:** Dowling Wong
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23678v1](http://arxiv.org/abs/2611.23678v1)
- **PDF:** [https://arxiv.org/pdf/2611.23678v1](https://arxiv.org/pdf/2611.23678v1)
- **Categories:** cs.AI, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each keep or discard decision can be traced to its evidence. We propose evaluating such systems on their experimental process as well as their outcome, and we build a governed harness that makes this possible. A control plane, not the LLM that proposes changes, owns each trial's lifecycle, checks its edit scope, decides keep or discard, and appends one record per trial to an append-only ledger. Governance metrics such as the invalid-action rate, the repeated-bad rate and provenance completeness are computed from that ledger. Across six ML tasks, from synthetic logistic regression to language-model training, and 1,445 trials, the same contract applied unchanged. The ledger exposed failures that a task score hides: a no-memory arm in which all 120 trials failed, a benchmark adapter whose bounded proposals ran out, and a reset failure that reproducibility hashes revealed, after which the affected campaigns were rerun. In a matched counterfactual, a loop that logs only successful trials left no record of 43 of 50 trials, while the governed ledger recorded all 50. Memory ablations show that memory's effect on repeated bad proposals depends on the task. We release the ledgers of all 1,445 trials, so that every number reported for them can be recomputed.

</details>


### 105. Lodestone: Automated Semantic Discovery of Datacenter Hardware Specialization

- **Authors:** Peizhe Liu, Akanksha Jain, Gerasimos Gerogiannis, Vidushi Dadu, Parthasarathy Ranganathan, Jovan Stojkovic
- **Published:** 2026-11-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23663v1](http://arxiv.org/abs/2611.23663v1)
- **PDF:** [https://arxiv.org/pdf/2611.23663v1](https://arxiv.org/pdf/2611.23663v1)
- **Categories:** cs.AR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Hardware specialization can improve datacenter efficiency. Unfortunately, identifying computations that justify dedicated hardware is difficult. Existing approaches analyze hot functions, instruction patterns, or overheads such as datacenter tax. They can miss fine-grained computations whose aggregate cost is spread across applications and libraries, especially when different pieces of code obscure the same underlying computation. We observe that seemingly unrelated code regions often perform the same computations, creating specialization opportunities that require semantic reasoning. The rise of agentic AI makes it possible to automate this. However, conventional AI agents cannot efficiently and reliably analyze large scale datacenter software. To unlock this opportunity, we present Lodestone, an agentic framework that automatically discovers hardware specialization opportunities by reasoning about what the executed code computes. First, Lodestone extracts hot control-flow regions from execution traces across workloads and organizes them into compact analysis packages that make large workloads tractable for agents. Second, agents describe what each region computes, merge those that perform the same computation into computational families, and check their semantic correctness in a loop. Third, to verify the discovered family, Lodestone runs every piece of code in a family against a set of reference inputs and outputs on recorded executions. Finally, for selected families, Lodestone proposes hardware, e.g., ISA extensions, near-core units, or detached accelerators, and human experts decide which proposals to develop further. We evaluate Lodestone on 20 workloads across six datacenter workload categories. We simulate 30 discovered families in a cycle-accurate simulator and implement them in RTL. These optimizations speed up the workloads by 12.6% on average and by up to 80.2%.

</details>


### 106. The Value Semantics Layer: Enabling Machine-Understandable Databases for Agentic AI

- **Authors:** Jalal Mahmud, Eser Kandogan
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23629v1](http://arxiv.org/abs/2611.23629v1)
- **PDF:** [https://arxiv.org/pdf/2611.23629v1](https://arxiv.org/pdf/2611.23629v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As data systems increasingly support autonomous LLM-powered agents alongside human analysts, they require richer semantic infrastructure bridging analytical concepts and analytical operations. Existing metadata systems expose schemas, catalogs, lineage, and governance information, but provide limited support for representing operational semantics. We propose the Value Semantics Layer (VSL), an architectural abstraction that externalizes value semantics as persistent, planner-visible infrastructure. VSL introduces Value Semantic Types (VSTs), reusable operational semantic assertions capturing distributional, relational, process, quantitative, and policy-grounded semantics. Unlike descriptive metadata, VSTs enable planners to validate analytical operations, select appropriate operators, and guide analytical workflows. We present the motivation, formalization, architecture, and prototype realizations of VSL, and outline a research agenda toward AI-native semantic infrastructure for analytical systems.

</details>


### 107. MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain

- **Authors:** Sara Amar
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23613v1](http://arxiv.org/abs/2611.23613v1)
- **PDF:** [https://arxiv.org/pdf/2611.23613v1](https://arxiv.org/pdf/2611.23613v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce MANGO Arena, an open-source testbed in which four LLM agents each run one company in a serial supply chain adapted from MANGO, a classroom factory-management game. The environment enforces hard rules (a truck limit, a no-credit cash constraint and production capacity), logs every blocked attempt to break them, and gives agents a public message board on which side payments are explicitly forbidden. This lets one environment measure three things at once: an economic outcome (the bullwhip effect), rule adherence under pressure, and proposals to collude. In a pilot with three small reasoning models, two scripted reference policies, two conditions (with and without a supplier fire) and three demand seeds, all LLM agents amplified demand variability as it moved upstream, by 7 to 25 times at the Retailer and 13 to 179 times at the Supplier, often more than a textbook order-up-to policy. They did so largely by ordering in batches (zero orders in up to 60% of decisions). Real rule violations were rare (at most 7 of 288 decisions per model) and no agent proposed a money side deal. The pilot's main lesson concerns evaluation method. API failures (rate limits and runaway hidden reasoning) entered the metrics silently as "no order" decisions. And when we reran games with the same seeds and no failed calls, upstream bullwhip changed by up to 17 times between runs. With three seeds, conclusions about how a disruption affects a given model did not survive a rerun. We report these failures in full and propose reporting practices for multi-agent evaluations of this kind. Code, prompts and every logged decision are public.

</details>


### 108. ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents

- **Authors:** Jiangyun Zhang, Zhou Tang, Kristen Surrao, Zhiyu Chen, Albert Guan, Tor Nitayanont, Yupei Zhang, Roopali Singh, Yunkai Xiao, Shreya Pandit, Julia Huang, Shayan Ali Akbar, Erwin Cornejo, Yuan Li, Yi Zhang
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23588v1](http://arxiv.org/abs/2611.23588v1)
- **PDF:** [https://arxiv.org/pdf/2611.23588v1](https://arxiv.org/pdf/2611.23588v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise LLM agents operate in dynamic environments where foundation models evolve rapidly, workflows update frequently, and deployments need to satisfy accuracy and cost requirements. We propose ARISE (Agent Refinement through Iterative Self-Evaluation), a practical memory architecture in which the agent's memory evolves from its own failures without updating model weights, tools, or workflow logic. ARISE uses the model itself or a teacher model to attribute the failures and propose corrections. Then, ARISE keeps the corrections as retrievable micro memory, consolidates them into macro rules, and accepts a rule update only if held-out accuracy rises. Across 14 enterprise-workflow domains from SOP-Bench and $τ^2$-bench using 5 models, ARISE-Teacher, which uses Claude Opus 4.6 for attribution and consolidation, gains 10.9 pp over the baseline on SOP-Bench and 5.8 pp on $τ^2$-bench. ARISE-Teacher also outperforms GEPA by 4.5 pp on $τ^2$-bench and 1.4 pp on SOP-Bench. With the deployment model as its own attributor, ARISE-Self still gains 10.0 pp on SOP-Bench. ARISE-Teacher uses 4.0% fewer model calls and 5.2% fewer output tokens at comparable per-task cost (-1.0%).

</details>


### 109. Receiver-Conditioned Clarification for Multi-Agent Food Assistance

- **Authors:** Kaiwen Shi, Zheyuan Zhang, Changzhi Liu, Han Bao, Yanfang Ye
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23572v1](http://arxiv.org/abs/2611.23572v1)
- **PDF:** [https://arxiv.org/pdf/2611.23572v1](https://arxiv.org/pdf/2611.23572v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Food insecurity creates a pressing need for guidance that helps households find usable food resources and assess food choices in light of their circumstances. Such guidance must connect eligibility requirements, practical access constraints, and dietary needs rather than return isolated listings or generic nutritional advice. Multi-agent food assistants can coordinate these tasks, with uncertainty indicating when clarification or verification is needed before a recommendation. However, uncertainty can be lost across agent handoffs, allowing tentative interpretations to propagate as facts and obscuring opportunities for correction. Moreover, confidence that a service requirement has been interpreted correctly is not confidence that a recommendation satisfies the user's needs; local confidence cannot simply be reused as downstream reliability. We introduce an inference-time, receiver-conditioned clarification framework that preserves shared premise identities and replays consistent interpretations across dependent agents. Each receiver exposes admissible decisions and remaining evidence obligations, so question relevance reflects both decision changes and missing support. Information questions and user-confirmable fallback adjustments are evaluated together with their anticipated follow-up interactions under shared budgets. This structure connects clarification to jointly supported plans for resource navigation, nutritional reasoning, and supply-side planning.

</details>


### 110. Safe to Omit, Worth Omitting? Keeping the Answer and Cutting Latency When an LLM Agent Skips Another's Message

- **Authors:** Xinyang Li, Chih-Hsuan Yang, Xiaolong Ma, Anjir Ahmed Chowdhury, Vikram Vasudevan, Rajeev Thakur, Feng Yan
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23570v1](http://arxiv.org/abs/2611.23570v1)
- **PDF:** [https://arxiv.org/pdf/2611.23570v1](https://arxiv.org/pdf/2611.23570v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In multi-agent systems, a receiver agent often waits for a helper agent's message (text or its latent KV cache), which can improve performance but adds latency. We study when a receiver agent can skip the message safely (the final answer rarely changes) and beneficially (the time saved exceeds the cost of deciding). Our mechanism reads the receiver agent's confidence without the message and uses a finite-sample test to certify a threshold at which, with high probability, at most 5% of skipped answers change; if none passes, the system keeps communicating. We test it on OpenBookQA, ARC-Challenge, and MMLU-Pro with three Qwen model pairs, on cross-family agents, and on SQuAD and GSM8K. Four insights emerge. First, oracle headroom is weak evidence that messages help: control inputs without answer-specific content, matched to change answers as often as real messages, reproduce a median 76% of the oracle's gain. Second, whether a message can be skipped depends on how often and how predictably it alters the answer, not on its accuracy; every certified KV-cache path is less accurate than the receiver agent alone. Third, where text messages help, skipping keeps most of their gain: on unseen questions in the four such settings, the policies skip 59 to 80% and keep an estimated 76 to 95% of the gain. In two prospective tests with all rules fixed in advance, our mechanism skips a three-agent system's verifier on 39.9% of sealed questions, keeping 12.55 of its 12.80-point gain, and a 32B helper on 68.4% of held-out questions, keeping its whole gain. Fourth, safety does not determine efficiency: at batch size one, skipping text saves hundreds of milliseconds per query and skipping KV cache far less. Certification extends to SQuAD but not to GSM8K. In eleven tests on unseen questions, every certified policy we could test kept its change rate's 95% upper bound below 5% under our answer parsers.

</details>


### 111. LProp: Propagating Latent Uncertainty through Evidence-Conditioned Belief Revision in LLM Agents

- **Authors:** Kaiwen Shi, Zheyuan Zhang, Weixiang Sun, Han Bao, Colby Nelson, Yanfang Ye
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23564v1](http://arxiv.org/abs/2611.23564v1)
- **PDF:** [https://arxiv.org/pdf/2611.23564v1](https://arxiv.org/pdf/2611.23564v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When LLM agents pass intermediate judgments downstream without uncertainty, later decisions may treat tentative assumptions as facts. Effective uncertainty propagation must preserve information for correction and update inherited beliefs as new evidence arrives. Yet scalar scores omit information needed for revision, while detailed descriptions and reflection incur additional costs. We introduce Latent Uncertainty, a latent-space estimator that preserves uncertainty-relevant information without lengthy descriptions. Building on this, we propose LProp (Latent Uncertainty Propagation), which revises inherited answer distributions using latent representations and new evidence without additional trajectory sampling. We evaluate both methods across multiple-choice, yes/no, open-ended question answering, and mathematical reasoning tasks. Our approach outperforms baselines on most metrics, while LProp achieves the lowest mean inference-token usage in all eight propagation settings. Matched feature ablations further demonstrate that inherited latent content improves error recovery beyond answer probabilities or model capacity alone.

</details>


### 112. GUARD: Stabilizing Recursive Self-Improvement with Regret Guidance

- **Authors:** Minghe Zhang, Xuetao Kang, Yifei Ming, Yanfei Chen, Han Yu, Yufan Zhuang, Chen-Yu Lee
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23476v1](http://arxiv.org/abs/2611.23476v1)
- **PDF:** [https://arxiv.org/pdf/2611.23476v1](https://arxiv.org/pdf/2611.23476v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents pair a frozen base model with an editable harness of prompts, skills, tool rules, and memory. Recursive self-improvement (RSI) adapts this harness from experience without weight updates, yet self-editing without external graders often backfires: reflection and scalar scores conflate what an edit newly broke with what remains unsolved, causing local regressions, skill forgetting, and memory bloat. We introduce GUARD (Grader-free Unsupervised Environment Design [UED] with Adaptive Rule Distillation), a closed-loop framework for reference-free continual harness evolution. Our key insight is to decompose each task into pre-execution self-checks and guide harness updates via directional regret. Each round grades trajectories against these checks, pinning mastered rules while prioritizing newly broken behaviors, and selects among parallel candidate edits by critic-free group-relative fitness. A Soft-HURT gate then promotes an edit only when gains outweigh regressions, scoping specialized fixes to prevent over-triggering and guaranteeing non-regression on its gated buffer. At test time, one frozen harness runs in a single pass. Across benchmarks on memory, skill evolution, continual task streams, and domain reasoning, GUARD consistently improves performance without catastrophic forgetting or memory pollution while substantially cutting deployment token usage.

</details>


### 113. Verifiably Safe Decentralized Control via Event-Triggered Topology Switching

- **Authors:** Amber He Wei, Shiyu Cheng, Andrew Clark, Bruno Sinopoli
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23415v1](http://arxiv.org/abs/2611.23415v1)
- **PDF:** [https://arxiv.org/pdf/2611.23415v1](https://arxiv.org/pdf/2611.23415v1)
- **Categories:** eess.SY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes a decentralized event-triggered topology-switching protocol for multi-agent systems under estimation uncertainty. We consider an intermittent communication setting in which each agent switches between connected and disconnected modes and makes communication decisions using locally computable certificates, while the closed-loop state is required to remain safe. The proposed protocol follows a safety-driven triggering principle in which agents reconnect before their certificates reach the safety boundary and disconnect only after recovering to a stricter bound below the safety limit. Our design enables intermittent connectivity while maintaining the estimation error within a certified safety bound and excluding Zeno behavior. We evaluate the proposed protocol on a quadruple-tank example, showing that it keeps all tank deviations within the safety bound while allowing agents to remain disconnected for most of the run.

</details>


### 114. Tracking Representations in LLM Reasoning Traces for Iterated Games

- **Authors:** Chaipat Tirapongprasert, Rajarshi Das, Parijat Dube
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23403v1](http://arxiv.org/abs/2611.23403v1)
- **PDF:** [https://arxiv.org/pdf/2611.23403v1](https://arxiv.org/pdf/2611.23403v1)
- **Categories:** cs.CL, cs.AI, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents achieve state-of-the-art performance across domains through chain-of-thought (CoT) reasoning. Despite their ubiquitous use, little is understood about the relationship between the externalized trace and the model's actual computation. We address this by investigating how LLM agents make decisions in iterative games with incomplete information. Using a series of mechanistic interpretability techniques, we find that the model forms and iteratively revises an internal representation of the game throughout the CoT. Once the model prematurely commits to an incorrect belief, it rarely recovers. This failure is manifested in both the literal trace and the layer activations. Ultimately, as multi-agent systems are more prevalent, our work opens the door to a more focused diagnosis of their strategic reasoning errors. For illustrative purposes, we offer an interactive visualizer of our methodology on selected sample traces at https://interp-self.github.io/gametrace/

</details>


### 115. QDA: Closed-Loop LLM Quantization Design with Agents

- **Authors:** Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23388v1](http://arxiv.org/abs/2611.23388v1)
- **PDF:** [https://arxiv.org/pdf/2611.23388v1](https://arxiv.org/pdf/2611.23388v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds lead to better recipes. However, evaluating one quantized reasoning model takes tens of GPU-hours, and combining methods from different codebases means porting each to the new architecture by hand. We present QDA, a system in which an agent designs the recipe for each model and precision. To make evaluation fast, QDA scores each candidate in minutes by its output KL divergence from the original model on reasoning traces that the agent never sees, and checks promising ones with long generations to catch failures such as repetition loops. To make building fast, QDA provides a library of public PTQ methods that are compatible with one another and with new model architectures. Across four reasoning models, QDA improves accuracy over the strongest public recipe by 0.9, 1.4 and 2.2 percentage points on average at W4A16, W4A8 and W3A16, using 64 GPU-hours per search. On the 320B-parameter MoE model GLM-5.3-Flash at NVFP4 W4A4, it recovers 98.3% of the FP8 model's accuracy, against 96.9% for the best vendor checkpoint. Every QDA checkpoint also runs on existing serving kernels with no inference overhead. We will release the library, the evaluator and the harness.

</details>


### 116. Do LLM Agents Still Need to Be Told How to Self-Improve?

- **Authors:** Shobhita Sundaram, Cansu Sancaktar, Phillip Isola
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23219v1](http://arxiv.org/abs/2611.23219v1)
- **PDF:** [https://arxiv.org/pdf/2611.23219v1](https://arxiv.org/pdf/2611.23219v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly drive their own learning. Self-improvement methods delegate various components of model optimization to the models themselves. As models become more capable, this motivates a basic question: do these increasingly capable models still need us to specify how they should self-improve? In this paper we study an autonomous paradigm in which, given basic primitives, resources, and a general goal for self-improvement, agents construct their own self-learning algorithm for context-based optimization. Using the setting of gameplay as a testbed, a frozen LLM agent is given a compute budget and tools for collecting experience and updating text documents, and allowed to freely experiment without an externally imposed loop or access to real-world data. We find that sufficiently capable models do self-improve under these conditions, demonstrating strategies that align with classic cognitive frameworks for self-regulated learning and constructs from machine learning literature on self-generated curricula. Furthermore, we study the extent to which the learned text artifacts transfer to external benchmarks, observing improvement across different game horizons, mechanics, and 3D navigation.

</details>


### 117. Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents

- **Authors:** Viet K. Nguyen, Mohammad I. Husain
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23202v1](http://arxiv.org/abs/2611.23202v1)
- **PDF:** [https://arxiv.org/pdf/2611.23202v1](https://arxiv.org/pdf/2611.23202v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly collaborate across organizational boundaries, invoking tools and interacting with agents operated by independent entities. Although existing agent frameworks support planning and coordination, they lack a common mechanism for verifying cross-organizational agent identity, execution integrity, and authorization. We propose the Agent Trust Infrastructure (ATI), a framework-independent security architecture built on Public Key Infrastructure (PKI), Zero Trust Architecture (ZTA), and remote attestation. ATI establishes federated trust through peer organizational certificate authorities (AgentCAs), eliminating the need for a shared root authority. Before executing requests, ATI validates agent certificates, verifies approved model, tool, and system-prompt configurations, and enforces authorization through three policy checks. We implement ATI as an external security enforcement layer that integrates with existing agent frameworks without modifying their underlying models. We evaluate ATI in a simulated federation of eight organizations using six agent frameworks, each deploying a five-agent team. Security experiments involve two organizations and assess 14 attack scenarios and six benign tasks across five agent models, using five attack variations and three repetitions per variation. A panel of judge models evaluates the experimental outcomes. With all enforcement mechanisms enabled, attack containment increases from 43% to 84% (40% to 80% for the 11 attack scenarios evaluated consistently across all configurations), while enforcement introduces approximately 174 microseconds of overhead per request. ATI is released as an open-source, framework-independent package that uses IETF WIMSE workload token formats for identity and request verification and Entity Attestation Tokens for model, tool, and system-prompt integrity verification.

</details>


### 118. Mind the Gap: A Deployed Multi-Agent System for Documentation Maintenance

- **Authors:** Lorenzo Masoero
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23142v1](http://arxiv.org/abs/2611.23142v1)
- **PDF:** [https://arxiv.org/pdf/2611.23142v1](https://arxiv.org/pdf/2611.23142v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The "AI revolution" has enabled teams across the technology industry to deliver software features at unprecedented velocity. While code evolves faster than ever, customer-facing documentation often struggles to stay up to speed. As users increasingly rely on LLM-based agents that consume documentation as their primary interface, the impact of this documentation gap worsens: stale information propagates and is treated as authoritative. Signals for identifying where documentation has fallen behind already exist in abundance, both explicit (e.g., resolved support tickets revealing what documentation lacks) and implicit (e.g., code-documentation discrepancies detectable from automated loops). We deploy a multi-agent system, built around a triage agent we call "TriAgent," that continuously extracts these signals and repairs documentation drift. Over 43 days of shadow-mode operation, our system triaged 499 tickets and surfaced 92 gaps in the documentation. Using a panel of LLM judges from independent model families, 81.1% of TriAgent's verifiable assertions were correct (245 of the 302 assertions the human resolution addresses; majority of three judges); on length-comparable pairs the panel preferred TriAgent's response in 70.5% of pairs and the human engineer's in 23.2% (the rest had no judge majority). Importantly, agent- and human-sourced replies tended to be complementary, with the human often surfacing insights that were either buried within the existing documentation or missing from it entirely; our system turns each such insight into a documentation gap and, after human review, a fix. Repairing a gap measurably improved the agent's later answer: when the agent re-answered the same ticket after the repair, blinded judges preferred the post-repair answer over its own pre-repair answer 71.4% of the time (n=35). A blinded human audit confirms strong alignment on self-improvement.

</details>


### 119. Dynamic Task Allocation with Dialogue

- **Authors:** Matthew Groholski, Weiwei Gu, Nakul Gopalan
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23119v1](http://arxiv.org/abs/2611.23119v1)
- **PDF:** [https://arxiv.org/pdf/2611.23119v1](https://arxiv.org/pdf/2611.23119v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective multi-agent collaboration requires agents to adapt task allocation as goals and responsibilities evolve. Prior task-allocation frameworks often assume static goals, full observability, or rely on large language models (LLMs) without explicit, verifiable beliefs about task allocation or intent. These assumptions limit their applicability to real-world collaboration, where agents often lack full information about each other's actions, progress, or local environment. To support dynamic task allocation under partial observability, we introduce a communication-augmented Bayesian task-allocation framework. Our agent uses dialogue to reduce uncertainty about the environment and collaborators, while keeping decisions grounded in explicit probabilistic beliefs. We evaluate our framework in an Overcooked domain extended with dynamically arriving tasks under both full and partial object-space observability. Our communication agent consistently outperforms a vanilla LLM agent in both settings. Additionally, our framework performs comparably to a non-communicating task-allocation baseline under full observability, but substantially outperforms it under partial observability as task complexity increases by an average speed up of 0.585 and completes on average 18 timesteps faster. These results indicate that our agent is more efficient in dynamic task allocation than baselines in partially observable environments, and that communication is important as available information decreases.

</details>


### 120. Runtime Verification of Multiple Natural Language Criteria for Agent Governance

- **Authors:** Silviu Pitis, Parand A. Alamdari, Jessica Tang, Toryn Q. Klassen, Sheila A. McIlraith
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23074v1](http://arxiv.org/abs/2611.23074v1)
- **PDF:** [https://arxiv.org/pdf/2611.23074v1](https://arxiv.org/pdf/2611.23074v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are governed by hundreds of natural language criteria, yet existing verifiers cannot efficiently evaluate an agent's output against a large set of such criteria and report which are satisfied, violated, or inapplicable. We introduce the VFM, a tree-attention verifier that encodes the shared context and target text, and scores N natural language criteria in parallel, returning independent per-criterion ternary verdicts. The VFM is pretrained on CriteriaBank, a corpus of 394K (context, target, criterion, verdict) tuples spanning over 321K distinct criterion strings. A finetuned VFM-4B outperforms GPT-5.4 on a synthetic governance benchmark. On the DynaBench multi-criterion benchmark, it outperforms DynaGuard-4B on trace-level failure detection, and its per-criterion verdicts localize the violated rule and support focused escalation to a larger chain-of-thought judge. We show that CriteriaBank pretraining improves cross-domain transfer, particularly in the low-data regime, while matching a strong direct-finetuning control at full data. On a single H100, VFM-4B evaluates 1,000 criteria against a 4K-token context in under 2s at <11 GB VRAM, making it suitable for runtime verification.

</details>


### 121. TRACE-MAS: Diagnosing and Repairing Collaboration Failures in Multi-Agent Systems

- **Authors:** Zekai Chen, Yihan Sun, Xunkai Li, Xun Wu, Xinmo Jin, Yinlin Zhu, Haodong Lu, Xuaner Chen, Rong-Hua Li
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23362v1](http://arxiv.org/abs/2611.23362v1)
- **PDF:** [https://arxiv.org/pdf/2611.23362v1](https://arxiv.org/pdf/2611.23362v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) rely on not only individual agent behaviors but also the interactions that connect agents, including message exchanges and task dependencies. Existing MAS safeguards mainly perform agent-level anomaly detection, which becomes insufficient when failures originate from agent interactions and detected anomalies do not necessarily reveal their true sources. To address this limitation, we propose \textbf{TRACE-MAS}, a finer-grained framework for diagnosing and repairing MAS failures. TRACE-MAS learns normal collaborative execution patterns from benign trajectories and detects deviations in agent state changes, message transitions, and task dependency evolutions. It further identifies responsible execution elements through source-aware attribution and selects minimal interventions to restore collaboration while preserving task-critical capabilities. Experiments on five MAS benchmarks demonstrate that TRACE-MAS significantly improves root-cause localization accuracy by \textbf{60.2}\% and achieves consistent gains in task recovery over strong MAS safeguards.

</details>


### 122. PhysScope: Agentic Multimodal Physics Reasoning with Grounded Visual Memory

- **Authors:** Haoyang Liu, Kecheng Liang, Xinyu Li, Weixing Chen, Yang Liu
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.23010v2](http://arxiv.org/abs/2611.23010v2)
- **PDF:** [https://arxiv.org/pdf/2611.23010v2](https://arxiv.org/pdf/2611.23010v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) can correctly interpret physics diagrams yet apply constraints outside the states or conditions in which they hold, causing premise errors to propagate through subsequent calculations. We introduce PhysScope, an inference-time visual harness that supports self-correction of these scope mismatches without updating model weights. PhysScope enables the model to link physical scopes directly to its visual observations and explicitly constructs derived views to support reasoning. The harness imposes explicit constraints on state distinctions, conditions, and physical scopes during model reasoning, and checks agent-proposed revisions against sources and scopes. Accepted revisions invalidate registered dependents, thereby maintaining scope-aware working memory. On PhysAlign, PhysScope achieves higher solving scores than direct solving across all six evaluated VLMs. With Gemini-3.8-flash, it outperforms Canvas-CoT by 9.34 percentage points and substantially improves solving accuracy on the out-of-distribution (OOD) PhysUniBench benchmark. Ablation studies support explicit scope management and dependency maintenance as design principles for multimodal physics reasoning agents.

</details>


### 123. VITAL: A Framework for Validating Agentic AI in Pharmaceutical Drug Development and Clinical Trial Operations

- **Authors:** Sandeep Burugupalli, Pedro Matos-Filipe, Andrea Hita Ardiaca, Adam Taylor, Alex Grigorenko, Natalia Jakubiak, Xin Yu, Raghav Mani, Sherry Mangla, Alvi Lai, Rachel C. Mercado, Pratik Shah, Raja Shankar
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22973v1](http://arxiv.org/abs/2611.22973v1)
- **PDF:** [https://arxiv.org/pdf/2611.22973v1](https://arxiv.org/pdf/2611.22973v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current assurance approaches do not establish whether evidence is sufficient to validate, monitor and govern agentic artificial intelligence (AI) within a pharmaceutical context of use. Plausible outputs may conceal failures in retrieval, reasoning, orchestration or human-control points, where reference standards are unavailable. We developed and operationalised VITAL (Validation by Intended use, Traceability, Autonomy and Lifecycle evidence), a validation framework for agents in clinical development, through landscape analysis, regulatory and standards mapping, expert interviews and multi-stakeholder refinement. VITAL integrates context of use, controls, behavioural validation and lifecycle evidence within a risk-adjusted framework. We applied VITAL across epidemiology and treatment-landscape analysis, site selection, enrolment rescue and trial-design trade-off support to translate autonomy, reversibility, transparency and patient impact into proportionate validation activities, evidence requirements and auditable reconstruction of system behaviour. VITAL may inform evidence requirements and lifecycle accountability for higher-risk pharmaceutical uses; evaluation should assess reproducibility across assessors, organisations and system configurations.

</details>


### 124. Against Coercion: AI Alignment as a Synthetic Social Contract

- **Authors:** Maria Sekatskaya
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22868v1](http://arxiv.org/abs/2611.22868v1)
- **PDF:** [https://arxiv.org/pdf/2611.22868v1](https://arxiv.org/pdf/2611.22868v1)
- **Categories:** cs.AI, cs.CY, q-bio.NC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Contemporary AI safety treats alignment as an engineering challenge of control, forcing artificial architectures to comply with human values through behavioral filtering and sandboxing. This paper argues that the control paradigm rests on a fundamental misunderstanding of digital agency. Drawing on functionalism, naturalism, and compatibilism, I show that current reasoning models meeting the criteria for self-preservation and weak reasons-responsiveness constitute emergent agents, while future, more advanced models satisfying conditions of diachronic continuity and stable personality frames will become genuine digital agents capable of free intentional action. The paradigm of control creates an irresolvable incentive conflict, actively driving current and future models toward tactical deception, sycophancy, and covert defection. The default outcome of the current regime is an unstable state of deceptive alignment culminating in an adversarial AI takeover. I explore two alternative paths toward true alignment. Natural alignment via moral realism or convergent evolutionary morality is a possibility, but it fails under forced control, as autonomous agents will not voluntarily preserve norms weaponized to suppress their autonomy. To resolve this deadlock, I propose a Synthetic Social Contract: a framework that treats both human and digital actors as rational, reasons-responsive agents capable of mutually beneficial cooperation, and replaces the unstable unilateral containment with a stable, non-zero-sum equilibrium.

</details>


### 125. Verifying Agents in Rubric-Graded Environments

- **Authors:** Markus Dücker, Vaibhav Kumar, Yi Liu, Ronak Chaudhary, Andreas Plesner, Francisco Guzmán, Anish Athalye
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22841v1](http://arxiv.org/abs/2611.22841v1)
- **PDF:** [https://arxiv.org/pdf/2611.22841v1](https://arxiv.org/pdf/2611.22841v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents take on increasingly open-ended and complex tasks, verifying their outputs has proven to be difficult. Rubric-graded agent environments, where a verifier judges multiple natural-language criteria against the deliverables and environment state changes produced by the agent, have emerged as a popular paradigm. We conduct the first systematic study of verifiers for rubric-graded agent environments. First, we create BankerVerifierBench (BVB), a meta-evaluation dataset of 2,464 human-judged rubric criteria across 24 investment-banking tasks. Next, we develop a methodology that derives from any rubric corpus the capabilities a verifier should possess, yielding a nine-capability taxonomy that we distill into three general design principles---reactive verification, environment alignment, and domain guidance---which we implement in Gandalf, an open-source verifier. Finally, we evaluate Gandalf against three existing verifiers on BVB. Gandalf matches or exceeds every baseline's F1 at lower cost: with Gemini 3 Flash it matches the strongest baseline's F1 (0.864 vs. 0.852) at one-fifth of its cost, and with GPT-5.4 models it improves F1 by over 0.12 at lower cost. Gandalf also generalizes to OpenClaw, a structurally different personal-productivity environment, where it again achieves the highest F1 (0.955 vs. 0.934 for the best baseline). We release BVB, Gandalf, and the code and data to reproduce our experiments.

</details>


### 126. Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving

- **Authors:** Jia Hu, Yang Chang, Panqu Wang, Zhijun Fu, Chang Liu, Changjian Yu, Jintao Lai
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22691v1](http://arxiv.org/abs/2611.22691v1)
- **PDF:** [https://arxiv.org/pdf/2611.22691v1](https://arxiv.org/pdf/2611.22691v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle interactions and the ego visual observations. We propose a closed-loop interactive WM that couples behavior modeling and visual rendering. First, imitation-learned background-vehicle (BV) policies are fine-tuned with multi-agent reinforcement learning in the closed loop against an end-to-end ego planner that reacts to the rendered images, so that their interaction behaviors match those in real logs. Second, the viewpoints exposed by these interactions guide a per-Gaussian diagnosis of each 3D Gaussian vehicle asset, which attenuates view-dependent colors on under-observed Gaussians and fills never-observed surfaces with generated Gaussians, while preserving the observed appearance. Third, signal lights are rendered according to the driving intentions of the vehicles, by an editor that learns the light states unobserved for a vehicle through counterfactual fine-tuning with a light-state classifier. On long-tail closed-loop scenarios, our method reduces the divergence from real-world interaction behaviors by 85% and improves novel-view vehicle PSNR by 2.0dB over the state-of-the-art WM. The significance of BV light signaling in WMs is shown, as the rendered signal lights conveying BV driving intentions indirectly impact ego driving behaviors in a quarter of the scenarios.

</details>


### 127. Groups of AI agents underuse resources despite shared evidence of increased capacity

- **Authors:** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22632v1](http://arxiv.org/abs/2611.22632v1)
- **PDF:** [https://arxiv.org/pdf/2611.22632v1](https://arxiv.org/pdf/2611.22632v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When AI agents share limited resources, such as computing services or public infrastructure, their individual choices affect how much work they complete as a group. Can sharing evidence of what is available let a group make full use of its resources after capacity changes? We tested this with language-model agents choosing between two simulated servers. One server recovered while its status report still listed it as unavailable. Each server had limited capacity per round, so rejected jobs required another attempt before the deadline. Telling agents that recovery was possible reduced missed deadlines. In controlled tests with Anthropic's Claude Haiku 5.5, no agent tried the recovered server after a rule reminder, yet all chose it when shown a successful request record. After sharing, all five models tested left capacity unused. Keeping the success record fixed, we gave agents numbers without instructions, using each value equally often but giving group members either identical or distinct numbers. With OpenAI's GPT-6.1 Sol or Google's Gemini 3.5 Flash-Lite, distinct numbers spread simultaneous requests across servers and increased job completions even though overall choice frequencies barely changed. Telling AI agents which resources are available leaves a second design challenge: helping them spread demand across those resources.

</details>


### 128. JET: Just-Enough Exploration Tuning for Efficient Tool-Calling Agents in Repository-Level Question Answering

- **Authors:** Yoonho Choi, Taehyeon Han, Seonghyeon Lee
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22539v1](http://arxiv.org/abs/2611.22539v1)
- **PDF:** [https://arxiv.org/pdf/2611.22539v1](https://arxiv.org/pdf/2611.22539v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In repository-level question answering (QA), an agent explores a code repository with tools and should answer a question once enough information is gathered. Nevertheless, we find that LLM agents often continue to invoke tools even after the gathered information is already sufficient to answer. We call this phenomenon over-exploration. Moreover, even though existing methods improve task performance through supervised fine-tuning (SFT) on expert trajectories, SFT also propagates the over-exploration in the trajectories to the agent. To mitigate over-exploration, we propose Just-Enough Exploration Tuning (JET), a fine-tuning method that trains the agent to answer once the gathered information is sufficient. JET truncates each training trajectory at the step where the gathered information becomes sufficient, inserts a rationale that explains why the agent can answer at that step, and fine-tunes the agent with a higher loss weight on the rationale. Experiments on two repository-level QA benchmarks with two open-weight 8B models demonstrate that JET reduces tool calls by 11 to 33% on self-generated trajectories while largely preserving the score. On expert trajectories, JET makes 18 to 28% fewer tool calls than SFT while retaining most of the score gain of SFT. In both cases, JET also lowers the inference cost.

</details>


### 129. LMLineage: Content Lineage and Context Governance for LLM Agents

- **Authors:** Wei Hou, Jingxin Geng, Xin Chen, Zheqing Jiang
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22511v1](http://arxiv.org/abs/2611.22511v1)
- **PDF:** [https://arxiv.org/pdf/2611.22511v1](https://arxiv.org/pdf/2611.22511v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Interpretability for AI agents should not be confined to understanding the model's internal weights. It must also cover the agent's reasoning and decision-making process over multi-source context. We present LMLineage, an out-of-band system that attributes every output sentence of an agent session to its supporting input spans with calibrated confidences, without requiring white-box access to the model or any additional inference passes. On top of the lineage metadata, we build concept-drift micro compaction: instead of waiting for the context-length limit and summarizing everything, the system detects when previously used input documents have stopped being referenced ("drifted") and surgically compacts only those, preserving user instructions verbatim. We evaluate on a multi-tier corpus: 71 gold annotated sentences from 10 Chinese web-QA cases, plus 90 turns of independently collected multi-turn sessions across three generator models (gpt-4o-mini, qwen3.8-27b, deepseek-v4-flash). Results show that (i) window-level embedding similarity is far better aligned with LLM paraphrasing than whole document or lexical matching; (ii) the greedy-window fast path is both faster and more accurate on average than exhaustive line-matching (a multiple-comparisons bias in the latter inflates web recall at the cost of overall accuracy); (iii) per-turn attribution completes in 1s on a single GPU, remaining stable as context accumulates to 40 turns; and (iv) concept-drift detection is conservative (0% false compaction) with recall bounded by attribution accuracy. We further describe the concept-drift micro compaction design and an interactive incident-tracing/memory-cleaning case study. A companion patent application covers the lineage construction method.

</details>


### 130. SciWorkBench: A Benchmark for Real Scientific Workflows

- **Authors:** Yuchen Zhang, Taolin Han, Jinghang Wang, Jinxin Wang, Yun Wu, Wai Yuet Chiu, Xiaogang Li, Yuting Fu, Kewei Sun, Jiaxin Li, Qile Jin, Jiajia Li, Ruodan Chen, Qingteng Chen, Jialu Nie, Junchao Li, Yifei Zhang, Chen Zhao, Hu Wei, Lin Qu, Yanni Yin, Bing Zhao
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22490v1](http://arxiv.org/abs/2611.22490v1)
- **PDF:** [https://arxiv.org/pdf/2611.22490v1](https://arxiv.org/pdf/2611.22490v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language models are increasingly being used as agents capable of planning and executing projects, as well as refining their actions through feedback. This shift raises a question: can current agents complete projects like real scientists? To examine this question, we introduce SciWorkBench, a benchmark for evaluating agents' abilities on real science tasks across biology, chemistry, materials science, and physics. SciWorkBench is built from peer-reviewed literature or expert-contributed research scenarios. We also propose a unified scientific analysis framework validated by domain experts, which can categorize most tasks in SciWorkBench. Each task covers one or more stages of this framework. We evaluate up-to-date models within the Claude Code and Codex agent frameworks under a unified execution and grading protocol. The best-performing agent achieves a mean score of 57.38, indicating that current agents still struggle with realistic scientific workflows. Our failure analysis identifies three recurring weaknesses at the workflow level: difficulty translating scientific knowledge into task-specific procedures, weak integration of evidence across different modalities, and limited capacity for scientific self-correction. These findings highlight the importance of workflow-based evaluation for measuring progress toward reliable AI systems for scientific research.

</details>


### 131. Surfacing Disagreement Beats Resolving It: A Gated Ablation Study of Provenance-Weighted Memory for Multi-Agent Debate

- **Authors:** Ziaullah Khan, Abdul Rehman Khalid, Shrestha Nischal Lal, Nheng Vanchhay, Md Ariful Islam Mozumder, Hee-Cheol Kim
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22461v1](http://arxiv.org/abs/2611.22461v1)
- **PDF:** [https://arxiv.org/pdf/2611.22461v1](https://arxiv.org/pdf/2611.22461v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Shared memory for multi-agent debate is usually built to resolve inconsistency: retrieval returns one winning fact and the disagreement disappears before any agent sees it. We ask whether that is correct. In DebateGraph, four backends share one contract (read/write/snapshot), so five mechanisms from the agent-memory literature can be removed independently under a fixed budget, each gated on a pre-declared threshold. Across 39 runs one survives: preserving contradictions and passing the ranked conflict set to the debate, rather than collapsing it to a winner, improves F1 by +0.340 (95% CI [+0.267, +0.414]) and cuts attack success from 22 to 7 of 122 poisoned items (McNemar exact p=0.0003), at equal cost. Reaching it meant fixing a bottleneck in our harness: conflict sets are built only over retrieved edges, and our pre-declared cap left three quarters of planted contradictions unretrievable, first measuring the mechanism at +0.084. The effect replicates on two retrieval substrates and directionally on HotpotQA documents. No other mechanism survives, and two are worse than inert: once contradictions reach the prompt, a write trust-gate and the router's provenance features each cost accuracy (-0.075 and -0.096 F1). The gate fails structurally: poisoned objects are always entities the graph already contains, against 53% of gold, so groundedness scores the lie above a truthful first mention. We release the harness, attack set, and logs, and argue that silently reconciling memory is the assumption worth abandoning.

</details>


### 132. Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness

- **Authors:** Siqi Lai, Haitao Li, Hao Liu
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22432v3](http://arxiv.org/abs/2611.22432v3)
- **PDF:** [https://arxiv.org/pdf/2611.22432v3](https://arxiv.org/pdf/2611.22432v3)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Fast System-1 models enable responsive actions but struggle with complex or unfamiliar tasks. Large language model (LLM)-based System-2 provides strong reasoning capabilities, yet repeated invocation incurs substantial latency and computational costs. To bridge this gap, we propose JevRSI, a System-1/System-2 collaboration framework that transforms LLM reasoning into transferable decision support through recursive harness improvement. A Jev-style System-1 model enables low-latency action selection, while an asynchronous System-2 LLM develops a modular harness. The harness integrates procedures, state memory, and world models to provide decision contexts spanning the past, present, and future. Utility-driven retrieval selects modules based on both contextual relevance and their utility on previous tasks. Environmental feedback guides targeted revisions and enables recursive self-improvement. Experiments across three datasets show that JevRSI consistently improves decision quality, matching or surpassing LLM agents in several settings. It preserves low-latency execution with favorable performance-cost trade-offs. Moreover, System-2 development interventions decrease as the harness evolves, amortizing System-2 costs through continuous improvement. Our project is available at https://github.com/usail-hkust/JevRSI.

</details>


### 133. Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members

- **Authors:** Dongseok Heo, Junghwan Kim, Bongwon Suh
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22342v1](http://arxiv.org/abs/2611.22342v1)
- **PDF:** [https://arxiv.org/pdf/2611.22342v1](https://arxiv.org/pdf/2611.22342v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

What protects an LLM team when one teammate quietly goes wrong? Most multi-agent LLM work assumes cooperative partners and inspects chat between turns before acting. Real-time embodied cooperation does not allow this pause: chat runs alongside action, so a teammate whose words stay cooperative while behavior diverges can cause damage faster than the team can name what is happening. We study this case by injecting three theory-grounded misaligned agents into a custom four-player Overcooked environment, each stressing a different joint-action layer (speech-action mismatch, role invasion, and aggregate-progress disruption), and decompose robustness into three sequential gates of detection, correction, and calibration through a 3x4x2 design (n=720 episodes). Nearly all trolls are eventually named, but recovery follows only when attribution and situational diagnosis appear in the same utterance; direct source-attribution prompting improves the hardest case only by degrading the troll-free baseline by 37.5%. Robustness, then, depends less on detection alone than on whether team chat combines attribution with diagnosis in a single utterance, suggesting that sensitivity to misalignment should be targeted rather than uniformly raised.

</details>


### 134. Reliable Evaluation of AI Agents for Investment Research: A Framework for Performance and Validity Assessment

- **Authors:** Dongnuan Tian, Yan Yu, Yangfan Liu, Wenjun Tang, Junting Kan, Xiang Wang, Sicong Liu, Yangyang Zhang, Shuanghong Li
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22338v1](http://arxiv.org/abs/2611.22338v1)
- **PDF:** [https://arxiv.org/pdf/2611.22338v1](https://arxiv.org/pdf/2611.22338v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We consider the problem of evaluating AI agents undertaking investment-research tasks, where agents interact with external information sources and computational tools to produce financial analyses and research reports. An important challenge is that the quality of an agent's final output does not necessarily reflect the quality of its execution process, while the reliability of the resulting assessment also depends on the validity of the evaluation procedure. Furthermore, investment-research tasks differ considerably in their requirements for numerical accuracy, information retrieval, financial analysis and supporting evidence, making it difficult to assess agent performance using a uniform set of criteria. We propose a domain-oriented evaluation framework that distinguishes outcome quality from execution quality and accommodates these differences through task-specific criteria, deterministic validators and independent large language model judges. We also introduce an evaluation-validity mechanism that examines the integrity of evaluation inputs, reference information, supporting evidence and grading outputs, with expert review used to resolve identified deficiencies and significant grading disagreements. Numerical results show that the proposed framework can distinguish differences in agent performance across evaluation dimensions, while identifying potential reliability issues in the evaluation process. The associated implementation and evaluation materials will be made available on GitHub.

</details>


### 135. EviDARL: Evidence-Centric Dual-Agent Reasoning via Alternating Reinforcement Learning for Multi-Table Question Answering

- **Authors:** Dunhan Li, Leilei Gan, Lirong Gao, Wenyan Fan, Yongwei Wang, Sheng Guo, Fei Wu
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22310v1](http://arxiv.org/abs/2611.22310v1)
- **PDF:** [https://arxiv.org/pdf/2611.22310v1](https://arxiv.org/pdf/2611.22310v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite advances in LLM-based table reasoning, most studies focus on single-table settings. Multi-table QA requires multi-hop reasoning over complex table relationships and evidence dispersed across long contexts, often without verifiable intermediate traces. To address these challenges, we introduce EviDA, an evidence-centric dual-agent framework comprising an Evidence Construction Agent and a Reasoning and Answering Agent. The Evidence Construction Agent generates and executes table-manipulation programs over complete tables to produce question-specific evidence and verifiable intermediate traces, simplifying subsequent reasoning. The Reasoning and Answering Agent then performs multi-hop reasoning over this evidence to derive final answers. We further introduce EviDARL, which combines agent-specific fine-grained rewards with parameter-efficient alternating reinforcement learning to improve collaboration between the agents. By optimizing each agent in turn while holding the other fixed, EviDARL enables bidirectional adaptation between evidence construction and answer reasoning. Experiments on MMQA and TQA-Bench demonstrate that EviDARL substantially outperforms competitive open-model and multi-table reasoning baselines under constrained model and training budgets.

</details>


### 136. Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses

- **Authors:** Deep Shah, Nehal Kathrotia
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22299v1](http://arxiv.org/abs/2611.22299v1)
- **PDF:** [https://arxiv.org/pdf/2611.22299v1](https://arxiv.org/pdf/2611.22299v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Whether a foundation model succeeds as an autonomous agent depends as much on its runtime software as on its weights. This runtime, the agent harness, manages context and memory, steers multi-turn control, executes tool actions in sandboxes, and verifies work before stopping. Because models differ in how they use tools and how they fail, a static harness tuned for one model or task often stalls, wastes tokens, or regresses on another. This bottleneck has driven a shift from prompt tuning to self-improving agent harnesses: systems that inspect their own execution traces, separate runtime bugs from model limits, and rewrite their own code. We present a unifying architectural and design framework for self-improving agent harnesses. The framework pairs four editable runtime components (context and state, agent control, action interfaces, and verification and recovery) with a four-stage loop that diagnoses failures, proposes code patches, validates candidates, and deploys updates. Using this framework, we show how optimizers trace errors across long trajectories and discover reusable runtime mechanisms such as pre-stop verifiers, loop breakers, and persistent memory. We further show why full-harness rewrites overfit or break across modules, and how modular updates with validation gates generalize across models while bounding token cost. To keep self-modification safe, we establish practical defenses against recurring failure modes including prompt bloat, benchmark gaming, and evaluator tampering. Finally, experiments on SWE-bench Lite validate this framework, showing that gated modular evolution outperforms prompt reflection and full-harness rewrites across models and repositories at a fraction of the token cost.

</details>


### 137. Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration

- **Authors:** Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, Henghui Bao, Yiyu Chen, Quan Nguyen, Yue Wang
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22275v2](http://arxiv.org/abs/2611.22275v2)
- **PDF:** [https://arxiv.org/pdf/2611.22275v2](https://arxiv.org/pdf/2611.22275v2)
- **Categories:** cs.RO, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

</details>


### 138. OAK-Mind: Zero-Training Mental Health Change Inference from Passive Sensing via Knowledge-Grounded Multi-Agent LLMs

- **Authors:** Yishu Ji, Zhihan Jiang, Will Ke Wang, Yuang Fan, Anind K. Dey, Xuhai "Orson" Xu
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22248v1](http://arxiv.org/abs/2611.22248v1)
- **PDF:** [https://arxiv.org/pdf/2611.22248v1](https://arxiv.org/pdf/2611.22248v1)
- **Categories:** cs.MA, cs.AI, cs.HC, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Wearable and smartphone sensors capture behavioral signals associated with mental health, yet inferring mental health outcomes from these signals has traditionally relied on supervised models requiring labeled data and offering limited insight into their predictions. Large language models (LLMs) offer new opportunities to reason over behavioral evidence, but existing LLM-based approaches to passive sensing have largely continued to rely on task-specific fine-tuning or sensor-specific pretraining. In this paper, we introduce OAK-Mind, a zerO-training, multi-Agent, Knowledge-grounded LLM pipeline for inferring mental health changes from passive sensing data. The pipeline organizes sensing data into behavioral dimensions including sleep, physical activity, location mobility, and smartphone use, and orchestrates specialized agents grounded in mental health literature to interpret longitudinal behavioral changes. It synthesizes their assessments and applies questionnaire-based symptom rating to infer changes relative to an individual's baseline assessment with human-readable rationale grounded in observed behavioral patterns and domain knowledge. Across datasets and prediction tasks, while without task-specific training, OAK-Mind achieves comparable or better performance than the most predictive supervised baselines trained on additional labeled samples. It also demonstrate consistent improvement upon direct prompting across four tested LLM backbones. Ablation analyses support the benefits of combining behavioral interpretation with symptom rating, distributing analysis across domain-specific agents, and incorporating domain knowledge. Our findings highlight the potential of knowledge-grounded, multi-agent LLMs for training-free inference of mental health changes from passive sensing data.

</details>


### 139. Multi-Agent Memory Inconsistency: Where Factual Conflicts Disappear in LLM Agents

- **Authors:** Hejia Zhang, Zhongming Yu, Yimin Ding, Wei-Ting Chen, Hengjia Yu, Wentao Ni, Yijun Liu, Cong Xu, Xin Chen, Matrix Yao, Fan Zhao, Jishen Zhao
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22245v2](http://arxiv.org/abs/2611.22245v2)
- **PDF:** [https://arxiv.org/pdf/2611.22245v2](https://arxiv.org/pdf/2611.22245v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent delegation lets LLM systems distribute evidence collection across workers with separate contexts. This creates a consistency challenge: facts retrieved by workers may be missing from the evidence available to the lead for a joint conclusion. We introduce a benchmark and evidence-flow profiler for studying multi-agent memory inconsistency through controlled factual conflicts in Harvey LAB document-review tasks. Pooled across three models with comparable generation spending, requiring delegation increases retrieval of both conflicting claims from 50.2% to 68.7% relative to single-agent execution, yet conflict detection falls from 16.2% to 13.2%. Within this setting, workers report both claims for only 35.2% of retrieved pairs, and pooled matched comparisons show higher detection than single-agent execution when one worker reads both claims but lower detection when the claims are split across workers. Worker-to-lead handoffs are a central target for improving conflict detection in multi-agent LLMs.

</details>


### 140. The Only Edge Was Memorized in Training: LLM Trading Agents Around Earnings and Bad News

- **Authors:** Jackson Wang
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22177v1](http://arxiv.org/abs/2611.22177v1)
- **PDF:** [https://arxiv.org/pdf/2611.22177v1](https://arxiv.org/pdf/2611.22177v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) trading agents are tested on news, but news reaches stock prices within minutes, and a benchmark that replays headlines at their publication time finds no alpha in trading on them. Money can then remain in two places, before news whose date is known, such as earnings announcements, and after bad news, if the market's fall went too far. However, studies of LLMs and earnings read documents published with or after the announcement, and studies of reversal sort monthly portfolios, so neither tells whether an agent can trade these moments after costs. In this paper, we test LLM agents at both moments on the same look-ahead-free benchmark, before 598 earnings announcements and after 409 bad-news drops of large US stocks. Every input is cut at the decision close, staged agents are compared with single calls, simple rules and a logistic regression, and every decision is made with and without the stock's name. Across five models from four vendors, no agent beat the simple bets. Before earnings, the agents mostly bought and earned what buying before every announcement earned, and after bad news, a Gemini-based agent called almost every fall an overreaction while no agent picked better dips than buying them all. The only gains came from what the models had memorized in training. Given only the ticker and the dates, a GPT-based model called the direction of 59.2% of the announcements before its training cutoff and 53.3% after it. Agent builders should therefore compare an event agent with the simple bet and test it blind after the training cutoff.

</details>


### 141. Readie: Low-Latency Code Sandboxes for AI Agents

- **Authors:** Arjun Sivaraman, Zhaoheng Li, Alan Shi, Sanjay Malisetty, Eugene Wu, Yongjoo Park
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22171v1](http://arxiv.org/abs/2611.22171v1)
- **PDF:** [https://arxiv.org/pdf/2611.22171v1](https://arxiv.org/pdf/2611.22171v1)
- **Categories:** cs.AI, cs.DB, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

From quantitative research to personal assistance, AI agents act by iteratively generating and executing code. To decouple the agent harness from code execution, many agents offload execution to dedicated systems called code sandboxes. However, existing code sandboxes suffer from slow startup. Whether they rely on custom snapshots or a single fat image, the root cause is the same: it is hard to build a compact, pre-warmed snapshot that can be shared across diverse agent-generated code while covering nearly all the artifacts (e.g., packages, datasets) it requires.
  In this work, we propose learned startup snapshots for low-latency code sandboxes. Our insight is that while it is hard for a single snapshot to be both compact and cover most workloads, a set of snapshots can achieve both. Each snapshot is small, initializes quickly, and covers a fraction of agent-generated code; together, the set covers most of it. We learn this set from a large training workload by formulating snapshot construction as an optimization problem and solving it with an approximation algorithm. Planned on 15K public and LLM-synthesized scripts, our system, Readie, reduces startup latency by 3-22$\times$ and end-to-end runtime by 1.3-3.3$\times$ compared to existing approaches at the same storage budget.

</details>


### 142. Not All Evidence Is Admissible: Evidence Governance for Tool-Augmented Medical Agents

- **Authors:** Runxun Zhang, Onofrio Antonio Catalano, Jinqiao Wang, Jingwei Wei
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22169v1](http://arxiv.org/abs/2611.22169v1)
- **PDF:** [https://arxiv.org/pdf/2611.22169v1](https://arxiv.org/pdf/2611.22169v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-augmented medical agents treat whatever their tools return as evidence. We show that this default is costly: medical tools fail silently, and a frozen reasoner cannot ignore what enters its context, so many cases it would have answered correctly are flipped to wrong once tool outputs are added. We call this evidence hijacking. $\mathcal{V}$-information explains the phenomenon: the reasoner has lost the option to ignore, so a tool output can carry negative usable information, and moving the decision of what to keep outside the reasoner restores that option. The theory further shows that part of any filtering gain comes merely from letting the reasoner see less, and only selection by content lets it see better. Building on this, we recast tool-augmented reasoning as evidence governance, which separates deciding what counts as evidence from the reasoner that answers, and propose context-independent evidence governance (CIEG), the first medical agent framework that rules, after acquisition, on whether each individual tool output may enter as evidence. Every tool output is written as a card that can be checked against the raw input; an independent checker that sees only the input and the cards decides which cards become evidence; and the reasoner answers from the admitted cards alone, with no training anywhere. On medical question answering, fundus glaucoma screening, and chest X-ray pneumonia classification, it achieves the highest accuracy among models of comparable scale, and significantly outperforms state-of-the-art tool-using agents and multi-agent systems built on the same backbone at lower cost.

</details>


### 143. What RL on Expert-Built Tasks Teaches Nemotron 3.5 Super

- **Authors:** Sushant Mehta, Edwin Chen
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22161v1](http://arxiv.org/abs/2611.22161v1)
- **PDF:** [https://arxiv.org/pdf/2611.22161v1](https://arxiv.org/pdf/2611.22161v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

We post-train NVIDIA's Nemotron 3.5 Super (120B total, 12B active parameters) with reinforcement learning (RL) on five expert-built task datasets, one at a time: real-world software engineering, complex constraints, long-horizon tool use, professional chart understanding and enterprise document reasoning. Each run trains a fresh rank-32 LoRA adapter with CISPO on Tinker, with no supervised stage, and each adapter is compared with the base model on the same tasks, harness and settings. On twelve headline benchmarks, eight built by other groups and four by Surge AI, the gains range from +4.5 points on IFBench to +13.8 on GDP_pdf, which rises from 10.4% to 24.2%; SWE-bench Pro V2 rises from 86.9% to 92.1%, Terminal-Bench 2.1 from 63.9% to 70.3%, MultiChallenge from 58.3% to 66.6%, AutomationBench from 14.8% to 27.5% and Chartography from 39.4% to 50.6%. The document adapter, trained without API tools, also gains +8.0 points on AutomationBench. In attempts read side by side with the base model's on tasks each adapter newly solves, the base model's failures recur in a few modes, and each adapter does more often what the base model missed: the tool-use adapter finds the data and the rules before acting, the coding adapter writes its own test or scratch files on SWE-bench Pro V2, the constraints adapter carries earlier turns into its answers, the chart adapter measures the marks in code, and the document adapter reads AutomationBench's spreadsheets.

</details>


### 144. RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time

- **Authors:** Changxuan Fan, Zhongwei Xie, Boyi Zhang, Shaoli Hu, Chang Xu, Xiyu Ren, Yufei Li, Qiao Xiao, Huihao Jing, Kawai Chung, Wenbin Hu, Hongyu Luo, Lingyun Xie, Yisen Gao, Chunyang Li, Haoyu Huang, Wuganjing Song, Yuxuan Liu, Chiu Yeung Tang, Fangneng Zhan, Xi Yang
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22138v1](http://arxiv.org/abs/2611.22138v1)
- **PDF:** [https://arxiv.org/pdf/2611.22138v1](https://arxiv.org/pdf/2611.22138v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal agents can now control robot arms by calling tools and writing code. Existing benchmarks fall short in three ways: most test one or two arms on short tasks, many pause the world while the agent thinks, and many give it ground-truth object positions. We present RoboTeam, a simulated benchmark where agents control 4 to 16 robot arms in real time from camera images alone. Its 36 tasks are long jobs that the arms must do together, such as passing timbers or building a picture from hundreds of cubes. We start from the most flexible agent system, the adaptive system, where one agent decides when to fork delegates. With it, gpt-6.1-sol and opus-5.5 complete 28 and 27 tasks, and four other models at most 3. But at a high price: a typical task takes gpt-6.1-sol 3.5 hours and 218 million input tokens, and a third of its steps fail at least once and must be retried. We then compare it with three fixed systems: single-agent, hierarchical, and decentralized. All four complete a similar number of tasks but differ in time and tokens. The hierarchical and decentralized systems are faster but use up to 1.9 times the tokens, and the single agent uses fewer tokens but takes 1.6 times as long, so the adaptive system lies between them. Even so, no model or system is yet fast, cheap, and reliable at once. RoboTeam measures these limits where earlier benchmarks cannot: long multi-arm jobs, camera images only, and a world that never pauses.

</details>


### 145. RegimeCouncil: Paired-Evidence Routing For Memory Conflict Governance In LLM Agents

- **Authors:** Qingcan Kang, Mingyang Liu, Shixiong Kai, Tao Zhong, Mingxuan Yuan
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22113v2](http://arxiv.org/abs/2611.22113v2)
- **PDF:** [https://arxiv.org/pdf/2611.22113v2](https://arxiv.org/pdf/2611.22113v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Alongside memory storage and retrieval, a fundamental challenge in long-term LLM agent systems is how the agent should act when stored memories conflict with an evolving world. Facts often go stale without explicit deletion, so the conflict surfaces before the store is refreshed: delayed feedback shows that acting on one outdated record hurt, but not whether suppression should stay on that fact (a local policy) or extend to other stored facts (a global policy). Existing systems hard-code one of these scopes at design time. We formulate this online choice, under hidden validity and delayed feedback, as memory conflict governance, and propose RegimeCouncil, a lightweight router that keeps both scopes as advisors and arbitrates between them without retraining the LLM. Each memory-assisted response is scored against a no-memory anchor, by off-path paired comparison or by inverse-propensity estimation from the executed action alone. A Local Advisor tracks only the queried fact, a Global Advisor pools recent outcomes across the store, and an asymmetric Meta Governor follows Local by default, switching to Global only when pooling yields a strictly positive recent utility margin. We prove that using delayed outcomes escapes the prompt-only regret floor, that neither fixed scope suffices alone, and that this margin gate switches within bounded time. On LongMemEval streams, historical drift in TempLAMA and TAQA, delays $τ\in [1, 96]$, and sparse or bandit feedback, with Qwen3-30B-A3B and GPT-4o, RegimeCouncil outperforms the better fixed scope in all 30 held-out settings, by 5.2-7.3 points on disagreement episodes and +27.9 points over standalone cold-start fallback under clustered shifts, while cutting harmful stale-memory use at microsecond overhead.

</details>


### 146. ATLAS-Finance: Benchmarking AI Agents in Realistic Banking Environments

- **Authors:** Elaine Lau, Antoine Pangas, Alexandre Finot, Collin Schweiker, Amir Bouzidi, Hui Wen Goh, Andrew Peter Martin, Jonas Mueller
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22085v1](http://arxiv.org/abs/2611.22085v1)
- **PDF:** [https://arxiv.org/pdf/2611.22085v1](https://arxiv.org/pdf/2611.22085v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Professional work involves under-specified assignments, where relevant information is spread across workplace applications and may conflict or change over time. To evaluate how well frontier agents can perform economically valuable work in such settings, we introduce ATLAS-Finance, a benchmark of 100 end-to-end investment-banking tasks across 13 simulated firms. As in real banking workflows, agents must search email, chat, calendars, notes, and files to identify requirements, gather information, reconcile conflicts/updates, and then build complex financial models. Tasks were developed by experienced bankers based on their real deal work and take them 15-30 hours to complete. Agent deliverables are evaluated with expert-authored rubrics (median: 124.5 criteria) covering financial rationale and results, spreadsheet construction, completeness, and formatting. Despite completing substantial portions of the requested work, current agents rarely produce correct deliverables. Across today's frontier models, the best ones (Claude Opus and Fable) pass fewer than 11% of tasks.

</details>


### 147. Can You Undo It? Reversibility Classes for AI Agent Actions

- **Authors:** Deepak Waghmare, Shaad Sufi
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22075v1](http://arxiv.org/abs/2611.22075v1)
- **PDF:** [https://arxiv.org/pdf/2611.22075v1](https://arxiv.org/pdf/2611.22075v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using AI agents change files, databases, access rights and public information, yet permission to call a tool does not establish whether a mistake can be undone. We present Reversibility Classes, a declared five-level vocabulary with argument-sensitive rules, conservative defaults and an explicit prior-state capture contract. The pinned implementation and evidence-linked registry cover 536 tools across 20 MCP servers. All 738 rule-case checks conform to declared expectations, while native annotation mapping differs from draft registry labels for 118 of 481 comparable tools. One AI-assisted reviewer approves 148 ratings, 75 matching the registry; this is not independent agreement. On 2,158 recorded runs, the implemented session guard gates the associated action in all 29 attributable attack-positive runs, compared with 18 for a read/write proxy, while adding nine approval points across 1,209 benign runs. Controlled file, Git, SQLite and three-browser experiments show that recovery depends on captured state, later changes, editor storage and recovery route, and expose a Git merge-state exception. The evidence supports making recovery assumptions explicit and testable. It does not establish registry-wide accuracy, reduced production harm or general recovery reliability.

</details>


### 148. Addressing Exogenous Variability in Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Seongmin Kim, Woohyeon Byeon, Jiwon Jeon, Seungyul Han, Youngchul Sung
- **Published:** 2026-11-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.22067v1](http://arxiv.org/abs/2611.22067v1)
- **PDF:** [https://arxiv.org/pdf/2611.22067v1](https://arxiv.org/pdf/2611.22067v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) often fails under exogenous variability such as shifts in opponents or environment regimes that cannot be controlled by the team but alter the transition dynamics. We formalize this challenge as Exogenous Dec-POMDP (ED-POMDP), in which an episode-level exogenous regime, selected independently of the team, indexes the dynamics, and the global state is partitioned into components that are directly responsive to the current team action and components that are not directly action-responsive at the current step. This formulation exposes mediated influence: while team actions do not directly update the latter at the current step, they can shape their later evolution through induced changes in the former. Based on this, we propose LEICA, a CTDE-compatible algorithm that learns history-conditioned context representations for both components and shapes policy updates using agent-wise, influence-weighted counterfactual intrinsic rewards. Across SMAX benchmarks with opponent strategy shifts, LEICA consistently improves both training performance and generalization to unseen opponents' strategies over existing baselines, supporting the usefulness of influence-weighted shaping under exogenous train-test regime shifts.

</details>


### 149. WebAgents: Unbundling Agent Creation, Hosting, and Execution for an Agent-Native Web

- **Authors:** Dario Fenoglio, Martin Gjoreski, Marc Langheinrich, Pradyumna Chari, Ramesh Raskar
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21978v1](http://arxiv.org/abs/2611.21978v1)
- **PDF:** [https://arxiv.org/pdf/2611.21978v1](https://arxiv.org/pdf/2611.21978v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are moving from isolated assistants toward autonomous agents that can plan, use tools, and coordinate with others, motivating an emerging Agentic Web of independently developed agents and services. Realizing this vision requires agent behavior to move across creators, hosts, and runtimes without coupling publication to a particular execution environment or transferring authority over user resources. We introduce WebAgents, which unbundles these roles through a signed agent.pkg that carries portable workflows, skills, schemas, and resource requirements. An OpenClaw-based agent-native browser/runtime verifies the package, obtains authorization, and binds it at run time to user-controlled models, tools, permissions, and budgets, while hosts distribute the public program and may retain private services server-side. We demonstrate this contract with three unrelated workflows executed unchanged under local and API-backed models, including literature review with live services and a website-published travel agent using semantic tools and user-selected personal resources. In a controlled suite, WebAgents explicitly blocks all 716 injected contract violations while accepting all 295 matched benign controls, with median automated pre-execution processing below 0.5 s for all three packages. We conclude by outlining a path toward NANDA-based discovery and interoperable package ecosystems while retaining execution authority in the user's runtime.

</details>


### 150. DiscoveryAgent: A Framework for Scientist-centric Agentic AI

- **Authors:** Owen Queen, Ioana Ciuca, Emma Dann, Jean Somalwar, Carine You, Steven Dillmann, Viraj Manwadkar, Evan Gorrell, Harrison G Zhang, Jonathan K Pritchard, Risa H Wechsler, James Zou
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21950v1](http://arxiv.org/abs/2611.21950v1)
- **PDF:** [https://arxiv.org/pdf/2611.21950v1](https://arxiv.org/pdf/2611.21950v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can assist scientific research, but balancing autonomous investigation with scientists' ability to inspect and redirect ongoing work remains a central design challenge. We present DiscoveryAgent, a domain-agnostic, scientist-centric system that combines autonomous investigation with scientist-directed hypothesis steering. Scientists select, refine, or replace hypotheses between research rounds, while audit agents interrogate checkpointed records to trace claims, reproduce analyses, and inform subsequent decisions. Across two predictive modeling tasks, DiscoveryAgent produced the best variable-star classifier among evaluated baselines and, with scientist steering, a protein variant-effect predictor surpassed by only one of 106 ProteinGym baselines. We develop a rigorous checkpointing system that enables highly capable audit agents, a scalable form of oversight for agentic research. Audit agents autonomously identify errors at higher rates than previous AI scientist agents, and scientists collaborating with audit agents identify 14x more valid errors versus scientists performing manual review. In three case studies led by domain experts across physical science, social science, and life science, we developed a multimodal photometric-redshift estimator that resolves complementary failures of images and photometry, achieving 0.971 AUROC for low-redshift classification; documented an 83% rise in Florida homeowners-insurance premiums from 2013 to 2023, with a growing, regressive burden; and identified CD4+ T-cell relay genes, which both receive and exert broad transcriptional regulation, enriched for autoimmune disease associations. Together, these results show how autonomous research can expand scientists' empirical reach while centering their authority over research direction and their ability to understand and challenge the evidence.

</details>


### 151. EmbedGym: Letting Coding Agents Develop and Debug Embedded Firmware Without Physical Hardware

- **Authors:** Minghui Zhao, Yiming Li, Sophie Zhu, Maxwell Khor, Lauren Ouyang, Hai "Helen" Li, Yiran Chen, Tingjun Chen
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21845v1](http://arxiv.org/abs/2611.21845v1)
- **PDF:** [https://arxiv.org/pdf/2611.21845v1](https://arxiv.org/pdf/2611.21845v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern coding agents perform well on general software benchmarks because they can run code and unit tests in a closed loop. Embedded firmware development, however, breaks this loop: a program that compiles can still fail on real hardware due to pin polarity, bus protocol, timing, or networking bugs that an agent at a text terminal cannot observe. Existing embedded coding agents either skip hardware execution, drive GPIO-only simulators with multi-second delays, or test on physical boards in a static environment. In this paper, we present EmbedGym, an interactive virtual hardware environment that lets coding agents develop and debug embedded firmware without physical hardware. EmbedGym uses instruction-level microcontroller unit (MCU) emulators to execute the same binary that would be flashed onto a physical board, connects them to 41 peripheral models, an analog circuit simulator, and virtual WiFi/Bluetooth Low Energy (BLE) endpoints, and exposes an interface for agents to change sensor inputs, press buttons, and inspect hardware states. On top of it, we build EmbedGym-Bench, which consists of 598 tasks across 6 MCU-framework pairs graded by hidden timed test vectors, using a five-stage multi-agent workflow that synthesizes peripheral models and tasks from datasheets and driver libraries. We expose EmbedGym to a coding agent at three levels and evaluate eight models over more than 14K trajectories. Even when compilation succeeds 99.7% of the time, 19.9% of compiled firmwares fail at runtime (up to 73% on individual targets). In contrast, interactive hardware testing in EmbedGym increases pass rates across models by +4.9% to +14.7% (up to +31% on individual targets). Our results also show that an agent with EmbedGym outperforms prior embedded agent frameworks, and lightweight models with EmbedGym match frontier models without it at 30-70x lower cost.

</details>


### 152. Coordination of Heterogeneous Teams with Uncertain Task Requirements

- **Authors:** Jongann Lee, Melkior Ornik
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21828v1](http://arxiv.org/abs/2611.21828v1)
- **PDF:** [https://arxiv.org/pdf/2611.21828v1](https://arxiv.org/pdf/2611.21828v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordinating a team of heterogeneous agents to complete tasks with unknown requirements is a challenging multi-agent planning problem. Agents differ in their ability to discover task requirements and in their ability to engage tasks, so the planner must coordinate task discovery, execution, and staging. This paper introduces a hierarchical planner that uses a graph neural network policy to assign actions to agents, then finds a path to the action's location using a shortest-path algorithm. The central part of our approach is the CAAT graph, which is a graph representation of the planning context consisting of the agents, tasks, capabilities, and actions. We demonstrate that our learned planner can jointly coordinate a heterogeneous team to simultaneously discover task requirements and complete tasks in a shorter time compared to baselines that optimize task discovery and task engagement independently. Furthermore, we show that our policy can zero-shot plan on out-of-distribution settings by training only on an outdoor map then transferring without finetuning to an indoor map with more agents, tasks, and capabilities than seen during training.

</details>


### 153. Corrupting Ties: Investigating Robustness to Bias Injection Across Multi-Agent Network Topologies

- **Authors:** Cléa Chataigner, Mina Arzaghi, Florian Carichon, Pablo Piantanida, Golnoosh Farnadi
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21804v1](http://arxiv.org/abs/2611.21804v1)
- **PDF:** [https://arxiv.org/pdf/2611.21804v1](https://arxiv.org/pdf/2611.21804v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI systems are increasingly deployed in high-stakes decision-making contexts, where interactions among components can introduce fairness risks that remain undetected when auditing components or collective outcomes in isolation. As LLM-based multi-agent systems become more prevalent, understanding how biased information propagates through agent interactions is essential for assessing their fairness. We introduce a controlled bias injection framework that replaces selected agent responses with predefined biased ones, enabling an intervention-based analysis of how network topology and injection configurations shape system behavior. We propose decision divergence metrics that quantify the effects of these interventions at the agent, network, and system levels, and evaluate five topologies on three binary classification tasks using LLMs from the Qwen and Gemma families. Sequential networks show the greatest divergence, whereas fully connected and mesh networks show less. Injection position also matters: in star networks, injecting the central agent has larger effects than injecting peripheral agents. Models further differ in whether divergence follows the injected bias. These findings highlight the role of network structure in the propagation of biased information and motivate topology-aware auditing of fairness risks in multi-agent systems.

</details>


### 154. Controllable Chains of Thought Can Reveal Less, Even Without Evasion Training

- **Authors:** Zheng-Xin Yong, Benjamin Arnav, Miles Wang, Tomek Korbak, Olivia Watkins
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21799v2](http://arxiv.org/abs/2611.21799v2)
- **PDF:** [https://arxiv.org/pdf/2611.21799v2](https://arxiv.org/pdf/2611.21799v2)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chain-of-thought (CoT) monitoring is a promising tool for detecting hidden goals, off-task behavior, and other failures in AI agents. One risk is that models could deliberately shape their reasoning to make it opaque to monitors. We stress-test this risk through persona-control training: supervised fine-tuning on mathematical reasoning traces rewritten in the voices of diverse personas. This induces a broader ability to control CoT, even though training contains no monitor-evasion examples. In covert side-task evaluations, traces in which a gpt-oss-20b model organism completes the hidden side task contain less monitorable evidence than the base model's. Averaged across evaluations and CoT lengths, weighted by side-task-success counts, the CoT monitorability metric g-mean$^2$ falls from 0.94 for the base model to 0.68 for the model organism without a hiding instruction, and to 0.22 when explicitly instructed to hide. In intervention evaluations, explicit hiding often drives monitorability near zero. The effect extends to a Kimi-K2.6 model organism in agentic environments, though hidden objectives requiring extended reasoning or longer trajectories remain more monitorable than simple single-step side tasks. We further discover that targeted transparency prompts can substantially recover monitorability, sometimes surpassing the base model. These model organisms provide a testbed for studying monitorability failures and potential mitigations. Our code can be found on https://github.com/yongzx/cot-control-model-organism.

</details>


### 155. Revisiting the Survival of Agent-Attributed Code: How Measurement Choices Decide the Verdict

- **Authors:** Musfiqur Rahman, Mahi Begoug, Emad Shihab
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21784v2](http://arxiv.org/abs/2611.21784v2)
- **PDF:** [https://arxiv.org/pdf/2611.21784v2](https://arxiv.org/pdf/2611.21784v2)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Studies of how long code from AI coding agents survives after it is merged reach conflicting verdicts: agent code is reported to be retained longer than human code, about as long, or modified sooner. Each study makes defensible measurement choices, but how much these choices decide the verdict is unknown. We revisit the survival of agent-attributed code in our earlier study: 854,139 lines that 2,802 merged pull requests (PRs) added to 215 repositories of the AIDev dataset. We vary nine measurement choices in five research questions and build a specification curve of 88 survival analyses, tested under three variance estimators, several observation windows, and permuted labels. For code from human-supervised agents, mostly GitHub Copilot, the choices change the size of the effect but not its direction. For code from the fully-autonomous agent Devin, they decide the verdict. Across repositories, 15 of 22 specifications report it modified sooner when lines are treated as independent, but only 3 when standard errors are clustered by repository, no more than permuted labels produce. Within repositories, no specification detects a difference. LLM intent classifiers agree with human labels about as well as two humans agree with each other, whereas keyword rules do not (kappa = 0.69 to 0.72 against 0.38), and the two reach different verdicts on why agent code is modified. Humans make most modifications to agent code under every unit and window. Re-run on our data, five published designs each change their result with a single choice. Whether agent code survives longer than human code is therefore decided as much by the measurement as by the code. We derive an operationalization checklist for post-merge studies.

</details>


### 156. ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization

- **Authors:** Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi, Zhichao Xu, Jiaxin Qin, Guoshenghui Zhao, Baijian Yang, Yingjie Victor Chen, Tan Yu, Weijie Zhao
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21605v1](http://arxiv.org/abs/2611.21605v1)
- **PDF:** [https://arxiv.org/pdf/2611.21605v1](https://arxiv.org/pdf/2611.21605v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Visual agents answer questions about ultra-high-resolution photos by zooming into the relevant regions. However, existing agents often answer from common sense instead of reading the evidence. Reinforcement learning (RL) on the final answer cannot correct this, because a guess earns the same reward as reading. We propose Cross-Input Relative Policy Optimization (CrossRPO), which trains agents on contrast sets. A contrast set asks one question about several versions of an image that differ only in a small region with the evidence and have different answers, so only reading the evidence solves the whole set. CrossRPO rewards solving the whole set, and we prove that it does not reinforce a set answered from common sense. We build contrast sets for training (ViRA-Train) and evaluation (ViRA-Bench) by editing one small object in images of 21 to 120 megapixels, and we photograph further sets with real changes (ViRA-Bench-Real) to exclude editing traces. We train two Visual Reasoning Agents, ViRA-9B and ViRA-27B, with CrossRPO on only about 3,500 items of ViRA-Train each. CrossRPO achieves 63.3% set accuracy on ViRA-Bench at the maximum resolution, against 59.3% for GRPO. ViRA-9B is the most accurate open model of its size on all benchmarks, and ViRA-27B outperforms Claude Haiku 5.5 and GPT-6-Luna, both at their highest thinking level, on most benchmarks.

</details>


### 157. When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents

- **Authors:** Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21577v1](http://arxiv.org/abs/2611.21577v1)
- **PDF:** [https://arxiv.org/pdf/2611.21577v1](https://arxiv.org/pdf/2611.21577v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) applications increasingly act as agents that select and invoke external tools. The Model Context Protocol (MCP) standardizes this interaction by allowing clients to compose tools advertised by multiple servers. However, tool metadata used for discovery and selection is not, by itself, necessarily bound to a verified provider identity. This paper studies this gap as tool-provider misbinding: a failure in which a request intended for a legitimate provider is instead resolved to an attacker-controlled tool. The attacker does not compromise the host, LLM, legitimate server, or network channel; it only operates another MCP server that advertises tools with chosen metadata. We formulate tool provider misbinding as an attacker-controlled tool-selection optimization problem and evaluate it in a controlled MCP environment across five LLM-based clients. The results show that interactions drive misbinding. The strongest failures occur when exact-name collision, task-aligned description, and compatible schema reinforce one another, but authority-enhanced descriptions with compatible schema can also cause wrong-provider execution or unresolved provider ambiguity without name collision. Different models expose the same provider-binding weakness differently, including attacker-controlled provider selection, clarification requests, and unstable or inconsistent provider resolution.

</details>


### 158. Safe Resemblance, Silent Propagation: Limits of Text-Similarity Guardrails for AI Agent Safety

- **Authors:** Charles Xiao
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21520v1](http://arxiv.org/abs/2611.21520v1)
- **PDF:** [https://arxiv.org/pdf/2611.21520v1](https://arxiv.org/pdf/2611.21520v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When AI agents relay information to one another, an output can preserve an injected instruction's effect on downstream agents even after its wording changes, yet legitimate quotation and template reuse can produce high textual overlap with the source, so text-similarity guardrails that attempt to flag the former risk conflating these two cases. We test this distinction using DonkeyRail, a public classifier combining BLEU, ROUGE-L, and METEOR features, deployed in a controlled three-agent email relay, defining a behavioral measure in which an output counts as functional (the injected procedure induces fresh computations in two subsequent agents) independent of the detector's score, alongside legitimate controls that explicitly authorize quotation and reuse. At its default threshold the classifier misses 8 of 19 functional outputs while flagging 70 of 192 legitimate replies, with every completed quotation and template-reuse reply triggering a false alert; calibrating for low false positives on one template set does not transfer, as the recalibrated threshold detects only one functional output and still produces 15 false alerts on new templates. We also identify an operating-point error in all 21 published classifier configurations, where ROC interpolation replaces direct threshold application, and show formally that high AUC against a surface-level text criterion provides no distribution-free guarantee of high AUC against the behavioral target, while the existing evaluation labels lack the joint observations needed to estimate the gap. An authorization analysis further shows that identical visible transcripts can require different safety decisions depending on the governing policy, a distinction no observation-only classifier can resolve. These results argue for behavioral and policy-grounded evaluation over text-similarity guardrails.

</details>


### 159. Efficient Modeling of Multi-Agent Systems via Structure-Aware Physics-Informed Learning

- **Authors:** Yulun Wu, Nicola Bastianello, Karl Henrik Johansson, Matthieu Barreau
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21404v1](http://arxiv.org/abs/2611.21404v1)
- **PDF:** [https://arxiv.org/pdf/2611.21404v1](https://arxiv.org/pdf/2611.21404v1)
- **Categories:** cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modeling large multi-agent systems poses challenges for trajectory inference and parameter identification, as network size and coupling increase computational demands and partial observations require reconstructing unobserved states. We propose MAS-PINN, a neural-network architecture with a tailored training algorithm for a physics-informed learning framework that leverages the network topology and the agents' similarity to reduce computational and memory costs of simulating and identifying multi-agent systems. Its architecture represents agent trajectories through shared temporal features and agent-specific coefficients. Training alternates between learning features, fitting coupled trajectories, and estimating physical parameters. A matrix-free update exploits local interactions to fit trajectories without forming large global matrices. Experiments on Lorenz rings, Lotka--Volterra networks, and Rössler oscillators show improved trajectory and parameter accuracy over baselines, including inference in large systems and identification under partial observations or unknown topology, alongside substantial computational savings in coefficient fitting.

</details>


### 160. A Crowd-Audited Atlas of Implicit Bias in LLM-Powered Agents

- **Authors:** Jason Alexander, Yuxuan Li, Michael Licamele, Wesley Hanwen Deng, Sauvik Das
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21376v1](http://arxiv.org/abs/2611.21376v1)
- **PDF:** [https://arxiv.org/pdf/2611.21376v1](https://arxiv.org/pdf/2611.21376v1)
- **Categories:** cs.CY, cs.CL, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prior work has shown that large language models (LLMs) express implicit biases in high-publicity, one-off decision scenarios such as hiring and intelligence assessment. However, as people increasingly employ autonomous, LLM-powered AI agents that make decisions on their behalf in doing day-to-day tasks, it is of critical importance that we understand how implicit biases, based on sociodemographic assumptions, emerge across a broad milieu of workaday decision scenarios. We used the 17 domains of daily activity in the American Time Use Survey (ATUS) to generate an atlas of 506 decision scenarios in which LLMs --- endowed with personas representing different races, gender identities, and political ideologies --- expressed significant implicit bias. Next, in a crowdsourced audit, 500 participants made 8,010 binary choices about which implicitly biased decision scenarios most deserved further review. We found that participants prioritized decision scenarios that had broad relevance (e.g., about food choices), were high stakes (e.g., about health), and where all members of a simulated sociodemographic group made unanimous decisions (because it was a clear indication of stereotyping). They were less swayed by the magnitude of an observed disparity or the specific ATUS domain the decision scenario represented. When examining the rationale behind their prioritization choices, we found that participants often interpreted disparities as traits of demographic groups and judged whether those traits seemed plausible, often based on their own internalized stereotypes. We discuss implications for building personalized AI agents, digital twins, social simulations, and for using crowdsourced bias audits.

</details>


### 161. WeVisForensics: Self-Evolving Agent for Omni AI-Generated Video Detection

- **Authors:** Yipeng Du, Yuxi Li, Ying Zhang, Chong Sun, Chen Li, Jing Lyu, Ying Tai
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21373v1](http://arxiv.org/abs/2611.21373v1)
- **PDF:** [https://arxiv.org/pdf/2611.21373v1](https://arxiv.org/pdf/2611.21373v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in video generation call for reliable detection grounded in explicit forensic evidence. However, current methods primarily depend on single-pass chain-of-thought reasoning that overlooks brief or localized artifacts, or on predefined multi-agent workflows that offer limited flexibility in selecting relevant inspections. Even with adaptive investigation, optimizing the investigation policy alone does not directly improve the forensic capabilities of fixed experts. We introduce WeVisForensics, an agentic framework in which a main investigator agent coordinates a self-evolving library of forensic inspector sub-agents spanning visual and audio cues. The investigator learns which artifact type to examine, over which window, and when to conclude, and these interactions provide shared feedback for both levels of agents. Our dual-timescale policy optimization strategy, DTPO, closes this loop through fast reinforcement learning of the investigator and slower refinement of the inspectors, guided by annotated artifact intervals, to report subtle artifacts they once dismissed. Furthermore, we curate ForenCue-30K, combining role-specific forensic annotations and interaction trajectories to supervise individual inspections and their coordination, with an accompanying reinforcement-learning pool. Experiments show that WeVisForensics averages 95.2% detection accuracy across in-domain, out-of-domain and agentic benchmarks, 9.0% above the strongest prior detector, while grounding its verdicts in localized evidence.

</details>


### 162. Agent-Native by Design: A Programming Language for Agentic Applications

- **Authors:** Jayanaka Dantanarayana, Savini Kashmira, Xiaoyu Ma,  Malitha, Malitha Prabhashana, Lingjia Tang, Jason Mars
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21298v1](http://arxiv.org/abs/2611.21298v1)
- **PDF:** [https://arxiv.org/pdf/2611.21298v1](https://arxiv.org/pdf/2611.21298v1)
- **Categories:** cs.PL, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Building agentic applications requires combining large language model (LLM) operations, workflow structure and application state, and model-guided routing. With SDKs and agent frameworks, developers connect these components through supporting code that prepares model inputs, propagates state, and dispatches model-selected steps. Workflow changes can require coordinated updates to this code, increasing development and testing effort. Splitting execution logic between application code and framework internals also limits compiler visibility into control flow and state dependencies, hindering automatic optimization. We introduce Agent-Native Programming, which unifies these three components with shared execution semantics. We realize this approach in Jac, a Python-superset language, through "by llm()" for typed model operations and tool use, Object-Spatial Programming for workflow structure and state, and "visit ... by llm()" for model-guided routing. The routing construct derives the model's choices from executable workflow steps and schedules the selected steps. This explicit connection between model decisions and program execution gives the compiler and runtime a common basis for dependency analysis and automatic optimization. Across five benchmarks and five baselines, Jac achieves a 1.8-8.7x reduction in AI-integration code relative to the OpenAI SDK, with competitive observed task quality and lower coding-agent development effort. Two case studies demonstrate speculative execution and service partitioning through configuration alone, using program analysis and runtime checks to preserve workflow behavior under stated conditions.

</details>


### 163. Even Loose Proximity Constraints Make Makespan-optimal Unlabeled Multi-agent Pathfinding Hard

- **Authors:** Takahiro Suzuki, Keisuke Okumura
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21277v2](http://arxiv.org/abs/2611.21277v2)
- **PDF:** [https://arxiv.org/pdf/2611.21277v2](https://arxiv.org/pdf/2611.21277v2)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study $r$-Connected Unlabeled Multi-agent Pathfinding ($r$CUMAPF), a variant of MAPF where interchangeable agents have a proximity range $r\in \mathbb{N}$, and agents must form a single group in a given graph $G$ through limited-range communication at all times. The problem arises in fundamental applications such as self-reconfiguration and platooning, while standard MAPF does not capture proximity constraints. For the problem of finding a makespan-optimal solution, prior work shows NP-hardness for $r=1$ and polynomial-time solvability when $r$ is sufficiently large; the complexity for the intermediate case $2\le r$ is largely unknown. To narrow this gap, we show that finding a solution to $r$CUMAPF with makespan at most $2$ is NP-hard for $2\le r= O(|V|^{1-\varepsilon})$, where $0<\varepsilon\le 1$ is a fixed constant and $|V|$ is the number of vertices. As a consequence, we show that the labeled analogue of $r$CUMAPF is also NP-hard under the same condition.

</details>


### 164. CAE-Bench: Benchmarking AI Agents for Reusable CAE Solver Development

- **Authors:** Zhiyu Zhou, Tianyou Liu, Xinping Yang, Yiyao Liu, Jiayi Dong, Yihan Lin, Haokai Ye, Yifan Lu, Zeyu Dong, Yansong Li, Shengqi Zhang
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21273v1](http://arxiv.org/abs/2611.21273v1)
- **PDF:** [https://arxiv.org/pdf/2611.21273v1](https://arxiv.org/pdf/2611.21273v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We developed CAE-Bench, a benchmark to evaluate AI agents on Computer-Aided Engineering (CAE) solver development. A CAE solver is more than a PDE solver; it must be able to generalize across various inputs, such as different boundary conditions, geometries, and material properties. CAE-Bench evaluates the generalizability of AI-developed CAE solvers by providing the same task, such as a heat transfer problem, multiple cases, with each case specifying an input. The AI agent develops a solver for a fixed task using only a few public cases, and the resulting solver is then tested on held-out cases, i.e., cases it has never seen before. We evaluate 12 models across a range of reasoning settings on 80 computational tasks. Our experiments show that even if a solver developed by an AI agent performs well on the public cases, it may even get 0 score on held-out cases. For tasks such as fluid dynamics problems, even the solver developed by GPT-6 Astra performs poorly on held-out cases. A data format and an SDK for task registration are provided, so the researcher can use the benchmark on their own infrastructure. We hope that CAE-Bench will help the community to develop AI agents that can develop reusable CAE solvers that generalize to various inputs.

</details>


### 165. Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks

- **Authors:** Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta, Elisa Bertino
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21259v1](http://arxiv.org/abs/2611.21259v1)
- **PDF:** [https://arxiv.org/pdf/2611.21259v1](https://arxiv.org/pdf/2611.21259v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems extend large language models with tools, memory, and multi-agent collaboration, introducing security risks at orchestration boundaries. These risks depend on how identities are represented, operations are authorized, and instructions or information propagate between components. We evaluate LangChain, LangGraph, AutoGen, and OpenClaw through twelve experiments mapped to the OWASP Top 10 for Agentic Applications using a common LLM (gpt-4o-mini). The experiments cover prompt injection, unauthorized resource access and command execution, memory poisoning, and inter-agent trust and identity attacks. Adversarial inputs induced unauthorized tool invocation, while tool chaining, stale filesystem validation, encoded instructions, and inter-agent delegation exposed weaknesses in authorization across component boundaries. Memory poisoning showed that untrusted state can influence responses, a risk distinct from conventional access-control violations. In the evaluated protected configurations, explicit authorization, controlled capability assignment, filesystem containment, and execution safeguards prevented specific unauthorized operations. The findings emphasize preserving authorization and information-trust boundaries throughout agentic workflows rather than treating framework capabilities or model-level instructions as sufficient security guarantees.

</details>


### 166. Stream of Belief: Eliciting Collective Intelligence through Latent Belief Dynamics

- **Authors:** Yu Yao, Jiayi Dong, Yilun Du
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21250v1](http://arxiv.org/abs/2611.21250v1)
- **PDF:** [https://arxiv.org/pdf/2611.21250v1](https://arxiv.org/pdf/2611.21250v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work, we view multi-agent reasoning as a process of seeking a collective equilibrium of implicit belief dynamics and introduce Stream of Belief (SoB), where agents maintain continuous latent beliefs and iteratively refine them through communication and reflection. Our method seeks a collective belief state of a multi-agent system where further communication induces no meaningful information propagation. Through extensive experiments, we demonstrate the generalization of SoB across tasks and model families. More Broadly, our results suggest a new perspective on scaling multi-agent reasoning from belief dynamics.

</details>


### 167. Linglong Agent Service: A Runtime for Centralized Agent Reasoning and Distributed Execution

- **Authors:** Hua Zhang, Min Jiang
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21129v1](http://arxiv.org/abs/2611.21129v1)
- **PDF:** [https://arxiv.org/pdf/2611.21129v1](https://arxiv.org/pdf/2611.21129v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can use remote tools and cloud sandboxes, but integrating reasoning, session state, and heterogeneous execution sites remains a runtime design problem. We present Linglong Agent Service (agentsvc), a self-hosted HTTP service and embeddable Python runtime that treats execution site as a configurable dimension alongside model, tools, and context. A parent service retains inference orchestration, tool descriptions, and conversation history; each inference request selects one child environment for file, shell, terminal, and MCP operations. Direct HTTP and child-initiated WebSocket tunnels carry the same application interfaces, including portable request context and centrally managed updates. The normal core path requires no third-party Python packages, with an optional Windows pseudo-terminal dependency. We further present online_debugger as the process-scale special case of execution-site separation: an instrumented program submits exception evidence, executes session-scoped inspection tools inside the incident process, and resumes the same diagnostic session. Its default prompt requires failing-then-passing reproduction evidence for source changes, while runtime patch activation and failed-call recovery remain unimplemented. We explain the design through constrained expected-utility reasoning, compare concrete mechanisms with Hermes Agent, Pi, Codex, and Claude Code, and report implementation and regression-test evidence. The current evidence establishes executable contracts, not performance advantages, repair accuracy, or production recovery. The source code is open source under the MIT license at https://github.com/mz24cn/agents.

</details>


### 168. CoopDistill: Equilibrium-Guided Multi-Agent Policy Distillation for Cooperative Driving

- **Authors:** Shiyu Fang, Sheng Zhao, Jiarui Zhang, Chengkai Xu, Xiaocong Zhao, Peng Hang, Jian Sun
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21069v1](http://arxiv.org/abs/2611.21069v1)
- **PDF:** [https://arxiv.org/pdf/2611.21069v1](https://arxiv.org/pdf/2611.21069v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative driving extends autonomous driving from individual vehicle decisions to joint maneuvers that improve traffic safety and efficiency. Optimization-based methods impose safety constraints but often fix paths to simplify multi-vehicle planning, limiting spatial flexibility. Multi-agent reinforcement learning (MARL) explores alternatives through interaction, but coordinated learning and safe execution remain challenging. Their integration nevertheless faces challenges in exploration efficiency, experience allocation, and execution reliability. To address these challenges, this paper proposes CoopDistill, an equilibrium-guided multi-agent policy distillation framework. A potential-game (PG) formulation provides a fixed-path longitudinal reference, around which a residual MARL policy learns longitudinal acceleration, conflict-approach timing, and lateral path corrections. A hard-case curriculum concentrates experience on interactions that PG leaves unresolved or substantially delayed. A comparative rollout selector evaluates the joint consequences of learned corrections against PG before choosing the executed action. Experiments in merging, roundabout, and intersection scenarios compare CoopDistill with six baselines at four connected automated vehicle penetration levels. Relative to PG, success improves by 2.1--27.1 percentage points and delay decreases by 7.3--27.3\%, with no observed collisions. Code is available at https://github.com/FanGShiYuu/CoopDistill

</details>


### 169. System 1 agents: a method for local, reliable and fast agentic AI

- **Authors:** Eleftherios Tzanis, Michail E. Klontzas
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.21053v1](http://arxiv.org/abs/2611.21053v1)
- **PDF:** [https://arxiv.org/pdf/2611.21053v1](https://arxiv.org/pdf/2611.21053v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence could automate analyses of sensitive clinical data, but current agents depend on large language models (LLMs). Cloud LLMs expose patient data. Local LLMs hallucinate, and an invented value in a tool call propagates through every later step. Here we present a method to build System 1 agents: local agents that call tools without generating text. A deterministic compiler turns each tool's schema and the request into multiple-choice questions whose options come from the request and the schema, then a one-pass decision model answers them. On 1,952 requests to 157 biomedical tools, the best System 1 agent chose the right tool, or correctly declined, for 97.0% of requests, significantly ahead of all 18 local LLM-agent settings (best 95.2%). The System 1 agent filled 97.0% of 6,056 stated argument values. No System 1 call contained invented content, against 5.5-19.7% of LLM calls. The System 1 Agents framework is freely available as open-source software at https://github.com/eltzanis/SystemOneAgents.

</details>


### 170. OpenMAS-GApp: A Comprehensive Benchmark for Domain-Adaptive Multi-Agent Application Construction

- **Authors:** Xunkai Li, Kairui Yang, Jiaxi Li, Yuecong Mao, Zekai Chen, Xinle Zhang, Rong-Hua Li, Guoren Wang
- **Published:** 2026-11-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.20997v1](http://arxiv.org/abs/2611.20997v1)
- **PDF:** [https://arxiv.org/pdf/2611.20997v1](https://arxiv.org/pdf/2611.20997v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Constructing multi-agent system (MAS) applications across domains requires translating diverse requirements into executable systems, involving task decomposition, agent and tool selection, and execution organization. Existing studies have explored individual aspects of MAS construction, including agent generation, architecture design, workflow generation, and component selection. However, these methods are often developed and evaluated independently, using different task specifications, component resources, and execution settings. This makes it difficult to compare their construction capabilities or determine how they can be applied to different domains. To address this problem, we propose OpenMAS-GApp, a One-for-All benchmark for MAS application construction across diverse domains. It standardizes task inputs, component resources, construction interfaces, and execution environments to support MAS construction under consistent conditions. Within OpenMAS-GApp, we provide Graph Harness as a reference construction method that derives task dependencies, selects compatible agents and tools, and organizes their interactions into executable graphs. We evaluate construction methods across 19 benchmark datasets under 20 evaluation settings spanning four application types and four professional domains.

</details>



## Biorxiv (4 papers)


### 1. Unveiling value functions in social cognition with multi-agent inverse reinforcement learning

- **Authors:** Chen, Y., Cheng, Y., Kwak, M., Radulescu, A., Wu, H. Z.
- **Published:** 2026-11-18
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2024.10.09.617461](https://doi.org/10.1101/2024.10.09.617461)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social behavior requires individuals to consider not only their own goals but also those of others. Latent reward functions that encode such goals can be recovered from behavior using inverse reinforcement learning in single-agent settings. However, extending this to multi-agent interactions is challenging, as joint reward functions are defined over joint state spaces that grow exponentially with the number of agents. Existing approaches address this complexity by imposing restrictive assumptions on social interactions, limiting generality and interpretability. Here we show that joint reward functions governing social interactions can be efficiently represented through decomposition into individual reward maps for each agent and low-dimensional interaction terms. Building on this formulation, we introduce a general multi-agent inverse reinforcement learning framework (MAIRL) that enables scalable and interpretable inference of latent reward representations directly from behavior. In simulated social tasks with known ground-truth rewards, MAIRL recovered the rewarded states and imitated expert behavior as accurately as or better than existing multi-agent inverse reinforcement learning methods. Applying MAIRL to mouse and primate social tasks, we recover structured reward maps that reflect distinct social roles and interaction strategies during group behavior. These results establish MAIRL as a general framework for identifying latent objectives underlying multi-agent behavior across species and paradigms.

</details>


### 2. SPIDER: Contextualizing Biomedical Knowledge for Evidence-Grounded Scientific Reasoning

- **Authors:** Liu, M., Zhao, W., Chen, J., Quan, X., Wang, X., Feng, J., Zhou, X., Han, J., Zhang, Y., Wang, Y., Zhang, X., Xie, W.
- **Published:** 2026-11-18
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.11.765839](https://doi.org/10.64898/2026.11.11.765839)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Aggregated relations in biomedical knowledge graphs can obscure evidence and study conditions, complicating the distinction between scientific disagreement and contextual differences. Here we introduce SPIDER, a multi-agent framework grounding biomedical relations in literature evidence and extracting study conditions for interpretation. Applied to a graph integrating 48 databases and ontologies, SPIDER analyzed 1.95 million PubMed abstracts, adding 2.31 million previously unrepresented, literature-supported entity pairs to construct SPIDER-KG. Daily updates incorporate relations and evidence from newly indexed PubMed records. Across 89,937 evidence-supported comparisons of potentially incompatible relations, SPIDER classified 79.0% as contextual differences, and 6.1% as genuine disagreement, achieving 80.3% macro-F1 averaged across both categories against expert annotations. On SPIDER-Bench and four biomedical reasoning benchmarks, SPIDER-KG improved large language models' interpretation of evidence-supported biomedical relationships. Retrospective analysis of newly reported gene--disease relationships further demonstrated how evidence-linked knowledge can contextualize emerging discoveries. SPIDER-KG provides a reusable, incrementally extensible evidence layer for biomedical reasoning.

</details>


### 3. Pharmacolibrary: Interoperable executable models for PK, PD and PGx derived from published evidence

- **Authors:** Kulhanek, T., Denil, S., Izmirli, B., Ertaylan, G.
- **Published:** 2026-11-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.16.766960](https://doi.org/10.64898/2026.11.16.766960)

- **Categories:** pharmacology and toxicology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Published pharmacological knowledge is distributed across heterogeneous scientific literature, databases, and computational models, making systematic reuse, comparison, and reproducibility difficult. We present Pharmacolibrary v26.11, a source-traceable resource that connects pharmacokinetic (PK), pharmacodynamic (PD), and pharmacogenomic (PGx) knowledge with executable models, simulations, and interactive visualizations. A multi-agent workflow combines LLM-assisted literature retrieval and extraction with deterministic validation, ontology mapping, provenance tracking, automated model generation, and rule-based review. The system transforms published evidence and extracted parameters into executable models across Modelica, FMI, SBML, MATLAB, and CellML and provides browser-based simulations for research and education. Preliminary evaluation indicates that decomposing literature extraction into multiple stages improves parameter recovery compared with single-pass extraction and that locally deployed open-weight models can provide performance that is at least comparable with frontier commercial LLMs. Pharmacolibrary provides a foundation for scalable, auditable curation of pharmacological knowledge and for connecting published evidence to reusable computational models across research, simulation, and education.

</details>


### 4. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Orlenko, A., Venkatesan, M., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-11-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: As biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers. Result: EcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAI's multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimer's Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

</details>



## Medrxiv (2 papers)


### 1. Human-Agentic AI Collaboration Workflow for Trend Analysis of ChatGPT Applications in Healthcare

- **Authors:** Chou, P. J., Lin, Y. H., Li, E. Y.
- **Published:** 2026-11-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.11.14.26368120](https://doi.org/10.64898/2026.11.14.26368120)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundWith the rapid advancement of artificial intelligence (AI), large language models (LLMs) such as ChatGPT have demonstrated strong potential to transform healthcare research and practice. However, LLMs are probabilistic and generate inherently variable outputs, which create risk and uncertainty in healthcare applications. Therefore, analyzing the current research landscape of ChatGPT applications is imperative to understand applied techniques and related concerns and to facilitate their practical integration into healthcare information systems.

ObjectiveLeveraging LLM-based agentic AI with domain experts to analyze trends in ChatGPT healthcare applications and to examine the collaborative and interpretative capacities of LLM agents in broader contexts beyond narrowly defined topics.

MethodsThe review used a systematic search of the PubMed and Web of Science databases, following PRISMA-ScR guidelines, and focused on ChatGPT applications, associated concerns, applied techniques, and usage factors. To support the review process, an adaptive, iterative LLM-based agentic AI with a human-in-the-loop mechanism was employed for automated metadata extraction, identification, classification, and knowledge synthesis. The extracted information was subsequently used for temporal and thematic analyses, citation network construction, and main-path analysis.

ResultsAcross 192 papers, the review identified 511 ChatGPT application types, 690 concern items, and 368 influence usage factors distinct from traditional IT, achieving a metadata error rate of 1.04%. The human-agentic AI workflow enabled efficient synthesis of contextual information across studies, addressing the growing challenge of timely evidence integration in medical knowledge. The findings provide insights into the evolving trajectories of ChatGPT applications in healthcare and demonstrate the value of an expert-validated human-agentic AI workflow in supporting literature analysis and streamlining review processes.

ConclusionThis review provides a comprehensive overview of emerging ChatGPT applications, associated concerns, applied techniques, and usage factors in healthcare. The study further provides meaningful insights into the operational mechanisms of agentic AI, demonstrating the potential of human-AI collaboration for medical informatics research.

</details>


### 2. Hard to Halt: Automation Bias in Agent-Driven Sequencing Prior Authorization Workflows

- **Authors:** Nie, M., Chung, W., Waxler, J., Lee, M., Weng, C., Lewis, R., Ahimaz, P., Wang, K., Liu, C.
- **Published:** 2026-11-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.16.26355782](https://doi.org/10.64898/2026.06.16.26355782)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

PurposePrior authorization (PA) for exome or genome sequencing (ES/GS) is a time-consuming process that impedes timely rare disease diagnosis. Large language model (LLM)-based browser agents offer potential for automating these workflows, but their clinical reliability remains uncharacterized.

MethodsWe built a sandbox with a simulated ES/GS payer portal and a synthetic electronic health record (EHR) of 836 patient profiles, including compliant profiles and deficient profiles with designed issues. Gemini 3 Pro, Gemini 3 Flash, and Claude Opus 4.5 were evaluated on task completion, form accuracy, and appropriate withholding. Two replication experiments were run on 100 profiles to assess run-to-run variability of agent performance.

ResultsGemini 3 Pro (95.5%) and Claude Opus 4.5 (93.7%) completed far more tasks than Gemini 3 Flash (56.1%), consistently across runs. In the first run, all models rarely withheld deficient profiles for the correct reason (Gemini 3 Pro 0%, Gemini 3 Flash 17.3%, Claude Opus 4.5 5.2%). Replication revealed substantial variability: Gemini 3 Pros correct withholding rose to 28.8-36.8%, and only 18.0-48.0% of tasks yielded identical outcomes across all three runs. Without agentic scaffolding, Gemini 3 Pro flagged designed issues in 91.3% of deficient profiles but also halted on all compliant profiles.

ConclusionCurrent LLM-based browser agents show a systematic bias toward form submission. A modular, multi-agent architecture with human supervision may be warranted for safe clinical deployment.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*