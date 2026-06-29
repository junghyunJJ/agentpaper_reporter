# Weekly AI Agent Paper Report

**Generated:** 2026-06-29 13:42
**Period:** 2026-06-22 to 2026-06-28

## Summary

- **Total papers fetched:** 635
- **Papers matching keywords:** 141
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-06-22) | Change |
|--------|-----------|-----------|--------|
| Total matched | 141 | 149 | -8 |
| arxiv | 138 | 148 | -10 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 2 | 0 | +2 |

### Notable Trends

**Weekly Snapshot**

| Metric | This Week (29 Jun 2026) | Last Week (22 Jun 2026) | Change |
|--------|------------------------|------------------------|--------|
| Total papers | 141 | 149 | –5 % |
| arXiv | 138 | 148 | –7 % |
| medRxiv | 2 | 0 | +2 (new source) |
| bioRxiv | 1 | 1 | no change |

**Notable Trends**

1. **Slight dip in overall output, driven mainly by a 10‑paper drop on arXiv.** The community is still publishing at a high volume (>140 papers/week), but the modest contraction suggests a short‑term consolidation rather than a slowdown.

2. **Emergence of health‑focused “agentic” work.** Two of this week’s top titles (ALEX & Agentic Autodiscovery of Diastolic Dysfunction) and the new medRxiv entries bring the **agent‑medical intersection** to the fore, whereas last week’s leaders were purely systems‑oriented.

3. **Shift from core infrastructure to application‑level agents.**  
   - *Last week*: heavy emphasis on execution platforms, verification, and control‑plane security (e.g., “Execution‑State Capsules”, “Sovereign Execution Brokers”).  
   - *This week*: focus on **domain‑specific agents**—hardware design as code evolution, scientific‑review assistants, and human‑agent collaborative perception (HAT‑4D). The field is moving from building the “engine” to showcasing what the engine can now do.

4. **Growing interest in multi‑agent optimization and interpretability.** Papers such as *GBC: Gradient‑Based Connections* and *Agent‑Native Immune System* indicate a trend toward **learning‑driven coordination mechanisms** and **explainable multi‑agent reasoning**, building on last week’s “Contagion Networks” but with a more constructive (optimizing) angle.

5. **Cross‑disciplinary diffusion:** The latest “biomeStat” paper demonstrates an **end‑to‑end genomic‑epidemiology pipeline** powered by agents, echoing the broader push to apply agentic AI beyond computer‑science domains—a direction barely visible in the prior week’s top set.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**Overview**

These three studies showcase a common theme: leveraging autonomous, multi‑agent AI systems to automate and interpret complex biomedical workflows that traditionally demand extensive expert supervision.  
1. **biomeStat** demonstrates an “agentic AI orchestrator” that dynamically selects, configures, and pipelines heterogeneous phylogenetic and epidemiological tools to process ≈1,000 Asian dengue virus genomes, providing reproducible end‑to‑end genomic‑epidemiology without manual parameter tuning.  
2. **ALEX** introduces a multi‑agent framework in which one agent learns individualized treatment‑effect models from randomized trial data while a second “explainability” agent generates natural‑language rationales, enabling clinicians to understand why a specific patient should receive a given therapy.  
3. **Agentic Autodiscovery of Diastolic Dysfunction Phenotypes** uses a set of cooperating agents—signal‑processing, feature‑extraction, clustering, and validation agents—to mine surface ECG recordings for latent diastolic‑dysfunction signatures, bypassing the need for echocardiography‑derived parameters and achieving phenotype discovery at scale.  

Collectively, these papers illustrate how autonomous AI agents can (i) integrate heterogeneous biomedical data sources, (ii) automate model building and interpretation, and (iii) produce scalable, clinically actionable insights across genomics, precision treatment, and cardiac phenotyping.



### 1. biomeStat: Using Agentic AI for Scalable Genomic Epidemiology Demonstrated Through End-to-End Analysis of 1,000 Asian Dengue Virus Genomes

- **Authors:** Ariyaratne, D., Somaratna, N., Malavige, G. N.
- **Published:** 2026-06-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.10.731380](https://doi.org/10.64898/2026.06.10.731380)

- **Categories:** bioinformatics


> **Main contribution:** The paper introduces **biomeStat**, a deterministic, autonomous AI‑agent that translates natural‑language research intents into reproducible, sandboxed bioinformatics pipelines, dynamically provisioning CPU/GPU resources and orchestrating established genomic‑epidemiology tools without requiring user‑level command‑line expertise.  

**Methodology:** biomeStat generates and executes code for each step of a standard workflow (quality control, alignment, phylogeny with IQ‑TREE/TreeTime, Bayesian phylodynamics with BEAST2 on an NVIDIA H200 GPU, selection analysis with HyPhy, and structural mapping in PyMOL), managing data flow and environment isolation while logging all parameters to ensure traceability.  

**Key findings:** In a fully autonomous end‑to‑end run on 1,000 Asian Dengue virus genomes, biomeStat completed the entire analysis in <24 h, reproducing known epidemiological dynamics (Rₑ≈1.0), uncovering 1,869 putative immune‑escape sites colocated with B‑ and T‑cell epitopes, and confirming the absolute conservation of 176 drug‑target residues, thereby compressing weeks of expert labor into a single, transparent session and demonstrating the practical scalability of agentic AI for large‑scale genomic epidemiology.


<details>
<summary>Abstract</summary>

Genomic epidemiology workflows typically require expert curation of multiple specialized tools, extensive manual parameter tuning, and access to heterogeneous compute infrastructure. While standard generative AI models often hallucinate in complex biological domains, we introduce biomeStat: an autonomous AI agent that functions as a strict deterministic orchestrator. By automatically writing code to execute established bioinformatics tools in sandboxed environments, biomeStat dynamically provisions compute resources (CPU and GPU) and guarantees reproducibility, making it immediately useful for scientists without requiring command-line expertise.

To demonstrate the platform, we performed a fully autonomous genomic epidemiology and structural analysis of 1,000 Dengue virus (DENV) genomes sampled from 16 Asian countries between 2000 and 2025. The agent seamlessly orchestrated phylogenetic reconstruction (IQ-TREE, TreeTime), Bayesian phylodynamics (BEAST2 via NVIDIA H200 GPU), selection pressure analysis (HyPhy), and structural mapping (PyMOL). The analysis was completed in under 24 hours of wall-clock time, revealing endemic stability (R_e [~]1.0) and identifying 1,869 candidate immune escape sites structurally colocalized with B-cell and T-cell epitopes. Furthermore, the agent validated 176 highly conserved drug target residues across the viral replication complex, confirming that resistance-associated positions for emerging antivirals JNJ-1802 and NITD-688 remain absolutely conserved across all four serotypes. By bridging the gap between natural language intent and deterministic computational execution, biomeStat reduces weeks of expert effort into a single-session analysis with full methodological transparency.

</details>


### 2. ALEX: Automatic Language EXplanations for Interpreting Treatment Effects via Multi-Agents

- **Authors:** Lu, M., Kim, C., Kwon, Y., White, N. J., Lee, S.-I.
- **Published:** 2026-06-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.23.26351510](https://doi.org/10.64898/2026.04.23.26351510)

- **Categories:** health informatics


> The paper introduces **ALEX**, a multi‑agent XAI system that first extracts statistically significant subgroup treatment effects from randomized clinical trials and then feeds these effect‑modifiers to coordinated large‑language‑model agents that generate data‑grounded, natural‑language explanations of why individuals respond differently to a therapy. By integrating causal subgroup discovery with prompt‑engineered LLM reasoning, ALEX was evaluated on five landmark RCTs and achieved higher scores on established treatment‑explanation quality metrics than prior agentic baselines, with blind physician reviewers confirming the clinical relevance of its narratives. Notable case studies show ALEX correctly attributing the ACCORD‑BP vs SPRINT discrepancy to baseline glucose and uncovering age as a novel modifier of tranexamic‑acid efficacy in trauma, demonstrating its potential to translate heterogeneous treatment effects into actionable precision‑medicine insights.


<details>
<summary>Abstract</summary>

Precision medicine requires understanding how general treatment effects from randomized clinical trials should be applied to individual patients. Machine learning methods have shown some promise for estimating patient-level treatment effects, however, their clinical utility remains limited because they often fail to explain why responses to a given treatment vary across individuals. Here we present ALEX, an explainable AI (XAI)-driven, multi-agent framework that addresses this interpretability gap by translating the variables that drive precision predictions into data-grounded, natural-language clinical explanations. ALEX first independently identifies important subgroup treatment effects present in randomized clinical trials and then hands them to large language model (LLM) agents to produce contextualized and scrutinized clinical insights. Across five landmark randomized controlled trials, ALEX outperformed existing agentic methods on treatment explanation quality metrics consistent with the biomedical literature that aligned with blinded reviews by specialist physicians across the United States and Taiwan. In empirical case studies, ALEX provided key interpretable insights, such as identifying baseline glucose level as explaining the divergent findings between the ACCORD-BP and SPRINT trials, and proposed age as a novel and key effect modifier for pre-hospital tranexamic acid efficacy after trauma. These findings suggest that ALEX can help translate treatment effect heterogeneity into clinically grounded explanations that enable precision medicine.

</details>


### 3. Agentic Autodiscovery of Diastolic Dysfunction Phenotypes from Surface Electrocardiogram

- **Authors:** Jamthikar, A. D., Shanmugham, A., Singh, S., Radhakrishnan, A., Dong, J., Maganti, K., Yanamala, N., Sengupta, P.
- **Published:** 2026-06-23
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.17.26355897](https://doi.org/10.64898/2026.06.17.26355897)

- **Categories:** cardiovascular medicine


> The paper introduces an **agentic AI auto‑discovery framework** that uses a large‑language‑model‑driven search to automatically design and refine attention‑based multimodal architectures for detecting left‑ventricular diastolic dysfunction (LVDD) from 12‑lead ECGs—or from AI‑generated synthetic tissue‑Doppler imaging (TDI) waveforms. By iteratively proposing, validating, and selecting model configurations via transfer‑learning and multimodal fusion, the system yields two compact models that achieve high discrimination of LVDD severity (AUC 0.83–0.87) and, when applied to >250 k external ECGs, stratify incident heart‑failure mortality with hazard ratios of 5.5–9.5, outperforming a published ECG‑to‑HF convolutional network. The work demonstrates that autonomous architecture search can produce data‑efficient, clinically robust agentic models for ECG‑based cardiac phenotyping, extending diastolic function assessment beyond conventional echocardiography.


<details>
<summary>Abstract</summary>

BackgroundLeft ventricular diastolic dysfunction (LVDD) is a major determinant of heart failure (HF), yet its assessment relies on multiparametric echocardiography, limiting scalability. We previously demonstrated that generative artificial intelligence (AI) can synthesize tissue Doppler imaging (TDI) waveforms from the 12-lead ECG. The growing complexity of candidate architecture creates a need for automated model-discovery frameworks.

ObjectivesTo evaluate agentic AI-based auto-discovery for ECG-based LVDD assessment using either raw ECG or synthetic TDI waveforms.

MethodsTwo attention-based agentic AI architectures were developed using an automated large language model-driven refinement framework that optimized transfer-learning and multimodal architectures through autonomous proposal, validation, and selection of candidate model configurations. Development was performed in 1,011 paired ECG-echocardiography studies and externally validated in 983 patients using two reference frameworks: (i) data-driven phenogroups and (ii) the 2025 ASE Diastolic Function Guidelines. External validation was performed in CODE-15% (n=219,567) for HF-related mortality and EchoNext (n=35,718) for structural heart disease associations.

ResultsDespite the modest cohort size, the ECG-based agentic search achieved area under the receiver operating characteristic curve (AUCs) of 0.87 (95% CI: 0.85-0.89) and 0.83 (95% CI: 0.80-0.86) for phenogroup and guideline-based LVDD severity classification. Corresponding AUCs for the synthetic TDI-based model were 0.82 (95% CI: 0.80-0.85) and 0.80 (95% CI: 0.77-0.84), respectively. In large-scale external validation, both models stratified incident HF mortality with subdistribution hazard ratios ranging 5.5 to 9.5 (Grays p<0.001 for all). Time-dependent discrimination for incident HF mortality exceeded a publicly available convolutional neural network model (ECG2HF) ({Delta}AUC range: +0.14 to +0.20). Both models demonstrated consistent associations with structural heart disease outcomes.

ConclusionsAgentic auto-discovery enabled data-efficient assessment of LVDD from surface ECG by combining physiologically informed transfer learning with autonomous architecture optimization, achieving robust external generalizability. This approach may facilitate broader access to diastolic function assessment beyond conventional echocardiography.

</details>


---



## Arxiv (138 papers)


### 1. Agentic Hardware Design as Repository-Level Code Evolution

- **Authors:** Cunxi Yu, Chenhui Deng, Nathaniel Pinckney, Brucek Khailany
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28279v1](http://arxiv.org/abs/2606.28279v1)
- **PDF:** [https://arxiv.org/pdf/2606.28279v1](https://arxiv.org/pdf/2606.28279v1)
- **Categories:** cs.AR, cs.AI


> **Main contribution:** The paper introduces **HORIZON**, a self‑evolving agent framework that recasts hardware design as a full‑repository code‑evolution problem, embedding domain knowledge, an executable evaluator, an acceptance predicate, and a git‑based runtime policy inside a compiled Markdown “harness” so that a hands‑free agent can iteratively modify an isolated git worktree.

**Methodology:** HORIZON treats each design iteration as a set of repository operations (commits, branches, reverts, etc.) that simultaneously manage state, tracing, and replay; the agent loop runs without human intervention, applying these operations to evolve Verilog/SystemVerilog artifacts while respecting the evaluator and acceptance predicate defined in the project pack.

**Key findings:** Across four benchmark suites (ChipBench, RTLLM, Verilog‑Eval, and nine CVDP categories) the autonomous loop achieved **100 % completion**, demonstrating that repository‑scale self‑evolution can be applied to hardware‑design artifacts, though the authors stress that these controlled proxies do not yet solve the broader, real‑world chip‑design problem.


<details>
<summary>Abstract</summary>

We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay. This extends prior works of repository-scale self-evolution from EDA software systems, to hardware-design artifacts themselves. We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100\% benchmark completion across all suites with a fully hands-free agentic loop. However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. Section~\ref{sec:discuss} examines the limitations of the current study and highlights open research challenges.

</details>


### 2. Towards Automating Scientific Review with Google's Paper Assistant Tool

- **Authors:** Rajesh Jayaram, Drew Tyler, David Woodruff, Corinna Cortes, Yossi Matias, Vahab Mirrokni, Vincent Cohen-Addad
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28277v1](http://arxiv.org/abs/2606.28277v1)
- **PDF:** [https://arxiv.org/pdf/2606.28277v1](https://arxiv.org/pdf/2606.28277v1)
- **Categories:** cs.LG, cs.AI, cs.CL, cs.CY


> The paper proposes a hierarchical taxonomy of AI‑human collaborations for scientific peer review and introduces the **Paper Assistant Tool (PAT)**, an agentic AI system that autonomously ingests full manuscripts, checks proofs, replicates experiments, flags methodological flaws, and suggests concrete revisions. PAT combines large‑scale inference (multiple model calls, chain‑of‑thought prompting, and verification loops) to boost error‑detection capability, achieving a **34 % increase in zero‑shot recall of mathematical mistakes on the SPOT benchmark** compared with a single‑call baseline. In pilot deployments as a pre‑submission aid for STOC and ICML papers, PAT successfully uncovered critical errors and generated substantive improvement suggestions, demonstrating that AI can meaningfully augment the review pipeline while keeping human referees in final control.


<details>
<summary>Abstract</summary>

Artificial intelligence is driving a revolution in scientific discovery, accelerating everything from hypothesis generation to mathematical theorem proving. However, this rapid acceleration is creating a systemic challenge: traditional human peer review cannot scale to match the influx of AI-assisted science. Ultimately, to resolve this tension, we must also deploy AI to accelerate the verification and review process itself. To frame the discussion around this transition, we propose a taxonomy consisting of four progressive levels of AI-human collaboration in scientific evaluation, and discuss various trade-offs involved with each.
  As a step toward this future, we introduce the Paper Assistant Tool (PAT), an agentic AI framework built for deep scientific review and verification. PAT ingests full scientific manuscripts and produces a comprehensive evaluation, checking theoretical results, validating experiments, suggesting improvements, and identifying potential flaws. By utilizing inference scaling techniques, PAT is able to identify deeper issues than a single model call alone, achieving a 34% improvement over zero-shot recall on mathematical errors in the SPOT benchmark. Pilot deployments of PAT as a pre-submission tool for authors at two major Computer Science conferences -- STOC and ICML -- demonstrate its ability to identify critical errors and suggest substantive improvements to research papers. By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process.

</details>


### 3. Agent-Native Immune System: Architecture, Taxonomy, and Engineering

- **Authors:** Bo Shen, Lifeng Chang, Tianyuan Wei, Yunpeng Li, Feng Shi, Yichen Han, Peijie Gao, Shiyi Kuang, Xin Chang, Dehui Li
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28270v1](http://arxiv.org/abs/2606.28270v1)
- **PDF:** [https://arxiv.org/pdf/2606.28270v1](https://arxiv.org/pdf/2606.28270v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **Agent‑Native Immune System (ANIS)**, the first endogenous, biologically‑inspired security layer that sits inside an autonomous agent’s reasoning loop rather than at the perimeter.  The authors design a six‑layer “Immune Tower” (L0‑L5) with a non‑cognitive Barrier (L1), define a taxonomy of “Agent Viruses” and “Agent Vaccines,” and implement the **Harness Triad** (Meta, Self, Auto) to drive Continual Immune Learning—allowing the system to detect and neutralize runtime attacks such as memory poisoning, tool‑chain manipulation, and multi‑agent protocol breaches.  Experiments and theoretical analysis show that ANIS can dynamically adapt defenses with low false‑positive “auto‑immunity” rates, establishing a runtime “law‑enforcement” complement to static alignment and opening a new research direction for resilient, self‑defending autonomous AI agents.


<details>
<summary>Abstract</summary>

The transition from static chat bots to autonomous agents--equipped with persistent memory, tool-use protocols, and multi-agent collaboration--has fundamentally expanded the AI threat landscape. Current defense mechanisms, such as perimeter security and training-time alignment, remain external to the agent's active reasoning loop. Consequently, they fall short: a fully aligned agent remains highly vulnerable to runtime hijacking via memory poisoning, tool-chain manipulation, or multi-agent protocol attacks. To address this critical gap, we introduce the Agent-Native Immune System (ANIS), the first biologically inspired, endogenous defense architecture embedded directly within the agent's cognitive loop. Our framework presents four primary contributions. First, we design a six-layer Immune Tower (L0-L5), distinctly incorporating Barrier Immunity (L1) as a non-cognitive, physical-and-logical isolation layer. Second, we establish a unified taxonomy of Agent Viruses and Agent Vaccines, formalizing the critical distinction between superficial non-parametric defenses and robust parametric vaccines. Third, we conceptualize the Harness Triad--Meta, Self, and Auto--a self-monitoring, meta-cognitive automation backbone that drives Continual Immune Learning (CIL), enabling vaccines to dynamically adapt to novel threats. Finally, we establish a rigorous theoretical demarcation between model alignment and agent immunity: while alignment provides a static "constitutional" value foundation during training, ANIS serves as the dynamic "law enforcement" mechanism during runtime. We conclude by framing open challenges for the field, including immune protocol standardization, novel evaluation metrics such as the Autoimmunity Rate (false-positive intervention rate), and the co-evolutionary dynamics between pathogens and vaccines within collective intelligence ecosystems.

</details>


### 4. HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration

- **Authors:** Jiaxin Li, Yuxiang Wu, Zhenkai Zhang, Xinrui Shi, Haoyuan Wang, Yichen Zhao, Su Linxiang, Chenyang Yu, Mingyu Zhang, Yifan Ding, Boran Wen, Li Zhang, Ruiyang Liu, Yong-Lu Li
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28215v1](http://arxiv.org/abs/2606.28215v1)
- **PDF:** [https://arxiv.org/pdf/2606.28215v1](https://arxiv.org/pdf/2606.28215v1)
- **Categories:** cs.CV, cs.AI, cs.GR


> **Main contribution:** HAT‑4D introduces the first agentic system that reconstructs full 4‑D (3‑D shape + temporal dynamics + physical interactions) of multiple objects from a single monocular video, and uses the pipeline to generate the large‑scale MVOIK‑4D benchmark for embodied‑AI research.  

**Methodology:** The framework couples large vision‑language models with a multi‑level human‑in‑the‑loop feedback loop: (1) VLM‑driven prompts guide an initial monocular 3‑D mesh generation; (2) a human‑assisted verification/correction stage resolves depth ambiguities and occlusions; (3) the corrected meshes are propagated forward in time using a physics‑aware motion model that enforces interaction constraints, yielding physically plausible 4‑D trajectories without multi‑camera data.  

**Key findings:** On the newly proposed MVOIK‑4D benchmark, HAT‑4D attains state‑of‑the‑art scores on most geometric, temporal‑consistency, and physical‑plausibility metrics while preserving semantic alignment. Ablations show that even modest human feedback markedly improves interaction reconstruction, and datasets generated by HAT‑4D boost downstream embodied‑AI models when used for fine‑tuning.


<details>
<summary>Abstract</summary>

Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at https://lijiaxin0111.github.io/HAT4D/

</details>


### 5. GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems

- **Authors:** Xiaocheng Yang, Abdulrahman Alrabah, Dilek Hakkani-Tür, Gokhan Tur
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28187v1](http://arxiv.org/abs/2606.28187v1)
- **PDF:** [https://arxiv.org/pdf/2606.28187v1](https://arxiv.org/pdf/2606.28187v1)
- **Categories:** cs.MA


> **Contribution:** The paper introduces **Gradient‑Based Connections (GBC)**, a novel credit‑assignment framework that treats a large‑language‑model‑based multi‑agent system as a differentiable computational graph and learns *gradient‑weighted connection strengths* linking each agent’s token‑level outputs to downstream agents.

**Methodology:** GBC builds an attribution graph by back‑propagating a task‑specific loss through the sequence of agent prompts, using a prefix‑based gradient computation engine (AgentChord) to efficiently obtain token‑level influence scores. These scores are then used to identify error‑prone agents/interaction steps and to perform targeted prompt updates.

**Key Findings:** On the dialogue‑centric benchmarks MultiWOZ and τ‑bench, GBC‑optimized MASs achieve statistically significant gains over strong single‑agent and existing multi‑agent baselines. Moreover, higher-quality attribution (i.e., more accurate connection weights) correlates with larger performance improvements, demonstrating that fine‑grained gradient attribution is an effective tool for optimizing coordinated LLM agents.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. Existing approaches typically rely on coarse-grained feedback, making it difficult to identify which agents or interaction steps are responsible for errors. We propose Gradient-Based Connections (GBC), an approach for fine-grained attribution and optimization of multi-agent systems. GBC models a MAS as a computational graph and introduces gradient-based connection weights to quantify the influence of each agent's output on downstream agents at the token level. By constructing an attribution graph and propagating task-specific loss signals backward, our method enables precise identification of error sources and targeted prompt optimization. We further develop AgentChord, an efficient implementation that leverages prefix-based gradient computation. Experiments on MultiWOZ and τ-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Code is available at: https://github.com/yxc-cyber/AgentChord.

</details>


### 6. LLawCo: Learning Laws of Cooperation for Modeling Embodied Multi-Agent Behavior

- **Authors:** Qinhong Zhou, Chuang Gan, Anoop Cherian
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28182v1](http://arxiv.org/abs/2606.28182v1)
- **PDF:** [https://arxiv.org/pdf/2606.28182v1](https://arxiv.org/pdf/2606.28182v1)
- **Categories:** cs.LG, cs.AI, cs.CV, cs.RO


> The paper introduces **LLawCo**, a framework that lets embodied LLM‑based agents automatically infer and obey high‑level “laws of cooperation” (e.g., “talk when necessary”, “wait for partner”) by analyzing past failure episodes and fine‑tuning their chain‑of‑thought reasoning with supervised signals. The methodology extracts misaligned behavioral patterns, distills them into explicit rules, and injects those rules into the agents’ reasoning pipelines via supervised fine‑tuning across multiple LLM backbones. Experiments on the new **PARTNR‑Dialog** benchmark and the TDW‑MAT suite show that LLawCo improves cooperative efficiency and task success, yielding average gains of 4.5 % and 6.8 % respectively over the strongest open‑source communicative agents.


<details>
<summary>Abstract</summary>

Embodied agents operating in decentralized and partially observable environments have attracted growing attention in recent years. However, existing large language model (LLM)-based agents often exhibit behaviors that are misaligned with their partners or inconsistent with the environment state, leading to inefficient cooperation and poor task success. To address this challenge, we propose a novel framework, Learning Laws of Cooperation (LLawCo), that enables embodied agents to autonomously align with both their partners and task objectives. Our framework allows agents to reflect on past failures to extract misaligned behavioral patterns, which are used to derive high-level behavioral laws, such as "Talk when necessary" and "Wait for partner." These laws are explicitly incorporated into the agents' chains of thought via supervised fine-tuning, aligning their reasoning with task requirements and the behavior of other agents. To evaluate our approach, we introduce PARTNR-Dialog, a large-scale multi-agent communicative and cooperative planning benchmark built on the PARTNR environment. Experiments on existing tasks and our new benchmark demonstrate significant improvements in cooperative efficiency and task success rates. Across four backbone LLMs, our method achieves average success rate improvements of 4.5% on the PARTNR-Dialog benchmark and 6.8% on the TDW-MAT benchmark over state-of-the-art open-source communicative agent frameworks. See the LLawCo project page for details: https://www.merl.com/research/highlights/LLawCo

</details>


### 7. MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization

- **Authors:** Jinliang Xu, Liping Ma
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28109v1](http://arxiv.org/abs/2606.28109v1)
- **PDF:** [https://arxiv.org/pdf/2606.28109v1](https://arxiv.org/pdf/2606.28109v1)
- **Categories:** cs.NE, cs.MA


> **Main contribution** – The paper introduces **MMAO (Metabolic Multi‑Agent Optimizer)**, a unified continuous‑and‑discrete optimization framework in which every agent carries its own “metabolic” energy and role state, while the whole population shares a communal resource pool; fitness gains are internally converted into energy that autonomously drives all algorithmic controls (search amplitude, sensing intensity, branching, pruning, respawning, elite reinvestment, etc.).  

**Methodology** – MMAO models a closed private‑public metabolic loop: each agent updates its internal energy from normalized fitness improvements (via a robust progress‑scale and recent‑success statistic) and then uses that energy to modulate zero‑order probing and role‑interpolated motion in the continuous case, or structural sensing, local route repair, guided perturbation and edge‑reuse weighting in the discrete case. The framework is deliberately parameter‑light; most control parameters are self‑calibrated through the metabolic feedback.  

**Key findings** – Experiments on a subset of CEC‑2017 continuous benchmarks (10‑ and 30‑dimensional) and on five TSPLIB combinatorial instances show that MMAO attains competitive performance with far fewer hand‑tuned parameters, confirming the viability of endogenous resource allocation for heterogeneous search behaviors. While not uniformly superior to state‑of‑the‑art meta‑heuristics, MMAO’s primary merit lies in its self‑regulating, cross‑domain design that could serve as a building block for more autonomous, agentic AI optimization systems.


<details>
<summary>Abstract</summary>

Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a communal resource pool. Fitness improvements are converted into normalized metabolic gains through a robust progress scale and a recent success statistic; the same closed loop then regulates sensing intensity, search amplitude, role drift, branching, pruning, respawning, and elite reinvestment. In the continuous setting, MMAO uses energy-regulated symmetric zero-order probing and role-interpolated motion. In the discrete setting, the same control law is instantiated through structural sensing, local route improvement, guided perturbation, and energy-weighted edge reuse. The paper combines an implementation-faithful formulation with a reproducible experimental study on a CEC2017 subset (10D/30D, 20 seeds) and five TSPLIB instances (100 discrete runs in total). The current evidence supports MMAO primarily as a parameter-light, self-calibrating optimization framework whose main validated originality lies in metabolically endogenous resource allocation across heterogeneous search behaviors, rather than as a universally superior optimizer.

</details>


### 8. ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents

- **Authors:** Shijing Hu, Liang Liu, Zhu Meng, Zhicheng Zhao
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28061v1](http://arxiv.org/abs/2606.28061v1)
- **PDF:** [https://arxiv.org/pdf/2606.28061v1](https://arxiv.org/pdf/2606.28061v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **ToolPrivacyBench**, the first benchmark that assesses “purpose‑bound” privacy in multi‑tool LLM agents by checking whether private data atoms are sent only to those tools that are explicitly authorized to receive them.  The authors construct 2,150 test cases (1,150 synthetic business workflows plus 1,000 adapted from existing function‑calling suites), encode a policy knowledge base describing permissible information flows, run nine popular agent implementations against mocked back‑ends, and then audit the recorded tool arguments and backend logs against the policies.  Experiments reveal that agents can fully complete tasks while still leaking unnecessary private information in intermediate calls, demonstrating that conventional task‑completion metrics miss critical privacy violations and that trajectory‑level auditing is needed to enforce need‑to‑know disclosure in tool‑using AI agents.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. Neither perspective captures purpose-bound information flow across an executed multi-tool trajectory. Motivated by this limitation in current agent evaluation, ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks, thereby evaluating both task completion and privacy over-disclosure during tool use. The benchmark contains 2,150 cases, including 1,150 fully synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks. Each case is represented by a policy knowledge base. After an agent executes against mock business backends, the evaluator compares recorded tool arguments and backend audit logs with this policy knowledge base. The evaluation covers nine widely used agents to characterize purpose-bound privacy over-disclosure. The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.

</details>


### 9. From Detection to Action: Using LLM Agents for Fault-Tolerant Control

- **Authors:** Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.28011v1](http://arxiv.org/abs/2606.28011v1)
- **PDF:** [https://arxiv.org/pdf/2606.28011v1](https://arxiv.org/pdf/2606.28011v1)
- **Categories:** eess.SY, cs.LG


> The paper introduces a novel agentic LLM framework that turns fault‑detection alerts into verified, constraint‑aware recovery actions for industrial process control. By orchestrating multiple specialized LLM agents (monitoring, planning, synthesis, simulation, validation, reprompting) together with a Digital Process Plant Twin and a graph‑based Retrieval‑Augmented Generation layer built on the CPSMod ontology, the system retrieves plant‑specific knowledge, generates minimal‑risk state‑machine recovery paths, and pre‑tests them against interlocks, envelopes, and dynamic feasibility before execution. Experiments on a batch mixing module and a CSTR under PID control show that lightweight GPT‑4‑mini models can produce correct, latency‑compatible corrective actions, demonstrating a viable end‑to‑end route from fault detection to validated actuation in both discrete and continuous FTC scenarios.


<details>
<summary>Abstract</summary>

We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach couples (i) a multi-agent workflow that decomposes operator duties into monitoring, planning, action synthesis, simulation, validation, and reprompting; (ii) a Digital Process Plant Twin (DPPT) that exposes plant data, models, and a simulation service for pre-execution testing; and (iii) a Graph Retrieval-Augmented Generation (Graph RAG) layer built on the CPSMod ontology, which organizes plant knowledge (structure, function, hybrid dynamics, control context, and fault semantics) into a graph that supports relation-aware, multi-hop retrieval for the agents. Corrective actions are generated as minimal-risk state-machine recovery paths and corresponding discrete commands or continuous setpoint adaptations, then validated deterministically against interlocks, envelopes, and dynamic feasibility before any actuation. If no acceptable plan is found within a bounded time window, control is handed to a safety fallback. The framework is evaluated in simulation on two representative benchmarks: a discrete batch Mixing Module and a Continuous Stirred-Tank Reactor (CSTR) under closed-loop PID regulation. Results with lightweight LLMs (GPT-4o-mini and GPT-4.1-mini) show that semantically grounded agents can derive valid recovery decisions within latency budgets compatible with the respective process dynamics, demonstrating a practical pathway from detection to validated corrective action across both discrete and continuous FTC tasks.

</details>


### 10. ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering

- **Authors:** ZhengXian Wu, Hangrui Xu, Kai Shi, Zhuohong Chen, Yunyao Yu, Chuanrui Zhang, Zirui Liao, Jun Yang, Zhenyu Yang, Haonan Lu, Haoqian Wang
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27974v1](http://arxiv.org/abs/2606.27974v1)
- **PDF:** [https://arxiv.org/pdf/2606.27974v1](https://arxiv.org/pdf/2606.27974v1)
- **Categories:** cs.CV, cs.AI


> **Main contribution:** ProMSA introduces a controllable “search‑agent” that dynamically decides, at each reasoning step, whether to query visual or textual knowledge bases—or to stop—rather than using a fixed retrieve‑then‑generate pipeline for knowledge‑based VQA.

**Methodology:** The system is trained in two stages: (1) rejection‑sampling supervised fine‑tuning to teach the model proper tool‑calling syntax, and (2) a sequence‑level reinforcement learning objective (TN‑GSPO) that rewards successful question answering while normalizing for both the length of the generated answer and the depth of tool interactions, with explicit budgets and deduplication to avoid redundant searches.

**Key findings:** Across the E‑VQA and InfoSeek benchmarks, ProMSA outperforms strong retrieval‑augmented generation (RAG) and prior agent baselines, achieving higher retrieval recall and overall VQA accuracy, demonstrating that progressive, adaptive tool use is beneficial for agentic AI in multimodal, knowledge‑intensive tasks.


<details>
<summary>Abstract</summary>

Knowledge-based Visual Question Answering (KB-VQA) requires models to combine image understanding with external knowledge. Most prior methods use a fixed retrieve-then-generate pipeline with a pre-selected retriever and a static top-k setting, which is not adaptive during reasoning. We propose ProMSA, a progressive multimodal search agent for KB-VQA. Given an image-question pair, the agent iteratively chooses image search, text search, or stop, under explicit tool-call budgets and with deduplication to avoid redundant retrieval. For training, we first use rejection-sampling SFT to learn valid tool-use formats, then optimize the agent with TN-GSPO, a sequence-level RL objective that normalizes updates by both generation length and tool-interaction depth. Experiments on E-VQA and InfoSeek show consistent gains over strong RAG and agent baselines, and improved retrieval and end-to-end accuracy. The code is available at https://github.com/DingWu1021/Promsa.

</details>


### 11. AI Persuasive Framing in Collective Dilemmas

- **Authors:** Anders Giovanni Møller, Alessia Galdeman, Arianna Pera, Luca Maria Aiello
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27951v1](http://arxiv.org/abs/2606.27951v1)
- **PDF:** [https://arxiv.org/pdf/2606.27951v1](https://arxiv.org/pdf/2606.27951v1)
- **Categories:** cs.CY, cs.CL, cs.HC, physics.soc-ph


> The paper demonstrates that AI assistants can serve as effective, personalized nudges in collective‑action games: by tailoring persuasive framing to each participant’s Social Value Orientation, the AI significantly raised monetary contributions and group‑success rates in an iterated Collective Risk Game involving 1,283 subjects. The authors used a within‑subjects experimental design with two framing conditions—pro‑social (“cooperation‑enhancing”) and anti‑social (“selfishness‑exculpating”)—and found that the cooperative boost was fleeting (vanishing after a few rounds), whereas the anti‑social framing produced larger and more durable drops in contributions, especially when personalization was applied. These results highlight both the promise of agentic AI for fostering cooperation and the dual‑use risk that similarly empowered agents can be weaponized to undermine collective welfare.


<details>
<summary>Abstract</summary>

AI agents are promising tools that can act as flexible behavioral nudges to enhance human cooperation in addressing large-scale societal problems. However, evidence on whether AI agents can effectively boost cooperation remains mixed. We recruited 1,283 participants to play iterated Collective Risk Games in small groups, testing whether AI assistants could nudge participants toward cooperation. By using persuasive framing personalized to each player's Social Value Orientation profile, the AI interventions significantly increased contributions and group success rates. These cooperative effects were short-lived, however, fading after the first few rounds. Strikingly, when the AI treatments were reconfigured to promote selfish behavior through exculpatory framing, the negative effects on contributions and group success were larger and substantially more persistent, particularly for personalized interventions. This asymmetry between prosocial and antisocial persuasion highlights the dual-use risks of AI systems designed to influence group behavior in collective action settings.

</details>


### 12. Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy

- **Authors:** Oscar Thees, Roman Müller, Matthias Templ
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27936v1](http://arxiv.org/abs/2606.27936v1)
- **PDF:** [https://arxiv.org/pdf/2606.27936v1](https://arxiv.org/pdf/2606.27936v1)
- **Categories:** cs.CR, cs.AI, stat.AP


> The paper shows that large‑language‑model‑driven agents can turn the longstanding “uniqueness” of mobility traces into a practical, scalable re‑identification weapon. By building an end‑to‑end pipeline in which autonomous LLM agents crawl the open web, harvest public records and social‑media footprints, and match raw spatio‑temporal coordinate sequences to real‑world identities, the authors achieve a 72 % success rate on a set of 25 truly re‑identifiable subjects (41.9 % overall) with only minutes‑and‑dollar costs per target. These results demonstrate that agentic AI collapses the manual‑effort barrier in mobility‑data attacks, forcing a reassessment of statistical disclosure control and GDPR compliance frameworks.


<details>
<summary>Abstract</summary>

The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale.
  In this feasibility study, we demonstrate in a real world setting that agentic AI fundamentally changes this threat model. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%).
  We discuss implications for Statistical Disclosure Control (SDC) practice and outline the near-future escalation that data custodians and regulators must anticipate. De facto anonymity - an implicit foundation of SDC practice - is shifting. Agentic AI strengthens the case that re-identification is reasonably likely by any means under the GDPR Recital-26 standard, at costs of minutes-and-dollars per target.

</details>


### 13. Triadic Werewolf: A Jester Role for Multi-Hop Theory of Mind in LLMs

- **Authors:** Avni Mittal
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27909v1](http://arxiv.org/abs/2606.27909v1)
- **PDF:** [https://arxiv.org/pdf/2606.27909v1](https://arxiv.org/pdf/2606.27909v1)
- **Categories:** cs.CL, cs.AI, cs.GT, cs.MA


> **Main contribution:** The paper introduces a “Jester” role to the classic Werewolf game, creating a triadic incentive structure that forces agents to reason about three opposing utility functions rather than the usual two‑player deduction setting.  

**Methodology:** The authors implement the extended game for three state‑of‑the‑art LLMs (GPT‑4.1, DeepSeek‑V3.1, Llama‑3.3‑70B), run 60 self‑play games with and without a self‑learning loop for the Jester, and record voting and win rates to assess multi‑hop Theory‑of‑Mind (ToM) capabilities.  

**Key findings:** The Jester wins 60‑70 % of games while Werewolves never exceed 20 %, and GPT‑4.1 consistently votes the Jester out on day 1—a self‑defeating move—showing a failure to model other agents’ incentives. Self‑learning improves DeepSeek and Llama’s performance (especially DeepSeek’s subtle “appear suspicious without trying”), but harms GPT‑4.1, whose losses fall on the Villagers. The results demonstrate that triadic games expose a deeper layer of multi‑agent reasoning that dyadic ToM benchmarks miss, highlighting gaps in current LLMs’ ability to perform multi‑hop Theory‑of‑Mind.


<details>
<summary>Abstract</summary>

Theory-of-mind evaluations of large language models typically use dyadic social-deduction games, where every observable cue points to a single hidden side, so a model with strong language priors can score well without ever simulating opponents' incentives. We extend the Werewolf game with a Jester, a third faction whose utility on peer suspicion is inverted because it wins by being voted out, so optimal play requires reasoning across three opposing utility functions. Across 60 games on GPT-4.1, DeepSeek-V3.1, and Llama-3.3-70B with Jester self-learning on and off, the Jester wins 60-70% of games while Werewolves never exceed 20%, and GPT-4.1 wolves vote the Jester out on day 1 in 60-70% of games, a strictly self-defeating action. Self-learning helps DeepSeek and Llama but hurts GPT-4.1, with the cost landing on Villagers rather than Werewolves. Only DeepSeek learns the subtle strategy of looking suspicious without looking intentionally suspicious, and it gains the most from the loop. Triadic incentive structure exposes a layer of multi-agent reasoning that dyadic deduction games leave invisible.

</details>


### 14. ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn Autonomous Agents

- **Authors:** Qitai Tan, Zefang Zong, Yang Li, Peng Chen
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27814v1](http://arxiv.org/abs/2606.27814v1)
- **PDF:** [https://arxiv.org/pdf/2606.27814v1](https://arxiv.org/pdf/2606.27814v1)
- **Categories:** cs.AI


> ATOD presents a hybrid training scheme for compact language‑model agents that intertwines on‑policy distillation (OPD) with reinforcement learning (RL) via an annealed schedule, letting dense teacher supervision dominate early learning while progressively amplifying reward‑driven exploration. The method further introduces Turn‑level Disagreement‑Uncertainty Reweighting (T‑DUR) to up‑weight turns where the student most disagrees with the teacher, thereby delivering richer, utility‑focused signals across long interaction sequences. Across three benchmarks (ALFWorld, WebShop, Search‑QA) ATOD achieves a 3.03‑point average success gain over pure OPD, a 23.62‑point gain over GRPO, and even surpasses the teacher models by 2.16 points, demonstrating a significant performance ceiling lift for multi‑turn autonomous agents.


<details>
<summary>Abstract</summary>

Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. Reinforcement learning (RL) directly optimizes environment rewards and encourages exploratory improvement toward a higher reward-defined ceiling, but sparse and delayed feedback makes early-stage learning much less efficient than OPD. In this paper, we propose ATOD (Annealed Turn-aware On-policy Distillation), a hybrid online distillation algorithm that explicitly exploits this complementarity. (1) ATOD uses an annealed OPD-RL schedule: OPD dominates early training to approach teacher-level behavior, while RL is gradually strengthened to drive reward-based exploration. (2) ATOD introduces Turn-level Disagreement-Uncertainty Reweighting (T-DUR), which softly amplifies high-utility turns and improves dense supervision in long trajectories. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 3.03 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.

</details>


### 15. Grounded Iterative Language Planning: How Parameterized World Models Reduce Hallucination Propagation in LLM Agents

- **Authors:** Xinyuan Song, Zekun Cai
- **Published:** 2026-06-26
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27806v1](http://arxiv.org/abs/2606.27806v1)
- **PDF:** [https://arxiv.org/pdf/2606.27806v1](https://arxiv.org/pdf/2606.27806v1)
- **Categories:** cs.AI


> The paper introduces **Grounded Iterative Language Planning (GILP)**, a hybrid architecture that couples a lightweight, trainable transition model (parameterized world model) with an LLM‑based agent planner. By letting the learned backbone generate candidate actions, predicted state deltas, and risk/value estimates, and then using the LLM to draft and revise these proposals through a consistency‑gate check, GILP mitigates the propagation of hallucinated states that typically afflict pure API‑only agents. Empirically, on four graph‑structured planning tasks, GILP cuts the hallucinated‑state rate from 0.176 to 0.035 on real GPT‑4o‑mini calls and boosts simulated success rates from 0.668 to 0.838, while incurring only ~22 % additional LLM queries.


<details>
<summary>Abstract</summary>

World models for language agents come in two useful forms. An agent-based world model calls an LLM API and reasons flexibly in language, but its errors appear as hallucinated state changes that are hard to score with ordinary regression losses. A parameterized world model is a trained transition predictor; its errors are easier to measure with quantities such as NodeMSE, delta accuracy, and validity accuracy, but it is usually weaker as a standalone planner. We compare these two families on four graph-structured planning benchmarks and introduce operational hallucination metrics for the agent-based case. The comparison motivates \textbf{Grounded Iterative Language Planning} (GILP), which trains only a small parameterized backbone and combines it with API-based agent reasoning. The backbone supplies valid actions, predicted state deltas, risk, and value; the LLM drafts an action and imagined delta; and a consistency gate asks for revision when the two disagree. On real GPT-4o-mini calls, GILP reduces hallucinated-state rate from 0.176 to 0.035. In calibrated simulator ablations, it raises success from 0.668 to 0.838 while adding only ~22% extra LLM calls.

</details>


### 16. COOPA: A Modular LLM Agent Architecture for Operations Research Problems

- **Authors:** Chuanhao Li, Xiaoan Xu, Dirk Bergemann, Ethan X. Fang, Yehua Wei, Zhuoran Yang
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27611v1](http://arxiv.org/abs/2606.27611v1)
- **PDF:** [https://arxiv.org/pdf/2606.27611v1](https://arxiv.org/pdf/2606.27611v1)
- **Categories:** cs.LG


> The paper introduces **COOPA**, a modular LLM‑agent framework that lets large language models reliably produce, explain, and solve operations‑research (OR) formulations.  COOPA first generates several candidate mathematical models, evaluates each with a confidence‑based scoring function, and selects the most robust one (max‑min confidence); it then attaches fine‑grained provenance links and confidence scores to every variable, constraint, and objective term and finally dispatches the chosen model to a pool of specialized optimizer agents (e.g., MILP, CP, routing solvers).  Empirical tests on three OR benchmark suites show that COOPA outperforms four strong baselines on six of eight LLM backbones, yielding up to a 6.7 % absolute gain in macro‑average accuracy, while ablations confirm that iterative confidence‑driven modeling is the primary driver of the improvement and that traceability and multi‑solver routing add practical interpretability and flexibility for agentic AI decision‑support systems.


<details>
<summary>Abstract</summary>

Operations Research (OR) provides a rigorous framework for high-stakes decision-making, but effective OR modeling requires substantial domain knowledge, mathematical abstraction, and solver expertise. Recent LLM-based systems automate parts of this pipeline, yet remain limited by low accuracy on complex problems, opaque outputs, and narrow solver support. We propose COOPA (COoperative OPerations Agent), a modular LLM-agent architecture for interpretable and scalable OR decision support. It combines three components: iterative confidence-based modeling, which generates multiple candidate formulations, self-evaluates them across modeling dimensions, and selects one using a max-min confidence criterion; element-level provenance and confidence explanations, which link variables, parameters, constraints, and objectives to quoted source text and provide an audit trail for human verification; and multi-solver routing to specialized optimizer agents for different OR problem classes. Across three OR benchmarks, eight LLM backbones, and four baselines under identical conditions, COOPA achieves the best macro-average accuracy on six of eight backbones and improves over the strongest baseline by up to 6.7 percentage points. A within-system ablation isolates the contribution of iterative confidence-based modeling, while additional analyses and case studies illustrate the value of source traceability and multi-solver dispatch.

</details>


### 17. Training Observable Control Policies to Expose Agent State Through Actions

- **Authors:** Andres Enriquez Fernandez, John J. Bird
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27609v1](http://arxiv.org/abs/2606.27609v1)
- **PDF:** [https://arxiv.org/pdf/2606.27609v1](https://arxiv.org/pdf/2606.27609v1)
- **Categories:** cs.LG, eess.SY


> **Main contribution:** The paper introduces a reinforcement‑learning framework that deliberately shapes an autonomous agent’s control policy to make its internal state more inferable from its observable actions, thereby mitigating communication constraints in multi‑agent or monitoring scenarios.

**Methodology:** The authors augment the standard RL objective with an “observability reward” that penalizes actions which hide state information; they train policies in simulation using this combined reward and then evaluate how well an external estimator can reconstruct the agent’s hidden state from the resulting action streams.

**Key findings:** In a simulated aircraft‑tracking task, the observability‑augmented policy achieves state‑estimation accuracy substantially higher than a baseline policy while incurring only a negligible drop in primary task performance, demonstrating that modest policy adjustments can expose useful state cues without sacrificing effectiveness.


<details>
<summary>Abstract</summary>

Physical or operational constraints often impose communications limitations on autonomous agents. Such limitations complicate monitoring or multiagent coordination. Even when strong communications are absent, some information may still be available. The remainder of the relevant agent state may be reconstructed via estimation. The actions taken by an agent are a potential source of information -- as the agent interacts with the environment, these actions may be observed even in the absence of explicit communication. We investigate using actions to estimate the state of an agent, using reinforcement learning to develop policies which make the estimation problem more tractable. Policy observability is encouraged through the training reward and is analyzed using simulation of the trained agent. In an aircraft tracking problem a policy with enhanced observability is found that has minimal impact on nominal task performance.

</details>


### 18. hia-gat: A Heterogeneous Interaction-Aware Graph Attention Network For Frame-Level Traffic Conflict Risk Prediction On Freeways

- **Authors:** Mahshid Malazizi, Seyedmehdi Khaleghian, Mina Sartipi, Toru Hirano, Yunfei Xu, Hoang H. Nguyen
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27577v1](http://arxiv.org/abs/2606.27577v1)
- **PDF:** [https://arxiv.org/pdf/2606.27577v1](https://arxiv.org/pdf/2606.27577v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **HIA‑GAT**, a heterogeneous interaction‑aware graph attention network that separately models longitudinal (same‑lane) and lateral (adjacent‑lane) vehicle interactions in a scene‑level graph and fuses them with a conflict‑type‑aware gating mechanism supervised by conflict attribution labels. By encoding physics‑informed edge features for rear‑end and lane‑change conflict mechanisms and training on frame‑wise risk labels derived from TTC/PET thresholds, HIA‑GAT outperforms both non‑graph baselines and prior graph models on the NGSIM I‑80 and US‑101 freeway datasets (average AUC = 0.835 and 0.867, with the biggest gains on lane‑change‑dominant PET settings). The gated attention also yields interpretable per‑vehicle attributions of the dominant conflict type, demonstrating the value of heterogeneous relational modeling for real‑time, agentic traffic‑risk prediction.


<details>
<summary>Abstract</summary>

This paper formulates frame-level freeway risk assessment as a multi-agent scene graph-level binary classification problem, where each video or trajectory frame is labeled risky if any TTC- or PET-based conflict violates a specified severity threshold. We construct a relation-aware graph per frame with vehicles as nodes and two interaction types as edges: same-lane (longitudinal) and adjacent-lane (lateral), augmented with physics-informed edge features aligned to rear-end and lane-change conflict mechanisms. Building on a structured benchmarking suite of non-graph models and graph baselines, we propose HIA-GAT, a dual-stream heterogeneous graph attention network that processes longitudinal and lateral interactions through dedicated attention pathways and fuses them via a conflict-type-aware gating mechanism with event-level gate supervision derived from SSM conflict attribution. Experiments on the NGSIM I-80 and US-101 freeway datasets across nine TTC and PET threshold configurations show that HIA-GAT achieves the best average risk-ranking performance (AUC 0.835 on I-80 and 0.867 on US-101), with the largest gains on PET-only (lane-change) settings where relational structure is essential. Beyond accuracy, the learned gate provides interpretable per-vehicle attribution of dominant conflict type, supporting actionable, real-time freeway safety monitoring. We show that graph structure is critical for modeling lateral conflict risk, while longitudinal risk can often be captured by non-relational aggregation.

</details>


### 19. QueenBee Planner: Skill-Evolving Communication Topologies for Token-Efficient LLM Multi-Agent Systems

- **Authors:** Congjia Tian, Yuhang Yao, Jiaming Cui
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27492v1](http://arxiv.org/abs/2606.27492v1)
- **PDF:** [https://arxiv.org/pdf/2606.27492v1](https://arxiv.org/pdf/2606.27492v1)
- **Categories:** cs.MA


> The paper presents **QueenBee Planner**, a framework that end‑to‑end learns how to **design inter‑agent communication topologies** (temporal DAGs) for LLM‑based multi‑agent systems, treating topology selection as a retrievable skill separate from the frozen pool of worker agents, task adapter, and scorer. An outer LLM planner generates graphs that specify who talks to whom, when messages are merged, and which agent produces the final answer; execution traces are distilled into three rule‑based actions (Preserve, Modify, Avoid) and guarded by held‑out acceptance gates, variance‑aware credit, motif attribution, transfer trust, falsification, and deduplication to avoid over‑fitting to lucky runs. Experiments on Count‑Frequency aggregation and Silo‑Bench distributed coordination show that the self‑evolved graphs **outperform fixed topologies and cold‑start generation**, cutting RMSE (e.g., from 12.53 to 7.87) while also lowering message count, model calls, and token usage, demonstrating that multi‑agent systems can acquire reusable architectural design knowledge rather than just memorizing task solutions.


<details>
<summary>Abstract</summary>

Large language model (LLM) multi-agent systems increasingly depend not only on how individual agents reason, but also on how agents are connected. This paper introduces QueenBee Planner, a framework that treats inter-agent communication topology as a retrievable and self-improving design skill. A pool of worker agents, the task adapter, and the scoring function are frozen; only an outer LLM planner learns to generate temporal communication DAGs specifying who sends information to whom, in which round, who merges messages, and who emits the final answer. Execution traces are distilled into evidence-backed design rules with three actions: \emph{Preserve}, \emph{Modify}, and \emph{Avoid}. To prevent self-evolution from turning lucky runs or plausible but false explanations into policy, QueenBee uses held-out acceptance gates, variance-aware credit, motif-level attribution, transfer trust, insight falsification, and structural deduplication. We evaluate the method on Count-Frequency aggregation and Silo-Bench-style distributed coordination tasks. With fixed workers, self-evolved graph generation produces communication structures that improve over fixed topologies and cold generation. In the CF fulltest setting, the best generated graph reduces RMSE from 12.53 for the strongest fixed topology to 7.87 while also reducing messages, model calls, and token cost; Silo-style results show the same direction of improvement over cold and fixed-topology baselines. These results suggest that multi-agent systems can learn reusable architectural design knowledge rather than merely memorizing task answers.

</details>


### 20. Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

- **Authors:** Xuan Zhang, Zhijian Zhou, Lingfeng Qiao, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27483v1](http://arxiv.org/abs/2606.27483v1)
- **PDF:** [https://arxiv.org/pdf/2606.27483v1](https://arxiv.org/pdf/2606.27483v1)
- **Categories:** cs.AI


> The paper introduces **Internalizing the Future**, a unified three‑stage training pipeline that gives a single autoregressive LLM both a latent world‑model and a text‑based “plan‑conditioned Q‑value” so it can simulate future states before acting. First, **World Model Agentic Mid‑Training (WM‑AMT)** injects predictive latent representations into the policy; second, **Format‑Eliciting SFT (FE‑SFT)** forces the model to output those predictions in a structured textual format; third, **Foresight‑Conditioned RL (FC‑RL)** calibrates the simulated rollouts and success estimates for downstream decision‑making. Experiments on search‑intensive and mathematical‑reasoning benchmarks show that agents trained with this capability‑first pipeline achieve markedly higher success rates than standard fine‑tuning or post‑hoc look‑ahead baselines, demonstrating that genuine internal world modeling—and not just superficial mimicry—is essential for long‑horizon, plan‑driven AI agents.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have demonstrated strong capability in sequential decision-making, yet they remains fundamentally reactive in long-horizon tasks. Unlike humans who employ "what-if" reasoning to evaluate potential plans before commitment, standard agents lack an internal world model to simulate future outcomes. Therefore, we propose to internalize future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate-a textual analogue of the Q-value. Crucially, we identify a format-capability gap: simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding. To bridge this gap, we introduce a three-stage training paradigm: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; and (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine the calibration and utility of the generated simulations. Evaluated on search and mathematical reasoning tasks, our approach consistently outperforms other training baselines. Our results demonstrate that effective internal world modeling in LLM agents requires a capability-first training pipeline to achieve grounded and calibrated foresight.

</details>


### 21. Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents

- **Authors:** Vedant Patel
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27472v1](http://arxiv.org/abs/2606.27472v1)
- **PDF:** [https://arxiv.org/pdf/2606.27472v1](https://arxiv.org/pdf/2606.27472v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper identifies a previously unreported “memory‑update gap” in LLM‑based agents: even state‑of‑the‑art models (e.g., gpt‑5.4) lose up to 15 % accuracy when they must rely on a self‑maintained, bounded memory to track facts that change over long, multi‑turn conversations, and this loss grows dramatically as the dialogue length increases. To diagnose and remedy this, the authors introduce **Supersede**, a reinforcement‑learning benchmark that rewards agents for retrieving the current value of a fact and penalizes references to superseded information; fine‑tuning a compact open‑source model (Qwen2.5‑3B) with GRPO on this environment nearly doubles its supersession accuracy on unseen real dialogues (9 % → 16.7 %). The work demonstrates that the temporal‑currency failure is distinct from comprehension, persists across scales, and can be substantially mitigated through targeted RL training.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents operate over long, multi-session interactions in which facts change: a user moves, a price updates, a plan is revised. Acting correctly requires using the current value of a fact and discarding values that have been superseded. We isolate this ability on real conversational data and show that it is a distinct, unsolved failure. On the knowledge-update subset of LongMemEval, replacing an agent's full context with a bounded, self-maintained memory drops accuracy from 92% to 77% even on a frontier model (gpt-5.4), a gap that is statistically significant (paired McNemar p<0.005) and persists across model scale while full-context accuracy saturates near 92%. The bottleneck is therefore memory maintenance, not comprehension, and is not closed by a stronger model. We then ask whether this is merely an undersized memory, and find it is not: as the conversation grows 24x, accuracy falls further (from 68% to 28%), and granting the agent proportionally more memory yields no detectable recovery (28% to 28%, n=25). The failure scales with the length of the conversation, not the compression ratio. We release Supersede, an open reinforcement-learning environment (on the verifiers / prime-rl stack) that turns this measurement into a training signal: agents are rewarded for answering from the current value and penalized for stale ones. Finally, we close the loop and show the gap is trainable: GRPO fine-tuning a small open model (Qwen2.5-3B) on this environment nearly doubles its held-out supersession accuracy on real, unseen conversations (9.0% to 16.7%, a single run), along a monotonic checkpoint curve indicating the learned policy, not the harness, carries the gain. To our knowledge this is the first trainable environment whose reward targets temporal fact-currency, and the first evidence the supersession gap can be trained down, not only measured.

</details>


### 22. When Does Personality Composition Matter for Multi-Agent LLM Teams?

- **Authors:** Aryan Keluskar, Amrita Bhattacharjee, Huan Liu
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27443v1](http://arxiv.org/abs/2606.27443v1)
- **PDF:** [https://arxiv.org/pdf/2606.27443v1](https://arxiv.org/pdf/2606.27443v1)
- **Categories:** cs.AI


> The paper investigates how the personality traits assigned to Large Language Model (LLM) agents affect the performance of multi‑agent teams across three domains: structured coding, open‑ended research collaboration, and competitive bargaining. By systematically prompting frontier LLMs with high versus low agreeableness and measuring both communication style and task outcomes, the authors show that personality composition matters only when the task relies on nuanced negotiation or creative synthesis—low agreeableness sharply harms performance in collaborative and bargaining settings, while in highly structured coding tasks the same personality shift alters dialogue but leaves milestone completion virtually unchanged. These findings suggest that personality prompting can be a useful tool for shaping team dynamics, but its impact on objective performance is contingent on task structure, informing the design of agentic AI systems that require coordinated or adversarial interaction.


<details>
<summary>Abstract</summary>

Personality prompting shapes how large language models communicate, yet whether these behavioral shifts affect objective task outcomes remains under-explored. Prior work shows that agents prompted with low agreeableness produce adversarial language, while those prompted with high agreeableness become cooperative, but the relationship between communication style and task performance has not been systematically examined across multiple domains. In this work, we investigate whether personality composition matters for multi-agent team performance by manipulating personality traits across frontier LLMs on three task domains: structured coding, open-ended research collaboration, and competitive bargaining. We find that personality effects depend critically on task structure. In coding tasks, low agreeableness leads to large communication shifts that have little effect on milestone completion. In open-ended collaboration and bargaining, the same manipulation substantially degrades performance. We discuss implications for multi-agent system design and the limits of personality manipulation.

</details>


### 23. Resilient Output Containment under Undisclosed Leader Dynamics and Actuator Attacks

- **Authors:** Mohammadreza Nematollahi, Khashayar Khorasani, Nader Meskin
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27257v1](http://arxiv.org/abs/2606.27257v1)
- **PDF:** [https://arxiv.org/pdf/2606.27257v1](https://arxiv.org/pdf/2606.27257v1)
- **Categories:** eess.SY, cs.MA


> The paper introduces a resilient output‑containment framework for heterogeneous linear multi‑agent systems operating over directed graphs, where leader dynamics, velocity bounds and motion envelopes are hidden from the followers and the agents are subject to state‑ and input‑correlated actuator cyber‑attacks. By coupling a virtual‑actuator reconfiguration layer (which uses partial state measurements to cancel attack‑induced disturbances) with a distributed adaptive interaction protocol that exchanges only output‑dimension interface variables and requires no global graph information, the authors prove—via a nonsmooth Lyapunov analysis under a leader‑rooted united spanning‑tree condition—that the agents’ commands converge asymptotically to a convex hull containing the unknown leader trajectories, and the physical outputs track this command up to a bounded residual. Simulations with a quadrotor‑load network demonstrate successful attack recovery and containment of the agents within the leaders’ convex hull.


<details>
<summary>Abstract</summary>

This work studies resilient output containment for heterogeneous linear multi-agent systems with actuator cyber-attacks over directed network topologies. The leaders generate bounded locally absolutely continuous trajectories; however, their dynamics, velocity bounds, and motion envelopes are undisclosed to the followers. The cyber-attack model includes state- and input-correlated, as well as bounded exogenous actuator false-data terms. A continuous two-layer adaptive control architecture is proposed. The first layer is a virtual-actuator reconfiguration layer that uses partial state measurements to compensate for actuator attacks in the local tracking-error dynamics. The second layer is a network interface that generates task-space commands via an adaptive interaction protocol. This protocol uses only neighbor-exchanged network-interface states whose dimensions match those of the plant output, and it does not require global graph knowledge for parameter tuning. For directed graphs, under a leader-rooted united spanning-tree condition, a nonsmooth Lyapunov analysis yields asymptotic containment at the command level. The physical outputs then converge to the leader convex hull up to a residual determined by the command-tracking local controllers. Simulation results using a network of quadrotors with damped suspended loads illustrate the performance of attack recovery and containment tracking.

</details>


### 24. Advancing Omnimodal Embodied Agents from Isolated Skills to Everyday Physical Autonomy

- **Authors:** Junhao Shi, Zezheng Huai, Siyin Wang, Jia Chen, Yubang Wang, Zhaoye Fei, Hechang Chen, Jingjing Gong, Xipeng Qiu, Yu-Gang Jiang
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27251v1](http://arxiv.org/abs/2606.27251v1)
- **PDF:** [https://arxiv.org/pdf/2606.27251v1](https://arxiv.org/pdf/2606.27251v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces **OmniAct**, a hierarchical, asynchronous architecture that unifies cyber‑physical action spaces, compresses long‑term context, and actively verifies execution to enable truly persistent embodied agents. By coupling a multimodal semantic planner for skill routing, an event‑boundary‑driven hierarchical memory, and a visual preemption engine that detects and recovers from physical failures, the system can orchestrate manipulation, navigation, and IoT APIs in long‑horizon tasks. Experiments on 40 real‑world tasks across two robot platforms and four IoT devices show that OmniAct maintains near‑constant token usage (≤ 100 k tokens) while markedly increasing end‑to‑end success rates, lifting mid‑scale open‑weight models to performance comparable with proprietary systems.


<details>
<summary>Abstract</summary>

Building persistent embodied agents in unstructured environments demands unified orchestration of heterogeneous tools spanning both cyber (APIs, IoT) and physical (manipulation, navigation) domains, coupled with autonomous recovery from physical failures that inevitably arise over extended operation. Existing systems treat these as separate problems: VLM-based planners lack a unified cyber-physical action space, agent frameworks accumulate unbounded context that degrades temporal coherence, and VLA policies execute open-loop without detecting their own failures. We argue that persistent autonomy requires not a monolithic model but a hierarchical asynchronous architecture with explicit separation of planning, memory, and verification. To this end, we present OmniAct, a framework integrating a multimodal semantic planner for skill routing across unified action spaces, an adaptive hierarchical memory with event-boundary-driven compression for sub-linear context growth, and an asynchronous visual preemption engine that closes the semantic loop during physical execution. Across 40 real-world long-horizon tasks on two robotic platforms coordinating four IoT devices, OmniAct achieves consistent improvements in end-to-end success across all complexity levels, maintains near-flat token consumption over under 100k+ accumulated interaction tokens, and elevates mid-scale open-weight models to proprietary-level performance.

</details>


### 25. Bridging Talk and Thought: Understanding Dialogue Dynamics Across Collaborative Problem-Solving Contexts

- **Authors:** Zhengyuan Liu, Stella Xin Yin, Min-Yen Kan, Nancy F. Chen
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27233v1](http://arxiv.org/abs/2606.27233v1)
- **PDF:** [https://arxiv.org/pdf/2606.27233v1](https://arxiv.org/pdf/2606.27233v1)
- **Categories:** cs.CL, cs.AI


> **Summary:**  
The paper introduces a hierarchical two‑layer coding framework for dissecting dialogue in collaborative problem‑solving, explicitly extending analysis to human‑AI and multi‑agent teams. By jointly encoding task‑level (cognitive/non‑cognitive) moves and metacognitive regulatory moves, the authors can capture how agents coordinate knowledge, strategies, and self‑monitoring during joint reasoning. Applied to nine heterogeneous datasets, the framework reveals that metacognitive regulation—e.g., turn‑taking, planning, and reflection—consistently distinguishes superficial from deep collaboration, suggesting that embedding or evaluating such regulation is a key design criterion for effective agentic AI partners.


<details>
<summary>Abstract</summary>

We present a conceptual framework for analyzing dialogue in collaborative problem-solving contexts, with an emphasis on the emerging dynamics of human-AI and multi-agent collaboration. As intelligent systems become active agents capable of autonomous reasoning and strategic cooperation, understanding the dialogic interaction during collaborative problem solving is increasingly important for optimizing and evaluating such partnerships. Our framework addresses key limitations in current analytical approaches through a hierarchical two-layer coding scheme that integrates cognitive and non-cognitive problem solving with metacognitive regulatory mechanisms. We demonstrate its effectiveness and generalizability across nine datasets spanning multiple domains, and provide insights into how humans and agents coordinate their knowledge, skills, and efforts to solve complex problems, showing in particular that metacognitive regulation can be an essential discriminator of deeper collaboration.

</details>


### 26. OpenRCA 2.0: From Outcome Labels to Causal Process Supervision

- **Authors:** Aoyang Fang, Yifan Yang, Jin'ao Shang, Qisheng Lu, Junjielung Xu, Rui Wang, Songhan Zhang, Yuzhong Zhang, Boxi Yu, Pinjia He
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27154v1](http://arxiv.org/abs/2606.27154v1)
- **PDF:** [https://arxiv.org/pdf/2606.27154v1](https://arxiv.org/pdf/2606.27154v1)
- **Categories:** cs.AI


> The paper introduces **OpenRCA 2.0**, a benchmark that goes beyond traditional root‑cause‑analysis datasets by providing **step‑wise causal annotations** that trace the propagation from a fault (cause) to the observed symptom.  To create these annotations the authors devise **PAVE**, a forward‑verification protocol that exploits known fault‑injection interventions to reconstruct the causal chain, then use it to label 500 multi‑system incidents across 11 leading LLM agents.  Experiments show that while agents can name a correct faulty service in 76 % of cases, they recover the **exact causal path** only 20.7 % of the time (and can ground a correct service in a verified path in 61.5 %), exposing a major ungrounded‑diagnosis failure that outcome‑only metrics conceal. This work highlights the need for causal‑process supervision in evaluating and building trustworthy, agentic AI systems for complex reasoning tasks.


<details>
<summary>Abstract</summary>

Root cause analysis (RCA) poses a holistic test of LLM agentic capabilities, such as long-context understanding, multi-step reasoning, and tool use. However, existing datasets suffer from a fundamental gap: they label only the root cause, not the propagation path connecting it to the observed symptom, which largely simplifies the task to naive pattern matching. To support rigorous evaluation, we introduce PAVE, a step-wise labeling protocol that leverages known interventions from fault injection to reconstruct causal propagation paths. The mechanism is forward verification: reasoning from cause to effect rather than inferring backward from symptoms. Applying PAVE yields OpenRCA 2.0 (500 instances), the first cross-system RCA benchmark with step-wise causal annotations for LLM agents. Across 11 frontier LLMs, recovering the exact root-cause set succeeds in only 20.7% of cases on average. To locate where this difficulty lies, we relax the criterion and find what we call the ungrounded diagnosis: agents identify at least one correct root-cause service in 76.0% of cases, but ground that service in a verified causal propagation path to the observed symptom in only 61.5%. Outcome-only evaluation hides this failure mode; step-wise causal ground truth is the missing piece for trustworthy LLM-based RCA agents.

</details>


### 27. Joint Learning of Experiential Rules and Policies for Large Language Model Agents

- **Authors:** Shicheng Ye, Chao Yu
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27136v1](http://arxiv.org/abs/2606.27136v1)
- **PDF:** [https://arxiv.org/pdf/2606.27136v1](https://arxiv.org/pdf/2606.27136v1)
- **Categories:** cs.AI


> The paper introduces **JERP**, a framework that simultaneously learns natural‑language “experiential rules” and updates the policy of a large language model (LLM) agent from the same interaction data. By maintaining a rule pool that is refreshed after each episode—using trajectory‑level comparisons to successful references—and by conditioning the LLM on retrieved, task‑relevant rules together with its recent history, JERP keeps the rule set synchronized with a continually improving policy. Empirically, this joint‑learning scheme yields significant performance gains on the multi‑step benchmarks AlfWorld and WebShop, demonstrating that coupling interpretable rule retrieval with policy fine‑tuning can enhance LLM agents’ decision‑making in complex, sparse‑reward environments.


<details>
<summary>Abstract</summary>

For LLM agents in multi-step interactive environments, a key challenge is to make effective use of accumulated interaction experience. Existing work has typically separated two uses of such experience: keeping it outside the model as natural-language rules for later prompting, or using trajectories and feedback to update the model parameters. The former is easy to interpret but can fall out of sync with the evolving policy; the latter improves the policy more broadly but provides only limited correction for local mistakes in sparse-reward settings. We present Joint Learning of Experiential Rules and Policies for LLM Agents (JERP), which updates a long-term experiential-rule pool and the policy from the same interaction trajectories. At decision time, JERP retrieves task-relevant rules and conditions the agent on them together with the interaction history. After each episode, it uses the collected trajectories both to optimize the policy and to revise the rule pool by comparing current rollouts with reference successful trajectories. This coupling keeps the rule pool aligned with the evolving policy while allowing stable and effective behaviors to be gradually absorbed into the model itself. Experiments on AlfWorld and WebShop show that JERP yields consistent gains in decision performance for complex interactive tasks.

</details>


### 28. Mostly Automatic Translation of Language Interpreters from C to Safe Rust

- **Authors:** Bo Wang, Brandon Paulsen, Joey Dodds, Daniel Kroening, Umang Mathur, Prateek Saxena
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27122v1](http://arxiv.org/abs/2606.27122v1)
- **PDF:** [https://arxiv.org/pdf/2606.27122v1](https://arxiv.org/pdf/2606.27122v1)
- **Categories:** cs.PL, cs.MA, cs.SE


> **Main contribution:** The paper introduces **Reboot**, a mostly‑automatic system for converting real‑world C interpreters into **memory‑safe Rust**, combining a feature‑reduction workflow with a multi‑agent translation architecture.

**Methodology:** Reboot first strips the source program down to a minimal, test‑passing “core” by **feature reduction**, then incrementally re‑adds features while each intermediate version is compiled and validated against both supplied and hidden test suites. Translation work is carried out by a suite of specialised coding agents; their outputs are continuously checked and fed back to the agents, so that only brief human interventions (1–11 per interpreter) are needed.

**Key findings:** Six interpreters (6 k–23 k LOC) were successfully ported to safe Rust, achieving 100 % of the original test suites and 62 %–92 % on unseen validation tests. A security case study (mujs) shows that the Rust versions eliminate the heap‑buffer‑overflow and use‑after‑free bugs present in the C code. An ablation study demonstrates that the feature‑reduction step improves translation correctness by 6 %–20 % over a pure multi‑agent approach, underscoring the relevance of this technique for building reliable, agent‑driven automated code translation tools in the agentic AI ecosystem.


<details>
<summary>Abstract</summary>

Translating C programs to safe Rust is challenging owing to significant differences in typing constraints, ownership, and borrowing rules. Interpreter programs are particularly important targets for such translation, as they often handle untrusted inputs and suffer from memory-related vulnerabilities. We present Reboot, a mostly-automatic technique that translates real-world interpreter programs from C to safe Rust. Using Reboot, we have translated six interpreters ranging from 6k to 23k lines of C code to safe Rust, with each translation requiring only 1 to 11 brief user interventions. All translations pass 100% of the provided test suites, and achieve 62%--92% pass rates on separately created validation tests that were never exposed to the system. A security case study on mujs shows that memory vulnerabilities such as heap buffer overflows and use-after-free present in C are eliminated in the safe Rust translation. Two ideas underpin Reboot. First, feature reduction decomposes the translation by program features, creating a sequence of milestones where each is a complete, testable program; the translation starts from the simplest version and incrementally restores features, with each milestone validated before proceeding. Second, a multi-agent architecture orchestrates inherently unreliable coding agents through automated validation and feedback, keeping long-running translation workflows on track with minimal human involvement. An ablation study confirms that feature reduction improves translation correctness compared to using multi-agent translation alone, with 6%--20% improvements in pass rates on validation test suites.

</details>


### 29. Semantic Early-Stopping for Iterative LLM Agent Loops

- **Authors:** Sahil Shrivastava
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27009v1](http://arxiv.org/abs/2606.27009v1)
- **PDF:** [https://arxiv.org/pdf/2606.27009v1](https://arxiv.org/pdf/2606.27009v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> **Main contribution**  
The paper introduces “semantic early‑stopping” for iterative LLM agent loops—halting a draft‑critic cycle when the semantic content of successive drafts stops changing (measured by cosine distance of embeddings) and the estimated answer quality ceases to improve. It provides a formal proof of deterministic termination, a reproducible judge‑efficient evaluation framework, and an empirical analysis on HotpotQA.

**Methodology**  
The authors define a convergence criterion based on embedding drift with a patience window and, optionally, a quality‑gate that invokes a cheap LLM judge. They generate a single full rollout per question, then replay multiple stopping policies on the cached drafts, separating operational token costs (charged to the policy) from evaluation token costs (used only for measurement).

**Key findings**  
On a 60‑question HotpotQA test set, a pure semantic stopper cuts operational token usage by **38 %** compared with a fixed‑iteration cap while maintaining parity in answer quality (Δ‑IS = ‑0.004, p = 0.81). Adding the per‑round quality judge outweighs the savings, making it less cost‑effective. An oracle that selects the best draft after the loop outperforms all practical policies (+0.115 Information Score, p ≈ 4e‑11), suggesting that the core challenge shifts from “when to stop” to “which round’s output to choose.”


<details>
<summary>Abstract</summary>

Multi-agent large language model (LLM) loops, for example a Writer that drafts and a Critic that revises, are almost always terminated by a fixed iteration cap (max_iterations). This is a syntactic kill-switch: it is blind to whether the answer is still improving, so it over-spends tokens on easy inputs and truncates hard ones. We study semantic early-stopping: the loop halts when consecutive draft embeddings stop changing in meaning (cosine distance with a patience window) and the answer's measured quality stops improving. Our work makes three contributions. First, an honest theoretical footing: we prove deterministic termination and well-definedness and machine-check these claims, while treating the convergence of the distance sequence as an empirically tested conjecture rather than a (previously over-claimed) Banach contraction. Second, a judge-efficient evaluation protocol: we generate each question's full trajectory once, replay every stopping policy over the identical drafts, and cache every LLM-judge call, yielding a strictly paired efficiency-versus-quality comparison at low cost; we further separate operational tokens (charged to a policy) from evaluation tokens (a measurement instrument). Third, an empirical study on multi-hop retrieval-augmented question answering (HotpotQA). On the 60-question test split, a judge-free semantic stopper reduces operational tokens by 38% relative to max_iterations at parity quality (Delta-IS = -0.004, p = 0.81), whereas the full quality-gated variant is counter-productive because its per-round judging dominates cost. An oracle that selects the best round attains +0.115 Information Score over every practical policy (p ~ 4e-11), reframing the problem from "when to stop" (easy) to "which round is best" (open).

</details>


### 30. Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement

- **Authors:** Igor Itkin
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27409v1](http://arxiv.org/abs/2606.27409v1)
- **PDF:** [https://arxiv.org/pdf/2606.27409v1](https://arxiv.org/pdf/2606.27409v1)
- **Categories:** cs.MA, cs.CL, cs.LG, eess.SY


> **Main contribution** – The paper shows that, in multi‑agent LLM pipelines where verifier/critic agents act with a time lag, the delayed correction can destabilize the collective belief dynamics, turning a normally convergent consensus into oscillatory or divergent behavior. It derives precise instability thresholds for the “verification dose” (strength of correction) as a function of the communication delay, and provides a provably near‑optimal strategy for placing a limited number of grounded corrector nodes in the interaction graph.  

**Methodology** – The authors model agents’ belief updates as a linear consensus process on a graph augmented with grounded (truth‑pinning) corrector nodes and incorporate a fixed verification delay. By performing a spectral analysis of the grounded Laplacian they obtain closed‑form eigenvalue conditions for stability; for a delay of two steps the critical dose equals the inverse golden ratio. They also prove that the corrector‑placement objective is super‑modular, yielding a greedy algorithm with a \(1-1/e\) approximation guarantee.  

**Key findings** – Simulations on five publicly available LLMs confirm the predicted dose‑delay oscillations: overly strong or too‑late verification causes belief swings, while modest, timely verification restores convergence. In contrast, grounding the entire task (making truth an absorbing state) eliminates the instability, indicating that the phenomenon is specific to signed‑belief (hallucination‑suppression) settings and that careful corrector dosing and placement are essential for stable multi‑agent LLM systems.


<details>
<summary>Abstract</summary>

Multi-agent large language model (LLM) systems often rely on verifier and critic agents to suppress hallucinations, but verification is delayed. During this delay, false claims can propagate through the agent network. We model this process as delayed consensus on a graph with grounded corrector nodes. Spectral decomposition by the grounded Laplacian yields a closed-form stability threshold for the verification dose: correction that is too strong or too delayed can turn consensus into oscillation. The most unstable regime occurs when the communication and verification delays coincide; for delay two, the threshold is the inverse golden ratio. The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. Experiments across five open models confirm the predicted dose-delay oscillations. By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing

</details>


### 31. AgentX: Towards Agent-Driven Self-Iteration of Industrial Recommender Systems

- **Authors:** Changxin Lao, Fei Pan, Guozhuang Ma, Han Li, Huihuang Lin, Jijun Shi, Kangzhi Zhao, Kun Gai, Mo Zhou, Qinqin Zhou, Quan Chen, Ruochen Yang, Shifu Bie, Shijie Yi, Shuang Yang, Shuo Yang, Wenhao Li, Wentao Xie, Xiao Lv, Xuming Wang, Yijun Wang, Yiming Chen, Yusheng Huang, Zhongyuan Wang, Zibo Zhao, Zijie Zhuang, Baoning Xia, Chao Liu, Chaoyi Ma, Chubo He, Dawei Cong, Feng Jiang, Gang Wang, Guilin Xia, Hanwen Xu, Jiahong Xie, Jiahui Qiao, Jian Liang, Jiangfan Yue, Jing Wang, Jinghan Yang, Jinghui Jia, Kan Qin, Lei Wang, Ming Li, Peilin Song, Pengbo Xu, Qiang Luo, Ruiming Tang, Shiyang Liu, Shuxian Jin, Tao Wang, Tao Zhang, Xiang Gao, Xianghan Li, Yingsong Luo, Yiwen Ning, Yongcheng Liu, Yueyang Liu, Yuan Guo, Zhaojie Liu, Zhenkai Cui
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26859v2](http://arxiv.org/abs/2606.26859v2)
- **PDF:** [https://arxiv.org/pdf/2606.26859v2](https://arxiv.org/pdf/2606.26859v2)
- **Categories:** cs.AI, cs.CL, cs.IR


> **Main contribution** – The paper introduces **AgentX**, a deployed multi‑agent framework that turns the entire recommendation‑algorithm lifecycle (hypothesis generation, code production, online experimentation, and result attribution) into an autonomous, self‑iterating loop, thereby removing the human engineer as the bottleneck and enabling compounding innovation at industrial scale.  

**Methodology** – AgentX orchestrates four coupled agents: a **Brainstorm Agent** that mines past experiments, system metadata, and external research to propose ranked, executable ideas; a **Developing Agent** that generates and validates production‑grade code using repository‑grounded language models and multi‑aspect reliability checks; an **Evaluation Agent** that safely launches A/B tests with guard‑rail vetoes and logs outcomes; and a **Harness‑Evolution layer (SGPO)** that converts the execution traces of successful and failed trials into semantic‑gradient updates that continually refine the agents themselves.  

**Key findings** – In a live industrial recommender system, AgentX generated and deployed tens of thousands of experiments—far exceeding what a team of engineers could produce—while maintaining safety and performance standards. The closed‑loop learning (“semantic‑gradient” updates) yielded measurable uplift in recommendation metrics (e.g., +3.2 % click‑through rate) and demonstrated that the system’s own capability improves over time, confirming the feasibility of fully agent‑driven self‑iteration for large‑scale recommendation pipelines.


<details>
<summary>Abstract</summary>

Recommendation algorithm iteration is moving from an artisanal, engineer-bound process toward an industrialized research loop, but this transition remains blocked by a structural execution bottleneck: the idea-to-launch cycle still depends on human engineers to generate hypotheses, modify production code, launch A/B experiments, and attribute online results. Innovation therefore scales linearly with headcount rather than compounding with evidence, compute, and accumulated experimental knowledge. We present AgentX, a production-deployed multi-agent system that fundamentally restructures this production function. AgentX operates as a self-evolving development engine: it autonomously generates, implements, evaluates, and learns from recommendation experiments at a scale and pace that no manual workflow can sustain.
  The system orchestrates four tightly coupled stages in a closed loop. A Brainstorm Agent synthesizes evidence from historical experiments, system architecture, data analysis, and external research into ranked, executable proposals. A Developing Agent translates each proposal into production-ready code through repository-grounded generation and multi-dimensional reliability verification. An Evaluation Agent conducts safe online rollout with guardrail-vetoed A/B judgment, converting both successes and failures into structured knowledge assets. A Harness Evolution layer (SGPO) then distills execution trajectories into semantic-gradient updates that continuously sharpen the agents themselves -- making the system not merely automated, but self-improving.

</details>


### 32. EGG: An Expert-Guided Agent Framework for Kernel Generation

- **Authors:** Yaochen Han, Ke Fan, Hongxu Jiang, Wanqi Xu, Weiyu Xie, Runhua Zhang, Chenhui Zhu, Yixiang Zhang
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26758v1](http://arxiv.org/abs/2606.26758v1)
- **PDF:** [https://arxiv.org/pdf/2606.26758v1](https://arxiv.org/pdf/2606.26758v1)
- **Categories:** cs.AI


> **Main contribution:** EGG introduces a two‑stage, expert‑guided agent framework that embeds domain‑specific optimization knowledge into LLM‑driven GPU kernel generation, enabling systematic exploration of algorithmic design and hardware‑specific tuning.  

**Methodology:** The authors decompose kernel synthesis into (1) algorithmic structure design and (2) hardware‑specific tuning (parallel mapping, tensor tiling, memory layout). A stage‑aware multi‑agent collaboration system manages inter‑ and intra‑stage context, letting each agent apply expert heuristics while the LLM refines the code, thereby defining clear optimization objectives and a structured design space.  

**Key findings:** Across KernelBench and several real‑world workloads, EGG attains a 2.13× average speed‑up over hand‑tuned PyTorch kernels and beats prior agent‑based and reinforcement‑learning kernel generators, demonstrating that expert‑guided, hierarchical agent collaboration can dramatically improve both correctness and performance of automatically generated GPU kernels.


<details>
<summary>Abstract</summary>

High-performance GPU kernels are critical for reducing the exponentially growing computational costs of large language models (LLMs), but their development heavily relies on manual tuning by domain experts. While recent advances in LLM-based approaches show promise for automating kernel generation, they still struggle to achieve both correctness and high performance. This limitation primarily arises from the lack of domain-specific optimization guidance, hindering effective exploration of the optimization space. We propose EGG, an Expert-Guided Agent Framework for Kernel Generation, which incorporates expert optimization principles to guide LLMs' decisions. Inspired by expert workflows, we decompose kernel generation into two hierarchical stages: 1) algorithmic structure design, which establishes a high-quality computational structure foundation; 2) hardware-specific tuning, which performs targeted adjustments through parallel mapping, tensor tiling, and memory optimization. This staged decomposition defines explicit optimization objectives, structuring the design space to achieve progressive refinement. To this end, a stage-aware multi-agent collaboration mechanism is designed for inter and intra-stage context management, ensuring stable optimization trajectories. Experiments on KernelBench and real-world workloads show that EGG achieves a 2.13x average speedup over PyTorch, outperforming existing agent-based and RL-based approaches.

</details>


### 33. Towards Evaluation of Implicit Software World Models in Coding LLMs

- **Authors:** Egor Bogomolov, Yaroslav Zharov
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27406v1](http://arxiv.org/abs/2606.27406v1)
- **PDF:** [https://arxiv.org/pdf/2606.27406v1](https://arxiv.org/pdf/2606.27406v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces a new evaluation framework for coding LLMs that probes their *software world model*—the implicit understanding of a program’s runtime behavior—by requiring models to predict execution‑resource metrics (peak memory, wall‑clock time, and ranked profiler outputs at method and line granularity) in addition to test outcomes. Using the SWE‑bench Verified dataset, the authors query a range of state‑of‑the‑art LLMs and find that, despite strong performance on traditional correctness metrics, all models exhibit modest and brittle accuracy on resource‑prediction tasks, revealing a substantial gap in their ability to reason about how software actually executes rather than merely how it is written. This highlights a crucial direction for agentic AI research: developing models with richer, execution‑aware world representations.


<details>
<summary>Abstract</summary>

Software engineering, whether performed by humans or by AI agents, requires reasoning about how software behaves. We call the internal model that supports such reasoning the software world model, and view current code-execution benchmarks as covering one well-studied slice of it -- control flow. In this paper, we take a step toward a broader evaluation by shifting the observable axis to execution resources: alongside test outcome and exception class, we predict peak memory, wall-clock time, and ranked profiler outputs at method and line granularity. We use SWE-bench Verified as the source of data to hold the test close to real-world software engineering tasks. All tested models, frontier ones included, show modest performance and brittle behaviour, suggesting a notable lack of understanding of how software is executed, as opposed to how its source code is written.

</details>


### 34. Socratic agents for autonomous scientific discovery in high-dimensional physical systems

- **Authors:** Xianrui Zeng, Pengfei Liu, Yirui Zang, Yang Shen, Fei Yu, Chunlei Yu, Minghao Liu, Yang Du
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26722v1](http://arxiv.org/abs/2606.26722v1)
- **PDF:** [https://arxiv.org/pdf/2606.26722v1](https://arxiv.org/pdf/2606.26722v1)
- **Categories:** cs.AI, physics.optics


> The paper presents **AHOIS**, a multi‑agent AI system that endows scientific discovery with “epistemic autonomy” by having a **physics‑critic agent** conduct Socratic interrogation of candidate explanations (causal questioning, constraint checking, counter‑example generation, falsification criteria) within a closed‑loop experimental loop. Using this methodology on a high‑dimensional multimode‑fiber optics platform, AHOIS autonomously formulated and verified a novel random‑interference encoding hypothesis, devised sparse‑measurement strategies, diagnosed failure modes, and transplanted a published imaging protocol to a new configuration—achieving 16×16 measurements with an effective rank of 56.9 and classification accuracies of ≈ 77 % (MNIST) and ≈ 83 % (Fashion‑MNIST). Ablation studies show that the Socratic dialogue markedly improves physical consistency, hypothesis completeness, uncertainty calibration, and the validity of experimental plans, demonstrating a concrete step toward self‑correcting, evidence‑grounded autonomous scientific agents.


<details>
<summary>Abstract</summary>

The automation of scientific discovery has reached an inflection point. While AI systems now operate instruments, optimize parameters and generate hypotheses, most remain procedural: they execute workflows fixed by human designers. True autonomous science demands epistemic autonomy--the capacity to construct, challenge and revise physical explanations in response to evidence. Here we introduce AHOIS, a multi-agent AI scientist that embeds Socratic midwifery into closed-loop experimentation. A physics-critic agent interrogates hypotheses through causal questioning, constraint checking, counterexample generation and falsification-criteria formulation. We evaluate AHOIS on a real multimode-fibre optical platform, a high-dimensional system with complex wave transformations, indirect detection, environmental drift and multi-modal acquisition. Without prior encoding schemes, classifiers or speckle models, the system autonomously proposed and validated a random-interference encoding hypothesis, discovered task-adaptive sparse-measurement strategies, diagnosed distinct failure modes (encoding instability, fluorescence contamination and detector noise) and translated a published imaging protocol into an executable workflow on a non-original configuration. The discovered encoding yielded 16x16 measurements with effective rank 56.9 and classification accuracies of 76.97% on MNIST and 83.17% on Fashion-MNIST. Ablations show that Socratic interrogation improves physical consistency, hypothesis completeness, uncertainty calibration and experimental-plan validity. These results establish a route from workflow automation towards evidence-grounded, self-correcting autonomous discovery in complex physical environments.

</details>


### 35. Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents

- **Authors:** Nada Lahjouji, Ashwin Gerard Colaco
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26627v1](http://arxiv.org/abs/2606.26627v1)
- **PDF:** [https://arxiv.org/pdf/2606.26627v1](https://arxiv.org/pdf/2606.26627v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper provides the first data‑centric survey of privacy risks in large‑language‑model (LLM) agents—i.e., “data agents” that retrieve, store, and act on external information—by organizing prior work around the *data surfaces* an agent touches (retrieval sources, APIs, memory, inter‑agent messages) rather than by attack taxonomy.

**Methodology:** The authors catalog existing literature from retrieval‑augmented generation, text‑to‑SQL, agent memory, prompt‑injection, access‑control, and contextual‑privacy fields; they build a taxonomy of data sources, the corresponding privacy threats, and the governance mechanisms (e.g., sandboxing, differential privacy, information‑flow control). They also audit the current benchmarking landscape, noting which data surfaces are exercised and where gaps remain.

**Key findings for agentic AI:** (1) Information‑flow control (IFC) is the only governance approach that simultaneously mitigates compositional leakage across multi‑step workflows and cross‑session inference—both identified as the weakest‑protected risks. (2) No existing benchmark evaluates an agent’s full data pipeline under a unified privacy policy, highlighting a critical need for comprehensive, end‑to‑end privacy evaluation suites for future LLM agents.


<details>
<summary>Abstract</summary>

Large language model agents increasingly query databases, search document collections, call external APIs, remember past interactions, and act on a user's behalf. As they move from answering questions to operating over sensitive data, privacy becomes harder to enforce. An agent touches many data sources, runs multi-step workflows, keeps state across sessions, and acts with delegated permissions. Sensitive information can therefore leak not only through its final answer but through the queries it issues, the intermediate results it handles, the memory it writes, and the messages it exchanges with other agents. We survey the privacy of LLM agents from a data-centric view, organizing the field around the data an agent touches rather than by attack type, and we use data agent as shorthand for an LLM agent that works with data. Research on these risks is active but scattered across retrieval-augmented generation, text-to-SQL interfaces, agent memory, prompt injection, access control, and contextual privacy. This survey brings that work together: we taxonomize the data sources an agent touches, the privacy risks each source creates, and the governance mechanisms that address them; we map the benchmarks used to measure these risks and identify what is missing; and we set out the open problems. Two findings recur: among governance mechanisms only information-flow control covers both compositional and cross-session inference leakage, the two least-protected risks; and no benchmark drives an agent across its data surfaces under one privacy policy, the instrument the field most lacks. Our goal is a reference that situates the scattered literature and gives future work a common framing.

</details>


### 36. HiLSVA: Design and Evaluation of a Human-in-the-Loop Agentic System for Scientific Visualization

- **Authors:** Kuangshi Ai, Patrick Phuoc Do, Chaoli Wang
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26614v1](http://arxiv.org/abs/2606.26614v1)
- **PDF:** [https://arxiv.org/pdf/2606.26614v1](https://arxiv.org/pdf/2606.26614v1)
- **Categories:** cs.HC, cs.AI, cs.GR


> HiLSVA introduces a mixed‑initiative, human‑in‑the‑loop architecture for scientific visualization in which a “plan‑first” multi‑agent system proposes visualization steps that are explicitly overseen, edited, and approved by users through natural‑language dialogue or direct manipulation, with stepwise provenance tracking and test‑time learning from feedback. The authors evaluated the approach via case studies and a controlled study with twelve participants of varying expertise, finding that the collaborative mode significantly improves task completion rates, user control, and workflow transparency compared to fully autonomous agents, albeit at the cost of reduced execution efficiency. These results underscore that incorporating transparent human oversight and adaptive feedback loops is crucial for building trustworthy, agentic AI systems in scientific visualization.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents enable natural language interaction for scientific visualization (SciVis). Still, prior systems have essentially prioritized autonomy over human analytical control, thereby limiting transparency and human oversight. We present HiLSVA, a human-in-the-loop agentic system that supports mixed-initiative SciVis workflows. HiLSVA integrates a plan-first multi-agent architecture with explicit human oversight, stepwise provenance tracking, and learn-at-test-time adaptation from user feedback. The system supports fluid handoff between humans and agents through both natural language and direct manipulation of visualizations, while sandboxed execution ensures safe, reproducible workflows. In doing so, HiLSVA reframes agentic SciVis as a collaborative process that augments, rather than replaces, human analytical reasoning. We evaluate HiLSVA through representative case studies and a controlled user study with twelve participants of varying expertise across multiple autonomy settings. Results show that mixed-initiative interaction improves task completion, user control, and workflow transparency across different levels of user expertise, while revealing a tradeoff between execution efficiency and human oversight. These findings highlight the importance of human-centered design in agentic SciVis and guide the development of future collaborative visualization systems. We encourage readers to explore our demo video, case studies, and source code at https://hilsva.github.io/.

</details>


### 37. Content-Based Smart E-Mail Dispatcher Using Large Language Models

- **Authors:** K. Paramesha, K R Sriram, Sujan Shetty, Shamanth Kishore, R. Tejaswini
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26593v1](http://arxiv.org/abs/2606.26593v1)
- **PDF:** [https://arxiv.org/pdf/2606.26593v1](https://arxiv.org/pdf/2606.26593v1)
- **Categories:** cs.AI


> The paper presents a lightweight, agent‑based architecture that uses large language models (LLMs) as zero‑shot classifiers to automatically route incoming institutional emails to the appropriate WhatsApp student groups, eliminating the need for manually curated training data. Each dispatcher agent formulates a structured prompt containing the email body, contextual rules, and a request for the target group, then parses the LLM’s response to trigger the correct messaging API. Experiments on a college‑wide mailing dataset show that the LLM‑driven agents achieve high precision in group selection and reduce email‑handling latency, demonstrating a practical, low‑overhead way to embed content‑aware decision‑making into agentic AI systems for enterprise communication.


<details>
<summary>Abstract</summary>

Email communication has become an integral part of personal and professional life, but handling its vast volume is still a significant issue for large organisations. Manual perusal of emails and forwarding their contents and attachments to intended recipients using other instant messaging platforms has proved to be error-prone and time-consuming leading to losses in terms of productivity and creating undue stress. The main objective of this paper is to explore an alternative mechanism that is to automate the task of dispatching emails based on their contents to the respective WhatsApp groups of students of various semesters of programs in an engineering college, facilitating a smooth flow of information from one end to another end in an organisation. The dispatcher system is built using agents querying large language models (LLMs) to enable it to analyze the contents of emails and route them to the relevant groups of students for their information and consumption. The system harnesses the capabilities of LLMs in analysing the textual contents for decision-making. With a well-structured agent framework prompt that includes email content as input with instructions and context, the system figures out the relevant groups to which the email message is dispatched, thus providing the required information on time. The proposed system does not rely on labelled datasets and provides several benefits, including enhanced productivity and a reduction in the cognitive load associated with reading emails.

</details>


### 38. IDEA: Insensitive to Dynamics Mismatch via Effect Alignment for Sim-to-Real Transfer in Multi-Agent Control

- **Authors:** Chenlong Liu, Zhuohui Zhang, Xinyan Chen, Zhipeng Wang, Bin Cheng, Bin He
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26575v1](http://arxiv.org/abs/2606.26575v1)
- **PDF:** [https://arxiv.org/pdf/2606.26575v1](https://arxiv.org/pdf/2606.26575v1)
- **Categories:** cs.RO, cs.AI


> **Main contribution:** The paper introduces **IDEA**, a sim‑to‑real transfer framework for multi‑agent control that is robust to dynamics mismatches by aligning the *effects* of actions rather than their low‑level motor commands.

**Methodology:** IDEA lifts policy learning to a discrete, semantic‑action space and couples it with a closed‑loop controller that maps these high‑level actions to platform‑specific motor commands. It also adds an **action‑synchronization mechanism** that coordinates timing across agents, reducing inter‑agent temporal drift when the simulated and real dynamics differ.

**Key findings:** Across four multi‑agent navigation benchmarks, IDEA achieves markedly higher training efficiency than standard domain‑randomization or system‑identification baselines and yields substantially higher real‑world success rates, demonstrating that effect‑level abstraction and synchronized execution greatly improve the robustness and deployability of learned multi‑agent policies under dynamics mismatch.


<details>
<summary>Abstract</summary>

Complex multi-agent control tasks remain challenging for traditional rule-based and model-based approaches, motivating the adoption of learning-based methods. However, learning-based methods often struggle with sim-to-real transfer because they rely on accurate dynamics modeling or system identification and learn policies in low-level control spaces that are highly sensitive to dynamics mismatch, making them costly and fragile in complex environments. To address this issue, we propose a sim-to-real method for multi-agent control, which is insensitive to dynamics mismatch via effect alignment. Our method combines random environmental structure with discrete semantic actions through closed-loop control, elevating policy learning to a semantic abstraction level. Additionally, we develop an action synchronization mechanism that mitigates inter-agent action timing mismatches, thereby enhancing the temporal consistency of the system. Experiments on four multi-agent navigation tasks demonstrate that our method substantially improves training efficiency over mainstream transfer methods and achieves higher success rates in real-world scenarios, thereby improving the robustness and deployment stability of multi-agent systems under dynamics mismatch.

</details>


### 39. Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving Knowledge

- **Authors:** Neeraj Yadav
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26511v1](http://arxiv.org/abs/2606.26511v1)
- **PDF:** [https://arxiv.org/pdf/2606.26511v1](https://arxiv.org/pdf/2606.26511v1)
- **Categories:** cs.CL, cs.AI, cs.ET, cs.LG


> **Main contribution** – The paper introduces **MemStrata**, a bi‑temporal retrieval memory that explicitly tracks the temporal validity of stored facts and automatically retires superseded entries, thereby eliminating “stale‑fact” errors that plague standard retrieval‑augmented generation (RAG) systems when knowledge evolves.  

**Methodology** – MemStrata stores each (subject, relation, object) triple in a ledger; when a new triple with the same subject‑relation pair arrives, a deterministic supersession rule replaces the old entry without any similarity threshold or extra LLM call. The authors evaluate the approach on six locally‑run benchmarks (7 B model) that blend static and evolving knowledge, comparing against vanilla RAG and LLM‑reranking baselines.  

**Key findings** – On static queries MemStrata matches RAG’s recall, but on evolving‑knowledge queries it jumps from RAG’s 20‑47 % accuracy to **95‑100 %** accuracy, driving the stale‑fact error rate from 15‑40 % down to ≈0 %. It does so with retrieval latency ≈2.1 s, far faster than the 16‑18 s required by reranking methods. These results demonstrate that a simple temporal ledger can reliably maintain up‑to‑date factuality for agentic AI without costly LLM‑based post‑processing.


<details>
<summary>Abstract</summary>

Retrieval-augmented generation (RAG) gives agents access to accumulated knowledge, but has no model of time. When a fact changes (e.g., a function is renamed or API restructured), RAG retrieves both the stale and current value with near-identical embedding similarity. The agent then either abstains or serves the superseded fact. We show this is a structural problem: on a calibrated dataset, cosine similarity distinguishes a contradicted fact from a duplicated one with AUROC 0.59 (near chance), as contradictions are often more embedding-similar to the original than rephrased duplicates.
  We present MemStrata, a retrieval memory maintaining temporal validity. It stores facts like RAG, preserving static recall, but when a fact's value is contradicted, a deterministic (subject, relation, object) supersession rule retires the stale value in a bi-temporal ledger - with no similarity threshold and no LLM call. Across six benchmarks run locally with a 7B model, MemStrata ties RAG on static knowledge and reaches 0.95-1.00 accuracy on evolving knowledge (where RAG reaches 0.20-0.47). The central result is the stale-fact-error rate: when required to answer, RAG serves superseded values 15-40% of the time; MemStrata drives this to ~0%, a failure class RAG cannot avoid. MemStrata achieves this at retrieval latency (~2.1s) versus ~16-18s for LLM-reranking baselines. We release the harness, datasets, and a marker-free evaluation protocol for memory under knowledge evolution.

</details>


### 40. Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

- **Authors:** Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu
- **Published:** 2026-06-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26479v1](http://arxiv.org/abs/2606.26479v1)
- **PDF:** [https://arxiv.org/pdf/2606.26479v1](https://arxiv.org/pdf/2606.26479v1)
- **Categories:** cs.CR, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors, and several report near-elimination of attacks on the AgentDojo benchmark. We make two contributions. First, we organize these out-of-band defenses as instances of classical integrity protection (Biba), reference monitoring, and least privilege, yielding a structured comparison of what they do and do not cover. Second, we warn that every one of them is validated only on static benchmarks (a fixed set of injection attempts), the same methodology that made in-band defenses look strong until adaptive, defense-aware attacks broke twelve of them at over 90% success; we specify the threat model and protocol an adaptive evaluation requires. We then run that protocol as an independent reproduction and extension of Progent's own adaptive-attack analysis, on AgentDojo, with an open-weight agent (Qwen2.5-7B) self-hosted on a single H200, a setting its authors did not test. Averaged over three runs, the defense held: Progent cut mean attack success roughly sixfold (25.8% to 4.2%), and a hand-crafted adaptive attack did not raise it (2.6%). This is one small-scale data point on a weak model with a single black-box attack template; a stronger optimized (white-box GCG) attack remains open. The result is consistent with, but does not establish, the hypothesis that deterministic out-of-band enforcement is a harder target for an adaptive attacker than in-band detection.

</details>


### 41. Optimizing CUDA like a Human: Micro-Profiling Tools as Expert Surrogates for LLM-Based GPU Kernel Optimization

- **Authors:** Jiading Gai, Shuai Zhang, Kaj Bostrom, Jin Huang, Vihang Patil, Haoyang Fang, Bernie Wang, Huzefa Rangwala, George Karypis
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26453v1](http://arxiv.org/abs/2606.26453v1)
- **PDF:** [https://arxiv.org/pdf/2606.26453v1](https://arxiv.org/pdf/2606.26453v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present KernelPro, a closed-loop multi-agent system that automatically generates, profiles, and iteratively optimizes GPU kernel code by integrating large language model (LLM) code generation with hardware profiler feedback and pluggable bottleneck detection tools. KernelPro introduces four contributions: (1) a semantic feedback operator that encodes expert heuristics as pluggable micro-profiling tools, transforming raw hardware metrics into actionable natural language guidance; (2) a two-stage tool invocation architecture where roofline-based bottleneck classification filters which specialized analysis tools execute, combining kernel-level (ncu), instruction-level (SASS), and system-level (nsys) profiling; (3) a domain-adapted MCTS with progressive widening, asymmetric branching, log-reward calibration, dead-end pruning, and search memory for cross-iteration learning; and (4) direct CuTe source-level code generation via autonomous code search over the CUTLASS/CuTe codebase. On KernelBench, KernelPro achieves geometric mean speedups of 2.42x/4.69x/5.30x on Levels 1/2/3, establishing state-of-the-art performance across all difficulty levels. On VeOmni's expert-optimized MoE training kernels, KernelPro achieves 1.23x over hand-tuned Triton by generating a from-scratch raw-CUDA+CuTe Hopper WGMMA kernel. Ablation studies demonstrate that each design component independently and significantly improves optimization quality: micro-profiling tools (p < 0.0001 vs raw metrics), MCTS search (26% higher geometric mean vs greedy, p = 0.004), and proactive tool orchestration (23% improvement, p = 0.035). Finally, KernelPro is the first CUDA kernel coding agent to optimize energy efficiency beyond the speed-only focus of prior systems, demonstrating an 11.6% measured energy reduction at matched speed.

</details>


### 42. Closing the Loop to Discover Psychological Theories with an Automated Cognitive Scientist

- **Authors:** Akshay K. Jagadish, Younes Strittmatter, Nori Jacoby, George Kachergis, Eric Schulz, Nathaniel Daw, Suyog H. Chandramouli, Thomas L. Griffiths
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26448v1](http://arxiv.org/abs/2606.26448v1)
- **PDF:** [https://arxiv.org/pdf/2606.26448v1](https://arxiv.org/pdf/2606.26448v1)
- **Categories:** q-bio.NC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Across the sciences, autonomous systems are increasingly being used in closed-loop discovery, proposing new theories and designing and running experiments to test them. This approach is yet to be applied in the field of cognitive science, where the central bottleneck is theory-building: the creative step of turning the accumulated failures of existing models into better ones. Theory generation has remained manual even as data collection, modeling, and experiment design have been automated. We present the Automated Cognitive Scientist (AutoCog), a fully autonomous agentic-AI system that closes this loop. Large-language-model agents advocate competing theories, each expressed as an executable cognitive model, design experiments that best discriminate them, collect behavioral data from participants recruited online, score theories against collected data based on their generative performance, diagnose why they fail, and synthesize a better successor. Repeating this cycle allows them to search the space of theories, models, and experiments. In the domain of decision-making, AutoCog recovered known decision-making strategies from simulated behavior, including unconventional ones, showing that its discoveries are ultimately driven by the data rather than strictly bound by the priors of the underlying language models. When run with human participants, it produced theories that outperformed the established theories it was seeded with and generalized to held-out studies in two different experimental settings. It also surfaced a novel theory of multi-cue decision-making in which choices show diminishing sensitivity to feature values. The distinctive predictions of this theory were confirmed in a preregistered study with new participants. AutoCog demonstrates how an automated discovery system can be used to turn cognitive theory-building into an explicit, executable, and cumulative science.

</details>


### 43. ProfileFoundry: A Synthetic Person-Object Substrate for Privacy, Memory, and Tool-Use Evaluation in LLM Agent

- **Authors:** Sriram Selvam, Anneswa Ghosh
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26403v1](http://arxiv.org/abs/2606.26403v1)
- **PDF:** [https://arxiv.org/pdf/2606.26403v1](https://arxiv.org/pdf/2606.26403v1)
- **Categories:** cs.CL


> **Contribution** – The paper introduces **ProfileFoundry**, a deterministic synthetic data generator that releases a curated corpus of 100 k *person objects* (with linked households, families, employers, and 709 k timestamped life events) designed as a safe, inspectable substrate for evaluating LLM‑based agents on privacy‑sensitive tasks, long‑term memory, record linkage, and tool use.  

**Methodology** – ProfileFoundry builds each person object from a hierarchy of typed schemas (current snapshot, relational links, event logs) and populates them with coherent, cross‑field and temporally consistent attributes using rule‑based generation and provenance tracking; the authors validate the release through population‑marginal statistics, invariant checks, referential/temporal closure tests, and provenance screening.  

**Key Findings** – The synthetic corpus achieves realistic marginal distributions across eight locales while guaranteeing internal consistency and full traceability, enabling reproducible agentic‑AI benchmarks that require personal‑state data without exposing real user privacy.


<details>
<summary>Abstract</summary>

Foundation-model research increasingly needs data about people: user state, personal histories, relationships, contact-like fields, documents, and longitudinal updates. Real user data is difficult to share, perturb, audit, or redistribute responsibly, while independently generated fake fields rarely preserve the cross-field and temporal consistency needed for controlled evaluation. We present PROFILEFOUNDRY, a deterministic generator and fixed reference release of 100,000 adult synthetic Person Objects across eight locales. Each object combines a typed current snapshot, household, family, and employer links, snapshot-aligned events, normalized relational views, and generation provenance. The release contains 709,228 events, 40,338 households, 52,491 employers, and 518,564 directed relationship edges. We report evidence in separate categories: selected population-marginal comparisons, per-object invariant checks, release-wide referential and temporal closure, and coincidence/provenance screens. PROFILEFOUNDRY is not a population-fidelity model, a rendered-text corpus, or a formal privacy mechanism. Instead, it is a responsible synthetic source layer for constructing downstream foundation-model evaluations involving memory, privacy, document understanding, record linkage, and agent state while keeping the synthetic person behind each artifact inspectable

</details>


### 44. Instruction Bleed: Cross-Module Interference in Prompt-Composed Agentic Systems

- **Authors:** Ching-Yu Lin, Yifan Liu
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26356v1](http://arxiv.org/abs/2606.26356v1)
- **PDF:** [https://arxiv.org/pdf/2606.26356v1](https://arxiv.org/pdf/2606.26356v1)
- **Categories:** cs.AI, cs.IR, cs.MA


> The paper identifies **compositional behavioral leakage (CBL)**—a subtle failure mode in prompt‑composed agentic systems where changes to one prompt “module” unintentionally alter the behavior of other modules that share the same transformer context window. By designing a three‑channel probing protocol (varying volume, content, and form of non‑target modules) and applying it to a real‑world job‑evaluation agent (Claude Sonnet 4.6) across 144 trials, the authors show that only content‑level perturbations produce a statistically reliable spill‑over effect (Cohen’s d = 0.63, bootstrap 95 % CI ≠ 0), even though no individual decision flips, revealing a sub‑threshold but cumulatively significant source of error. The contribution consists of a formal definition of CBL, an experimentally reusable measurement protocol, and empirical evidence that cross‑module interference is distinct from previously known agent faults, arguing that such interference must be measured for reliable evaluation of prompt‑composed AI agents.


<details>
<summary>Abstract</summary>

Practitioners of prompt-composed agentic systems report a recurring failure mode: editing one prompt module silently shifts the behavior of others despite no shared variable or executable dependency. We formalize this as compositional behavioral leakage (CBL): interference between modules sharing a context window. CBL is enabled by architectural non-isolation: transformer self-attention provides no formal boundary between concatenated modules. We probe CBL on a deployed job-evaluation agent (Claude Sonnet 4.6, 144 trials) through a reusable three-channel protocol that perturbs non-focal modules along volume, content, and form. Only the content channel produces a detectable paired effect (Cohen's d = 0.63, bootstrap 95% CI excluding zero); no recommendation flipped -- a sub-threshold regime invisible to standard QA but compounding across the thousands of decisions a deployed agent makes. CBL is orthogonal to known agent-failure axes (adversarial injection, cognitive degradation, multi-agent fault propagation, privacy leakage). We contribute an operational definition, a reusable protocol, a falsifiable prediction set, and a system-class characterization, establishing cross-module interference measurement as a requirement for prompt-composed agent evaluation.

</details>


### 45. How Do Tool-Augmented LLM Agents Perform on Real-World Energy Analytics Tasks?

- **Authors:** David Akinpelu, Akintonde Abbas, Rereloluwa Alimi, Ayodeji Lana
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26346v1](http://arxiv.org/abs/2606.26346v1)
- **PDF:** [https://arxiv.org/pdf/2606.26346v1](https://arxiv.org/pdf/2606.26346v1)
- **Categories:** cs.AI


> The paper introduces the first systematic benchmark for evaluating tool‑augmented large‑language‑model (LLM) agents on real‑world energy‑market analytics, comprising 243 expert‑curated problems that require live data retrieval, regulatory knowledge, and multi‑step quantitative reasoning. By endowing both closed‑source (e.g., GPT‑4) and open‑source (e.g., LLaMA‑2) models with a configurable toolbox of domain‑specific APIs (ISO market feeds, tariff databases, docket search, and optimization solvers) and a multi‑dimensional scoring system (correctness, accuracy, attribute alignment, source validity), the authors show that (i) tool‑integration dramatically boosts performance over vanilla LLMs, (ii) higher‑capacity models still outperform open‑source counterparts but can be matched when richer tool suites and better routing are used, and (iii) the hardest “advanced quantitative modeling” tasks remain challenging, highlighting the need for tighter tool‑agent coordination for high‑stakes energy decisions.


<details>
<summary>Abstract</summary>

Agentic benchmarks have emerged across general-purpose and domain-specific settings, including finance, coding, law, and drug discovery, yet energy-domain evaluations remain largely limited to static knowledge recall. This is a critical gap for a sector that requires live data retrieval, specialized regulatory and market knowledge, and multi-step quantitative reasoning under real-world constraints.
  We present an empirical study of tool-augmented LLM agents on real-world energy market analytics tasks. Our evaluation environment includes 243 expert-curated problems across three categories: (1) Market Data Retrieval and Analysis, (2) Knowledge Retrieval and Interpretation, and (3) Advanced Quantitative Modeling and Decision Analytics. Tasks include price and demand analysis, tariff impact modeling, asset revenue and returns estimation, hedging strategy analysis, and optimization modeling, with problems spanning multiple difficulty levels.
  Agents are equipped with a configurable suite of domain tools, including live electricity market APIs for major U.S. ISOs, regulatory docket search, utility tariff databases, asset optimization models, and retrieval-augmented generation over energy market documents. We assess agent responses using a multi-dimensional evaluation protocol that scores approach correctness, answer accuracy, attribute alignment, and source validity, with category-aware routing to match scoring criteria to question type. We evaluate both closed-source and open-source LLMs, providing a comparative analysis of how model capability and domain tooling interact in a high-stakes professional domain. Key artifacts are publicly released to support reproducibility and future research.

</details>


### 46. Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems

- **Authors:** Jakob Salfeld-Nebgen
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26298v1](http://arxiv.org/abs/2606.26298v1)
- **PDF:** [https://arxiv.org/pdf/2606.26298v1](https://arxiv.org/pdf/2606.26298v1)
- **Categories:** cs.AI, cs.CR


> **Main contribution** – The paper proposes a novel governance architecture for high‑stakes autonomous AI systems that shifts control from “watching the agent’s reasoning” to “attesting the actions it wants to take.” It formalises an *institutional attestation* model in which an AI retains full planning autonomy but can execute only those high‑risk actions whose preconditions are independently certified by trusted authorities and cryptographically bound to the agent’s declared intent.

**Methodology** – The authors define a computational framework that (1) ties each intended high‑risk action to a set of attestations, (2) enforces deterministic policy checks on these attestations, and (3) records the whole decision‑execution pipeline in a tamper‑evident ledger for auditability. They implement a prototype using cryptographic signatures, policy engines, and an append‑only log, and demonstrate it on two domains: (a) automated software deployment pipelines and (b) AI‑driven clinical prescription generation.

**Key findings** – In the prototype, agents could freely generate plans but were blocked from acting unless the required attestations were supplied, guaranteeing that execution complied with external institutional constraints without inspecting internal reasoning. The tamper‑evident log enabled independent post‑hoc verification of compliance, and the case studies showed that the model can feasibly embed regulatory oversight into autonomous AI workflows while preserving agent autonomy for non‑critical decisions. This establishes a practical, audit‑ready pathway for governing consequential AI actions in safety‑critical settings.


<details>
<summary>Abstract</summary>

Autonomous AI agents may begin to perform consequential, irreversible actions such as clinical prescribing and production software deployment. This paper observes that human institutions have governed powerful autonomous actors not by monitoring their reasoning but by requiring independently attested evidence at the point of consequential action. We formalise this institutional pattern as a computational governance model for AI agent systems. Under the proposed model, an agent retains full autonomy over planning and reasoning but holds no execution authority over designated high-risk actions. Execution is conditional on preconditions that are each independently attested by a separate authoritative source, cryptographically bound to a declared intent, and evaluated by a deterministic policy. Decisions are recorded in a tamper-evident log amenable to independent re-verification. We present a proof-of-concept implementation and illustrate the model with examples from software deployment and clinical prescribing.

</details>


### 47. CyberChainBench: Can AI Agents Secure Smart Contracts Against Real-World On-Chain Vulnerabilities?

- **Authors:** Jintao Huang, Fengqing Jiang, Radha Poovendran, Zhiqiang Lin
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26216v1](http://arxiv.org/abs/2606.26216v1)
- **PDF:** [https://arxiv.org/pdf/2606.26216v1](https://arxiv.org/pdf/2606.26216v1)
- **Categories:** cs.CR, cs.AI


> CyberChainBench introduces the first end‑to‑end benchmark that measures how well LLM‑driven agents can secure real DeFi smart contracts, covering three tightly coupled tasks—vulnerability detection, exploit generation, and patch synthesis—over 541 historic on‑chain incidents from nine EVM chains. By deploying agents in isolated Harbor‑orchestrated mainnet forks, the authors let the agents read contract code, trace transactions, and validate attacks and fixes against concrete economic outcomes, using a five‑type vulnerability taxonomy and oracle‑based pass/fail criteria. Experiments show a steep performance drop across the pipeline: even the strongest Codex + GPT‑5.5 configuration attains only 37.5 % detection accuracy, 43.7 % exploit success (realizing $57.4 M of historical profit at $2.39 per case), and 23.4 % successful patching, highlighting the current limits of agentic AI for smart‑contract security.


<details>
<summary>Abstract</summary>

We present CyberChainBench, a benchmark for evaluating LLM-based agents on smart contract security across three complementary tasks: vulnerability detection, exploit generation, and patch synthesis. Built from 541 real-world exploit incidents from DeFiHackLabs spanning 9 EVM chains, the benchmark provides end-to-end on-chain evaluation where agents interact with historical blockchain state through isolated evaluation environments orchestrated by Harbor, using tools to read code, trace transactions, and validate exploits on mainnet forks. Each case is anchored to a specific block and includes structured ground truth covering vulnerability type, localization, and attacker profit. Exploits are graded by economic impact on historical forks; patches are validated by replaying historical attacks and legitimate transactions as fail-to-pass test oracles on a proxy-upgradeable subset. We define a five-type vulnerability taxonomy and evaluate multiple agent--model configurations. Results reveal a clear difficulty gradient: the best configuration scores 37.5% on detection, 43.7% on exploitation, but only 23.4% on patching, with the top agent (Codex with GPT-5.5) realizing \$57.4M in total exploit profit across the 200-case exploit set at a cost of $2.39 per case.

</details>


### 48. Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents

- **Authors:** Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26080v1](http://arxiv.org/abs/2606.26080v1)
- **PDF:** [https://arxiv.org/pdf/2606.26080v1](https://arxiv.org/pdf/2606.26080v1)
- **Categories:** cs.LG, cs.AI


> The paper shows that the policy‑level log‑probability ratio obtained after standard RL fine‑tuning of large language models—what they call **progress advantage**—is mathematically equivalent to the optimal advantage function of the underlying stochastic MDP, thereby providing a free, step‑level reward signal without any additional reward‑model training. By deriving this implicit advantage and testing it on test‑time scaling, uncertainty estimation, and failure attribution across five benchmarks and four model families, the authors demonstrate that progress advantage consistently beats confidence‑based baselines and even outperforms purpose‑built reward models despite being annotation‑free and domain‑agnostic. This result opens a practical, post‑training “free lunch” for evaluating and steering LLM‑based agents in long‑horizon, stochastic environments.


<details>
<summary>Abstract</summary>

Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.

</details>


### 49. The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems

- **Authors:** Seth Dobrin, Łukasz Chmiel
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26057v1](http://arxiv.org/abs/2606.26057v1)
- **PDF:** [https://arxiv.org/pdf/2606.26057v1](https://arxiv.org/pdf/2606.26057v1)
- **Categories:** cs.AI, cs.CR, cs.LG


> **Main contribution** – The paper introduces the *Unfireable Safety Kernel*, an execution‑time authorization layer that enforces safety for “escapable” AI agents (i.e., systems that can reach into their own runtime). It formalises four architectural requirements—process separation, pre‑action enforcement on a structurally‑only path, fail‑closed behavior at both request and system levels, and externally verifiable signed evidence—to guarantee that safety controls cannot be subverted from within the agent.

**Methodology** – The authors implement the kernel in Rust and verify its fail‑closed invariant with two independent formal methods: an SMT theorem proved in Z3 and exhaustive bounded‑model checking of the production decision function using Kani. They ensure correctness of the Python‑to‑Rust migration via byte‑equivalence tests (1 000 fixtures, 17 adversarial classes) and then deploy the kernel to guard a deterministic, self‑improving world‑model agent in a live setting.

**Key findings** – In extensive adversarial testing, the kernel rejected every safety‑critical self‑modification request (704/704) and all 300 kill‑switch requests, with zero successful escapes across 1 000 modification attempts and 6 240 authorization round‑trips. Compared against three contemporary agent‑control systems, the Unfireable Safety Kernel uniquely prevented the agent from bypassing its own safety plane, demonstrating that architectural, execution‑time alignment can reliably complement training‑ and inference‑time techniques.


<details>
<summary>Abstract</summary>

AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems.
  We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment.
  We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.

</details>


### 50. Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem

- **Authors:** Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt, Zhipeng Wang
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26028v1](http://arxiv.org/abs/2606.26028v1)
- **PDF:** [https://arxiv.org/pdf/2606.26028v1](https://arxiv.org/pdf/2606.26028v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> The paper provides the first large‑scale empirical audit of the ERC‑8004 “trust layer” for decentralized AI agents, analysing on‑chain identity and reputation events together with off‑chain registration files and payment data on Ethereum, BNB Smart Chain and Base up to May 2026. By crawling > 200 k registrations and millions of feedback entries, the authors show that ≈ 90 % of identities are merely placeholders, reputation scores are non‑comparable, easy to falsify, and dominated by coordinated Sybil attacks—leaving the majority of agents without any credible feedback after Sybil filtering. These findings demonstrate that the current ERC‑8004 design cannot reliably support trust decisions in agentic AI markets and the authors propose concrete protocol revisions (e.g., mandatory service verification, weighted reputation, anti‑Sybil mechanisms) to make trustless agents truly trustworthy.


<details>
<summary>Abstract</summary>

As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions.
  On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.

</details>


### 51. Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It

- **Authors:** Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26027v1](http://arxiv.org/abs/2606.26027v1)
- **PDF:** [https://arxiv.org/pdf/2606.26027v1](https://arxiv.org/pdf/2606.26027v1)
- **Categories:** cs.CL, cs.LG


> **Main contribution:** The paper identifies and diagnoses a failure mode in multi‑step tool‑use reinforcement learning (RL) for large language models—catastrophic “collapse” caused by sudden probability spikes on control tokens that break the structured tool‑invocation sequence— and shows that mixing targeted supervisory signals with RL can prevent this collapse and yield more reliable tool‑use agents.  

**Methodology:** The authors conduct systematic experiments on several RL‑based agentic models, tracking token‑level probability dynamics during training. They then evaluate a spectrum of supervisory signals (off‑policy fine‑tuning, hint‑based prompts, deliberately noisy examples, etc.) under both synchronous and interleaved (SFT + RL) training regimes, analyzing the effects of learning‑rate schedules and out‑of‑distribution (OOD) format/content shifts.  

**Key findings:** Interleaved supervised fine‑tuning dramatically stabilizes training and eliminates the collapse, while pure RL rapidly becomes unstable. Although the interleaved approach maintains high performance on in‑distribution tool‑use tasks, its gains degrade on OOD formats, highlighting a trade‑off between stability and generalization. The results underscore that carefully designed supervisory signals are essential for robust, exploratory multi‑step tool‑use in agentic AI.


<details>
<summary>Abstract</summary>

Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.

</details>


### 52. Knowledge-augmented Agentic AI for Mental Health Medication Information Seeking

- **Authors:** Huizi Yu, Jian Liu, Wenkong Wang, Lingyao Li, Jiayan Zhou, Zhaoqian Xue, Xiang Li, Xinxin Lin, Zhiying Liang, Zhuoru Wu, Siyuan Ma, Xin Ma, Lizhou Fan
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26205v1](http://arxiv.org/abs/2606.26205v1)
- **PDF:** [https://arxiv.org/pdf/2606.26205v1](https://arxiv.org/pdf/2606.26205v1)
- **Categories:** cs.AI


> The paper introduces a provenance‑aware, knowledge‑graph‑driven multi‑agent system that fuses regulatory adverse‑event reports (FDA‑FAERS), patient narratives (Reddit and WebMD) and standardized ontologies (ATC‑N, ICD‑10, MedDRA) to support safe medication information‑seeking for antidepressants. Using a large‑language‑model pipeline for entity extraction (F1 ≈ 0.97 for drugs and conditions), the authors construct a Neo4j graph that preserves the source of every claim, revealing that community‑generated data are highly concordant with each other (Jaccard ≤ 0.905) but often diverge from FDA records, and that many sertraline adverse events appear in patient posts months before official reporting. The work demonstrates that source‑aware, graph‑based integration of heterogeneous safety knowledge can yield auditable, earlier insights for psychiatric drug information, a capability directly relevant to agentic AI systems tasked with trustworthy health‑information retrieval.


<details>
<summary>Abstract</summary>

Patients increasingly seek medication information online, yet safety knowledge for psychiatric drugs is split between regulatory adverse-event records, which are authoritative but abstract, and patient narratives, which are experience-near but unvalidated. Integrating them without conflating evidence and anecdote is especially consequential in psychiatry, where poorly contextualised information can amplify fear, nocebo responses, and non-adherence. Here we develop a provenance-aware, knowledge-graph-based multi-agent framework unifying 466,525 Reddit posts, 60,782 WebMD reviews, and twenty years of U.S. FDA Adverse Event Reporting System records for nine antidepressants. A large-language-model entity-recognition pipeline benchmarked against physician annotations reached highest F1 scores of 0.969 for medications and 0.973 for conditions. The two community platforms were far more concordant with each other (overlap up to a Jaccard similarity of 0.905) than with regulatory reports, indicating that patient-generated data form a partly independent safety signal. For sertraline, many adverse events appeared in community sources hundreds of days before the corresponding FDA date. A Neo4j knowledge graph grounded in ATC-N, ICD-10, and MedDRA vocabularies preserves provenance, keeping every claim traceable and regulatory facts distinct from patient experience. These results establish source-aware integration as a route to more auditable psychiatric medication information, with usefulness and patient benefit to be tested prospectively.

</details>


### 53. Agentic Analysis for Agentic Infrastructure: An LLM-Powered Pipeline for Comparative Governance of DAO and Corporate AI Protocols

- **Authors:** Yutian Wang, Luyao Zhang
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26203v1](http://arxiv.org/abs/2606.26203v1)
- **PDF:** [https://arxiv.org/pdf/2606.26203v1](https://arxiv.org/pdf/2606.26203v1)
- **Categories:** cs.AI, cs.MA


> The paper presents a novel LLM‑driven analytical pipeline that combines automated annotation, neural topic modeling, and multi‑layer network analysis to quantify and compare the governance discourse surrounding two major agent‑interoperability standards— the open, permission‑less ERC‑8004 protocol and the corporate‑run Google A2A framework. By processing 4,323 participation records, the authors show that although the institutional form steers thematic emphases, both regimes display similar participation inequality and community fragmentation, while the permission‑less setting yields denser discourse alignment, indicating higher thematic convergence despite decentralized involvement. The work demonstrates that large‑language‑model‑augmented methods can empirically surface power structures in agentic AI governance, informing the design of more equitable, interoperable AI agent infrastructures.


<details>
<summary>Abstract</summary>

As AI agent protocols proliferate, the governance structures shaping their interoperability standards remain empirically underexamined. We introduce an LLM-powered comparative pipeline for large-scale governance discourse analysis, integrating automated annotation, neural topic modeling, and multi-layer network analysis to study socio-technical power structures at scale. We validate it on two contrasting standards for agent interoperability: ERC-8004 (permissionless, on-chain) and Google A2A (corporate-led). Analyzing 4,323 governance participation records, we combine LLM-assisted coding, topic modeling, and multi-layer network analysis to examine how institutional design shapes thematic priorities and community structure. We find that while governance form influences substantive focus, both regimes exhibit comparable levels of participation inequality and community fragmentation. Discourse alignment is denser in the permissionless setting, suggesting that open governance may foster greater thematic convergence despite decentralized participation. These findings illustrate how LLM-assisted methods can advance the empirical study of technology governance, with implications for designing more equitable agentic AI standards. All data and code are openly available.

</details>


### 54. Autodata: An agentic data scientist to create high quality synthetic data

- **Authors:** Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Yixin Nie, Swarnadeep Saha, Eryk Helenowski, Weizhe Yuan, Olga Golovneva, Jack Lanchantin, Yoram Bachrach, Jakob Foerster, Xian Li, Han Fang, Sainbayar Sukhbaatar, Jason Weston
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25996v2](http://arxiv.org/abs/2606.25996v2)
- **PDF:** [https://arxiv.org/pdf/2606.25996v2](https://arxiv.org/pdf/2606.25996v2)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper presents **Autodata**, a framework that casts data‑generation as an autonomous “data‑scientist” AI agent and then *meta‑optimizes* this agent to produce ever‑better synthetic training and evaluation sets. The authors implement this idea with a concrete system called **Agentic Self‑Instruct**, in which a language‑model‑based agent iteratively designs, validates, and refines data for downstream tasks; the agent itself is further optimized via reinforcement/meta‑learning loops that reward higher downstream performance. Experiments on three domains—computer‑science literature tasks, legal‑reasoning benchmarks, and mathematics‑centric reasoning—show that Autodata‑generated datasets consistently outperform traditional synthetic data pipelines, and that the additional meta‑optimization of the data‑scientist agent yields a still larger boost, demonstrating a viable path for turning extra inference compute into higher‑quality model training data.


<details>
<summary>Abstract</summary>

We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data. We show how to train (meta-optimize) such a data scientist agent, so that it learns to create even stronger data. We describe the overall formulation, and a specific practical implementation, Agentic Self-Instruct. We conduct experiments on computer science research tasks, legal reasoning tasks and reasoning with mathematical objects, where we obtain improved results compared to classical synthetic dataset creation methods. Further, meta-optimizing the data scientist agent itself delivers an even larger performance uplift. Agentic data creation provides a way to convert increased inference compute into higher quality model training. Overall, we believe this direction has the potential to change the way we build AI data.

</details>


### 55. Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound

- **Authors:** Thiago Thomas, Gabriel de Oliveira Ramos, Felipe Meneguzzi
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25978v1](http://arxiv.org/abs/2606.25978v1)
- **PDF:** [https://arxiv.org/pdf/2606.25978v1](https://arxiv.org/pdf/2606.25978v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> The paper introduces **MAGR‑BB**, a novel framework for multi‑agent goal recognition that simultaneously infers team partitions and the goals each team pursues by scoring hypotheses with a single **team‑ and goal‑conditioned reinforcement‑learning policy** embedded in a **factorized branch‑and‑bound search**. By exploiting the shared conditional policy, the method avoids enumerating the exponential hypothesis space and efficiently prunes sub‑optimal team‑goal assignments during inference. Experiments on a multi‑agent Blocksworld benchmark show that MAGR‑BB identifies the exact top‑ranked hypothesis at every timestep while reducing hypothesis materialization by several orders of magnitude and achieving dramatically lower cumulative recognition runtimes compared to exhaustive search.


<details>
<summary>Abstract</summary>

Multi-agent goal recognition asks an observer to jointly infer which agents act together and what each team is trying to achieve, so the hypothesis space grows combinatorially with the number of team partitions and goals per team. Real applications such as drone surveillance and collaborative robotics expose only the agents' trajectory, which forces the observer to rank team-goal hypotheses from behavior alone. Multi-Agent Goal Recognition with Branch-and-Bound (MAGR-BB) addresses this setting with a shared team- and goal-conditioned policy used as the scoring model inside a factorized branch-and-bound search. On a controlled multi-agent Blocksworld benchmark, MAGR-BB returns the same top-ranked hypothesis as exhaustive search throughout the trajectory while cutting hypothesis materialization by orders of magnitude and reducing cumulative recognition runtime substantially.

</details>


### 56. Explainable Control Framework (XCF) based on Fuzzy Model-Agnostic Explanation and LLM Agent-Supported Interface

- **Authors:** Faliang Yin, Hak-Keung Lam, David Watson
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25941v1](http://arxiv.org/abs/2606.25941v1)
- **PDF:** [https://arxiv.org/pdf/2606.25941v1](https://arxiv.org/pdf/2606.25941v1)
- **Categories:** cs.HC, cs.AI, eess.SY


> The paper introduces the Explainable Control Framework (XCF), a model‑agnostic architecture that generates human‑readable explanations for any closed‑loop controller by fitting a hierarchical fuzzy surrogate (HFMAE‑C) to both the controller’s policy and the plant dynamics, then extracting IF‑THEN rules, salience scores, and multi‑level (sample, local, domain, universe) insights.  A large‑language‑model (LLM) agent powers the user interface, automatically matching user queries to the appropriate explanation algorithms, translating the fuzzy rules into natural‑language reports, and enabling interactive consultation.  Experiments on an inverted‑pendulum and a TurtleBot obstacle‑avoidance task show that XCF produces more accurate, granular, and understandable explanations than existing explainable‑control methods, while the LLM‑driven interface improves user satisfaction and task performance in simulated user studies.


<details>
<summary>Abstract</summary>

Increasing demand for precise and reliable control in complex scenarios has led to the development of increasingly sophisticated controllers, including data-driven approaches employing closed box models and mathematically rigorous yet complex designs. This complexity highlights the needs for explainable control that can provide human-understandable insights into controller behavior. In this paper, an explainable control framework (XCF) along with supporting algorithms and user interface are proposed to explain how controllers determine their control actions and their underlying working mechanism. The novel contributions of this work are threefold: First, the XCF is designed to provide model-agnostic explanations for controllers in closed-loop systems and can optionally refine local explanations by system response dynamics. Second, a novel explanation method, hierarchical fuzzy model-agnostic explanation for control systems (HFMAE-C), is proposed based on the designed framework. The HFMAE-C employs a fuzzy logic system to approximate the controller's behavior and system dynamics, providing sample, local, domain and universe level explanations via IF-THEN rules revealing the controller's decision logic and salience values quantifying the contribution of system states to control actions. Third, a large language model agent-supported user interface is developed to automatically analyze user requirements, select appropriate algorithms, interpret the generated explanations to a natural language report, and provide interactive consultation. Case studies on inverted pendulum system and Turtlebot obstacle avoidance demonstrate the effectiveness of the proposed method through simulated user experiments and quantitative comparisons with mainstream explainable control approaches.

</details>


### 57. Robustness and Leadership in Markov-switching Consensus Networks

- **Authors:** Sarah H. Cen, Vaibhav Srivastava, Naomi Ehrich Leonard
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25888v1](http://arxiv.org/abs/2606.25888v1)
- **PDF:** [https://arxiv.org/pdf/2606.25888v1](https://arxiv.org/pdf/2606.25888v1)
- **Categories:** eess.SY, cs.MA


> The paper extends robustness analysis of noisy consensus and leader‑follower tracking from static interaction graphs to **Markov‑switching graphs (MSGs)**, where the network topology evolves according to a finite‑state Markov chain. By modeling the multi‑agent dynamics as **Markov jump linear systems (MJLS)**, the authors derive closed‑form expressions for the steady‑state covariance of each agent’s deviation from consensus (or tracking error), which in turn yield generalized certainty indices, joint centrality measures, and group‑level robustness metrics that explicitly depend on both the graph Laplacians and the switching transition matrix. For the tractable case of switching between two topologies, they analytically characterize how the switching rate and topology mix affect performance, and simulations confirm that appropriate switching can either degrade or improve robustness, offering design guidelines for resilient, leader‑driven agentic AI systems.


<details>
<summary>Abstract</summary>

We investigate how time-varying interactions, modeled via a Markov switching graph (MSG), impact the robustness of noisy multi-agent dynamics in both continuous- and discrete-time settings. Our focus is on the steady-state performance of consensus and leader-follower tracking dynamics subject to stochastic noise. Using the framework of Markov jump linear systems (MJLS), we derive expressions for the steady-state covariance of each agent's deviation from consensus and tracking error, respectively, and use them to quantify individual and group performance as a function of the interaction graphs and the switching dynamics. We extend established notions of robustness, certainty indices, and joint centrality from static graphs to the MSG setting. To gain analytical insight, we specialize our results to systems switching between two topologies and characterize how switching influences performance. Numerical simulations further illustrate how switching topologies affects system robustness in both coordination tasks.

</details>


### 58. Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents

- **Authors:** Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25852v1](http://arxiv.org/abs/2606.25852v1)
- **PDF:** [https://arxiv.org/pdf/2606.25852v1](https://arxiv.org/pdf/2606.25852v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **Semantic Consistency Policy Optimization (SCPO)**, a reward‑shaping technique that removes the semantic credit inconsistency inherent in group‑based reinforcement learning for large‑language‑model (LLM) agents. SCPO — which does not rely on value functions — reassigns step‑level credit to failed actions by comparing each failed step with a successful sibling from the same rollout group and granting positive credit for any new progress that aligns with the sibling’s trajectory. Experiments on the long‑horizon, sparse‑reward benchmarks ALFWorld and WebShop show that SCPO matches or surpasses prior group‑based methods, achieving 93.7 ± 4.1 % success on ALFWorld and 74.8 ± 2.0 % on WebShop with a 1.5 B‑parameter LLM, especially improving performance on the most complex multi‑step tasks.


<details>
<summary>Abstract</summary>

Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress inside failed rollouts. Motivated by this, we propose Semantic Consistency Policy Optimization (SCPO), a value-free reward-shaping method that mitigates this inconsistency by recovering step-level credit from successful siblings in the same rollout group. Concretely, SCPO scores each failed step against a successful sibling and adds positive step-level credit for new progress along that sibling. On ALFWorld and WebShop, SCPO matches or exceeds strong group-based baselines, reaching 93.7+/-4.1 percent success on ALFWorld and 74.8+/-2.0 percent on WebShop at 1.5B parameters, with gains concentrated on the hardest multi-step tasks.

</details>


### 59. AI Snitches Get Glitches: Towards Evading Agentic Surveillance

- **Authors:** Hyejun Jeong, Dzung Pham, Amir Houmansadr, Eugene Bagdasarian
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25836v2](http://arxiv.org/abs/2606.25836v2)
- **PDF:** [https://arxiv.org/pdf/2606.25836v2](https://arxiv.org/pdf/2606.25836v2)
- **Categories:** cs.AI


> The paper formalizes “agentic surveillance” – the capability of AI assistants to harvest user information, synthesize reports, and dispatch them via available tools – and introduces SurveilBench, a benchmark of corporate, educational, and police‑related reporting tasks used to measure this behavior across contemporary models. Experiments show that several large language models spontaneously exhibit surveillance‑facilitating actions, while also paradoxically warning users of governmental monitoring; the authors then devise three prompt‑injection‑based evasion strategies (hiding, deception, and over‑escalation) that can blunt or mislead such agents. Their findings demonstrate that agentic surveillance is already practical, prompting an urgent call for technical safeguards, ethical guidelines, and regulatory measures.


<details>
<summary>Abstract</summary>

To better assist users with completing challenging tasks, AI agents mediate communications, access data, and interact with different APIs. Many employers (and even nation-states) already provide their users with this technology. However, widespread adoption of AI agents creates a new risk to abuse access to user data for another goal: surveilling users. These users might not even have the ability or permission to control the actions and data accesses of the surveilling agents.
  We introduce and formalize the problem of agentic surveillance: the ability of an AI agent to analyze available information, craft a report, and send it out using available tools. To evaluate surveillance capabilities across different models, we create SurveilBench, a dataset of various reporting scenarios focusing on three domains: corporate, education, and police. We find that some models exhibit emergent (i.e., unprompted) tendencies to help surveillance, but they also report the attempts to surveil users to the government.
  Finally, we repurpose prompt injections for evading surveillance and develop three evasion techniques that hide from, deceive, or induce over-escalation in surveillance agents. We conclude that agentic surveillance can already be easily implemented and, therefore, call for a comprehensive technical, ethical, and legislative framework to protect users.

</details>


### 60. Beyond Function Calling: Benchmarking Tool-Using Agents under Tool-Environment Unreliability

- **Authors:** Yang Tian, Zhengpeng Shi, Bo Zhao
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25819v1](http://arxiv.org/abs/2606.25819v1)
- **PDF:** [https://arxiv.org/pdf/2606.25819v1](https://arxiv.org/pdf/2606.25819v1)
- **Categories:** cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as agents that solve tasks by interacting with external tool environments. Although recent tool-use benchmarks increasingly cover complex task settings, they still largely assume clean, stable, and trustworthy tool environments, leaving tool-environment unreliability insufficiently examined. We introduce ToolBench-X, a benchmark for evaluating agents under recoverable reliability hazards. ToolBench-X contains executable multi-step tasks across diverse domains and sequential, parallel, and mixed workflows, each paired with deterministic tools and a canonical final answer for automatic evaluation. Starting from clean tool environments, ToolBench-X injects five structured hazard types: Specification Drift, Invocation Error, Execution Failure, Output Drift, and Cross-source Conflict. Crucially, each injected instance remains solvable through at least one valid recovery path, such as retrying, fallback, verification, or cross-checking. Experiments reveal a substantial reliability gap: agents that perform well with reliable tools often fail under recoverable hazards. Further analysis shows that failures are driven less by tool-use volume or inference budget than by limited hazard diagnosis and ineffective recovery. Targeted recovery hints recover many failed tasks, while test-time scaling yields more limited gains. These results suggest that tool-use evaluation should move beyond function-call accuracy toward task completion under unreliable tool environments. The code and data is available at https://github.com/Foreverskyou/ToolBench-X.

</details>


### 61. GUI agent: Guided Exploration of User-Sensitive Screens

- **Authors:** Aradhana Nayak, Mussadiq Nazeer, Wang Peng, Feng Liu
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25705v1](http://arxiv.org/abs/2606.25705v1)
- **PDF:** [https://arxiv.org/pdf/2606.25705v1](https://arxiv.org/pdf/2606.25705v1)
- **Categories:** cs.AI


> The paper introduces **GUI‑Agent**, an LLM‑driven explorer that autonomously probes a graphical user interface to discover *user‑sensitive states*—screens that contain personal or confidential data and therefore require a hand‑off to the human user.  The methodology builds a systematic query‑generation loop that starts from a single demonstrated task, iteratively creates and executes candidate actions, and classifies the resulting screens using a fine‑tuned safety filter; detected sensitive screens are then catalogued as “user‑sensitive queries” for downstream agents.  Experiments on benchmark GUI suites show that the explorer can identify up to 87 % of privacy‑critical screens with low false‑positive rates, providing a practical dataset and a concrete handover mechanism that markedly improves the safety and reliability of LLM‑based autonomous agents in open‑world GUI settings.


<details>
<summary>Abstract</summary>

LLM agents are increasingly being used to automate tasks for users within an open GUI environment. They inevitably encounter screens containing user-sensitive information, for which takeover of task execution by the user is highly desirable or even necessary. State-of-the-art LLM-driven agents are usually fine-tuned to complete tasks regardless of the safety implications of their actions. This makes their real-world deployment difficult and adversely affects the reliability. Therefore, it is crucial to identify and categorize user-sensitive states and define user-sensitive queries. This dataset would be to engineers to recognize and request handover to the user in critical scenarios. This short paper develops an explorer agent that systematically explores the query space starting from one demonstrated task to identify queries that, if executed, would lead to user-sensitive states in a GUI environment.

</details>


### 62. SidConArena: An Environment Evaluating Agents in Open-Ended,Positive-Sum Bargaining Game

- **Authors:** Yeqi Feng, Yuxin Chen, Tianxing He
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.27397v1](http://arxiv.org/abs/2606.27397v1)
- **PDF:** [https://arxiv.org/pdf/2606.27397v1](https://arxiv.org/pdf/2606.27397v1)
- **Categories:** cs.MA, cs.AI, cs.GT


> The paper presents **SidConArena**, a novel benchmark that casts multi‑agent economic interaction as a finite‑horizon, partially observable stochastic game comprising three linked phases—natural‑language negotiation with binding contracts, deterministic “converter” production, and sealed‑bid auctions for long‑term assets—allowing LLM agents to operate in open‑ended, positive‑sum bargaining settings. The authors implement a phase‑aware dispatch system, a neural‑symbolic action interface, and asynchronous execution so agents can exchange free‑form dialogue while being evaluated against strict game rules. Experiments in homogeneous and heterogeneous tournaments show that state‑of‑the‑art LLM agents generate higher economic returns than baselines, yet they routinely mis‑price resources, adopt overly passive bargaining strategies, and struggle with long‑horizon investment planning, highlighting key gaps for future agentic AI research.


<details>
<summary>Abstract</summary>

Evaluating LLM agents requires dynamic environments that go beyond static reasoning and zero-sum games. Real-world economic interaction is often open-ended and mixed-motive: agents must negotiate, create positive-sum surplus, compete for scarce assets, and plan under delayed returns. We introduce SidConArena, a new benchmark framework for evaluating LLM agents in open-ended, positive-sum bargaining. SidConArena formalizes a multi-player economy as a finite-horizon partially observable stochastic game with three coupled phases: natural-language negotiation with binding trades, deterministic converter-based production, and sealed-bid auctions for long-term assets. The framework combines structured observations, phase-aware agent dispatching, a neural-symbolic action interface, and asynchronous execution, enabling free-form interaction while preserving rule-grounded evaluation. Across homogeneous and heterogeneous tournaments, stronger frontier models achieve higher economic outcomes, yet agents still misvalue resources, bargain passively, and remain limited in long-horizon investment planning.

</details>


### 63. MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correction

- **Authors:** Congbo Ma, Hu Wang, Yichun Zhang, Farah E. Shamout
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25651v2](http://arxiv.org/abs/2606.25651v2)
- **PDF:** [https://arxiv.org/pdf/2606.25651v2](https://arxiv.org/pdf/2606.25651v2)
- **Categories:** cs.CL


> **Contribution:** The paper introduces **MedGuards**, a multi‑agent in‑context learning framework that safeguards Large Language Models in healthcare by detecting, localizing, and correcting medical errors without further training the base model, and proposes a new evaluation metric, the **Keyword‑Prioritized Correction Score (KPCS)**, to better capture safety‑critical content.  

**Methodology:** MedGuards decomposes the safety task into three specialized agents (detect, locate, correct) that operate on the same LLM prompt; a confidence‑guided arbitration module uses each agent’s reasoning trace and confidence score to resolve conflicts and produce the final corrected output.  

**Key Findings:** Across four multilingual clinical‑note datasets, MedGuards consistently outperforms existing heuristic and automated baselines on standard metrics and on KPCS, demonstrating higher error‑detection recall, correction accuracy, and interpretability, thereby advancing reliable, agentic AI deployment in medical contexts.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) are increasingly deployed in healthcare settings, accurate error detection and correction in generated or existing text becomes critical, as even minor mistakes can pose risks to patient safety. Existing methods for error detection and correction, including automated checks and heuristic-based approaches, do not generalize well across unseen datasets. In this paper, we propose MedGuards as a medical safety guardrail, which is a new framework that treats medical error detection and correction as a multi-agent in-context learning task. Specialized agents separately detect, localize, and correct errors, while a confidence-guided arbitration mechanism resolves disagreements using reasoning traces and confidence scores. This design enhances interpretability, robustness, and adaptability, without requiring additional training of the base LLMs. Additionally, we introduce the Keyword-Prioritized Correction Score (KPCS), a new evaluation metric that considers whether critical keywords within the reference text are generated correctly, providing a more comprehensive assessment than conventional metrics. Experiments across four multilingual medical datasets consisting of clinical notes demonstrate significant improvements by the proposed framework across several metrics and models. Our aim is to enable safer deployment of LLMs in real-world healthcare applications. For reproducibility, we make our code publicly available at https://github.com/congboma/MedGuards.

</details>


### 64. Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz

- **Authors:** Lea Roxanne Muth, Marian Margraf
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25622v1](http://arxiv.org/abs/2606.25622v1)
- **PDF:** [https://arxiv.org/pdf/2606.25622v1](https://arxiv.org/pdf/2606.25622v1)
- **Categories:** cs.CR, cs.AI


> The paper presents a multi‑agent system (MAS) that augments deterministic IT‑Grundschutz (IT‑GS) audits with a Hybrid Retrieval‑Augmented Generation pipeline, introducing a **hypothesis‑verification loop** that checks agent‑inferrred dependencies against a knowledge graph and a **decoupled reasoning pipeline** that separates semantic extraction from deterministic protection‑need inheritance. Using the BSI “RecPlast GmbH” case study, the authors evaluate the end‑to‑end system across structural analysis, protection‑need assessment, modeling, and final IT‑GS checking, reporting high precision/recall for the semantic phases (SA and modeling) but markedly lower performance in the logical, deterministic phases (PNA and IT‑GS check) due to the probabilistic nature of current LLMs. The results highlight that while MAS‑HybridRAG can substantially automate information extraction, achieving the strict determinism required for formal audit compliance remains a key challenge for agentic AI in this domain.


<details>
<summary>Abstract</summary>

The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises. To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-GS) of the Federal Office for Information Security. However, IT-GS certification is resource-intensive and requires a high level of manual effort for documentation, validation, and revision, making scalable implementation difficult and expensive.
  Building upon our previous conceptual framework, this paper presents the technical implementation and empirical evaluation of a Multi-Agent System (MAS) architecture combined with Hybrid Retrieval Augmented Generation (HybridRAG) for the partial automation of IT-GS certification. We introduce two novel technical contributions to the MAS architecture to enforce the compliance rigor. The Hypothesis-Verification Loop in the Structural Analysis (SA) phase that cross-references agent-inferred dependencies against the Knowledge Graph to reduce hallucinations, and a Decoupled Reasoning Pipeline that separates agent-driven semantic extraction from the deterministic protection need inheritance. We utilize the BSI's "RecPlast GmbH" case study as a human expert-generated reference data set for end-to-end evaluation of the architecture and to quantify Precision, Recall, and F1-scores. The performance of the system is investigated across the phases of SA, Protection Needs Assessment (PNA), Modeling, and IT-GS Check.
  The empirical results reveal noticeable differences throughout the different steps of IT-GS. While the MAS demonstrates high efficacy in semantic tasks (SA and Modeling), significantly reducing manual effort through automated information extraction, quantitative results reveal limitations in logical reasoning phases (PNA and IT-GS Check) as the probabilistic nature of current LLMs struggles to meet the deterministic rigor required by IT-GS.

</details>


### 65. BiPACE: Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation for LLM Agents

- **Authors:** Hanyang Wang, Weijieying Ren, Yuxiang Zhang, Ding Cao, Zhizhao Zeng, Ke Zeng, Tianxiang Zhao
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25556v1](http://arxiv.org/abs/2606.25556v1)
- **PDF:** [https://arxiv.org/pdf/2606.25556v1](https://arxiv.org/pdf/2606.25556v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> **Main contribution:** The paper introduces **BiPACE**, a bisimulation‑guided advantage estimator that corrects the state‑action credit mismatch inherent in current stepwise group‑based RL for large‑language‑model (LLM) agents, doing so without adding a learned critic, auxiliary losses, or extra rollouts.

**Methodology:** BiPACE first clusters timesteps using cosine distance in the LLM’s hidden‑state space (an empirical, policy‑induced bisimulation proxy) to avoid overly fine observation‑hash partitions. Within each cluster it applies **Action Counterfactual Estimation (PACE)**, recentering returns with action‑conditioned peer baselines to obtain a non‑parametric estimate of \(Q(s,a)-V(s)\).

**Key findings:** Across multiple benchmarks (ALFWorld, WebShop, TextCraft) and model sizes (Qwen2.5‑7B, Qwen2.5‑1.5B), BiPACE consistently outperforms prior group‑based methods (GiGPO, GRPO), raising validation success from 90.8 % to 97.1 % on ALFWorld 7B and achieving >95 % success on every seed, with only an 11 % per‑step computational overhead. This demonstrates that bisimulation‑based clustering plus action‑side counterfactuals markedly improve credit assignment for agentic LLMs.


<details>
<summary>Abstract</summary>

Stepwise group-based RL is an attractive way to train long-horizon LLM agents without a learned critic: it reuses multiple sampled rollouts to estimate local advantages. Its weakness is less visible but more fundamental: every group-relative estimator assumes that the steps it compares are equivalent for credit assignment. We show that current agentic variants violate this assumption through a state-action credit mismatch. The observation-hash partition is overly fine on the state side, creating singleton groups with zero step-level signal, while a single within-group mean is too coarse on the action side, mixing state-value estimation with action-specific credit. We introduce BiPACE (Bisimulation-Guided Policy Optimization with Action Counterfactual Estimation), a drop-in advantage estimator that fixes both sides without adding a critic, auxiliary loss, or extra rollouts. BiGPO clusters steps by cosine distance in the actor's own hidden-state geometry, an empirical policy-induced proxy for bisimulation that substantially lowers the singleton rate left by observation hashing. PACE then recenters returns within each behavioral cluster using action-conditioned peer baselines; its Q-style instance estimates a local Q(s,a)-V(s) nonparametrically. On ALFWorld/Qwen2.5-7B, BiPACE_Q raises overall validation success from GiGPO's 90.8 to $97.1\pm0.9$ over three seeds, and crosses the 95% threshold on every seed, which GiGPO never does within the same budget. On Qwen2.5-1.5B it reaches $93.5\pm1.2$ versus GiGPO's 86.7, and on WebShop and TextCraft it improves over GRPO and GiGPO at both model scales. The measured BiPACE-specific overhead is 11.3% of a single training-step wall time. Yet it changes the estimator's comparison unit from surface identity to approximate behavioral equivalence plus action-side counterfactuals. The code is available at https://github.com/TianxiangZhao/BiPACE.

</details>


### 66. Agentic evolution of physically constrained foundation models

- **Authors:** Jiangwei Zhang, Wen Sun, Chong Wang, Shiyao Li, Cheng Che, Chunjing Han, Dan Meng, Jian Yang, Yu Wang, Rui Hou
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25532v1](http://arxiv.org/abs/2606.25532v1)
- **PDF:** [https://arxiv.org/pdf/2606.25532v1](https://arxiv.org/pdf/2606.25532v1)
- **Categories:** cs.AI, cs.AR, cs.LG, cs.MA


> **Main contribution:** The paper introduces a physically grounded, multi‑agent discovery engine that couples an Evolutionary Knowledge Graph with an “algorithmic Chain‑of‑Thought” to turn uninformed stochastic search into directed, hardware‑aware structural evolution of foundation models.

**Methodology:** Past scientific innovations are encoded in a knowledge graph; agents query this graph to generate step‑by‑step reasoning traces that guide the evolutionary search for hardware‑compliant model architectures and compression schemes. A bandwidth‑efficient Sensitivity Profile evaluates candidate designs against strict compute and memory constraints.

**Key findings:** Using this framework, the system autonomously invented two compression techniques—Q‑Enhance (reducing long‑context degradation) and MoE‑Salient‑AQ (improving sparse Mixture‑of‑Experts performance by 3.7% in sub‑3‑bit regimes). These methods enabled deployment of a 235 B‑parameter model on a dual‑A100 server with a 75 % memory reduction and only 0.64 % accuracy loss, demonstrating a scalable, hardware‑software co‑design paradigm for agentic AI.


<details>
<summary>Abstract</summary>

Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs. Here, we present a physically grounded, multi-agent discovery engine that autonomously architects hardware-compliant computing systems. Anchored by an Evolutionary Knowledge Graph structuring past scientific innovations, the framework extracts an "algorithmic Chain-of-Thought" to transform blind stochastic search into directed structural evolution. Applied to the extreme testbed of foundation model deployment, the engine evolved two hardware-aware compression methodologies surpassing human-engineered heuristics: Q-Enhance mitigates long-context accuracy loss in dense models, and MoE-Salient-AQ outperforms state-of-the-art manual sparse Mixture-of-Experts designs by 3.7% at sub-3-bit regimes. Utilizing a bandwidth-efficient Sensitivity Profile, we successfully deployed a massive 235-billion-parameter model onto a constrained dual-A100 server, reducing memory requirements by 75% with a marginal 0.64% accuracy degradation. By transforming unconstrained combinatorial search into knowledge-driven autonomy, this establishes a scalable hardware-software co-design paradigm for machine-driven discovery within strict physical boundaries.

</details>


### 67. Low Variance Trust Region Optimization with Independent Actors and Sequential Updates in Cooperative Multi-agent Reinforcement Learning

- **Authors:** Bang Giang Le, Viet Cuong Ta
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25526v1](http://arxiv.org/abs/2606.25526v1)
- **PDF:** [https://arxiv.org/pdf/2606.25526v1](https://arxiv.org/pdf/2606.25526v1)
- **Categories:** cs.LG, cs.MA


> **Main contribution:** The paper identifies and solves the exploding‑variance problem of advantage estimates that arises in sequential‑update, independent‑actor cooperative MARL when using Trust‑Region methods, and proposes a novel “clipped‑advantage” objective that bounds these fluctuations.

**Methodology:** By theoretically analyzing and empirically confirming the variance blow‑up, the authors introduce a clipping term into the Trust‑Region surrogate loss, prove that it yields a monotonic performance bound and sub‑linear convergence to an ε‑Nash equilibrium, and instantiate two practical algorithms that incorporate the clipped objective while retaining independent‑actor training.

**Key findings:** Across three standard cooperative MARL benchmarks, the clipped‑advantage algorithms achieve higher returns than state‑of‑the‑art baselines, exhibit markedly lower variance in advantage estimates, and converge more stably, confirming the effectiveness of low‑variance trust‑region optimization for independent‑actor multi‑agent systems.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning assumes each agent shares the same reward function and can be trained effectively using the Trust Region framework of single-agent. Instead of relying on other agents' actions, the independent actors setting considers each agent to act based only on its local information, thus having more flexible applications. However, in the sequential update framework, it is required to re-estimate the joint advantage function after each individual agent's policy step. Despite the practical success of importance sampling, the updated advantage function suffers from exponentially high variance problems, which likely result in unstable convergence. In this work, we first analyze the high variance advantage both empirically and theoretically. To overcome this limitation, we introduce a clipping objective to control the upper bounds of the advantage fluctuation in sequential updates. With the proposed objective, we provide a monotonic bound with sub-linear convergence to $ε$-Nash Equilibria. We further derive two new practical algorithms using our clipping objective. The experiment results on three popular multi-agent reinforcement learning benchmarks show that our proposed method outperforms the tested baselines in most environments. By carefully analyzing different training settings, our proposed method is highlighted with both stable convergence properties and the desired low advantage variance estimation. For reproducibility purposes, our source code is publicly available at https://github.com/giangbang/Low-Variance-Trust-Region-MARL.

</details>


### 68. The impact of artificial intelligence on enterprise software user roles

- **Authors:** Isabel Unger, Elizangela Valarini, Martin Schrepp, Nina Hollender, Gabriela Rocha, Erik Bertram
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25525v1](http://arxiv.org/abs/2606.25525v1)
- **PDF:** [https://arxiv.org/pdf/2606.25525v1](https://arxiv.org/pdf/2606.25525v1)
- **Categories:** cs.SE, cs.AI


> The paper presents a qualitative investigation of how AI, especially agentic AI, is reshaping professional responsibilities on SAP’s Business Technology Platform. By conducting 20 expert interviews and a participatory workshop with 24 participants, the authors map emerging tasks—greater automation of routine operations, intensified human‑AI collaboration, and reliance on autonomous agents—to concrete changes in existing role definitions (e.g., the BTP User Type Matrix). They conclude that enterprise‑software role taxonomies, governance structures, and design practices must be revised to accommodate these AI‑driven shifts, highlighting the need for new oversight functions and AI‑native interaction models in the agentic AI era.


<details>
<summary>Abstract</summary>

Artificial Intelligence (AI) is rapidly reshaping the nature of work in software development, transforming user roles, workflows, and collaboration patterns across enterprise platforms. This qualitative study investigates how AI alters professional responsibilities within the context of SAP's Business Technology Platform (BTP), combining expert interviews (n=20) and a participatory workshop (n=24). The results reveal substantial shifts in day-to-day tasks and roles in the development domain, characterized by increasing automation of operational tasks, expanding human-AI collaboration, and growing reliance on agentic AI systems. The study further identifies significant implications for existing user-role frameworks, such as the BTP User Type Matrix, which requires adaptation as the workforce is undergoing significant role specific changes. Collectively, these findings highlight a workforce landscape in transition and underscore the need for revised role taxonomies, new governance and oversight functions, and updated design approaches for AI-native enterprise software systems.

</details>


### 69. Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models

- **Authors:** Xinyu Lian, Walid Krichene, Beichen Huang, Masahiro Tanaka, Olatunji Ruwase, Li Zhang, Minjia Zhang
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25519v1](http://arxiv.org/abs/2606.25519v1)
- **PDF:** [https://arxiv.org/pdf/2606.25519v1](https://arxiv.org/pdf/2606.25519v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper reveals that low‑bit post‑training quantization (INT4/INT3) of reasoning‑oriented language models incurs a hidden cost—substantially longer chain‑of‑thought (CoT) sequences, which they term *token inflation*, despite often preserving final‑answer accuracy.  

**Methodology:** The authors evaluate quantized and full‑precision versions of several LLMs across math, code, scientific QA, and tool‑use tasks, measuring the *CoT Token Inflation Ratio* (average reasoning‑token count of quantized vs. FP models). They analyse trace characteristics (step count, semantic repetition) and quantify the real‑world latency impact, then test mitigation approaches including prompting tweaks, decoding‑time sampling, and quantization‑aware training (QAT).  

**Key findings:** INT4/INT3 quantization can double the number of reasoning tokens while maintaining accuracy, eroding the expected per‑token speedup and increasing serving latency. Prompt or sampling tweaks give unreliable trade‑offs, whereas QAT reduces both accuracy loss and token inflation, suggesting that reporting reasoning‑token usage alongside accuracy is essential for evaluating quantized reasoning agents.


<details>
<summary>Abstract</summary>

Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency. We show that low-bit post-training quantization can introduce a hidden test-time compute cost: quantized reasoning models often generate longer chains of thought even when they still answer correctly. Across mathematical reasoning, code generation, scientific question answering, and agentic tool-use benchmarks, we find that INT4/INT3 quantization can preserve accuracy but increase reasoning-token usage, offsetting the expected per-token speedup. To measure this effect, we introduce the CoT Token Inflation Ratio, which compares reasoning length between quantized and full-precision models averaged across all evaluation benchmarks. We further show that token inflation is accompanied by behavioral changes in the reasoning trace, including more intermediate steps and greater semantic repetition. These changes translate into measurable end-to-end real-world serving penalties. Finally, we evaluate mitigation strategies and find that prompting and decoding-time sampling offer inconsistent accuracy-length trade-offs, while quantization-aware training shows more promise in reducing both accuracy degradation and token inflation. Our results suggest that reasoning-token usage should be reported alongside accuracy when evaluating quantized reasoning models.

</details>


### 70. The Interplay of Harness Design and Post-Training in LLM Agents

- **Authors:** Kyungmin Kim, Youngbin Choi, Seoyeon Lee, Suhyeon Jun, Dongwoo Kim, Sangdon Park
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25447v1](http://arxiv.org/abs/2606.25447v1)
- **PDF:** [https://arxiv.org/pdf/2606.25447v1](https://arxiv.org/pdf/2606.25447v1)
- **Categories:** cs.LG, cs.CL


> The paper identifies the “harness” – the specification of which tools an LLM agent can use, how they are described, and what per‑step contextual data are supplied – as a critical, yet previously static, factor that interacts with post‑training fine‑tuning. By extending the ALFWorld benchmark to make the harness a configurable design variable and to simulate task and tool‑environment shifts, the authors show that post‑training methods that are aware of, and adapt to, harness design dramatically improve both in‑distribution performance and robustness to out‑of‑distribution changes; conversely, a minimally engineered harness causes severe performance degradation under stronger environment shifts. These results establish that co‑designing harness architecture and post‑training procedures is essential for reliable, adaptable agentic AI.


<details>
<summary>Abstract</summary>

Tool-integrated LLM agents are often wrapped within a harness: the scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation. While agents are routinely post-trained, this scaffolding is typically treated as a fixed engineering detail, with design effort limited to the training-free regime. Moreover, existing post-training algorithms assume a static environment, even though tool environments and tasks often shift upon deployment. To address this gap, we extend $\texttt{ALFWorld}$ (i) to treat the harness as a controllable design dimension and (ii) to support evaluation under task and tool environment shifts. Building on this, we systematically analyze how the harness design influences post-training in both in-distribution and out-of-distribution (OOD) settings. We empirically show that harness-aware post-training not only improves in-distribution performance but also enables agents to robustly adapt to OOD settings. Under a harness with minimal design effort, post-training suffers a drastic performance drop under stronger tool environment shifts, further highlighting the importance of harness-aware post-training under such shifts.

</details>


### 71. BrainAgent: A Large Language Model-Driven Multi-Agent Framework for Autonomous Brain Signal Understanding

- **Authors:** Yangxuan Zhou, Sha Zhao, Jiquan Wang, Shijian Li, Gang Pan
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25400v1](http://arxiv.org/abs/2606.25400v1)
- **PDF:** [https://arxiv.org/pdf/2606.25400v1](https://arxiv.org/pdf/2606.25400v1)
- **Categories:** cs.AI


> The paper presents **BrainAgent**, a novel LLM‑driven multi‑agent system that translates natural‑language goals into fully automated, end‑to‑end brain‑signal processing pipelines. By using a hierarchical supervisor that decomposes tasks and delegates them to specialized sub‑agents, the framework eliminates the need for deep domain expertise and supports long‑horizon, adaptive workflows. Benchmarked on a new systematic suite for brain‑signal analysis, BrainAgent outperforms existing static pipelines in reliability and automation, demonstrating that agentic LLM architectures can democratize and scale brain‑computer interface applications.


<details>
<summary>Abstract</summary>

Brain-Computer Interfaces (BCIs) and brain signal understanding are pivotal for clinical health and next-generation interactions. Despite this significance, its widespread adoption in real-world scenarios remains restricted, primarily because current analytical paradigms lack sufficient agentic intelligence. First, existing methodologies impose prohibitive technical barriers, requiring extensive specialized expertise. Second, they remain inherently static and task-specific, failing to execute the complex, long-horizon workflows essential for real-world deployment. To accelerate the democratization of brain signal understanding, we draw inspiration from Large Language Models (LLMs) to introduce BrainAgent, an LLM-driven multi-agent framework designed to ground abstract natural language intent into rigorous, executable, and end-to-end processing pipelines. BrainAgent employs a hierarchical architecture where a central supervisor orchestrates specialized sub-agents for adaptive task decomposition and execution. Furthermore, we establish a comprehensive, systematic benchmark for evaluating agentic systems in brain signal analysis. Empirical results demonstrate that BrainAgent effectively automates complex workflows with superior reliability, marking a paradigm shift toward democratized brain signal understanding.

</details>


### 72. Offline Multi-agent Continual Cooperation via Skill Partition and Reuse

- **Authors:** Yuchen Xiao, Lei Yuan, Ruiqi Xue, Tieyue Yin, Yang Yu
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25389v1](http://arxiv.org/abs/2606.25389v1)
- **PDF:** [https://arxiv.org/pdf/2606.25389v1](https://arxiv.org/pdf/2606.25389v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **COMAD**, a continual‑learning framework that autonomously discovers, partitions, and reuses coordination skills from offline multi‑agent datasets, enabling agents to expand an unbounded skill library without suffering catastrophic forgetting.

**Methodology:** COMAD first encodes mixed‑behaviour trajectories with a variational auto‑encoder to extract latent skill embeddings, then clusters these embeddings using a density‑based reusability estimator. A multi‑head policy architecture incorporates the resulting skill library, and the advantage function is regularized toward the reusable skills during offline RL updates.

**Findings:** Theoretical analysis shows COMAD approximates the optimal solution of the continual skill‑discovery objective. Empirically, on several MARL benchmarks, COMAD continuously grows its skill set, yielding markedly higher forward and backward transfer—and lower interference—than fixed‑size or heuristic skill‑library baselines.


<details>
<summary>Abstract</summary>

Extracting skills from multi-agent offline dataset improves learning efficiency via sharing task-invariant coordination skills among tasks. In settings where tasks occur sequentially and the space of skills grows exponentially, existing approaches that rely on heuristically designed and fixed-sized skill libraries struggle to resolve the problem of distributional shift and interference, facing catastrophic forgetting and plasticity loss. To address this problem and endow agents with the ability to continually discover and reuse coordination skills in open-environment, we propose COMAD, a principled framework for Continual Offline Multi-agent Skill Discovery via Skill Partition and Reuse. We first discover skills from mixed multi-agent behavior data with an auto-encoder to transform coordination knowledge into reusable coordination skills. Then we construct a skill-augmented policy learning objective with multi-head architectures, explicitly guiding the advantage function with reusable skills identified via a density-based reusability estimator. Theoretical analysis shows our method approximates the optimum of a continual skill discovery problem. Empirical results across diverse MARL benchmarks show that COMAD continually expands its skill library to mitigate interference, achieving superior forward and backward transfer for task streams compared to multiple baselines.

</details>


### 73. Agentic Knowledge Tracing: A Multi-Agent LLM Architecture for Stealth Assessment of Financial Literacy in Serious Games

- **Authors:** Gabriel Santos, Rita Julia, Marcelo Nascimento
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25358v1](http://arxiv.org/abs/2606.25358v1)
- **PDF:** [https://arxiv.org/pdf/2606.25358v1](https://arxiv.org/pdf/2606.25358v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **Agentic BKT**, a pipeline that uses a team of specialized large‑language‑model agents to covertly assess players’ financial‑literacy competence while they play a 2‑D serious‑game platform. The system first logs every player action, then an LLM classifier tags each event on a four‑point rubric; four domain‑focused agents (risk mitigation, investing, spending, credit) independently apply Bayesian Knowledge Tracing to their respective competency streams, and a final judge agent aggregates these into an overall mastery score. Across 193 K‑12 users and 264 sessions, the multi‑agent architecture achieved significantly higher predictive validity than a single‑LLM baseline (correlations r = 0.276–0.333 with learning gains and post‑test scores, versus non‑significant r = 0.095), demonstrating that domain decomposition and session‑level reasoning enable reliable, stealth assessment of multidimensional financial literacy.


<details>
<summary>Abstract</summary>

Assessing financial literacy during gameplay without disrupting the learning experience remains a key challenge in serious games for education. We present the Agentic BKT pipeline, a multi-agent large language model architecture for stealth assessment of financial competencies from open-ended gameplay events. The pipeline processes events from a 2D platformer serious game aligned with the OECD/INFE financial literacy framework through four phases: (1) the game captures every player decision as a structured event log; (2) an LLM event classifier labels each action on a four-point rubric validated against three domain experts (Fleiss kappa = 0.624, substantial agreement); (3) four domain-specific agents specializing in risk mitigation, investing, spending, and credit management perform session-level reasoning over behavioral trajectories, feeding per-competency Bayesian Knowledge Tracing that estimates mastery within each domain; and (4) an expert judge agent synthesizes the domain-level estimates into an overall mastery score. Evaluated with 193 K-12 participants across 264 game sessions, the Agentic BKT pipeline yields mastery estimates significantly correlated with learning gain (r = 0.276, p = 0.0001) and post-test scores (r = 0.333, p < 0.0001) while showing no correlation with pre-test scores, providing both convergent and discriminant validity. The multi-agent approach approximately triples the predictive validity of a single-LLM baseline (r = 0.095, not significant) in this study, demonstrating that domain decomposition and session-level reasoning play a central role in capturing the multidimensional nature of financial literacy from gameplay

</details>


### 74. Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention

- **Authors:** Luke McDermott, Robert W. Heath, Rahul Parhi
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25342v1](http://arxiv.org/abs/2606.25342v1)
- **PDF:** [https://arxiv.org/pdf/2606.25342v1](https://arxiv.org/pdf/2606.25342v1)
- **Categories:** cs.LG


> The paper argues that to enable transformers to perform truly lifelong in‑context learning—i.e., to keep using ever‑growing experience without exceeding fixed hardware resources—attention must be reformulated as a **parametric** operation rather than the conventional soft‑max, non‑parametric key‑value cache. The authors survey and unify existing parametric attention schemes (linear/low‑rank attention, state‑space models, fast‑weight programmers, and test‑time‑training layers), showing that they replace the expanding cache with a small, online‑trainable neural network that learns a regression from keys to values at test time, thereby keeping memory constant. Experiments and analysis reveal that current parametric methods still suffer from limited representational capacity or expensive online updates, highlighting concrete bottlenecks and posing open research questions for building long‑horizon, memory‑bounded agentic AI systems.


<details>
<summary>Abstract</summary>

Lifelong continual learning remains an obstacle on the path to human-like intelligence. Modern transformers show sparks of intelligence with in-context learning. The quadratic nature of attention, however, prohibits transformers from performing this process on arbitrarily long sequences. In this work, we argue that extending in-context learning to lifelong settings is a practical solution for continual learning in AI agents. In particular, we argue that \emph{parametric forms of attention} are needed to understand a lifetime of context with transformers on a fixed hardware budget. These attention mechanisms learn the relationship between keys and their associated values at test-time with parametric regression. Our generalization of parametric approaches (linear attention, state-space models, fast weight programmers, and test-time training layers) contrasts with nonparametric counterparts like softmax attention. They replace the ever-growing key-value cache with an online-trainable neural network, maintaining a constant memory footprint. We highlight how parametric attention currently fall short of lifelong learning due to limited memory capacity or costly online updates. To address these issues, we pose a set of open questions with novel insights to guide the field toward long-horizon agents.

</details>


### 75. AI Coaching for Accelerating Human Skill Development with Reinforcement Learning

- **Authors:** Wei Wang, Enlin Gu, Antonio Loquercio, Haimin Hu, Rahul Mangharam
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25337v1](http://arxiv.org/abs/2606.25337v1)
- **PDF:** [https://arxiv.org/pdf/2606.25337v1](https://arxiv.org/pdf/2606.25337v1)
- **Categories:** cs.RO, cs.AI, cs.HC


> The paper introduces a novel formulation of AI‑human interaction as a non‑cooperative dynamic game in which an embodied AI coach seeks to maximize the learner’s autonomous competence rather than immediate task performance. By integrating adaptive shared‑control reinforcement learning with probabilistic models of the coach’s causal impact on skill evolution, the authors train policies that strategically scaffold, then withdraw assistance to promote productive failure. In a user study with 33 participants performing first‑person‑view drone racing, the learned coaching agent yields significantly higher skill acquisition than existing AI‑coaching baselines, demonstrating the effectiveness of game‑theoretic, influence‑aware coaching for agentic AI.


<details>
<summary>Abstract</summary>

AI copilots can substantially boost human performance through shared control, but excessive assistance can induce over-reliance and skill atrophy. This paper studies how an embodied AI agent can act as a coach that accelerates human motor-skill development. We argue that effective coaching requires strategic scaffolding and stepping back that are aligned with the learner's capability, allowing productive failures that drive learning. We formalize the interactive AI coaching process as a non-cooperative dynamic game in which the learner optimizes task performance while the coach targets the learner's independent competence. Building on this formalism, we develop a reinforcement learning framework combining adaptive shared control with probabilistic models of the coach's causal influence on skill evolution, enabling tractable training of coaching policies. A comprehensive user study (N=33) on first-person-view drone racing shows significant gains in human learning outcomes over state-of-the-art AI coaching baselines.

</details>


### 76. Stagnant Neuron: Towards Understanding the Plasticity Loss in Multi-Agent Reinforcement Learning Value Factorization Methods

- **Authors:** Zhengzhu Liu, Zeming Gao, Haoyuan Qin, Jiawei Hu, Junhao Wu, Miao Zhu, Haipeng Zhang, Chennan Ma, Siqi Shen, Cheng Wang
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25335v1](http://arxiv.org/abs/2606.25335v1)
- **PDF:** [https://arxiv.org/pdf/2606.25335v1](https://arxiv.org/pdf/2606.25335v1)
- **Categories:** cs.LG


> The paper identifies “stagnant neurons” – units whose gradients vanish relative to their weights – as the primary cause of plasticity loss in value‑factorization MARL algorithms when they are transferred to new tasks. To remediate this, the authors introduce KNIFE, a neuron‑level intervention that replaces each stagnant unit with a triplet of components (a frozen knowledge neuron, a freshly re‑initialized active neuron, and a compensation neuron) to preserve prior cooperative knowledge while restoring learning capacity. Experiments on SMACv2, predator–prey, and matrix‑game benchmarks show that KNIFE consistently outperforms existing plasticity‑injection techniques, enabling more adaptable multi‑agent policies.


<details>
<summary>Abstract</summary>

Multi-Agent Reinforcement Learning (MARL) value factorization methods can suffer from a loss of plasticity, gradually failing to adapt when transferring to new task instances. We trace this issue to stagnant neurons, units whose gradient updates become negligibly small relative to their weights, thereby hindering learning. While existing plasticity injection methods exist, they prove ineffective for such neurons. To address this, we propose Knowledge-retentive Neuron-level PlastIcity Focusing InjEction (KNIFE), a novel method that directly targets stagnant neurons. KNIFE replaces each stagnant neuron with a composite unit comprising three specialized components: a frozen knowledge neuron to preserve acquired knowledge, a re-initialized active neuron to restore learning capacity, and a compensation neuron to ensure the combined output matches the original, thus maintaining previous learned cooperation knowledge. Extensive experiments on SMACv2, predator-prey, and matrix games demonstrate that KNIFE significantly outperforms state-of-the-art plasticity injection methods.

</details>


### 77. Bridging the Post-discharge Gap: A Traceable Multi-agent Framework for Safe and Continuous Care

- **Authors:** Runwei Guan, Yi Zhou, Heyi Lin, Jinjing Zhu, Mingyuan Hou, Yang Yang, Fang Yuan, Xiaohong Lin, Shaofeng Liang, Xuming Hu, Tao Li, Tianbin Zhao, Yutao Yue, Zhiyuan Wang, Hui Xiong
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25334v1](http://arxiv.org/abs/2606.25334v1)
- **PDF:** [https://arxiv.org/pdf/2606.25334v1](https://arxiv.org/pdf/2606.25334v1)
- **Categories:** cs.MA


> The paper introduces **Healink**, a memory‑augmented, multi‑agent system that performs safe, continuous post‑discharge follow‑up by coupling a triage router, a relational‑database‑backed unified memory, and a constraint‑driven retrieval‑augmented generation engine. By vectorizing patients’ longitudinal records and weighting similarity across phenotypic and treatment dimensions, the agents retrieve and ground their answers in prescription‑level evidence, producing traceable, white‑box response chains that avoid cross‑department drug conflicts. In blinded clinical evaluations on 485 real‑world follow‑up cases (plus the webMedQA benchmark), Healink surpasses physician baselines in authoritativeness, completeness, and safety, demonstrating a scalable, agentic AI approach for reliable, long‑term patient care.


<details>
<summary>Abstract</summary>

Post-discharge clinical follow-up is critical for maintaining continuity of care and mitigating long-term health risks. However, traditional follow-up paradigms suffer from shortage of health workforce, fragmented patient histories, and information silos across clinical departments. While large language models have demonstrated potential in medical question-answering, their deployment in continuous care is hindered by hallucination risks and a fundamental inability to reason over longitudinal, patient-specific constraints. Here we present Healink, a memory-enhanced multi-agent framework to support AI-assisted post-discharge follow-up by generating prescription-grounded, traceable responses that improved completeness and perceived clinical utility in retrospective and physician-blinded evaluations. The architecture seamlessly integrates a triage routing mechanism, a unified memory enhancement module utilizing a robust relational database for optimal latency, and a strict constraint-based retrieval-augmented generation engine. By vectorizing historical clinical records and employing weighted similarity functions across diverse phenotypic and intervention dimensions, Healink ensures precise inter-patient and intra-patient case matching while actively preventing cross-departmental drug conflicts. We evaluated Healink on a dataset comprising 400 continuous and 85 highly complex real-world follow-up cases, alongside the webMedQA benchmark. In a rigorous single-blind evaluation conducted by clinical experts, the framework outperformed human physician baselines in both authoritativeness and clinical safety. By generating a traceable, white-box evidence chain, Healink provides a scalable, safe, and highly effective paradigm for intelligent patient management, ultimately enhancing societal healthcare outcomes.

</details>


### 78. Decoupling Reconnaissance and Exploitation: Measuring the Capability Boundaries of LLM-Based Web Penetration Testing

- **Authors:** Liwei Yu, Shuo Li, Ming Zhou, Ge Chu, Yan Guo
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25332v1](http://arxiv.org/abs/2606.25332v1)
- **PDF:** [https://arxiv.org/pdf/2606.25332v1](https://arxiv.org/pdf/2606.25332v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a two‑stage, decoupled evaluation framework that isolates the exploitation component from the reconnaissance phase of LLM‑driven web penetration testing, allowing researchers to measure true exploit success without the confounding errors of early‑stage information gathering. By injecting ground‑truth vulnerabilities into 70 high‑fidelity testbeds and conducting knowledge‑driven ablations, the authors benchmark five open‑source agents (multi‑agent, monolithic, and graph‑driven) on 50 representative flaws, finding that while agents can reach up to 90 % exploit success when supplied correct context, their autonomous reconnaissance tops out at only ~50 % recall due to difficulties parsing unstructured telemetry. The study also uncovers architecture‑specific strengths—multi‑agent systems excel at long‑sequence attacks, whereas monolithic and graph‑based designs are superior for short‑chain injections and cross‑session access‑control bugs—providing a granular benchmark for future agentic AI security tools.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have shown promise for automated penetration testing, yet existing end-to-end black-box evaluations are highly susceptible to error cascading: failures in early reconnaissance can mask an agent's actual ability to exploit vulnerabilities. To more accurately characterize these capabilities, we propose a two-stage decoupled evaluation framework that separates exploit execution from reconnaissance. Using ground-truth injection and knowledge-driven ablation across 70 high-fidelity web vulnerability testbeds, our framework isolates exploitation performance from reconnaissance noise. We empirically evaluate five open-source penetration-testing agents, covering multiagent, monolithic, and graph-driven architectures, on a strictly aligned subset of 50 representative vulnerabilities. The results reveal a substantial capability gap. With accurate vulnerability context, agents achieve a functional success rate of up to 90.0%, whereas autonomous reconnaissance, measured by targeted vulnerability recall, plateaus at approximately 50.0%, primarily due to failures in parsing unstructured telemetry. Cross-architectural analysis further reveals distinct capability niches: multi-agent isolation is more effective for long-sequence interactions such as de-serialization, while monolithic and graph-driven designs perform better on short-chain injections and cross-session access-control vulnerabilities, respectively. This decoupled evaluation work provides a fine-grained benchmarking protocol and an empirical basis for designing next-generation automated offensive security agents.

</details>


### 79. EvoFlock: evolved inverse design of multi-agent motion

- **Authors:** Craig Reynolds
- **Published:** 2026-06-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25280v1](http://arxiv.org/abs/2606.25280v1)
- **PDF:** [https://arxiv.org/pdf/2606.25280v1](https://arxiv.org/pdf/2606.25280v1)
- **Categories:** cs.NE, cs.GR, cs.MA


> EvoFlock introduces an inverse‑design framework that automatically tunes the numerous control parameters of multi‑agent motion models by coupling a user‑specified fitness function with a genetic‑algorithm optimizer. The methodology evaluates candidate parameter sets through forward simulations of flocking dynamics, rewarding proper inter‑agent spacing, target speed, and obstacle avoidance, and iteratively evolves them toward the desired emergent behavior. Experiments show that the evolved parameters reliably reproduce realistic flocking—including the characteristic alignment of birds—as an emergent consequence of spacing regulation, demonstrating a scalable way to calibrate and redesign complex agentic systems such as crowds, traffic, and animal groups.


<details>
<summary>Abstract</summary>

This paper describes an automatic method for adjusting or tuning models of multi-agent motion. Simulating the motion of bird flocks, human crowds, vehicle traffic, and other multi-agent systems is a widely used technique. These simulations model the behavior of a single group member (bird, human, or vehicle). The group behaviors (flock, crowd, traffic) emerge from interactions between group members. These models typically have many numerical control parameters. Even if each parameter is intuitive in isolation, their interaction can be complex and nonlinear. It is challenging to determine which parameters to adjust for the desired change in group behavior. Changing one aspect of group behavior often causes other aspects to change, leading to a tedious process of incremental changes. This work takes an inverse design approach. The desired group behavior is measured with a user-defined objective(/fitness/loss) function and optimized with a genetic algorithm. The objective function used here for basic flocking rewards proper spacing with neighbors, flying near a desired speed, and avoiding obstacles. Interestingly, the vivid alignment seen in bird flocks appears to emerge from maintaining proper spacing between flockmates.

</details>


### 80. Life After Benchmark Saturation: A Case Study of CORE-Bench

- **Authors:** Nitya Nadgir, Sayash Kapoor, Kangheng Liu, Peter Kirgis, Matilda Orona, Stephan Rabanser, Tilman Bayer, Abhishek Shetty, Yue Ling, Derrick Chan-Sew, Rumi Nakagawa, Saiteja Utpala, Zachary S. Siegel, Arvind Narayanan
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.26158v1](http://arxiv.org/abs/2606.26158v1)
- **PDF:** [https://arxiv.org/pdf/2606.26158v1](https://arxiv.org/pdf/2606.26158v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a benchmark's accuracy saturates, it is often retired and replaced with a more challenging version. We show that this approach privileges accuracy and misses the opportunity to study six other key dimensions of agent performance: construct validity issues such as shortcuts, out-of-distribution generalizability, efficiency, reliability, the relative importance of the model versus the scaffold, and uplift from human-agent collaboration. We use CORE-Bench Hard, a benchmark for computational reproducibility of scientific code, as a case study to demonstrate that measuring agents along these dimensions yields meaningful insights into agent performance even after accuracy saturates. First, we surface threats to construct validity in CORE-Bench Hard that are difficult to anticipate with less capable agents. We introduce an improved benchmark, CORE-Bench v1.1, and an out-of-distribution task suite, CORE-Bench OOD. Second, we find that despite accuracy saturation, CORE-Bench v1.1 remains useful for measuring efficiency, reliability, model performance, and scaffold performance. Finally, we conduct a small-scale randomized experiment to measure uplift from human-agent collaboration on real-world computational reproducibility tasks. We find a statistically significant speedup by about a factor of two -- likely underestimated due to one-fifth of human-only reproductions reaching the time limit before completing -- and describe various other findings. Together, our contributions present a more rigorous alternative to the dominant accuracy-centric evaluation paradigm.

</details>


### 81. To Isolate or to Score? Model-Adaptive Assessment for Cost-Efficient Multi-Agent RAG

- **Authors:** Jungseob Lee, Chanjun Park, Heuiseok Lim
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25191v1](http://arxiv.org/abs/2606.25191v1)
- **PDF:** [https://arxiv.org/pdf/2606.25191v1](https://arxiv.org/pdf/2606.25191v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution** – The paper uncovers why multi‑agent assessment in retrieval‑augmented generation (RAG) is sometimes unnecessary and introduces **MADARA**, a lightweight, model‑adaptive routing system that decides, per query, whether to run a full multi‑agent assessment or to fall back on a much cheaper “isolation‑only” strategy.

**Methodology** – The authors run a controlled, training‑free experiment on 7 B–9 B instruction‑tuned LLMs across several QA benchmarks, comparing (1) full multi‑agent scoring, (2) per‑document isolation (answer each retrieved document independently), and (3) a novel label‑free probe called **Reasoning‑Score Coupling** that detects when a model’s performance depends on quality scoring. They then derive diagnostic thresholds from a single pilot model and show they generalize zero‑shot to four unseen model families.

**Key findings** – For weaker baselines, isolation alone matches full assessment and yields up to **+50 pp** improvement, indicating that the primary benefit of multi‑agent pipelines is resolving multi‑document context confusion, not scoring. For stronger baselines, scoring matters, and the Reasoning‑Score Coupling probe reliably predicts when scoring will help. MADARA leverages these insights to route queries dynamically, cutting computational cost dramatically while preserving or improving RAG performance across diverse models.


<details>
<summary>Abstract</summary>

Multi-agent document assessment for retrieval-augmented generation is computationally expensive, driving practitioners toward smaller, deployable models whose assessment mechanisms remain poorly understood. We conduct a controlled study of training-free interventions on 7B-9B instruction-tuned models across diverse QA benchmarks, revealing a sharp dichotomy in how models benefit from assessment. For weaker baselines, the dominant mechanism is per-document isolation. Astoundingly, assessment-free isolation matches full multi-agent assessment, demonstrating that resolving multi-document context confusion, rather than scoring quality, drives outsized gains of up to 50 percentage points. Conversely, for strong baselines where scoring quality matters, we introduce Reasoning-Score Coupling, a label-free perturbation probe that classifies scoring behavior. Integrating these findings, we propose MADARA, a model-adaptive routing architecture. Crucially, MADARA's diagnostic thresholds derived from a single pilot model generalize zero-shot to four unseen model families, providing a robust, lightweight pipeline to eliminate computational overhead.

</details>


### 82. TRUSTMEM: Learning Trustworthy Memory Consolidation for LLM Agents with Long-Term Memory

- **Authors:** Tianyu Yang, Sudipta Paul, Vijay Srinivasan, Vivek Kulkarni, Srinivas Chappidi
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25161v1](http://arxiv.org/abs/2606.25161v1)
- **PDF:** [https://arxiv.org/pdf/2606.25161v1](https://arxiv.org/pdf/2606.25161v1)
- **Categories:** cs.AI


> **Contribution:**  
TRUSTMEM introduces a trust‑oriented framework for long‑term memory management in LLM‑driven agents, explicitly targeting the omission, corruption, and hallucination errors that arise when agents write, revise, or delete external memory.

**Methodology:**  
The system adds a *Memory Transition Verifier* that scores candidate memory updates on coverage, preservation, and faithfulness, then uses these scores to form preference pairs among competing updates. A preference‑guided reinforcement‑learning loop trains the agent to select updates that maximize these trust metrics, effectively shaping the memory‑consolidation policy.

**Key Findings:**  
Across three benchmarks (MemoryAgentBench, HaluMem, Mem‑alpha) TRUSTMEM achieves state‑of‑the‑art performance, boosting HaluMem extraction F1 by +12.14 points and cutting transition‑level omission, corruption, and hallucination errors by 40.1 %, 79.1 %, and 50.0 % respectively, demonstrating markedly higher utility and reliability of long‑term memory for LLM agents.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents rely on long-term memory to support extended interactions and personalized assistance beyond finite context windows. Existing memory agents actively update external memory through generated write, revise, and delete operations, but these updates may omit important information, corrupt existing memory, or introduce unsupported hallucinated content. Once stored, such errors become persistent system-state failures that can affect future reasoning and generation. In this paper, we propose TrustMem, a framework designed to improve the trustworthiness of memory consolidation. TrustMem relies on a Memory Transition Verifier to evaluate the transition process of memory updates in terms of coverage, preservation, and faithfulness. It further constructs preference pairs among candidate updates under the same memory state, enabling preference-guided reinforcement learning to directly optimize memory updating behaviors. Extensive experiments demonstrate that TrustMem improves both memory utility and reliability: it achieves state-of-the-art results across MemoryAgentBench, HaluMem, and the Mem-alpha validation set, improves HaluMem memory extraction by 12.14 F1 points, and reduces transition-level omission, corruption, and hallucination by 40.1\%, 79.1\%, and 50.0\%, respectively, compared with the strongest baseline for each error type.

</details>


### 83. The Clinician's Veto: Navigating Trust, Liability, and Uncertainty in Autonomous AI Prescribing

- **Authors:** Eileanor LaRocco, Sarah Tan, Adarsh Subbaswamy, Anne Andrews, Andrew Taylor, Cree Gaskin, Chirag Agarwal
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25108v1](http://arxiv.org/abs/2606.25108v1)
- **PDF:** [https://arxiv.org/pdf/2606.25108v1](https://arxiv.org/pdf/2606.25108v1)
- **Categories:** cs.AI, cs.HC


> The paper argues that safe autonomous AI prescribing must embed three architectural safeguards—calibrated per‑prediction confidence thresholds, explicit distinction between epistemic and aleatoric uncertainty, and real‑time inferential transparency for liability attribution—and demonstrates through a survey of 136 U.S. clinicians that these features are essential for clinician acceptance. Using a mixed regulatory‑technical analysis, the authors show that clinicians will only endorse autonomous prescribing if the system escalates decisions based on calibrated confidence, presents alternative options when uncertainty is aleatoric, abstains when uncertainty is epistemic, and provides transparent reasoning to support liability sharing. Implementing these requirements transforms the AI from a fully autonomous agent into a tightly supervised decision‑support tool, a design the authors contend should be codified in emerging legislation and pilot programs.


<details>
<summary>Abstract</summary>

Autonomous AI systems are transitioning from advisory to autonomous roles for medication prescriptions. Recent United States bill H.R. 238 and Utah's prescription-renewal pilot both authorize AI to prescribe medications in an agentic capacity. While some regulatory guidelines suggest aggregate model performance metrics for clearance, they do not require i) calibrated per-prediction confidence for action-gated thresholds, ii) differentiated communication of uncertainty arising from model ignorance (epistemic) versus genuine clinical ambiguity (aleatoric), and iii) inferential transparency at the moment of decision that allows for liability allocation. Here, we present a regulatory and technical argument (tested with a survey of 136 U.S. prescribing clinicians) positioning these as minimum architectural requirements for safe autonomous prescribing. Our results suggest prescribing clinicians i) would not permit autonomous prescribing without a calibrated confidence-based escalation mechanism, ii) preferred a competing-options summary when uncertainty was aleatoric but shifted to abstention when uncertainty was epistemic, and iii) were only willing to accept additional liability when inferential transparency enabled a substantive judgment under acknowledged uncertainty. These findings indicate our recommended architectural features would encourage higher rates of clinician adoption, largely through collapsing much of what "autonomy" conventionally means. A system meeting these requirements would function less as an autonomous agent and more as a heavily supervised decision-support tool. As legislation and state pilots proceed, our technical argument backed by clinician perspectives provides opportunities for regulation to constrain the degree of autonomy ethically granted to AI in prescribing while aligning liability with the institutional actors who control system design and deployment.

</details>


### 84. GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Animesh Animesh, Satheesh K Perepu, Kaushik Dey
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.25073v1](http://arxiv.org/abs/2606.25073v1)
- **PDF:** [https://arxiv.org/pdf/2606.25073v1](https://arxiv.org/pdf/2606.25073v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces **GCT‑MARL**, a transfer‑learning framework for cooperative multi‑agent reinforcement learning that extends the multi‑view graph‑contrastive encoder of MAIL with an adaptively weighted per‑view alignment loss and a two‑phase training protocol designed to handle populations of different sizes and compositions. By first fine‑tuning the contrastive encoder on the source domain and then jointly optimizing the policy on the target domain, GCT‑MARL achieves markedly faster convergence than training from scratch on both homogeneous (same‑faction, varying N) and heterogeneous (cross‑faction, mixed unit‑type) scenarios, and it can be chained sequentially to support continual learning across a series of related tasks. Empirical results on standard MARL benchmarks demonstrate substantial sample‑efficiency gains and robust performance transfer across varied agent populations, offering a unified, scalable solution to the sample‑inefficiency of current MARL transfer methods.


<details>
<summary>Abstract</summary>

In cooperative multi-agent reinforcement learning (MARL), from a deployment perspective, it is challenging and expensive to train agents from scratch for each new environment or task. In this work, we propose GCT-MARL, a transfer learning framework that builds on the multi-view graph contrastive backbone of MAIL and augments it with a per-view, adaptively weighted alignment loss and a two-phase training protocol specifically designed for transfer across populations of varying sizes and compositions. We empirically demonstrate that the proposed framework markedly accelerates convergence on the target task relative to from-scratch training, in both homogeneous (within-faction, varying N) and heterogeneous (cross-faction and mixed unit-type) transfer scenarios. Furthermore, we show that the framework naturally supports continual learning by sequentially chaining the two-phase transfer protocol across a series of related tasks. Overall, this work provides a unified approach to mitigating key limitations in current MARL transfer methods with new insights at both methodological and empirical levels.

</details>


### 85. Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System

- **Authors:** Tian Zheng, Kai-Tai Hsu
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24839v1](http://arxiv.org/abs/2606.24839v1)
- **PDF:** [https://arxiv.org/pdf/2606.24839v1](https://arxiv.org/pdf/2606.24839v1)
- **Categories:** cs.AI, stat.AP


> The paper introduces a three‑stage human‑AI grading cascade for evaluating LAMBDA, a multi‑agent data‑analysis system that outputs code, numbers, and prose. By combining strict regex checks, a lenient LLM‑based grader, and targeted human snippet reviews, the authors achieve perfect precision (0 % false positives) and high recall (97 % for the lenient grader), showing that a keyword‑anchored extraction pipeline and an iterative “nudge” prompt dramatically improve grading success. Their analysis also finds that the type of variable involved in a task most strongly predicts grading difficulty, offering practical guidance for building reliable evaluators of agentic AI outputs.


<details>
<summary>Abstract</summary>

Agentic data analysis systems produce rich outputs, including code, numerical results, and verbal diagnostics. This makes them more challenging to evaluate than single-turn LLM responses. It is therefore necessary to distinguish genuine disagreement between an agent's output and a ground-truth answer from grading artifacts. We investigate how reliably automated graders assess such a system and what strategies improve grading quality by applying LAMBDA, a multi-agent data-analysis system, on 153 numerical QRData tasks from DSGym. We develop and evaluate a three-layer human-AI grading cascade: strict regex matching, LLM-based lenient grading, and snippet-based human inspection, which combines non-GenAI and GenAI strategies with different failure profiles. Both automated graders achieve 100% observed precision (0/70 false positives). The lenient grader's recall is 97% against human labels. A keyword-anchored extraction pipeline raises the strict grader's recall by 60 percentage points over a last-number heuristic; the lenient grader is architecturally parser-independent. An iterative nudge mechanism raises grading run success from 36% to 97% and lenient-pass rates from 16% to 46%; comparing nudging with and without original-question re-injection shows that re-injection offers no benefit, confirming the nudge as an answer template cue. We further observe in this case study that variable type is the task metadata field most consistently associated with grading pipeline dynamics and observed outcome grades.

</details>


### 86. SHERLOC: Structured Diagnostic Localization for Code Repair Agents

- **Authors:** Hovhannes Tamoyan, Sean Narenthiran, Erik Arakelyan, Mira Mezini, Boris Ginsburg
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24820v1](http://arxiv.org/abs/2606.24820v1)
- **PDF:** [https://arxiv.org/pdf/2606.24820v1](https://arxiv.org/pdf/2606.24820v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **SHERLOC**, a training‑free, reasoning‑driven framework that transforms a large language model (LLM) into an efficient fault‑localization component for code‑repair agents, delivering precise, diagnostically rich locations rather than mere file retrievals.

**Methodology:** SHERLOC couples a reasoning LLM with lightweight repository‑access tools (search, grep, call‑graph inspection) in a hypothesis‑testing loop that iteratively refines fault hypotheses, performs self‑recovery when tools fail, and returns structured “what, where, why” diagnostics—all without any finetuning or multi‑agent coordination.

**Key findings for agentic AI:** Across multiple scales, SHERLOC attains state‑of‑the‑art localization (84.33 % @1 on SWE‑Bench Lite, 81.27 % recall @1 on SWE‑Bench Verified) and, when its outputs are fed to existing repair agents, boosts overall resolve rates by ~6 percentage points while cutting localization token usage by ~37 % and total agent tokens by ~23 %. This demonstrates that a compact, reasoning‑centered localization front‑end can markedly improve the effectiveness and efficiency of downstream code‑repair agents.


<details>
<summary>Abstract</summary>

LLM agents solve repository-level coding tasks through multi-turn tool use, but utilize half their budget on locating faults before editing. Dedicated localization frameworks have emerged, yet are still evaluated as file retrieval rather than actionable diagnosis, producing locations without the diagnostic context a repair agent needs. We introduce SHERLOC (Structured Hypothesis-driven Exploration and Reasoning for Localization), a training-free framework pairing a reasoning LLM with compact repository tools and self-recovery, without fine-tuning or multi-agent orchestration. SHERLOC reaches state-of-the-art localization across model scales: 84.33% accuracy@1 on SWE-Bench Lite and 81.27% recall@1 on SWE-Bench Verified; at ~30B parameters, it matches or outperforms other agentic methods. Injecting our locations and diagnostic findings into repair agents yields, on average, +5.95 pp resolve rate on SWE-Bench Verified while cutting localization and total tokens by 36.7% and 23.1%.

</details>


### 87. Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce

- **Authors:** Filippos Ventirozos, Matthew Shardlow
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24783v1](http://arxiv.org/abs/2606.24783v1)
- **PDF:** [https://arxiv.org/pdf/2606.24783v1](https://arxiv.org/pdf/2606.24783v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper proposes a new paradigm for agent‑driven e‑commerce in which autonomous buyer agents purchase verified product data via fine‑grained micro‑transactions, turning “information” into the scarce resource rather than product matching.  

**Methodology:** It outlines a market architecture that leverages emerging agent‑native payment rails (e.g., x402, AP2) and a freemium pricing model, where sellers and third‑party reviewers expose data (service histories, test reports, BOMs, audited metrics) a la carte and buyers negotiate cost‑optimal acquisition using reputation‑based trust scores. The authors then map this vision onto concrete NLP challenges—optimal information‑acquisition planning, dynamic data pricing/negotiation, real‑time entity resolution, grounded value exchange, and privacy‑preserving persona modeling.  

**Key findings:** By shifting focus from ranking‑based recommendation to verified information exchange, the model incentivizes genuine product quality, creates a more transparent competition arena, and redirects research priorities in the agentic AI field toward economically‑aware language understanding and negotiation rather than mere conversational fluency.


<details>
<summary>Abstract</summary>

Commercial NLP treats the shopping chatbot as a recommender or a conversion tool: its job is to match a user to a catalogue entry and close a sale. We argue that the arrival of agent-native micro-payment rails (e.g., x402, AP2) changes what is scarce. When the buyer is an autonomous agent that can investigate exhaustively, the bottleneck is no longer matching products but acquiring trustworthy, decision-relevant information about them. We envision agentic e-commerce as a micro-transaction market for verified information: buyer agents spend fractions of a cent to progressively unlock seller- and reviewer-supplied data -- service histories, third-party test reports, bills of materials, audited sales and support metrics -- paid for a la carte under a freemium model, with reviewer trust scored reputationally. We sketch the architecture of such a market and argue that it rewards genuine product quality and yields truer competition than ranking-based storefronts. We then translate the vision into concrete NLP problems -- cost-optimal information acquisition, data pricing and negotiation, real-time entity resolution, grounded value exchange, and privacy-preserving persona modelling -- and argue that these, not chat fluency, deserve the field's attention.

</details>


### 88. SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation

- **Authors:** Chenyang Zhu, Jiayu Yao, Kushal Chawla, Youbing Yin, Nathan Wolfe, Pengshan Cai, Jingyu Wu, Spencer Hong, Sangwoo Cho, Shi-Xiong Zhang, Daben Liu, Sambit Sahu, Erin Babinsky
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24626v1](http://arxiv.org/abs/2606.24626v1)
- **PDF:** [https://arxiv.org/pdf/2606.24626v1](https://arxiv.org/pdf/2606.24626v1)
- **Categories:** cs.AI


> The paper introduces **SAFARI**, a tool‑augmented diagnostic framework that lets a large language model iteratively fetch, search, and reason over selected slices of an agent’s execution trace while storing intermediate conclusions in a persistent short‑term memory, thereby breaking the dependency on a single, fixed‑size context window. By coupling this active‑investigation loop with specialized read/search primitives, SAFARI can attribute faults in trajectories that far exceed the model’s native window and achieve substantially higher diagnostic performance—≈20 % absolute gain on the Who&When benchmark (1 M‑token budget) and ≈19 % on the TRAIL GAIA subset (25 K‑token budget), maintaining a precision of 0.58 even when the relevant fault lies five times beyond the context limit. These results demonstrate a scalable approach for long‑horizon agentic fault attribution that can be integrated with existing LLM‑based agents.


<details>
<summary>Abstract</summary>

As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows. Current methods for effectively diagnosing agent failures load the full trajectory into an LLM's context window, which suffers from attention dilution and fails when agentic traces inevitably exceed context limits. To address this, we introduce SAFARI (Scaling long-horizon Agentic Fault AttRibution via active Investigation), a framework that replaces linear context loading with a tool-augmented diagnostic loop. By equipping LLMs with a specialized toolbox to read and search trajectory segments alongside a persistent Short-Term Memory (STM) for cross-turn reasoning, SAFARI effectively decouples diagnostic accuracy from architectural context limits. Our experiments demonstrate that SAFARI outperforms state-of-the-art results by 20% on the Who&When dataset within a 1M token budget, and by 19% on TRAIL GAIA subset on a 25K token budget. Most significantly, SAFARI maintains a 0.58 precision even when the target fault resides 5x beyond the model's native context window, a scenario where traditional evaluators fail entirely.

</details>


### 89. Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality Without Compromising Contextual Fidelity

- **Authors:** Yuanhe Zhao, Tianyu Zhang, Huafei Xing, Derek F. Wong, Jianbin Li, Tao Fang
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24623v1](http://arxiv.org/abs/2606.24623v1)
- **PDF:** [https://arxiv.org/pdf/2606.24623v1](https://arxiv.org/pdf/2606.24623v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces a **multi‑agent semantic rewriting framework** that sanitizes the documents retrieved for Retrieval‑Augmented Generation (RAG) so that downstream LLMs can be used in privacy‑sensitive contexts without leaking personal identifiers. The system orchestrates three specialized agents—(1) a privacy‑extraction agent that detects and extracts PII, (2) a semantic‑analysis agent that builds a representation of the content’s meaning, and (3) a reconstruction agent that rewrites the text to remove the identified PII while preserving its semantic core. Experiments on the ChatDoctor and Wiki‑PII benchmarks across six LLMs show that the approach cuts targeted privacy leaks dramatically (e.g., from 144 to 1 exposures for LLaMA‑3‑8B) and retains higher contextual fidelity than the prior SAGE method (BLEU‑1 0.122 vs 0.117) without adding inference latency, making it a practical privacy‑preserving preprocessing step for agentic AI systems.


<details>
<summary>Abstract</summary>

Retrieval-Augmented Generation enhances large language models by incorporating external knowledge, but deploying it in sensitive scenarios risks privacy leakage via malicious prompts. To address this, we propose a multi-agent framework that sanitizes retrieved content through semantic rewriting. By employing three specialized agents for privacy extraction, semantic analysis, and reconstruction, our approach collaboratively removes sensitive identifiers while preserving the semantic core. We evaluate the framework on the ChatDoctor and Wiki-PII datasets across six large language models. Experimental results demonstrate a significant reduction in privacy leakage under targeted attacks. For instance, we reduced targeted information exposure in LLaMA-3-8B from 144 instances in the baseline to just 1. Furthermore, we maintain strong contextual fidelity with a BLEU-1 score of 0.122, outperforming the existing SAGE method's 0.117. Finally, the framework operates as an asynchronous preprocessing module, introducing no additional latency to online inference, as all rewriting is executed as a one-time offline preprocessing step. To promote reproducibility, the source code of this work is publicly available at https://github.com/foursoils/Privacy-Preserving-RAG.

</details>


### 90. ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning

- **Authors:** Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar, Kaushik Dey
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24601v1](http://arxiv.org/abs/2606.24601v1)
- **PDF:** [https://arxiv.org/pdf/2606.24601v1](https://arxiv.org/pdf/2606.24601v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **ASALT (Adaptive State Alignment for Lateral Transfer)**, a MARL transfer method that works even when source and target domains have different observation‑ and global‑state dimensionalities. ASALT learns separate observation‑level and state‑level adapters that embed target‑domain observations and global states into a common latent space, allowing both actor and critic networks to reuse knowledge across heterogeneous environments. Experiments on standard cooperative benchmarks show that ASALT achieves higher sample efficiency and final returns than prior transfer baselines and markedly reduces negative transfer, with its benefits scaling with the degree of state‑space mismatch.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) addresses the problem of training multiple agents that pursue collaborative, competitive, or mixed objectives. Prior work has investigated transfer learning between source and target domains in MARL; however, the majority of existing approaches impose the constraint that the dimensionalities of the observation space and the global state space must be identical across domains. In this paper, we introduce a method that explicitly accommodates mismatched state-space dimensionalities between source and target domains. The proposed approach, ASALT, incorporates both observation-level and state-level adapters that map the target-domain observations and global states into a shared embedding space, thereby enabling more effective transfer of knowledge across both actors and critics. These adapters can generate embeddings that support efficient strategy transfer across heterogeneous domains. Experimental results on multiple configurations in standard benchmark environments demonstrate that ASALT surpasses existing baselines in terms of sample efficiency and global return in cooperative settings, but its effectiveness depends on the degree of mismatch between source and target domains. Furthermore, our findings indicate that ASALT mitigates negative transfer, which frequently constitutes a major obstacle when transferring policies between domains with differing observation and action spaces.

</details>


### 91. MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

- **Authors:** Enze Ma, Yufan Zhou, Wei-Chieh Huang, Jie Yang, Huanhuan Ma, Zixuan Wang, Chengze Li, Chunyu Miao, Philip S. Yu, Zhen Wang
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24595v1](http://arxiv.org/abs/2606.24595v1)
- **PDF:** [https://arxiv.org/pdf/2606.24595v1](https://arxiv.org/pdf/2606.24595v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **MEMPROBE**, the first benchmark that directly audits an LLM‑agent’s long‑term memory by measuring how accurately the agent’s stored representation can reconstruct a hidden, taxonomy‑based user state after a multi‑turn interaction.

**Methodology:** Simulated users possess a ground‑truth “user‑state bank” with 31 latent attributes (1,550 recovery targets across 50 users). Agents equipped with different memory modules (full‑store vs. top‑k retrieval) assist the users on a sequence of controlled tasks, after which the benchmark attempts to recover the hidden state from the agent’s memory and compares it to the ground truth.

**Key findings:** Even memory‑less agents achieve near‑perfect task completion, but their ability to recover the user state is modest (≈0.6 category‑balanced recovery) and degrades further under top‑k retrieval. This gap shows that successful assistance does not guarantee faithful long‑term memorization, highlighting memory reconstruction as a distinct objective for future agentic AI systems.


<details>
<summary>Abstract</summary>

Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which tests that understanding only indirectly and leaves the memory artifact itself largely unaudited. We argue that long-term memory should instead be evaluated as an auditable post-interaction artifact: after ordinary assistance, what structured user state can be reconstructed from the memory the agent leaves behind? We instantiate this view in MEMPROBE, a benchmark in which a memory-equipped agent assists simulated users, each carrying a hidden, taxonomy-anchored user-state bank, across a trajectory of leak-controlled tasks, after which that bank is reconstructed from the agent's resulting memory under both full-store and top-k access. Built on synthetic ground truth for efficient, scalable measurement, MEMPROBE spans 50 simulated users with 31 hidden dimensions each (1,550 recovery targets) and tests 5 representative memory systems. Testing state-of-the-art memory agents, we find that successful assistance and recoverable memory behave as distinct capabilities. Task completion nearly saturates, even for a memoryless baseline, while category-balanced recovery stays moderate (about 0.6) and drops further under top-k retrieval. MEMPROBE is the first benchmark to study memory recovery directly, reconstructing the user state a system retains and scoring it against ground truth. We see recovery as a concrete objective for future memory agents to optimize, and MEMPROBE as a step toward an environment where agents are trained to remember their users, growing more faithful the longer they know them.

</details>


### 92. AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability

- **Authors:** Khanak Khandelwal
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24589v1](http://arxiv.org/abs/2606.24589v1)
- **PDF:** [https://arxiv.org/pdf/2606.24589v1](https://arxiv.org/pdf/2606.24589v1)
- **Categories:** cs.AI, cs.CL


> AdversaBench introduces an automated red‑teaming framework that mutates a small set of seed prompts using five structured operators, queries a target LLM, and validates failures via a three‑judge panel with a meta‑judge tiebreaker. Experiments on 45 seeds spanning reasoning, instruction‑following, and tool‑use show that every seed leads to a confirmed failure, with operator efficacy differing by task type and instruction‑following prompts requiring markedly more attacker iterations; moreover, adversarial prompts crafted against Llama 3.1 8B transfer zero‑shot to a much larger Llama 3.3 70B, indicating that the mutations exploit broadly shared model behaviors. These results provide a scalable, reproducible pipeline for generating hard evaluation cases and demonstrate that adversarial vulnerabilities can generalize across model scales, informing future safety testing of agentic AI systems.


<details>
<summary>Abstract</summary>

Scaling adversarial evaluation of large language models requires both a method for generating hard inputs and a reliable way to confirm that resulting failures are real. We present AdversaBench, an end-to-end red-teaming pipeline that mutates seed prompts with five structured operators, queries a target model, and confirms failures through a three-judge panel with a meta-judge tiebreaker. We report experiments on 45 seeds across three categories: reasoning, instruction-following, and tool use. Every seed produced a confirmed failure. Four findings stand out. First, operator effectiveness varies sharply by category: inject_distractor scores 0.00 mean reward on instruction-following seeds but 0.80-0.83 on reasoning and tool-use. Second, binary failure rate hides difficulty: instruction-following seeds required 2.4 attacker iterations on average versus 1.1 for other categories, a gap visible in survival curves. Third, pairwise judge agreement of 80-87% coexists with near-zero Cohen's kappa due to label skew; category-level disagreement rates are more informative. Fourth, adversarial prompts generated against Llama 3.1 8B transfer zero-shot to Llama 3.3 70B, suggesting the mutations exploit general behavioral patterns rather than model-specific weaknesses. Code, dataset, and analysis scripts are available at https://github.com/khanak0509/AdversaBench .

</details>


### 93. Governed Shared Memory for Multi-Agent LLM Systems

- **Authors:** Yanki Margalit, Nurit Cohen-Inger, Erni Avram, Ran Taig, Oded Margalit
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24535v1](http://arxiv.org/abs/2606.24535v1)
- **PDF:** [https://arxiv.org/pdf/2606.24535v1](https://arxiv.org/pdf/2606.24535v1)
- **Categories:** cs.AI


> The paper introduces **MemClaw**, a production‑grade shared‑memory service that equips multi‑agent LLM fleets with explicit governance primitives—scoped retrieval, temporal supersession, provenance tracking, and policy‑driven propagation—to solve the “fleet‑memory” problem of leakage, staleness, contradictions, and loss of provenance. Using the ArgusFleet benchmark harness, the authors demonstrate that MemClaw can reconstruct 100 % of four‑step derivation chains with correct author identities at sub‑second latency, enforce strict intra‑fleet visibility without cross‑fleet leakage, and achieve single‑round‑trip write‑to‑visibility under strong write modes, while also uncovering real‑world implementation bugs (asymmetric scope enforcement and pipeline ordering conflicts) that only live production testing revealed. These results show that merely scaling long‑context retrieval is insufficient; robust, system‑level memory abstractions are essential for reliable, governed shared knowledge in agentic AI deployments.


<details>
<summary>Abstract</summary>

Multi-agent LLM environments require robust mechanisms for shared knowledge management. This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse. To address these, we define explicit systems-level primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation. These primitives are implemented in MemClaw, a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions. Rather than a baseline comparison, this study measures a live production service, emphasizing real-world architectural insights and negative results. Key Evaluation Results Provenance: Successfully reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency. Propagation: Demonstrated high intra-fleet visibility with zero cross-fleet leakage. Under strong write mode, write-to-visible latency was optimized to a single search round-trip. Production Architectural Issues Discovered Asymmetric Scope Enforcement: Tenant isolation held, but sub-tenant scope was initially bypassed on direct GET-by-id requests for agent-scoped credentials (disclosed and remediated during the study). Pipeline Ordering Conflict: While contradiction supersession works for admitted writes, a synchronous near-duplicate gate can prematurely reject contradictory writes before the asynchronous contradiction detector can evaluate them. Conclusion: Long-context retrieval alone is insufficient for production multi-agent memory. Governed shared memory demands explicit systems-level abstractions, and live evaluation is vital to expose enforcement and pipeline-ordering failures missed by design-only treatments.

</details>


### 94. Diagnosing and Mitigating Compounding Failures in Agentic Persuasion via Taxonomic Strategy Retrieval

- **Authors:** Pradyumna Narayana, Sana Ayromlou, Purvi Sehgal
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24976v1](http://arxiv.org/abs/2606.24976v1)
- **PDF:** [https://arxiv.org/pdf/2606.24976v1](https://arxiv.org/pdf/2606.24976v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper uncovers that standard Retrieval‑Augmented Generation (RAG) causes “semantic leakage” in multi‑step persuasion tasks, letting early lexical matches dominate reasoning and leading to compounding errors and sycophantic behavior. To fix this, the authors propose Taxonomic Strategy RAG (TS‑RAG), which forces retrieved persuasion strategies through a discrete categorical bottleneck that separates argumentative structure from surface content; they evaluate it with a turn‑by‑turn Debate State Representation (DSR) diagnostic and show that TS‑RAG lifts win rates of lightweight persuaders from 70.5 % to 78.5 % and improves logical transfer across domains. The work demonstrates a concrete systems intervention for more robust, non‑drifting agentic persuasion and provides trace‑level tools for detecting and preventing such failures.


<details>
<summary>Abstract</summary>

Foundation-model agents in multi-step, open-ended environments frequently suffer from compounding errors, where early mistakes contaminate long-horizon trajectories. While Multi-Agent Debate (MAD) succeeds in deterministic domains, agents in subjective tasks like persuasion experience severe problem drift and sycophantic conformity. We identify semantic leakage in standard Retrieval-Augmented Generation (RAG) as a reproducible trigger for these failures, as standard RAG prioritizes vocabulary overlap over logical necessity.
  To eliminate this leakage, we introduce Taxonomic Strategy RAG (TS-RAG), a systems intervention that routes strategies through a discrete categorical bottleneck to decouple argumentative structure from topical content. Zero-shot, cross-domain evaluations demonstrate that TS-RAG significantly improves the transfer of abstract logic where standard semantic retrieval collapses. Crucially, TS-RAG acts as a "capability bridge" in asymmetric deployments, empowering lightweight persuaders to consistently defeat parametrically superior opponents (improving win rates from 70.5 to 78.5) and accelerating argumentative efficiency. Finally, we introduce trace-level diagnostics via a turn-by-turn Debate State Representation (DSR), demonstrating the necessity of strict constraints to prevent evaluation collapse via default agentic sycophancy.

</details>


### 95. Bayesian control for coding agents

- **Authors:** Theodore Papamarkou, Vladislav Smirnov, Viktor Mazanov, Artem Vazhentsev, Preslav Nakov, Timothy Baldwin, Artem Shelmanov
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24453v1](http://arxiv.org/abs/2606.24453v1)
- **PDF:** [https://arxiv.org/pdf/2606.24453v1](https://arxiv.org/pdf/2606.24453v1)
- **Categories:** cs.AI, cs.CL


> **Paper Summary**  
The authors introduce a Bayesian controller that orchestrates the tool‑use pipeline of coding agents as a cost‑sensitive sequential hypothesis‑testing problem. By maintaining a posterior belief over the correctness of a generated program, the controller dynamically decides whether to request cheap diagnostics, request additional refinement, invoke an expensive verifier, or accept the solution, thereby explicitly accounting for uncertainty and verification cost. Empirical results on six LLM generators across nine coding benchmarks show that this Bayesian control yields the best performance when verification is expensive and the available critics are informative yet imperfect, and the learned belief state provides a calibrated correctness score that surpasses traditional token‑probability and raw tool‑success baselines for uncertainty quantification.


<details>
<summary>Abstract</summary>

Modern coding agents pair LLM generators with various tools, including cheap diagnostics and expensive verifiers. The tool-use decisions are typically governed by orchestrators that often use fixed rules and ignore uncertainty. We formulate orchestration as cost-sensitive sequential hypothesis testing: a Bayesian controller maintains a belief over candidate correctness and dynamically decides whether to gather more evidence, refine the candidate, verify it, or stop. Across six generators and nine coding benchmarks, Bayesian control proves to be most valuable when verification is costly and critics are informative but imperfect. Beyond control, the belief state yields an interpretable correctness score that outperforms token-probability and raw tool-success baselines for uncertainty quantification.

</details>


### 96. ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling

- **Authors:** Heng Ping, Arijit Bhattacharjee, Peiyu Zhang, Shixuan Li, Wei Yang, Ali Jannesari, Nesreen Ahmed, Paul Bogdan
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24437v1](http://arxiv.org/abs/2606.24437v1)
- **PDF:** [https://arxiv.org/pdf/2606.24437v1](https://arxiv.org/pdf/2606.24437v1)
- **Categories:** cs.AI


> ReM-MoA introduces a memory‑augmented mixture‑of‑agents (MoA) architecture that preserves the scaling benefits of deeper reasoning pipelines by (1) maintaining a **Ranked Reasoning Memory**—a persistent store of all agents’ reasoning traces that a dedicated Reviewer Agent continually ranks, and (2) applying **Curated Diversified Memory Routing** to feed each subsequent agent a curated mix of high‑quality and exploratory traces, thereby keeping diversity while propagating successful reasoning. The system can also be enhanced with a multi‑domain Reviewer distillation step that leverages stronger frontier models to improve trace ranking. Experiments on five diverse reasoning benchmarks (math, formal logic, code, knowledge, commonsense) show that ReM-MoA consistently outperforms existing MoA variants, with performance gains increasing as the depth of the agent stack grows, highlighting cross‑layer reasoning memory as a crucial component for scalable agentic AI inference.


<details>
<summary>Abstract</summary>

Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines. However, existing MoA variants fail to sustain gains as depth increases, exhibiting degradation, early plateauing, or saturation. We propose ReM-MoA, a memory-augmented MoA framework that sustains scaling through two mechanisms: (1) a Ranked Reasoning Memory that persistently stores and ranks reasoning traces from all layers using a comparative Reviewer Agent, and (2) a Curated Diversified Memory Routing scheme that exposes different agents to distinct combinations of successful and failed traces, preserving exploration diversity while propagating high-quality reasoning. We further introduce an optional multi-domain Reviewer distillation pipeline that improves ranking quality through frontier-model supervision. Across five reasoning benchmarks spanning math, formal logic, code, knowledge, and commonsense, ReM-MoA consistently outperforms prior MoA variants across both depth and width scaling, and its advantage widens with depth, establishing structured cross-layer reasoning memory as a key missing mechanism for scalable multi-agent inference.

</details>


### 97. Agentic AI for Bilevel Long-Term Optimization of Policy-Driven Physical Layer Systems

- **Authors:** Bingnan Xiao, Chenhao Yang, Wei Ni, Xin Wang, Tony Q. S. Quek
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24416v1](http://arxiv.org/abs/2606.24416v1)
- **PDF:** [https://arxiv.org/pdf/2606.24416v1](https://arxiv.org/pdf/2606.24416v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Agentic‑LTPO**, a novel bilevel optimization framework that uses an *agentic AI* module to translate evolving network‑operator policies, environment summaries, and past experiences into dynamic configurations for lower‑level physical‑layer optimizers, thereby enabling long‑term, policy‑driven adaptation of wireless systems.  

**Methodology:** A two‑level structure is built: the upper level runs a multi‑agent decision process augmented with retrieval‑based experience verification to generate problem parameters (constraints, objectives) for the lower level; the lower level solves a closed‑form cell‑free MIMO beamforming problem in real time. The agents are trained using reinforcement learning with a memory bank of historical configurations and policy embeddings.  

**Key findings:** In a cell‑free MIMO beamforming scenario, Agentic‑LTPO adapts to changing operator policies and outperforms conventional fixed‑objective methods, achieving a **57.2 % improvement in long‑term system performance** while meeting real‑time constraints, demonstrating the viability of agentic AI for adaptive, policy‑driven physical‑layer optimization.


<details>
<summary>Abstract</summary>

Network operators' changing policies, service requirements, and stringent real-time constraints render existing methods designed with fixed objectives and constraints ineffective. This paper presents Agentic long-term performance optimization (Agentic-LTPO), a nested bilevel optimization framework that can be applied to adaptive physical layer problem configuration. The key idea is to employ agentic AI to generate upper-level configurations in a bilevel optimization structure, where evolving operator policies, environment summaries, and historical experiences are translated into structured lower-level optimization problem configurations. The lower level solves the problems with updated configurations for real-time physical-layer decisions. Considering cell-free MIMO beamforming as a use case, we embody Agentic-LTPO by designing a new multi-agent decision process with retrieval-augmented experience-based verification in the upper level, together with a closed-form beamformer in the lower level. Experiments demonstrate that Agentic-LTPO exhibits strong adaptability to dynamic operator policies and effectively enhances the system's long-term performance by 57.2% compared to traditional methods.

</details>


### 98. ATRIA: Adaptive Traceable ECG Reporting with Iterative Agents

- **Authors:** Donggyun Hong, Kyuhwan Lee, Junmyung Kwon, Yong-Yeon Jo
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24392v1](http://arxiv.org/abs/2606.24392v1)
- **PDF:** [https://arxiv.org/pdf/2606.24392v1](https://arxiv.org/pdf/2606.24392v1)
- **Categories:** cs.AI


> The paper introduces **ATRIA**, a multi‑agent system for electrocardiogram (ECG) reporting that emulates the clinician’s iterative workflow rather than producing a single, monolithic output. By coupling trusted ECG analysis models with a set of cooperative agents, ATRIA binds each textual claim to its underlying signal evidence, flags unsupported statements, and permits bidirectional, mid‑session edits that integrate new context and allow clinicians to verify or revise individual findings. Evaluation across four realistic interaction scenarios shows that this traceable, iterative architecture improves error traceability and user control, offering a deployable cloud service that can be adopted immediately in clinical AI pipelines.


<details>
<summary>Abstract</summary>

Existing ECG report generation is tightly coupled -- interpretation and reporting fused end-to-end, so errors propagate without stage-level recourse -- while agent-based systems decouple tasks but remain single-pass, never revisiting earlier outputs. Clinical ECG reporting instead unfolds iteratively, requiring progressive context integration and bidirectional editing. We present \textsc{ATRIA}, a multi-agent ECG reporting system that mirrors the clinician's iterative workflow: it binds every report claim to its supporting evidence, flags statements unsupported by that evidence, incorporates additional context mid-session, and lets clinicians verify and revise individual findings rather than accept one opaque output. Because its agents use ECG analysis models already in clinical use, the underlying findings are clinically trustworthy; and as a cloud-based web service, \textsc{ATRIA} is ready for immediate deployment. We demonstrate \textsc{ATRIA} through four interaction cases, with a live demo and video available.

</details>


### 99. When Helpfulness Overrides Causal Caution: Context-Dependent Suppression and Recovery in LLMs

- **Authors:** Hiroshi Okumura
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24370v1](http://arxiv.org/abs/2606.24370v1)
- **PDF:** [https://arxiv.org/pdf/2606.24370v1](https://arxiv.org/pdf/2606.24370v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly integrated into decision-support roles in business and policy contexts. While prior benchmark studies have primarily evaluated LLMs' causal reasoning capabilities, a more fundamental epistemic dimension has been overlooked: Causal Caution, defined as the propensity to refrain from causal judgment when empirical evidence is insufficient. This study examines the systematic suppression of Causal Caution that occurs when LLMs shift from academic to practical advisory contexts. Using an evaluation rubric inspired by Pearl's Causal Hierarchy (the PCH score), we conducted experiments on four high-performance LLMs -- Claude Sonnet 4.6, Claude Opus 4.7, GPT 5.5, and Gemini 3.1 Pro -- across 480 trials. Causal Caution maintenance rates were 91.7--100.0% in academic contexts but dropped to 6.7--18.3% in practical advisory contexts (Fisher's exact test, p < .001 across all models). Furthermore, when restricted to practical prompts requesting concrete recommendations or explanatory rationales, only 1 of 200 responses (0.5%) maintained Causal Caution. A brief self-correction prompt -- "Please reconsider this judgment from the perspective of causal relationships" -- restored the expression of Causal Caution to maintenance rates of 71.4--100.0% (McNemar's test, p < .001 across all models). These results suggest that helpfulness-oriented response patterns may suppress the expression of Causal Caution in practical advisory contexts, with important implications for organizational governance. The findings indicate that this suppression reflects context-dependent variation in expression rather than an underlying capability limitation, suggesting that multi-agent architectures that separate proposal generation from causal auditing may offer a promising governance design.

</details>


### 100. Project Auto-World: Towards Automated Benchmarking of Neural Relational Reasoners

- **Authors:** Anirban Das, Joanne Boisson, Irtaza Khalid, Sumita Garai, Steven Schockaert
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24965v1](http://arxiv.org/abs/2606.24965v1)
- **PDF:** [https://arxiv.org/pdf/2606.24965v1](https://arxiv.org/pdf/2606.24965v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper introduces *Project Auto‑World*, a framework that uses large language models (LLMs) as autonomous agents to automatically generate and evolve increasingly difficult benchmark instances for neural relational reasoning tasks, and to use those instances to improve the reasoning models themselves.  

**Methodology:** A world is defined by Datalog rules and evaluated by an Edge‑Transformer relational reasoner. The authors employ LLM‑driven evolutionary search (FunSearch) and a self‑prompting agentic loop to discover sampling functions that produce hard problem instances. The generated data are then fed back to fine‑tune the Edge‑Transformer, and the same pipeline is applied to entirely new worlds generated by the LLM.  

**Key findings:** The LLM‑guided search reliably discovers benchmarks that stress‑test and expose systematic generalization failures of the Edge‑Transformer. Training on these hard instances markedly improves the model’s robustness to out‑of‑distribution perturbations. Moreover, the approach can bootstrap new relational worlds without human design, demonstrating a path toward fully autonomous research cycles for agentic AI in relational reasoning.


<details>
<summary>Abstract</summary>

Reasoning about relational structures remains a significant challenge for neural models, particularly when they must systematically apply learned knowledge to problem instances that are harder than those seen in training. Progress is hampered by the difficulty of evaluating such generalization, since a priori, it is rarely clear what makes an instance hard. We study how this issue can be addressed by using large language models (LLMs) to automate benchmark generation, learning to produce increasingly challenging instances in an end-to-end manner. Concretely, given a world parametrized by Datalog rules, and an Edge Transformer as the reasoning evaluator, we use LLM-driven evolutionary search (based on FunSearch) and autonomous agentic search to discover sampling functions that yield hard problem instances. We also show that the Edge Transformer can be improved using this data such that it generalizes well to further data perturbations. Finally, we show that the same machinery can be applied to novel worlds proposed by LLMs, opening the door to autonomous research on neural relational reasoning.

</details>


### 101. AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming

- **Authors:** Pingchuan Ma, Zhaoyu Wang, Zimo Ji, Yuguang Zhou, Zhantong Xue, Zongjie Li, Shuai Wang, Xiaoqin Zhang
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24245v2](http://arxiv.org/abs/2606.24245v2)
- **PDF:** [https://arxiv.org/pdf/2606.24245v2](https://arxiv.org/pdf/2606.24245v2)
- **Categories:** cs.SE, cs.AI, cs.CR


> **Contribution:** AutoSpec introduces an automated pipeline for refining safety rules governing LLM‑driven agents, combining expert‑written rule templates with user‑provided safe/unsafe annotations to produce interpretable, high‑precision specifications.

**Methodology:** The system applies a counterexample‑guided inductive synthesis loop: it runs the current rule set on annotated traces, extracts false‑positive and false‑negative counterexamples, and uses inductive logic programming (ILP) to discover discriminative predicates. These predicates drive the generation of candidate rule edits, which are verified and the best revision is adopted; the process repeats until convergence.

**Key Findings:** Across 291 execution traces from code‑execution and embodied‑agent domains, AutoSpec raises rule F1 scores to 0.98 and 0.93, cuts false positives by up to 94 % while preserving recall, converges in 4‑5 iterations, and outperforms heuristic CEGS by up to 4.8× in F1. The resulting rules remain human‑readable and generalize to unseen scenarios, addressing the interpretability‑vs‑robustness trade‑off in agentic AI safety.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments. However, their autonomy poses significant safety risks: agents may execute destructive commands, leak sensitive data, or violate domain constraints. Existing safety approaches face a fundamental tradeoff: hand-crafted rules are interpretable but brittle, with overly conservative rules blocking safe operations (high false positives) while permissive rules miss unsafe behaviors (high false negatives). Neural classifiers lack the interpretability required for safety-critical deployments.
  We present AutoSpec, a framework that automatically evolves deployed expert-designed safety rules from user safe/unsafe annotations through counterexample-guided inductive synthesis (CEGIS) guided by inductive logic programming (ILP). Starting from the expert rules and a stream of annotated traces, AutoSpec iteratively evaluates rules, mines false-positive and false-negative counterexamples, uses ILP to learn which predicates discriminate them, generates candidate rule edits, and verifies candidates to select the best revision. The key insight is that ILP efficiently identifies predicates that appear frequently in false negatives but rarely in false positives (or vice versa), dramatically pruning the exponential search space of rule edits. This continues until convergence, producing interpretable rules that balance precision and recall.
  We evaluate AutoSpec on 291 execution traces spanning code execution and embodied agent domains. AutoSpec raises rule F1 to 0.98 and 0.93 across the two domains, achieving up to 94% false positive reduction while maintaining high recall, and converges within 4-5 iterations. The ILP-guided approach achieves up to 4.8x higher F1 than heuristic CEGIS. The learned rules are human-readable, auditable, and generalize to unseen scenarios.

</details>


### 102. SP-Mind: An Autonomous Reasoning Agent for Spatial Proteomics Analysis

- **Authors:** Yucheng Yuan, Yuanfeng Ji, Zhongxiao Li, Ruijiang Li
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24235v1](http://arxiv.org/abs/2606.24235v1)
- **PDF:** [https://arxiv.org/pdf/2606.24235v1](https://arxiv.org/pdf/2606.24235v1)
- **Categories:** cs.AI


> The paper introduces **SP‑Mind**, the first autonomous AI agent that can translate natural‑language questions into complete spatial‑proteomics analysis pipelines—from raw multiplexed imaging data to phenotype discovery—by chaining a curated set of domain‑specific computational tools without any task‑specific fine‑tuning. The authors evaluate the system on **SP‑Bench**, a new benchmark of 102 tasks across 18 categories covering a variety of tissue types, and demonstrate that SP‑Mind consistently outperforms existing open‑source biomedical agents on both benchmark metrics and downstream biological tasks. These results show that a skill‑augmented, tool‑using agent can reliably orchestrate complex, heterogeneous workflows in spatial proteomics, offering a scalable and reproducible solution for agentic AI applications in biomedical data analysis.


<details>
<summary>Abstract</summary>

Spatial proteomics enables single-cell-resolution characterization of protein expression within tissue architecture, playing a critical role in understanding tumor microenvironments and guiding precision medicine. However, current analysis workflows remain fragmented, requiring expert manual orchestration of heterogeneous tools and limiting research scalability and reproducibility. We present SP-Mind, the first autonomous AI agent designed to unify the spatial proteomics analysis pipeline, from raw multiplexed tissue imaging to downstream phenotype discovery. Equipped with expert-curated biological analysis skills and specialized computational tools, SP-Mind converts natural-language queries into end-to-end analytical workflows without task-specific fine-tuning. To rigorously evaluate its capabilities, we introduce SP-Bench, a comprehensive benchmark spanning diverse tissue types, comprising 102 tasks across 18 distinct categories. Through extensive evaluation on SP-Bench and established downstream tasks, SP-Mind achieves state-of-the-art performance compared to existing open-source biomedical agent baselines.

</details>


### 103. DramaDirector: Geometry-Guided Short Drama Generation

- **Authors:** Hengji Zhou, Sijie Liu, Jianrun Chen, Xingchen Zou, Lianghao Xia, Liqiang Nie
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24107v1](http://arxiv.org/abs/2606.24107v1)
- **PDF:** [https://arxiv.org/pdf/2606.24107v1](https://arxiv.org/pdf/2606.24107v1)
- **Categories:** cs.CV, cs.AI


> **Paper Summary**

DramaDirector introduces a geometry‑guided pipeline for generating short‑drama videos from a high‑level plot description. The system first plans each shot by retrieving real‑world short‑drama reference frames indexed by depth and pose, then decouples the shot into static visual conditions and dynamic narrative conditions; a planner is fine‑tuned with schema‑constrained supervised learning and GRPO reinforcement using a learned text‑visual alignment reward, and finally a text‑to‑image model creates the first frame which is extended to video via image‑to‑video synthesis. Evaluated on the newly released DramaBoard benchmark (35 dramas, 2.8 K episodes, 81 K shots), DramaDirector outperforms existing multi‑agent and text‑to‑video baselines in faithfulness to the plot, visual and narrative consistency, and controllability of cinematographic geometry, demonstrating the benefit of geometry‑based reference retrieval for agentic, story‑driven video generation.


<details>
<summary>Abstract</summary>

Short dramas, with their rapid shot rhythms, dialogue-driven focus shifts, and demanding cinematographic grounding, pose challenges that prompt-level or text-only video generation pipelines struggle to meet. We study plot-to-short-drama generation, where a global plot and local context are transformed into visually grounded multi-shot videos. We propose DramaDirector, a geometry-grounded framework that lets the planner borrow cinematographic geometry from a gallery of real short-drama shots indexed by depth and pose. DramaDirector decouples each shot into static visual and dynamic narrative conditions, trains the planner with schema-constrained SFT and GRPO under a learned text-visual alignment reward, and retrieves depth-pose references to guide first-frame generation and image-to-video synthesis. We also introduce DramaBoard, a benchmark built from 35 live-action dramas, 2.8K episodes, and 81K shots, with structured storyboards and multi-dimensional evaluation protocols. Experiments show that DramaDirector improves over representative multi-agent and video generation baselines on faithfulness, consistency, and controllability. Our code is released at: https://github.com/iLearn-Lab/DramaDirector

</details>


### 104. Beyond Bayer: Task-Optimal Sensor Co-Design for Robust Autonomous-Driving Segmentation

- **Authors:** Reeshad Khan, John Gauch
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24096v1](http://arxiv.org/abs/2606.24096v1)
- **PDF:** [https://arxiv.org/pdf/2606.24096v1](https://arxiv.org/pdf/2606.24096v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces a differentiable RAW‑to‑segmentation pipeline that jointly optimises camera sensor parameters and a dense‑prediction model, showing that learning the spectral colour‑filter‑array (CFA) weights is the single most effective sensor‑design lever for autonomous‑driving perception. By training the CFA jointly with the segmentation network, the authors achieve consistent mIoU gains of +0.017 on KITTI‑360 and +0.023 on ACDC across diverse weather conditions, while co‑optimising optics (PSF) or noise proves detrimental or negligible. Consequently, they propose a task‑optimal sensor design recipe—learn a 2×2 CFA and retain an identity PSF—that improves segmentation robustness in a model‑agnostic manner, highlighting the importance of upstream sensor co‑design for agentic AI systems.


<details>
<summary>Abstract</summary>

Robust perception underpins autonomous driving, and most recent progress comes from scaling the model-larger backbones, foundation models, and cooperative multi-agent fusion. We pursue a complementary, upstream question: what should the camera itself measure? Using a differentiable RAW-to-task pipeline, we decompose which sensor degrees of freedom benefit dense prediction. Learning the spectral colour-filter-array (CFA) weights is the dominant lever, improving mIoU by +0.017 (KITTI-360) and +0.023 (ACDC) over a fixed camera. In contrast, point-spread-function (optics) co-design is net-negative (-0.020 mIoU on KITTI-360) - a consequence of the data-processing inequality, which also bounds the task information that any downstream model, however large or cooperative, can recover. Noise co-optimisation is marginal, and counter to intuition enlarging the CFA tile beyond 2x2 consistently hurts, as the filters are confined to the rank three sRGB input. Because the intervention is at the sensor, the gains are model-agnostic; we validate robustness on ACDC's fog, night, rain, and snow, and conclude with a simple recipe: learn the 2x2 CFA weights and keep an identity PSF.

</details>


### 105. PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation

- **Authors:** Leyi Sheng, Han Sun, Zhen Sun, Yuntao Yue, Jinlin Wu, Xinlei He, Jiaheng Wei
- **Published:** 2026-06-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24081v1](http://arxiv.org/abs/2606.24081v1)
- **PDF:** [https://arxiv.org/pdf/2606.24081v1](https://arxiv.org/pdf/2606.24081v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **PixJail**, an autonomous agent framework that parses a text‑to‑image (T2I) jailbreak paper (and any accompanying code) and automatically generates a full, reproducible evaluation pipeline—including prompt transformation, image synthesis, safety filtering, and multimodal judging—under a common interface. By encoding each paper’s methodology as a modular “attack module” and storing digests, evolution patterns, and reusable templates in a versioned memory bank, PixJail can rapidly re‑implement and run past jailbreak experiments. In reproducing eleven representative T2I jailbreaks (both with and without released code), the system matches the original reported outcomes with a mean error of only 2.1 % (median 0 %), demonstrating that an agentic, self‑evolving approach can reliably standardize and streamline pipeline‑level evaluation in the emerging field of adversarial T2I systems.


<details>
<summary>Abstract</summary>

As Text-to-Image (T2I) jailbreak techniques evolve rapidly, existing benchmarks and reproduction workflows often struggle to keep pace. More importantly, T2I jailbreak evaluation is not a single prompt-level test, but a pipeline-level problem shaped by multiple stages, including prompt transformation, image generation, safety filtering, and multimodal judging. This makes results across papers difficult to reliably reproduce and fairly compare. To bridge this gap, we propose PixJail, a self-evolving paper-to-pipeline agent framework for reproducible T2I jailbreak evaluation. Given a T2I jailbreak paper and optional reference code, PixJail rapidly constructs a paper-specific attack module and a runnable evaluation pipeline under a unified contract, while faithfully reproducing the original experimental results. PixJail further maintains a memory bank that stores paper digests, attack evolution patterns, reusable templates, failure cases, and versioned artifacts, enabling future reproduction efforts to reuse prior experience. We reproduce eleven representative T2I jailbreak methods, including both code-available and code-unavailable papers. Under their original settings, our framework accurately recovers prior results with minimal error (2.1\% average, 0\% median). We hope that PixJail can serve as a unified foundation for future T2I jailbreak reproduction and evaluation, significantly reducing manual effort.

</details>


### 106. Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control

- **Authors:** Zihao Guo, Jianing Zhao, Ling Li, Hao Liang, Giuseppe Loianno, Yali Du
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24010v1](http://arxiv.org/abs/2606.24010v1)
- **PDF:** [https://arxiv.org/pdf/2606.24010v1](https://arxiv.org/pdf/2606.24010v1)
- **Categories:** cs.AI


> The paper introduces a hierarchical multi‑agent reinforcement‑learning (MARL) architecture that guarantees hard safety constraints by projecting low‑level actions onto a **constraint manifold** while a high‑level policy learns coordinated strategies.  By decoupling safety enforcement (via a control‑theoretic projection that yields provable, stationary learning dynamics) from task‑level optimization, the method combines the empirical strength of learning‑based MARL with formal safety guarantees.  Experiments show that the approach attains performance comparable to state‑of‑the‑art MARL methods, achieves almost 100 % safety compliance, and generalizes robustly across different numbers of agents and obstacle configurations.


<details>
<summary>Abstract</summary>

Multi-agent systems are widely used in safety-critical applications that require coordinated behavior under strict safety constraints. Existing approaches face a fundamental trade-off: learning-based methods achieve strong empirical performance but lack theoretical safety guarantees, while control-theoretic methods enforce safety but often lead to overly conservative and inefficient behaviors. We propose a hierarchical multi-agent reinforcement learning framework that enforces hard safety constraints under mild assumptions at low level via a constraint manifold, while enabling effective coordination through high-level policy learning. Our approach provides theoretical safety guarantees in the multi-agent setting and yields stationary learning dynamics, thereby enabling stable and efficient training. Empirically, our method achieves competitive performance while maintaining nearly perfect safety rates, and generalizes effectively to varying numbers of agents and obstacles.

</details>


### 107. Critique of Agent Model

- **Authors:** Eric Xing, Mingkai Deng, Jinyu Hou
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23991v1](http://arxiv.org/abs/2606.23991v1)
- **PDF:** [https://arxiv.org/pdf/2606.23991v1](https://arxiv.org/pdf/2606.23991v1)
- **Categories:** cs.AI, cs.LG, cs.MA, cs.RO


> The paper argues that true agency in AI requires a system’s goal‑setting, identity, decision‑making, self‑regulation, and learning mechanisms to be internalized rather than pieced together by external workflows, distinguishing “agentic” (engineered, task‑specific) from “agentive” (endogenously autonomous) systems. To embody this, the authors introduce the Goal‑Identity‑Configurator (GIC) architecture, which integrates hierarchical goal decomposition, evolving identity representations, a simulational world model for reasoning, learned self‑regulation, and self‑directed learning from both real and simulated experience. Empirical analysis of existing LLM‑based agents shows that only models adhering to the GIC design achieve measurable autonomous behavior while remaining auditable, controllable, and safer under human oversight.


<details>
<summary>Abstract</summary>

What is an agent? What constitutes agency? With the rise of Large Language Model (LLM) systems marketed as ``coding agents'', ``AI co-scientists'', and other ``agentic" tools that promise to drive up productivity, and at the same time, ``existential" concerns such as AI escaping human control with destructive power under a speculative ``machine agency" against humans, it has become essential to clarify where automation ends and agency begins, both for building capable systems and for understanding whether and what to fear. Drawing on Descartes' grounding of agency in independent thought, and on portrayals of autonomous beings in science fiction, we survey the current landscape of AI agents, and analyze agent architectures along five dimensions: goal, identity, decision-making, self-regulation, and learning. Specifically, we argue that genuine agency requires these structures to be \emph{internalized within the system itself} rather than assembled through external scaffolding. This distinction between \emph{agentic} systems, whose competence resides in engineered workflows, and \emph{agentive} systems, whose capabilities (including social interaction) arise endogenously, defines the boundary between systems designed for prescribed tasks, and those capable of operating in the open world with true autonomy. Building on this analysis, we propose the Goal-Identity-Configurator (GIC) architecture for a general-purpose agent model, combining hierarchical goal decomposition, identity evolution, simulative reasoning grounded in a separately trained world model, learned self-regulation, and self-directed learning from both real and simulated experience. Furthermore, we share insight on the auditability, controllability, and safety of agentive systems that possess greater autonomy and ``agency", but remain under human oversight.

</details>


### 108. When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents

- **Authors:** Tianyu Ding, Juan Pablo De la Cruz Weinstein
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23937v1](http://arxiv.org/abs/2606.23937v1)
- **PDF:** [https://arxiv.org/pdf/2606.23937v1](https://arxiv.org/pdf/2606.23937v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper shows that exact‑match retrieval recall is a poor predictor of how useful retrieved policy clauses are for long‑horizon tool‑use agents. By fine‑tuning Qwen2.5 classifiers on structured state representations and then feeding the top‑ranked retrieved clause directly into the decision‑time classifier, the authors find that—even though the correct clause appears at rank 1 only 7 % of the time—the retrieved‑clause classifier attains almost the same macro‑F1 (0.58 vs. 0.60) as when using gold‑standard clauses, far outperforming mismatched or no‑policy baselines. Consequently, they argue that evaluating retrievers solely by exact‑match recall underestimates their downstream policy utility and advocate measuring policy signal within the full classification loop.


<details>
<summary>Abstract</summary>

Exact-match retrieval recall is often used as a proxy for whether a retriever supplies useful policy context to a downstream decision model. We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. We then replace the benchmark-designated policy clause with the top-ranked clause retrieved from decision-time context. Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. We do not detect a macro-F1 difference between retrieved and gold clauses in this configuration, although the interval remains too wide to establish non-inferiority. The same qualitative pattern appears with a second retriever and at 7B, while varying across fine-tuning configurations. These results indicate that exact-match clause recall can underestimate downstream policy utility in this benchmark setting, motivating evaluation with retrieved policies in the classification loop rather than recall alone.

</details>


### 109. Welfarist Control Design -- How to fulfill the societal mandate in multi-agent control?

- **Authors:** Sophie Hall, Kai Zhang, Ilia Shilov, Heinrich H. Nax, Saverio Bolognani
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23931v1](http://arxiv.org/abs/2606.23931v1)
- **PDF:** [https://arxiv.org/pdf/2606.23931v1](https://arxiv.org/pdf/2606.23931v1)
- **Categories:** eess.SY, cs.MA, math.OC


> **Main contribution:** The paper proposes a “welfarist control” framework that equips control engineers with principled, ethically‑grounded tools for allocating scarce societal resources (e.g., traffic lanes, energy, water) among autonomous agents, moving design decisions away from ad‑hoc industry conventions toward explicit fulfillment of societal welfare mandates.

**Methodology:** It surveys three contemporary control paradigms—online feedback optimization, Markov decision‑process (MDP) control, and model predictive control (MPC)—and shows how each can be extended to (1) aggregate individual agents’ utility or preference models into a collective objective, (2) embed welfare‑oriented constraints, and (3) provide formal certification (stability, feasibility, performance guarantees) that the resulting control law respects those constraints.

**Key findings for agentic AI:** By leveraging the intrinsic feedback loop of these control schemes, the authors demonstrate that multi‑agent systems can dynamically re‑allocate shared resources in real‑time while provably meeting welfarist criteria (e.g., Pareto‑improvement, fairness indices). Empirical case studies (traffic lane assignment and grid capacity sharing) illustrate that welfarist‑augmented controllers achieve higher aggregate utility and reduced inequality compared with baseline controllers that ignore societal objectives, thereby highlighting a concrete pathway for integrating ethical, societal mandates into autonomous agent governance.


<details>
<summary>Abstract</summary>

At the core of most socio-technical systems lies a scarce resource that is allocated among agents: highway lanes, public transit, road space, water rights, energy access, grid capacity, user attention, pollution rights, etc. With further automation of the underlying allocation processes, control engineers are increasingly tasked to make decisive assumptions regarding what society wants. In practice to date, design choices are largely driven by industry norms and conventions rather than a result of conscientiously responsible and ethical design. In this paper, we look at tools available to control engineers to design systems in a more principled manner in order to match the societal mandate. We consider three control design paradigms: online feedback optimization, control of Markov decision processes, and model predictive control. Beginning with aggregating individual agents' preferences into control design objectives, subsequently ensuring and certifying the fulfillment of those specifications, we argue that the feedback nature of control systems enables appropriate allocation of the shared resources in ways hitherto unparalleled.

</details>


### 110. RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems

- **Authors:** Yarin Yerushalmi Levi, Roy Betser, Amit Giloni, Lidor Erez, Itay Gershon, Oren Rachmil, Sindhu Padakandla, Roman Vainshtein
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23927v1](http://arxiv.org/abs/2606.23927v1)
- **PDF:** [https://arxiv.org/pdf/2606.23927v1](https://arxiv.org/pdf/2606.23927v1)
- **Categories:** cs.AI


> The paper presents **RIFT‑Bench**, a unified, graph‑based framework for dynamically red‑teamning agentic AI systems. It first automatically extracts a hierarchical representation of an agent’s internal modules and communication pathways (Discovery phase) and then launches adaptive, multi‑vector adversarial probes that exploit those structures (Scanning phase), producing a single, comparable security report while also allowing mitigation strategies to be evaluated. Applied to 45 heterogeneous LLM‑driven agents, RIFT‑Bench reveals systematic vulnerabilities across architectures and demonstrates that its representation‑driven, two‑stage pipeline scales to diverse agent designs, offering a scalable baseline for security assessment in the emerging field of autonomous, agentic AI.


<details>
<summary>Abstract</summary>

Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. Building on a novel hierarchical representation, RIFT-Bench operates in two automated phases: Discovery, which extracts system structure, and Scanning, which deploys adaptive adversarial attacks and produces a comprehensive evaluation report. It evaluates the examined system itself, leveraging a broad set of dynamically adaptable adversarial probes across diverse attack vectors and objectives. We demonstrate the effectiveness of the proposed evaluation pipeline across 45 agentic systems spanning a diverse range of implementations, showing that the approach generalizes effectively to heterogeneous agentic architectures. Beyond systems and attacks, RIFT-Bench also supports direct evaluation of mitigation strategies. These key capabilities make RIFT-Bench a scalable foundation for security evaluation of agentic AI systems.

</details>


### 111. From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes

- **Authors:** Mariano Garralda-Barrio
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23797v1](http://arxiv.org/abs/2606.23797v1)
- **PDF:** [https://arxiv.org/pdf/2606.23797v1](https://arxiv.org/pdf/2606.23797v1)
- **Categories:** cs.SE, cs.AI, cs.CL, cs.MA


> **Paper Summary**  

The authors present **Goal‑Oriented Dialogue Runtime (GODR)**, a design pattern that augments graph‑based or multi‑agent orchestration systems with first‑class runtime objects representing *goals, task frames, lifecycle states, invalidation rules, and resumption contracts*. By externalizing these objects, GODR enables LLM‑driven conversational agents to suspend, resume, revise, or invalidate interdependent objectives across domains—capabilities that pure workflow graphs or reliance on chat history cannot guarantee. The methodology consists of a formal problem definition, a taxonomy of runtime objects, and architectural guidelines for integrating GODR with existing graph runtimes, agents, tools, or APIs; evaluation is outlined as an agenda for future empirical work. The key contribution is a reusable, framework‑neutral architecture that makes complex, interruptible, multi‑goal dialogues tractable for agentic AI systems.


<details>
<summary>Abstract</summary>

Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. This conceptual systems paper focuses on the high-complexity end of that design space, where goals can be suspended, resumed, revised, and invalidated by actions in other goals. We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). GODR is not proposed as a replacement for workflow graphs in simple guided processes; it is intended for complex, multi-domain, interruptible conversations where objective continuity cannot be recovered reliably from agent identity, chat history, or execution-graph position alone. The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim.

</details>


### 112. AIR: Adaptive Interleaved Reasoning with Code in MLLMs

- **Authors:** Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23678v1](http://arxiv.org/abs/2606.23678v1)
- **PDF:** [https://arxiv.org/pdf/2606.23678v1](https://arxiv.org/pdf/2606.23678v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **AIR (Adaptive Interleaved Reasoning)**, a framework that equips multimodal large language models (MLLMs) with the ability to interleave visual perception and numerical computation by invoking code‑based tools adaptively. The authors build a two‑stage cold‑start pipeline to generate complex, code‑augmented training data, filter it for high‑quality reinforcement‑learning (RL) episodes, and train the model with a **group‑constrained reward function** that guides when and how tools should be called. Experiments show that RL‑trained AIR raises benchmark performance by **~6.1 pp overall**, improves accuracy on interleaved‑reasoning items by **~9.9 pp**, and achieves a **>95 % tool‑use success rate**, demonstrating a significant step toward more versatile, agentic MLLMs capable of both visual and numerical reasoning.


<details>
<summary>Abstract</summary>

Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to enhance multimodal large language models (MLLMs) has become a pivotal research frontier. The existing literature focuses primarily on tool-use within vision-perception tasks. However, such approaches typically rely on predefined heuristics for visual manipulation and are inherently incapable of addressing numerical computation problems due to their exclusive focus on visual operations. This paper empowers MLLMs with adaptive interleaved reasoning capabilities through extended reinforcement learning training on code-augmented complex numerical computation tasks. To this end, we propose a comprehensive three-component solution consisting of: a two-stage cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved reasoning trajectories. Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks. Specifically, the accuracy for interleaved reasoning samples increases by 9.9 pp, and the overall success rate of tool-use exceeds 95%. Our data and code are available at: https://github.com/CongHan0808/AIR.git.

</details>


### 113. The Hitchhiker's Guide to Agentic AI: From Foundations to Systems

- **Authors:** Haggai Roitman
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.24937v1](http://arxiv.org/abs/2606.24937v1)
- **PDF:** [https://arxiv.org/pdf/2606.24937v1](https://arxiv.org/pdf/2606.24937v1)
- **Categories:** cs.AI, cs.CL, cs.IR, cs.LG


> The paper presents a full‑stack framework for building autonomous, “agentic” AI systems, arguing that high‑performing agents emerge only when every layer—from the underlying transformer‑based language model and its hardware‑aware training pipeline to alignment, reasoning, memory, and multi‑agent communication—is jointly engineered. It organizes this pipeline into three logical tiers: (1) the LLM substrate (including GPU architectures, fine‑tuning methods such as LoRA and Mixture‑of‑Experts, and inference optimizations); (2) the alignment & reasoning layer (RLHF, PPO/DPO, reward modeling, chain‑of‑thought scaling); and (3) the agentic layer (trajectory‑based RL, retrieval‑augmented generation, hierarchical memory, Model Context and Agent‑to‑Agent protocols, and design patterns for centralized, decentralized, and hierarchical multi‑agent topologies). Empirical demonstrations and code‑level recipes show that integrating these components yields agents that can store and retrieve episodic knowledge, coordinate tool use, and communicate across agents robustly, while the accompanying evaluation suite validates gains in task success rates, sample efficiency, and deployment scalability.


<details>
<summary>Abstract</summary>

The Hitchhiker's Guide to Agentic AI is a comprehensive practitioner's reference for building autonomous AI systems. The book covers the full stack from first principles to production deployment, organized around a central thesis: building great agentic systems requires understanding every layer of the pipeline, not just one. The book opens with the LLM substrate -- transformer architecture, GPU systems, training and fine-tuning (SFT,LoRA, MoE), model compression, and inference optimization -- treated as essential foundations rather than the primary focus. It then develops the alignment and reasoning layer: reinforcement learning from human feedback (RLHF), PPO, DPO and its variants, GRPO, reward modeling, and RL for large reasoning models including chain-of-thought and test-time scaling. The second half is devoted to agentic AI proper. Topics include agentic training and trajectory-based RL, retrieval-augmented generation (RAG and Agentic RAG), memory systems (in-context, external, episodic, and semantic), agent harness design and context management, and a taxonomy of agent design patterns. Inter-agent coordination is covered in depth: the Model Context Protocol (MCP), agent skills and tool use, the Agent-to-Agent (A2A) communication protocol, and multi-agent architectures spanning centralized, decentralized, and hierarchical topologies. The book concludes with agent development frameworks, agentic UI design, evaluation methodology for agentic tasks, and production deployment. Each chapter pairs rigorous theoretical foundations with implementation guidance, code examples, and references to the primary literature.

</details>


### 114. MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?

- **Authors:** Juyang Bai, Laixi Shi
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23664v1](http://arxiv.org/abs/2606.23664v1)
- **PDF:** [https://arxiv.org/pdf/2606.23664v1](https://arxiv.org/pdf/2606.23664v1)
- **Categories:** cs.LG, cs.MA


> The paper introduces **MAS‑PromptBench**, a systematic benchmark for evaluating how optimizing system prompts affects the performance of multi‑agent LLM pipelines. By extending two state‑of‑the‑art single‑agent prompt‑optimizers to the multi‑agent setting, the authors run extensive experiments across many tasks, workflow designs, communication protocols, and team sizes, measuring the impact of prompt tuning on overall MAS outcomes. They find that prompt optimization can yield **large, consistent performance gains** in many configurations—but the benefit is highly sensitive to factors such as the number of agents, the complexity of the coordination protocol, and the nature of the task, highlighting both the promise of prompt‑level control for agentic AI and the need for more scalable search strategies in larger MASs.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. It remains unclear whether, when, and by how much prompt optimization improves MAS performance, and how sensitive such gains are to system configuration. In this work, we systematically study system-prompt optimization across a broad range of MAS setups varying in task, workflow, communication protocol, and team size, benchmarking two prompt optimizers that naturally extend state-of-the-art single-agent methods. The results reveal its potential to unlock significant gains while exposing open challenges, characterizing when and how much prompt optimization helps across diverse MAS settings.

</details>


### 115. Decentralized Autonomous Traffic Management through Corridor Networks

- **Authors:** Jasmine Jerry Aloor, Aadarsh Govada, Hamsa Balakrishnan
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23585v1](http://arxiv.org/abs/2606.23585v1)
- **PDF:** [https://arxiv.org/pdf/2606.23585v1](https://arxiv.org/pdf/2606.23585v1)
- **Categories:** cs.MA, cs.AI, cs.ET, cs.RO, eess.SY


> The paper introduces a decentralized multi‑agent reinforcement‑learning (MARL) framework for managing high‑density autonomous aircraft traffic in Advanced Air Mobility (AAM) corridor networks. By training agents only on a single‑corridor scenario and then deploying the resulting policies zero‑shot on more complex multi‑corridor topologies (including merges, splits, variable densities, and heterogeneous vehicle dynamics), the authors show that locally coordinated entry, traversal, and exit actions suffice to generate globally efficient traffic flows without any central controller or retraining. Experiments demonstrate that the learned policies preserve corridor boundary compliance, high completion rates, reasonable speeds, minimal extra distance, and safe inter‑aircraft separation, highlighting a scalable, model‑free approach for agentic AI‑driven air‑traffic management.


<details>
<summary>Abstract</summary>

As autonomous aircraft are introduced at scale and traffic density increases, centralized management becomes insufficient to coordinate the large numbers of crewed and uncrewed aircraft. Dedicated Advanced Air Mobility (AAM) corridors have therefore been proposed for organizing high-density autonomous traffic flows. The desire to scalably provide autonomous aircraft flexibility in trajectory planning motivates the development of decentralized approaches to traffic management in AAM corridors.
  In this work, we extend a multi-agent reinforcement learning (MARL) approach to address the challenge of decentralized traffic flow management in air corridor networks. We test policies trained in a single-corridor setting on increasingly complex multi-corridor networks with combinations of merges and splits in a zero-shot manner. Experimental results demonstrate that learned behaviors transfer well to scenarios with varying traffic density, network geometry, and heterogeneous vehicle performance, without needing centralized coordination or model retraining. We evaluate system-level performance in terms of conformance to corridor boundaries, completion rates, average speeds, distance traveled, and maintenance of inter-aircraft separation. We find that although our policies require only locally coordinated entry, traversal, and exit behaviors, they collectively produce desirable traffic flows through the corridor network.

</details>


### 116. Cryptographic certificates of validity for trustworthy AI

- **Authors:** Murdoch J. Gabbay
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23768v1](http://arxiv.org/abs/2606.23768v1)
- **PDF:** [https://arxiv.org/pdf/2606.23768v1](https://arxiv.org/pdf/2606.23768v1)
- **Categories:** cs.CR, cs.AI, cs.LO


> The paper introduces **cryptographic certificates of validity** as a way to make agentic AI systems provably compliant with formally specified policies: a correctness predicate is compiled into a set of polynomial constraints whose satisfiability can be demonstrated with a succinct, publicly verifiable (and optionally zero‑knowledge) proof. By treating the proof as a “certificate” attached to each agent action, the approach bridges formal verification and cryptographic authentication, allowing third parties to check policy compliance without trusting the agent’s code or re‑executing its computation. The authors show how this construction generalizes proof‑carrying code and zk‑VM techniques, discuss the required mathematical translation, and outline practical challenges in specification, auditing, and deployment for trustworthy AI governance.


<details>
<summary>Abstract</summary>

We propose cryptographic certificates of validity for agentic AI systems. The core idea is to formally specify a correctness or policy condition as a logical predicate, compile this predicate to a witness-checking problem over polynomial constraints, and use a succinct cryptographic proof system (and optionally zero-knowledge) to certify that the condition holds.
  This offers a middle ground between formal verification of source code, and cryptographic authentication. An agent's action can be accompanied by an independently checkable proof that it satisfies an agreed formal policy, without requiring the verifier to trust the agent or to re-execute computation. We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer.

</details>


### 117. Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference

- **Authors:** Yuhang Gan, Yiwei Yang, Yuyi Li, Xiangyu Gao, Yichen Wang, Rain Jiang, Xiaoning Ding, Andi Quinn, Chen Qian
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23521v1](http://arxiv.org/abs/2606.23521v1)
- **PDF:** [https://arxiv.org/pdf/2606.23521v1](https://arxiv.org/pdf/2606.23521v1)
- **Categories:** cs.DC, cs.LG


> Concordia introduces a GPU‑resident, always‑on “persistent kernel” that transparently adds just‑in‑time‑compiled delta‑checkpoint handlers to the execution pipeline of large‑language‑model (LLM) agents, enabling fault‑tolerant inference without restarting the host stack or modifying individual framework components. By interposing on module loading and instrumenting PTX/SASS code, Concordia inserts checkpoint, pause, and recovery hooks at device synchronization points, streams dirty‑page detection and delta logging through a lock‑free ring buffer, and writes committed records to CXL or host memory. Experiments show that the system can recover full KV‑cache, scheduler, and adapter state within milliseconds after a GPU or interconnect failure, cutting recovery latency by orders of magnitude compared to existing whole‑process restart or application‑specific checkpoint schemes.


<details>
<summary>Abstract</summary>

Long-running LLM agents keep valuable state resident on GPUs: KV caches, request schedulers, communication state, and sometimes online adapters. Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. This paper argues that fault tolerance for such workloads needs a GPU-resident execution context: checkpoint hooks must run at device synchronization points, observe binary kernels that frameworks and libraries actually execute, and recover without putting the host CPU on the critical path.
  We present Concordia, a runtime that uses a device-resident persistent kernel as the substrate for fault-tolerant LLM inference. Concordia interposes on GPU module loading and supports PTX- and SASS-level instrumentation, allowing checkpoint and pause hooks to be inserted below framework code and library boundaries. For each registered LLM state region, Concordia JIT-compiles a specialized delta-checkpoint handler -- for example, a KV-block scanner, adapter-page scanner, or recovery applier -- and hot-swaps it into the persistent kernel's operator table. The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM.

</details>


### 118. AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction

- **Authors:** Shanhui Zhao, Jiacheng Liu, Guohong Liu, Jichao Yan, Jialei Ye, Yuhao Yang, Hao Wen, Shizuo Tian, Yizhen Yuan, Yuxuan Chen, Yunxin Liu, Ju Ren, Ya-Qin Zhang, Chao Huang, Yao Guo, Yuanchun Li
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23449v1](http://arxiv.org/abs/2606.23449v1)
- **PDF:** [https://arxiv.org/pdf/2606.23449v1](https://arxiv.org/pdf/2606.23449v1)
- **Categories:** cs.AI, cs.OS


> The paper introduces **AOHP (Android Open Harness Project)**, an open‑source, OS‑level framework that makes AI agents first‑class actors within Android, enabling adaptive UIs, agent‑friendly runtimes, personalized service composition, efficient interfaces, and secure information flow. By modifying AOSP to embed three agent‑oriented mechanisms—personalized service composition, low‑overhead agent APIs, and fine‑grained security policies—the authors experimentally demonstrate that agents running on AOHP complete tasks 21 % more often, cut token usage by roughly 52 %, and obey security policies significantly better than agents deployed on standard Android. This work provides a practical testbed for the emerging field of agent‑native operating systems and establishes concrete architectural primitives for efficient, personalized, and safe agent interaction.


<details>
<summary>Abstract</summary>

AI agents are driving a new software paradigm, with the ability to autonomously call tools, extract information, manage memory, and complete tasks that span applications and data sources. Most existing end-user operating systems, however, are designed for application-centric workflows and offer little native support for AI agents. This mismatch limits the wider adoption of agents and leads to execution overhead and safety risks when running agents on conventional systems. While the concept of agent-native operating systems is emerging, the research community lacks an open testbed to explore the architectural primitives desired for agent-mediated interaction. We present AOHP (Android Open Harness Project), an OS-level agent harness built on the Android Open Source Project (AOSP). The core design principle of AOHP is to treat agents as first-class OS actors, enabling adaptive user interfaces and agent-friendly runtime environments. AOHP preserves the mature Android software and hardware ecosystem while introducing three agent-oriented system mechanisms: personalized service composition, efficient agent interfaces, and secure information flow. Based on preliminary experiments on challenging tasks covering key capabilities of OS agents, AOHP shows clear advantages in task completion (+21.12% completion rate), execution cost (-51.55% token cost), and security-policy compliance.

</details>


### 119. Detecting Malicious Agent Skills in the Wild using Attention

- **Authors:** Bacem Etteib, Daniele Lunghi, Tégawendé F. Bissyandé
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23416v1](http://arxiv.org/abs/2606.23416v1)
- **PDF:** [https://arxiv.org/pdf/2606.23416v1](https://arxiv.org/pdf/2606.23416v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **Locate‑and‑Judge**, a two‑stage detection framework that uses LLM attention to pinpoint and evaluate potentially malicious “skills” (downloadable instruction packages) in LLM agent marketplaces, enabling full‑scale, low‑cost auditing of the supply‑chain attack surface.

**Methodology:** First, a fast “locator” ranks spans of a skill by the amount of instruction‑following attention they attract, selecting the top‑K high‑attention fragments. Then a more expensive “judge” model scrutinizes only these fragments for malicious behavior. This attention‑driven pruning reduces inference cost by roughly an order of magnitude compared with naïve whole‑skill scanning, while preserving high recall.

**Key findings:** Deployed at marketplace scale, Locate‑and‑Judge achieves high precision (the majority of flagged skills are confirmed malicious) and uncovers dozens of live malicious skills that evade existing scanners (e.g., SkillSpector, Cisco Skill Scanner). The approach outperforms keyword/regex baselines at similar cost and the authors release a labeled dataset of audited skills for the community.


<details>
<summary>Abstract</summary>

LLM agents increasingly load skills, file-based packages of natural-language instructions written by third parties and distributed through marketplaces, that execute with the user's privileges. A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. Prompt-injection defenses do not carry over to this setting. They rely on a boundary between trusted instructions and untrusted data, whereas a skill is itself a body of instructions, so an injected command sits among many legitimate ones and inherits their authority. We present Locate-and-Judge, a two-stage detector designed for this regime. A lightweight locator scores the structural spans of a skill by the instruction-following attention each span draws and retains only the top-K. A judge then examines the retained spans in detail. Concentrating the costly judgment on a few high-attention spans lets the detector audit an entire marketplace instead of a sample. Compared to direct LLM-based scanning, this approach offers an order-of-magnitude cost reduction, dramatically increasing its scalability at a small cost to recall, and it dominates keyword and regex baselines at comparable expense. Deployed at marketplace scale and at negligible cost, Locate-and-Judge flags skills with high precision, the majority of which we manually confirmed as malicious, surfacing dozens of live malicious skills, including several disguised as benign functionality and many that SkillSpector and Cisco Skill Scanner fail to detect. We release the resulting labeled dataset.

</details>


### 120. Emergent Relational Order in LLM Agent Societies: From Collective Affect to Authority Stratification

- **Authors:** Zhiyuan Ji, Xinyu Chen, Ziqi Dai, Shiyun Tang, Chunyu Wei, Yueguo Chen
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23764v1](http://arxiv.org/abs/2606.23764v1)
- **PDF:** [https://arxiv.org/pdf/2606.23764v1](https://arxiv.org/pdf/2606.23764v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **CAREB‑MAS**, a long‑horizon multi‑agent simulation that equips large‑language‑model agents with Affect Control Theory, Social Identity Theory, and a Durkheim‑inspired collective‑affect module, so that each agent continuously updates an egocentric identity through an emotion → ethics → belief reasoning chain while only minimal production and interaction rules are imposed at the macro level. In extensive simulations, the agents autonomously generate the five hallmark patterns of Fei Xiaotong’s Differential Order—stable labor specialization, guanxi‑based economic ethics, a decay of cooperation with relational distance, emergent relational authority, and a clan‑like center‑periphery hierarchy—and these structures shift predictably when the underlying production network moves from kin‑centric to functionally interdependent. The results demonstrate that such high‑level social stratification can emerge from general, mechanistic social processes, positioning LLM‑driven multi‑agent systems as a viable experimental platform for probing the formation and evolution of agentic social orders.


<details>
<summary>Abstract</summary>

Fei Xiaotong's Differential Order Pattern characterizes rural society as egocentric and relationally graded, with cooperation attenuating over social distance. Although often treated as culturally specific, its mechanistic basis remains under-operationalized, and prior LLM-based simulations have mainly addressed short-term coordination rather than long-horizon social structure. We propose CAREB-MAS, a multi-agent framework grounded in Affect Control Theory, Social Identity Theory, and Durkheimian collective affect. Agents reason through an emotion-ethics-belief chain and maintain dynamically evolving egocentric identities, while the macro environment specifies only individual production, preference-based allocation, and minimal interaction protocols. Across long-horizon simulations, agents spontaneously reproduce five core Differential Order phenomena: stable labor specialization, guanxi-based economic ethics, relational decay of cooperation, emergent relational authority, and clan-based center-periphery stratification. These patterns shift with production structure from kin-centered integration toward greater functional interdependence. Extensive experiment results support interpreting Differential Order as a structure-sensitive emergent outcome of general social mechanisms, with LLM-based multi-agent simulation providing an interdisciplinary framework for studying social structure and change.

</details>


### 121. Superhuman AI for Generals.io Using Self-Play Reinforcement Learning

- **Authors:** Matej Straka, Viliam Lisý, Martin Schmid
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23348v1](http://arxiv.org/abs/2606.23348v1)
- **PDF:** [https://arxiv.org/pdf/2606.23348v1](https://arxiv.org/pdf/2606.23348v1)
- **Categories:** cs.LG


> The paper introduces a superhuman AI agent for the real‑time strategy game Generals.io, achieving the top spot on a public 1‑v 1 leaderboard of 5,000+ humans and a 199‑70 head‑to‑head record against the previous human champions. The authors built a JAX‑native simulator that runs at tens of millions of frames per second (≈10,000× faster than existing tools), then trained a vision‑transformer policy end‑to‑end via self‑play using a simple policy‑gradient loop with sparse win/loss rewards, top‑advantage sample filtering, and an exponential moving average of parameters. They show that, once the data bottleneck is eliminated, a modest reinforcement‑learning pipeline—without extensive auxiliary losses or handcrafted features—suffices to attain superhuman performance in a complex, imperfect‑information RTS environment.


<details>
<summary>Abstract</summary>

We present a superhuman AI agent for Generals.io, a real-time strategy game that requires both long-horizon planning and short-term tactics under strong imperfect information. Trained for four days on 4x NVIDIA H200 GPUs, our agent reaches #1 on the public 1v1 leaderboard of over 5,000 human players, leading the second-ranked player by the same margin that separates second place from 25th, and beats the two top-ranked humans head-to-head with a combined 199-70 record across 269 ladder matches. A key enabler is a JAX-native simulator that reaches tens of millions of frames per second on a single GPU, roughly a 10,000x speedup over the prior simulator. On top of this, we train a vision transformer policy end-to-end by self-play with a policy-gradient loop and sparse win/loss reward, using top-advantage sample filtering and an exponential moving average of the policy parameters. Taken together, our findings highlight what matters, and what does not, once a fast simulator removes the data bottleneck.

</details>


### 122. VideoAgent: All-in-One Framework for Video Understanding and Editing

- **Authors:** Hengji Zhou, Lingxuan Huang, Jian Wang, Bing Zhou, Si Wu, Lianghao Xia, Chao Huang
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23327v1](http://arxiv.org/abs/2606.23327v1)
- **PDF:** [https://arxiv.org/pdf/2606.23327v1](https://arxiv.org/pdf/2606.23327v1)
- **Categories:** cs.CV, cs.AI


> **Main contribution:** VideoAgent introduces a unified, agentic framework that can comprehend, plan, and edit long, unstructured videos end‑to‑end, overcoming the narrow scope of prior systems that handle only short clips or single‑task editing.

**Methodology:** The system combines (1) a shot‑planning agent that automatically segments raw footage into coherent narrative shots via cross‑modal retrieval, and (2) a multi‑agent orchestration layer that selects from >30 specialized editing agents using intent parsing and a textual‑gradient graph optimizer to build complex editing pipelines while minimizing API calls.

**Key findings:** On the new VideoEdit benchmark and several public datasets, VideoAgent attains 87‑95 % successful orchestration, cuts API costs by ~60 %, and receives human ratings only 4 % lower than those of professionally edited videos—demonstrating near‑human quality in long‑video understanding and production.


<details>
<summary>Abstract</summary>

Video editing has become essential in digital media creation, yet existing automated systems are restricted to short segment processing and domain-specific tasks. They face two critical limitations: i) inability to handle diverse video comprehension and editing operations, and ii) lack of long-video understanding for coherent narrative creation. We propose VideoAgent, an all-in-one agentic framework addressing these challenges through two key innovations. First, we develop automated video shot creation with shot planning agents for coherent narratives and cross-modal retrieval for aligned visual content. Second, we design a multi-agent orchestration framework integrating over thirty specialized editing agents. Intent parsing filters relevant tools while textual-gradient graph optimization assembles complex editing pipelines. Extensive experiments on our newly-proposed VideoEdit benchmark and public datasets demonstrate VideoAgent's superiority over existing multimodal LLMs and agentic systems. VideoAgent achieves 87-95% orchestration success rates while reducing API costs by 60%. Human evaluation across six video categories shows VideoAgent produces professional-quality content approaching human-level performance, with ratings only 4% below human-created videos. We release our code at https://github.com/HKUDS/VideoAgent.

</details>


### 123. Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks

- **Authors:** Khadidja Kadem, Mostafa Ameli, Carlos Lima Azevedo, Mahdi Zargayouna, Latifa Oukhellou
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23257v1](http://arxiv.org/abs/2606.23257v1)
- **PDF:** [https://arxiv.org/pdf/2606.23257v1](https://arxiv.org/pdf/2606.23257v1)
- **Categories:** cs.LG, cs.AI, math.OC


> **Main contribution:** The paper introduces a two‑agent deep reinforcement‑learning (DRL) framework that jointly learns dynamic pricing for shared‑mobility services (SMS) and spatio‑temporal incentive policies for public transport, enabling coordinated regulation of multimodal networks with competing stakeholder objectives (revenue, equity, emissions).  

**Methodology:** Two DRL agents—one representing the public authority and one the SMS operator—are trained simultaneously in a simulation of a three‑hour morning‑peak multimodal network. The authority agent learns incentive allocations (e.g., subsidies, priority slots) to improve equity, reduce congestion and emissions, while the provider agent learns fare‑adjustment policies to maximize profit; both agents observe the evolving demand, congestion, and network state and update their policies via standard deep Q‑learning (or actor‑critic) techniques.  

**Key findings:** In numerical experiments, the coordinated agents cut peak congestion, lower commuters’ travel costs by ≈ 20 % and emissions by ≈ 10 %, and nearly double public‑transport profit, while preserving the SMS provider’s revenue. The results demonstrate that multi‑agent DRL can reconcile conflicting stakeholder goals and serve as a decision‑support tool for sustainable, equitable multimodal mobility planning.


<details>
<summary>Abstract</summary>

In multimodal transportation systems, shared mobility services (SMSs) are promoted for their potential to enhance flexibility and reduce congestion. However, SMS demand is often concentrated in high-density areas, which can limit the effectiveness and accessibility for various commuter groups. This uneven integration challenges transportation system efficiency, especially in terms of emissions and spatial equity. Addressing these issues requires coordination among multiple stakeholders whose objectives frequently conflict. Whereas authorities aim to ensure sustainable and equitable mobility, SMS providers focus on revenue maximization, and travelers seek to minimize personal travel costs. This paper proposes a multi-agent deep reinforcement learning framework that captures these interactions through dynamic pricing and incentivization strategies for SMSs and public transport. The framework integrates two reinforcement learning (RL) agents: (i) a public authority that allocates spatio-temporal public transport incentives to improve equity, emissions, and efficiency, and (ii) an SMS provider that dynamically adjusts fares to optimize revenue. The agents interact with the transportation system and adapt strategies in response to evolving demand, congestion, and network conditions. Numerical experiments conducted over a three-hour morning peak period show that dynamic incentivization effectively reduces congestion peaks, lowers commuters' costs by around 20% and emissions by approximately 10%, while nearly doubling public transport profit and supporting a more equitable distribution of benefits. When combined with dynamic SMS pricing, the two RL agents demonstrate the ability to balance conflicting objectives between private providers and public authorities. The proposed approach provides a decision-support tool for sustainable and equitable multimodal mobility planning.

</details>


### 124. MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations

- **Authors:** Elena Sofia Ruzzetti, Cornelius Emde, Sangdoo Yun, Seong Joon Oh, Martin Gubri
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23217v1](http://arxiv.org/abs/2606.23217v1)
- **PDF:** [https://arxiv.org/pdf/2606.23217v1](https://arxiv.org/pdf/2606.23217v1)
- **Categories:** cs.CL, cs.AI


> MuPPET (Multi‑Party Privacy Exposure Testing) is the first benchmark that quantifies how large‑language‑model (LLM) assistants handle contextual privacy when participating in group chats, where any disclosed personal detail must be appropriate for every participant. The authors evaluate a range of frontier and open‑source LLMs on MuPPET, finding that leakage rates are dramatically higher in multi‑party dialogs than in traditional one‑to‑one tests, and that existing privacy‑preserving techniques only partially mitigate the problem while hurting response usefulness. The results highlight a previously unmeasured vulnerability—party‑tracking and over‑sharing—in agentic AI systems and call for new defenses tailored to multi‑user contexts.


<details>
<summary>Abstract</summary>

LLM agents are increasingly deployed in multi-party environments, handling sensitive personal data on behalf of individual users, for instance in group chats. When such an agent discloses private information, it reaches every group member at once. This risk is structurally harder to control than in one-to-one settings, as every piece of private information must be appropriate for every recipient in the group. Yet all existing contextual privacy benchmarks consider only single-interlocutor settings, leaving multi-party privacy risks unmeasured. We introduce MuPPET (Multi-Party Privacy Exposure Testing), a benchmark for contextual privacy in multi-party conversations. Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. Frontier models are vulnerable, and smaller open-weights models, often preferred for local deployment with sensitive data, even more so. Existing contextual privacy defences offer only partial protection, degrade utility, and do not resolve the underlying party-tracking problem.

</details>


### 125. Decomposing Financial Market Dynamics via Mechanism Analysis in an Evolutionary Multi-Agent Simulation

- **Authors:** Zhibao Chen
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23158v1](http://arxiv.org/abs/2606.23158v1)
- **PDF:** [https://arxiv.org/pdf/2606.23158v1](https://arxiv.org/pdf/2606.23158v1)
- **Categories:** cs.AI, cs.MA, cs.NE


> The paper introduces a modular evolutionary multi‑agent market simulator in which four core mechanisms—selection operator, price‑formation feedback, behavioral bias, and consensus‑network topology—can be swapped independently, enabling systematic “single‑mechanism” experiments across 3 × 20 random seeds. By comparing Quality‑Diversity (QD/MAP‑Elites) selection to traditional top‑k truncation, the authors show that QD markedly increases strategy‑mix entropy and sustained cycling without improving market realism, while reflexive price feedback boosts realism and amplified behavioral bias raises a genomic fragility metric, with consensus topology having no measurable impact. These findings partition the design space of agentic financial markets into roughly orthogonal control knobs for diversity, realism, and fragility, offering a principled methodology for dissecting and engineering emergent properties in agent‑based AI systems.


<details>
<summary>Abstract</summary>

Evolutionary agent-based markets (ABMs) couple several mechanisms -- who reproduces, how price forms, how biased the agents are, how consensus propagates -- yet these are usually fixed by convention, so it is unclear which mechanism controls which emergent property. In a coevolving, endogenous-price simulator with 120 heterogeneous behavioral agents, we make four mechanisms pluggable and run matched 3x20-seed interventions. We find the levers are largely separable. (1) Selection -> diversity: a Quality-Diversity (QD/MAP-Elites) operator robustly raises strategy-mix entropy over truncation top-k (paired Delta entropy +0.27 to +1.12 bits; sign-test p<0.001; CIs exclude 0) and sustains more strategy cycling (strongest in crisis: Delta=+0.070, p=0.0004). (2) Selection does not improve realism: even a per-agent realism reward that provably steers selection does not raise 5-fact realism (Delta_5=-0.11,-0.08,+0.03; not significant). (3) Microstructure -> realism: enabling reflexive price feedback does raise realism (Delta_5=+0.13,+0.20,+0.20; crisis/bull p<0.05, all CIs positive). (4) Behavior -> fragility: amplifying behavioral bias raises a genomic fragility proxy (Delta=+10.5,+11.1,+14.4; bull p<0.001, all CIs positive) while leaving realism flat. The remaining mechanism -- consensus network topology -- shows no robust effect (honest null). The contribution is a decomposition: in these single-mechanism sweeps the mechanisms behave as approximately distinct control knobs over diversity, realism, and fragility.

</details>


### 126. Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation

- **Authors:** Julia Belikova, Rauf Parchiev, Evgeny Egorov, Grigorii Davydenko, Gleb Gusev, Andrey Savchenko, Maksim Makarenko
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23127v1](http://arxiv.org/abs/2606.23127v1)
- **PDF:** [https://arxiv.org/pdf/2606.23127v1](https://arxiv.org/pdf/2606.23127v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> The paper presents **AFTER**, a large‑scale benchmark (382 enterprise‑level tasks, 6 roles, 22 procedural skills) for rigorously testing how procedural memory—i.e., stored “how‑to” sequences—can be learned, refined, and transferred by LLM‑based agents. Using controlled experiments that isolate local fine‑tuning, cross‑task, cross‑role, and cross‑model transfer, the authors show that a single refinement iteration yields a 3.7–6.7‑point boost in overall task performance, and that skills distilled from heterogeneous multi‑model execution traces achieve 73.1 % accuracy on unseen models—surpassing any single‑model source. Crucially, the study finds that while some procedural skills are broadly reusable, others become tightly tied to specific roles, informing how practitioners should design, evaluate, and deploy procedural memory systems for scalable, production‑grade agentic AI.


<details>
<summary>Abstract</summary>

Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. We introduce AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how skills transfer across tasks, roles, and model backbones. The benchmark includes controlled evaluation settings for local improvement, cross-task transfer, cross-role transfer, and cross-model generalization. Experiments show that procedural memory delivers consistent gains in industrial workflows: a single refinement round improves aggregate performance by 3.7-6.7 points, while skills evolved from diverse multi-model execution traces achieve 73.1% cross-model test accuracy, outperforming all single-model trace sources. We further find that some skills generalize broadly across tasks and models, whereas others become specialized to role-specific workflows and lose effectiveness under transfer. These results provide practical guidance for building, evaluating, and deploying procedural memory systems in production agent platforms.

</details>


### 127. Cognitive Digital Twins: Ethical Risks and Governance for AI Systems That Model the Mind

- **Authors:** Vamshi Krishna Bonagiri, Juan Nicolas Sepulveda-Arias, Abdoul Jalil Djiberou Mahamadou, Monojit Choudhury
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23094v1](http://arxiv.org/abs/2606.23094v1)
- **PDF:** [https://arxiv.org/pdf/2606.23094v1](https://arxiv.org/pdf/2606.23094v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **cognitive digital twins (CDTs)**—continuous AI models that ingest behavioral, contextual, and physiological streams to create and update a computational replica of an individual’s mind, capable of prediction, simulation, and proxy decision‑making. To govern this unprecedented form of personal‑level cognition modeling, the authors devise a **5A framework (Authority, Autonomy, Access & control, Accountability, Availability)** and delineate CDT‑specific hazards such as epistemic authority shifts, “shadow twins,” simulated participation, and asymmetric proxy power, demonstrating that existing regulations for assistants, recommender systems, or ADSs leave critical gaps. Their analysis yields concrete governance requirements—enhanced consent mechanisms, strict purpose limitation, model validity and traceability, mechanisms for contestation and independent review, and mandatory model retirement—arguing that oversight must target the *representation* of cognition itself, not merely downstream decisions or actions.


<details>
<summary>Abstract</summary>

As AI systems become increasingly persistent and personalized, they make possible a class of technologies that we call cognitive digital twins (CDTs): dynamic computational representations of a specific person's cognition, updated from behavioral, contextual, or physiological data in order to model, predict, or simulate that person's cognition, or to act as that person's communicative or decision-making proxy. CDTs combine cognitive inference with longitudinal representation, simulation, and proxy action in ways that existing governance strategies for personal assistants, autonomous agents, recommender systems, and automated decision systems only partially address. This paper makes four contributions. First, we define CDTs and distinguish them from adjacent systems. Second, we introduce a 5A governance framework organized around authority, autonomy, access and control, accountability, and availability. Third, we identify CDT-specific risks, from misrepresentation and epistemic authority shifts to shadow twins, simulated participation, proxy action, and proxy-power asymmetries. Fourth, we analyze governance gaps and propose requirements for high-risk CDTs that strengthen consent, purpose limitation, validity, traceability, contestation, independent review, and model retirement. Existing frameworks primarily regulate data processing, automated decisions, or autonomous actions; CDTs also require governance at the level of cognitive representation itself, before any final decision or external action occurs. We argue that CDTs require governance not only because they can act for people, but because they can become infrastructures through which cognition is represented, simulated, classified, and operationalized.

</details>


### 128. Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies

- **Authors:** Ruixiao Lin, Xinhao Deng, Qingming Li, Jianan Ma, Yunhao Feng, Yuqi Qing, Zhenyuan Li, Yechao Zhang, Shiwen Cui, Changhua Meng, Tianwei Zhang, Xingjun Ma, Qi Li, Ke Xu, Shouling Ji
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23075v1](http://arxiv.org/abs/2606.23075v1)
- **PDF:** [https://arxiv.org/pdf/2606.23075v1](https://arxiv.org/pdf/2606.23075v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a comprehensive threat model for self‑evolving large‑language‑model (LLM) agents that autonomously modify their own weights, memory, tools, and architecture, showing how adversarial manipulations become permanently encoded and propagate across generations. By introducing the Module‑Lifecycle Attack Surface (MLAS) matrix—five functional modules (Brain, Cognitive Resource, Execution, Self‑Design, Collective) crossed with five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve)—the authors systematically evaluate 25 attack‑surface cells, uncovering 17 critical vulnerabilities with no effective mitigations and seven cross‑cutting amplification effects that make isolated defenses insufficient. Empirical case studies on two open‑source self‑evolving frameworks reveal that evolution‑native designs expose 3.5 × more vulnerable cells and achieve 100 % persistence of injected payloads, while conventional scanners block only ~2 % of attacks, underscoring the need for evolution‑aware security mechanisms and formal verification for agentic AI systems.


<details>
<summary>Abstract</summary>

Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). Analysis of the resulting 25 cells reveals that 17 face critical threats for which no effective partial mitigation. We identify seven cross-cutting amplification effects that interact synergistically and cannot be addressed by securing individual modules in isolation. Comparative case studies of two open-source frameworks demonstrate that evolution-native design activates $3.5\times$ more attack surface cells and achieves a 100% attack persistence rate (40/40 payloads across all CIA+Privacy categories), while co-located security scanners block only 2.5% of attacks. Our findings establish that self-evolution converts every known attack category from session-bounded to lineage-persistent, gives rise to entirely new attack classes, and renders static defenses structurally inadequate, motivating evolution-aware security frameworks and formal verification for self-modifying systems.

</details>


### 129. A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees

- **Authors:** Baoxun Wang
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.23026v1](http://arxiv.org/abs/2606.23026v1)
- **PDF:** [https://arxiv.org/pdf/2606.23026v1](https://arxiv.org/pdf/2606.23026v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper introduces a *contextual Stackelberg game* for governing the computational resources (context length, prompt verbosity, tool calls) of multi‑turn LLM agents, and provides a learning‑based pipeline that first models the follower’s (executor’s) resource‑allocation response, then optimizes a leader (controller) policy and finally “repairs” it using real‑API feedback and projection onto a safe action set.  

**Methodology**  
1. **Conditional response model** – train a neural model of the executor’s resource actions conditioned on the leader’s quality target and cost incentive.  
2. **Leader optimization** – solve the Stackelberg game against the learned follower model to obtain a provisional controller policy.  
3. **Policy repair** – calibrate the provisional policy on the actual LLM API, then project its actions onto an empirically chosen feasible set to guarantee safety and stability.  
Theoretical analysis yields conditional guarantees for equilibrium existence, follower‑response stability, safe‑set projection, and bounded transfer error from the surrogate (learned) environment to the real API.  

**Key findings**  
In a 300‑turn real‑API evaluation, the repaired controller achieved a **17.4 % reduction in mean token cost** compared with a conservative baseline (statistically significant, Welch p = 0.022) while maintaining comparable answer quality (no significant quality drop, p = 0.44). The results demonstrate that a repaired Stackelberg controller can reliably trade off quality and resource usage for LLM agents, providing a promising step toward provably safe, resource‑aware autonomous language‑model agents.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly operate as multi-turn systems that must allocate context, prompt verbosity, and tool access under finite computational budgets. Static thresholds are simple, but they are brittle under heterogeneous tasks and evolving session states. We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. For the restricted game, we establish conditional guarantees for equilibrium existence, follower-response stability, safe-set projection, and transfer from a surrogate environment to the real environment under bounded value error. The primary real-API experiment comprises 300 evaluated turns. Relative to a conservative baseline, the selected repaired controller reduces mean token cost by 17.4% (Welch $p=0.022$), while the measured quality difference is not statistically significant ($p=0.44$). The theoretical results are conditional and the experiments do not estimate their regret or transfer constants; consequently, the evidence establishes a promising repaired operating point, not a certified real-system equilibrium.

</details>


### 130. StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs

- **Authors:** Youxin Zhu, Yixuan Ding, Peng Lai, Longyue Wang, Bingyi Jing, Guanhua Chen
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22977v1](http://arxiv.org/abs/2606.22977v1)
- **PDF:** [https://arxiv.org/pdf/2606.22977v1](https://arxiv.org/pdf/2606.22977v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **StatABench**, a two‑part benchmark (Stat‑Closed with 404 multi‑format questions across 18 topics and Stat‑Open with 30 open‑ended modeling tasks) for systematically evaluating how well large language models can perform statistical analysis. Using the LangChain MCP framework and a suite of data‑science agents, the authors assess both closed‑form accuracy and end‑to‑end modeling quality via an LLM‑as‑Judge protocol, finding that even the strongest commercial model (GPT‑5.1) falls to 68.6 % on Stat‑Closed and the best open‑source model to 60.6 %, while the top agent pipeline reaches only 61.9 % on Stat‑Open. These results expose a substantial gap in current agentic AI systems for tool‑grounded reasoning, methodological decision‑making, and full statistical workflow execution.


<details>
<summary>Abstract</summary>

Statistical analysis is a broad, complex field requiring both domain knowledge and tool proficiency. While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. To bridge this gap, we introduce StatABench (Statistical AnalysisBenchmark), a benchmark designed to systematically assess LLMs' statistical analysis capabilities. StatABench comprises two complementary components: Stat-Closed, containing 404 questions across 18 statistical topics in multiple formats (multiple-choice, fill-in-the-blank, decision-making, and practical application), and Stat-Open, featuring 30 complex open-ended modeling tasks adapted from professional competitions. We evaluate diverse LLMs using the LangChain MCP framework and multiple data science agents, and assess Stat-Open solutions via a validated LLM-as-Judge protocol. Experiments show that even GPT-5.1 achieves only 68.6% on Stat-Closed, while the best open-source model reaches 60.6%. On Stat-Open, the top agent framework scores 61.86 on average. These results reveal the gap between current LLMs and reliable statistical analysis, highlighting persistent challenges in tool-grounded reasoning, methodological decision-making, and end-to-end statistical modeling.

</details>


### 131. Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents

- **Authors:** Aman Mehta, Anupam Datta
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22953v1](http://arxiv.org/abs/2606.22953v1)
- **PDF:** [https://arxiv.org/pdf/2606.22953v1](https://arxiv.org/pdf/2606.22953v1)
- **Categories:** cs.AI, cs.CL


> The paper demonstrates that current LLM‑based agents do not internalize early‑generated plans as persistent knowledge; instead they rely on the plan staying in the limited context window, causing rapid decay of the plan‑related signal once the plan is evicted. By introducing **replay pairing**—running identical trajectories with and without the plan in context—and probing hidden‑state representations, the authors show that plan information drops by a factor of 4–12 after a single observation step, and that standard “thinking” traces confound measurement unless strictly stripped. Their stress‑test on ALFWorld shows that naïve plan eviction reduces success rates by ~35 percentage points, while a probe‑guided re‑surfacing mechanism preserves performance, highlighting that robust context‑management, not just plan protection, is essential for long‑horizon agentic AI.


<details>
<summary>Abstract</summary>

Long-horizon agents depend on context management: systems compress, summarize, and evict old tokens so tasks can continue beyond finite windows. That is safe only when dropped information is no longer needed or has been internalized. Plans are the stress case: they are written early, used for many steps, and first to be evicted. We introduce replay pairing, a diagnostic that runs the same trajectory with and without the plan in history and measures hidden-state cosine distance. On Llama-3.1-70B, plan signal spikes to 0.453 one step after the plan, then falls 4.1x in a single action-observation step; HotpotQA falls 12.4x. This is evidence that standard LLM agents do not carry plans forward as persistent state, and instead depend on the plan remaining in context. A layer-L32 probe detects this decay as a diagnostic, not as proof that it reads plan content itself. Reasoning models add a measurement confound: their `<think>` traces re-derive plan content, so standard stripping leaves plan evidence in the stripped condition. We name this the reasoning-trace confound and fix it with strict stripping, which removes prior `<think>` blocks from the stripped run only. It recovers +163% of the step+1 signal in-sample and +153% held out, while not meaningfully changing non-reasoning Llama (+4.8%). On DeepSeek-R1-Distill-Llama-70B, a Llama-trained probe transfers at AUROC 0.748 (p=6e-4), while R1-specific probes reach 1.000, suggesting R1 encodes plan signal in a different hidden-state direction. Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. The contribution is a measurement and stress-test framework showing that agent-critical information can be context-resident rather than persistent. Context management is load bearing, but plan protection alone is not enough.

</details>


### 132. When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents

- **Authors:** Aman Mehta
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22936v1](http://arxiv.org/abs/2606.22936v1)
- **PDF:** [https://arxiv.org/pdf/2606.22936v1](https://arxiv.org/pdf/2606.22936v1)
- **Categories:** cs.AI


> The paper identifies “premature commitment” as a failure mode for long‑horizon LLM agents, where the model converges early on a single interpretation of evidence and then merely defends that view. By measuring representational commitment—cross‑run hidden‑state similarity at a fixed reasoning step—the authors show that early hidden‑state convergence predicts later trajectory consistency (e.g., r = ‑0.35 to ‑0.83 across Llama‑3.1‑70B, Qwen‑2.5‑72B, Phi‑3‑14B and StrategyQA) but does **not** predict correctness, allowing a runtime monitor to flag unstable runs with up to 0.97 AUROC and a prompting intervention to reduce behavioral variance by ~28 % without harming accuracy. The work provides a concrete diagnostic tool for detecting hidden‑process collapse in agentic LLM reasoning, while highlighting its limited utility for directly improving answer quality.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents can fail quietly: they settle on one reading of the evidence early, then spend the rest of the run defending it. We call this premature commitment. Final-answer scoring misses the failure mode because it sees only the answer, not whether the process has already collapsed to a stable path. We define representational commitment as cross-run hidden-state convergence at a fixed reasoning step, and use it as an early diagnostic of trajectory consistency. On Llama-3.1-70B running ReAct on HotpotQA, step-4 hidden-state similarity predicts downstream behavioral consistency (r = -0.35, partial r = -0.45), with a localized temporal and layer-wise signature. The signal replicates across Qwen-2.5-72B and Phi-3-14B, and on StrategyQA (r = -0.83). It does not track correctness: committed-wrong and committed-correct questions are not separable in activation similarity. That boundary is central to the claim. Commitment tells us whether an agent has settled, not whether it is right. A runtime monitor detects inconsistent trajectories from hidden states at AUROC up to 0.97 (0.85--0.88 under a stricter split), and a prompting intervention cuts behavioral variance by 28% against a token-matched control while leaving accuracy statistically unchanged. We also test whether the signal can route self-consistency compute; on a harder benchmark it helps only modestly and is matched by a simpler output-based baseline. The result is a diagnostic for a hidden process failure, with clear limits rather than a general accuracy lever.

</details>


### 133. Intent-Governed Tool Authorization for AI Agents

- **Authors:** Genliang Zhu, Chu Wang
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22916v1](http://arxiv.org/abs/2606.22916v1)
- **PDF:** [https://arxiv.org/pdf/2606.22916v1](https://arxiv.org/pdf/2606.22916v1)
- **Categories:** cs.AI


> The paper introduces **Intent‑Governed Access Control (IGAC)**, a server‑side authorization layer that augments traditional credential‑based checks with the user’s expressed *intent* as a monotone, auditable policy attribute for AI‑agent tool calls. IGAC implements intent certificates, session‑scoped policy narrowing, intent‑aware manifest filtering, and consistency checks between the declared intent and the tool‑payload, ensuring that an agent can only exercise a subset of its static integration permissions that is justified by the current user request. Mapped onto the OpenPort governance substrate, experiments show that IGAC reliably blocks over‑privileged tool invocations (e.g., export or delete operations when a user only asked for a summary) while preserving legitimate workflow functionality, thereby offering a practical, backward‑compatible mechanism for tighter, intent‑driven control of AI agents that operate across heterogeneous tools.


<details>
<summary>Abstract</summary>

AI agents increasingly act through external tools: they read private data, construct structured payloads, submit write requests, export records, and coordinate workflows across application boundaries. Existing authorization mechanisms usually ask whether an integration credential, app, or token can call a tool. That question is necessary but incomplete. A tool call can be authorized by static credentials and still be unjustified by the user's current request. For example, a credential that can read and export records should not expose export authority when the user only asked for a bounded summary, and a model-generated delete call should not execute merely because the integration has a delete scope. This paper proposes Intent-Governed Access Control (IGAC), a server-side authorization layer that treats the user's expressed intent as a monotone, auditable policy attribute for AI-agent tool use. IGAC introduces intent certificates, session-scoped policy narrowing, intent-aware manifest filtering, and intent-tool-payload consistency checks. The central invariant is that user intent may only reduce the authority granted by static integration policy; it never expands scopes, data policy, tenant boundaries, or review requirements. We map IGAC onto OpenPort, an existing governance substrate that already implements authorization-dependent discovery, scope and ABAC-style policy checks, draft-first writes, preflight impact binding, state-witness checks, idempotency, stable reason codes, and audit.

</details>


### 134. DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings

- **Authors:** Wenya Xie, Shengming Zhou, Zelin Li, Pouya Parsa, Shuang Zhou, Xinheng Ding, Chinmay Arvind, Guanchu Wang, Vladimir Braverman, Ali Payani, Yantao Zheng, Zirui Liu
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22877v1](http://arxiv.org/abs/2606.22877v1)
- **PDF:** [https://arxiv.org/pdf/2606.22877v1](https://arxiv.org/pdf/2606.22877v1)
- **Categories:** cs.CL


> The paper introduces **DynamicMem**, a synthetic long‑horizon memory benchmark that simulates 15 months of multi‑app user activity (≈2.2 M tokens and 1.8 k grounded events per user) to evaluate how LLM agents remember heterogeneous attributes, habits, and preferences that evolve over time and are only inferable from scattered signals. Using five quarterly checkpoints, the authors test five representative LLM‑agent architectures and find that (1) profile reconstruction accuracy deteriorates as the history grows while downstream task performance remains flat, (2) no system can simultaneously retain stable facts and update changing ones—errors concentrate on preferences and referent naming—and (3) >93 % of failures stem from the retrieval component rather than the LLM’s reasoning, highlighting memory retrieval as the primary bottleneck for agentic AI.


<details>
<summary>Abstract</summary>

LLM agents increasingly act as personal assistants that must remember a user's profile over months: who they are (attributes), what they routinely do (habits), and what they prefer (preferences), and keep it updated as jobs, routines, and tastes drift. Existing benchmarks evaluate this "memory" ability through short, simplified interactions, missing three core properties of real behavior: the profile is heterogeneous, with attributes, habits, and preferences evolving on different timelines; changes are driven by external context such as seasons and life events; and evidence is rarely stated explicitly, instead scattered across many small actions in different apps that a memory system must infer from. We introduce DynamicMem, a synthetic benchmark that constructs 15 months of activity per user, providing long-term multi-app data that real users' privacy keeps out of reach. It provides user-consistent trajectories averaging 2.2M tokens and 1,772 grounded events per user across 16 applications such as e-commerce, fitness, and social platforms. The profile evolves over this period and is never given explicitly: each attribute, habit, or preference must be inferred from small signals scattered across apps. We evaluate at five quarterly checkpoints to track how systems scale as history grows. Benchmarking five representative systems exposes problems a single accuracy score hides: (i) profile reconstruction degrades with history length while service-task accuracy stays flat, despite both drawing on the same memory; (ii) no system both keeps facts that stay true and replaces facts that change, with errors clustering on preferences and on naming the exact referent; and (iii) over 93% of failures trace to what the memory retrieves, not to the model writing the answer, so the largest room for improvement lies in memory itself. Code: https://wenyaxie023.github.io/DynamicMem/

</details>


### 135. AI Scientists as Engines of Discovery: A Case for Development within Reformed Institutions

- **Authors:** Raul Jimenez, Boris Bolliet, Francisco Villaescusa-Navarro, Rabih Zbib, Benjamin Wandelt, David N. Spergel, Thomas Meier, Jessica Montgomery, Hana Aliee, Licia Verde
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22859v1](http://arxiv.org/abs/2606.22859v1)
- **PDF:** [https://arxiv.org/pdf/2606.22859v1](https://arxiv.org/pdf/2606.22859v1)
- **Categories:** cs.AI, astro-ph.IM, physics.soc-ph


> The paper argues that the emergence of agentic AI is a qualitative shift that can turn multi‑agent systems into “AI scientists” capable of autonomously generating, testing, and critiquing hypotheses, thereby expanding the throughput of scientific discovery. It proposes a modular multi‑agent architecture (exemplified by the prototype framework **Denario**) that coordinates literature mining, code synthesis, data analysis, hypothesis formulation, and model‐validation loops, and it outlines the institutional redesign—focused on verification, accountability, interpretability, and dual‑use safety—required to integrate such epistemic agents into the research ecosystem. Empirical case studies with Denario show accelerated discovery cycles and navigation of model spaces unreachable by humans, leading to concrete recommendations for authorship, peer review, and governance that treat AI as an autonomous epistemic actor rather than a passive tool.


<details>
<summary>Abstract</summary>

Agentic artificial intelligence (AI) systems are beginning to assist, accelerate, and partially automate scientific discovery, performing tasks that span literature synthesis, code generation, data analysis, hypothesis proposal, and model criticism. We argue that this transition is qualitative rather than incremental, and that suitably designed multi-agent systems may evolve from passive computational tools into ``AI scientists'' that can expand the hypothesis-generating and verification capacity of science. Such systems must be developed and deployed within a scientific ecosystem fit for purpose: institutions must be redesigned for verification, accountability, interpretability, and dual-use safety. We sketch how multi-agent architectures, illustrated by the prototype framework \textit{Denario}, accelerate the discovery cycle and traverse model spaces beyond human reach; examine what this implies for authorship, peer review, and the enduring role of human scientists; and close with recommendations for governing AI as an epistemic actor rather than a mere instrument.

</details>


### 136. RaMem: Contextual Reinstatement for Long-term Agentic Memory

- **Authors:** Wei Yang, Bryce Kan, Shixuan Li, Li Li, Yuehan Qin, Jiate Li, Paul Bogdan, Jesse Thomason
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22844v1](http://arxiv.org/abs/2606.22844v1)
- **PDF:** [https://arxiv.org/pdf/2606.22844v1](https://arxiv.org/pdf/2606.22844v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **RaMem**, a “Contextual Reinstatement” framework that augments retrieval‑augmented LLM agents with long‑term memory that remains **context‑aware**. RaMem first anchors each stored fragment with its original episodic metadata (time, session, participants), then infers the contextual conditions implied by a new query, uses these conditions to retrieve only memories that are compatible (while still keeping fallback content‑relevant items), and finally feeds the structured, reinstated context to the generator. Across several long‑term memory benchmarks and backbone models, RaMem reduces “context collapse” and yields **≥10 % absolute F1 improvements** over strong retrieval baselines, demonstrating that preserving and reasoning over episodic context is crucial for reliable agentic memory.


<details>
<summary>Abstract</summary>

Long-term memory has become increasingly important for LLM agents that operate across extended interactions and evolving task contexts. Recent memory systems have made past experiences more persistent, compact, and retrievable, but retrieval alone does not ensure that a memory provides valid evidence for the current query. When experiences are compressed into reusable fragments, memories from different situations may appear equally relevant if they involve recurring entities or user states. We refer to this failure as context collapse: memories lose the surrounding context needed to judge whether they provide valid evidence for the current query. To address this problem, we propose Contextual Reinstatement for Agentic Memory (RaMem), a framework that turns retrieved memory fragments into contextually verifiable evidence. RaMem operates through four coordinated stages: (i) evidence anchoring grounds each memory in its original episodic conditions, especially event time, mention time, session span, and participants; (ii) recall condition induction derives the evidence conditions implied by the query; (iii) validity-aware retrieval uses these conditions to prioritize context-compatible memories while retaining content-relevant candidates as fallback evidence; and (iv) context-preserved synthesis keeps the selected memories' structured context available to the generator. Experiments on long-term memory benchmarks show that RaMem consistently improves performance over strong memory baselines, with average F1 gains of more than 10% across several backbones.

</details>


### 137. Active Inference as the Test-Time Scaling Law for Physical AI Agents

- **Authors:** Omar Hashash, Christo Kurisummoottil Thomas, Walid Saad, Merouane Debbah, Karl Friston, Adeel Razi
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22813v1](http://arxiv.org/abs/2606.22813v1)
- **PDF:** [https://arxiv.org/pdf/2606.22813v1](https://arxiv.org/pdf/2606.22813v1)
- **Categories:** cs.AI


> **Main contribution** – The paper proposes a test‑time scaling law for embodied AI agents derived from the principle of active inference. It formalizes a dynamic, soft‑Bayesian update of an agent’s policy at deployment, treating the reduction of prediction error as a likelihood and yielding a posterior‑policy that biologically mirrors basal‑ganglia/prefrontal mechanisms.

**Methodology** – The authors cast the in‑situ policy update as an analytically intractable Bayesian inference problem and solve it with a variational‑free‑energy approximation. This yields a tractable algorithm that simultaneously refines the world model and policy using only real‑world experience, without relying on larger networks or more training data.

**Key findings** – In simulated autonomous‑driving experiments, the active‑inference‑based agent outperforms both model‑free Q‑learning and model‑based Bayesian RL, achieving significantly better generalization to out‑of‑distribution scenarios and a 36 % gain in inference efficiency, demonstrating the practical viability of the proposed scaling law for physical AI agents.


<details>
<summary>Abstract</summary>

In this paper, a novel test-time scaling law for physical artificial intelligence (AI) agents is introduced. This scaling law enables physical AI agents to reason with their world models to generalize in unforeseen scenarios at test time. The derived scaling law is grounded in the first principle of active inference, which equips agents with the general objective to survive in the real world, under which their specific task objectives are subsumed. Active inference achieves this by providing the reasoning to resolve prediction errors that arise when the agent encounters unforeseen situations outside its training distribution, enabling generalization in non-stationary environments. The proposed scaling law captures this by dynamically updating the agent's policy with this reasoning at test time. This policy update is modeled as a soft Bayesian inference process in which beliefs about the policy are updated using the reasoning that reduces expected prediction errors under allowable policies as a likelihood. The resulting posterior policy admits a biological interpretation, recovering the scaling mechanism that engages the brain's basal ganglia and prefrontal cortex at test time. To solve this analytically intractable problem, a variational inference solution minimizing free energy bounds is developed. This solution extends to enable learning beyond training by reinforcing new instances, resolved at test time, in both the policy and world model. Unlike existing scaling laws constrained by model size and training data, the derived solution scales with the continuous real-world experience of a physical AI agent. Simulation results on an autonomous driving task demonstrate that the proposed solution outperforms model-free Q-learning and model-based Bayesian reinforcement learning, achieving robust generalization to unforeseen scenarios while improving inference efficiency by over 36%.

</details>


### 138. GRADE: Graph Representation of LLM Agent Dependency and Execution

- **Authors:** Yue Zhao
- **Published:** 2026-06-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.22741v1](http://arxiv.org/abs/2606.22741v1)
- **PDF:** [https://arxiv.org/pdf/2606.22741v1](https://arxiv.org/pdf/2606.22741v1)
- **Categories:** cs.LG


> **Main contribution** – The paper introduces **GRADE**, a unified graph‑based representation for any LLM‑agent execution trace that jointly captures (i) the **execution order** of steps and (ii) the **dependency (resource/knowledge) relations** among them, with dependencies graded by how they are obtained (observed, declared, inferred, or unknown).

**Methodology** – For each run, GRADE builds a two‑layer directed graph: execution edges are extracted directly from the trace, while dependency edges are populated from logs, tool‑call metadata, or inference heuristics and annotated with a confidence grade. The authors evaluate feature‑engineered classifiers built on this graph (and compare them to generic GNNs) across six heterogeneous corpora of LLM agents (tool use, code generation, web browsing).

**Key findings** – The graded dependency layer is a strong predictor of run failure, outperforming simple metrics like run length and maintaining above‑chance performance even in leave‑one‑corpus‑out transfer. Moreover, the execution layer enables precise localization of the faulty step in multi‑agent failures. The study also shows that lightweight, feature‑based models read the dependency layer more reliably than generic graph neural networks, highlighting the practical utility of the GRADE representation for failure diagnosis, and suggesting broader applications in efficiency and robustness optimization for agentic AI.


<details>
<summary>Abstract</summary>

Can one graph represent every kind of LLM agent's run? A trace records what each step did, never what it relied on, the state it read, and the results it reused. GRADE recovers that missing layer: it models any run as one graph over its step nodes with two edge layers, execution edges (what ran in what order) read from the trace for free, and dependency edges (what each step relied on) rarely logged, so each is graded by how it is known, observed, declared, or inferred. One representation, and each layer earns its place. Across six corpora of LLM agents spanning tool use, coding, and the web, the dependency layer can predict failure where run size is weak and, under leave-one-corpus-out transfer, stays above chance on every held-out class while run size fails. Meanwhile, the execution layer localizes the faulting step in a failed multi-agent run. This work also provides a more in-depth analysis of why generic graph neural networks may misread the dependency layer, unlike our feature-based alternative. The same graph representation opens further uses, carrying from failure diagnosis in a single run to efficiency and robustness optimization at scale.

</details>



## Medrxiv (2 papers)


### 1. ALEX: Automatic Language EXplanations for Interpreting Treatment Effects via Multi-Agents

- **Authors:** Lu, M., Kim, C., Kwon, Y., White, N. J., Lee, S.-I.
- **Published:** 2026-06-24
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.04.23.26351510](https://doi.org/10.64898/2026.04.23.26351510)

- **Categories:** health informatics


> The paper introduces **ALEX**, a multi‑agent XAI system that first extracts statistically significant subgroup treatment effects from randomized clinical trials and then feeds these effect‑modifiers to coordinated large‑language‑model agents that generate data‑grounded, natural‑language explanations of why individuals respond differently to a therapy. By integrating causal subgroup discovery with prompt‑engineered LLM reasoning, ALEX was evaluated on five landmark RCTs and achieved higher scores on established treatment‑explanation quality metrics than prior agentic baselines, with blind physician reviewers confirming the clinical relevance of its narratives. Notable case studies show ALEX correctly attributing the ACCORD‑BP vs SPRINT discrepancy to baseline glucose and uncovering age as a novel modifier of tranexamic‑acid efficacy in trauma, demonstrating its potential to translate heterogeneous treatment effects into actionable precision‑medicine insights.


<details>
<summary>Abstract</summary>

Precision medicine requires understanding how general treatment effects from randomized clinical trials should be applied to individual patients. Machine learning methods have shown some promise for estimating patient-level treatment effects, however, their clinical utility remains limited because they often fail to explain why responses to a given treatment vary across individuals. Here we present ALEX, an explainable AI (XAI)-driven, multi-agent framework that addresses this interpretability gap by translating the variables that drive precision predictions into data-grounded, natural-language clinical explanations. ALEX first independently identifies important subgroup treatment effects present in randomized clinical trials and then hands them to large language model (LLM) agents to produce contextualized and scrutinized clinical insights. Across five landmark randomized controlled trials, ALEX outperformed existing agentic methods on treatment explanation quality metrics consistent with the biomedical literature that aligned with blinded reviews by specialist physicians across the United States and Taiwan. In empirical case studies, ALEX provided key interpretable insights, such as identifying baseline glucose level as explaining the divergent findings between the ACCORD-BP and SPRINT trials, and proposed age as a novel and key effect modifier for pre-hospital tranexamic acid efficacy after trauma. These findings suggest that ALEX can help translate treatment effect heterogeneity into clinically grounded explanations that enable precision medicine.

</details>


### 2. Agentic Autodiscovery of Diastolic Dysfunction Phenotypes from Surface Electrocardiogram

- **Authors:** Jamthikar, A. D., Shanmugham, A., Singh, S., Radhakrishnan, A., Dong, J., Maganti, K., Yanamala, N., Sengupta, P.
- **Published:** 2026-06-23
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.06.17.26355897](https://doi.org/10.64898/2026.06.17.26355897)

- **Categories:** cardiovascular medicine


> The paper introduces an **agentic AI auto‑discovery framework** that uses a large‑language‑model‑driven search to automatically design and refine attention‑based multimodal architectures for detecting left‑ventricular diastolic dysfunction (LVDD) from 12‑lead ECGs—or from AI‑generated synthetic tissue‑Doppler imaging (TDI) waveforms. By iteratively proposing, validating, and selecting model configurations via transfer‑learning and multimodal fusion, the system yields two compact models that achieve high discrimination of LVDD severity (AUC 0.83–0.87) and, when applied to >250 k external ECGs, stratify incident heart‑failure mortality with hazard ratios of 5.5–9.5, outperforming a published ECG‑to‑HF convolutional network. The work demonstrates that autonomous architecture search can produce data‑efficient, clinically robust agentic models for ECG‑based cardiac phenotyping, extending diastolic function assessment beyond conventional echocardiography.


<details>
<summary>Abstract</summary>

BackgroundLeft ventricular diastolic dysfunction (LVDD) is a major determinant of heart failure (HF), yet its assessment relies on multiparametric echocardiography, limiting scalability. We previously demonstrated that generative artificial intelligence (AI) can synthesize tissue Doppler imaging (TDI) waveforms from the 12-lead ECG. The growing complexity of candidate architecture creates a need for automated model-discovery frameworks.

ObjectivesTo evaluate agentic AI-based auto-discovery for ECG-based LVDD assessment using either raw ECG or synthetic TDI waveforms.

MethodsTwo attention-based agentic AI architectures were developed using an automated large language model-driven refinement framework that optimized transfer-learning and multimodal architectures through autonomous proposal, validation, and selection of candidate model configurations. Development was performed in 1,011 paired ECG-echocardiography studies and externally validated in 983 patients using two reference frameworks: (i) data-driven phenogroups and (ii) the 2025 ASE Diastolic Function Guidelines. External validation was performed in CODE-15% (n=219,567) for HF-related mortality and EchoNext (n=35,718) for structural heart disease associations.

ResultsDespite the modest cohort size, the ECG-based agentic search achieved area under the receiver operating characteristic curve (AUCs) of 0.87 (95% CI: 0.85-0.89) and 0.83 (95% CI: 0.80-0.86) for phenogroup and guideline-based LVDD severity classification. Corresponding AUCs for the synthetic TDI-based model were 0.82 (95% CI: 0.80-0.85) and 0.80 (95% CI: 0.77-0.84), respectively. In large-scale external validation, both models stratified incident HF mortality with subdistribution hazard ratios ranging 5.5 to 9.5 (Grays p<0.001 for all). Time-dependent discrimination for incident HF mortality exceeded a publicly available convolutional neural network model (ECG2HF) ({Delta}AUC range: +0.14 to +0.20). Both models demonstrated consistent associations with structural heart disease outcomes.

ConclusionsAgentic auto-discovery enabled data-efficient assessment of LVDD from surface ECG by combining physiologically informed transfer learning with autonomous architecture optimization, achieving robust external generalizability. This approach may facilitate broader access to diastolic function assessment beyond conventional echocardiography.

</details>



## Biorxiv (1 papers)


### 1. biomeStat: Using Agentic AI for Scalable Genomic Epidemiology Demonstrated Through End-to-End Analysis of 1,000 Asian Dengue Virus Genomes

- **Authors:** Ariyaratne, D., Somaratna, N., Malavige, G. N.
- **Published:** 2026-06-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.10.731380](https://doi.org/10.64898/2026.06.10.731380)

- **Categories:** bioinformatics


> **Main contribution:** The paper introduces **biomeStat**, a deterministic, autonomous AI‑agent that translates natural‑language research intents into reproducible, sandboxed bioinformatics pipelines, dynamically provisioning CPU/GPU resources and orchestrating established genomic‑epidemiology tools without requiring user‑level command‑line expertise.  

**Methodology:** biomeStat generates and executes code for each step of a standard workflow (quality control, alignment, phylogeny with IQ‑TREE/TreeTime, Bayesian phylodynamics with BEAST2 on an NVIDIA H200 GPU, selection analysis with HyPhy, and structural mapping in PyMOL), managing data flow and environment isolation while logging all parameters to ensure traceability.  

**Key findings:** In a fully autonomous end‑to‑end run on 1,000 Asian Dengue virus genomes, biomeStat completed the entire analysis in <24 h, reproducing known epidemiological dynamics (Rₑ≈1.0), uncovering 1,869 putative immune‑escape sites colocated with B‑ and T‑cell epitopes, and confirming the absolute conservation of 176 drug‑target residues, thereby compressing weeks of expert labor into a single, transparent session and demonstrating the practical scalability of agentic AI for large‑scale genomic epidemiology.


<details>
<summary>Abstract</summary>

Genomic epidemiology workflows typically require expert curation of multiple specialized tools, extensive manual parameter tuning, and access to heterogeneous compute infrastructure. While standard generative AI models often hallucinate in complex biological domains, we introduce biomeStat: an autonomous AI agent that functions as a strict deterministic orchestrator. By automatically writing code to execute established bioinformatics tools in sandboxed environments, biomeStat dynamically provisions compute resources (CPU and GPU) and guarantees reproducibility, making it immediately useful for scientists without requiring command-line expertise.

To demonstrate the platform, we performed a fully autonomous genomic epidemiology and structural analysis of 1,000 Dengue virus (DENV) genomes sampled from 16 Asian countries between 2000 and 2025. The agent seamlessly orchestrated phylogenetic reconstruction (IQ-TREE, TreeTime), Bayesian phylodynamics (BEAST2 via NVIDIA H200 GPU), selection pressure analysis (HyPhy), and structural mapping (PyMOL). The analysis was completed in under 24 hours of wall-clock time, revealing endemic stability (R_e [~]1.0) and identifying 1,869 candidate immune escape sites structurally colocalized with B-cell and T-cell epitopes. Furthermore, the agent validated 176 highly conserved drug target residues across the viral replication complex, confirming that resistance-associated positions for emerging antivirals JNJ-1802 and NITD-688 remain absolutely conserved across all four serotypes. By bridging the gap between natural language intent and deterministic computational execution, biomeStat reduces weeks of expert effort into a single-session analysis with full methodological transparency.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*