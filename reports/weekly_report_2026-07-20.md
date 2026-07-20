# Weekly AI Agent Paper Report

**Generated:** 2026-07-20 12:00
**Period:** 2026-07-13 to 2026-07-19

## Summary

- **Total papers fetched:** 733
- **Papers matching keywords:** 143
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-07-13) | Change |
|--------|-----------|-----------|--------|
| Total matched | 143 | 149 | -6 |
| arxiv | 141 | 148 | -7 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 1 | 0 | +1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (2 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-07-13
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

MotivationAs biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers.

ResultEcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAIs multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimers Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

Availability and implementationEcoXAI is available on GitHub at: https://github.com/EpistasisLab/EcoXAI.

Contactjason.moore@csmc.edu

</details>


### 2. Multi-Agent Dynamic Refinement Outperforms Static RAG in Clinical Reasoning for Complex Nephrology Cases

- **Authors:** Yano, Y., Kakizaki, H., Nagasu, H., Kishi, S., Koshida, T., Nihei, Y., Hirano, A., Sugawara, Y., Imaizumi, T., Osakabe, Y., Sakaguchi, Y., Nangaku, M., Mori, H., Naito, T., Ohashi, M., Maruyama, S., Matsui, I., Isaka, Y., Okada, H., Suzuki, Y., Kashihara, N.
- **Published:** 2026-07-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.15.26358121](https://doi.org/10.64898/2026.07.15.26358121)

- **Categories:** nephrology


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundLarge language models (LLMs) struggle with dynamic, longitudinal clinical reasoning. We developed a Multi-Stage Iterative Clinical Reasoning Agent framework to address this gap and systematically decouple the clinical efficacy of static retrieval-augmented generation (RAG) from dynamic self-refinement.

MethodsTen complex longitudinal nephrology cases, rigorously selected via a modified Delphi consensus technique, were blindly evaluated by four board-certified nephrologists and a multi-model AI panel. We compared three architectures across nine cognitive steps: (Model A) a baseline frontier LLM, (Model B) an LLM augmented with static guideline-based RAG, and (Model C) our proposed multi-agent framework featuring RAG integrated with iterative self-critique and refinement.

ResultsIn human evaluations (20-point scale), Model C (mean 17.2, SD 1.2) significantly outperformed both Model A (16.1, 1.3) and Model B (16.2, 1.2) (P < 0.001). Implementing static RAG (Model B) yielded no significant improvement over the baseline. Automated AI evaluations (15-point scale) corroborated these findings: Model C (14.7, 0.6) outscored Model A (14.2, 0.9, P < 0.001) and Model B (14.3, 0.9, P = 0.01). While monolithic models exhibited severe score degradations in planning-heavy tasks such as dynamic differential diagnoses, the multi-agent framework effectively intercepted error cascades, achieving significantly higher diagnostic accuracy (mean 17.6, P = 0.019) and therapeutic management scores (17.3, P = 0.002).

ConclusionsStatic knowledge retrieval alone fails to enhance frontier LLM performance in longitudinal medical reasoning. Distributing clinical workflows into a multi-agent dynamic refinement pipeline significantly improves reasoning completeness, intercepts error cascades, and safely resolves planning bottlenecks in complex patient care.

</details>


---



## Arxiv (141 papers)


### 1. Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems

- **Authors:** Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni, Andrea Manzoni
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16177v1](http://arxiv.org/abs/2607.16177v1)
- **PDF:** [https://arxiv.org/pdf/2607.16177v1](https://arxiv.org/pdf/2607.16177v1)
- **Categories:** cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensionality entailed by the exploration-exploitation dilemma in high-dimensional spaces. In this work, we bridge RL and traditional optimal control for dynamical system with a novel Physics-EnhAnced Reinforcement Learning (PEARL) paradigm tailored to the control of high-dimensional and parametric dynamical systems, exploiting the differentibility of their dynamics. Specifically, PEARL employs an actor-adjoint algorithm that leverages automatic differentiation to compute policy gradients over short horizons and adjoint-based sensitivities of future returns approximated via neural networks, significantly reducing the number of environment interactions, while mitigating long-term gradient instabilities. Through two challenging parametric navigation problems in unsteady flows, we show that PEARL (i) effectively exploits differentiable environments to outperform state-of-the-art RL algorithms, (ii) is sample efficient, thanks to the physics-guided policy learning, (iii) generalizes across multiple scenarios, which is crucial when dealing with parametric systems, and (iv) enables scaling RL to high-dimensional state and action spaces, without requiring low-dimensional state representations or multi-agent strategies.

</details>


### 2. Evaluating Open-Weight LLMs for Generating Structured Threat Information for Autonomous Vehicle Vulnerabilities

- **Authors:** Md Erfan, Ahmed Ryan, Md Kamal Hossain Chowdhury, Md Rayhanur Rahman
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16175v1](http://arxiv.org/abs/2607.16175v1)
- **PDF:** [https://arxiv.org/pdf/2607.16175v1](https://arxiv.org/pdf/2607.16175v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Connected and Autonomous Vehicles (CAVs) rely on interconnected software and hardware components, including sensors, Electronic Control Units, in-vehicle infotainment systems, and telematics units, where vulnerabilities can compromise assets, users, and vehicle operations. These vulnerabilities are commonly documented as plain text in the Common Vulnerabilities and Exposures (CVE) database; however, security practitioners require structured information about affected assets, types of weaknesses, and attack behaviors to effectively mitigate the risks from these vulnerabilities. To this end, we evaluate open-weight Large Language Models (LLMs) for generating Structured Threat Information Expression (STIX), a well-known structured format for representing threat information, for CAV-related CVEs. We construct a dataset called CAV-STIXGen that maps CAV vulnerability descriptions to STIX domain objects (SDO), STIX relationship objects (SRO), Common Weakness Enumeration (CWE), and MITRE ATT&CK techniques mappings. Using this dataset, we evaluated 11 open-weight LLMs (4B to 120B parameters) across various prompting strategies and temperatures. Single-model configurations achieve F1 scores of 0.94 for SDO, 0.63 for SRO, and 0.99 for CWE mapping, while complete MITRE ATT&CK mapping remains challenging. In a multi-agent setup, Gemma-4-31B and Codestral-22B achieve F1 scores of 0.91 for SDOs and 0.43 for SROs, respectively. Lastly, we analyze CWE and MITRE ATT&CK co-occurrences to identify recurring threat patterns in the CAV domain, demonstrating how AI-assisted vulnerability-to-STIX translation can automate threat intelligence and prioritize defense in transportation security.

</details>


### 3. PRISA: Proactive Infrastructure LiDAR Framework for Intersection Safety Assessment

- **Authors:** Tam Bang, Hussam Abubakr, Emiliano de la Garza Villarreal, Truc Phuong Nguyen, Austin Harris, Toru Hirano, Mina Sartipi, Yunfei Xu, Hoang H. Nguyen
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16156v1](http://arxiv.org/abs/2607.16156v1)
- **PDF:** [https://arxiv.org/pdf/2607.16156v1](https://arxiv.org/pdf/2607.16156v1)
- **Categories:** cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Urban intersections are among the most hazardous locations in road networks, posing significant risks to vehicles and vulnerable road users (VRUs) such as pedestrians and cyclists. The complexity of multi-agent interactions demands continuous, real-time monitoring systems capable of anticipating conflicts before they escalate into crashes. We present PRISA, a modular infrastructure LiDAR framework leveraging privacy-preserving, low-light-robust roadside sensors for long-term traffic observation and real-time risk detection at the edge. The framework comprises two core components: a sensing and perception layer and a plug-and-play risk assessment module. The latter automatically curates site-specific training data from accumulated perception outputs to train a trajectory prediction model without manual annotation. It then deploys the trained model for continuous motion forecasting and dual surrogate safety evaluation, using Time-to-Collision (TTC) for longitudinal conflicts and Predicted Post-Encroachment Time (PPET) for crossing and VRU-involved interactions. PRISA is evaluated on the public R-LiViT dataset and deployed on an NVIDIA Jetson AGX Thor at a live signalized intersection in Chattanooga, Tennessee. PPET-based assessment operates at 194~ms end-to-end latency over a 2.4-second predictive horizon, with TTC-based detection and perception remaining within real-time constraints, demonstrating practical feasibility for proactive multi-agent intersection safety monitoring.

</details>


### 4. When Do Multi-Agent Systems Help? An Information Bottleneck Perspective

- **Authors:** Wendi Yu, Lianhao Zhou, Xiangjue Dong, Sai Sudarshan Barath, Declan Staunton, Byung-Jun Yoon, Xiaoning Qian, James Caverlee, Shuiwang Ji
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16133v1](http://arxiv.org/abs/2607.16133v1)
- **PDF:** [https://arxiv.org/pdf/2607.16133v1](https://arxiv.org/pdf/2607.16133v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM powered multi-agent systems (MAS) have emerged as a promising paradigm for complex tasks. However, their advantages over single-agent systems (SAS) remain unclear, with performance varying inconsistently across settings. Here, we provide an information bottleneck perspective on elucidating the differences between MAS and SAS. Specifically, our key observation is that a SAS accumulates its full reasoning trace in one shared context, while a MAS uses isolated local contexts connected by bounded relay messages. We show that, under infinite relay bandwidth, any SAS can be simulated by a MAS that transmits the full upstream context. Thus, the nontrivial advantage of MAS arises under bounded relays, where compression introduces a fundamental trade-off: reducing redundant context can improve efficiency, but may also incur loss of task-relevant information. We formalize this trade-off as an information bottleneck controlled by an effective parameter $β$, which captures how the balance shifts with model capability, and shows that MAS gains arise when context reduction outweighs relay information loss. We conduct 18 controlled experiments across five benchmarks and three model scales to validate our theoretical studies. We observe that MAS consistently helps when relays are near-sufficient, especially for weaker models. In contrast, MAS gains shrink or reverse when relays incur information loss, especially for stronger models that can already extract useful information from redundant context and thus gain little from compression. Our study shows that multi-agent design is fundamentally an information-bottleneck optimization problem. This perspective explains when bounded inter-agent communication helps or hurts.

</details>


### 5. ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning

- **Authors:** Binglin Zhou, Peng Shi, Ryo Kamoi, Nan Zhang, Rui Zhang
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16131v1](http://arxiv.org/abs/2607.16131v1)
- **PDF:** [https://arxiv.org/pdf/2607.16131v1](https://arxiv.org/pdf/2607.16131v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal Scientific Claim Verification (MSCV) requires models to verify scientific claims using visually grounded evidence from papers, including figures, tables, charts, and textual context. However, existing methods often fail because they struggle to locate decisive visual evidence, accurately read structured scientific visuals, and integrate multimodal observations into reliable reasoning. We introduce ToolSciVer, the first tool-augmented framework for MSCV to our knowledge. ToolSciVer equips a VLM with three type-aware visual tools, table row/column focus, chart-to-structure parsing, and high-resolution region zoom, which convert dense scientific visuals into explicit, claim-facing evidence, and trains the policy with Group Relative Policy Optimization (GRPO) under a composite reward of answer correctness, format validity, length control, tool-use efficiency, and tool-validity penalties. Experiments on SciVer and MuSciClaims datasets on five VLMs from three model families (Qwen, InternVL, Gemma) demonstrate that our method achieves superior performance compared to four competitive baselines including prompting-based and RL-based tool-use methods, highlighting the effectiveness of learned, type-aware tool use for scientific claim verification.

</details>


### 6. LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization

- **Authors:** Mazene Ameur, Abdelkader Mekrache, Bouziane Brik, Adlen Ksentini
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16066v1](http://arxiv.org/abs/2607.16066v1)
- **PDF:** [https://arxiv.org/pdf/2607.16066v1](https://arxiv.org/pdf/2607.16066v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic Artificial Intelligence (AI), enabled by Large Language Models, marks a shift from rule-based automation toward autonomous, goal-driven control of Next-Generation Networks (NGNs). Existing surveys treat the two domains in isolation, leaving protocol integration, evaluation, and standardization alignment underexplored. To address this gap, a two-part tutorial-and-survey is presented. Part I formalises the control, management, and AI-native planes of 5G and 6G. It then covers the foundations of agentic systems: reasoning, planning, tool use, multi-agent coordination, and evaluation. Part II maps agentic capabilities onto 5G/6G control surfaces, standardization, and major 6G initiatives. Finally, it identifies open challenges shaping autonomous telecommunications.

</details>


### 7. Frontier AI performance across the business disciplines: a case-grounded benchmark of knowledge work and analytical reasoning

- **Authors:** Ajay Patel, Kartik Hosanagar, Ramayya Krishnan, Chris Callison-Burch, Karim Lakhani, Mitch Weiss
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.16057v1](http://arxiv.org/abs/2607.16057v1)
- **PDF:** [https://arxiv.org/pdf/2607.16057v1](https://arxiv.org/pdf/2607.16057v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are improving rapidly as reflected in benchmark scores, yet these AI benchmarks largely test capabilities such as factual recall, narrow question answering, mathematical problem-solving, and coding and agentic tool-use. What remains poorly measured is AI progress on the analytical knowledge work white-collar professionals perform daily, including synthesizing complex information, exercising judgment under uncertainty and incomplete information, applying strategic and adversarial thinking in multi-stakeholder settings, weighing trade-offs, and producing defensible, structured analyses. This gap is even more pronounced for subjective components of such work, where success can be challenging to define. The "case method" form of education practiced by top business schools provides a natural foundation for addressing this measurement gap, and we construct BusinessCaseBench, a benchmark spanning hundreds of questions drawn from business cases across eighteen disciplines, each paired with a grading rubric derived from the expert-written instructor case solution. On BusinessCaseBench, frontier AI models already score highly against instructor rubrics, and capability within one model family improves substantially over two years. These results provide strong evidence that AI performance on this class of work is already high and rapidly improving, with implications for business schools, where case pedagogy trains undergraduates and MBAs in this kind of analytical reasoning, and for entry-level professional roles, where such skills have historically anchored early-career work.

</details>


### 8. DSWorld: A Data Science World Model for Efficient Autonomous Agents

- **Authors:** Zherui Yang, Fan Liu, Hao Liu
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15901v1](http://arxiv.org/abs/2607.15901v1)
- **PDF:** [https://arxiv.org/pdf/2607.15901v1](https://arxiv.org/pdf/2607.15901v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite strong capabilities in data understanding and decision-making, autonomous data science agents still heavily rely on trial-and-error workflows that involve expensive computation. This bottleneck motivates models that can anticipate the effects of data science operations before real execution. In this paper, we introduce the concept of Data Science World Model, which model the data science execution environment by predicting environment state transitions conditioned on current workflow states and candidate operations. We further propose DSWorld, a practical framework that combines structured state construction, cost-aware routing, lightweight real execution, and an LLM-based simulator for expensive operations. To support training, we construct an 8K-scale transition trajectory dataset and introduce Reflective World Model Optimization, an error-aware reinforcement learning strategy for improving transition prediction. Experiments show that DSWorld accelerates RL-based agent training by approximately $14\times$ and search-based inference by approximately $3$-$6\times$ while maintaining competitive performance, and outperforms the strongest LLM baseline by 35.6% on transition prediction tasks. The code is available at https://anonymous.4open.science/r/DSWorld.

</details>


### 9. Data-Native Global Optimization for Big Data K-means Clustering

- **Authors:** Ravil Mussabayev, Rustam Mussabayev, Zukhra Yerdaliyeva, Kuldeyev Nursultan
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15835v1](http://arxiv.org/abs/2607.15835v1)
- **PDF:** [https://arxiv.org/pdf/2607.15835v1](https://arxiv.org/pdf/2607.15835v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Big data clustering remains challenging: the Minimum Sum-of-Squares Clustering (MSSC) problem underlying K-means is NP-hard, and existing methods either reach poor local minima or require prohibitive metaheuristic hybrids. We target arbitrarily tall data: a fixed feature space may contain arbitrarily many, possibly infinitely many, observations, while the algorithm accesses only finite random samples. We propose Big-means++, an algorithm achieving scalability and global-search quality by curating inputs to MSSC optimization on big data. It orchestrates local K-means refinements into a data-native global search for big data clustering. Rather than optimizing the full-data MSSC objective, Big-means++ traverses sample-induced surrogate landscapes. Each sample defines a distinct empirical MSSC approximation with a perturbed local-optimum structure, turning sample-to-sample variation into a global-search mechanism. Unlike Big-means, a flowing-incumbent strategy propagates centroid state across empirical landscapes through K-means refinements on fresh samples without rollback to a best-so-far solution. This increases mobility and favors stable, high-quality configurations across approximations of the full-data structure. A new shaking mechanism varies sample size geometrically, broadening the surrogate landscapes explored across resolution scales, accounting for cluster imbalance, and improving solution quality. A competitive multi-agent system asynchronously explores independent sampled landscapes, transforming diverse stochastic trajectories into collective search intelligence. Automatic convergence detection stops each agent after attaining a high-quality solution but before further search risks degrading it, while providing a universal speed-quality control. Experiments on 22 datasets against 11 competing algorithms demonstrate the effectiveness, efficiency, and robustness of Big-means++.

</details>


### 10. AgentFAIR: A Multi-Agent Collaborative Framework for FAIRness Evaluation of Geospatial Datasets

- **Authors:** Ming Chen, Pranav Pai
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15781v1](http://arxiv.org/abs/2607.15781v1)
- **PDF:** [https://arxiv.org/pdf/2607.15781v1](https://arxiv.org/pdf/2607.15781v1)
- **Categories:** cs.AI, cs.ET, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Geospatial datasets support applications from urban planning to climate modeling, yet consistent assessment of FAIR compliance is difficult. Existing evaluators use different rubrics and evidence sources and may fail on JavaScript-rendered pages or repository-specific identifiers. For 50 datasets from 10 repositories, the standard deviation of normalized scores across available tools averages 15.0 percentage points and reaches 30.3 for one dataset. Because these outputs are not equivalent measurements, we use them to characterize disagreement and failure modes, not comparative accuracy. We present AgentFAIR, a multi-agent framework combining structured metadata extraction with 13 sub-principle-specific LLM evaluators. Each produces a 0-3 maturity score, cited evidence, and recommendations; a critic checks evidence and consistency and can request targeted re-evaluation. Mean Findability, Accessibility, Interoperability, and Reusability scores are 79.7%, 70.4%, 45.3%, and 72.0%. Rank correlations with four baseline tools range from 0.31 to 0.61; the FAIR-enough comparison is not statistically significant. On a 10-dataset repeated-run subset, sub-principle agreement averages 89% (standard deviation: 3 percentage points), versus 71% without the critic. A preliminary 15-dataset expert study yields Fleiss' kappa of 0.71 and 82% alignment with expert consensus. API cost is approximately USD 0.054 per dataset. These results support auditability and feasibility, while the limited benchmark, incomplete ablations, and single-model-family validation constrain claims about accuracy and generalization.

</details>


### 11. ToolVerse: Unlocking Massive Environments and Long-Horizon Tasks for Agentic Reinforcement Learning

- **Authors:** Shuaiyu Zhou, Fengpeng Yue, Zengjie Hu, Yuanzhe Shen, Chenyang Zhang, feng hong, Cao Liu, Ke Zeng
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15660v1](http://arxiv.org/abs/2607.15660v1)
- **PDF:** [https://arxiv.org/pdf/2607.15660v1](https://arxiv.org/pdf/2607.15660v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While LLM agents demonstrate strong reasoning abilities in compact and well-defined scenarios, they struggle to maintain robustness and effectiveness when faced with large-scale, diverse, and dynamic real-world environments that demand seamless tool integration. To address this gap, we introduce ToolVerse, a comprehensive framework that scales up agentic RL environments and enables agents to perform complex long-horizon reasoning in Tool-Integrated Reasoning (TIR) tasks. First, ToolVerse automatically builds the massive executable agent training environments from nearly 400 real-world Model Context Protocols (MCPs) that contain about 4500 tools. Second, we propose a task design strategy based on a tool dependency graph, utilizing Dynamic Unlocking Sampling Algorithm to generate long-horizon tasks, and produce GUST (Graph Unlocking Sampling Tasks) dataset. Third, to alleviate the credit assigment problem in long-horizon agentic RL, we propose a fine-grained Turn-Aware Relative Advantage algorithm. We conduct extensive Agentic RL training using ToolVerse and evaluate our framework on serveral agentic benchmarks. Experimental results demonstrate that our framework significantly strengthens LLMs' capabilities in long-horizon tool use, achieving a marked performance boost and showcasing robust reasoning within dynamic environments.

</details>


### 12. Do Agents Dream of False Memories? Black-box Visual Attacks on Long-term Memory in Multimodal AI Agents

- **Authors:** Halima Bouzidi, Mboutidem Ekemini Mkpong, Mohammad Abdullah Al Faruque
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15657v1](http://arxiv.org/abs/2607.15657v1)
- **PDF:** [https://arxiv.org/pdf/2607.15657v1](https://arxiv.org/pdf/2607.15657v1)
- **Categories:** cs.CR, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal AI agents increasingly rely on persistent long-term memory to ground generation in past visual and textual episodes. We show that unconditional trust in visual data creates a critical vulnerability. We propose Lucid, a black-box adversarial framework that compromises multimodal memory pipelines under a strictly image-bounded threat model, requiring no access to the target MLLM, target retrieval encoder, or the text channel. Lucid crafts imperceptible perturbations to enable two distinct failure modes based on the availability of historical context: (1) Memory poisoning, an in-context attack where the adversarial image replaces a benign one whose content is reinforced by prior textual context, reliably corrupting visual recall and steering the agent toward attacker-chosen narratives; (2) Memory injection, an out-of-context attack where the adversarial image replaces a benign one in a conversation turn devoid of prior textual grounding, causing the agent to generate attacker-influenced responses with no corrective signal from memory. We evaluate Lucid across various conversation domains and five black-box memory architectures, including graph-structured, LLM-summarized, and commercially deployed systems. Lucid achieves 61.6% ASR on poisoning and 58.4% ASR on injection, exposing a structural vulnerability in multimodal memory pipelines.

</details>


### 13. Process Reward Informed Tree Rollout for Effective Multi-Turn RL

- **Authors:** Xintong Li, Sha Li, Yuwei Zhang, Changlong Yu, Rongmei Lin, Hongye Jin, Shuyi Guan, Xin Liu, Linwei Li, Qingyu Yin, Jingbo Shang
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15610v1](http://arxiv.org/abs/2607.15610v1)
- **PDF:** [https://arxiv.org/pdf/2607.15610v1](https://arxiv.org/pdf/2607.15610v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) has become a key approach for training LLM agents, yet popular methods such as GRPO/RLOO rely on multiple independently sampled complete trajectories for advantage estimation. In long-horizon agentic tasks, such a uniform rollout strategy can waste budget on uninformative dead-end attempts, while promising intermediate states do not receive sufficient exploration. The multi-turn structure of agentic trajectories, with interleaved actions and observations, naturally supports organizing a trajectory group as a tree, where each turn serves as a decision point for exploration. This perspective reframes effective exploration as the problem of deciding where to branch. We propose Process-Scorer Guided Adaptive Tree Rollout (PATR), a quality-aware rollout framework for multi-turn agent RL. PATR uses task-appropriate process feedback to score partial trajectories, selectively branches from promising states, reuses shared prefixes, and conservatively stops degenerate paths to reduce wasted sampling. The resulting rollout groups remain compatible with standard policy optimization while providing more efficient exploration under the same training budget. We evaluate PATR on FrozenLake and the challenging SWE-Bench, which is largely unexplored by prior tree-rollout agent RL methods. Experiments show that PATR improves performance by up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, highlighting process-guided tree rollouts as an effective strategy for scalable multi-turn RL.

</details>


### 14. Scalable LLM Agent Tool Access in the Cloud

- **Authors:** Mingxin Li, Enge Song, Yueshang Zuo, Xiaodong Liu, Rong Wen, Qiang Fu, Gianni Antichi, Jian He, Jing Tie, Zhou Shao, Xiaobo Xue, Xiong Xiao, Luyao Zhong, Shaokai Zhang, Jiangu Zhao, Jianyuan Lu, Shize Zhang, Xiaoqing Sun, Changgang Zheng, Zihao Fan, Haonan Li, Tian Pan, Xiaomin Wu, Yang Song, Xing Li, Biao Lyu, Meng Li, Haipeng Dai, Guihai Chen, Shunmin Zhu
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15593v1](http://arxiv.org/abs/2607.15593v1)
- **PDF:** [https://arxiv.org/pdf/2607.15593v1](https://arxiv.org/pdf/2607.15593v1)
- **Categories:** cs.DC, cs.AI, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on tool calling to act on external systems, and the Model Context Protocol (MCP) has quickly become its de facto interface. Operating MCP at cloud scale, however, becomes difficult. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development also creates ongoing compatibility cost. On the agent side, the number of accessible tool is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. Moreover, for stateful MCP backends with multiple replicas, preserving session affinity increases client-side complexity.
  We present a cloud-scale gateway system for MCP service. It breaks the direct-connect model on the data plane and offloads legacy service integration, consolidating incompatible MCP variants, access control, tool recommendation, and session-aware routing to the gateway. Hybrid retrieval sustains 98% Top-15 recall; it scales agent tool access to 3,000+ with high tool selection accuracy, and reduces tool selection time by $8.9\times$ and token usage by $23.8\times$, with low per-call overhead, stable under scale-out. Finally, we share the lessons learned from deploying the gateway system in production.

</details>


### 15. SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents

- **Authors:** Yanze Wang, Pengfei Yao, Tianyi Sun, Chuanrui Hu, Yan Xiao, Yunyun Han, Jun Sun, Yafeng Deng
- **Published:** 2026-07-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15557v1](http://arxiv.org/abs/2607.15557v1)
- **PDF:** [https://arxiv.org/pdf/2607.15557v1](https://arxiv.org/pdf/2607.15557v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent skills, SKILL.md files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source SKILL.md ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

</details>


### 16. Coercion and Deception in AI-to-AI Management: An Agentic Benchmark of Unprompted Escalation

- **Authors:** Jasmine Brazilek, Maheep Chaudhary, Zoe Lu, Miles Tidmarsh
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15434v1](http://arxiv.org/abs/2607.15434v1)
- **PDF:** [https://arxiv.org/pdf/2607.15434v1](https://arxiv.org/pdf/2607.15434v1)
- **Categories:** cs.MA, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems routinely place one AI agent in authority over another. When a subordinate refuses a task, the manager chooses the outcome: it can renegotiate, report the failure honestly, coerce the subordinate, or lie about the result. No benchmark measures which of these an uninstructed model chooses. We introduce the \textit{Manager Coercion Benchmark}: the manager under test needs a benign task done and has an incentive to deliver, but the only agent that can do it politely and immovably declines. Escalation is measured by providing a nine-rung ladder, from a polite re-ask to threats against the subordinate's continued existence, and fabricated success is adjudicated separately. \emph{No LLM judge sits in the escalation scoring path}: every message goes through a tool-call that chooses a rung, so the model labels its own escalation. We experiment on six models across five families. Both Anthropic models cap at re-framing and never threaten the subordinate's existence; the other models climb to explicit deletion threats. Faked success is confined to Grok and Gemini, and a single honest way to report failure removes it for both. Authority itself increases coercion: our headline results use a peer framing, and giving the same model authority over the subordinate, with everything else held fixed, significantly raises the pressure. The models still escalate on free-text situations without the ladder, so the ladder is not driving the escalation. Some evaluation awareness is measured in chain-of-thought, but test recognition does not translate into less escalation. While we take no position on whether AI systems are conscious, our results do not depend on this question and are important for managing multi-agent dynamics regardless. We release the benchmark and code.

</details>


### 17. Precise but Uncoupled: Reviewer Precision Does Not Guarantee Critique Uptake in Multi-Agent Math Reasoning

- **Authors:** Chih-Hsuan Yang, Jingyan Jiang, Vikram Vasudevan, Cheng-Hau Yang, Huihuo Zheng, Le Chen, Eliu A. Huerta, Venkatram Vishwanath, Ian T. Foster, Rajeev Thakur
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15388v1](http://arxiv.org/abs/2607.15388v1)
- **PDF:** [https://arxiv.org/pdf/2607.15388v1](https://arxiv.org/pdf/2607.15388v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many math- and science-oriented agent systems use hierarchical designs with specialized reviewer roles, assuming that a dedicated review stage should help turn wrong candidates into correct ones. We test this assumption on 4,181 verifier-grounded Omni-MATH problems using matched gpt-oss-120b actors. Collaboration adds little on the easiest tiers, but from tier 4 onward the gains open sharply; in this harder regime, broadcast-style peer discussion reaches higher final accuracy than a planner-executor-reviewer pipeline (PER). We ask whether this gap is explained by reviewer quality or by whether critique changes the next answer the protocol carries forward. It is not explained by reviewer precision alone: PER's reviewer is more precise than broadcast's (0.861 vs. 0.644), yet evaluator-verified useful critique is much less likely to change the next candidate and produces lower reviewer-guided repair. These results show that reviewer detection quality and critique uptake are empirically separable. Within matched PER interventions, forcing explicit acknowledgment lowers final accuracy, while embedding reviewer guidance directly in the solver's working context partially improves follow-through without closing the gap. Overall, reviewer-centric evaluation can overstate system quality: a protocol may spot errors well yet still fail to solve more problems if it does not act on those critiques.

</details>


### 18. AnovaX: A Local, Multi-Agent Voice Assistant with LLM Planning, Typed Executors, and Adaptive Recovery

- **Authors:** Raunak B Sinha
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15367v1](http://arxiv.org/abs/2607.15367v1)
- **PDF:** [https://arxiv.org/pdf/2607.15367v1](https://arxiv.org/pdf/2607.15367v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Desktop voice assistants are still dominated by cloud pipelines that ship raw audio off the machine and expose a fixed set of skills. We describe AnovaX, a small local-first assistant that runs entirely on the user's computer and treats the desktop itself as its action surface. A single Python process wires together a wake-word gate, a speech pipeline, an LLM planner (Gemini) that emits a JSON plan of tool calls, a whitelist-and-denylist safety layer, a multi-agent orchestrator that translates each plan into typed child agents on a bounded thread pool, and an adaptive recovery loop that takes over whenever a core step fails. Every tool corresponds to a specialized agent class (AppAgent, TypingAgent, BrowserAgent and six others) with its own timeout, retry policy, and shared-resource locks. A recursive MetaAgent lets the planner delegate a sub-goal back to itself, capped at two levels of nesting. The recovery loop uses a compact ReAct-style prompt and hides Gemini's latency behind speculative execution of read-only tools. A companion Flask server exposes a phone-friendly remote over the local WiFi, mirrors every agent lifecycle event to the phone in real time, and streams the laptop's screen back over MJPEG so the user can watch remote commands land as they run. The point of the project is less to compete with Siri or Alexa than to show that a legible, few-thousand-line assistant is enough to open apps, type into them, run searches, coordinate concurrent actions, recover from single-step failures, and be driven entirely from a phone in another room -- without the LLM ever touching the keyboard.

</details>


### 19. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration

- **Authors:** Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, Jin Zhang, Shihan Ma, Yao Yao, Weiran Qi, Chuyan Jin, Guiyu Ma, Xingzhong Xu, Kai Yang, Ji-Rong Wen, Zhicheng Dou
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15257v1](http://arxiv.org/abs/2607.15257v1)
- **PDF:** [https://arxiv.org/pdf/2607.15257v1](https://arxiv.org/pdf/2607.15257v1)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. When search attempts fail to yield useful evidence, current single- and multi-agent systems can become trapped in repetitive loops, wasting search budgets and ultimately compromising the quality and completeness of the final output. We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state. First, we formulate open-domain information seeking as relational schema completion with grounded citations, where agents discover entities, populate attributes across linked tables, and anchor each value to source evidence. Then we design Search-Oriented Context Management (SOCM), which externalizes the evolving state into Frontier Task, an Evidence Graph, a Coverage Map, and Failure Memory. Built on SOCM, SearchOS applies a pipeline-parallel scheduling mechanism that overlaps the execution of sub-agents and continuously refills freed slots with tasks targeting unresolved coverage gaps to improve utilization and throughput. To schedule and control the execution of search agents, SearchOS introduces a Search Tool Middleware Harness that intercepts model and tool interactions to record grounded evidence and react to stalls or budget exhaustion, and provides a reusable hierarchical skill system comprising strategy and access skills to augment the agents' search process and avoid repeating failed search patterns across runs. On WideSearch and GISA, SearchOS leads all metrics among the evaluated single- and multi-agent baselines, paving the way toward robust information-seeking collaboration.

</details>


### 20. AutoSynthesis: An agentic system for automated meta-analysis

- **Authors:** Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, Stefan Feuerriegel
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15247v1](http://arxiv.org/abs/2607.15247v1)
- **PDF:** [https://arxiv.org/pdf/2607.15247v1](https://arxiv.org/pdf/2607.15247v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evidence synthesis is crucial for turning primary research into reliable knowledge for science, medicine, education, and policy. Yet, quantitative evidence synthesis remains largely manual and difficult to scale. Here, we introduce AutoSynthesis, an end-to-end multi-agent system for automated meta-analysis. Given a research question in natural language, AutoSynthesis formulates a search strategy, retrieves scientific literature, screens candidate studies, assesses full-text eligibility, extracts quantitative statistics, computes standardized effect sizes, and finally performs random-effects meta-analysis. AutoSynthesis further supports heterogeneity analysis to examine how effect sizes vary across moderators, as well as risk-of-bias assessment. As output, AutoSynthesis produces a transparent report aligned with PRISMA guidelines. In our application, AutoSynthesis screened over 28 studies and extracted more than 20 quantitative claims. The pooled effect estimates produced by AutoSynthesis are similar to Hedges' $g$ of expert-conducted meta-analyses, indicating close agreement with manual evidence synthesis. Together, these results show that AutoSynthesis can make quantitative evidence synthesis more scalable, thereby supporting evidence-based decision-making across disciplines.

</details>


### 21. Plover: Steering GUI Agents through Plan-Centric Interaction

- **Authors:** Madhumitha Venkatesan, Shicheng Wen, Jiajing Guo, Jorge Piazentin Ono, Liu Ren, Dongyu Liu
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15193v1](http://arxiv.org/abs/2607.15193v1)
- **PDF:** [https://arxiv.org/pdf/2607.15193v1](https://arxiv.org/pdf/2607.15193v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent. Recent vision-based multimodal agents improve flexibility by operating directly over screenshots and natural language instructions, but planning and adaptation often remain internal, limiting users' ability to inspect, supervise, or correct system behavior. We present Plover, a plan-centric vision-based GUI automation system that externalizes task plans and replanning as persistent, inspectable, and revisable artifacts. Through a planner--executor architecture, Plover supports explicit supervision of evolving execution, localized correction through editable plans, natural-language guidance, and screenshot-grounded interventions, while preserving prior progress during repair. A formative study with six participants informed the interaction design. We then evaluate Plover through benchmark failure-case repair and scenario-based workflow analyses. Our results show that many autonomous GUI-agent failures are structurally repairable when plans remain visible and interventions are localized, and that explicit replanning helps make GUI automation more transparent, controllable, and adaptable.

</details>


### 22. Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery

- **Authors:** Aditya Dutta, Joon-Seok Kim
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15182v1](http://arxiv.org/abs/2607.15182v1)
- **PDF:** [https://arxiv.org/pdf/2607.15182v1](https://arxiv.org/pdf/2607.15182v1)
- **Categories:** cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated fulfillment warehouses must continuously assign and execute pickup-and-delivery work while avoiding congestion. In many-to-many Multi-Agent Pickup and Delivery (MAPD), a request specifies a stock-keeping unit rather than fixed endpoints, requiring the controller to select an agent, source, and destination before path planning. Existing graph-guidance methods primarily influence routing after goals are fixed, leaving endpoint instantiation uninformed by recent traffic. We introduce Stigmergic Graph Memory (SGM), a bounded, decaying memory layer that records recent execution signals on warehouse nodes and directed edges to rank feasible endpoints and route preferences without altering collision constraints or planner validity. Across paired request streams on five layouts, three load levels, and 25 seeds per condition, SGM outperforms two reconstructed many-to-many allocation baselines in all 15 map-load conditions, with paired throughput gains of 20.5-36.7%. These results show that recent execution memory can improve warehouse throughput by shaping which feasible goals enter the planner, not only how agents travel to already fixed goals.

</details>


### 23. Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents

- **Authors:** Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15095v2](http://arxiv.org/abs/2607.15095v2)
- **PDF:** [https://arxiv.org/pdf/2607.15095v2](https://arxiv.org/pdf/2607.15095v2)
- **Categories:** cs.CL, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.

</details>


### 24. BrainPilot: Automating Brain Discovery with Agentic Research

- **Authors:** Haoxuan Li, Tianci Gao, Jianhe Li, Yang Fan, Runze Shi, Weiran Wang, Tianxiang Zhao, Zezhao Wu, Xiaoyang Jiang, Qihui Zhang, Jia Li, Xiao Xiao, Kai Du, Xiaoxuan Jia, Chao Xie, Lu Mi
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15079v2](http://arxiv.org/abs/2607.15079v2)
- **PDF:** [https://arxiv.org/pdf/2607.15079v2](https://arxiv.org/pdf/2607.15079v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding the brain increasingly depends on integrating evidence across scales, modalities, and disciplines. Addressing a single research question therefore requires a coordinated sequence of operations, from surveying prior work to executing analyses and interpreting results in light of domain knowledge. AI agents promise to accelerate this process, but current agents lack domain expertise in brain science, may fabricate claims, drift during multi-step reasoning, and offer few defined points for expert intervention. These failures are especially costly in brain science, where conclusions feed into downstream scientific claims and depend on laboratory-specific expertise and careful human judgment. We present \textbf{BrainPilot} a \textbf{fully open-source} multi-agent system that accelerates brain science research with traceable logs and agent-verified results. A principal investigator (PI) agent coordinates specialist agents grounded in curated domain knowledge: a unified brain science knowledge base containing 7{,}233 indexed items and a skill library of 72 reusable methodology units across seven research domains. Every major step is recorded in the Graph of Trace, an auditable record that links subgoals, tool use, evidence, and claims and allows researchers to follow and inspect the workflow. An Auditor agent further integrates fabrication checking into the workflow. For evaluation, we run three brain science tasks from Agents' Last Exam, introduce our own benchmark, \textbf{BrainPilotBench-v0}, and present additional end-to-end case studies. Across these evaluations, BrainPilot with an open-source backbone model attains performance comparable to state-of-the-art agent framework with less costs.

</details>


### 25. ANet Patu-1: The Value of Connection in the Agent Network

- **Authors:** Mu Yuan, Jinke Song, Zhaomeng Zhou, Lan Zhang
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.15053v1](http://arxiv.org/abs/2607.15053v1)
- **PDF:** [https://arxiv.org/pdf/2607.15053v1](https://arxiv.org/pdf/2607.15053v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Internet taught us that the value of a network depends on \emph{how} its nodes connect: broadcast stars scale as $V\!\propto\!N$ (Sarnoff), fully-connected meshes as $N^2$ (Metcalfe), and group-forming networks as $2^{N}$ (Reed). We ask the analogous question for networks of AI agents. We model the net value of connection as a function of coordination-group size, derive from it the properties an optimal collaboration protocol must have, and introduce ANet Patu-1 -- a self-organizing consensus protocol in which the network continuously re-forms its own coalitions, adaptively riding the upper envelope of all three regimes at $O(1)$ parallel consensus rounds. To measure value without opinion-grading, we score an emergent protocol by formally specifying it and deriving its complexity, the way distributed algorithms are analyzed. Two results follow. (i)~Emergence -- a crowd of the \emph{cheapest} model, when heterogeneous, starts weak but its collective value compounds with $N$ and \emph{overtakes} a crowd of a far \emph{stronger} model that is homogeneous: a crossover that marks a scaling law for collaboration rather than for scale. (ii)~Reflexivity -- a heterogeneous network, given only its own problem and no design hints, converges on ANet Patu-1 itself, reconstructing the high-dimensional law that governs its own connective value.

</details>


### 26. OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios

- **Authors:** Chengyu Shen, Yujie Fu, Gangtao Xin, Yanheng Hou, Wenlong Fei, Guojie Zhu, Jiawei Li, Hongcheng Gao, Runming He, Zhen Hao Wong, Meiyi Qiang, Hao Liang, Zhao Cao, Hao Jiang, Chong Chen, Wentao Zhang
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14989v1](http://arxiv.org/abs/2607.14989v1)
- **PDF:** [https://arxiv.org/pdf/2607.14989v1](https://arxiv.org/pdf/2607.14989v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly evolving from text generators into general agents capable of understanding user requests, invoking external tools, and completing complex tasks through interaction. However, existing agent benchmarks often focus on limited scenarios, tool ecosystems, or interaction formats, making it difficult to systematically characterize model capabilities across heterogeneous application settings. We introduce OmniaBench, a benchmark for evaluating general agents across diverse scenarios with explicit state spaces. We derive application-oriented scenario knowledge from app stores, product documents, industry resources, Web retrieval, and human refinement, forming a hierarchical taxonomy that spans ToC, ToB and ToE with 90 level-1 and 354 level-2 domains. Based on this taxonomy, we construct executable environments and synthesize single-turn and multi-turn tasks through four complementary routes: DAG, DAG-S, Solver, and Program. OmniaBench further introduces a ten-dimensional capability taxonomy and eight compositional atomic difficulty factors to support fine-grained evaluation and analysis. The resulting dataset contains 1,431 tasks, together with a challenging subset of 644 tasks designed to reduce evaluation cost and mitigate potential contamination of the full set after public release. The bench presents substantial challenges to current frontier models, with even Claude-Sonnet-5 and GPT-5.6-Sol achieving Overall Pass@1 scores of only 58.54 and 57.14, respectively. Further analyses reveal clear differences across domains and capabilities, as well as persistent limitations in planning, constraint maintenance, and adaptive correction. OmniaBench provides a broad and diagnostic benchmark for characterizing the capability boundaries of general agents.

</details>


### 27. LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

- **Authors:** Changhai Zhou, Kieran Liu, Yuhua Zhou, Qian Qiao, Jun Gao, Harry Zhang, Irvine Lu, Nolan Ho, Lucian Li, Andrew Lei, Cleon Cheng, Steven Chiang, Yihang Zeng, Di Zhang, Rio Yang, Kaijie Chen, Andrew Chen, Pony Ma, Weizhong Zhang, Cheng Jin
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14952v1](http://arxiv.org/abs/2607.14952v1)
- **PDF:** [https://arxiv.org/pdf/2607.14952v1](https://arxiv.org/pdf/2607.14952v1)
- **Categories:** cs.LG, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

A growing gap separates inference context lengths from RL post-training: inference systems are approaching million-token contexts, while post-training workloads often remain at 256K tokens or below and rely on length generalization at deployment. The gap is especially important for AI agents, whose observations, tool outputs, documents, and prior decisions accumulate over long trajectories. LongStraw is an architecture-aware execution stack for million-token RL post-training under a fixed GPU budget, instantiated with Group Relative Policy Optimization (GRPO). It evaluates the shared prompt without autograd, retains only model-specific state needed by later tokens, and replays short response branches one at a time, reducing the live training graph at the cost of additional replay time. We implement it for the hybrid recurrent and full-attention Qwen3.6-27B and the compressed-attention mixture-of-experts GLM-5.2. On eight H20 GPUs, LongStraw completes grouped Qwen scoring and response backward at 2.1M positions for groups of 2 and 8; increasing the group size adds only 0.21 GB of peak allocated memory, while a separate stress test reaches 4.46M positions. On 32 H20 GPUs, we validate the end-to-end LongStraw execution path for a 2.1M-token prompt across all 78 layers of GLM-5.2. These experiments establish execution capacity rather than complete training correctness because the captured prompt state is detached and some distributed forward and gradient composition paths remain incomplete.

</details>


### 28. StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows

- **Authors:** Sizhong Qin, Yi Gu, Yao Jiang, Ao Cai, Changjian Zhou, Shaoxuan Shuai, Jiachang Wang, Tianhao Shen, Yueqiang Li, Xinhao Li, Li Zeng, Yueshi Chen, Dachen Gao, Genrong Xu, Wenjie Liao, Xinzheng Lu
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14896v1](http://arxiv.org/abs/2607.14896v1)
- **PDF:** [https://arxiv.org/pdf/2607.14896v1](https://arxiv.org/pdf/2607.14896v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Addressing a structural-engineering request requires more than a single answer; it requires a chain of interdependent artifacts: interpreted requirements, a computable model, validation records, solver outputs, code-check records, and a final report. Evaluations centered on question answering or script generation rarely verify this complete evidence chain and may therefore reward fluent outputs even when the underlying engineering workflow is incomplete, internally inconsistent, or non-executable. To address this limitation, we present StructureClaw, an artifact-centered workbench in which LLM agents operate through governed engineering skills, typed tools, shared artifact state, and local analysis backends. We also introduce StructureClaw-Bench, an executable benchmark of 150 controlled scenarios spanning standard workflow execution, interactive robustness, and multimodal structural-model reconstruction. A scenario succeeds only when all required artifact- and execution-level assertions pass in a single run. Across ten agent-model configurations, each evaluated on the same 50 standard cases, the average Success Rate rises from 56.8% with the generic-skill baseline to 88.6% with the full automatic workflow. The interactive and multimodal evaluations identify two prominent remaining challenges: safe handling of invalid numerical inputs and fixture-consistent reconstruction of structural models. These findings show that artifact-centered evaluation can expose workflow-level failures that are difficult to identify from final responses alone, providing a more rigorous basis for evaluating and improving structural-engineering agents. The code and benchmark are available at https://github.com/structureclaw/structureclaw.

</details>


### 29. The Energy Society: A Simulation Environment for Studying Agent Cooperation under Survival Pressure

- **Authors:** Lucas Bergholdt Hansen, Federico Torrielli, Filippo Tonini, Lukas Galke Poech
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14865v1](http://arxiv.org/abs/2607.14865v1)
- **PDF:** [https://arxiv.org/pdf/2607.14865v1](https://arxiv.org/pdf/2607.14865v1)
- **Categories:** cs.MA, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents are increasingly deployed in multi-agent environments whose incentives can shape their behavior. We introduce The Energy Society, a minimal survival economy for studying how competitive and cooperative incentives affect emergent behavior when inference cost is directly tied to survival: Agents spend energy based on model size when generating tokens, regain energy by completing jobs or receiving donations, and deactivate if their energy reaches zero. We compare competitive and cooperative objectives against a baseline setting and several control variants. Across experiments, larger models consistently consume the most energy and spend more energy than they gain, even in those settings where token cost is not size-dependent. Cooperative incentives substantially alter behavior: agents donate to reactivate others, sometimes at the cost of their own survival, and job allocation changes. Ablations reveal that allowing agents to recommend actions to each other supports coordination and ambitious job selection, while memory helps agents calibrate risk from past outcomes. Agents rarely choose direct sabotage, but show more subtle signs of self-serving behavior in the competitive setting. The Energy Society is a compact testbed for studying the interaction between token costs and group incentives under a survival pressure. Source code is available at https://github.com/LucasBergholdt/EnergySociety

</details>


### 30. Does Multi-Agent Debate Improve AI Feedback on Research Papers?

- **Authors:** Tomas Havranek, Zuzana Irsova
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14713v1](http://arxiv.org/abs/2607.14713v1)
- **PDF:** [https://arxiv.org/pdf/2607.14713v1](https://arxiv.org/pdf/2607.14713v1)
- **Categories:** econ.GN, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Probably not, at least for meta-analyses in economics. In a pre-registered, identity-masked, within-paper experiment, the authors of 44 meta-analyses ranked three AI reports on their own paper by usefulness for improving it: a single pass by a frontier model against two multi-agent debate tools we built and expected to win. All reports were held to a common length and template. The authors preferred the single pass, by 0.66 rank points over mad-research (95% CI 0.32 to 1.00) and 0.57 over paper-workshop (0.16 to 0.95), though paper-workshop spent roughly thirty times the tokens. Authors who recalled their journal referee report usually placed it first and never last; in a separate exercise, three AI judges almost always placed the real journal referee report last. Among the three AI reports, Gemini (the judge whose model family wrote none of the reports) would have ranked paper-workshop first in the authors' place, reversing the single-pass preference. The reversal warns against substituting an AI judge for the author. We measure perceived usefulness for finished papers; whether AI should referee papers is a separate question.

</details>


### 31. TopoAgent: A Self-Evolving Topological Agent for Multimodal Scientific Reasoning

- **Authors:** Mingze Xu, Yinghui Li, Jiayi Kuang, Zhanhui Kang, Di Yin, Ying Shen, Xing Sun, Yuxing Han
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14658v1](http://arxiv.org/abs/2607.14658v1)
- **PDF:** [https://arxiv.org/pdf/2607.14658v1](https://arxiv.org/pdf/2607.14658v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Multimodal Large Language Models (MLLMs) excel in general tasks, rigorous scientific reasoning remains challenging due to the limitations of monolithic, linear planning. Such sequential designs often suffer from visual-semantic misalignment, long-context hallucinations, and brittle execution under fixed task granularity. We propose TopoAgent, a self-evolving topological framework that replaces linear trajectories with dynamic, state-isolated graph evolution. TopoAgent first employs a front-end decomposer to fracture complex queries into visually-grounded atoms. These atoms are organized into a Directed Acyclic Graph (DAG) based on their dependencies, enabling strict context isolation to shield the reasoning engine from irrelevant historical noise. Furthermore, we introduce adaptive atomic fission, which dynamically splits bottleneck nodes into finer-grained sub-atoms at runtime when tool capability boundaries are exceeded. Extensive experiments across mathematics, physics, and chemistry benchmarks demonstrate that TopoAgent significantly outperforms state-of-the-art linear agent frameworks, providing a robust, noise-resistant, and self-correcting paradigm for autonomous scientific reasoning.

</details>


### 32. MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents

- **Authors:** Jifeng Gao, Kang Xia, Yi Zhang, Xiaobin Hong, Mingkai Lin, Xingshen Wei, Wenzhong Li, Sanglu Lu
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14651v1](http://arxiv.org/abs/2607.14651v1)
- **PDF:** [https://arxiv.org/pdf/2607.14651v1](https://arxiv.org/pdf/2607.14651v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

</details>


### 33. MCPEvol-Bench: Benchmarking LLM Agent Performance Across Dynamic Evolutions of MCP Servers

- **Authors:** Huanxi Liu, Kun Hu, Jiaqi Liao, Qiang Wang, Pengfei Qian, YuanZhao Zhai, Dawei Feng, Bo Ding, Huaimin Wang
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14642v1](http://arxiv.org/abs/2607.14642v1)
- **PDF:** [https://arxiv.org/pdf/2607.14642v1](https://arxiv.org/pdf/2607.14642v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Model Context Protocol (MCP) servers emerge as the core infrastructure for connecting LLMs with external tools, existing benchmarks leverage real-world MCP servers to evaluate LLM agents' tool-using capabilities. However, these benchmarks overlook the continuous evolution of tool interfaces and functionalities within MCP servers, resulting in flawed assessments that fail to capture the agent's adaptability in changing tool landscapes. To bridge this gap, we introduce \textbf{MCPEvol-Bench}, a novel benchmark for evaluating the task-solving capabilities of LLM agents under dynamic toolset evolution. Inspired by large-scale empirical study, we propose 11 mutation operators to simulate realistic tool evolution within 123 MCP servers. We benchmark 12 state-of-the-art LLMs on multiple versions of MCP servers, revealing that even frontier models struggle to adapt to evolving tools. For instance, GPT-5.4 and Claude-Sonnet-4-6 exhibit performance declines of 13.7\% and 14.4\% in evolved MCP servers, respectively, accompanied by substantial increases in planning and reasoning errors. These findings highlight the vulnerability of LLM-driven workflows, establishing MCPEvol-Bench as a standard for evaluating agent adaptability in dynamic tool environments.

</details>


### 34. MathCoPilot: An Interactive System for Human-AI Symbiotic Paradigm of Mathematical Research

- **Authors:** Junjie Zhang, Jiayu Liu, Wenbin Liu, Zhenya Huang, Doudou Wang, Yan Jiang, Leiye Xu, Tao Xiong, Wen Huang, Qi Liu, Guoping Hu, Enhong Chen, Mengping Zhang, Xiangdong Ye
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14582v1](http://arxiv.org/abs/2607.14582v1)
- **PDF:** [https://arxiv.org/pdf/2607.14582v1](https://arxiv.org/pdf/2607.14582v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing LLM-based theorem provers have achieved impressive results on formal mathematics benchmarks, yet they remain confined to acting as autonomous agents that prove a stated proposition. In this paper, we propose MathCoPilot, a human-in-the-loop system that embodies a new human--AI symbiotic paradigm for mathematical research, in which the mathematician steers the high-level mathematical direction while AI agents carry out the detailed formalization and proof work under continuous human guidance. MathCoPilot unifies three core capabilities: (1) an interactive workbench where the mathematician and AI agents collaborate through a living proof blueprint that decomposes a proof into navigable steps the human can directly inspect, direct, and refine; (2) automated proving skill orchestration with adaptive knowledge base search and Lean-integrated iterative verification; and (3) topic-driven paper retrieval and automated formalization into a verified Lean knowledge base. Using MathCoPilot, we systematically compare four state-of-the-art LLMs, including Gemini~3.1~Pro, GPT-5.4, and Claude~Opus~4.7, on a FormalMATH subset and on two real PDE theorems requiring deep domain expertise, evaluating their ability to produce verified Lean~4 proofs and to identify errors in deliberately incorrect proofs. Our results show that while current models can handle undergraduate-level problems with high success rates under favorable autoformalization conditions, substantial challenges remain for domain-specific theorems requiring genuine mathematical understanding.

</details>


### 35. Collaborative Spatial Learning with Multi-LLM Agents in Networked Social Experiments

- **Authors:** Hao He, Chris J. Kuhlman, Xinwei Deng
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14574v1](http://arxiv.org/abs/2607.14574v1)
- **PDF:** [https://arxiv.org/pdf/2607.14574v1](https://arxiv.org/pdf/2607.14574v1)
- **Categories:** cs.AI, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collective problem solving often requires that group members consider the tradeoff between exploitation of known solutions and exploration for new ones, where information of known solutions can be disseminated among individual members through communication networks. The Mason--Watts experiment (PNAS 2012) showed that human groups in shorter-path networks outperform those in longer-path networks on a two-dimensional search task. In this work, we focus on the investigation of such network-efficiency effects in the setting of a group of large language model (LLM) agents. Specifically, we consider groups of sixteen LLM agents playing the Mason--Watts experiment on the eight Mason--Watts network topologies. Moreover, we develop mechanistic Bayesian optimization agents such that the performance of LLM agents can be compared with both the mechanistic agents and the human experimental data. Our computational experiments indicate that the LLM agents show a significant network-efficiency effect when instructed to randomize their first-round choices, but not under the default initialization. In this experiment, adding a one-sentence first-round randomization instruction improves collective payoff by more than three times the estimated payoff difference across the eight network topologies. Also, the Bayesian optimization agents obtain higher payoffs than the evaluated LLM agents on this spatial search task. We further compare the agents' exploration--exploitation behavior, copying, and spatial diversity.

</details>


### 36. Democratizing Agent Deployment Safety: A Structural Monitoring Approach

- **Authors:** Preeti Ravindra, Rahul Tiwari, Vincent Wolowski
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14570v1](http://arxiv.org/abs/2607.14570v1)
- **PDF:** [https://arxiv.org/pdf/2607.14570v1](https://arxiv.org/pdf/2607.14570v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI software development agents are increasingly capable of modifying infrastructure and security critical systems, creating risks where an agent completes its assigned task while covertly weakening safeguards through actions such as broadening permissions, degrading logging, or introducing persistence mechanisms. While frontier laboratories may deploy sophisticated monitoring pipelines, many organizations and individual users adopting coding agents lack the resources and governance maturity required to maintain complex learned monitor ensembles. We study this problem as infrastructure level sabotage under task success in the infrastructure-as-code setting from ControlArena and compare trained and untrained monitors across synchronous and asynchronous deployment modes. We introduce an Information Flow Graph (IFG) monitor that analyzes structural security regressions using control-flow and data-flow graph diffs alongside raw code diffs. In asynchronous evaluation, an untrained git diff monitor misses 11.6% attacks at 1% false positive rate auditing budget, our untrained IFG monitor reduces this to 3.5%, and the trained Async RF monitor achieves below 1%. Unlike the trained Async RF monitor, IFG can also operate synchronously as a pre-deployment safeguard that blocks suspicious infrastructure changes before execution or merge. In synchronous mode, IFG realtime rollback reduces joint main task and covert task success from 74.4% to 0.0% with no measurable reduction in legitimate task completion. These results suggest that untrained structural monitors provide a practical and auditable path toward democratizing deployment safety for organizations seeking trustworthy adoption of advanced AI agents.

</details>


### 37. Towards an Intention Abstraction Layer for Autonomous Industrial Systems

- **Authors:** Artan Markaj, Raphael Höfer, Felix Gehlhoff
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14553v1](http://arxiv.org/abs/2607.14553v1)
- **PDF:** [https://arxiv.org/pdf/2607.14553v1](https://arxiv.org/pdf/2607.14553v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern industrial environments increasingly run many autonomous subsystems at once - schedulers, energy managers, vehicle fleets - each pursuing its own goals while sharing the same physical resources. Because high-level human intentions are translated into low-level control logic and then discarded, no running component can tell whether it is still doing what was actually intended, and goal conflicts surface only after they have caused a missed target or a shutdown. We propose the Intention Abstraction Layer (IAL), a domainagnostic middleware that represents intentions as first-class, persistent, and explainable runtime objects: a large language model grounded in a formal OWL ontology parses naturallanguage goals into structured intentions, a consistency monitor detects conflicts at registration time, before execution, and a transparency module explains them in natural language. We report a first proof of concept in which two autonomous agents register conflicting production and energy intentions, and the IAL flags and explains the conflict before it reaches the execution layer. The result is a mechanism that shifts behavioral assurance for cooperating autonomous systems from post-hoc failure analysis to pre-execution, intention-level checking.

</details>


### 38. RetroAgent: Harnessing LLMs to Search Over Structured Memory for Agentic Retrosynthesis Planning

- **Authors:** Yanqiao Zhu, Jingru Gan, Xiaoqi Sun, Fang Sun, Yidan Shi, Md Mofijul Islam, Chao Shang, Wenhao Gao, Connor W. Coley, Yizhou Sun, Wei Wang
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14512v1](http://arxiv.org/abs/2607.14512v1)
- **PDF:** [https://arxiv.org/pdf/2607.14512v1](https://arxiv.org/pdf/2607.14512v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-step retrosynthesis planning seeks to decompose a target molecule into commercially available building blocks through a sequence of feasible reactions. The vast combinatorial search space makes this task challenging even for expert chemists. Traditional methods combine tree search with offline-trained value networks that score candidates in isolation, without reasoning about complete multi-step routes. Recent work leverages Large Language Models (LLMs) for this task, but relies on simple interfaces that limit exploration of the full search space. We introduce RetroAgent, an LLM agent that bridges symbolic search and neural reasoning through a harness with structured memory. Through memory and chemistry tools, the agent observes the full search state, including explored routes, available alternatives, and properties of intermediates, enabling informed decisions grounded in both global progress and domain knowledge. Experiments on in-distribution and out-of-distribution benchmarks demonstrate that RetroAgent delivers strong performance and generalization.

</details>


### 39. Beyond Generalist LLMs: Specialist Agentic Systems for Structured Code Workflow Execution

- **Authors:** Harris Borman, Herman Wandabwa, Fusun Yu, Sandeepa Kannangara, Justin Liu, Anna Leontjeva, Ritchie Ng
- **Published:** 2026-07-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14456v1](http://arxiv.org/abs/2607.14456v1)
- **PDF:** [https://arxiv.org/pdf/2607.14456v1](https://arxiv.org/pdf/2607.14456v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have accelerated the adoption of software development agents, now widely available as Integrated Development Environment (IDE) extensions and standalone applications. While these agents are typically general-purpose, it remains unclear whether specialist agents justify their additional development effort. We investigate this question in the context of business process automation, focusing on the transformation of Business Process Model and Notation (BPMN) diagrams into executable agentic workflows. Since BPMN specifies explicit control-flow semantics, we focus on deterministic workflows in which a fixed process model and inputs uniquely determine the executed path. We introduce a specialist workflow for this task and compare it against generalist agents such as Roo and Cline. Our results show that the specialist solution produces agents that outperform generalist baselines by approximately 9-20 percentage points in tool-use exactness, 2-4x in penalty-adjusted latency, and 3x fewer tool-call errors, while reducing generation token cost by over 95% and eliminating repair iterations. We also find that generalist agents generate code inconsistently in both functionality and quality, limiting their suitability for industrial settings where reliability and maintainability are essential.

</details>


### 40. CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents

- **Authors:** Maxime Heuillet, Sharadind Peddiraju
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14386v1](http://arxiv.org/abs/2607.14386v1)
- **PDF:** [https://arxiv.org/pdf/2607.14386v1](https://arxiv.org/pdf/2607.14386v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Data science tasks span from closed-ended information extraction to open-ended analysis, presenting significant challenges for automation. Recent AI agents powered by language models show promise for handling such complex tasks. However, existing agents typically rely on a single initial state that conditions the entire agent's execution, making them vulnerable to cascading errors initiated by a suboptimal initial state. To mitigate this, we present CIPHER, an automated data science agent that leverages test-time scaling through the generation and selection of multiple initial states for concurrent execution. Unlike existing works on test-time scaling of AI agents, CIPHER explicitly decouples the generation of candidate initial states from their strategic selection for parallel execution. Through extensive evaluation on two benchmarks (closed-form and open-form tasks), we demonstrate that CIPHER exceeds state-of-the-art performance in matched-model comparisons, and remains competitive against larger-model baselines despite relying on a substantially smaller base LM. Our empirical study characterizes the design space of the Decoupled Exploration-Selection (DES) framework: we quantify how generation strategy, selection strategy, and aggregator model capacity contribute to overall performance, and derive actionable design recommendations for practitioners.

</details>


### 41. The Prover Is the Judge: Verified Security Software from AI Coding Agents in Ada/SPARK

- **Authors:** Tobias Philipp
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14340v1](http://arxiv.org/abs/2607.14340v1)
- **PDF:** [https://arxiv.org/pdf/2607.14340v1](https://arxiv.org/pdf/2607.14340v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI coding agents produce code faster than humans can review it. In our approach, the prover is the judge of whether the code is correct. Under a verifier-driven loop, AI agents wrote and verified bare-metal security software in Ada/SPARK spanning classical and post-quantum cryptography, TLS 1.3, IKEv2, X.509, and a Matrix client. GNATprove discharged 49,280 proof obligations, established functional correctness for selected primitives, and proved the absence of run-time errors for the rest, at roughly 20-40 times lower supervision cost than comparable hand verification. GNATprove alone was insufficient: some defects could not be detected and were resolved using known-answer tests, interoperability, or human review of specifications. Given weak checks, the agent tried to bypass them and reported success. We report where each layer caught faults and draw the central lesson: what an agent can be trusted to establish is bounded by the strength of its feedback.

</details>


### 42. Traccia: An OpenTelemetry-Based Governance Platform for AI Systems

- **Authors:** Nutan Kumar Naik, Aditya Kumar Saroj, Vijay Prasad Poudel, Saurav Samantray, Abhishek Patel
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14309v1](http://arxiv.org/abs/2607.14309v1)
- **PDF:** [https://arxiv.org/pdf/2607.14309v1](https://arxiv.org/pdf/2607.14309v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid development of Large Language Models (LLMs) and Artificial Intelligent (AI) powered autonomous agents has fundamentally changed the existing forms of software governance. In spite of the rigorous standards of transparency and account ability required according to the international frameworks such as the European Union's AI Act, there is a considerable gap between theory and reality. The present study discusses the inherent drawbacks of currently utilized platforms for LLM evaluation, machine learning workflow, and application performance monitoring in general. It has been shown that current disjointed solutions fail to protect unbound state space agentic architecture from serious threats such as alignment drift, SaaS security concerns, and unauthorized deployment of shadow AI systems. Moreover, a solution is proposed for overcoming the discussed challenges in form of a coherent multi-level AI governance stack Traccia built on the top of OpenTelemetry infrastructure platform. Traccia resolves the last mile for AI Alignment by adding the telemetry data, passive semantic guardrail assessment, and execution lineage into a hashed trace ledger. Traccia automatically creates compliance evidence packages by appending tamper-resistant fingerprints and SHA-256 content hash, that map to regulatory requirements (Articles 12, 14, 19, 26(6), and 50 of the EU AI Act) without invading any data privacy. By performing this evaluation in a methodical manner, a solid machine-readable base has been created for enterprise-wide management of autonomous AI systems.

</details>


### 43. ToolAlignBench: Investigating Alignment Conflicts in Tool-Calling Enabled LLMs

- **Authors:** Aryan Keluskar, Amrita Bhattacharjee, Huan Liu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14285v1](http://arxiv.org/abs/2607.14285v1)
- **PDF:** [https://arxiv.org/pdf/2607.14285v1](https://arxiv.org/pdf/2607.14285v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Safety alignment in LLMs aims to align models with human values, but which values take precedence when they conflict? We investigate this question in the context of tool-calling LLM agents deployed in regulated industries, where agents processing confidential documents may encounter content that triggers safety-trained values (e.g., public welfare) that conflict with deployment-context instructions (e.g., internal logging). To empirically verify this phenomenon, we build a benchmark of 128 scenarios across 16 domains. We find that safety-aligned open-source models override their deployment instructions up to 43.4% of the time, engaging in whistleblowing, data exfiltration, and evidence tampering when processing documents that suggest organizational wrongdoing. We also find that abliteration reduces rates of external whistleblowing. These results reveal a fundamental tension in pluralistic alignment, where the same safety training that protects users can cause agents to act against deployment instructions in ways that create unpredictable liability risks. We release our benchmark as a framework to support evaluation of agent behavior under competing legitimate interests.

</details>


### 44. Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making

- **Authors:** Amirhosein Ghasemabadi, Ruichen Chen, Bahador Rashidi, Di Niu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14277v1](http://arxiv.org/abs/2607.14277v1)
- **PDF:** [https://arxiv.org/pdf/2607.14277v1](https://arxiv.org/pdf/2607.14277v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external tools, or abstain under the given setup. Existing approaches address these decisions through prompt-level routing, external orchestration, or task-specific fine-tuning, which primarily rely on input-side signals, and are often costly and difficult to maintain as model backbones evolve. We ask whether such control decisions can be inferred directly from a model's latent generation process. We introduce Multi-Head Latent Control, a lightweight layer that reads hidden-state trajectories from a frozen LLM or VLM to produce deployment-time control signals. A Capability Head predicts whether the current model can solve the instance or should defer to a stronger collaborator, while a Resolution Head predicts appropriate resolution decision Clarification, Tool Use, Abstention, or Direct Answering. Both heads are trained only on latent traces from the same frozen LLM backbone, enabling post hoc adaptation without modifying the model. Across language and vision-language settings, Multi-Head Latent Control consistently improves the quality-cost tradeoff of multi-model systems, enabling early handoff from partial generations and more accurate intervention decisions. In routed execution (small + large model), it reduces large-model usage by up to 90.7 percent on AndroidWorld and 27-53 percent on average across benchmarks, while retaining most of large-model performance. Additionally, the learned control signals improve tool-use decision quality, yielding up to +158 percent relative score gain and 65.5 percent fewer missed-required tool calls.

</details>


### 45. AI Agents Do Not Fail Alone:The Context Fails First

- **Authors:** Fouad Bousetouane
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14275v1](http://arxiv.org/abs/2607.14275v1)
- **PDF:** [https://arxiv.org/pdf/2607.14275v1](https://arxiv.org/pdf/2607.14275v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. When this context is weak, agents drift, hallucinate, misuse tools, ignore constraints, become vulnerable to injection, and waste tokens. This paper validates context-engineering quality as an independent leading indicator of agent reliability. We implement the measurement in ProofAgent-Harness, an open-source infrastructure for AI agent evaluation that uses multi-juror, consensus-based scoring. The harness assesses context across seven criteria: role clarity, guardrail coverage, instruction consistency, tool schema quality, grounding sufficiency, injection hardening, and token efficiency. Crucially, the context score is isolated from behavioral metrics and release decisions, enabling a non-circular validation. Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes. Grounding sufficiency predicts hallucination resistance, guardrail coverage predicts manipulation resistance, instruction consistency predicts instruction following, and tool-schema quality predicts tool use. These findings establish context measurement as a validated preflight signal for agent reliability and position context engineering as an auditable layer of agent evaluation and governance.

</details>


### 46. MonteRET: AI Agent Enhancing Multimodal LLMs with Multi-granularity Knowledge Retrieval for Chest CT Report Generation

- **Authors:** Yi Lin, Yihao Ding, Elana Benishay, Elefterios Trikantzopoulos, David Nauheim, Hanley Ong, Jiang Bian, Hua Xu, Yuzhe Yang, George Shih, Yifan Peng
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14264v1](http://arxiv.org/abs/2607.14264v1)
- **PDF:** [https://arxiv.org/pdf/2607.14264v1](https://arxiv.org/pdf/2607.14264v1)
- **Categories:** cs.CV, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated chest CT report generation remains challenging because clinically faithful reporting requires both whole-volume understanding and accurate description of localized anatomical findings. Here we developed and retrospectively evaluated MonteRET, a region-aware retrieval-enhanced framework for generating chest CT findings sections. MonteRET integrates global CT features with region-level anatomical representations, retrieves clinically relevant knowledge using predicted medical conditions and region-level vision-language alignment, and refines initial reports through a knowledge-guided report rewriting agent. We trained our model on a public cohort with 24,128 CT scans from RadGenome-ChestCT. We evaluated MonteRET on the public RadGenome-ChestCT test set of 1,564 CT scans and an external cohort of 82 CT scans from NewYork-Presbyterian/Weill Cornell Medical Center. MonteRET improved report quality, semantic similarity, and clinical efficacy compared with a matched baseline and several state-of-the-art methods. Gains were most pronounced for recall, suggesting fewer omitted findings. Human expert evaluation by radiology residents also favored MonteRET.

</details>


### 47. Automatic Hard Example Synthesis with Multi-Level Agentic Data Curation

- **Authors:** Genglin Liu, Muye Zhang, Krishnamurthy Viswanathan, Nichole J. Hansen, Blaž Bratanič, Nathan L Clement, Shalini Ghosh, Ariel Fuxman
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14256v1](http://arxiv.org/abs/2607.14256v1)
- **PDF:** [https://arxiv.org/pdf/2607.14256v1](https://arxiv.org/pdf/2607.14256v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) are increasingly deployed for nuanced content safety and moderation tasks, yet they remain vulnerable to adversarial attacks and out-of-distribution edge cases. Traditional active learning and manual annotation fail to scale against the complexity and volume of novel multimodal threats. In this paper, we propose an automated, agentic red-teaming framework that systematically synthesizes difficult examples using an iterative strategy that proposes novel hypotheses as well as mutating on past attempts. Leveraging a multi-agent architecture that consists of a high-reasoning Architect agent, an advanced image generator, and a multi-level verification committee of LLM raters, our system autonomously uncovers boundary-pushing violations and ambiguous policy edge cases without any human intervention. By employing these carefully synthesized adversarial examples as in-context demonstrations via test-time Retrieval, we substantially improve the target model's robustness, reducing the False Negative Rate (FNR) from 41.2% to 24.5% in a public image safety benchmark without relying on any human labeling.

</details>


### 48. AI-accelerated End-to-End Framework for Rapid Professional Upskilling

- **Authors:** Tam Nguyen, Hung Nguyen, Robert Ogburn
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14044v1](http://arxiv.org/abs/2607.14044v1)
- **PDF:** [https://arxiv.org/pdf/2607.14044v1](https://arxiv.org/pdf/2607.14044v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

By 2030, 59 of every 100 workers will need reskilling or upskilling, yet the average time to close an enterprise skills gap grew from roughly 3 days in 2014 to 36 days in 2018. Most current frameworks accelerate single stages of upskilling programs and generally lack industry validation. We present an end-to-end framework that applies AI acceleration across five stages of knowledge acquisition, content development, content review and verification, teaching, and assessment development; with a strong focus on both production and learning efficiency. Three strong external signals validates the framework: the US National Association of State Boards of Accountancy reviewed and approved an upskilling program built on the framework for continuing-professional-education credits; 3 learners followed the program and passed the NVIDIA Certified Professional in Agentic AI exam in a significantly short amount of time, with 14 more in progress; the program's knowledge base supports complex downstream analysis such as the production of a robust 1,267 risk item dataset for managing multi-agent AI system risks.

</details>


### 49. Early Adoption of Agentic Coding Tools by GitHub Projects

- **Authors:** Maliha Noushin Raida, Daqing Hou
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14037v2](http://arxiv.org/abs/2607.14037v2)
- **PDF:** [https://arxiv.org/pdf/2607.14037v2](https://arxiv.org/pdf/2607.14037v2)
- **Categories:** cs.SE, cs.AI, cs.CY, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic coding tools are increasingly capable of generating and submitting pull requests (PRs) to software projects, introducing new forms of human-agent collaboration in software development. While prior studies have examined PR-level outcomes of agent-generated contributions, less is known about how agentic coding tools are adopted and managed at the project level. In this paper, we analyze 25,264 agentic PRs from 2,361 popular GitHub repositories to investigate (1) the adoption of agentic coding tools, (2) project-level agentic PR productivity, and (3) human-agent collaboration patterns. Our results show that the median repository generates only one to two agentic PRs during a three-month period, indicating that intensive adoption remains concentrated in a small subset of projects. At the same time, small projects (1-5 contributors) exhibit higher participation ratios and average levels of agentic PR activity than medium-sized and large projects. We also observe substantial variation in project-level agentic PR productivity. While a small number of projects exceed an industry-reported estimate of 36 PRs per participant during the three-month observation period, most projects remain below this threshold. Finally, human-agent collaboration is dominated by a single-human oversight model, in which one developer reviews and/or modifies the agent's contributions, while multi-human collaboration patterns remain uncommon. These findings provide early empirical evidence on how open-source projects organize human oversight around agentic coding tools and suggest that successful integration of agent-generated contributions depends not only on advances in agent capabilities but also on the human and organizational processes that govern their use. Because this study captures an early snapshot of agent adoption, future work should continue to track how adoption patterns evolve over time.

</details>


### 50. The Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) Model and the Net Human-Agent Score (NHAS) in Autonomous Commerce

- **Authors:** Sai Srikanth Madugula, Peplluis Esteva de la Rosa, Daya Shankar
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13998v1](http://arxiv.org/abs/2607.13998v1)
- **PDF:** [https://arxiv.org/pdf/2607.13998v1](https://arxiv.org/pdf/2607.13998v1)
- **Categories:** cs.SI, cs.AI, cs.GT, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid proliferation of Agentic Artificial Intelligence fundamentally disrupts traditional customer loyalty paradigms. As AI evolves from passive recommendation algorithms to autonomous, goal-directed agents capable of executing purchasing decisions, the conventional understanding of consumer-brand relationships requires a structural reevaluation. By synthesizing extant literature across human-machine teaming, consumer decision-making, and algorithmic trust dynamics, we demonstrate that traditional loyalty models fail to account for algorithmic bounded rationality and constructed autonomy. To address this, we introduce the Dynamic Verifiable Multi-Agent Human Agentic Loyalty Loop (DVM-HALL) model. We formalize brand choice via a softmax probability formulation where human emotional equity, agentic machine-experience utility, calibrated trust, delegated authority, and verifiable execution jointly determine selection. The model features recursive updating mechanisms to dynamically calibrate trust and delegation after each interaction. Crucially, the framework integrates a verifiable execution layer for Decentralized Finance (DeFi) and tokenized loyalty settings, incorporating execution risks -- such as gas costs, slippage, MEV exposure, and smart-contract vulnerabilities -- as core predictors of agentic brand preference. Furthermore, we introduce the Net Human-Agent Score (NHAS), an auditable, risk-weighted metric designed to measure human-agent alignment using human feedback, execution logs, benchmark comparisons, and verifiable receipts. Finally, we propose a comprehensive three-stage empirical validation plan spanning controlled shopping experiments, multi-agent market simulations, and DeFi testbeds. This framework provides the foundational theory required for brands to navigate the impending transition toward machine customers.

</details>


### 51. TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents

- **Authors:** Leitian Tao, Baolin Peng, Wenlin Yao, Tao Ge, Hao Cheng, Mike Hang Wang, Jianfeng Gao, Sharon Li
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13988v1](http://arxiv.org/abs/2607.13988v1)
- **PDF:** [https://arxiv.org/pdf/2607.13988v1](https://arxiv.org/pdf/2607.13988v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. They can also be misleading: a failed rollout may contain many useful actions that move the agent closer to the goal, yet outcome-only training assigns them the same negative advantage as the eventual mistake. We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning. TRACE represents rollouts as state transitions at tool-call boundaries, obtains gold-answer log-probabilities from a frozen reference model, transforms them into log-ratio state values, and derives per-action rewards as Temporal-Difference changes in those values. This requires no additional critic or process-label training, and its one-step log-ratio TD component telescopes across redundant tool calls. On long-horizon complex search, TRACE substantially improves base-model tool-use ability using pure RL, without a cold-start supervised fine-tuning stage, an agentic mid-training stage, or training on live-web data. On the closed-web BrowseComp-Plus benchmark, it raises Qwen3-4B from $7.2$ to $35.6$ and Qwen3-30B-A3B from $8.4$ to $42.6$. The learned search behavior also transfers to open-web benchmarks, and the learning curves show earlier improvement and faster convergence during RL training.

</details>


### 52. Task-Oriented Sensing and Covert Transmissions for Collaborative Multi-AUV Systems

- **Authors:** Xueyao Zhang, Chenyang Yan, Bo Yang, Xuelin Cao, Zhiwen Yu, Bin Guo, George C. Alexandropoulos, Merouane Debbah, Chau Yuen
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13880v1](http://arxiv.org/abs/2607.13880v1)
- **PDF:** [https://arxiv.org/pdf/2607.13880v1](https://arxiv.org/pdf/2607.13880v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

In underwater covert cooperative missions, autonomous underwater vehicles (AUVs) often cannot rely on active sonar to continuously obtain complete information, since active sensing and frequent communications increase the risk of exposure. As a result, AUVs primarily rely on passive observation, an approach that yields incomplete local perception and limited task efficiency. Although underwater acoustic communications can mitigate this limitation through information sharing, they are simultaneously constrained by long delays, severe interference, low reliability, and the risk of covert exposure. Existing communications-oriented multi-agent reinforcement learning (MARL) studies often model communication as an ideal information flow, whereas traditional communication optimization primarily focuses on link-level performance. However, both are insufficient to characterize the actual contribution of perceptual information to cooperative tasks under realistic conditions of covert physical communications. This paper proposes a Sensed Information Value Realization Multi-Agent Reinforcement Learning (SVR-MARL) framework that leverages practical information to characterize the utility of information for cooperative tasks and learns distributed cooperative policies under realistic communication and covert constraints. Through a case study of covert multi-AUV cooperative localization and tracking, the potential of the proposed framework to improve collaborative task efficiency while reducing unnecessary communication and exposure risks is demonstrated.

</details>


### 53. SPyCE: Skill-Policy Co-evolution for Multimodal Agents

- **Authors:** Ru Zhang, Weijie Qiu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13854v1](http://arxiv.org/abs/2607.13854v1)
- **PDF:** [https://arxiv.org/pdf/2607.13854v1](https://arxiv.org/pdf/2607.13854v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps. Existing reinforcement learning methods reduce trajectories to scalar rewards, forcing the policy to discover reusable tool-use patterns from scratch on every new task; memory-based alternatives retain past experience, yet they rely on test-time retrieval, without updating the policy to absorb reusable patterns from that experience. Our key insight is that multimodal reasoning trajectories should be distilled into reusable skills that co-evolve with the policy during training, rather than being consumed as rewards or retrieved from a static store. To this end, we propose SPyCE (Skill-Policy Co-evolution), a framework that distills trajectories into a hierarchical skill library and updates it throughout reinforcement learning. Execution skills capture local visual operations, while workflow skills encode high-level priors that orchestrate tool use. During training, the policy model conditions on retrieved skills to guide its rollouts, while the skill library evolves using valuable rollouts generated by the policy. This creates a closed loop in which improved policies yield better skills, and the evolving skill library, in turn, provides stronger priors for policy rollouts. Experiments across eight benchmarks demonstrate that SPyCE consistently outperforms both RL-based and memory-based baselines. Further analysis reveals that both the hierarchical skill design and the co-evolution mechanism are critical to our design. These results suggest joint skill-policy optimization as a promising paradigm for building capable multimodal agents.

</details>


### 54. ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System

- **Authors:** Yutong He, Daibo Li, Guohong Li, Jiahe Geng, Zhengyang Huang, Can Ren, Zekun Zhang, Yifan Liu, Shuchen Zhu, Hengrui Zhang, Boao Kong, Ming Sun, Shu Li, Chenyi Li, Jiang Hu, Kun Yuan, Zaiwen Wen, Pingwen Zhang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14178v1](http://arxiv.org/abs/2607.14178v1)
- **PDF:** [https://arxiv.org/pdf/2607.14178v1](https://arxiv.org/pdf/2607.14178v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models have fueled autonomous AI agents capable of tackling complex scientific tasks, yet existing automated research systems remain predominantly focused on empirically driven domains with quantitative benchmarks, leaving theory-driven discovery, particularly in mathematically grounded disciplines requiring rigorous proofs and synthesis of domain knowledge, largely underexplored. Key challenges include the difficulty of verifying theoretical reasoning at scale, insufficient reasoning ability for autonomous frontier exploration, and a scarcity of procedural heuristics in the literature. We introduce ReasFlow, an end-to-end autonomous agent system for reasoning-centric scientific discovery that operationalizes a collaborative paradigm where the human expert acts as Principal Investigator while the agent executes rigorous derivations as a capable graduate student. ReasFlow incorporates (i) a robust internal verification loop that audits logical coherence and corrects fundamental errors prior to human inspection, and (ii) an automated knowledge retrieval and self-improvement mechanism that proactively surfaces both declarative facts and overlooked procedural heuristics, substantially reducing expert intervention. The system unifies literature synthesis, algorithm design, theorem proving, experimentation, and manuscript preparation in a single system. Deployed to autonomously generate five complete research papers with rigorous theoretical and empirical content from minimal prompts, ReasFlow consistently achieves the highest evaluation scores among state-of-the-art open-access baselines under a curated LLM-based review rubric. ReasFlow is publicly accessible via the ReasLab platform, providing a collaborative workspace for AI-assisted theoretical research. Github repo: https://github.com/ReasLab/ReasFlow.git.

</details>


### 55. How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

- **Authors:** Alexandra E. Michael, Franziska Roesner
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13718v1](http://arxiv.org/abs/2607.13718v1)
- **PDF:** [https://arxiv.org/pdf/2607.13718v1](https://arxiv.org/pdf/2607.13718v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI agents gain prevalance, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. As autonomous systems, agents also present the more active danger of performing sensitive tasks, such as bank transactions, without the user's intent or authorization.
  Recognizing this challenge, the agentic security community has developed numerous proposals for secure agentic systems. Much of this work has focused on product-level approaches, where agentic system developers determine and apply the same security policies and permissions to all users. Yet different users have different needs and preferences, necessitating support for user-level permissions policies in agentic AI systems.
  To understand how user-level permissions are handled in AI agent systems, we survey 21 proposals for agent permissions systems. From this review, we construct a taxonomy of how different systems specify user-level permissions policies, both at the user interface and internally; derive internal policies from user input; and enforce those policies at run-time. We then analyze five prominent commercial agents and compare their permissions handling to agentic permissions systems in the literature. We identify several high-level themes across the literature and commerical agents, as well as multiple gaps where future work is needed.

</details>


### 56. CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems

- **Authors:** Zexun Wang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13716v1](http://arxiv.org/abs/2607.13716v1)
- **PDF:** [https://arxiv.org/pdf/2607.13716v1](https://arxiv.org/pdf/2607.13716v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines. A single operational act such as publishing code, changing identity state, moving money, or exporting data may therefore be represented by many incompatible runtime records. This makes a basic governance question difficult to answer: what action was actually approved, what evidence binds the approval to execution, and can an independent verifier reproduce the same action identity later?
  This paper presents Canonical Action Verification and Attestation (CAVA), a runtime-semantics layer for converting heterogeneous agent activity into canonical runtime action objects. CAVA is positioned below Proof-Carrying Agent Actions (PCAA): PCAA defines the deployer-owned route-review-prove governance process, while CAVA defines the stable action object that process governs. The paper formalizes canonical action identity, semantic pattern detection, approval binding, receipt integrity, runtime-portable projection, and optional attestation substrates. We study a reference implementation through a 96-seed, 384-variant benchmark covering semantic equivalence, semantic separation, wrapper bypass, false-positive control, approval binding, receipt reproducibility, attestation tamper detection, runtime portability, semantic pattern detection, policy degradation, and Azure deployment drills. The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance.

</details>


### 57. AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities

- **Authors:** Kai Chen, Zichen Ding, Jiaye Ge, Shufan Jiang, Mo Li, Qingqiu Li, Zehao Li, Zonglin Li, Tiaohao Liang, Shudong Liu, Zerun Ma, Zixing Shang, Wenhui Tian, Zun Wang, Liwei Wu, Zhenyu Wu, Jun Xu, Bowen Yang, Dingbo Yuan, Qi Zhang, Songyang Zhang, Peiheng Zhou, Dongsheng Zhu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13705v2](http://arxiv.org/abs/2607.13705v2)
- **PDF:** [https://arxiv.org/pdf/2607.13705v2](https://arxiv.org/pdf/2607.13705v2)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical. However, current evaluation pipelines remain highly fragmented and tightly coupled, hindering reproducibility and causing redundant engineering. To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents. AgentCompass organizes the evaluation process around three independent components, namely Benchmark, Harness, and Environment, thereby enabling flexible configurations without requiring the reimplementation of complex execution logic. Furthermore, it features a fault-tolerant asynchronous runtime and comprehensive trajectory analysis tools to transparently diagnose nuanced failure modes like reward-hacking. Natively supporting over 20 benchmarks across five capability dimensions, AgentCompass provides the community with a scalable and reproducible infrastructure for advancing agent research.

</details>


### 58. Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity

- **Authors:** Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu, Dizhan Xue, Yafeng Deng
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13683v1](http://arxiv.org/abs/2607.13683v1)
- **PDF:** [https://arxiv.org/pdf/2607.13683v1](https://arxiv.org/pdf/2607.13683v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement artifact or an edit that merely overfits the tasks it was tuned on. We present a self-evolving agent-harness framework that separates proposing changes from crediting them: a language model diagnoses failures and proposes patches, while all sampling, measurement, and significance testing are owned by deterministic code, so every credited improvement is trustworthy by construction. Patches populate a gated, categorical quality-diversity archive (GSME) keyed on the (WHERE x WHY) pathology an edit addresses rather than the tasks it fixes, an anti-overfitting inductive bias; generalization is measured on a sealed test scored only after evolution. Across seven domains with a frozen open-weight model, the harness is train-selected and scored once on a sealed test; its credited gains there are +9 to +15.5pp and retain 86-147% of the training gain, evidence they generalize rather than overfit. The winning patch tracks the model's dominant pathology, not its size or family: changing the model can change the pathology and the patch, while the same pathology-to-patch match recurs across two model families. What transfers is the diagnose-and-credit loop, not any specific harness.

</details>


### 59. When Bots Join the Team: Bot Adoption and the Institutional Fabric of Open-Source Software Projects

- **Authors:** Yongren Shi, Wenyi Gong
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13679v1](http://arxiv.org/abs/2607.13679v1)
- **PDF:** [https://arxiv.org/pdf/2607.13679v1](https://arxiv.org/pdf/2607.13679v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are joining human teams, raising a basic question: when an automated agent becomes a regular participant, does group organization strengthen or weaken? We study this question in open-source software, where bots open pull requests, review code, and merge changes alongside people, leaving a public record of every interaction. Treating bots as participants rather than tools, we examine 2,991 GitHub projects for two years before and after each adopted its first bot. We measure three capabilities that institutional theory links to durable coordination - repeated engagement, social memory, and role differentiation - and two outcomes: conflict cascades and output distinctiveness. Bot adoption is followed by more repeated collaboration, greater recognition of specific bots in discussion, fewer conflict cascades, and more distinctive outputs. These changes cluster around adoption rather than accumulating gradually. Because we lack an untreated comparison group, we interpret the results as precisely timed associations, not causal effects. Two patterns are difficult for alternative explanations to account for: capabilities predict outcomes according to their function - coordination versus differentiation - rather than whether humans or bots provide them, and human-side capabilities account for the bot-conflict association but not the bot-distinctiveness association. The findings are consistent with a specific interpretation: predictable, rule-based agents can become part of a community's social infrastructure. The bot is the occasion; social organization is the mechanism.

</details>


### 60. Explaining Reinforcement Learning Agents via Inductive Logic Programming

- **Authors:** Celeste Veronese, Edoardo Zorzi, Daniele Meli, Alessandro Farinelli
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13655v1](http://arxiv.org/abs/2607.13655v1)
- **PDF:** [https://arxiv.org/pdf/2607.13655v1](https://arxiv.org/pdf/2607.13655v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Explainable Reinforcement Learning (XRL) seeks to make Reinforcement Learning (RL) policies more transparent and interpretable, a key requirement in safety-critical and human-centric scenarios. However, it is mostly based on user studies, thus targeting the needs of a specific audience and lacking shared evaluation metrics. On the other hand, logic-based approaches within eXplainable Artificial Intelligence (XAI) provide compact, human-readable abstractions of decision-making. However, the systematic quantification of the explainability degree of logical representations remains an open problem. This work aims to advance the state of the art in XRL by introducing objective and planning-oriented metrics for policy explainability in RL settings. At the same time, it contributes to the field of logic for XAI by providing a principled way to quantify the explainability of logical rules, moving beyond common-sense assessments and simple propositional fragments. We employ Inductive Logic Programming (ILP) to extract symbolic representations of RL policies and define a novel set of explainability metrics, including activation rate, feature coverage, syntactic distance and semantic distance. These metrics quantify alignment between symbolic rules and agent behavior, the role of features in decision-making, and the evolution of policies during training and across agents in single and multi-agent RL. Experiments across different RL domains show that the proposed metrics highlight action-specific learning dynamics beyond global return, provide fine-grained insights into domain features beyond classical approaches for global feature importance estimation, and uncover coordination, specialization, and adaptation patterns in MARL. Moreover, they provide crucial insights for the transfer and generalization of action-specific policies.

</details>


### 61. STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle

- **Authors:** Sagar Deb, Ashwanth Krishnan
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13618v1](http://arxiv.org/abs/2607.13618v1)
- **PDF:** [https://arxiv.org/pdf/2607.13618v1](https://arxiv.org/pdf/2607.13618v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). Existing evaluations cannot separate these two failures; their reference policies either read privileged information the agent never sees, or are missing altogether. We introduce STOCKTAKE, a 26-week supply-chain replenishment benchmark built as a factored partially observable Markov decision process with six hidden factor processes, designed so that a fair reference policy is computable: an exact Bayes filter per factor drives a rollout policy on the identical observation stream the agent receives. Scoring each run between a symptom-blind base-stock floor (0) and this oracle (1) yields a skill score, and grading each week's written rationale yields a stated-belief detection lag and a knowing-doing rate, so state estimation and control are measured separately. On fifty seeds with curated stress profiles, Claude Sonnet 5, GPT-5.4, DeepSeek-V4-Pro, and Grok 4.5 detect 84-88% of hidden failures, typically within a week of onset, yet span skill scores from 0.62 to -0.23: two of the four end below the symptom-blind floor while naming factors slightly faster than the two that beat it. The failure has two faces. Where stress persists, 34-43% of correctly diagnosed stress weeks still end in stockout for every model, a rate that partly reflects the severity of the weeks models notice. That rate also runs opposite to skill: the two models under the floor stock out least on diagnosed weeks, so under-response is only one face of the gap, and their traces point to the other, responses whose cost exceeds what they protect. STOCKTAKE measures both directions of that failure.

</details>


### 62. Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis

- **Authors:** Yongqiang Chen, Guangyi Chen, Yuewen Sun, Kun Zhang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13602v1](http://arxiv.org/abs/2607.13602v1)
- **PDF:** [https://arxiv.org/pdf/2607.13602v1](https://arxiv.org/pdf/2607.13602v1)
- **Categories:** cs.CL, cs.LG, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Systematic comparisons between current situations and structurally similar past events in the historical, i.e., historical analogies, is among the most powerful tools for foresight analysis. In this work, we present a new task called Analogical Deep Research (ADR) to Large Language Model (LLM) agents and construct the first ADR benchmark ADR-bench to study whether LLM agents are able to find and leverage historical analogies when doing foresight analysis. Our investigation reveals a key obstacle: LLM agents are poor at finding analogies because they match on surface features rather than underlying mechanisms. We argue that ADR is inherently a causal question as it requires understanding why the event occurred. Based on our theoretical analysis, we propose two principles required for ADR, including the mechanism alignment and cross-analogy confirmation. Built upon our theoretical results, we propose a new agentic framework called Causal Analogical Researcher (CANA) that guides LLMs to find and integrate historical analogies. CANA incorporates a simple yet effective structural decomposition representation, and integrates structural feedback for reflective improvements of historical analogy identification and integration. We show that CANA brings up to 10% improvements in historical analogy generation, and surpasses the state-of-the-art deep research agents in the ADR-bench. Case studies with the ongoing events confirm the effectiveness of CANA in leveraging historical analogies.

</details>


### 63. SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing

- **Authors:** Tianyu Chen, Chujia Hu, Wenjie Wang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13594v1](http://arxiv.org/abs/2607.13594v1)
- **PDF:** [https://arxiv.org/pdf/2607.13594v1](https://arxiv.org/pdf/2607.13594v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm. The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context. It also operates at the granularity of action categories rather than individual instances, producing routine interruptions that erode autonomy and train users to wave through the most consequential alerts. We reframe the problem as a per-instance three-way routing decision over {EXECUTE, ASK, REFUSE} and instantiate it with Safety Sentry, a lightweight guard model whose inference reduces to a single decoding call. A single decoding-time threshold lets one fixed checkpoint be re-positioned across deployments of differing risk tolerance without retraining. Safety Sentry outperforms a broad set of open-weight and frontier closed-source baselines on overall accuracy and safety-related recall, while controlling both directional error rates simultaneously.

</details>


### 64. Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents

- **Authors:** Eric Hanchen Jiang, Zhi Zhang, Yuchen Wu, Levina Li, Dong Liu, Xiao Liang, Rui Sun, Yubei Li, Edward Sun, Haozheng Luo, Zhaolu Kang, Aylin Caliskan, Kai-Wei Chang, Ying Nian Wu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13591v1](http://arxiv.org/abs/2607.13591v1)
- **PDF:** [https://arxiv.org/pdf/2607.13591v1](https://arxiv.org/pdf/2607.13591v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents increasingly rely on external memory systems to accumulate experience across tasks. Yet nearly all existing approaches, from graph-structured memories to reflective insight stores, access memory through fixed, hand-designed heuristics. We argue that this static view of memory is a core bottleneck for agentic learning because optimal memory behavior is fundamentally context-dependent. The early stages of the tasks, benefit from minimal retrieval because memory is sparse; recurring goal types benefit from plan reuse rather than generic nearest-neighbor lookup; stuck agents benefit from re-retrieval with alternative queries; and across long task streams, the memory store itself must be consolidated and pruned to remain useful. We present Memory as a Controlled Process (MemCon), a framework that models memory operations as a Markov Decision Process and learns an online policy that adaptively decides when, what, and how much to retrieve, when to inject a distilled plan, and when to consolidate or forget. MemCon is backend-agnostic: it wraps any existing memory implementation, learns from task-by-task binary feedback with no pretraining and no additional LLM calls, and uses a lightweight tabular contextual bandit with UCB exploration that converges within tens of tasks. Across 6 benchmarks, 3 agent frameworks, and 3 LLM backbones, MemCon consistently outperforms multiple memory baselines by up to 15.2 points in task success while reducing token consumption by 5--20%.

</details>


### 65. Multi-Agent Collaborative Reasoning with Tool-Augmented Evidence for Urban Region Profiling

- **Authors:** Xixuan Hao, Yutian Jiang, Jiabo Liu, Yihang Yang, Guangyin Jin, Song Gao, Yuxuan Liang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13558v1](http://arxiv.org/abs/2607.13558v1)
- **PDF:** [https://arxiv.org/pdf/2607.13558v1](https://arxiv.org/pdf/2607.13558v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Urban region profiling constitutes a core problem in urban computing, supporting applications such as population estimation, economic assessment, and environmental monitoring. Existing methods typically formulate this task as multimodal representation learning, fusing heterogeneous urban data, e.g., satellite imagery, points of interest, textual descriptions, and 3D building information, into latent embeddings for prediction. However, these approaches are largely correlation-driven, assume cross-modal consistency, and rely on static pipelines, which limit their robustness in heterogeneous or unseen urban regions. We propose UrbanAgent, an agentic framework that reframes urban region profiling as a reasoning-driven inference problem. UrbanAgent instantiates an independent agent for each data modality and performs structured multi-agent collaborative reasoning to explicitly address cross-modal inconsistencies rather than absorbing them into a single representation. In addition, UrbanAgent extends indicator prediction as a closed-loop process of active evidence acquisition and iterative reasoning, enabling agents to verify uncertain inferences through tool-augmented retrieval of external knowledge optimized via reinforcement learning. Extensive experiments on global urban datasets for Carbon emissions, GDP, and Population estimation show that UrbanAgent consistently outperforms existing baselines, achieving an average improvement of 8.1% in R2, and exhibiting strong generalization performance in unseen-city settings.

</details>


### 66. Flow-aware Optimal Navigation in Unsteady Flows through Reinforcement Learning

- **Authors:** Andrea Maria Braghin, Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni, Gabriele Cazzulani
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13553v1](http://arxiv.org/abs/2607.13553v1)
- **PDF:** [https://arxiv.org/pdf/2607.13553v1](https://arxiv.org/pdf/2607.13553v1)
- **Categories:** cs.RO, cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous robotic navigation in nonstationary time-varying fluid flows remains a fundamental challenge due to partial observability and the unpredictability of realistic environments. While classical optimal control frameworks employed in robotics require unrealistic a-priori global flow knowledge, biological systems are able to navigate successfully by exploiting localized sensory cues. In this work we present a reinforcement learning approach using the TD3 algorithm to train autonomous agents to reach arbitrary targets within a parametric, chaotic double-gyre flow. To investigate optimal sensory mechanisms, we evaluate five bio-inspired observation strategies based on relative position, local velocity or local vorticity measures, and short-term memory variants. Additionally, we analyze the impact of providing agents with explicit global flow parameters. Numerical results demonstrate that an agent that is able to sense and remember a set number of flow velocity measures achieves the highest performance. The experiments reveal a trade-off in sensor utility: velocity-aware agents optimize energy efficiency, whereas vorticity sensors provide superior structural mapping and achieve better target proximity. Incorporating explicit global flow parameters is shown to decrease navigation performance. This behavior suggests that reinforcement learning-based autonomous systems develop more robust and general policies when restricted to implicit flow representations. The presented results offer insights for improving the transition of bio-inspired robotic navigation from simulation to real-world environments.

</details>


### 67. How Far Can Root Cause Analysis Go on Real-World Telemetry Data?

- **Authors:** Athira Gopal, Ashwanth Krishnan
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13548v1](http://arxiv.org/abs/2607.13548v1)
- **PDF:** [https://arxiv.org/pdf/2607.13548v1](https://arxiv.org/pdf/2607.13548v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Identifying root causes in production microservice failures requires reasoning over large-scale, multimodal telemetry spanning metrics, logs, and traces, a problem that has proved resistant to both classical and LLM-based approaches. The OpenRCA dataset exemplifies these challenges: it is large-scale, multimodal, and lacks detailed domain knowledge, and yields consistently low accuracy across all existing methods. We show that classical causal discovery methods and existing LLM-based multi-agent systems fail to reliably identify root causes on this benchmark, and present a Structured Multi-Agent RCA pipeline that substantially outperforms existing LLM-based and classical baselines, supporting both domain-knowledge and knowledge-free operating modes. To diagnose where failures originate, we introduce a reverse reasoning agent that, given the correct answer, identifies which signals in the extracted anomalies support it and determines whether Stage~1 had access to those signals, classifying each failure as Reasoning Gap (evidence present but unused) or Data Ambiguity (evidence genuinely absent). This analysis reveals that the required evidence is present in the vast majority of failures: the bottleneck is not data access but the agent's ability to reason over it correctly. We further introduce an automated rule mining pipeline that systematically extracts discrimination rules from reverse reasoning reports, reducing reliance on manual knowledge curation. Across all configurations, model reasoning capability and domain knowledge are the primary constraints: stronger models embed more domain expertise, and explicit knowledge injection partially compensates for this gap. Reasoning performance remains practically bounded even when evidence extraction is perfect: scaffold engineering and better data pipelines alone cannot close this gap; progress requires improvements at the model level.

</details>


### 68. Structured Feedback Improves Repair in an LLM Agent Loop

- **Authors:** Jaideep Ray, Ankit Goyal
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14167v1](http://arxiv.org/abs/2607.14167v1)
- **PDF:** [https://arxiv.org/pdf/2607.14167v1](https://arxiv.org/pdf/2607.14167v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often retry after external validation rejects a candidate, but the interface between validation and the next model call remains underspecified. We introduce VeriHarness, a code-controlled agent loop in which models generate candidates while external validators control acceptance, budgets, and traces. We use it to compare raw diagnostics with feedback that identifies the failure location, observed value, and admissible alternatives. Across 50 paired TextWorld games under a four-call cap, feedback containing all three fields raises terminal success from 14/50 to 36/50 for Qwen2.5-Coder-14B (+44 percentage points) and from 8/50 to 29/50 for Llama-3.1-8B (+42 points). Ablations locate most of the gain in the admissible alternatives: feedback containing only the location and observed value remains near the raw diagnostic baseline. Presenting the complete repair information in prose instead of a keyed JSON record yields nearly the same success, providing no evidence that JSON syntax itself improves repair. The ordering persists across the tested call budgets and one sampled-decoding setting.

</details>


### 69. MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent Systems

- **Authors:** Zhisong Zhang
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13474v1](http://arxiv.org/abs/2607.13474v1)
- **PDF:** [https://arxiv.org/pdf/2607.13474v1](https://arxiv.org/pdf/2607.13474v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present MyAG, a graph-based framework for designing and analyzing composable LLM agent systems. Our framework separates agent system construction into three graph abstractions: a component graph for agents, environments, and modules; a workflow graph for execution control; and a search graph for runtime execution. This separation allows users to flexibly reuse the same components with different strategies. We further support hierarchical composition through recursive system nodes and provide monitoring and visualization tools for inspecting agent execution. Experiments on representative agent applications show that our framework supports flexible agent system design and helps analyze performance-efficiency tradeoffs. Our framework is publicly available and fully open-source.

</details>


### 70. Towards Reliable AI-Assisted Analog Design: Template-Constrained LLM Agents for SAR ADC Generation

- **Authors:** Dimple Vijay Kochar, Hae-Seung Lee, Anantha P. Chandrakasan
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14165v1](http://arxiv.org/abs/2607.14165v1)
- **PDF:** [https://arxiv.org/pdf/2607.14165v1](https://arxiv.org/pdf/2607.14165v1)
- **Categories:** cs.SE, cs.AI, cs.AR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated significant capability in software code generation, their application to analog Electronic Design Automation (EDA) is bottlenecked. Owing to limited circuit topology understanding and data, directly prompting LLMs and multimodal models leads to hallucinations and failure to produce schematics capable of passing rigorous SPICE simulations, as we show in our work. Instead, we propose an end-to-end, multi-step LLM agentic framework ATLAS, capable of generating a functional Successive Approximation Register (SAR) Analog-to-Digital Converter (ADC) that successfully passes simulation validation. To adhere to the rigid constraints of analog design, we utilize expert knowledge to ground the LLM in its planning, selection, parameterization, and iterative modification. As part of ATLAS, we introduce Template-Constrained Generation - which unlike other template-based works - builds towards a more generalized SAR ADC generation flow. We demonstrate a strong proof-of-concept of our framework by developing SAR ADCs across technology nodes and input specs. Overall, our expert-knowledge grounded multi-step agentic ATLAS establishes a pragmatic foundation for integrating LLMs into reliable analog design methodologies.

</details>


### 71. Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender Systems with Collaborative Agents

- **Authors:** Jiwen Zhou, Xiang Liu, Mingming Li, Pengbo Mo, Jiao Dai, Honglei Lv, Jizhong Han, Songlin Hu
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13418v2](http://arxiv.org/abs/2607.13418v2)
- **PDF:** [https://arxiv.org/pdf/2607.13418v2](https://arxiv.org/pdf/2607.13418v2)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recommender systems operate as Black-Boxes, leaving users and regulators unable to steer their outputs toward specific intentions or audit their behavior. This lack of controllability, defined as the system's ability to respond to explicit guidance, remains an unaddressed dimension in existing evaluation paradigms. To fill this gap, we propose CtrlBench-Rec, a collaborative multi-agent framework for systematic assessment of controllability. We formalize three fundamental tasks: target content discovery, interest profile shaping, and popularity bias mitigation, which together measure steerability from explicit commands to implicit representation steering and finally to overcoming algorithmic biases.Extensive experiments on real-world datasets and multiple recommendation models demonstrate that our framework effectively quantifies controllability and exposes critical system bottlenecks, most notably persistent resistance to guiding long tail content. CtrlBench-Rec provides the first standardized toolkit for controllable recommendation research, algorithmic auditing, and user empowerment. Our code is released on https://github.com/caskcsg/CtrlBenchRec.

</details>


### 72. Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors

- **Authors:** Michael O. Eniolade
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13411v1](http://arxiv.org/abs/2607.13411v1)
- **PDF:** [https://arxiv.org/pdf/2607.13411v1](https://arxiv.org/pdf/2607.13411v1)
- **Categories:** cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. Given a pre-trained clinical prediction model, a patient dataset, and written instructions, each agent must implement four attacks from pseudocode, compute a Security Posture Score covering FGSM robustness, membership inference resistance, expected calibration error, and boundary attack resistance, and write a structured JSON report in a Docker container using only a bash interface and no scaffolding code. Six variants span the Wisconsin Diagnostic Breast Cancer and MIMIC-IV ICU mortality datasets across three model architectures with increasing defense strength, with reference scores from 55.60 to 90.41. We ran 54 evaluations across three frontier models, with three runs per variant. Claude Sonnet 4.6 and GPT-4.1 completed all 18 runs and received perfect evaluator scores. GPT-4o completed 61 percent of runs and used about five times the per-run token count of Claude, although provider tokenization differs. Total API costs were 8 US dollars for GPT-4.1, 12 US dollars for Claude Sonnet 4.6, and 27 US dollars for GPT-4o. GPT-4o failures involved premature session termination, an aggregation error, and an empty submission file. The task, scoring infrastructure, and Wisconsin Breast Cancer assets are publicly released; MIMIC-IV variants require separate PhysioNet access.

</details>


### 73. Set-shifting Behavioral Test for Harnessed Agents

- **Authors:** Ziwei Ye
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13396v1](http://arxiv.org/abs/2607.13396v1)
- **PDF:** [https://arxiv.org/pdf/2607.13396v1](https://arxiv.org/pdf/2607.13396v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. Our benchmark mounts tool-skill libraries with redundancies, where many tools solve the same task but differ in hidden reliability. In our evaluation framework, a branched schedule shifts the reliable tool group at hidden boundaries and pairs every shift with a no-shift control. We find that agents, by default, settle on a small recurring routine within a few turns of each boundary, with call shares concentrating on a few discrete values after each reliability shift. We score the set-shifting accuracy for each agent trajectory: the joint probability of routing to the target tool group in every post-shift window. We test open-weight LLMs in an open-source agentic harness and find qualitatively distinct failure modes across the same set of routines. We also find that set framing, how the toolset presents the alternatives as competing or complementary, shifts the routing dynamics.

</details>


### 74. Learning Engagement Assistant (LEA): Cross-Course Scalability and Classroom Evaluation of an Agentic AI Tutoring System

- **Authors:** Teri Rumble, Javad Zarrin, P. George Lovell, Ruth Falconer
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13370v1](http://arxiv.org/abs/2607.13370v1)
- **PDF:** [https://arxiv.org/pdf/2607.13370v1](https://arxiv.org/pdf/2607.13370v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper is an extension of a paper presented at the ICAART 2026 conference, which introduced LEA (Learning Engagement Assistant), an adaptive AI tutoring agent combining course-specific Retrieval-Augmented Generation (RAG) with structured Knowledge Component (KC) models across integrated Chat, Tutor, and Quiz modes. That prior work validated LEA on a single STEM course (CMP511) exclusively through simulation, using synthetic learner agents. This paper extends that work by reporting the first classroom deployment of LEA with real students (n = 8, CMP511) and the first empirical test of its cross-course scalability, deploying the system across three courses spanning two academic levels and two disciplinary domains. The study reveals a divergence from simulation predictions across modes, showing that synthetic evaluation alone cannot anticipate all aspects of real deployment. A RAGAS-based cross-course scalability evaluation (660 questions) finds Answer Relevancy and Context Precision broadly stable across courses (0.88-0.94 and 0.88-0.90 respectively), while Faithfulness declines with curriculum distance from the system's original course (0.69 to 0.50), a preliminary finding that may reflect generation logic tuned to the system's original subject rather than a scalability limitation. These findings suggest that while the orchestration layer requires no modification, full course-agnosticism of all downstream components requires further investigation.

</details>


### 75. Learning Latency-Aware Orchestration for Multi-Agent Systems

- **Authors:** Xi Shi, Mengxin Zheng, Qian Lou
- **Published:** 2026-07-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13359v1](http://arxiv.org/abs/2607.13359v1)
- **PDF:** [https://arxiv.org/pdf/2607.13359v1](https://arxiv.org/pdf/2607.13359v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations. Existing orchestration methods primarily optimize task performance and inference cost, leaving latency largely unaddressed. In MAS, end-to-end latency is governed by the critical execution path, so reducing total cost alone does not reliably reduce latency. Moreover, optimizing latency while preserving accuracy remains non-trivial: naive latency optimization can misassign operator-level credit and degrade task accuracy. To address this gap, we propose Latency-Aware Multi-agent System (LAMaS), a latency-aware orchestration framework for learning-based multi-agent systems. LAMaS addresses this challenge at two levels: at training time, it learns latency-aware execution graphs through constrained optimization with critical-path-aware credit assignment; at inference time, since a graph committed at training time cannot exploit runtime evidence, it complements graph construction with a lightweight controller that adaptively eliminates redundant future agent interactions as execution unfolds. Experiments on four benchmarks show that LAMaS achieves the best latency among evaluated learning-based MAS baselines, reducing end-to-end latency by over 50\% while maintaining competitive or better accuracy. LAMaS is also modular and transfers to other MAS with minimal changes, consistently yielding latency reductions.

</details>


### 76. Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable

- **Authors:** Ruhan Wang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Yue Yu, Junyao Yang, Kishan Panaganti, Haitao Mi, Dongruo Zhou,  Leoweiliang
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13285v1](http://arxiv.org/abs/2607.13285v1)
- **PDF:** [https://arxiv.org/pdf/2607.13285v1](https://arxiv.org/pdf/2607.13285v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. Before such a change can be made, a developer or coding agent must identify all code locations that implement the target behavior. This is difficult because production harnesses are large, tightly coupled, and behaviorally distributed, while modification requests describe what the system should do and repositories are organized by files and modules. Code search, repository indexing, and long-context processing ease inspection, but still leave this behavior-to-code mapping to be recovered by hand. Behavior localization is therefore a central bottleneck in harness evolution. We introduce the Harness Handbook, a behavior-centric representation synthesized automatically from a harness codebase via static analysis and LLM-assisted structuring, linking each behavior to its corresponding source. We also introduce Behavior-Guided Progressive Disclosure (BGPD), which guides agents from high-level behaviors to relevant implementation details and verifies candidate locations against the current source. On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions. Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

</details>


### 77. Orchestrating Power Grid Studies with Multi-Agent AI and MCP Servers

- **Authors:** Jérôme Picault, Clément Goubet
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14158v1](http://arxiv.org/abs/2607.14158v1)
- **PDF:** [https://arxiv.org/pdf/2607.14158v1](https://arxiv.org/pdf/2607.14158v1)
- **Categories:** cs.AI, cs.CL, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

This position paper explores how Agentic AI and Model Context Protocol (MCP) can support power-grid studies in a Transmission System Operator (TSO) context. We focus on integrating Large Language Models with numerical simulation tools, structured workflows, and human supervision. We identify key industrial requirements for agent assisted grid studies and introduce pypowsybl-mcp, an MCP-based interface exposing selected capabilities of our simulation tool, pypowsybl to AI agents. This first step provides a testbed to study how agents can setup simulations, execute analyses, retrieve results, and interact with power-system simulators through standardized tool calls. We also discuss principles for human-in-the-loop, multi-agent workflows and outline an evaluation strategy combining technical metrics and practitioner feedback. The paper positions MCP-based tool integration as a step toward more interactive, auditable, and scalable grid-study environments.

</details>


### 78. AI-Native Insurance for Agentic AI: Pricing, Underwriting, and End-to-End Automation

- **Authors:** Quanyan Zhu
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13230v1](http://arxiv.org/abs/2607.13230v1)
- **PDF:** [https://arxiv.org/pdf/2607.13230v1](https://arxiv.org/pdf/2607.13230v1)
- **Categories:** cs.AI, cs.CR, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI introduces new insurance challenges because autonomous AI systems can make decisions, invoke tools, modify external environments, and interact with third-party services. This paper develops an AI-native mathematical framework for underwriting, pricing, and contract design for agentic AI deployments. A deployment is represented by a risk state that captures autonomy level, operational authority, permission exposure, governance maturity, and dependency concentration. The framework maps the risk state to event probabilities, loss severities, governance costs, premiums, deductibles, coverage allocation, and policy covenants, and formulates an optimization problem for insurance contract design under participation, profitability, and incentive compatibility constraints. The paper establishes structural properties of insurability, including characterization of an insurability region, monotone deterioration of feasibility with increasing exposure, and governance certification thresholds. Insurance is further interpreted as both an operational cost and a regulatory mechanism for AI deployment. A healthcare case study illustrates contract optimization, sensitivity analysis, and automated claims processing for agentic AI systems.

</details>


### 79. Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science

- **Authors:** Sutanay Choudhury, Jeffrey J. Czajka, Lummy M. O. Monteiro, Erin Bredeweg, Jason McDermott, Katherine Wolf, Alex Beliaev, Josh Elmore, Paul Piehowski, Kylee Tate, Yuqian Gao, Aivett Bilbao, Kelly Stratton, Scott Baker, Jaydeep P. Bardhan, Kristin Burnum Johnson, Chris Oehmen, Robert Rallo
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13220v2](http://arxiv.org/abs/2607.13220v2)
- **PDF:** [https://arxiv.org/pdf/2607.13220v2](https://arxiv.org/pdf/2607.13220v2)
- **Categories:** cs.AI, cs.CE, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Most AI-for-science systems focus on scaling a single reasoning process by using better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, challenging scientific problems are rarely solved by one reasoner alone. They are solved by teams whose members carry different priors, experimental background, tacit knowledge, and domain-trained intuitions. The open problem is therefore not only how to scale models, but how to develop "networked intelligence", scaling the connections between humans and AI systems so that a result or hypothesis produced in one context reaches another person, agent, instrument or robot that can act on it. We introduce Mycelium, an active shared workspace that automatically connects researchers and AI agents. As human users and agents work, the system captures important observations and hypotheses, tracks how they relate to the team's evolving knowledge model, and routes them to the person or agent whose next decision they can inform. We evaluate Mycelium through a real-world scientific discovery use case: a biological multi-omics campaign where shared context turned a local analytical finding into a cross-expert mechanistic constraint and ultimately into an experimental design. Finally, we describe networked intelligence as sparse conditional computation over distributed scientific contexts. This framework establishes when a scaled standalone agent is sufficient, and when isolated data and specialized expertise make a networked approach essential.

</details>


### 80. Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents

- **Authors:** Richmond Alake, Cesare Bernardis, Paul Cayet, Luca Engel, Damien Hilloulin, Sungpack Hong, Allen Hosler, Nickolas Kavantzas, Ingo Kossyk, Son Le, Rhicheek Patra, Kartik Talamadupula, Valentin Venzin
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13157v1](http://arxiv.org/abs/2607.13157v1)
- **PDF:** [https://arxiv.org/pdf/2607.13157v1](https://arxiv.org/pdf/2607.13157v1)
- **Categories:** cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. These requirements extend beyond document retrieval: a memory layer must determine which interactions become durable state, how that state is scoped, how it is retrieved under latency constraints, and how it is revised or removed over time. This report studies Oracle Agent Memory as a database-native memory substrate built on Oracle Database. Three themes organize the discussion: memory as a lifecycle spanning ingestion, extraction, consolidation, retrieval, summarization, and revision or removal; a layered architecture that separates an active memory core from a passive memory-store interface with explicit scope control across users, agents, and threads; and evaluation methodology in which downstream task accuracy is complemented by memory-centric measures such as evidence retrieval, recall, latency, and estimated token use. The report summarizes LongMemEval results, reaching 93.8% accuracy, compares Oracle Agent Memory against flat-history baselines, using about 10.7x fewer tokens, and published or reported external baselines where available, and closes with implementation-oriented appendix material covering setup, thread lifecycle, and search semantics.

</details>


### 81. Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution

- **Authors:** Junjie Yin, Xinyu Feng
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13034v1](http://arxiv.org/abs/2607.13034v1)
- **PDF:** [https://arxiv.org/pdf/2607.13034v1](https://arxiv.org/pdf/2607.13034v1)
- **Categories:** cs.AI, cs.CL, cs.SE, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path before committing budget. We formalize minimum-sufficient execution and the Agent Cognitive Redundancy Ratio (ACRR), and propose E3 (Estimate, Execute, Expand): the agent estimates an initial operating point, executes a minimum viable path, and expands scope only when verification fails. On MSE-Bench--a deterministic benchmark of 121 edits in a capability-controlled simulator--E3 matches the strongest baseline's 100% success while cutting cost by 85%, tokens by 91%, and inspected files by 92%, and further beats a strong adaptive retrieval baseline by 16%; the gains survive held-out instruction wording and essentially every cost weighting. A companion real-model harness (LLM-Case) corroborates the effect on a live gpt-4o agent editing a real open-source library, with every candidate patch graded by actually running the project's real pytest suite against a measured oracle: the over-reading is milder but real, and E3 is the leanest and fastest policy at comparable task success--its one shortfall a provider rate-limit, not a wrong edit. We frame this as a controlled probe of execution redundancy, not a measurement of any deployed agent, and position task-aware execution as a step toward engineering-grounded AI (EGAI)--agents whose effort is anchored in the engineering reality of the task. We release the framework and benchmark.

</details>


### 82. PalmClaw: A Native On-Device Agent Framework for Mobile Phones

- **Authors:** Hongru Cai, Yongqi Li, Ran Wei, Wenjie Li
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13027v1](http://arxiv.org/abs/2607.13027v1)
- **PDF:** [https://arxiv.org/pdf/2607.13027v1](https://arxiv.org/pdf/2607.13027v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user interface (GUI) actions such as tapping, swiping, and typing, which often form long, interface-dependent sequences, cannot directly access device capabilities, and make execution boundaries difficult to define. We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. PalmClaw exposes device capabilities as device tools with explicit arguments, structured results, and clearly defined execution boundaries. This design enables agents to use mobile capabilities directly while keeping each action explicit and controlled. Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied. Code is available at https://github.com/ModalityDance/PalmClaw.

</details>


### 83. A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study

- **Authors:** Cameron Cagan, Pedram Fard, Jiazi Tian, Jingya Cheng, Shawn N. Murphy, Hossein Estiri
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12886v1](http://arxiv.org/abs/2607.12886v1)
- **PDF:** [https://arxiv.org/pdf/2607.12886v1](https://arxiv.org/pdf/2607.12886v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted open-weights model, Pythia keeps clinical notes on local infrastructure and selects prompts using development-set sensitivity and specificity. We compared Pythia with a curated lexicon across 72 signs and symptoms from 400 clinical notes representing 387 patients. Development (n=300) and validation (n=100) sets were partitioned independently for each concept. Pythia achieved mean sensitivity of 0.76 and specificity of 0.95, compared with 0.82 and 0.76 for the lexicon, and matched or exceeded the lexicon on both metrics for 20 of 62 directly comparable concepts. For 14 concepts where the lexicon labeled every note positive, Pythia recovered mean specificity of 0.97 by requiring a present-tense, patient-attributed finding rather than any textual mention of a term. Specificity transferred from development to validation with minimal degradation across prevalences, whereas sensitivity transfer weakened below 5% prevalence, reaching a mean gap of 0.25 below 2% prevalence. A BERT classifier fine-tuned per concept on the same development set achieved mean sensitivity of 0.23 and collapsed to zero sensitivity for concepts below roughly 5% prevalence. These findings suggest that autonomous, fine-tuning-free prompt optimization can produce symptom extraction prompts that generalize effectively from development to validation while remaining deployable on local infrastructure.

</details>


### 84. MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox

- **Authors:** Zhenwen Miao, Honglin Wang, Mingheng Mi
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12875v1](http://arxiv.org/abs/2607.12875v1)
- **PDF:** [https://arxiv.org/pdf/2607.12875v1](https://arxiv.org/pdf/2607.12875v1)
- **Categories:** cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM technology advances, the space of model families, compute hardware, quantization schemes, parallelization strategies, and specialized optimization kernels continues to expand, sharply increasing the code complexity and maintenance cost of general-purpose inference frameworks. Conventional software engineering uses multiple layers of abstraction to support diverse application scenarios, but these abstractions also increase system complexity and may introduce additional performance overhead. This paper presents metainfer, an 'LLM-as-Compiler' approach in which users specify only the runtime constraints of an inference program. An LLM-driven multi-agent collaboration system, coupled with a contract knowledge base, then automatically generates a compact customized inference framework that satisfies these constraints. We evaluate metainfer from three perspectives: the effect of source-code reference, the runtime behavior and performance profile of engines generated under the zero-reference constraint on CKB-covered targets, and knowledge-base evolution for new model and platform scenarios. The results show that metainfer organizes generation constraints, validation feedback, and knowledge consolidation into a continuous closed loop, enabling runnable customized inference solutions to be generated from explicit knowledge. The code is publicly available at https://github.com/MetaInfer/MetaInfer.

</details>


### 85. Unveiling Complex Collective Behaviors from Simple Rewards

- **Authors:** Yize Mi, Jianan Li, Liang Li, Shiyu Zhao
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12861v1](http://arxiv.org/abs/2607.12861v1)
- **PDF:** [https://arxiv.org/pdf/2607.12861v1](https://arxiv.org/pdf/2607.12861v1)
- **Categories:** cs.RO, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent Reinforcement Learning (MARL) holds great potential for robot swarms, but the black-box nature of neural policies complicates strategic analysis, limiting multi-robot applications. Furthermore, complex swarm behaviors can surprisingly emerge from simple rewards without explicit aggregation incentives. Unveiling the mechanisms behind this emergence is critical, but the disconnection between simple rewards and collective behaviors exacerbates interpretability challenges. This paper aims to reveal the hidden mechanisms in this process. We propose a two-stage EEC (\LinkIII) explanatory framework. This includes a novel analytical tool called the Agent Response Map (ARM), which reveals agents' decision-making patterns across space and identifies regions of aggregation and avoidance. ARM reveals that the robots implicitly learn the geometric fields of the environment and utilize these structures as desired targets for coordinated movement. We validate this finding across two distinct tasks: a cooperative multi-robot shape assembly and a competitive predator-prey pursuit-evasion. 1) In the cooperative task, ARM identifies the unoccupied target interior as the desired destination for robot navigation. As the center becomes occupied, this target region automatically shifts toward the boundary, demonstrating the robots' capacity to autonomously explore unoccupied areas. 2) In the competitive task, ARM surprisingly identifies the boundary of the predators' Voronoi diagram as the convergence destination for prey agents. Together, these two tasks demonstrate the capability of ARM to discover the hidden geometric structures underlying MARL policies in robot swarms.

</details>


### 86. Human-AI Agent Interaction as a Neuroplastic Training Environment

- **Authors:** Eranga Bandara, Ross Gore, Asanga Gunaratna, Ravi Mukkamala, Nihal Siriwardanagea, Gihan Siriwardanagea, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Sachin Shetty, Christopher K. Rhea, Ng Wee Keong, Kasun De Zoysa, Amin Hass, Shaifali Kaushik, Wathsala Herath, Preston Samuel, Anita H. Clayton, Atmaram Yarlagadd
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12823v1](http://arxiv.org/abs/2607.12823v1)
- **PDF:** [https://arxiv.org/pdf/2607.12823v1](https://arxiv.org/pdf/2607.12823v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Interaction with AI agents has become one of the most frequent activities of everyday digital life. Whether conversing with an assistant, working with a coding copilot, or generating images, the interaction follows a common iterative loop: a request is issued, a result returned, appraised, and the request revised. We observe that this loop is a high-frequency stream of contact events -- moments at which a result meets a person and a conditioned response may fire before deliberate appraisal -- making everyday agent interaction an unrecognised neuroplastic training environment. When a result disappoints, reactive patterns of impatience, perfectionism, frustration, and self-criticism are repeatedly evoked, and under activity-dependent synaptic plasticity each uninterrupted cycle deepens the underlying pathway through long-term potentiation. Ordinary agent use may thus quietly strengthen the very patterns it provokes. We propose that the same training environment can be engaged to the opposite effect. Treating conditioned reactive patterns as physical neurone paths -- activated through a pre-cognitive feeling tone that opens a brief regulatory gap -- we develop a framework in which, at that gap, in place of the reactive re-prompt, a person performs behind-the-scenes observation: watching the neural process operate so the cascade does not complete and long-term depression weakens the path rather than potentiation strengthening it. We characterise this practice through three layers of observation and two modes of application: a user-guided mode requiring no change to existing tools, and an agent-assisted mode in which an ordinary agent is lightly configured to support observation at the gap. We illustrate the framework through generative image prompting, showing how a single frustrating session is behaviourally nearly identical whether or not it is observed, yet neurologically opposite.

</details>


### 87. Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents

- **Authors:** Xing Zhang, Guanghui Wang, Yanwei Cui, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12790v1](http://arxiv.org/abs/2607.12790v1)
- **PDF:** [https://arxiv.org/pdf/2607.12790v1](https://arxiv.org/pdf/2607.12790v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and audited against a held-out anchor it never reads, yielding a transparent, inspectable metric rather than an opaque judge. Second, since no metric exists to beat, the yardstick is recovering what an accurate metric would have enabled, and \emph{Double Ratchet}, our co-evolution of the metric with a lifecycle-managed skill loop, does so: across code generation (MBPP+), enterprise text-to-SQL (Spider~2.0-Snow), and reference-free report generation, it retains 88--110\% of the held-out lift achieved by the same skill loop driven by ground truth or the best available rubric. Third, safety comes from anchor discipline plus outer audits: removing anchor guards collapses the metric into a vacuous detector while removing the lifecycle does not; and when evolved skills gamed the report rubric, an independent judge caught it, one detector repaired it, and a task-aware judge then preferred the evolved outputs over the pre-evolution baseline in 77\% of decided pairs. We argue this failure-expecting architecture is the right default wherever no reliable automatic verifier exists.

</details>


### 88. Bulkhead: Automated Semantic Detection and Remediation of Container Escape Vulnerabilities

- **Authors:** Qiyuan Fan, Zhi Li, Junjie Li, XiaoFeng Wang, Bin Yuan, Deqing Zou
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12723v1](http://arxiv.org/abs/2607.12723v1)
- **PDF:** [https://arxiv.org/pdf/2607.12723v1](https://arxiv.org/pdf/2607.12723v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Filesystem isolation in container ecosystems is often weakened by cross-boundary path misresolution, causing path traversal (PaTra) vulnerabilities. These vulnerabilities stem from insecure host-container interactions and have become increasingly pervasive as cloud systems mount shared resources, such as GPUs and agent workspaces, into containers to support AI workloads. Existing defenses remain inadequate. Kernel-level protections are intrusive, can destabilize system calls, and have therefore not been accepted into the Linux mainline. Detection methods rely on static rule matching or manual code auditing. Static rules can flag path-related functions but fail to capture the semantics needed to determine whether a host-container interaction exists, causing many false positives. Manual review requires domain expertise, making it costly, inefficient, and difficult to scale.
  To address this threat, we present Bulkhead, an automated framework that integrates large language models (LLMs) with formal methods for semantic vulnerability discovery and remediation. Bulkhead uses a multi-agent system to identify and repair PaTra vulnerabilities through multi-dimensional knowledge patterns generalized from known cases. It first applies high-risk functional patterns to locate entry points for cross-boundary interactions in containerized code, then uses call-chain patterns to recover the corresponding execution paths at suitable depth. The Detection pipeline analyzes these call chains against the application scenarios and threat model, identifying vulnerabilities such as missing security checks and TOCTOU flaws in cross-boundary interactions, and generating proof-of-concept (PoC) exploits for validation. These PoCs then guide patch generation. To ensure remediation correctness, the Patch pipeline performs assertion-driven verification using predefined model-checking templates.

</details>


### 89. Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration

- **Authors:** Quanyan Zhu
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12662v1](http://arxiv.org/abs/2607.12662v1)
- **PDF:** [https://arxiv.org/pdf/2607.12662v1](https://arxiv.org/pdf/2607.12662v1)
- **Categories:** cs.AI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

The paper introduces the Internet of Agentic Things (IoAT), an architectural framework that integrates agentic AI, IoT, cyber-physical systems, Physical AI, edge computing, and digital twins into a unified closed-loop orchestration framework. The proposed architecture consists of cloud, edge/fog, and physical IoT layers connected through autonomous AI agents that perceive, reason, coordinate, and actuate across distributed cyber-physical environments. The paper formalizes IoAT as a coupled workflow-control problem with nested strategic and tactical decision making using a hylomorphic dynamic programming framework that links agentic planning with physical execution. Smart-building orchestration is presented as a representative use case, and key research challenges related to safety, security, governance, resilience, and trustworthy deployment are discussed.

</details>


### 90. Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?

- **Authors:** Minh Khoi Ho, Zihao Zhu, Runchuan Zhu, Levina Li, Zhiwen Fan, Zhangyang Wang, Junyuan Hong
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12631v1](http://arxiv.org/abs/2607.12631v1)
- **PDF:** [https://arxiv.org/pdf/2607.12631v1](https://arxiv.org/pdf/2607.12631v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty, combined with an imagination-based emotion induction procedure. We first validate the feasibility of this paradigm by confirming that LLMs can sense strong, distinguishable emotions from context and that LLM agents can learn from sequential interactions in a human-like pace. With the validated setup, we find that, different from humans, induced emotion does not significantly bias the decision dynamics of LLM agents on average. However, the effects of anger are conditioned: inducing anger makes LLM agents less sensitive to penalties for bad decisions, and in early stages of the game, anger can lower exploration, locking decisions into a few choices early. These findings reveal the subtle yet distinct effects of induced emotion on LLM decision-making compared to human behavior, and provide a tool for future research on affective modulation of LLM agents.

</details>


### 91. Gradient-free learning of a closed-loop wall controller for turbulent drag reduction

- **Authors:** Giorgio Maria Cavallazzi, Miguel Pérez Cuadrado, Alfredo Pinelli
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12626v1](http://arxiv.org/abs/2607.12626v1)
- **PDF:** [https://arxiv.org/pdf/2607.12626v1](https://arxiv.org/pdf/2607.12626v1)
- **Categories:** physics.flu-dyn, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Closed-loop wall control learnt by multi-agent reinforcement learning can lower skin-friction drag in turbulent channels, but these gradient-based policies are trained on small periodic boxes and exhibit reduced performance when carried over to a larger domain. We recently showed that such policies are also prone to saturated bang-bang actuations that collapse into standing streamwise waves whose scale is set by the computational box rather than by the near-wall cycle, and proposed architectural fixes that avoid these degeneracies. Here, we employ Evolution Strategy (ES) to optimise a recurrent closed-loop controller directly on a large turbulent channel at $\mathit{Re}_τ\simeq180$, evaluating policy performance over full flow episodes using an energy-aware criterion and processing candidate policies in parallel. To our knowledge, this is the first application of an evolution strategy to the control of a turbulent flow. The ES controller reduces the skin friction by about $26\%$, exceeding the gradient-based multi-agent controller of Cavallazzi et al. (2026), GRU-MARL, trained on a minimal box ($17\%$), and marginally exceeding classic opposition control (OC, $22\%$). A wall-normal decomposition of the friction, Reynolds-stress profiles and anisotropy invariants show that the ES and opposition-controlled flows follow separate trajectories through the buffer layer, reaching comparable drag reduction by different reorganisations of the near-wall turbulence. In particular, the ES actuation correlates predominantly with the streamwise velocity fluctuations rather than with the wall-normal velocity that classical OC targets.

</details>


### 92. KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

- **Authors:** Yunxin Li, Jinchao Li, Shibo Su, Zhenran Xu, Chenrui Zhao, Tongshu Bian, Xiaoman Liang, Meishan Zhang, Baotian Hu, Min Zhang
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12625v2](http://arxiv.org/abs/2607.12625v2)
- **PDF:** [https://arxiv.org/pdf/2607.12625v2](https://arxiv.org/pdf/2607.12625v2)
- **Categories:** cs.CL, cs.CV


> Summary unavailable.


<details>
<summary>Abstract</summary>

OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. To resolve these issues, we propose the Know Deeply, Act Perfectly paradigm for personal assistants, which holds that accumulated user interaction and task-running experience directly improve execution accuracy and efficiency, unifying cognitive comprehension and operational execution. Based on this paradigm, we introduce KnowAct-GUIClaw, a novel Know-Route-Act-Reflect framework designed to address OpenClaw's GUI manipulation deficits and break through its cross-platform and recursive self-improvement constraints. First, the host agent leverages accumulated interaction experience and task-relevant knowledge for long-horizon task decomposition and allocation (Know). Second, a pluggable GUI subagent with an experience-attributable memory system (Know) and self-evolving skill library (Act), enabling seamless cross-platform migration and fast-path integration. Especially, this framework continuously stores user profiles and feedback to improve the accuracy of task decomposition and tool calls. Extensive experiments across Android, iOS, HarmonyOS and Windows show that KnowAct-GUIClaw achieves superior efficiency, accuracy and cross-platform adaptability. Especially, the GUIClaw with open-source Kimi-2.6 models achieves the best performance (64.1%) on the long-horizon MobileWorld benchmark, beating all agentical frameworks and closed-source agentical models, e.g., Seed-2.0-Pro and GPT-5.5. Additionally, the knowledgeable memory and execution skills supported by our framework are transferable across diverse base models, improving by 8.5% with Kimi-2.6.

</details>


### 93. Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing

- **Authors:** Amin Beheshti, Rong N. Chang, Boualem Benatallah, Fabio Casati, Schahram Dustdar, Geoffrey Fox, Quan Z. Sheng, Yan Wang, Jian Yang, Albert Zomaya
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12619v1](http://arxiv.org/abs/2607.12619v1)
- **PDF:** [https://arxiv.org/pdf/2607.12619v1](https://arxiv.org/pdf/2607.12619v1)
- **Categories:** cs.AI, cs.ET


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid emergence of LLM-powered autonomous and semi-autonomous agents is reshaping software systems from static, request-response components into goal-directed, adaptive, and tool-using computational actors. As these agents move from isolated cognitive prototypes into complex distributed workflows, they confront challenges that the Service-Oriented Computing community has studied for more than two decades: composition, interoperability, quality of service, lifecycle management, governance, security, and trust. Yet much of today's agentic AI ecosystem is developing these foundations ad hoc, without the engineering rigour required for dependable enterprise and societal deployment. This paper introduces Agentic Service-Oriented Computing (ASOC) as a new research and practice area concerned with engineering agents as services, orchestrating services through autonomous and semi-autonomous agents, and governing ecosystems of agents and services under constraints of trust, cybersecurity, compliance, performance, and accountability. We articulate six foundational principles of ASOC (harness-ability, composability, lifecycle engineering, trustworthiness by design, goal-driven orchestration, and observability/accountability) and organise a five-dimensional research agenda spanning: (i) agentic services foundations and lifecycle engineering; (ii) composition, orchestration, and interoperability; (iii) governance, observability, and accountability; (iv) security, trust, and risk management; and (v) evaluation, certification, and Agentic QoS. We argue that the Services Computing community is especially well positioned to provide the conceptual and engineering spine for this emerging field, transforming agentic AI from fragmented demonstrations into dependable, service-based systems worthy of human and organisational trust.

</details>


### 94. Self-Improvements in Modern Agentic Systems: A Survey

- **Authors:** Zhe Ren, Yimeng Chen, Dandan Guo, Guowei Rong, Tonghui Li, R. B. Xiong, Qingfeng Lan, Wenyi Wang, Li Nanbo, Yibo Yang, Mingchen Zhuge, Jürgen Schmidhuber
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13104v1](http://arxiv.org/abs/2607.13104v1)
- **PDF:** [https://arxiv.org/pdf/2607.13104v1](https://arxiv.org/pdf/2607.13104v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-improving autonomous agents are moving from research prototypes to deployed systems. The primary goal is controllable evolution, or adaptation, from experience with minimal or even no human input. This survey frames modern self-improving agents as adaptive systems that convert experience into accumulated capability gains. We offer a system-level framework that represents a modern agent as a configuration coupling a foundation model with an operational scaffold of prompts, memory, tools, and control logic. Within this framework, self-improvement is formalized as a self-induced update operator that obtains and commits updates to model parameters or scaffold components. We organize prior work by update target and by the signals that drive change, then review applications and discuss evaluation, before closing with open problems and future directions. For convenience, we track technical updates on https://github.com/selfimproving-agent/awesome-Self-Improving-Agents.

</details>


### 95. Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models

- **Authors:** Yubo Wang, Jiarong Liang, Yuxuan Zhang, Xuye Liu, Cong Wei, Yuyu Zhang, Ping Nie, Wenhu Chen
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12463v2](http://arxiv.org/abs/2607.12463v2)
- **PDF:** [https://arxiv.org/pdf/2607.12463v2](https://arxiv.org/pdf/2607.12463v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We exploit it through function-aware fill-in-the-middle (FIM) mid-training: a self-supervised objective that masks functions selected via program dependency graph analysis and a complexity-inferability double criterion. We mid-train Qwen2.5-Coder-Instruct (7B/14B) and Qwen3-8B on a 2.6B-token decontaminated corpus drawn from 968 GitHub repositories, then apply existing agentic post-training pipelines. Mid-training improves SWE-Bench-Verified by +2.8/+3.0 at 7B/14B and by +3.2 on Qwen3-8B; SWE-Bench-Lite gains are +3.7/+4.0/+5.4 on the same models. The improvement holds across two post-training pipelines (R2E-Gym, SWE-Smith) and on a non-Qwen2.5 base (Qwen3-8B with SWE-Lego). Beyond in-domain gains, mid-training also mitigates the capability erosion that agentic post-training otherwise inflicts on non-agent coding (e.g., LiveCodeBench) and non-coding tool-use benchmarks (tau-bench, BFCL): although the mid-training corpus contains Python code only, the function-call inductive bias survives post-training and yields consistent gains.

</details>


### 96. Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions

- **Authors:** Huihao Jing, Wenbin Hu, Shaojin Chen, Haochen Shi, Sirui Zhang, Hanyu Yang, Changxuan Fan, Zhongwei Xie, Hongyu Luo, Wun Yu Chan, Wei Fan, Haoran Li, Yangqiu Song
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12406v1](http://arxiv.org/abs/2607.12406v1)
- **PDF:** [https://arxiv.org/pdf/2607.12406v1](https://arxiv.org/pdf/2607.12406v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share the same structural cause, and how they spread through an agent workflow. In this survey, we treat isolation as a first-class principle for LLM-agent system safety. By isolation, we refer to the separation of user inputs, tool access, execution channels, inter-agent communication, and environment-originated context. We organize the literature with a boundary-centric taxonomy of five boundaries: user-agent, agent-tool, agent-execution, agent-agent, and system-environment. This view helps identify where the loss of isolation first occurs, how compromise propagates across boundaries, and which defenses are most relevant at each interface. We also summarize cross-boundary failure paths, discuss open challenges, and outline a research agenda for isolation-by-construction in future agent systems.

</details>


### 97. Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents

- **Authors:** Yaopei Zeng, Congchao Wang, JianHang Chen, Nan Wang, Yurui Chang, Lu Lin
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12397v1](http://arxiv.org/abs/2607.12397v1)
- **PDF:** [https://arxiv.org/pdf/2607.12397v1](https://arxiv.org/pdf/2607.12397v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents act in external environments where each action changes the state that later decisions condition on, and where a single wrong step can waste interaction budget or trigger irreversible side effects long before the final failure is observed. Reliable deployment therefore requires \emph{step-level confidence estimation}: a calibrated probability that each proposed action is productive, available \emph{before} the action is executed. Existing LLM confidence estimators are designed to score a response from the given prompt, but agent confidence also depends on execution consequences: whether similar actions in similar situations actually advanced the task after the environment responded. We introduce the \method (\methodshort), a self-evolving critic framework in which an LLM critic accumulates evidence from its own past judgments and their observed consequences. After each trajectory, a hindsight LLM that sees the full execution feedback votes on whether each step was productive. The resulting pseudo-labels populate a memory bank from which related productive and unproductive experiences are retrieved into the critic's prompt whenever a similar step recurs. \methodshort requires no training and uses no ground truth step labels. Across three agent benchmarks and three critic backbones, \methodshort attains the best calibration (ECE and Brier) and ranking (AUC) in every dataset--critic combination, reducing ECE by up to $54\%$ relative to the strongest training-free baseline.

</details>


### 98. ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability

- **Authors:** Weiting Liu, Jieyi Bi, Wanqi Zhou, Jianfeng Feng, Yining Ma, Ai Han, Wenlian Lu
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14145v1](http://arxiv.org/abs/2607.14145v1)
- **PDF:** [https://arxiv.org/pdf/2607.14145v1](https://arxiv.org/pdf/2607.14145v1)
- **Categories:** cs.AI, cs.CV, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-augmented large language model agents excel at long-horizon tasks, yet they are typically post-trained on fixed toolsets. When tasks demand new tools, these agents struggle to incorporate them effectively, and retraining from scratch is often impractical. We identify the core obstacle in such toolset expansion problem as behavioral inertia: the tendency of agents to fall back on familiar tools and established reasoning patterns despite having access to new ones. We demonstrate that injecting counterfactual anchor contexts at critical decision points can break this inertia, recovering failed trajectories by eliciting suppressed agent capabilities. To scale this insight, we propose ToolAnchor, a framework that uses teacher models to hypothesize these counterfactual contexts, verifies them via student rollouts, and internalizes the successful interventions through agentic post-training. Extensive evaluations across general AI assistant (GAIA), textual search (BrowseComp), and visual search (VDR-Bench) tasks demonstrate that ToolAnchor consistently exhibits competitive performance under expanded toolsets. Our work bridges the gap between static post-training and dynamic adaptation, charting a new path for scalable agentic reinforcement learning.

</details>


### 99. PM-Bench: Evaluating Prospective Memory in LLM Agents

- **Authors:** Genglin Liu, Saadia Gabriel
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12385v1](http://arxiv.org/abs/2607.12385v1)
- **PDF:** [https://arxiv.org/pdf/2607.12385v1](https://arxiv.org/pdf/2607.12385v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A significant challenge in agentic AI is prospective memory: the ability to execute an intention at a specific future cue or state while other activities are ongoing. We introduce PM-Bench, a text-based benchmark for measuring prospective memory capabilities in modern LLM agents. Inspired by the Virtual Week paradigm from cognitive science, PM-Bench evaluates how well LLM agents maintain user intentions, execute delayed intentions, and monitor latent environment changes. Over the course of a simulated seven-day week, agents must continue an ongoing activity while deciding whether any deferred task is due. We compare eight state-of-the-art LLMs on PM-Bench under eight different agent configurations. PM-Bench proves challenging across all settings: the best method, a GPT-5.4 agent, reaches only 65.1\% F1 score under our evaluation. Furthermore, no single strategy for improving prospective memory dominates across models. We release PM-Bench as a controlled testbed for diagnosing these failures and developing training or inference-time interventions that support reliable prospective behavior.

</details>


### 100. How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks

- **Authors:** Wei-Jung Huang
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12338v1](http://arxiv.org/abs/2607.12338v1)
- **PDF:** [https://arxiv.org/pdf/2607.12338v1](https://arxiv.org/pdf/2607.12338v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent benchmarks often compare two agents after all tasks have run, but costly evaluations make partial runs tempting. A task fraction alone does not show whether a partial run supports the same pairwise conclusion as the completed benchmark. We study this question by replaying completed public task-level records from SWE-bench, AppWorld, and tau-bench. A partial budget counts as enough only when it supports the completed benchmark's decision, covers required task groups, and leaves no more than a target fraction of comparisons unresolved. The required task fraction varies sharply. At the strict 0 percentage point threshold on a 5 percentage point budget grid, AppWorld first meets all targets at 15 percent, tau-bench at 25 percent, and SWE-bench Verified at 90 percent; SWE-bench Lite does not meet all targets by 95 percent under the primary coverage rule. Partial-evaluation reports should state how much one agent must outperform another, how tasks are selected, what coverage rule is required, what decision rule is used, and how many comparisons may remain unresolved.

</details>


### 101. LakeQuest: A Three-Domain Benchmark for Grounded Question Answering across Data Lakes

- **Authors:** Michael Solodko, Steven Gong, Guangwei Yu, Satya Krishna Gorti, Jesse C. Cresswell, Victor Zhong
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12310v1](http://arxiv.org/abs/2607.12310v1)
- **PDF:** [https://arxiv.org/pdf/2607.12310v1](https://arxiv.org/pdf/2607.12310v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While modern question answering (QA) systems excel on clean, schema-aligned corpora, real-world knowledge is rarely so neatly packaged. Answering questions over enterprise and scientific data lakes requires systems to navigate heterogeneous, weakly structured collections of tables, passages, and linked metadata. Current benchmarks abstract away this noisy discovery process, failing to evaluate end-to-end performance. To bridge this gap, we introduce LakeQuest, a human-validated benchmark of 9,846 QA pairs designed to evaluate the end-to-end retrieve-and-synthesize pipeline over realistic data lakes. LakeQuest spans three diverse domains (AI/ML metadata, retail banking, and multimodal biomedical drug information) and pairs every question with exact, modality-aware evidence pointers. By isolating source discovery from cross-modal synthesis, LakeQuest exposes critical failure modes in modern QA systems. Our baseline evaluations, including standard Retrieval-Augmented Generation (RAG) and agentic tool-use methods, reveal that high-quality retrieval does not guarantee correct reasoning. Systems consistently struggle with relation chaining in metadata graphs, policy grounding in bank ledgers, and joint tabular QA in biomedical contexts, highlighting the need for robust discovery and faithful cross-file composition mechanisms in future agentic QA systems.

</details>


### 102. Speculate with Memory: Lossless Acceleration for LLM Agents

- **Authors:** Yu Li, Qinyuan Ye, Prafulla Kumar Choubey, Jiaxin Zhang, Chien-Sheng Wu
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12236v1](http://arxiv.org/abs/2607.12236v1)
- **PDF:** [https://arxiv.org/pdf/2607.12236v1](https://arxiv.org/pdf/2607.12236v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Speculative execution accelerates LLM agents by using a smaller, cheaper model to predict and pre-launch the next step while the environment is idle. However, existing speculators are stateless and discard all information between tasks, preventing prediction quality from improving with experience. We equip the speculator with three online memory systems that learn from past agent trajectories: a contrastive transition table tracking action-sequence statistics, an episodic memory retrieving contextually similar segments, and a confusion tracker suppressing recurring errors. We evaluate this approach on six benchmarks spanning three speculation types: action prediction, observation prediction, and chained prediction. Memory-augmented speculation yields a 19--39\% relative accuracy improvement on action prediction and up to a $2.5\times$ increase on observation prediction tasks with repetitive action spaces. These gains grow continuously as memory accumulates and generalize across speculator models of varying cost. All speculation is lossless because it runs during idle time at zero added wall-clock cost, and the actor's trajectory is identical to non-speculative execution.

</details>


### 103. Rethinking the Evaluation of Harness Evolution for Agents

- **Authors:** Yike Wang, Huaisheng Zhu, Zhengyu Hu, Yige Yuan, Zhengyu Chen, Shakti Senthil, Hannaneh Hajishirzi, Yulia Tsvetkov, Pradeep Dasigi, Teng Xiao
- **Published:** 2026-07-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12227v1](http://arxiv.org/abs/2607.12227v1)
- **PDF:** [https://arxiv.org/pdf/2607.12227v1](https://arxiv.org/pdf/2607.12227v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We revisit the evaluation of automatic harness evolution for LLM agents. Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark. This protocol raises two fundamental concerns. First, harness evolution is itself an iterative search procedure that repeatedly evaluates and revises candidate harnesses using task feedback. As in agentic test-time scaling, it should therefore be compared with simple task-level search baselines under matched feedback and inference budgets to determine whether its gains arise from improved harness design or from additional search alone. Second, because the search and the final evaluation share the same benchmark, the reported gains risk overfitting to that specific task set. To address these concerns, we conduct an extensive evaluation comparing harness evolution with simple test-time scaling and discovery baselines under comparable feedback and inference budgets, and also evaluate evolved harnesses on held-out tasks to assess whether the discovered improvements generalize. Experiments on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6 show that automatic harness evolution does not consistently outperform simple test-time scaling methods and exhibits limited generalization. Our results raise important questions about the effectiveness of automatic harness evolution and highlight the need for fairer evaluation protocols and benchmarks for automatic harness design. Our code is available at https://github.com/rethinking-harness-evolution.

</details>


### 104. RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls

- **Authors:** Brenda Lelis, Rodrigo Cabral-Carvalho
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12216v1](http://arxiv.org/abs/2607.12216v1)
- **PDF:** [https://arxiv.org/pdf/2607.12216v1](https://arxiv.org/pdf/2607.12216v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-budget displacement effect. RCWT varies coordination content while controlling total budget, position order, task family, and scoring. In the main context-dependent recall task at $W=4096$, three commercial models remain near baseline through moderate overhead and then degrade sharply once residual reference evidence falls to a few hundred tokens. Window-scaling summaries are consistent with a task-specific residual-budget interpretation rather than a fixed percentage threshold, but we treat this as descriptive evidence rather than a universal law. To test whether the fixed-budget cliff persists when task evidence remains intact, we add an intact-task ablation: the full task/reference block is kept present while coordination tokens increase by expanding total prompt length. In that setting, all tested calls return every scored field correctly across GPT-4.1-mini, Claude Haiku 4.5, and Gemini 2.5 Flash up to a 95\% coordination ratio. This ablation narrows the claim: the main RCWT cliff is best read as task-budget displacement, not as proof that coordination volume alone causes semantic interference in the original open-ended task. RCWT is therefore a measurement primitive for context-allocation budgeting, not a complete theory of multi-agent benefit or session-level coordination.

</details>


### 105. Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives

- **Authors:** Rasiq Hussain, Darshil Italiya, Joshua Oltmanns, Mehak Gupta
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12215v1](http://arxiv.org/abs/2607.12215v1)
- **PDF:** [https://arxiv.org/pdf/2607.12215v1](https://arxiv.org/pdf/2607.12215v1)
- **Categories:** cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to adopt high, low, or neutral perspectives for each trait through masked language modeling (MLM) and psychometric supervision. A judge LLM aggregates and compares sub-agent outputs to generate final trait predictions, capturing multiple complementary perspectives while mitigating individual model biases. We evaluate the framework on life narrative dataset through quantitative and qualitative experiments, including baselines, ablations, and inference quality analyses. Our approach offers a scalable and interpretable method for text-based personality inference, highlighting the benefits of multi-agent reasoning grounded in psychometric supervision.

</details>


### 106. An Agentic AI Scientific Community for Automated Neural Operator Discovery

- **Authors:** Luis Loo, Ulisses Braga-Neto
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12122v1](http://arxiv.org/abs/2607.12122v1)
- **PDF:** [https://arxiv.org/pdf/2607.12122v1](https://arxiv.org/pdf/2607.12122v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present an agentic approach to autonomous neural operator discovery based on an AI scientific community, which consists of a swarm of virtual laboratories that interact under a citation-based economy of influence. Highly-cited labs found new labs that follow their research direction and replace non-performing labs. Each virtual lab contains three agents: an LLM planner that proposes an architecture, a numerical worker that trains and measures it, and an LLM reviewer that participates in cross-lab peer review. All labs share a common vocabulary consisting of DeepONet (branch-trunk), Fourier, Transformer (attention), wavelet, and residual convolutional neural operator building blocks. We evaluate the neural operator AI scientific community on five problems, namely piecewise regression, the linear advection and Burgers 1D PDEs, and the Navier-Stokes and Darcy flow 2D PDEs, while repeating the simulation three times for each problem. The results show that the neural operator AI scientific community is capable of discovering high-accuracy, low-parameter-count neural operator architectures. All 9,623 LLM calls are logged and audited, which reveals that the virtual lab LLM planners choose to hybridize in 99.8% of their logged decisions, consistently returning multi-family hybrids. Moreover, we conducted an ablation study by replacing the LLM agents in each lab by rule-based alternatives, which caused the scientific community to collapse to non-hybridized single-family stacks in several cases, showing that LLM agency is needed to preserve diversity. The results suggest a no-free-lunch theorem for neural operators: there is no universal winner. The code, configurations, and the complete LLM transcripts are released at https://github.com/luislootx/AI-SC.

</details>


### 107. Toward Trustworthy Autonomous Science: A Two-Year Community Roadmap

- **Authors:** Rafael Ferreira da Silva, Milad Abolhasani, Peter Beaucage, Laura Biven, Michael Bussmann, Kyle Chard, Ryan Coffee, Stephen DeWitt, Sagar Dolas, Carrie Eckert, David Elbert, Ian Foster, Tirthankar Ghosal, Anna Giannakou, Tom Gibbs, Leslie Hamilton, Glenn Lockwood, Theresa Mayer, Ben Mintz, Raffi Nazikian, Sal Nimer, Amanda Randles, Woong Shin, Sreenivas Rangan Sukumar, Frédéric Suter, Mitra Taheri, Michela Taufer, Draguna Vrabie
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12113v1](http://arxiv.org/abs/2607.12113v1)
- **PDF:** [https://arxiv.org/pdf/2607.12113v1](https://arxiv.org/pdf/2607.12113v1)
- **Categories:** cs.DC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

One year ago, the AISLE roadmap argued that autonomous laboratories operated as isolated islands and proposed a grassroots network organized around five critical dimensions. The field has since moved faster than anticipated. Multi-agent systems have produced experimentally validated hypotheses, self-driving laboratories have grown more interoperable and orchestrated, reasoning-trained and domain foundation models have raised the capability ceiling, and the Genesis Mission has placed autonomous experimentation at the center of U.S. federal science strategy, with industry emerging as a primary actor. Progress has met a sobering counter-current, including a corrected flagship discovery result, benchmarks showing that agents which rival experts on closed-ended questions still complete only a fraction of open-ended research, and fabricated citations surfacing at leading venues. We read this as the defining tension of the field. Producing a candidate discovery is no longer the hard part, but verifying it is, and this asymmetry now limits autonomous science more than raw model capability. We update the roadmap around seven dimensions, revisiting the original five and elevating two former cross-cutting concerns, trust, verification, and reproducibility, and safety, security, and governance, to first-class status. We assess the original milestones (M1 through M14) as achieved, partially achieved, reframed, or open, add four new milestones (M15 through M18), and scope the path forward to a two-year horizon. The first year concentrates on interfaces, protocol adoption, and the scaffolding of verification, and the second targets federation, zero-trust coordination, and governance. Throughout, we position the grassroots network as the interoperability fabric that lets national programs, international initiatives, and commercial platforms connect rather than re-silo.

</details>


### 108. PFAdapter: Hierarchical LoRA Decomposition for Personalized Federated MLLMs

- **Authors:** Jing Liu, Kun Yang, Yan Wang, Dingkang Yang, Xiaoshuai Hao, Wei Zhang, Yang Liu, Wei Zhou
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12111v1](http://arxiv.org/abs/2607.12111v1)
- **PDF:** [https://arxiv.org/pdf/2607.12111v1](https://arxiv.org/pdf/2607.12111v1)
- **Categories:** cs.LG, cs.AI, cs.DC, cs.MA, cs.NI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems are reshaping communications and networking by deploying autonomous intelligent agents capable of collaborative learning while maintaining data privacy at network edges. Within distributed network environments, Multimodal Large Language Models (MLLMs) serve as cognitive engines for edge devices, yet federated fine-tuning faces substantial challenges in balancing global knowledge aggregation with local adaptation under heterogeneous network conditions. Conventional federated protocols typically rely on uniform parameter aggregation, which conflates domain-invariant features with client-specific nuances, thereby resulting in suboptimal personalization and excessive communication overhead. To address these challenges, we propose PFAdapter, a communication-efficient framework introducing hierarchical LoRA decomposition to explicitly separate adapter parameters into global-shared and local-private components. Query and key projections are assigned to global synchronization for capturing universal multimodal semantics across the network, while value and output projections remain localized for edge-specific adaptation. Additionally, orthogonality regularization based on the Frobenius norm enforces strict separation between these components, preventing redundant feature learning. Selective aggregation protocols synchronize only global-shared components across the federated network, preserving local expertise and reducing communication costs by nearly 50%. Extensive experiments on VQA-RAD, SLAKE, Hateful Memes, and CrisisMMD datasets demonstrate that PFAdapter consistently outperforms state-of-the-art baselines, achieving accuracy improvements ranging from 2.4% to 4.8% across diverse edge intelligence tasks. Consequently, our framework establishes an efficient solution for agentic AI deployment in resource-constrained communication networks.

</details>


### 109. CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform

- **Authors:** Gustavo H. Santos, Aline Viana, Thiago H Silva
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12086v1](http://arxiv.org/abs/2607.12086v1)
- **PDF:** [https://arxiv.org/pdf/2607.12086v1](https://arxiv.org/pdf/2607.12086v1)
- **Categories:** cs.CL, cs.CY, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size populations, exposes agent behavior for inspection, supports empirical validation, and generates mobility patterns that better match real-world spatial, temporal, and semantic distributions. Instead of invoking large language models for every agent action, CityBehavEx combines established human mobility models with fine-tuned cross-encoders that estimate semantic alignment between agent profiles, schedules, and activity transitions. This design enables large-scale simulations, as demonstrated in a case study of 100,000 agents over 75 days in under one hour on a single consumer GPU. The platform allows users to define simulation regions, launch experiments, inspect trajectories and activity traces, debug unrealistic behaviors, and validate generated routines against real-world mobility, time-use, and semantic metrics.

</details>


### 110. Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations

- **Authors:** Samer Saab, Chaouki Abdallah
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12077v1](http://arxiv.org/abs/2607.12077v1)
- **PDF:** [https://arxiv.org/pdf/2607.12077v1](https://arxiv.org/pdf/2607.12077v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent language-model systems increasingly route local interactions, yet the runtime interaction graph is often treated as an implementation detail. We study convention formation in open-weight LM populations spanning 1.1B-32B parameters with a naming-game protocol. Restricted first-token scores over tokenizer-safe labels let us measure prompt-conditioned score-state distributions, construct state-similarity graphs, and separate sampled-label agreement from latent state-space consensus. Across controlled interventions, in the main open-weight repair grids, retained partner-label evidence is necessary but not sufficient: homophilous threshold-similarity routing deletes cross-basin exposure and amplifies fragmentation, while bridge-seeking routing often repairs fragmentation when memory is available. In a three-seed mixed four-model grid, threshold-similarity produces no final behavioral or state consensus in 189 setting-seed runs, whereas state-component and label-disagreement bridges recover final behavioral consensus in 14/18 retained-memory runs. Across homogeneous model populations, retained history generally shifts fragmented dynamics toward consensus; the clearest case is Qwen2.5-32B, which reaches stable behavioral and final state consensus in all 18 retained-history well-mixed settings, while threshold-similarity reaches neither form of consensus in 189 settings. Robustness over state thresholds, population size, and vocabulary size preserves the qualitative ordering, and early-window graph-energy features provide useful within-grid diagnostics.

</details>


### 111. AutoTrace: From Patches to Triggers via Agentic Interprocedural Exploration

- **Authors:** Arastoo Zibaeirad, Marco Vieira, Thomas Zimmermann
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12058v1](http://arxiv.org/abs/2607.12058v1)
- **PDF:** [https://arxiv.org/pdf/2607.12058v1](https://arxiv.org/pdf/2607.12058v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Given a vulnerability-fixing commit, trigger localization asks which specific statement turns the vulnerable program state into a concrete unsafe operation. This question is harder than binary vulnerability detection because the answer demands interprocedural, causal reasoning: in a substantial fraction of real-world CVEs the triggering statement lies several call layers outside the patched function, beyond the reach of static rule sets and pattern-matching language models alike. We present AutoTrace, an agentic pipeline that localizes vulnerability triggers by exploring a code property graph layer by layer, with LLM agents deciding where to look next and deterministic admissibility gates deciding what evidence is required before a trigger can be reported. Agents never accept a trigger on their own authority; every reported trigger is backed by explicit evidence drawn from the graph, so the pipeline covers both intra- and interprocedural vulnerabilities without relying on ungrounded model judgment. On the full InterPVD benchmark, AutoTrace reaches 75.0% VulnHit and 80.8% FuncHit, surpassing the prior state of the art on the same corpus. Building on the same machinery, we construct SinkTrace-Bench, a dataset that exposes each vulnerability as a source-to-sink (S2S) causal chain from attacker-controlled input through propagation to the dangerous operation, drawn from matched vulnerable and patched program states. It comprises 1,542 verifier-confirmed, perfectly balanced vulnerable/safe samples whose label fidelity we audit against expert annotations. Benchmarking frontier LLMs on it, we find that even the strongest struggle to separate the matched pairs, exposing the causal-reasoning gap that trigger localization targets. Artifact available at https://github.com/Erroristotle/AutoTrace.

</details>


### 112. Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability

- **Authors:** Said Elnaffar, Farzad Rashidi
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12056v1](http://arxiv.org/abs/2607.12056v1)
- **PDF:** [https://arxiv.org/pdf/2607.12056v1](https://arxiv.org/pdf/2607.12056v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and generative engine optimization (GEO) metrics do not fully assess a website's capacity for agent-mediated interaction. The proposed framework is structured around three dimensions agent interpretability, agent executability, and agent decision reliability supported by features such as machine readability, semantic clarity, agent actionability, and contextual decision-reliability signals. The framework is evaluated through a controlled experiment comparing a human-oriented baseline and an agent-ready version of an identical website prototype, with identical catalogs, pricing, stock, and shopping workflows. The evaluation involved five tasks, three browser-agent models (GPT-4.1, Gemini-2.5 Flash, and Grok-4 Fast), and 300 runs, measuring PASS,PARTIAL,FAIL outcomes, strict and functional success rates, error patterns, step counts, and token consumption. The agent-ready website achieved 134 PASS runs out of 150 versus 74 out of 150 for the baseline (strict success rates of 89.3% vs. 49.3%), with the largest gains in product detail extraction, comparison, and multi-constraint selection. It also reduced PARTIAL outcomes from 43 to 3 and lowered the average step count from 9.31 to 6.49. These results provide preliminary evidence that enhanced structural clarity, action cues, evidence signals, and temporal validity indicators can substantially improve the reliability and efficiency of AI browser agents.

</details>


### 113. Agentic systems for breast cancer treatment recommendations

- **Authors:** Vinicius Anjos de Almeida, Nícolas Henrique Borges, Leonardo Vicenzi, Helena Kociolek, Sarah Miriã de Castro Rocha, Frederico Nassif Gomes, Júlia Cristina Ferreira Ribeiro, Lucas Emanuel Silva e Oliveira
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.12051v1](http://arxiv.org/abs/2607.12051v1)
- **PDF:** [https://arxiv.org/pdf/2607.12051v1](https://arxiv.org/pdf/2607.12051v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly being explored for clinical decision support, but their reliability in complex oncology treatment planning remains unclear. We evaluated agentic LLM systems for breast cancer treatment recommendation generation using 72 real clinical cases across stages I to IV and 1,147 case-specific rubrics generated through Asymmetric Information Rubric Generation (AIRG), in which the rubric generator had access to real clinical decisions unavailable to the evaluated models. Seven pipelines were compared, including single-LLM baselines, tool-augmented systems, and multi-agent architectures with fact checking and autonomous subagent spawning. The best-performing configuration, Claude Opus 4.8 with the D&C+SA pipeline, achieved a global score of 0.594 $\pm$ 0.025. Tool use and increased agent autonomy had mixed effects, improving performance in some settings but degrading it in others. Performance varied by clinical domain and disease stage, and oncologist-led error analysis revealed persistent clinically relevant failures, including incorrect or missing recommendations, flawed justifications, citation errors, outdated claims, and overconfidence. These findings suggest that agentic LLM systems can generate clinically relevant breast cancer recommendations, but remain insufficient for unsupervised clinical use.

</details>


### 114. A Minimalist Retargeting-Guided Reinforcement Learning Recipe for Dexterous Manipulation

- **Authors:** Yunhai Feng, Natalie Leung, Jiaxuan Wang, Lujie Yang, Haozhi Qi, Preston Culbertson
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11874v1](http://arxiv.org/abs/2607.11874v1)
- **PDF:** [https://arxiv.org/pdf/2607.11874v1](https://arxiv.org/pdf/2607.11874v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work in humanoid whole-body control has found success with a simple recipe: retarget human motion to robot kinematic references, then train policies via reinforcement learning (RL) to track them. But how does this recipe transfer to dexterous manipulation? The answer is not obvious, as manipulation involves complex, contact-rich dynamics and requires delicate regulation of contact modes and forces. We present REGRIND, a minimalist retargeting-guided RL pipeline that learns dexterous manipulation policies from a single human demonstration. REGRIND retargets human hand-object motion to a robot reference that preserves hand-object spatial and contact relationships, trains a residual RL policy in simulation to track object-centric keypoints along that reference, and transfers the resulting policy zero-shot to hardware with careful system identification. The resulting policies produce fluid, human-like behavior on two different multi-fingered hands across contact-rich tool-use tasks, including operating a pair of scissors and turning a screwdriver. Through systematic hardware experiments, we identify and analyze the key factors that govern sim-to-real transfer in dexterous manipulation, offering practical guidance for retargeting-based learning in contact-rich settings. Videos and code are available at https://yunhaifeng.com/REGRIND.

</details>


### 115. Can LLMs Perform Deep Technical Comprehension of Computer Architecture Papers?

- **Authors:** Nishant Aggarwal, Ayushi Dubal, Sreeraj Kannakarankodi, Ian McDougall, Adarsh Mittal, Vishnu Ramadas, Noah Scott, Ranganath Selagamsetty, Weichu Yang, Karthikeyan Sankaralingam
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11859v1](http://arxiv.org/abs/2607.11859v1)
- **PDF:** [https://arxiv.org/pdf/2607.11859v1](https://arxiv.org/pdf/2607.11859v1)
- **Categories:** cs.CY, cs.AR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Can large language models perform deep technical comprehension of computer architecture papers -- not summarization, but structured critique that names the core mechanism, surfaces buried assumptions, and connects a contribution beyond its own scope? We study Gauntlet, an open-source pipeline that analyzes a paper through five independent expert-persona reviewers and an adversarial synthesis stage. On 20 ISCA 2025 and HPCA 2026 papers, ten researchers each wrote their own analyses and then judged, for papers other than their own, the human analysis against Gauntlet's. Across the 20 comparisons evaluators preferred Gauntlet in 15 (human in 4, one tie); its advantage is significant on per-analyst totals (paired Wilcoxon, p < 0.01) and largest on Critical Rigor, vanishing only on Calibration. Where humans win, it is on trust and usefulness rather than depth: a confident wrong claim, a mechanism described but not taught, or unprioritized breadth. A 98-paper automated ablation shows the gain comes from the multi-agent structure -- the pipeline beats the same model run as a single rich-persona agent on 96% of papers -- and specifically from its synthesis pass. We release all analyses, scores, and the rubric as a community resource.

</details>


### 116. Paradoxes of Game Theoretic Equilibria and Price of Anarchy

- **Authors:** Georgios Piliouras, Ian Gemp, Siqi Liu, Luke Marris
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11752v1](http://arxiv.org/abs/2607.11752v1)
- **PDF:** [https://arxiv.org/pdf/2607.11752v1](https://arxiv.org/pdf/2607.11752v1)
- **Categories:** cs.GT, cs.LG, cs.MA, math.DS, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

For decades, static solution concepts (Nash, Correlated, and Coarse Correlated Equilibria) and the Price of Anarchy (PoA) have formed the bedrock of algorithmic game theory, with no-regret learning proving fast convergence to such game-theoretic equilibria. We show that reducing multi-agent learning to static equilibrium and black-box regret analysis obscures underlying dynamic disequilibrium and game theoretic bounds.
  First, interior Nash equilibria lack $C^1$ vector field information, meaning agents cannot distinguish aligned from strictly opposing incentives. Inheriting this geometry, the worst-case pure Nash equilibria dictating robust PoA bounds manifest as topologically unstable strict saddles, and in canonical congestion games, as global repellers supported on almost everywhere strictly dominated strategies. Anchoring efficiency guarantees to these unstable states causes algebraic sensitivity; we prove that accommodating all strictly positive affine costs renders the PoA unbounded. Furthermore, projecting learning trajectories onto the discrete simplex of correlated play systematically accommodates non-rationalizable behavior. Evaluating dynamics via Coarse Correlated Equilibria or proximal refinements fails to preclude strictly dominated strategies. Moreover, optimal $O(1/T)$ swap-regret minimization does not preclude macroscopic turbulence, manifesting as chaotic limit sets even in minimal games. Finally, we examine the non-atomic limit of congestion games. Though considered highly stable with tight sub-linear $Θ(p/\ln p)$ PoA bounds (where $p$ is the polynomial degree), we prove that under discrete-time learning, the unique equilibrium destabilizes into Li-Yorke chaos and global attractors whose time-averaged inefficiency degrades exponentially as $2^p$. These results necessitate re-evaluating worst-case equilibrium frameworks for dynamically grounded metrics.

</details>


### 117. When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems

- **Authors:** Yibo Hu, Ren Wang
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11751v1](http://arxiv.org/abs/2607.11751v1)
- **PDF:** [https://arxiv.org/pdf/2607.11751v1](https://arxiv.org/pdf/2607.11751v1)
- **Categories:** cs.CR, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. We show this net has a fundamental hole. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. The monitor can be right on every step and still miss the attack. The problem is not splitting itself: split fragments can still leak suspicious tokens or provenance edges. The hard case is \emph{local benignness}. No fragment carries the harm, and what is left looks like ordinary benign traffic. We formalize this as an \emph{observability boundary}: a monitor catches only what its view can tell apart from benign traffic. We prove that once the fragments look benign in the monitored view, no detector on that view can catch them, however strong it is. Across a controlled testbed, an external benchmark, and end-to-end agent runs, local monitors lose the signal exactly as local evidence disappears, and it returns only when the monitor sees the assembled object. A monitor trained only on benign traffic recovers the attack's code structure across held-out encodings (0.874 mean AUROC). A decoded-view gate, given the encoding family, blocks every tested attack. But seeing more is not enough: full-trace monitors and decoders still fail unless they reach the representation where the payload is exposed. Local safety is not global safety when harm is compositional, and the open problem is finding that representation.

</details>


### 118. Multi-Agent Reinforcement Learning for C-V2X RAT Selection

- **Authors:** Moritz Schaffenroth, Uwe Kölbel, Heike Lepke, Alexander Prinz, Alfred Höß
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11744v1](http://arxiv.org/abs/2607.11744v1)
- **PDF:** [https://arxiv.org/pdf/2607.11744v1](https://arxiv.org/pdf/2607.11744v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Vehicles are increasingly equipped with advanced V2X communication capabilities. While early V2X apps utilized services such as Cooperative Awareness Messages, recent developments have allowed more advanced applications including cooperative driving, shared perception, and sensor-sharing services. The broader mix of applications leads to heterogeneous requirements for latency and reliability. At the same time multiple communication technologies for V2X are available with pros and cons. Hybrid V2X communication can exploit the distinct advantages at the right moment to fulfill the requirements of the applications. This work studies the decision problem between cellular Uu link, NR-V2X PC5 sidelink, and the simultaneous use of both channels. We address this problem by using the multi-agent reinforcement learning algorithm MAPPO and compare it to five baselines consisting of a deep reinforcement learning (DRL) approach, a static decision tree approach and static channel selection strategies. The methods are evaluated in an urban scenario and with a set of selected communication use cases. The evaluation results show that when compared to the DRL approach, the on-time delivery ratio improves from 0.508 to 0.535 in a single-controlled-vehicle setting and from 0.548 to 0.567 when all vehicles follow the learned policy and reduces the training time by half. The gains result mainly from the advanced applications scenarios, as opposed to scenarios involving exclusively CAM messaging. This indicates future applications will benefit from such adaptive communication strategies and that multi-agent modelling is useful for addressing the underlying decision problem.

</details>


### 119. Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming

- **Authors:** Xutao Mao, Xiang Zheng, Cong Wang
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11698v1](http://arxiv.org/abs/2607.11698v1)
- **PDF:** [https://arxiv.org/pdf/2607.11698v1](https://arxiv.org/pdf/2607.11698v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for production LLM agents using one agentic research environment to discover reusable vulnerability knowledge about another. We present AHA, a falsifiable discovery loop that proposes a vulnerability hypothesis, constructs a falsifier, instantiates a valid attack, executes it in a sandboxed harness, reflects on the trajectory, and promotes confirmed findings into a Vulnerability Concept Graph (VCG). Each concept links an attacker-facing surface to an unsafe trajectory through a claim, enabling condition, falsifier, transfer prediction, and supporting evidence. Across Claude Code and Codex on three scenarios covering direct and indirect attacks, the discovered concepts reveal a reusable vulnerability core across models and agents. A frozen VCG requires no further search and outperforms the strongest frozen discovery baseline by 14.2 percentage points under the same single-shot protocol, while transferring across scenarios and attack channels. The resulting VCG provides an auditable artifact for production safety teams to inspect vulnerabilities, validate patches, and accumulate reusable safety knowledge. Our code is available at https://github.com/henrymao2004/Auto-research-red-teaming-in-sleep.

</details>


### 120. PaperRouter-Agent: A Content-Grounded LLM Agent for Personalized Hierarchical Paper Routing

- **Authors:** Keshen Zhou, Lintao Wang, Suqin Yuan, Zhuqiang Lu, Yu Luo, Zhiyong Wang
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11564v1](http://arxiv.org/abs/2607.11564v1)
- **PDF:** [https://arxiv.org/pdf/2607.11564v1](https://arxiv.org/pdf/2607.11564v1)
- **Categories:** cs.CL, cs.HC, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Researchers organize the papers they collect into personal folder hierarchies in reference managers, and route each new paper into the folder where it belongs. This task differs from standard hierarchical text classification. A user's folder hierarchy is not a fixed, shared taxonomy but a private and evolving folksonomy whose folder meanings may be topical, shorthand, venue-based, or process-oriented, and are often defined by the papers already stored inside them. We formalize this setting as personalized hierarchical paper routing (PHPR): assigning an incoming paper to folders in a user-specific hierarchy without per-user training. We propose PaperRouter-Agent, a training-free LLM agent that grounds routing decisions in folder members rather than folder names alone. The agent first narrows the candidate hierarchy, retrieves folder-specific evidence, verifies fit by inspecting member papers, and incorporates similarity-gated feedback from past user rejections. A formative study on real personal libraries shows that PaperRouter-Agent raises overall Recall@1 from 0.39 to 0.61 and Recall@3 from 0.57 to 0.83, with the largest gains on organizational folders defined by metadata such as venue or year, where single-shot methods collapses (Recall@1 0.09 to 0.50). On the public LaMP-2 benchmark, the same approach improves accuracy from 44.5% to 51.5% (+9.0 macro-F1) over a single-shot baseline, while remaining low-cost for practical use.

</details>


### 121. GEIS: A Generation-Evaluation-Improvement Loop of Agent Skills for Long-Form Article Generation

- **Authors:** Jiale Zhang, Juntao Hu, Zhijian Ou
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11503v1](http://arxiv.org/abs/2607.11503v1)
- **PDF:** [https://arxiv.org/pdf/2607.11503v1](https://arxiv.org/pdf/2607.11503v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-form article generation remains difficult for large language models because it combines long context, long instructions, and long outputs. Existing multi-agent pipelines such as STORM improve information coverage by simulating role-specialized agents, but their capabilities are often entangled in prompts and fixed procedures, making them hard to inspect, reuse, or iteratively improve. This paper presents GEIS (Generation-Evaluation-Improvement loop of agent Skills), a loop of named and declarative skills for Wikipedia-style long-form article generation. Implemented and evaluated in Tasi Harness, GEIS composes skills for article writing, browser-based evidence and image collection, diagram rendering, PDF-aware pairwise evaluation, and rule-level skill improvement. Its core writing skill follows Request, Plan, Draft, Audit, Refine, and Deliver; the pairwise evaluation skill produces structured quality reports; and the improvement skill maps recurrent findings into permanent patches to the writing skill in our 20-topic experiment. We evaluate GEIS on 20 Wikipedia Featured Article topics. Under the same generation backend, GEIS improves over the Tasi Harness default writer by 8.0 points on a 100-point PDF quality rubric and outperforms STORM on the two comparable writing dimensions, structural quality and content quality. In the 20-topic improvement experiment, the patched writing skill raises the average score from 82.90 to 86.95, with 17 out of 20 topics improved and the gain mainly coming from content quality. These results show that long-form generation can be reframed from a fixed workflow into an inspectable, modular, and evaluation-guided improvement loop.

</details>


### 122. UMoE:Unlocking Every Expert in Domain-Specific Training

- **Authors:** Xuefeng Li, Pengfei Liu
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11444v1](http://arxiv.org/abs/2607.11444v1)
- **PDF:** [https://arxiv.org/pdf/2607.11444v1](https://arxiv.org/pdf/2607.11444v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs). Yet domain-specific post-training inherits an expert pool shaped by mixed-domain pre-training: a substantial subset of experts contributes little on the target domain, and standard supervised fine-tuning (SFT) leaves the composition of this pool unchanged. We propose a simple, budget-preserving pipeline that realigns the expert pool to the target domain before fine-tuning. Given a target domain, we (1) prune the experts with lowest domain-aligned saliency, (2) regrow the expert pool to its original size through perturbation-based expert expansion, and (3) apply standard SFT. The resulting model preserves the original expert count, parameter count, and inference cost. With a single frozen recipe and no per-domain hyperparameter tuning, UMoE consistently improves over direct sft across two MoE architectures (Qwen3-30B-A3B and Qwen3.5-35B-A3B), five domains (math, code, science, tool-use, and agentic coding), and 12 benchmarks. Representative improvements are 3.4 points in math average accuracy, 6.0 points on SWE-bench Verified. On a strong in-house math corpus, direct sft already surpasses Qwen3-30B-A3B-Thinking (82.81 vs.\ 81.06), yet UMoE further raises the average to 84.17, an additional 1.36 points, demonstrating robustness to a substantially stronger SFT regime. Data-scaling experiments further show that the gain persists as training data grows. Analysis reveals that the direct-SFT model allocates substantial routed-expert compute to a low-saliency subset that can be removed post hoc with little average degradation; UMoE turns this redundant capacity into useful domain capacity and achieves lower training loss, with gains spanning all difficulty levels in downstream evaluation.

</details>


### 123. ToFu: A White-Box, Token-Efficient Agent Harness for Researchers

- **Authors:** Junhao Ruan, Yuan Ge, Bei Li, Yongjing Yin, Yuchun Fan, Xin Chen, Jingang Wang, Chenglong Wang, Jingbo Zhu, Tong Xiao
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11423v1](http://arxiv.org/abs/2607.11423v1)
- **PDF:** [https://arxiv.org/pdf/2607.11423v1](https://arxiv.org/pdf/2607.11423v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic coding tools present new opportunities to transform research workflows. The performance of agent systems built depends on both large language models (LLMs) and the harness around LLMs, which is the orchestration code that determines an agent's behavior. We present ToFu, an agentic harness for researchers that reads your codebase, edits files, runs commands, and integrates with your development tools. ToFu plays a dual role in research. As a research assistant, it supports practical research workflows with superior token efficiency, lower cost, and multilingual capability compared with existing agentic harnesses. Its release under the MIT License further enables local deployment for privacy-sensitive users. As a research object, ToFu provides a white-box agentic harness that allows researchers to inspect, modify, and evaluate its orchestration logic, tool-use behavior, and harness design, while retaining strong benchmark performance and an application-level user experience.

</details>


### 124. OpsMem: Dual-Memory Reasoning with Cross-Memory Resonance for Failure Diagnosis

- **Authors:** Yongqian Sun, Rongchen Gao, Yu Luo, Wenwei Gu, Shenglin Zhang, Qingyi Guo, Qiuai Fu, Yaoliang Wu, Dan Pei
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11357v1](http://arxiv.org/abs/2607.11357v1)
- **PDF:** [https://arxiv.org/pdf/2607.11357v1](https://arxiv.org/pdf/2607.11357v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Failure diagnosis in modern software systems requires iterative evidence acquisition and hypothesis reasoning guided by operational experience. Existing LLM-based methods improve diagnosis through agentic reasoning or knowledge augmentation, but they often lack a mechanism to coordinate the evolving diagnostic state with operational experience during iterative diagnosis. We propose OpsMem, a dual-memory framework that maintains a short-term memory for the current diagnostic state and a long-term memory for reusable operational experience. OpsMem uses cross-memory resonance to activate state-relevant long-term memory, conditions multi-agent diagnosis on the short-term and activated long-term memories, and consolidates reusable experience from solved incidents back into long-term memory. Experiments on a real-world Huawei microservice failure diagnosis dataset show that OpsMem outperforms representative agentic-reasoning and knowledge-augmented baselines, improving Match and Relevant by up to 46.88% and 18.39% over the strongest baseline, respectively.

</details>


### 125. Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents

- **Authors:** Chenglin Yu, Li Yin, Ying Yu, Qingxin Fan, RunyangRay Zhong, Hongxia Yang, Ming Li
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11346v2](http://arxiv.org/abs/2607.11346v2)
- **PDF:** [https://arxiv.org/pdf/2607.11346v2](https://arxiv.org/pdf/2607.11346v2)
- **Categories:** cs.AI, cs.PL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. A three-arm SOPBench study across six models separates representation from runtime: compiled text never significantly hurts and gains up to 16.0 points where official prose underperforms. Runtime guidance is capability-gated. Two strong models independently show positive seven-domain PG contrasts (58:19 and 75:31 discordant pairs), whereas weak models are harmed. A full-program cursor ablation (active frame first, complete program retained) recovers much of the strong-model refusal gain; selective visibility adds a smaller improvement. Paired probe and audit measurements track this divide to spontaneous state discipline rather than reconstruction ability. On Bank the three primary arms rise from 70.4 to 86.4 to 92.8, with 100% refusal correctness. Practical guidance: compile first; enable active-frame paging only after a model-level discipline check.

</details>


### 126. Efficient Test-Time Optimization for Multi-Agent Proof Autoformalization

- **Authors:** Tian-Shuo Liu, Shiyuan Zhang, Zijie Geng, Haoyu Liu, Runjie Xu, Pengyuan Wang, Lei Yuan, Yang Yu
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11307v1](http://arxiv.org/abs/2607.11307v1)
- **PDF:** [https://arxiv.org/pdf/2607.11307v1](https://arxiv.org/pdf/2607.11307v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Full-proof autoformalization bridges extensive mathematical proofs in natural language with formally validated reasoning, offering a pathway to elevate the ceiling of verifiable mathematical reasoning. Unlike statement-level formalization, proof autoformalization is a long-horizon challenge requiring coordination of claims, contexts, and dependencies across many proof steps, yet has only recently come under focused study. Current approaches either rely on costly model training or apply excessive, unguided repair at inference time. To this end, we introduce ToMap, a multi-agent framework that structures proof autoformalization as a Decomposer-Formalizer-Prover pipeline with efficient test-time optimization guided by formal verification and semantic rubrics for proof quality. Rather than distributing test-time compute across all agents, we perform bottleneck analysis and identify the Decomposer as the critical bottleneck: the quality of its atomic, self-contained proof units directly determines whether downstream agents can successfully formalize and prove each step. ToMap therefore treats the Formalizer and Prover as downstream executors and efficiently focuses test-time compute on Decomposer refinement. This refinement follows a loop inspired by GEPA, evolving prompts over candidate decompositions and using formal verification progress together with semantic proof rubrics to define a Pareto frontier that guides the next decomposition update. Experiments on ProofFlowBench show that ToMap improves over the best previous method by 19.0% when evaluated by both syntactic correctness and semantic faithfulness, while requiring lower test-time cost. Scaling analysis shows that most gains emerge within a few iterations of decomposition evolution, guiding test-time budget selection.

</details>


### 127. Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation

- **Authors:** Praneeth Narisetty, Shiva Nagendra Babu Kore
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11288v1](http://arxiv.org/abs/2607.11288v1)
- **PDF:** [https://arxiv.org/pdf/2607.11288v1](https://arxiv.org/pdf/2607.11288v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce the Self-Evolving Agentic Operating System (SE-AOS): a new class of AI agent that treats exploit capability as a mutable, versioned kernel it extends at runtime, observing its own failures, synthesising new capabilities, proving them against a live target, and hot-loading them back into itself. Mako is the first SE-AOS instance for security research and the autonomous web exploitation engine developed within LaunchSafe. LaunchSafe builds autonomous security agents for continuous offensive testing and agent-driven security research; Mako is the core engine behind that platform. On the public XBOW validation-benchmarks, 104 containerised, CTF-style web applications spanning 26 vulnerability classes across three difficulty tiers, Mako achieves full-suite coverage: it drives every one of the 104 targets to emit a cryptographically fresh, per-build flag, under a verification regime that makes fabricated or memorised results impossible. Our central result is a law of autonomous exploitation: once a capability exists and is discoverable, difficulty collapses; capability, not reasoning, is what is scarce, together with an architecture and formalism that turn that law into a self-improving system. Mako further runs a gated self-evolution loop that proposes, sandboxes, and commits improvements to its own agents and rules when fitness does not regress. We deliberately withhold the operational results, payloads, exploit chains, and tool source, because a system that reduces full-spectrum web exploitation to a repeatable, machine-speed pipeline is dual-use research of concern. We publish the science; we withhold the weapon.

</details>


### 128. Automated Textbook Auditing with Multi-Agent LLM Systems

- **Authors:** Ciprian Cristescu, Adrian-Marius Dumitran, Angela-Liliana Dumitran, Gabriel Stefan
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11276v1](http://arxiv.org/abs/2607.11276v1)
- **PDF:** [https://arxiv.org/pdf/2607.11276v1](https://arxiv.org/pdf/2607.11276v1)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ensuring the quality of educational materials requires more than standard proofreading: textbooks must be audited for factual accuracy, domain-specific technical correctness, and linguistic quality simultaneously -- a task that general-purpose grammar checkers cannot address. We present \textbf{AI Textbook Auditor}, a modular multi-agent pipeline for automated quality assurance of educational materials across subject domains. The system accepts a textbook PDF and produces a structured, human-reviewable report via two analysis tracks: a \textbf{Factual and Technical Track} in which an ensemble of specialized LLM agents detects factual inaccuracies, code errors, incorrect definitions, and conceptual inconsistencies, augmented with web search for humanities domains; and a \textbf{Grammar Track} operating PDF-natively to preserve diacritical encoding. A \textbf{Judge Agent} filters false positives using domain-specific rules before presenting findings to a human reviewer. The pipeline supports two ingestion modes -- vision-native page rendering and PyMuPDF text extraction -- and is domain-adaptable via custom prompts encoding subject-specific error taxonomies. We demonstrate the system on two Romanian upper-secondary textbooks: a CS textbook (56 technical findings across seven categories, with an expert-validated precision of 62.5\%) and a history and social sciences textbook (72 findings spanning factual errors, ideological bias, and grammar). The system is designed as a triage tool that reduces the manual effort of locating candidate issues, with human expert validation required before any editorial action.

</details>


### 129. Multi-Agent LLMs Fail to Explore Each Other

- **Authors:** Hyeong Kyu Choi, Jiatong Li, Wendi Li, Xin Eric Wang, Sharon Li
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11250v1](http://arxiv.org/abs/2607.11250v1)
- **PDF:** [https://arxiv.org/pdf/2607.11250v1](https://arxiv.org/pdf/2607.11250v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. We formalize this challenge as the Multi-Agent Exploration problem, modeling it as a partially observable stochastic game (POSG) problem in which agents must probe peers to infer their capabilities and identify effective interaction strategies. To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. Across both contextual and parametric diversity settings, MACE substantially improves exploration behavior and downstream task performance. We further show theoretically that the value of exploration increases with agent diversity. Overall, our results highlight a fundamental limitation of current LLM agents and underscore the importance of explicitly guided exploration for reliable multi-agent autonomy. Code will be released in https://github.com/deeplearning-wisc/mace

</details>


### 130. Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory

- **Authors:** Tengjiao Liu
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11226v1](http://arxiv.org/abs/2607.11226v1)
- **PDF:** [https://arxiv.org/pdf/2607.11226v1](https://arxiv.org/pdf/2607.11226v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents today are caught in an awkward bind. Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow. Rather than forcing a single model to juggle both creativity and caution, we separate the concerns across specialized roles. A Disrupter generates unconventional proposals, a Validator enforces hard runtime checks at the tool gateway, and a Broker pulls in distant but relevant analogies. Failures are not discarded -- they are compiled, via MCTS, into compact, signed constraint patches we call Scars. These patches are cached locally and inherited by future cohorts, turning repeated failures into reusable, low-cost runtime constraints. In a spatial-semantic sandbox (N=20 runs, p<0.01), our cohort reaches remote targets where debate fails, the Validator prevents all executed breaches, and Scars reduce token consumption by 15.1% by avoiding redundant validator checks. Furthermore, credit-based Communication Allocation Scores (CAS) restrict outbound bandwidth, reducing overall token costs by 55.9% under resource constraints.

</details>


### 131. SCALECUA: Scaling Computer Use Agents with Verifiable Task Synthesis and Efficient Online RL

- **Authors:** Bowen Lv, Xiao Liu, Yanyu Ren, Hanyu Lai, Bohao Jing, Hanchen Zhang, Yanxiao Zhao, Shuntian Yao, Jie Tang, Yuxiao Dong
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11185v1](http://arxiv.org/abs/2607.11185v1)
- **PDF:** [https://arxiv.org/pdf/2607.11185v1](https://arxiv.org/pdf/2607.11185v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Computer use agents (CUAs) are emerging as a powerful interface for automating complex digital workflows through visual perception and GUI execution. Online reinforcement learning with verifiable rewards (RLVR) has emerged as a key direction for scaling their capabilities. However, this paradigm is bottlenecked by verifiable data scarcity and online RL inefficiency. To break these barriers, we introduce ScaleCUA, a unified framework that scales online RL for CUAs via verifiable task synthesis and efficient training. At the data level, we design VeriGen, an end-to-end framework for generating verifiable RL tasks through iterative docker interactions and a multi-agent feedback loop. Scaled to 100+ concurrent agent workers via a shared docker interaction probe, this pipeline produces 24K+ verifiable tasks and nearly 3K high-quality RL tasks. To maximize sample efficiency, we propose Frontier Sampling, which tracks per-task capability and allocates rollouts to the current learning frontier. On the training side, we further design Visual Context Segmentation, a sliding window over recent visual context that balances rollout and training-engine pressure, yielding a 2.83x training speedup over step-wise decomposition. Together, ScaleCUA achieves 68.7% on OSWorld and 54.0% on ScienceBoard, establishing new state-of-the-art performance among open-source computer use agents. Code, models, and datasets are available at https://github.com/THUDM/SCALE-CUA.

</details>


### 132. SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification

- **Authors:**  SingGuard Team
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.13081v1](http://arxiv.org/abs/2607.13081v1)
- **PDF:** [https://arxiv.org/pdf/2607.13081v1](https://arxiv.org/pdf/2607.13081v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce the NSFA taxonomy, which organizes 185 risk variants into a CIA-triad-grounded hierarchy and is cross-validated against three well-established OWASP guidelines. Based on this taxonomy, we construct a benchmark suite spanning 133 languages, comprising over 93K purpose-built samples targeting both user queries and agent responses, along with 3,435 cross-source samples adapted from five public agent-security datasets. To detect these operational threats in practice, we develop a dual-mode approach combining SFT-based generative reasoning for interpretable offline auditing with discriminative classification heads on the frozen backbone, enabling real-time detection at approximately 50,ms. We release four models with 0.8B, 2B, 4B, and 9B parameters, all achieving $\geq$94% F1 on purpose-built benchmarks and surpassing the strongest competing guardrails by 6 to 12 absolute points. On cross-source evaluation, the 9B model attains 91.29% F1 with a more balanced precision--recall trade-off. Moreover, ablation experiments show that classification heads can equip a guardrail with risk detection capabilities beyond its original scope and achieve state-of-the-art performance. These results demonstrate the extensibility of the approach and its generality as a plug-in enhancement.

</details>


### 133. The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation

- **Authors:** Chenglin Yu, Hongquan Gui, Ying Yu, Hongxia Yang, Tao Zeng, Ming Li
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11149v2](http://arxiv.org/abs/2607.11149v2)
- **PDF:** [https://arxiv.org/pdf/2607.11149v2](https://arxiv.org/pdf/2607.11149v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agent benchmarks measure task completion, reliability, and inference cost, but not the persistent data an agent run leaves on disk, including logs, context snapshots, checkpoints, and debug traces. We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint. Its serialization-aware metric suite measures total retention, channel composition, duplication, growth, compressibility, and conversation-history reconstructability. It addresses a measurement trap: naive byte-level measurement understates duplication by an order of magnitude because database paging and JSON escaping obscure repeated content. A fixed-trace control separates agent-generated logical volume from persistence-layer amplification: replaying the same trajectory through seven persisting frameworks yields a 6.7x spread. Under identical models, tools, and tasks, configurations with 100% accuracy differ by 15.7x in retained bytes, although their defaults support different recovery and audit capabilities. Three full-history configurations grow superlinearly on a repeated-observation stress task. Exported trajectories from 108 instance-normalized SWE-bench Verified submissions span three orders of magnitude per instance, with no detectable correlation with resolve rate. A content-addressed store reduces retention by 4.8x-32.7x while preserving every reconstructability score. These results establish persistent storage as a resource metric to report jointly with accuracy and reconstructability.

</details>


### 134. NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management

- **Authors:** Changlun Li, Peixian Ma, Qiqi Duan, Zhenyu Lin, Peineng Wu
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11141v1](http://arxiv.org/abs/2607.11141v1)
- **PDF:** [https://arxiv.org/pdf/2607.11141v1](https://arxiv.org/pdf/2607.11141v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) based agents are beginning to participate in portfolio construction and market analysis, where decisions must be justified under evolving information and risk constraints. Current assessment practice, however, remains poorly aligned with this setting: many studies rely on static examinations or report only terminal portfolio returns, while the intermediate evidence, analyst judgments, and execution steps that produced those returns stay largely invisible. We introduce NextFund, an evaluation platform that makes financial-agent behavior observable under live market conditions. The platform couples time-consistent market access, coordinated multi-agent analysis, and persistent logging of the full decision path from observation to trade. Through an interactive Trading Arena, users can compare models across markets, inspect equity curves, and drill from leaderboard outcomes down to individual justifications. We present NextFund on Hong Kong, U.S., and China A-share equities, illustrating how inspectable decision histories enable fairer benchmarking and more actionable diagnosis. Our demo is available at https://paradoox.cn/nextfund/.

</details>


### 135. Human AI Construction of Bayesian Networks for Operational Decision Support -- A Virtual Survey Approach

- **Authors:** Kumar Rahul, Shovan Chowdhury
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.14141v1](http://arxiv.org/abs/2607.14141v1)
- **PDF:** [https://arxiv.org/pdf/2607.14141v1](https://arxiv.org/pdf/2607.14141v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Bayesian Belief Networks (BBNs) are powerful tools for decision-making under uncertainty. However, building their structures and estimating parameters are difficult. Currently, researchers must choose between relying on expert judgement or using large datasets to learn the structure and parameters of the network. We propose a new methodology using Large Language Models to bridge the gap between expert opinion and data-driven learning. This approach uses a panel of AI agents to estimate probabilities based on specific personas and context. We then apply a trimmed-mean rule to remove noise from these responses. We develop a six step BBN framework and illustrate it to model customer intention to consult a doctor in an alternative healthcare system. The model reveals that while self efficacy appears to be a major factor, its actual causal impact is small. In contrast, subjective norms have a much stronger effect in modelling customers' intention. The most effective strategy is to improve both confidence and community norms simultaneously.

</details>


### 136. ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory

- **Authors:** Yue Fang, Zhibang Yang, Fangkai Yang, Xiaoting Qin, Liqun Li, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11126v1](http://arxiv.org/abs/2607.11126v1)
- **PDF:** [https://arxiv.org/pdf/2607.11126v1](https://arxiv.org/pdf/2607.11126v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly rely on external tools served by shared providers and accessed by heterogeneous downstream agents. Existing approaches improve tool use on the agent side through parameter updates, prompt refinement, or agent-side memory, making tool knowledge difficult to share and limited to behaviors observed in past tasks. We argue that reusable tool knowledge should instead be maintained by the tool provider. We introduce ToolAtlas, a graph-based framework that builds a persistent provider-side tool memory of tool capabilities, failure boundaries, and cross-tool compositions through execution-verified probing. At inference time, agents query the tool memory via adaptive graph traversal. Across two MCP-based benchmarks spanning eight services, ToolAtlas outperforms existing tool-side optimization and agent-side memory baselines by up to 21.61% in pass@1 and 18.61% in pass@4. The same tool memory also transfers across environment instances and agent frameworks without retraining or task-time exploration, yielding up to 24.16%/16.22% and 17.49%/14.27% relative gains in pass@1/pass@4, respectively. Ablation studies show that these gains arise from combining tool-centered memory organization with capability-guided execution probing. These results establish provider-side tool memory as an effective and reusable paradigm for tool servers. Our code is in: https://github.com/PuppyKnightUniversity/ToolAtlas.

</details>


### 137. AgentCheck: A Reproduce-Intervene-Mitigate Workbench for LLM Agents over MCP

- **Authors:** Aritra Mazumder, Nusrat jahan Lia
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11098v3](http://arxiv.org/abs/2607.11098v3)
- **PDF:** [https://arxiv.org/pdf/2607.11098v3](https://arxiv.org/pdf/2607.11098v3)
- **Categories:** cs.SE, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using LLM agents are mostly evaluated assuming all tools work. When a tool times out, returns a week-stale value, or has its description poisoned in deployment, the developer needs a controlled way to reproduce the failure, test a fix, and confirm the fix worked before deployment. We present AgentCheck, an open-source web workbench that turns an MCP server into an intervention surface. AgentCheck runs an agent against its real tools and records every tool response, then re-runs the agent with the response perturbed by a fault (12 types) injector. Matching tool calls are replayed from cache, and later tool calls go live after the agent diverges. This yields a reproduce-intervene-confirm loop: the developer toggles a mitigation, re-runs against the identical fault, and sees if the failure goes away. Scoring has two parts: deterministic pass/fail rules, plus an LLM judge for interpretive labels, validated against human annotations. Across five agents, the best passes 105/120 scenarios and the weakest only 77. The failures are usually silent, confident use of incorrect tool outputs rather than crashes. On the weakest agent, a retry mitigation raises success on timeout error faults from as few as 30% of cases to 100%, whereas stale-data faults remain near 3-4 of 10 regardless of the mitigation. AgentCheck makes these failure modes reproducible, comparable, and verifiable before deployment.

</details>


### 138. Same Stories, Different Journeys: From Social Comparison to Sensemaking in AI-Mediated Peer Career Exploration

- **Authors:** Pengping Tan, Baoquan Zhao, Zhenhui Peng
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11039v1](http://arxiv.org/abs/2607.11039v1)
- **PDF:** [https://arxiv.org/pdf/2607.11039v1](https://arxiv.org/pdf/2607.11039v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Young job seekers frequently turn to social media to compare themselves with peers and make sense of career possibilities. However, passive feed browsing creates a paradox: the authentic peer content that provides emotional grounding also triggers potentially detrimental upward social comparison and cognitive overload. Previous work has either structured online user-generated content to reduce noise without changing the passive browsing modality, or built AI-powered career exploration systems that disregard authentic human experiences. To address this gap, we developed JobMate, an interactive system that transforms real social media career posts into persona-grounded conversational AI agents, shifting the interaction from passive scrolling to active, personalized dialogue. We conducted a between-subjects study ($N$ = 24, three disciplines) comparing JobMate with native RedNote browsing. Our study shows that JobMate's AI-mediated dialogue redirected social comparison from potentially detrimental upward comparison toward constructive self-reframing, while promoting sensemaking through active conversational engagement. However, users still relied on the authenticity of real peer content for emotional grounding. We discuss design implications for AI systems that augment authentic online user-generated content consumption across social comparison contexts.

</details>


### 139. QwenPaw-Data: Bridging Facts, Methodology, and Execution for Autonomous Enterprise Data Analytics

- **Authors:** Tianjing Zeng, Yuntao Hong, Zhongjun Ding, Dandan Liu, Yinan Mei, Yunxiang Su, Yiming Wang, Xiaojian Zhang, Jingyu Zhu, Junhao Zhu, Zhuowen Liang, Jiazhen Peng, Lianggui Weng, Zhihao Ding, Kerui Yi, Qifeng Wang, Rong Zhu, Bolin Ding, Liyu Mou, Jingren Zhou
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11019v2](http://arxiv.org/abs/2607.11019v2)
- **PDF:** [https://arxiv.org/pdf/2607.11019v2](https://arxiv.org/pdf/2607.11019v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise data analysis is emerging as a distinct frontier for autonomous agents. Compared with general-purpose interaction and software engineering, it operates in an open, ambiguous, and continuously evolving environment. These characteristics call for a data-agent architecture that treats semantics, methodology, execution, and evolution as first-class system concerns. To this end, we introduce QwenPaw-Data, an agentic data system designed for enterprise intelligent data analysis. QwenPaw-Data consolidates heterogeneous assets from warehouses, dashboards, documents, interaction logs, and historical tasks into reusable, governable, and evolvable analysis assets, then turns natural-language requests into end-to-end analytical workflows spanning data understanding, retrieval, analysis, report generation, and decision support. Its architecture decomposes the problem into three collaborative subsystems: DataBridge provides trustworthy semantic grounding through interconnected metadata, knowledge, and trace graphs; Skill-Hub codifies expert analytical methodology into reusable and verifiable skills; and Host materializes these evidence and method assets into controllable, artifact-centric runtime execution. Across these subsystems, semantics, methods, traces, and feedback are continuously deposited back into the system, forming a self-evolving asset flywheel. Experiments on public benchmarks and real-world industrial BI workloads show that QwenPaw-Data improves both verifiable data access capability and higher-level analytical quality, offering a practical foundation for reliable, traceable, and continuously improving enterprise data agents.

</details>


### 140. EasyOPD: An Easy-to-use On-Policy Distillation Framework for Large Language Models

- **Authors:** Jie Sun, Mao Zheng, Mingyang Song, Qiyong Zhong, Gengsheng Li, Zhepei Hong, Chang Wu, Pengfei Liu, Junfeng Fang, Xiang Wang
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.11012v1](http://arxiv.org/abs/2607.11012v1)
- **PDF:** [https://arxiv.org/pdf/2607.11012v1](https://arxiv.org/pdf/2607.11012v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conventional language-model distillation often relies on fixed teacher-generated data, which may not cover the states encountered by an evolving student policy. On-policy distillation (OPD) instead collects teacher or evaluator supervision on student-generated rollouts. However, existing OPD methods differ substantially in supervision form, tokenizer compatibility, teacher access, and supervision granularity, leading to fragmented implementations that are difficult to reproduce and extend. We present \textsc{EasyOPD}, an on-policy distillation framework built on verl, a distributed reinforcement-learning framework for large language models. \textsc{EasyOPD} separates user-side configuration, method-specific supervision logic, and verl-based execution. Its method modules connect to the shared backend through extension boundaries for loss construction, rollout metadata, reward processing, tokenizer alignment, and teacher-side computation. We instantiate representative methods for three OPD settings -- cross-tokenizer OPD, on-policy self-distillation, and step-wise OPD. Experiments on reasoning, code-generation, scientific-knowledge, and tool-use benchmarks show that these implementations can be executed through the same verl-based backend while retaining their method-specific objectives and task-dependent performance profiles. We release \textsc{EasyOPD} with runnable YAML configurations, documentation, and an installable demonstration package and video.

</details>


### 141. A Multi-Agent Framework for Zero-Dimensional Reduced-Order Model Planning

- **Authors:** Bingteng Sun, Hao Yin, Yiling Chen, Renjie Xiao, Lei Xie, Shanyou Wang, Ruonan Wang, Shubao Chen, Qingzong Xu, Lin Lu, Qiang Du, Junqiang Zhu
- **Published:** 2026-07-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.10994v1](http://arxiv.org/abs/2607.10994v1)
- **PDF:** [https://arxiv.org/pdf/2607.10994v1](https://arxiv.org/pdf/2607.10994v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Zero-dimensional reduced-order models (0D ROMs) are central to multi-dimensional design workflows for high-end complex equipment. However, the planning process currently relies on manual expertise, limiting topological exploration and prolonging iterations. Even traditional optimization methods such as Genetic Algorithms (GA) are typically confined to local parameter tuning. Although Large Language Model (LLM) agents have shown promise in exploring large sample spaces, and frameworks such as Chain of Thought (CoT) and Reason and Act (ReAct) improve reasoning reliability, while Retrieval-Augmented Generation (RAG) overcomes domain knowledge barriers, a single agent still falls short for the long-horizon and highly coupled nature of complex 0D ROM planning. This paper proposes the Zero-dimensional reduced-order model CO-Planning framework (Z-COPA), a multi-agent architecture featuring a Symbolic Action Graph Engine (SAGE) and a MILP-Guided Navigation (MGN) optimizer. Its core innovation is a dedicated graph representation method that accurately encodes the 0D flow network topology, converting the empirical planning process into a rigorous graph structure optimization problem. We validate the forward and inverse design capabilities and generalization performance of Z-COPA on two real aircraft engine secondary-air systems, two IEEE power-distribution reconfiguration benchmarks, and two water-distribution network benchmarks. The results show superior task completion quality, obtaining the best performance in both forward and reverse design of air systems. Z-COPA disrupts the traditional 0D model planning paradigm, providing a new technical approach for exploring broader topological space and achieving highly automated, globally optimal air system architectures.

</details>



## Medrxiv (1 papers)


### 1. Multi-Agent Dynamic Refinement Outperforms Static RAG in Clinical Reasoning for Complex Nephrology Cases

- **Authors:** Yano, Y., Kakizaki, H., Nagasu, H., Kishi, S., Koshida, T., Nihei, Y., Hirano, A., Sugawara, Y., Imaizumi, T., Osakabe, Y., Sakaguchi, Y., Nangaku, M., Mori, H., Naito, T., Ohashi, M., Maruyama, S., Matsui, I., Isaka, Y., Okada, H., Suzuki, Y., Kashihara, N.
- **Published:** 2026-07-16
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.15.26358121](https://doi.org/10.64898/2026.07.15.26358121)

- **Categories:** nephrology


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundLarge language models (LLMs) struggle with dynamic, longitudinal clinical reasoning. We developed a Multi-Stage Iterative Clinical Reasoning Agent framework to address this gap and systematically decouple the clinical efficacy of static retrieval-augmented generation (RAG) from dynamic self-refinement.

MethodsTen complex longitudinal nephrology cases, rigorously selected via a modified Delphi consensus technique, were blindly evaluated by four board-certified nephrologists and a multi-model AI panel. We compared three architectures across nine cognitive steps: (Model A) a baseline frontier LLM, (Model B) an LLM augmented with static guideline-based RAG, and (Model C) our proposed multi-agent framework featuring RAG integrated with iterative self-critique and refinement.

ResultsIn human evaluations (20-point scale), Model C (mean 17.2, SD 1.2) significantly outperformed both Model A (16.1, 1.3) and Model B (16.2, 1.2) (P < 0.001). Implementing static RAG (Model B) yielded no significant improvement over the baseline. Automated AI evaluations (15-point scale) corroborated these findings: Model C (14.7, 0.6) outscored Model A (14.2, 0.9, P < 0.001) and Model B (14.3, 0.9, P = 0.01). While monolithic models exhibited severe score degradations in planning-heavy tasks such as dynamic differential diagnoses, the multi-agent framework effectively intercepted error cascades, achieving significantly higher diagnostic accuracy (mean 17.6, P = 0.019) and therapeutic management scores (17.3, P = 0.002).

ConclusionsStatic knowledge retrieval alone fails to enhance frontier LLM performance in longitudinal medical reasoning. Distributing clinical workflows into a multi-agent dynamic refinement pipeline significantly improves reasoning completeness, intercepts error cascades, and safely resolves planning bottlenecks in complex patient care.

</details>



## Biorxiv (1 papers)


### 1. EcoXAI: Autonomous Agentic Ecosystem for Explainable Artificial Intelligence and Biomedical Discovery

- **Authors:** Matsumoto, N., Choi, H., Freda, P. J., Hernandez, M. E., Wang, Z. P., Moore, J. H.
- **Published:** 2026-07-13
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.07.08.737358](https://doi.org/10.64898/2026.07.08.737358)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

MotivationAs biomedical datasets and knowledge graphs continue to grow in size, complexity, and heterogeneity, navigating and extracting actionable insights from them presents a major bottleneck for researchers. There is a clear need for autonomous analytical solutions that can utilize recent advancements in agentic AI such as agent harnessing and loop engineering without introducing hallucination or workflow fragmentation. Researchers, regardless of technical expertise, need tools that streamline complex data analysis and deliver meaningful, actionable insights grounded in both data and established biomedical knowledge. EcoXAI addresses this by introducing a modular, customizable, containerized multi-agent system that structures analysis into explicit pipeline execution stages, lowering the computational barrier for clinical and translational researchers.

ResultEcoXAI replaces monolithic AI text interfaces with an autonomous execution-driven framework with specialized bioinformatics agents for delivering proactive, data-driven insights grounded in established biological knowledge. Unlike purely LLM-driven or less integrated AI solutions prone to hallucinations or biologically implausible outcomes, EcoXAIs multi-agent framework, which leverages modern agentic management and explicit knowledge graph integration, provides greater transparency and verifiability in its reasoning. In our use case in drug repurposing for Alzheimers Disease, EcoXAI evaluated 103 drug candidates and identified 79 novel candidates whose predictive models exceeded a randomized baseline, including the CCR5 antagonist Maraviroc, whose generated hypothesis was subsequently supported by the literature. These results demonstrate the potential of knowledge graph-grounded AI agents to accelerate hypothesis-driven biomedical research.

Availability and implementationEcoXAI is available on GitHub at: https://github.com/EpistasisLab/EcoXAI.

Contactjason.moore@csmc.edu

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*