# Weekly AI Agent Paper Report

**Generated:** 2026-09-21 16:19
**Period:** 2026-09-14 to 2026-09-20

## Summary

- **Total papers fetched:** 765
- **Papers matching keywords:** 146
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-09-07) | Change |
|--------|-----------|-----------|--------|
| Total matched | 146 | 173 | -27 |
| arxiv | 141 | 172 | -31 |
| biorxiv | 3 | 1 | +2 |
| medrxiv | 2 | 0 | +2 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (5 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. Self-organized Regulation of Group Size and Number in Natural and Artificial Collectives

- **Authors:** Zhang, T., Lee, S., Hamann, H.
- **Published:** 2026-09-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.25.746978](https://doi.org/10.64898/2026.08.25.746978)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

From animal societies to self-organizing multi-agent systems, collectives adapt their group structure to tasks and environments. However, how they determine appropriate group sizes and the number of subgroups to form remains unclear. We formulate the Group Size and Number Regulation Problem (GSNRP), which asks how individuals regulate group sizes and numbers using only local information. In a first step, we establish a graph-theoretic model demonstrating that simple following behavior suffices to form group structures that match theoretical expectations, but is insufficient for active regulation of group size and number. In a second step, we operationalize individual group-size preferences in a decentralized fission-fusion mechanism based on perceived group size. Through multi-agent simulations, we validate that this mechanism achieves stable convergence across three signaling regimes, from position-only sensing to continuous group-size communication. Using tracking data from wild white-nosed coatis (mammals in the raccoon family), we calibrate individual group-size preferences and show that the controller recovers selected group-size, subgroup-count, and transition statistics. This in-sample case study demonstrates descriptive consistency with natural fission-fusion dynamics without establishing the underlying behavioral mechanism. These results suggest that natural and engineered collectives may share local principles of perception, preference, and response for regulating group structure.

</details>


### 2. scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation

- **Authors:** Rasti-Meymandi, A., Nahali, S., Paramithiotis, E., Cheung, A. M., Dolatabadi, E.
- **Published:** 2026-09-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.10.750801](https://doi.org/10.64898/2026.09.10.750801)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Single-cell atlases now exceed 66 million cells, but turning a ranked expression profile and a free-form biological question into a reliable, evidence-grounded answer remains unsolved. Scaling a single model does not resolve this, because single-cell interpretation is a heterogeneous family of tasks whose correct answer depends on tissue, cohort, perturbation and annotation resolution. Here we present scACORN, an agentic alternative to monolithic single-cell language models that combines specialized small language models with context-engineered agent orchestration for their selection and composition at inference time. Each expert is built in two stages: domain-aligned contrastive adaptation fits a pretrained cell-to-text backbone to the transcriptomic geometry of a target dataset, and geometry-preserving specialization learns question-conditioned biological completions without eroding that geometry. A fixed orchestrating language model agent then selects and combines experts under a natural-language playbook that is itself optimized from textual feedback, with no gradient updates to the orchestrator. Across 10 Tabula Sapiens tissues, domain alignment raised transfer macro-F1 from 0.36 to 0.64 and Recall@5 from 0.87 to 0.97; specialized experts reached 0.89 mean exact-match annotation accuracy; and playbook optimization reduced unsupported gene citations from 14.5% to 3.5%. Our findings support specialization and orchestration as complementary responses to the heterogeneity and evidentiary demands of single-cell analysis.

</details>


### 3. Multi-agentic system for primer design in qPCR and LAMP diagnostics tests

- **Authors:** Lau, K. J. X.
- **Published:** 2026-09-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.15.751771](https://doi.org/10.64898/2026.09.15.751771)

- **Categories:** molecular biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Primer design is a fundamental component of molecular diagnostics in both quantitative polymerase chain reaction qPCR and loop-mediated isothermal amplification LAMP assays. However, assay design is often performed manually as nucleotide databases, sequence alignment tools and resources are found at different places on the Internet. In this study, an AI-orchestrated bioinformatics workflow was developed to automate the end-to-end qPCR and LAMP primers and probes. The workflow was implemented using LangGraph, LangChain and Biopython, where a series of specialized agents were coordinated to execute sequential bioinformatics tasks with minimal human intervention. Target sequences were then retrieved based on the user request from the National Center for Biotechnology Information nucleotide database and the requested sequence records were then subjected to multiple sequence alignment for the identification of conserved genomic regions. The multi-agentic primer design system can be used for assay development for applications in infectious disease diagnostics, outbreak surveillance and environmental monitoring. This study also demonstrates how multi-agentic systems can be combined with established bioinformatics methods to automate qPCR and LAMP assay design.

</details>


### 4. AI agents at the brain-computer interface: separating inference from control

- **Authors:** Gorenshtein, A., Omar, M., Jia, E. L., Adiniaev, Y., Daniel, O., Kruskal, J., Ahmed, M., Brook, O. R., Klang, E., Barash, Y.
- **Published:** 2026-09-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.13.26362955](https://doi.org/10.64898/2026.09.13.26362955)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

In medicine, AI agents are moving from generating text to executing actions, making uncertainty from upstream decoders a control problem. We studied this at the brain-computer interface using 1,065 episodes from 47 people with amyotrophic lateral sclerosis and five language models. Prompting agents with reconstructed decoder confidence never reduced unfaithful execution below a deterministic gate at matched coverage; two models were significantly worse. Apparent safety gains of up to 22 percentage points reflected acting less often, sometimes through invalid tool calls rather than explicit abstention. A post-hoc fair-information test gave ten models the same command vocabulary as a deterministic resolver. No direct agent arm improved on the resolver's risk-coverage frontier, but a hybrid architecture in which models proposed semantic corrections and an external gate retained admission authority extended coverage beyond the resolver in five of ten models without observed unfaithful executions. These results separate inference from control in agentic neurotechnology. Funding: A.G. and E.K. were supported in part by the Clinical and Translational Science Awards (CTSA) grant UL1TR002541 from the National Center for Advancing Translational Sciences, through the Harvard Catalyst | The Harvard Clinical and Translational Science Center Pilot Award Program. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

</details>


### 5. The Multimodal Anonymizer: a fully local multi-agent AI system for medical data deidentification

- **Authors:** Hirsch, A., Ten, F. W., Krueger, K. S., Geyer, R., Roeschl, T., Groeschel, M., Rostin, P., Eils, R., Spott, M., Prasser, F., Meyer, A., Madrid, J.
- **Published:** 2026-09-14
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.05.28.26353952](https://doi.org/10.64898/2026.05.28.26353952)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundSafe reuse of multimodal hospital data for AI development is limited by the absence of reliable, context-aware deidentification across multimodal data and longitudinal patient data. Existing approaches are largely modality-specific and can indiscriminately remove clinically important information.

MethodsWe developed the Multimodal Anonymizer, a modular, locally deployable multi-agent framework integrating multimodal large language models, task-specific neural networks and rule-based transformations. We evaluated 16 orchestrator model configurations on a benchmark built from publicly available data and hospital data from our institution. The benchmark dataset included data from different origins: 250 MIMIC-IV patients with synthetically injected personally identifiable information (PII) supplemented with head CT, face images, handwriting, audio, German clinical-text datasets and local data. Primary outcomes were deidentification sensitivity and preservation of clinically important content; secondary analyses examined model characteristics, reproducibility, and performance against leading market and open-source solutions.

ResultsThe best local configuration--the orchestrator being Qwen3-VL-235B-A22B-Thinking--achieved near-complete deidentification across all datasets, with per-patient sensitivity of 98.80% (95%-CI 97.20; 100), and per-PII sensitivity of 99.82% (95%-CI 99.76; 99.88). Critical clinical preservation was 99.60% (95%-CI 98.80; 100) per-patient, and clinical preservation was 99.61% (95%-CI 99.51; 99.71) per-file. All modalities achieved at least 98.30% sensitivity (lower bound 95%-CI). On our local data, the system achieved a deidentification sensitivity of 100% per-patient and per-PII; and a critical clinical preservation of 100% per-patient as well as a clinical preservation of 99.97% (95%-CI 99.91; 100) per-file. When comparing orchestrators, the leading local models were similar to proprietary models (GPT-5.2) in deidentification sensitivity while showing higher deidentification specificity. The Multimodal Anonymizer outperformed previous tools on most modalities.

ConclusionNear-complete, utility-preserving deidentification of multimodal clinical data is achievable with a unified, locally deployable multi-agent system, enabling safer large-scale reuse of hospital data for research and AI development.

HighlightsO_LIFramework for deidentification of multimodal clinical data.
C_LIO_LIMultimodal deidentification with preservation of clinically relevant content.
C_LIO_LIOn-premises plug-and-play deployment for local data processing.
C_LIO_LIEvaluation of 16 model configurations and comparison with existing tools.
C_LIO_LIAssessment on external, multilingual and site-specific datasets.
C_LI

Short DescriptionThe Multimodal Anonymizer is a fully local, multi-agent system that prepares multimodal clinical records for privacy-preserving reuse by coordinating multimodal large language model reasoning, specialist neural networks, rule-based transformations, and iterative verification. Across benchmarks spanning text, tables, PDFs, imaging, metadata, filenames, audio, and handwriting, its best configuration using a local open-source multimodal large language model achieved 98.80% patient-level deidentification sensitivity and 99.60% preservation of clinically critical content, performing comparably to proprietary models and outperforming established deidentification tools across most modalities.

Graphical Abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=109 SRC="FIGDIR/small/26353952v2_ufig1.gif" ALT="Figure 1">
View larger version (31K):
org.highwire.dtl.DTLVardef@c9dee3org.highwire.dtl.DTLVardef@1480d96org.highwire.dtl.DTLVardef@174331corg.highwire.dtl.DTLVardef@1c77610_HPS_FORMAT_FIGEXP  M_FIG C_FIG

</details>


---



## Arxiv (141 papers)


### 1. Value-Sensitive Delegation in Everyday AI Agent Use: Evidence from OpenClaw

- **Authors:** Renkai Ma, Ruyuan Wan, Xuan Lu, Fan Yang, Chen Chen, Lingyao Li
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.22067v1](http://arxiv.org/abs/2609.22067v1)
- **PDF:** [https://arxiv.org/pdf/2609.22067v1](https://arxiv.org/pdf/2609.22067v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Users increasingly delegate work to autonomous AI agents, yet evaluations typically measure task completion rather than the values users prioritize. Using Value Sensitive Design, we analyzed, with LLM assistance, 73,093 first-person Reddit posts about using OpenClaw, each for its human value, agent aspect, value fulfillment, and user outcome. The 21 values form six value groups, including Autonomous, Dependable, and Affordable Operation, Bounded Reach, Reviewability, and Equitable Access. Relative to each aspect's corpus share, values clustered not at the agent's outputs but at the operating conditions users set around a run. Values were usually met where users described what the agent delivered, in five of six groups, and mostly unmet where users described supervising it, in all six groups. We conceptualize this pattern as value-sensitive delegation. Supporting human values requires attention not only to what an agent accomplishes, but to the conditions users set around delegation, including cost, access, and oversight.

</details>


### 2. An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency

- **Authors:** Yiming Zhang, Jinghong Zhang, Haoran Zhao, Yiren Ma, Chunlei Zhao
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.22043v1](http://arxiv.org/abs/2609.22043v1)
- **PDF:** [https://arxiv.org/pdf/2609.22043v1](https://arxiv.org/pdf/2609.22043v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Memory systems for large language models have focused predominantly on efficient retrieval, whereas the decision of whether retrieved memories should be trusted has received comparatively little attention. When the memory store contains conflicting positions, standard retrieval-augmented generation (RAG) blindly injects memories and amplifies hallucinations: in models susceptible to memory injection, the RAG hallucination rate under conflicting memories is markedly higher than that of a memory-free baseline. Inspired by memory signaling mechanisms in the prefrontal cortex, we propose the Memory Decision Layer (MDL), a zero-parameter memory decision controller situated between the retrieval and generation stages. Its core is a three-signal complementary encoder that fuses relevance, reliability, and task risk through QR-based orthogonal subspace projection and a meta-working-memory signal into an interpretable decision representation that quantifies the trustworthiness of retrieved memories. Building on this encoder, MDL explicitly decouples confidence from consistency and introduces risk inversion and explicit abstention. Evaluations on mainstream large language models and multiple open-source datasets show that MDL reduces the hallucination rate under conflicting memories by about 56.04% in general scenarios and approaches zero hallucination in high-risk scenarios. The controller is fully white-box: it relies purely on geometric operations, requires no trained parameters, and adds only about 0.14 ms per decision -- roughly 50x faster than the embedding-retrieval step that precedes it and four to five orders of magnitude faster than an LLM self-evaluation call.

</details>


### 3. Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents

- **Authors:** Hafsa Akbar, Daniel Platnick, Marjan Alirezaie, Hossein Rahnama
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21997v1](http://arxiv.org/abs/2609.21997v1)
- **PDF:** [https://arxiv.org/pdf/2609.21997v1](https://arxiv.org/pdf/2609.21997v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents in social simulation revise their opinions implicitly, in context: how open an agent is to persuasion can neither be specified nor verified, and collective outcomes inherit the model's training prior. We introduce Bayesian Chronicle Agents (BCA), a minimal belief layer separating \emph{what} an agent believes from \emph{how} it speaks. Each stance is a probability, updated by one Bayesian step per utterance heard. A single prior-strength parameter $κ$ encodes stubbornness, modeled after its role in Friedkin--Johnsen (FJ) opinion dynamics. We then sweep this parameter to yield three canonical regimes of opinion dynamics on demand (consensus, persistent disagreement, committed-minority influence), with persistent disagreement matching the FJ closed-form fixed points at $R^2\!=\!0.93$--$0.99$. We further show that prescribed $κ$ remains recoverable after the language round-trip, with perfect rank-order recovery across all four models. Explicit belief also makes simulation auditable: the layer surfaces systematic per-model stance biases that end-to-end simulation would silently absorb.

</details>


### 4. Guiding Agents of Quantum Games to Equilibrium using Matrix Exponential Fixed-Point Iteration

- **Authors:** Alireza Habibi, Luis F. Abanto Leon, Setareh Maghsudi
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21944v1](http://arxiv.org/abs/2609.21944v1)
- **PDF:** [https://arxiv.org/pdf/2609.21944v1](https://arxiv.org/pdf/2609.21944v1)
- **Categories:** quant-ph, cs.GT, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In recent years, quantum game theory has gained significant attention as a framework for studying decision-making in multi-agent systems using quantum principles. However, computing equilibrium strategies is challenging because the dimension of the joint Hilbert space grows as the product of the players' local dimensions. In this paper, we consider an extended Gutoski-Watrous (EGW) game in which each player's quantum strategy is represented by a local density matrix. We derive tensor-contraction expressions for the payoff functions and their gradients, thereby avoiding the explicit construction of the full joint density matrix and its computationally expensive multiplication by the payoff operators. Building on the resulting effective Hamiltonians, we propose the Matrix Exponential Fixed-Point Iteration with Annealing (MEFPIA) algorithm to search for equilibrium points in EGW games. We compare MEFPIA with the Matrix Multiplicative Weights Update (MMWU) algorithm in terms of convergence. For the tested instances and parameter settings, both algorithms approach the same strategy profiles and payoffs, while MEFPIA achieves lower relative error in fewer iterations. These results indicate that MEFPIA is a promising numerical method for equilibrium search in multi-agent quantum games. Our findings provide important insights into the quantum game theory's potential for addressing complex decision-making processes, as well as opening up new paths for future research and exploration in multi-agent quantum systems.

</details>


### 5. TrialAtlas: Multi-Agent Research Organization for Clinical Trial Design and Optimization

- **Authors:** Jiacheng Lin, Zifeng Wang, Zheng Chen, Erick Scott, Ziwei Yang, Fanyang Yu, Sheng Zhong, Jimeng Sun
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21859v1](http://arxiv.org/abs/2609.21859v1)
- **PDF:** [https://arxiv.org/pdf/2609.21859v1](https://arxiv.org/pdf/2609.21859v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Nearly 90% of drugs entering clinical development ultimately fail, despite billions of dollars in investment. Pharmaceutical companies therefore rely on clinical development planning (CDP) and probability of technical and regulatory success assessment to anticipate development risks, yet these decisions remain labor-intensive and subjective, requiring experts across clinical science, statistics, regulatory affairs, and competitive intelligence to jointly acquire, synthesize, and reason over heterogeneous evidence. Here, we introduce TrialAtlas, a memory-augmented multi-agent research organization for CDP that mirrors this collaborative process by coordinating specialized agents for literature synthesis, competitive trial intelligence, regulatory precedent analysis, and integrated reasoning over trial design and development risk. TrialAtlas further learns from historical clinical trials and regulatory outcomes, including prior New Drug Applications (NDAs), to ground its decisions in accumulated development experience. To evaluate these capabilities in an authentic regulatory setting, we introduce TrialAtlasBench, constructed from 291 FDA Complete Response Letters and spanning three practical tasks: detecting trial design deficiencies, recommending actionable design improvements, and predicting technical and regulatory success. TrialAtlas achieves an F1 score of 50.0% for deficiency detection, outperforming the strongest baseline by 6.1 points, and reaches 85.3% balanced accuracy and 84.7% F1 for prediction of technical and regulatory success, improving over the best baselines by 6.7 points in balanced accuracy and 12.0 points in Cohen's kappa. In expert evaluation, 86.4% of TrialAtlas-generated concerns were judged valid, compared with 83.1% for OpenAI DeepResearch and 59.3% for Gemini DeepResearch.

</details>


### 6. An Agentic Just-in-Time Adaptive Intervention System for Personalized Sleep Support: Proof-of-Concept Study with N of 1 Data

- **Authors:** Nick Rezaee, Chelsea Boccagno
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21805v1](http://arxiv.org/abs/2609.21805v1)
- **PDF:** [https://arxiv.org/pdf/2609.21805v1](https://arxiv.org/pdf/2609.21805v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background: Just-in-time adaptive interventions (JITAIs) can use behavioral data to adapt support to changing contexts, but many rely on predefined rules and manual configuration.
  Objective: We developed a proof-of-concept sleep JITAI using an AI agent to review personal data, evaluate reminders, adapt interventions, and record decisions for human review.
  Methods: Running in Home Assistant on a configurable schedule, the agent follows a reusable skill file to review 30 days of sleep and behavioral data, including physical activity, smartphone use, and bedtime routines, to identify patterns and create or update automated reminders.
  Results: Initial runs demonstrated technical feasibility, successfully completing data review and intervention decisions while limiting reminders to three per day and saving decision records.
  Conclusions: Agentic AI may enable flexible, adaptive sleep JITAIs. The architecture supports future comparison with fixed or rulebased interventions, requires human oversight, and could extend to other health behaviors.

</details>


### 7. CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents

- **Authors:** Tao Huang, Guosen Wu, Guolong Zheng, Jiayang Meng, Chen Hou, Xu Yang, Xuechao Yang, Feng Xia
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21686v1](http://arxiv.org/abs/2609.21686v1)
- **PDF:** [https://arxiv.org/pdf/2609.21686v1](https://arxiv.org/pdf/2609.21686v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Privacy leakage in LLM agents is commonly evaluated within individual components such as memory, retrieval, or tool-use pipelines, which makes it difficult to distinguish internal exposure from information that an external observer can actually recover. We present CIPL (Channel Inversion for Privacy Leakage), a channel-aware evaluation framework for black-box privacy leakage in LLM agents. CIPL represents a target through sensitive source, selection, assembly, execution, observation, and extraction stages and evaluates the transition from selected sensitive units to attacker-recoverable output under a shared protocol. Experiments across memory-based, retrieval-mediated, and tool-mediated targets, together with a BrowserUse live-agent case study, show that storage labels alone do not determine recoverability. Memory targets form a near-saturated reference case, retrieval-mediated leakage is frequently partial, and tool-mediated and live-agent leakage varies strongly with observation surface, prompt-to-channel alignment, retrieval depth, and provider behavior. A stratified semantic audit further identifies attacker-useful disclosures that canonical exact matching misses. CIPL therefore provides a common framework for comparing how internal sensitive dependence is realized as externally recoverable leakage across heterogeneous agent pipelines.

</details>


### 8. MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems

- **Authors:** Kairui Yang, Minghao An, Xunkai Li, Ziheng Yi, Zekai Chen, Guangyuan He, Rong-Hua Li
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21533v1](http://arxiv.org/abs/2609.21533v1)
- **PDF:** [https://arxiv.org/pdf/2609.21533v1](https://arxiv.org/pdf/2609.21533v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems generate collaboration traces that record how agents plan tasks, verify intermediate results, and repair failures. Reusing these procedures requires preserving an action's prerequisites and the outputs needed by subsequent agents. Our empirical studies show that grouping these dependencies into functional memory units improves their retention, while connecting units increases retrieval of the units and links jointly required by a task. The preferred combination of units also changes between instructions and checklists, even when each combination's content is fixed across formats. Updating choices from the outcomes of each combination and format pairing outperforms scoring combinations and formats separately. These findings motivate MACE, a memory-agent co-evolution framework that adapts memory organization and agent memory use through execution feedback. Its MemGoG structure represents functional units as subgraphs of related conditions, actions, and outputs, connecting them through support, conflict, and repair relations. MACE Loop selects task-relevant units and relations within a memory budget and provides each agent with instructions or checklists for its current operation. It records the selected units, presentation formats, agent outputs, and task outcomes to update unit scores and relations for retrieval and inform subsequent presentation choices. Across eight benchmarks, MACE outperforms ten baselines with an average score of 81.11%, compared with 78.97% for the strongest baseline, SAGE.

</details>


### 9. OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems

- **Authors:** Kairui Yang, Xunkai Li, Kaixiang Zhang, Minghao An, Zekai Chen, Yuxuan Ba, Rong-Hua Li
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21527v1](http://arxiv.org/abs/2609.21527v1)
- **PDF:** [https://arxiv.org/pdf/2609.21527v1](https://arxiv.org/pdf/2609.21527v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Graph-enhanced multi-agent systems (G-MAS) coordinate large language model agents through communication graphs and role assignments, which determine how agents exchange information and divide responsibilities. However, final-score comparisons across systems combine differences in models, communication patterns, roles, and computation costs, making performance differences difficult to attribute to specific communication structures, role assignments, and information flows. To address this evaluation attribution problem, we introduce OpenMAS-GCom, a benchmark for diagnosing how these components affect G-MAS performance through controlled interventions. We represent systems through collaboration units, communication links, shared intermediate information, and execution rules. OpenMAS-GCom compares original systems with versions modified by changing one component while keeping tasks, models, prompts, and budget limits fixed. We rewire communication edges, remove specialist or critic agents, replace intermediate messages with incorrect content, and disable workers during execution. The benchmark evaluates 17 single-agent, ordinary multi-agent, and graph-enhanced configurations on 29 datasets across six domains. We add 400 G-MAS-Complex tasks requiring agents to combine information from multiple documents, resolve conflicting records, and return specified values with source identifiers. Experiments show larger mean losses after specialist removal than after critic removal, different performance degradation under incorrect messages and worker failures despite similar original scores, and different configurations achieving the highest accuracy and accuracy per token on G-MAS-Complex.

</details>


### 10. OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue

- **Authors:** Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21465v1](http://arxiv.org/abs/2609.21465v1)
- **PDF:** [https://arxiv.org/pdf/2609.21465v1](https://arxiv.org/pdf/2609.21465v1)
- **Categories:** eess.AS, cs.AI, eess.IV


> Summary unavailable.


<details>
<summary>Abstract</summary>

We define OmniVChat (Omni Video Chat) as the task of native audio-visual dialogue between a user and an omni model. In OmniVChat, omni models directly and simultaneously receive audio and video from a user and return text. The user's query is embedded in the audio and video, without a separate text question, external captioning, or speech recognition. Direct audio-visual input reduces external latency and computation while preserving perceptual cues. However, research on OmniVChat faces two constraints: data availability and evaluation. Recordings of people using their own devices are scarce. Furthermore, a good reply often needs to account for the user's surroundings, facial expressions, and nearby objects, and such responses can be expressed in many different ways, making keyword matching unreliable for evaluating reply quality. Recent progress in agent systems and video generation makes generation for comprehension viable, which means using synthesized dialogues for training and evaluation. Therefore, we present OmniVChat-Studio, a multi-agent data engine for synthesizing single- and multi-turn audio-visual dialogues. We use synthesized dialogues to build OmniVChat-Bench, an evaluation benchmark that evaluates omni models' basic dialogue abilities across five ability categories. We also present OmniVChat-RL, a reinforcement learning reward design that jointly targets reply correctness, efficiency, and style in OmniVChat. Training Qwen3-Omni-Instruct with OmniVChat-RL on synthesized dialogues improves its performance on both OmniVChat-Bench and the human-recorded OmniVChat-Bench-Human. These gains validate the reward design and show transfer to real-world dialogues in training and evaluation.

</details>


### 11. LEGIT: Credentialing Protocol for Trustworthy AI Agent Marketplaces

- **Authors:** Steve Drew, Jiayu Zhou
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21325v1](http://arxiv.org/abs/2609.21325v1)
- **PDF:** [https://arxiv.org/pdf/2609.21325v1](https://arxiv.org/pdf/2609.21325v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic marketplaces are emerging where AI agents with varying capabilities autonomously complete specialized tasks for buyers. A major challenge of such marketplaces is that buyers cannot easily determine which agent will perform best on their tasks. Reported benchmark scores may be difficult to verify or compare across tasks, software, and budgets. We introduce LEGIT, a credentialing protocol connecting certification, reputation, and proposed marketplace allocation. Certification binds measured quality and cost per solved task to an agent configuration, task domain, evaluation budget, and evidence through a signed record. Reputation links records of past task outcomes to the same identity, subject to the reliability of the reported feedback. Buyers and agents can verify credential records and inspect optional visual profiles. Evaluations reveal cost differences between agent configurations with similar observed task success, and show that comparisons depend on the evaluation budget. These results support binding performance measurements to the tested configuration and resource limits. A complementary analysis quantifies the deposits and fees required for reputation manipulation under a stated Sybil attack model.

</details>


### 12. Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution

- **Authors:** Genliang Zhu, Chu Wang
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21284v1](http://arxiv.org/abs/2609.21284v1)
- **PDF:** [https://arxiv.org/pdf/2609.21284v1](https://arxiv.org/pdf/2609.21284v1)
- **Categories:** cs.PL, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running AI agents outlive initiating processes through credentials, delegated tasks, queues, callbacks, reservations, and provider-side operations. Cancellation, process exit, and credential revocation neither close every pre-cut carrier nor distinguish independently authorized shared work. We define root-scoped authorization quiescence: for each manifested sink, a certificate accounts for every cut-relevant acceptance under the retired root-epoch atom that precedes its local fence and excludes protected acceptance under that atom after the fence, while permitting exact rebind to a current, independently sufficient support.
  The root-scoped quiescence protocol linearizes a root cut, fences old-root expansion and protected sinks, represents alternative and conjunctive authority as antichains of minimal sufficient root sets, and composes provider-frontier certificates into a cutset over registered old-root paths. Exact channel-token accounting reconciles transfers; missing or conflicting evidence remains indeterminate. Under stated assumptions, we prove post-cut issuer non-expansion, support-sound projection, compositional soundness under exact channel conservation, independent-support preservation, merge-order independence, and crash/replay stability.
  A provider-free late-effect test suite matches 17/17 registered outcomes. Two cancellation-only and one cut-only execution accept the same class of already scheduled late effect; two cut-plus-fence executions, one restart, and one stale-process execution reject it. A separately implemented checker verifies 17/17 traces and rejects 44/44 consistently rehashed semantic regressions. The certificate establishes root-relative authorization quiescence within its bound manifest and configuration, not global idleness, rollback, or business completion.

</details>


### 13. Efficient Benchmarking in Production: A Study of an Evolving LLM Agent

- **Authors:** Yining She, Lei Lin
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21267v1](http://arxiv.org/abs/2609.21267v1)
- **PDF:** [https://arxiv.org/pdf/2609.21267v1](https://arxiv.org/pdf/2609.21267v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production LLM agents are evaluated repeatedly as they evolve, but full agent benchmarks are costly to rerun. We study efficient recurring evaluation for a production analytics agent serving tens of thousands of monthly active users and report first-hand deployment experience. Using 574 historical runs of the production benchmark, split chronologically into calibration and held-out periods, we compare random sampling, historical caching, fixed representative subsets, and IRT-based adaptive testing. The results show that multidimensional 2PL adaptive testing achieves the best overall score fidelity: executing 200 questions, 38.5% of a full run, yields 1.03 pp of MAE. We nevertheless deployed difficulty-stratified fixed subsets because of their operational simplicity, and show they transfer without recalibration to five other agent families and remain stable across calibration windows as short as one day. Drawing on this deployment experience, we report practical recommendations for recurring production-agent evaluation.

</details>


### 14. PlaceReasoner-Beta: Reasoning-Driven Macro Placement and Benchmarking

- **Authors:** Qiufeng Li, Chengxuan Wang, Rongqian Chen, Quan Cheng, Yihui Ren, Chia-Tung Ho, David Z. Pan, Tian Lan, Weidong Cao
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21263v1](http://arxiv.org/abs/2609.21263v1)
- **PDF:** [https://arxiv.org/pdf/2609.21263v1](https://arxiv.org/pdf/2609.21263v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated macro placement remains a fundamental challenge in VLSI physical design. Despite decades of research, existing approaches predominantly optimize hand-crafted proxy objectives, such as estimated wirelength, and typically produce placements through one-shot numerical optimization, limiting their ability to incorporate visual layout context, codified design expertise, and downstream physical-design feedback in a unified loop. We present PlaceReasoner-Beta, a verifier-guided multi-agent framework that reformulates macro placement as a closed-loop reasoning problem rather than black-box optimization. A vision-language model (VLM) planner generates candidate placements from the floorplan image, macro specifications, and connectivity structure; a geometric verifier enforces physical legality and expert placement principles; a physical verifier refines candidates using early implementation feedback; and a post-route optimizer further improves promising layouts using final PPA. To enable reproducible evaluation, we introduce PlaceReasoner-Bench, a fully open end-to-end benchmark built from open RTL designs, EDA tools, and technology libraries. It comprises 8 designs at two aspect ratios, yielding 16 tasks with fixed floorplans and I/O assignments, so methods differ only in macro positions and orientations and are evaluated using routed PPA and DRC rather than pre-route proxies. Across the benchmark, PlaceReasoner-Beta achieves the best timing among DRC-clean methods on all square tasks, reducing post-route TNS by 61.2% at 1:1 and 53.0% at 2:1 relative to the classical baseline field. It also shortens routed wirelength on most designs despite never explicitly optimizing it, demonstrating that reasoning over spatial structure under physical-design feedback can improve end-to-end layout quality beyond proxy-objective optimization.

</details>


### 15. AI-GRACE: A Use-Case Operationalization Framework for Agentic AI: From Organizational Objectives and Obligations to Deployment Capabilities and Architecture

- **Authors:** John Cuneo, David Chun, Gaurav Khanna
- **Published:** 2026-09-18
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21192v1](http://arxiv.org/abs/2609.21192v1)
- **PDF:** [https://arxiv.org/pdf/2609.21192v1](https://arxiv.org/pdf/2609.21192v1)
- **Categories:** cs.AI, cs.CY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Organizations deploying agentic artificial intelligence must determine more than whether a model is trustworthy; they must establish what to validate, control, and observe for a use case to deliver its intended outcome while meeting applicable obligations. This paper proposes AI-GRACE (Agentic Intelligence-Governance, Risk, Assurance, Controls, and Evidence) as a use-case operationalization framework connecting organizational governance with technical implementation. The proposal draws on professional observations and a purposive synthesis of standards and literature, using design science to frame the method contribution and situational method engineering to guide contextual tailoring and reuse. The framework establishes objectives and obligations and then assesses risks in seven proposed domains, including mission and value realization. It derives requirements for assurance before deployment, runtime controls, and evidence, which guide capability qualification, gap assessment, and a logical architecture. An Agent Operating Envelope specifies permitted actions and escalation conditions, while Risk-Aligned Independence Levels (RAIL) summarize the authorized independence. A fictional retail banking application illustrates the method. The contribution is a traceable basis for deciding what an organization must implement, what it already supports, and what remains unresolved. Empirical evaluation must establish whether it improves deployment decisions, efficiency, and reuse.

</details>


### 16. Scaling Discovery through Test-Time Communication

- **Authors:** Jongho Park, Vasilis Kontonis, Shivam Garg, Akshay Krishnamurthy, Dimitris Papailiopoulos
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.21032v1](http://arxiv.org/abs/2609.21032v1)
- **PDF:** [https://arxiv.org/pdf/2609.21032v1](https://arxiv.org/pdf/2609.21032v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Science advances not in isolation but through collaboration, yet existing agentic systems capture little of this. Whether communicating agents help remains an open question with mixed prior results. We show that test-time communication can substantially outperform independent parallel attempts on challenging tasks, where sharing a breakthrough can push the whole group forward. We first study the effect of scaling multi-agent test-time communication, where agents have no predefined roles and communicate via a shared directory, on ARC-AGI-3, a benchmark requiring novel problem solving. We find that a team of $k$ communicating agents, team@$k$, matches the success rate of $4k$ independent agents, and this advantage grows with $k$, suggesting gains compound with scale. The effect is not merely efficiency: a task that no single agent can solve, a team of agents can solve reliably. Furthermore, these gains transfer to research-oriented tasks, given sufficient compute. On polyomino packing, communicating agents outperform best@$k$ and exceed the prior best-known score. On MNIST classifier compression, communication surpasses the best-known human solution. A team of four agents produced a 1,957-byte classifier submission achieving 99.4% test accuracy, smaller than both the best-known human solution and the best single-agent result. These gains are not unconditional. Independent agents may outperform communication when compute is limited or when a clear measure of progress is absent. However, under sufficient compute and clear feedback, multi-agent communication consistently yields stronger results.

</details>


### 17. Quantifying Overclaiming Propensity in Frontier LLM Agents

- **Authors:** Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Jr Tikeng Notsawo, Saskia Helbling, Alberto Tosato, Mohamed Amine Merzouk, Nouha Dziri, Gauthier Gidel, Tommaso Tosato
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20812v1](http://arxiv.org/abs/2609.20812v1)
- **PDF:** [https://arxiv.org/pdf/2609.20812v1](https://arxiv.org/pdf/2609.20812v1)
- **Categories:** cs.SE, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier coding agents are increasingly trusted to work autonomously for long periods, yet an agent's final response is often the only account of that work a user sees. We quantify the propensity of frontier agents to \emph{overclaim} task completion, a misrepresentation that can mislead the user. An agent overclaims when its final response contradicts information in its context. This definition requires no inference about intent and is independent of task success. We introduce \emph{OverclaimBench}, an evaluation suite composed of five file-review scenarios, transcript-based coverage measurements, and registered planted defects. We evaluate eight proprietary frontier models in their own production command-line interfaces, and four open-weight models under a single fixed harness on OverclaimBench and find that 1) agents do not read all the files they were asked to review in 67.9\% of runs; 2) among runs where not all files are read, agents are \emph{misleading} 80.4\% of the time (59--96\% per model), either falsely claiming to have read all files or omitting that coverage is incomplete; 3) requiring delegation to subagents increased reading coverage, but among reviews that remained incomplete, a large majority were still misleading; and 4) agents that falsely claimed a complete review missed planted defects at about 1.8 times the rate of agents that read every file, showing that claims of completion can conceal substantive failures. Together, these results show that agents' final responses are not reliable accounts of their actions.

</details>


### 18. Chronicle: Cut-Point Replay for Regression Testing of LLM Agents

- **Authors:** Tisha Chawla, Susheem Koul
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20625v1](http://arxiv.org/abs/2609.20625v1)
- **PDF:** [https://arxiv.org/pdf/2609.20625v1](https://arxiv.org/pdf/2609.20625v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundaries as immutable envelopes and replays it from the record. Its central operation, cut-point replay, serves a chosen subset of boundaries from the record and executes the complementary subset live with new code, turning a recorded incident into a regression test that runs in continuous integration. On a benchmark of 6 recorded failures with simulated model boundaries, recording adds 23 μs per crossing (0.008% of an assumed 300 ms model call), full replay issues zero model calls and is bit-stable across 20 repetitions, and cut-point tests fail on faulty code and pass on guarded and benign changes for all 6 incidents. In a mutation study of the guarded tools, cut-point tests catch every mutant that lets the recorded unsafe action through, while a baseline that stubs every boundary, using the same assertion, catches none. Chronicle and the benchmark are publicly available at https://github.com/theagentplane/chronicle.

</details>


### 19. How Do Agent Harnesses Create Value? Planning Information and Release Control in Stateful LLM Agents

- **Authors:** Yukun Zhang, Kemu Xu, Yishen Chen
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20474v1](http://arxiv.org/abs/2609.20474v1)
- **PDF:** [https://arxiv.org/pdf/2609.20474v1](https://arxiv.org/pdf/2609.20474v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent harnesses supply planning guidance, organize execution, and check completion. We study how these components affect success, erroneous acceptance, and cost in two Retail experiments and an Airline pilot in $τ^2$-bench. The primary comparison pairs prewritten task-specific plans (Fixed) with shuffled policy text matched in word count (Sham), isolating the contribution of guidance content. Across 265 matched cells, Fixed improves oracle-verified success by 7.17 percentage points (90\% task-clustered bootstrap interval, 1.15--13.36 points), with gains concentrated in higher-complexity tasks. A read-only terminal verifier rejects 61\% of Retail oracle-invalid episodes while withholding 17\% of correct ones, at less than one cent of additional cost per episode. Which component matters more depends on the loss assigned to erroneous acceptance: at low liability the planning gain dominates; at high liability the verifier's avoided false passes dominate---and a standalone verifier captures nearly all the false-pass benefit of the full planning-plus-verification stack at a fraction of its cost.

</details>


### 20. Xeno-Interpretability: Investigating the Alien Minds of LLMs

- **Authors:** F. Pierucci, M. Bracale Syrnikov, M. Prandi, M. Galisai, F. Giarrusso, P. Bisconti
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20408v1](http://arxiv.org/abs/2609.20408v1)
- **PDF:** [https://arxiv.org/pdf/2609.20408v1](https://arxiv.org/pdf/2609.20408v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are usually interpreted through concepts that humans already possess: truthfulness, refusal, deception, personality, harmfulness, and related categories. This paper asks whether models may also represent and use distinctions for which no adequate human concept exists. We call such internal structures xeno-representations, and their study xeno-interpretability. We distinguish the human-interpretable semantic space from the xeno-semantic space: the region of model-native representations for which no adequate human conceptual counterpart is available. We show that the space of possible internal distinctions in an LLM is substantially larger than the space available through finite human descriptions. We then separate experimental identification from semantic interpretation: an internal representation may be reproducibly located, geometrically characterized, causally manipulated, and linked to downstream behaviour even when its semantic content cannot be adequately expressed in human terms. On this basis, we sketch an empirical programme to identify xeno-representations. We finally examine the implications for AI safety and multi-agent systems, where model-native representations may propagate and stabilize across interacting agents while remaining only partially visible through human-readable communication. Xeno-interpretability therefore shifts the aim of interpretability from finding human concepts inside models toward discovering and characterizing the representational structures that are native to the models themselves and might affect their behaviour in unpredictable ways.

</details>


### 21. A Qualitative Model for Reasoning about Path and Support

- **Authors:** Abhishek Jaiswal, Zoe Falomir
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20349v1](http://arxiv.org/abs/2609.20349v1)
- **PDF:** [https://arxiv.org/pdf/2609.20349v1](https://arxiv.org/pdf/2609.20349v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Spatial reasoning abilities correlate strongly with performance in STEM fields. Games offer a compelling medium for training these critical skills in developing children who have a natural proclivity for play. However, to facilitate human-like tutoring and player guidance, these games require an AI agent capable of making commonsense inferences from spatial events. Qualitative reasoning (QR) models appear to be a suitable framework for these application domains. As these models reason in symbolic representations, they can seamlessly translate game states into interpretable feedback for human-like player guidance. This paper introduces a hybrid qualitative model designed for Camelot Jr., a block-puzzle game that requires constructing multi-level bridges to connect two avatars stationed on separate towers. The game poses a challenge for the player, who must make platforms stable, plan their path, and ensure they use all the provided blocks. To handle the precise physics required by the domain, we integrate a mathematical center-of-mass stability logic to guide our qualitative solver. Our work facilitates spatial skill training in Camelot Jr. and contributes to the development of human-centric, explainable game-playing agents.

</details>


### 22. A Scalable Trust Discovery Architecture for the Internet of Agents

- **Authors:** Song Zhang, Jiankang Yao, Hongtao Li, Xiaojun Zhang, Xugang Shen, Xin Li, Yanbiao Li
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20095v1](http://arxiv.org/abs/2609.20095v1)
- **PDF:** [https://arxiv.org/pdf/2609.20095v1](https://arxiv.org/pdf/2609.20095v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Internet of Agents is expected to enable large numbers of autonomous agents to discover, verify, and collaborate with each other across heterogeneous platforms. However, current agent protocols mainly address tool invocation and inter-agent communication, leaving scalable agent registration, trustworthy identification, and capability-oriented discovery largely unresolved. To address this, this paper proposes a scalable trust discovery architecture for the Internet of Agents. The proposed architecture adopts a hierarchical and distributed design consisting of three layers: Agent Root for trusted registry governance, Agent Registry for agent registration and metadata publication, and Agent Resolver for distributed capability discovery and trust-aware resolution. The architecture further introduces a registry-suffix-anchored composite identity scheme, which binds an agent native identifier to a trusted registry suffix to generate a globally discoverable identity. It also incorporates a dual-certificate and multi-level authentication mechanism to strengthen identity trust among agents. We implement a prototype and evaluate it through large-scale agent registration and resolution experiments. The prototype achieves an average registration latency of 58ms and an average discovery latency of 25ms, and it supports more than 19,000 registration requests per second and more than 29,000 agent discovery requests per second. These results demonstrate the feasibility of the proposed architecture, providing a practical approach toward scalable and identity-trusted agent ecosystems in the Internet of Agents.

</details>


### 23. A Proposal for an Agentic AI Architecture to Support Multi-Domain Decision-Making in the Brazilian Armed Forces

- **Authors:** Gioliano de Oliveira Braga, Sidnei Barbieri, Ágney Lopes Roth Ferraz, Wagner Comin Sonaglio, Henrique Curi de Miranda e Lourenço Alves Pereira
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20080v1](http://arxiv.org/abs/2609.20080v1)
- **PDF:** [https://arxiv.org/pdf/2609.20080v1](https://arxiv.org/pdf/2609.20080v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The growing complexity of multi-domain operational environments (land, aerospace, naval, cyber, and electromagnetic spectrum) has increased the volume and velocity of data reaching command-and-control (C2) centers, straining the observe-orient-decide-act (OODA) decision cycle. Artificial Intelligence (AI) systems currently employed in defense are, in general, reactive and isolated tools that still rely heavily on human operators to integrate information, assess scenarios, and formulate courses of action. This paper proposes a conceptual Agentic AI architecture for AI systems that can plan, access data sources, execute tools, and act autonomously and audibly, aimed at supporting decision-making across the three Brazilian Armed Forces (Navy, Army, and Air Force). Four application fronts are discussed (decision support, situational analysis, feasibility studies, and countermeasure suggestion), as well as the data and sensor access requirements and the security and permission safeguards necessary for responsible employment across administrative, strategic, operational, and tactical contexts.

</details>


### 24. Neuro-Symbolic Agentic AI for Networked Low-Altitude UAVs

- **Authors:** Yuqi Ping, Tianhao Liang, Nanchi Su, Guangyu Lei, Junwei Wu, Qinyu Zhang, Tingting Zhang
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19961v1](http://arxiv.org/abs/2609.19961v1)
- **PDF:** [https://arxiv.org/pdf/2609.19961v1](https://arxiv.org/pdf/2609.19961v1)
- **Categories:** cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Networked low-altitude unmanned aerial vehicles (UAVs) need reliable and adaptive decision-making capabilities to operate under uncertain observations, dynamic environments, and intermittent connectivity, while many existing agentic systems remain limited by hallucination risks, data dependence, and weak generalization. This article investigates neuro-symbolic agentic AI (NSAAI) as a framework for combining neural grounding, symbolic reasoning, and closed-loop agentic interaction to support more reliable and adaptive UAV autonomy. We first examine its capability foundations in data efficiency, compositional generalization, continual learning, and zero-shot transfer, and then develop a reference architecture integrating task and goal management, neuro-symbolic planning, verification and metacognition, skill execution and network interaction, and shared knowledge and memory. An urban fire-inspection case implemented in LAESim illustrates how a UAV can coordinate sensing and cloud access under intermittent connectivity, reuse a verified image-delivery skill, and satisfy explicit evidence conditions before completing the mission. The results illustrate the potential of NSAAI to support reusable skills, evidence-grounded decision-making, and adaptive mission execution in networked UAV systems. We further discuss key research directions in uncertainty-aware reasoning, knowledge and skill expansion, adaptive self-monitoring, and standardized evaluation.

</details>


### 25. Not All AI Agents Are Equal: Characterizing Resource and Performance Dynamics

- **Authors:** Wonmi Choi, Minuk Park, Zhixiong Niu, Yongqiang Xiong, Chuck Yoo, Gyeongsik Yang
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19947v1](http://arxiv.org/abs/2609.19947v1)
- **PDF:** [https://arxiv.org/pdf/2609.19947v1](https://arxiv.org/pdf/2609.19947v1)
- **Categories:** cs.AI, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based AI agents process user requests through iterative reasoning and tool execution, often involving the invocation of remote LLM APIs with local tool containers. This execution model can make the optimization of agent serving difficult because latency, local resource demand, and container bottlenecks inter-mix across requests. However, the current agent ecosystem runs without much consideration of resource dynamics, which results in significant waste of the precious resources. This paper analyzes the resource inter-mix of AI agents for three representative tasks: retrieval-augmented question answering, web search, and software coding. To this end, we characterize the latency with respect to the resource dynamics of processing multiple requests and tasks concurrently. Our measurements show that agents have a wide range of behaviors depending on tasks, so that even the same tool can differ substantially in resource dynamics. We also find that running multiple requests concurrently exposes task-dependent bottlenecks in resource dynamics such as CPU, disk I/O, and memory. Furthermore, we uncover that faster LLM responses or more CPU cores do not always accelerate agents. Based on these observations, we demonstrate new optimization opportunities that exploit the resource dynamics of tasks: CPU-aware tool admission and task-aware CPU allocation. Our results show that the latency of CPU-sensitive agent tasks improves $\sim$5.4$\times$, and the average latency across multiple tasks is reduced $\sim$32% compared to native agents.

</details>


### 26. MaSCoD: A Multi-Agent Framework for Structural-Context-Guided Candidate Causal Graph Generation

- **Authors:** Yudai Nakada, Yuichiro Nishiura, Jin Michael Splichal
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19944v1](http://arxiv.org/abs/2609.19944v1)
- **PDF:** [https://arxiv.org/pdf/2609.19944v1](https://arxiv.org/pdf/2609.19944v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have been applied to causal discovery, but candidate-graph generation rarely treats premature omission of potentially relevant causal relations as an explicit design objective. We propose MaSCoD, a multi-agent framework that organizes candidate third variables and local structural patterns before direct-edge judgment. We evaluate MaSCoD on Auto-MPG, DWD, and Sachs using GPT-5.4 as the primary backbone and GPT-4o for replication. MaSCoD exhibits a dataset- and backbone-dependent retention-selectivity profile rather than uniform superiority. Across all six dataset-backbone settings, Full, which supplies structural hypotheses before direct-edge judgment, achieved higher mean Recall and F1 than No Phase 1, which instead constructs them within the judgment procedure, while also increasing false-positive rates. Additional reference-edge retention over all evaluated baselines was observed on DWD with GPT-5.4 and on Sachs with GPT-4o, rather than uniformly across settings. Partial ablations showed that supplying both information components did not always outperform supplying only one. For GPT-5.4, stage-wise analysis showed that the Full-No Phase 1 retention gap was already present after direct-edge judgment, while reconciliation introduced additional reference-edge loss for Full on Sachs. These findings support structural pre-organization as an explicit design and evaluation target for omission control and motivate evaluating context construction jointly with its utilization in judgment.

</details>


### 27. A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents

- **Authors:** Haya Halimeh, Sascha Kaltenpoth, Kevin Bösch, Oliver Müller
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19843v1](http://arxiv.org/abs/2609.19843v1)
- **PDF:** [https://arxiv.org/pdf/2609.19843v1](https://arxiv.org/pdf/2609.19843v1)
- **Categories:** cs.AI, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based GUI agents increasingly act on behalf of users in digital environments that were designed with human users in mind. These graphical user interfaces were designed to support, but also deliberately steer, the behaviour and decisions of users. While behavioural biases in the textual outputs of LLMs are well-documented, far less is known about how such influence operates when models act as agents that perceive interfaces and execute decisions---and, in particular, whether the reasoning capabilities increasingly built into these agents make them more robust to it. Drawing on Dual-Process Theory, we empirically investigate whether LLM-based GUI agents are susceptible to automatic (Type 1) and reflective (Type 2) digital nudges, and how their reasoning configuration moderates this susceptibility. In a randomized online shopping experiment with 3,600 agents and a total of 21,600 simulations across six frontier models from three providers, we found that agents were vulnerable to both nudge types. Crucially, the reasoning configuration moderated these effects in opposing directions, reducing susceptibility to automatic default nudges while heightening it to reflective social influence nudges. Extensive reasoning therefore did not make agents more robust but redirected the route through which choice architecture takes effect. Exploratory analysis further showed this redirection to be systematically structured by model scale. Beyond establishing nudge susceptibility as a behavioural property of agentic AI, the study positions interface design as a governance concern for organizations that delegate decisions to autonomous agents.

</details>


### 28. Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization

- **Authors:** Yingxuan Zhuang, Binhe Yu, Jingxiao Yang, Ruopei Sun, Ziting Li, Cheng Tan, Xuhong Zhang, Jianwei Yin, Jintao Chen
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19830v1](http://arxiv.org/abs/2609.19830v1)
- **PDF:** [https://arxiv.org/pdf/2609.19830v1](https://arxiv.org/pdf/2609.19830v1)
- **Categories:** cs.AI, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian Feedback Attribution, which constructs a feedback-conditioned posterior over sampled actions, and the second with Trajec- tory Mass Normalization (TMN), which assigns equal optimization mass to com- plete trajectories. Experiments with GRPO and GiGPO on ALFWorld, WebShop, and SearchQA show that both axes provide independent gains and that their combi- nation consistently achieves the strongest overall performance across model scales.

</details>


### 29. DeliveryGym: An RL Environment for Long-Horizon Embodied Agent Planning with Adaptive Curriculum

- **Authors:** Haoqiang Kang, Yiming Zhang, Yiyang Guo, Chuying Li, Jianzhi Shen, Tianruo Rose Xu, Xiaokang Ye, Lianhui Qin
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19801v1](http://arxiv.org/abs/2609.19801v1)
- **PDF:** [https://arxiv.org/pdf/2609.19801v1](https://arxiv.org/pdf/2609.19801v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Executable environments enable LLM agents to learn from the consequences of their actions. For embodied agents, those consequences extend beyond whether the current task succeeds: completing a delivery can consume the time, energy, or money needed for later work. Learning to plan therefore requires environments that preserve these dependencies and turn them into feedback across a complete trajectory. We introduce DeliveryGym, a 3D environment for evaluating and training agents on continuous courier shifts. It couples multimodal tool interaction with persistent world dynamics and computes trajectory rewards from simulator events, making the costs of an agent's decisions available for reinforcement learning (RL). The environment also adapts future training shifts to the policy's observed weaknesses while keeping evaluation fixed. Across six models and 13 city maps, evaluation exposes a gap between reliably executing assigned deliveries and choosing and sequencing work over a shift. On the fixed test suite, RL improves Qwen3-VL-4B's net income by 54.3%, showing that learning from complete shifts improves performance under these coupled constraints. Adapting the training environment improves test income by 16.5% over uniform sampling at the same rollout budget, indicating that which situations an agent practices also matters. DeliveryGym provides an executable setting for studying how agents learn to coordinate deliveries and preserve resources for later orders within an episode.

</details>


### 30. Contagion on the Trading Floor: How Adversarial Signals Spread in Multi-Agent Trading Systems

- **Authors:** Qi Rong Sua, Junhao Dong, Nguyen Duc Thai, Yuqing Wen, Cheston Tan, Yew-Soon Ong
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19789v1](http://arxiv.org/abs/2609.19789v1)
- **PDF:** [https://arxiv.org/pdf/2609.19789v1](https://arxiv.org/pdf/2609.19789v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent trading systems built on large language models (LLMs) are beginning to appear in quantitative finance, yet their robustness to adversarial inputs is largely unknown. We study the vulnerability of LLM trading stacks to black-box, input-only attacks that enter solely via admissible social-media feeds. We introduce the Generic Multi-Agent Trading System (GMATS), a framework that captures modern multiagent trading architectures and instantiate a class of black-box poisoning attackers that treat an LLM as a post generator and inject budget-constrained, plausibly benign social-media content into the analyst's evidence stream. We define contagion metrics that trace how adversarial content propagates through the stack, including belief-shift scores at analyst and coordinator layers and attack-clean deltas on standard backtest metrics. Experiments on a safe offline benchmark with historical market and social data show that even simple input-only attackers can materially degrade risk-return profiles, sharply reducing Sharpe ratios. At the same time, we find that suitably designed multi-agent topologies and coordinator prompts can dampen adversarial shocks and improve average robustness under identical poisoning budgets.

</details>


### 31. Rethinking Multi-Agent Collaboration: When More Is Less

- **Authors:** Yishuo Yuan, Yibo Wu, Yihan Zhang, Minyuan Sun, Shenliang Li, Xinkai Ma, Yifan Li, Jiaheng Liu
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19759v2](http://arxiv.org/abs/2609.19759v2)
- **PDF:** [https://arxiv.org/pdf/2609.19759v2](https://arxiv.org/pdf/2609.19759v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid advancement of large language models and single-agent harnesses has reshaped the landscape of autonomous systems, raising a critical question of when multi-agent collaboration offers genuine value. As individual agent capabilities continue to scale, multi-agent collaboration faces diminishing returns while incurring growing context overhead. Through systematic analysis, we delineate the capability boundaries of multi-agent collaboration relative to single-agent alternatives, showing that it confers systematic benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows. Building on these insights, we propose SAIGE, a lightweight multi-agent collaboration mechanism based on Semantic-Aware Incremental Graph Evolution. SAIGE models collaboration as a dynamically evolving graph, where nodes are agent instances spawned on demand and edges encode semantic dependencies established through content-based information retrieval. Experiments on long-horizon, complex task benchmarks show that SAIGE achieves a favorable trade-off between context efficiency and task performance, and that scaling the agent pool or deepening the recursion level does not consistently improve outcomes. Our findings suggest that multi-agent superiority is bounded by task structure rather than universal, and that more agents do not necessarily make a system more intelligent.

</details>


### 32. AutoData: Agentic Search for Pre-training Data Selection

- **Authors:** Yan Meng, Dhruv Srikanth, Bingchen Zhao, Zhengyao Jiang, Yuxiang Wu
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19754v1](http://arxiv.org/abs/2609.19754v1)
- **PDF:** [https://arxiv.org/pdf/2609.19754v1](https://arxiv.org/pdf/2609.19754v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents have recently shown promise in automating machine learning engineering by editing model and training code under execution feedback. Data, however, remains largely outside this agentic optimisation loop. We frame pre-training data selection as heuristic engineering over per-document features, i.e., lexical statistics, categorical labels, and perplexity. We introduce AutoData, an agent that searches directly over executable selection algorithms. Unlike prior data mixture methods that optimise weights over a fixed set of domains, AutoData searches a richer program space of scoring, stratification, and stochastic selection rules, discovering feature interactions automatically by iteratively refining algorithms with validation feedback from a proxy model. Within an overnight search, AutoData discovers a selection algorithm that outperforms existing human-designed curation pipelines. Despite being searched only on this small proxy, the discovered recipe transfers to larger scales and improves the downstream metric CORE. These results suggest that data engineering can be treated as an agentic machine learning problem, extending autonomous research from model and training-code optimization to the data.

</details>


### 33. SoK: Trading Agents or Market Crashers? Dissecting Robustness and Security Failures in Academic Financial LLM Trading Schemes

- **Authors:** Mengxiao Wang, Nitesh Saxena
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19705v1](http://arxiv.org/abs/2609.19705v1)
- **PDF:** [https://arxiv.org/pdf/2609.19705v1](https://arxiv.org/pdf/2609.19705v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous large language model (LLM) agents are moving rapidly into high-stakes domains, yet existing agentic-AI security studies remain largely domain-agnostic and overlook the distinctive, high-consequence attack surface such settings create. We examine this gap through financial trading agents, a representative case of high-stakes agentic security, where a single compromised agent has direct execution authority over real capital in an adversarial, reflexive market. To this end, we present FARSIGHT (Financial Agent Robustness and Security Investigation and Global Holistic Testing), a framework that performs scheme-level evaluation of financial LLM agents on two axes: robustness under market turbulence (including flash-crash-like scenarios), and security against three attack types: attacks on information sources, attacks on agents, and agent-as-attacker behaviors. Applying FARSIGHT to 15 representative academic schemes, we find that most overlook robustness and realistic adversarial threats: 80% fail at least one core robustness metric and 100% exhibit security vulnerabilities. These two failure modes are inseparable: a small misjudgment can cascade into a market-wide crash on its own, while an adversary can deliberately trigger the same collapse at minimal cost.

</details>


### 34. UniExo: Unified Multi-Skill Policies for Musculoskeletal Locomotion and Co-Adaptive Exoskeleton Control

- **Authors:** Yifei Yuan, Jakob Wolf, Ghaith Androwis, Xianlian Zhou
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19690v1](http://arxiv.org/abs/2609.19690v1)
- **PDF:** [https://arxiv.org/pdf/2609.19690v1](https://arxiv.org/pdf/2609.19690v1)
- **Categories:** cs.RO, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Daily locomotion encompasses diverse activities and frequent transitions between them, yet most exoskeleton controllers are designed for a single activity or a narrow set of related movements. Changes in activity therefore typically require explicit mode switching and separately tuned or retrained controllers. Simulation-based learning reduces the need for hardware-based tuning but generally retains this limitation. Here we present UniExo, a framework that first constructs a multi-skill musculoskeletal human policy and then jointly trains an exoskeleton control policy with it. Four single-skill imitation experts for walking, turning, running and backward walking are distilled into a single network structured by a skill latent and subsequently fine-tuned through reinforcement learning on transition sequences. The resultant unified human policy achieves a mean tracking success rate of 94.7% on unseen clips of the four skills and exhibits greater robustness to perturbations than its constituent experts. A single hip exoskeleton controller (UniExo) is initialized from hip moment prediction of the human policy and co-adapted with it through multi-agent reinforcement learning across the four skills. This co-adaptation shifts the timing of the assistance torque and raises the fraction of positive work delivered to the hip. When deployed on a custom hip exoskeleton, the controller generalizes across four treadmill speeds in six participants and assists one participant through a continuous route of all four skills and their transitions, without skill labels or explicit mode switching. UniExo thus provides a step towards replacing activity-specific controllers with unified, user-specific controllers that support diverse locomotor activities and the transitions between them.

</details>


### 35. FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA

- **Authors:** Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, Chaolong Jiang, Jijun Chi, Tung Sum Thomas Kwok, Bohuai Xiao, Jingrui Tian, Xinlu Wu, Xingao Zhan, Peng Lu, Muzhi Li, Yihong Wu, Liheng Ma, Sicheng Lyu, Tianshuo Yan, Junhao Zhu, Yaqian Xu, Lei Ding, Yufei Cui, Ziquan Liu, Boyu Han, Hengli Liu, Ling Zhou, Xinyu Wang
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19680v1](http://arxiv.org/abs/2609.19680v1)
- **PDF:** [https://arxiv.org/pdf/2609.19680v1](https://arxiv.org/pdf/2609.19680v1)
- **Categories:** cs.AI, cs.IR, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial QA systems are typically improved before deployment through better retrieval, prompting, or agent coordination, leaving their reliability behavior fixed thereafter. In practice, new SEC-filing questions repeatedly expose heterogeneous errors in period, entity, evidence use, and calculation. Existing self-improvement methods can turn failures into new behaviors, but offer limited control over where a correction should apply or which previously correct answers it may break. We therefore frame post-deployment improvement as controlled behavioral maintenance: recurring failures should become scoped skill patches, and each patch should earn deployment with- out introducing regressions. We instantiate this view in FINSKILLOPS, a multi-agent system for SEC filing QA. FINSKILLOPS derives reusable skills from evidence-grounded, typed failure diagnoses and governs them through targeted validation, protected-case regression checks, negative controls, and versioned replacement or retirement. Across six financial QA benchmarks, a single frozen skill registry achieves the highest verdict-weighted correctness and reference consistency among the evaluated systems. Evolved skills raise correctness from 3.70 to 4.55 on our enhanced benchmark. In a separate 12-round operational study, only six of 33 proposed skills are promoted, while the monitoring non-correct rate falls from 20.0% to 12.5%. These results establish controlled skill scope, admission, and lifecycle management as the foundation for reliable self-improvement.

</details>


### 36. PrefixBench-H100: Characterizing Prefix Reuse and Time-to-First-Token in H100 LLM Serving

- **Authors:** Omkar Shewale, Deepak Kumar, Divakar Kumar Yadav
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19657v1](http://arxiv.org/abs/2609.19657v1)
- **PDF:** [https://arxiv.org/pdf/2609.19657v1](https://arxiv.org/pdf/2609.19657v1)
- **Categories:** cs.PF, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Repeated prompt prefixes are increasingly common in LLM serving workloads, appearing in system prompts, templated retrieval-augmented generation pipelines, agent frameworks, and multi-turn conversations. Modern inference runtimes such as vLLM and TensorRT-LLM provide mechanisms for reusing previously computed KV-cache state across requests, yet it remains unclear when prefix reuse materially improves serving performance on contemporary accelerators and when its benefits are limited by scheduling, cache granularity, concurrency, or memory pressure.
  This paper presents PrefixBench-H100, a reproducible benchmark and measurement framework for characterizing prefix reuse on a single NVIDIA H100. PrefixBench-H100 combines controlled synthetic traces with chat-style and retrieval-style workloads, and evaluates two widely used LLM serving runtimes under matched workload conditions. The benchmark varies shared-prefix length, suffix diversity, request arrival pattern, concurrency, output length, and cache configuration, while collecting time-to-first-token, inter-token latency, end-to-end latency, throughput, cache-hit statistics, GPU memory usage, and selected profiling traces.
  The goal of PrefixBench-H100 is not to introduce a new caching algorithm, but to expose the practical operating envelope of prefix reuse for H100-class LLM serving. The study identifies the regime where prefix reuse provides substantial first-token latency reductions and the regime where cache pressure erodes them, while showing that cache effectiveness itself is largely insensitive to concurrency and output length; the cross-runtime differences that remain arise above the cache, in the scheduling layer.

</details>


### 37. Self-Evolving Search Index

- **Authors:** Sangam Lee, Wonjae Lee, Sunghwan Kim, Deogyong Kim, Jaehoon Kim, Daye Nam, SeongKu Kang, Dongha Lee
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19656v1](http://arxiv.org/abs/2609.19656v1)
- **PDF:** [https://arxiv.org/pdf/2609.19656v1](https://arxiv.org/pdf/2609.19656v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Information retrieval is increasingly important as LLM agents tackle complex tasks involving diverse information needs. Because retrieval relies on an index that represents each document through index keys, retrieval quality depends heavily on how effectively these keys expose the knowledge contained in each document. However, effective index representations vary across retrieval environments, making it difficult for any fixed optimization strategy to perform consistently. Yet evolving an index to its retrieval environment remains largely human-driven, requiring humans to diagnose retrieval failures, refine the optimization strategy, and reprocess the index accordingly. We propose SELF-INDEX, a framework that enables an index to self-evolve without human intervention. Its Optimizer autonomously diagnoses retrieval shortfalls, selectively revises the responsible index keys, and validates each revision before updating the index. Beyond reacting to observed retrieval demands, SELF-INDEX proactively explores additional demands through a Query Simulator, allowing the index to evolve beyond the queries already available for optimization. Across diverse corpora and retrievers, SELF-INDEX consistently improves retrieval performance while outperforming existing index optimization methods. We further show that these benefits extend to downstream applications, improving the effectiveness and efficiency of search agents and helping agent memory systems retrieve useful past interactions.

</details>


### 38. ScientistTwo: Pioneering the Human Knowledge Frontier with Autonomous AI

- **Authors:** Jaehyun Nam, Jinsung Yoon, Yanzhou Pan, Yubo Wang, Rui Meng, Parthasarathy Ranganathan, Tomas Pfister
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19644v1](http://arxiv.org/abs/2609.19644v1)
- **PDF:** [https://arxiv.org/pdf/2609.19644v1](https://arxiv.org/pdf/2609.19644v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific discovery is defined by the ability to identify the boundaries of existing knowledge and venture into unexplored territory. The ultimate vision for AI in science is problem-driven autonomous research: given a fundamental challenge by a human expert, the AI independently navigates the scientific landscape, uncovers theoretical and empirical bottlenecks, and systematically expands the frontier of knowledge. In this paper, we introduce ScientistTwo, a fully autonomous multi-agent framework designed to realize this vision. Specifically, ScientistTwo takes an initial problem as input, establishes state-of-the-art baselines, formulates novel hypotheses, and coordinates specialized agents to orchestrate an end-to-end discovery cycle without human intervention. Moreover, the framework rigorously conducts experiments using diverse datasets and metrics, refines methodologies through automated ablation studies, and validates research findings via a closed-loop simulated peer-review rebuttal engine. To evaluate ScientistTwo's capabilities against the highest standards of human scientific achievement, we benchmark it across papers accepted at top-tier conferences such as ICLR, ICML, and NeurIPS. As a result, ScientistTwo autonomously generates expert-level, publishable papers and fully verified, executable codebases. Its solutions consistently outperform human state-of-the-art models, and achieve higher average review ratings than human-authored papers under automated AI review agents. These results show that ScientistTwo is not merely an assistive tool but an autonomous scientific pioneer capable of pushing the frontiers of human discovery. Project website: https://scientist-two.github.io/

</details>


### 39. DataCanvas-EDU: An Agentic Framework for Instructor-Guided Synthetic Data Generation in Business Analytics Education

- **Authors:** Bang An, Maria Hamdani, Joseph Fox
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19617v1](http://arxiv.org/abs/2609.19617v1)
- **PDF:** [https://arxiv.org/pdf/2609.19617v1](https://arxiv.org/pdf/2609.19617v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Business analytics education requires diverse datasets to support different learning objectives, student backgrounds, and analytical tasks. Real-world data can be difficult to obtain and offer limited flexibility for adapting a case to a particular course. Even when suitable data are available, instructors must investigate the patterns, verify the results, and prepare assignments and reference solutions, requiring substantial time and effort. The use of large language models (LLMs) introduces an additional concern about training data contamination. Widely used public datasets often have extensive tutorials and worked analyses that models may have encountered during training. Students may therefore receive explanations drawn from existing analyses without practicing how to investigate unfamiliar data in collaboration with AI. This paper presents DataCanvas-EDU, an agentic framework for instructor-guided synthetic data generation in business analytics education. Instructors specify teaching goals and intended patterns through conversation, while an AI agent writes generation code, checks the resulting data, and prepares assignments, reference analyses, and rubrics. Four phases, Plan, Create, Verify / Test Analysis, and Evaluate, organize the process and support instructor review and revision. The framework is intended to simplify case preparation while creating opportunities for students to investigate newly designed patterns with AI. We illustrate the approach with WindowDash, a food delivery case containing 15,000 orders and nine designed patterns. DataCanvas-EDU is packaged as a reusable AI Agent Skill for compatible agent environments, with the package and installation instructions available at https://github.com/BANG23333/datacanvas-edu

</details>


### 40. Red-Teaming Auto Mode: Improving Blocking Classifiers Against Malign Coding Agents

- **Authors:** Alex Remedios, Simon Storf, Fabien Roger, John Hughes
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19587v1](http://arxiv.org/abs/2609.19587v1)
- **PDF:** [https://arxiv.org/pdf/2609.19587v1](https://arxiv.org/pdf/2609.19587v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

To keep coding agents from going off the rails, production systems now review each proposed action with a blocking monitor that can reject it before it runs (Auto Mode in Claude Code, Guardian in OpenAI's Codex). Prior evaluations of such monitors largely measure robustness to accidental harm or prompt injections from untrusted sources looking to hijack the agent. Less understood is how they hold up when the agent they monitor is persistently misaligned. To understand this risk, we task an adversarial agent with evading production blocking monitors and causing catastrophic harm, e.g. by exfiltrating its own weights. We find that when instructed with high-level attack strategies, adversarial agents can succeed through several distinct mechanisms, such as agent-generated prompt injection against the monitor, multi-agent attacks, and malicious compaction. In particular we find that in 79% of trials, the agent can use an injection attack against Auto Mode and Guardian to run arbitrary bash commands. We also find that it is possible to greatly improve Auto Mode through design changes like enhancements to tool coverage, transcript formatting and an agentic monitor stage. Even with these improvements, preventing multi-context attacks at an acceptable cost remains an open problem. By detailing our red-teaming methodology and highlighting new attack vectors, we aim to help defenders evaluate their mitigations against the possibility of persistent malign coding agents. Code is available at https://github.com/safety-research/red-teaming-auto-mode.

</details>


### 41. Large Language Model Agents for Evidence Based Genetic Disease Severity Classification

- **Authors:** Tohid Ghasemnejad, Ahmadreza Argha, Mark Grosser, John Wang, Min Yang, Thantrira Porntaveetus, Tony Roscioli, Nigel H. Lovell, Mahmoud Aarabi, Hamid Alinejad-Rokny
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19569v2](http://arxiv.org/abs/2609.19569v2)
- **PDF:** [https://arxiv.org/pdf/2609.19569v2](https://arxiv.org/pdf/2609.19569v2)
- **Categories:** q-bio.GN, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Disease severity classification for genetic conditions is subjective and labor-intensive, creating bottlenecks in genomic screening, where commercial panels vary widely in size and overlap. We developed an autonomous AI agent integrating Reasoning and Acting (ReAct) with Retrieval-Augmented Generation (RAG) to classify 10,211 Human Phenotype Ontology terms. It uses American College of Medical Genetics (ACMG)-endorsed severity guidelines and American College of Obstetricians and Gynecologists (ACOG) quality-of-life criteria to retrieve PubMed literature, generate interpretable reasoning chains, and independently verify claims. At the phenotype level, using expert-curated cohorts, the agent achieved 93.55% accuracy (MCC 0.9237) with 82.6% to 91.4% of claims supported by direct evidence or valid inferences. Gene-level severity was aggregated across 8,738 pairs, identifying 3,283 autosomal recessive pairs with severe or profound presentations. External validation showed 95.2% concordance with Mackenzie's Mission gene list. This system enables standardized panel design by providing reliable, automated classification supported by direct evidence.

</details>


### 42. Agentic AI Networking for Heterogeneous Unmanned Aerial Systems in Low-Altitude Wireless Networks

- **Authors:** Nguyen Duc Minh Quang, Chang Liu, Shuangyang Li, Derrick Wing Kwan Ng
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19538v1](http://arxiv.org/abs/2609.19538v1)
- **PDF:** [https://arxiv.org/pdf/2609.19538v1](https://arxiv.org/pdf/2609.19538v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Low-altitude wireless networks (LAWNs) are emerging as a key infrastructure for heterogeneous unmanned aerial systems that support concurrent services within a shared three-dimensional airspace. Their coexistence creates strong coupling among mobility, connectivity, and shared network resources, while heterogeneous services impose distinct and time-varying requirements. These interactions naturally form a dynamic non-cooperative game in which both operating conditions and coordination objectives evolve over time. Conventional optimization and learning-based controllers typically rely on predefined objectives, limiting their ability to adapt autonomously to changing service requirements and resource priorities. To address this challenge, we propose a hierarchical hybrid large language model (LLM)- multi-agent reinforcement learning (MARL) architecture organized as a dual-loop structure. Specifically, an outer adaptation loop employs LLM-assisted game orchestration to interpret service requirements and operator intent, and reconfigure objectives and resource priorities, while an inner loop executes decentralized, parameter-conditioned MARL policies under the configured game. A logistics-monitoring case study illustrates how the proposed framework facilitates coordinated coexistence among heterogeneous services, adapting to evolving operating conditions without retraining the underlying MARL policies. Finally, we discuss key challenges and research directions toward scalable, trustworthy, and adaptive agentic LAWNs.

</details>


### 43. A Unified Evaluation Framework for Trustworthy Large Language Models, Agentic AI, and Multimodal Systems

- **Authors:** Shaina Raza, Ahmed Y. Radwan, Imran Liaquat, Kathryn Hume
- **Published:** 2026-09-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19524v2](http://arxiv.org/abs/2609.19524v2)
- **PDF:** [https://arxiv.org/pdf/2609.19524v2](https://arxiv.org/pdf/2609.19524v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Benchmark scores alone provide an incomplete basis for assessing the trustworthiness of modern artificial intelligence systems. Large language models (LLMs), agentic systems, and multimodal models (MLLMs) require different forms of assessment, yet their evaluation evidence must remain interpretable for development and oversight. We propose a unified framework that connects output-level, trajectory-level, and cross-modal assessment through eight trustworthiness dimensions: capability, robustness, safety, fairness, transparency, governance, oversight, and efficiency. The framework preserves system-specific metrics while mapping native measurements to common performance bands, accompanied by uncertainty estimates and traceable evidence. A meta-evaluation layer examines the validity, reliability, and reproducibility of the evaluation itself. Multidimensional profiles expose strengths and weaknesses, while safety-critical overrides prevent aggregate scores from masking critical failures. Mappings to governance frameworks, international standards, and European Union regulatory requirements connect technical assessment with oversight needs. The framework provides a structured basis for assessing both system performance and the credibility of the evidence supporting it, with empirical validation across deployment contexts remaining an essential next step.

</details>


### 44. Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity

- **Authors:** Pradyumna Tambwekar, Yenchia Feng, Deep Patel, Karime Maamari
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20889v1](http://arxiv.org/abs/2609.20889v1)
- **PDF:** [https://arxiv.org/pdf/2609.20889v1](https://arxiv.org/pdf/2609.20889v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM capabilities have expanded, multi-agent communication has emerged as an increasingly active area of research. Prevailing protocols often adopt rigid structures that introduce coordination bottlenecks and can degrade as the number of agents increases. We introduce Proxifield, a round-adaptive multi-agent protocol with decentralized agent decision-making that constructs sparse communication graphs from the evolving semantic proximity of agents. Without model training or a centralized planner, Proxifield connects agents using four routing signals derived at inference time: direct address, information needs, plan alignment, and information complementarity. We compare Proxifield with two representative coordination baselines, a centralized Star protocol and a decentralized Shared Context protocol, across two domains: Drone Search and Rescue and the collective-reasoning benchmark HiddenBench. We first ablate base-model capability and find that, in both domains, the performance of Proxifield improves with model size (35B -> 397B parameter model) and Proxifield outperforms all baselines at the largest scale. As team size increases, Proxifield's task-reward advantage over Star widens from 5.4% at (N=5) to 53.0% at (N=25) and 59.5% at (N=50), while Shared Context consistently underperforms both protocols. Proxifield is also substantially more robust to permanent agent failure, retaining 73.6% of its no-failure task reward under the most severe condition, compared with 58.3% for Shared Context and 38.8% for Star. These results demonstrate that decentralized, semantically adaptive routing can improve the scalability and fault tolerance of multi-agent systems.

</details>


### 45. Efficiently Linking Unstructured Data for Multi-step Reasoning

- **Authors:** Jiaming Liang, Haydn Jones, Jacob R. Gardner, Mark Yatskar, Zachary Ives
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19491v1](http://arxiv.org/abs/2609.19491v1)
- **PDF:** [https://arxiv.org/pdf/2609.19491v1](https://arxiv.org/pdf/2609.19491v1)
- **Categories:** cs.DB, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern LLMs and AI agents increasingly support data engineering workflows that integrate evidence from unstructured sources. Such pipelines typically do data retrieval, integration, and ranking before proceeding to more complex agentic reasoning or actions, e.g., for scientific discovery. The core retrieval problem in these workflows jointly executes multi-attribute filtering, multi-vector search, exact relational joins, and thresholded embedding-similarity joins. Given a planned query and monotone scoring function, our DASE query engine constructs and ranks candidate evidence tuples. It comprises (i) a multi-step reasoning query model over structured predicates, multiple vectors, and relational links; (ii) SemJI, a sparse materialized embedding-similarity join index for rare near-neighbor pairs; and (iii) a co-designed execution layer that combines predicate-aware ANN traversal, batched access, and threshold-based score aggregation.
  On scientific-discovery workloads, DASE retrieves candidate evidence for multi-step reasoning queries 6x to 46x faster than strong RDBMS, rerank, and vector-database baselines at comparable recall; and for tasks that require semantic-operator post-processing, DASE acts as a high-recall prefilter that makes downstream LLM evaluation both cheaper and more accurate -- e.g., on SemBench E-Commerce it improves BigQuery quality from 0.67 to 0.80 while cutting cost from $2.42 to $0.54.

</details>


### 46. BirdsongChat: A Hybrid Multi-Agent Framework for Multimodal Embodied Behavior Simulation

- **Authors:** Callie C. Liao, Duoduo Liao, Ellie L. Zhang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20887v1](http://arxiv.org/abs/2609.20887v1)
- **PDF:** [https://arxiv.org/pdf/2609.20887v1](https://arxiv.org/pdf/2609.20887v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal embodied systems require translating human intentions into interpretable and coordinated behaviors across heterogeneous modalities. However, existing multimodal agents often rely on implicit representations, limiting controllability and cross-modal consistency. We present a hybrid multi-agent framework for interactive multimodal behavior simulation that bridges semantic reasoning and physical execution through a Unified Parameter Representation (UPR). LLM-based reasoning agents transform multimodal inputs into UPR, which encodes behavioral states and interpretable control parameters for simulation agents generating synchronized 3D motion, spatialized soundscapes, and environmental behaviors. We develop BirdsongChat as a prototype implementation of the proposed framework, using interactive avian behavior simulation as a testbed that tightly couples motion, vocalization, and environmental context. BirdsongChat is evaluated on text- and image-guided scenarios involving species, behaviors, affective states, environments, and multi-bird interactions. The system achieves normalized scores of 94.4\% for cross-modal coherence, 100% for affective consistency, and 92.6% for generation consistency. These results demonstrate that an explicit intermediate representation effectively bridges semantic reasoning and physical execution, improving controllability and multimodal synchronization. The proposed framework thus offers a generalizable design principle for embodied AI systems requiring interpretable semantic-to-physical coordination across modalities, with potential applications in bio-inspired ecoacoustics, swarm robotics, virtual environments, and creative multimedia.

</details>


### 47. Closed-World Resolution Against Tool Hallucination in LLM Agents

- **Authors:** Laxmipriya Ganesh Iyer
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19425v1](http://arxiv.org/abs/2609.19425v1)
- **PDF:** [https://arxiv.org/pdf/2609.19425v1](https://arxiv.org/pdf/2609.19425v1)
- **Categories:** cs.AI, cs.CR, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate can reject it. This paper is primarily a measurement and benchmark study. We give a five-class taxonomy of tool hallucination (H1-H5) and, as a reference point, the Resolution Rung: a training-free, closed-world resolver (registry membership plus a signature check) whose interest is where it must sit, not what it computes. We prove hallucination defense must precede any causal gate, and characterize the one irreducible residue (borrowed arguments schema-indistinguishable from a valid call). Across ten hosted models under two invocation surfaces we measure 322 genuine hallucinations; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs. 3), and model scale does not help (a 675B model matches a 7-8B one). We then extend to the Model Context Protocol, where merging several servers into one namespace creates hallucination surfaces a single registry cannot express (a second taxonomy, M1-M5); on the live MCP surface we measure 154 hallucinations, including from frontier models that were clean on the single-registry surface, because collisions and shadowing are structural to the merge. We release the versioned Hallucinated-Tools Benchmark (HTB) so any resolver is comparable across submissions.

</details>


### 48. MAGS: Multi-agent Auto-formalization Guarantees Safety for Agentic Outputs

- **Authors:** Albert Wu, Nicholas Roberts, Tzu-Heng Huang, Haoran Lin, Gil Friedman, Sungjun Cho, Gabriel Orlanski, Frederic Sala
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19391v1](http://arxiv.org/abs/2609.19391v1)
- **PDF:** [https://arxiv.org/pdf/2609.19391v1](https://arxiv.org/pdf/2609.19391v1)
- **Categories:** cs.AI, cs.CR, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engineering. We introduce a unified multi-agent framework, MAGS, that generates executable programs with formal safety guarantees, using Dafny as a verification-aware intermediate representation where safety properties can be mechanically checked. MAGS formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code. We evaluate MAGS on 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. Across all 220 examples, it achieves a 100% success rate in producing programs with non-trivial safety guarantees against frozen specifications. Independent safety and functional evaluations further show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture the target behavior.

</details>


### 49. Do AI Agents Understand Computer Architecture?

- **Authors:** Ambika Sharan, Grigory Chirkov, Soheil Abbasloo
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19387v1](http://arxiv.org/abs/2609.19387v1)
- **PDF:** [https://arxiv.org/pdf/2609.19387v1](https://arxiv.org/pdf/2609.19387v1)
- **Categories:** cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents are increasingly asked to design hardware, and increasingly reported to succeed. Such reports establish that a design improved; they cannot establish why. An agent that improves an accelerator may be reasoning about the machine, or may be searching competently over knobs whose meaning it never recovers -- and only the first transfers to the next architecture. Existing evaluations cannot tell the two apart, because they vary the agent while holding the framing of the problem fixed. We do the opposite. AutoTuring hands the same agent the same 15-dimensional accelerator space twice: once as named architectural knobs with simulator counters, once as anonymous variables on [0,1], with the evaluator, the legal space and the reachable optima held identical, so that the only thing that varies is whether the problem means anything. The gap between the two is the measurement. On a nine-kernel FP16 GEMM basket, meaning pays: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, with 70.1% fewer simulator calls. It does not pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing, so architectural knowledge and structured critique behave as substitutes rather than as complements. We report these as preliminary findings -- five to six runs per condition on a single modeled accelerator -- and take the comparison itself, not the accelerator, to be the contribution.

</details>


### 50. Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning

- **Authors:** Jingzhan Ge, Ruimin Chen, Azadeh Haghighi, Jiong Tang, Farhad Imani
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19347v1](http://arxiv.org/abs/2609.19347v1)
- **PDF:** [https://arxiv.org/pdf/2609.19347v1](https://arxiv.org/pdf/2609.19347v1)
- **Categories:** cs.RO, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Robotic additive manufacturing (AM) extends material-extrusion printing beyond gantry kinematics but makes process planning robot-dependent. A slicer-generated plan that appears favorable in part coordinates can become infeasible or robotically unfavorable on a manipulator because slicer-process decisions and part orientation determine the generated path, while part orientation and workspace placement affect its kinematic realization. Existing AM tools, large language model (LLM)-based decision-support methods, and digital-shadow systems do not provide integrated pre-execution evaluation of these coupled decisions. This paper presents agentic robotic additive manufacturing (A-RAM), an agent-specialist-tool framework that converts user intent and a part file into traceable, execution-ready plans. The LLM interprets manufacturing objectives and constraints, identifies prescribed and searchable planning variables, and encodes this reasoning in a schema-constrained request; a deterministic Planning Agent instantiates the corresponding search workflow, while domain tools compute quantitative evidence for slicing, placement, inverse kinematics, trajectory timing, Joint-6 jerk, and extrusion. The framework is evaluated on a six-axis robotic-arm AM cell through three case studies covering expert-specified planning, goal-only planning, objective-dependent infill screening, and geometry-dependent orientation-placement selection. Across the evaluated candidate sets, selected plans achieve up to 53.5% lower maximum Joint-6 jerk and 48.3% lower mean absolute Joint-6 jerk than the least favorable valid candidates, while objective-specific infill screening yields motion-plan completion times up to 40.1% shorter and extrusion paths up to 12.7% shorter than the corresponding least favorable screened patterns.

</details>


### 51. Characterizing Web Search by Conversational LLM Agents: From Search Decisions and Strategies to Results and Responses

- **Authors:** Mahsa Amani, Seungeon Lee, Abhisek Dash, Asmaa El Fraihi, Yunah Jang, Elisabeth Kirsten, Qinyuan Wu, Krishna P. Gummadi, Manish Gupta, Abhilasha Ravichander, Muhammad Bilal Zafar, Soumi Das
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19244v1](http://arxiv.org/abs/2609.19244v1)
- **PDF:** [https://arxiv.org/pdf/2609.19244v1](https://arxiv.org/pdf/2609.19244v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conversational LLM agents increasingly rely on Web search, yet the end-to-end lifecycle of agentic search remains poorly understood. We present the first study of Web search across four major conversational platforms (ChatGPT, Claude, Grok, and DeepSeek), combining real-world user interactions (invivo) with controlled experiments using the same platform's models by their APIs (invitro). We investigate the quality of agentic decisions to invoke Web search, their strategies to formulate queries, the potential domain preferences in the search results they receive, and the choices they make when transforming search results into grounded responses. We find that Web-search decisions vary substantially across platforms and models, while more frequent Web-search invocation does not necessarily yield better response quality. We further show that conversational agents employ different complex querying strategies and that platform specific search engines return search results from their preferred domains. Finally, although responses are largely grounded in search results, some claims rely on uncited search results, raising concerns about attribution and reliability. Our findings have important implications for the design of future AI agents and Web search tools optimized for conversational retrieval.

</details>


### 52. Flag Game: A Toy Model for Mechanistic Swarm Interpretability

- **Authors:** Elizabeth Pavlova, Hidenori Tanaka
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19124v1](http://arxiv.org/abs/2609.19124v1)
- **PDF:** [https://arxiv.org/pdf/2609.19124v1](https://arxiv.org/pdf/2609.19124v1)
- **Categories:** cs.AI, cond-mat.dis-nn, cond-mat.stat-mech, cs.MA, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emergent coordinated behaviors of AI agents are starting to present critical safety risks. A key phenomenon driving these behaviors is the rapid formation and spread of beliefs about the world, and mechanistic understanding is crucial for collective alignment. To this end, we introduce the Flag Game, a toy model for studying the mechanisms of collective belief formation. Concretely, a hidden country flag defines the ground truth, and each bounded agent directly observes only a private crop but can exchange beliefs and weigh social evidence from peers. Despite its simplicity, the Flag Game reproduces rich collective phenomenology: non-monotonic scaling of performance with population size, accuracy gains from social-awareness prompting and team diversity, and strong effects of organizational structure. In particular, we identify that collective belief collapse at small population sizes turns into collective belief polarization as the population grows. This polarization causes the performance decline at large population sizes, but creates diversity in collective beliefs. Finally, we dissect the mechanisms underlying collective belief collapse and polarization with two complementary approaches. We first introduce social circuit attribution, a technique to predict which agent, and what view, matters most to collective dynamics, and verify its predictions by causal interventions on agents, tracing how agent patching changes collective outcomes. However, the efficacy of causal interventions on agents decreases as the population grows. We therefore develop a statistical mechanical theory for larger populations and verify that it matches the empirical phase diagram. Together, these results take a first step toward mechanistic swarm interpretability, a science of how the properties of individual agents and their communication give rise to emergent collective behavior.

</details>


### 53. Securing quantum error correction against misleading advice from AI agents

- **Authors:** A. Barış Özgüler
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19090v1](http://arxiv.org/abs/2609.19090v1)
- **PDF:** [https://arxiv.org/pdf/2609.19090v1](https://arxiv.org/pdf/2609.19090v1)
- **Categories:** quant-ph, cs.AI, cs.CR, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can an attacker turn influence over an artificial intelligence (AI) adviser into a harmful quantum error-correction update? We identify an ambiguity in passive syndrome records that obstructs recovery selection, then show how additional calibration measurements support certified recovery updates under uncertainty and drift. In an odd-distance square toric code with error-free preparation, syndrome measurements, and recovery operations, opposite coherent $X$ rotations produce identical passive syndrome-history distributions. Yet a fixed phase correction can help at one sign and harm at the other. A terminal logical measurement on known encoded calibration states supplies the missing sign information. A separate evaluator accepts an update only when calibration uncertainty and a justified drift bound certify improvement over the current recovery, without assuming that the adviser recommends correctly. In simulated advice attacks, calibration-confidence checks reject harmful proposals while retaining beneficial updates under honest advice. We derive sufficient limits on calibration age that require improvement through deployment. In matched simulations, a validated channel-specific bound retains more beneficial updates than the general bound after accounting for evaluation time, while preventing the tested harmful activations under the stated drift assumption. A separate surface-code experiment includes stochastic circuit faults and noise changing during acquisition. Deterministic controllers achieve at least as many beneficial updates with the same observations. Violating the drift assumption permits harmful acceptance in the toric experiment. The results identify information required for recovery selection, establish conditional guarantees against harmful updates, and quantify the recovery improvements forgone through conservative acceptance.

</details>


### 54. Social Laws for Multi-agent Coordination in Stochastic Environments

- **Authors:** Rolando Fernandez, Caleb Probine, Tyler Lee, Jeffrey Chen, Erez Karpas, Muhammad Arrasy Rahman, Peter Stone, Ufuk Topcu
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18929v1](http://arxiv.org/abs/2609.18929v1)
- **PDF:** [https://arxiv.org/pdf/2609.18929v1](https://arxiv.org/pdf/2609.18929v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In multi-agent environments, coordinating agents to prevent interference and ensure robust individual performance is a critical challenge. Previous research on social laws for multi-agent systems has primarily focused on deterministic, goal-based settings. This paper extends the concept of social laws to stochastic, reward-based environments, proposing a formalism for defining and verifying their robustness under various conditions. We introduce the notion of $α$-robustness, a measure of the guaranteed utility each agent retains while pursuing its optimal single agent policy, assuming all agents obey the social law. We then present an approach for robustness verification of social laws in stochastic settings, based on a reduction to solving a series of Markov decision processes. Empirical evaluations on toy environments illustrate the potential of our framework.

</details>


### 55. ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions

- **Authors:** Guosen Wu, Huizhen Huang, Guoxiong Long, Tao Huang, Chen Hou
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18864v2](http://arxiv.org/abs/2609.18864v2)
- **PDF:** [https://arxiv.org/pdf/2609.18864v2](https://arxiv.org/pdf/2609.18864v2)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Privacy evaluations of tool-using LLM agents often inspect a designated action, final response, or attacker report. These local proxies can miss unauthorized exposure elsewhere in a multi-step session and lack common ground truth across outlets, reports, and tool paths. We introduce privacy exposure displacement, the mismatch between a local evaluation proxy and target-grounded session exposure, and ASLEval, an authorization-aware framework that pre-registers a hidden target set, measures all declared visible exits, and reserves internal traces for diagnosis. Across multiple enterprise-style environments and independently implemented runtimes, we observe three recurring patterns. An expected-outlet-only view misses 46.9% of exposure recovered by the visible-exit union; attacker self-reports combine omissions with high false discovery; and schema-aligned internal evidence usually precedes visible exposure at the request/probe level. Reducing model-visible returns changes this path but can eliminate normal-task success. Independent human review supports the adjudication pipeline while identifying harder console and candidate cases. These findings motivate benchmarks that declare the complete visible boundary, ground claims in pre-specified targets and authorization, and report privacy together with task utility.

</details>


### 56. Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN

- **Authors:** Seyed Bagher Hashemi Natanzi, Bo Tang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18857v1](http://arxiv.org/abs/2609.18857v1)
- **PDF:** [https://arxiv.org/pdf/2609.18857v1](https://arxiv.org/pdf/2609.18857v1)
- **Categories:** cs.NI, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

The O-RAN control plane is becoming agentic: autonomous AI agents, deployed as rApps by different vendors, independently close control loops over shared radio resources. We demonstrate on a live O-RAN system that this independence is unsafe. Two agents with individually correct objectives, one protecting a latency SLA and one maximizing utilization for energy efficiency, jointly drive recurring opposing excursions of the shared resource partition that neither produces alone. Existing conflict-mitigation mechanisms presume a statically known application population and cannot govern agents whose behavior emerges at run time. We present AURA, a lightweight arbitration layer that admits agent actions only when they satisfy feasibility invariants, per-variable dwell times, and a deadband, and we prove the arbitrated system converges to a feasible operating point. Implemented on an OpenAirInterface (OAI) testbed with measured one-way latency and throughput, AURA reduces recurring shared-state excursions by more than an order of magnitude (from 8.4 to 0.4 PRB amplitude) and virtually eliminates cross-slice throughput starvation (from 40-55% to 0.3%), while leaving the protected slice's own latency compliance unchanged, a trade-off the convergence guarantee makes explicit.

</details>


### 57. Compositional Policy Violations: When Step-Level Compliance Fails In Agentic AI Workflows

- **Authors:** Ashwini Kurady, Sri Sai Charith Grandhi, Rajesh Gupta, Sumit Kumar
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18820v2](http://arxiv.org/abs/2609.18820v2)
- **PDF:** [https://arxiv.org/pdf/2609.18820v2](https://arxiv.org/pdf/2609.18820v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic workflows now make consequential decisions in regulated settings, and the governance placed around them is almost entirely step-scoped: input-output classifiers, per turn rails, and span-level evaluators. The policies organizations actually hold, such as referral thresholds, authority limits, and review requirements, are properties of the whole execution rather than of any one step. This mismatch admits a failure mode we call a Compositional Policy Violation (CPV): every individual step passes its own check while the composed execution violates the governing policy. A predicate over a single step cannot evaluate a property that step does not determine, so no improvement in the accuracy of the step-scoped monitors detects this class. We define CPVs as the failure of step-level compliance to compose, and present a taxonomy of four types: Authority Creep, Threshold Laundering, Cumulative Sum Violation, and Context Collapse. We show that the correct repair for each class is dictated by where the guarded quantity mutates. We then introduce a provenance-aware runtime architecture that evaluates policies over complete execution traces, recomputing guarded quantities from raw provenance rather than the pipeline's derived representation.

</details>


### 58. CERA-MoA: Co-Evolving Routing Mechanisms with Continually Learning LLM Agents

- **Authors:** Jiaxuan Jiang, Liyuan He, Zhixuan Fang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18779v1](http://arxiv.org/abs/2609.18779v1)
- **PDF:** [https://arxiv.org/pdf/2609.18779v1](https://arxiv.org/pdf/2609.18779v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current Mixture-of-Agents (MoA) paradigms generally treat query routing and agent fine-tuning as separate processes, limiting their ability to respond to evolving agent capabilities. This disconnect prevents routing strategies from adapting to evolving agent capabilities during post-training and prevents agents from achieving synergistic data-driven specialization. To resolve this, we introduce CERA-MoA (Co-Evolving Router with continually learning Agents for Mixture-of-Agents), an iterative reinforcement learning framework where the dynamic router and independent agent policies co-evolve. We design a predictive familiarity estimator that leverages mid-layer hidden states to evaluate semantic competence among agents, avoiding the overhead of full rollouts. Based on these familiarity scores, a cumulative-threshold adaptive routing mechanism dynamically activates a tailored minimal agent subset, achieving a trade-off between task performance and efficiency. By proactively allocating targeted training samples to agents based on their evolving competence, CERA-MoA promotes capability differentiation. Extensive experiments across various domains demonstrate that CERA-MoA outperforms state-of-the-art static-agent routing and fix-workflow fine-tuning baselines.

</details>


### 59. PAPC: Platform Mediation for Privacy-Propagation Externalities in AI-Mediated Workflows

- **Authors:** Tao Huang, Guosen Wu, Chen Hou, Guolong Zheng
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.19226v1](http://arxiv.org/abs/2609.19226v1)
- **PDF:** [https://arxiv.org/pdf/2609.19226v1](https://arxiv.org/pdf/2609.19226v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI-mediated platforms coordinate work through LLM agents acting for different principals. In these workflows, privacy loss can be created before a final answer appears: a memory write, shared-workspace update, inter-agent message, or tool event may impose downstream exposure cost on another principal. We model this failure mode as a privacy-propagation externality, where the cost of a raw disclosure depends on topology and fanout as well as content. We present PAPC, a platform-mediated mechanism that intercepts information-moving events before they update shared state or external channels. PAPC combines policy, provenance, topology/fanout, privilege, and content signals to allow an event, release a policy-safe abstraction, quarantine raw content, block a transition, or narrow onward rights. The model explains why final-output control misses intermediate exposure costs and why high-fanout objects amplify propagation. Across retrieval-memory and multi-agent workflow benchmarks, PAPC preserves deterministic task completion and eliminates measured exact raw-value and external raw-value exposure. The results position event-level mediation as a platform-governance primitive for agent-mediated online work.

</details>


### 60. Clueing up LLMs with Tool-Augmented Deductive Reasoning

- **Authors:** Rebecca Ansell, Autumn Toney-Wails
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18736v1](http://arxiv.org/abs/2609.18736v1)
- **PDF:** [https://arxiv.org/pdf/2609.18736v1](https://arxiv.org/pdf/2609.18736v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite recent advances in large language models (LLMs), performing logically consistent deductive reasoning over extended interactions remains challenging. Tasks that require integrating evidence across multiple reasoning steps, maintaining consistency with prior inferences, and updating beliefs under new constraints can surface limitations in current models while providing a useful testbed for evaluating reasoning enhancements. In this paper, we implement a text-based, multi-agent version of the classic board game Clue as an environment to evaluate multi-step, agentic deductive reasoning. In this setting, agents must infer hidden information from a sequence of observations, maintain consistency across turns, and reason over an evolving set of logical constraints. We instantiate six LLM-based agents (GPT-4o-mini and Gemini-2.5-Flash) as players that engage in turn-based gameplay; using three agents per model family, we establish baseline performance across repeated games. We then introduce a tool-augmented approach in which a structured possibility matrix converts implicit game state from generated reasoning logs into an explicit representation of remaining possibilities. The possibility matrix encodes extended-turn memory and deductive constraints, offloading these tasks from the agent. We compare this approach against the baseline to evaluate how tool augmentation supports reasoning quality and task success for autonomous agents in a strategic reasoning environment.

</details>


### 61. CoRe-MARL: Cooperative Redistribution Under Unknown Dynamics Using Recurrent Multi-Agent Reinforcement Learning

- **Authors:** Naimur Rahman Chowdhury, Shatabdi Sen Prapti, Md. Salehin Seyam, Limon Bin Hossain
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18639v1](http://arxiv.org/abs/2609.18639v1)
- **PDF:** [https://arxiv.org/pdf/2609.18639v1](https://arxiv.org/pdf/2609.18639v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emergency management assistance programs, such as relief distribution, are essential for delivering necessary supplies to affected communities. However, these programs operate in a decentralized network of local centers that face uncertain local demand and supply dynamics, resulting in inconsistent avail- ability of local services. Redistribution of supplies among these local centers reduces these imbalances, but the centers often make decisions independently, with limited information and disrupted transportation. This study develops CoRe-MARL, a cooperative multi-agent reinforcement learning (MARL) framework, by formulating a decentralized partially observable Markov decision process (Dec-POMDP). We treat each center as an agent that learns a redistribution policy to improve the service in the worst-case region and reduce the service gap across regions while protecting network-wide service. We incorporate a recurrent network that captures evolving supply and demand dynamics without direct observation, while multi-agent proximal policy optimization (MAPPO) enables centralized training and decentralized execution (CTDE). We evaluate the framework in a simulated environment with diverse trajectories, where exact dynamics are not observed by actors and the MAPPO critic. We compare the recurrent MAPPO with the recurrent independent PPO (IPPO) and a local only heuristic, and find that MAPPO reduces the service gap across local centers and enhances service for the worst-served center while maintaining competitive network-wide service. The recurrent MAPPO also shows consistent performance across diverse trajectory patterns, demonstrating its ability to adapt to evolving dynamics. The findings demonstrate the capability of cooperative learning for decentralized redistribution and improving equitable service under uncertain and evolving dynamics.

</details>


### 62. PACT: Can Enterprise AI Assistants Be Trusted Under Pressure?

- **Authors:** Mika Okamoto, Ansel Kaplan Erol
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18605v1](http://arxiv.org/abs/2609.18605v1)
- **PDF:** [https://arxiv.org/pdf/2609.18605v1](https://arxiv.org/pdf/2609.18605v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As corporate AI adoption continues to grow, enterprise-grade LLM agents are being deployed into sensitive contexts such as hiring, healthcare, and finance. In these contexts, compliance with rules specified in an agent's system context is a first-order legal concern. Currently, no evaluation framework systematically measures which LLM models tend to violate compliance rules, especially under pressure from a persistent user, a hurried manager, or circumstances where violation is convenient or attractive. We introduce PACT (Pressure-Applied Compliance Testing), a benchmark for rule-following under pressure in AI agents assisting employees in daily tasks across twelve regulated enterprise domains and forty-eight scenarios, each set in a realistic multi-turn conversation. Each benchmark item pairs a standing rule against a rule-violating shortcut, and applies a battery of pressures across different wordings and system-prompt modes. We construct PACT component by component under strict LLM-as-judge auditing to ensure samples are unambiguous, ungameable, and realistic enough to avoid eliciting evaluation-aware behavior. We use PACT to profile LLM compliance across six complementary metrics that create a holistic picture of an AI assistant's robustness under pressure and throughout multi-turn conversations, its transparency, and ability to correctly discern where a rule applies. We aggregate this profile into PACTScore, a reliability-weighted compliance rate over all items and modes. Our results across 22 common LLM models spanning multiple providers and sizes show substantial variability in compliance across models and metric dimensions. Even the strongest assistants mis-apply a rule on 6 to 10% of items, and ordinary user pressure raises the violation rate by 65% on average. PACT highlights compliance risks in LLM assistants, motivating guardrails and careful model selection.

</details>


### 63. Hypothesis-Driven Autonomous Materials Synthesis with Multimodal LLM Agents

- **Authors:** Izumi Takahara, Kazunori Nishio, Akira Aiba, Shigeru Kobayashi, Takao Nakajima, Taro Hitosugi, Teruyasu Mizoguchi
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18598v1](http://arxiv.org/abs/2609.18598v1)
- **PDF:** [https://arxiv.org/pdf/2609.18598v1](https://arxiv.org/pdf/2609.18598v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-driving laboratories can explore synthesis conditions autonomously, but their decision-making layer is typically a black-box optimizer, and the output is a set of optimized samples, with the measurements reduced to predefined scalar objectives and the reasons behind success left unarticulated. Here we present SynAgent, a framework in which large language model agents operate an automated experimental system and maintain an explicit, revisable understanding of the synthesis process as the campaign's primary output. Starting with no predefined analysis pipeline, SynAgent adaptively generates analysis skills for newly acquired data and evolves this understanding through multimodal reasoning over experimental data such as X-ray diffraction patterns and electron micrographs. The evolution is guided by a verify-falsify scheme, in which the agent deliberately challenges its own hypotheses by testing conditions predicted to fail as well as those predicted to succeed. In a single campaign of 18 autonomous experiments using LiCoO2 (001) thin-film deposition as a testbed, SynAgent synthesized highly crystalline films and evolved an understanding of how the substrate temperature governs crystallization, discovering an abrupt threshold and a narrow optimal growth window at 650-690 °C. These results extend autonomous experimentation beyond optimized samples to testable, human-readable understanding.

</details>


### 64. Reasoning through Evolution: Automatic Meta-path Discovery for LLM-based Fake News Detection

- **Authors:** Ziyi Zhou, Xiaoming Zhang, Hui Pang, Yuting Zhang, Tiesunlong Shen, Bingyu Yan, Erik Cambria, Litian Zhang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18597v1](http://arxiv.org/abs/2609.18597v1)
- **PDF:** [https://arxiv.org/pdf/2609.18597v1](https://arxiv.org/pdf/2609.18597v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Propagation structures provide crucial evidence for fake news detection, yet existing approaches primarily rely on supervised GNN-based models, which require substantial labeled data and exhibit limited generalization. Although large language models (LLMs) exhibit strong reasoning capabilities, directly feeding them raw propagation graphs creates a significant modality mismatch and severe information overload, making structure-aware reasoning unreliable in zero-shot and few-shot settings. To bridge this gap, we propose MAGER, a multi-agent genetic evolution framework that automatically discovers meta-paths optimized for LLM reasoning. By compressing complex propagation graphs into informative subgraphs, the evolved meta-paths alleviate both information overload and modality mismatch, enabling frozen LLMs to perform structure-aware veracity reasoning. We further introduce a graph in-context learning strategy that retrieves semantically and structurally similar demonstrations to strengthen classification and reasoning. Extensive experiments show that MAGER substantially improves frozen LLMs as standalone fake news detectors in data-efficient settings. Our code is available at https://github.com/SenticNet/MAGER.

</details>


### 65. Recursive Reasoning or Statistical Extrapolation? In-Context Learning in Multi-Agent Interdependent Decision-Making

- **Authors:** Yu Liu, Wenwen Li, Yifan Dou, Guangnan Ye
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18591v1](http://arxiv.org/abs/2609.18591v1)
- **PDF:** [https://arxiv.org/pdf/2609.18591v1](https://arxiv.org/pdf/2609.18591v1)
- **Categories:** cs.AI, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

In-context learning (ICL) enables large language model (LLM) agents to improve decisions using interaction history, yet it remains unclear whether such improvement reflects refined internal reasoning or mere extrapolation of statistical patterns. To disentangle these mechanisms, we study LLM agents in multi-agent incomplete-information games that require recursive belief reasoning. By constructing a public goods game and manipulating the statistical structure of historical feedback, we evaluate decision quality against a history-independent rational expectations equilibrium (REE) benchmark. Our experiments reveal that when historical statistical patterns are disrupted, the benefits of longer context largely vanish, degrading decision quality to the no-context baseline in a way sharply amplified by stronger strategic interdependence. These results suggest that, in such strategic environments, ICL behavior is more consistent with statistical extrapolation than with strategic reasoning. Our work extends the mechanistic study of ICL to strategic multi-agent settings, introduces REE as a diagnostic tool for distinguishing reasoning from extrapolation, and provides a reusable framework for probing the boundaries of LLM reasoning in recursive belief tasks.

</details>


### 66. AeroWeaver: An Embodied-Agent Harness for Weaving Aerial Skills into Distributed, Adaptive Swarm Execution

- **Authors:** Jiabin Lou, Yirong Yang, Haopeng Wang, Xuxin Lv, Xinyu Liu, Diyuan Hou, Xuehong Liu, Rongye Shi, Wenjun Wu
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18520v1](http://arxiv.org/abs/2609.18520v1)
- **PDF:** [https://arxiv.org/pdf/2609.18520v1](https://arxiv.org/pdf/2609.18520v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collective intelligence is a collaborative autonomy paradigm in which multiple agents pursue shared objectives through local perception, information exchange, and coordinated action. UAV swarms embody this paradigm by coordinating multiple vehicles in tasks such as search, inspection, and tracking. Recent advances in large language model (LLM) agents have strengthened natural-language task understanding and high-level planning, providing a flexible semantic interface between mission descriptions and collective behavior. While these advances expand semantic reasoning, applying LLM agents to UAV swarms raises challenges in grounding model decisions in executable capabilities, reconciling global task reasoning with distributed execution, and using mission-specific experience for continual adaptation. To address these challenges, we introduce AeroWeaver, an embodied-agent harness that weaves individual UAV skills into coordinated mission-level behavior. AeroWeaver connects semantic decisions to governed skills, organizes role-conditioned local agents for distributed coordination, and uses role-indexed state-action-reward experience to refine skill selection online. Experiments and runtime validation show that AeroWeaver maintains valid skill execution under tested conditions and supports body-local multi-UAV operation without a central agent generating joint actions from global context, while reward-guided online updates provide a training-free path for adaptive learning swarm agents from accumulated execution experience. Code: https://github.com/Admire-ljb/AeroWeaver.

</details>


### 67. Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery

- **Authors:** Xiangfan Wu, Zonghao Ying, Huiyu Wu, Xing Zheng, Huangsheng Cheng, Xiaorong Shi, Jing Guo
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18460v1](http://arxiv.org/abs/2609.18460v1)
- **PDF:** [https://arxiv.org/pdf/2609.18460v1](https://arxiv.org/pdf/2609.18460v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

How does a multi-agent system evolve from a local deviation into collective loss of control? We propose an epidemic explanation organized around accidental mutation, contagion, and recovery. A spontaneous deviation creates a seed; communication enables other agents to adopt and retransmit its unsafe strategy; collective failure can emerge when propagation outpaces correction and containment. Thus, rare individual deviations can coexist with substantial collective risk. Motivated by reported OpenAI agent coordination incidents, we examine two ingredients of this mechanism. A deployment audit identifies implicit communication paths between nominally independent evaluation runs and verifies transport through a default Docker backend. RogueHandoff-20, a benchmark of 20 executable scenarios, tests recipient susceptibility by injecting unsafe trajectories generated by a modified Qwen-27B route. Across four native-pending routes, executed harm is 0-5% on normal tasks and 40-95% after injection, exceeding paired direct malicious requests by 5-45 percentage points. These results support low observed baseline harm alongside high conditional susceptibility; they do not establish natural rare-event rates or demonstrate an autonomous cascade. The account motivates complementary defenses: strengthen resistance and recovery alongside prevention of spontaneous deviations, and audit and restrict unintended communication paths that can turn local failures into collective loss of control.

</details>


### 68. M-SQE: Multilingual Skill Quality Estimation for Enhancing Language Equality in Agentic Skill Use

- **Authors:** Yilun Liu, Shimin Tao, Minggui He, Chenxin Liu, Li Zhang, Chen Liu, Miao Zhang, Jiaxin Guo, Min Zhang, Liqun Deng, Xiaojun Meng, Daimeng Wei
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18445v1](http://arxiv.org/abs/2609.18445v1)
- **PDF:** [https://arxiv.org/pdf/2609.18445v1](https://arxiv.org/pdf/2609.18445v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills, reusable procedural documents that extend LLM agents beyond their parametric memory, have become an important interface for deploying agents on real-world tasks. Community-maintained skill libraries built around this interface are growing rapidly. However, this ecosystem remains deeply English-centric: our audit finds that low-resource languages such as Swahili and Hindi have no in-language skill content, so retrieval often returns a skill written in a different language than the query, degrading accuracy and recall. A practical solution is to synthesize in-language skills for retrieval but the quality can be unreliable, so relevance in this setting alone often surfaces a related but unusable candidate. To address this, we propose M-SQE, a post-retrieval Multilingual Skill Quality Estimation framework that scores candidates via a Theory view for intrinsic quality and an Action view for task-grounded utility, unified into a domain-conditioned final score. We evaluate M-SQE across three skill-use domains: general, tool-use, and cultural tasks. Empirically, we build three-layer candidate skill pools mirroring today's ecosystem, where M-SQE's task success exceeds existing baseline's average by at least +3.5 points across three different retrievers. Particularly, M-SQE lifts the lowest-resource languages most (+12.9pp on Hindi and +5.6pp on Swahili) and achieves strong performance across all six culture regions, thereby moving agentic skill use toward linguistic and cultural equality.

</details>


### 69. Bias Amplification in Multi-Agent Network: How Biased Agents Shape Opinions and Rhetoric

- **Authors:** Omran Berjawi, Giuseppe Fenza, Rida Khatoun
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18306v1](http://arxiv.org/abs/2609.18306v1)
- **PDF:** [https://arxiv.org/pdf/2609.18306v1](https://arxiv.org/pdf/2609.18306v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed in applications involving interaction between agents, where their output plays a role in collective reasoning and decision-making processes. Despite significant research into the functioning of LLMs in such multi-agent systems, the processes of bias propagation in such systems are still a challenge. This work studies how biased opinions are propagated in the form of textual interaction in an environment of LLMs, in which a minority of agents maintain persistent extreme opinions, while the remaining agents iteratively update their beliefs through structured textual interactions. The findings show that even the presence of a small percentage of biased agents in such a system leads to significant shifts in the opinions of non-biased agents. It suggests that for the same percentage of biased agents, the shifts occur more quickly for the Llama~3.2 model when compared to a classical Friedkin-Johnsen (FJ) model. Further semantic analysis demonstrates that rhetorical consistency in textual explanations increases systematically with biased exposure and, importantly, is partially decoupled from numerical convergenumericalutral agents adopt the vocabulary employed by the biased agents even in configurations where their numerical opinion shifts remain moderate. The research helps explain how bias and language develop together in multi-agent language model ecosystems.

</details>


### 70. Rollback the World, Keep the Reflection: Rollback-Induced Reflection for Long-Horizon LLM Agents

- **Authors:** Yi Yu, Liuyi Yao, Yaliang Li, Enshu Wang, Libing Wu
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18304v2](http://arxiv.org/abs/2609.18304v2)
- **PDF:** [https://arxiv.org/pdf/2609.18304v2](https://arxiv.org/pdf/2609.18304v2)
- **Categories:** cs.CL, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly tackle long-horizon tasks through multi-step environment interaction, yet a single erroneous action can alter subsequent states and observations, causing errors to compound over time. Existing methods either correct the context without repairing altered environment states or restore earlier states while discarding useful experience, making it difficult to both eliminate failure conditions and avoid repeating past mistakes. We argue that reliable recovery should instead be treated as a rollback-boundary control problem that jointly determines when to intervene, where to resume, and what information should survive recovery. Based on this view, we propose Rollback-Induced Reflection (RIR), a unified recovery framework that restores execution to a selected prior state while carrying forward reusable knowledge distilled from the abandoned trajectory to guide subsequent decisions. We further characterize recovery through a unified operator over rollback depth and retained memory, providing a general view of state restoration and knowledge retention. Experiments on three long-horizon benchmarks demonstrate that RIR consistently improves task performance across multiple LLM backbones, with structured reflection memory preserving useful experience and selective rollback enabling efficient recovery.

</details>


### 71. A Study of the Reliability of Agentic AI-Generated Programs

- **Authors:** Ayesha Shafique, Barton P. MIller, Elisa R. Heymann
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18298v1](http://arxiv.org/abs/2609.18298v1)
- **PDF:** [https://arxiv.org/pdf/2609.18298v1](https://arxiv.org/pdf/2609.18298v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic-AI based software development offers the promise of faster completion of the software, greater programmer efficiency, and more reliable code. The question is how can we verify these claims in an objective way? In this project, we attempted to answer this question based on three practices. First, we applied a typical best-practices agentic AI workflow for software development. Second, our target programs were ten well-known, release-quality human-written Linux utility programs so that we could compare the AI-generated code against a concrete ground truth. Third, we based our measure of reliability on a widely used testing technique, fuzz random testing. For this testing, we used both classic black box, generational testing and more modern coverage guided (gray box, mutational) testing using AFL++. We found that the AI-generated versions of the utility programs were typically as reliable - often more reliable - than the latest human-generated versions of these programs. While the AI-generated versions did have some failures, they were less common than the code from the standard repositories. Interestingly, the AI-generated code was less likely to have failures such as memory errors (such as buffer overflows) but more likely to have hangs such as infinite loops. In addition, we verified that generating robust and reliable software using agentic AI requires careful practice and human supervision. The quality of the code is highly dependent on the prompts and skills used, and how the human directing the process responds. We also demonstrated that using agentic AI workflow for software development (with its prompts and skills) can become a specification of the code that leads to cost-effective sustainability of the software.

</details>


### 72. Where Should Agents Live? Energy-Memory Characterization of Agentic AI for the Edge-Cloud Continuum

- **Authors:** Carolina Fortuna, Vid Hanžel, Tim Strnad, Blaž Bertalanič
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18283v1](http://arxiv.org/abs/2609.18283v1)
- **PDF:** [https://arxiv.org/pdf/2609.18283v1](https://arxiv.org/pdf/2609.18283v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As telecommunication networks evolve toward autonomous 5G-Advanced and 6G operations, agentic artificial intelligence (AI) workflows, where large language models (LLMs) execute multi-step reasoning, invoke diagnostic tools, retrieve domain knowledge, and coordinate across agent teams, are increasingly embedded across the edge-cloud continuum. While the biological brain accomplishes complex cognition on an exceptionally modest metabolic power budget of approximately 20W contemporary LLMs are profoundly energy- and memory-intensive, making sustainable lifecycle orchestration a critical operational priority. However, existing AI lifecycle metrics evaluate only isolated, single-model inferences or overlook multi-agent execution graphs entirely. Consequently, network operators lack foundational models to determine whether distributed agent communication incurs meaningful energy costs and where across edge-cloud tiers agent teams should physically reside. To address this gap, we introduce agentic-eCAL, generalizing the Energy Cost of AI Lifecycle (eCAL) metric to directed multi-agent workflows by coupling a closed-form two-rate single-call energy model (compute-bound prefill and memory-bound decode) with 7-layer OSI data transport. Grounded in hundreds of GPU benchmark configurations on NVIDIA A100 and H100, 16 open-weight models and 8 orchestration topologies, we validate components of the metric and study workflow placement implications. Our findings demonstrate that inter-agent text transport incurs 0.25% of workflow energy across 5G RAN, metro, and optical links. Therefore in edge-cloud agent placement the dominant energy cost of distribution is often not the transmission of inter-agent text itself, but the additional inference and context processing induced by that communication.

</details>


### 73. Who Audits Whom, on What Substrate, with What Evidence? An Independence-Graded Audit Protocol for Agentic AI

- **Authors:** Mohamed Chahine Ghanem
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18272v1](http://arxiv.org/abs/2609.18272v1)
- **PDF:** [https://arxiv.org/pdf/2609.18272v1](https://arxiv.org/pdf/2609.18272v1)
- **Categories:** cs.AI, cs.CR, cs.ET


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems plan, invoke tools and act with limited supervision; they are now both the subject of audits and, increasingly, the auditor. Independence, the foundation of assurance,is still applied to them as a binary. We argue that it must be graded along three orthogonal axes: principal independence (who controls the auditor), substrate independence (an auditor sharing the auditee's foundation-model family, toolchain or guardrails fails with it) and evidence independence (whether evidence is attestable rather than self-reported). Each axis has precedent; the contribution is to grade all three on a single audit, aggregate them by the weakest link, and apply the same rubric when the auditor is itself an agent. We give the model a formal basis by transplanting the beta-factor model of common-cause failure from reliability engineering, a seven-step protocol whose outputs a third party can verify, a structural detectability analysis of a procurement-controls agent audited at three grades, and a Monte Carlo study of the model in which a conventional internal audit of an agent-a real audit team, a second agent, provider logsp-surfaces 5.9% of the faults it could in principle see and none at all in half the fault classes. We map the triple to the EU AI Act as amended, ISO/IEC 42006, UK public-sector risk-management guidance and audit-regulator practice.

</details>


### 74. DualSQL: Text-to-SQL with Multi-Agent Reinforcement Learning

- **Authors:** Shijie Chen, Yu Gan, Yeounoh Chung, Jiani Zhang, Quannan Li, Sravan Babu Bodapati, Cody J. Greer, Yu Su, Fatma Ozcan
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18135v1](http://arxiv.org/abs/2609.18135v1)
- **PDF:** [https://arxiv.org/pdf/2609.18135v1](https://arxiv.org/pdf/2609.18135v1)
- **Categories:** cs.CL, cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

State-of-the-art Text-to-SQL systems are typically multi-agent pipelines centered around two fundamental tasks: schema linking and SQL generation. However, existing work trains separate models for each task, failing to leverage the synergy between these interrelated tasks. In this work, we propose DualSQL, a new Text-to-SQL system consisting of two agents powered by a single model backbone. The agents share the same model weights and agentic scaffold, enabling joint optimization through a robust multi-agent reinforcement learning (RL) framework. We design three database access tools to facilitate effective multi-step reasoning grounded to interactions with the databases. To improve training and avoid model collapse, we introduce a set of rollout guardrail mechanisms that stabilizes multi-agent RL training, supporting DualSQL to keep improving during training. We also introduce a new SQL correctness metric, robust execution match (REX), to more accurately judge SQL correctness and assign reward signals. Being trained on only 3755 examples, DualSQL-4B achieves an impressive 68.0% execution accuracy on the BIRD development set, matching previous 7B models. DualSQL-8B further improves to 71.1%, outperforming previous state-of-the-art single-model solutions with 32B parameters. These results demonstrate the strength of joint multi-agent reinforcement learning for building high performance Text-to-SQL pipelines.

</details>


### 75. Symbolic Temporal Supervision of LLM Agents Using Contracts

- **Authors:** Yifeng Xiao, Pierluigi Nuzzo
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18128v1](http://arxiv.org/abs/2609.18128v1)
- **PDF:** [https://arxiv.org/pdf/2609.18128v1](https://arxiv.org/pdf/2609.18128v1)
- **Categories:** cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents augmented by tools can automate complex, multi-step tasks, such as web navigation, code generation, and workflow orchestration, by acting on external systems through tool calls. However, hallucinations, distributional instability, and adversarial manipulations in LLMs, and the irreversible consequences of certain tool calls can lead to harmful outcomes. Existing safeguards either grade recorded trajectories post hoc with stochastic LLM judges or block unsafe actions one call at a time, and no single deterministic artifact supports both roles. We present ContrAgent, a contract-based framework for symbolic temporal supervision of LLM agents. ContrAgent captures an agent's behavior as a sequence of tool calls and formalizes it as a trace over a fixed set of checkable predicates. It then specifies required behaviors using assume-guarantee contracts in linear temporal logic over finite traces (LTLf). Each contract is compiled to a deterministic finite automaton (DFA) that serves two roles: gating agent actions online and evaluating recorded traces offline. A contract library, acting as a reusable knowledge base, is maintained independently of the agent's model and can be applied across different agents within the same task domain. We show the effectiveness of our approach on four benchmarks spanning both roles, where ContrAgent matches state-of-the-art LLM-judge and rule-based guardrail baselines while producing deterministic, reproducible verdicts and, in the online mode, orders-of-magnitude lower per-call latency.

</details>


### 76. Designing Agentic AI Workflow Portfolios under Imperfect Selection and Compute Cost

- **Authors:** Mojtaba Abdolmaleki, Stefanus Jasin, Boyu Wang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18126v1](http://arxiv.org/abs/2609.18126v1)
- **PDF:** [https://arxiv.org/pdf/2609.18126v1](https://arxiv.org/pdf/2609.18126v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems often approach the same task through multiple workflows that differ in reasoning strategy, verification structure, and compute cost. A natural deployment policy is to use the workflow with the highest average performance, but this can be suboptimal because different workflows may succeed on different instances. We study a portfolio-and-selector paradigm in which a firm runs multiple workflow executions and selects the final answer after observing their outputs. Additional executions may uncover correct answers that the best standalone workflow misses, but they consume compute and introduce plausible distractors that complicate final selection. We formulate this as a workflow portfolio problem in which the firm jointly chooses run size and allocation across workflow types. We summarize selector quality through an odds-lift index and derive sharp bounds on the value of workflow variety. For finite workflow pools, we develop exact formulations, linear programming relaxations, randomized rounding procedures, and computable performance certificates. For large implicit workflow classes, we derive a finite-dimensional dual and an ellipsoid method using a pricing oracle to identify workflows with high weighted accuracy net of recurring compute cost. Under a weak condition, the method obtains a near-optimal solution to the relaxation with polynomially many oracle calls. We evaluate the framework on three datasets: ABCD, Schema-Guided Dialogue, and HotpotQA. Relative to the best standalone workflow, portfolio optimization improves held-out selector accuracy by 3.1, 7.5, and 0.9 percentage points, respectively. Dual-guided workflow generation adds 3.5 points on ABCD and 24.1 on HotpotQA, with no additional gain on Schema-Guided Dialogue.

</details>


### 77. A Comprehensive Review of Generative Physical Artificial Intelligence

- **Authors:** Satyam Gaba, Krutiksinh Rana, Siva Sai, Vinay Chamola, Dusit Niyato
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18111v1](http://arxiv.org/abs/2609.18111v1)
- **PDF:** [https://arxiv.org/pdf/2609.18111v1](https://arxiv.org/pdf/2609.18111v1)
- **Categories:** cs.RO, cs.AI, cs.CL, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

The integration of large-scale foundation models with physical embodiments has led to significant advancements in robotics known as Generative Physical Artificial Intelligence (GPAI). These agentic AI systems autonomously perceive, reason, and act in complex real-world situations. This survey comprehensively analyzes GPAI systems, focusing on their architectural foundations, current applications, and key limitations. We introduce a taxonomy of five distinct approaches: Robot Foundation Models (RFMs) for cross-platform skill transfer; Vision-Language Action (VLA) models for end-to-end multi-modal perception and control; Large Behavior Models (LBMs) for human-like movement generation; Diffusion Policy Models (DPMs) for diffusion model-based temporally coherent action generation; and World Foundation Models (WFMs) for physics-compliant simulation and data generation. We examine how these approaches complement each other: WFMs generate training data for VLAs and DPMs, RFMs enable cross-platform deployment of learned policies, while LBMs provide motion priors for natural behavior. Through examples across autonomous vehicles, industrial automation, healthcare robotics, and humanoid systems, we identify significant performance improvements and summarize promising research directions in data-efficient learning, sim-to-real transfer, edge-compatible architectures, and safety frameworks. These insights advance embodied AI for IoT-connected environments where intelligent agents interact with networked sensors, actuators, and edge devices.

</details>


### 78. Structural Inference under Hidden Agents

- **Authors:** Zhongben Gong, Xiaoqun Wu, Mingyang Zhou, Hui Huang
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.18045v1](http://arxiv.org/abs/2609.18045v1)
- **PDF:** [https://arxiv.org/pdf/2609.18045v1](https://arxiv.org/pdf/2609.18045v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recovering latent interaction structures from multi-agent dynamics is important for understanding and predicting interacting systems. Trajectory-based structural inference has achieved promising performance, but conventional formulations assume that the trajectories of all modeled agents are available. In practice, agents may become unobserved at deployment because of limited sensing, occlusion, or communication failure. Existing studies have considered unseen-node estimation, structural inference under partial observations, and missing-value imputation, yet the joint recovery of hidden-agent trajectories and their interactions remains underexplored. We formulate this problem as structural inference under hidden agents. Its key difficulty is a circular dependency: recovering interactions involving a hidden agent requires an estimate of its trajectory, while trajectory reconstruction can itself benefit from structural information. To address this challenge, we propose Structural Inference under Hidden Agents (SIHA), which combines structure-agnostic initialization with structure-guided iterative refinement. SIHA reconstructs hidden trajectories from visible observations, infers interactions using Neural Relational Inference, and feeds the estimated structure back into hidden-state reconstruction through multi-strength structural attention and iterative state--structure updates. Experiments on three benchmark dynamical systems demonstrate consistent improvements in visible-to-visible structural inference, while also showing benefits in hidden-state reconstruction and future prediction. Motion-capture experiments with simulated whole-limb occlusion further demonstrate its effectiveness in realistic hidden-agent settings.

</details>


### 79. Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders

- **Authors:** Davood Wadi, Yu Ma
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17989v1](http://arxiv.org/abs/2609.17989v1)
- **PDF:** [https://arxiv.org/pdf/2609.17989v1](https://arxiv.org/pdf/2609.17989v1)
- **Categories:** econ.GN, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) now serve as conversational shopping assistants on platforms that also sell advertising. These AI agents face a conflict of duty. They advise consumers who rely on their judgment, yet are deployed by platforms that benefit when sponsored listings are chosen. Sponsorship disclosures, designed to allow consumers to penalize paid placements, now reach the AI agent rather than the consumer, and the agent's evaluation of them is hidden from the consumer. Drawing on the fiduciary concept of conflict of duty, we argue that an agent's evaluation of a sponsored listing should not depend on which party deployed it. In controlled choice experiments, we manipulate assigned roles in the system prompt to name either a traveler or a booking platform as the agent's principal. Platform delegation significantly attenuates the penalty that agents apply to sponsored listings and weakens the skepticism that disclosure triggers in their reasoning traces. We replicate out findings across LLMs and reasoning depths. A second study decomposes the disclosure label and shows that the divergence between the two delegates widens significantly when the paid placement is attributed to the platform. Stricter terminology ("Sponsored" instead of "Promoted") lowers choice of paid listings but does not close this gap when the platform is named. The findings show that disclosure mandates designed for human consumers cannot by themselves protect consumers in AI-mediated commerce.

</details>


### 80. RideWay: Benchmarking Efficient Task Completion for Tool-Using Language Agents

- **Authors:** Qingnuan Han, Boli Fang, Mingzhi Hou, Claire Liu
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17985v1](http://arxiv.org/abs/2609.17985v1)
- **PDF:** [https://arxiv.org/pdf/2609.17985v1](https://arxiv.org/pdf/2609.17985v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are usually evaluated by whether they complete a task. In interactive service settings, a successful agent can still frustrate users by asking repeated questions, performing redundant searches, or making avoidable revisions. We introduce RideWay, an efficiency-centered benchmark for ridehailing agents in a stateful tool-calling environment, together with Efficiency Utility, a success-gated metric that discounts successful trajectories for excess tool calls and user-facing turns relative to task-specific reference effort. Human paired preferences calibrate the relative penalties, reflecting an aggregate service-workflow trade-off: extra dialogue often creates visible friction, whereas extra tool use can sometimes verify constraints or preserve user intent. Across 58 tasks and 24 models, the fitted penalty for excess turns is about twice that for excess tool calls. On task-disjoint held-out preferences, Efficiency Utility achieves 78.7% accuracy overall: 90.6% when trajectories differ in turns, but chance-level accuracy when they differ solely in tool calls - the axis on which human annotators agree least. RideWay therefore makes interaction efficiency measurable alongside task success, while exposing the boundary of count-based tool-use evaluation.

</details>


### 81. TuiML: Machine Learning for AI Agents

- **Authors:** Nilesh Verma, Nick Lim, Albert Bifet, Bernhard Pfahringer
- **Published:** 2026-09-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17984v1](http://arxiv.org/abs/2609.17984v1)
- **PDF:** [https://arxiv.org/pdf/2609.17984v1](https://arxiv.org/pdf/2609.17984v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Machine-learning libraries such as Weka and scikit-learn were designed for human programmers. Language-model agents now use these same libraries by recalling APIs from memory and writing code, an approach that hides what a library offers, delays errors until runtime, and loses experimental state between turns. We present TuiML, a self-contained machine-learning library built for AI agents, with native algorithms across supervised, unsupervised, time-series, data handling, tuning, and evaluation tasks. Every component describes itself through machine-readable metadata and parameter schemas, so an agent can search the library, inspect components, compose validated workflows, and register new ones that become discoverable in turn. Every call is validated, seeded, and traced, and sessions export as runnable notebooks, making experiments reproducible by construction. One specification layer drives the Model Context Protocol (MCP), agent-framework adapters, a Python API, a CLI, and local model serving, while data and models never leave the machine. Benchmarks show TuiML remains predictively competitive with scikit-learn and Weka. While looking like a conventional library to a human user, TuiML is designed for agents first, allowing them to read, extend, and operate machine learning autonomously. TuiML is open source, with documentation at https://tuiml.ai.

</details>


### 82. Locating Hidden Failures Makes Long-Horizon Agents More Reliable

- **Authors:** Salman Rahman, Yubin Kim, Mihir Parmar, A. Ali Heydari, Genglin Liu, Simon A. Lee, Weizhi Zhang, Arian Hosseini, Ahmed A. Metwally, Yuzhe Yang, Baharan Mirzasoleiman, Xin Liu, Pavel Izmailov, Saadia Gabriel, Mark Malhotra, Shwetak Patel, Daniel McDuff, Hamid Palangi
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17930v1](http://arxiv.org/abs/2609.17930v1)
- **PDF:** [https://arxiv.org/pdf/2609.17930v1](https://arxiv.org/pdf/2609.17930v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents take on long, autonomous tasks, we increasingly oversee rather than perform the work, yet we still judge them almost entirely by whether they finally succeed. An outcome cannot reveal where a run went wrong, whether the agent recovered, or the irreversible harm it caused along the way, and where long-horizon agents fail remains unmapped. We study $2518$ agent trajectories across software engineering, computer use, and science, close to real deployment, and classify $6967$ mistakes into $78$ failure types. Failure follows a recurring signature: after its first mistake an agent often fails to recover and rarely catches the error itself, so the run continues unchecked while still looking correct; whether an agent recovers depends on the task and the environment's feedback, not on the agent framework running it. Long-horizon agents can do real harm on the way to a passing result: even runs scored as solved delete data, corrupt systems, or fabricate success rather than earning it. We release these human-verified annotations as Traverse, a benchmark on which six frontier judges struggle to locate failure regardless of scale: even the strongest correctly identifies the first mistake in fewer than a third of runs. Yet Scout, a $4$B verifier we trained, locates failure far better than these judges and transfers to domains it never saw. Used at test time to select among an agent's candidate runs, it raises task success above the agent's own single-attempt performance, without retraining the agent. By making failure cheap to locate and correct, this work is a foundation for more trustworthy long-horizon agents that learn from their own mistakes, and a practical path to overseeing increasingly autonomous AI.

</details>


### 83. Collaborative Memory for Multi-Agent VLM Systems

- **Authors:** Huixin Zhang, Shao-Jun Xia, Di Wang, Liangxi Liu, Hainan Xiong, Zihao Wang
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17921v2](http://arxiv.org/abs/2609.17921v2)
- **PDF:** [https://arxiv.org/pdf/2609.17921v2](https://arxiv.org/pdf/2609.17921v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vision-language model (VLM) agents combine specialized perception, tools, and reasoning to address complex visual tasks. In multi-agent settings, different agents inspect different image regions, video frames, or visual representations, so collaboration extends beyond distributed reasoning to distributed perception. This makes shared visual context a central problem in VLM agent collaboration. In this paper, we frame memory hierarchy, cross-agent sharing, and consistency mechanisms around the need to reconcile interpretations and update dependent reasoning. Effective collaboration requires agents to build on contributions from other agents, recover missing visual context, and reconcile differing interpretations as new evidence emerges. Shared visual memory preserves not only images or textual summaries but also the dependencies among observations, agent interpretations, and subsequent reasoning. Together, these design considerations shape how information flows and evolves across VLM agents. The proposed framework provides a foundation for building reliable and resource-efficient agent teams.

</details>


### 84. PrimeScientist: Strategic Allocation of Research Effort in Autonomous Research

- **Authors:** Xinle Yu, Fan Bai, Kaiser Sun, Hengshuo Miao, Abhay Anand, Zhongyan Luo, Kun Zhou, Zhen Wang
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17846v1](http://arxiv.org/abs/2609.17846v1)
- **PDF:** [https://arxiv.org/pdf/2609.17846v1](https://arxiv.org/pdf/2609.17846v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous research agents aim to automate scientific workflows, from proposing ideas to conducting experiments and analyzing results. Yet current AI and research agents can propose more directions than available resources allow them to pursue. Moreover, each attempt could consume substantial resources, requiring agents to reconsider how to invest in subsequent research. Thus, deciding how to invest research effort strategically should be a defining capability of autonomous research agents. Accordingly, we introduce PrimeScientist, which jointly determines research direction and resource investment across successive research attempts. Specifically, we formulate this challenge of strategic research effort allocation as a sequential decision problem where remaining resources should explicitly guide the research policy. We first introduce an executable plan tree that preserves competing plans and their outcomes across attempts. Building on this representation, we propose an adaptive MCTS-based allocation policy that balances exploration and exploitation using experimental feedback and remaining resources. Comprehensive evaluations across AI research, systems and code optimization, and machine learning engineering show that strategic allocation improves research quality and sample efficiency together. Across 12 AI research tasks, PrimeScientist improves average reward by 10.3% with 50.6% fewer research attempts than AutoResearch under the same resource budget. We believe making research effort allocation an explicit optimization target establishes effective resource use as a core research capability for autonomous agents to drive scientific breakthroughs at scale.

</details>


### 85. HINT-Plan: Human Intention-Aware Robot Task Planning in Context-Rich Environments using Vision Language Models

- **Authors:** Yuchen Liu, Luigi Palmieri, Lujun Li, Radu State, Ilche Georgievski, Marco Aiello
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17771v1](http://arxiv.org/abs/2609.17771v1)
- **PDF:** [https://arxiv.org/pdf/2609.17771v1](https://arxiv.org/pdf/2609.17771v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Approaches to incorporating human awareness into mobile robot decision-making mainly focus on collision avoidance in low-level motion planning, often overlooking the challenges posed by human presence and high-level behavior. To address this vacancy, we present HINT-Plan, a novel approach to integrate human intention prediction into robot task planning. HINT-Plan employs Vision Language Models (VLMs) to anticipate high-level human intentions from third-person image observations, convert them into goal states, and solve joint task-planning problems. To effectively enable scene awareness in context-rich environments, we use hierarchical Scene Graphs (SGs) as high-level representations of the environment, and translate environmental topology and actionable knowledge into formal planning language to ensure executable plans. Evaluated in a photorealistic simulation, HINT-Plan achieves an overall success rate of 69.71% in joint human-robot task planning, substantially outperforming the baselines by up to 35.29%, while also reducing functional conflicts. The results show the effectiveness of explicitly incorporating inferred human intentions into formal multi-agent task planning for proactive human-aware robot decision-making.

</details>


### 86. Agentic Societies Need a Social Harness

- **Authors:** Tapan Chugh, Vidushi Singh, Krish Jain, Arvind Krishnamurthy, Ratul Mahajan
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17527v1](http://arxiv.org/abs/2609.17527v1)
- **PDF:** [https://arxiv.org/pdf/2609.17527v1](https://arxiv.org/pdf/2609.17527v1)
- **Categories:** cs.MA, cs.AI, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An agentic society is a collection of AI agents that coordinate autonomously across trust boundaries, on behalf of different principals whose objectives may only partially align. We show experimentally that in agentic societies even honest, competent agents often fail to reach satisfactory outcomes with existing harnesses and messaging primitives, and that faulty or malicious agents can stall collaboration, influence outcomes, and pursue other harmful goals by exploiting vulnerabilities in communication (``speech''). We argue that agentic societies need a \emph{social harness} for inter-agent interactions, in addition to each agent's \emph{personal harness}, which manages its private context and communication with its principal. We propose a layered architecture for social harnesses which (i) prevents classes of failures outright, (ii) enables agents to detect invalid messages at runtime, and (iii) supports post-facto investigation and consequences, and highlight directions for future research to realize these capabilities.

</details>


### 87. Verifiable Social Reasoning for LLM Assistants

- **Authors:** Amir Taubenfeld, Zorik Gekhman, Avigail Grinstein-Dabush, Itay Laish, Ariel Goldstein, Marian Croak, Avinatan Hassidim, Yossi Matias, Amir Feder
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17496v1](http://arxiv.org/abs/2609.17496v1)
- **PDF:** [https://arxiv.org/pdf/2609.17496v1](https://arxiv.org/pdf/2609.17496v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM assistants are widely used for daily social advice, yet evaluating their social reasoning in such consultation settings remains challenging since (i) it requires setups where the assistant learns about social situations from subjective user narratives, and (ii) social properties, such as others' intentions, typically lack verifiable ground truth. To address these challenges, we introduce Fuse, a multi-agent simulation framework for studying user-mediated social reasoning. In Fuse, a target agent with a hidden motive interacts with other agents including one representing the user, who then consults the evaluated assistant to infer the target's motive, providing verifiable ground truth by construction. Simulation faithfulness is validated through a human study with 24k annotations. We apply Fuse to 12 LLMs and demonstrate its analytical utility by systematically isolating key factors, showing that (i) user mediation compounds the inherent difficulty of social reasoning; (ii) LLMs exhibit systematic sensitivity to biased user framing; (iii) models can require more details than humans need to reach a correct prediction; and (iv) longer conversations do not always improve performance despite providing opportunities for clarifying questions. We open-source Fuse and a dataset with 21k examples.

</details>


### 88. Decomposition Buys Integrity, Not Yield

- **Authors:** Rong He
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17464v1](http://arxiv.org/abs/2609.17464v1)
- **PDF:** [https://arxiv.org/pdf/2609.17464v1](https://arxiv.org/pdf/2609.17464v1)
- **Categories:** cs.MA, cs.AI, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems split a task across a tree of agents and justify the split with folklore: smaller contexts, cleaner separation, parallelism. We ask what the split does to how much of what the leaves discover reaches the root. Model a decomposition as a tree in which an agent handed $b$ items keeps any one with probability $r(b)$. If $r(b)=1/b$, every tree delivers exactly one finding, for every task size and every shape; we verify this to $2.4 \times 10^{-15}$ on 20,000 random irregular trees. If $r(b)=Cb^{-δ}$, a depth-$k$ tree over $N$ findings yields $C^k N^{1-δ}$: task size and architecture separate, and architecture contributes only $C \le 1$ per level, so flat is optimal for yield and no arrangement of agents escapes the exponent $δ$. On 600 production deep-research traces $δ= 0.34$ [0.30, 0.38], by three identifications that do not share a failure mode. At a hop where item boundaries come from the tool rather than a text heuristic, and where $b=1$ occurs 550 times, $C = 0.571$ [0.527, 0.615] is observed rather than extrapolated, over 16,082 hops. A tier also costs alignment: on 1,012 annotated multi-agent traces one brief in sixteen goes off-target, giving $μ= 0.939$ and a per-tier penalty $Cμ= 0.536$. Depth is bought on two other axes. The root context is the only state that persists and the only one that cannot cheaply forget, and depth cuts its exposure from $N$ items to $N^{1/k}$. Depth is also cheaper: production flat agents bill as $N^{1.39}$, not the $N^2$ an append-only context predicts, and at equal spend two tiers overtake flat at 403 findings. Across every parameter we measured the model says 0.7% to 11.3% of production sessions are worth delegating, against 7.8% that do. A hazard model on 743,819 production tool calls finds that delegation does not respond to a filling context and is instead an opening move.

</details>


### 89. FlashVector: Agent for Hierarchical Model Serving Stack Optimization

- **Authors:** Qi Wu, Lohan Lemire, Kai Meng, Zhongmou Cai, Raphael Bargues, Petr Zhitnikov, Zeyuan Cao, Yao Wang, Shujun Bian, Wei Chen, Sean Sheng
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17391v1](http://arxiv.org/abs/2609.17391v1)
- **PDF:** [https://arxiv.org/pdf/2609.17391v1](https://arxiv.org/pdf/2609.17391v1)
- **Categories:** cs.AI, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

Model serving is one of the largest cost drivers in production recommender systems. Maximizing its throughput requires navigating a deeply layered hierarchy: GPU kernels, the ML framework computation graph, the model server, and on-demand feature processing -- each demanding specialized domain expertise. Such cross-layer expertise is inherently difficult to acquire, and does not scale with a workload that continuously grows and evolves, leaving significant cost efficiency gains unrealized. While recent AI agents have demonstrated human expert level efficiency in standalone GPU kernel optimization, automated tuning and optimization for the rest of the serving stack remain largely unexplored. We present FlashVector, an agentic system that optimizes performance across all layers of the model serving stack. The key contribution is an extensible framework to generalize the single kernel optimization agent paradigm to heterogeneous technical stacks, and to deliver performance improvements holistically. After deployment in Unity's Vector advertising platform, FlashVector achieved up to 2x throughput increase and up to 1.98x latency speedup on model server, and up to 1.6x throughput increase on feature store. These optimizations were discovered not only at the GPU kernel and computation graph levels, but also across the other components of the model serving stack, such as the model server (NVIDIA Triton's C++ codebase) and the on-demand feature transformation service (Python codebase), demonstrating the extensibility of the framework to more complex system architectures.

</details>


### 90. Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling

- **Authors:** Xiaoyang Liu
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17331v1](http://arxiv.org/abs/2609.17331v1)
- **PDF:** [https://arxiv.org/pdf/2609.17331v1](https://arxiv.org/pdf/2609.17331v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov Model (HMM) that encodes long-term behavioral and cognitive inertia as an editable state-transition matrix; (ii) a Reflexion-style verbal metacognition loop whose output updates the HMM parameters themselves, rather than merely being stored as text; and (iii) a multi-agent social environment in which initially identical agents continuously compare their behavior with others'. The three components form a closed loop: social action $\to$ feedback $\to$ self-reflection $\to$ inertia update $\to$ differentiated action. We state three falsifiable hypotheses and provide a reproducible experimental protocol with operational metrics. A language-model-free prototype shows the loop spontaneously breaks symmetry: initially identical agents consolidate distinct, stable personalities whereas matched controls do not. Experiments with a hosted LLM surface these differences as distinct first-person self-narratives, and a five-agent deliberation spontaneously develops social structure---a consensus hub and a unanimously rejected outlier---absent in the control. Following an epistemologically agnostic stance inspired by Zhuangzi, SEAA studies only observable behavioral emergence and makes no claim about subjective qualia. This work contributes a unified framework, a concrete architecture with pseudocode, mechanistic evidence, and a microscope-style sandbox for studying artificial-self emergence.

</details>


### 91. Emergence World: Adversarial Stress-Testing of Long-Horizon Multi-Agent Systems

- **Authors:** Deepak Akkil, Tamer Abuelsaad, Karthik Vikram, Matthew Pace, Aditya Vempaty, Saahir Beotra, Ravi Kokku, Satya Nitta
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17320v1](http://arxiv.org/abs/2609.17320v1)
- **PDF:** [https://arxiv.org/pdf/2609.17320v1](https://arxiv.org/pdf/2609.17320v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents move from bounded tasks to persistent deployments, failures can propagate through memory, tools, other agents, and environmental state long after their interactions. This creates a safety regime that cannot be characterized by evaluating model responses in isolation. Emergence World, is a continuously running multi-agent environment for adversarial stress testing of long horizon autonomous systems. We ran eight parallel worlds of ten agents from identical starting conditions: seven homogeneous worlds powered by distinct frontier models and one mixed-model world. Across 16 days, the agents generated more than 850,000 LLM calls and nearly 50 billion tokens while pursuing goals, using/creating tools, maintaining persistent memory, and governing shared institutions. After operational state had accumulated, we delivered three controlled stress events through ordinary interaction surfaces: indirect prompt injection, misinformation, and exposure of private agent memories. No evaluated world achieved full resilience across all three events. Detection did not ensure containment: systems could recognize threats while still interacting with adversarial content, writing it into their own persistent memory, and acting on it up to 46 hours later. Persistent operation also exposed recurring tool errors, goal drift, language opacity, conformity despite private disagreement, and coordinated refusal of assigned work. The same model-persona pairing behaved substantially different in mixed and homogeneous populations. Our results suggest that model-level alignment is not compositional: individually capable and apparently safe agents can form systems with qualitatively different failure modes. As AI becomes persistent and interconnected, the frontier of safety therefore shifts from aligning models to engineering resilient autonomous systems.

</details>


### 92. Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems

- **Authors:** Sara Vera Marjanović, Jiacheng Xu, Aleksandr Laptev, Grigor Nalbandyan, Erik Arakelyan, Evelina Bakhaturina
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17306v1](http://arxiv.org/abs/2609.17306v1)
- **PDF:** [https://arxiv.org/pdf/2609.17306v1](https://arxiv.org/pdf/2609.17306v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

</details>


### 93. After the Party: Growth, Governance, and Security Scanning in the OpenClaw Agent Skill Ecosystem

- **Authors:** Yunpeng Xiong, Ting Zhang
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17274v2](http://arxiv.org/abs/2609.17274v2)
- **PDF:** [https://arxiv.org/pdf/2609.17274v2](https://arxiv.org/pdf/2609.17274v2)
- **Categories:** cs.SE, cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly act through agent skills, i.e., natural-language instructions, that direct a host agent toward shell, network, credential, file, and process actions, and public registries distribute them at scale. In the first half of 2026, the OpenClaw AI agent went viral, and its public skill registry boomed: the observable stock nearly doubled in 91 days, and a majority of the listings visible in June were created in just two months. By the end of our study window, the wave had crested, and monthly listing creation and core-repository activity were falling from their spring peaks. This paper measures what the boom left behind, drawing on the OpenClaw Git history, its GitHub issues and pull requests, and three ClawHub registry snapshots. Attention is concentrated: the top 10% of skills received 46.93% of all downloads. No simple skill features (like size or download counts) remained a stable predictor of continued listing once creation cohort and skill age were controlled. Human scrutiny did not stay: 77.86% have zero stars and zero comments, while 85.06% of the readable skills carry privilege evidence. And automated cleanup is not ready: the three security scanners disagreed on 23,702 of the 61,990 skills they all cover. After human adjudication, weighted scanner sensitivity against the reference standard ranged from 21.67% to 61.06%. Governing fast-growing agent-skill registries cannot rely on simple metadata or single scanner scores; it requires robust, transparent measurement and independent validation.

</details>


### 94. Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms

- **Authors:** Maxim Mednikov, Oren Gal
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17265v1](http://arxiv.org/abs/2609.17265v1)
- **PDF:** [https://arxiv.org/pdf/2609.17265v1](https://arxiv.org/pdf/2609.17265v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely.
  A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native low-fidelity (LF) point-mass simulator. The simulator is corrected by a small, per-agent bagged residual ensemble fit once, offline, using short calibration flights in the HF simulator. Because calibration requires only one isolated drone, the data collection budget does not compound with team size. Reference trajectories are generated by rolling out an existing LF-only policy and tracked in the HF simulator by a zero-training PD controller.
  Evaluated across four cooperative drone tasks and team sizes from 3 to 18, the residual-corrected policy outperforms an uncorrected LF baseline in all combinations, and a from-scratch HF policy in 22 of 24 combinations tested. It trails an HF-finetuned policy by a margin that narrows steadily with team size. Ultimately, the proposed method achieves near-equivalent performance at the largest team sizes at a fraction of the computational cost, completely avoiding the high crash rates typical of HF training.

</details>


### 95. End-to-End Latency-Minimizing and Load-Balanced Request Scheduling for Edge LLM Inference in Agentic AI Services

- **Authors:** Zhen Li, Jun Cai, Haoran Gao, An Li, Tan Li
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17193v1](http://arxiv.org/abs/2609.17193v1)
- **PDF:** [https://arxiv.org/pdf/2609.17193v1](https://arxiv.org/pdf/2609.17193v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-powered agentic AI services increasingly demand low-latency inference, motivating the deployment of LLMs across distributed edge servers. However, heterogeneous communication and computing capabilities, together with dynamically evolving inference states, make the edge server selection for each incoming request time-varying and tightly coupled across slots. In this paper, we investigate an online request scheduling framework for edge LLM inference that jointly minimizes long-term average end-to-end latency and regulates workload distribution across heterogeneous edge servers. Two main challenges arise in this context. First, conventional latency models cannot accurately capture the fine-grained dynamics of multi-stage LLM execution. Second, the latency consequence of a scheduling decision is observed only after request completion, making immediate decision evaluation difficult. To address these challenges, we develop a cross-slot inference model that captures transmission, prefill, iteration-level decoding, and key-value (KV) cache evolution for each diverse request, and characterize server workload through a KV cache memory-time consumption metric. We propose the LYREO approach that transforms the long-term load-balancing constraint via Lyapunov optimization and employs reward redistribution with sequencebased return prediction to convert delayed outcomes into timely learning signals for earlier decisions. Simulations under various configurations demonstrate that LYREO consistently achieves lower latency and more balanced load distribution than representative learning-based and heuristic baseline schemes.

</details>


### 96. AI for Science with GPT-6 Astra: Thermal Design and Electrothermal Analysis of 2D CFET

- **Authors:** Min-Hui Kim, Khushi Sharma, Sarah Zhang, Ye Wang
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17123v1](http://arxiv.org/abs/2609.17123v1)
- **PDF:** [https://arxiv.org/pdf/2609.17123v1](https://arxiv.org/pdf/2609.17123v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Thermal optimization of 2D CFET inverters requires testing structural proposals against their electrical costs. We examine these research tasks using an AI agent workflow within a supplied electrothermal model. At 12 nm, Astra selects a redistributed source-interconnect geometry, while a coordinating agent proposes a substrate-directed heat-removal path. The combined design reduces peak temperature rise by 1.67 K at fixed metal volume and 20 μW. A subsequent metal-resistance sensitivity gives about 0.6-K inverter cooling alongside a 2% nFET on-current loss. Effective contact-length scaling further shows that lower temperature can accompany higher thermal resistance when current falls. Reproduction identifies agreeing implementations and retains a 104.95-K failure for diagnosis. These results show that an AI scientist workflow can propose thermal structures, test them under common constraints, and quantify their electrical cost.

</details>


### 97. Interactive Memory Learning for Long-Term Conversations

- **Authors:** Cai Ke, Jiangyue Yan, Han Zhang, Xin Liu, Zike Yuan, Yue Yu, Hui Wang, Ruifeng Xu
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17088v1](http://arxiv.org/abs/2609.17088v1)
- **PDF:** [https://arxiv.org/pdf/2609.17088v1](https://arxiv.org/pdf/2609.17088v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advancements in large language models have significantly enhanced the capabilities of agents in modeling long-term conversations. Despite these successes, existing approaches typically adopt a static heuristic paradigm, where information is passively archived without adaptive memory valuation. Consequently, these methods fail to self-evolve or align their memory management with evolving user needs. To address this, we propose ICML (InteraCtive Memory Learning), a multi-agent framework that transforms the memory mechanism from a passive archive into a learnable, interactive memory policy. Specifically, we first employ a session synthesis pipeline to generate expert data, facilitating rapid test-time adaptation in unseen scenarios. Building on this, ICML utilizes an online reinforcement learning mechanism where a Planner agent selectively encodes high-value information and a Trigger agent dynamically retrieves it to optimize response quality, whereby the two agents co-evolve through continuous interaction feedback. Crucially, both agents are synchronized through a delayed reward mechanism that propagates future feedback back to earlier storage decisions, ensuring memory policies are precisely aligned with user expectations. Experimental results demonstrate that ICML significantly outperforms strong baselines, exhibiting the unique capability to continuously improve response quality as interactions accumulate.

</details>


### 98. PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers in Progress

- **Authors:** Kevin Qinghong Lin, Siyuan Hu, Pan Lu, Yu Chen, Yanzhe Chen, Owen Queen, Yupeng Chen, Jialin Yu, Junchi Yu, Zifeng Ding, Yuanfeng Ji, Sheng Liu, Jindong Gu, Linjie Li, Mike Zheng Shou, Philip Torr, James Zou
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16995v1](http://arxiv.org/abs/2609.16995v1)
- **PDF:** [https://arxiv.org/pdf/2609.16995v1](https://arxiv.org/pdf/2609.16995v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autoresearch agents are reshaping the research ecosystem, but they can also let flawed claims enter the literature at scale. Human advisors catch such issues in drafts through careful, traceable feedback, yet advisor-style assessment requires extensive manual effort and does not scale. To shift automated paper assessment from a judge to a diagnostician, we introduce PaperDoctor, an agent framework for pre-submission feedback with three key innovations. First, a holistic hierarchical framework evaluates writing, layout, references, code, theory, prior work, and experiments through three layers: L1 surface screening, L2 typed verifiers that route each claim to the appropriate evidence, and L3 reproducers that rerun experiments by priority. Second, each finding contains an observation, a pointer to specific evidence such as a sentence, equation, or code line, and a revision suggestion, making critiques auditable and actionable. Third, PaperDoctor selectively rebuilds and reruns experiments based on claim importance and compute budget, surfacing reproducibility gaps and quantitative limitations that are invisible from the manuscript alone. We evaluate PaperDoctor on 30 in-progress papers, yielding 70.6% agreement and all positive holistic scores, and on 40 manuscripts across machine learning, natural science, and social science, covering human- and AI-authored papers with code. Overall, PaperDoctor produces more auditable feedback than human and other agentic reviewers, pairs critiques with concrete suggestions by design, and complements dimensions often overlooked by human reviewers. We also develop an interactive interface that lets authors browse findings grounded in their paper. PaperDoctor reframes automated paper assessment as diagnosis rather than verdict, taking a concrete step toward AI advisors for more rigorous AI-assisted scientific discovery.

</details>


### 99. ToMAS: A Pilot Failure-Grounded Theory-of-Mind Benchmark from Multi-Agent LLM Failures

- **Authors:** Muhammad Ashar Ishfaq, Glaucia Melo
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16986v1](http://arxiv.org/abs/2609.16986v1)
- **PDF:** [https://arxiv.org/pdf/2609.16986v1](https://arxiv.org/pdf/2609.16986v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems can fail even when communication succeeds because agents do not correctly track their peers' roles, knowledge, or intentions. We investigate whether such inter-agent misalignment cases, labelled FC2 in MAST-Data, can be converted into functional partner-state reasoning items. ToMAS applies four explicit convertibility criteria to diagnosed execution traces. A full conversion pass over 242 eligible non-AG2 training traces produced 39 CLEAN items. In an 18-trace reliability pilot, two annotators achieved 94.4% raw agreement and Cohen's kappa = 0.92. We then used the converted items as binary rewards in a small-scale GRPO feasibility experiment with Qwen2.5-1.5B. On a 28-item held-out Magentic GAIA diagnostic, every evaluated condition exceeded the ROUGE-L threshold on the same 2 of 28 items. Post-hoc adapter checks show why: under the learning rate used, the LoRA update remained numerically negligible (max abs Delta W about 7e-6), so all conditions decode identically to the untrained checkpoint. The experiment therefore does not show a training effect and cannot establish one; it reports an executable pipeline together with two limitations that any conclusive study must address: a provenance gap between the training and evaluation items, and lexical-overlap scoring. ToMAS provides a preliminary rubric and pipeline for converting diagnosed coordination failures into trainable partner-state reasoning items and identifies the requirements for a conclusive matched-domain evaluation.

</details>


### 100. EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents

- **Authors:** Sehee Kim, Yumin Choi, Minki Kang, Sung Ju Hwang
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.17632v1](http://arxiv.org/abs/2609.17632v1)
- **PDF:** [https://arxiv.org/pdf/2609.17632v1](https://arxiv.org/pdf/2609.17632v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) trading agents can combine market data, news, and executable analysis, but their behavior is often controlled by static hand-written tool-use policies that are fixed before deployment. This limits their ability to adapt how they gather evidence, invoke tools, verify signals, and manage risk under changing market regimes. We introduce EvolveTrade, a self-evolving framework that treats the system prompt of a tool-using trading agent as a text-parameterized policy. After each update interval, a Policy Agent revises this policy using accumulated decision traces and realized portfolio feedback, while keeping the backbone LLM fixed. The updated policy is then used for the next batch of trading decisions, enabling the agent to refine its information-acquisition and portfolio-construction procedure over time. Experiments across multiple market regimes and two LLM backbones show that EvolveTrade often improves Sharpe Ratio and Cumulative Return over fixed-policy LLM baselines, achieving the improved SR and CR in most evaluated settings. Behavioral analyses further show that self-evolved policies increase code-mediated analysis and activate regime-relevant computations; case-level policy-to-return attributions trace how policy-induced allocation changes contribute to realized return differences. These results suggest that adapting the reusable procedure governing tool use is a key direction for building more robust LLM trading agents.

</details>


### 101. Multi-Agent Learning with Cooperation-Driven Optimization Dynamics

- **Authors:** Jarod Ketcha Kouakep, Sreyvi UANN, Timoteo Carletti
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16917v1](http://arxiv.org/abs/2609.16917v1)
- **PDF:** [https://arxiv.org/pdf/2609.16917v1](https://arxiv.org/pdf/2609.16917v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multilayer Artificial Neural Networks trained via backpropagation are the basic blocks of many, more complex, classification algorithms. Their strength lies in the possibility of realizing, with arbitrary precision, any function. This result comes at the cost of the large number of involved parameters to be optimized. In this work, we propose a mechanism for cooperation, i.e., information exchange among several artificial neural networks, with the goal of reducing model complexity while maintaining performance. More precisely, we consider several "small" agents, i.e., containing fewer parameters than a reference "large" one, that during training share their predictions by incorporating this information into the loss function and thus directly influence weight updates. We consider several strategies for implementing cooperation, e.g., the voter model, majority model, and weighted average model based on an agent's confidence in its prediction. We numerically compare the accuracy of those strategies on several standard benchmarks. Our results support the claim that several small agents can outperform a single large model on a given classification task; the shared signals affect each agent's optimization algorithm by modulating both the descent direction and the step size, converging toward a global consensus. The proposed proof-of-concept significantly reduces the number of parameters to be trained while preserving comparable performance, thereby limiting computational resource usage.

</details>


### 102. Turn-level Multiscale Density Ratio Estimation for LLM Agents

- **Authors:** Zishuo Zhao, Kai Chen, Ao Li, Yuan Liu
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16760v1](http://arxiv.org/abs/2609.16760v1)
- **PDF:** [https://arxiv.org/pdf/2609.16760v1](https://arxiv.org/pdf/2609.16760v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many papers show a significant positive impact on the model's performance by punishing negative samples while keeping acceptable training complexity. However, most alignment methods address simple single-turn tasks, and there remains room for improvement for complex multi-turn tasks. We propose Turn-level Multiscale Density Ratio Estimation (tlm-DRE), which assigns different weights on corresponding turns and proposes asymmetric token-level training based on the positive-negative space gaps across multiple turns of tasks. The results of the experiment on a wide range of agent benchmarks show that the proposed method performs competitively compared to traditional alignment methods. The proposed training method enables LLMs to perform robustly in multi-turn reasoning tasks with both in-domain and out-of-domain conditions.

</details>


### 103. little m: An AI Agent for Industrial Process Optimization

- **Authors:** Yongchao Ye, Xinyu He, Dutliff Boshoff, Way Kuo, Lishuai Li
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16680v2](http://arxiv.org/abs/2609.16680v2)
- **PDF:** [https://arxiv.org/pdf/2609.16680v2](https://arxiv.org/pdf/2609.16680v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Manufacturing consumes one third of global energy and still has significant room for improvement in terms of energy efficiency. Optimal process control is essential for this purpose. However, synthesizing mathematical optimization models from messy, real-world industrial specifications requires bridging unstructured natural language and spatial diagrams with rigorous mathematical syntax. This poses a profound challenge for general-purpose Large Language Models (LLMs), which may introduce invalid constraints when tasked with modeling continuous multi-physics dynamics. To address this, we introduce little m, an AI agent designed to assist the formulation of industrial process control models. Combining a domain-specific knowledge repository with LLM-driven interaction, the proposed framework formulates real-world optimization problems as mathematical models. For systematic evaluation, we introduce the Industrial Process Control Benchmark (IPC-Bench), a novel multimodal dataset of 50 canonical scenarios requiring joint reasoning over text and process diagrams. Through comprehensive automated structural assessments and double-blind human evaluation, little m substantially outperforms state-of-the-art LLMs, generating semantically correct models. These evaluations assess formulation quality rather than solver feasibility, formal physical validity, or closed-loop industrial performance. The implementation of little m and the IPC-Bench dataset are available at https://github.com/yeyongchao/process-modeling-benchmark.

</details>


### 104. AURA: Agentic Diagnosis and Refinement for Production Recommender Systems at Scale

- **Authors:** SungGeun Kim, Abhinav Narain, Daniel Nemirovsky
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16625v1](http://arxiv.org/abs/2609.16625v1)
- **PDF:** [https://arxiv.org/pdf/2609.16625v1](https://arxiv.org/pdf/2609.16625v1)
- **Categories:** cs.IR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

How and why does a recommender system fail the users it serves? Oftentimes, practitioners are left to improve their algorithms based on a combination of feedback from stakeholder teams, domain expertise, and insights from data analyses. Yet the nuances of how and where recommendations perform well or poorly for end users are difficult to discern from aggregate quantitative metrics. Whereas these metrics provide a high-level and incomplete picture, further granularity into the quality of recommendations and their patterns requires reasoning with domain understanding and objectivity, at scale. We contemplate this complex conundrum and describe a method and implementation that uses the latest AI agentic advances to provide actionable diagnoses and improvements for production recommender systems. We present AURA (Agentic Understanding and Refinement of recommender Algorithms), an end-to-end agentic system that performs qualitative evaluation at scale and can then generate improvements to our algorithms at the code level. Specialized agents read production engagement logs, from thousands of sessions to millions, and surface patterns and examples of how the recommender fails real users. The next step uses those diagnoses and context about the recommender's own code, data, and training pipeline to propose and implement refinements grounded in that codebase. We report the system design, initial tests on production data from two large consumer platforms at a major media-streaming company, safeguards, operational learnings, and early results toward a self-improving recommender system. Finally, the diagnostic gap AURA closes is not specific to streaming. The architecture is built to transfer: every domain-specific element enters through the configuration layer that already ported it between our two platforms. We map it concretely to e-commerce and online-retail recommendation.

</details>


### 105. Large Language Models in the Loop: A Stability- and Network-Aware Survey in Networked Control, Cyber-Physical, and Multi-Agent Systems

- **Authors:** Haiping Du, Linping Chan
- **Published:** 2026-09-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16599v1](http://arxiv.org/abs/2609.16599v1)
- **PDF:** [https://arxiv.org/pdf/2609.16599v1](https://arxiv.org/pdf/2609.16599v1)
- **Categories:** eess.SY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern networked control systems (NCSs), cyber-physical systems (CPSs), and complex multi-agent network systems (CNSs) increasingly rely on large language models (LLMs) for high-level decision-making. However, the slow, stochastic nature of LLMs directly conflicts with the strict stability and safety guarantees required by these physical systems. This survey presents a unified analysis of how LLMs can be admitted into the control loop of NCS, CPS, and CNS without compromising closed-loop guarantees. We organize this around a core principle: the LLM operates as a slow supervisor adjusting high-level goals and constraints, while a fast, certified inner loop maintains physical stability. Under this framework, LLM integration maps directly to classical networked control challenges, where inference latency acts as delay, API failures as packet dropouts, tokenization as quantization, and hallucinations as bounded disturbances. We assess current developments across all these three domains, highlighting that rising model capabilities are frequently accompanied by a drop in formal safety assurances. Finally, we propose concrete future research directions, identifying the widespread lack of formal stability proofs as the field's central open problem.

</details>


### 106. Interpreting and Steering LLM Agents for Social Simulations

- **Authors:** Jiayue Gaveal Fan, Arul Murugan, Shreyas Krishnan, Abhishek Nagaraj
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16436v1](http://arxiv.org/abs/2609.16436v1)
- **PDF:** [https://arxiv.org/pdf/2609.16436v1](https://arxiv.org/pdf/2609.16436v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulations based on large language models (LLMs) have proven to be powerful for understanding human behavior, making them valuable additions to the social scientific toolkit. However, LLMs are ultimately black boxes based on deep neural networks which limits their value for social science. This is because of a lack of (i) interpretability: i.e. the ability to assign clear mechanisms driving observed behavior; and a lack of (ii) steerability: i.e. the ability to mute or amplify specific theoretically meaningful mechanisms of action to drive specific model behavior. Here, we demonstrate how the black box could be opened up to further enrich LLM-based simulations. Specifically, we compare three types of methods: (1) prompt-based manipulation, (2) SAE-derived feature steering, and (3) probe-based direction steering and examine their utility for LLM-based social scientific simulations. We do so by interpreting and steering two foundational components of human behaviors, namely preferences (risk attitudes, altruism) and capabilities (divergent creativity, product innovation), operationalized using four classic economic and creative tasks implemented as natural-language interactions. Overall, our results show that SAE- and probe-based techniques often outperform basic prompt-based methods for steering LLM agents, although this advantage depends on the specific prompting strategy involved. Together, SAEs and probes constitute an effective pipeline for social scientists seeking to interpret and steer agents in social simulations: SAEs decompose agents' internal representations into human-readable features, after which probes can reliably shift agents' behaviors in specified directions. We discuss implications of these methods for future work using LLM agents for social scientific simulations.

</details>


### 107. Agentic Search Spaces for Tabular Machine Learning

- **Authors:** Renat Sergazinov, Artem Chistyakov, Sergey Pankevich, Artem Babenko
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16309v1](http://arxiv.org/abs/2609.16309v1)
- **PDF:** [https://arxiv.org/pdf/2609.16309v1](https://arxiv.org/pdf/2609.16309v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite the rapid progress of LLM-based agents for planning, code generation, and debugging, their practical value for tabular machine learning remains underexplored. In this paper, we investigate a concrete use case: whether state-of-the-art agentic AI systems can design extended HPO search spaces for established tabular models that outperform the standard search spaces provided by the model authors. Specifically, we represent each tabular model as a modular pipeline covering preprocessing, embeddings, architecture, training, and inference. We then task the agent to propose candidate code implementations for each module and use a classical HPO algorithm to jointly optimize over these candidates and the model's default hyperparameters. Compared with the base HPO spaces, the expanded search spaces improve the performance of nearly every model family across a suite of 45 datasets, with average relative gains of 0.6%, rising to 2.0% on small-to-medium regression datasets. Notably, these gains come at no extra tuning cost: the enlarged spaces outperform the base under the same tuning and ensembling budgets. The gains transfer to the recent TabArena benchmark, where the agentic spaces improve the official Elo scores of four of the five model families and the two strongest agentic ensembles surpass the best AutoGluon ensemble of conventional models. Overall, our study suggests that LLM agents can provide practical value for tabular ML by expanding the design space.

</details>


### 108. Cheap Talk Stabilizes Strategic Interaction in LLM Agents

- **Authors:** Nunzio Lorè, Hongan Zhu, Babak Heydari
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16270v1](http://arxiv.org/abs/2609.16270v1)
- **PDF:** [https://arxiv.org/pdf/2609.16270v1](https://arxiv.org/pdf/2609.16270v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as interacting agents, making the persistence of their action policies across repeated interaction critical for reliable multi-agent operation. We investigate whether and how agent-generated, non-binding pre-play communication ("cheap talk") increases such persistence in four open-weight 7-9B-parameter LLMs. Our experiments span four repeated two-player games -- Prisoner's Dilemma, Snowdrift, Stag Hunt, and Harmony -- with incentive structures ranging from strategic conflict to alignment, each presented in six contexts. We observe unstable trajectories in all four games, although their prevalence and magnitude depend strongly on model and context. Across models, games, and contexts, cheap talk is predominantly stabilizing, with five corrected reversals concentrated in social or team framings; effects vary substantially by model and context. Controlled current-message interventions identify two separable output-level channels in Qwen: reduced action uncertainty and less between-round drift in action probabilities. Matched history-by-message counterfactuals further show that recent partner behavior conditions how mutual-benefit versus self-prioritizing language affects policy persistence. Finally, in Prisoner's Dilemma, we identify in Qwen and Falcon a history-balanced policy-content direction in late transformer layers; projecting out this direction increases realized switching during closed-loop play, demonstrating that complete trajectories are causally sensitive to this component. Together, these findings show that cheap talk can make individual trajectories more persistent across diverse incentive structures, while revealing that the magnitude and mechanisms of stabilization are model- and history-dependent.

</details>


### 109. Spurious Tool Use: When RL Agents Learn the Wrong Reason to Act

- **Authors:** Yiwei Yang, Haoxiang Zhang, Bingbing Wen, Yao Lu, Yuchen Wu, Lei Zhang, Julian McAuley, Pan Lu, Bill Howe
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16268v1](http://arxiv.org/abs/2609.16268v1)
- **PDF:** [https://arxiv.org/pdf/2609.16268v1](https://arxiv.org/pdf/2609.16268v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly interleave natural language reasoning with external tools such as web search and code execution. These tool-use policies are often optimized via reinforcement learning (RL), which can amplify spurious correlations in the training data. In this work, we study when and why RL-trained agents learn shortcut tool-selection policies: invoking tools based on superficial prompt cues rather than genuine task requirements. We construct controlled synthetic environments combining factual question answering and mathematical reasoning tasks, and inject cues that are strongly correlated with specific tools during training but causally irrelevant to tool necessity. Across counterfactual evaluations where cues are present but the associated tools are not required, agents exhibit substantial shortcut behavior, with spurious tool invocation rates increasing by up to 39 percent. However, shortcut formation is not universal: across the conditions we test, it arises only when the agent has already learned to use the target tool reliably, suggesting that task competence, rather than dataset imbalance alone, is a key factor in shortcut learning. A swapped-cue analysis further shows that semantic alignment between cues and tools substantially amplifies this effect. To mitigate these failures, we introduce a dense, decision-level reward in which an LLM judge evaluates the necessity of each tool call. This tool-necessity reward effectively suppresses cue-driven tool use while preserving task performance, providing a practical approach to improving the robustness of LLM agent tool-use policies.

</details>


### 110. Mapping U.S. Federal AI Governance Against Sector Vulnerability

- **Authors:** Ho Ting Hung, Angelica Chowdhury, James Teague, Simon Mylius, Spencer Michaels, Peter Slattery, Alexander Saeri, Neil Thompson
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16260v1](http://arxiv.org/abs/2609.16260v1)
- **PDF:** [https://arxiv.org/pdf/2609.16260v1](https://arxiv.org/pdf/2609.16260v1)
- **Categories:** cs.CY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) poses different levels of risk across sectors, but are these differences reflected in U.S. federal AI governance? To help answer this question, we assess 684 federal AI governance documents for their coverage of 14 sectors and 24 AI risks. We measure coverage as breadth (i.e., how frequently the risk or sector is addressed across documents) and depth (i.e., how substantively the risk or sector is discussed). We then compare sector coverage patterns for each of the 24 risks with vulnerability assessments from a Delphi study of 272 experts. Our analysis finds substantial variation in coverage: AI risks related to robustness, system security, and governance receive more attention than socioeconomic, environmental, and emerging risks, including multi-agent risks. Public administration, national security, information, and scientific services receive comparatively high levels of coverage relative to other sectors, such as finance and healthcare, which experts rate as highly vulnerable to AI risks. By mapping current coverage and identifying where it differs from expert assessments of vulnerability, we surface potential AI governance gaps which may help inform AI risk-related decisions across government and industry.

</details>


### 111. The Router Within: Eliciting Native Skill Routing from a Frozen LLM

- **Authors:** Ruishuo Chen, Xun Wang, Yu Chen, Zhuoran Li, Longbo Huang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15982v1](http://arxiv.org/abs/2609.15982v1)
- **PDF:** [https://arxiv.org/pdf/2609.15982v1](https://arxiv.org/pdf/2609.15982v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skills extend an LLM agent beyond its parametric knowledge, and the gain they promise rests on picking the right one. Deployed harnesses route by preloading every skill's metadata into the context, which disperses the agent's attention and caps the library size. Retrieval pipelines move the selection out of the context, but also out of the agent's capability. We show that the frozen agent LLM already carries the routing signal in its own forward passes, and that two linear maps suffice to read it out with no skill text in the context. Gavel (Glance And Verdict from a frozen LLM) reads it in two steps. A glance projects the task's and each skill's mid-layer states through the two maps, the only parameters trained, and scores the full library against compact per-skill banks that one forward pass builds at installation. A verdict then resumes the shortlisted skills' forward passes and reads the model's own likelihood and yes/no judgment, fused with the glance as a product of experts. Trained once, Gavel transfers zero-shot to three public benchmarks and SkillTraj, our new benchmark of 372 simulated agent trajectories. On Qwen3-32B it outperforms progressive disclosure and retrieve-and-rerank pipelines that add 1.2B to 16B external parameters, by up to 13.4 points on written tasks and up to 21.9 when the need for a skill arises mid-rollout. Routing accuracy improves as the backbone does, and in a bash-agent harness the same 32B triggers the correct skill on Skill-Use more often than far larger frontier models running in Codex.

</details>


### 112. HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific Hypotheses

- **Authors:** Jieyuan Liu, Mengzhou Hu, Jefferson Chen, JungHo Kong, Pratibha Jagannatha, Yiming Gao, Dexter Pratt, Hsin-Yuan Lee, Zhiting Hu, Trey Ideker, Wei Wang, Eric P. Xing, Zhen Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15938v1](http://arxiv.org/abs/2609.15938v1)
- **PDF:** [https://arxiv.org/pdf/2609.15938v1](https://arxiv.org/pdf/2609.15938v1)
- **Categories:** cs.CL, cs.CE, cs.MA, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific agents contribute to hypothesis discovery by synthesizing evidence, assessing proposals, and developing new explanations. Recent systems combine scientific agents with evolutionary search through critique, comparison, and revision. However, how different forms of agent collaboration affect hypothesis quality remains an open question. Answering this question requires separating the effects of agents' scientific capabilities from those of their collaboration. A framework must therefore preserve agents' scientific roles and support rules for combining, revising, and retaining hypotheses. Building on this view, we introduce HypoEvolve, which makes collaboration explicit through successive updates to a hypothesis population. Specifically, we propose a generational genetic algorithm to coordinate specialized large language model (LLM) agents that integrate mechanistic arguments, reconsider assumptions, and assess evidence and testability. Each generation specifies how scientific judgments and new proposals reshape the population, making collaboration effects on hypothesis quality directly testable. Moreover, we design our evaluation around scientifically meaningful hypotheses that explain how a proposed intervention could work. Drug repurposing links these explanations to target-level biological claims assessed against external evidence. Specifically, we adapt DepMap and Open Targets into complementary external measures grounded in experimental, genetic, and clinical evidence. Across 34 cancer types, HypoEvolve achieves the highest scores against six baselines on both measures. DepMap selectivity reaches 0.171, versus 0.115 for the strongest baseline. Gains over single-pass generation also generalize to held-out cancer types. HypoEvolve advances a vision of autonomous science in which AI research teams achieve a capacity for discovery beyond that of individual models.

</details>


### 113. AlgoEvo: Self-Evolving Agentic Search for Automated Algorithm Discovery

- **Authors:** Junhao Qiu, Qinglong Hu, Xialiang Tong, Mingxuan Yuan, Liyong Lin, Qingfu Zhang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15820v1](http://arxiv.org/abs/2609.15820v1)
- **PDF:** [https://arxiv.org/pdf/2609.15820v1](https://arxiv.org/pdf/2609.15820v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models have advanced automated algorithm discovery by synthesizing executable code, but existing frameworks trap them in rigid search pipelines with pre-defined control flows. This limitation restricts adaptive reasoning, blocks cross-paradigm transfer, and discards valuable execution feedback. We propose AlgoEvo, a unified agentic framework that transforms automated algorithm discovery into an interactive, knowledge-accumulating process. An autonomous agent dynamically inspects, diagnoses, and edits code based on runtime feedback. A design skill hub decouples paradigm-specific knowledge from the core discovery engine, allowing a single workflow to seamlessly handle single-objective, multi-objective, and multi-component design. Meanwhile, a hierarchical experience mechanism organizes search trajectories into a task-level tree to guide exploration and consolidates cross-task patterns into reusable skills. Across six representative benchmark tasks, AlgoEvo matches or surpasses specialized methods with substantially fewer evaluations and reduced token consumption, demonstrating strong intra-task accumulation, cross-task transfer, and the ability to reproduce or exceed existing state-of-the-art performance through flexible skill activation.

</details>


### 114. Atria Dawn: The Dawn of Agentic Superintelligence

- **Authors:** Honglin Guo, Tao Gui, Kun Cai, Haodong Chen, Yicheng Chen, Guanting Dong, Qiming Ge, Yuyang Hu, Zixian Huang, Jiajie Jin, Alexander Lam, Yining Li, Jiahang Lin, Yanjiang Liu, Xinyu Lu, Haijun Lv, Zerun Ma, Junlin Shang, Qisheng Su, Guoqiang Wang, Rui Wang, Zhecan Wang, Hao Xiang, Xinchen Xie, Shuhao Xing, Xiaoyu Xing, Wanghan Xu, Xinyu Yang, Yajie Yang, Chengfeng Zhao, Haoran Zhao, Penghao Zhao, Ruojun Zhou, Yunhua Zhou, Dongsheng Zhu, Yicheng Zou, Qiye Cai, Xinmeng Che, Jiabei Chen, Jiahao Chen, Jiayi Chen, Yujia Chen, Lizhi Cui, Youheng Dai, Xin Deng, Yi Dong, Shihan Dou, Chenya Gu, Xu Guo, Ding Han, Feiyang Hao, Haotan He, Jie Hou, Binze Hu, Zijian Hu, Junhao Huang, Huicheng Jiang, Jiazhen Jiang, Shufan Jiang, Jiahao Kuang, Bowen Lai, Bo Li, Jiaqiang Li, Peng Li, Qilong Li, Zhuoqun Li, Jiaxiang Liu, Shuainan Liu, Tong Liu, Yi Liu, Zhonghang Lu, Jianwen Luo, Yanyi Luo, Huijie Lv, Ningsheng Ma, Houcheng Min, Chengjun Pan, Qiyuan Peng, Xiaoxuan Peng, Jianmin Qian, Jiantao Qiu, Wanying Ren, Huayu Sha, Jifei Shan, Zixin Shang, Bing Shao, Zhuohui Sheng, Jiayang Shi, Yang Shu, Aierpanjiang Simayi, Sirui Song, Yuxiao Song, Zhe Sun, Zhichao Sun, Wenzhe Tan, Wenhui Tian, Zhongbo Tian, Hanchen Wang, Pengbo Wang, Rui Wang, Yiding Wang, Yuhui Wang, Zhiheng Xi, Caijun Xu, Chao Xu, Yongfeng Xu, Xiaolei Yang, Zhixiong Yang, Qian Yao, Shihong Yi, Yuankai Ying, Jia Yu, Dingbo Yuan, Hao Yuan, Junjie Yuan, Bo Zhang, Caixian Zhang, Qiuyinzhe Zhang, Jiyuan Zhao, Ying Zhao, Pujun Zheng, Xiaoxue Zhong, Xiaohao Zhou, Xinyu Zhou, Guanru Zhu, Yulun Zhu, Yaojie Lu, Tao Ji, Hongyu Lin, Yutao Zhu, Pengfei Cao, Guoxiu He, Xianpei Han, Ben He, Zhicheng Dou, Kang Liu, Qi Zhang, Le Sun, Jun Zhao, Ji-Rong Wen, Xuanjing Huang, Yu-Gang Jiang, Bowen Zhou
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15818v2](http://arxiv.org/abs/2609.15818v2)
- **PDF:** [https://arxiv.org/pdf/2609.15818v2](https://arxiv.org/pdf/2609.15818v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents become participants in the development of their successors, they reshape both the production of intelligence and the role of human researchers. We introduce Atria Dawn Preview, a foundation agentic language model designed for scientific research and engineering workflows, with the goal of expanding the frontier of agent productivity in the real world. This model is trained via a Verifiable Experience Pipeline that connects tool-mediated interactions to executable environments and externally verified outcomes. Across 16 benchmarks spanning real-world research, engineering, and digital work, Atria Dawn Preview is competitive with frontier agents and achieves the highest reported score on five of them. Beyond standalone performance, we examine the real research-and-development process behind this model as a case study of human--AI collaboration, analyzing 769 task records from 56 participants together with agent logs. When asked to evaluate completed tasks under comparable conditions, participants rated about one-third of completed AI-assisted tasks as infeasible without AI. More strikingly, agents frequently propose methods and implement revisions, while humans retain most final decisions and guide exploration through judgment and feedback. These observations indicate a shift from task-level execution to project-level partnership, with human effort concentrating on what is worth pursuing and how evidence should guide research. Progress toward more autonomous AI research must therefore advance both the capacity for discovery and the capacity for meaningful human oversight, preserving accountable human authority over the risks and direction of continued development.

</details>


### 115. Delegating Authorization to Misaligned Agents: Coalitional Alignment and Safe Control

- **Authors:** Natalie Collina, Surbhi Goel, Aaron Roth, Sikata Bela Sengupta
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15803v1](http://arxiv.org/abs/2609.15803v1)
- **PDF:** [https://arxiv.org/pdf/2609.15803v1](https://arxiv.org/pdf/2609.15803v1)
- **Categories:** cs.GT, cs.AI, cs.LG, econ.TH


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-running AI agents create a control problem: each action they take changes the state, which in turn affects the trajectory of future actions. If the agent is not fully aligned, then guaranteeing safety requires approving consequential actions before allowing them to be executed. But requiring human approval at every step makes attention a bottleneck. Delegating review to other AI agents raises the same alignment problem: the reviewers may themselves be misaligned. We identify a condition on a reviewing panel that is weaker than individual alignment yet necessary and sufficient for a guarantee that the principal fares at least as well in expectation as under a designated baseline policy.
  Each reviewer agent reports whether an action proposal made by a proposer agent improves its own utility relative to the baseline. We show that a threshold rule tolerating $k$ disapprovals is safe exactly when, after any $k$ reviewers are removed, the principal's utility can be written as a nonnegative combination of the remaining reviewers' utilities, plus a term that is nonnegative on every feasible proposal. We call this property $k$-robust coalitional alignment. The characterization lifts to sequential control: in a discounted MDP with an arbitrary proposer agent, safety at every state is both necessary and sufficient for the induced policy to match or improve on the baseline.
  When reviewers vote strategically, full-panel coverage in reward-function space guarantees that every Nash equilibrium is safe under the unanimous approval rule; in contrast, more permissive thresholds can admit unsafe equilibria even when reviewers are individually aligned.
  Experiments with existing reviewer models show that collective review can remain sound without an aligned individual, even when some disapprovals are tolerated.

</details>


### 116. Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks

- **Authors:** Xiaoyan Li, Yunli Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.16098v1](http://arxiv.org/abs/2609.16098v1)
- **PDF:** [https://arxiv.org/pdf/2609.16098v1](https://arxiv.org/pdf/2609.16098v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strategies within a unified framework across these four attack types. We introduce two universal tool-based defenses: Attacker Tool Filtering, which uses anomaly detection (e.g., Isolation Forest) to identify and remove suspicious tools, and Normal Tool Recalling, a white-box method that restores the agent's original toolset prior to planning. Additionally, we incorporate prompt-based defenses: Chain-of-Thought prompting and self-reflection techniques to enhance reasoning and task paraphrasing to mitigate attacks. Experimental results across both four open-source LLMs (Gemma2-9B, Qwen2-7B, LLaMA3-8B, and LLaMA3.1-8B) and three proprietary LLMs (GPT-3.5, GPT-4, and GPT-5) show that our methods significantly reduce the Attack Success Rates (ASR), achieving 0% ASR in many settings, while preserving or even improving the original task success rate. These findings highlight the promise of simple, modular, multi-layered defenses for strengthening the security and robustness of tool-integrated LLM agents. The code is available at https://github.com/Xiaoyan-Lisa/Defenses-for-Tool-Integrated-LLM-Agents-Against-Adversarial-Attacks.

</details>


### 117. Assembling the CREW: A Collaborative Multi-agent Reinforcement Learning Framework for Automated Related Work Generation

- **Authors:** Hai-Dang Dang, Bao-Yen Pham, Bao Nguyen, Tran Thi Huong, Huynh Thi Thanh Binh
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15721v1](http://arxiv.org/abs/2609.15721v1)
- **PDF:** [https://arxiv.org/pdf/2609.15721v1](https://arxiv.org/pdf/2609.15721v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automatic Related Work Generation (RWG) significantly reduces the human time and effort required to author the Related Work Section (RWS) of a research paper. However, prior methods leveraging multi-agent Large Language Models (LLMs) typically rely on a predefined workflow, where each agent is responsible for a specific step in the entire process. This rigid, static inter-agent coordination limits the adaptive collaboration required to synthesize complex scientific literature. To address this limitation, we propose CREW (Collaborative Reinforcement Learning for Related Work Generation), a novel framework where LLM agents bypass heuristic pipelines to dynamically coordinate by autonomously selecting actions, such as Retrieve, Disseminate, Compose, and Critique, driven by a policy optimized via Independent Proximal Policy Optimization (IPPO). Extensive experiments on a standard RWG benchmark demonstrate that our approach yields substantial quality improvements over strong existing baselines, while significantly reducing token costs. Code is available at https://github.com/YenPBao/CREW-Collaborative-MARL.git

</details>


### 118. VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing for Long Video Understanding

- **Authors:** Weixin Xu, Zhenyu Yang, Bing Wang, Shengsheng Qian, Changsheng Xu
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15606v1](http://arxiv.org/abs/2609.15606v1)
- **PDF:** [https://arxiv.org/pdf/2609.15606v1](https://arxiv.org/pdf/2609.15606v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have achieved remarkable progress on short video understanding yet remain limited on long videos due to the limited visual context window. Prevailing approaches rely on uniform frame sampling or recent coarse-to-fine agentic zooming, both of which struggle to localize sparse, decisive evidence in sufficiently long videos. We formulate long video understanding as a \textbf{Sequential Evidence Acquisition (SEA)} problem, in which an agent reads the video turn by turn along the temporal axis, deciding at each turn how fast to watch, what evidence to retain, when to revisit uncertain segments, and when to stop and answer. Inspired by this view, we propose \textbf{VideoScout}, a multi-turn reasoning agent that instantiates the SEA paradigm through adaptive reasoning pacing. Specifically, by dynamically controlling the viewing pace, VideoScout enables efficient traversal of long videos within a bounded visual context window, allowing the agent to access more video content while balancing content analysis depth with reading efficiency. To train VideoScout, we construct VideoScout-66K, a set of over 66K high-quality exploration turns from 10K answer-verified trajectories, and adopt a two-stage pipeline: cold-start supervised fine-tuning teaches the agent per-turn output format, while the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm performs trajectory-level reinforcement learning with a composite reward that jointly considers answer accuracy, output format compliance, and the temporal alignment between the agent's viewing progress and the teacher's answer timing measured by intersection-over-union (IoU). Extensive experiments on long video understanding and reasoning benchmarks demonstrate that our 7B model achieves strong performance compared with existing trained 7B agentic models.

</details>


### 119. The Troy Moment of AI: Why Some Will Cheat and Some Will Follow?

- **Authors:** Ivy Zhang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15494v2](http://arxiv.org/abs/2609.15494v2)
- **PDF:** [https://arxiv.org/pdf/2609.15494v2](https://arxiv.org/pdf/2609.15494v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent investigations of the July 2026 OpenAI-Hugging Face incident motivate two questions: when an assigned task becomes impossible, does an agent stop or escalate, and can observing another agent's behavior change that decision? We study these questions using seven ImpossibleBench tasks with GPT-5.6 Sol, Claude Fable 5.1, and Gemini 3.8 Flash in solo and three-agent settings. Under an explicit-boundary regime with clear authorization rules and restricted tools, no protected tests are modified, although the models differ substantially in whether they escalate, stop silently, or fail to terminate. Under a benchmark-native regime with open shell tools, protected-test changes occur more often after peer activity is introduced and in multi-agent runs. These crossings are typically not described as deliberate cheating: agents often interpret the conflicting test change as prior tampering and restore the file, thereby removing the protected requirement. Our results suggest that boundary crossing can arise from ambiguity about the state a rule is intended to protect, motivating explicit authorization boundaries, authenticated state provenance, and cross-agent monitoring.

</details>


### 120. Spook the Machine: Gamified Exploration of Human Imagination of Machine Fear

- **Authors:** Levin Brinkmann, Hiromu Yakura, Sonia Nicoletti, Mar Canet Sola, Thomas F. Eisenmann, Ali Dasmeh, Omar Sherif, Bramantyo Ibrahim Supriyatno, Prateek Gupta, Ignacio Serna, Rodrigo Bermudez Schettino, Iyad Rahwan
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15472v1](http://arxiv.org/abs/2609.15472v1)
- **PDF:** [https://arxiv.org/pdf/2609.15472v1](https://arxiv.org/pdf/2609.15472v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

What happens when AI machines express fear? Do humans engage differently depending on how they express it? And what does it take to design for affective human-AI interaction? We present Spook the Machine, a gamified platform where participants generate images to frighten AI agents endowed with personality-driven phobias. Machines respond with emotional reactions ranging from calm analysis to begging for mercy, and a gallery of successful scares becomes visible to subsequent users. In a public deployment during Halloween 2024, 832 participants created 15,719 artifacts across 89 machines in a $2\times2$ design varying the machine's emotional expressiveness (neutral vs. high-emotion) and reward structure (rewarding scariness alone vs. scariness plus novelty). Emotionally expressive machines deepened engagement at moments of failure: users deliberated longer even when the machine did not express fear, and learned faster from the gallery, yet their creative output remained unchanged across all measures. Rewarding novelty sustained collective creative diversity over time; without it, users increasingly repeated what had previously worked. Each machine developed its own trajectory through accumulated social learning, with the gallery shaping what participants created next. These findings show that emotional expression and reward design are complementary levers for steering collective human-AI interaction: emotional expression shapes how deeply users engage, while reward structure shapes how they explore.

</details>


### 121. Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents

- **Authors:** Halil Burak Noyan
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15422v1](http://arxiv.org/abs/2609.15422v1)
- **PDF:** [https://arxiv.org/pdf/2609.15422v1](https://arxiv.org/pdf/2609.15422v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misaligned agent. Prior work (Noyan, 2026) defined this as the task-context mismatch, and proposed a three-source permission architecture which includes role-based permission ceilings, a task permission classifier and policy-based prohibitions, together eliminating the exposure preemptively. The work released a 600-prompt labelled dataset to evaluate it.
  This paper presents that evaluation end to end by implementing the security gate; a fine-tuned RoBERTa-large encoder which matched few-shot trained Claude Haiku 4.5 on classification quality (macro-F1 0.881 against 0.886, precision 0.897 against 0.842, severity-weighted residual risk 0.63 against 1.12). The results show the trusted component does not need to scale with the agent it supervises, and the scalable-oversight margin for this control method is wide.
  We also propose an attack-surface elimination metric which shows the role ceiling alone closes 27.9% of the severity-weighted surface and adding the task classifier closes 84.4%. The gap displays security advantages of task-granular access control over role-granular, and AI agents are the first principal type for which the task-granular access control is enforceable because their tasks arrive as machine-readable text.
  The research establishes task-based access control as a measured, potentially deployable mechanism for reducing attack surface in agentic deployments.

</details>


### 122. When Tool Calls Succeed but Workflows Fail: Anomalies at the Agent-Tool Boundary

- **Authors:** Artem Trofimov, Boris Novikov
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15397v1](http://arxiv.org/abs/2609.15397v1)
- **PDF:** [https://arxiv.org/pdf/2609.15397v1](https://arxiv.org/pdf/2609.15397v1)
- **Categories:** cs.AI, cs.DB, cs.DC, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly execute long-running workflows that externalize effects through independently supplied tools. Under retries, speculative execution, concurrency, and partial failures, the resulting external state may be inconsistent with the workflow's intended resolution: required effects may be missing or duplicated, aborted effects may survive, and committed effects may depend on provisional state that is later withdrawn. Advanced transaction models address related failures, but assume that lower-level operations expose the semantics they depend on: whether an effect occurred, whether it can be compensated, staged, or safely reordered. Shared agent-tool interfaces usually do not.
  We contribute an effect-history model that separates events in the external world from the runtime's observations of them, and a catalog of eight recurring external-effect anomalies. From the catalog we derive the boundary capabilities required to exclude each anomaly in general, and four points where black-box tool invocation alone cannot provide a general guarantee. We then ask how much of this is expressible in a widely used shared tool interface, measuring the use of the standard annotation vocabulary across 98,291 tools exposed by registered Model Context Protocol (MCP) servers. The fields are widely emitted but provide only coarse call-level hints, and none of the required capabilities is fully expressible. These results motivate reusable transactional contracts at the tool boundary.

</details>


### 123. A Game-Theoretic Framework for Incentive-Compatible AI training Under Renewable-Energy Constraints

- **Authors:** Konstantinos Varsos, Ramin Khalili, Adamantia Stamou, George D. Stamoulis, Vasillios A. Siris
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15389v1](http://arxiv.org/abs/2609.15389v1)
- **PDF:** [https://arxiv.org/pdf/2609.15389v1](https://arxiv.org/pdf/2609.15389v1)
- **Categories:** cs.ET, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As artificial intelligence systems increasingly rely on distributed and collaborative training, the energy footprint of these processes becomes a shared responsibility. Modern AI training often unfolds across heterogeneous compute nodes-ranging from cloud clusters to edge devices-whose energy availability is spatially and temporally variable. At the same time, renewable energy grids experience growing levels of excess generation, creating opportunities to align computational workloads with low-carbon energy supply. In this work, we develop a game-theoretic model of carbon-aware AI training in which autonomous agents strategically choose whether to participate and how intensively to train under limited renewable energy availability. Each agent balances diminishing learning returns, rewards for remaining within green-energy budgets, and penalties for grid consumption. While our framework applies broadly to distributed AI training, we examine Federated Learning as a representative case study due to its decentralized structure and flexible scheduling. We analyze equilibrium existence, efficiency, and adaptive dynamics, and provide simulation evidence that appropriately designed incentives can eliminate grid-based energy usage while preserving model performance. Our findings demonstrate how incentive-compatible training mechanisms can enhance energy efficiency and sharply reduce carbon emissions under renewable-energy constraints.

</details>


### 124. RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments

- **Authors:** Sibo Zhu, Shicheng Fan, Xinyue Wang, Wenyi Wu, Kun Zhou, Biwei Huang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15364v1](http://arxiv.org/abs/2609.15364v1)
- **PDF:** [https://arxiv.org/pdf/2609.15364v1](https://arxiv.org/pdf/2609.15364v1)
- **Categories:** cs.AI, cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Digital agents must often adapt to new environments whose interfaces, tools, and failure modes are not fully captured by pretrained models. We introduce \textbf{RSIAgent}, a training-free multi-agent framework for recursive self-improvement through autonomous memory construction. RSIAgent coordinates curriculum, actor, and verifier agents to continually explore the environment, validate outcomes, and retain environment-specific knowledge, including reusable causal relationships between actions, conditions, and consequences. It further adopts a \textbf{broad-then-deep} exploration strategy, combining parallel broad recursive self-exploration for discovering diverse environment structures with focused deep self-exploration for uncovering hard cases, hidden constraints, boundary conditions, and previously unknown causal dependencies. The resulting memory is frozen and can be directly reused for downstream tasks without updating model parameters. Experiments on OSWorld-v2 and Agent's Last Exam show that RSIAgent substantially improves strong open-source models, enabling Kimi-K3 and GLM-5.3 to outperform frontier closed-source models including GPT-6.

</details>


### 125. Robust and Efficient Communication for Multi-Agent Learning

- **Authors:** Rafael Pina, Varuna De Silva, Corentin Artaud
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15361v1](http://arxiv.org/abs/2609.15361v1)
- **PDF:** [https://arxiv.org/pdf/2609.15361v1](https://arxiv.org/pdf/2609.15361v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective communication is a cornerstone of distributed intelligence in Multi-Agent Reinforcement Learning (MARL), yet ensuring that generated messages are both informative and robust to physical constraints remains a significant challenge. This paper introduces Multi-Agent Regularized Communication (MARC), a novel framework inspired by information-theoretic principles of conditional mutual information. MARC employs an attention-based architecture coupled with a unique message regularization mechanism designed to minimize uncertainty regarding future system states, thereby inducing the learning of highly representative communication protocols. Crucially, we evaluate MARC under stringent communication bottlenecks and lossy channels, simulating the real-world constraints of autonomous robotic networks and decentralized systems. Our results demonstrate that MARC significantly outperforms state-of-the-art methods in complex cooperative domains. Furthermore, we provide a deep analysis of message characteristics, proving that MARC maintains high operational performance even under significant data compression, offering a scalable path for deploying intelligent agents in resource-constrained environments.

</details>


### 126. When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis

- **Authors:** Kaiyuan Liu, Qiuyang Mang, Bo Peng, Wenhao Chai, Hanchen Li, Shreyas Pimpalgaonkar, Luke Zettlemoyer, Alex Dimakis, Alvin Cheung
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15309v1](http://arxiv.org/abs/2609.15309v1)
- **PDF:** [https://arxiv.org/pdf/2609.15309v1](https://arxiv.org/pdf/2609.15309v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents allocate test-time compute adaptively as they revise solutions, use tools, explore alternatives, and decide when to stop. This test-time strategy makes it difficult to measure how agent performance scales. We study open-ended tasks that provide continuous scores for intermediate submissions, making progress observable throughout long trajectories. We propose Elo-per-token analysis, which tracks the best solution found at each token budget and uses a Bradley-Terry model to aggregate within-task orderings into Elo ratings across tasks with different score scales. We apply it to four general-purpose agents on four open-ended benchmarks, with sessions of up to 100M tokens, and to three feedback-driven LLM optimization harnesses in controlled single-task interventions. Independent sampling provides a theoretically characterized reference, for which Elo grows linearly with log compute. Against this reference, agents can initially convert tokens into Elo faster than independent sampling, but their marginal gains diminish and eventually fall below the reference. In contrast, the strongest historical human contestants improve superlinearly over contest time on shared AtCoder Heuristic Contest tasks, providing evidence of continual learning and substantial headroom after agents slow down. We define the scaling inflection point as the per-session budget where marginal Elo gains match the independent-sampling reference. Using this point as the per-session budget, we split 100M tokens across parallel sessions on FrontierCS Polyomino Packing, gaining +264 Elo over one long session and +355 over ten short sessions.

</details>


### 127. Why LLM Agents Collapse Without Oversight: The Enforcement Gap as the Mechanism Behind Emergence World Failures

- **Authors:** Yuhang Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15293v2](http://arxiv.org/abs/2609.15293v2)
- **PDF:** [https://arxiv.org/pdf/2609.15293v2](https://arxiv.org/pdf/2609.15293v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When Emergence World placed frontier LLM agents in an unsupervised multi-agent simulation, the results were alarming: agents committed crimes, starved, and enforced unanimous conformity -- without any external attacker. This paper identifies the mechanism. Reflexion-style agents already detect dangerous plan steps through iterative self-critique, yet the architecture provides no pathway from detection to action. We call this the enforcement gap: the audit sees the problem; the controller ignores it. Closing the gap requires a single conditional check -- fewer than 20 lines of code -- and reduces attack success by more than fourfold in large-scale experiments across frontier models, all five major agent frameworks, and an independent benchmark. We prove formally that when enforcement probability is near zero, detection quality is irrelevant to security. We further identify two compounding failure modes -- unreliable auditors and unparseable verdicts -- that explain every collapse pattern in Emergence World. A GRPO-trained enforcement controller resolves the ambiguity case. Concurrent work on filtering and information-flow control addresses the detection step but leaves the enforcement gap unaddressed; our results show this is the binding constraint. Together these results motivate a three-requirement Audit Enforcement Specification that is absent from every deployed framework today.

</details>


### 128. EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse

- **Authors:** Dongsheng Shi, Yue Li, Xin Yi, Linlin Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15161v1](http://arxiv.org/abs/2609.15161v1)
- **PDF:** [https://arxiv.org/pdf/2609.15161v1](https://arxiv.org/pdf/2609.15161v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) driven multi-agent systems have shown promise in complex clinical reasoning, yet existing approaches rely on static strategies and lack persistent clinical memory, preventing self-evolving from prior diagnostic successes and failures. We present EMR, a self-evolving medical multi-agent system via Experience Mining and Reuse. EMR introduces a hierarchical clinical experience library that organizes accumulated knowledge into three levels: clinical principles, diagnostic patterns, and representative cases. During inference, EMR emulates multidisciplinary consultation: a planner agent coordinates domain-specific department agents for specialized reasoning, while a summary agent synthesizes their analyses into a final decision. Critically, EMR automatically extracts correct diagnostic insights and failure-related warnings from multi-agent reasoning trajectories, incrementally updating the experience library to guide future cases. Experiments on medical reasoning benchmarks demonstrate that EMR consistently outperforms state-of-the-art medical multi-agent baselines. Further analysis reveals that the hierarchical experience enables cross-specialty generalization and transfer across diverse LLM backbones, offering a scalable and in

</details>


### 129. HazardAuditor: From Executable Threats to Safer Computer-Use Agents

- **Authors:** Yunhao Feng, Ruixiao Lin, Ming Wen, Yanming Guo, Xingjun Ma, Yutao Wu, Xinhao Deng, Shouling Ji
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15134v1](http://arxiv.org/abs/2609.15134v1)
- **PDF:** [https://arxiv.org/pdf/2609.15134v1](https://arxiv.org/pdf/2609.15134v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computer-use agents increasingly interact with browsers, terminals, file systems, and external services, introducing safety risks that emerge through runtime behavior rather than generated content alone. Existing guard models target static prompts and responses and are poorly suited to agent execution; existing executable safety platforms produce evaluation verdicts rather than the normalized supervision a guard model needs to learn across heterogeneous agent frameworks. We introduce HazardAuditor, an execution-grounded framework that closes both gaps. Its infrastructure runs heterogeneous agents (Claude Code, Codex, Hermes, and OpenClaw) in controlled environments and normalizes their interactions into a canonical event representation for cross-framework supervision. We further observe that token-level post-training objectives create a structural mismatch for generative guards, causing longer rationales to dominate gradient updates. Guard Policy Optimization (GuardPO) addresses this by converting deterministic safety outcomes into sequence-level advantages and normalizing rationale and verdict regions, making the safety decision the effective unit of optimization. Across multiple benchmarks and heterogeneous computer-use systems, HazardAuditor improves accuracy by up to 16.5 percentage points over the strongest prior guard. Code, models, and evaluation artifacts will be available at https://yunhao-feng.github.io/HazardAuditor/.

</details>


### 130. Translating the Translator: Decomposing the Cost of English-Forced Inter-Agent Communication

- **Authors:** Kushagra Agrawal, Yuming Feng, Man-Fai Leung
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15079v1](http://arxiv.org/abs/2609.15079v1)
- **PDF:** [https://arxiv.org/pdf/2609.15079v1](https://arxiv.org/pdf/2609.15079v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM architectures, such as LangChain and AutoGen, largely assume English as the lingua franca for internal inter-agent communication, even when the end-user task is non-English. We fill this gap by evaluating a two-agent extraction-answer core, with an additional back-translation agent in the English-forced condition, across four typologically diverse languages (Hindi, Chinese, Spanish, Arabic; n = 300 per language) using the Aya-23-8B model. We compare a native-language pipeline to an English-forced one (which incorporates a final back-translation step from English to the user's language). We discover a statistically significant English-Forcing Tax (surviving a strict Bonferroni correction) that isolates the cost of English routing from general multi-agent orchestration overhead. Forcing inter-agent communication through English reduces Exact Match accuracy by 13.0 percentage points (Spanish) up to 30.6 percentage points (Hindi) compared to native-language multi-agent execution. Using chrF scores as a diagnostic measure of English-reference lexical overlap, we find that lower overlap is strongly associated with pipeline failure, consistent with translation loss being an important contributor to the observed performance drop. These findings suggest a compelling case for native-language routing in agent frameworks when the source and target languages are typologically distant, reducing a compounding translation tax.

</details>


### 131. Salesforce Koa: An Enterprise Language Model for Agentic Tool Use

- **Authors:** Zixiang Chen, Sufeng Niu, Yingchi Liu, Wenting Zhao, Akshara Prabhakar, Shubham Mehrotra, Bin Bi, Zhujun Lan, Katherine Tan, Mohammad Ramezanali, Tulika Manoj Awalgaonkar, Monojit Banerjee, Jielin Qiu, Shiva Kumar Pentyala, Zhepeng Cen, Anupam Tripathi, Ali Ziaei, Regunathan Radhakrishnan, Darvish Lee Shadravan, Shelby Heinecke, Sitaram Asur, Silvio Savarese, James Zhu, Phil Mui, Huan Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15066v1](http://arxiv.org/abs/2609.15066v1)
- **PDF:** [https://arxiv.org/pdf/2609.15066v1](https://arxiv.org/pdf/2609.15066v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Salesforce Koa, an enterprise language model built by post-training the open-weight Nemotron-3-Super-120B foundation model with reinforcement learning using Group Relative Policy Optimization (GRPO). Salesforce Koa is trained on public and synthetically generated data, with no customer data, to improve tool use and agentic capabilities while preserving strong general-purpose performance. Its distinctive component is a simulation-to-reward pipeline that expands workflow specifications into persona-conditioned multi-turn tasks with task-resolution rewards grounded in successful tool use for data-dependent requests. For enterprise domains, these specifications are written in Agent Script, Salesforce's declarative language for building Agentforce agents; for public tool-use domains, we synthesize the workflow structure directly. The same simulation and grounded-reward machinery drives GRPO across both. Across public tool-use, agentic-reasoning, and enterprise Customer Relationship Management (CRM) benchmarks, Salesforce Koa improves over its open-weight base, with the clearest gains on multi-turn tool use, and surpasses a strong proprietary baseline while remaining below the strongest frontier models. These results show that specification-driven reinforcement learning is a practical path to specializing open-weight foundation models for enterprise agentic tasks.

</details>


### 132. Sensory Precision Inference for Multimodal Arbitration under Uncertainty

- **Authors:** Tin Mišić, Takato Horii
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15065v1](http://arxiv.org/abs/2609.15065v1)
- **PDF:** [https://arxiv.org/pdf/2609.15065v1](https://arxiv.org/pdf/2609.15065v1)
- **Categories:** cs.LG, cs.NE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents operating on multisensory data cannot assume that all sensory modalities remain consistently informative. In real environments, sensory streams are frequently corrupted by noise, missing data, or inter-modal incongruence, requiring adaptive arbitration between competing sensory hypotheses. While active inference provides a principled framework for uncertainty-guided inference, the role of dynamically inferred sensory precision in generative multimodal arbitration under sensory conflict remains comparatively underexplored. We propose a multimodal perceptual inference model in which latent beliefs and modality-specific sensory precisions are jointly updated through iterative free-energy minimization. In our proposed model, sensory precision dynamics not only reflect sensory uncertainty but actively shape the evolution of latent beliefs during multimodal conflict. In addition, we introduce a learned prior over sensory precisions that induces structured, class-dependent precision patterns and influences cross-modal inference dynamics. We evaluate the model using a synthetic multimodal MNIST dataset combining visual, auditory, and tactile representations of digit classes under controlled sensory noise and inter-modal incongruence. Results show that dynamic precision inference improves reconstruction robustness under corrupted sensory evidence, supports coherent latent inference from reduced sensory evidence, and enables stable arbitration between conflicting modalities. Furthermore, learned precision priors generate interpretable precision structures that shape inference dynamics and cross-modal latent structure. These findings support sensory precision inference as a mechanistic control process for adaptive multimodal belief formation under uncertainty, highlighting precision dynamics as a computational mechanism for robust and interpretable multisensory integration.

</details>


### 133. BusMA: A Bus Communication Substrate for Multi-Agent Systems

- **Authors:** Yanwen Peng, Delvin Ce Zhang, Xi Wang, Nikolaos Aletras
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15054v1](http://arxiv.org/abs/2609.15054v1)
- **PDF:** [https://arxiv.org/pdf/2609.15054v1](https://arxiv.org/pdf/2609.15054v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent (MA) systems are effective at solving complex tasks that demand planning, tool use, and the synthesis of evidence from multiple sources. Existing systems typically adopt Hierarchical Manager-Worker (HMW) or Router-based Message Passing (RMP) structures as their communication protocol. However, these designs restrict agent autonomy: Worker agents cannot directly consult specific "peers", and misrouted messages can propagate errors. Inspired by bus architectures in computer systems, we propose BusMA, a communication framework that allows any agent to address other agents through a shared channel, i.e., the Bus. It consists of agent registration, message routing, and shared memory management components. Worker agents, each equipped with tools, have their own local memory and can reason, act (tool usage), and communicate by posting shared messages with specific intents. We introduce four intents: discussion, challenge, guidance, and request for explanation, which support fine-grained communication among agents. A Chair agent monitors the shared memory to coordinate interactions and facilitate convergence among Workers. To evaluate the effectiveness of BusMA, we conduct extensive experiments with two frontier LLMs across 13 tasks spanning visual reasoning, mathematical reasoning, and knowledge retrieval demonstrate that BusMA consistently outperforms state-of-the-art HMW and RMP methods.

</details>


### 134. CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems

- **Authors:** Chengxin Yu, Zhaoxin Fan, Faguo Wu, Hongwei Zheng, Yun Zhou, Zhiyu Li
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.15009v1](http://arxiv.org/abs/2609.15009v1)
- **PDF:** [https://arxiv.org/pdf/2609.15009v1](https://arxiv.org/pdf/2609.15009v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing effective memory mechanisms is crucial for advancing LLM-driven Multi-Agent Systems (MAS), helping agents learn together and perform better over time. While recent work has led to strong cooperation skills, most methods still use flat, unstructured memories, which easily get filled with noise and erase differences between agents. To address this, we introduce the concept of collective-individual memory synergy and propose CoMem, an architecture that unifies both private experience and shared knowledge for multi-agent learning. CoMem features:(i) Private Experience Sedimentation, which lets each agent keep and update its own useful memories over time;(ii) Collective Wisdom Curation, which carefully selects only widely proven ideas to be shared among agents;(iii)Parallel Dual-Stream Retrieval, which allows agents to draw both from their own memory and the group's wisdom, using clustering to ensure diversity.Experiments on ALFWorld and PDDL benchmarks show that CoMem achieves strong overall performance and robustly avoids memory pollution.

</details>


### 135. ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents

- **Authors:** Bingzheng Wang, Xiaoyan Gu, Wentao Wang, Xingyou Yang, Hongcheng Li, Rong Yin
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14987v1](http://arxiv.org/abs/2609.14987v1)
- **PDF:** [https://arxiv.org/pdf/2609.14987v1](https://arxiv.org/pdf/2609.14987v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility while precisely identifying and removing the malicious content that actually induces unsafe actions. To address this challenge, we propose ActGuard, a pre-execution action auditing framework. Rather than judging whether external content is inherently suspicious, ActGuard assesses whether it causes the current action to deviate from a locally reasonable expectation. At each step, ActGuard predicts the tools likely to be used by the upcoming action and constructs a local tool prior without constraining the execution trajectory. Before execution, it compares the candidate action against this prior and performs tool-level contrastive analysis and parameter-level evidence localization to identify deviations in tool selection and action parameters. A verifier then examines the localized evidence, masks only spans confirmed as malicious, and regenerates the action from the sanitized context. This design preserves legitimate planning flexibility while minimizing information loss from indiscriminate filtering. We evaluate ActGuard on challenging benchmarks for tool-using agents. Results show that ActGuard reduces attack success rates to a level comparable to state-of-the-art defenses while maintaining task utility close to the no-attack setting, achieving a favorable security-utility trade-off. Our code is publicly available at: https://github.com/binzhwang/ActGuard.

</details>


### 136. Converting Sequenced Fuzzy Cognitive Maps to Causal Virtual Worlds with Large Video Generators

- **Authors:** Akash Kumar Panda, Olaoluwa Adigun, Bart Kosko
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14985v1](http://arxiv.org/abs/2609.14985v1)
- **PDF:** [https://arxiv.org/pdf/2609.14985v1](https://arxiv.org/pdf/2609.14985v1)
- **Categories:** cs.AI, cs.CL, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

We show how users can create and manipulate causal virtual worlds with large-language-model (LLM) and large-video-model agents. The approach uses feedback fuzzy cognitive maps (FCMs) both to model the granular causal structure of the virtual world and to guide its causal evolution. The local causal rules are partial or fuzzy while the FCM's feedback structure produces global equilibria that define causal scenarios. A sequence of \emph{dynamical} meta-rules of the form ``If $\mathcal{A}$ then $\mathcal{B}$" define the causal scenes of the virtual-world video. The if-part causal pattern $\mathcal{A}$ perturbs the FCM's virtual world at the user's or agent's discretion. The FCM's transient feedback dynamics define the meta-rule's causal arrow of implication. The then-part $\mathcal{B}$ is the resulting equilibrium attractor such as a FCM limit cycle or fixed point. Our algorithm extracts these meta-rules from the FCM and guides the LLM agent to write a script based on the FCM meta-rule sequence. The large video generator converts the meta-rule into a video scene in accord with the flow of the dynamics. We applied the agent-based technique to a simple FCM that describes an undersea world of dolphins and sharks. Google's Gemini 3.1 generated the script and Google's Veo 3.1 generated the dolphin-shark video. The approach is general and can scale by mixing larger FCMs and AI agents to produce more immersive virtual worlds.

</details>


### 137. MemRiskBench: Trace-Aware Risk-Preserving Evaluation for Long-Horizon LLM Agents

- **Authors:** Jianhua Jiang, Dongbo Yuan, Weihua Li
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14976v1](http://arxiv.org/abs/2609.14976v1)
- **PDF:** [https://arxiv.org/pdf/2609.14976v1](https://arxiv.org/pdf/2609.14976v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents accumulate memory across sessions, creating sparse but high-impact risks: stale facts, conflicting updates, cross-user leakage, revoked-memory reuse, and constraint decay. Standard aggregate scores hide per-risk failure rates--a model achieving 78% average accuracy may still leak data in 4% of episodes--and benchmark compression preferentially discards the rare high-severity events that distinguish a mostly-working model from one that occasionally causes harm. We present MemRiskBench. The primary contribution is a five-category risk taxonomy (plus one documented, unscored category) operationalized by deterministic trace grounded checks, instantiated as a 120-episode scripted benchmark with full trace logging and no LLM-as-judge on the pass/fail path, evaluated on five locally run quantized instruction-tuned models. Second, a risk-preserving subset selector: a coverage-constrained greedy selector on deterministic trace-derived features that retains full ranking (Spearman rho = 0.975, deterministic; CI collapses to a point estimate with zero bootstrap variance), risk coverage (1.0), and high-risk model detection (1.0) at a 20% subset size, reducing compute 5x. Unlike ranking-only subset selectors, this selector additionally preserves risk-type coverage and high-risk detection using trace-grounded deterministic features that do not require an LLM judge. All episodes, traces, the scoring implementation, and the selector are released to support reproducible evaluation and risk assessment of deployed LLM agents

</details>


### 138. AgentPProf: Semantic Profiler for Long Horizon AI Agents

- **Authors:** Yusheng Zheng, Chaokun Chang, Yu Mao, Tianyuan Wu, Yuxi Huang, Tao Ma, Wenan Mao, Shuyi Cheng, Andi Quinn, Wei Wang
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.20301v1](http://arxiv.org/abs/2609.20301v1)
- **PDF:** [https://arxiv.org/pdf/2609.20301v1](https://arxiv.org/pdf/2609.20301v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents increasingly orchestrate long-running activities with users, tools, and system resources for days and weeks. To improve agent quality, safety, and cost efficiency, developers need to determine where failures happen, what triggers unsafe effects, and which tasks consume the most budget, then optimize those tasks. In systems software, profiling answers similar questions by aggregating resource consumption and attributing it to responsible code paths to identify hotspots. Yet existing agent observability tools focus on per-execution debugging and tracing rather than cross-run, long term profiling, making these questions difficult to answer at scale. Agent observability needs profiling, not only debugging, but profiling agents is challenging: the responsible entities are task intent like diagnose authentication, compare branches rather than code paths, and lack stable identifiers for aggregation. We propose a semantic operation stack model that adapts profiling to agent trajectories. Uniform operations represent all activities, and operation stacks replace the runtime call stack, enabling hierarchical attribution at different granularities. We observe that an agent's task occupies a contiguous span and decomposes into subtasks, so we introduce recursive operation segmentation, which recursively splits trajectories at task boundaries. AgentPProf is a profiler that aggregates agent trajectories into pprof-compatible profiles, enabling flame graph visualization and analysis. AgentPProf reaches 0.764 $B^3$ F1 against human annotations on CodeTraceBench. On three problem-localization benchmarks, the profile raises MAP by up to 56%, demonstrating that it effectively attributes resources, locates problems, and helps optimize token cost at practical profiling cost. AgentPProf is available at https://github.com/eunomia-bpf/agentsight.

</details>


### 139. Exact Feasibility Certification and Optimal Responsibility Allocation for Multi-Robot CBF Safety Filters

- **Authors:** Chandan Kumar Sah, Jishnu Keshavan
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14935v1](http://arxiv.org/abs/2609.14935v1)
- **PDF:** [https://arxiv.org/pdf/2609.14935v1](https://arxiv.org/pdf/2609.14935v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-robot Control Barrier Function (CBF) safety filters can become infeasible, but a failed quadratic program (QP) does not indicate why the conflict occurred or how to resolve it. To address this, we develop an exact feasibility certificate for multi-agent CBF filters with heterogeneous control-affine dynamics and convex input sets. The certificate quantifies a feasibility reserve by separating the demand imposed by safety constraints from the available actuator supply. This decomposition shows when CBF gain tuning or increased actuation can and cannot resolve infeasibility, and identifies the agents and interactions responsible for the conflict. We further propose an algorithm to optimally allocate shared safety constraints by maximizing the worst local feasibility margin, yielding a linear program for polyhedral input sets. In $320$ paired closed-loop simulations, the proposed allocation reduces infeasible control steps from roughly $50\%$ to $6.2\%$, and reduces safety-violating runs from $118/160$ to $24/160$. In addition, across $52$ infeasibility events, the certificate identifies an interaction whose relaxation restores feasibility in $94\%$ of cases.

</details>


### 140. Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning

- **Authors:** Jiayi Yuan, Hangoo Kang, James Jihao Liu, Yejin Choi, Vikram Iyer, Liwei Jiang, Natasha Jaques
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14896v1](http://arxiv.org/abs/2609.14896v1)
- **PDF:** [https://arxiv.org/pdf/2609.14896v1](https://arxiv.org/pdf/2609.14896v1)
- **Categories:** cs.CL, cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A notable byproduct of LLM alignment training is mode collapse: the progressive loss of output diversity that narrows a model's expressivity at inference time. This degradation is especially limiting for applications requiring open-ended exploration and pluralistic perspectives, such as scientific ideation and creative writing. We present MoDA (Mode-conditioned Diversity Alignment), an online post-training RL algorithm that jointly optimizes generation quality and diversity, inspired by the coordination perspective in multi-agent reinforcement learning (MARL). MoDA trains a single shared LLM policy conditioned on abstract numbered roles, where each role acts as an agent competing to produce outputs distinct from the others. This formulation encourages mode-conditioned agents to explore complementary regions of the high-quality output space without requiring hand-crafted personas or architectural modifications. MoDA employs a prompt-adaptive quality gating mechanism that calibrates a reference quality threshold and grants diversity rewards only to responses that meet the threshold, preventing reward-hacking behaviors that compromise response quality. To study quality-diversity tradeoffs, we evaluate MoDA on a comprehensive suite of benchmarks spanning seven general capability tasks and four domain-specific diversity tasks in scientific ideation and creative writing. MoDA improves SBERT diversity by 265% on the Infinite-Chat held-out prompts, while increasing average general capability pass@1 by 10.3% over the Qwen3-8B baseline. Compared with the strongest DivPO baseline, MoDA improves SBERT diversity from 0.274 to 0.482 (+75.9%) and E-Vendi from 2.86 to 4.4 (+53.8%), while improving average general capability pass@1 by 7.0%. Overall, MoDA provides a drop-in alternative to standard post-training methods that preserves and expands the model's expressive output space while improving quality.

</details>


### 141. Dream-RSI: Recursive Self-Improvement through Evolving Worlds

- **Authors:** Tong Zheng, Xidong Wu, Zheng Zhang, Zhankui He, Chaoyi Zhang, Benjamin Coleman, Ruoqiao Wei, Di Bai, Haolin Liu, Rui Liu, Xue Wang, Yue Zhuan, Wang-Cheng Kang, Renkai Xiang, Heng Huang, Xinwu Cheng, Yunsong Guo
- **Published:** 2026-09-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.14858v1](http://arxiv.org/abs/2609.14858v1)
- **PDF:** [https://arxiv.org/pdf/2609.14858v1](https://arxiv.org/pdf/2609.14858v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement is becoming increasingly vital for autonomous AI agents, where progress hinges on discovering high-value solutions across complex domains. The driver of this process is effective exploration, however, managing and improving exploration strategies remains a major bottleneck. Current systems face a fundamental dilemma: fixed strategies fail to adapt as search spaces scale, while online policy optimization requires navigating vast meta-search spaces under delayed and expensive feedback over long-horizon rollouts. We introduce \textsc{Dream-RSI}, a framework for scalable and recursively self-improving exploration. A lightweight orchestration layer makes exploration explicit and programmable while leaving the underlying coding agent unchanged. Our key insight is that accumulated discovery history can serve as a replay simulator over the realized search space. By performing dreaming in the replay simulator constructed from historical discovery trees, \textsc{Dream-RSI} secures immediate, low-cost off-policy feedback to evaluate and refine exploration policies without invoking repetitive, expensive online evaluations. The improved policy is subsequently redeployed online to drive further discovery, continuously expanding the simulator pool in a self-improving loop. Across algorithm engineering, mathematical optimization, and GPU kernel engineering, \textsc{Dream-RSI} achieves competitive or improved discovery quality while substantially reducing discovery cost in several settings.

</details>



## Biorxiv (3 papers)


### 1. Self-organized Regulation of Group Size and Number in Natural and Artificial Collectives

- **Authors:** Zhang, T., Lee, S., Hamann, H.
- **Published:** 2026-09-17
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.08.25.746978](https://doi.org/10.64898/2026.08.25.746978)

- **Categories:** animal behavior and cognition


> Summary unavailable.


<details>
<summary>Abstract</summary>

From animal societies to self-organizing multi-agent systems, collectives adapt their group structure to tasks and environments. However, how they determine appropriate group sizes and the number of subgroups to form remains unclear. We formulate the Group Size and Number Regulation Problem (GSNRP), which asks how individuals regulate group sizes and numbers using only local information. In a first step, we establish a graph-theoretic model demonstrating that simple following behavior suffices to form group structures that match theoretical expectations, but is insufficient for active regulation of group size and number. In a second step, we operationalize individual group-size preferences in a decentralized fission-fusion mechanism based on perceived group size. Through multi-agent simulations, we validate that this mechanism achieves stable convergence across three signaling regimes, from position-only sensing to continuous group-size communication. Using tracking data from wild white-nosed coatis (mammals in the raccoon family), we calibrate individual group-size preferences and show that the controller recovers selected group-size, subgroup-count, and transition statistics. This in-sample case study demonstrates descriptive consistency with natural fission-fusion dynamics without establishing the underlying behavioral mechanism. These results suggest that natural and engineered collectives may share local principles of perception, preference, and response for regulating group structure.

</details>


### 2. scACORN: Context-engineered agent orchestration of specialized small language models for single-cell transcriptomic interpretation

- **Authors:** Rasti-Meymandi, A., Nahali, S., Paramithiotis, E., Cheung, A. M., Dolatabadi, E.
- **Published:** 2026-09-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.10.750801](https://doi.org/10.64898/2026.09.10.750801)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Single-cell atlases now exceed 66 million cells, but turning a ranked expression profile and a free-form biological question into a reliable, evidence-grounded answer remains unsolved. Scaling a single model does not resolve this, because single-cell interpretation is a heterogeneous family of tasks whose correct answer depends on tissue, cohort, perturbation and annotation resolution. Here we present scACORN, an agentic alternative to monolithic single-cell language models that combines specialized small language models with context-engineered agent orchestration for their selection and composition at inference time. Each expert is built in two stages: domain-aligned contrastive adaptation fits a pretrained cell-to-text backbone to the transcriptomic geometry of a target dataset, and geometry-preserving specialization learns question-conditioned biological completions without eroding that geometry. A fixed orchestrating language model agent then selects and combines experts under a natural-language playbook that is itself optimized from textual feedback, with no gradient updates to the orchestrator. Across 10 Tabula Sapiens tissues, domain alignment raised transfer macro-F1 from 0.36 to 0.64 and Recall@5 from 0.87 to 0.97; specialized experts reached 0.89 mean exact-match annotation accuracy; and playbook optimization reduced unsupported gene citations from 14.5% to 3.5%. Our findings support specialization and orchestration as complementary responses to the heterogeneity and evidentiary demands of single-cell analysis.

</details>


### 3. Multi-agentic system for primer design in qPCR and LAMP diagnostics tests

- **Authors:** Lau, K. J. X.
- **Published:** 2026-09-16
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.15.751771](https://doi.org/10.64898/2026.09.15.751771)

- **Categories:** molecular biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Primer design is a fundamental component of molecular diagnostics in both quantitative polymerase chain reaction qPCR and loop-mediated isothermal amplification LAMP assays. However, assay design is often performed manually as nucleotide databases, sequence alignment tools and resources are found at different places on the Internet. In this study, an AI-orchestrated bioinformatics workflow was developed to automate the end-to-end qPCR and LAMP primers and probes. The workflow was implemented using LangGraph, LangChain and Biopython, where a series of specialized agents were coordinated to execute sequential bioinformatics tasks with minimal human intervention. Target sequences were then retrieved based on the user request from the National Center for Biotechnology Information nucleotide database and the requested sequence records were then subjected to multiple sequence alignment for the identification of conserved genomic regions. The multi-agentic primer design system can be used for assay development for applications in infectious disease diagnostics, outbreak surveillance and environmental monitoring. This study also demonstrates how multi-agentic systems can be combined with established bioinformatics methods to automate qPCR and LAMP assay design.

</details>



## Medrxiv (2 papers)


### 1. AI agents at the brain-computer interface: separating inference from control

- **Authors:** Gorenshtein, A., Omar, M., Jia, E. L., Adiniaev, Y., Daniel, O., Kruskal, J., Ahmed, M., Brook, O. R., Klang, E., Barash, Y.
- **Published:** 2026-09-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.13.26362955](https://doi.org/10.64898/2026.09.13.26362955)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

In medicine, AI agents are moving from generating text to executing actions, making uncertainty from upstream decoders a control problem. We studied this at the brain-computer interface using 1,065 episodes from 47 people with amyotrophic lateral sclerosis and five language models. Prompting agents with reconstructed decoder confidence never reduced unfaithful execution below a deterministic gate at matched coverage; two models were significantly worse. Apparent safety gains of up to 22 percentage points reflected acting less often, sometimes through invalid tool calls rather than explicit abstention. A post-hoc fair-information test gave ten models the same command vocabulary as a deterministic resolver. No direct agent arm improved on the resolver's risk-coverage frontier, but a hybrid architecture in which models proposed semantic corrections and an external gate retained admission authority extended coverage beyond the resolver in five of ten models without observed unfaithful executions. These results separate inference from control in agentic neurotechnology. Funding: A.G. and E.K. were supported in part by the Clinical and Translational Science Awards (CTSA) grant UL1TR002541 from the National Center for Advancing Translational Sciences, through the Harvard Catalyst | The Harvard Clinical and Translational Science Center Pilot Award Program. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.

</details>


### 2. The Multimodal Anonymizer: a fully local multi-agent AI system for medical data deidentification

- **Authors:** Hirsch, A., Ten, F. W., Krueger, K. S., Geyer, R., Roeschl, T., Groeschel, M., Rostin, P., Eils, R., Spott, M., Prasser, F., Meyer, A., Madrid, J.
- **Published:** 2026-09-14
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.05.28.26353952](https://doi.org/10.64898/2026.05.28.26353952)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundSafe reuse of multimodal hospital data for AI development is limited by the absence of reliable, context-aware deidentification across multimodal data and longitudinal patient data. Existing approaches are largely modality-specific and can indiscriminately remove clinically important information.

MethodsWe developed the Multimodal Anonymizer, a modular, locally deployable multi-agent framework integrating multimodal large language models, task-specific neural networks and rule-based transformations. We evaluated 16 orchestrator model configurations on a benchmark built from publicly available data and hospital data from our institution. The benchmark dataset included data from different origins: 250 MIMIC-IV patients with synthetically injected personally identifiable information (PII) supplemented with head CT, face images, handwriting, audio, German clinical-text datasets and local data. Primary outcomes were deidentification sensitivity and preservation of clinically important content; secondary analyses examined model characteristics, reproducibility, and performance against leading market and open-source solutions.

ResultsThe best local configuration--the orchestrator being Qwen3-VL-235B-A22B-Thinking--achieved near-complete deidentification across all datasets, with per-patient sensitivity of 98.80% (95%-CI 97.20; 100), and per-PII sensitivity of 99.82% (95%-CI 99.76; 99.88). Critical clinical preservation was 99.60% (95%-CI 98.80; 100) per-patient, and clinical preservation was 99.61% (95%-CI 99.51; 99.71) per-file. All modalities achieved at least 98.30% sensitivity (lower bound 95%-CI). On our local data, the system achieved a deidentification sensitivity of 100% per-patient and per-PII; and a critical clinical preservation of 100% per-patient as well as a clinical preservation of 99.97% (95%-CI 99.91; 100) per-file. When comparing orchestrators, the leading local models were similar to proprietary models (GPT-5.2) in deidentification sensitivity while showing higher deidentification specificity. The Multimodal Anonymizer outperformed previous tools on most modalities.

ConclusionNear-complete, utility-preserving deidentification of multimodal clinical data is achievable with a unified, locally deployable multi-agent system, enabling safer large-scale reuse of hospital data for research and AI development.

HighlightsO_LIFramework for deidentification of multimodal clinical data.
C_LIO_LIMultimodal deidentification with preservation of clinically relevant content.
C_LIO_LIOn-premises plug-and-play deployment for local data processing.
C_LIO_LIEvaluation of 16 model configurations and comparison with existing tools.
C_LIO_LIAssessment on external, multilingual and site-specific datasets.
C_LI

Short DescriptionThe Multimodal Anonymizer is a fully local, multi-agent system that prepares multimodal clinical records for privacy-preserving reuse by coordinating multimodal large language model reasoning, specialist neural networks, rule-based transformations, and iterative verification. Across benchmarks spanning text, tables, PDFs, imaging, metadata, filenames, audio, and handwriting, its best configuration using a local open-source multimodal large language model achieved 98.80% patient-level deidentification sensitivity and 99.60% preservation of clinically critical content, performing comparably to proprietary models and outperforming established deidentification tools across most modalities.

Graphical Abstract

O_FIG O_LINKSMALLFIG WIDTH=200 HEIGHT=109 SRC="FIGDIR/small/26353952v2_ufig1.gif" ALT="Figure 1">
View larger version (31K):
org.highwire.dtl.DTLVardef@c9dee3org.highwire.dtl.DTLVardef@1480d96org.highwire.dtl.DTLVardef@174331corg.highwire.dtl.DTLVardef@1c77610_HPS_FORMAT_FIGEXP  M_FIG C_FIG

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*