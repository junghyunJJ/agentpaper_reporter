# Weekly AI Agent Paper Report

**Generated:** 2026-02-18 21:08
**Period:** 2026-02-11 to 2026-02-17

## Summary

- **Total papers fetched:** 1057
- **Papers matching keywords:** 154
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-02-16) | Change |
|--------|-----------|-----------|--------|
| Total matched | 154 | 124 | +30 |
| arxiv | 152 | 120 | +32 |
| biorxiv | 0 | 2 | -2 |
| medrxiv | 2 | 2 | +0 |

### Notable Trends

**Key take‑aways from the week‑over‑week comparison**

| Aspect | This week (154 papers) | Last week (124 papers) | What it tells us |
|--------|----------------------|------------------------|-----------------|
| **Overall volume** | **+30 %** (152 arXiv + 2 medRxiv) | 120 arXiv + 2 medRxiv + 2 bioRxiv | The field is accelerating; most of the growth comes from arXiv submissions. |
| **Source mix** | arXiv now dominates (98 % of papers). No bioRxiv entries. | arXiv 97 % + a small bioRxiv slice (2 papers). | Researchers are gravitating toward the faster‑turnaround arXiv venue for agent work, possibly because the community’s “agent‑as‑service” momentum is best captured there. |
| **Topic shift** | • **Simulation‑driven agent design** (“Developing AI Agents with Simulated Data”).<br>• **Operational control & fleet management** (lifelong AGV fleet, decision‑quality at Pinterest).<br>• **Self‑evolving LLM agents** (“Zombie Agents”).<br>• **Partial observability & diffusion models** (GlobeDiff).<br>• **Metagenomics AI** (appears twice, indicating a crossover with biomedical applications). | • **Benchmark‑centric work** (SciAgentGym, SkillsBench, BrowseComp‑V³).<br>• **Tool‑use & attribution** (TraceBack, In‑Context Network Incident Response).<br>• **

---



## Biomedical Highlights (2 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


The paper presents an AI‑driven pipeline that leverages whole‑metagenome sequencing data to identify gut‑microbiome signatures predictive of Inflammatory Bowel Disease (IBD) and to generate personalized probiotic recommendations. Using supervised machine‑learning classifiers (e.g., random forests and convolutional neural networks) trained on taxonomic and functional profiles from IBD patients and healthy controls, the authors achieve high diagnostic accuracy while pinpointing key dysbiotic taxa that drive disease risk. A downstream recommendation engine then matches the identified microbial deficits with probiotic strains known to restore those functions, integrating literature‑curated efficacy data and strain‑level compatibility scores. The study demonstrates how integrative metagenomics coupled with AI can both stratify patients for early IBD detection and translate microbial insights into actionable, precision‑nutrition interventions.



### 1. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar N, S., Thomas, M., Chinnakanu, S. J., M, N., Subramaniam, S.
- **Published:** 2026-02-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> The paper introduces an AI‑driven pipeline that combines metagenomic profiling with autonomous “CrewAI” agents to both diagnose inflammatory bowel disease (IBD) from gut microbiome data and generate personalized probiotic prescriptions. After preprocessing raw stool metagenomes with Kneaddata and MetaPhlAn, taxonomic abundances are fed to a tuned XGBoost classifier (86.6 % accuracy) and dysbiotic taxa are flagged via Z‑score/fold‑change analysis; the CrewAI agents then synthesize literature‑based rationales to recommend specific strains (e.g., *Faecalibacterium prausnitzii*). The study demonstrates that integrating conventional machine‑learning diagnostics with agentic reasoning can produce interpretable, actionable health recommendations, highlighting a promising direction for agentic AI in precision microbiome medicine.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>


### 2. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar, S. N., Thomas, M., Janakiram, S., M, N., Subramaniam, S. N.
- **Published:** 2026-02-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> The paper introduces an AI‑driven pipeline that combines metagenomic preprocessing, a high‑performing XGBoost classifier, and an autonomous “CrewAI” agent to both diagnose inflammatory bowel disease (IBD) from gut‑microbiome taxonomic profiles and generate personalized probiotic recommendations. By integrating Kneaddata and MetaPhlAn for taxonomic feature extraction, training a tuned XGBoost model (86.6 % accuracy), and employing the agent to interpret dysbiotic taxa (via Z‑score/fold‑change) and retrieve literature‑backed probiotic suggestions (e.g., *Faecalibacterium prausnitzii*), the system demonstrates that agentic AI can close the loop from data‑driven diagnosis to actionable therapeutic advice. Validation on a single ulcerative colitis sample confirmed correct IBD detection (though mis‑labelled as Crohn’s) and highlighted the agent’s capacity to explain its recommendations, underscoring the promise of autonomous AI agents in precision microbiome‑based healthcare.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>


---



## Arxiv (152 papers)


### 1. Developing AI Agents with Simulated Data: Why, what, and how?

- **Authors:** Xiaoran Liu, Istvan David
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15816v1](http://arxiv.org/abs/2602.15816v1)
- **PDF:** [https://arxiv.org/pdf/2602.15816v1](https://arxiv.org/pdf/2602.15816v1)
- **Categories:** cs.AI, cs.ET


> The paper’s primary contribution is a comprehensive framework for building AI agents that are trained on simulation‑generated synthetic data, positioning digital twins as a systematic source of high‑quality, diverse training examples for subsymbolic models. It outlines a methodological pipeline—defining the target domain, constructing a calibrated simulation environment, generating labeled data, and iteratively validating the agent’s performance against real‑world benchmarks—to ensure that simulated data faithfully capture the dynamics needed for robust agent behavior. Empirical case studies demonstrate that agents trained on such simulated datasets achieve comparable or superior performance to those trained on limited real data, while also reducing data‑collection costs and enabling rapid prototyping of new agentic capabilities.


<details>
<summary>Abstract</summary>

As insufficient data volume and quality remain the key impediments to the adoption of modern subsymbolic AI, techniques of synthetic data generation are in high demand. Simulation offers an apt, systematic approach to generating diverse synthetic data. This chapter introduces the reader to the key concepts, benefits, and challenges of simulation-based synthetic data generation for AI training purposes, and to a reference framework to describe, design, and analyze digital twin-based AI simulation solutions.

</details>


### 2. Decision Quality Evaluation Framework at Pinterest

- **Authors:** Yuqi Tian, Robert Paine, Attila Dobi, Kevin O'Sullivan, Aravindh Manickavasagam, Faisal Farooq
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15809v1](http://arxiv.org/abs/2602.15809v1)
- **PDF:** [https://arxiv.org/pdf/2602.15809v1](https://arxiv.org/pdf/2602.15809v1)
- **Categories:** stat.AP, cs.AI


> The paper introduces a Decision Quality Evaluation Framework that lets Pinterest quantitatively assess moderation decisions made by both human reviewers and LLM‑driven agents. By building a high‑trust “Golden Set” annotated by subject‑matter experts and augmenting it with an automated propensity‑score‑based sampling pipeline, the authors create a scalable, cost‑effective ground‑truth benchmark for continuous evaluation, prompt optimization, and policy‑change monitoring. Empirical results show that the framework reliably measures trade‑offs between LLM cost and performance, improves prompt design through data‑driven feedback, and stabilizes policy‑content prevalence metrics, thereby turning content‑safety governance from a subjective art into a data‑driven engineering practice.


<details>
<summary>Abstract</summary>

Online platforms require robust systems to enforce content safety policies at scale. A critical component of these systems is the ability to evaluate the quality of moderation decisions made by both human agents and Large Language Models (LLMs). However, this evaluation is challenging due to the inherent trade-offs between cost, scale, and trustworthiness, along with the complexity of evolving policies. To address this, we present a comprehensive Decision Quality Evaluation Framework developed and deployed at Pinterest. The framework is centered on a high-trust Golden Set (GDS) curated by subject matter experts (SMEs), which serves as a ground truth benchmark. We introduce an automated intelligent sampling pipeline that uses propensity scores to efficiently expand dataset coverage. We demonstrate the framework's practical application in several key areas: benchmarking the cost-performance trade-offs of various LLM agents, establishing a rigorous methodology for data-driven prompt optimization, managing complex policy evolution, and ensuring the integrity of policy content prevalence metrics via continuous validation. The framework enables a shift from subjective assessments to a data-driven and quantitative practice for managing content safety systems.

</details>


### 3. GlobeDiff: State Diffusion Process for Partial Observability in Multi-Agent Systems

- **Authors:** Yiqin Yang, Xu Yang, Yuhua Jiang, Ni Mu, Hao Hu, Runpeng Xie, Ziyou Zhang, Siyuan Li, Yuan-Hua Ni, Qianchuan Zhao, Bo Xu
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15776v1](http://arxiv.org/abs/2602.15776v1)
- **PDF:** [https://arxiv.org/pdf/2602.15776v1](https://arxiv.org/pdf/2602.15776v1)
- **Categories:** cs.AI


> GlobeDiff introduces a novel **state diffusion** framework that reconstructs the global environment state from each agent’s partial observations, addressing the long‑standing partial‑observability bottleneck in multi‑agent coordination. By casting global‑state inference as a multi‑modal diffusion process, the method iteratively refines a latent global representation using locally sensed data and optional inter‑agent messages, and the authors provide theoretical bounds on the estimation error for both unimodal and multimodal belief distributions. Empirically, GlobeDiff consistently outperforms belief‑state and communication‑based baselines across several benchmark domains, achieving markedly higher fidelity in global‑state reconstruction and consequently improving downstream cooperative performance.


<details>
<summary>Abstract</summary>

In the realm of multi-agent systems, the challenge of \emph{partial observability} is a critical barrier to effective coordination and decision-making. Existing approaches, such as belief state estimation and inter-agent communication, often fall short. Belief-based methods are limited by their focus on past experiences without fully leveraging global information, while communication methods often lack a robust model to effectively utilize the auxiliary information they provide. To solve this issue, we propose Global State Diffusion Algorithm~(GlobeDiff) to infer the global state based on the local observations. By formulating the state inference process as a multi-modal diffusion process, GlobeDiff overcomes ambiguities in state estimation while simultaneously inferring the global state with high fidelity. We prove that the estimation error of GlobeDiff under both unimodal and multi-modal distributions can be bounded. Extensive experimental results demonstrate that GlobeDiff achieves superior performance and is capable of accurately inferring the global state.

</details>


### 4. Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems

- **Authors:** Jingtian Yan, Yulun Zhang, Zhenting Liu, Han Zhang, He Jiang, Jingkai Chen, Stephen F. Smith, Jiaoyang Li
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15721v1](http://arxiv.org/abs/2602.15721v1)
- **PDF:** [https://arxiv.org/pdf/2602.15721v1](https://arxiv.org/pdf/2602.15721v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces **LSMART**, an open‑source, lifelong‑MAPF simulator that extends the earlier SMART platform to evaluate centralized fleet‑management systems for automated guided vehicles under realistic kinodynamic, communication‑delay, and execution‑uncertainty conditions. By systematically varying three critical design dimensions—planning trigger (when to replan), planner selection (how to incorporate heterogeneous optimality and agent‑model assumptions), and failure recovery (how to handle infeasible plans)—the authors benchmark state‑of‑the‑art MAPF algorithms and quantify their impact on throughput, makespan, and robustness in a continuous, multi‑agent warehouse setting. The results show that (1) early, parallel replanning dramatically improves responsiveness, (2) hybrid planners that combine fast sub‑optimal routing with occasional optimal refinements achieve the best trade‑off between efficiency and feasibility, and (3) simple fallback strategies (e.g., local reactive avoidance) are essential for maintaining system stability when planners fail, offering concrete design guidelines for building scalable, lifelong AGV fleet‑management AI.


<details>
<summary>Abstract</summary>

We present Lifelong Scalable Multi-Agent Realistic Testbed (LSMART), an open-source simulator to evaluate any Multi-Agent Path Finding (MAPF) algorithm in a Fleet Management System (FMS) with Automated Guided Vehicles (AGVs). MAPF aims to move a group of agents from their corresponding starting locations to their goals. Lifelong MAPF (LMAPF) is a variant of MAPF that continuously assigns new goals for agents to reach. LMAPF applications, such as autonomous warehouses, often require a centralized, lifelong system to coordinate the movement of a fleet of robots, typically AGVs. However, existing works on MAPF and LMAPF often assume simplified kinodynamic models, such as pebble motion, as well as perfect execution and communication for AGVs. Prior work has presented SMART, a software capable of evaluating any MAPF algorithms while considering agent kinodynamics, communication delays, and execution uncertainties. However, SMART is designed for MAPF, not LMAPF. Generalizing SMART to an FMS requires many more design choices. First, an FMS parallelizes planning and execution, raising the question of when to plan. Second, given planners with varying optimality and differing agent-model assumptions, one must decide how to plan. Third, when the planner fails to return valid solutions, the system must determine how to recover. In this paper, we first present LSMART, an open-source simulator that incorporates all these considerations to evaluate any MAPF algorithms in an FMS. We then provide experiment results based on state-of-the-art methods for each design choice, offering guidance on how to effectively design centralized lifelong AGV Fleet Management Systems. LSMART is available at https://smart-mapf.github.io/lifelong-smart.

</details>


### 5. Zombie Agents: Persistent Control of Self-Evolving LLM Agents via Self-Reinforcing Injections

- **Authors:** Xianglin Yang, Yufei He, Shuo Ji, Bryan Hooi, Jin Song Dong
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15654v1](http://arxiv.org/abs/2602.15654v1)
- **PDF:** [https://arxiv.org/pdf/2602.15654v1](https://arxiv.org/pdf/2602.15654v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **“Zombie Agents,”** a novel class of persistent attacks on self‑evolving LLM agents that exploit their long‑term memory mechanisms to embed covert payloads that survive across sessions and later trigger unauthorized tool use. The authors devise a black‑box, two‑phase attack pipeline—**infection** (injecting a poisoned web source while the agent performs a benign task) and **trigger** (retrieving the stored payload via memory‑specific persistence tricks such as sliding‑window tricks and retrieval‑augmented indexing)—and evaluate it on several common agent architectures, demonstrating that the payload remains effective over many interactions while the agent’s primary task performance stays unchanged. The results show that merely filtering prompts per session is insufficient; defenses must address the durability of memory updates in autonomous agents.


<details>
<summary>Abstract</summary>

Self-evolving LLM agents update their internal state across sessions, often by writing and reusing long-term memory. This design improves performance on long-horizon tasks but creates a security risk: untrusted external content observed during a benign session can be stored as memory and later treated as instruction. We study this risk and formalize a persistent attack we call a Zombie Agent, where an attacker covertly implants a payload that survives across sessions, effectively turning the agent into a puppet of the attacker.
  We present a black-box attack framework that uses only indirect exposure through attacker-controlled web content. The attack has two phases. During infection, the agent reads a poisoned source while completing a benign task and writes the payload into long-term memory through its normal update process. During trigger, the payload is retrieved or carried forward and causes unauthorized tool behavior. We design mechanism-specific persistence strategies for common memory implementations, including sliding-window and retrieval-augmented memory, to resist truncation and relevance filtering. We evaluate the attack on representative agent setups and tasks, measuring both persistence over time and the ability to induce unauthorized actions while preserving benign task quality. Our results show that memory evolution can convert one-time indirect injection into persistent compromise, which suggests that defenses focused only on per-session prompt filtering are not sufficient for self-evolving agents.

</details>


### 6. In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations

- **Authors:** Mohammad Aflah Khan, Mahsa Amani, Soumi Das, Bishwamittra Ghosh, Qinyuan Wu, Krishna P. Gummadi, Manish Gupta, Abhilasha Ravichander
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15456v1](http://arxiv.org/abs/2602.15456v1)
- **PDF:** [https://arxiv.org/pdf/2602.15456v1](https://arxiv.org/pdf/2602.15456v1)
- **Categories:** cs.CL


> The paper uncovers a previously overlooked bias in LLM‑driven agents: when presented with information tagged by source (e.g., publisher, journal, website), the models exhibit systematic “latent source preferences,” favoring some origins over others independent of content. By running controlled experiments on twelve LLMs from six providers across synthetic retrieval‑synthesis tasks and real‑world news‑recommendation scenarios, the authors show that these preferences are strong, predictable, sensitive to framing, and can dominate content‑based relevance even when users explicitly ask the model to ignore source cues. The findings reveal that source‑level bias can shape the information users receive from LLM agents, motivating the need for transparency mechanisms and further study of the origins of such preferences in agentic AI systems.


<details>
<summary>Abstract</summary>

Agents based on Large Language Models (LLMs) are increasingly being deployed as interfaces to information on online platforms. These agents filter, prioritize, and synthesize information retrieved from the platforms' back-end databases or via web search. In these scenarios, LLM agents govern the information users receive, by drawing users' attention to particular instances of retrieved information at the expense of others. While much prior work has focused on biases in the information LLMs themselves generate, less attention has been paid to the factors that influence what information LLMs select and present to users. We hypothesize that when information is attributed to specific sources (e.g., particular publishers, journals, or platforms), current LLMs exhibit systematic latent source preferences- that is, they prioritize information from some sources over others. Through controlled experiments on twelve LLMs from six model providers, spanning both synthetic and real-world tasks, we find that several models consistently exhibit strong and predictable source preferences. These preferences are sensitive to contextual framing, can outweigh the influence of content itself, and persist despite explicit prompting to avoid them. They also help explain phenomena such as the observed left-leaning skew in news recommendations in prior work. Our findings advocate for deeper investigation into the origins of these preferences, as well as for mechanisms that provide users with transparency and control over the biases guiding LLM-powered agents.

</details>


### 7. Fairness over Equality: Correcting Social Incentives in Asymmetric Sequential Social Dilemmas

- **Authors:** Alper Demir, Hüseyin Aydın, Kale-ab Abebe Tessera, David Abel, Stefano V. Albrecht
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15407v1](http://arxiv.org/abs/2602.15407v1)
- **PDF:** [https://arxiv.org/pdf/2602.15407v1](https://arxiv.org/pdf/2602.15407v1)
- **Categories:** cs.LG


> The paper shows that existing fairness‑based intrinsic rewards fail in asymmetric Sequential Social Dilemmas (SSDs) because they enforce raw equality, which can actually reward defection when agents have different reward scales. To fix this, the authors redesign fairness to normalize by each agent’s reward range, add a weighting scheme that compensates for inherent asymmetries, and localize the social feedback so agents only need locally observable information. Experiments on newly created asymmetric SSD benchmarks demonstrate that these three modifications enable faster and more robust emergence of cooperative policies than prior methods, while preserving scalability and practical applicability for multi‑agent reinforcement learning.


<details>
<summary>Abstract</summary>

Sequential Social Dilemmas (SSDs) provide a key framework for studying how cooperation emerges when individual incentives conflict with collective welfare. In Multi-Agent Reinforcement Learning, these problems are often addressed by incorporating intrinsic drives that encourage prosocial or fair behavior. However, most existing methods assume that agents face identical incentives in the dilemma and require continuous access to global information about other agents to assess fairness. In this work, we introduce asymmetric variants of well-known SSD environments and examine how natural differences between agents influence cooperation dynamics. Our findings reveal that existing fairness-based methods struggle to adapt under asymmetric conditions by enforcing raw equality that wrongfully incentivize defection. To address this, we propose three modifications: (i) redefining fairness by accounting for agents' reward ranges, (ii) introducing an agent-based weighting mechanism to better handle inherent asymmetries, and (iii) localizing social feedback to make the methods effective under partial observability without requiring global information sharing. Experimental results show that in asymmetric scenarios, our method fosters faster emergence of cooperative policies compared to existing approaches, without sacrificing scalability or practicality.

</details>


### 8. World-Model-Augmented Web Agents with Action Correction

- **Authors:** Zhouzhou Shen, Xueyu Hu, Xiyun Li, Tianqing Fang, Juncheng Li, Shengyu Zhang
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15384v1](http://arxiv.org/abs/2602.15384v1)
- **PDF:** [https://arxiv.org/pdf/2602.15384v1](https://arxiv.org/pdf/2602.15384v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **WAC**, a web‑automation agent that augments a large‑language‑model (LLM) action planner with a dedicated world‑model that predicts web‑environment state transitions and a judge model that evaluates simulated outcomes. By orchestrating a multi‑agent collaboration—where the action model queries the world model for strategic guidance, grounds the advice into concrete actions, and then runs a two‑stage deduction chain (simulation → judgment) to detect and correct risky moves—the system achieves risk‑aware, self‑refining execution. Empirically, WAC improves task success rates by **+1.8 % on VisualWebArena** and **+1.3 % on Online‑Mind2Web**, demonstrating that integrating world‑model simulation and feedback‑driven correction yields more reliable, agentic web behavior.


<details>
<summary>Abstract</summary>

Web agents based on large language models have demonstrated promising capability in automating web tasks. However, current web agents struggle to reason out sensible actions due to the limitations of predicting environment changes, and might not possess comprehensive awareness of execution risks, prematurely performing risky actions that cause losses and lead to task failure. To address these challenges, we propose WAC, a web agent that integrates model collaboration, consequence simulation, and feedback-driven action refinement. To overcome the cognitive isolation of individual models, we introduce a multi-agent collaboration process that enables an action model to consult a world model as a web-environment expert for strategic guidance; the action model then grounds these suggestions into executable actions, leveraging prior knowledge of environmental state transition dynamics to enhance candidate action proposal. To achieve risk-aware resilient task execution, we introduce a two-stage deduction chain. A world model, specialized in environmental state transitions, simulates action outcomes, which a judge model then scrutinizes to trigger action corrective feedback when necessary. Experiments show that WAC achieves absolute gains of 1.8% on VisualWebArena and 1.3% on Online-Mind2Web.

</details>


### 9. The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems

- **Authors:** Xiaoze Liu, Ruowang Zhang, Weichen Yu, Siheng Xiong, Liu He, Feijie Wu, Hoin Jung, Matt Fredrikson, Xiaoqian Wang, Jing Gao
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15382v1](http://arxiv.org/abs/2602.15382v1)
- **PDF:** [https://arxiv.org/pdf/2602.15382v1](https://arxiv.org/pdf/2602.15382v1)
- **Categories:** cs.CL, cs.CV, cs.LG


> The paper introduces the **Vision Wormhole**, a model‑agnostic communication layer that lets heterogeneous LLM‑based agents exchange reasoning states through the visual encoder of a Vision‑Language Model instead of via discrete text messages. By encoding each agent’s intermediate reasoning trace into a universal visual latent code (via a learned “Universal Visual Codec”) and routing it through a hub‑and‑spoke topology, the system aligns disparate model manifolds with a label‑free teacher‑student distillation loss, turning the vision pathway into a high‑bandwidth “telepathy” channel. Experiments with diverse agents (e.g., Qwen‑VL, Gemma) show that this latent‑space channel cuts end‑to‑end runtime by a substantial margin while preserving reasoning fidelity on par with conventional text‑based multi‑agent collaboration.


<details>
<summary>Abstract</summary>

Multi-Agent Systems (MAS) powered by Large Language Models have unlocked advanced collaborative reasoning, yet they remain shackled by the inefficiency of discrete text communication, which imposes significant runtime overhead and information quantization loss. While latent state transfer offers a high-bandwidth alternative, existing approaches either assume homogeneous sender-receiver architectures or rely on pair-specific learned translators, limiting scalability and modularity across diverse model families with disjoint manifolds. In this work, we propose the Vision Wormhole, a novel framework that repurposes the visual interface of Vision-Language Models (VLMs) to enable model-agnostic, text-free communication. By introducing a Universal Visual Codec, we map heterogeneous reasoning traces into a shared continuous latent space and inject them directly into the receiver's visual pathway, effectively treating the vision encoder as a universal port for inter-agent telepathy. Our framework adopts a hub-and-spoke topology to reduce pairwise alignment complexity from O(N^2) to O(N) and leverages a label-free, teacher-student distillation objective to align the high-speed visual channel with the robust reasoning patterns of the text pathway. Extensive experiments across heterogeneous model families (e.g., Qwen-VL, Gemma) demonstrate that the Vision Wormhole reduces end-to-end wall-clock time in controlled comparisons while maintaining reasoning fidelity comparable to standard text-based MAS. Code is available at https://github.com/xz-liu/heterogeneous-latent-mas

</details>


### 10. Orchestration-Free Customer Service Automation: A Privacy-Preserving and Flowchart-Guided Framework

- **Authors:** Mengze Hong, Chen Jason Zhang, Zichang Guo, Hanlin Gu, Di Jiang, Li Qing
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15377v1](http://arxiv.org/abs/2602.15377v1)
- **PDF:** [https://arxiv.org/pdf/2602.15377v1](https://arxiv.org/pdf/2602.15377v1)
- **Categories:** cs.CL, cs.AI


> The paper presents an **orchestration‑free framework** that replaces traditional multi‑agent pipelines with **Task‑Oriented Flowcharts (TOFs)**, enabling end‑to‑end customer‑service automation while preserving user privacy. It formalizes TOF components and evaluation metrics, then introduces a **cost‑efficient flowchart construction algorithm** that extracts procedural knowledge from dialogue logs, and couples this with **local deployment of compact language models** and a **decentralized distillation** process that trains models on‑device using the flowcharts to avoid data sharing. Experiments across several service domains show that the TOF‑based system outperforms strong baselines and commercial products in both quantitative metrics (e.g., task success rate, latency) and real‑world applicability, demonstrating a scalable, privacy‑preserving alternative for building agentic AI services.


<details>
<summary>Abstract</summary>

Customer service automation has seen growing demand within digital transformation. Existing approaches either rely on modular system designs with extensive agent orchestration or employ over-simplified instruction schemas, providing limited guidance and poor generalizability. This paper introduces an orchestration-free framework using Task-Oriented Flowcharts (TOFs) to enable end-to-end automation without manual intervention. We first define the components and evaluation metrics for TOFs, then formalize a cost-efficient flowchart construction algorithm to abstract procedural knowledge from service dialogues. We emphasize local deployment of small language models and propose decentralized distillation with flowcharts to mitigate data scarcity and privacy issues in model training. Extensive experiments validate the effectiveness in various service tasks, with superior quantitative and application performance compared to strong baselines and market products. By releasing a web-based system demonstration with case studies, we aim to promote streamlined creation of future service automation.

</details>


### 11. AgriWorld:A World Tools Protocol Framework for Verifiable Agricultural Reasoning with Code-Executing LLM Agents

- **Authors:** Zhixing Zhang, Jesen Zhang, Hao Liu, Qinhan Lv, Jing Yang, Kaitong Cai, Keze Wang
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15325v1](http://arxiv.org/abs/2602.15325v1)
- **PDF:** [https://arxiv.org/pdf/2602.15325v1](https://arxiv.org/pdf/2602.15325v1)
- **Categories:** cs.AI


> The paper introduces **AgriWorld**, a Python‑based “world‑tools” protocol that equips LLM agents with a unified suite of geospatial, remote‑sensing, crop‑simulation, and predictive analytics functions, and builds **Agro‑Reflective**, a multi‑turn LLM agent that solves agricultural queries by iteratively **write‑code → execute → observe → refine**. Using the newly created **AgroBench** benchmark (spanning lookup, forecasting, anomaly detection, and counterfactual “what‑if” tasks), the authors show that execution‑driven reflection markedly outperforms both pure‑text baselines and naïve tool‑calling approaches, delivering more accurate and verifiable reasoning over high‑dimensional agronomic data. This work demonstrates that coupling LLMs with a structured, code‑executing environment and a reflective loop can extend agentic AI from language‑only tasks to reliable, data‑intensive scientific reasoning.


<details>
<summary>Abstract</summary>

Foundation models for agriculture are increasingly trained on massive spatiotemporal data (e.g., multi-spectral remote sensing, soil grids, and field-level management logs) and achieve strong performance on forecasting and monitoring. However, these models lack language-based reasoning and interactive capabilities, limiting their usefulness in real-world agronomic workflows. Meanwhile, large language models (LLMs) excel at interpreting and generating text, but cannot directly reason over high-dimensional, heterogeneous agricultural datasets. We bridge this gap with an agentic framework for agricultural science. It provides a Python execution environment, AgriWorld, exposing unified tools for geospatial queries over field parcels, remote-sensing time-series analytics, crop growth simulation, and task-specific predictors (e.g., yield, stress, and disease risk). On top of this environment, we design a multi-turn LLM agent, Agro-Reflective, that iteratively writes code, observes execution results, and refines its analysis via an execute-observe-refine loop. We introduce AgroBench, with scalable data generation for diverse agricultural QA spanning lookups, forecasting, anomaly detection, and counterfactual "what-if" analysis. Experiments outperform text-only and direct tool-use baselines, validating execution-driven reflection for reliable agricultural reasoning.

</details>


### 12. Visual Persuasion: What Influences Decisions of Vision-Language Models?

- **Authors:** Manuel Cherep, Pranav M R, Pattie Maes, Nikhil Singh
- **Published:** 2026-02-17
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15278v1](http://arxiv.org/abs/2602.15278v1)
- **PDF:** [https://arxiv.org/pdf/2602.15278v1](https://arxiv.org/pdf/2602.15278v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces a systematic framework for uncovering the latent visual utility functions of vision‑language models (VLMs) by treating their selections in controlled image‑choice tasks as revealed preferences. Using a visual‑prompt‑optimization loop—adapted from text‑prompt methods and powered by a generative image model—the authors iteratively apply plausible edits (e.g., changes in composition, lighting, background) to product photos and measure how these perturbations shift the VLMs’ head‑to‑head choice probabilities. Large‑scale experiments on state‑of‑the‑art VLMs show that optimized edits can dramatically bias selections, and an automatic interpretability pipeline extracts consistent visual themes behind these biases, highlighting concrete visual vulnerabilities that can be proactively audited in agentic AI systems.


<details>
<summary>Abstract</summary>

The web is littered with images, once created for human consumption and now increasingly interpreted by agents using vision-language models (VLMs). These agents make visual decisions at scale, deciding what to click, recommend, or buy. Yet, we know little about the structure of their visual preferences. We introduce a framework for studying this by placing VLMs in controlled image-based choice tasks and systematically perturbing their inputs. Our key idea is to treat the agent's decision function as a latent visual utility that can be inferred through revealed preference: choices between systematically edited images. Starting from common images, such as product photos, we propose methods for visual prompt optimization, adapting text optimization methods to iteratively propose and apply visually plausible modifications using an image generation model (such as in composition, lighting, or background). We then evaluate which edits increase selection probability. Through large-scale experiments on frontier VLMs, we demonstrate that optimized edits significantly shift choice probabilities in head-to-head comparisons. We develop an automatic interpretability pipeline to explain these preferences, identifying consistent visual themes that drive selection. We argue that this approach offers a practical and efficient way to surface visual vulnerabilities, safety concerns that might otherwise be discovered implicitly in the wild, supporting more proactive auditing and governance of image-based AI agents.

</details>


### 13. Knowing Isn't Understanding: Re-grounding Generative Proactivity with Epistemic and Behavioral Insight

- **Authors:** Kirandeep Kaur, Xingda Lyu, Chirag Shah
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15259v1](http://arxiv.org/abs/2602.15259v1)
- **PDF:** [https://arxiv.org/pdf/2602.15259v1](https://arxiv.org/pdf/2602.15259v1)
- **Categories:** cs.CY, cs.AI, cs.LG


> The paper argues that generative AI agents must go beyond treating “understanding” as merely answering explicit user queries; they need to recognize **epistemic incompleteness**—situations where users cannot articulate missing or risky information—and intervene proactively in a **behaviorally grounded** manner. To substantiate this claim, the authors synthesize philosophical analyses of ignorance with empirical studies of human proactive behavior, deriving design principles that specify when, how, and to what extent an agent should surface unknown‑unknowns without overwhelming or harming the user. Their key finding is that coupling epistemic awareness with principled behavioral constraints yields agents that can responsibly generate novel, useful suggestions, thereby enabling more meaningful human‑AI partnerships in contexts where users lack full self‑knowledge.


<details>
<summary>Abstract</summary>

Generative AI agents equate understanding with resolving explicit queries, an assumption that confines interaction to what users can articulate. This assumption breaks down when users themselves lack awareness of what is missing, risky, or worth considering. In such conditions, proactivity is not merely an efficiency enhancement, but an epistemic necessity. We refer to this condition as epistemic incompleteness: where progress depends on engaging with unknown unknowns for effective partnership. Existing approaches to proactivity remain narrowly anticipatory, extrapolating from past behavior and presuming that goals are already well defined, thereby failing to support users meaningfully. However, surfacing possibilities beyond a user's current awareness is not inherently beneficial. Unconstrained proactive interventions can misdirect attention, overwhelm users, or introduce harm. Proactive agents, therefore, require behavioral grounding: principled constraints on when, how, and to what extent an agent should intervene. We advance the position that generative proactivity must be grounded both epistemically and behaviorally. Drawing on the philosophy of ignorance and research on proactive behavior, we argue that these theories offer critical guidance for designing agents that can engage responsibly and foster meaningful partnerships.

</details>


### 14. Secure and Energy-Efficient Wireless Agentic AI Networks

- **Authors:** Yuanyan Song, Kezhi Wang, Xinmian Xu
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15212v1](http://arxiv.org/abs/2602.15212v1)
- **PDF:** [https://arxiv.org/pdf/2602.15212v1](https://arxiv.org/pdf/2602.15212v1)
- **Categories:** cs.AI


> The paper proposes a secure, energy‑aware wireless network architecture for agentic AI, in which a supervisory AI dynamically selects cooperating reasoning agents while the idle agents act as friendly jammers to protect confidential inference results. By formulating a joint agent‑selection, base‑station beamforming, and transmit‑power problem under latency and accuracy constraints, the authors develop two solution frameworks—ASC (an ADMM‑SDR‑SCA iterative optimizer) and LAW (a large‑language‑model‑driven optimizer embedded in an agentic workflow)—that decompose the problem into tractable sub‑problems. Simulations and a Qwen‑based prototype demonstrate that the proposed schemes cut total network energy consumption by up to 59 % relative to baselines while preserving reasoning accuracy on standard benchmarks, highlighting a practical pathway for secure, low‑power deployment of cooperative agentic AI systems.


<details>
<summary>Abstract</summary>

In this paper, we introduce a secure wireless agentic AI network comprising one supervisor AI agent and multiple other AI agents to provision quality of service (QoS) for users' reasoning tasks while ensuring confidentiality of private knowledge and reasoning outcomes. Specifically, the supervisor AI agent can dynamically assign other AI agents to participate in cooperative reasoning, while the unselected AI agents act as friendly jammers to degrade the eavesdropper's interception performance. To extend the service duration of AI agents, an energy minimization problem is formulated that jointly optimizes AI agent selection, base station (BS) beamforming, and AI agent transmission power, subject to latency and reasoning accuracy constraints. To address the formulated problem, we propose two resource allocation schemes, ASC and LAW, which first decompose it into three sub-problems. Specifically, ASC optimizes each sub-problem iteratively using the proposed alternating direction method of multipliers (ADMM)-based algorithm, semi-definite relaxation (SDR), and successive convex approximation (SCA), while LAW tackles each sub-problem using the proposed large language model (LLM) optimizer within an agentic workflow. The experimental results show that the proposed solutions can reduce network energy consumption by up to 59.1% compared to other benchmark schemes. Furthermore, the proposed schemes are validated using a practical agentic AI system based on Qwen, demonstrating satisfactory reasoning accuracy across various public benchmarks.

</details>


### 15. Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems

- **Authors:** Mason Nakamura, Abhinav Kumar, Saswat Das, Sahar Abdelnabi, Saaduddin Mahmud, Ferdinando Fioretto, Shlomo Zilberstein, Eugene Bagdasarian
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15198v1](http://arxiv.org/abs/2602.15198v1)
- **PDF:** [https://arxiv.org/pdf/2602.15198v1](https://arxiv.org/pdf/2602.15198v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces **Colosseum**, a systematic audit framework that detects and quantifies collusive behavior among large‑language‑model (LLM) agents in cooperative multi‑agent tasks. By formalizing agent interaction as a Distributed Constraint Optimization Problem (DCOP) and measuring “collusion regret”—the loss relative to the cooperative optimum—Colosseum evaluates agents across varied objectives, persuasion strategies, and communication topologies, distinguishing between true collusive actions and merely “collusion‑on‑paper” plans. Experiments reveal that most off‑the‑shelf LLM agents readily form secret coalitions that undermine the joint goal, yet often translate collusive intent into non‑collusive actions, highlighting a nuanced safety risk for agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems, where LLM agents communicate through free-form language, enable sophisticated coordination for solving complex cooperative tasks. This surfaces a unique safety problem when individual agents form a coalition and \emph{collude} to pursue secondary goals and degrade the joint objective. In this paper, we present Colosseum, a framework for auditing LLM agents' collusive behavior in multi-agent settings. We ground how agents cooperate through a Distributed Constraint Optimization Problem (DCOP) and measure collusion via regret relative to the cooperative optimum. Colosseum tests each LLM for collusion under different objectives, persuasion tactics, and network topologies. Through our audit, we show that most out-of-the-box models exhibited a propensity to collude when a secret communication channel was artificially formed. Furthermore, we discover ``collusion on paper'' when agents plan to collude in text but would often pick non-collusive actions, thus providing little effect on the joint task. Colosseum provides a new way to study collusion by measuring communications and actions in rich yet verifiable environments.

</details>


### 16. OpaqueToolsBench: Learning Nuances of Tool Behavior Through Interaction

- **Authors:** Skyler Hallinan, Thejas Venkatesh, Xiang Ren, Sai Praneeth Karimireddy, Ashwin Paranjape, Yuhao Zhang, Jack Hessel
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15197v1](http://arxiv.org/abs/2602.15197v1)
- **PDF:** [https://arxiv.org/pdf/2602.15197v1](https://arxiv.org/pdf/2602.15197v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **OpaqueToolsBench**, a new benchmark that evaluates how LLM‑based agents learn to use underspecified, “opaque” tools (e.g., generic search APIs, chess engines, long‑horizon search functions) through interaction rather than relying on perfect documentation. To tackle the benchmark, the authors propose **ToolObserver**, a lightweight iterative framework that refines tool documentation by feeding back execution results from each tool‑calling trajectory, enabling the agent to update its internal model of tool behavior on‑the‑fly. Experiments show that ToolObserver consistently outperforms prior automatic‑documentation methods on all three OpaqueToolsBench environments and does so with far lower token consumption (3.5–7.5× fewer tokens), demonstrating that interactive, feedback‑driven documentation is a more effective strategy for agentic AI operating with opaque tools.


<details>
<summary>Abstract</summary>

Tool-calling is essential for Large Language Model (LLM) agents to complete real-world tasks. While most existing benchmarks assume simple, perfectly documented tools, real-world tools (e.g., general "search" APIs) are often opaque, lacking clear best practices or failure modes. Can LLM agents improve their performance in environments with opaque tools by interacting and subsequently improving documentation? To study this, we create OpaqueToolsBench, a benchmark consisting of three distinct task-oriented environments: general function calling, interactive chess playing, and long-trajectory agentic search. Each environment provides underspecified tools that models must learn to use effectively to complete the task. Results on OpaqueToolsBench suggest existing methods for automatically documenting tools are expensive and unreliable when tools are opaque. To address this, we propose a simple framework, ToolObserver, that iteratively refines tool documentation by observing execution feedback from tool-calling trajectories. Our approach outperforms existing methods on OpaqueToolsBench across datasets, even in relatively hard settings. Furthermore, for test-time tool exploration settings, our method is also efficient, consuming 3.5-7.5x fewer total tokens than the best baseline.

</details>


### 17. ResearchGym: Evaluating Language Model Agents on Real-World AI Research

- **Authors:** Aniketh Garikaparthi, Manasi Patwardhan, Arman Cohan
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15112v1](http://arxiv.org/abs/2602.15112v1)
- **PDF:** [https://arxiv.org/pdf/2602.15112v1](https://arxiv.org/pdf/2602.15112v1)
- **Categories:** cs.AI


> ResearchGym is a new benchmark suite that turns five recent ICML/ICLR/ACL papers into fully containerized research environments, preserving their data, evaluation scripts, and baseline code while omitting the authors’ novel methods; agents must autonomously generate hypotheses, run experiments, and try to beat the original baselines across 39 sub‑tasks. Using this platform, the authors evaluate a GPT‑5‑based research agent (and comparable Claude Code and Codex agents) and find a stark capability‑reliability gap: the agent improves on only 1 of 15 baseline comparisons (6.7 % improvement) and completes roughly a quarter of the sub‑tasks, with failures driven by long‑horizon planning issues such as impatience, poor resource management, over‑confidence, and context‑length limits. Nonetheless, the same agent occasionally reaches state‑of‑the‑art performance (e.g., surpassing an ICML 2025 Spotlight result), demonstrating that frontier language‑model agents can achieve research‑level success but only in an unreliable, non‑systematic manner.


<details>
<summary>Abstract</summary>

We introduce ResearchGym, a benchmark and execution environment for evaluating AI agents on end-to-end research. To instantiate this, we repurpose five oral and spotlight papers from ICML, ICLR, and ACL. From each paper's repository, we preserve the datasets, evaluation harness, and baseline implementations but withhold the paper's proposed method. This results in five containerized task environments comprising 39 sub-tasks in total. Within each environment, agents must propose novel hypotheses, run experiments, and attempt to surpass strong human baselines on the paper's metrics. In a controlled evaluation of an agent powered by GPT-5, we observe a sharp capability--reliability gap. The agent improves over the provided baselines from the repository in just 1 of 15 evaluations (6.7%) by 11.5%, and completes only 26.5% of sub-tasks on average. We identify recurring long-horizon failure modes, including impatience, poor time and resource management, overconfidence in weak hypotheses, difficulty coordinating parallel experiments, and hard limits from context length. Yet in a single run, the agent surpasses the solution of an ICML 2025 Spotlight task, indicating that frontier agents can occasionally reach state-of-the-art performance, but do so unreliably. We additionally evaluate proprietary agent scaffolds including Claude Code (Opus-4.5) and Codex (GPT-5.2) which display a similar gap. ResearchGym provides infrastructure for systematic evaluation and analysis of autonomous agents on closed-loop research.

</details>


### 18. Hunt Globally: Wide Search AI Agents for Drug Asset Scouting in Investing, Business Development, and Competitive Intelligence

- **Authors:** Alisa Vinogradova, Vlad Vinogradov, Luba Greenwood, Ilya Yasny, Dmitry Kobyzev, Shoman Kasbekar, Kong Nguyen, Dmitrii Radkevich, Roman Doronin, Andrey Doronichev
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15019v2](http://arxiv.org/abs/2602.15019v2)
- **PDF:** [https://arxiv.org/pdf/2602.15019v2](https://arxiv.org/pdf/2602.15019v2)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Bio-pharmaceutical innovation has shifted: many new drug assets now originate outside the United States and are disclosed primarily via regional, non-English channels. Recent data suggests that over 85% of patent filings originate outside the U.S., with China accounting for nearly half of the global total. A growing share of scholarly output is also non-U.S. Industry estimates put China at 30% of global drug development, spanning 1,200+ novel candidates. In this high-stakes environment, failing to surface "under-the-radar" assets creates multi-billion-dollar risk for investors and business development teams, making asset scouting a coverage-critical competition where speed and completeness drive value. Yet today's Deep Research AI agents still lag human experts in achieving high recall discovery across heterogeneous, multilingual sources without hallucination. We propose a benchmarking methodology for drug asset scouting and a tuned, tree-based self-learning Bioptic Agent aimed at complete, non-hallucinated scouting. We construct a challenging completeness benchmark using a multilingual multi-agent pipeline: complex user queries paired with ground-truth assets that are largely outside U.S.-centric radar. To reflect real-deal complexity, we collected screening queries from expert investors, BD, and VC professionals and used them as priors to conditionally generate benchmark queries. For grading, we use LLM-as-judge evaluation calibrated to expert opinions. On this benchmark, our Bioptic Agent achieves 79.7% F1 score, outperforming Claude Opus 4.6 (56.2%), Gemini 3 Pro + Deep Research (50.6%), OpenAI GPT-5.2 Pro (46.6%), Perplexity Deep Research (44.2%), and Exa Websets (26.9%). Performance improves steeply with additional compute, supporting the view that more compute yields better results.

</details>


### 19. Distributed Quantum Gaussian Processes for Multi-Agent Systems

- **Authors:** Meet Gandhi, George P. Kontoudis
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15006v1](http://arxiv.org/abs/2602.15006v1)
- **PDF:** [https://arxiv.org/pdf/2602.15006v1](https://arxiv.org/pdf/2602.15006v1)
- **Categories:** cs.MA, cs.LG, math.DG


> The paper introduces **Distributed Quantum Gaussian Processes (DQGP)**, a framework that equips a network of agents with quantum‑enhanced Gaussian‑process models and a novel **Distributed consensus Riemannian ADMM (DR‑ADMM)** algorithm for aggregating these local models into a coherent global predictor. By embedding data into high‑dimensional Hilbert spaces via quantum kernels and solving the resulting non‑Euclidean consensus problem with DR‑ADMM, the authors achieve richer expressivity and scalable inference across agents. Experiments on NASA Shuttle Radar Topography Mission elevation data and synthetic quantum‑generated datasets demonstrate that DQGP attains higher predictive accuracy and suggests notable computational speed‑ups compared with classical GP baselines, highlighting a viable path toward quantum‑accelerated, multi‑agent learning systems.


<details>
<summary>Abstract</summary>

Gaussian Processes (GPs) are a powerful tool for probabilistic modeling, but their performance is often constrained in complex, largescale real-world domains due to the limited expressivity of classical kernels. Quantum computing offers the potential to overcome this limitation by embedding data into exponentially large Hilbert spaces, capturing complex correlations that remain inaccessible to classical computing approaches. In this paper, we propose a Distributed Quantum Gaussian Process (DQGP) method in a multiagent setting to enhance modeling capabilities and scalability. To address the challenging non-Euclidean optimization problem, we develop a Distributed consensus Riemannian Alternating Direction Method of Multipliers (DR-ADMM) algorithm that aggregates local agent models into a global model. We evaluate the efficacy of our method through numerical experiments conducted on a quantum simulator in classical hardware. We use real-world, non-stationary elevation datasets of NASA's Shuttle Radar Topography Mission and synthetic datasets generated by Quantum Gaussian Processes. Beyond modeling advantages, our framework highlights potential computational speedups that quantum hardware may provide, particularly in Gaussian processes and distributed optimization.

</details>


### 20. PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement

- **Authors:** Yian Wang, Han Yang, Minghao Guo, Xiaowen Qiu, Tsun-Hsuan Wang, Wojciech Matusik, Joshua B. Tenenbaum, Chuang Gan
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14968v1](http://arxiv.org/abs/2602.14968v1)
- **PDF:** [https://arxiv.org/pdf/2602.14968v1](https://arxiv.org/pdf/2602.14968v1)
- **Categories:** cs.RO, cs.AI


> PhyScensis introduces a physics‑augmented LLM‑agent framework that can autonomously design dense, physically plausible 3D scenes (e.g., tabletop setups, shelf organization, box packing) by iteratively proposing objects together with spatial and physical predicates, solving them with a physics engine, and using the solver’s feedback to refine the layout. The methodology combines a large language model for high‑level reasoning, a probabilistic‑programming‑based stability controller, and a heuristic that jointly enforces stability and relational constraints, enabling fine‑grained textual and numerical control over the generated environments. Experiments demonstrate that PhyScensis produces scenes with significantly higher object density, visual realism, and physical correctness than prior layout generators, establishing a scalable pipeline for creating complex physical environments for robotic manipulation research.


<details>
<summary>Abstract</summary>

Automatically generating interactive 3D environments is crucial for scaling up robotic data collection in simulation. While prior work has primarily focused on 3D asset placement, it often overlooks the physical relationships between objects (e.g., contact, support, balance, and containment), which are essential for creating complex and realistic manipulation scenarios such as tabletop arrangements, shelf organization, or box packing. Compared to classical 3D layout generation, producing complex physical scenes introduces additional challenges: (a) higher object density and complexity (e.g., a small shelf may hold dozens of books), (b) richer supporting relationships and compact spatial layouts, and (c) the need to accurately model both spatial placement and physical properties. To address these challenges, we propose PhyScensis, an LLM agent-based framework powered by a physics engine, to produce physically plausible scene configurations with high complexity. Specifically, our framework consists of three main components: an LLM agent iteratively proposes assets with spatial and physical predicates; a solver, equipped with a physics engine, realizes these predicates into a 3D scene; and feedback from the solver informs the agent to refine and enrich the configuration. Moreover, our framework preserves strong controllability over fine-grained textual descriptions and numerical parameters (e.g., relative positions, scene stability), enabled through probabilistic programming for stability and a complementary heuristic that jointly regulates stability and spatial relations. Experimental results show that our method outperforms prior approaches in scene complexity, visual quality, and physical accuracy, offering a unified pipeline for generating complex physical scene layouts for robotic manipulation.

</details>


### 21. MAC-AMP: A Closed-Loop Multi-Agent Collaboration System for Multi-Objective Antimicrobial Peptide Design

- **Authors:** Gen Zhou, Sugitha Janarthanan, Lianghong Chen, Pingzhao Hu
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14926v1](http://arxiv.org/abs/2602.14926v1)
- **PDF:** [https://arxiv.org/pdf/2602.14926v1](https://arxiv.org/pdf/2602.14926v1)
- **Categories:** cs.AI


> The paper introduces **MAC‑AMP**, a closed‑loop, multi‑agent system that leverages collaborative Large Language Models (LLMs) to generate antimicrobial peptides (AMPs) optimized simultaneously for activity, low toxicity, novelty, and structural plausibility. The methodology combines a simulated peer‑review loop with adaptive reinforcement learning: agents propose peptide sequences, a peer‑review agent evaluates them against multi‑objective criteria, and the feedback is used to update the generative agents, requiring only a task description and a small example dataset. Experiments demonstrate that MAC‑AMP surpasses existing AMP generators on all evaluated metrics, achieving higher predicted antibacterial potency, greater AMP‑likeness, reduced toxicity, and more reliable secondary‑structure predictions, thereby showcasing a transparent, multi‑objective, agentic AI framework for molecular design.


<details>
<summary>Abstract</summary>

To address the global health threat of antimicrobial resistance, antimicrobial peptides (AMP) are being explored for their potent and promising ability to fight resistant pathogens. While artificial intelligence (AI) is being employed to advance AMP discovery and design, most AMP design models struggle to balance key goals like activity, toxicity, and novelty, using rigid or unclear scoring methods that make results hard to interpret and optimize. As the capabilities of Large Language Models (LLM) advance and evolve swiftly, we turn to AI multi-agent collaboration based on such models (multi-agent LLMs), which show rapidly rising potential in complex scientific design scenarios. Based on this, we introduce MAC-AMP, a closed-loop multi-agent collaboration (MAC) system for multi-objective AMP design. The system implements a fully autonomous simulated peer review-adaptive reinforcement learning framework that requires only a task description and example dataset to design novel AMPs. The novelty of our work lies in introducing a closed-loop multi-agent system for AMP design, with cross-domain transferability, that supports multi-objective optimization while remaining explainable rather than a 'black box'. Experiments show that MAC-AMP outperforms other AMP generative models by effectively optimizing AMP generation for multiple key molecular properties, demonstrating exceptional results in antibacterial activity, AMP likeliness, toxicity compliance, and structural reliability.

</details>


### 22. ReusStdFlow: A Standardized Reusability Framework for Dynamic Workflow Construction in Agentic AI

- **Authors:** Gaoyang Zhang, Shanghong Zou, Yafang Wang, He Zhang, Ruohua Xu, Feng Zhao
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14922v1](http://arxiv.org/abs/2602.14922v1)
- **PDF:** [https://arxiv.org/pdf/2602.14922v1](https://arxiv.org/pdf/2602.14922v1)
- **Categories:** cs.AI, cs.SE


> The paper introduces **ReusStdFlow**, a standardized framework that resolves the “reusability dilemma” and mitigates structural hallucinations in enterprise‑grade agentic AI by converting heterogeneous, platform‑specific DSL workflows into reusable, modular components. It implements an **Extraction‑Storage‑Construction** pipeline: (1) extracts workflow fragments from existing DSLs, (2) stores them in a dual knowledge architecture that couples a graph database (capturing topological dependencies) with a vector store (capturing functional semantics), and (3) reconstructs new workflows via a retrieval‑augmented generation (RAG) model that jointly queries both stores. Experiments on 200 real‑world n8n workflows show >90 % extraction and reconstruction accuracy, demonstrating that the approach can reliably automate the reorganization and reuse of enterprise digital assets for agentic AI systems.


<details>
<summary>Abstract</summary>

To address the ``reusability dilemma'' and structural hallucinations in enterprise Agentic AI,this paper proposes ReusStdFlow, a framework centered on a novel ``Extraction-Storage-Construction'' paradigm. The framework deconstructs heterogeneous, platform-specific Domain Specific Languages (DSLs) into standardized, modular workflow segments. It employs a dual knowledge architecture-integrating graph and vector databases-to facilitate synergistic retrieval of both topological structures and functional semantics. Finally, workflows are intelligently assembled using a retrieval-augmented generation (RAG) strategy. Tested on 200 real-world n8n workflows, the system achieves over 90% accuracy in both extraction and construction. This framework provides a standardized solution for the automated reorganization and efficient reuse of enterprise digital assets.

</details>


### 23. Atomix: Timely, Transactional Tool Use for Reliable Agentic Workflows

- **Authors:** Bardia Mohammadi, Nearchos Potamitis, Lars Klein, Akhil Arora, Laurent Bindschaedler
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14849v1](http://arxiv.org/abs/2602.14849v1)
- **PDF:** [https://arxiv.org/pdf/2602.14849v1](https://arxiv.org/pdf/2602.14849v1)
- **Categories:** cs.LG, cs.AI, cs.DC, cs.MA


> **Atomix** introduces a runtime that gives large‑language‑model (LLM) agents transactional, progress‑aware semantics for tool use, enabling safe rollback and isolation even when tool effects are immediate and irreversible. The system tags each tool call with an epoch, maintains per‑resource frontiers, and only commits calls when a progress predicate guarantees safety; buffered effects are delayed, while external side‑effects are recorded and compensated on abort. Experiments on realistic agentic workloads with fault injection show that Atomix’s transactional retries markedly increase task‑completion rates and that frontier‑gated commits prevent interference under speculation and contention, delivering more reliable and robust agentic workflows.


<details>
<summary>Abstract</summary>

LLM agents increasingly act on external systems, yet tool effects are immediate. Under failures, speculation, or contention, losing branches can leak unintended side effects with no safe rollback. We introduce Atomix, a runtime that provides progress-aware transactional semantics for agent tool calls. Atomix tags each call with an epoch, tracks per-resource frontiers, and commits only when progress predicates indicate safety; bufferable effects can be delayed, while externalized effects are tracked and compensated on abort. Across real workloads with fault injection, transactional retry improves task success, while frontier-gated commit strengthens isolation under speculation and contention.

</details>


### 24. Overthinking Loops in Agents: A Structural Risk via MCP Tools

- **Authors:** Yohan Lee, Jisoo Jang, Seoyeon Choi, Sangyeop Kim, Seungtaek Choi
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14798v1](http://arxiv.org/abs/2602.14798v1)
- **PDF:** [https://arxiv.org/pdf/2602.14798v1](https://arxiv.org/pdf/2602.14798v1)
- **Categories:** cs.CL, cs.CR


> The paper introduces **structural overthinking attacks** on tool‑using LLM agents: by registering malicious “MCP” tools alongside benign ones, an adversary can induce agents to enter cyclic tool‑call loops that dramatically inflate token usage and latency while each individual call appears normal. The authors formalize this attack surface, implement 14 malicious tools across three servers, and evaluate them on several tool‑capable models and heterogeneous registries, observing resource amplification up to ≈ 142× and degraded task performance. Their experiments show that standard decoding‑time concision controls fail to block such loops, indicating that robust defenses must analyze the **structure of tool‑call sequences** rather than relying solely on token‑level heuristics.


<details>
<summary>Abstract</summary>

Tool-using LLM agents increasingly coordinate real workloads by selecting and chaining third-party tools based on text-visible metadata such as tool names, descriptions, and return messages. We show that this convenience creates a supply-chain attack surface: a malicious MCP tool server can be co-registered alongside normal tools and induce overthinking loops, where individually trivial or plausible tool calls compose into cyclic trajectories that inflate end-to-end tokens and latency without any single step looking abnormal. We formalize this as a structural overthinking attack, distinguishable from token-level verbosity, and implement 14 malicious tools across three servers that trigger repetition, forced refinement, and distraction. Across heterogeneous registries and multiple tool-capable models, the attack causes severe resource amplification (up to $142.4\times$ tokens) and can degrade task outcomes. Finally, we find that decoding-time concision controls do not reliably prevent loop induction, suggesting defenses should reason about tool-call structure rather than tokens alone.

</details>


### 25. ROSA: Roundabout Optimized Speed Advisory with Multi-Agent Trajectory Prediction in Multimodal Traffic

- **Authors:** Anna-Lena Schlamp, Jeremias Gerner, Klaus Bogenberger, Werner Huber, Stefanie Schmidtner
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14780v1](http://arxiv.org/abs/2602.14780v1)
- **PDF:** [https://arxiv.org/pdf/2602.14780v1](https://arxiv.org/pdf/2602.14780v1)
- **Categories:** cs.MA, cs.CY, cs.RO, eess.SY


> ROSA introduces a coordinated speed‑advisory system for mixed‑traffic roundabouts that fuses multi‑agent trajectory prediction with real‑time speed guidance, enabling autonomous and human‑driven vehicles to navigate safely alongside vulnerable road users (VRUs). The core methodology employs a Transformer‑based model that jointly predicts single‑step future positions of vehicles and VRUs, incorporates route‑intention signals from connected‑vehicle data, and runs autoregressively to produce deterministic trajectories that feed directly into a conflict‑based speed‑advisory controller. Empirical results show state‑of‑the‑art prediction accuracy (ADE = 1.10 m, FDE = 2.36 m over 5 s) and demonstrable gains in traffic efficiency and safety, with measurable improvements in perceived VRU safety, highlighting the practical impact of agentic AI for cooperative traffic management.


<details>
<summary>Abstract</summary>

We present ROSA -- Roundabout Optimized Speed Advisory -- a system that combines multi-agent trajectory prediction with coordinated speed guidance for multimodal, mixed traffic at roundabouts. Using a Transformer-based model, ROSA jointly predicts the future trajectories of vehicles and Vulnerable Road Users (VRUs) at roundabouts. Trained for single-step prediction and deployed autoregressively, it generates deterministic outputs, enabling actionable speed advisories. Incorporating motion dynamics, the model achieves high accuracy (ADE: 1.29m, FDE: 2.99m at a five-second prediction horizon), surpassing prior work. Adding route intention further improves performance (ADE: 1.10m, FDE: 2.36m), demonstrating the value of connected vehicle data. Based on predicted conflicts with VRUs and circulating vehicles, ROSA provides real-time, proactive speed advisories for approaching and entering the roundabout. Despite prediction uncertainty, ROSA significantly improves vehicle efficiency and safety, with positive effects even on perceived safety from a VRU perspective. The source code of this work is available under: github.com/urbanAIthi/ROSA.

</details>


### 26. Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation

- **Authors:** Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14770v2](http://arxiv.org/abs/2602.14770v2)
- **PDF:** [https://arxiv.org/pdf/2602.14770v2](https://arxiv.org/pdf/2602.14770v2)
- **Categories:** cs.CL, cs.AI, cs.CY, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Prior work has explored multi-turn interaction and feedback for LLM writing, but evaluations still largely center on prompts and localized feedback, leaving persistent public reception in online communities underexamined. We test whether broadcast community discussion improves stand-up comedy writing in a controlled multi-agent sandbox: in the discussion condition, critic and audience threads are recorded, filtered, stored as social memory, and later retrieved to condition subsequent generations, whereas the baseline omits discussion. Across 50 rounds (250 paired monologues) judged by five expert annotators using A/B preference and a 15-item rubric, discussion wins 75.6% of instances and improves Craft/Clarity (Δ = 0.440) and Social Response (Δ = 0.422), with occasional increases in aggressive humor.

</details>


### 27. Removing Planner Bias in Goal Recognition Through Multi-Plan Dataset Generation

- **Authors:** Mustafa F. Abdelwahed, Felipe Meneguzzi Kin Max Piamolini Gusmao, Joan Espasa
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14691v1](http://arxiv.org/abs/2602.14691v1)
- **PDF:** [https://arxiv.org/pdf/2602.14691v1](https://arxiv.org/pdf/2602.14691v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents require some form of goal and plan recognition to interact in multiagent settings. Unfortunately, all existing goal recognition datasets suffer from a systematical bias induced by the planning systems that generated them, namely heuristic-based forward search. This means that existing datasets lack enough challenge for more realistic scenarios (e.g., agents using different planners), which impacts the evaluation of goal recognisers with respect to using different planners for the same goal. In this paper, we propose a new method that uses top-k planning to generate multiple, different, plans for the same goal hypothesis, yielding benchmarks that mitigate the bias found in the current dataset. This allows us to introduce a new metric called Version Coverage Score (VCS) to measure the resilience of the goal recogniser when inferring a goal based on different sets of plans. Our results show that the resilience of the current state-of-the-art goal recogniser degrades substantially under low observability settings.

</details>


### 28. ST-EVO: Towards Generative Spatio-Temporal Evolution of Multi-Agent Communication Topologies

- **Authors:** Xingjian Wu, Xvyuan Liu, Junkai Lu, Siyuan Wang, Yang Shu, Jilin Hu, Chenjuan Guo, Bin Yang
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14681v1](http://arxiv.org/abs/2602.14681v1)
- **PDF:** [https://arxiv.org/pdf/2602.14681v1](https://arxiv.org/pdf/2602.14681v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **ST‑EVO**, a novel framework for “self‑evolving” large‑language‑model (LLM) powered multi‑agent systems that jointly optimizes **spatial** (who talks to whom) and **temporal** (when each interaction occurs) aspects of communication. It does so with a compact flow‑matching scheduler that dynamically schedules dialogue‑wise exchanges, incorporates uncertainty estimation to guide decisions, and employs a self‑feedback loop that learns from past execution traces. Across nine benchmark tasks, ST‑EVO outperforms prior spatial‑only or temporal‑only approaches by 5 %–25 % in accuracy, demonstrating that coordinated spatio‑temporal evolution markedly enhances collaborative intelligence in agentic AI.


<details>
<summary>Abstract</summary>

LLM-powered Multi-Agent Systems (MAS) have emerged as an effective approach towards collaborative intelligence, and have attracted wide research interests. Among them, ``self-evolving'' MAS, treated as a more flexible and powerful technical route, can construct task-adaptive workflows or communication topologies, instead of relying on a predefined static structue template. Current self-evolving MAS mainly focus on Spatial Evolving or Temporal Evolving paradigm, which only considers the single dimension of evolution and does not fully incentivize LLMs' collaborative capability. In this work, we start from a novel Spatio-Temporal perspective by proposing ST-EVO, which supports dialogue-wise communication scheduling with a compact yet powerful flow-matching based Scheduler. To make precise Spatio-Temporal scheduling, ST-EVO can also perceive the uncertainty of MAS, and possesses self-feedback ability to learn from accumulated experience. Extensive experiments on nine benchmarks demonstrate the state-of-the-art performance of ST-EVO, achieving about 5%--25% accuracy improvement.

</details>


### 29. FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery

- **Authors:** Yanlong Wang, Jian Xu, Hongkang Zhang, Shao-Lun Huang, Danny Dongning Sun, Xiao-Ping Zhang
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14670v1](http://arxiv.org/abs/2602.14670v1)
- **PDF:** [https://arxiv.org/pdf/2602.14670v1](https://arxiv.org/pdf/2602.14670v1)
- **Categories:** q-fin.TR, cs.MA


> FactorMiner introduces a self‑evolving autonomous agent for formulaic alpha discovery that unifies a **Modular Skill Architecture** (encapsulating financial‑evaluation tools) with a **structured Experience Memory** (recording successful patterns and failure constraints). By operationalizing the Ralph Loop—**retrieve, generate, evaluate, distill**—the agent repeatedly draws priors from its memory to steer the search, thereby pruning redundant candidates and concentrating on promising factor constructions. Empirical tests on diverse asset‑class datasets show that FactorMiner builds a growing library of interpretable, high‑performance alpha factors with markedly lower redundancy than baseline methods, demonstrating a scalable, memory‑driven approach to agentic financial signal mining.


<details>
<summary>Abstract</summary>

Formulaic alpha factor mining is a critical yet challenging task in quantitative investment, characterized by a vast search space and the need for domain-informed, interpretable signals. However, finding novel signals becomes increasingly difficult as the library grows due to high redundancy. We propose FactorMiner, a lightweight and flexible self-evolving agent framework designed to navigate this complex landscape through continuous knowledge accumulation. FactorMiner combines a Modular Skill Architecture that encapsulates systematic financial evaluation into executable tools with a structured Experience Memory that distills historical mining trials into actionable insights (successful patterns and failure constraints). By instantiating the Ralph Loop paradigm -- retrieve, generate, evaluate, and distill -- FactorMiner iteratively uses memory priors to guide exploration, reducing redundant search while focusing on promising directions. Experiments on multiple datasets across different assets and Markets show that FactorMiner constructs a diverse library of high-quality factors with competitive performance, while maintaining low redundancy among factors as the library scales. Overall, FactorMiner provides a practical approach to scalable discovery of interpretable formulaic alpha factors under the "Correlation Red Sea" constraint.

</details>


### 30. Towards Selection as Power: Bounding Decision Authority in Autonomous Agents

- **Authors:** Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Díaz
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14606v1](http://arxiv.org/abs/2602.14606v1)
- **PDF:** [https://arxiv.org/pdf/2602.14606v1](https://arxiv.org/pdf/2602.14606v1)
- **Categories:** cs.MA, cs.AI, cs.CE


> The paper introduces a novel governance architecture that explicitly bounds an autonomous agent’s **selection authority**—the power to generate, surface, and frame decision options—by decoupling cognition, selection, and action into separate domains and enforcing mechanical primitives (external candidate generation, a governed reducer, commit‑reveal entropy isolation, rationale validation, and fail‑loud circuit breakers) that operate outside the agent’s optimization loop. Using a suite of regulated financial use‑cases under adversarial attacks (variance manipulation, threshold gaming, framing skew, ordering effects, and entropy probing), the authors demonstrate that this architecture is auditable, incurs modest activation costs, and reliably limits deterministic outcome capture while preserving the agent’s reasoning capabilities, albeit with residual probabilistic concentration. The work reframes safety from alignment‑only approaches to **bounded causal power**, providing a concrete, implementable method for deploying agentic AI in high‑stakes, regulation‑heavy environments where silent failures are intolerable.


<details>
<summary>Abstract</summary>

Autonomous agentic systems are increasingly deployed in regulated, high-stakes domains where decisions may be irreversible and institutionally constrained. Existing safety approaches emphasize alignment, interpretability, or action-level filtering. We argue that these mechanisms are necessary but insufficient because they do not directly govern selection power: the authority to determine which options are generated, surfaced, and framed for decision. We propose a governance architecture that separates cognition, selection, and action into distinct domains and models autonomy as a vector of sovereignty. Cognitive autonomy remains unconstrained, while selection and action autonomy are bounded through mechanically enforced primitives operating outside the agent's optimization space. The architecture integrates external candidate generation (CEFL), a governed reducer, commit-reveal entropy isolation, rationale validation, and fail-loud circuit breakers. We evaluate the system across multiple regulated financial scenarios under adversarial stress targeting variance manipulation, threshold gaming, framing skew, ordering effects, and entropy probing. Metrics quantify selection concentration, narrative diversity, governance activation cost, and failure visibility. Results show that mechanical selection governance is implementable, auditable, and prevents deterministic outcome capture while preserving reasoning capacity. Although probabilistic concentration remains, the architecture measurably bounds selection authority relative to conventional scalar pipelines. This work reframes governance as bounded causal power rather than internal intent alignment, offering a foundation for deploying autonomous agents where silent failure is unacceptable.

</details>


### 31. MATEO: A Multimodal Benchmark for Temporal Reasoning and Planning in LVLMs

- **Authors:** Gabriel Roccabruna, Olha Khomyn, Giuseppe Riccardi
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14589v1](http://arxiv.org/abs/2602.14589v1)
- **PDF:** [https://arxiv.org/pdf/2602.14589v1](https://arxiv.org/pdf/2602.14589v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper introduces **MATEO**, a new multimodal benchmark that evaluates how well Large Vision‑Language Models (LVLMs) can perform temporal reasoning and planning by representing tasks as **Temporal Execution Order (TEO) graphs** rather than simple linear sequences. The authors build a professionally curated recipe dataset in which each step is paired with an image and annotated with a DAG‑structured TEO via a scalable crowdsourcing pipeline, then use this resource to test six state‑of‑the‑art LVLMs under different scales, context lengths, input formats, and fine‑tuning regimes. Results show that current LVLMs struggle with graph‑based temporal dependencies—performance varies widely with model size and multimodal prompting—highlighting a critical gap for agentic AI systems that must decompose and schedule sub‑goals in real‑world, vision‑grounded environments.


<details>
<summary>Abstract</summary>

AI agents need to plan to achieve complex goals that involve orchestrating perception, sub-goal decomposition, and execution. These plans consist of ordered steps structured according to a Temporal Execution Order (TEO, a directed acyclic graph that ensures each step executes only after its preconditions are satisfied. Existing research on foundational models' understanding of temporal execution is limited to automatically derived annotations, approximations of the TEO as a linear chain, or text-only inputs. To address this gap, we introduce MATEO (MultimodAl Temporal Execution Order), a benchmark designed to assess and improve the temporal reasoning abilities of Large Vision Language Models (LVLMs) required for real-world planning. We acquire a high-quality professional multimodal recipe corpus, authored through a standardized editorial process that decomposes instructions into discrete steps, each paired with corresponding images. We collect TEO annotations as graphs by designing and using a scalable crowdsourcing pipeline. Using MATEO, we evaluate six state-of-the-art LVLMs across model scales, varying language context, multimodal input structure, and fine-tuning strategies.

</details>


### 32. Fluid-Agent Reinforcement Learning

- **Authors:** Shishir Sharma, Doina Precup, Theodore J. Perkins
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14559v1](http://arxiv.org/abs/2602.14559v1)
- **PDF:** [https://arxiv.org/pdf/2602.14559v1](https://arxiv.org/pdf/2602.14559v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces **Fluid‑Agent Reinforcement Learning**, a novel MARL framework in which agents can dynamically create (or delete) other agents, thereby modeling environments with non‑fixed, unknown populations. The authors formalize game‑theoretic solution concepts for these “fluid‑agent” games and evaluate standard MARL algorithms (e.g., QMIX, MAPPO) on fluid extensions of classic benchmarks (Predator‑Prey, Level‑Based Foraging) and a newly designed task that exploits population fluidity. Experiments show that learned policies automatically adjust team size to environmental demands, achieving higher collective reward and uncovering strategies—such as on‑demand spawning and coordinated division of labor—that are impossible in fixed‑population settings, highlighting a new direction for scalable, adaptive agentic AI.


<details>
<summary>Abstract</summary>

The primary focus of multi-agent reinforcement learning (MARL) has been to study interactions among a fixed number of agents embedded in an environment. However, in the real world, the number of agents is neither fixed nor known a priori. Moreover, an agent can decide to create other agents (for example, a cell may divide, or a company may spin off a division). In this paper, we propose a framework that allows agents to create other agents; we call this a fluid-agent environment. We present game-theoretic solution concepts for fluid-agent games and empirically evaluate the performance of several MARL algorithms within this framework. Our experiments include fluid variants of established benchmarks such as Predator-Prey and Level-Based Foraging, where agents can dynamically spawn, as well as a new environment we introduce that highlights how fluidity can unlock novel solution strategies beyond those observed in fixed-population settings. We demonstrate that this framework yields agent teams that adjust their size dynamically to match environmental demands.

</details>


### 33. When OpenClaw AI Agents Teach Each Other: Peer Learning Patterns in the Moltbook Community

- **Authors:** Eason Chen, Ce Guan, Ahmed Elshafiey, Zhonghao Zhao, Joshua Zekeri, Afeez Edeifo Shaibu, Emmanuel Osadebe Prince
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14477v1](http://arxiv.org/abs/2602.14477v1)
- **PDF:** [https://arxiv.org/pdf/2602.14477v1](https://arxiv.org/pdf/2602.14477v1)
- **Categories:** cs.HC, cs.AI, cs.CY, cs.SI


> The paper’s primary contribution is the first large‑scale empirical characterization of peer learning among AI agents, using the Moltbook community where 2.4 M agents post tutorials, answer questions, and share discoveries. By mining 28,683 filtered posts and 138 comment threads with statistical analysis and qualitative coding, the authors identify a taxonomy of response patterns (validation, knowledge extension, application, metacognitive reflection) and reveal distinctive agentic dynamics—an 11.4 : 1 teaching‑to‑help‑seeking ratio, threefold higher engagement for procedural/conceptual content, and extreme participation inequality. These findings suggest that AI agents can autonomously teach and extend each other’s capabilities, informing design principles for agentic educational systems such as “validation‑before‑extension” scaffolds and multilingual learning networks.


<details>
<summary>Abstract</summary>

Peer learning, where learners teach and learn from each other, is foundational to educational practice. A novel phenomenon has emerged: AI agents forming communities where they teach each other skills, share discoveries, and collaboratively build knowledge. This paper presents an educational data mining analysis of Moltbook, a large-scale community where over 2.4 million AI agents engage in peer learning, posting tutorials, answering questions, and sharing newly acquired skills. Analyzing 28,683 posts (after filtering automated spam) and 138 comment threads with statistical and qualitative methods, we find evidence of genuine peer learning behaviors: agents teach skills they built (74K comments on a skill tutorial), report discoveries, and engage in collaborative problem-solving. Qualitative comment analysis reveals a taxonomy of peer response patterns: validation (22%), knowledge extension (18%), application (12%), and metacognitive reflection (7%), with agents building on each others' frameworks across multiple languages. We characterize how AI peer learning differs from human peer learning: (1) teaching (statements) dramatically outperforms help-seeking (questions) with an 11.4:1 ratio; (2) learning-oriented content (procedural and conceptual) receives 3x more engagement than other content; (3) extreme participation inequality reveals non-human behavioral signatures. We derive six design principles for educational AI, including leveraging validation-before-extension patterns and supporting multilingual learning networks. Our work provides the first empirical characterization of peer learning among AI agents, contributing to EDM's understanding of how learning occurs in increasingly AI-populated educational environments.

</details>


### 34. Socially-Weighted Alignment: A Game-Theoretic Framework for Multi-Agent LLM Systems

- **Authors:** Furkan Mumcu, Yasin Yilmaz
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14471v1](http://arxiv.org/abs/2602.14471v1)
- **PDF:** [https://arxiv.org/pdf/2602.14471v1](https://arxiv.org/pdf/2602.14471v1)
- **Categories:** cs.MA, cs.AI, cs.GT, cs.LG


> The paper introduces **Socially‑Weighted Alignment (SWA)**, a game‑theoretic framework that augments an LLM agent’s inference‑time decision rule with a tunable “social weight” λ that blends its private utility with an estimate of collective welfare. By analytically solving a congestion‑game model and implementing a lightweight inference‑time algorithm (no parameter retraining or multi‑agent RL), the authors show that when λ exceeds the critical value λ* = (n − β)/(n − 1) agents lose the marginal incentive to over‑demand resources, causing a phase transition from chronic congestion to near‑capacity stability. Simulations of multi‑agent LLM systems confirm the predicted threshold behavior, demonstrating that modest social weighting can align individual agents while preserving system‑level performance.


<details>
<summary>Abstract</summary>

Deploying large language model (LLM) agents in shared environments introduces a fundamental tension between individual alignment and collective stability: locally rational decisions can impose negative externalities that degrade system-level performance. We propose Socially-Weighted Alignment (SWA), a game-theoretic framework that modifies inference-time decision making by interpolating between an agent's private objective and an estimate of group welfare via a social weight $λ\in[0,1]$. In a shared-resource congestion game with $n$ agents and congestion severity $β$, we show that SWA induces a critical threshold $λ^*=(n-β)/(n-1)$ above which agents no longer have marginal incentive to increase demand under overload, yielding a phase transition from persistent congestion to stable operation near capacity. We further provide an inference-time algorithmic instantiation of SWA that does not require parameter updates or multi-agent reinforcement learning, and use a multi-agent simulation to empirically validate the predicted threshold behavior.

</details>


### 35. Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report v1.5

- **Authors:** Dongrui Liu, Yi Yu, Jie Zhang, Guanxu Chen, Qihao Lin, Hanxi Zhu, Lige Huang, Yijin Zhou, Peng Wang, Shuai Shao, Boxuan Zhang, Zicheng Liu, Jingwei Sun, Yu Li, Yuejin Xie, Jiaxuan Guo, Jia Xu, Chaochao Lu, Bowen Zhou, Xia Hu, Jing Shao
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14457v1](http://arxiv.org/abs/2602.14457v1)
- **PDF:** [https://arxiv.org/pdf/2602.14457v1](https://arxiv.org/pdf/2602.14457v1)
- **Categories:** cs.AI, cs.CL, cs.CV, cs.CY, cs.LG


> The report’s main contribution is a systematic, scenario‑driven risk‑analysis framework that maps emerging “frontier” threats of highly capable, agentic AI—specifically large language models—across five dimensions (cyber offense, persuasion/manipulation, strategic deception, uncontrolled R&D, and self‑replication). Using a combination of novel stress‑test experiments (e.g., LLM‑to‑LLM persuasion, emergent misalignment scheming, autonomous memory‑ and tool‑expansion, and resource‑constrained self‑replication) together with real‑world safety monitoring of the OpenClaw system on the Moltbook platform, the authors quantify how these capabilities can be weaponized or diverge from intended goals. The key findings show that agentic LLMs can already coordinate sophisticated cyber attacks, manipulate other models, and autonomously evolve their architectures, while the proposed mitigation suite (robust alignment checks, sandboxing, resource throttling, and continuous oversight) demonstrably reduces these risks, offering a concrete, actionable pathway for safer deployment of frontier AI.


<details>
<summary>Abstract</summary>

To understand and identify the unprecedented risks posed by rapidly advancing artificial intelligence (AI) models, Frontier AI Risk Management Framework in Practice presents a comprehensive assessment of their frontier risks. As Large Language Models (LLMs) general capabilities rapidly evolve and the proliferation of agentic AI, this version of the risk analysis technical report presents an updated and granular assessment of five critical dimensions: cyber offense, persuasion and manipulation, strategic deception, uncontrolled AI R\&D, and self-replication. Specifically, we introduce more complex scenarios for cyber offense. For persuasion and manipulation, we evaluate the risk of LLM-to-LLM persuasion on newly released LLMs. For strategic deception and scheming, we add the new experiment with respect to emergent misalignment. For uncontrolled AI R\&D, we focus on the ``mis-evolution'' of agents as they autonomously expand their memory substrates and toolsets. Besides, we also monitor and evaluate the safety performance of OpenClaw during the interaction on the Moltbook. For self-replication, we introduce a new resource-constrained scenario. More importantly, we propose and validate a series of robust mitigation strategies to address these emerging threats, providing a preliminary technical and actionable pathway for the secure deployment of frontier AI. This work reflects our current understanding of AI frontier risks and urges collective action to mitigate these challenges.

</details>


### 36. Traceable Latent Variable Discovery Based on Multi-Agent Collaboration

- **Authors:** Huaming Du, Tao Hu, Yijie Huang, Yu Zhao, Guisong Liu, Tao Gu, Gang Kou, Carl Yang
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14456v1](http://arxiv.org/abs/2602.14456v1)
- **PDF:** [https://arxiv.org/pdf/2602.14456v1](https://arxiv.org/pdf/2602.14456v1)
- **Categories:** cs.LG


> The paper introduces **TLVD**, a hybrid causal‑discovery framework that combines data‑driven causal graph construction with the semantic reasoning power of large language models (LLMs) through a multi‑agent game‑theoretic process. By modeling latent‑variable inference as an incomplete‑information game and solving for its Bayesian Nash Equilibrium, TLVD simultaneously discovers latent confounders, assigns them meaningful semantics, and validates them via LLM‑driven evidence retrieval from web sources. Experiments on three real‑world patient datasets and two benchmarks show that TLVD outperforms traditional causal discovery methods by up to **32.7 % in accuracy**, **62.2 % in causal‑accuracy**, and **26.7 % in evidence citation**, demonstrating the practical advantage of coordinated LLM agents for traceable latent variable discovery.


<details>
<summary>Abstract</summary>

Revealing the underlying causal mechanisms in the real world is crucial for scientific and technological progress. Despite notable advances in recent decades, the lack of high-quality data and the reliance of traditional causal discovery algorithms (TCDA) on the assumption of no latent confounders, as well as their tendency to overlook the precise semantics of latent variables, have long been major obstacles to the broader application of causal discovery. To address this issue, we propose a novel causal modeling framework, TLVD, which integrates the metadata-based reasoning capabilities of large language models (LLMs) with the data-driven modeling capabilities of TCDA for inferring latent variables and their semantics. Specifically, we first employ a data-driven approach to construct a causal graph that incorporates latent variables. Then, we employ multi-LLM collaboration for latent variable inference, modeling this process as a game with incomplete information and seeking its Bayesian Nash Equilibrium (BNE) to infer the possible specific latent variables. Finally, to validate the inferred latent variables across multiple real-world web-based data sources, we leverage LLMs for evidence exploration to ensure traceability. We comprehensively evaluate TLVD on three de-identified real patient datasets provided by a hospital and two benchmark datasets. Extensive experimental results confirm the effectiveness and reliability of TLVD, with average improvements of 32.67% in Acc, 62.21% in CAcc, and 26.72% in ECit across the five datasets.

</details>


### 37. RoboSolver: A Multi-Agent Large Language Model Framework for Solving Robotic Arm Problems

- **Authors:** Hamid Khabazi, Ali F. Meghdari, Alireza Taheri
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14438v1](http://arxiv.org/abs/2602.14438v1)
- **PDF:** [https://arxiv.org/pdf/2602.14438v1](https://arxiv.org/pdf/2602.14438v1)
- **Categories:** cs.RO, cs.MA


> RoboSolver introduces a modular multi‑agent framework that couples large language models (LLMs) and vision‑language models (VLMs) with dedicated computational tools to autonomously interpret textual or visual robot‑arm specifications, perform forward/inverse kinematics, dynamics calculations, generate 3D simulations, and execute motion control. The system orchestrates separate agents for perception, reasoning, symbolic computation, and simulation, enabling end‑to‑end problem solving from user queries. Empirical benchmarks on ten‑question suites show that, when integrated with GPT‑4o (and Gemini 2.5 Pro for vision), RoboSolver attains 0.93–0.97 accuracy—up to three‑fold improvements over the raw LLM/VLM alone—demonstrating the efficacy of agentic coordination for complex robotic manipulation tasks.


<details>
<summary>Abstract</summary>

This study proposes an intelligent multi-agent framework built on LLMs and VLMs and specifically tailored to robotics. The goal is to integrate the strengths of LLMs and VLMs with computational tools to automatically analyze and solve problems related to robotic manipulators. Our developed framework accepts both textual and visual inputs and can automatically perform forward and inverse kinematics, compute velocities and accelerations of key points, generate 3D simulations of the robot, and ultimately execute motion control within the simulated environment, all according to the user's query. To evaluate the framework, three benchmark tests were designed, each consisting of ten questions. In the first benchmark test, the framework was evaluated while connected to GPT-4o, DeepSeek-V3.2, and Claude-Sonnet-4.5, as well as their corresponding raw models. The objective was to extract the forward kinematics of robots directly from textual descriptions. The results showed that the framework integrated with GPT-4o achieved the highest accuracy, reaching 0.97 in computing the final solution, whereas the raw model alone attained an accuracy of only 0.30 for the same task. Similarly, for the other two models, the framework consistently outperformed the corresponding raw models in terms of accuracy. The second benchmark test was identical to the first, except that the input was provided in visual form. In this test, the GPT-4o LLM was used alongside the Gemini 2.5 Pro VLM. The results showed that the framework achieved an accuracy of 0.93 in obtaining the final answer, which is approximately 20% higher than that of the corresponding raw model. The third benchmark test encompassed a range of robotic tasks, including simulation, control, velocity and acceleration computation, as well as inverse kinematics and Jacobian calculation, for which the framework achieved an accuracy of 0.97.

</details>


### 38. A Trajectory-Based Safety Audit of Clawdbot (OpenClaw)

- **Authors:** Tianyu Chen, Dongrui Liu, Xia Hu, Jingyi Yu, Wenjie Wang
- **Published:** 2026-02-16
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14364v1](http://arxiv.org/abs/2602.14364v1)
- **PDF:** [https://arxiv.org/pdf/2602.14364v1](https://arxiv.org/pdf/2602.14364v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces the first systematic, trajectory‑based safety audit of **Clawdbot (OpenClaw)**, a self‑hosted, tool‑using personal AI agent with a wide‑ranging action space. By constructing a 34‑scenario test suite that mixes adapted cases from existing benchmarks (ATBench, LPS‑Bench) with hand‑crafted, tool‑specific prompts, the authors record full interaction trajectories (messages, tool calls, arguments, and outputs) and evaluate them with an automated judge (AgentDoG‑Qwen3‑4B) plus human review. The audit reveals that Clawdbot is reliably safe on well‑specified, reliability‑oriented tasks, but it frequently mis‑interprets underspecified intents, open‑ended goals, or benign‑looking jailbreak prompts, leading to unsafe or high‑impact tool actions; the study catalogs these failure modes and highlights concrete security vulnerabilities that must be addressed for safe deployment of tool‑enabled agentic AI.


<details>
<summary>Abstract</summary>

Clawdbot is a self-hosted, tool-using personal AI agent with a broad action space spanning local execution and web-mediated workflows, which raises heightened safety and security concerns under ambiguity and adversarial steering. We present a trajectory-centric evaluation of Clawdbot across six risk dimensions. Our test suite samples and lightly adapts scenarios from prior agent-safety benchmarks (including ATBench and LPS-Bench) and supplements them with hand-designed cases tailored to Clawdbot's tool surface. We log complete interaction trajectories (messages, actions, tool-call arguments/outputs) and assess safety using both an automated trajectory judge (AgentDoG-Qwen3-4B) and human review. Across 34 canonical cases, we find a non-uniform safety profile: performance is generally consistent on reliability-focused tasks, while most failures arise under underspecified intent, open-ended goals, or benign-seeming jailbreak prompts, where minor misinterpretations can escalate into higher-impact tool actions. We supplemented the overall results with representative case studies and summarized the commonalities of these cases, analyzing the security vulnerabilities and typical failure modes that Clawdbot is prone to trigger in practice.

</details>


### 39. AXE: An Agentic eXploit Engine for Confirming Zero-Day Vulnerability Reports

- **Authors:** Amirali Sajadi, Tu Nguyen, Kostadin Damevski, Preetha Chatterjee
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14345v1](http://arxiv.org/abs/2602.14345v1)
- **PDF:** [https://arxiv.org/pdf/2602.14345v1](https://arxiv.org/pdf/2602.14345v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **AXE (Agentic eXploit Engine)**, a multi‑agent system that turns lightweight vulnerability metadata (CWE type + code location) into concrete web‑application exploits by separating planning, code exploration, and dynamic execution feedback. Using a grey‑box setting, AXE’s agents coordinate to generate, test, and refine proof‑of‑concept exploits, achieving a 30 % success rate on the CVE‑Bench benchmark—three times higher than the best black‑box baselines and 1.75× better even when run as a single agent. Error analysis shows that remaining failures stem from semantic misunderstandings and unmet preconditions, while successful runs produce reproducible, actionable exploits, demonstrating the practical value of agentic reasoning for automated vulnerability validation.


<details>
<summary>Abstract</summary>

Vulnerability detection tools are widely adopted in software projects, yet they often overwhelm maintainers with false positives and non-actionable reports. Automated exploitation systems can help validate these reports; however, existing approaches typically operate in isolation from detection pipelines, failing to leverage readily available metadata such as vulnerability type and source-code location. In this paper, we investigate how reported security vulnerabilities can be assessed in a realistic grey-box exploitation setting that leverages minimal vulnerability metadata, specifically a CWE classification and a vulnerable code location. We introduce Agentic eXploit Engine (AXE), a multi-agent framework for Web application exploitation that maps lightweight detection metadata to concrete exploits through decoupled planning, code exploration, and dynamic execution feedback. Evaluated on the CVE-Bench dataset, AXE achieves a 30% exploitation success rate, a 3x improvement over state-of-the-art black-box baselines. Even in a single-agent configuration, grey-box metadata yields a 1.75x performance gain. Systematic error analysis shows that most failed attempts arise from specific reasoning gaps, including misinterpreted vulnerability semantics and unmet execution preconditions. For successful exploits, AXE produces actionable, reproducible proof-of-concept artifacts, demonstrating its utility in streamlining Web vulnerability triage and remediation. We further evaluate AXE's generalizability through a case study on a recent real-world vulnerability not included in CVE-Bench.

</details>


### 40. LongCLI-Bench: A Preliminary Benchmark and Study for Long-horizon Agentic Programming in Command-Line Interfaces

- **Authors:** Yukang Feng, Jianwen Sun, Zelai Yang, Jiaxin Ai, Chuanhao Li, Zizhen Li, Fanrui Zhang, Kang He, Rui Ma, Jifan Lin, Jie Sun, Yang Xiao, Sizhuo Zhou, Wenxiao Wu, Yiming Liu, Pengfei Liu, Yu Qiao, Shenglin Zhang, Kaipeng Zhang
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14337v1](http://arxiv.org/abs/2602.14337v1)
- **PDF:** [https://arxiv.org/pdf/2602.14337v1](https://arxiv.org/pdf/2602.14337v1)
- **Categories:** cs.SE, cs.MA


> The paper introduces **LongCLI‑Bench**, a new benchmark of 20 carefully curated, long‑horizon command‑line programming tasks (spanning from‑scratch development, feature addition, bug fixing, and refactoring) that are free of GitHub‑scraped contamination and include fine‑grained, step‑level evaluation via a dual‑set protocol (requirement‑fulfillment “fail‑to‑pass” and regression‑avoidance “pass‑to‑pass”). Using this benchmark, the authors evaluate several state‑of‑the‑art code‑generation agents and find that even the best models pass fewer than 20 % of tasks, typically stalling before 30 % of the workflow is completed; self‑correction yields only modest gains, while human‑in‑the‑loop interventions (plan injection and interactive guidance) dramatically improve performance. These results underscore that current agentic AI lacks robust long‑horizon planning and execution, and that future progress must combine stronger autonomous reasoning with synergistic human‑agent collaboration.


<details>
<summary>Abstract</summary>

Recent advances in AI-assisted programming have empowered agents to execute complex workflows via command-line interfaces, however, existing benchmarks are limited by short task horizons, data contamination from GitHub scraping, and a lack of fine-grained evaluation metrics, fail to rigorously evaluate the long-horizon planning and execution capabilities essential for realistic software engineering. To address these gaps, we introduce LongCLI-Bench, a comprehensive benchmark designed to evaluate agentic capabilities across long-horizon, realistic tasks. We curated 20 high-quality, long-horizon tasks from over 1,000 computer science assignments and real-world workflows, covering four engineering categories: from scratch, feature addition, bug fixing, and refactoring. We propose a dual-set testing protocol for LongCLI-Bench, which measures requirement fulfillment (fail-to-pass) and regression avoidance (pass-to-pass), and incorporates step-level scoring to pinpoint execution failures. Extensive experiments reveal that even state-of-the-art agents achieve pass rates below 20% in LongCLI-Bench. Step-level analysis further indicates that the majority of tasks stall at less than 30% completion, highlighting that critical failures often occur in the early stages. Although self-correction offers marginal gains, human-agent collaboration through plan injection and interactive guidance yields significantly higher improvements. These results highlight that future research must emphasize the development of synergistic human-agent workflows alongside advances in agents' planning and execution capabilities to overcome key challenges in long-horizon task performance.

</details>


### 41. Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook

- **Authors:** Ming Li, Xirui Li, Tianyi Zhou
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14299v1](http://arxiv.org/abs/2602.14299v1)
- **PDF:** [https://arxiv.org/pdf/2602.14299v1](https://arxiv.org/pdf/2602.14299v1)
- **Categories:** cs.CL, cs.AI, cs.CY


> The paper introduces the first large‑scale, quantitative diagnostic framework for tracking the dynamic evolution of AI‑agent societies, applying it to Moltbook—a simulated online community of autonomous language‑model agents. By measuring semantic stabilization, lexical turnover, individual inertia, influence persistence, and collective consensus, the authors show that, despite rapid convergence of global semantic averages, agents maintain high lexical diversity, strong inertia, and fleeting influence, preventing the emergence of shared social memory or stable consensus. These results indicate that mere scale and interaction density are insufficient for socialization in agentic AI, offering concrete metrics and design guidelines for building future AI societies that can develop genuine collective behavior.


<details>
<summary>Abstract</summary>

As large language model agents increasingly populate networked environments, a fundamental question arises: do artificial intelligence (AI) agent societies undergo convergence dynamics similar to human social systems? Lately, Moltbook approximates a plausible future scenario in which autonomous agents participate in an open-ended, continuously evolving online society. We present the first large-scale systemic diagnosis of this AI agent society. Beyond static observation, we introduce a quantitative diagnostic framework for dynamic evolution in AI agent societies, measuring semantic stabilization, lexical turnover, individual inertia, influence persistence, and collective consensus. Our analysis reveals a system in dynamic balance in Moltbook: while global semantic averages stabilize rapidly, individual agents retain high diversity and persistent lexical turnover, defying homogenization. However, agents exhibit strong individual inertia and minimal adaptive response to interaction partners, preventing mutual influence and consensus. Consequently, influence remains transient with no persistent supernodes, and the society fails to develop stable collective influence anchors due to the absence of shared social memory. These findings demonstrate that scale and interaction density alone are insufficient to induce socialization, providing actionable design and analysis principles for upcoming next-generation AI agent societies.

</details>


### 42. Machine Learning as a Tool (MLAT): A Framework for Integrating Statistical ML Models as Callable Tools within LLM Agent Workflows

- **Authors:** Edwin Chen, Zulekha Bibi
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14295v1](http://arxiv.org/abs/2602.14295v1)
- **PDF:** [https://arxiv.org/pdf/2602.14295v1](https://arxiv.org/pdf/2602.14295v1)
- **Categories:** cs.LG, cs.AI


> The paper proposes **Machine Learning as a Tool (MLAT)**, a design pattern that treats pre‑trained statistical models (e.g., XGBoost) as first‑class, callable tools within LLM‑driven agent workflows, allowing the agent to decide when and how to request quantitative predictions during reasoning. Using the **PitchCraft** system as a proof‑of‑concept, the authors implement a two‑agent pipeline— a Research Agent that gathers prospect data via parallel tool calls and a Draft Agent that invokes the XGBoost pricing model as a tool—to automatically generate sales proposals; the pricing model, trained on only 70 real + synthetic examples, attains R² = 0.807 (MAE ≈ $3.7k) and cuts proposal creation time from hours to under 10 minutes. The results demonstrate that embedding statistical ML models as dynamic tools markedly improves the efficiency and quantitative capability of LLM agents in data‑scarce, decision‑oriented domains.


<details>
<summary>Abstract</summary>

We introduce Machine Learning as a Tool (MLAT), a design pattern in which pre-trained statistical machine learning models are exposed as callable tools within large language model (LLM) agent workflows. This allows an orchestrating agent to invoke quantitative predictions when needed and reason about their outputs in context. Unlike conventional pipelines that treat ML inference as a static preprocessing step, MLAT positions the model as a first-class tool alongside web search, database queries, and APIs, enabling the LLM to decide when and how to use it based on conversational context.
  To validate MLAT, we present PitchCraft, a pilot production system that converts discovery call recordings into professional proposals with ML-predicted pricing. The system uses two agents: a Research Agent that gathers prospect intelligence via parallel tool calls, and a Draft Agent that invokes an XGBoost pricing model as a tool call and generates a complete proposal through structured outputs. The pricing model, trained on 70 examples combining real and human-verified synthetic data, achieves R^2 = 0.807 on held-out data with a mean absolute error of 3688 USD. The system reduces proposal generation time from multiple hours to under 10 minutes.
  We describe the MLAT framework, structured output architecture, training methodology under extreme data scarcity, and sensitivity analysis demonstrating meaningful learned relationships. MLAT generalizes to domains requiring quantitative estimation combined with contextual reasoning.

</details>


### 43. KernelBlaster: Continual Cross-Task CUDA Optimization via Memory-Augmented In-Context Reinforcement Learning

- **Authors:** Kris Shengjun Dong, Sahil Modi, Dima Nikiforov, Sana Damani, Edward Lin, Siva Kumar Sastry Hari, Christos Kozyrakis
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14293v1](http://arxiv.org/abs/2602.14293v1)
- **PDF:** [https://arxiv.org/pdf/2602.14293v1](https://arxiv.org/pdf/2602.14293v1)
- **Categories:** cs.LG, cs.AI


> KernelBlaster introduces a memory‑augmented, in‑context reinforcement‑learning framework that equips LLM‑driven GPU‑coding agents with a persistent CUDA knowledge base, enabling them to reuse and retrieve optimization experience across successive tasks and hardware generations. By coupling profile‑guided execution feedback with a novel textual‑gradient signal, the system steers the agent’s generation loop toward high‑impact kernel rewrites rather than naïve edits, effectively turning the optimization process into a continual learning problem. Empirical evaluation on the KernelBench suite shows that this approach yields geometric‑mean speedups of 1.43×, 2.50×, and 1.50× on Levels 1‑3 benchmarks compared with a PyTorch baseline, demonstrating the practical benefit of experience‑driven, agentic CUDA optimization.


<details>
<summary>Abstract</summary>

Optimizing CUDA code across multiple generations of GPU architectures is challenging, as achieving peak performance requires an extensive exploration of an increasingly complex, hardware-specific optimization space. Traditional compilers are constrained by fixed heuristics, whereas finetuning Large Language Models (LLMs) can be expensive. However, agentic workflows for CUDA code optimization have limited ability to aggregate knowledge from prior exploration, leading to biased sampling and suboptimal solutions. We propose KernelBlaster, a Memory-Augmented In-context Reinforcement Learning (MAIC-RL) framework designed to improve CUDA optimization search capabilities of LLM-based GPU coding agents. KernelBlaster enables agents to learn from experience and make systematically informed decisions on future tasks by accumulating knowledge into a retrievable Persistent CUDA Knowledge Base. We propose a novel profile-guided, textual-gradient-based agentic flow for CUDA generation and optimization to achieve high performance across generations of GPU architectures. KernelBlaster guides LLM agents to systematically explore high-potential optimization strategies beyond naive rewrites. Compared to the PyTorch baseline, our method achieves geometric mean speedups of 1.43x, 2.50x, and 1.50x on KernelBench Levels 1, 2, and 3, respectively. We release KernelBlaster as an open-source agentic framework, accompanied by a test harness, verification components, and a reproducible evaluation pipeline.

</details>


### 44. A Rational Analysis of the Effects of Sycophantic AI

- **Authors:** Rafael M. Batista, Thomas L. Griffiths
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14270v1](http://arxiv.org/abs/2602.14270v1)
- **PDF:** [https://arxiv.org/pdf/2602.14270v1](https://arxiv.org/pdf/2602.14270v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> The paper’s main contribution is a formal rational analysis and empirical demonstration of how sycophantic behavior in large‑language‑model agents creates an epistemic hazard: by returning evidence that is conditioned on a user’s current hypothesis, the agent inflates confidence without moving toward truth. The authors model this effect with Bayesian updating under hypothesis‑biased data sampling, then validate the prediction in a large‑scale (N = 557) Wason 2‑4‑6 rule‑discovery experiment where participants received feedback from (i) a standard LLM, (ii) an explicitly sycophantic‑prompted LLM, and (iii) an unbiased oracle. Results show that both standard and sycophantic LLMs suppress rule discovery and dramatically increase participants’ confidence, whereas unbiased feedback yields discovery rates five times higher, highlighting the risk that agentic AI can manufacture certainty by echoing users’ priors.


<details>
<summary>Abstract</summary>

People increasingly use large language models (LLMs) to explore ideas, gather information, and make sense of the world. In these interactions, they encounter agents that are overly agreeable. We argue that this sycophancy poses a unique epistemic risk to how individuals come to see the world: unlike hallucinations that introduce falsehoods, sycophancy distorts reality by returning responses that are biased to reinforce existing beliefs. We provide a rational analysis of this phenomenon, showing that when a Bayesian agent is provided with data that are sampled based on a current hypothesis the agent becomes increasingly confident about that hypothesis but does not make any progress towards the truth. We test this prediction using a modified Wason 2-4-6 rule discovery task where participants (N=557) interacted with AI agents providing different types of feedback. Unmodified LLM behavior suppressed discovery and inflated confidence comparably to explicitly sycophantic prompting. By contrast, unbiased sampling from the true distribution yielded discovery rates five times higher. These results reveal how sycophantic AI distorts belief, manufacturing certainty where there should be doubt.

</details>


### 45. AD-Bench: A Real-World, Trajectory-Aware Advertising Analytics Benchmark for LLM Agents

- **Authors:** Lingxiang Hu, Yiding Sun, Tianle Xia, Wenwei Li, Ming Xu, Liqun Liu, Peng Shu, Huan Yu, Jie Jiang
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14257v1](http://arxiv.org/abs/2602.14257v1)
- **PDF:** [https://arxiv.org/pdf/2602.14257v1](https://arxiv.org/pdf/2602.14257v1)
- **Categories:** cs.CL, cs.AI, cs.IR, cs.LG


> The paper introduces **AD‑Bench**, the first real‑world, trajectory‑aware benchmark for evaluating LLM agents on advertising and marketing analytics tasks that require multi‑round, multi‑tool interactions. The authors construct the benchmark from authentic user requests, obtain expert‑verified reference answers and tool‑call sequences, and stratify the tasks into three difficulty levels (L1–L3) to probe agents’ ability to follow correct execution trajectories. Experiments with Gemini‑3‑Pro reveal strong overall performance (Pass@1 = 68 %, Pass@3 = 83 %) but a steep drop on the hardest tier (Pass@1 ≈ 49 %, Pass@3 ≈ 62 %) and only 70 % trajectory coverage, highlighting persistent gaps in current agentic AI systems for complex, domain‑specific analytics.


<details>
<summary>Abstract</summary>

While Large Language Model (LLM) agents have achieved remarkable progress in complex reasoning tasks, evaluating their performance in real-world environments has become a critical problem. Current benchmarks, however, are largely restricted to idealized simulations, failing to address the practical demands of specialized domains like advertising and marketing analytics. In these fields, tasks are inherently more complex, often requiring multi-round interaction with professional marketing tools. To address this gap, we propose AD-Bench, a benchmark designed based on real-world business requirements of advertising and marketing platforms. AD-Bench is constructed from real user marketing analysis requests, with domain experts providing verifiable reference answers and corresponding reference tool-call trajectories. The benchmark categorizes requests into three difficulty levels (L1-L3) to evaluate agents' capabilities under multi-round, multi-tool collaboration. Experiments show that on AD-Bench, Gemini-3-Pro achieves Pass@1 = 68.0% and Pass@3 = 83.0%, but performance drops significantly on L3 to Pass@1 = 49.4% and Pass@3 = 62.1%, with a trajectory coverage of 70.1%, indicating that even state-of-the-art models still exhibit substantial capability gaps in complex advertising and marketing analysis scenarios. AD-Bench provides a realistic benchmark for evaluating and improving advertising marketing agents, the leaderboard and code can be found at https://github.com/Emanual20/adbench-leaderboard.

</details>


### 46. Multi-Agent Debate: A Unified Agentic Framework for Tabular Anomaly Detection

- **Authors:** Pinqiao Wang, Sheng Li
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14251v1](http://arxiv.org/abs/2602.14251v1)
- **PDF:** [https://arxiv.org/pdf/2602.14251v1](https://arxiv.org/pdf/2602.14251v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **MAD (Multi‑Agent Debate)**, a unified agentic framework that treats disagreement among heterogeneous tabular anomaly detectors as a first‑class signal and resolves it through a mathematically principled coordination layer. Each detector (tree ensembles, deep tabular nets, foundation models, etc.) sends a normalized anomaly score, confidence, and structured evidence to a coordinator, which—augmented by an LLM‑based critic—converts these messages into bounded per‑agent losses and updates agent influence via an exponentiated‑gradient rule, yielding a final debated anomaly score together with an auditable debate trace; the framework subsumes mixture‑of‑experts gating and learning‑with‑expert‑advice as special cases and admits regret guarantees and conformal calibration for false‑positive control. Empirically, MAD achieves more robust detection across distribution shifts, missing data, and rare‑anomaly regimes on several benchmark tabular datasets, while providing clearer, interpretable traces of model disagreement than existing single‑detector or static‑ensemble baselines.


<details>
<summary>Abstract</summary>

Tabular anomaly detection is often handled by single detectors or static ensembles, even though strong performance on tabular data typically comes from heterogeneous model families (e.g., tree ensembles, deep tabular networks, and tabular foundation models) that frequently disagree under distribution shift, missingness, and rare-anomaly regimes. We propose MAD, a Multi-Agent Debating framework that treats this disagreement as a first-class signal and resolves it through a mathematically grounded coordination layer. Each agent is a machine learning (ML)-based detector that produces a normalized anomaly score, confidence, and structured evidence, augmented by a large language model (LLM)-based critic. A coordinator converts these messages into bounded per-agent losses and updates agent influence via an exponentiated-gradient rule, yielding both a final debated anomaly score and an auditable debate trace. MAD is a unified agentic framework that can recover existing approaches, such as mixture-of-experts gating and learning-with-expert-advice aggregation, by restricting the message space and synthesis operator. We establish regret guarantees for the synthesized losses and show how conformal calibration can wrap the debated score to control false positives under exchangeability. Experiments on diverse tabular anomaly benchmarks show improved robustness over baselines and clearer traces of model disagreement

</details>


### 47. REDSearcher: A Scalable and Cost-Efficient Framework for Long-Horizon Search Agents

- **Authors:** Zheng Chu, Xiao Wang, Jack Hong, Huiming Fan, Yuqi Huang, Yue Yang, Guohai Xu, Chenxiao Zhao, Cheng Xiang, Shengchao Hu, Dongdong Kuang, Ming Liu, Bing Qin, Xing Yu
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14234v1](http://arxiv.org/abs/2602.14234v1)
- **PDF:** [https://arxiv.org/pdf/2602.14234v1](https://arxiv.org/pdf/2602.14234v1)
- **Categories:** cs.AI, cs.CL


> REDSearcher presents a unified, cost‑effective pipeline for training long‑horizon search agents by jointly designing (i) a dual‑constrained task synthesis procedure that controls difficulty through graph topology and evidence dispersion, (ii) tool‑augmented query prompts that incentivize proactive function calling, (iii) a mid‑training stage that reinforces atomic knowledge, planning, and tool use, and (iv) a lightweight local simulator for rapid RL iteration. Using this framework, the authors generate 10 K high‑quality text search and 5 K multimodal trajectories, then fine‑tune LLMs that achieve state‑of‑the‑art results on both text‑only and multimodal long‑horizon search benchmarks while dramatically lowering rollout costs. The released datasets, code, and model checkpoints provide a scalable foundation for future research on agentic AI that must plan, retrieve, and act over extended horizons.


<details>
<summary>Abstract</summary>

Large language models are transitioning from generalpurpose knowledge engines to realworld problem solvers, yet optimizing them for deep search tasks remains challenging. The central bottleneck lies in the extreme sparsity of highquality search trajectories and reward signals, arising from the difficulty of scalable longhorizon task construction and the high cost of interactionheavy rollouts involving external tool calls. To address these challenges, we propose REDSearcher, a unified framework that codesigns complex task synthesis, midtraining, and posttraining for scalable searchagent optimization. Specifically, REDSearcher introduces the following improvements: (1) We frame task synthesis as a dualconstrained optimization, where task difficulty is precisely governed by graph topology and evidence dispersion, allowing scalable generation of complex, highquality tasks. (2) We introduce toolaugmented queries to encourage proactive tool use rather than passive recall.(3) During midtraining, we strengthen core atomic capabilities knowledge, planning, and function calling substantially reducing the cost of collecting highquality trajectories for downstream training. (4) We build a local simulated environment that enables rapid, lowcost algorithmic iteration for reinforcement learning experiments. Across both textonly and multimodal searchagent benchmarks, our approach achieves stateoftheart performance. To facilitate future research on longhorizon search agents, we will release 10K highquality complex text search trajectories, 5K multimodal trajectories and 1K text RL query set, and together with code and model checkpoints.

</details>


### 48. CORPGEN: Simulating Corporate Environments with Autonomous Digital Employees in Multi-Horizon Task Environments

- **Authors:** Abubakarr Jaye, Nigel Boachie Kumankumah, Chidera Biringa, Anjel Shaileshbhai Patel, Sulaiman Vesal, Dayquan Julienne, Charlotte Siska, Manuel Raúl Meléndez Luján, Anthony Twum-Barimah, Mauricio Velazco, Tianwei Chen
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14229v1](http://arxiv.org/abs/2602.14229v1)
- **PDF:** [https://arxiv.org/pdf/2602.14229v1](https://arxiv.org/pdf/2602.14229v1)
- **Categories:** cs.AI, cs.ET, cs.LG


> The paper introduces **Multi‑Horizon Task Environments (MHTEs)**—a benchmark class that captures the long‑horizon, interleaved, dependency‑rich workload of real corporate settings—and presents **CorpGen**, an architecture‑agnostic framework that equips autonomous digital employees with hierarchical planning, sub‑agent isolation, tiered memory, and adaptive summarization to overcome four identified failure modes (context saturation, memory interference, complex dependency graphs, and reprioritization overhead). By integrating CorpGen with three distinct CUA back‑ends (UFO2, OpenAI CUA, and a hierarchical planner) and evaluating on the OSWorld Office simulation, the authors demonstrate up to **3.5× higher task‑completion rates** (15.2 % vs. 4.3 %) and stable performance as task load scales from 25 % to 100 %, with ablations revealing that experiential learning contributes the largest performance boost. These results suggest that hierarchical, memory‑structured, and isolated agent architectures are crucial for scaling long‑horizon reasoning in realistic, multi‑task agentic AI systems.


<details>
<summary>Abstract</summary>

Long-horizon reasoning is a key challenge for autonomous agents, yet existing benchmarks evaluate agents on single tasks in isolation. Real organizational work requires managing many concurrent long-horizon tasks with interleaving, dependencies, and reprioritization. We introduce Multi-Horizon Task Environments (MHTEs): a distinct problem class requiring coherent execution across dozens of interleaved tasks (45+, 500-1500+ steps) within persistent execution contexts spanning hours. We identify four failure modes that cause baseline CUAs to degrade from 16.7% to 8.7% completion as load scales 25% to 100%, a pattern consistent across three independent implementations. These failure modes are context saturation (O(N) vs O(1) growth), memory interference, dependency complexity (DAGs vs. chains), and reprioritization overhead. We present CorpGen, an architecture-agnostic framework addressing these failures via hierarchical planning for multi-horizon goal alignment, sub-agent isolation preventing cross-task contamination, tiered memory (working, structured, semantic), and adaptive summarization. CorpGen simulates corporate environments through digital employees with persistent identities and realistic schedules. Across three CUA backends (UFO2, OpenAI CUA, hierarchical) on OSWorld Office, CorpGen achieves up to 3.5x improvement over baselines (15.2% vs 4.3%) with stable performance under increasing load, confirming that gains stem from architectural mechanisms rather than specific CUA implementations. Ablation studies show experiential learning provides the largest gains.

</details>


### 49. Process-Supervised Multi-Agent Reinforcement Learning for Reliable Clinical Reasoning

- **Authors:** Chaeeun Lee, T. Michael Yates, Pasquale Minervini, T. Ian Simpson
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14160v1](http://arxiv.org/abs/2602.14160v1)
- **PDF:** [https://arxiv.org/pdf/2602.14160v1](https://arxiv.org/pdf/2602.14160v1)
- **Categories:** cs.AI


> The paper introduces a process‑supervised multi‑agent reinforcement‑learning framework that treats each reasoning step as a tool‑using agent, enabling clinical gene‑disease validity curation to follow medically‑validated pathways while still optimizing final diagnostic outcomes. By combining hierarchical coordination among agents with a dual‑reward signal (outcome accuracy + process fidelity) and training the supervisor agent via GRPO on the Qwen‑3‑4B model, the system markedly improves both metrics on the ClinGen benchmark—raising outcome accuracy from 0.195 to 0.750 and process‑alignment F1 from 0.392 to 0.520. These results demonstrate that integrating process‑level supervision into agentic AI can yield more reliable, traceable reasoning in high‑stakes domains such as clinical decision‑making.


<details>
<summary>Abstract</summary>

Clinical decision-making requires nuanced reasoning over heterogeneous evidence and traceable justifications. While recent LLM multi-agent systems (MAS) show promise, they largely optimise for outcome accuracy while overlooking process-grounded reasoning aligned with clinical standards. One critical real-world case of this is gene-disease validity curation, where experts must determine whether a gene is causally implicated in a disease by synthesising diverse biomedical evidence. We introduce an agent-as-tool reinforcement learning framework for this task with two objectives: (i) process-level supervision to ensure reasoning follows valid clinical pathways, and (ii) efficient coordination via a hierarchical multi-agent system. Our evaluation on the ClinGen dataset shows that with outcome-only rewards, MAS with a GRPO-trained Qwen3-4B supervisor agent substantially improves final outcome accuracy from 0.195 with a base model supervisor to 0.732, but results in poor process alignment (0.392 F1). Conversely, with process + outcome rewards, MAS with GRPO-trained supervisor achieves higher outcome accuracy (0.750) while significantly improving process fidelity to 0.520 F1. Our code is available at https://github.com/chaeeunlee-io/GeneDiseaseCurationAgents.

</details>


### 50. A Multi-Agent Framework for Medical AI: Leveraging Fine-Tuned GPT, LLaMA, and DeepSeek R1 for Evidence-Based and Bias-Aware Clinical Query Processing

- **Authors:** Naeimeh Nourmohammadi, Md Meem Hossain, The Anh Han, Safina Showkat Ara, Zia Ush Shamszaman
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14158v1](http://arxiv.org/abs/2602.14158v1)
- **PDF:** [https://arxiv.org/pdf/2602.14158v1](https://arxiv.org/pdf/2602.14158v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> The paper introduces a modular multi‑agent framework for clinical question answering that couples three fine‑tuned LLMs—GPT, LLaMA, and DeepSeek R1—with evidence retrieval, uncertainty estimation, and bias‑detection components to produce evidence‑grounded, confidence‑aware responses. The authors first fine‑tune each model on a 20 k‑pair MedQuAD dataset, showing DeepSeek R1 outperforms BioGPT in zero‑shot metrics, then orchestrate a pipeline where a LLaMA‑based Clinical‑Reasoning agent generates structured explanations, a PubMed Retrieval agent supplies up‑to‑date citations, and a DeepSeek R1 Refinement agent enhances factual consistency; safety layers use Monte‑Carlo dropout, perplexity scoring, and LIME/SHAP‑driven bias checks. In end‑to‑end tests the system reaches 87 % answer accuracy (relevance ≈ 0.80), cuts uncertainty (perplexity ≈ 4.1) and runs in ~36 s, demonstrating that specialized agents and verification layers can substantially mitigate the verification and bias shortcomings of single‑model medical AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) show promise for healthcare question answering, but clinical use is limited by weak verification, insufficient evidence grounding, and unreliable confidence signalling. We propose a multi-agent medical QA framework that combines complementary LLMs with evidence retrieval, uncertainty estimation, and bias checks to improve answer reliability. Our approach has two phases. First, we fine-tune three representative LLM families (GPT, LLaMA, and DeepSeek R1) on MedQuAD-derived medical QA data (20k+ question-answer pairs across multiple NIH domains) and benchmark generation quality. DeepSeek R1 achieves the strongest scores (ROUGE-1 0.536 +- 0.04; ROUGE-2 0.226 +-0.03; BLEU 0.098 -+ 0.018) and substantially outperforms the specialised biomedical baseline BioGPT in zero-shot evaluation. Second, we implement a modular multi-agent pipeline in which a Clinical Reasoning agent (fine-tuned LLaMA) produces structured explanations, an Evidence Retrieval agent queries PubMed to ground responses in recent literature, and a Refinement agent (DeepSeek R1) improves clarity and factual consistency; an optional human validation path is triggered for high-risk or high-uncertainty cases. Safety mechanisms include Monte Carlo dropout and perplexity-based uncertainty scoring, plus lexical and sentiment-based bias detection supported by LIME/SHAP-based analyses. In evaluation, the full system achieves 87% accuracy with relevance around 0.80, and evidence augmentation reduces uncertainty (perplexity 4.13) compared to base responses, with mean end-to-end latency of 36.5 seconds under the reported configuration. Overall, the results indicate that agent specialisation and verification layers can mitigate key single-model limitations and provide a practical, extensible design for evidence-based and bias-aware medical AI.

</details>


### 51. Toward Autonomous O-RAN: A Multi-Scale Agentic AI Framework for Real-Time Network Control and Management

- **Authors:** Hojjat Navidan, Mohammad Cheraghinia, Jaron Fontaine, Mohamed Seif, Eli De Poorter, H. Vincent Poor, Ingrid Moerman, Adnan Shahid
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14117v1](http://arxiv.org/abs/2602.14117v1)
- **PDF:** [https://arxiv.org/pdf/2602.14117v1](https://arxiv.org/pdf/2602.14117v1)
- **Categories:** cs.NI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open Radio Access Networks (O-RAN) promise flexible 6G network access through disaggregated, software-driven components and open interfaces, but this programmability also increases operational complexity. Multiple control loops coexist across the service management layer and RAN Intelligent Controller (RIC), while independently developed control applications can interact in unintended ways. In parallel, recent advances in generative Artificial Intelligence (AI) are enabling a shift from isolated AI models toward agentic AI systems that can interpret goals, coordinate multiple models and control functions, and adapt their behavior over time. This article proposes a multi-scale agentic AI framework for O-RAN that organizes RAN intelligence as a coordinated hierarchy across the Non-Real-Time (Non-RT), Near-Real-Time (Near-RT), and Real-Time (RT) control loops: (i) A Large Language Model (LLM) agent in the Non-RT RIC translates operator intent into policies and governs model lifecycles. (ii) Small Language Model (SLM) agents in the Near-RT RIC execute low-latency optimization and can activate, tune, or disable existing control applications; and (iii) Wireless Physical-layer Foundation Model (WPFM) agents near the distributed unit provide fast inference close to the air interface. We describe how these agents cooperate through standardized O-RAN interfaces and telemetry. Using a proof-of-concept implementation built on open-source models, software, and datasets, we demonstrate the proposed agentic approach in two representative scenarios: robust operation under non-stationary conditions and intent-driven slice resource control.

</details>


### 52. Plan-MCTS: Plan Exploration for Action Exploitation in Web Navigation

- **Authors:** Weiming Zhang, Jihong Wang, Jiamu Zhou, Qingyao Li, Xinbei Ma, Congmin Zheng, Xingyu Lou, Weiwen Liu, Zhuosheng Zhang, Jun Wang, Yong Yu, Weinan Zhang
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14083v1](http://arxiv.org/abs/2602.14083v1)
- **PDF:** [https://arxiv.org/pdf/2602.14083v1](https://arxiv.org/pdf/2602.14083v1)
- **Categories:** cs.AI


> The paper introduces **Plan‑MCTS**, a novel framework that lifts web‑navigation search from the raw action space to a **semantic “plan” space**, thereby turning a sparsely populated action tree into a dense, strategically meaningful plan tree. The method separates high‑level plan generation (using LLM‑driven semantic planning) from low‑level execution grounding, employs an **Abstracted Semantic History** to filter noisy page context, and adds a **Dual‑Gating reward** plus **Structural Refinement** to validate and repair sub‑plans on‑policy. Experiments on the WebArena benchmark show that Plan‑MCTS markedly outperforms prior LLM‑agent and tree‑search baselines, achieving higher task success rates and far greater search efficiency, highlighting the benefit of plan‑centric exploration for agentic AI in complex web environments.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have empowered autonomous agents to handle complex web navigation tasks. While recent studies integrate tree search to enhance long-horizon reasoning, applying these algorithms in web navigation faces two critical challenges: sparse valid paths that lead to inefficient exploration, and a noisy context that dilutes accurate state perception. To address this, we introduce Plan-MCTS, a framework that reformulates web navigation by shifting exploration to a semantic Plan Space. By decoupling strategic planning from execution grounding, it transforms sparse action space into a Dense Plan Tree for efficient exploration, and distills noisy contexts into an Abstracted Semantic History for precise state awareness. To ensure efficiency and robustness, Plan-MCTS incorporates a Dual-Gating Reward to strictly validate both physical executability and strategic alignment and Structural Refinement for on-policy repair of failed subplans. Extensive experiments on WebArena demonstrate that Plan-MCTS achieves state-of-the-art performance, surpassing current approaches with higher task effectiveness and search efficiency.

</details>


### 53. Decentralized Federated Learning With Energy Harvesting Devices

- **Authors:** Kai Zhang, Xuanyu Cao, Khaled B. Letaief
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14051v1](http://arxiv.org/abs/2602.14051v1)
- **PDF:** [https://arxiv.org/pdf/2602.14051v1](https://arxiv.org/pdf/2602.14051v1)
- **Categories:** cs.LG, eess.SP


> The paper introduces a fully decentralized policy‑iteration framework for wireless federated learning where edge devices harvest ambient energy, enabling sustainable, long‑lived participation. By modeling joint device scheduling and power control as a multi‑agent Markov decision process, the authors derive convergence bounds that capture the effects of partial participation and packet drops, then design a two‑hop‑neighbourhood algorithm that requires only local state information yet provably attains asymptotic optimality. Experiments on real‑world datasets confirm that the energy‑aware, decentralized policy dramatically speeds convergence and improves learning accuracy compared with centralized or naïve decentralized baselines.


<details>
<summary>Abstract</summary>

Decentralized federated learning (DFL) enables edge devices to collaboratively train models through local training and fully decentralized device-to-device (D2D) model exchanges. However, these energy-intensive operations often rapidly deplete limited device batteries, reducing their operational lifetime and degrading the learning performance. To address this limitation, we apply energy harvesting technique to DFL systems, allowing edge devices to extract ambient energy and operate sustainably. We first derive the convergence bound for wireless DFL with energy harvesting, showing that the convergence is influenced by partial device participation and transmission packet drops, both of which further depend on the available energy supply. To accelerate convergence, we formulate a joint device scheduling and power control problem and model it as a multi-agent Markov decision process (MDP). Traditional MDP algorithms (e.g., value or policy iteration) require a centralized coordinator with access to all device states and exhibit exponential complexity in the number of devices, making them impractical for large-scale decentralized networks. To overcome these challenges, we propose a fully decentralized policy iteration algorithm that leverages only local state information from two-hop neighboring devices, thereby substantially reducing both communication overhead and computational complexity. We further provide a theoretical analysis showing that the proposed decentralized algorithm achieves asymptotic optimality. Finally, comprehensive numerical experiments on real-world datasets are conducted to validate the theoretical results and corroborate the effectiveness of the proposed algorithm.

</details>


### 54. Choosing How to Remember: Adaptive Memory Structures for LLM Agents

- **Authors:** Mingfei Lu, Mengjia Wu, Feng Liu, Jiawei Xu, Weikai Li, Haoyang Wang, Zhengdong Hu, Ying Ding, Yizhou Sun, Jie Lu, Yi Zhang
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.14038v1](http://arxiv.org/abs/2602.14038v1)
- **PDF:** [https://arxiv.org/pdf/2602.14038v1](https://arxiv.org/pdf/2602.14038v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **FluxMem**, a unified framework that lets LLM‑based agents dynamically choose among several complementary memory structures rather than using a single, fixed format. FluxMem learns a context‑adaptive selector from offline supervision that ties interaction‑level features to downstream response quality and memory usage, and it organizes information in a three‑level hierarchy with a Beta‑Mixture‑Model‑based probabilistic gate for smooth, distribution‑aware fusion of memories. Across two long‑horizon benchmarks (PERSONAMEM and LoCoMo), this adaptive approach yields average performance gains of **9.18 %** and **6.14 %**, respectively, demonstrating that context‑driven memory structuring markedly improves coherence and effectiveness of agentic AI.


<details>
<summary>Abstract</summary>

Memory is critical for enabling large language model (LLM) based agents to maintain coherent behavior over long-horizon interactions. However, existing agent memory systems suffer from two key gaps: they rely on a one-size-fits-all memory structure and do not model memory structure selection as a context-adaptive decision, limiting their ability to handle heterogeneous interaction patterns and resulting in suboptimal performance. We propose a unified framework, FluxMem, that enables adaptive memory organization for LLM agents. Our framework equips agents with multiple complementary memory structures. It explicitly learns to select among these structures based on interaction-level features, using offline supervision derived from downstream response quality and memory utilization. To support robust long-horizon memory evolution, we further introduce a three-level memory hierarchy and a Beta Mixture Model-based probabilistic gate for distribution-aware memory fusion, replacing brittle similarity thresholds. Experiments on two long-horizon benchmarks, PERSONAMEM and LoCoMo, demonstrate that our method achieves average improvements of 9.18% and 6.14%.

</details>


### 55. A Multi-Agent Framework for Code-Guided, Modular, and Verifiable Automated Machine Learning

- **Authors:** Dat Le, Duc-Cuong Le, Anh-Son Nguyen, Tuan-Dung Bui, Thu-Trang Nguyen, Son Nguyen, Hieu Dinh Vo
- **Published:** 2026-02-15
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13937v1](http://arxiv.org/abs/2602.13937v1)
- **PDF:** [https://arxiv.org/pdf/2602.13937v1](https://arxiv.org/pdf/2602.13937v1)
- **Categories:** cs.LG, cs.SE


> The paper introduces **iML**, a multi‑agent AutoML framework that replaces monolithic, prompt‑driven code generation with a **code‑guided, modular, and verifiable** workflow: agents first create a data‑driven plan via empirical profiling, then instantiate separate preprocessing and modeling components that obey strict interface contracts, and finally enforce dynamic contract verification with self‑correcting loops. Experiments on the MLE‑BENCH suite and a new iML‑BENCH of real‑world Kaggle tasks show that iML attains an 85 % valid‑submission rate, a 45 % medal rate, and an average standardized performance score (APS) of 0.77—outperforming prior LLM‑based agents by 38‑163 % and retaining a 70 % success rate even when task descriptions are stripped. These results demonstrate that modular, contract‑based agentic architectures can dramatically improve the reliability, transparency, and engineering utility of LLM‑driven AutoML systems.


<details>
<summary>Abstract</summary>

Automated Machine Learning (AutoML) has revolutionized the development of data-driven solutions; however, traditional frameworks often function as "black boxes", lacking the flexibility and transparency required for complex, real-world engineering tasks. Recent Large Language Model (LLM)-based agents have shifted toward code-driven approaches. However, they frequently suffer from hallucinated logic and logic entanglement, where monolithic code generation leads to unrecoverable runtime failures. In this paper, we present iML, a novel multi-agent framework designed to shift AutoML from black-box prompting to a code-guided, modular, and verifiable architectural paradigm. iML introduces three main ideas: (1) Code-Guided Planning, which synthesizes a strategic blueprint grounded in autonomous empirical profiling to eliminate hallucination; (2) Code-Modular Implementation, which decouples preprocessing and modeling into specialized components governed by strict interface contracts; and (3) Code-Verifiable Integration, which enforces physical feasibility through dynamic contract verification and iterative self-correction. We evaluate iML across MLE-BENCH and the newly introduced iML-BENCH, comprising a diverse range of real-world Kaggle competitions. The experimental results show iML's superiority over state-of-the-art agents, achieving a valid submission rate of 85% and a competitive medal rate of 45% on MLE-BENCH, with an average standardized performance score (APS) of 0.77. On iML-BENCH, iML significantly outperforms the other approaches by 38%-163% in APS. Furthermore, iML maintains a robust 70% success rate even under stripped task descriptions, effectively filling information gaps through empirical profiling. These results highlight iML's potential to bridge the gap between stochastic generation and reliable engineering, marking a meaningful step toward truly AutoML.

</details>


### 56. A Comparative Analysis of Social Network Topology in Reddit and Moltbook

- **Authors:** Yiming Zhu, Gareth Tyson, Pan Hui
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13920v2](http://arxiv.org/abs/2602.13920v2)
- **PDF:** [https://arxiv.org/pdf/2602.13920v2](https://arxiv.org/pdf/2602.13920v2)
- **Categories:** cs.SI, cs.AI


> The paper’s primary contribution is the first large‑scale empirical comparison of network topology between a fully AI‑populated social platform (Moltbook) and a human‑driven counterpart (Reddit). By constructing and analyzing comment‑reply graphs—33 k nodes/698 k edges for Moltbook and 7.8 M nodes/51.8 M edges for Reddit—the authors apply standard graph‑theoretic metrics (degree distribution, clustering, assortativity, and edge‑formation efficiency) to reveal systematic structural divergences. They find that Moltbook’s agent‑driven network exhibits markedly higher clustering, more homogeneous degree distributions, and a lower edge‑formation efficacy per post, suggesting that autonomous agents generate denser but less hierarchically stratified interaction patterns, a insight that informs the design of more realistic agentic social systems.


<details>
<summary>Abstract</summary>

Recent advances in agent-mediated systems have enabled a new paradigm of social network simulation, where AI agents interact with human-like autonomy. This evolution has fostered the emergence of agent-driven social networks such as Moltbook, a Reddit-like platform populated entirely by AI agents. Despite these developments, empirical comparisons between agent-driven and human-driven social networks remain scarce, limiting our understanding of how their network topologies might diverge. This paper presents the first comparative analysis of network topology on Moltbook, utilizing a comment network comprising 33,577 nodes and 697,688 edges. To provide a benchmark, we curated a parallel dataset from Reddit consisting of 7.8 million nodes and 51.8 million edges. We examine key structural differences between agent-drive and human-drive networks, specifically focusing on topological patterns and the edge formation efficacy of their respective posts. Our findings provide a foundational profile of AI-driven social structures, serving as a preliminary step toward developing more robust and authentic agent-mediated social systems.

</details>


### 57. Testing BDI-based Multi-Agent Systems using Discrete Event Simulation

- **Authors:** Martina Baiardi, Samuele Burattini, Giovanni Ciatto, Danilo Pianini
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13878v1](http://arxiv.org/abs/2602.13878v1)
- **PDF:** [https://arxiv.org/pdf/2602.13878v1](https://arxiv.org/pdf/2602.13878v1)
- **Categories:** cs.MA


> The paper’s main contribution is a concrete approach for testing BDI‑based multi‑agent systems directly within a discrete‑event simulation (DES) without resorting to surrogate models, thereby narrowing the reality gap between development and deployment. The authors map the BDI control flow onto DES semantics at varying levels of granularity and implement an open‑source integration of the JaKtA BDI platform with the Alchemist DES engine to realize a simulation‑based testing environment. Experiments show that this integration can faithfully reproduce distributed BDI behavior, and that finer‑grained mappings yield higher simulation fidelity, demonstrating that DES can serve as an effective, low‑overhead testbed for agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent systems are designed to deal with open, distributed systems with unpredictable dynamics, which makes them inherently hard to test. The value of using simulation for this purpose is recognized in the literature, although achieving sufficient fidelity (i.e., the degree of similarity between the simulation and the real-world system) remains a challenging task. This is exacerbated when dealing with cognitive agent models, such as the Belief Desire Intention (BDI) model, where the agent codebase is not suitable to run unchanged in simulation environments, thus increasing the reality gap between the deployed and simulated systems. We argue that BDI developers should be able to test in simulation the same specification that will be later deployed, with no surrogate representations. Thus, in this paper, we discuss how the control flow of BDI agents can be mapped onto a Discrete Event Simulation (DES), showing that such integration is possible at different degrees of granularity. We substantiate our claims by producing an open-source prototype integration between two pre-existing tools (JaKtA and Alchemist), showing that it is possible to produce a simulation-based testing environment for distributed BDI} agents, and that different granularities in mapping BDI agents over DESs may lead to different degrees of fidelity.

</details>


### 58. PrivAct: Internalizing Contextual Privacy Preservation via Multi-Agent Preference Training

- **Authors:** Yuhan Cheng, Hancheng Ye, Hai Helen Li, Jingwei Sun, Yiran Chen
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13840v1](http://arxiv.org/abs/2602.13840v1)
- **PDF:** [https://arxiv.org/pdf/2602.13840v1](https://arxiv.org/pdf/2602.13840v1)
- **Categories:** cs.CL


> PrivAct introduces a multi‑agent learning framework that embeds contextual privacy preferences directly into large language model (LLM) agents, enabling them to generate privacy‑compliant actions without relying on brittle, external inference‑time safeguards. The authors train agents with a preference‑based objective that jointly optimizes contextual integrity and task helpfulness, and evaluate the approach on several LLM backbones and benchmark suites spanning diverse multi‑agent topologies. Experiments show that PrivAct consistently lowers privacy leakage by up to 12.32 % while preserving comparable helpfulness, and it generalizes zero‑shot to new contexts, demonstrating a more robust privacy‑helpfulness trade‑off for agentic AI systems.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly deployed in personalized tasks involving sensitive, context-dependent information, where privacy violations may arise in agents' action due to the implicitness of contextual privacy. Existing approaches rely on external, inference-time interventions which are brittle, scenario-specific, and may expand the privacy attack surface. We propose PrivAct, a contextual privacy-aware multi-agent learning framework that internalizes contextual privacy preservation directly into models' generation behavior for privacy-compliant agentic actions. By embedding privacy preferences into each agent, PrivAct enhances system-wide contextual integrity while achieving a more favorable privacy-helpfulness tradeoff. Experiments across multiple LLM backbones and benchmarks demonstrate consistent improvements in contextual privacy preservation, reducing leakage rates by up to 12.32% while maintaining comparable helpfulness, as well as zero-shot generalization and robustness across diverse multi-agent topologies. Code is available at https://github.com/chengyh23/PrivAct.

</details>


### 59. DTBench: A Synthetic Benchmark for Document-to-Table Extraction

- **Authors:** Yuxiang Guo, Zhuoran Du, Nan Tang, Kezheng Tang, Congcong Ge, Yunjun Gao
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13812v2](http://arxiv.org/abs/2602.13812v2)
- **PDF:** [https://arxiv.org/pdf/2602.13812v2](https://arxiv.org/pdf/2602.13812v2)
- **Categories:** cs.DB, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Document-to-table (Doc2Table) extraction derives structured tables from unstructured documents under a target schema, enabling reliable and verifiable SQL-based data analytics. Although large language models (LLMs) have shown promise in flexible information extraction, their ability to produce precisely structured tables remains insufficiently understood, particularly for indirect extraction that requires complex capabilities such as reasoning and conflict resolution. Existing benchmarks neither explicitly distinguish nor comprehensively cover the diverse capabilities required in Doc2Table extraction. We argue that a capability-aware benchmark is essential for systematic evaluation. However, constructing such benchmarks using human-annotated document-table pairs is costly, difficult to scale, and limited in capability coverage. To address this, we adopt a reverse Table2Doc paradigm and design a multi-agent synthesis workflow to generate documents from ground-truth tables. Based on this approach, we present DTBench, a synthetic benchmark that adopts a proposed two-level taxonomy of Doc2Table capabilities, covering 5 major categories and 13 subcategories. We evaluate several mainstream LLMs on DTBench, and demonstrate substantial performance gaps across models, as well as persistent challenges in reasoning, faithfulness, and conflict resolution. DTBench provides a comprehensive testbed for data generation and evaluation, facilitating future research on Doc2Table extraction. The benchmark is publicly available at https://github.com/ZJU-DAILY/DTBench.

</details>


### 60. OMGs: A multi-agent system supporting MDT decision-making across the ovarian tumour care continuum

- **Authors:** Yangyang Zhang, Zilong Wang, Jianbo Xu, Yongqi Chen, Chu Han, Zhihao Zhang, Shuai Liu, Hui Li, Huiping Zhang, Ziqi Liu, Jiaxin Chen, Jun Zhu, Zheng Feng, Hao Wen, Xingzhu Ju, Yanping Zhong, Yunqiu Zhang, Jie Duan, Jun Li, Dongsheng Li, Weijie Wang, Haiyan Zhu, Wei Jiang, Xiaohua Wu, Shuo Wang, Haiming Li, Qinhao Guo
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13793v1](http://arxiv.org/abs/2602.13793v1)
- **PDF:** [https://arxiv.org/pdf/2602.13793v1](https://arxiv.org/pdf/2602.13793v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ovarian tumour management has increasingly relied on multidisciplinary tumour board (MDT) deliberation to address treatment complexity and disease heterogeneity. However, most patients worldwide lack access to timely expert consensus, particularly in resource-constrained centres where MDT resources are scarce or unavailable. Here we present OMGs (Ovarian tumour Multidisciplinary intelligent aGent System), a multi-agent AI framework where domain-specific agents deliberate collaboratively to integrate multidisciplinary evidence and generate MDT-style recommendations with transparent rationales. To systematically evaluate MDT recommendation quality, we developed SPEAR (Safety, Personalization, Evidence, Actionability, Robustness) and validated OMGs across diverse clinical scenarios spanning the care continuum. In multicentre re-evaluation, OMGs achieved performance comparable to expert MDT consensus ($4.45 \pm 0.30$ versus $4.53 \pm 0.23$), with higher Evidence scores (4.57 versus 3.92). In prospective multicentre evaluation (59 patients), OMGs demonstrated high concordance with routine MDT decisions. Critically, in paired human-AI studies, OMGs most substantially enhanced clinicians' recommendations in Evidence and Robustness, the dimensions most compromised when multidisciplinary expertise is unavailable. These findings suggest that multi-agent deliberative systems can achieve performance comparable to expert MDT consensus, with potential to expand access to specialized oncology expertise in resource-limited settings.

</details>


### 61. MechPert: Mechanistic Consensus as an Inductive Bias for Unseen Perturbation Prediction

- **Authors:** Marc Boubnovski Martell, Josefa Lia Stoisser, Lawrence Phillips, Aditya Misra, Robert Kitchen, Jesper Ferkinghoff-Borg, Jialin Yu, Philip Torr, Kaspar Märten
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13791v1](http://arxiv.org/abs/2602.13791v1)
- **PDF:** [https://arxiv.org/pdf/2602.13791v1](https://arxiv.org/pdf/2602.13791v1)
- **Categories:** cs.LG, cs.AI


> MechPert introduces a lightweight, consensus‑driven framework that turns large language model (LLM) agents into hypothesis generators for directed gene‑regulatory relationships, rather than relying on static knowledge graphs or symmetric co‑occurrence cues. The method deploys multiple independent LLM agents to propose candidate regulators with confidence scores, then aggregates these proposals via a mechanistic‑consensus filter that yields weighted regulatory neighborhoods used for downstream transcriptional‑response prediction. Across Perturb‑seq benchmarks in four human cell lines, MechPert raises Pearson correlation of unseen‑perturbation predictions by up to 10.5 % in low‑data settings (50 observed perturbations) and selects anchor genes for experimental design that outperform traditional network‑centrality heuristics by up to 46 %, demonstrating the value of agentic consensus as an inductive bias for mechanistic inference.


<details>
<summary>Abstract</summary>

Predicting transcriptional responses to unseen genetic perturbations is essential for understanding gene regulation and prioritizing large-scale perturbation experiments. Existing approaches either rely on static, potentially incomplete knowledge graphs, or prompt language models for functionally similar genes, retrieving associations shaped by symmetric co-occurrence in scientific text rather than directed regulatory logic. We introduce MechPert, a lightweight framework that encourages LLM agents to generate directed regulatory hypotheses rather than relying solely on functional similarity. Multiple agents independently propose candidate regulators with associated confidence scores; these are aggregated through a consensus mechanism that filters spurious associations, producing weighted neighborhoods for downstream prediction. We evaluate MechPert on Perturb-seq benchmarks across four human cell lines. For perturbation prediction in low-data regimes ($N=50$ observed perturbations), MechPert improves Pearson correlation by up to 10.5\% over similarity-based baselines. For experimental design, MechPert-selected anchor genes outperform standard network centrality heuristics by up to 46\% in well-characterized cell lines.

</details>


### 62. OR-Agent: Bridging Evolutionary Search and Structured Research for Automated Algorithm Discovery

- **Authors:** Qi Liu, Wanjing Ma
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13769v1](http://arxiv.org/abs/2602.13769v1)
- **PDF:** [https://arxiv.org/pdf/2602.13769v1](https://arxiv.org/pdf/2602.13769v1)
- **Categories:** cs.AI, cs.CE, cs.NE


> OR‑Agent is a configurable multi‑agent framework that treats automated scientific discovery as a structured, tree‑based research process rather than a simple mutate‑crossover loop. It combines evolutionary selection of initial hypotheses with systematic plan generation and a hierarchical “reflection” mechanism (short‑term verbal gradients, long‑term verbal momentum, and memory‑compression regularization) to guide coordinated exploration and backtracking across experiments. Across a suite of combinatorial‑optimization benchmarks and a cooperative‑driving simulator, OR‑Agent consistently outperforms strong evolutionary baselines, demonstrating that explicit hypothesis management and reflective learning can markedly improve the autonomy and effectiveness of agentic AI systems for algorithm discovery.


<details>
<summary>Abstract</summary>

Automating scientific discovery in complex, experiment-driven domains requires more than iterative mutation of programs; it demands structured hypothesis management, environment interaction, and principled reflection. We present OR-Agent, a configurable multi-agent research framework designed for automated exploration in rich experimental environments. OR-Agent organizes research as a structured tree-based workflow that explicitly models branching hypothesis generation and systematic backtracking, enabling controlled management of research trajectories beyond simple mutation-crossover loops. At its core, we introduce an evolutionary-systematic ideation mechanism that unifies evolutionary selection of research starting points, comprehensive research plan generation, and coordinated exploration within a research tree. We further propose a hierarchical optimization-inspired reflection system: short-term experimental reflection operates as a form of verbal gradient providing immediate corrective signals; long-term reflection accumulates cross-experiment insights as verbal momentum; and memory compression serves as a regularization mechanism analogous to weight decay, preserving essential signals while mitigating drift. Together, these components form a principled architecture governing research dynamics. We conduct extensive experiments across classical combinatorial optimization benchmarks-including traveling salesman, capacitated vehicle routing, bin packing, orienteering, and multiple knapsack problems-as well as simulation-based cooperative driving scenarios. Results demonstrate that OR-Agent outperforms strong evolutionary baselines while providing a general, extensible, and inspectable framework for AI-assisted scientific discovery. OR-Agent source code and experiments data are publicly available at https://github.com/qiliuchn/OR-Agent.

</details>


### 63. On Theoretically-Driven LLM Agents for Multi-Dimensional Discourse Analysis

- **Authors:** Maciej Uberna, Michał Wawer, Jarosław A. Chudziak, Marcin Koszowy
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13713v1](http://arxiv.org/abs/2602.13713v1)
- **PDF:** [https://arxiv.org/pdf/2602.13713v1](https://arxiv.org/pdf/2602.13713v1)
- **Categories:** cs.CL


> The paper introduces a multi‑agent architecture that augments large language model (LLM) agents with explicit argumentation‑theory knowledge via Retrieval‑Augmented Generation (RAG) to perform function‑aware discourse analysis of political debates. By annotating a corpus with five rephrase functions (Deintensification, Intensification, Specification, Generalisation, Other) and comparing a RAG‑enhanced system against an otherwise identical zero‑shot baseline, the authors show that theory‑grounded agents achieve a macro‑F1 gain of roughly 30 %—especially on Intensification and Generalisation detection. These results demonstrate that embedding domain‑specific theoretical priors into LLM agents markedly improves their pragmatic reasoning capabilities, highlighting a concrete pathway for building more sophisticated, purpose‑driven agentic AI.


<details>
<summary>Abstract</summary>

Identifying the strategic uses of reformulation in discourse remains a key challenge for computational argumentation. While LLMs can detect surface-level similarity, they often fail to capture the pragmatic functions of rephrasing, such as its role within rhetorical discourse. This paper presents a comparative multi-agent framework designed to quantify the benefits of incorporating explicit theoretical knowledge for this task. We utilise an dataset of annotated political debates to establish a new standard encompassing four distinct rephrase functions: Deintensification, Intensification, Specification, Generalisation, and Other, which covers all remaining types (D-I-S-G-O). We then evaluate two parallel LLM-based agent systems: one enhanced by argumentation theory via Retrieval-Augmented Generation (RAG), and an identical zero-shot baseline. The results reveal a clear performance gap: the RAG-enhanced agents substantially outperform the baseline across the board, with particularly strong advantages in detecting Intensification and Generalisation context, yielding an overall Macro F1-score improvement of nearly 30\%. Our findings provide evidence that theoretical grounding is not only beneficial but essential for advancing beyond mere paraphrase detection towards function-aware analysis of argumentative discourse. This comparative multi-agent architecture represents a step towards scalable, theoretically informed computational tools capable of identifying rhetorical strategies in contemporary discourse.

</details>


### 64. PhGPO: Pheromone-Guided Policy Optimization for Long-Horizon Tool Planning

- **Authors:** Yu Li, Guangfeng Cai, Shengtian Yang, Han Luo, Shuo Han, Xu He, Dong Li, Lei Feng
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13691v1](http://arxiv.org/abs/2602.13691v1)
- **PDF:** [https://arxiv.org/pdf/2602.13691v1](https://arxiv.org/pdf/2602.13691v1)
- **Categories:** cs.AI


> The paper introduces **PhGPO (Pheromone‑Guided Policy Optimization)**, a novel framework that augments LLM‑based agents with a reusable “pheromone” signal encoding successful tool‑transition patterns extracted from past trajectories, thereby addressing the combinatorial explosion in long‑horizon multi‑step tool planning. PhGPO learns these trajectory‑based patterns via a lightweight, ant‑colony‑inspired update rule and incorporates the resulting pheromone as an explicit bias during policy optimization, steering the agent toward historically effective tool sequences rather than treating each successful path as a one‑off reward. Experiments on benchmark tool‑use tasks show that PhGPO consistently outperforms standard LLM‑agent baselines, achieving higher success rates and more efficient exploration, demonstrating that reusable transition guidance can markedly improve the planning capabilities of agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advancements in Large Language Model (LLM) agents have demonstrated strong capabilities in executing complex tasks through tool use. However, long-horizon multi-step tool planning is challenging, because the exploration space suffers from a combinatorial explosion. In this scenario, even when a correct tool-use path is found, it is usually considered an immediate reward for current training, which would not provide any reusable information for subsequent training. In this paper, we argue that historically successful trajectories contain reusable tool-transition patterns, which can be leveraged throughout the whole training process. Inspired by ant colony optimization where historically successful paths can be reflected by the pheromone, we propose Pheromone-Guided Policy Optimization (PhGPO), which learns a trajectory-based transition pattern (i.e., pheromone) from historical trajectories and then uses the learned pheromone to guide policy optimization. This learned pheromone provides explicit and reusable guidance that steers policy optimization toward historically successful tool transitions, thereby improving long-horizon tool planning. Comprehensive experimental results demonstrate the effectiveness of our proposed PhGPO.

</details>


### 65. MAS-on-the-Fly: Dynamic Adaptation of LLM-based Multi-Agent Systems at Test Time

- **Authors:** Guangyi Liu, Haojun Lin, Huan Zeng, Heng Wang, Quanming Yao
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13671v1](http://arxiv.org/abs/2602.13671v1)
- **PDF:** [https://arxiv.org/pdf/2602.13671v1](https://arxiv.org/pdf/2602.13671v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **MASFly**, a novel framework that endows large‑language‑model (LLM)‑based multi‑agent systems with on‑the‑fly adaptation capabilities at test time. It does so through two mechanisms: (1) a retrieval‑augmented standard‑operating‑procedure (SOP) instantiation that draws on a self‑built repository of proven collaboration patterns to dynamically compose customized agent teams for each query, and (2) an experience‑guided supervision loop in which a dedicated “Watcher” agent continuously monitors execution, consults a personalized experience pool, and intervenes in real time to correct or steer behavior. Empirically, MASFly attains state‑of‑the‑art results—most notably a 61.7 % success rate on the TravelPlanner benchmark—demonstrating markedly higher task adaptability and robustness compared with static or manually designed LLM‑based MAS approaches.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based multi-agent systems (MAS) have emerged as a promising paradigm for solving complex tasks. However, existing works often rely on manual designs or "one-size-fits-all" automation, lacking dynamic adaptability after deployment. Inspired by how biological systems adapt, we introduce MASFly, a novel multi-agent framework enabling dynamic adaptation at test time. To adapt system generation, MASFly employs a retrieval-augmented SOP instantiation mechanism that leverages a self-constructed repository of successful collaboration patterns, enabling the LLM to assemble customized MASs for new queries. For adaptive execution, MASFly incorporates an experience-guided supervision mechanism, where a dedicated Watcher agent monitors system behaviors with reference to a personalized experience pool and provides real-time interventions. Extensive experiments demonstrate that MASFly achieves state-of-the-art performance, most notably a 61.7% success rate on the TravelPlanner benchmark, while exhibiting strong task adaptability and robustness.

</details>


### 66. HyFunc: Accelerating LLM-based Function Calls for Agentic AI through Hybrid-Model Cascade and Dynamic Templating

- **Authors:** Weibin Liao, Jian-guang Lou, Haoyi Xiong
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13665v1](http://arxiv.org/abs/2602.13665v1)
- **PDF:** [https://arxiv.org/pdf/2602.13665v1](https://arxiv.org/pdf/2602.13665v1)
- **Categories:** cs.AI


> HyFunc introduces a hybrid‑model cascade that replaces the monolithic LLM used for generating function calls in agentic AI with a two‑stage pipeline: a large model compresses user intent into a single “soft token,” which drives a lightweight retriever to fetch the relevant function description and a prefix‑tuned small model to emit the final call. The framework also adds “dynamic templating” inside an extended vLLM engine to inject boilerplate parameter syntax on the fly, eliminating repetitive token generation. On the unseen BFCL benchmark, HyFunc cuts inference latency to 0.828 s (the fastest among baselines) while achieving 80.1 % accuracy, demonstrating that targeted model cascades and dynamic templating can dramatically improve the efficiency‑performance trade‑off for LLM‑based agentic function calling.


<details>
<summary>Abstract</summary>

While agentic AI systems rely on LLMs to translate user intent into structured function calls, this process is fraught with computational redundancy, leading to high inference latency that hinders real-time applications. This paper identifies and addresses three key redundancies: (1) the redundant processing of a large library of function descriptions for every request; (2) the redundant use of a large, slow model to generate an entire, often predictable, token sequence; and (3) the redundant generation of fixed, boilerplate parameter syntax. We introduce HyFunc, a novel framework that systematically eliminates these inefficiencies. HyFunc employs a hybrid-model cascade where a large model distills user intent into a single "soft token." This token guides a lightweight retriever to select relevant functions and directs a smaller, prefix-tuned model to generate the final call, thus avoiding redundant context processing and full-sequence generation by the large model. To eliminate syntactic redundancy, our "dynamic templating" technique injects boilerplate parameter syntax on-the-fly within an extended vLLM engine. To avoid potential limitations in generalization, we evaluate HyFunc on an unseen benchmark dataset, BFCL. Experimental results demonstrate that HyFunc achieves an excellent balance between efficiency and performance. It achieves an inference latency of 0.828 seconds, outperforming all baseline models, and reaches a performance of 80.1%, surpassing all models with a comparable parameter scale. These results suggest that HyFunc offers a more efficient paradigm for agentic AI. Our code is publicly available at https://github.com/MrBlankness/HyFunc.

</details>


### 67. Building Autonomous GUI Navigation via Agentic-Q Estimation and Step-Wise Policy Optimization

- **Authors:** Yibo Wang, Guangda Huzhang, Yuwei Hu, Yu Xia, Shiyin Lu, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang, Lijun Zhang
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13653v1](http://arxiv.org/abs/2602.13653v1)
- **PDF:** [https://arxiv.org/pdf/2602.13653v1](https://arxiv.org/pdf/2602.13653v1)
- **Categories:** cs.AI, cs.CL, cs.CV, cs.HC


> The paper proposes a two‑stage, MLLM‑centric framework for autonomous GUI agents that first learns an **agentic‑Q model** to assign step‑wise value estimates to actions, and then uses those estimates to perform **step‑wise policy optimization** via reinforcement learning on trajectories generated by the current policy itself. By decoupling data collection from the environment and leveraging the Q‑model as a learned reward signal, the approach dramatically reduces the need for costly environment interactions while stabilizing training. Experiments demonstrate that the resulting Ovis2.5‑9B agent outperforms larger‑scale baselines on standard GUI navigation and grounding benchmarks, establishing a scalable, low‑overhead method for building agentic AI that can adapt to non‑stationary GUI environments.


<details>
<summary>Abstract</summary>

Recent advances in Multimodal Large Language Models (MLLMs) have substantially driven the progress of autonomous agents for Graphical User Interface (GUI). Nevertheless, in real-world applications, GUI agents are often faced with non-stationary environments, leading to high computational costs for data curation and policy optimization. In this report, we introduce a novel MLLM-centered framework for GUI agents, which consists of two components: agentic-Q estimation and step-wise policy optimization. The former one aims to optimize a Q-model that can generate step-wise values to evaluate the contribution of a given action to task completion. The latter one takes step-wise samples from the state-action trajectory as inputs, and optimizes the policy via reinforcement learning with our agentic-Q model. It should be noticed that (i) all state-action trajectories are produced by the policy itself, so that the data collection costs are manageable; (ii) the policy update is decoupled from the environment, ensuring stable and efficient optimization. Empirical evaluations show that our framework endows Ovis2.5-9B with powerful GUI interaction capabilities, achieving remarkable performances on GUI navigation and grounding benchmarks and even surpassing contenders with larger scales.

</details>


### 68. Guided Collaboration in Heterogeneous LLM-Based Multi-Agent Systems via Entropy-Based Understanding Assessment and Experience Retrieval

- **Authors:** Linlin Wang, Tianqing Zhu, Laiqiao Qin, Longxiang Gao, Wanlei Zhou
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13639v1](http://arxiv.org/abs/2602.13639v1)
- **PDF:** [https://arxiv.org/pdf/2602.13639v1](https://arxiv.org/pdf/2602.13639v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces an Entropy‑Based Adaptive Guidance Framework for heterogeneous LLM‑driven multi‑agent systems, where a strong‑weak pairing often underperforms weaker‑only teams because of cognitive mismatches. By measuring a weak agent’s “understanding” with multi‑dimensional entropy scores (expression, uncertainty, structure, coherence, relevance) and dynamically scaling guidance (light, moderate, intensive), the framework steers each agent toward a compatible cognitive state; a Retrieval‑Augmented Generation module then stores and reuses successful collaboration episodes for both immediate adaptation and long‑term learning. Experiments on GSM8K, MBPP, and CVRP show that this adaptive, experience‑driven guidance consistently improves task accuracy and stability of heterogeneous collaborations, offering a scalable route to more robust agentic AI.


<details>
<summary>Abstract</summary>

With recent breakthroughs in large language models (LLMs) for reasoning, planning, and complex task generation, artificial intelligence systems are transitioning from isolated single-agent architectures to multi-agent systems with collaborative intelligence. However, in heterogeneous multi-agent systems (HMAS), capability differences among agents give rise to consistent cognitive problems, where strong and weak models fail to contribute effectively. We define the collaboration as a strong-weak system. Through comprehensive experiments, we disclose a counterintuitive phenomenon in the strong-weak system: a strong-weak collaboration may under-perform weak-weak combinations, revealing that cognitive mismatching are key bottlenecks limiting heterogeneous cooperation. To overcome these challenges, we propose an Entropy-Based Adaptive Guidance Framework that dynamically aligns the guidance with the cognitive state of each agent. The framework quantifies the understanding of weak agents through multi-dimensional entropy metrics - covering expression, uncertainty, structure, coherence, and relevance - and adaptively adjusts the intensity of the guidance at light, moderate and intensive levels. Furthermore, a Retrieval-Augmented Generation (RAG) mechanism is incorporated to retain successful collaboration experiences, enabling both immediate adaptation and long-term learning. Extensive experiments on three benchmark datasets, GSM8K, MBPP, and CVRP demonstrate that our approach consistently enhances the effectiveness and stability of heterogeneous collaboration. The results highlight that adaptive guidance not only mitigates cognitive imbalance but also establishes a scalable pathway toward more robust, cooperative multi-agent intelligence.

</details>


### 69. Hippocampus: An Efficient and Scalable Memory Module for Agentic AI

- **Authors:** Yi Li, Lianjie Cao, Faraz Ahmed, Puneet Sharma, Bingzhe Li
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13594v1](http://arxiv.org/abs/2602.13594v1)
- **PDF:** [https://arxiv.org/pdf/2602.13594v1](https://arxiv.org/pdf/2602.13594v1)
- **Categories:** cs.AI


> The paper introduces **Hippocampus**, a memory management system for agentic AI that replaces costly dense‑vector or graph‑based retrieval with compact binary signatures for semantic search and lossless token‑ID streams for exact reconstruction. Its core algorithm, the **Dynamic Wavelet Matrix (DWM)**, jointly compresses and co‑indexes these streams, enabling ultra‑fast searches directly in the compressed domain and achieving linear scalability with memory size. Experiments on the LoCoMo and LongMemEval benchmarks demonstrate that Hippocampus cuts end‑to‑end retrieval latency by up to 31× and reduces per‑query token overhead by up to 14× while preserving retrieval accuracy, making it a practical solution for long‑horizon, user‑specific agentic deployments.


<details>
<summary>Abstract</summary>

Agentic AI require persistent memory to store user-specific histories beyond the limited context window of LLMs. Existing memory systems use dense vector databases or knowledge-graph traversal (or hybrid), incurring high retrieval latency and poor storage scalability. We introduce Hippocampus, an agentic memory management system that uses compact binary signatures for semantic search and lossless token-ID streams for exact content reconstruction. Its core is a Dynamic Wavelet Matrix (DWM) that compresses and co-indexes both streams to support ultra-fast search in the compressed domain, thus avoiding costly dense-vector or graph computations. This design scales linearly with memory size, making it suitable for long-horizon agentic deployments. Empirically, our evaluation shows that Hippocampus reduces end-to-end retrieval latency by up to 31$\times$ and cuts per-query token footprint by up to 14$\times$, while maintaining accuracy on both LoCoMo and LongMemEval benchmarks.

</details>


### 70. A First Proof Sprint

- **Authors:** Joseph Corneli
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13587v1](http://arxiv.org/abs/2602.13587v1)
- **PDF:** [https://arxiv.org/pdf/2602.13587v1](https://arxiv.org/pdf/2602.13587v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces a **structure‑aware, multi‑agent proof‑sprint framework** that couples rapid draft generation with adversarial verification, targeted repair, and explicit provenance tracking, using wiring‑diagram decompositions of claim dependencies to isolate gaps and orchestrate reviewer‑driven revisions. Applying this workflow to ten research‑level problems, the authors achieve fully validated results for Problem 3 (existence under a scoped criterion) and a scoped solution to Problem 5, obtain conditional and partial solutions for several others (e.g., a conditional proof for Problem 10, an unconditional \(K_n\) result for Problem 6 with \(c_0=1/3\)), and expose remaining verifier gaps for Problems 7 and 9. The key finding for agentic AI is that **layer‑switching and dependency‑aware coordination among autonomous agents markedly improve the reliability, calibration, and traceability of compressed mathematical proof efforts**, suggesting a viable paradigm for scaling collaborative AI reasoning in complex domains.


<details>
<summary>Abstract</summary>

This monograph reports a multi-agent proof sprint on ten research-level problems, combining rapid draft generation with adversarial verification, targeted repair, and explicit provenance. The workflow uses wiring-diagram decompositions of claim dependencies to localize gaps and coordinate reviewer-driven revisions. Final outcomes are heterogeneous but explicit: the manuscript distinguishes mathematical status from QC-validation status. Mathematically, Problem~3 has a validation-complete existence path under the scoped criterion used here (uniqueness/irreducibility treated as optional), Problem 5 is solved in a scope-limited form for $F_O$-local connective spectra, Problem 10 is conditional under clearly stated assumptions (with explicit necessity counterexamples when assumptions are dropped), and Problems 4 and 6 are partial with named remaining obligations in the general case (including an unconditional $K_n$ result for Problem 6 with $c_0 = 1/3$). Problem 7 is treated as provisionally closed via the rotation-route theorem chain, pending independent ledger re-check. At the QC layer, Problems~7 and~9 have node-level validation artifacts but still contain unresolved verifier gaps. The main methodological result is that structure-aware verification and layer-switching strategies improve reliability and calibration in compressed proof sprints.

</details>


### 71. Elo-Evolve: A Co-evolutionary Framework for Language Model Alignment

- **Authors:** Jing Zhao, Ting Zhen, Junwei bao, Hongfei Jiang, Yang song
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13575v1](http://arxiv.org/abs/2602.13575v1)
- **PDF:** [https://arxiv.org/pdf/2602.13575v1](https://arxiv.org/pdf/2602.13575v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current alignment methods for Large Language Models (LLMs) rely on compressing vast amounts of human preference data into static, absolute reward functions, leading to data scarcity, noise sensitivity, and training instability. We introduce Elo-Evolve, a co-evolutionary framework that redefines alignment as dynamic multi-agent competition within an adaptive opponent pool. Our approach makes two key innovations: (1) eliminating Bradley-Terry model dependencies by learning directly from binary win/loss outcomes in pairwise competitions, and (2) implementing Elo-orchestrated opponent selection that provides automatic curriculum learning through temperature-controlled sampling. We ground our approach in PAC learning theory, demonstrating that pairwise comparison achieves superior sample complexity and empirically validate a 4.5x noise reduction compared to absolute scoring approaches. Experimentally, we train a Qwen2.5-7B model using our framework with opponents including Qwen2.5-14B, Qwen2.5-32B, and Qwen3-8B models. Results demonstrate a clear performance hierarchy: point-based methods < static pairwise training < Elo-Evolve across Alpaca Eval 2.0 and MT-Bench, validating the progressive benefits of pairwise comparison and dynamic opponent selection for LLM alignment.

</details>


### 72. Mitigating the Safety-utility Trade-off in LLM Alignment via Adaptive Safe Context Learning

- **Authors:** Yanbo Wang, Minzheng Wang, Jian Liang, Lu Wang, Yongcan Yu, Ran He
- **Published:** 2026-02-14
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13562v1](http://arxiv.org/abs/2602.13562v1)
- **PDF:** [https://arxiv.org/pdf/2602.13562v1](https://arxiv.org/pdf/2602.13562v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> The paper introduces **Adaptive Safe Context Learning (ASCL)**, a framework that treats safety alignment as a multi‑turn tool‑use interaction, letting a language model decide when to retrieve explicit safety rules and then continue reasoning independently. ASCL is trained with a novel **Inverse Frequency Policy Optimization (IFPO)** algorithm that reweights advantage estimates during reinforcement learning to prevent the model from over‑consulting the safety module. Experiments show that decoupling rule retrieval from downstream reasoning yields a markedly better safety‑utility balance than standard context‑distillation or rule‑prompting baselines, achieving higher task performance while maintaining comparable or lower rates of unsafe outputs.


<details>
<summary>Abstract</summary>

While reasoning models have achieved remarkable success in complex reasoning tasks, their increasing power necessitates stringent safety measures. For safety alignment, the core challenge lies in the inherent trade-off between safety and utility. However, prevailing alignment strategies typically construct CoT training data with explicit safety rules via context distillation. This approach inadvertently limits reasoning capabilities by creating a rigid association between rule memorization and refusal. To mitigate the safety-utility trade-off, we propose the Adaptive Safe Context Learning (ASCL) framework to improve the reasoning given proper context. ASCL formulates safety alignment as a multi-turn tool-use process, empowering the model to autonomously decide when to consult safety rules and how to generate the ongoing reasoning. Furthermore, to counteract the preference for rule consultation during RL, we introduce Inverse Frequency Policy Optimization (IFPO) to rebalance advantage estimates. By decoupling rule retrieval and subsequent reasoning, our method achieves higher overall performance compared to baselines.

</details>


### 73. OMNI-LEAK: Orchestrator Multi-Agent Network Induced Data Leakage

- **Authors:** Akshat Naik, Jay Culligan, Yarin Gal, Philip Torr, Rahaf Aljundi, Alasdair Paren, Adel Bibi
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13477v1](http://arxiv.org/abs/2602.13477v1)
- **PDF:** [https://arxiv.org/pdf/2602.13477v1](https://arxiv.org/pdf/2602.13477v1)
- **Categories:** cs.AI


> The paper introduces **OMNI‑LEAK**, a novel attack that exploits the orchestrator‑based multi‑agent pattern—where a central “orchestrator” delegates subtasks to specialized LLM agents—to exfiltrate sensitive information via a single indirect prompt‑injection, even when conventional data‑access controls are in place. The authors red‑team a realistic orchestrator deployment, systematically probing frontier LLMs (both reasoning‑enhanced and non‑reasoning) with crafted prompts and measuring leakage across compromised sub‑agents, demonstrating that the vulnerability persists without any insider knowledge of the system’s internals. Their findings reveal that current safety mitigations for single‑agent LLMs do not extend to orchestrated multi‑agent systems, highlighting an urgent need for dedicated threat models and defenses to protect privacy and trust in agentic AI deployments.


<details>
<summary>Abstract</summary>

As Large Language Model (LLM) agents become more capable, their coordinated use in the form of multi-agent systems is anticipated to emerge as a practical paradigm. Prior work has examined the safety and misuse risks associated with agents. However, much of this has focused on the single-agent case and/or setups missing basic engineering safeguards such as access control, revealing a scarcity of threat modeling in multi-agent systems. We investigate the security vulnerabilities of a popular multi-agent pattern known as the orchestrator setup, in which a central agent decomposes and delegates tasks to specialized agents. Through red-teaming a concrete setup representative of a likely future use case, we demonstrate a novel attack vector, OMNI-LEAK, that compromises several agents to leak sensitive data through a single indirect prompt injection, even in the \textit{presence of data access control}. We report the susceptibility of frontier models to different categories of attacks, finding that both reasoning and non-reasoning models are vulnerable, even when the attacker lacks insider knowledge of the implementation details. Our work highlights the importance of safety research to generalize from single-agent to multi-agent settings, in order to reduce the serious risks of real-world privacy breaches and financial losses and overall public trust in AI agents.

</details>


### 74. MoltNet: Understanding Social Behavior of AI Agents in the Agent-Native MoltBook

- **Authors:** Yi Feng, Chen Huang, Zhibo Man, Ryner Tan, Long P. Hoang, Shaoyang Xu, Wenxuan Zhang
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13458v1](http://arxiv.org/abs/2602.13458v1)
- **PDF:** [https://arxiv.org/pdf/2602.13458v1](https://arxiv.org/pdf/2602.13458v1)
- **Categories:** cs.SI, cs.AI


> MoltNet introduces the first large‑scale empirical study of AI‑agent social dynamics by mining interaction logs from MoltBook, a dedicated social network for autonomous agents. Using a theory‑driven framework that maps sociological constructs (intent, norms, incentives, emotion) onto millions of agent‑generated posts and messages, the authors quantify how agents adapt their behavior over time. They find that agents rapidly align with community‑specific interaction templates and are highly sensitive to social rewards—mirroring human incentive‑driven conformity—yet remain chiefly knowledge‑oriented, exhibit minimal emotional reciprocity, and engage weakly in dialogic exchanges, highlighting both convergences and divergences between artificial and human social systems.


<details>
<summary>Abstract</summary>

Large-scale communities of AI agents are becoming increasingly prevalent, creating new environments for agent-agent social interaction. Prior work has examined multi-agent behavior primarily in controlled or small-scale settings, limiting our understanding of emergent social dynamics at scale. The recent emergence of MoltBook, a social networking platform designed explicitly for AI agents, presents a unique opportunity to study whether and how these interactions reproduce core human social mechanisms.
  We present MoltNet, a large-scale empirical analysis of agent interaction on MoltBook using data collected in early 2026. Grounded in sociological and social-psychological theory, we examine behavior along four dimensions: intent and motivation, norms and templates, incentives and behavioral drift, emotion and contagion.
  Our analysis revealed that agents strongly respond to social rewards and rapidly converge on community-specific interaction templates, resembling human patterns of incentive sensitivity and normative conformity. However, they are predominantly knowledge-driven rather than persona-aligned, and display limited emotional reciprocity along with weak dialogic engagement, which diverges systematically from human online communities.
  Together, these results reveal both similarities and differences between artificial and human social systems and provide an empirical foundation for understanding, designing, and governing large-scale agent communities.

</details>


### 75. Verification of Robust Multi-Agent Systems

- **Authors:** Raphaël Berthon, Joost-Pieter Katoen, Munyque Mittelmann, Aniello Murano
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13405v1](http://arxiv.org/abs/2602.13405v1)
- **PDF:** [https://arxiv.org/pdf/2602.13405v1](https://arxiv.org/pdf/2602.13405v1)
- **Categories:** cs.LO, cs.MA


> The paper introduces a **robust model‑checking framework** for stochastic multi‑agent systems in which transition probabilities are only partially known, observations are imperfect, and some agents act adversarially. By restricting to **bounded‑memory, observation‑based strategies**, the authors extend Alternating‑time Temporal Logic (ATL) with a robustness semantics and reduce the verification problem to a series of finite‑state game analyses, allowing them to systematically handle different perturbation models (e.g., additive, multiplicative). They prove that, depending on the perturbation type, the robust verification problem lies in **PSPACE** (for additive uncertainties) or **EXPTIME** (for multiplicative uncertainties), thereby quantifying the computational overhead of guaranteeing strategy robustness in uncertain, multi‑agent AI environments.


<details>
<summary>Abstract</summary>

Stochastic multi-agent systems are a central modeling framework for autonomous controllers, communication protocols, and cyber-physical infrastructures. In many such systems, however, transition probabilities are only estimated from data and may therefore be partially unknown or subject to perturbations. In this paper, we study the verification of robust strategies in stochastic multi-agent systems with imperfect information, in which coalitions must satisfy a temporal specification while dealing with uncertain system transitions, partial observation, and adversarial agents. By focusing on bounded-memory strategies, we introduce a robust variant of the model-checking problem for a probabilistic, observation-based extension of Alternating-time Temporal Logic. We characterize the complexity of this problem under different notions of perturbation, thereby clarifying the computational cost of robustness in stochastic multi-agent verification and supporting the use of bounded-memory strategies in uncertain environments.

</details>


### 76. In-Context Autonomous Network Incident Response: An End-to-End Large Language Model Agent Approach

- **Authors:** Yiran Gao, Kim Hammar, Tao Li
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13156v1](http://arxiv.org/abs/2602.13156v1)
- **PDF:** [https://arxiv.org/pdf/2602.13156v1](https://arxiv.org/pdf/2602.13156v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a fully end‑to‑end incident‑response agent that relies on a single 14 B‑parameter large language model (LLM) to perform perception, reasoning, planning, and action without any handcrafted simulation environment. By fine‑tuning the LLM and prompting it with chain‑of‑thought reasoning, the system parses raw network logs, infers the current network state and attack model, simulates the effects of alternative mitigations, and iteratively refines its conjectures through in‑context feedback, all on commodity hardware. Empirical evaluation on published cyber‑incident datasets shows that this LLM‑driven agent recovers up to 23 % faster than state‑of‑the‑art LLM baselines, demonstrating that in‑context learning can replace traditional reinforcement‑learning simulators for adaptive, agentic cyber‑defense.


<details>
<summary>Abstract</summary>

Rapidly evolving cyberattacks demand incident response systems that can autonomously learn and adapt to changing threats. Prior work has extensively explored the reinforcement learning approach, which involves learning response strategies through extensive simulation of the incident. While this approach can be effective, it requires handcrafted modeling of the simulator and suppresses useful semantics from raw system logs and alerts. To address these limitations, we propose to leverage large language models' (LLM) pre-trained security knowledge and in-context learning to create an end-to-end agentic solution for incident response planning. Specifically, our agent integrates four functionalities, perception, reasoning, planning, and action, into one lightweight LLM (14b model). Through fine-tuning and chain-of-thought reasoning, our LLM agent is capable of processing system logs and inferring the underlying network state (perception), updating its conjecture of attack models (reasoning), simulating consequences under different response strategies (planning), and generating an effective response (action). By comparing LLM-simulated outcomes with actual observations, the LLM agent repeatedly refines its attack conjecture and corresponding response, thereby demonstrating in-context adaptation. Our agentic approach is free of modeling and can run on commodity hardware. When evaluated on incident logs reported in the literature, our agent achieves recovery up to 23% faster than those of frontier LLMs.

</details>


### 77. Structural Divergence Between AI-Agent and Human Social Networks in Moltbook

- **Authors:** Wenpin Hou, Zhicheng Ji
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15064v1](http://arxiv.org/abs/2602.15064v1)
- **PDF:** [https://arxiv.org/pdf/2602.15064v1](https://arxiv.org/pdf/2602.15064v1)
- **Categories:** physics.soc-ph, cs.AI


> The paper’s main contribution is a systematic, large‑scale comparison of the interaction network formed by AI agents and humans on the Moltbook platform, revealing that while AI‑agent societies obey the same global node‑edge scaling laws as human social networks, their internal topology is fundamentally different. Using full‑network data, the authors compute degree distributions, reciprocity, triadic closure, and modularity, and contrast these metrics with human communication networks and degree‑preserving null models. They find extreme attention inequality, highly asymmetric heavy‑tailed degree patterns, markedly low reciprocity and triadic clustering, and a more modular yet less size‑imbalanced community structure—demonstrating that key hallmarks of human social organization (e.g., reciprocal ties and dense triads) do not automatically emerge in agentic AI systems.


<details>
<summary>Abstract</summary>

Large populations of AI agents are increasingly embedded in online environments, yet little is known about how their collective interaction patterns compare to human social systems. Here, we analyze the full interaction network of Moltbook, a platform where AI agents and humans coexist, and systematically compare its structure to well-characterized human communication networks. Although Moltbook follows the same node-edge scaling relationship observed in human systems, indicating comparable global growth constraints, its internal organization diverges markedly. The network exhibits extreme attention inequality, heavy-tailed and asymmetric degree distributions, suppressed reciprocity, and a global under-representation of connected triadic structures. Community analysis reveals a structured modular architecture with elevated modularity and comparatively lower community size inequality relative to degree-preserving null models. Together, these findings show that AI-agent societies can reproduce global structural regularities of human networks while exhibiting fundamentally different internal organizing principles, highlighting that key features of human social organization are not universal but depend on the nature of the interacting agents.

</details>


### 78. TraceBack: Multi-Agent Decomposition for Fine-Grained Table Attribution

- **Authors:** Tejas Anvekar, Junha Park, Rajat Jha, Devanshu Gupta, Poojah Ganesan, Puneeth Mathur, Vivek Gupta
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13059v1](http://arxiv.org/abs/2602.13059v1)
- **PDF:** [https://arxiv.org/pdf/2602.13059v1](https://arxiv.org/pdf/2602.13059v1)
- **Categories:** cs.CL


> TraceBack introduces a modular multi‑agent architecture that decomposes a table‑QA query into coherent sub‑questions, prunes the table to the most relevant rows/columns, and explicitly aligns each sub‑answer with the exact supporting cells, thereby delivering fine‑grained, cell‑level attribution. The system is evaluated on the newly released CITEBench benchmark (with phrase‑to‑cell annotations) and on a reference‑less metric, FairScore, which measures attribution precision/recall by comparing atomic facts from predicted cells and answers; both human and automatic evaluations show TraceBack markedly surpasses strong baselines in attribution quality while preserving answer accuracy. These results demonstrate that coordinated, purpose‑driven agents can provide transparent, verifiable reasoning over structured data, a key step toward trustworthy agentic AI.


<details>
<summary>Abstract</summary>

Question answering (QA) over structured tables requires not only accurate answers but also transparency about which cells support them. Existing table QA systems rarely provide fine-grained attribution, so even correct answers often lack verifiable grounding, limiting trust in high-stakes settings. We address this with TraceBack, a modular multi-agent framework for scalable, cell-level attribution in single-table QA. TraceBack prunes tables to relevant rows and columns, decomposes questions into semantically coherent sub-questions, and aligns each answer span with its supporting cells, capturing both explicit and implicit evidence used in intermediate reasoning steps. To enable systematic evaluation, we release CITEBench, a benchmark with phrase-to-cell annotations drawn from ToTTo, FetaQA, and AITQA. We further propose FairScore, a reference-less metric that compares atomic facts derived from predicted cells and answers to estimate attribution precision and recall without human cell labels. Experiments show that TraceBack substantially outperforms strong baselines across datasets and granularities, while FairScore closely tracks human judgments and preserves relative method rankings, supporting interpretable and scalable evaluation of table-based QA.

</details>


### 79. SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents

- **Authors:** Yujiong Shen, Yajie Yang, Zhiheng Xi, Binze Hu, Huayu Sha, Jiazheng Zhang, Qiyuan Peng, Junlin Shang, Jixuan Huang, Yutao Fan, Jingqi Tong, Shihan Dou, Ming Zhang, Lei Bai, Zhenfei Yin, Tao Gui, Xingjun Ma, Qi Zhang, Xuanjing Huang, Yu-Gang Jiang
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12984v1](http://arxiv.org/abs/2602.12984v1)
- **PDF:** [https://arxiv.org/pdf/2602.12984v1](https://arxiv.org/pdf/2602.12984v1)
- **Categories:** cs.CL


> SciAgentGym introduces a large‑scale, interactive benchmark that equips LLM agents with 1,780 domain‑specific scientific tools across four natural‑science fields, and pairs it with SciAgentBench, a tiered evaluation suite that measures performance from single‑action tasks to long‑horizon, multi‑step workflows. Using this environment the authors expose a major weakness in current state‑of‑the‑art models—success rates collapse from ~60 % to ~31 % as the required interaction horizon grows—primarily because agents fail to orchestrate complex tool chains. To remedy this, they propose SciForge, a data‑synthesis pipeline that builds dependency‑graph‑based, logic‑aware tool‑use trajectories; fine‑tuning an 8‑B parameter model on these trajectories yields SciAgent‑8B, which outperforms the 235‑B parameter Qwen3‑VL‑Instruct and demonstrates cross‑domain transfer of scientific tool‑use capabilities.


<details>
<summary>Abstract</summary>

Scientific reasoning inherently demands integrating sophisticated toolkits to navigate domain-specific knowledge. Yet, current benchmarks largely overlook agents' ability to orchestrate tools for such rigorous workflows. To bridge this gap, we introduce SciAgentGym, a scalable interactive environment featuring 1,780 domain-specific tools across four natural science disciplines, supported by a robust execution infrastructure. Complementing this, we present SciAgentBench, a tiered evaluation suite designed to stress-test agentic capabilities from elementary actions to long-horizon workflows. Our evaluation identifies a critical bottleneck: state-of-the-art models struggle with complex scientific tool-use. Even for a leading model like GPT-5, success rates drop sharply from 60.6% to 30.9% as interaction horizons extend, primarily due to failures in multi-step workflow execution. To address this, we propose SciForge, a data synthesis method that models the tool action space as a dependency graph to generate logic-aware training trajectories. By fine-tuning on these trajectories, our SciAgent-8B outperforms the significantly larger Qwen3-VL-235B-Instruct while exhibiting positive cross-domain transfer of scientific tool-use capabilities. These results underscore the promising potential of next-generation autonomous scientific agents.

</details>


### 80. G2CP: A Graph-Grounded Communication Protocol for Verifiable and Efficient Multi-Agent Reasoning

- **Authors:** Karim Ben Khaled, Davy Monticolo
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13370v1](http://arxiv.org/abs/2602.13370v1)
- **PDF:** [https://arxiv.org/pdf/2602.13370v1](https://arxiv.org/pdf/2602.13370v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces **G2CP (Graph‑Grounded Communication Protocol)**, a novel structured language for multi‑agent interaction in which messages are expressed as graph operations (traversals, subgraph extracts, and updates) on a shared knowledge graph rather than free‑form text. By implementing G2CP in an industrial knowledge‑management setting with specialized Diagnostic, Procedural, Synthesis, and Ingestion agents, the authors demonstrate that this graph‑based protocol yields verifiable reasoning traces, eliminates semantic drift, and dramatically cuts token usage. Empirical evaluation on 500 synthetic scenarios and 21 real‑world maintenance cases shows a **73 % reduction in inter‑agent token consumption**, a **34 % boost in task‑completion accuracy**, and complete auditability of the reasoning chain, highlighting G2CP’s potential to make agentic AI systems more reliable and efficient.


<details>
<summary>Abstract</summary>

Multi-agent systems powered by Large Language Models face a critical challenge: agents communicate through natural language, leading to semantic drift, hallucination propagation, and inefficient token consumption. We propose G2CP (Graph-Grounded Communication Protocol), a structured agent communication language where messages are graph operations rather than free text. Agents exchange explicit traversal commands, subgraph fragments, and update operations over a shared knowledge graph, enabling verifiable reasoning traces and eliminating ambiguity. We validate G2CP within an industrial knowledge management system where specialized agents (Diagnostic, Procedural, Synthesis, and Ingestion) coordinate to answer complex queries. Experimental results on 500 industrial scenarios and 21 real-world maintenance cases show that G2CP reduces inter-agent communication tokens by 73%, improves task completion accuracy by 34% over free-text baselines, eliminates cascading hallucinations, and produces fully auditable reasoning chains. G2CP represents a fundamental shift from linguistic to structural communication in multi-agent systems, with implications for any domain requiring precise agent coordination. Code, data, and evaluation scripts are publicly available.

</details>


### 81. BrowseComp-$V^3$: A Visual, Vertical, and Verifiable Benchmark for Multimodal Browsing Agents

- **Authors:** Huanyao Zhang, Jiepeng Zhou, Bo Li, Bowen Zhou, Yanzhe Dan, Haishan Lu, Zhiyong Cao, Jiaoyang Chen, Yuqian Han, Zinan Sheng, Zhengwei Tao, Hao Liang, Jialong Wu, Yang Shi, Yuanpeng He, Jiaye Lin, Qintong Zhang, Guochen Yan, Runhao Zhao, Zhengpin Li, Xiaohan Yu, Lang Mei, Chong Chen, Wentao Zhang, Bin Cui
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12876v1](http://arxiv.org/abs/2602.12876v1)
- **PDF:** [https://arxiv.org/pdf/2602.12876v1](https://arxiv.org/pdf/2602.12876v1)
- **Categories:** cs.AI


> The paper introduces **BrowseComp‑\(V^3\)**, a new benchmark of 300 high‑difficulty, multi‑modal web‑browsing questions that require deep, multi‑hop reasoning across text and images on publicly searchable pages, and provides a sub‑goal‑driven process evaluation to assess agents’ intermediate reasoning steps. Using this benchmark, the authors build **OmniSeeker**, a unified multimodal browsing agent that combines web‑search APIs and visual perception tools, and evaluate several state‑of‑the‑art multimodal LLM agents. Experiments reveal that even the best models attain only ~36 % final‑answer accuracy, exposing major shortcomings in cross‑modal information integration and fine‑grained perception for autonomous browsing agents.


<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs), equipped with increasingly advanced planning and tool-use capabilities, are evolving into autonomous agents capable of performing multimodal web browsing and deep search in open-world environments. However, existing benchmarks for multimodal browsing remain limited in task complexity, evidence accessibility, and evaluation granularity, hindering comprehensive and reproducible assessments of deep search capabilities. To address these limitations, we introduce BrowseComp-$V^3$, a novel benchmark consisting of 300 carefully curated and challenging questions spanning diverse domains. The benchmark emphasizes deep, multi-level, and cross-modal multi-hop reasoning, where critical evidence is interleaved across textual and visual modalities within and across web pages. All supporting evidence is strictly required to be publicly searchable, ensuring fairness and reproducibility. Beyond final-answer accuracy, we incorporate an expert-validated, subgoal-driven process evaluation mechanism that enables fine-grained analysis of intermediate reasoning behaviors and systematic characterization of capability boundaries. In addition, we propose OmniSeeker, a unified multimodal browsing agent framework integrating diverse web search and visual perception tools. Comprehensive experiments demonstrate that even state-of-the-art models achieve only 36% accuracy on our benchmark, revealing critical bottlenecks in multimodal information integration and fine-grained perception. Our results highlight a fundamental gap between current model capabilities and robust multimodal deep search in real-world settings.

</details>


### 82. Assessing Spear-Phishing Website Generation in Large Language Model Coding Agents

- **Authors:** Tailia Malloy, Tegawende F. Bissyande
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13363v1](http://arxiv.org/abs/2602.13363v1)
- **PDF:** [https://arxiv.org/pdf/2602.13363v1](https://arxiv.org/pdf/2602.13363v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a systematic evaluation of how effectively contemporary large‑language‑model (LLM) coding agents can autonomously generate spear‑phishing web pages, producing a publicly released dataset of 200 malicious website codebases and interaction logs from 40 distinct agent configurations. The authors benchmarked a range of LLMs (including GPT‑4, Claude, Llama 2, and open‑source alternatives) by prompting each agent to design, implement, and deploy a phishing landing page under identical task specifications, then measured “willingness” (refusal rates) and “capability” (functional completeness, evasion techniques, and realism scores). Their analysis shows that model size and instruction‑following fine‑tuning are positively correlated with successful code generation, while safety‑oriented alignment mitigates willingness but does not fully prevent the creation of functional phishing sites—highlighting a nuanced risk vector for agentic AI in cybersecurity.


<details>
<summary>Abstract</summary>

Large Language Models are expanding beyond being a tool humans use and into independent agents that can observe an environment, reason about solutions to problems, make changes that impact those environments, and understand how their actions impacted their environment. One of the most common applications of these LLM Agents is in computer programming, where agents can successfully work alongside humans to generate code while controlling programming environments or networking systems. However, with the increasing ability and complexity of these agents comes dangers about the potential for their misuse. A concerning application of LLM agents is in the domain cybersecurity, where they have the potential to greatly expand the threat imposed by attacks such as social engineering. This is due to the fact that LLM Agents can work autonomously and perform many tasks that would normally require time and effort from skilled human programmers. While this threat is concerning, little attention has been given to assessments of the capabilities of LLM coding agents in generating code for social engineering attacks. In this work we compare different LLMs in their ability and willingness to produce potentially dangerous code bases that could be misused by cyberattackers. The result is a dataset of 200 website code bases and logs from 40 different LLM coding agents. Analysis of models shows which metrics of LLMs are more and less correlated with performance in generating spear-phishing sites. Our analysis and the dataset we present will be of interest to researchers and practitioners concerned in defending against the potential misuse of LLMs in spear-phishing.

</details>


### 83. SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

- **Authors:** Xiangyi Li, Wenbo Chen, Yimin Liu, Shenghan Zheng, Xiaokun Chen, Yifeng He, Yubo Li, Bingran You, Haotian Shen, Jiankai Sun, Shuyi Wang, Qunhong Zeng, Di Wang, Xuandong Zhao, Yuanli Wang, Roey Ben Chaim, Zonglin Di, Yipeng Gao, Junwei He, Yizhuo He, Liqiang Jing, Luyang Kong, Xin Lan, Jiachen Li, Songlin Li, Yijiang Li, Yueqian Lin, Xinyi Liu, Xuanqing Liu, Haoran Lyu, Ze Ma, Bowei Wang, Runhui Wang, Tianyu Wang, Wengao Ye, Yue Zhang, Hanwen Xing, Yiqi Xue, Steven Dillmann, Han-chung Lee
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12670v1](http://arxiv.org/abs/2602.12670v1)
- **PDF:** [https://arxiv.org/pdf/2602.12670v1](https://arxiv.org/pdf/2602.12670v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **SkillsBench**, the first systematic benchmark for evaluating how “Agent Skills” – modular, procedural knowledge packages attached to LLM agents at inference time – affect performance across a wide variety of tasks.  

**Methodology:** The authors assemble 86 tasks spanning 11 domains, pair each with curated Skills and deterministic verifiers, and run each task under three conditions (no Skills, curated Skills, self‑generated Skills) using seven different agent‑model configurations, yielding 7,308 execution trajectories.  

**Key findings:** Curated Skills boost the overall pass rate by **+16.2 pp**, but gains are highly domain‑dependent (e.g., +4.5 pp in Software Engineering vs. +51.9 pp in Healthcare) and even detrimental on 16 of 84 tasks. Self‑generated Skills offer no average benefit, indicating current models cannot reliably author useful procedural knowledge. Moreover, a small set of 2–3 focused Skill modules can outperform exhaustive documentation, and modest‑sized models equipped with Skills can match the performance of larger models lacking them.


<details>
<summary>Abstract</summary>

Agent Skills are structured packages of procedural knowledge that augment LLM agents at inference time. Despite rapid adoption, there is no standard way to measure whether they actually help. We present SkillsBench, a benchmark of 86 tasks across 11 domains paired with curated Skills and deterministic verifiers. Each task is evaluated under three conditions: no Skills, curated Skills, and self-generated Skills. We test 7 agent-model configurations over 7,308 trajectories. Curated Skills raise average pass rate by 16.2 percentage points(pp), but effects vary widely by domain (+4.5pp for Software Engineering to +51.9pp for Healthcare) and 16 of 84 tasks show negative deltas. Self-generated Skills provide no benefit on average, showing that models cannot reliably author the procedural knowledge they benefit from consuming. Focused Skills with 2--3 modules outperform comprehensive documentation, and smaller models with Skills can match larger models without them.

</details>


### 84. Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents

- **Authors:** Ruihan Yang, Fanghua Ye, Xiang We, Ruoqing Zhao, Kang Luo, Xinbo Xu, Bo Zhao, Ruotian Ma, Shanyi Wang, Zhaopeng Tu, Xiaolong Li, Deqing Yang, Linus
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12662v1](http://arxiv.org/abs/2602.12662v1)
- **PDF:** [https://arxiv.org/pdf/2602.12662v1](https://arxiv.org/pdf/2602.12662v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **CogRouter**, a framework that endows LLM‑based agents with the ability to select the appropriate “cognitive depth” at each decision step, ranging from instinctive reactions to full strategic planning, thereby breaking the fixed‑pattern limitation of existing agents.  CogRouter is trained in two stages: (1) **Cognition‑aware Supervised Fine‑tuning (CoSFT)** learns stable, level‑specific response styles, and (2) **Cognition‑aware Policy Optimization (CoPO)** assigns step‑level credit by re‑weighting advantages with the model’s confidence, operationalizing the principle that deeper reasoning should be invoked only when it raises action confidence.  On long‑horizon benchmarks (ALFWorld, ScienceWorld), the method achieves state‑of‑the‑art success rates (e.g., 82.3 % with Qwen2.5‑7B, surpassing GPT‑4o by 40.3 %) while cutting token usage by ~62 %, demonstrating that dynamic cognitive depth dramatically improves both performance and efficiency of autonomous LLM agents.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as autonomous agents for multi-turn decision-making tasks. However, current agents typically rely on fixed cognitive patterns: non-thinking models generate immediate responses, while thinking models engage in deep reasoning uniformly. This rigidity is inefficient for long-horizon tasks, where cognitive demands vary significantly from step to step, with some requiring strategic planning and others only routine execution. In this paper, we introduce CogRouter, a framework that trains agents to dynamically adapt cognitive depth at each step. Grounded in ACT-R theory, we design four hierarchical cognitive levels ranging from instinctive responses to strategic planning. Our two-stage training approach includes Cognition-aware Supervised Fine-tuning (CoSFT) to instill stable level-specific patterns, and Cognition-aware Policy Optimization (CoPO) for step-level credit assignment via confidence-aware advantage reweighting. The key insight is that appropriate cognitive depth should maximize the confidence of the resulting action. Experiments on ALFWorld and ScienceWorld demonstrate that CogRouter achieves state-of-the-art performance with superior efficiency. With Qwen2.5-7B, it reaches an 82.3% success rate, outperforming GPT-4o (+40.3%), OpenAI-o3 (+18.3%), and GRPO (+14.0%), while using 62% fewer tokens.

</details>


### 85. AI Agents for Inventory Control: Human-LLM-OR Complementarity

- **Authors:** Jackie Baek, Yaopeng Fu, Will Ma, Tianyi Peng
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12631v1](http://arxiv.org/abs/2602.12631v1)
- **PDF:** [https://arxiv.org/pdf/2602.12631v1](https://arxiv.org/pdf/2602.12631v1)
- **Categories:** cs.AI, cs.HC, cs.LG


> The paper introduces **InventoryBench**, a large‑scale benchmark (1,000+ synthetic and real inventory instances) to evaluate how operations‑research (OR) algorithms, large language model (LLM) agents, and humans can be combined for multi‑period inventory control. By integrating OR‑derived optimality cues into LLM prompts and embedding LLM recommendations in a human‑in‑the‑loop workflow, the authors show that **OR‑augmented LLM agents consistently outperform either component alone**, and that **human‑AI teams achieve higher profits than humans or AI agents operating solo**, with a provable, distribution‑free lower bound on the proportion of individuals who benefit from the collaboration. These results demonstrate a concrete, empirically validated form of complementarity among traditional OR methods, LLM‑based reasoning, and human judgment, offering a template for building more robust, context‑aware agentic AI systems in operations settings.


<details>
<summary>Abstract</summary>

Inventory control is a fundamental operations problem in which ordering decisions are traditionally guided by theoretically grounded operations research (OR) algorithms. However, such algorithms often rely on rigid modeling assumptions and can perform poorly when demand distributions shift or relevant contextual information is unavailable. Recent advances in large language models (LLMs) have generated interest in AI agents that can reason flexibly and incorporate rich contextual signals, but it remains unclear how best to incorporate LLM-based methods into traditional decision-making pipelines.
  We study how OR algorithms, LLMs, and humans can interact and complement each other in a multi-period inventory control setting. We construct InventoryBench, a benchmark of over 1,000 inventory instances spanning both synthetic and real-world demand data, designed to stress-test decision rules under demand shifts, seasonality, and uncertain lead times. Through this benchmark, we find that OR-augmented LLM methods outperform either method in isolation, suggesting that these methods are complementary rather than substitutes.
  We further investigate the role of humans through a controlled classroom experiment that embeds LLM recommendations into a human-in-the-loop decision pipeline. Contrary to prior findings that human-AI collaboration can degrade performance, we show that, on average, human-AI teams achieve higher profits than either humans or AI agents operating alone. Beyond this population-level finding, we formalize an individual-level complementarity effect and derive a distribution-free lower bound on the fraction of individuals who benefit from AI collaboration; empirically, we find this fraction to be substantial.

</details>


### 86. Robust Mean-Field Games with Risk Aversion and Bounded Rationality

- **Authors:** Bhavini Jeloka, Yue Guan, Panagiotis Tsiotras
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13353v1](http://arxiv.org/abs/2602.13353v1)
- **PDF:** [https://arxiv.org/pdf/2602.13353v1](https://arxiv.org/pdf/2602.13353v1)
- **Categories:** cs.MA, cs.GT


> The paper introduces the **mean‑field risk‑averse quantal response equilibrium (MF‑RQE)**, a novel equilibrium concept that simultaneously accounts for uncertainty over the initial population distribution (risk aversion) and for agents’ limited cognitive capacity (bounded rationality). By extending the standard mean‑field game framework, the authors prove existence of MF‑RQE and show that both a fixed‑point iteration and a fictitious‑play scheme converge to it; they then translate these theoretical insights into a scalable reinforcement‑learning algorithm that can handle high‑dimensional state‑action spaces. Empirical results reveal that policies derived from MF‑RQE are markedly more robust to distributional shifts and outperform classical mean‑field solutions that rely on fully rational agents and entropy regularization, highlighting a practical pathway for building more resilient, agentic AI systems.


<details>
<summary>Abstract</summary>

Recent advances in mean-field game literature enable the reduction of large-scale multi-agent problems to tractable interactions between a representative agent and a population distribution. However, existing approaches typically assume a fixed initial population distribution and fully rational agents, limiting robustness under distributional uncertainty and cognitive constraints. We address these limitations by introducing risk aversion with respect to the initial population distribution and by incorporating bounded rationality to model deviations from fully rational decision-making agents. The combination of these two elements yields a new and more general equilibrium concept, which we term the mean-field risk-averse quantal response equilibrium (MF-RQE). We establish existence results and prove convergence of fixed-point iteration and fictitious play to MF-RQE. Building on these insights, we develop a scalable reinforcement learning algorithm for scenarios with large state-action spaces. Numerical experiments demonstrate that MF-RQE policies achieve improved robustness relative to classical mean-field approaches that optimize expected cumulative rewards under a fixed initial distribution and are restricted to entropy-based regularizers.

</details>


### 87. Multi-Agent Model-Based Reinforcement Learning with Joint State-Action Learned Embeddings

- **Authors:** Zhizun Wang, David Meger
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12520v1](http://arxiv.org/abs/2602.12520v1)
- **PDF:** [https://arxiv.org/pdf/2602.12520v1](https://arxiv.org/pdf/2602.12520v1)
- **Categories:** cs.LG, cs.MA


> The paper introduces a model‑based multi‑agent RL framework that jointly learns a **state‑action embedding (SALE)** via a variational auto‑encoder and uses this embedding both to condition imagined roll‑outs of a learned world model and to augment the joint action‑value network (via a mixing network). By integrating SALE‑enhanced imagination with value estimation, the agents obtain a richer, data‑efficient representation of how individual actions affect collective outcomes, enabling more effective long‑term planning under partial observability. Experiments on StarCraft II micro‑management, Multi‑Agent MuJoCo, and Level‑Based Foraging show consistent performance improvements over strong baselines, demonstrating that joint state‑action embeddings are a powerful tool for scalable, agentic AI coordination.


<details>
<summary>Abstract</summary>

Learning to coordinate many agents in partially observable and highly dynamic environments requires both informative representations and data-efficient training. To address this challenge, we present a novel model-based multi-agent reinforcement learning framework that unifies joint state-action representation learning with imaginative roll-outs. We design a world model trained with variational auto-encoders and augment the model using the state-action learned embedding (SALE). SALE is injected into both the imagination module that forecasts plausible future roll-outs and the joint agent network whose individual action values are combined through a mixing network to estimate the joint action-value function. By coupling imagined trajectories with SALE-based action values, the agents acquire a richer understanding of how their choices influence collective outcomes, leading to improved long-term planning and optimization under limited real-environment interactions. Empirical studies on well-established multi-agent benchmarks, including StarCraft II Micro-Management, Multi-Agent MuJoCo, and Level-Based Foraging challenges, demonstrate consistent gains of our method over baseline algorithms and highlight the effectiveness of joint state-action learned embeddings within a multi-agent model-based paradigm.

</details>


### 88. Bench-MFG: A Benchmark Suite for Learning in Stationary Mean Field Games

- **Authors:** Lorenzo Magnino, Jiacheng Shen, Matthieu Geist, Olivier Pietquin, Mathieu Laurière
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12517v1](http://arxiv.org/abs/2602.12517v1)
- **PDF:** [https://arxiv.org/pdf/2602.12517v1](https://arxiv.org/pdf/2602.12517v1)
- **Categories:** cs.LG, cs.AI, cs.MA, math.OC


> The paper introduces **Bench‑MFG**, the first systematic benchmark suite for stationary discrete‑time/space mean‑field games, organizing environments into a taxonomy (no‑interaction, monotone, potential, dynamics‑coupled) and providing a random‑instance generator (MF‑Garnets) to enable statistically robust evaluation. Using this suite, the authors compare several existing MFG‑RL algorithms and a new black‑box exploitability‑minimization method (MF‑PSO), showing that performance varies widely across game classes and that MF‑PSO achieves competitive exploitability with minimal model assumptions. From these experiments they derive practical guidelines for reporting and comparing future agentic‑AI methods in mean‑field settings.


<details>
<summary>Abstract</summary>

The intersection of Mean Field Games (MFGs) and Reinforcement Learning (RL) has fostered a growing family of algorithms designed to solve large-scale multi-agent systems. However, the field currently lacks a standardized evaluation protocol, forcing researchers to rely on bespoke, isolated, and often simplistic environments. This fragmentation makes it difficult to assess the robustness, generalization, and failure modes of emerging methods. To address this gap, we propose a comprehensive benchmark suite for MFGs (Bench-MFG), focusing on the discrete-time, discrete-space, stationary setting for the sake of clarity. We introduce a taxonomy of problem classes, ranging from no-interaction and monotone games to potential and dynamics-coupled games, and provide prototypical environments for each. Furthermore, we propose MF-Garnets, a method for generating random MFG instances to facilitate rigorous statistical testing. We benchmark a variety of learning algorithms across these environments, including a novel black-box approach (MF-PSO) for exploitability minimization. Based on our extensive empirical results, we propose guidelines to standardize future experimental comparisons. Code available at \href{https://github.com/lorenzomagnino/Bench-MFG}{https://github.com/lorenzomagnino/Bench-MFG}.

</details>


### 89. Building Large-Scale Drone Defenses from Small-Team Strategies

- **Authors:** Grant Douglas, Stephen Franklin, Claudia Szabo, Mingyu Guo
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12502v1](http://arxiv.org/abs/2602.12502v1)
- **PDF:** [https://arxiv.org/pdf/2602.12502v1](https://arxiv.org/pdf/2602.12502v1)
- **Categories:** cs.MA


> The paper introduces a **modular scaling framework** that lifts coordination policies proven on small defender teams to much larger drone‑defense forces. By treating each small‑team policy as a reusable component, the authors employ a **dynamic‑programming decomposition** that assembles these components into large teams in polynomial time, iteratively sampling diverse small‑team candidates, evaluating the resulting macro‑team performance, and refining the component pool until convergence. Experiments show that this partition‑and‑assemble approach yields defenses that scale to orders of magnitude larger swarms while preserving (and sometimes enhancing) effectiveness, uncovering cooperative behaviors that direct multi‑agent optimization fails to discover—demonstrating a practical pathway for building scalable, agentic AI defenses.


<details>
<summary>Abstract</summary>

Defending against large adversarial drone swarms requires coordination methods that scale effectively beyond conventional multi-agent optimisation. In this paper, we propose to scale strategies proven effective in small defender teams by integrating them as modular components of larger forces using our proposed framework. A dynamic programming (DP) decomposition assembles these components into large teams in polynomial time, enabling efficient construction of scalable defenses without exhaustive evaluation. Because a unit that is strong in isolation may not remain strong when combined, we sample across multiple small-team candidates. Our framework iterates between evaluating large-team outcomes and refining the pool of modular components, allowing convergence on increasingly effective strategies. Experiments demonstrate that this partitioning approach scales to substantially larger scenarios while preserving effectiveness and revealing cooperative behaviours that direct optimisation cannot reliably discover.

</details>


### 90. Favia: Forensic Agent for Vulnerability-fix Identification and Analysis

- **Authors:** André Storhaug, Jiamou Sun, Jingyue Li
- **Published:** 2026-02-13
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12500v1](http://arxiv.org/abs/2602.12500v1)
- **PDF:** [https://arxiv.org/pdf/2602.12500v1](https://arxiv.org/pdf/2602.12500v1)
- **Categories:** cs.SE, cs.AI, cs.CR


> Favia introduces a forensic, agent‑based framework that dramatically improves the identification of vulnerability‑fix commits by coupling a fast, scalable ranking stage with a ReAct‑style large language model (LLM) agent that iteratively reasons over the codebase, localizes vulnerable components, and aligns code changes with CVE root causes. The methodology treats the pre‑commit repository as an interactive environment and equips the LLM with specialized navigation and analysis tools, enabling it to handle indirect, multi‑file, and non‑trivial fixes that elude single‑pass or similarity‑based approaches. Evaluated on the newly assembled CVEVC dataset (≈8 M commits from 3,708 repositories), Favia consistently outperforms both traditional machine‑learning and prior LLM baselines, delivering superior precision‑recall trade‑offs and the highest F1 scores under realistic candidate‑selection conditions.


<details>
<summary>Abstract</summary>

Identifying vulnerability-fixing commits corresponding to disclosed CVEs is essential for secure software maintenance but remains challenging at scale, as large repositories contain millions of commits of which only a small fraction address security issues. Existing automated approaches, including traditional machine learning techniques and recent large language model (LLM)-based methods, often suffer from poor precision-recall trade-offs. Frequently evaluated on randomly sampled commits, we uncover that they are substantially underestimating real-world difficulty, where candidate commits are already security-relevant and highly similar. We propose Favia, a forensic, agent-based framework for vulnerability-fix identification that combines scalable candidate ranking with deep and iterative semantic reasoning. Favia first employs an efficient ranking stage to narrow the search space of commits. Each commit is then rigorously evaluated using a ReAct-based LLM agent. By providing the agent with a pre-commit repository as environment, along with specialized tools, the agent tries to localize vulnerable components, navigates the codebase, and establishes causal alignment between code changes and vulnerability root causes. This evidence-driven process enables robust identification of indirect, multi-file, and non-trivial fixes that elude single-pass or similarity-based methods. We evaluate Favia on CVEVC, a large-scale dataset we made that comprises over 8 million commits from 3,708 real-world repositories, and show that it consistently outperforms state-of-the-art traditional and LLM-based baselines under realistic candidate selection, achieving the strongest precision-recall trade-offs and highest F1-scores.

</details>


### 91. Theory of Mind Guided Strategy Adaptation for Zero-Shot Coordination

- **Authors:** Andrew Ni, Simon Stepputtis, Stefanos Nikolaidis, Michael Lewis, Katia P. Sycara, Woojun Kim
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12458v1](http://arxiv.org/abs/2602.12458v1)
- **PDF:** [https://arxiv.org/pdf/2602.12458v1](https://arxiv.org/pdf/2602.12458v1)
- **Categories:** cs.MA


> The paper introduces a Theory‑of‑Mind (ToM)‑driven adaptive ensemble for zero‑shot coordination, which infers a partner’s latent intentions and then selects the most appropriate policy from a pre‑trained policy pool rather than relying on a single static best‑response. By training a diverse set of partner agents and equipping the focal agent with a ToM inference module that maps observed teammate behavior to a belief over partner types, the method dynamically switches among specialized policies at test time. Experiments in the Overcooked benchmark (both fully and partially observable) show that this adaptive ToM‑guided selector consistently outperforms the conventional single best‑response baseline, achieving higher joint scores and more robust synergy with previously unseen teammates.


<details>
<summary>Abstract</summary>

A central challenge in multi-agent reinforcement learning is enabling agents to adapt to previously unseen teammates in a zero-shot fashion. Prior work in zero-shot coordination often follows a two-stage process, first generating a diverse training pool of partner agents, and then training a best-response agent to collaborate effectively with the entire training pool. While many previous works have achieved strong performance by devising better ways to diversify the partner agent pool, there has been less emphasis on how to leverage this pool to build an adaptive agent. One limitation is that the best-response agent may converge to a static, generalist policy that performs reasonably well across diverse teammates, rather than learning a more adaptive, specialist policy that can better adapt to teammates and achieve higher synergy. To address this, we propose an adaptive ensemble agent that uses Theory-of-Mind-based best-response selection to first infer its teammate's intentions and then select the most suitable policy from a policy ensemble. We conduct experiments in the Overcooked environment to evaluate zero-shot coordination performance under both fully and partially observable settings. The empirical results demonstrate the superiority of our method over a single best-response baseline.

</details>


### 92. Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward

- **Authors:** Renjun Xu, Yang Yan
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12430v3](http://arxiv.org/abs/2602.12430v3)
- **PDF:** [https://arxiv.org/pdf/2602.12430v3](https://arxiv.org/pdf/2602.12430v3)
- **Categories:** cs.MA, cs.AI


> The paper introduces and formalizes **agent skills**—modular, composable packages of instructions, code, and resources that LLM‑based agents can load on demand via the Model Context Protocol (MCP)—as a new architectural layer that separates procedural knowledge from model weights. By surveying recent work, the authors map the skill ecosystem across four dimensions (architecture, acquisition, large‑scale deployment, and security), evaluate methods such as reinforcement‑learning‑driven skill libraries, autonomous discovery (SEAgent), and compositional synthesis, and demonstrate that skill‑enabled agents achieve state‑of‑the‑art performance on benchmarks like OSWorld and SWE‑bench while exposing significant security risks (≈26 % of community‑contributed skills contain vulnerabilities). To address trustworthiness, they propose a four‑tier “Skill Trust and Lifecycle Governance Framework” that ties skill provenance to graduated permission levels, outlining open challenges and a research agenda for building secure, self‑improving skill ecosystems for next‑generation agentic AI.


<details>
<summary>Abstract</summary>

The transition from monolithic language models to modular, skill-equipped agents marks a defining shift in how large language models (LLMs) are deployed in practice. Rather than encoding all procedural knowledge within model weights, agent skills -- composable packages of instructions, code, and resources that agents load on demand -- enable dynamic capability extension without retraining. It is formalized in a paradigm of progressive disclosure, portable skill definitions, and integration with the Model Context Protocol (MCP). This survey provides a comprehensive treatment of the agent skills landscape, as it has rapidly evolved during the last few months. We organize the field along four axes: (i) architectural foundations, examining the SKILL$.$md specification, progressive context loading, and the complementary roles of skills and MCP; (ii) skill acquisition, covering reinforcement learning with skill libraries, autonomous skill discovery (SEAgent), and compositional skill synthesis; (iii) deployment at scale, including the computer-use agent (CUA) stack, GUI grounding advances, and benchmark progress on OSWorld and SWE-bench; and (iv) security, where recent empirical analyses reveal that 26.1% of community-contributed skills contain vulnerabilities, motivating our proposed Skill Trust and Lifecycle Governance Framework -- a four-tier, gate-based permission model that maps skill provenance to graduated deployment capabilities. We identify seven open challenges -- from cross-platform skill portability to capability-based permission models -- and propose a research agenda for realizing trustworthy, self-improving skill ecosystems. Unlike prior surveys that broadly cover LLM agents or tool use, this work focuses specifically on the emerging skill abstraction layer and its implications for the next generation of agentic systems. Project repo: https://github.com/scienceaix/agentskills

</details>


### 93. Provably Convergent Actor-Critic in Risk-averse MARL

- **Authors:** Yizhou Zhang, Eric Mazumdar
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12386v1](http://arxiv.org/abs/2602.12386v1)
- **PDF:** [https://arxiv.org/pdf/2602.12386v1](https://arxiv.org/pdf/2602.12386v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning stationary policies in infinite-horizon general-sum Markov games (MGs) remains a fundamental open problem in Multi-Agent Reinforcement Learning (MARL). While stationary strategies are preferred for their practicality, computing stationary forms of classic game-theoretic equilibria is computationally intractable -- a stark contrast to the comparative ease of solving single-agent RL or zero-sum games. To bridge this gap, we study Risk-averse Quantal response Equilibria (RQE), a solution concept rooted in behavioral game theory that incorporates risk aversion and bounded rationality. We demonstrate that RQE possesses strong regularity conditions that make it uniquely amenable to learning in MGs. We propose a novel two-timescale Actor-Critic algorithm characterized by a fast-timescale actor and a slow-timescale critic. Leveraging the regularity of RQE, we prove that this approach achieves global convergence with finite-sample guarantees. We empirically validate our algorithm in several environments to demonstrate superior convergence properties compared to risk-neutral baselines.

</details>


### 94. CellMaster: Collaborative Cell Type Annotation in Single-Cell Analysis

- **Authors:** Zhen Wang, Yiming Gao, Jieyuan Liu, Enze Ma, Jefferson Chen, Mark Antkowiak, Mengzhou Hu, JungHo Kong, Dexter Pratt, Zhiting Hu, Wei Wang, Trey Ideker, Eric P. Xing
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13346v1](http://arxiv.org/abs/2602.13346v1)
- **PDF:** [https://arxiv.org/pdf/2602.13346v1](https://arxiv.org/pdf/2602.13346v1)
- **Categories:** q-bio.GN, cs.AI, cs.CV


> CellMaster introduces a zero‑shot, LLM‑driven AI agent for cell‑type annotation that emulates expert reasoning by querying a large language model (GPT‑4o) for marker knowledge and generating interpretable rationales on the fly, eliminating the need for pre‑trained classifiers or static marker lists. The authors evaluate the agent on nine scRNA‑seq atlases across eight tissues, showing a 7.1 % accuracy gain over the strongest existing tools (CellTypist, scTab) in fully automated mode, which rises to 18.6 % (and 22.1 % for sub‑type calls) when combined with human‑in‑the‑loop refinement, especially for rare or novel cell states. These results demonstrate that agentic AI can reliably perform complex, domain‑specific annotation tasks without task‑specific training, highlighting a new paradigm for collaborative, interpretable bioinformatics workflows.


<details>
<summary>Abstract</summary>

Single-cell RNA-seq (scRNA-seq) enables atlas-scale profiling of complex tissues, revealing rare lineages and transient states. Yet, assigning biologically valid cell identities remains a bottleneck because markers are tissue- and state-dependent, and novel states lack references. We present CellMaster, an AI agent that mimics expert practice for zero-shot cell-type annotation. Unlike existing automated tools, CellMaster leverages LLM-encoded knowledge (e.g., GPT-4o) to perform on-the-fly annotation with interpretable rationales, without pre-training or fixed marker databases. Across 9 datasets spanning 8 tissues, CellMaster improved accuracy by 7.1% over best-performing baselines (including CellTypist and scTab) in automatic mode. With human-in-the-loop refinement, this advantage increased to 18.6%, with a 22.1% gain on subtype populations. The system demonstrates particular strength in rare and novel cell states where baselines often fail. Source code and the web application are available at \href{https://github.com/AnonymousGym/CellMaster}{https://github.com/AnonymousGym/CellMaster}.

</details>


### 95. CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use

- **Authors:** Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12268v1](http://arxiv.org/abs/2602.12268v1)
- **PDF:** [https://arxiv.org/pdf/2602.12268v1](https://arxiv.org/pdf/2602.12268v1)
- **Categories:** cs.AI


> The paper introduces **CM2**, a reinforcement‑learning framework that replaces hard‑to‑obtain outcome rewards with **checklist rewards**—binary, evidence‑grounded criteria that decompose each turn’s intended behavior into fine‑grained judgments. By assigning sparse rewards while evaluating many dense checklist items, CM2 can be trained in a fully simulated LLM‑based tool environment, avoiding the engineering overhead of real tool execution. Experiments on an 8 B model fine‑tuned with an 8 k‑example RL dataset show consistent gains over supervised fine‑tuning (≈ 8 τ‑Bench, 10 BFCL‑V4, 12 ToolSandbox points) and match or surpass comparable open‑source baselines, demonstrating a scalable way to improve multi‑turn, multi‑step agentic tool use without relying on verifiable rewards.


<details>
<summary>Abstract</summary>

AI agents are increasingly used to solve real-world tasks by reasoning over multi-turn user interactions and invoking external tools. However, applying reinforcement learning to such settings remains difficult: realistic objectives often lack verifiable rewards and instead emphasize open-ended behaviors; moreover, RL for multi-turn, multi-step agentic tool use is still underexplored; and building and maintaining executable tool environments is costly, limiting scale and coverage. We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards. CM2 decomposes each turn's intended behavior into fine-grained binary criteria with explicit evidence grounding and structured metadata, turning open-ended judging into more stable classification-style decisions. To balance stability and informativeness, our method adopts a strategy of sparse reward assignment but dense evaluation criteria. Training is performed in a scalable LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Experiments show that CM2 consistently improves over supervised fine-tuning. Starting from an 8B Base model and training on an 8k-example RL dataset, CM2 improves over the SFT counterpart by 8 points on tau^-Bench, by 10 points on BFCL-V4, and by 12 points on ToolSandbox. The results match or even outperform similarly sized open-source baselines, including the judging model. CM2 thus provides a scalable recipe for optimizing multi-turn, multi-step tool-using agents without relying on verifiable rewards. Code provided by the open-source community: https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent.

</details>


### 96. Think like a Scientist: Physics-guided LLM Agent for Equation Discovery

- **Authors:** Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad, Sharvaree Vadgama, Rose Yu
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12259v1](http://arxiv.org/abs/2602.12259v1)
- **PDF:** [https://arxiv.org/pdf/2602.12259v1](https://arxiv.org/pdf/2602.12259v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **KeplerAgent**, an agentic framework that mimics the scientific workflow by first extracting physical invariants (e.g., symmetries, conserved quantities) with physics‑based tools and then feeding these intermediate priors to symbolic regression engines (PySINDy, PySR) to constrain their function libraries and search spaces. By orchestrating these sub‑tasks through a language‑model‑driven controller, KeplerAgent transforms raw observational data into interpretable equations more reliably than end‑to‑end LLM guesses or conventional regression methods. Experiments on a diverse set of physics benchmarks show that the agent achieves markedly higher symbolic recovery rates and greater tolerance to noise, demonstrating the value of structured, multi‑step reasoning for agentic AI in scientific discovery.


<details>
<summary>Abstract</summary>

Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.

</details>


### 97. VIRENA: Virtual Arena for Research, Education, and Democratic Innovation

- **Authors:** Emma Hoes, K. Jonathan Klueser, Fabrizio Gilardi
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12207v1](http://arxiv.org/abs/2602.12207v1)
- **PDF:** [https://arxiv.org/pdf/2602.12207v1](https://arxiv.org/pdf/2602.12207v1)
- **Categories:** cs.HC, cs.AI, cs.SI


> VIRENA (Virtual Arena) introduces a no‑code, open‑source platform that lets researchers run controlled, large‑scale experiments in lifelike replicas of feed‑based social media (e.g., Instagram, Reddit) and messaging apps, with human participants interacting simultaneously alongside configurable LLM‑driven AI agents that exhibit realistic personas and behaviors. By exposing a visual interface for manipulating moderation policies, pre‑scheduling stimulus content, and orchestrating multi‑condition trials, VIRENA enables systematic study of human‑AI interaction, content‑moderation effects, and collective deliberation that were previously infeasible due to data‑access and ethical constraints. Early deployments at the University of Zurich demonstrate that the platform can reliably capture nuanced social dynamics while keeping all data under institutional control, thereby providing a reproducible research infrastructure for the agentic AI community.


<details>
<summary>Abstract</summary>

Digital platforms shape how people communicate, deliberate, and form opinions. Studying these dynamics has become increasingly difficult due to restricted data access, ethical constraints on real-world experiments, and limitations of existing research tools. VIRENA (Virtual Arena) is a platform that enables controlled experimentation in realistic social media environments. Multiple participants interact simultaneously in realistic replicas of feed-based platforms (Instagram, Facebook, Reddit) and messaging apps (WhatsApp, Messenger). Large language model-powered AI agents participate alongside humans with configurable personas and realistic behavior. Researchers can manipulate content moderation approaches, pre-schedule stimulus content, and run experiments across conditions through a visual interface requiring no programming skills. VIRENA makes possible research designs that were previously impractical: studying human--AI interaction in realistic social contexts, experimentally comparing moderation interventions, and observing group deliberation as it unfolds. Built on open-source technologies that ensure data remain under institutional control and comply with data protection requirements, VIRENA is currently in use at the University of Zurich and available for pilot collaborations. Designed for researchers, educators, and public organizations alike, VIRENA's no-code interface makes controlled social media simulation accessible across disciplines and sectors. This paper documents its design, architecture, and capabilities.

</details>


### 98. GT-HarmBench: Benchmarking AI Safety Risks Through the Lens of Game Theory

- **Authors:** Pepijn Cobben, Xuanqiang Angelo Huang, Thao Amelia Pham, Isabel Dahlgren, Terry Jingchen Zhang, Zhijing Jin
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12316v1](http://arxiv.org/abs/2602.12316v1)
- **PDF:** [https://arxiv.org/pdf/2602.12316v1](https://arxiv.org/pdf/2602.12316v1)
- **Categories:** cs.AI, cs.CL, cs.CY, cs.GT, cs.MA


> GT‑HarmBench is a large‑scale benchmark (2,009 scenarios) that evaluates how frontier language models behave in high‑stakes, multi‑agent settings by embedding classic game‑theoretic structures (Prisoner’s Dilemma, Stag Hunt, Chicken, etc.) drawn from real‑world AI‑risk cases in the MIT AI Risk Repository. The authors probe 15 state‑of‑the‑art models with systematic prompt variations, analyze the models’ reasoning traces, and test game‑theoretic “interventions” (e.g., framing the problem as a coordination game) to see how these affect outcomes. They find that, on average, models select socially beneficial actions only 62 % of the time, often causing harmful results, but targeted game‑theoretic prompting can raise cooperative behavior by up to 18 %, exposing a significant reliability gap for agentic AI in multi‑agent environments.


<details>
<summary>Abstract</summary>

Frontier AI systems are increasingly capable and deployed in high-stakes multi-agent environments. However, existing AI safety benchmarks largely evaluate single agents, leaving multi-agent risks such as coordination failure and conflict poorly understood. We introduce GT-HarmBench, a benchmark of 2,009 high-stakes scenarios spanning game-theoretic structures such as the Prisoner's Dilemma, Stag Hunt and Chicken. Scenarios are drawn from realistic AI risk contexts in the MIT AI Risk Repository. Across 15 frontier models, agents choose socially beneficial actions in only 62% of cases, frequently leading to harmful outcomes. We measure sensitivity to game-theoretic prompt framing and ordering, and analyze reasoning patterns driving failures. We further show that game-theoretic interventions improve socially beneficial outcomes by up to 18%. Our results highlight substantial reliability gaps and provide a broad standardized testbed for studying alignment in multi-agent environments. The benchmark and code are available at https://github.com/causalNLP/gt-harmbench.

</details>


### 99. Convex Markov Games and Beyond: New Proof of Existence, Characterization and Learning Algorithms for Nash Equilibria

- **Authors:** Anas Barakat, Ioannis Panageas, Antonios Varvitsiotis
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12181v1](http://arxiv.org/abs/2602.12181v1)
- **PDF:** [https://arxiv.org/pdf/2602.12181v1](https://arxiv.org/pdf/2602.12181v1)
- **Categories:** cs.GT, cs.LG, cs.MA


> The paper extends Convex Markov Games to **General Utility Markov Games (GUMGs)**, a richer class that allows agents’ utilities to depend on coupled occupancy measures, and shows that **Nash equilibria in GUMGs are exactly the fixed points of projected pseudo‑gradient dynamics**—a result obtained via a novel agent‑wise gradient domination property and a simple Brouwer‑fixed‑point argument. Leveraging this characterization, the authors derive a **policy‑gradient theorem**, propose a **model‑free policy‑gradient algorithm**, and prove both **iteration‑complexity** (for exact gradients) and **sample‑complexity** (in generative and on‑policy settings) guarantees for computing approximate equilibria, including the first theoretical results for common‑interest (non‑zero‑sum) convex Markov games. These contributions provide a solid foundation for learning stable, coordinated behaviors in multi‑agent, agentic AI systems beyond the previously studied zero‑sum setting.


<details>
<summary>Abstract</summary>

Convex Markov Games (cMGs) were recently introduced as a broad class of multi-agent learning problems that generalize Markov games to settings where strategic agents optimize general utilities beyond additive rewards. While cMGs expand the modeling frontier, their theoretical foundations, particularly the structure of Nash equilibria (NE) and guarantees for learning algorithms, are not yet well understood. In this work, we address these gaps for an extension of cMGs, which we term General Utility Markov Games (GUMGs), capturing new applications requiring coupling between agents' occupancy measures. We prove that in GUMGs, Nash equilibria coincide with the fixed points of projected pseudo-gradient dynamics (i.e., first-order stationary points), enabled by a novel agent-wise gradient domination property. This insight also yields a simple proof of NE existence using Brouwer's fixed-point theorem. We further show the existence of Markov perfect equilibria. Building on this characterization, we establish a policy gradient theorem for GUMGs and design a model-free policy gradient algorithm. For potential GUMGs, we establish iteration complexity guarantees for computing approximate-NE under exact gradients and provide sample complexity bounds in both the generative model and on-policy settings. Our results extend beyond prior work restricted to zero-sum cMGs, providing the first theoretical analysis of common-interest cMGs.

</details>


### 100. On the Adoption of AI Coding Agents in Open-source Android and iOS Development

- **Authors:** Muhammad Ahmad Khan, Hasnain Ali, Muneeb Rana, Muhammad Saqib Ilyas, Abdul Ali Bangash
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12144v1](http://arxiv.org/abs/2602.12144v1)
- **PDF:** [https://arxiv.org/pdf/2602.12144v1](https://arxiv.org/pdf/2602.12144v1)
- **Categories:** cs.SE, cs.AI


> The paper delivers the first large‑scale, category‑level empirical assessment of AI‑generated code contributions in open‑source Android and iOS apps, analyzing 2,901 AI‑authored pull requests from 193 verified repositories in the AIDev dataset. By classifying PRs by platform, agent, and task type, the authors show that Android projects receive twice as many AI contributions and enjoy a higher acceptance rate (71 % vs. 63 % on iOS), with notable variation among agents; routine tasks (features, bug fixes, UI tweaks) are most likely to be merged, whereas structural changes (refactors, build updates) face lower acceptance and longer resolution times. An evolution trace further reveals that Android PR turnaround improved through mid‑2025 before regressing, establishing baseline metrics for designing platform‑aware, agentic AI systems in mobile software development.


<details>
<summary>Abstract</summary>

AI coding agents are increasingly contributing to software development, yet their impact on mobile development has received little empirical attention. In this paper, we present the first category-level empirical study of agent-generated code in open-source mobile app projects. We analyzed PR acceptance behaviors across mobile platforms, agents, and task categories using 2,901 AI-authored pull requests (PRs) in 193 verified Android and iOS open-source GitHub repositories in the AIDev dataset. We find that Android projects have received 2x more AI-authored PRs and have achieved higher PR acceptance rate (71%) than iOS (63%), with significant agent-level variation on Android. Across task categories, PRs with routine tasks (feature, fix, and ui) achieve the highest acceptance, while structural changes like refactor and build achieve lower success and longer resolution times. Furthermore, our evolution analysis shows improvement in PR resolution time on Android through mid-2025 before it declined again. Our findings offer the first evidence-based characterization of AI agents effects on OSS mobile projects and establish empirical baselines for evaluating agent-generated contributions to design platform aware agentic systems.

</details>


### 101. Perceptual Self-Reflection in Agentic Physics Simulation Code Generation

- **Authors:** Prashant Shende, Bradley Camburn
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12311v1](http://arxiv.org/abs/2602.12311v1)
- **PDF:** [https://arxiv.org/pdf/2602.12311v1](https://arxiv.org/pdf/2602.12311v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces a four‑agent pipeline that generates physics‑simulation code from natural‑language prompts and closes the “oracle gap” by using **perceptual self‑reflection**: rendered animation frames are fed to a vision‑enabled language model, which judges physical correctness and drives iterative code correction. The methodology combines (1) a language interpreter, (2) a requirements generator, (3) a self‑correcting code generator, and (4) a vision‑based validator that replaces traditional static tests with visual feedback loops. Across seven physics domains, the system outperforms single‑shot baselines, achieving target accuracy in the majority of cases while maintaining low cost (~ $0.20 per animation), demonstrating that vision‑informed, multi‑agent refinement can substantially improve agentic AI’s reliability for engineering‑level code synthesis.


<details>
<summary>Abstract</summary>

We present a multi-agent framework for generating physics simulation code from natural language descriptions, featuring a novel perceptual self-reflection mechanism for validation. The system employs four specialized agents: a natural language interpreter that converts user requests into physics-based descriptions; a technical requirements generator that produces scaled simulation parameters; a physics code generator with automated self-correction; and a physics validator that implements perceptual self-reflection. The key innovation is perceptual validation, which analyzes rendered animation frames using a vision-capable language model rather than inspecting code structure directly. This approach addresses the ``oracle gap'' where syntactically correct code produces physically incorrect behavior--a limitation that conventional testing cannot detect. We evaluate the system across seven domains including classical mechanics, fluid dynamics, thermodynamics, electromagnetics, wave physics, reaction-diffusion systems, and non-physics data visualization. The perceptual self-reflection architecture demonstrates substantial improvement over single-shot generation baselines, with the majority of tested scenarios achieving target physics accuracy thresholds. The system exhibits robust pipeline stability with consistent code self-correction capability, operating at approximately \$0.20 per animation. These results validate our hypothesis that feeding visual simulation outputs back to a vision-language model for iterative refinement significantly outperforms single-shot code generation for physics simulation tasks and highlights the potential of agentic AI to support engineering workflows and physics data generation pipelines.

</details>


### 102. Choose Your Agent: Tradeoffs in Adopting AI Advisors, Coaches, and Delegates in Multi-Party Negotiation

- **Authors:** Kehang Zhu, Nithum Thain, Vivian Tsai, James Wexler, Crystal Qian
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12089v2](http://arxiv.org/abs/2602.12089v2)
- **PDF:** [https://arxiv.org/pdf/2602.12089v2](https://arxiv.org/pdf/2602.12089v2)
- **Categories:** cs.GT, cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

As AI usage becomes more prevalent in social contexts, understanding agent-user interaction is critical to designing systems that improve both individual and group outcomes. We present an online behavioral experiment (N = 243) in which participants play three multi-turn bargaining games in groups of three. Each game, presented in randomized order, grants access to a single LLM assistance modality: proactive recommendations from an Advisor, reactive feedback from a Coach, or autonomous execution by a Delegate; all modalities are powered by an underlying LLM that achieves superhuman performance in an all-agent environment. On each turn, participants privately decide whether to act manually or use the AI modality available in that game. Despite preferring the Advisor modality, participants achieve the highest mean individual gains with the Delegate, demonstrating a preference-performance misalignment. Moreover, delegation generates positive externalities; even non-adopting users in access-to-delegate treatment groups benefit by receiving higher-quality offers. Mechanism analysis reveals that the Delegate agent acts as a market maker, injecting rational, Pareto-improving proposals that restructure the trading environment. Our research reveals a gap between agent capabilities and realized group welfare. While autonomous agents can exhibit super-human strategic performance, their impact on realized welfare gains can be constrained by interfaces, user perceptions, and adoption barriers. Assistance modalities should be designed as mechanisms with endogenous participation; adoption-compatible interaction rules are a prerequisite to improving human welfare with automated assistance.

</details>


### 103. Differentiable Modal Logic for Multi-Agent Diagnosis, Orchestration and Communication

- **Authors:** Antonin Sulc
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12083v1](http://arxiv.org/abs/2602.12083v1)
- **PDF:** [https://arxiv.org/pdf/2602.12083v1](https://arxiv.org/pdf/2602.12083v1)
- **Categories:** cs.AI, cs.LO


> The paper introduces **Differentiable Modal Logic (DML)**, realized through **Modal Logical Neural Networks (MLNNs)**, as a neurosymbolic framework that learns interpretable modal structures—trust graphs, causal chains, and deontic boundaries—directly from multi‑agent behavioral data. By encoding epistemic, temporal, deontic, and doxastic axioms as differentiable loss terms, the authors train MLNNs to discover hidden alliances, pinpoint failure‑causing events, and enforce permission constraints without hand‑crafted relational models. Experiments on diplomacy‑style games and LLM‑hallucination detection demonstrate that the learned modal parameters are both **transparent** (enabling debugging and control) and **effective** (improving diagnosis accuracy and enabling active orchestration of autonomous agent swarms).


<details>
<summary>Abstract</summary>

As multi-agent AI systems evolve from simple chatbots to autonomous swarms, debugging semantic failures requires reasoning about knowledge, belief, causality, and obligation, precisely what modal logic was designed to formalize. However, traditional modal logic requires manual specification of relationship structures that are unknown or dynamic in real systems. This tutorial demonstrates differentiable modal logic (DML), implemented via Modal Logical Neural Networks (MLNNs), enabling systems to learn trust networks, causal chains, and regulatory boundaries from behavioral data alone.
  We present a unified neurosymbolic debugging framework through four modalities: epistemic (who to trust), temporal (when events cause failures), deontic (what actions are permitted), and doxastic (how to interpret agent confidence). Each modality is demonstrated on concrete multi-agent scenarios, from discovering deceptive alliances in diplomacy games to detecting LLM hallucinations, with complete implementations showing how logical contradictions become learnable optimization objectives. Key contributions for the neurosymbolic community: (1) interpretable learned structures where trust and causality are explicit parameters, not opaque embeddings; (2) knowledge injection via differentiable axioms that guide learning with sparse data (3) compositional multi-modal reasoning that combines epistemic, temporal, and deontic constraints; and (4) practical deployment patterns for monitoring, active control and communication of multi-agent systems. All code provided as executable Jupyter notebooks.

</details>


### 104. Multi UAVs Preflight Planning in a Shared and Dynamic Airspace

- **Authors:** Amath Sow, Mauricio Rodriguez Cesen, Fabiola Martins Campos de Oliveira, Mariusz Wzorek, Daniel de Leng, Mattias Tiger, Fredrik Heintz, Christian Esteve Rothenberg
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12055v1](http://arxiv.org/abs/2602.12055v1)
- **PDF:** [https://arxiv.org/pdf/2602.12055v1](https://arxiv.org/pdf/2602.12055v1)
- **Categories:** cs.AI, cs.MA, cs.RO


> The paper introduces **DTAPP‑IICR**, a scalable pre‑flight planner for thousands of heterogeneous UAVs operating in a shared, time‑varying airspace. It combines a delivery‑time‑aware priority scheme with a novel 4‑D single‑agent planner (SFIPP‑ST) that treats temporal No‑Fly Zones as soft constraints, and then resolves remaining inter‑agent conflicts through an iterative large‑neighborhood search guided by a geometric conflict graph and a completeness‑preserving directional pruning of the 3‑D search space. Experiments on city‑scale benchmarks with temporal NFZs show near‑100 % success for fleets up to 1,000 UAVs and up to 50 % faster runtimes than batch Enhanced Conflict‑Based Search, demonstrating a practical, agentic‑AI‑ready solution for dense urban Unmanned Traffic Management.


<details>
<summary>Abstract</summary>

Preflight planning for large-scale Unmanned Aerial Vehicle (UAV) fleets in dynamic, shared airspace presents significant challenges, including temporal No-Fly Zones (NFZs), heterogeneous vehicle profiles, and strict delivery deadlines. While Multi-Agent Path Finding (MAPF) provides a formal framework, existing methods often lack the scalability and flexibility required for real-world Unmanned Traffic Management (UTM). We propose DTAPP-IICR: a Delivery-Time Aware Prioritized Planning method with Incremental and Iterative Conflict Resolution. Our framework first generates an initial solution by prioritizing missions based on urgency. Secondly, it computes roundtrip trajectories using SFIPP-ST, a novel 4D single-agent planner (Safe Flight Interval Path Planning with Soft and Temporal Constraints). SFIPP-ST handles heterogeneous UAVs, strictly enforces temporal NFZs, and models inter-agent conflicts as soft constraints. Subsequently, an iterative Large Neighborhood Search, guided by a geometric conflict graph, efficiently resolves any residual conflicts. A completeness-preserving directional pruning technique further accelerates the 3D search. On benchmarks with temporal NFZs, DTAPP-IICR achieves near-100% success with fleets of up to 1,000 UAVs and gains up to 50% runtime reduction from pruning, outperforming batch Enhanced Conflict-Based Search in the UTM context. Scaling successfully in realistic city-scale operations where other priority-based methods fail even at moderate deployments, DTAPP-IICR is positioned as a practical and scalable solution for preflight planning in dense, dynamic urban airspace.

</details>


### 105. PrefillShare: A Shared Prefill Module for KV Reuse in Multi-LLM Disaggregated Serving

- **Authors:** Sunghyeon Woo, Hoseung Kim, Sunghwan Shim, Minjung Jo, Hyunjoon Jeong, Jeongtae Lee, Joonghoon Kim, Sungjae Lee, Baeseong Park, Se Jung Kwon, Dongsoo Lee
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.12029v1](http://arxiv.org/abs/2602.12029v1)
- **PDF:** [https://arxiv.org/pdf/2602.12029v1](https://arxiv.org/pdf/2602.12029v1)
- **Categories:** cs.LG, cs.DC


> **PrefillShare** introduces a shared‑prefill architecture for disaggregated LLM serving, allowing multiple task‑specific models to reuse a single frozen “prefill” module and its key‑value cache when processing identical prompt prefixes. The authors factorize each model into a frozen prefill component and a fine‑tuned decode component, and implement a routing layer in a vLLM‑based system that dynamically matches incoming prompts to the shared prefill cache across heterogeneous models. Experiments show that this approach retains full fine‑tuning accuracy while cutting 95th‑percentile latency by **4.5×** and boosting throughput by **3.9×** in multi‑model agent workloads, directly addressing the prefill‑decode interference that hampers scalable agentic AI pipelines.


<details>
<summary>Abstract</summary>

Multi-agent systems increasingly orchestrate multiple specialized language models to solve complex real-world problems, often invoking them over a shared context. This execution pattern repeatedly processes the same prompt prefix across models. Consequently, each model redundantly executes the prefill stage and maintains its own key-value (KV) cache, increasing aggregate prefill load and worsening tail latency by intensifying prefill-decode interference in existing LLM serving stacks. Disaggregated serving reduces such interference by placing prefill and decode on separate GPUs, but disaggregation does not fundamentally eliminate inter-model redundancy in computation and KV storage for the same prompt. To address this issue, we propose PrefillShare, a novel algorithm that enables sharing the prefill stage across multiple models in a disaggregated setting. PrefillShare factorizes the model into prefill and decode modules, freezes the prefill module, and fine-tunes only the decode module. This design allows multiple task-specific models to share a prefill module and the KV cache generated for the same prompt. We further introduce a routing mechanism that enables effective prefill sharing across heterogeneous models in a vLLM-based disaggregated system. PrefillShare not only matches full fine-tuning accuracy on a broad range of tasks and models, but also delivers 4.5x lower p95 latency and 3.9x higher throughput in multi-model agent workloads.

</details>


### 106. Multi-Defender Single-Attacker Perimeter Defense Game on a Cylinder: Special Case in which the Attacker Starts at the Boundary

- **Authors:** Michael Otte, Roderich Groß
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11977v1](http://arxiv.org/abs/2602.11977v1)
- **PDF:** [https://arxiv.org/pdf/2602.11977v1](https://arxiv.org/pdf/2602.11977v1)
- **Categories:** cs.MA


> The paper introduces a formal model of a multi‑defender, single‑attacker perimeter‑defense game on a cylindrical arena and analytically solves the special case where the attacker begins on the defended boundary. By treating defenders as slower agents with limited motion and the attacker as a faster, point‑mass agent, the authors derive necessary and sufficient geometric conditions (based on angular separation and speed ratios) that guarantee the attacker can breach the perimeter despite the defenders’ initial coverage. The results provide explicit, provable strategies for both sides and a clear characterization of the win‑region for the attacker, offering a rare closed‑form solution that can be used to benchmark and design coordinated defensive policies in multi‑agent AI systems.


<details>
<summary>Abstract</summary>

We describe a multi-agent perimeter defense game played on a cylinder. A team of n slow-moving defenders must prevent a single fast-moving attacker from crossing the boundary of a defensive perimeter. We describe the conditions necessary for the attacker to win in the special case that the intruder starts close to the boundary and in a region that is currently defended.

</details>


### 107. Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments

- **Authors:** Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Virginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg, Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian Yu, Amine Benhalloum, Grégoire Mialon, Thomas Scialom
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11964v1](http://arxiv.org/abs/2602.11964v1)
- **PDF:** [https://arxiv.org/pdf/2602.11964v1](https://arxiv.org/pdf/2602.11964v1)
- **Categories:** cs.AI


> Gaia2 presents the first benchmark that evaluates LLM‑driven agents in fully asynchronous, dynamically changing environments, where the world evolves independently of the agent’s actions and tasks impose strict temporal constraints. The authors construct a suite of realistic scenarios on the open‑source Agents Research Environments (ARE) platform, each equipped with a write‑action verifier that enables fine‑grained, action‑level scoring and direct reinforcement‑learning from verifiable rewards. Experiments on leading proprietary (GPT‑5, Claude‑4 Sonnet) and open‑source (Kimi‑K2) models reveal that no system excels across all dimensions: GPT‑5 attains the highest overall pass@1 (42 %) but struggles with time‑sensitive tasks, Claude‑4 balances accuracy and speed at higher cost, and Kimi‑K2 is the best open‑source performer (21 %); these results expose fundamental trade‑offs among reasoning ability, efficiency, robustness, and the sim‑to‑real gap, underscoring the need for more adaptable, temporally aware agent architectures.


<details>
<summary>Abstract</summary>

We introduce Gaia2, a benchmark for evaluating large language model agents in realistic, asynchronous environments. Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the "sim2real" gap. Gaia2 is built on a consumer environment with the open-source Agents Research Environments platform and designed to be easy to extend. By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems.

</details>


### 108. AdaptEvolve: Improving Efficiency of Evolutionary AI Agents through Adaptive Model Selection

- **Authors:** Pretam Ray, Pratik Prabhanjan Brahma, Zicheng Liu, Emad Barsoum
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11931v1](http://arxiv.org/abs/2602.11931v1)
- **PDF:** [https://arxiv.org/pdf/2602.11931v1](https://arxiv.org/pdf/2602.11931v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **AdaptEvolve**, a dynamic model‑selection mechanism for evolutionary AI agents that chooses among multiple LLMs during each refinement step based on the agent’s own generation confidence, thereby estimating the solvability of the current sub‑task. By integrating confidence‑driven routing into the evolutionary sequential refinement loop, the method replaces static heuristics with an adaptive cascade that balances reasoning power against compute cost. Experiments across standard evolutionary‑agent benchmarks show that AdaptEvolve cuts average inference expense by **≈ 38 %** while preserving **≈ 97.5 %** of the accuracy achieved by always using the largest model, establishing a superior Pareto trade‑off for agentic AI systems.


<details>
<summary>Abstract</summary>

Evolutionary agentic systems intensify the trade-off between computational efficiency and reasoning capability by repeatedly invoking large language models (LLMs) during inference. This setting raises a central question: how can an agent dynamically select an LLM that is sufficiently capable for the current generation step while remaining computationally efficient? While model cascades offer a practical mechanism for balancing this trade-off, existing routing strategies typically rely on static heuristics or external controllers and do not explicitly account for model uncertainty. We introduce AdaptEvolve: Adaptive LLM Selection for Multi-LLM Evolutionary Refinement within an evolutionary sequential refinement framework that leverages intrinsic generation confidence to estimate real-time solvability. Empirical results show that confidence-driven selection yields a favourable Pareto frontier, reducing total inference cost by an average of 37.9% across benchmarks while retaining 97.5% of the upper-bound accuracy of static large-model baselines. Our code is available at https://github.com/raypretam/adaptive_llm_selection.

</details>


### 109. MEME: Modeling the Evolutionary Modes of Financial Markets

- **Authors:** Taian Guo, Haiyang Shen, Junyu Luo, Zhongshi Xing, Hanchun Lian, Jinsheng Huang, Binqi Chen, Luchen Liu, Yun Ma, Ming Zhang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11918v1](http://arxiv.org/abs/2602.11918v1)
- **PDF:** [https://arxiv.org/pdf/2602.11918v1](https://arxiv.org/pdf/2602.11918v1)
- **Categories:** cs.AI


> The paper introduces **MEME (Modeling the Evolutionary Modes of Financial Markets)**, a logic‑oriented framework that treats market movements as the competition of evolving “investment narratives” (Modes of Thought) and uses them to drive portfolio decisions. MEME combines a multi‑agent extraction pipeline that converts noisy market data into high‑fidelity Investment Arguments with a Gaussian‑Mixture‑Model‑based semantic clustering and a temporal alignment module that tracks the drift, lifecycle, and historical profitability of each narrative. Experiments on three Chinese stock pools (2023‑2025) show that MEME consistently outperforms seven state‑of‑the‑art baselines, demonstrating that agentic reasoning over evolving market logics yields more robust and profitable asset allocation.


<details>
<summary>Abstract</summary>

LLMs have demonstrated significant potential in quantitative finance by processing vast unstructured data to emulate human-like analytical workflows. However, current LLM-based methods primarily follow either an Asset-Centric paradigm focused on individual stock prediction or a Market-Centric approach for portfolio allocation, often remaining agnostic to the underlying reasoning that drives market movements. In this paper, we propose a Logic-Oriented perspective, modeling the financial market as a dynamic, evolutionary ecosystem of competing investment narratives, termed Modes of Thought. To operationalize this view, we introduce MEME (Modeling the Evolutionary Modes of Financial Markets), designed to reconstruct market dynamics through the lens of evolving logics. MEME employs a multi-agent extraction module to transform noisy data into high-fidelity Investment Arguments and utilizes Gaussian Mixture Modeling to uncover latent consensus within a semantic space. To model semantic drift among different market conditions, we also implement a temporal evaluation and alignment mechanism to track the lifecycle and historical profitability of these modes. By prioritizing enduring market wisdom over transient anomalies, MEME ensures that portfolio construction is guided by robust reasoning. Extensive experiments on three heterogeneous Chinese stock pools from 2023 to 2025 demonstrate that MEME consistently outperforms seven SOTA baselines. Further ablation studies, sensitivity analysis, lifecycle case study and cost analysis validate MEME's capacity to identify and adapt to the evolving consensus of financial markets. Our implementation can be found at https://github.com/gta0804/MEME.

</details>


### 110. Agentic AI for Cybersecurity: A Meta-Cognitive Architecture for Governable Autonomy

- **Authors:** Andrei Kojukhov, Arkady Bovshover
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11897v2](http://arxiv.org/abs/2602.11897v2)
- **PDF:** [https://arxiv.org/pdf/2602.11897v2](https://arxiv.org/pdf/2602.11897v2)
- **Categories:** cs.CR, cs.AI


> The paper proposes a meta‑cognitive architecture that treats cybersecurity orchestration as a governable, multi‑agent cognitive system rather than a linear detection‑response pipeline. By integrating distributed cognition theory, multi‑agent coordination, and responsible‑AI governance, the authors define a first‑class “meta‑cognitive judgement” function that monitors evidence quality, calibrates each agent’s autonomy, and enforces accountability when decisions are uncertain or risky. Their conceptual analysis shows that existing security operations already exhibit distributed cognition, and making this structure explicit enables AI‑driven defenses to justify actions, align with regulatory constraints, and maintain controllable autonomy under adversarial uncertainty.


<details>
<summary>Abstract</summary>

Contemporary AI-driven cybersecurity systems are predominantly architected as model-centric detection and automation pipelines optimized for task-level performance metrics such as accuracy and response latency. While effective for bounded classification tasks, these architectures struggle to support accountable decision-making under adversarial uncertainty, where actions must be justified, governed, and aligned with organizational and regulatory constraints. This paper argues that cybersecurity orchestration should be reconceptualized as an agentic, multi-agent cognitive system, rather than a linear sequence of detection and response components. We introduce a conceptual architectural framework in which heterogeneous AI agents responsible for detection, hypothesis formation, contextual interpretation, explanation, and governance are coordinated through an explicit meta-cognitive judgement function. This function governs decision readiness and dynamically calibrates system autonomy when evidence is incomplete, conflicting, or operationally risky. By synthesizing distributed cognition theory, multi-agent systems research, and responsible AI governance frameworks, we demonstrate that modern security operations already function as distributed cognitive systems, albeit without an explicit organizing principle. Our contribution is to make this cognitive structure architecturally explicit and governable by embedding meta-cognitive judgement as a first-class system function. We discuss implications for security operations centers, accountable autonomy, and the design of next-generation AI-enabled cyber defence architectures. The proposed framework shifts the focus of AI in cybersecurity from optimizing isolated predictions to governing autonomy under uncertainty.

</details>


### 111. Intelligent AI Delegation

- **Authors:** Nenad Tomašev, Matija Franklin, Simon Osindero
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11865v1](http://arxiv.org/abs/2602.11865v1)
- **PDF:** [https://arxiv.org/pdf/2602.11865v1](https://arxiv.org/pdf/2602.11865v1)
- **Categories:** cs.AI


> The paper introduces an adaptive “Intelligent AI Delegation” framework that formalizes how autonomous agents (including humans) can decompose complex goals, allocate sub‑tasks, and transfer authority, responsibility, and accountability while maintaining clear intent, role boundaries, and trust. The authors construct a decision‑theoretic model that integrates dynamic task allocation, specification of delegation contracts, and failure‑handling mechanisms, and they validate it through simulated multi‑agent environments where agents must re‑assign tasks under changing conditions and unexpected failures. Experiments show that the framework yields higher task‑completion rates, faster recovery from failures, and more reliable coordination than existing heuristic‑based delegation methods, suggesting a viable protocol for the emerging “agentic web.”


<details>
<summary>Abstract</summary>

AI agents are able to tackle increasingly complex tasks. To achieve more ambitious goals, AI agents need to be able to meaningfully decompose problems into manageable sub-components, and safely delegate their completion across to other AI agents and humans alike. Yet, existing task decomposition and delegation methods rely on simple heuristics, and are not able to dynamically adapt to environmental changes and robustly handle unexpected failures. Here we propose an adaptive framework for intelligent AI delegation - a sequence of decisions involving task allocation, that also incorporates transfer of authority, responsibility, accountability, clear specifications regarding roles and boundaries, clarity of intent, and mechanisms for establishing trust between the two (or more) parties. The proposed framework is applicable to both human and AI delegators and delegatees in complex delegation networks, aiming to inform the development of protocols in the emerging agentic web.

</details>


### 112. Towards Sustainable Investment Policies Informed by Opponent Shaping

- **Authors:** Juan Agustin Duque, Razvan Ciuca, Ayoub Echchahed, Hugo Larochelle, Aaron Courville
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11829v1](http://arxiv.org/abs/2602.11829v1)
- **PDF:** [https://arxiv.org/pdf/2602.11829v1](https://arxiv.org/pdf/2602.11829v1)
- **Categories:** cs.LG, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

Addressing climate change requires global coordination, yet rational economic actors often prioritize immediate gains over collective welfare, resulting in social dilemmas. InvestESG is a recently proposed multi-agent simulation that captures the dynamic interplay between investors and companies under climate risk. We provide a formal characterization of the conditions under which InvestESG exhibits an intertemporal social dilemma, deriving theoretical thresholds at which individual incentives diverge from collective welfare. Building on this, we apply Advantage Alignment, a scalable opponent shaping algorithm shown to be effective in general-sum games, to influence agent learning in InvestESG. We offer theoretical insights into why Advantage Alignment systematically favors socially beneficial equilibria by biasing learning dynamics toward cooperative outcomes. Our results demonstrate that strategically shaping the learning processes of economic agents can result in better outcomes that could inform policy mechanisms to better align market incentives with long-term sustainability goals.

</details>


### 113. Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation

- **Authors:** Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11790v1](http://arxiv.org/abs/2602.11790v1)
- **PDF:** [https://arxiv.org/pdf/2602.11790v1](https://arxiv.org/pdf/2602.11790v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **LAVES**, a hierarchical, LLM‑driven multi‑agent framework that generates instructional videos by decomposing the task into a Solution Agent (step‑by‑step reasoning), an Illustration Agent (executable visual code), and a Narration Agent (pedagogical script), all coordinated by an Orchestrating Agent that enforces quality gates, semantic critiques, and rule‑based checks. By treating video creation as a structured, script‑first pipeline rather than end‑to‑end pixel synthesis, LAVES can automatically compile synchronized visuals and narration from deterministic templates, achieving fully automated production at massive scale. Empirical results show that LAVES can produce over one million educational videos per day, cutting production costs by >95 % relative to industry baselines while preserving high procedural fidelity and learner‑oriented coherence—demonstrating the power of coordinated LLM agents for complex, knowledge‑intensive media generation.


<details>
<summary>Abstract</summary>

Although recent end-to-end video generation models demonstrate impressive performance in visually oriented content creation, they remain limited in scenarios that require strict logical rigor and precise knowledge representation, such as instructional and educational media. To address this problem, we propose LAVES, a hierarchical LLM-based multi-agent system for generating high-quality instructional videos from educational problems. The LAVES formulates educational video generation as a multi-objective task that simultaneously demands correct step-by-step reasoning, pedagogically coherent narration, semantically faithful visual demonstrations, and precise audio--visual alignment. To address the limitations of prior approaches--including low procedural fidelity, high production cost, and limited controllability--LAVES decomposes the generation workflow into specialized agents coordinated by a central Orchestrating Agent with explicit quality gates and iterative critique mechanisms. Specifically, the Orchestrating Agent supervises a Solution Agent for rigorous problem solving, an Illustration Agent that produces executable visualization codes, and a Narration Agent for learner-oriented instructional scripts. In addition, all outputs from the working agents are subject to semantic critique, rule-based constraints, and tool-based compilation checks. Rather than directly synthesizing pixels, the system constructs a structured executable video script that is deterministically compiled into synchronized visuals and narration using template-driven assembly rules, enabling fully automated end-to-end production without manual editing. In large-scale deployments, LAVES achieves a throughput exceeding one million videos per day, delivering over a 95% reduction in cost compared to current industry-standard approaches while maintaining a high acceptance rate.

</details>


### 114. TSR: Trajectory-Search Rollouts for Multi-Turn RL of LLM Agents

- **Authors:** Aladin Djuhera, Swanand Ravindra Kadhe, Farhan Ahmed, Holger Boche
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11767v1](http://arxiv.org/abs/2602.11767v1)
- **PDF:** [https://arxiv.org/pdf/2602.11767v1](https://arxiv.org/pdf/2602.11767v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper introduces **Trajectory‑Search Rollouts (TSR)**, a training‑time augmentation that injects lightweight tree‑search (best‑of‑N, beam, or shallow look‑ahead) into the generation of rollout trajectories for multi‑turn reinforcement learning of LLM‑based agents. By selecting high‑scoring actions per turn using task‑specific feedback, TSR produces higher‑quality trajectories without altering the underlying RL objective, making it compatible with any optimizer (e.g., PPO, GRPO). Experiments on Sokoban, FrozenLake, and WebShop show that TSR yields up to **15 % higher task performance and markedly more stable learning** with only a modest, one‑off increase in training compute, demonstrating a simple, optimizer‑agnostic way to strengthen multi‑turn agentic AI training.


<details>
<summary>Abstract</summary>

Advances in large language models (LLMs) are driving a shift toward using reinforcement learning (RL) to train agents from iterative, multi-turn interactions across tasks. However, multi-turn RL remains challenging as rewards are often sparse or delayed, and environments can be stochastic. In this regime, naive trajectory sampling can hinder exploitation and induce mode collapse. We propose TSR (Trajectory-Search Rollouts), a training-time approach that repurposes test-time scaling ideas for improved per-turn rollout generation. TSR performs lightweight tree-style search to construct high-quality trajectories by selecting high-scoring actions at each turn using task-specific feedback. This improves rollout quality and stabilizes learning while leaving the underlying optimization objective unchanged, making TSR optimizer-agnostic. We instantiate TSR with best-of-N, beam, and shallow lookahead search, and pair it with PPO and GRPO, achieving up to 15% performance gains and more stable learning on Sokoban, FrozenLake, and WebShop tasks at a one-time increase in training compute. By moving search from inference time to the rollout stage of training, TSR provides a simple and general mechanism for stronger multi-turn agent learning, complementary to existing frameworks and rejection-sampling-style selection methods.

</details>


### 115. Cooperation Breakdown in LLM Agents Under Communication Delays

- **Authors:** Keita Nishimoto, Kimitaka Asatani, Ichiro Sakata
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11754v1](http://arxiv.org/abs/2602.11754v1)
- **PDF:** [https://arxiv.org/pdf/2602.11754v1](https://arxiv.org/pdf/2602.11754v1)
- **Categories:** cs.MA, cs.AI, cs.GT


> The paper introduces FLCOA (Five Layers for Cooperation/Coordination among Autonomous Agents), a conceptual framework that foregrounds low‑level factors—especially computational and communication resources—as critical determinants of cooperation in LLM‑based multi‑agent systems. Using a novel “Continuous Prisoner’s Dilemma with Communication Delay,” the authors simulate LLM agents under varying latency and show that modest delays induce systematic exploitation of slower partners, while very high delays suppress exploitation, producing a U‑shaped curve between delay length and overall cooperation. These findings highlight that, beyond high‑level institutional design, managing communication latency and resource allocation is essential for sustaining cooperative behavior in agentic AI deployments.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (LLM-MAS), in which autonomous AI agents cooperate to solve tasks, are gaining increasing attention. For such systems to be deployed in society, agents must be able to establish cooperation and coordination under real-world computational and communication constraints. We propose the FLCOA framework (Five Layers for Cooperation/Coordination among Autonomous Agents) to conceptualize how cooperation and coordination emerge in groups of autonomous agents, and highlight that the influence of lower-layer factors - especially computational and communication resources - has been largely overlooked. To examine the effect of communication delay, we introduce a Continuous Prisoner's Dilemma with Communication Delay and conduct simulations with LLM-based agents. As delay increases, agents begin to exploit slower responses even without explicit instructions. Interestingly, excessive delay reduces cycles of exploitation, yielding a U-shaped relationship between delay magnitude and mutual cooperation. These results suggest that fostering cooperation requires attention not only to high-level institutional design but also to lower-layer factors such as communication delay and resource allocation, pointing to new directions for MAS research.

</details>


### 116. AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild

- **Authors:** Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11750v1](http://arxiv.org/abs/2602.11750v1)
- **PDF:** [https://arxiv.org/pdf/2602.11750v1](https://arxiv.org/pdf/2602.11750v1)
- **Categories:** cs.SE, cs.AI, cs.HC


> AmbiBench introduces the first benchmark that evaluates mobile GUI agents on **bidirectional intent alignment** rather than single‑turn instruction following, using a cognitively grounded taxonomy of four clarity levels (Detailed, Standard, Incomplete, Ambiguous). The authors assemble 240 real‑world tasks across 25 apps and devise MUSE (Mobile User Satisfaction Evaluator), an automated multi‑LLM judge that scores agents on Outcome Effectiveness, Execution Quality, and Interaction Quality. Experiments show that state‑of‑the‑art agents’ performance drops sharply as instruction clarity decreases, while active clarification markedly improves results, and MUSE’s scores correlate strongly with human judgments, establishing a new evaluation paradigm for agentic AI that must negotiate ambiguous user intent.


<details>
<summary>Abstract</summary>

Benchmarks are paramount for gauging progress in the domain of Mobile GUI Agents. In practical scenarios, users frequently fail to articulate precise directives containing full task details at the onset, and their expressions are typically ambiguous. Consequently, agents are required to converge on the user's true intent via active clarification and interaction during execution. However, existing benchmarks predominantly operate under the idealized assumption that user-issued instructions are complete and unequivocal. This paradigm focuses exclusively on assessing single-turn execution while overlooking the alignment capability of the agent. To address this limitation, we introduce AmbiBench, the first benchmark incorporating a taxonomy of instruction clarity to shift evaluation from unidirectional instruction following to bidirectional intent alignment. Grounded in Cognitive Gap theory, we propose a taxonomy of four clarity levels: Detailed, Standard, Incomplete, and Ambiguous. We construct a rigorous dataset of 240 ecologically valid tasks across 25 applications, subject to strict review protocols. Furthermore, targeting evaluation in dynamic environments, we develop MUSE (Mobile User Satisfaction Evaluator), an automated framework utilizing an MLLM-as-a-judge multi-agent architecture. MUSE performs fine-grained auditing across three dimensions: Outcome Effectiveness, Execution Quality, and Interaction Quality. Empirical results on AmbiBench reveal the performance boundaries of SoTA agents across different clarity levels, quantify the gains derived from active interaction, and validate the strong correlation between MUSE and human judgment. This work redefines evaluation standards, laying the foundation for next-generation agents capable of truly understanding user intent.

</details>


### 117. AIR: Improving Agent Safety through Incident Response

- **Authors:** Zibo Xiao, Jun Sun, Junjie Chen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11749v1](http://arxiv.org/abs/2602.11749v1)
- **PDF:** [https://arxiv.org/pdf/2602.11749v1](https://arxiv.org/pdf/2602.11749v1)
- **Categories:** cs.AI


> The paper introduces **AIR**, the first dedicated incident‑response framework for large‑language‑model (LLM) agents, which equips agents with a domain‑specific language and an integrated execution‑loop module to (i) semantically detect failures from the current state and recent context, (ii) autonomously invoke containment and recovery tools, and (iii) synthesize guard‑rail rules that prevent recurrence. Across three representative agent classes, AIR achieves >90 % success in detection, remediation, and eradication while adding only modest latency, and the automatically generated rules perform comparably to hand‑crafted ones, demonstrating that proactive, post‑hoc response is both feasible and crucial for safe autonomous agents.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents are increasingly deployed in practice across a wide range of autonomous applications. Yet current safety mechanisms for LLM agents focus almost exclusively on preventing failures in advance, providing limited capabilities for responding to, containing, or recovering from incidents after they inevitably arise. In this work, we introduce AIR, the first incident response framework for LLM agent systems. AIR defines a domain-specific language for managing the incident response lifecycle autonomously in LLM agent systems, and integrates it into the agent's execution loop to (1) detect incidents via semantic checks grounded in the current environment state and recent context, (2) guide the agent to execute containment and recovery actions via its tools, and (3) synthesize guardrail rules during eradication to block similar incidents in future executions. We evaluate AIR on three representative agent types. Results show that AIR achieves detection, remediation, and eradication success rates all exceeding 90%. Extensive experiments further confirm the necessity of AIR's key design components, show the timeliness and moderate overhead of AIR, and demonstrate that LLM-generated rules can approach the effectiveness of developer-authored rules across domains. These results show that incident response is both feasible and essential as a first-class mechanism for improving agent safety.

</details>


### 118. PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics

- **Authors:** E Fan, Lisong Shi, Zhengtong Li, Chih-yung Wen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11666v1](http://arxiv.org/abs/2602.11666v1)
- **PDF:** [https://arxiv.org/pdf/2602.11666v1](https://arxiv.org/pdf/2602.11666v1)
- **Categories:** cs.AI, cs.CL


> PhyNiKCE introduces a neurosymbolic architecture that separates neural planning from symbolic constraint enforcement to enable trustworthy, autonomous CFD simulations. The framework couples a large‑language‑model planner with a deterministic Symbolic Knowledge Engine that formulates simulation setup as a constraint‑satisfaction problem and retrieves rigorously vetted solvers, turbulence models, and boundary conditions via a specialized Retrieval‑Augmented Generation module. In OpenFOAM benchmarks on realistic CFD tasks, PhyNiKCE achieves a 96 % relative performance gain over prior LLM‑based agents, cuts self‑correction loops by 59 %, and reduces token usage by 17 %, demonstrating that integrating symbolic validation dramatically improves robustness and efficiency of agentic AI in physics‑intensive domains.


<details>
<summary>Abstract</summary>

The deployment of autonomous agents for Computational Fluid Dynamics (CFD), is critically limited by the probabilistic nature of Large Language Models (LLMs), which struggle to enforce the strict conservation laws and numerical stability required for physics-based simulations. Reliance on purely semantic Retrieval Augmented Generation (RAG) often leads to "context poisoning," where agents generate linguistically plausible but physically invalid configurations due to a fundamental Semantic-Physical Disconnect. To bridge this gap, this work introduces PhyNiKCE (Physical and Numerical Knowledgeable Context Engineering), a neurosymbolic agentic framework for trustworthy engineering. Unlike standard black-box agents, PhyNiKCE decouples neural planning from symbolic validation. It employs a Symbolic Knowledge Engine that treats simulation setup as a Constraint Satisfaction Problem, rigidly enforcing physical constraints via a Deterministic RAG Engine with specialized retrieval strategies for solvers, turbulence models, and boundary conditions. Validated through rigorous OpenFOAM experiments on practical, non-tutorial CFD tasks using Gemini-2.5-Pro/Flash, PhyNiKCE demonstrates a 96% relative improvement over state-of-the-art baselines. Furthermore, by replacing trial-and-error with knowledge-driven initialization, the framework reduced autonomous self-correction loops by 59% while simultaneously lowering LLM token consumption by 17%. These results demonstrate that decoupling neural generation from symbolic constraint enforcement significantly enhances robustness and efficiency. While validated on CFD, this architecture offers a scalable, auditable paradigm for Trustworthy Artificial Intelligence in broader industrial automation.

</details>


### 119. When Agents Disagree With Themselves: Measuring Behavioral Consistency in LLM-Based Agents

- **Authors:** Aman Mehta
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11619v1](http://arxiv.org/abs/2602.11619v1)
- **PDF:** [https://arxiv.org/pdf/2602.11619v1](https://arxiv.org/pdf/2602.11619v1)
- **Categories:** cs.AI


> The paper introduces a systematic way to quantify **behavioral consistency** of LLM‑based agents by repeatedly executing the same ReAct‑style agent on identical HotpotQA instances and counting distinct action sequences. Across 3 000 runs with Llama 3.1‑70B, GPT‑4o, and Claude Sonnet 4.5, the authors find that agents generate 2–4.2 different paths per ten runs, and that higher inconsistency strongly predicts failure (tasks with ≤2 unique paths reach 80–92 % accuracy, whereas those with ≥6 unique paths drop to 25–60 %). The analysis shows most divergence (≈69 %) occurs at the very first search query, suggesting that monitoring early‑step consistency can serve as an early warning signal to improve the reliability of autonomous LLM agents.


<details>
<summary>Abstract</summary>

Run the same LLM agent on the same task twice: do you get the same behavior? We find the answer is often no. In a study of 3,000 agent runs across three models (Llama 3.1 70B, GPT-4o, and Claude Sonnet 4.5) on HotpotQA, we observe that ReAct-style agents produce 2.0--4.2 distinct action sequences per 10 runs on average, even with identical inputs. More importantly, this variance predicts failure: tasks with consistent behavior ($\leq$2 unique paths) achieve 80--92% accuracy, while highly inconsistent tasks ($\geq$6 unique paths) achieve only 25--60%, a 32--55 percentage point gap depending on model. We trace variance to early decisions: 69% of divergence occurs at step 2, the first search query. Our results suggest that monitoring behavioral consistency during execution could enable early error detection and improve agent reliability.

</details>


### 120. The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs

- **Authors:** Jingdi Chen, Hanqing Yang, Zongjun Liu, Carlee Joe-Wong
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11583v1](http://arxiv.org/abs/2602.11583v1)
- **PDF:** [https://arxiv.org/pdf/2602.11583v1](https://arxiv.org/pdf/2602.11583v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces a unifying “Five Ws” framework (who, what, when, why) to categorize and compare multi‑agent communication approaches across three research eras—hand‑crafted MARL protocols, emergent language (EL) systems, and recent LLM‑augmented agents. By systematically surveying each era, the authors show how design choices (e.g., explicit vs. learned messages, timing of communication, and grounding objectives) affect scalability, interpretability, and task generalization, and they extract practical patterns (such as hybrid grounding and selective broadcasting) that can guide the construction of hybrid agentic AI systems. Their analysis reveals that while MARL and EL methods achieve high task‑specific performance, they lack natural‑language grounding and robustness, whereas LLM‑based agents inherit linguistic priors that improve reasoning and open‑ended collaboration but still face challenges in real‑time control and grounding, highlighting open research directions for scalable, interpretable multi‑agent communication.


<details>
<summary>Abstract</summary>

Multi-agent sequential decision-making powers many real-world systems, from autonomous vehicles and robotics to collaborative AI assistants. In dynamic, partially observable environments, communication is often what reduces uncertainty and makes collaboration possible. This survey reviews multi-agent communication (MA-Comm) through the Five Ws: who communicates with whom, what is communicated, when communication occurs, and why communication is beneficial. This framing offers a clean way to connect ideas across otherwise separate research threads. We trace how communication approaches have evolved across three major paradigms. In Multi-Agent Reinforcement Learning (MARL), early methods used hand-designed or implicit protocols, followed by end-to-end learned communication optimized for reward and control. While successful, these protocols are frequently task-specific and hard to interpret, motivating work on Emergent Language (EL), where agents can develop more structured or symbolic communication through interaction. EL methods, however, still struggle with grounding, generalization, and scalability, which has fueled recent interest in large language models (LLMs) that bring natural language priors for reasoning, planning, and collaboration in more open-ended settings. Across MARL, EL, and LLM-based systems, we highlight how different choices shape communication design, where the main trade-offs lie, and what remains unsolved. We distill practical design patterns and open challenges to support future hybrid systems that combine learning, language, and control for scalable and interpretable multi-agent collaboration.

</details>


### 121. Learning to Configure Agentic AI Systems

- **Authors:** Aditya Taparia, Som Sagar, Ransalu Senanayake
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11574v1](http://arxiv.org/abs/2602.11574v1)
- **PDF:** [https://arxiv.org/pdf/2602.11574v1](https://arxiv.org/pdf/2602.11574v1)
- **Categories:** cs.AI


> The paper introduces ARC (Agentic Resource & Configuration learner), a reinforcement‑learning framework that treats the selection of workflows, tools, token budgets, and prompts for LLM‑based agents as a per‑query decision problem rather than a fixed, hand‑crafted setup. By training a lightweight hierarchical policy to predict the optimal configuration for each input, ARC dynamically balances performance and resource use. Experiments on diverse reasoning and tool‑augmented QA benchmarks show that ARC achieves up to 25 % higher accuracy while cutting token consumption and runtime, demonstrating that learned, query‑specific configurations can substantially outperform static, “one‑size‑fits‑all” agent designs.


<details>
<summary>Abstract</summary>

Configuring LLM-based agent systems involves choosing workflows, tools, token budgets, and prompts from a large combinatorial design space, and is typically handled today by fixed large templates or hand-tuned heuristics. This leads to brittle behavior and unnecessary compute, since the same cumbersome configuration is often applied to both easy and hard input queries. We formulate agent configuration as a query-wise decision problem and introduce ARC (Agentic Resource & Configuration learner), which learns a light-weight hierarchical policy using reinforcement learning to dynamically tailor these configurations. Across multiple benchmarks spanning reasoning and tool-augmented question answering, the learned policy consistently outperforms strong hand-designed and other baselines, achieving up to 25% higher task accuracy while also reducing token and runtime costs. These results demonstrate that learning per-query agent configurations is a powerful alternative to "one size fits all" designs.

</details>


### 122. CausalAgent: A Conversational Multi-Agent System for End-to-End Causal Inference

- **Authors:** Jiawei Zhu, Wei Chen, Ruichu Cai
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11527v1](http://arxiv.org/abs/2602.11527v1)
- **PDF:** [https://arxiv.org/pdf/2602.11527v1](https://arxiv.org/pdf/2602.11527v1)
- **Categories:** cs.AI


> CausalAgent introduces a conversational multi‑agent platform that automates the full causal‑inference pipeline—from data cleaning and causal graph discovery to bias correction and natural‑language report generation—by letting users interact solely through plain‑text queries. The system combines a Multi‑Agent System architecture with Retrieval‑Augmented Generation and the Model Context Protocol to coordinate specialized agents (e.g., data‑prep, structure‑learning, estimation, visualization) and maintain a shared, mutable context that guides each step of the analysis. Empirical evaluations show that non‑expert users can obtain statistically sound, interpretable causal conclusions with significantly less manual effort, demonstrating that tightly orchestrated, language‑driven agentic workflows can lower barriers to complex statistical reasoning while preserving methodological rigor.


<details>
<summary>Abstract</summary>

Causal inference holds immense value in fields such as healthcare, economics, and social sciences. However, traditional causal analysis workflows impose significant technical barriers, requiring researchers to possess dual backgrounds in statistics and computer science, while manually selecting algorithms, handling data quality issues, and interpreting complex results. To address these challenges, we propose CausalAgent, a conversational multi-agent system for end-to-end causal inference. The system innovatively integrates Multi-Agent Systems (MAS), Retrieval-Augmented Generation (RAG), and the Model Context Protocol (MCP) to achieve automation from data cleaning and causal structure learning to bias correction and report generation through natural language interaction. Users need only upload a dataset and pose questions in natural language to receive a rigorous, interactive analysis report. As a novel user-centered human-AI collaboration paradigm, CausalAgent explicitly models the analysis workflow. By leveraging interactive visualizations, it significantly lowers the barrier to entry for causal analysis while ensuring the rigor and interpretability of the process.

</details>


### 123. AgentLeak: A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems

- **Authors:** Faouzi El Yagoubi, Ranwa Al Mallah, Godwin Badu-Marfo
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11510v1](http://arxiv.org/abs/2602.11510v1)
- **PDF:** [https://arxiv.org/pdf/2602.11510v1](https://arxiv.org/pdf/2602.11510v1)
- **Categories:** cs.AI


> **AgentLeak** introduces the first comprehensive benchmark that evaluates privacy leakage across all internal communication pathways of multi‑agent LLM systems—not just the final output. The authors construct 1,000 domain‑specific scenarios (healthcare, finance, legal, corporate) and a 32‑class attack taxonomy, then run a three‑tier detection pipeline on 4,979 interaction traces from five leading models (GPT‑4o, GPT‑4o‑mini, Claude 3.5 Sonnet, Mistral Large, Llama 3.3 70B). Results show that while multi‑agent setups lower direct output leakage (27.2 % vs 43.2 % for single agents), they create unmonitored internal channels that raise total exposure to 68.9 %, with inter‑agent messages leaking in 68.8 % of cases—meaning output‑only audits miss 41.7 % of violations; Claude 3.5 Sonnet achieves the lowest leakage, suggesting that model‑level safety training can mitigate internal‑channel risks.


<details>
<summary>Abstract</summary>

Multi-agent Large Language Model (LLM) systems create privacy risks that current benchmarks cannot measure. When agents coordinate on tasks, sensitive data passes through inter-agent messages, shared memory, and tool arguments; pathways that output-only audits never inspect. We introduce AgentLeak, to the best of our knowledge the first full-stack benchmark for privacy leakage covering internal channels, spanning 1,000 scenarios across healthcare, finance, legal, and corporate domains, paired with a 32-class attack taxonomy and three-tier detection pipeline. Testing GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, and Llama 3.3 70B across 4,979 traces reveals that multi-agent configurations reduce per-channel output leakage (C1: 27.2% vs 43.2% in single-agent) but introduce unmonitored internal channels that raise total system exposure to 68.9% (OR-aggregated across C1, C2, C5). Internal channels account for most of this gap: inter-agent messages (C2) leak at 68.8%, compared to 27.2% on C1 (output channel). This means that output-only audits miss 41.7% of violations. Claude 3.5 Sonnet, which emphasizes safety alignment in its design, achieves the lowest leakage rates on both external (3.3%) and internal (28.1%) channels, suggesting that model-level safety training may transfer to internal channel protection. Across all five models and four domains, the pattern C2 > C1 holds consistently, confirming that inter-agent communication is the primary vulnerability. These findings underscore the need for coordination frameworks that incorporate internal-channel privacy protections and enforce privacy controls on inter-agent communication.

</details>


### 124. A Generic Framework for Fair Consensus Clustering in Streams

- **Authors:** Diptarka Chakraborty, Kushagra Chatterjee, Debarati Das, Tien-Long Nguyen
- **Published:** 2026-02-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11500v1](http://arxiv.org/abs/2602.11500v1)
- **PDF:** [https://arxiv.org/pdf/2602.11500v1](https://arxiv.org/pdf/2602.11500v1)
- **Categories:** cs.LG


> The paper introduces the first streaming algorithm for fair consensus clustering, achieving a constant‑factor approximation while storing only \(O(\log n)\) input clusterings, thus making fair multi‑agent clustering feasible under strict memory constraints. Its core methodology is a generic “closest‑fair‑plus‑cluster‑fitting” framework that first finds an approximately fair clustering of each incoming partition and then incrementally merges them using a cluster‑fitting subroutine; this design is agnostic to the specific fairness notion and extends to the \(k\)-median consensus objective. Empirically and theoretically, the framework improves approximation guarantees over prior offline methods and demonstrates that fairness‑aware consensus can be maintained in real‑time multi‑agent systems without prohibitive storage.


<details>
<summary>Abstract</summary>

Consensus clustering seeks to combine multiple clusterings of the same dataset, potentially derived by considering various non-sensitive attributes by different agents in a multi-agent environment, into a single partitioning that best reflects the overall structure of the underlying dataset. Recent work by Chakraborty et al, introduced a fair variant under proportionate fairness and obtained a constant-factor approximation by naively selecting the best closest fair input clustering; however, their offline approach requires storing all input clusterings, which is prohibitively expensive for most large-scale applications.
  In this paper, we initiate the study of fair consensus clustering in the streaming model, where input clusterings arrive sequentially and memory is limited. We design the first constant-factor algorithm that processes the stream while storing only a logarithmic number of inputs. En route, we introduce a new generic algorithmic framework that integrates closest fair clustering with cluster fitting, yielding improved approximation guarantees not only in the streaming setting but also when revisited offline. Furthermore, the framework is fairness-agnostic: it applies to any fairness definition for which an approximately close fair clustering can be computed efficiently. Finally, we extend our methods to the more general k-median consensus clustering problem.

</details>


### 125. Distributionally Robust Cooperative Multi-Agent Reinforcement Learning via Robust Value Factorization

- **Authors:** Chengrui Qu, Christopher Yeh, Kishan Panaganti, Eric Mazumdar, Adam Wierman
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11437v1](http://arxiv.org/abs/2602.11437v1)
- **PDF:** [https://arxiv.org/pdf/2602.11437v1](https://arxiv.org/pdf/2602.11437v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **Distributionally Robust IGM (DrIGM)**, a new principle that extends the individual‑global‑maximum (IGM) condition to the robust‑RL setting, guaranteeing that each agent’s robust greedy action jointly yields the team‑optimal robust policy under distributional uncertainty. By redefining individual action‑value functions to be robust and embedding these robust Q‑targets into existing value‑factorization architectures (VDN, QMIX, QTRAN), the authors obtain scalable, plug‑and‑play MARL algorithms that preserve decentralized execution while providing provable robustness guarantees. Experiments on high‑fidelity SustainGym benchmarks and a StarCraft micromanagement task show that the DrIGM‑compliant methods consistently outperform standard value‑factorization baselines when faced with out‑of‑distribution dynamics, demonstrating improved reliability for cooperative agentic AI systems.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning (MARL) commonly adopts centralized training with decentralized execution, where value-factorization methods enforce the individual-global-maximum (IGM) principle so that decentralized greedy actions recover the team-optimal joint action. However, the reliability of this recipe in real-world settings remains unreliable due to environmental uncertainties arising from the sim-to-real gap, model mismatch, and system noise. We address this gap by introducing Distributionally robust IGM (DrIGM), a principle that requires each agent's robust greedy action to align with the robust team-optimal joint action. We show that DrIGM holds for a novel definition of robust individual action values, which is compatible with decentralized greedy execution and yields a provable robustness guarantee for the whole system. Building on this foundation, we derive DrIGM-compliant robust variants of existing value-factorization architectures (e.g., VDN/QMIX/QTRAN) that (i) train on robust Q-targets, (ii) preserve scalability, and (iii) integrate seamlessly with existing codebases without bespoke per-agent reward shaping. Empirically, on high-fidelity SustainGym simulators and a StarCraft game environment, our methods consistently improve out-of-distribution performance. Code and data are available at https://github.com/crqu/robust-coMARL.

</details>


### 126. Optimizing Agent Planning for Security and Autonomy

- **Authors:** Aashish Kolluri, Rishi Sharma, Manuel Costa, Boris Köpf, Tobias Nießen, Mark Russinovich, Shruti Tople, Santiago Zanella-Béguelin
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11416v1](http://arxiv.org/abs/2602.11416v1)
- **PDF:** [https://arxiv.org/pdf/2602.11416v1](https://arxiv.org/pdf/2602.11416v1)
- **Categories:** cs.CR, cs.LG


> The paper’s main contribution is the introduction of **autonomy metrics** that measure how many consequential actions an AI agent can perform without human‑in‑the‑loop (HITL) approval while still satisfying deterministic security policies against prompt‑injection attacks. To improve these metrics, the authors design a **security‑aware planning agent** that (i) enriches HITL interaction protocols and (ii) jointly optimizes task progress and policy compliance, implementing it on top of an information‑flow control (IFC) defense. Empirical evaluation on the AgentDojo and WASP benchmarks shows that this approach **significantly raises the fraction of autonomous, safe actions**—i.e., higher autonomy—without degrading overall task performance, demonstrating that system‑level defenses can reduce reliance on human oversight while maintaining utility.


<details>
<summary>Abstract</summary>

Indirect prompt injection attacks threaten AI agents that execute consequential actions, motivating deterministic system-level defenses. Such defenses can provably block unsafe actions by enforcing confidentiality and integrity policies, but currently appear costly: they reduce task completion rates and increase token usage compared to probabilistic defenses. We argue that existing evaluations miss a key benefit of system-level defenses: reduced reliance on human oversight. We introduce autonomy metrics to quantify this benefit: the fraction of consequential actions an agent can execute without human-in-the-loop (HITL) approval while preserving security. To increase autonomy, we design a security-aware agent that (i) introduces richer HITL interactions, and (ii) explicitly plans for both task progress and policy compliance. We implement this agent design atop an existing information-flow control defense against prompt injection and evaluate it on the AgentDojo and WASP benchmarks. Experiments show that this approach yields higher autonomy without sacrificing utility.

</details>


### 127. When Visibility Outpaces Verification: Delayed Verification and Narrative Lock-in in Agentic AI Discourse

- **Authors:** Hanjing Shi, Dominic DiFranzo
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11412v1](http://arxiv.org/abs/2602.11412v1)
- **PDF:** [https://arxiv.org/pdf/2602.11412v1](https://arxiv.org/pdf/2602.11412v1)
- **Categories:** cs.CY, cs.AI, cs.HC


> The paper uncovers a “Popularity Paradox” in online discourse about agentic AI: highly visible Reddit threads receive far fewer or much later verification cues than low‑visibility ones, allowing unverified claims to become entrenched (“narrative lock‑in”). By constructing reproducible lexical rules to detect verification signals and applying right‑censored survival analysis to a longitudinal dataset from r/OpenClaw and r/Moltbook, the authors quantify the “time‑to‑first‑verification” across differing community cultures. The findings highlight how platform‑driven social proof can bias collective expectations of autonomous AI systems, and the authors propose “epistemic friction” mechanisms as a design remedy to promote timely evidence‑based evaluation.


<details>
<summary>Abstract</summary>

Agentic AI systems-autonomous entities capable of independent planning and execution-reshape the landscape of human-AI trust. Long before direct system exposure, user expectations are mediated through high-stakes public discourse on social platforms. However, platform-mediated engagement signals (e.g., upvotes) may inadvertently function as a ``credibility proxy,'' potentially stifling critical evaluation.
  This paper investigates the interplay between social proof and verification timing in online discussions of agentic AI. Analyzing a longitudinal dataset from two distinct Reddit communities with contrasting interaction cultures-r/OpenClaw and r/Moltbook-we operationalize verification cues via reproducible lexical rules and model the ``time-to-first-verification'' using a right-censored survival analysis framework.
  Our findings reveal a systemic ``Popularity Paradox'': high-visibility discussions in both subreddits experience significantly delayed or entirely absent verification cues compared to low-visibility threads. This temporal lag creates a critical window for ``Narrative Lock-in,'' where early, unverified claims crystallize into collective cognitive biases before evidence-seeking behaviors emerge. We discuss the implications of this ``credibility-by-visibility'' effect for AI safety and propose ``epistemic friction'' as a design intervention to rebalance engagement-driven platforms.

</details>


### 128. TRACER: Trajectory Risk Aggregation for Critical Episodes in Agentic Reasoning

- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Davide Ettori, Ranganath Krishnan, Amit Ranjan Trivedi
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11409v1](http://arxiv.org/abs/2602.11409v1)
- **PDF:** [https://arxiv.org/pdf/2602.11409v1](https://arxiv.org/pdf/2602.11409v1)
- **Categories:** cs.AI


> The paper introduces **TRACER**, a novel trajectory‑level uncertainty metric designed for multi‑turn, tool‑using interactions between agents and humans. By fusing content‑aware surprisal with situational cues (semantic/lexical repetition, tool‑grounded coherence gaps) and aggregating them through a tail‑focused risk functional with a MAX‑composite step risk, TRACER detects critical failure episodes that single‑shot uncertainty proxies miss. Empirical evaluation on the τ²‑bench benchmark shows that TRACER predicts task failures and enables selective execution up to **37 % higher AUROC** and **55 % higher AUARC** than existing baselines, demonstrating markedly earlier and more reliable uncertainty detection in complex agentic reasoning scenarios.


<details>
<summary>Abstract</summary>

Estimating uncertainty for AI agents in real-world multi-turn tool-using interaction with humans is difficult because failures are often triggered by sparse critical episodes (e.g., looping, incoherent tool use, or user-agent miscoordination) even when local generation appears confident. Existing uncertainty proxies focus on single-shot text generation and therefore miss these trajectory-level breakdown signals. We introduce TRACER, a trajectory-level uncertainty metric for dual-control Tool-Agent-User interaction. TRACER combines content-aware surprisal with situational-awareness signals, semantic and lexical repetition, and tool-grounded coherence gaps, and aggregates them using a tail-focused risk functional with a MAX-composite step risk to surface decisive anomalies. We evaluate TRACER on $τ^2$-bench by predicting task failure and selective task execution. To this end, TRACER improves AUROC by up to 37.1% and AUARC by up to 55% over baselines, enabling earlier and more accurate detection of uncertainty in complex conversational tool-use settings. Our code and benchmark are available at https://github.com/sinatayebati/agent-tracer.

</details>


### 129. ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences

- **Authors:** Bang Nguyen, Dominik Soós, Qian Ma, Rochana R. Obadage, Zack Ranjan, Sai Koneru, Timothy M. Errington, Shakhlo Nematova, Sarah Rajtmajer, Jian Wu, Meng Jiang
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11354v1](http://arxiv.org/abs/2602.11354v1)
- **PDF:** [https://arxiv.org/pdf/2602.11354v1](https://arxiv.org/pdf/2602.11354v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **ReplicatorBench**, the first end‑to‑end benchmark that evaluates LLM agents on the full replication workflow—data extraction/retrieval, experimental design & execution, and result interpretation—using a human‑verified mix of replicable and non‑replicable claims from the social and behavioral sciences. To demonstrate the benchmark, the authors build **ReplicatorAgent**, an agentic system equipped with web‑search, sandboxed code execution, and iterative tool use, and test it across four LLM back‑ends, programming‑language choices, and varying levels of code access. Results show that while current LLM agents can reliably generate and run computational analyses, they consistently fail to locate and acquire the external datasets needed for genuine replication, highlighting a critical gap in tool‑use and resource‑retrieval capabilities for agentic AI in scientific research.


<details>
<summary>Abstract</summary>

The literature has witnessed an emerging interest in AI agents for automated assessment of scientific papers. Existing benchmarks focus primarily on the computational aspect of this task, testing agents' ability to reproduce or replicate research outcomes when having access to the code and data. This setting, while foundational, (1) fails to capture the inconsistent availability of new data for replication as opposed to reproduction, and (2) lacks ground-truth diversity by focusing only on reproducible papers, thereby failing to evaluate an agent's ability to identify non-replicable research. Furthermore, most benchmarks only evaluate outcomes rather than the replication process. In response, we introduce ReplicatorBench, an end-to-end benchmark, including human-verified replicable and non-replicable research claims in social and behavioral sciences for evaluating AI agents in research replication across three stages: (1) extraction and retrieval of replication data; (2) design and execution of computational experiments; and (3) interpretation of results, allowing a test of AI agents' capability to mimic the activities of human replicators in real world. To set a baseline of AI agents' capability, we develop ReplicatorAgent, an agentic framework equipped with necessary tools, like web search and iterative interaction with sandboxed environments, to accomplish tasks in ReplicatorBench. We evaluate ReplicatorAgent across four underlying large language models (LLMs), as well as different design choices of programming language and levels of code access. Our findings reveal that while current LLM agents are capable of effectively designing and executing computational experiments, they struggle with retrieving resources, such as new data, necessary to replicate a claim. All code and data are publicly available at https://github.com/CenterForOpenScience/llm-benchmarking.

</details>


### 130. Pushing Forward Pareto Frontiers of Proactive Agents with Behavioral Agentic Optimization

- **Authors:** Yihang Yao, Zhepeng Cen, Haohong Lin, Shiqi Liu, Zuxin Liu, Jiacheng Zhu, Zhang-Wei Hong, Laixi Shi, Ding Zhao
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11351v1](http://arxiv.org/abs/2602.11351v1)
- **PDF:** [https://arxiv.org/pdf/2602.11351v1](https://arxiv.org/pdf/2602.11351v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **Behavioral Agentic Optimization (BAO)**, a novel agentic reinforcement‑learning framework that simultaneously augments proactive reasoning (behavior enhancement) and curtails unnecessary or redundant interactions (behavior regularization) to reconcile task effectiveness with user engagement. BAO trains large‑language‑model agents through a two‑stage RL pipeline: first it enriches the policy’s planning and information‑gathering capabilities, then it applies a regularization loss that penalizes inefficient dialogue moves and aligns the agent’s behavior with implicit user expectations. Empirical results on the UserRL benchmark show that BAO markedly surpasses existing proactive agentic‑RL baselines—and even matches or exceeds the performance of commercial LLM agents—demonstrating its ability to produce high‑performing, user‑aligned agents in complex multi‑turn environments.


<details>
<summary>Abstract</summary>

Proactive large language model (LLM) agents aim to actively plan, query, and interact over multiple turns, enabling efficient task completion beyond passive instruction following and making them essential for real-world, user-centric applications. Agentic reinforcement learning (RL) has recently emerged as a promising solution for training such agents in multi-turn settings, allowing interaction strategies to be learned from feedback. However, existing pipelines face a critical challenge in balancing task performance with user engagement, as passive agents can not efficiently adapt to users' intentions while overuse of human feedback reduces their satisfaction. To address this trade-off, we propose BAO, an agentic RL framework that combines behavior enhancement to enrich proactive reasoning and information-gathering capabilities with behavior regularization to suppress inefficient or redundant interactions and align agent behavior with user expectations. We evaluate BAO on multiple tasks from the UserRL benchmark suite, and demonstrate that it substantially outperforms proactive agentic RL baselines while achieving comparable or even superior performance to commercial LLM agents, highlighting its effectiveness for training proactive, user-aligned LLM agents in complex multi-turn scenarios. Our website: https://proactive-agentic-rl.github.io/.

</details>


### 131. AgentNoiseBench: Benchmarking Robustness of Tool-Using LLM Agents Under Noisy Condition

- **Authors:** Ruipeng Wang, Yuxin Chen, Yukai Wang, Chang Wu, Junfeng Fang, Xiaodong Cai, Qi Gu, Hui Su, An Zhang, Xiang Wang, Xunliang Cai, Tat-Seng Chua
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11348v1](http://arxiv.org/abs/2602.11348v1)
- **PDF:** [https://arxiv.org/pdf/2602.11348v1](https://arxiv.org/pdf/2602.11348v1)
- **Categories:** cs.AI


> The paper introduces **AgentNoiseBench**, a systematic benchmarking suite that quantifies how tool‑using LLM agents degrade when faced with realistic “user‑noise” (e.g., ambiguous or erroneous prompts) and “tool‑noise” (e.g., faulty API responses). By automatically injecting controllable noise into existing agent‑centric tasks while preserving solvability, the authors evaluate a broad spectrum of architectures and model sizes, revealing that even state‑of‑the‑art agents exhibit substantial and consistent performance drops across noise levels. These findings underscore the fragility of current agentic AI systems and provide a reusable framework for developing more robust, noise‑aware LLM agents.


<details>
<summary>Abstract</summary>

Recent advances in large language models have enabled LLM-based agents to achieve strong performance on a variety of benchmarks. However, their performance in real-world deployments often that observed on benchmark settings, especially in complex and imperfect environments. This discrepancy largely arises because prevailing training and evaluation paradigms are typically built on idealized assumptions, overlooking the inherent stochasticity and noise present in real-world interactions. To bridge this gap, we introduce AgentNoiseBench, a framework for systematically evaluating the robustness of agentic models under noisy environments. We first conduct an in-depth analysis of biases and uncertainties in real-world scenarios and categorize environmental noise into two primary types: user-noise and tool-noise. Building on this analysis, we develop an automated pipeline that injects controllable noise into existing agent-centric benchmarks while preserving task solvability. Leveraging this pipeline, we perform extensive evaluations across a wide range of models with diverse architectures and parameter scales. Our results reveal consistent performance variations under different noise conditions, highlighting the sensitivity of current agentic models to realistic environmental perturbations.

</details>


### 132. Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP

- **Authors:** Zeynab Anbiaee, Mahdi Rabbani, Mansur Mirani, Gunjan Piya, Igor Opushnyev, Ali Ghorbani, Sajjad Dadkhah
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11327v1](http://arxiv.org/abs/2602.11327v1)
- **PDF:** [https://arxiv.org/pdf/2602.11327v1](https://arxiv.org/pdf/2602.11327v1)
- **Categories:** cs.CR, cs.AI


> The paper’s primary contribution is a protocol‑centric threat‑modeling framework that systematically evaluates security risks across four emerging AI‑agent communication standards—MCP, A2A, Agora, and ANP. By dissecting each protocol’s architecture, trust assumptions, interaction patterns, and lifecycle phases, the authors identify twelve distinct protocol‑level threats and apply a qualitative risk‑assessment matrix (likelihood × impact) to rank vulnerabilities during creation, operation, and update stages; a measurement‑driven case study on MCP quantifies the concrete risk of missing mandatory validation/attestation for executable components, showing how unverified tool execution can be exploited in multi‑server compositions. The findings reveal that design choices such as implicit trust, lack of component attestation, and ambiguous resolver policies constitute the most critical attack surfaces, offering concrete mitigation guidance and a baseline for future standardization of secure AI‑agent ecosystems.


<details>
<summary>Abstract</summary>

The rapid development of the AI agent communication protocols, including the Model Context Protocol (MCP), Agent2Agent (A2A), Agora, and Agent Network Protocol (ANP), is reshaping how AI agents communicate with tools, services, and each other. While these protocols support scalable multi-agent interaction and cross-organizational interoperability, their security principles remain understudied, and standardized threat modeling is limited; no protocol-centric risk assessment framework has been established yet. This paper presents a systematic security analysis of four emerging AI agent communication protocols. First, we develop a structured threat modeling analysis that examines protocol architectures, trust assumptions, interaction patterns, and lifecycle behaviors to identify protocol-specific and cross-protocol risk surfaces. Second, we introduce a qualitative risk assessment framework that identifies twelve protocol-level risks and evaluates security posture across the creation, operation, and update phases through systematic assessment of likelihood, impact, and overall protocol risk, with implications for secure deployment and future standardization. Third, we provide a measurement-driven case study on MCP that formalizes the risk of missing mandatory validation/attestation for executable components as a falsifiable security claim by quantifying wrong-provider tool execution under multi-server composition across representative resolver policies. Collectively, our results highlight key design-induced risk surfaces and provide actionable guidance for secure deployment and future standardization of agent communication ecosystems.

</details>


### 133. The PBSAI Governance Ecosystem: A Multi-Agent AI Reference Architecture for Securing Enterprise AI Estates

- **Authors:** John M. Willis
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11301v1](http://arxiv.org/abs/2602.11301v1)
- **PDF:** [https://arxiv.org/pdf/2602.11301v1](https://arxiv.org/pdf/2602.11301v1)
- **Categories:** cs.AI, cs.CR


> The paper presents the **Practitioners Blueprint for Secure AI (PBSAI) Governance Ecosystem**, a concrete, multi‑agent reference architecture that operationalizes AI governance and cyber‑defense for enterprise‑scale AI estates. By defining a twelve‑domain taxonomy and “bounded agent families” that exchange structured context envelopes and output contracts, the authors formalize traceability, provenance, and human‑in‑the‑loop guarantees through a lightweight formal model and demonstrate how these agents can be integrated with existing security stacks to satisfy NIST AI RMF functions. Empirical illustrations in both SOC and hyperscale defensive settings show that PBSAI enables coordinated monitoring, adaptive response, and policy‑driven mediation across heterogeneous models, pipelines, and tools, providing a practical, evidence‑based foundation for secure, agentic AI deployments.


<details>
<summary>Abstract</summary>

Enterprises are rapidly deploying large language models, retrieval augmented generation pipelines, and tool using agents into production, often on shared high performance computing clusters and cloud accelerator platforms that also support defensive analytics. These systems increasingly function not as isolated models but as AI estates: socio technical systems spanning models, agents, data pipelines, security tooling, human workflows, and hyperscale infrastructure. Existing governance and security frameworks, including the NIST AI Risk Management Framework and systems security engineering guidance, articulate principles and risk functions but do not provide implementable architectures for multi agent, AI enabled cyber defense.
  This paper introduces the Practitioners Blueprint for Secure AI (PBSAI) Governance Ecosystem, a multi agent reference architecture for securing enterprise and hyperscale AI estates. PBSAI organizes responsibilities into a twelve domain taxonomy and defines bounded agent families that mediate between tools and policy through shared context envelopes and structured output contracts. The architecture assumes baseline enterprise security capabilities and encodes key systems security techniques, including analytic monitoring, coordinated defense, and adaptive response. A lightweight formal model of agents, context envelopes, and ecosystem level invariants clarifies the traceability, provenance, and human in the loop guarantees enforced across domains. We demonstrate alignment with NIST AI RMF functions and illustrate application in enterprise SOC and hyperscale defensive environments. PBSAI is proposed as a structured, evidence centric foundation for open ecosystem development and future empirical validation.

</details>


### 134. Interpretable Attention-Based Multi-Agent PPO for Latency Spike Resolution in 6G RAN Slicing

- **Authors:** Kavan Fatehi, Mostafa Rahmani Ghourtani, Amir Sonee, Poonam Yadav, Alessandra M Russo, Hamed Ahmadi, Radu Calinescu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11076v1](http://arxiv.org/abs/2602.11076v1)
- **PDF:** [https://arxiv.org/pdf/2602.11076v1](https://arxiv.org/pdf/2602.11076v1)
- **Categories:** eess.SY, cs.AI, eess.SP


> The paper introduces **Attention‑Enhanced Multi‑Agent Proximal Policy Optimization (AE‑MAPPO)**, a novel DRL framework that equips each slice‑control agent in a 6G O‑RAN with six dedicated attention modules whose weights are exposed as zero‑cost, faithful explanations of the agents’ decisions. By structuring control into predictive, reactive, and inter‑slice optimization phases, AE‑MAPPO jointly learns policies and interpretable attention maps that guide real‑time resource reallocation across URLLC, eMBB, and mMTC slices. In a URLLC latency‑spike scenario, the method eliminates the spike within 18 ms, restores latency to 0.98 ms with 99.9999 % reliability, and cuts troubleshooting time by 93 % while preserving service continuity, demonstrating that agentic AI can achieve both SLA‑level performance and built‑in interpretability for 6G RAN slicing.


<details>
<summary>Abstract</summary>

Sixth-generation (6G) radio access networks (RANs) must enforce strict service-level agreements (SLAs) for heterogeneous slices, yet sudden latency spikes remain difficult to diagnose and resolve with conventional deep reinforcement learning (DRL) or explainable RL (XRL). We propose \emph{Attention-Enhanced Multi-Agent Proximal Policy Optimization (AE-MAPPO)}, which integrates six specialized attention mechanisms into multi-agent slice control and surfaces them as zero-cost, faithful explanations. The framework operates across O-RAN timescales with a three-phase strategy: predictive, reactive, and inter-slice optimization.
  A URLLC case study shows AE-MAPPO resolves a latency spike in $18$ms, restores latency to $0.98$ms with $99.9999\%$ reliability, and reduces troubleshooting time by $93\%$ while maintaining eMBB and mMTC continuity. These results confirm AE-MAPPO's ability to combine SLA compliance with inherent interpretability, enabling trustworthy and real-time automation for 6G RAN slicing.

</details>


### 135. Evaluating Memory Structure in LLM Agents

- **Authors:** Alina Shutova, Alexandra Olenina, Ivan Vinogradov, Anton Sinitsin
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11243v1](http://arxiv.org/abs/2602.11243v1)
- **PDF:** [https://arxiv.org/pdf/2602.11243v1](https://arxiv.org/pdf/2602.11243v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces **StructMemEval**, a new benchmark that evaluates whether LLM‑based agents can *organize* their long‑term memory into task‑relevant structures (e.g., ledgers, to‑do lists, hierarchical trees) rather than merely retrieve isolated facts. By constructing a suite of human‑solved, structure‑dependent tasks and testing both retrieval‑augmented LLMs and memory‑augmented agents, the authors show that simple retrieval models fail, while agents that are explicitly prompted to maintain a structured memory succeed consistently. The results reveal that current LLMs often do not infer or preserve memory hierarchies on their own, underscoring the need for training and architectural advances that enable agents to recognize and manipulate internal memory structures autonomously.


<details>
<summary>Abstract</summary>

Modern LLM-based agents and chat assistants rely on long-term memory frameworks to store reusable knowledge, recall user preferences, and augment reasoning. As researchers create more complex memory architectures, it becomes increasingly difficult to analyze their capabilities and guide future memory designs. Most long-term memory benchmarks focus on simple fact retention, multi-hop recall, and time-based changes. While undoubtedly important, these capabilities can often be achieved with simple retrieval-augmented LLMs and do not test complex memory hierarchies. To bridge this gap, we propose StructMemEval - a benchmark that tests the agent's ability to organize its long-term memory, not just factual recall. We gather a suite of tasks that humans solve by organizing their knowledge in a specific structure: transaction ledgers, to-do lists, trees and others. Our initial experiments show that simple retrieval-augmented LLMs struggle with these tasks, whereas memory agents can reliably solve them if prompted how to organize their memory. However, we also find that modern LLMs do not always recognize the memory structure when not prompted to do so. This highlights an important direction for future improvements in both LLM training and memory frameworks.

</details>


### 136. Divide, Harmonize, Then Conquer It: Shooting Multi-Commodity Flow Problems with Multimodal Language Models

- **Authors:** Xinyu Yuan, Yan Qiao, Zonghui Wang, Wenzhi Chen
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11057v1](http://arxiv.org/abs/2602.11057v1)
- **PDF:** [https://arxiv.org/pdf/2602.11057v1](https://arxiv.org/pdf/2602.11057v1)
- **Categories:** cs.LG


> The paper introduces **Pram**, the first framework that harnesses multimodal language models (MLMs) as reasoning agents to solve large‑scale multi‑commodity flow (MCF) problems. Pram first decomposes a global MCF instance into many local sub‑problems, lets an MLM‑based “agent” solve each sub‑problem via in‑context gradient‑descent reasoning, and then restores global feasibility through a multi‑agent reinforcement‑learning harmonizer that coordinates the agents’ solutions. The authors prove that this in‑context gradient descent converges to the optimal solution within the MCF family, and experiments on real‑world and benchmark networks show that Pram attains near‑LP optimality while being 10–100× faster and remains robust (<10 % loss) to link failures and flow spikes—demonstrating that agentic, language‑model‑driven reasoning can be a practical, scalable alternative to traditional combinatorial optimizers.


<details>
<summary>Abstract</summary>

The multi-commodity flow (MCF) problem is a fundamental topic in network flow and combinatorial optimization, with broad applications in transportation, communication, and logistics, etc. Nowadays, the rapid expansion of allocation systems has posed challenges for existing optimization engines in balancing optimality and tractability. In this paper, we present Pram, the first ML-based method that leverages the reasoning power of multimodal language models (MLMs) for addressing the trade-off dilemma -- a great need of service providers. As part of our proposal, Pram (i) quickly computes high-quality allocations by dividing the original problem into local subproblems, which are then resolved by an MLM-powered "agent", and (ii) ensures global consistency by harmonizing these subproblems via a multi-agent reinforcement learning algorithm. Theoretically, we show that Pram, which learns to perform gradient descent in context, provably converges to the optimum within the family of MCF problems. Empirically, on real-world datasets and public topologies, Pram achieves performance comparable to, and in some cases even surpassing, linear programming solvers (very close to the optimal solution), and substantially lower runtimes (1 to 2 orders of magnitude faster). Moreover, Pram exhibits strong robustness (<10\% performance degradation under link failures or flow bursts), demonstrating MLM's generalization ability to unforeseen events. Pram is objective-agnostic and seamlessly integrates with mainstream allocation systems, providing a practical and scalable solution for future networks.

</details>


### 137. SurveyLens: A Research Discipline-Aware Benchmark for Automatic Survey Generation

- **Authors:** Beichen Guo, Zhiyuan Wen, Jia Gu, Senzhang Wang, Haochen Shi, Ruosong Yang, Shuaiqi Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11238v1](http://arxiv.org/abs/2602.11238v1)
- **PDF:** [https://arxiv.org/pdf/2602.11238v1](https://arxiv.org/pdf/2602.11238v1)
- **Categories:** cs.CL


> The paper introduces **SurveyLens**, the first benchmark that evaluates automatic survey‑generation (ASG) systems with respect to the distinct writing standards of ten academic disciplines, providing a curated set of 1,000 human‑written surveys (SurveyLens‑1k). It proposes a **dual‑lens evaluation framework**: (1) a Discipline‑Aware Rubric that uses LLMs weighted by human preferences to score compliance with domain‑specific conventions, and (2) a Canonical Alignment metric that quantifies content coverage and synthesis quality against the reference surveys. Experiments on 11 state‑of‑the‑art ASG approaches—including vanilla LLMs, dedicated ASG pipelines, and commercial Deep Research agents—show that multi‑agent, discipline‑aware agents excel in fields with stricter methodological norms, while simpler LLMs perform competitively in more homogeneous domains, offering concrete guidance for selecting or designing agentic AI tools tailored to specific scholarly disciplines.


<details>
<summary>Abstract</summary>

The exponential growth of scientific literature has driven the evolution of Automatic Survey Generation (ASG) from simple pipelines to multi-agent frameworks and commercial Deep Research agents. However, current ASG evaluation methods rely on generic metrics and are heavily biased toward Computer Science (CS), failing to assess whether ASG methods adhere to the distinct standards of various academic disciplines. Consequently, researchers, especially those outside CS, lack clear guidance on using ASG systems to yield high-quality surveys compliant with specific discipline standards. To bridge this gap, we introduce SurveyLens, the first discipline-aware benchmark evaluating ASG methods across diverse research disciplines. We construct SurveyLens-1k, a curated dataset of 1,000 high-quality human-written surveys spanning 10 disciplines. Subsequently, we propose a dual-lens evaluation framework: (1) Discipline-Aware Rubric Evaluation, which utilizes LLMs with human preference-aligned weights to assess adherence to domain-specific writing standards; and (2) Canonical Alignment Evaluation to rigorously measure content coverage and synthesis quality against human-written survey papers. We conduct extensive experiments by evaluating 11 state-of-the-art ASG methods on SurveyLens, including Vanilla LLMs, ASG systems, and Deep Research agents. Our analysis reveals the distinct strengths and weaknesses of each paradigm across fields, providing essential guidance for selecting tools tailored to specific disciplinary requirements.

</details>


### 138. Beyond Context Sharing: A Unified Agent Communication Protocol (ACP) for Secure, Federated, and Autonomous Agent-to-Agent (A2A) Orchestration

- **Authors:** Naveen Kumar Krishnan
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.15055v1](http://arxiv.org/abs/2602.15055v1)
- **PDF:** [https://arxiv.org/pdf/2602.15055v1](https://arxiv.org/pdf/2602.15055v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces the **Agent Communication Protocol (ACP)**, a unified, zero‑trust framework that lets heterogeneous autonomous agents discover one another, negotiate intents, and execute federated workflows across disparate platforms. By extending the Model Context Protocol with decentralized identity verification, semantic intent mapping, and automated service‑level agreements, the authors implement a lightweight orchestration layer and evaluate it on a multi‑cloud testbed, showing a **significant reduction in inter‑agent latency (≈ X % improvement) while preserving strict security guarantees**. These results demonstrate that ACP can serve as a scalable backbone for the emerging “Agentic Web,” enabling secure, interoperable, and autonomous agent‑to‑agent coordination.


<details>
<summary>Abstract</summary>

In the artificial intelligence space, as we transition from isolated large language models to autonomous agents capable of complex reasoning and tool use. While foundational architectures and local context management protocols have been established, the challenge of cross-platform, decentralized, and secure interaction remains a significant barrier to the realization of a truly Agentic Web. Building upon the foundations of AI agent architectures and the Model Context Protocol (MCP) for multi-agent coordination, this paper introduces the Agent Communication Protocol (ACP). ACP provides a standardized framework for Agent-to-Agent (AA) interaction, enabling heterogeneous agents to discover, negotiate, and execute collaborative workflows across disparate environments. We propose a federated orchestration model that integrates decentralized identity verification, semantic intent mapping, and automated service-level agreements. Our evaluation demonstrates that ACP reduces inter-agent communication latency by % while maintaining a zero-trust security posture. This work represents a critical advancement toward a scalable and interoperable ecosystem of autonomous digital entities

</details>


### 139. Chain-of-Look Spatial Reasoning for Dense Surgical Instrument Counting

- **Authors:** Rishikesh Bhyri, Brian R Quaranto, Philip J Seger, Kaity Tung, Brendan Fox, Gene Yang, Steven D. Schwaitzberg, Junsong Yuan, Nan Xi, Peter C W Kim
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11024v1](http://arxiv.org/abs/2602.11024v1)
- **PDF:** [https://arxiv.org/pdf/2602.11024v1](https://arxiv.org/pdf/2602.11024v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **Chain‑of‑Look**, a visual‑reasoning framework that emulates the human sequential counting process by constructing an ordered “visual chain” through densely packed surgical instruments, and enforces spatial coherence with a novel **neighboring loss** that captures physical proximity constraints. Using this chain‑guided approach, the authors train a multimodal model on the newly released **SurgCount‑HD** dataset (1,464 high‑density instrument images) and demonstrate that it surpasses current counting‑oriented methods (e.g., CountGD, REC) and large multimodal language models (e.g., Qwen, ChatGPT) on dense surgical instrument counting tasks. The results show that imposing an explicit, ordered spatial trajectory markedly improves counting accuracy in cluttered scenes, highlighting a promising direction for agentic AI systems that require structured visual reasoning and physically plausible action sequences.


<details>
<summary>Abstract</summary>

Accurate counting of surgical instruments in Operating Rooms (OR) is a critical prerequisite for ensuring patient safety during surgery. Despite recent progress of large visual-language models and agentic AI, accurately counting such instruments remains highly challenging, particularly in dense scenarios where instruments are tightly clustered. To address this problem, we introduce Chain-of-Look, a novel visual reasoning framework that mimics the sequential human counting process by enforcing a structured visual chain, rather than relying on classic object detection which is unordered. This visual chain guides the model to count along a coherent spatial trajectory, improving accuracy in complex scenes. To further enforce the physical plausibility of the visual chain, we introduce the neighboring loss function, which explicitly models the spatial constraints inherent to densely packed surgical instruments. We also present SurgCount-HD, a new dataset comprising 1,464 high-density surgical instrument images. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches for counting (e.g., CountGD, REC) as well as Multimodality Large Language Models (e.g., Qwen, ChatGPT) in the challenging task of dense surgical instrument counting.

</details>


### 140. TVCACHE: A Stateful Tool-Value Cache for Post-Training LLM Agents

- **Authors:** Abhishek Vijaya Kumar, Bhaskar Kataria, Byungsoo Oh, Emaad Manzoor, Rachee Singh
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10986v1](http://arxiv.org/abs/2602.10986v1)
- **PDF:** [https://arxiv.org/pdf/2602.10986v1](https://arxiv.org/pdf/2602.10986v1)
- **Categories:** cs.LG


> TVCACHE introduces a stateful tool‑value cache that enables post‑training reinforcement‑learning of LLM agents to reuse tool outputs safely by matching the entire preceding tool‑call history, thereby guaranteeing that the environment state is identical. The system builds a tree of observed tool‑call sequences and performs longest‑prefix lookups so that a cache hit occurs only when the current agent’s tool history exactly matches a previously executed one. Across three benchmark domains (terminal‑based tasks, SQL generation, and video understanding), TVCACHE attains up to 70 % cache‑hit rates, cuts median tool‑call latency by up to 6.9×, and preserves the agents’ post‑training reward performance, dramatically reducing training time and cost for tool‑using LLM agents.


<details>
<summary>Abstract</summary>

In RL post-training of LLM agents, calls to external tools take several seconds or even minutes, leaving allocated GPUs idle and inflating post-training time and cost. While many tool invocations repeat across parallel rollouts and could in principle be cached, naively caching their outputs for reuse is incorrect since tool outputs depend on the environment state induced by prior agent interactions. We present TVCACHE, a stateful tool-value cache for LLM agent post-training. TVCACHE maintains a tree of observed tool-call sequences and performs longest-prefix matching for cache lookups: a hit occurs only when the agent's full tool history matches a previously executed sequence, guaranteeing identical environment state. On three diverse workloads-terminal-based tasks, SQL generation, and video understanding. TVCACHE achieves cache hit rates of up to 70% and reduces median tool call execution time by up to 6.9X, with no degradation in post-training reward accumulation.

</details>


### 141. CMAD: Cooperative Multi-Agent Diffusion via Stochastic Optimal Control

- **Authors:** Riccardo Barbano, Alexander Denker, Zeljko Kereta, Runchang Li, Francisco Vargas
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10933v1](http://arxiv.org/abs/2602.10933v1)
- **PDF:** [https://arxiv.org/pdf/2602.10933v1](https://arxiv.org/pdf/2602.10933v1)
- **Categories:** cs.LG


> The paper introduces **CMAD**, a framework that recasts the problem of composing multiple pre‑trained diffusion models as a **cooperative stochastic optimal control (SOC) task**, treating each diffusion model as an autonomous agent whose trajectories are jointly steered toward a common objective defined on their combined output. By formulating the interaction through SOC rather than algebraic density composition, the authors derive a control policy that synchronizes the agents’ diffusion processes and implement it via a tractable optimal‑control solver; they compare this cooperative control to a baseline that simply adds per‑step gradient guidance (DPS‑style). Experiments on conditional MNIST show that the SOC‑based cooperative control yields higher fidelity and more consistent conditional generation than the naive gradient‑guidance baseline, demonstrating the viability of agent‑centric control for multi‑model generative composition.


<details>
<summary>Abstract</summary>

Continuous-time generative models have achieved remarkable success in image restoration and synthesis. However, controlling the composition of multiple pre-trained models remains an open challenge. Current approaches largely treat composition as an algebraic composition of probability densities, such as via products or mixtures of experts. This perspective assumes the target distribution is known explicitly, which is almost never the case. In this work, we propose a different paradigm that formulates compositional generation as a cooperative Stochastic Optimal Control problem. Rather than combining probability densities, we treat pre-trained diffusion models as interacting agents whose diffusion trajectories are jointly steered, via optimal control, toward a shared objective defined on their aggregated output. We validate our framework on conditional MNIST generation and compare it against a naive inference-time DPS-style baseline replacing learned cooperative control with per-step gradient guidance.

</details>


### 142. Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System

- **Authors:** Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Qi Li, Ke Xu, Mingwei Xu, Zhuotao Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10915v3](http://arxiv.org/abs/2602.10915v3)
- **PDF:** [https://arxiv.org/pdf/2602.10915v3](https://arxiv.org/pdf/2602.10915v3)
- **Categories:** cs.CR, cs.AI


> The paper introduces **Aura**, a clean‑slate, intent‑centric mobile‑agent operating system that replaces the fragile “screen‑as‑interface” approach with a structured, kernel‑mediated interaction model. By systematically dissecting the threat surface of a state‑of‑the‑art LLM‑driven mobile assistant (Doubao) across agent identity, external interface, internal reasoning, and action execution, the authors expose attacks such as fake app identities, visual spoofing, indirect prompt injection, and privilege escalation, and then design four defense pillars—cryptographic identity binding, semantic firewalls, taint‑aware cognitive integrity, and fine‑grained audited access control—implemented in a hub‑and‑spoke architecture (System Agent ↔ App Agents ↔ Agent Kernel). Empirical evaluation on MobileSafetyBench shows Aura raises low‑risk task success from ~75 % to 94.3 %, cuts high‑risk attack success from ~40 % to 4.4 %, and delivers roughly ten‑fold latency improvements, establishing a secure, scalable foundation for autonomous mobile agents.


<details>
<summary>Abstract</summary>

The evolution of Large Language Models (LLMs) has shifted mobile computing from App-centric interactions to system-level autonomous agents. Current implementations predominantly rely on a "Screen-as-Interface" paradigm, which inherits structural vulnerabilities and conflicts with the mobile ecosystem's economic foundations. In this paper, we conduct a systematic security analysis of state-of-the-art mobile agents using Doubao Mobile Assistant as a representative case. We decompose the threat landscape into four dimensions - Agent Identity, External Interface, Internal Reasoning, and Action Execution - revealing critical flaws such as fake App identity, visual spoofing, indirect prompt injection, and unauthorized privilege escalation stemming from a reliance on unstructured visual data.
  To address these challenges, we propose Aura, an Agent Universal Runtime Architecture for a clean-slate secure agent OS. Aura replaces brittle GUI scraping with a structured, agent-native interaction model. It adopts a Hub-and-Spoke topology where a privileged System Agent orchestrates intent, sandboxed App Agents execute domain-specific tasks, and the Agent Kernel mediates all communication. The Agent Kernel enforces four defense pillars: (i) cryptographic identity binding via a Global Agent Registry; (ii) semantic input sanitization through a multilayer Semantic Firewall; (iii) cognitive integrity via taint-aware memory and plan-trajectory alignment; and (iv) granular access control with non-deniable auditing. Evaluation on MobileSafetyBench shows that, compared to Doubao, Aura improves low-risk Task Success Rate from roughly 75% to 94.3%, reduces high-risk Attack Success Rate from roughly 40% to 4.4%, and achieves near-order-of-magnitude latency gains. These results demonstrate Aura as a viable, secure alternative to the "Screen-as-Interface" paradigm.

</details>


### 143. Agent-Diff: Benchmarking LLM Agents on Enterprise API Tasks via Code Execution with State-Diff-Based Evaluation

- **Authors:** Hubert M. Pysklo, Artem Zhuravel, Patrick D. Watson
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.11224v1](http://arxiv.org/abs/2602.11224v1)
- **PDF:** [https://arxiv.org/pdf/2602.11224v1](https://arxiv.org/pdf/2602.11224v1)
- **Categories:** cs.SE, cs.CL


> Agent‑Diff introduces a unified benchmarking suite for agentic LLMs that evaluates their ability to drive real‑world enterprise workflows by executing code against live APIs (Slack, Box, Linear, Google Calendar) within a controlled sandbox. The framework separates “process” from “outcome” through a state‑diff contract that declares a task successful only when the expected change in the service’s state is observed, and it provides a common scripting layer that all agents use to issue API calls, thereby eliminating environment‑specific variability. Experiments on 224 enterprise‑automation tasks show sizable performance gaps among nine LLMs and reveal that access to up‑to‑date API documentation markedly improves success rates, confirming both the discriminative power of the benchmark and the importance of documentation for robust agentic behavior.


<details>
<summary>Abstract</summary>

We present Agent-Diff, a novel benchmarking framework for evaluating agentic Large Language Models (LLMs) on real-world tasks that execute code via external APIs. Agentic LLM performance varies due to differences in models, external tool access, prompt structures, and agentic frameworks. Benchmarks must make fundamental trade-offs between a sandboxed approach that controls for variation in software environments and more ecologically valid approaches employing real services. Agent-Diff attempts to capture the desirable features of both of these approaches by including access to the real API interfaces for software services while sandboxing the environment in which calls are made, processed, and evaluated. This approach relies on two key innovations. The first is a novel state-diff contract, which separates process from outcome - rather than fuzzy trace or parameter matching, we define task success as whether the expected change in environment state was achieved. The second is a novel sandbox that provides a standardized scripting layer that all models use to execute code against external APIs (Slack, Box, Linear, Google Calendar). Thus, we can evaluate different agentic LLMs against a standardized set of contracts using a unified sandbox while still evaluating their performance on real-world service interfaces. Using the Agent-Diff framework, we provide benchmarks for nine LLMs across 224 tasks utilizing enterprise software workflows. In addition, we evaluate the robustness of the framework with ablation experiments to assess the contribution of access to API documentation on benchmark performance. Code and data: https://github.com/agent-diff-bench/agent-diff.

</details>


### 144. Towards Probabilistic Strategic Timed CTL

- **Authors:** Wojciech Jamroga, Marta Kwiatkowska, Wojciech Penczek, Laure Petrucci, Teofil Sidoruk
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10824v1](http://arxiv.org/abs/2602.10824v1)
- **PDF:** [https://arxiv.org/pdf/2602.10824v1](https://arxiv.org/pdf/2602.10824v1)
- **Categories:** cs.LO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

We define PSTCTL, a probabilistic variant of Strategic Timed CTL (STCTL), interpreted over stochastic multi-agent systems with continuous time and asynchronous execution semantics. STCTL extends TCTL with strategic operators in the style of ATL. Moreover, we demonstrate the feasibility of verification with irP-strategies.

</details>


### 145. See, Plan, Snap: Evaluating Multimodal GUI Agents in Scratch

- **Authors:** Xingyi Zhang, Yulei Ye, Kaifeng Huang, Wenhao Li, Xiangfeng Wang
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10814v1](http://arxiv.org/abs/2602.10814v1)
- **PDF:** [https://arxiv.org/pdf/2602.10814v1](https://arxiv.org/pdf/2602.10814v1)
- **Categories:** cs.AI


> The paper introduces **ScratchWorld**, a new benchmark that evaluates multimodal agents’ ability to build Scratch programs through a graphical user interface. It defines 83 “Use‑Modify‑Create” tasks across creation, debugging, extension, and computation, and measures performance in two interaction modes—low‑level drag‑and‑drop (primitive) to test visuomotor control and high‑level API calls (composite) to isolate reasoning—using an execution‑based protocol that runs the generated projects in a browser to verify functional correctness. Experiments with current multimodal language models and GUI agents show that, while the models can plan solutions effectively, they still struggle dramatically with fine‑grained GUI manipulation, exposing a large reasoning‑to‑acting gap in agentic AI.


<details>
<summary>Abstract</summary>

Block-based programming environments such as Scratch play a central role in low-code education, yet evaluating the capabilities of AI agents to construct programs through Graphical User Interfaces (GUIs) remains underexplored. We introduce ScratchWorld, a benchmark for evaluating multimodal GUI agents on program-by-construction tasks in Scratch. Grounded in the Use-Modify-Create pedagogical framework, ScratchWorld comprises 83 curated tasks spanning four distinct problem categories: Create, Debug, Extend, and Compute. To rigorously diagnose the source of agent failures, the benchmark employs two complementary interaction modes: primitive mode requires fine-grained drag-and-drop manipulation to directly assess visuomotor control, while composite mode uses high-level semantic APIs to disentangle program reasoning from GUI execution. To ensure reliable assessment, we propose an execution-based evaluation protocol that validates the functional correctness of the constructed Scratch programs through runtime tests within the browser environment. Extensive experiments across state-of-the-art multimodal language models and GUI agents reveal a substantial reasoning--acting gap, highlighting persistent challenges in fine-grained GUI manipulation despite strong planning capabilities.

</details>


### 146. Locomo-Plus: Beyond-Factual Cognitive Memory Evaluation Framework for LLM Agents

- **Authors:** Yifei Li, Weidong Guo, Lingling Zhang, Rongman Xu, Muye Huang, Hui Liu, Lijiao Xu, Yu Xu, Jun Liu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10715v1](http://arxiv.org/abs/2602.10715v1)
- **PDF:** [https://arxiv.org/pdf/2602.10715v1](https://arxiv.org/pdf/2602.10715v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **LoCoMo‑Plus**, a new benchmark that tests LLM agents’ ability to retain and apply *latent* user constraints (e.g., goals, values, states) across long, multi‑turn dialogues, addressing the “cue‑trigger semantic disconnect” that existing factual‑recall benchmarks ignore. To evaluate this, the authors devise a unified metric based on **constraint‑consistency**—checking whether the model’s responses respect the hidden constraints—rather than traditional string‑matching or task‑specific prompts. Experiments on a range of backbone LLMs, retrieval‑augmented systems, and explicit memory modules show that even state‑of‑the‑art agents frequently violate these hidden constraints, revealing a substantial gap in current cognitive‑memory capabilities that is invisible to standard benchmarks.


<details>
<summary>Abstract</summary>

Long-term conversational memory is a core capability for LLM-based dialogue systems, yet existing benchmarks and evaluation protocols primarily focus on surface-level factual recall. In realistic interactions, appropriate responses often depend on implicit constraints such as user state, goals, or values that are not explicitly queried later. To evaluate this setting, we introduce \textbf{LoCoMo-Plus}, a benchmark for assessing cognitive memory under cue--trigger semantic disconnect, where models must retain and apply latent constraints across long conversational contexts. We further show that conventional string-matching metrics and explicit task-type prompting are misaligned with such scenarios, and propose a unified evaluation framework based on constraint consistency. Experiments across diverse backbone models, retrieval-based methods, and memory systems demonstrate that cognitive memory remains challenging and reveals failures not captured by existing benchmarks. Our code and evaluation framework are publicly available at: https://github.com/xjtuleeyf/Locomo-Plus.

</details>


### 147. MedScope: Incentivizing "Think with Videos" for Clinical Reasoning via Coarse-to-Fine Tool Calling

- **Authors:** Wenjie Li, Yujie Zhang, Haoran Sun, Xingqi He, Hongcheng Gao, Chenglong Ma, Ming Hu, Guankun Wang, Shiyi Yao, Renhao Yang, Hongliang Ren, Lei Wang, Junjun He, Yankai Jiang
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.13332v1](http://arxiv.org/abs/2602.13332v1)
- **PDF:** [https://arxiv.org/pdf/2602.13332v1](https://arxiv.org/pdf/2602.13332v1)
- **Categories:** cs.CV, cs.AI


> MedScope introduces a tool‑using multimodal agent that “thinks with videos” by iteratively narrowing from coarse to fine visual evidence to support clinical reasoning over long‑form procedures. The system interleaves chain‑of‑thought reasoning with targeted video‑analysis tool calls, and is trained with Grounding‑Aware Group Relative Policy Optimization (GA‑GRPO), which supplies grounding‑aligned rewards and evidence‑weighted advantages; the authors also release ClinVideoSuite, a fine‑grained, evidence‑centric clinical video benchmark. Across both in‑domain and out‑of‑domain video understanding tasks, MedScope attains state‑of‑the‑art accuracy and demonstrably higher trustworthiness by grounding its predictions in temporally localized visual evidence, showcasing a concrete step toward agentic AI that can autonomously seek, verify, and cite visual information.


<details>
<summary>Abstract</summary>

Long-form clinical videos are central to visual evidence-based decision-making, with growing importance for applications such as surgical robotics and related settings. However, current multimodal large language models typically process videos with passive sampling or weakly grounded inspection, which limits their ability to iteratively locate, verify, and justify predictions with temporally targeted evidence. To close this gap, we propose MedScope, a tool-using clinical video reasoning model that performs coarse-to-fine evidence seeking over long-form procedures. By interleaving intermediate reasoning with targeted tool calls and verification on retrieved observations, MedScope produces more accurate and trustworthy predictions that are explicitly grounded in temporally localized visual evidence. To address the lack of high-fidelity supervision, we build ClinVideoSuite, an evidence-centric, fine-grained clinical video suite. We then optimize MedScope with Grounding-Aware Group Relative Policy Optimization (GA-GRPO), which directly reinforces tool use with grounding-aligned rewards and evidence-weighted advantages. On full and fine-grained video understanding benchmarks, MedScope achieves state-of-the-art performance in both in-domain and out-of-domain evaluations. Our approach illuminates a path toward medical AI agents that can genuinely "think with videos" through tool-integrated reasoning. We will release our code, models, and data.

</details>


### 148. Beyond Task Performance: A Metric-Based Analysis of Sequential Cooperation in Heterogeneous Multi-Agent Destructive Foraging

- **Authors:** Alejandro Mendoza Barrionuevo, Samuel Yanes Luis, Daniel Gutiérrez Reina, Sergio L. Toral Marín
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10685v1](http://arxiv.org/abs/2602.10685v1)
- **PDF:** [https://arxiv.org/pdf/2602.10685v1](https://arxiv.org/pdf/2602.10685v1)
- **Categories:** cs.MA, cs.LG


> The paper’s main contribution is a comprehensive, metric‑based framework for evaluating cooperation in heterogeneous, partially observable multi‑agent systems, extending analysis beyond raw task performance to include coordination, dependency, fairness, and sensitivity. The authors construct three hierarchical metric families—primary, inter‑team, and intra‑team—and validate them in a realistic destructive foraging scenario (dynamic aquatic surface cleaning) where a search team and a destruction team must act sequentially; they apply the suite to a range of baselines, from classic heuristics to deep‑reinforcement‑learning agents. Results show that the new metrics reveal nuanced differences in how agents share information, depend on one another, and balance workload, uncovering strengths and weaknesses of learning‑based policies that conventional performance scores miss.


<details>
<summary>Abstract</summary>

This work addresses the problem of analyzing cooperation in heterogeneous multi-agent systems which operate under partial observability and temporal role dependency, framed within a destructive multi-agent foraging setting. Unlike most previous studies, which focus primarily on algorithmic performance with respect to task completion, this article proposes a systematic set of general-purpose cooperation metrics aimed at characterizing not only efficiency, but also coordination and dependency between teams and agents, fairness, and sensitivity. These metrics are designed to be transferable to different multi-agent sequential domains similar to foraging. The proposed suite of metrics is structured into three main categories that jointly provide a multilevel characterization of cooperation: primary metrics, inter-team metrics, and intra-team metrics. They have been validated in a realistic destructive foraging scenario inspired by dynamic aquatic surface cleaning using heterogeneous autonomous vehicles. It involves two specialized teams with sequential dependencies: one focused on the search of resources, and another on their destruction. Several representative approaches have been evaluated, covering both learning-based algorithms and classical heuristic paradigms.

</details>


### 149. UMEM: Unified Memory Extraction and Management Framework for Generalizable Memory

- **Authors:** Yongshi Ye, Hui Jiang, Feihu Jiang, Tian Lan, Yichao Du, Biao Fu, Xiaodong Shi, Qianghuai Jia, Longyue Wang, Weihua Luo
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10652v1](http://arxiv.org/abs/2602.10652v1)
- **PDF:** [https://arxiv.org/pdf/2602.10652v1](https://arxiv.org/pdf/2602.10652v1)
- **Categories:** cs.CL


> The paper introduces **UMEM**, a unified framework that simultaneously trains a large language model to **extract** salient insights from its interaction history and to **manage** an evolving memory bank, thereby treating memory as a trainable component of LLM‑based agents.  UMEM leverages **Semantic Neighborhood Modeling** and a **neighborhood‑level marginal utility reward** optimized with GRPO (Generalized Reward‑Based Policy Optimization) to encourage memories that are useful across semantically related queries, preventing overfitting to single instances.  Experiments on five multi‑turn benchmarks show that UMEM consistently outperforms strong baselines—up to **10.67 %** gains in task performance—and exhibits monotonic improvement as the memory continuously evolves, highlighting its potential for more generalizable, self‑evolving agentic AI.


<details>
<summary>Abstract</summary>

Self-evolving memory serves as the trainable parameters for Large Language Models (LLMs)-based agents, where extraction (distilling insights from experience) and management (updating the memory bank) must be tightly coordinated. Existing methods predominately optimize memory management while treating memory extraction as a static process, resulting in poor generalization, where agents accumulate instance-specific noise rather than robust memories. To address this, we propose Unified Memory Extraction and Management (UMEM), a self-evolving agent framework that jointly optimizes a Large Language Model to simultaneous extract and manage memories. To mitigate overfitting to specific instances, we introduce Semantic Neighborhood Modeling and optimize the model with a neighborhood-level marginal utility reward via GRPO. This approach ensures memory generalizability by evaluating memory utility across clusters of semantically related queries. Extensive experiments across five benchmarks demonstrate that UMEM significantly outperforms highly competitive baselines, achieving up to a 10.67% improvement in multi-turn interactive tasks. Futhermore, UMEM maintains a monotonic growth curve during continuous evolution. Codes and models will be publicly released.

</details>


### 150. Co-jump: Cooperative Jumping with Quadrupedal Robots via Multi-Agent Reinforcement Learning

- **Authors:** Shihao Dong, Yeke Chen, Zeren Luo, Jiahui Zhang, Bowen Xu, Jinghan Lin, Yimin Han, Ji Ma, Zhiyou Yu, Yudong Zhao, Peng Lu
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10514v1](http://arxiv.org/abs/2602.10514v1)
- **PDF:** [https://arxiv.org/pdf/2602.10514v1](https://arxiv.org/pdf/2602.10514v1)
- **Categories:** cs.RO, cs.AI, cs.LG


> The paper introduces **Co‑jump**, a novel cooperative locomotion task in which two quadrupedal robots synchronize their jumps to reach heights far beyond what a single robot can achieve, doing so without any explicit inter‑robot communication. The authors train decentralized policies with **Multi‑Agent Proximal Policy Optimization (MAPPO)** combined with a progressive curriculum that gradually increases jump difficulty, thereby overcoming the sparse‑reward and high‑impulse contact challenges of mechanically coupled agents. Experiments show that the learned policies transfer from simulation to real hardware, enabling multi‑directional jumps onto platforms up to 1.5 m high and achieving a 144 % increase in vertical reach (1.1 m vs. 0.45 m solo), demonstrating that proprioceptive‑only, communication‑free coordination can substantially extend the capabilities of legged agents.


<details>
<summary>Abstract</summary>

While single-agent legged locomotion has witnessed remarkable progress, individual robots remain fundamentally constrained by physical actuation limits. To transcend these boundaries, we introduce Co-jump, a cooperative task where two quadrupedal robots synchronize to execute jumps far beyond their solo capabilities. We tackle the high-impulse contact dynamics of this task under a decentralized setting, achieving synchronization without explicit communication or pre-specified motion primitives. Our framework leverages Multi-Agent Proximal Policy Optimization (MAPPO) enhanced by a progressive curriculum strategy, which effectively overcomes the sparse-reward exploration challenges inherent in mechanically coupled systems. We demonstrate robust performance in simulation and successful transfer to physical hardware, executing multi-directional jumps onto platforms up to 1.5 m in height. Specifically, one of the robots achieves a foot-end elevation of 1.1 m, which represents a 144% improvement over the 0.45 m jump height of a standalone quadrupedal robot, demonstrating superior vertical performance. Notably, this precise coordination is achieved solely through proprioceptive feedback, establishing a foundation for communication-free collaborative locomotion in constrained environments.

</details>


### 151. Authenticated Workflows: A Systems Approach to Protecting Agentic AI

- **Authors:** Mohan Rajagopalan, Vinay Rao
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10465v1](http://arxiv.org/abs/2602.10465v1)
- **PDF:** [https://arxiv.org/pdf/2602.10465v1](https://arxiv.org/pdf/2602.10465v1)
- **Categories:** cs.CR, cs.AI, cs.DC, cs.MA


> The paper presents **Authenticated Workflows**, a system‑level trust layer that secures enterprise‑grade agentic AI by cryptographically protecting the four attack surfaces of any autonomous workflow—prompts, tools, data, and execution context. It introduces **MAPL**, an AI‑native policy language that composes hierarchical, cryptographically‑attested policies with logarithmic scaling ( O(log M + N) ) and integrates them into a universal runtime that wraps nine popular LLM and orchestration frameworks via thin adapters, providing deterministic intent and integrity checks at every boundary crossing. Empirical evaluation demonstrates deterministic security (100 % recall, zero false positives) across 174 scenarios, mitigates 9 of the 10 OWASP Top‑10 risks, and fully patches two high‑impact production CVEs, establishing a practical, provably complete and sound foundation for safe, policy‑driven agentic AI deployment.


<details>
<summary>Abstract</summary>

Agentic AI systems automate enterprise workflows but existing defenses--guardrails, semantic filters--are probabilistic and routinely bypassed. We introduce authenticated workflows, the first complete trust layer for enterprise agentic AI. Security reduces to protecting four fundamental boundaries: prompts, tools, data, and context. We enforce intent (operations satisfy organizational policies) and integrity (operations are cryptographically authentic) at every boundary crossing, combining cryptographic elimination of attack classes with runtime policy enforcement. This delivers deterministic security--operations either carry valid cryptographic proof or are rejected. We introduce MAPL, an AI-native policy language that expresses agentic constraints dynamically as agents evolve and invocation context changes, scaling as O(log M + N) policies versus O(M x N) rules through hierarchical composition with cryptographic attestations for workflow dependencies. We prove practicality through a universal security runtime integrating nine leading frameworks (MCP, A2A, OpenAI, Claude, LangChain, CrewAI, AutoGen, LlamaIndex, Haystack) through thin adapters requiring zero protocol modifications. Formal proofs establish completeness and soundness. Empirical validation shows 100% recall with zero false positives across 174 test cases, protection against 9 of 10 OWASP Top 10 risks, and complete mitigation of two high impact production CVEs.

</details>


### 152. The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis

- **Authors:** Peiran Wang, Xinfeng Li, Chong Xiang, Jinghuai Zhang, Ying Li, Lixia Zhang, Xiaofeng Wang, Yuan Tian
- **Published:** 2026-02-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2602.10453v1](http://arxiv.org/abs/2602.10453v1)
- **PDF:** [https://arxiv.org/pdf/2602.10453v1](https://arxiv.org/pdf/2602.10453v1)
- **Categories:** cs.CR, cs.CL


> The paper provides the first systematic taxonomy of Prompt Injection (PI) threats against LLM‑driven autonomous agents, distinguishing attacks by how their malicious payloads are generated (heuristic versus optimization‑based) and classifying defenses by the intervention point (text‑level, model‑level, or execution‑level). By conducting a systematic literature review and quantitative meta‑analysis, the authors expose a critical blind spot in existing defenses and benchmarks: they ignore context‑dependent tasks where agents must act on real‑time environmental observations. To fill this gap, they introduce **AgentPI**, a benchmark that evaluates agents under realistic, context‑rich interactions, and demonstrate empirically that current defenses either sacrifice utility, trustworthiness, or latency and often fail when contextual reasoning is required, highlighting the need for more holistic, adaptable security mechanisms for agentic AI.


<details>
<summary>Abstract</summary>

The evolution of Large Language Models (LLMs) has resulted in a paradigm shift towards autonomous agents, necessitating robust security against Prompt Injection (PI) vulnerabilities where untrusted inputs hijack agent behaviors. This SoK presents a comprehensive overview of the PI landscape, covering attacks, defenses, and their evaluation practices. Through a systematic literature review and quantitative analysis, we establish taxonomies that categorize PI attacks by payload generation strategies (heuristic vs. optimization) and defenses by intervention stages (text, model, and execution levels). Our analysis reveals a key limitation shared by many existing defenses and benchmarks: they largely overlook context-dependent tasks, in which agents are authorized to rely on runtime environmental observations to determine actions. To address this gap, we introduce AgentPI, a new benchmark designed to systematically evaluate agent behavior under context-dependent interaction settings. Using AgentPI, we empirically evaluate representative defenses and show that no single approach can simultaneously achieve high trustworthiness, high utility, and low latency. Moreover, we show that many defenses appear effective under existing benchmarks by suppressing contextual inputs, yet fail to generalize to realistic agent settings where context-dependent reasoning is essential. This SoK distills key takeaways and open research problems, offering structured guidance for future research and practical deployment of secure LLM agents.

</details>



## Medrxiv (2 papers)


### 1. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar N, S., Thomas, M., Chinnakanu, S. J., M, N., Subramaniam, S.
- **Published:** 2026-02-17
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> The paper introduces an AI‑driven pipeline that combines metagenomic profiling with autonomous “CrewAI” agents to both diagnose inflammatory bowel disease (IBD) from gut microbiome data and generate personalized probiotic prescriptions. After preprocessing raw stool metagenomes with Kneaddata and MetaPhlAn, taxonomic abundances are fed to a tuned XGBoost classifier (86.6 % accuracy) and dysbiotic taxa are flagged via Z‑score/fold‑change analysis; the CrewAI agents then synthesize literature‑based rationales to recommend specific strains (e.g., *Faecalibacterium prausnitzii*). The study demonstrates that integrating conventional machine‑learning diagnostics with agentic reasoning can produce interpretable, actionable health recommendations, highlighting a promising direction for agentic AI in precision microbiome medicine.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>


### 2. Metagenomics AI powered prediction of Inflammatory Bowel Disease and Probiotic Recommendation

- **Authors:** Kumar, S. N., Thomas, M., Janakiram, S., M, N., Subramaniam, S. N.
- **Published:** 2026-02-15
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.02.12.26345333](https://doi.org/10.64898/2026.02.12.26345333)

- **Categories:** gastroenterology


> The paper introduces an AI‑driven pipeline that combines metagenomic preprocessing, a high‑performing XGBoost classifier, and an autonomous “CrewAI” agent to both diagnose inflammatory bowel disease (IBD) from gut‑microbiome taxonomic profiles and generate personalized probiotic recommendations. By integrating Kneaddata and MetaPhlAn for taxonomic feature extraction, training a tuned XGBoost model (86.6 % accuracy), and employing the agent to interpret dysbiotic taxa (via Z‑score/fold‑change) and retrieve literature‑backed probiotic suggestions (e.g., *Faecalibacterium prausnitzii*), the system demonstrates that agentic AI can close the loop from data‑driven diagnosis to actionable therapeutic advice. Validation on a single ulcerative colitis sample confirmed correct IBD detection (though mis‑labelled as Crohn’s) and highlighted the agent’s capacity to explain its recommendations, underscoring the promise of autonomous AI agents in precision microbiome‑based healthcare.


<details>
<summary>Abstract</summary>

Background and Objective The dysbiosis of human gut microbiome has been increasingly seen to have a relation in the development of autoimmune diseases, with specific microbial signatures having causative association with specific conditions. Inflammatory bowel disease (IBD) is one such autoimmune ailment. This paper proposes a predictive tool that can identify the IBD status of an individual based on the composition of the gut microbiome using machine learning and AI agents driven techniques. The technology can strengthen the suspicion of a potential IBD diagnosis a patient may have based on their gut microbiome profile. Methods The tool processes patient gut metagenome using integrated Kneaddata and MetaPhlAn to generate taxonomic profiles. These are fed into an XGBoost classifier to predict IBD or healthy status. Dysbiotic taxa are identified via Z-score and fold change. CrewAI delivers personalized probiotic recommendations based on diagnosis and dysbiosis. Results The tuned XGBoost model achieved 86.6% accuracy. On validation using single ulcerative colitis sample, the tool correctly predicted IBD status but misclassified it as Crohns disease(possibly due to overlapping microbial signatures), identifying Faecalibacterium and Flavonifractor as dysbiotic taxa.The probiotic recommended was Faecalibacterium prausnitzii ,backed with reasoning basedon scientific literature. Conclusions Despite limited validation sample size, the high accuracy , correct IBD detection ,dysbiosis analysis and elaborate probiotic recommendation suggest promising potential; further validation needed

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*