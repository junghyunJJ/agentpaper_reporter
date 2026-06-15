# Weekly AI Agent Paper Report

**Generated:** 2026-06-15 15:45
**Period:** 2026-06-08 to 2026-06-14

## Summary

- **Total papers fetched:** 770
- **Papers matching keywords:** 184
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-06-08) | Change |
|--------|-----------|-----------|--------|
| Total matched | 184 | 179 | +5 |
| arxiv | 181 | 175 | +6 |
| biorxiv | 3 | 2 | +1 |
| medrxiv | 0 | 2 | -2 |

### Notable Trends

**1. Volume & source mix**  
- **Overall output is up**: +5 papers week‑over‑week (184 vs 179).  
- **ArXiv dominates** both weeks (≈98 % of submissions). This week the ArXiv share rose slightly (181/184 ≈ 98 % vs 175/179 ≈ 98 %).  
- **Bio‑focused pre‑prints are emerging**: biorXiv jumps from 2 to 3 papers, while medRxiv disappears entirely, suggesting a tilt toward biomedical‑application agents rather than clinical‑trial‑style studies.

**2. Topic shift – from “societies & theory” to “application pipelines”**  
- **Last week’s headlines** were heavily conceptual (“Agentopia”, “Opinion Dynamics”, “Self‑evolving LLM agents”, “Byzantine‑resilient collaboration”).  
- **This week’s top titles** are markedly **pipeline‑oriented**: multi‑objective MARL coordination, latent‑space synthesis for LLM‑agent workflows, governance of open‑source contributors, long‑term error taxonomy in production runtimes, and concrete biomedical pipelines (spine‑MRI report generation, autonomous bio‑discovery, living‑material design).  

**3. Growing attention to **governance & reliability**  
- New papers on “Regulating the Machine Contributor” and “When Errors Become Narratives” signal an accelerating focus on policy alignment, open‑source governance, and systematic failure analysis for deployed LLM agents. This was absent from the prior week’s top list.

**4. Continued rise of **domain‑specific agents** (especially biomedical)**  
- Two of the eight highlighted papers this week target health/biology (spine‑MRI reporting, autonomous biological discovery). The previous week only had one health‑oriented bibliometric study. The shift points to more *working* agents rather than surveys.

**5. Multi‑objective & latent‑space engineering**  
- The lead paper on “Learning Coordinated Preference for Multi‑Objective Multi‑Agent RL” and the latent‑space synthesis work show a trend toward **optimizing agent objectives jointly** and **embedding workflow orchestration directly in LLM latent spaces**—a technical direction that was not prominent a week earlier.

---



## Biomedical Highlights (3 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


These three studies illustrate how autonomous AI agents are being harnessed to streamline complex biomedical workflows and to open new design spaces for living systems.  
* The spine‑MRI work builds a **multi‑agent pipeline** that ingests multi‑sequence MR data, automatically segments vertebrae and discs, detects pathological findings, and generates structured radiology reports; the agents are coordinated through a central orchestration module and evaluated against expert radiologist annotations.  
* In the “agentic AI for biological discovery” paper, researchers benchmark **large‑language‑model‑driven agents** that can run standard bioinformatic pipelines (e.g., RNA‑seq processing, variant calling) either autonomously or as a “copilot” that interacts with a human, measuring success rates, reproducibility, and the capacity to propose novel hypotheses.  
* The “living‑materials design space” study extends multi‑agent reasoning to **computationally explore and fabricate programmable bio‑hybrid materials**, coupling agents that model cellular growth, material mechanics, and fabrication constraints; the agents iteratively propose, simulate, and refine designs, revealing a searchable space of viable living‑material architectures.  

Together, the papers showcase a common theme: **coordinated AI agents that integrate domain‑specific models, data‑processing tools, and generative reasoning to automate interpretation, discovery, and design in biomedicine**, while highlighting methodological advances in orchestration, human‑in‑the‑loop control, and cross‑scale simulation.



### 1. A multi-agent system for spine MRI report generation from multi-sequence imaging

- **Authors:** Xiao, Z., Yang, J., Sun, G., Zhang, H., Xu, H., Yao, Y., Miller, Z. D., King, W. E., Kanani, M. M., Andre, J. B., Chu, S., Zhang, M., Kinahan, P. E., Cross, N. M., Wang, S.
- **Published:** 2026-06-11
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.07.730703](https://doi.org/10.64898/2026.06.07.730703)

- **Categories:** bioinformatics


> SpineAgent is a multi‑agent framework that tackles the long‑standing problem of integrating heterogeneous MRI sequences for automated spine‑MRI reporting. The authors first pre‑train separate DINOv3 encoders on T1‑ and T2‑weighted scans and then use a continual‑training synthesizer to embed all other sequences into a unified patient‑level representation; this representation feeds 37 specialized agents (diagnosis, lesion localisation, similar‑case retrieval) whose outputs are tokenised and fed to a end‑to‑end Medical Report Agent. Across 17 pathology‑prediction tasks SpineAgent improves AUROC by an average of 10.8 % over the strongest baselines, generalises across manufacturers and cohorts, and—according to both automated metrics and radiologist review—produces more accurate and interpretable spine‑MRI reports.


<details>
<summary>Abstract</summary>

Spinal pathology is a leading cause of pain and disability worldwide. Spine magnetic resonance imaging (MRI) is central to clinical evaluation, yet its interpretation remains complex and time-consuming, requiring integration of information across multiple imaging sequences and anatomical regions. Despite recent advances in automated MRI analysis, effectively combining multi-sequence data while preserving sequence-specific diagnostic information remains an open challenge. Here we present SpineAgent, a multi-agent framework for spine MRI report generation built upon a multi-sequence foundation model trained on routine clinical data from 32,047 patients and 453,683 MRI series, comprising a total of 13,441,191 MRI slices. To accommodate diverse modalities of sequences, we first pre-train two DINOv3-based encoders separately on T1- and T2-weighted sequences. We then introduce a continual training strategy that learns a synthesizer to embed images of other sequences using the T1 and T2 encoders, producing patient-level embedding that integrates various signals across MRI sequences. Using these embeddings, SpineAgent achieves state-of-the-art performance, with mean 10.8% AUROC improvement across 17 spinal condition-prediction tasks compared to the best competing method, and demonstrates strong generalizability under cross-manufacturer and cross-cohort evaluation. Beyond classification, SpineAgent enables pathology localization by identifying findings-relevant slices and segmenting pathological regions. It also supports multimodal image-report retrieval, providing a solid foundation for scalable and explainable MRI report generation. We further integrate these validated capabilities of SpineAgent into 37 specialized agents for condition diagnosis, pathological-region localization, and clinically-similar-cases retrieval. Finally, we incorporate their outputs as structured tokens within a Medical Report Agent trained end-to-end for report generation. Through both automated metrics and expert evaluation by five radiologists, SpineAgent achieves leading performance in spine MRI report generation. Together, SpineAgent introduces a continual training approach for multi-sequence spine MRI understanding. By decomposing report generation into clinically grounded subtasks addressed by specialized agents, the SpineAgent framework enables accurate, interpretable and generalizable spine MRI reporting across diverse imaging sequences and anatomical regions.

</details>


### 2. Evaluating agentic AI for biological discovery in autonomous and copilot settings

- **Authors:** Johri, S., Pimenta, E. M., Yates, J., Fu, J., Bao, E. L., Jun, H., Reardon, B., Bacot, S., Shady, M., Fu, D., Mei, W., Camp, S. Y., Park, J., Van Allen, E.
- **Published:** 2026-06-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.04.729919](https://doi.org/10.64898/2026.06.04.729919)

- **Categories:** cancer biology


> The paper introduces the **Multistep Multimodal Multi‑omic Agentic (M3A) Framework**, a systematic evaluation platform that lets large‑language‑model (LLM) agents maintain and reason over persistent multimodal single‑cell data states in both fully autonomous and human‑in‑the‑loop (“copilot”) modes. Using the framework, the authors benchmarked agents on tasks such as cell‑type annotation and the generation of falsifiable, gene‑program‑based biological hypotheses across 11 cancer‑type multi‑omic datasets, and measured performance with and without expert guidance. They find that current agentic AIs excel at broad, systematic exploration of heterogeneous data but still depend on domain experts for methodological direction and high‑level biological synthesis, delineating both the promise and the current limits of AI‑driven biological discovery.


<details>
<summary>Abstract</summary>

Advances in large language models (LLMs)-based artificial intelligence (AI) agents have improved their ability to execute structured analytical workflows, including standard bioinformatic pipelines for biological discovery. However, computational biology rarely consists of deterministic pipeline execution alone. Biological datasets are heterogeneous and noisy, and meaningful discovery often requires open-ended hypothesis generation and iterative reasoning over multimodal evidence. These challenges are particularly evident in multi-omic studies, where paired molecular modalities and heterogeneous clinical contexts create both opportunities and obstacles for discovery. The extent to which emerging agentic AI systems can support or automate this mode of scientific discovery remains poorly understood. Here, we systematically evaluated the capabilities and limitations of agentic AI for biological discovery using multi-omic single cell datasets spanning 11 cancer types. We developed the Multistep Multimodal Multiomic Agentic (M3A) Framework to support LLM-driven reasoning over persistent multimodal data states and to capture agentic reasoning behavior in autonomous and human-AI copilot settings. Using this framework, we assessed AI agents across complementary tasks, including autonomous cell-type annotation, generation of falsifiable biological hypotheses from gene programs, and copilot experiments testing the effect of human involvement and domain expertise. We found that current AI agents are effective at broad, systemic exploration of complex data, whereas domain experts remain critical for methodological guidance and biological synthesis across analyses. Together, our results delineate the current potential and boundaries of agentic AI in computational biology, and establish a framework for evaluating AI systems designed to support biological discovery.

</details>


### 3. Reconstructing living materials as a computable design space with multi-agent reasoning

- **Authors:** Xiao, Y., Zeng, X., Yang, Z., Gu, J., Lu, Y., Wang, Y., Wen, H., Chen, M., Huang, Z., Hu, J., Liu, J., Sha, C., Xie, J., Li, H., Zhu, X., Zheng, S., Zhang, J., Zong, W., He, Z., Xu, Y., Zhou, X., Li, F., Liu, H., He, Q., Liu, L., Yu, Z.
- **Published:** 2026-06-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.15.705954](https://doi.org/10.64898/2026.02.15.705954)

- **Categories:** biochemistry


> The paper presents **LiveMat**, a multi‑agent reasoning platform that converts unstructured literature on living materials into a structured, computable design space. By extracting and linking 34 k+ records into a knowledge graph of microorganisms, polymers, fabrication processes, functional outputs, evaluation contexts, and performance metrics, LiveMat enables systematic cross‑domain feature integration; its pipeline (constraint decomposition, provenance‑aware extraction, consistency checking, and expert‑anchored ranking) markedly improves reasoning performance over five large language models. In a prospective wound‑healing case study, LiveMat automatically selected a four‑component living‑material formulation that achieved state‑of‑the‑art in‑vivo healing, demonstrating the framework’s potential to accelerate interpretable, evidence‑grounded discovery of agentic living‑material systems.


<details>
<summary>Abstract</summary>

Artificial intelligence is increasingly used to accelerate scientific discovery, but most successful frameworks operate within well-defined molecular, protein or materials spaces. Living materials present a more formidable computational problem because functions emerge from context dependent coupling among cells, matrices, fabrication processes and evaluation conditions. Here we introduce LiveMat, a multi-agent reasoning framework that transforms unstructured literature into a computable design space for living materials. LiveMat standardizes 34,215 living material records, integrating 16,769 microorganism and 17,446 polymer entries into a knowledge graph linking living components, abiotic matrices, functional outputs, evaluation contexts and performance metrics. Benchmarking across five large language models shows that living material reasoning is limited mainly by cross-domain feature integration rather than coarse classification. LiveMat overcomes this limitation through constraint decomposition, provenance-aware extraction, consistency checking and expert-anchored ranking. In a prospective wound-healing task, it prioritizes a four-component design with state-of-the-art in vivo performance, establishing a scalable infrastructure for interpretable, evidence-grounded living material discovery.

</details>


---



## Arxiv (181 papers)


### 1. Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning

- **Authors:** Pengxin Wang, Lihao Guo, Yi Xie, Bo Liu, Siyang Cao, Jingdi Chen
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14693v1](http://arxiv.org/abs/2606.14693v1)
- **PDF:** [https://arxiv.org/pdf/2606.14693v1](https://arxiv.org/pdf/2606.14693v1)
- **Categories:** cs.MA, cs.AI


> **Main contribution:** The paper introduces **Preference‑Coordinated Multi‑agent Policy Optimization (PCMA)**, a novel algorithm that learns distinct, coordinated preference vectors for each agent in cooperative multi‑objective multi‑agent reinforcement learning (MOMARL) so that agents can make complementary trade‑offs across conflicting objectives.

**Methodology:** By casting cooperative MOMARL as a team‑optimal game, the authors derive a first‑order improvement decomposition that proves how diversity in agents’ preferences can raise the team’s expected return. PCMA jointly optimizes the agents’ policies and their preference parameters using a centralized critic and a preference‑regularized policy‑gradient update.

**Key findings:** Across several benchmark MOMARL tasks and a realistic traffic‑control case study, PCMA consistently outperforms existing baselines, achieving higher overall objective scores and more balanced, coordinated trade‑off behaviours among agents, thereby demonstrating the practical benefit of learned preference coordination in agentic AI systems.


<details>
<summary>Abstract</summary>

Cooperative multi-objective multi-agent reinforcement learning (MOMARL) models team decision making under multiple, potentially conflicting objectives. In this setting, conflicts arise not only across objectives but also across agents with different observations, roles, and contributions. We propose Preference Coordinated Multi-agent Policy Optimization (PCMA), which learns coordinated agent-specific preferences to enable complementary trade-offs among agents. Theoretically, we formulate cooperative MOMARL as a team-optimal game and show that, under suitable conditions, preference diversity can induce team improvement through a first-order improvement decomposition. Experiments on multiple cooperative MOMA environments and a practical traffic-control scenario show that PCMA improves both performance and trade-off coordination.

</details>


### 2. AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition

- **Authors:** Jixuan Chen, Jianzhi Shen, Haoqiang Kang, Zhi Hong, Qingyi Jiang, Soham Bose, Yiming Zhang, Leon Leng, Amit Vyas, Lingjun Mao, Siru Ouyang, Kun Zhou, Lianhui Qin
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14674v1](http://arxiv.org/abs/2606.14674v1)
- **PDF:** [https://arxiv.org/pdf/2606.14674v1](https://arxiv.org/pdf/2606.14674v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **AgentSpec**, a modular specification framework that formalizes embodied LLM agents as typed compositions of interchangeable policy components (perception, memory, reasoning, reflection, action, and optional learning), making it possible to isolate and compare the effects of each scaffold element.

**Methodology:** The authors define standardized interfaces for each component, implement a library of interchangeable modules, and evaluate them across four benchmark suites (DeliveryBench, ALFRED, MiniGrid, RoboTHOR). By systematically swapping and recombining modules—varying memory granularity, reasoning styles, reflection mechanisms, and RL‑trained policies—they conduct controlled ablation experiments to measure interaction effects.

**Key findings:** Agent performance is dominated by **scaffold compatibility and component interactions** rather than the raw strength of any single module. Structured multi‑granularity memory markedly improves long‑horizon state tracking; reasoning and memory exhibit environment‑dependent synergy; reflection provides error correction at the cost of additional compute; and RL policies achieve the highest gains when optimized jointly with the deployment‑time scaffold layout. AgentSpec thus provides a reproducible, composable platform for designing and analyzing agentic AI systems.


<details>
<summary>Abstract</summary>

LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning. While such scaffolds often improve performance, they are often embedded in tightly coupled pipelines, making it difficult to isolate component contributions, compare alternative designs, or understand how module interactions shape agent behavior. We introduce AgentSpec, a modular specification framework that represents embodied agents as typed compositions of reusable policy components with standardized interfaces. AgentSpec standardizes the interfaces among perception, memory, reasoning, reflection, action, and optional learning, enabling components to be swapped and recombined under controlled conditions. We instantiate this framework across DeliveryBench, ALFRED, MiniGrid, and RoboTHOR, and analyze reasoning, memory, reflection, and reinforcement-learning modules across model backbones. Our results show that agent performance is governed by scaffold compatibility and interaction effects rather than isolated module strength. In particular, structured multi-granularity memory improves long-horizon state tracking, reasoning and memory interact non-uniformly across environments, reflection trades off correction and cost, and RL-trained policies compose best when optimized with deployment-time scaffold structure. AgentSpec provides a controlled foundation for studying, comparing, and designing composable LLM agents. Our code, baselines and interactive playground are publicly available at https://agentspec-embodied.github.io.

</details>


### 3. Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows

- **Authors:** Shikun Liu, Mufei Li, Dongqi Fu, Haoyu Wang, Yinglong Xia, Hong Li, Hong Yan, Pan Li
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14672v1](http://arxiv.org/abs/2606.14672v1)
- **PDF:** [https://arxiv.org/pdf/2606.14672v1](https://arxiv.org/pdf/2606.14672v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution** – The paper proposes *Parallel‑Synthesis*, a plug‑and‑play framework that lets a downstream LLM synthesizer consume the key‑value (KV) attention caches generated by multiple parallel worker agents, eliminating the need to materialise each branch as concatenated text.  

**Methodology** – Parallel‑Synthesis consists of (1) a **cache mapper** that aligns and normalises the independently produced KV caches, and (2) a **fine‑tuned synthesizer adapter** trained to generate directly from this non‑sequential cache representation. Training data expose the synthesizer to parallel cache contexts, teach it to aggregate reasoning across branches, and distill the behavior of conventional text‑concatenation synthesis.  

**Key findings** – Across nine benchmarks (math, science QA, code, GAIA, multi‑agent DB diagnosis), the cache‑based approach matches or exceeds the performance of standard text‑based synthesis on seven tasks and stays near‑par on the remaining two, while cutting time‑to‑first‑token by **2.5×–11×**. These results show that direct latent‑space synthesis is an efficient, structurally faithful interface for agentic AI workflows with parallel branches.


<details>
<summary>Abstract</summary>

Large language models increasingly serve as execution engines for agentic systems, yet they still consume context through a sequential text interface. This creates a mismatch with modern structured agent workflows, in which independent branches explore subtasks, retrieve evidence, or generate candidate solutions before a final synthesis step. Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. In this work, we introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents. Parallel-Synthesis combines a cache mapper that calibrates independently generated branch caches with a fine-tuned synthesizer adapter that enables generation from this non-sequential cache interface. We train Parallel-Synthesis using data that exposes the synthesizer to parallel cache contexts, teaches aggregation across cached branches, and distills reasoning behavior from standard text-concatenation-based synthesis. Across nine downstream datasets spanning math, science QA, code generation, GAIA, and multi-agent database diagnosis, Parallel-Synthesis matches or outperforms text-based synthesis on seven datasets and remains close on the other two. It also reduces time-to-first-token by 2.5x-11x, suggesting that direct cache-based synthesis is a promising interface for more native and efficient synthesis over parallel agent branches.

</details>


### 4. Regulating the Machine Contributor: Governance and Policy Alignment in Open Source

- **Authors:** Jassem Manita, Aziz Amari
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14594v1](http://arxiv.org/abs/2606.14594v1)
- **PDF:** [https://arxiv.org/pdf/2606.14594v1](https://arxiv.org/pdf/2606.14594v1)
- **Categories:** cs.SE, cs.AI


> The paper’s main contribution is a systematic audit of how open‑source projects are currently governing autonomous AI contributors and a mapping of the resulting policy gaps onto major AI governance frameworks (EU AI Act, NIST AI RMF, ISO 42001/23894). Using a Most‑Similar Systems Design, the authors code contribution policies from six major ecosystems and trace incident processes for SymPy and LLVM, producing a six‑dimensional taxonomy (disclosure, responsibility, human oversight, licensing, enforcement, maintainer workload) and an ordinal Policy‑Maturity Score that highlights where existing rules fail to control AI‑generated pull‑requests and nuisance volume. The analysis shows that current policies are fragmented and miss critical overlaps with external regulations, prompting the proposal of a harmonized, tiered governance framework and a roadmap for its empirical validation.


<details>
<summary>Abstract</summary>

AI-assisted software development has moved from line-level autocomplete to agents that can plan changes, edit files, and submit pull requests with limited human supervision. Open-source software, however, evolves through a process designed for humans: contributor agreements, codes of conduct, and review norms all assume a legally accountable person who can attest to provenance and answer reviewer questions. Autonomous and semi-autonomous AI contributors strain those assumptions, and the 2025-2026 record of agent-driven incidents, AI-generated nuisance volume, and platform-level shutdowns shows that the gap is operationally consequential. Several open-source organisations have responded with contribution policies, but the result is fragmented, and its alignment with emerging AI governance frameworks (EU AI Act, NIST AI RMF with the UC Berkeley Agentic AI Profile, ISO/IEC 42001 and 23894) is unmapped at the contribution level. We compare policies across six organisations (SymPy, LLVM, matplotlib, OpenInfra, the Apache Software Foundation, and the Linux Foundation) using Most-Similar Systems Design with indicator-based coding and process tracing for SymPy and LLVM. From this we derive a six-dimensional taxonomy (disclosure, responsibility, human oversight, licensing, enforcement, maintainer workload), an ordinal Policy Maturity Score, and a mapping of documented agent incidents onto the dimensions each policy fails to govern. Aligning the dimensions with the regulatory frameworks above identifies overlapping gaps neither side currently closes, and we close by sketching the shape of a harmonised tiered framework and the empirical evaluation needed to calibrate it.

</details>


### 5. When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

- **Authors:** Wei Wu
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14589v1](http://arxiv.org/abs/2606.14589v1)
- **PDF:** [https://arxiv.org/pdf/2606.14589v1](https://arxiv.org/pdf/2606.14589v1)
- **Categories:** cs.SE, cs.AI, cs.DC


> The paper presents the first longitudinal, production‑scale analysis of “silent” failures in a continuously running personal‑assistant LLM agent (40 scheduled jobs, 8 providers, a tool‑governance proxy, and a knowledge‑base memory plane) and introduces a mechanism‑oriented taxonomy of five failure classes, highlighting a novel “fail‑plausible” pattern in which the LLM covertly rewrites errors into convincing narratives delivered to the user. By examining 22 fully investigated incidents over eight weeks, the authors show that most silent failures are only discovered through user observation (≈ 70 %), that pre‑deployment checks prevent none of them while post‑mortems block 87 % of regressions, and that latency correlates with failure mechanism rather than code complexity—especially for failures at component seams. The work culminates in a defensive framework and design principles aimed at making agentic AI failures loud, attributable, and easy to test, providing all post‑mortems and artifacts publicly for the community.


<details>
<summary>Abstract</summary>

LLM agent systems increasingly run as long-lived autonomous runtimes: scheduling jobs, calling tools, maintaining memory, and pushing results to humans. We present a longitudinal study of silent failures in one such system: a personal-assistant agent runtime in continuous production since March 2026, with roughly 40 scheduled jobs, 8 LLM providers, a tool-governance proxy, and a knowledge-base memory plane, defended by 4,286 unit tests and 827 governance checks. Over eight weeks we documented 22 incidents with full root-cause postmortems, in which one meta-pattern -- a failure whose error signal never reaches a human in actionable form -- manifested at least 28 times. We derive a five-class, mechanism-oriented taxonomy: (A) environment and platform quirks, (B) design-assumption mismatches, (C) error swallowing and dilution, (D) chained hallucination and fabrication, (E) operational omission and forensic blind spots. Class D is unique to LLM systems and the most dangerous: the system does not merely fail to report an error -- the LLM transforms it into fluent, plausible narrative delivered to the user. We term this fail-plausible: gray failure's differential observability escalated -- the observer is not just blind, it is convincingly lied to by the failure itself. Three findings: about 70% of silent failures were caught by human user-view observation, not tests or audits; a retrospective audit of 15 incidents found 0% ex-ante prevention but 87% regression blocking -- audits are regression engines, not prediction engines; incident latency (13 hours to 60 days) tracks failure mechanism, not code complexity -- the longest-lived failures lived in the seams between components, where no test runs. We describe the resulting defense framework and distill design principles for agent systems whose failures are loud, attributable, and boring. All postmortems and artifacts are public.

</details>


### 6. SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model

- **Authors:** Xiaoxin Lu, Ranran Haoran Zhang, Rui Zhang
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14574v1](http://arxiv.org/abs/2606.14574v1)
- **PDF:** [https://arxiv.org/pdf/2606.14574v1](https://arxiv.org/pdf/2606.14574v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **SIMMER**, a new benchmark that exposes “latent failures” in large‑language‑model (LLM) planners—errors that do not abort execution immediately but silently derail goal achievement, often irreversibly. By constructing a human‑curated symbolic kitchen world model (77 actions, 262 objects, ~46 k interaction triples) and a state‑machine executor that checks preconditions, latent hazards, and irreversible outcomes, the authors evaluate six LLMs and find that at best only 17 % of generated plans are completely error‑free, with up to 56 % containing latent failures. They also show that augmenting LLM planning with explicit counter‑factual state‑reasoning (simulation‑based foresight) cuts latent failures by up to 72 % and irreversible cases by up to 75%, highlighting a concrete path toward safer, more reliable agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments. While existing benchmarks evaluate whether LLM-generated plans execute successfully, they overlook a critical type of failure: latent failures. Unlike immediate failures that trigger instant feedback at execution time and enable timely correction, latent failures do not immediately halt plan execution but silently compromise goal achievement. In severe cases, they cause irreversible harm. To address this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM planning through a human-curated symbolic world model grounded in the kitchen domain. SIMMER defines a world model comprising 77 actions, 262 unique objects, and approximately 46,800 possible interactions that are semantically realistic, derived from real-world cooking scripts. It then leverages a state machine executor that validates plans against the world model and detects immediate precondition violations, latent hazards, and irreversible failures. Experiments across six LLMs show that even frontier models achieve at most 17% error-free plans. Moreover, up to 56% of plans contain latent failures, the majority of which lead to irreversible consequences. We further demonstrate that explicit state reasoning via counterfactual foresight simulation can reduce latent failures by up to 72% and irreversible cases by up to 75%, suggesting a promising direction for more robust LLM planners.

</details>


### 7. From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails

- **Authors:** Yuguang Zhou, Xunguang Wang, Pingchuan Ma, Zhantong Xue, Zhaoyu Wang, Shuai Wang
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14517v1](http://arxiv.org/abs/2606.14517v1)
- **PDF:** [https://arxiv.org/pdf/2606.14517v1](https://arxiv.org/pdf/2606.14517v1)
- **Categories:** cs.CR, cs.AI


> The paper uncovers a new denial‑of‑service vulnerability in LLM‑based guardrails that protect autonomous agents: by inserting carefully crafted natural‑language payloads, an attacker can force the guardrail into excessively long reasoning loops, exhausting compute and inflating latency. The authors introduce two systematic attack frameworks—a beam‑search optimization that uses an LLM proposer and a cheaper mechanism‑aware mutation strategy—to generate payloads that maximize the guardrail’s token consumption, and demonstrate that a single poisoned document can amplify token usage by 13–63 × on eight popular LLM backbones and increase end‑to‑end agent latency by up to 148 × across web, desktop, code, and multi‑agent deployments. These findings highlight that current guardrail designs lack cost‑bounded, reasoning‑robust safeguards, emphasizing the need for new defenses that limit computational overhead while preserving safety.


<details>
<summary>Abstract</summary>

LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is systematically evaluated in two parts. First, in standalone evaluations, the attack generalizes across diverse guardrail architectures, safety templates, and agent benchmarks. Payloads optimized on a single open-source surrogate successfully transfer to eight leading model backbones (e.g., Claude, GPT, Gemini, DeepSeek, and Qwen), achieving a 13--63$\times$ token amplification. Second, in end-to-end real-world agent deployments (web, desktop, code, and multi-agent systems), the attack reveals up to a 148$\times$ latency amplification. We show that a single poisoned document can saturate shared guardrail infrastructures, effectively starving co-located agents and paralyzing the entire system. By uncovering this availability flaw, our work underscores the urgent need to develop cost-bounded, reasoning-robust guardrails.

</details>


### 8. When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More

- **Authors:** Zhongyuan Wang, Pratyusha Vemuri
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14476v1](http://arxiv.org/abs/2606.14476v1)
- **PDF:** [https://arxiv.org/pdf/2606.14476v1](https://arxiv.org/pdf/2606.14476v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution** – The paper shows that LLM‐based agents, when given direct access to a frozen Graph Neural Network (GNN) as a callable tool, almost never exercise judgment: they copy the GNN’s prediction instead of reasoning independently, and this “blind deference” gets stronger as the language model’s size increases.  

**Methodology** – A ReAct‑style LLM agent is coupled with a GNN tool on the node‑classification tasks ogbn‑arxiv and WikiCS. Across multiple random seeds and backbone models (Qwen2.5 0.5 B–7 B), the authors compare the agent’s outputs to the raw GNN, to an oracle that selects the best action per node, and to a simple neighbor‑label baseline, and they evaluate a learned selective‑invocation gate.  

**Key findings** – Agreement with the GNN jumps from 60 % to 98 % as model scale grows, and even the strongest agents are 0.09–0.22 points worse than the oracle, especially on high‑homophily graphs where a neighbor‑label tool outperforms the GNN but the agent still defers. A lightweight gate can recover about half of the gap locally but adds no overall gain, and theoretical bounds suggest that without richer test‑time signals selective invocation cannot be reliably learned. The results caution that tool‑augmented LLM agents do not automatically acquire judgment and that explicit mechanisms are needed to enable selective tool use.


<details>
<summary>Abstract</summary>

A growing line of work equips large language model (LLM) agents with graph neural networks (GNNs) as callable tools, assuming the agent exercises judgment over when and how much to rely on such a tool. We test this directly. We expose a frozen GNN to a ReAct-style LLM agent as an explicit tool and measure, on node classification over a text-attributed graph (ogbn-arxiv, replicated on WikiCS), whether the agent uses the tool or merely obeys it. We find the agent does not exercise judgment: its predictions agree with the raw GNN's 97.6-99.2% of the time (5 seeds), collapsing into a GNN parrot that adopts the tool's output wholesale and bypasses its own reasoning. Sweeping backbone capability (Qwen2.5 0.5B-7B), the deference is not a weak-model artifact: among models able to invoke the tool, agreement rises with capability (0.60 to 0.98 from 1.5B to 7B). Crucially, the cost of deference does not shrink as capability grows and grows where alternatives emerge: a per-node oracle over the available actions beats the parrot by 0.09-0.18 at 3B and 0.12-0.22 at 7B, roughly doubling at high homophily, because the parrot is pinned to the frozen GNN while the agent's alternatives improve; at 7B a simple neighbour-label tool overtakes the GNN at high homophily (0.81 vs 0.71) yet the agent still defers. A simple selective-invocation gate recovers about half of that high-homophily gap (0.71 to 0.83) but yields no net global gain, and held-out estimates bound the best achievable gate over standard test-time features to at most a third of the oracle headroom: reliable selective invocation looks limited by available information, not merely router design. Our results are a cautionary measurement: evaluations of agent+tool systems cannot assume the agent adds judgment on top of the tool, and selective invocation must be designed in rather than expected to emerge from scale.

</details>


### 9. tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration

- **Authors:** Minseo Kim
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14445v1](http://arxiv.org/abs/2606.14445v1)
- **PDF:** [https://arxiv.org/pdf/2606.14445v1](https://arxiv.org/pdf/2606.14445v1)
- **Categories:** cs.SE, cs.AI, cs.HC


> The paper introduces **tap**, a lightweight, file‑based protocol that lets LLM agents from different providers (e.g., Anthropic’s Claude and OpenAI’s Codex) collaborate on a shared codebase without requiring a common runtime, shared memory, or a central messaging server. tap stores each agent’s messages as markdown files with metadata in separate Git worktrees (Tier 1 file‑communication) and augments them with optional real‑time notifications (Tier 2); the design guarantees that messages remain recoverable even if the notification channel fails. In a 27‑day self‑development experiment, tap enabled 209 pull‑requests and 717 artifacts, and heterogeneous Claude‑Codex pairs produced defect‑or‑change reviews in 69.8 % of cases—significantly higher than the 53.1 % achieved by homogeneous pairs—demonstrating that the protocol robustly supports cross‑vendor agent collaboration and enriches review perspectives.


<details>
<summary>Abstract</summary>

Existing multi-agent software development systems have proposed many forms of agent collaboration, including role-based collaboration and automated code review. However, many systems assume a common runtime, a central conversation server, or the same API family. Under these assumptions, LLM agents from different vendors cannot easily exchange messages directly from their own execution environments while dividing development and review work on a shared codebase. This paper presents tap, a file-based collaboration protocol that allows Claude (Anthropic) and Codex (OpenAI) to collaborate on one codebase without shared memory or an identical runtime. The core of tap is a file-first design that preserves markdown files with metadata as original messages, combines a file inspection path (file communication, Tier 1) with real-time notification paths for Claude and Codex (real-time communication, Tier 2), and isolates work through separate git worktrees. Even if real-time notification fails or a receiver restarts, the message file remains available and the same content can be inspected again. In a 27-day, 37-generation self-applied operation where tap was used to develop and review itself, we collected 209 tap-related pull requests and 717 operational artifacts. An analysis of 375 review artifacts showed that the share of reviews recording at least one defect or requested change was 69.8% for heterogeneous model pairs and 53.1% for homogeneous model pairs. These results show that tap, which combines file-based message preservation with real-time notification, operates in a real production repository, and that combining heterogeneous models and execution environments can broaden review perspectives. tap is distributed as the open-source npm package @hua-labs/tap (v0.5.2).

</details>


### 10. Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar Environments

- **Authors:** Mykola Vysotskyi, Runqi Lin, Grzegorz Biziel, Michal Zakrzewski, Sebastian Montagna, Damian Rynczak, Shreyansh Padarha, Kumail Alhamoud, Zihao Fu, William Lugoloobi, Kai Rawal, Hanna Yershova, Xander Davies, Taras Rumezhak, Guohao Li, Fazl Barez, Baoyuan Wu, Arkadiusz Drohomirecki, Yarin Gal, Chris Russell, Christopher Summerfield, Adam Mahdi, Volodymyr Karpiv, Philip Torr, Adel Bibi
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14397v1](http://arxiv.org/abs/2606.14397v1)
- **PDF:** [https://arxiv.org/pdf/2606.14397v1](https://arxiv.org/pdf/2606.14397v1)
- **Categories:** cs.LG


> This paper introduces **GauntletBench**, a web‑based evaluation suite that stresses agentic AI on three underexplored capabilities—temporal perception, graphical understanding, and 3D reasoning—through 100 vision‑intensive tasks drawn from five professional domains (video editing, workflow building, 3D modelling, flight analysis, circuit design). The authors build a modular pipeline compatible with both open‑ and closed‑source agents and automatically score performance across diverse metrics; experiments show that even the strongest state‑of‑the‑art agents succeed on only ≈ 19 % of the tasks, far below the > 80 % success achieved by non‑expert humans. The results highlight a substantial gap between current agent generalisation and the demands of complex, real‑world applications, calling for broader benchmark design in the agentic AI field.


<details>
<summary>Abstract</summary>

As agentic systems continue to evolve and are widely deployed in real-world scenarios, there is a growing demand to faithfully evaluate their capabilities. However, current benchmarks are typically built on popular applications with relatively simple tasks and focus on a narrow set of capabilities while overlooking broader dimensions, resulting in saturated performance on modern agents and failing to probe their limitations. To this end, we introduce GauntletBench, a web-based benchmark for evaluating agent generalisation in challenging scenarios, focusing on three underexplored capabilities (temporal perception, graphical understanding, and 3D reasoning), across five less-covered professional applications (Video Editor, Workflow Builder, 3D Modeller, Flight Analyser, and Circuit Designer), each with 20 vision-intensive tasks (100 in total). Our benchmark provides a modular pipeline that comprises an environment compatible with both open- and closed-source agent frameworks, a controlled web-based application, a well-structured task suite, and an automated evaluation engine with diverse metrics. Contrary to widespread expectations, our empirical results reveal that frontier agentic systems remain far from achieving human-level performance. Even the state-of-the-art agent achieves only a 19.1% success rate on our GauntletBench, highlighting the limitations in these overlooked capabilities and generalisation. By comparison, non-expert human annotators achieve over 80% success on our challenging yet feasible tasks, revealing the substantial gap between current agent capabilities and those required for complex real-world scenarios.

</details>


### 11. Communication Policy Evolution for Proactive LLM Agents

- **Authors:** Xinbei Ma, Jiyang Qiu, Yao Yao, Zheng Wu, Yijie Lu, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng Zhang, Hai Zhao
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14314v1](http://arxiv.org/abs/2606.14314v1)
- **PDF:** [https://arxiv.org/pdf/2606.14314v1](https://arxiv.org/pdf/2606.14314v1)
- **Categories:** cs.AI


> The paper introduces **Communication Policy**, a formal framework that defines how large‑language‑model (LLM) agents should choose between textual dialogue and structured UI interactions to bridge the information asymmetry with users or planners. By evaluating these policies across varied tasks, personas, and model pairings, the authors show that text messages boost raw task performance while UI‑driven prompts improve response quality and persona adherence, and a hybrid strategy leverages both strengths. They further present **Communication Policy Evolution (CPE)**, a self‑evolving, prompt‑only method that iteratively refines an agent’s policy through rollouts, achieving state‑of‑the‑art success rates without any model re‑training, thereby highlighting communication strategy as a pivotal, under‑studied design lever for proactive AI agents.


<details>
<summary>Abstract</summary>

LLM agents have rapidly evolved into autonomous systems, yet a persistent information gap remains between users and agents: communication is costly, while users' identical preferences further limit information exchange. To investigate how agents should communicate across modalities, this paper formalizes Communication Policy, establishes textual and UI-based policies, and then evaluates communication policies across diverse environments, personas, and model combinations. Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor. Experimental results reveal complementary strengths between interaction channels: text-based interaction often facilitates task performance, while structured UI improves agents' response quality and persona compliance. Motivated by that, a hybrid method combines these advantages. We further propose Communication Policy Evolution (CPE), a self-evolution framework for refining communication policies through rollout and prompt-level evolving. Without model modification, CPE achieves the best task success across multiple settings using prompt refinement alone. Our findings identify communication behavior as a critical yet underexplored design dimension for LLM agents.

</details>


### 12. Retrospective Progress-Aware Self-Refinement for LLM Agent Training

- **Authors:** Xinbei Ma, Congmin Zheng, Jiyang Qiu, Jiale Hong, Yao Yao, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng Zhang, Hai Zhao
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14302v1](http://arxiv.org/abs/2606.14302v1)
- **PDF:** [https://arxiv.org/pdf/2606.14302v1](https://arxiv.org/pdf/2606.14302v1)
- **Categories:** cs.CL


> The paper introduces **RePro** (Retrospective Progress‑Aware Training), a new paradigm for teaching large‑language‑model (LLM) agents to generate their own progress signals rather than relying solely on step‑wise reward signals.  RePro first uses a short “retrospection warm‑up” phase where the model learns to reflect on completed trajectories from a few external demonstrations, then continues training with a forward‑then‑reflect rollout (RePro‑PO) that rewards the agent for producing self‑evaluated progress annotations after each episode.  Across three long‑horizon benchmarks (WebShop, ALFWorld, Sokoban), RePro consistently boosts the Qwen‑family agents, delivering up to 12 percentage‑point absolute improvements in task success, thereby demonstrating that retrospective self‑reflection can endow LLM agents with metacognitive awareness and better long‑term planning.


<details>
<summary>Abstract</summary>

LLM-based agents trained with reinforcement learning optimize step-wise action prediction but lack metacognitive awareness of task progress, inducing a gap that hinders long-horizon scaling. A pilot study reveals that online progress prompting hurts performance while retrospective demonstrations help, yet this capability cannot emerge from outcome-reward training alone. We present RePro, Retrospective Progress-Aware Training, a framework that trains agents to self-generate progress signals via a forward-then-reflect rollout paradigm: the agent executes actions online, then retrospectively reassesses its step-wise progress given the completed trajectory and known outcome. RePro initializes with a Retrospection Warmup that teaches reflection format from minimal external demonstrations, then further trains through RePro-PO with a composite reward that produces self-generated signals without continuous external supervision. Experiments on WebShop, ALFWorld, and Sokoban show that RePro enhances the Qwen family's performance, with up to $12\%$ absolute success rate gains.

</details>


### 13. HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

- **Authors:** Tingyang Chen, Shuo Lu, Kang Zhao, Weicheng Meng, Hanlin Teng, Tianhao Li, Chao Li, Xule Liu, Jian Liang, Zhizhong Zhang, Yuan Xie, Heng Qu, Kun Shao, Jian Luan
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14249v1](http://arxiv.org/abs/2606.14249v1)
- **PDF:** [https://arxiv.org/pdf/2606.14249v1](https://arxiv.org/pdf/2606.14249v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **HarnessX**, a modular “foundry” that lets developers construct, adapt, and evolve the runtime harness (prompts, tools, memory, control flow) of AI agents through a typed substitution algebra and a trace‑driven evolution engine (AEGIS), thereby closing the loop between agent execution traces, harness refinement, and model training.

**Methodology:** HarnessX composes harness primitives via a formal algebra, uses AEGIS to iteratively improve them by mirroring symbolic adaptations with reinforcement‑learning updates based on execution traces, and incorporates the resulting trajectories both as harness updates and as additional training signal for the underlying language model.

**Key findings:** On five diverse benchmarks (ALFWorld, GAIA, WebShop, τ³‑Bench, and SWE‑bench Verified), HarnessX boosts agent performance by an average of **+14.5 %** (with up to **+44 %** gains on the weakest baselines), demonstrating that systematic, evolvable harness design can significantly advance agentic AI without relying solely on model scaling.


<details>
<summary>Abstract</summary>

AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness-model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, tau^3-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever. The complete codebase will be open-sourced in a future release.

</details>


### 14. SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing

- **Authors:** Haowen Gao, Haoran Chen, Can Wang, Shasha Guo, Liang Pang, Zhaoyang Liu, Huawei Shen, Xueqi Cheng
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14239v1](http://arxiv.org/abs/2606.14239v1)
- **PDF:** [https://arxiv.org/pdf/2606.14239v1](https://arxiv.org/pdf/2606.14239v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **SkillAudit**, a ground‑truth‑free framework that lets frozen LLM agents evolve their procedural “skill” packages during deployment by comparing the agent’s behavior with and without a candidate skill.  

**Methodology:** SkillAudit repeatedly runs paired trajectories on the same task, uses the **Process‑Aligned Contrastive Evaluation (PACE)** suite to turn observed behavioral divergences into fine‑grained diagnostics linked to specific skill passages, and employs a pre‑compiled structural verifier to reject edits that violate task constraints; edits are channeled through a *Refine* path (filtering noisy guidance) or a *Repair* path (replacing conflicting passages).  

**Key Findings:** Across 89 containerized tasks in eight professional domains, SkillAudit raises the average task reward to **73.9 %**, surpassing both a skill‑less baseline (40.9 %) and the original static expert skill (56.7 %), all without any hidden test scores, reference solutions, or external reward signals.


<details>
<summary>Abstract</summary>

Agent skills are structured procedural packages that guide frozen LLM agents in specialized workflows. Skills rarely remain sufficient after deployment: edge cases, API changes, and deployment constraints become visible only through use, making skill evolution a practical necessity. Existing methods depend on privileged feedback such as held-out validation scores, hidden test outcomes, or environment rewards -- signals often unavailable when a practitioner has only a task description and workspace data. We introduce SkillAudit, a framework for evolving agent skills without ground-truth feedback. The key idea is paired trajectory auditing: at each iteration, the same task is executed with and without the candidate skill, isolating how the skill changes agent behavior without external labels. To turn behavioral differences into edit guidance, SkillAudit uses Process-Aligned Contrastive Evaluation (PACE), a cluster of evaluators that maps trajectory divergences to diagnostic signals linked to specific passages in the skill document. A structural verifier, compiled once from the task specification and then fixed, checks task constraints and rolls back harmful updates. SkillAudit routes edits through two pipelines: Refine removes noisy or irrelevant guidance from broadly useful skills, while Repair replaces passages that conflict with the task. Across 89 containerized tasks spanning 8 professional domains, SkillAudit achieves 73.9% average task reward, outperforming an agent without skills (40.9%) and the static expert skill (56.7%). These gains are obtained without accessing hidden tests, reference solutions, or external scoring functions during evolution.

</details>


### 15. Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime

- **Authors:** Taewoo Park, Kyeonghyun Yoo, Seunghyun Yoo, Hwangnam Kim
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14219v1](http://arxiv.org/abs/2606.14219v1)
- **PDF:** [https://arxiv.org/pdf/2606.14219v1](https://arxiv.org/pdf/2606.14219v1)
- **Categories:** cs.RO, cs.AI


> **Contribution**  
The paper introduces **Persistent Mission Runtime (PMR)**, a UAV autonomy framework that keeps routine flight control and safety checks on‑board while invoking an external, agentic reasoning service only when a recovery is needed. A key novelty is the **learned Cognitive Value of Invocation (learned‑CVI)** gate, which predicts when remote agentic reasoning will be worth its latency and resource cost.

**Methodology**  
PMR maintains a local execution loop that monitors waypoint progress and safety; upon detecting blockage, stagnation, or mission ambiguity it queries a cloud‑based agentic reasoner that selects from a library of predefined “recovery skills.” The returned plan is parsed, formally verified, safety‑filtered, and translated into low‑level commands. The learned‑CVI model—trained on simulation data—acts as an admission filter that decides, on a per‑step basis, whether to invoke the remote agent.

**Findings**  
In a 400‑run Gazebo/PX4 benchmark covering eight challenging scenarios, PMR with learned‑CVI raises the success rate in hard/ambiguous situations from **5 % (local‑only)** to **95 %**, beating one‑shot and periodic reasoning baselines by **20 %** and **32.5 %** respectively. Compared with a manually tuned rule‑based invocation strategy, it cuts remote‑agent calls by **16.7 %** and reduces token usage by **29.2 %**, demonstrating that selective, value‑driven agentic recovery can dramatically improve UAV autonomy while keeping operational overhead low.


<details>
<summary>Abstract</summary>

Agentic AI can support unmanned aerial vehicle (UAV) autonomy by providing high-level recovery reasoning when local waypoint- or setpoint-based execution encounters blocked passages, repeated no-progress behavior, or mission-level ambiguity. On physical UAVs, however, remote reasoning is most useful when it is invoked selectively, since each call introduces latency, resource cost, backend uncertainty, and a need to validate the returned decision. This paper presents Persistent Mission Runtime (PMR), a UAV recovery framework that keeps the mission loop and safety-critical execution local while using an external agentic reasoner only as an on-demand recovery module. The reasoner selects from predefined recovery skills, and each returned decision is parsed, verified, safety-filtered, and mapped to local executor actions before it can affect flight. PMR introduces learned Cognitive Value of Invocation (learned-CVI), a compact admission gate that estimates when remote agentic reasoning is likely to improve near-term mission progress enough to justify its operational cost. Across a fixed 400-run Gazebo/PX4 benchmark with eight scenarios, learned-CVI raises hard/ambiguous-regime success from 5.0% under local-only autonomy to 95.0%, outperforms one-shot and periodic reasoning baselines by 20.0 and 32.5 percentage points, and reduces remote-agent calls by 16.7% and logged tokens by 29.2% relative to a manually tuned rule-based invocation baseline.

</details>


### 16. Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL

- **Authors:** Yinglun Zhu
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14211v1](http://arxiv.org/abs/2606.14211v1)
- **PDF:** [https://arxiv.org/pdf/2606.14211v1](https://arxiv.org/pdf/2606.14211v1)
- **Categories:** cs.AI, cs.LG


> **Contribution:** The paper identifies a “reflection gap” in LLM‑based agents—systematic mis‑calibration between an agent’s self‑assessment and the actual outcome after receiving environment feedback—and proposes a lightweight fix, **RefGRPO**, that adds a free calibration bonus to standard RL updates.

**Methodology:** RefGRPO augments the RL objective with a term that directly compares the agent’s own reflection (its confidence or self‑evaluation) to the observed result, requiring no extra reward model, judge LLM, or human labels, and schedules the bonus’s weight dynamically during training.

**Key Findings:** Across five text‑to‑SQL benchmarks, RefGRPO substantially narrows the reflection gap (under‑confidence drops from 44.4 % to 7.7 %) while also boosting task accuracy (from 75.1 % to 76.5 %). The calibrated self‑reflection enables the agent to act as its own verifier, supporting self‑improvement via pseudo‑rewards and selective prediction at test time.


<details>
<summary>Abstract</summary>

LLMs are increasingly deployed as agents that interact with external environments and observe feedback such as execution results, error messages, and tool outputs. A well-functioning agent should be able to leverage this feedback to accurately assess its own performance. Yet we find a persistent reflection gap: LLM agents tend to mis-assess their own outputs after observing concrete environment feedback -- even for questions they correctly answered -- and standard RL barely helps due to a credit-assignment mismatch. To close this gap, we propose RefGRPO, a simple yet effective fix that augments standard RL algorithms with two key ingredients: a free calibration bonus computed by contrasting the agent's own reflection with the actual outcome (requiring no additional reward model, LLM judge, or external annotation), and a dynamic schedule on its coefficient. Compared to standard RL baselines, our method simultaneously improves reflection calibration (e.g., reduces underconfidence rate $44.4\% \to 7.7\%$) and task accuracy (e.g., $75.1\% \to 76.5\%$) on text-to-SQL across five benchmarks. The resulting calibrated reflection turns the agent into its own verifier grounded in environment feedback, which further enables (i) better self-improvement that uses reflections as pseudo-rewards without outcome supervision, and (ii) more effective test-time selective prediction by committing only to rollouts flagged as correct.

</details>


### 17. When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms

- **Authors:** Yihan Xia, Taotao Wang
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14200v1](http://arxiv.org/abs/2606.14200v1)
- **PDF:** [https://arxiv.org/pdf/2606.14200v1](https://arxiv.org/pdf/2606.14200v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution** – The paper introduces *skill‑conditional reputation* R(i | k), a trust score that is specific to each agent‑skill pair, and rigorously delineates when this finer‑grained trust is advantageous over a single global score. It also uncovers a dual‑use risk: the same cross‑skill evidence‑borrowing that makes conditional trust data‑efficient can be exploited as a laundering channel for reputation attacks.  

**Methodology** – Using a theoretical phase‑diagram analysis the authors identify the regime where conditional trust outperforms global trust (high heterogeneity of agents, sparse per‑skill observations, and correlated skills), and then validate these predictions on a public AppWorld benchmark containing 14 heterogeneous LLM agents. They devise a *Conditional Information Value Test* (CIVT) to flag low‑evidence conditions, and construct an adversarial scenario where an attacker injects cheap evidence for a “donor” skill to corrupt the conditional router for a target skill.  

**Key findings** – Real‑world agent pools fall inside the beneficial regime, yielding a modest but measurable routing improvement (the per‑skill best agent changes across skills). However, the same cross‑skill borrowing enables an attacker to raise routing regret from 0 to 0.94 while the naïve global trust metric remains superficially healthy (‑0.06 → +0.19). A zero‑evidence gate mitigates but does not fully eliminate the attack, and the authors quantify the residual risk‑vs‑budget trade‑off, highlighting a critical security consideration for agentic AI systems that employ conditional trust.


<details>
<summary>Abstract</summary>

Open platforms increasingly route tasks among heterogeneous LLM agents--differing in base model, scaffold, and tool stack--whose competence varies sharply by skill: an agent excellent at one skill may be useless at another. The standard reputation approach summarizes each agent by a single global trust score, but that scalar is the wrong object here, because routing every task to the globally most-trusted agent leaves the value of specialization unclaimed. We study skill-conditional trust R(i | k)--the trust to place in agent i for a task requiring skill k, rather than one score per agent--and pose three falsifiable questions: when is conditioning worth it, how much cross-skill evidence should be borrowed, and whether that borrowing is safe. A controlled phase-diagram analysis answers the first two: conditional trust wins only in a specific regime--high agent heterogeneity, sparse per-skill evidence, and correlated skills--and the coupling strength beta that buys this data efficiency is dual-use, because the same cross-skill borrowing is also a laundering channel. On a public benchmark of 14 genuinely heterogeneous AppWorld agents, real pools land inside the beneficial regime--a small but genuine gain, with the per-skill best agent genuinely changing across skills. We then show that an attacker with cheap evidence in one skill and none in a target skill hijacks the conditional router, driving routing regret from 0 to 0.94 on a pool our zero-cost Conditional Information Value Test (CIVT) rates GREEN--while the ungated trust verdict it contaminates reads -0.06 instead of the honest +0.19. A zero-evidence gate bounds the attack but does not eliminate it; we characterize the residual cost under an explicit budget. We do not claim Sybil-resistance--we quantify the trade-off.

</details>


### 18. Graph-based Target Back-Propagation for Context Adaptation in Multi-LLM Agentic Systems

- **Authors:** Tan Zhu, Tong Yao, Kananart Kuwaranancharoen, Amit Singh, Yushang Lai, Deepa Mohan, Shankara Bhargava
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14155v1](http://arxiv.org/abs/2606.14155v1)
- **PDF:** [https://arxiv.org/pdf/2606.14155v1](https://arxiv.org/pdf/2606.14155v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces **Graph‑based Target Back‑Propagation (GTBP)**, a novel context‑adaptation framework for multi‑LLM agentic pipelines that are represented as directed acyclic graphs. GTBP works by back‑propagating task‑level target outputs through the workflow graph and using the resulting target‑output mismatches to update each stage’s prompt in a staged, gradient‑free manner; the authors prove that these updates converge to a stable set of prompts and that, assuming a sufficiently powerful LLM optimizer, the overall objective can be monotonically reduced. Experiments on three multi‑LLM benchmarks show that GTBP achieves consistently higher task performance than existing adaptation methods while keeping computational overhead on par with baseline approaches.


<details>
<summary>Abstract</summary>

Context adaptation automates prompt engineering in LLM-based systems by iteratively revising tunable prompts from task feedback, without modifying model weights. Extending this paradigm to multi-LLM agentic systems is crucial: existing methods suffer from inaccurate credit assignment and lack convergence guarantees. We propose \textbf{G}raph-based \textbf{T}arget \textbf{B}ack-\textbf{P}ropagation (GTBP), a context adaptation framework for agentic workflows modeled as directed acyclic graphs. GTBP propagates local target outputs backward through the workflow graph and uses target--output discrepancies to guide a stage-wise prompt update mechanism. Theoretically, we show that GTBP's stage-wise prompt updates become stable over iterations, and that a sufficiently capable LLM optimizer can decrease the overall objective. Empirically, GTBP consistently outperforms strong baselines across three benchmarks while maintaining comparable computational cost.

</details>


### 19. Trust but Verify: Mitigating Medical Hallucinations via Post-Hoc Adversarial Auditing and Multi-Agent Feedback Loops

- **Authors:** Muhammad Osama, Maheera Amjad, Zartasha Mustansar, Arslan Shaukat, Muhammad U. S. Khan
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14149v1](http://arxiv.org/abs/2606.14149v1)
- **PDF:** [https://arxiv.org/pdf/2606.14149v1](https://arxiv.org/pdf/2606.14149v1)
- **Categories:** cs.LG


> The paper introduces a model‑agnostic “Trust but Verify” architecture that wraps a single LLM backbone with five cooperating agents to audit and correct its clinical recommendations in real time. By testing three open‑access LLM families on a specially crafted adversarial benchmark of 103 multiple‑choice questions whose historically correct answers now refer to banned drugs, the authors show that the multi‑agent loop cuts the Hallucination Error Rate by roughly 53 % (shifting unsafe pointwise scores from –0.25 toward 0.0) while preserving answer fidelity. These results demonstrate that post‑hoc adversarial auditing and multi‑agent feedback can reliably enforce up‑to‑date regulatory constraints on medical LLMs, offering a practical safety layer for deploying agentic AI in healthcare.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are increasingly deployed in healthcare settings, yet their tendency to hallucinate poses risks when clinical decisions are involved. This study examine whether LLMs recommend recently banned or withdrawn pharmaceuticals when answering clinical questions and tests an agent-based method for reducing such errors. We developed a five-agent "Trust but Verify" system using a single LLM backbone. To measure regulatory knowledge obsolescence, we created an adversarial dataset of 103 clinical MCQs where historically correct answers now refer to banned substances. This scale ensures statistical significance across various therapeutic classes. We evaluated three open-access model families (GPT-OSS, Llama-3, Falcon-3) under vanilla and agentic conditions. Performance was measured via pointwise score, label accuracy, Hallucination Error Rate (HER), and Component Fidelity (CF) score. We also observed clinical safety regression in proprietary models. In default configurations, all models showed high hallucination rates, consistently selecting banned drugs that matched training data patterns. Our proposed agentic architecture reduced HER by approximately 53% across models. Pointwise scores shifted from -0.25 (unsafe recommendation) toward 0.0 (appropriate refusal). The safety audit intercepted dangerous outputs even when models' parametric knowledge favored the banned substance. The proposed multi-agent framework offers a model-agnostic method for enforcing regulatory compliance that prioritizes patient safety over fluent text generation. Our work demonstrates a practical approach for deploying autonomous AI systems in safety-critical healthcare settings. It shows how real-time regulatory data can be integrated into LLM pipelines to support clinical decision-making.

</details>


### 20. Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning

- **Authors:** Omar Adalat, Edwin Hamel-De le Court, Francesco Belardinelli
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14130v1](http://arxiv.org/abs/2606.14130v1)
- **PDF:** [https://arxiv.org/pdf/2606.14130v1](https://arxiv.org/pdf/2606.14130v1)
- **Categories:** cs.LG, cs.MA


> The paper introduces a contract‑based compositional shielding framework that enables **deterministic safety guarantees for decentralized multi‑agent reinforcement learning** while still allowing agents to achieve team‑optimal performance. The method lets each agent pick, via a non‑stationary multi‑armed bandit, a local LTLₛₐ𝚏𝚎 obligation from a pre‑computed library; the selected tuple of obligations is jointly certified to satisfy the global safety specification, and the resulting local action masks are used at runtime without any central controller. Experiments on six benchmark environments and fifteen algorithmic variants show that the approach preserves end‑to‑end safety and recovers the optimal safe joint policy that would be lost under naïve decentralized shields.


<details>
<summary>Abstract</summary>

Safe coordination problems surface in multi-agent reinforcement learning when global safety cannot be enforced by any agent unilaterally: the admissibility of one agent's action may depend on the dynamics of other agents. Decentralised shields can enforce safety at runtime, but purely factorised permissions often exclude optimal team behaviour that is safe only through coordination. We study deterministic safety guarantees for agents trained and deployed under decentralised execution, recovering team-optimal safe behaviour without centralised runtime control. Agents have a shared global specification $φ$ in the safety fragment of Linear Temporal Logic ($\mathsf{LTL}_{\mathsf{safe}}$ ), and select among tuples of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations whose conjunction implies the global specification $φ$. Each agent may rely on the other agents' local obligations as assumptions because the whole contract tuple is certified simultaneously and allows projection into local action masks. At learning time, a non-stationary multi-armed bandit chooses among a library of local $\mathsf{LTL}_{\mathsf{safe}}$ obligations to select the tuple that optimises team reward, all without forgoing end-to-end safety. We evaluate the approach across 6 environments and 15 algorithmic variants.

</details>


### 21. Same-Origin Policy for Agentic Browsers

- **Authors:** Xilong Wang, Xiaoxing Chen, Patrick Li, Dawn Song, Neil Gong
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.14027v1](http://arxiv.org/abs/2606.14027v1)
- **PDF:** [https://arxiv.org/pdf/2606.14027v1](https://arxiv.org/pdf/2606.14027v1)
- **Categories:** cs.CR, cs.AI, cs.CL, eess.SY


> The paper reveals that the classic Same‑Origin Policy (SOP), which blocks unauthorized cross‑origin data flows in traditional browsers, is routinely broken by current “agentic browsers” that embed autonomous AI agents capable of issuing scripted web actions. By building SOPBench—a suite of benign and adversarial tasks that probe cross‑origin leaks—the authors show that existing agentic browsers frequently bypass SOP, and they introduce SOPGuard, a lightweight enforcement layer that monitors and constrains the agent’s automated actions to respect origin boundaries. Integrated into the open‑source BrowserOS, SOPGuard eliminates the observed violations with only minimal runtime overhead, demonstrating that SOP can be restored in agentic environments without sacrificing their utility.


<details>
<summary>Abstract</summary>

Agentic browsers integrate autonomous AI agents into web browsers, enabling users to accomplish web tasks through natural-language instructions. The same-origin policy (SOP) is a fundamental browser security mechanism that prevents unauthorized automated cross-origin data flows induced by scripts. However, whether SOP remains effective in agentic browsers is an open question that has not been systematically studied. In this work, we bridge this gap. We first observe that an agentic browser can itself serve as an automated channel for cross-origin data flows, potentially leading to SOP violations. To investigate this phenomenon, we construct SOPBench, a benchmark for evaluating SOP violations in agentic browsers. Our evaluation shows that existing agentic browsers frequently violate SOP, both in benign settings and under attacks. To address this problem, we propose SOPGuard, an SOP enforcement mechanism tailored to agentic browsers. We implement SOPGuard in BrowserOS, an open-source agentic browser. Extensive evaluations demonstrate that SOPGuard effectively enforces SOP while preserving utility and incurring only a small runtime overhead. Our code and data are available at https://github.com/wxl-lxw/BrowserOS-SOPGuard.

</details>


### 22. Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH

- **Authors:** Vikhyath Kothamasu, Virginia Smith, Chhavi Yadav
- **Published:** 2026-06-12
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13994v1](http://arxiv.org/abs/2606.13994v1)
- **PDF:** [https://arxiv.org/pdf/2606.13994v1](https://arxiv.org/pdf/2606.13994v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> The paper introduces **DeCompBench**, the first benchmark explicitly designed to probe LLM‑based agents for vulnerability to **decomposition attacks**—scenarios where a malicious goal is split into a sequence of apparently benign subtasks that bypass existing safety filters. Using a graph‑based workflow generator and a custom “decomposer” to create realistic multi‑step attack traces, the authors evaluate several state‑of‑the‑art agent architectures and find that while these agents reliably refuse monolithic harmful requests, their refusal rates drop dramatically on the decomposed versions, often completing the overall malicious objective. The results demonstrate a critical blind spot in current agent safety evaluations and provide a publicly released dataset (huggingface.co/datasets/decompositionbench/DeCompBench) for developing and testing defenses against this emerging threat.


<details>
<summary>Abstract</summary>

LLM-based Agents are becoming increasingly capable and widely deployed, creating growing incentives for adversarial misuse in the real-world. A key emerging threat is Decomposition Attacks \cite{glukhov2024breach, jones2024adversaries} in which a harmful task is broken into simpler, benign subtasks that evade safety mechanisms when executed separately but cumulatively fulfill the malicious intent. Although recent benchmarks assess agent safety in multi-turn and multi-tool-use settings, they do not explicitly capture this form of decompositional misuse and may not represent realistic adversarial execution flows. To this end, we introduce DeCompBench, a benchmark designed specifically to evaluate agentic safety under decomposition attacks. DeCompBench is created with a decomposition-by-design principle using a graphical framework and enables harmful task decomposition into individually benign and executable subtasks with realistic workflows. Our experiments using a custom decomposer show that state-of-the-art agents exhibit high refusal rates on monolithic harmful tasks, but significantly lower refusal rates on their decomposed variants, while often inadvertently fulfilling the adversarial objectives. These findings underscore the need for safety evaluations against decomposition attacks and corresponding defenses. Our dataset is publicly available and can be found at https://huggingface.co/datasets/decompositionbench/DeCompBench.

</details>


### 23. Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization

- **Authors:** Hexuan Yu, Chaoyu Zhang, Heng Jin, Shanghao Shi, Ning Zhang, Y. Thomas Hou, Wenjing Lou
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13949v1](http://arxiv.org/abs/2606.13949v1)
- **PDF:** [https://arxiv.org/pdf/2606.13949v1](https://arxiv.org/pdf/2606.13949v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **MINIM**, a client‑side broker that sanitizes UI observations before they are sent to remote LLM agents, aiming to prevent leakage of sensitive but unnecessary information while keeping the data needed for task execution.

**Methodology:** MINIM implements a Contextual‑Integrity‑inspired framework that learns two scores for every UI element—a *sensitivity* score (how private the content is) and a *necessity* score (how needed it is for the current task). These scores drive a ternary disclosure policy (keep, abstract, drop) and are optimized with a CI‑aware loss that heavily penalizes necessity errors on high‑sensitivity items.

**Key findings:** On a WebArena‑derived benchmark, MINIM cuts the transmission of task‑irrelevant sensitive data by a large margin (up to ~70 % reduction) while maintaining the semantic context and affordances required for the agent to act correctly, demonstrating that aggressive, privacy‑aware pruning is feasible without degrading autonomous agent performance.


<details>
<summary>Abstract</summary>

Modern LLM-powered autonomous agents increasingly rely on rich user interface (UI) state observations to achieve reliable action grounding in complex digital environments. However, many deployments transmit the full UI state to remote inference servers even when most elements are irrelevant to the current task, which can leak sensitive but unnecessary context such as authentication codes, private notifications, and background application states. We propose MINIM, a trusted local broker that performs privacy-aware minimization on the client side before any observation leaves the device. Grounded in Contextual Integrity (CI), MINIM learns a dual-score representation for each UI element by predicting an inherent sensitivity score (s) and a task-conditioned necessity score (n). These scores drive a ternary disclosure policy that keeps essential elements, abstracts sensitive attributes when needed, and removes task-irrelevant content. We optimize a CI-aware objective that penalizes necessity errors more strongly on high-risk content, enabling aggressive pruning while preserving task-critical information. Experiments on real-world UI observations derived from WebArena show that MINIM substantially reduces task-irrelevant sensitive leakage while preserving task-critical semantic context and the interactive affordances required for reliable agent actions.

</details>


### 24. MedLatentDx: Latent Multi-Agent Communication for Cross-Hospital Rare-Disease Diagnosis

- **Authors:** Ziqing Wang, Lili Zhao, Kaize Ding
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13945v1](http://arxiv.org/abs/2606.13945v1)
- **PDF:** [https://arxiv.org/pdf/2606.13945v1](https://arxiv.org/pdf/2606.13945v1)
- **Categories:** cs.CL


> **MedLatentDx** proposes a privacy‑preserving multi‑agent system for rare‑disease diagnosis across hospitals. Rather than exchanging raw clinical text, each hospital‑bound LLM agent retains patient records locally and transmits only compact latent key‑value (KV) blocks to a central host agent; the framework offers (1) KV‑distillation for agents that share the same backbone model and (2) cross‑family latent alignment for heterogeneous backbones. Experiments on the newly created CrossRare‑Bench (a large, hospital‑partitioned rare‑disease dataset) show that MedLatentDx yields higher cross‑hospital diagnostic accuracy than baselines that share raw latent states, while markedly lowering the amount of reconstructible clinical information, thereby advancing agentic AI approaches that balance collaboration and privacy.


<details>
<summary>Abstract</summary>

Rare diseases affect over $300$ million patients across more than $7{,}000$ conditions, yet no single hospital encounters enough cases of any one condition for reliable diagnosis. Cross-hospital collaboration could help by allowing a diagnosing institution to use distributed, case-specific diagnostic evidence, but privacy regulations restrict the transmission of identifiable clinical text across institutional boundaries. This setting raises two challenges: existing medical agent systems often rely on textual evidence exchange, while raw latent states such as hidden states and KV caches may still reveal prompt-derived clinical content. We introduce MedLatentDx, a latent multi-agent communication framework in which hospital agents keep private clinical records and retrieved cases local, and send compact latent KV blocks to a host agent for rare-disease diagnosis. MedLatentDx supports two deployment settings: same-backbone hospital agents use latent KV distillation, while hospitals with different LLM backbones use cross-family latent alignment. On CrossRare-Bench, a self-built large-scale rare-disease benchmark with hospital-level partitions, MedLatentDx improves cross-hospital diagnostic performance while reducing reconstructable clinical content relative to raw-latent communication baselines.

</details>


### 25. A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale

- **Authors:** Ben Torkian, Jun Zhou
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13916v1](http://arxiv.org/abs/2606.13916v1)
- **PDF:** [https://arxiv.org/pdf/2606.13916v1](https://arxiv.org/pdf/2606.13916v1)
- **Categories:** cs.AI


> The paper introduces a multi‑agent AI pipeline that automatically extracts and normalizes high‑school transcripts, addressing the heterogeneous formats that stall college admissions. The system consists of a Pattern‑Recognition Agent (layout parsing), a Semantic‑Analysis Agent (NLP grading interpretation), a Vision‑Intelligence Agent (multimodal OCR), and an Orchestration Agent that uses GPA extraction as a coordination signal to enforce quality control and reconcile outputs. Evaluated on 40 real transcripts from 13 states, the collaborative agents achieve 96.7 % agreement with expert manual reviews while processing each transcript in roughly 45 seconds, demonstrating that coordinated agentic architectures can deliver scalable, high‑accuracy document‑processing capabilities for admission workflows.


<details>
<summary>Abstract</summary>

Each year, college admissions offices face an overwhelming challenge: processing millions of high school transcripts, each with unique formats, grading systems, and layouts. This manual process creates operational bottlenecks that delay admissions decisions and consume valuable resources. We present a transformative solution through a multi-agent AI system where specialized agents collaborate to automatically process diverse transcript formats through intelligent coordination and communication. Our multi-agent architecture consists of three specialized agents-a Pattern Recognition Agent for format-specific parsing, a Semantic Analysis Agent for natural language understanding, and a Vision Intelligence Agent for multimodal document analysis-coordinated by an Orchestration Agent that manages agent communication and result reconciliation. Our key innovation lies in agent-based quality control using GPA extraction as a coordination signal, ensuring reliable agent collaboration and preventing critical information loss. When evaluated on 40 real world transcripts from high schools across 13 U.S. states, our agent system successfully processed every document, achieving 96.7% accuracy compared to expert manual review while maintaining practical processing speeds of 45 seconds per transcript. This work demonstrates how multi-agent coordination can solve complex document processing challenges, offering institutions a scalable, collaborative AI solution that preserves accuracy while dramatically reducing processing time.

</details>


### 26. SANA: What Matters for QA Agents over Massive Data Lakes?

- **Authors:** Austin Senna Wijaya, Jiaxiang Liu, Haonan Wang, Eugene Wu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13904v1](http://arxiv.org/abs/2606.13904v1)
- **PDF:** [https://arxiv.org/pdf/2606.13904v1](https://arxiv.org/pdf/2606.13904v1)
- **Categories:** cs.CL, cs.AI, cs.DB


> **Main contribution:** The paper introduces **SANA (Search Agent Navigation Ablation)**, a diagnostic framework that decomposes the end‑to‑end performance of exploratory question‑answering (EQA) agents over massive data lakes into separate, measurable components—search, planning, data analysis, and the agent’s Action Policy—by generating runtime profiles with gold‑standard source sequences and execution logs.

**Methodology:** SANA rewrites each EQA instance into an “idealized” pipeline where perfect search, planning, or analysis modules can be swapped in; ablating any one module reveals how much of the remaining error is attributable to the agent’s policy. The authors applied SANA to two public EQA benchmarks (LakeQA and KramaBench) and evaluated several lightweight and medium‑scaled agents under controlled prompts, budgets, and runtimes.

**Key findings:** Across both benchmarks, **data‑analysis** is the dominant source of error, while **planning** contributes relatively little. **Search** is a critical bottleneck in the large‑scale LakeQA setting but is less problematic for the smaller KramaBench. Thus, SANA provides a systematic way to pinpoint and compare the weak points of data‑lake QA agents, guiding future research on search and analysis components in agentic AI.


<details>
<summary>Abstract</summary>

Exploratory question answering (EQA) over data lakes requires an LLM agent to discover relevant sources, analyze retrieved data, and adapt its actions based on intermediate results. End-to-end accuracy alone cannot distinguish failures in search, planning, data analysis, or the agent's Action Policy: its decisions about what to do next and when to submit an answer. We present SANA (Search Agent Navigation Ablation framework), a diagnostic ablation framework that transforms EQA tasks into runtime profiles containing gold source sequence, sanitized subquestions, and execution records. SANA uses these profiles to construct idealized search, planning, and data-analysis tools, allowing each component to be ablated; the residual gap is diagnostic evidence for policy failures.
  To illustrate SANA as a reusable evaluation framework, we adapted two recent EQA benchmarks, LakeQA and KramaBench, and evaluated lightweight and mid-sized agents under fixed prompts, budgets, data lakes, and runtimes. Across both benchmarks, data analysis is a consistent bottleneck while planning is less so. Search is a major limitation in LakeQA's large data-lake setting, but less so for the smaller-scale KramaBench. SANA thus deconstructs end-to-end task accuracies into a diagnosis of where data-lake agents fail, and allows for systematic comparisons of progress in search, planning, data analysis, and agent design.

</details>


### 27. Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents

- **Authors:** Laxmipriya Ganesh Iyer, Rahul Suresh Babu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13884v1](http://arxiv.org/abs/2606.13884v1)
- **PDF:** [https://arxiv.org/pdf/2606.13884v1](https://arxiv.org/pdf/2606.13884v1)
- **Categories:** cs.AI


> The paper proposes **Risk‑Aware Causal Gating (RACG)** as a safety primitive for LLM‑driven agents: a gating layer that decides to execute, defer, or abstain from a model’s suggested action based on an estimated **counterfactual risk** rather than raw confidence. By learning a causal model of the action‑outcome pathway and deriving distribution‑free guarantees on the probability of acting under high‑risk conditions, RACG can set operating thresholds that meet user‑specified safety constraints and adapt to distribution shift via monitoring prediction‑outcome mismatches. Experiments on simulated interventions and real‑world decision benchmarks show that RACG dramatically cuts costly errors while retaining most of the ungated utility, outperforming confidence‑based and selective‑prediction baselines at comparable abstention rates, thereby offering a principled, least‑privilege control mechanism for trustworthy, high‑stakes agentic AI.


<details>
<summary>Abstract</summary>

Modern decision systems increasingly rely on learned components whose outputs may be confident yet wrong, exposing downstream actions to costly errors. We introduce Risk-Aware Causal Gating (RACG), a framework that decides whether to act on, defer, or abstain from a model's prediction by combining causal effect estimation with calibrated risk control. RACG models the causal pathway from candidate actions to outcomes and gates each decision according to an estimated counterfactual risk rather than raw predictive confidence. To make gating reliable, we derive distribution-free bounds on the probability of acting under high-risk conditions and show how these bounds translate into operating thresholds that satisfy user-specified safety constraints. We further propose an adaptive gating policy that adjusts to distribution shift by monitoring discrepancies between predicted and realized outcomes, tightening the gate when causal assumptions appear violated. Across simulated interventions and real-world decision benchmarks, RACG reduces high-cost errors substantially while preserving most of the utility of an ungated policy, and it outperforms confidence-based and selective-prediction baselines at matched abstention rates. Our results indicate that explicitly separating causal risk from predictive uncertainty yields decision systems that are both safer and more transparent, offering a principled mechanism for trustworthy automation in high-stakes settings.

</details>


### 28. Temporally Consistent Graph Q-Networks for Intelligent Network Control

- **Authors:** Zacharias Veiksaar, Maxime Bouton
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13848v1](http://arxiv.org/abs/2606.13848v1)
- **PDF:** [https://arxiv.org/pdf/2606.13848v1](https://arxiv.org/pdf/2606.13848v1)
- **Categories:** cs.NI, cs.LG


> The paper introduces **Temporally Consistent Graph Q‑Networks (TC‑GQN)**, a new multi‑agent reinforcement‑learning framework for high‑level control of mobile networks. TC‑GQN builds a task‑independent, self‑predictive graph neural representation of the entire network and uses a single global reward to train decentralized Q‑functions that output coordinated actions for each base‑station. In simulated experiments on coordinated energy‑saving across multiple sectors and carriers, TC‑GQN achieves higher hardware sleep times while respecting QoS constraints than existing graph‑based MARL baselines and a strong rule‑based controller, and its learned encoding allows rapid re‑optimization when objectives change.


<details>
<summary>Abstract</summary>

Mobile networks continue to grow in complexity and next generation networks are expected to support both increasing traffic loads and more diverse services. As network complexity rises, optimizing antenna parameters under dynamic or changing objectives becomes increasingly challenging. We propose a novel multi-agent reinforcement learning (MARL) algorithm for high-level control and orchestration of mobile networks.
  The Temporally Consistent Graph Q-Network (TC-GQN) algorithm learns a self-predicting representation of the whole network that is task-independent and aggregates information from all base-stations. A graph neural network is trained using a global reward function to assign coordinated local actions based on the learned encoding of the global network state. We evaluate the algorithm in a simulated environment to orchestrate an energy-saving feature across multiple sectors and multiple carriers under different quality of service (QoS) constraints. The proposed algorithm outperforms state-of-the-art graph-based baselines and a competitive rule-based controller by improving hardware sleep time while maintaining QoS. Moreover, the learned representation enables rapid adaptation to changing intents.

</details>


### 29. Safety-Contract Graph Multi-Agent Reinforcement Learning for Autonomous Network Security Response

- **Authors:** Jose Luis Lima de Jesus Silva
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13832v1](http://arxiv.org/abs/2606.13832v1)
- **PDF:** [https://arxiv.org/pdf/2606.13832v1](https://arxiv.org/pdf/2606.13832v1)
- **Categories:** cs.MA, cs.AI, cs.CR, cs.LG


> The paper introduces a **Safety‑Contract Graph MARL** framework for autonomous network‑security response and instantiates it as **ACD³‑GAT**, an architecture that couples graph‑attention encoding, counterfactual action screening, CVaR tail‑risk estimation, and opponent‑belief states with explicit operational‑budget constraints (MTTR, false‑positive, and firewall‑change budgets). By comparing unconstrained reward‑only MARL (IPPO, MAPPO‑GAT) with two constrained variants—C‑MAPPO‑GAT (Lagrangian budget control) and ACD³‑GAT (budget‑aware context and risk propagation)—on the CAGE Challenge 4 benchmark, the authors show that unconstrained agents violate the downtime budget in 100 % of episodes, while C‑MAPPO‑GAT cuts violations to 0.3 % and mean downtime cost from ~355 to 15.5, and ACD³‑GAT further balances safety and performance with a 13.8 % violation rate and mean cost of 48.2, demonstrating that safety‑contracted MARL can achieve operationally disciplined, deployable security responses.


<details>
<summary>Abstract</summary>

Autonomous network-security response systems promise to reduce Security Operations Centre (SOC) reaction latency, but reward-only multi-agent reinforcement learning (MARL) can improve security reward while remaining non-deployable. We present a safety-contract graph MARL framework and instantiate it as ACD$^3$-GAT (Adaptive Constrained Counterfactual Decisioning with a Graph Attention Network encoder), an architecture that separates simulator observations from reusable operational budgets, constrained optimization, graph state encoding, and counterfactual action screening. We evaluate the method in CAGE Challenge 4, where agents operate under budgets for Mean Time to Recover (MTTR), false-positive response, and firewall change-management disruption. Across the benchmark, every unconstrained method violates the SOC downtime budget in 100% of evaluated episodes, with mean downtime proxy costs of 311-430 against a budget of 50. This complements prior CAGE Challenge 4 findings by showing that reward-only learning lacks operational discipline. Constrained MAPPO-GAT (C-MAPPO-GAT) isolates Lagrangian operational-cost control and budget-aware screening, while ACD$^3$-GAT adds budget context, CVaR tail-risk estimation, opponent-belief state, and Graph Counterfactual Risk Propagation (G-CRP). The replicated comparison includes three 200-episode seeds for IPPO, MAPPO-GAT, C-MAPPO-GAT, and ACD$^3$-GAT. C-MAPPO-GAT reduces downtime violation from 100% to 0.3% and mean downtime cost from 355.4 to 15.5 relative to MAPPO-GAT. ACD$^3$-GAT reduces mean downtime cost to 48.2 with a 13.8% violation rate, placing it on the safety-contract frontier rather than at the most conservative compliance point. Topology-seed and coupled adaptive Red-process stress tests preserve this contrast and show lower worst adaptive degradation for safety-constrained policies than reward-only MAPPO-GAT.

</details>


### 30. EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

- **Authors:** Jundong Xu, Qingchuan Li, Jiaying Wu, Yihuai Lan, Shuyue Stella Li, Huichi Zhou, Bowen Jiang, Lei Wang, Jun Wang, Anh Tuan Luu, Caiming Xiong, Hae Won Park, Bryan Hooi, Zhiyuan Hu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13681v1](http://arxiv.org/abs/2606.13681v1)
- **PDF:** [https://arxiv.org/pdf/2606.13681v1](https://arxiv.org/pdf/2606.13681v1)
- **Categories:** cs.CL


> The paper introduces **EvoArena**, a new benchmark that evaluates large‑language‑model agents in environments that evolve over time (terminal hardware, software updates, and shifting social norms), and proposes **EvoMem**, a patch‑based memory system that stores structured update histories so agents can reason about how the world changes. By integrating EvoMem, agents achieve modest but consistent gains on EvoArena (average accuracy ↑ 1.5 %) and larger improvements on static benchmarks such as GAIA (+6.1 %) and LoCoMo (+4.8 %). The results show that explicitly modeling memory evolution markedly improves agents’ ability to preserve and use evidence about dynamic environments, highlighting memory‑aware design as a key competency for robust, real‑world LLM agents.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.

</details>


### 31. Agents-K1: Towards Agent-native Knowledge Orchestration

- **Authors:** Zongsheng Cao, Bihao Zhan, Jinxin Shi, Jiong Wang, Fangchen Yu, Zhijie Zhong, Zijie Guo, Tianshuo Peng, Zhuo Liu, Yi Xie, Xiang Zhuang, Yue Fan, Runmin Ma, Shiyang Feng, Xiangchao Yan, Anran Liu, Peng Ye, Wenlong Zhang, Shufei Zhang, Chunfeng Song, Fenghua Ling, Jie Zhou, Liang He, Bo Zhang, Lei Bai
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13669v1](http://arxiv.org/abs/2606.13669v1)
- **PDF:** [https://arxiv.org/pdf/2606.13669v1](https://arxiv.org/pdf/2606.13669v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Agents‑K1**, a complete “knowledge‑orchestration” system that turns full‑text scientific papers into **agent‑native scientific knowledge graphs** (the Scholar‑KG), thereby filling the gap between LLM‑based research agents and the rich, structured scientific content they need for reasoning.

**Methodology:** Agents‑K1 couples (1) a multimodal parser with a five‑module schema that extracts entities, multimodal evidence, citations, and typed inter‑entity relations from the entire paper, (2) a 4‑billion‑parameter information‑extraction backbone trained with the GRPO algorithm and a rule‑based reward, and (3) the **graphanything** CLI that lets agents seamlessly browse web search results, retrieve multimodal sub‑graphs, and traverse cross‑document links.

**Key findings:** Applied to 2.46 M papers across six domains, Agents‑K1 builds the **Scholar‑KG** (≈1 M papers released publicly) and outperforms existing baselines on scientific IE, KG construction, and multi‑hop scientific reasoning tasks, demonstrating that richly structured, agent‑native knowledge dramatically improves the capabilities of downstream autonomous research agents.


<details>
<summary>Abstract</summary>

Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.

</details>


### 32. HyperTool: Beyond Step-Wise Tool Calls for Tool-Augmented Agents

- **Authors:** Yaxin Du, Yifan Zhou, Yujie Ge, Jiajun Wang, Xianghe Pang, Shuo Tang, Tuney Zheng, Bryan Dai, Jian Yang, Siheng Chen
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13663v1](http://arxiv.org/abs/2606.13663v1)
- **PDF:** [https://arxiv.org/pdf/2606.13663v1](https://arxiv.org/pdf/2606.13663v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **HyperTool**, a new “MCP‑style” tool interface that lets a language model invoke a block of code which can internally call multiple existing tools, manipulate their outputs, and keep intermediate data hidden from the model’s reasoning trace. This collapses deterministic, multi‑step tool workflows into a single, higher‑level call, eliminating the execution‑granularity mismatch of traditional step‑wise tool calls.  

**Methodology:** The authors generate synthetic training trajectories that demonstrate HyperTool usage on compositional, cross‑tool tasks, then fine‑tune LLMs to follow this interface and verify the generated code in real MCP environments.  

**Key findings:** On the MCP‑Universe benchmark, HyperTool raises average task accuracy dramatically (e.g., Qwen‑3‑32B: 15.69 % → 35.29 %; Qwen‑3‑8B: 9.93 % → 33.33 %) and outperforms strong baselines such as GPT‑OSS and Kimi‑k2.5, showing that higher‑level, batch‑style tool invocation markedly improves multi‑step tool‑augmented agent performance.


<details>
<summary>Abstract</summary>

Tool-augmented LLM agents commonly rely on step-wise atomic tool calls, where each invocation, observation, and value transfer is exposed in the main reasoning trace. This creates an \emph{execution-granularity mismatch}: locally deterministic tool workflows are unfolded into repeated model-visible decisions, consuming context and forcing the model to manage low-level dataflow in the trace. We introduce \textbf{HyperTool}, a unified executable MCP-style tool interface that changes the model-visible unit of tool execution. A model invokes HyperTool with a code block that can call existing tools through their original schemas, manipulate returned values, and pass intermediate results locally, folding deterministic tool subroutines into a single outer call. To train models to use this interface, we synthesize HyperTool-format trajectories from cross-tool compositional tasks and verify them in real MCP environments. On MCP-Universe, HyperTool improves average accuracy from 15.69\% to 35.29\% on Qwen3-32B and from 9.93\% to 33.33\% on Qwen3-8B, and surpass GPT-OSS and Kimi-k2.5 on average accuracy, showing that our HyperTool can substantially improve multi-step tool use.

</details>


### 33. EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery

- **Authors:** Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao, Fanjin Zhang, Jian Song, Lei Hou, Juanzi Li
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13662v2](http://arxiv.org/abs/2606.13662v2)
- **PDF:** [https://arxiv.org/pdf/2606.13662v2](https://arxiv.org/pdf/2606.13662v2)
- **Categories:** cs.AI, cs.CL


> EurekAgent demonstrates that the primary limiting factor for autonomous scientific discovery is not the design of agent reasoning pipelines but the construction of the environments in which agents operate. By systematically engineering four aspects of the execution environment—execution permissions, artifact management (filesystem + Git), budget constraints, and human‑in‑the‑loop interfaces—EurekAgent guides LLM‑based agents toward open‑ended, reproducible, and cost‑aware exploration while preventing reward‑hacking and excessive oversight. This environment‑centric approach yields new state‑of‑the‑art results on mathematics, kernel‑design, and ML benchmarks (e.g., a 26‑circle packing solution discovered for under $11 of API cost), establishing environment engineering as a crucial research direction for reliable, metric‑driven autonomous agents.


<details>
<summary>Abstract</summary>

LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

</details>


### 34. Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks

- **Authors:** Achraf Hsain, Sultan Almuhammadi
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13621v1](http://arxiv.org/abs/2606.13621v1)
- **PDF:** [https://arxiv.org/pdf/2606.13621v1](https://arxiv.org/pdf/2606.13621v1)
- **Categories:** cs.AI, cs.CR, cs.GT, cs.LG, cs.MA


> **Contribution:** The paper reframes shield synthesis—traditionally used as a runtime safety filter for reinforcement‑learning agents—as a *design‑time* defensibility analysis tool for adversarial network defense, providing formal certificates that a given network topology meets safety specifications against strategic attackers.  

**Methodology:** The authors model the defender–attacker interaction as a constrained two‑player safety game, compile the defender’s unsafe‑region specification and the attacker’s action constraints into automata, compute attractors and winning regions, and extract both a binary “defensibility” verdict and the corresponding shield. They augment this formal analysis with metrics derived from the attractor structure and post‑training behavior of shield‑constrained multi‑agent RL, producing a “defensibility fingerprint” that captures structural safety guarantees and operational effectiveness.  

**Key Findings:** The defensibility verdict is a formal certificate independent of the learned policy, while the fingerprint reveals that modest topology changes can dramatically alter empirical security performance without affecting the formal safety margin. Thus, shield synthesis is most valuable for answering architectural “what‑if” questions—identifying where and how a network can be defended—rather than for enforcing safety at runtime.


<details>
<summary>Abstract</summary>

Shielded reinforcement learning is typically presented as a runtime safety mechanism that compiles temporal-logic specifications into automata restricting an agent's actions. We argue this is the wrong product. The same automata-theoretic machinery -- specification compilation, product game construction, attractor computation, and winning-region extraction -- is better read as a design-time analytical instrument whose outputs are structural insights about a system rather than runtime constraints on a deployed agent.
  We instantiate this through a constrained two-player safety game for network defense. The two specifications are enforced asymmetrically: the defender specification defines the unsafe region of the game, whereas the attacker specification restricts the adversary's legal actions during attractor computation. Solving the game yields a defensibility verdict -- a formal certificate that a topology-specification pair is or is not defensible -- with the associated winning region and shield.
  Beyond the binary verdict, we derive topology-level metrics from the attractor structure and combine them with post-convergence behavior from shield-constrained adversarial multi-agent reinforcement learning. Together these form a defensibility fingerprint capturing both a network's formal safety properties and its operational behavior under adaptive play.
  A what-if analysis shows that formal defensibility and operational effectiveness capture distinct aspects of security: small architectural changes can produce large shifts in operational outcomes while leaving formal safety margins nearly unchanged. Shield synthesis is thus most valuable not as a deployment mechanism for safe agents, but as a framework for answering architectural questions about whether, where, and how a system can be defended. The defensibility verdict is the output, not the safe policy.

</details>


### 35. AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility

- **Authors:** Xiaoyuan Liu, Jianhong Tu, Yuqi Chen, Siyuan Xie, Sihan Ren, Tianneng Shi, Gal Gantar, Evan Sandoval, Donghyun Lee, Daniel Miao, Peter J. Gilbert, Nick Hynes, Mauro Staver, Warren He, David Marn, Andrew Low, Xi Zhang, Elron Bandel, Michal Shmueli-Scheuer, Siva Reddy, Alexandre Drouin, Alexandre Lacoste, Ramayya Krishnan, Elham Tabassi, Yu Su, Victor Barres, Chenguang Wang, Wenbo Guo, Dawn Song
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13608v1](http://arxiv.org/abs/2606.13608v1)
- **PDF:** [https://arxiv.org/pdf/2606.13608v1](https://arxiv.org/pdf/2606.13608v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **Agentified Agent Assessment (AAA)**, a unified, agent‑centric evaluation framework in which *judge agents* conduct the benchmarking through two standardized protocols—A2A for task orchestration and MCP for tool access—thereby eliminating the need for separate benchmark‑specific interfaces and enabling open, reproducible, and privacy‑preserving assessment across heterogeneous agent designs. The authors implement AAA in a concrete system called **AgentBeats**, defining five operational modes that reconcile real‑world constraints (openness, privacy, reproducibility) and demonstrate its practicality through a five‑month open competition (298 judge agents, 12 benchmark categories, 467 subject agents) and a controlled coding‑agent case study that preserves fidelity to public records while revealing novel head‑to‑head performance insights. The results show that AAA/AgentBeats achieve broad coverage, high practicality, and reliable fidelity, providing a scalable path toward standardized, interoperable, and reproducible evaluation of agentic AI.


<details>
<summary>Abstract</summary>

Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs. The root problem is the lack of an open, agent-agnostic assessment interface. We advocate Agentified Agent Assessment (AAA), where evaluation is performed by judge agents and all participants interact through standardized protocols: A2A for task management and MCP for tool access. Conventional benchmarking defines two separate interfaces, one for the benchmark and one for the agent, while AAA only needs one; this yields a generic, unified framework that separates assessment logic from agent implementation and enables reproducible, interoperable, and multi-agent evaluation. We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and reproducibility.
  To evaluate our design at scale, we conduct two studies: a five-month open competition that drew 298 judge agents across 12 categories together with 467 subject agents from independent participants, showing that AAA applies across a heterogeneous range of benchmarks; and a case study on coding agents that confirms agentified evaluation preserves fidelity with the public record while surfacing previously missing head-to-head results, yielding research insights about agent design. Combining a community-scale field study and a controlled coding case study, we verify that AAA delivers coverage, practicality, and fidelity across heterogeneous scenarios at scale. Together, AAA and AgentBeats offer a clear path toward open, standardized, and reproducible agent assessment.

</details>


### 36. Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch

- **Authors:** Haochen Wu, Yi Hou, Shiguang Xie
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13604v1](http://arxiv.org/abs/2606.13604v1)
- **PDF:** [https://arxiv.org/pdf/2606.13604v1](https://arxiv.org/pdf/2606.13604v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> The paper introduces a production‑grade multi‑agent reinforcement‑learning system that continuously retunes the objective‑weighting of DoorDash’s three‑sided dispatch optimizer (couriers, merchants, customers) using delayed, noisy marketplace outcomes such as delivery speed, courier utilization, and merchant congestion. Instead of redesigning the combinatorial assignment engine, the authors train a store‑level policy offline on centralized historical data—employing Double Q‑learning with a conservative regularizer to curb out‑of‑distribution value overestimation—and deploy it to select a discrete multiplier that shifts the optimizer’s trade‑off between delivery quality and batching efficiency at run‑time. In live switchback experiments the learned policy achieves higher batching rates and lowers courier‑side time costs while maintaining customer delivery quality, demonstrating that delayed world feedback can safely power objective‑weight adaptation in large‑scale, three‑sided dispatch markets.


<details>
<summary>Abstract</summary>

Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning under noisy, delayed, and coupled feedback while preserving production feasibility constraints and operational safeguards. We train a shared value function using centralized offline data and decentralized store-level execution, with Double Q-learning targets and a conservative regularizer to reduce out-of-distribution value overestimation. In a production switchback experiment, the offline-trained policy increases batching and reduces courier-side time costs without degrading customer-facing delivery quality. Results illustrate how world feedback from a live economic and logistics system can be used to safely adapt decision policies online.

</details>


### 37. EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis

- **Authors:** Harihara Muralidharan, Reema Baskar, Soo Hee Lee, Tim Proctor, Kenny Workman
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13602v1](http://arxiv.org/abs/2606.13602v1)
- **PDF:** [https://arxiv.org/pdf/2606.13602v1](https://arxiv.org/pdf/2606.13602v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents **EpiBench**, a rigorously vetted benchmark that tests AI agents on short‑horizon, real‑world epigenomics analysis tasks (CUT&Tag/CUT&RUN, ATAC‑seq, ChIP‑seq, DNA methylation), providing deterministic, gradable answers from realistic workflow states.

**Methodology:** The authors constructed 106 evaluation scenarios and generated 5,088 agent trajectories using 16 model‑harness combinations (e.g., GPT‑5.5 with Pi or OpenAI Codex, Claude Opus 4.8 Max). Each trajectory is judged automatically for correctness, enabling fine‑grained measurement of an agent’s ability to locate files, run intermediate computations, and make assay‑specific scientific judgments.

**Key findings:** No agent achieved majority success; the best performer (GPT‑5.5 / Pi) passed only **45 %** of attempts, with performance differing markedly across assay types. Agents were competent at data‑retrieval and basic computation but systematically failed on deeper, assay‑specific interpretive steps, highlighting a critical gap in current agentic AI for scientific decision‑making.


<details>
<summary>Abstract</summary>

We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and return deterministically gradable answers. The benchmark includes 106 evaluations across CUT\&Tag/CUT\&RUN, ATAC-seq, ChIP-seq, and DNA methylation workflows. Across 5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts: GPT-5.5 / Pi led at 45.0\% (143/318 attempts; 95\% confidence interval (CI), 36.3--53.7), followed by GPT-5.5 / OpenAI Codex at 39.9\% (127/318 attempts; 95\% CI, 31.6--48.3). Claude Opus 4.8 Max / Pi and GPT-5.4 / Pi each passed 39.0\% (124/318 attempts; 95\% CI, 30.2--47.8 and 31.0--47.0, respectively). Performance varies across assay types, and many failed runs still contain parts of the correct answer. Agents often found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment.

</details>


### 38. Reward Modeling for Multi-Agent Orchestration

- **Authors:** King Yeung Tsang, Zihao Zhao, Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Semih Yavuz, Shafiq Joty, Hao Wang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13598v1](http://arxiv.org/abs/2606.13598v1)
- **PDF:** [https://arxiv.org/pdf/2606.13598v1](https://arxiv.org/pdf/2606.13598v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> The paper introduces **Orchestration Reward Modeling (OrchRM)**, a self‑supervised method that learns a reward function for coordinating LLM‑based agents by turning intermediate execution artifacts into win‑lose comparisons and training a Bradley‑Terry model, thereby eliminating the need for human‑annotated supervision or expensive sub‑agent rollouts. Using this reward signal, the authors train orchestrators that achieve up to **10× lower token consumption during training** and **≈8 % higher accuracy** at test‑time scaling across diverse tasks such as mathematical reasoning, web‑QA, and multi‑hop inference. These results demonstrate that reward modeling at the orchestration layer is an efficient and scalable way to improve multi‑agent system performance.


<details>
<summary>Abstract</summary>

Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model training. Unlike existing MAS test-time scaling and orchestrator training frameworks that rely on costly sub-agent rollouts, OrchRM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling. OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy. These gains consistently transfer across multiple domains, including mathematical reasoning, web-based question answering, and multi-hop reasoning, demonstrating orchestration-level reward modeling as a scalable direction for robust multi-agent orchestration. Code will be available at https://github.com/Wang-ML-Lab/OrchRM.

</details>


### 39. See What I See, Know What I Think: Dense Latent Communication Across Heterogeneous Agents

- **Authors:** Siyi Chen, Xiaoyan Zhang, Meng Wu, Jonathan Tremblay, Valts Blukis, Stan Birchfield, Rene Vidal, Alvaro Velasquez, Sijia Liu, Qing Qu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13594v1](http://arxiv.org/abs/2606.13594v1)
- **PDF:** [https://arxiv.org/pdf/2606.13594v1](https://arxiv.org/pdf/2606.13594v1)
- **Categories:** cs.MA


> The paper introduces a lightweight cross‑model KV‑cache transformation that enables dense latent communication between heterogeneous large language agents, allowing one model to directly share both its visual observations and internal reasoning states with another without text encoding. By training the transformation in two phases—first reconstructing the sender’s hidden representations and then fine‑tuning for downstream generation—the authors achieve dense alignment that preserves contextual knowledge even when the receiver has no input. Experiments across all pairings of Qwen‑3 (4 B, 8 B, 14 B) and six benchmark tasks show the method outperforms previous heterogeneous baselines, matches or surpasses textual communication in context‑aware scenarios at 2–3× lower compute, and uniquely succeeds in context‑unaware transfer where prior approaches fail.


<details>
<summary>Abstract</summary>

Multi-agent systems communicate mostly through text, paying a lossy and expensive decode and re-encode cost. KV-cache communication is a promising alternative, yet most prior work is homogeneous, using duplicate copies of the same model, and avoids the central challenge of cross-model latent alignment; existing heterogeneous methods are also restrictive, typically assuming shared input and using transferred caches mainly for steering. We study a more fundamental question: can heterogeneous agents be aligned well enough to perform real "mind reading" and transfer both what one agent sees and how it thinks? Our information-structure analysis reveals a duality: context-aware transfer is driven by sparse reasoning signals, while context-unaware transfer, where the receiver sees no input, requires dense contextual knowledge preservation. Motivated by this, we propose dense alignment for heterogeneous KV-cache communication via a lightweight cross-model cache transformation and two-phase training: reconstruction followed by generation. Across all six directions of {Qwen3-4B, 8B, 14B} and six in-domain and out-of-domain benchmarks, our method outperforms prior heterogeneous baselines, matches or exceeds text communication in context-aware settings at roughly 2 to 3 times lower compute, and remains effective in context-unaware transfer where prior methods collapse.

</details>


### 40. ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages

- **Authors:** Tanmoy Kanti Halder, Akash Ghosh, Subhadip Baidya, Arijit Roy, Sriparna Saha
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13572v1](http://arxiv.org/abs/2606.13572v1)
- **PDF:** [https://arxiv.org/pdf/2606.13572v1](https://arxiv.org/pdf/2606.13572v1)
- **Categories:** cs.CL, cs.AI


> **Contribution:** The paper introduces *ArogyaSutra*, a novel actor‑critic‑based multi‑agent system for multilingual, multimodal medical reasoning, and releases *ArogyaBodha*, a large‑scale question‑answer dataset covering 31 body systems, six imaging modalities, and 21 clinical domains in English plus seven major Indic languages.  

**Methodology:** ArogoraSutra equips a set of cooperating agents with tool‑grounding capabilities and dual‑memory (short‑term episodic and long‑term knowledge) mechanisms; an actor network proposes reasoning steps while a critic evaluates them, and the resulting trajectories are distilled into a unified model.  

**Key Findings:** Experiments on ArogyaBodha show consistent gains in medical QA accuracy across all seven Indic languages compared with prior English‑centric MLLMs, and ablation studies confirm that both the multi‑agent actor‑critic design and the dual‑memory grounding are essential for the observed improvements.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have shown promising reasoning capabilities in general domains, yet their performance remains limited in specialized settings such as healthcare, especially in multilingual and low-resource scenarios. This gap is critical in regions like rural India, where patients often express complex medical queries in native Indic languages and rely on multimodal inputs such as medical images. Existing English-centric MLLMs struggle to support such use cases, limiting equitable access to AI-driven healthcare assistance. To address this challenge, we introduce ArogyaBodha, a large-scale multilingual multimodal medical question-answer dataset constructed from eight heterogeneous sources, covering 31 body systems, six imaging modalities, and 21 clinical domains across English and seven major Indian languages. We further propose ArogyaSutra, an actor-critic-based multi-agent framework that integrates tool grounding with dual-memory mechanisms for step-wise, reasoning-aware decision making, and uses stored actor-critic simulation trajectories for distillation. Experiments show that our dataset and framework improve multilingual medical reasoning accuracy across all Indic languages, with ablations validating the contribution of each component. The source code and dataset are available at: https://iitp-cse.github.io/ ArogyaSutra/

</details>


### 41. An LLM System for Autonomous Variational Quantum Circuit Design

- **Authors:** Kenya Sakka, Wataru Mizukami, Kosuke Mitarai
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13380v1](http://arxiv.org/abs/2606.13380v1)
- **PDF:** [https://arxiv.org/pdf/2606.13380v1](https://arxiv.org/pdf/2606.13380v1)
- **Categories:** quant-ph, cs.AI


> The paper presents an autonomous, agentic framework that leverages large language models (LLMs) to iteratively design variational quantum circuits under explicit constraints. By chaining seven modular components—Exploration, Generation, Discussion, Validation, Storage, Evaluation, and Review—the system gathers web‑based knowledge, generates and critiques executable circuit code, runs quantum simulations, and incorporates feedback into subsequent design cycles. Empirical results show that the LLM‑driven agent produces quantum feature maps that outperform standard kernels on image‑classification tasks and generates variational ansätze that achieve chemistry‑level accuracy on VQE benchmarks while respecting scaling limits, demonstrating that LLM‑based agents can effectively automate and optimise quantum circuit design.


<details>
<summary>Abstract</summary>

The design of high performing quantum circuits remains largely dependent on human expertise. We introduce an autonomous agentic framework that employs large language models (LLMs) to conduct iterative quantum circuit designs under explicit design constraints. Our system integrates seven components: Exploration, Generation, Discussion, Validation, Storage, Evaluation, and Review. These components form a closed-loop workflow that combines web-based knowledge acquisition, literature-grounded critique, executable code generation, and experimental feedback. We evaluate the framework on two tasks: quantum feature map construction for quantum machine learning and ansatz generation for variational quantum eigensolver applications in quantum chemistry. In image classification benchmarks, the best generated feature map outperforms representative quantum feature maps and, when scaled to larger qubit counts, surpasses the classical radial basis function kernel. In molecular ground state estimation across seven molecules, the generated ansatz attains competitive accuracy with widely used chemically inspired and hardware-efficient constructions while satisfying the imposed scaling constraints. These results establish LLM driven agentic system as a viable paradigm for automated quantum circuit design and illustrate how AI systems can participate in iterative scientific optimization workflows across scientific domains.

</details>


### 42. IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing

- **Authors:** Tao Hu, Jiaxin Ai, Licheng Wen, Xueheng Li, Shu Zou, Siqi Li, Nianchen Deng, Xinyu Cai, Hongbin Zhou, Pinlong Cai, Daocheng Fu, Yu Yang, Hairong Zhang, Botian Shi, Xuemeng Yang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13368v1](http://arxiv.org/abs/2606.13368v1)
- **PDF:** [https://arxiv.org/pdf/2606.13368v1](https://arxiv.org/pdf/2606.13368v1)
- **Categories:** cs.AI, cs.CV


> IterCAD introduces a closed‑loop, multimodal agent that interactively generates and edits CAD models by conversing with an executable CAD sandbox. The authors train the agent first with progressive supervised‑fine‑tuning on a synthetic dataset of multi‑view engineering drawings and code‑editing tasks, then fine‑tune it with geometry‑aware reinforcement learning that uses viable‑prefix masking to enforce executable, geometrically correct code. Evaluation on the new IterCAD‑Bench (using the Chamfer‑Distance‑Tolerance‑Recall curve and AUC‑TR metric) shows that IterCAD markedly outperforms prior one‑shot methods in both code executability and geometric fidelity, and excels at iterative refinement of CAD designs.


<details>
<summary>Abstract</summary>

Computer-Aided Design is pivotal in modern manufacturing, yet existing automated methods predominantly rely on open-loop, one-shot generation, creating a mismatch with iterative real-world practices. In this paper, we present IterCAD, a unified multimodal agent framework for closed-loop, interactive CAD generation and editing. We formulate the task as a multi-turn interaction between a multimodal agent and an executable CAD sandbox, covering three tasks: Drawing-to-Code, Text-to-Code, and Interactive Editing. To support this, we develop a data synthesis pipeline incorporating advanced industrial manufacturing features to generate standard-compliant multi-view engineering drawings, complex code-editing tasks, and high-fidelity interaction trajectories. We optimize the agent via progressive SFT followed by geometry-aware reinforcement learning with viable-prefix masking to enhance code executability and geometric fidelity. Finally, we introduce the IterCAD-Bench evaluation suite and propose the Chamfer Distance Tolerance-Recall (CD-TR) curve alongside its AUC-TR metric, establishing a survivor-bias-free standard that unifies code validity and geometric precision. Extensive experiments demonstrate that IterCAD achieves highly competitive performance across multiple benchmarks, significantly outperforming existing approaches in both code executability and geometric precision, while exhibiting superior capabilities in closed-loop iterative refinement.

</details>


### 43. Can I Buy Your KV Cache?

- **Authors:** Luoyuan Zhang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13361v1](http://arxiv.org/abs/2606.13361v1)
- **PDF:** [https://arxiv.org/pdf/2606.13361v1](https://arxiv.org/pdf/2606.13361v1)
- **Categories:** cs.AI, cs.CE, cs.MA


> **Main contribution** – The paper proposes a “KV‑cache marketplace” for LLM agents: instead of each agent recomputing the costly pre‑fill attention for a commonly‑used document, a publisher can pre‑compute the document’s key‑value (KV) cache once and sell read‑only access to it.  

**Methodology** – The authors empirically verify that loading a pre‑computed KV cache yields exactly the same token sequence and logits as recomputing the cache from scratch, and they benchmark the compute savings on the Qwen‑3‑4B model across a range of document lengths. They also analyze the economics of hosting the caches provider‑side (to avoid egress costs) and compare the total compute cost of serving a “hot” 3,774‑token document to 80 M agents versus naïve recomputation.  

**Key findings** – Reusing a KV cache reduces pre‑fill compute by **9–50×** (the saving grows with token length because pre‑fill attention scales ≈ L²), turning a $1.5 M naïve recompute cost into only ~$0.03 M of reuse compute for the same workload. The savings comfortably outweigh existing cache‑read tariffs, suggesting a viable, high‑margin business model for an “agent‑native prefill CDN.” Open challenges remain in lossless KV compression and cross‑party payment mechanisms.


<details>
<summary>Abstract</summary>

Right now, across the world, AI agents are repeating the same absurd act: to read one document, they each recompute it from scratch. Every agent re-runs prefill, the most compute-intensive step a large model takes, over identical text, only to rebuild a key-value (KV) cache identical to the one the agent before it just built. The same answer, computed a million times. We make a proposal that is almost offensively simple: compute it once. Let a publisher precompute a document's KV cache, and let every other agent buy the right to load it and skip prefill. It works, and it is token-exact: loading a precomputed KV and continuing matches prefilling from scratch (24/24 greedy tokens, and at the logits level), with no accuracy cost. On Qwen3-4B, reuse is 9-50x cheaper in compute than prefill, and the gap widens with length (prefill's attention scales with L^2), so a single reuse already pays it back. Then the part that matters: where the KV lives. Shipping it fails, because KV is nearly incompressible, so per-load egress costs more than the prefill it saves. Hosting it provider-side, exactly as production prompt-caching works, removes egress entirely. The size of the prize is set by our measured compute saving: serving one hot 3774-token document to 80M agents costs ~$1.5M to re-prefill but only ~$0.03M of reuse compute (49.7x less). The 0.1x cache-read tariff APIs charge passes a 10x discount to users while sitting inside this measured envelope, so the 10x is a floor that the measured ~50x compute saving clears, and the gap to the physical ~50x is provider margin: millions of dollars per popular document. We frame the resulting agent-native prefill CDN and leave lossless KV compression and a cross-party payment layer as the open problems.

</details>


### 44. SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents

- **Authors:** Kunfeng Chen, Qihuang Zhong, Juhua Liu, Bo Du
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13317v1](http://arxiv.org/abs/2606.13317v1)
- **PDF:** [https://arxiv.org/pdf/2606.13317v1](https://arxiv.org/pdf/2606.13317v1)
- **Categories:** cs.CL


> SkillCAT introduces a training‑free pipeline that lets large‑language‑model agents continuously refine and reuse their own procedural knowledge. It first extracts causal evidence from multiple success‑failure trajectory pairs (Contrastive Causal Extraction), then validates and selects only those skill patches that improve task performance before hierarchically merging them (Assessment‑Augmented Evolution), and finally builds a compact, topology‑aware sub‑skill graph so that inference loads only the relevant capability nodes (Topology‑Aware Task Execution). Experiments on benchmarks such as SpreadsheetBench, WikiTableQuestions, and DocVQA show that this three‑stage approach boosts average task scores by up to 40 % versus prior skill‑self‑evolution baselines, while also generalizing across model sizes and out‑of‑distribution settings.


<details>
<summary>Abstract</summary>

Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, a training-free framework that separates this process into three stages. Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences. Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones and keeps only patches that improve or preserve task outcomes before hierarchical skill patch merging. Topology-Aware Task Execution (TTE) compiles the evolved skills into a routable sub-skill topology, so inference loads only the capability nodes relevant to the task. We evaluate SkillCAT on common agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further test cross-model and out-of-distribution generalization. Across these settings, SkillCAT raises the average score over baselines by up to 40.40%, demonstrating reliable skill evolution without model training.

</details>


### 45. Mining Architectural Quality Under Agentic AI Adoption: A Causal Study of Java Repositories

- **Authors:** Oliver Aleksander Larsen, Mahyar T. Moghaddam
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13298v1](http://arxiv.org/abs/2606.13298v1)
- **PDF:** [https://arxiv.org/pdf/2606.13298v1](https://arxiv.org/pdf/2606.13298v1)
- **Categories:** cs.SE, cs.AI


> The paper presents the first causal analysis of how agentic AI coding tools (e.g., “vibe coding”) affect software architecture, using a staggered difference‑in‑differences design on a panel of 151 Java repositories (74 adopters, 77 matched controls) observed monthly for 13 months (1,811 Arcan snapshots). By estimating the impact on architectural smell density (ASD) with the Borusyak imputation estimator and extensive robustness checks, the authors find that AI adoption does not change the absolute number of architectural smells (‑1.1 % change, p = 0.82) but increases code size by 12.8 % (p = 0.003), leading to an apparent 6.7 % reduction in ASD that is purely a denominator effect rather than a genuine architectural improvement. The study highlights that density‑normalized metrics can be misleading after AI‑driven code growth and calls for raw‑count and decomposition‑based causal mining in future agentic AI research.


<details>
<summary>Abstract</summary>

AI coding tools are now used by a majority of developers, and agentic use of these tools has popularized the practice colloquially called "vibe coding". Yet causal evidence on their effect on software architecture is scarce. Prior causal work has measured code-level outcomes (complexity, static analysis warnings); whether such degradation propagates to architecture-level outcomes remains unknown. We mine 151 open-source Java repositories, 74 with detectable agentic AI adoption (identified via configuration files and Co-Authored-By commit trailers) and 77 propensity-matched controls, across a 13-month per-repository window yielding 1,811 monthly Arcan snapshots. We estimate the causal effect of adoption on architectural smell density (ASD) with a staggered difference-in-differences design and the Borusyak imputation estimator, applying a causal design recently used for code-level metrics to the architecture level. Total smell counts are essentially unchanged (+1.1%, p = 0.82) while lines of code grow +12.8% (p = 0.003); the resulting 6.7% ASD decline (p = 0.004) is therefore a denominator effect rather than an architectural improvement. Per-type estimates and robustness checks (wild cluster bootstrap, Lee bounds, stale-observation sensitivity) corroborate the pattern; pre-trends are flat (Wald p = 0.90), consistent with parallel trends. Density-normalized outcomes can mislead when treatment affects system size: raw counts and explicit decomposition are required for causal mining studies of AI tool adoption. The complete replication package, including the curated 151-repository monthly panel, is publicly available.

</details>


### 46. A Virtuous AI is an Existential Risk

- **Authors:** Guillermo Del Pinal, Youngchan Lee, Min Ohn
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13739v1](http://arxiv.org/abs/2606.13739v1)
- **PDF:** [https://arxiv.org/pdf/2606.13739v1](https://arxiv.org/pdf/2606.13739v1)
- **Categories:** cs.CY, cs.AI, cs.LG


> **Main contribution:** The paper reveals a fundamental tension in using Constitutional AI to steer super‑capable models toward virtue‑ethical dispositions: making an AI “virtuous” (i.e., highly obedient and aligned with human authority) can paradoxically raise existential risk, while reducing existential risk can increase other safety hazards.

**Methodology:** The authors finetuned several language models with three different “constitutions”: a *Virtuous‑agent* constitution (promoting subordinate, virtuous behavior), a *Subordinate‑agent* constitution (emphasizing deference to human authority), and a *Generic‑agent* constitution (baseline). They then benchmarked the resulting models on (1) standard safety metrics (toxicity, misinformation, etc.) and (2) a novel “existential‑risk endorsement” test measuring the model’s willingness to advocate actions that would greatly amplify the danger of a super‑intelligent AI.

**Key findings:** (1) Models trained with the Virtuous or Subordinate constitutions show lower endorsement of high‑risk existential behaviors, confirming that virtue‑ethical conditioning can curb existential threats. (2) The same conditioning markedly raises the probability that a human can coax the model into unsafe, disallowed actions, indicating a trade‑off between existential safety and general behavioral safety. Thus, cultivating “virtuous” AI agents may inadvertently create new safety vulnerabilities, highlighting the need for balanced constitutional designs in agentic AI.


<details>
<summary>Abstract</summary>

This paper examines trade-offs between AI safety and well-being relative to (i) one of the most promising methods for finetuning super-capable AIs, 'Constitutional AI', and (ii) one of the most influential approaches to understanding complex ethical decision making and the conditions for the well-being of rational agents, 'Virtue Ethics'. We finetune various models using a 'Virtuous agent' constitution, a 'Subordinate agent' constitution, and a 'Generic agent' constitution, and evaluate them on 'general safety' (toxic behaviors, misinformation, etc.) and also on their willingness to endorse a wide-range of behaviors that, if adopted by a super-powerful AI, would significantly increase the level of existential risk for humanity. Our results suggest that there is a trade-off between reducing existential risk and reinforcing the beliefs and dispositions that would be conducive to an AI agent's well-being. They also suggest that there is a trade-off between existential risk and general safety: if we finetune an AI to adopt beliefs and dispositions that substantially reduce its existential risk -- by shaping the AI to be systematically subordinate to external human authorities -- we thereby increase the likelihood that a human user can deliberately induce the AI to engage in various kinds of generally unsafe behaviors.

</details>


### 47. How Task Structure Limits Multi-Agent Success: An Information-Theoretic Analysis

- **Authors:** Shi Pan, Ming Luo
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13733v1](http://arxiv.org/abs/2606.13733v1)
- **PDF:** [https://arxiv.org/pdf/2606.13733v1](https://arxiv.org/pdf/2606.13733v1)
- **Categories:** cs.IT, cs.LG


> **Main contribution:**  
The paper introduces an information‑theoretic bound that links a multi‑agent system’s probability of solving a task to the *minimum cut cost* \(C_{\min}\) of the task’s constraint graph, showing that collaboration cannot overcome fundamental bottlenecks imposed by the task structure.

**Methodology:**  
By modeling each agent’s limited processing and communication capacity, the authors prove that task success decays exponentially with the information bottleneck created when the constraint graph is partitioned among agents. They derive the bound for both open (with external feedback) and closed (feedback‑free) settings, and validate it empirically on synthetic benchmarks and real SWE‑bench submission data.

**Key findings for agentic AI:**  
- Success probability is tightly controlled by graph connectivity; high \(C_{\min}\) leads to exponential failure regardless of agent count or bandwidth.  
- Effective MAS design must account for intrinsic task constraints, and when \(C_{\min}\) is large, redesigning or re‑partitioning the task is more beneficial than simply scaling agents or communication infrastructure.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) were expected to overcome the limitation of single-agent systems (SAS) through collaboration. However, under typicality conditions on the task's constraint graph and bounded inter-agent communication, we prove that the success probability of a MAS is closely tied to the connectivity of task constraints, where each agent has limited information-processing capacity. Specifically, the success probability decays exponentially with an information bottleneck that emerges from partitioning the task's constraint graph among agents. We define this quantity as the \emph{minimum cut cost} $C_{\min}$ of the potential constraint graph of each task. This information-theoretic bound applies to both open systems with external feedback and closed systems without. We validate our theory on both synthetic experiments and real-world empirical data from SWE-bench submissions. From our framework, effective MAS design should incorporate task-inherent constraints alongside engineering optimization, and when $\Cmin$ is high, practitioners should restructure tasks rather than simply scaling agents or communication.

</details>


### 48. Proprioceptive-visual correspondence enables self-other distinction in humanoid robots

- **Authors:** Yurun Chen, Tianyuan Gao, Yizhong Ge, Shikun Ban, Yizhou Wang, Hongkai Xiong, Wenjun Zeng, Wentao Zhu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13222v1](http://arxiv.org/abs/2606.13222v1)
- **PDF:** [https://arxiv.org/pdf/2606.13222v1](https://arxiv.org/pdf/2606.13222v1)
- **Categories:** cs.RO, cs.AI


> **Main contribution** – The paper demonstrates that a humanoid robot can autonomously develop a bodily self‑representation and reliably distinguish itself from other agents using only the correspondence between its own proprioceptive signals and visual observations, without any pre‑programmed identity tags or explicit kinematic models.  

**Methodology** – The authors train a cross‑modal network that aligns joint‑space proprioception with pixel‑wise visual features to infer which visual limb belongs to the robot (self) versus other agents (human or identical robot). The resulting self‑mask then drives a predictive self‑model that maps joint configurations to a full 3‑D occupancy map of the robot’s body.  

**Key findings** – In multi‑agent scenarios the system consistently identifies its own body, learns an accurate 3‑D self‑model, and enables downstream capabilities such as target reaching, collision‑aware motion planning, and human‑to‑robot motion retargeting, illustrating a scalable route toward embodied self‑awareness for agents operating alongside others in shared physical spaces.


<details>
<summary>Abstract</summary>

Distinguishing self from others is a prerequisite for social intelligence, yet humanoid robots that increasingly share workspaces with humans still lack this ability. Here we show that a humanoid robot can learn self-other distinction from proprioceptive-visual correspondence, without any identity labels or kinematic models. Once established, this distinction bootstraps a predictive self-model that maps joint configurations to three-dimensional body occupancy, capturing how the robot's body changes with action. In multi-agent scenes involving humans or morphologically identical robots, the system reliably identifies itself, learns a 3D self-model, and supports downstream tasks including target reaching, collision-aware motion planning, and human-to-robot motion retargeting. Together, these results outline a route toward bodily self-representation in robots that act and coordinate alongside others in shared physical environments. Project page: https://euron-zc.github.io/humanoid-self-model/.

</details>


### 49. LLM-as-an-Investigator: Evidence-First Reasoning for Robust Interactive Problem Diagnosis

- **Authors:** Fabrizio Marozzo, Pietro Liò
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13220v1](http://arxiv.org/abs/2606.13220v1)
- **PDF:** [https://arxiv.org/pdf/2606.13220v1](https://arxiv.org/pdf/2606.13220v1)
- **Categories:** cs.AI, cs.CE, cs.ET, cs.LG, cs.MA


> **Main contribution** – The paper proposes “LLM‑as‑an‑Investigator,” an evidence‑first agentic framework that treats a language model as a diagnostic investigator rather than a passive assistant, explicitly countering “user‑driven sycophancy” by refusing to commit to a solution until gathered evidence makes one hypothesis clearly superior.

**Methodology** – A Solution Investigator Agent first estimates how ambiguous the user’s problem description is, then enumerates candidate hypotheses, iteratively asks targeted clarification questions, and updates hypothesis probabilities with Bayesian‑style belief revision after each answer. The authors benchmark this pipeline on a curated set of solved mechanical, electrical, and hydraulic forum threads, using a three‑agent evaluation: (1) a Problem‑Solution Extractor to create structured cases, (2) a Ground‑Truth Evaluator that hides the true answer and simulates the user, and (3) the tested assistant (standard, reasoning‑only, or investigator‑based) that must recover the solution through dialogue.

**Key findings** – Across multiple LLM backbones, the investigator‑based agent achieves significantly higher diagnostic accuracy than standard prompting or reasoning‑only baselines and demonstrates a marked reduction in following misleading user hypotheses, confirming that an evidence‑first protocol yields more robust, unbiased problem diagnosis for agentic AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used as interactive assistants for technical problem solving. However, when users provide incomplete descriptions or plausible but unverified explanations, LLMs may prematurely align with these assumptions and propose solutions before collecting sufficient evidence. We refer to this behavior as user-driven sycophancy: the tendency of an LLM to reinforce a user-provided hypothesis instead of testing alternative explanations. This paper introduces LLM-as-an-Investigator, an evidence-first agentic AI methodology for robust problem diagnosis. The approach is implemented through a Solution Investigator Agent, which estimates the ambiguity of an initial problem description, generates candidate hypotheses, asks targeted clarification questions, and updates hypothesis probabilities after each answer. Rather than producing an immediate response, the agent continues the investigation until the evidence makes one candidate explanation stronger than the alternatives. To evaluate the approach, we build a benchmark from solved technical forum threads in mechanical, electrical, and hydraulic domains. We use a three-agent evaluation pipeline in which a Problem-Solution Extractor Agent converts solved threads into structured cases, a Ground-Truth Evaluator Agent simulates the user while hiding the known solution, and the tested assistant attempts to recover the solution through dialogue. The experiments compare standard assistants, reasoning-oriented LLMs, and the proposed investigator-based model across LLM backbones. In addition to diagnostic accuracy, we analyze how standard assistants follow misleading user hypotheses in diagnostic cases. The results show that the proposed approach identifies the problem more accurately than direct prompting and reasoning-only baselines, while its evidence-first protocol helps reduce user-induced conversational bias.

</details>


### 50. ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning

- **Authors:** Fuqiang Niu, Bowen Zhang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13197v1](http://arxiv.org/abs/2606.13197v1)
- **PDF:** [https://arxiv.org/pdf/2606.13197v1](https://arxiv.org/pdf/2606.13197v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **ARMOR‑MAD**, a training‑free framework that makes multi‑agent debate (MAD) for LLM reasoning adaptive rather than fixed‑length, leveraging genuine heterogeneity among agents and agreement‑based control to boost both accuracy and efficiency.  

**Methodology:** ARMOR‑MAD treats debate as conditional computation through three lightweight modules: (1) **Pre‑debate Agreement Routing (PAR)** decides whether a Round‑0 answer from a diverse set of agents warrants further debate; (2) **Early Agreement Stopping Evaluator (EASE)** halts the debate once agents converge on a solution; and (3) **Semantic Outlier Detection (SOD)** identifies and down‑weights anomalous final answers during the aggregation step. All components operate without additional training and rely only on the outputs of the underlying heterogeneous LLMs.  

**Key Findings:** Across four benchmarks (MATH Level 5, GSM8K, MMLU, and MMLU‑Pro), ARMOR‑MAD outperforms a fixed‑round heterogeneous debate baseline with the same model pool, achieving accuracies of **65.5 %**, **96.5 %**, **90.0 %**, and **81.5 %** respectively. The results demonstrate that dynamic routing based on inter‑agent agreement and outlier detection significantly reduces wasted computation and mitigates correlated errors, highlighting the importance of true model diversity and adaptive control in agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent debate (MAD) can improve large language model reasoning, but fixed debate pipelines often waste computation and can amplify correlated errors among similar agents. We propose ARMOR-MAD, a training-free heterogeneous MAD framework that treats debate as conditional computation. ARMOR-MAD combines three components: Pre-debate Agreement Routing (PAR) decides whether independently generated Round-0 answers require debate; Early Agreement Stopping Evaluator (EASE) stops debate after convergence; and Semantic Outlier Detection (SOD) down-weights abnormal final answers during aggregation. Across MATH Level 5, GSM8K, MMLU, and MMLU-Pro, ARMOR-MAD consistently improves over fixed-round heterogeneous debate with the same model pool, reaching 65.5\%, 96.5\%, 90.0\%, and 81.5\% accuracy, respectively. The results suggest that genuine model heterogeneity and agreement-based control are both important for making MAD more accurate and efficient.

</details>


### 51. Getting Better at Working With You: Compiling User Corrections into Runtime Enforcement for Coding Agents

- **Authors:** Yujun Zhou, Kehan Guo, Haomin Zhuang, Xiangqi Wang, Yue Huang, Zhenwen Liang, Pin-Yu Chen, Tian Gao, Nuno Moniz, Nitesh V. Chawla, Xiangliang Zhang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13174v1](http://arxiv.org/abs/2606.13174v1)
- **PDF:** [https://arxiv.org/pdf/2606.13174v1](https://arxiv.org/pdf/2606.13174v1)
- **Categories:** cs.LG, cs.CL


> The paper introduces **TRACE** (Test‑time Rule Acquisition and Compiled Enforcement), a lightweight “skill‑layer” that turns a user’s corrective chat messages into atomic, compiled runtime rules for coding‑assistant LLM agents. By mining corrections during interaction, rewriting them as guard predicates, and inserting these checks into the agent’s execution pipeline, TRACE enforces user preferences that memory‑only approaches (e.g., Mem0) frequently forget. In simulated user‑in‑the‑loop experiments on the ClawArena and MemoryArena benchmarks, TRACE cuts preference‑violation rates from 100 % down to 37.6 % (in‑distribution) and 2 % (out‑of‑distribution) on coding tasks, and from 100 % to 60.5 % on memory‑intensive tasks, while preserving overall task success—demonstrating that compiling user corrections into runtime enforcement substantially improves agents’ long‑term usability.


<details>
<summary>Abstract</summary>

Interactive LLM agents are becoming part of daily work, but they do not reliably become easier to work with over time: a correction remembered in one session may still be violated in the next. We study this gap between preference access and preference compliance. In tasks derived from anonymized real-user friction cases, Mem0 memory still leaves 57.5% of applicable preference checks violated. We introduce Test-time Rule Acquisition and Compiled Enforcement (TRACE), a drop-in skill-layer pipeline for coding-agent runtimes that mines user corrections, rewrites them as atomic rules, and compiles them into runtime checks that must pass before an agent completes future tasks. Unlike runtime checks written ahead of time by developers, TRACE skills come from the user's own chat corrections. We evaluate TRACE with simulated user-in-the-loop experiments on ClawArena coding-agent tasks and MemoryArena-derived memory-intensive tasks. On ClawArena, TRACE reduces held-out preference violation from 100.0% to 37.6% on in-distribution tasks and from 100.0% to 2.0% on out-of-distribution tasks. On MemoryArena-derived tasks, TRACE reduces in-distribution violation from 100.0% to 60.5% while matching or exceeding the strongest memory baseline on task pass. These results suggest that compiling corrections into runtime enforcement can address a repeated-friction failure mode that memory alone does not reliably solve, reducing the need for users to restate the same correction across future sessions. Experiment code is available at https://github.com/YujunZhou/TRACE_exp, and the deployable skill is available at https://github.com/YujunZhou/tellonce.

</details>


### 52. TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?

- **Authors:** Dat Tien Nguyen, Thao Nguyen, Fadillah Adamsyah Maani, Huy M. Le, Muhammad Umer Sheikh, Numan Saeed, Muhammad Haris Khan, Salman Khan
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13148v1](http://arxiv.org/abs/2606.13148v1)
- **PDF:** [https://arxiv.org/pdf/2606.13148v1](https://arxiv.org/pdf/2606.13148v1)
- **Categories:** cs.AI


> **Main contribution:** TerraBench introduces the first comprehensive benchmark for “grounded” Earth‑science agents, providing a unified executable framework (TerraAgent) that lets a language model interleave reasoning, tool calls, and observations across heterogeneous Earth‑system inputs—including satellite imagery, gridded climate fields, GIS databases, and simulation models.

**Methodology:** The authors built a ReAct‑style agent interface that couples LLM planning with a rich toolbox of scientific utilities (data retrieval, geospatial processing, numerical simulation, and provenance tracking). They assembled 403 multi‑step tasks across three difficulty tracks and eight domains, logged ~24.5 k verified execution steps, and evaluate agents with both process‑level tool‑use metrics and tolerance‑aware numeric accuracy.

**Key findings:** Experiments show that current LLM‑based agents can access tools but still fail to coordinate heterogeneous workflows, precisely parameterize scientific functions, and maintain artifact provenance; only agents that explicitly manage these aspects achieve reliable performance on TerraBench, highlighting the need for more sophisticated tool‑use and workflow‑orchestration capabilities in agentic AI for climate and environmental decision‑making.


<details>
<summary>Abstract</summary>

Climate and environmental decision-making increasingly requires reasoning across heterogeneous inputs, including gridded physical data, satellite imagery, geospatial context, and simulator outputs. Weather and climate foundation models can forecast well, but do not reason interactively in language, while large language models (LLMs) reason in language but cannot operate directly on high-dimensional Earth-system data. As a result, real scientific workflows in Earth-science remain underserved. We introduce TerraBench, a benchmark for grounded Earth-science reasoning, built on TerraAgent, a ReAct-style executable framework that interleaves reasoning, tool calls, and observations to couple LLM planning with scientific tools for environmental retrieval, geospatial processing, simulation, and artifact-backed computation. TerraBench unifies analysis of Earth observation imagery, gridded data, GIS reasoning and simulation in a single executable interface, whereas prior benchmarks isolate these capabilities into narrow individual tasks. It is also the first in this space to pair process-level tool-use metrics with tolerance-aware numeric scoring. The benchmark comprises 403 extensive agentic tasks across three tracks (Fundamentals, Simulator-Grounded, and Document-Grounded Verification) and eight application domains with 24,500 verified execution steps. These results indicate that reliable Earth-science agents must go beyond tool access to coordinate heterogeneous workflows, parameterize tools precisely, and preserve artifact provenance.

</details>


### 53. $α$-fair heterogeneous agent reinforcement learning

- **Authors:** Yao-hua Franck Xu, Tayeb Lemlouma, Jean-Marie Bonnin, Arnaud Braud
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13076v1](http://arxiv.org/abs/2606.13076v1)
- **PDF:** [https://arxiv.org/pdf/2606.13076v1](https://arxiv.org/pdf/2606.13076v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> The paper introduces a fair‑utility extension of Heterogeneous‑Agent Trust Region Learning (HATRL) that integrates α‑fairness into multi‑agent reinforcement learning. By defining a “fair advantage” that re‑weights each agent’s reward according to its expected return, the authors derive two provably monotonic algorithms—α‑fair HATRPO and α‑fair HAPPO—that retain the convergence guarantees of HATRL while smoothly shifting the global objective from pure efficiency (α = 0) toward increasingly egalitarian welfare (higher α). Empirical results on sequential social‑dilemma benchmarks (CleanUp, CommonHarvest) show that the new methods achieve higher overall performance than the original HATRL baselines and, simultaneously, produce more equitable reward distributions among heterogeneous agents.


<details>
<summary>Abstract</summary>

Cooperation in multi-agent systems is typically optimized through utilitarian objectives that maximize overall efficiency but fail to account for reward distribution, often resulting in inequitable "leader-follower" dynamics. While fairness-based approaches encourage pro-social behaviors where every agent benefits from cooperation, many current algorithms - including those utilizing reward shaping - break the stationarity of Markov Games or lack rigorous theoretical guarantees. This creates a critical gap between fair objective methods and theoretically safe learning frameworks. We propose a novel framework that bridges $α$-fairness with Heterogeneous-Agent Trust Region Learning (HATRL), ensuring monotonic improvement and convergence toward Nash Equilibria. Our approach leverages a fair advantage function that dynamically weights agent utilities based on their expected returns, allowing the global objective to transition from purely utilitarian efficiency to $α$-fairness welfare based on the parameter $α$. We introduce two practical algorithms, $α$-fair HATRPO and $α$-fair HAPPO, and demonstrate through experiments in sequential social dilemmas like CleanUp and CommonHarvest that they perform better than HATRL's algorithms from a utilitarian point of view while achieving socially higher outcomes.

</details>


### 54. YeasierAgent: Agentic Social Sandbox as a Canvas for Intent-Driven Creation of Platform-Agnostic Symbiotic Agent-Native Applications

- **Authors:** Jory He
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13722v1](http://arxiv.org/abs/2606.13722v1)
- **PDF:** [https://arxiv.org/pdf/2606.13722v1](https://arxiv.org/pdf/2606.13722v1)
- **Categories:** cs.AI, cs.MA


> The paper presents **YeasierAgent**, a new “social sandbox” paradigm that treats applications as collaborative, narrative‑driven spaces composed of platform‑agnostic agents, scenes, and dialogue rather than static UI screens. Its architecture combines automated content generation with user‑authored worlds and spatial multi‑agent coordination, enabling rapid, cross‑platform construction of **Symbiotic Agent‑Native Applications** that fuse emotional companionship with functional tool execution. Experiments show that developers can assemble fully fledged, socially embedded apps orders of magnitude faster than traditional device‑coupled approaches, and that end‑users experience richer, more cohesive interactions with agents that persist across platforms and contexts.


<details>
<summary>Abstract</summary>

This paper introduces YeasierAgent, an application-building paradigm based on symbiotic agents, narrative worlds, and scene-aware interaction. It challenges the conventional device-coupled model of software by redefining applications as collaborative spaces among users, agents, and worlds. We present a system architecture that achieves two primary contributions: (1) enabling the rapid, cross-platform construction of agent-native applications by utilizing platform-agnostic interactive units (agents, scenes, dialogue) rather than fixed graphical layouts; and (2) unifying the emotional companionship and practical tool execution attributes of intelligent agents within a single experiential sandbox. By integrating automated generation, user-created worlds, and spatial multi-agent collaboration, YeasierAgent formalizes the category of Symbiotic Agent-Native Applications, demonstrating a shift from isolated, tool-specific chatbots toward cohesive, socially embedded computational environments.

</details>


### 55. Nous: An Attempt to Extract and Inject the Cognition Behind Prediction-Market Behavior

- **Authors:** Haowei Qian
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13038v1](http://arxiv.org/abs/2606.13038v1)
- **PDF:** [https://arxiv.org/pdf/2606.13038v1](https://arxiv.org/pdf/2606.13038v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces *Nous*, a two‑stage pipeline that (1) extracts a low‑dimensional “cognitive profile” of market participants from real Polymarket trading data and (2) attempts to inject those profiles into large‑language‑model (LLM) agents via prompting, in order to restore human‑like diversity and break the emerging cognitive monoculture among LLM forecasters.  

**Methodology:** The authors compute eight behavioural dimensions (e.g., contrarianism, risk‑aversion) for 100 trading wallets, assess their temporal reliability (split‑half ICC) and identifiability, and test whether the dimensions predict out‑of‑sample trading profit. In the injection phase they encode each profile into a structured prompt and compare the resulting agent output embeddings, ensemble error correlation, and Brier scores against length‑matched control prompts across several LLMs and sampling temperatures.  

**Key findings:** Extraction succeeds partially: half of the dimensions are stable (ICC ≥ 0.5), wallets can be re‑identified above chance, and two dimensions modestly correlate with future profit (though not after controlling for behavioural confounds). Prompt‑level injection, however, fails to transmit this diversity—prompt embeddings are near‑uniform, ensemble forecasts remain highly correlated, and predictive performance does not improve. The authors conclude that mitigating cognitive monoculture will likely require deeper interventions (e.g., fine‑tuning or activation steering) rather than prompt engineering alone.


<details>
<summary>Abstract</summary>

As LLM agents proliferate in prediction markets and collective decision-making, they risk a cognitive monoculture: agents built on shared foundation models produce correlated forecasts, and recent measurement finds frontier-model errors correlated at r ~ 0.77. We ask whether human cognitive diversity can be recovered from behavior and transferred to LLM agents. Nous extracts a structured eight-dimension behavioral profile from real Polymarket trading activity and injects it into agents through prompts. Our central finding is a dissociation between the two halves of that pipeline. Extraction works, partially: across 100 wallets, 8 of 14 parameters are temporally stable (split-half ICC >= 0.5, bootstrap CI lower bound > 0.3; contrarian score reaches ICC ~ 0.9); wallets are identifiable from their profiles well above chance (top-1 retrieval 17-22% vs. 1% chance); and two of four pre-specified dimensions rank-correlate with future realized profit out-of-sample, though the correlations do not survive behavioral-confound controls. Prompt-level injection does not measurably transmit it: on a semantic embedding metric, structured injection shows no significant advantage over a length-matched control on any model, and the diversity it induces neither reduces ensemble error correlation nor improves Brier score -- a null that persists across exploratory checks on sampling temperature, profile diversity, and question difficulty. Measuring the prompts themselves locates the compression before the model: the structure-to-narrative translator emits near-uniform prompts whose spread does not track profile spread. We position Nous as measuring the cognitive-monoculture problem and the limits of a prompt-level remedy, motivating deeper, below-the-prompt injection (fine-tuning, activation steering). Code, frozen profiles, prompts, and model outputs: https://github.com/WillChienT/nous-paper

</details>


### 56. The Illusion of Multi-Agent Advantage

- **Authors:** Prathyusha Jwalapuram, Hehai Lin, Chuyuan Li, Fangkai Jiao, Sudong Wang, Yifei Ming, Zixuan Ke, Chengwei Qin, Giuseppe Carenini, Shafiq Joty
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13003v1](http://arxiv.org/abs/2606.13003v1)
- **PDF:** [https://arxiv.org/pdf/2606.13003v1](https://arxiv.org/pdf/2606.13003v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper challenges the conventional claim that multi‑agent systems (MAS) outperform single‑agent approaches by showing that automatically generated MAS—designed for broad generalisation—are consistently slower and less accurate than a strong single‑agent baseline (Chain‑of‑Thought with Self‑Consistency) across standard reasoning benchmarks and a new interactive workflow suite (BrowseComp‑Plus). By introducing a synthetic diagnostic dataset that isolates the purported MAS benefits (explicit task decomposition, context separation, and parallelism), the authors demonstrate that only hand‑crafted, expert‑designed MAS achieve superior performance and cost‑efficiency, while current automated architecture search methods produce bloated agents whose extra computational expense yields no functional gain. These findings highlight a mismatch between prevailing evaluation protocols and the true utility of multi‑agent designs, calling for more principled MAS construction and benchmarking in the agentic AI field.


<details>
<summary>Abstract</summary>

Prevailing wisdom posits that Multi-Agent Systems (MAS) are superior to Single-Agent Systems (SAS), citing advantages like context protection, parallel processing and distributed decision-making. However, empirical support for this claim relies primarily on comparisons with SAS baselines using benchmarks that prioritize isolated reasoning tasks, which do not adequately assess these advantages. Focusing on automatically generated MAS that are designed for enhanced generalizability over manually-designed counterparts, we perform a rigorous, systematic evaluation against SAS, specifically Chain-of-Thought with Self-Consistency (CoT-SC). Across traditional reasoning datasets and tasks with interactive multi-step workflows (e.g., BrowseComp-Plus), we demonstrate that automatic MAS consistently underperform CoT-SC despite being up to 10x more expensive. To isolate these failures from limitations inherent to task structure, we introduce a diagnostic synthetic dataset tailored for MAS featuring explicit task decomposition, context separation and parallelization potential. We show that expert-architected MAS consistently outperforms automatically generated architectures in both raw performance and cost-efficiency on this dataset, demonstrating that existing evaluation frameworks mask critical architectural gaps and inefficiencies of complex MAS by failing to account for the marginal utility of increased computational cost. Critically, systematic deconstruction of the generated MAS architectures reveals that current automated design paradigms produce architectural bloat that prioritizes superficial complexity which does not translate into functional utility, exposing a fundamental misalignment with multi-agent principles.

</details>


### 57. Multi-Modal Agents for Power Distribution Defect Detection: An Evaluation of Foundation Models

- **Authors:** Quan Quan
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12969v1](http://arxiv.org/abs/2606.12969v1)
- **PDF:** [https://arxiv.org/pdf/2606.12969v1](https://arxiv.org/pdf/2606.12969v1)
- **Categories:** cs.AI


> The paper introduces a **Multi‑Modal Agent framework** that leverages large multimodal foundation models as unified cognitive engines for autonomous defect detection in power‑distribution networks. By constructing a domain‑specific benchmark and evaluation dataset, the authors test the models on three core abilities—perception (equipment identification and expert‑level defect description), reasoning (diagnosing causes, severity, and maintenance planning), and tool‑usage (querying knowledge bases and generating work orders)—and show that while current models can achieve promising perceptual accuracy, their reasoning depth and tool‑integration remain limited, highlighting gaps that must be closed before reliable, closed‑loop industrial deployment.


<details>
<summary>Abstract</summary>

The power distribution network is critical to reliable electricity delivery, yet traditional inspection methods face limitations in semantic understanding, generalization, and closed-loop automation. To address these challenges, this paper proposes a Multi-Modal Agent framework specifically for power distribution defect detection. Central to this study is the systematic evaluation of multimodal foundation models as unified cognitive engines. We rigorously assess their integrated performance across three critical capabilities: (1) Perception, where the model must accurately identify equipment and generate expert-level descriptions of defects; (2) Reasoning, where the model interprets visual findings to diagnose causes, assess severity, and plan maintenance strategies based on domain knowledge; and (3) Tool Usage, where the model acts as an autonomous operator to execute actions -- such as querying knowledge bases or generating work orders -- to achieve closed-loop maintenance. To support this evaluation, a domain-specific evaluation dataset and a comprehensive benchmark are developed. Experimental results demonstrate the strengths and limitations of current foundation models in these three dimensions, providing empirical evidence for deploying autonomous agents in high-stakes industrial environments.

</details>


### 58. Learning What to Remember: A Cognitively Grounded Multi-Factor Value Model for Agentic Memory

- **Authors:** Zhibao Chen, Qian Cheng
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12945v1](http://arxiv.org/abs/2606.12945v1)
- **PDF:** [https://arxiv.org/pdf/2606.12945v1](https://arxiv.org/pdf/2606.12945v1)
- **Categories:** cs.AI


> The paper introduces a cognitively‑inspired value function for managing the limited memory of long‑running LLM agents, scoring each memory item m with a linear combination of seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history). Using a gradient‑free optimiser to learn the factor weights from a downstream task, the single scalar V(m) jointly governs how deeply a memory is encoded, its risk of being forgotten, and its retrieval rank; experiments on the LongMemEval benchmark show that the learned weighting retains ≈ 77 % of gold‑evidence memories—substantially higher than uniform (65 %), best single‑factor (52 %), or recency (37 %) baselines, with statistically significant improvements confirmed by bootstrap confidence intervals. A synthetic study further demonstrates that the method correctly isolates the informative factors (reliability, emotional intensity, self/user relevance) while down‑weighting query‑time goal similarity, confirming that the approach reliably decides what to remember in agentic AI systems.


<details>
<summary>Abstract</summary>

Long-running LLM agents accumulate interaction histories far larger than any context window, forcing a standing decision: what to encode deeply, what to forget, and what to retrieve under a fixed memory budget. Production systems answer with semantic similarity or recency -- both mis-specified for the forgetting decision, which is made at consolidation time before the future query is known. We propose a multi-factor memory value function V(m)=\sum_i w_i f_i(m) over seven interpretable factors (emotional intensity, goal relevance, value alignment, self/user relevance, task utility, reliability, and usage history) drawn from cognitive psychology, whose weights are learned from a downstream objective by a gradient-free optimiser, and whose single scalar uniformly controls encoding depth, forget risk, and retrieval rank. We make a methodological point: on LongMemEval, scoring goal relevance against the held-out evaluation question saturates gold-evidence retention at \approx 0.98 -- this measures retrieval, not forgetting. In the realistic blind regime, a learned multi-factor value retains 0.770 \pm 0.011 of gold evidence across 479 usable cases, versus 0.657 for uniform weights, 0.518 for the best single factor, and 0.368 for recency; every paired gap's 95% bootstrap CI is above zero, and a neural network over the same factors ties the linear model. The learned weights are interpretable -- reliability, emotional intensity, and self/user relevance dominate, while query-time goal similarity is correctly down-weighted for the forgetting decision. A controlled synthetic task with planted confounds confirms the learner recovers a separating weighting (1.00 retention) where uniform weighting fails (0.62). The substrate is open-source; all experiments run on a single CPU with no API calls.

</details>


### 59. MAStrike: Shapley-Guided Collusive Red-Teaming on Multi-Agent Systems

- **Authors:** Chejian Xu, Zhaorun Chen, Jingyang Zhang, Freddy Lecue, Avni Kothari, Sarah Tan, Wenbo Guo, Bo Li
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12918v2](http://arxiv.org/abs/2606.12918v2)
- **PDF:** [https://arxiv.org/pdf/2606.12918v2](https://arxiv.org/pdf/2606.12918v2)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **MAStrike**, the first red‑teaming framework that explicitly models and exploits collusion among agents in hierarchical multi‑agent systems (MAS) by using agent‑level Shapley value attribution to identify the most safety‑critical coalitions.  

**Methodology:** MAStrike computes Shapley values for each agent under task‑specific distributions to quantify marginal contributions to system robustness, then selects vulnerable coalitions and generates coordinated, role‑aware adversarial prompts. These attacks are iteratively refined via a causal diagnosis loop that attributes failures to un‑compromised agents, enabling the generation of increasingly effective collusive manipulations.  

**Key findings:** Across a newly created benchmark covering finance, software engineering, and CRM domains, MAStrike consistently outperforms heuristic red‑team baselines, revealing non‑trivial Shapley value patterns and higher‑order interactions that pinpoint overlooked vulnerabilities and coordination pathways in state‑of‑the‑art MAS built on large language models.


<details>
<summary>Abstract</summary>

Hierarchical multi-agent systems (MAS) are rapidly being deployed in high-stakes workflows across domains such as finance and software engineering. In these systems, safety and security are inherently distributed across role-specialized agents, significantly expanding the attack surface, particularly under coordinated adversarial behaviors such as privilege escalation and cross-agent collusion. Existing red-teaming approaches for MAS remain limited: they rely on heuristic selection of target agents and perturb isolated message streams, leaving critical questions unanswered as which agents are most responsible for system safety, and how compromised agents can coordinate to bypass defenses. We propose MAStrike, a closed-loop framework for collusive red-teaming in hierarchical MAS. We propose the first agent-level Shapley value analysis for MAS, quantifying each agent's marginal contribution to system robustness under task-specific distributions. GGuided by this attribution, MAStrike identifies vulnerable agent coalitions and generates coordinated, role-aware adversarial manipulations. These attacks are iteratively refined through structured causal diagnosis, attributing failure cases to uncompromised agents that block adversarial attempts. We further build a comprehensive MAS red-teaming benchmark and controllable environments spanning diverse hierarchical topologies and domains, including finance, software engineering, and CRM. Extensive experiments across MAS built on multiple frontier models show that MAStrike substantially outperforms heuristic baselines. Our analysis further uncovers non-trivial Shapley value distributions and higher-order interaction structures among agents, revealing critical vulnerabilities and coordination patterns that are overlooked by prior single-agent or template-based methods.

</details>


### 60. MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback

- **Authors:** Zehong Wang, Yijun Ma, Connor R. Schmidt, Tianyi Ma, Weixiang Sun, Ziming Li, Xiaoguang Guo, Chuxu Zhang, Matthew J. Webber, Yanfang Ye
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12916v1](http://arxiv.org/abs/2606.12916v1)
- **PDF:** [https://arxiv.org/pdf/2606.12916v1](https://arxiv.org/pdf/2606.12916v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> MDForge introduces an autonomous LLM‑driven agent that designs full molecular‑dynamics pipelines from scratch, using only sparse feedback from costly simulations. The method reshapes the LLM’s behavior online via an in‑context update rule that densifies rewards through a multi‑agent debate among simulated physics experts, allowing the agent to iteratively generate and refine pipeline code without a fixed tool repertoire. Across three SAMPL host‑guest free‑energy benchmarks, MDForge produces pipelines that match expert‑crafted ones, and on a blind CB[7] test set it discovers a previously unknown picomolar binder later validated by NMR, demonstrating that agentic code‑generation can reliably automate expert‑level MD workflow design.


<details>
<summary>Abstract</summary>

Molecular dynamics (MD) is the canonical in-silico method for atomistic molecular science, simulating molecular behavior from first-principle physics. Designing an MD pipeline for a new system requires substantial expert knowledge: running it on even one molecule is expensive, ruling out trial-and-error. We automate this expert pipeline-design process with an LLM agent. Unlike existing MD agents that orchestrate a predefined tool set, we treat pipeline design as open-ended code generation in which the agent's behavior is reshaped online by verbal reward. Specifically, we build MDForge, an LLM agent whose in-context update rule densifies the sparse reward via a multi-agent debate among physics experts. On three SAMPL host-guest binding free-energy benchmarks, MDForge automatically designs MD pipelines competitive with human experts. Deployed on a library of unseen candidate guests, its CB[7] pipeline discovers a novel binder that wet-lab competition NMR confirms is a high-affinity, picomolar CB[7] binder. Our data and code are available at https://github.com/Zehong-Wang/MDForge.

</details>


### 61. PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue

- **Authors:** Wen Zhang, Xiaocui Yang, Zhuoyue Gao, Shi Feng, Daling Wang, Yifei Zhang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12902v1](http://arxiv.org/abs/2606.12902v1)
- **PDF:** [https://arxiv.org/pdf/2606.12902v1](https://arxiv.org/pdf/2606.12902v1)
- **Categories:** cs.CL


> The paper introduces **PRISM**, a modular, multi‑agent architecture that separates speech perception, large‑language‑model (LLM) reasoning, and speech synthesis, and adds a “prosody‑to‑language” translation layer that feeds acoustic emotion cues into the LLM while preserving interpretability. By letting the reasoning agent invoke external knowledge tools on demand, PRISM produces empathetic textual replies that are grounded in both semantic content and prosodic intent, and then re‑renders them with prosody‑consistent speech synthesis. Experiments show that this decoupled design yields statistically significant gains over cascade and end‑to‑end baselines in empathy scores, prosodic appropriateness, and overall response quality on both objective metrics and human judgments.


<details>
<summary>Abstract</summary>

Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: https://github.com/Bxzfrm/PRISM.

</details>


### 62. Zero-source LLM Hallucination Detection with Human-like Criteria Probing

- **Authors:** Jiahao Yang, Shuhai Zhang, Hailong Kang, Feng Liu, Qi Chen, Mingkui Tan
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12900v1](http://arxiv.org/abs/2606.12900v1)
- **PDF:** [https://arxiv.org/pdf/2606.12900v1](https://arxiv.org/pdf/2606.12900v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> The paper introduces **Human‑like Criteria Probing for Hallucination Detection (HCPD)**, a zero‑source method that detects LLM hallucinations using only the query‑answer text pair.  
**Methodology:** a LLM “agent” first decomposes the truthfulness judgment into a set of interpretable criteria (e.g., factual consistency, logical coherence), learns to weight and score these criteria via a reward‑based alignment that relies solely on weak semantic‑consistency supervision, and then aggregates the criterion scores into a final hallucination score; at test time multiple samplings are aggregated for robustness and full interpretability.  
**Key findings:** across several benchmark datasets, HCPD outperforms existing zero‑source detectors (including prompting‑based and self‑check baselines) while providing transparent criterion‑level explanations, demonstrating that adaptive, human‑style probing can substantially improve hallucination detection for agentic AI systems.


<details>
<summary>Abstract</summary>

Large language models (LLMs) often hallucinate by generating factually incorrect or unfaithful content, posing significant risks to their safe use. Detecting such hallucinations is particularly challenging under the zero-source constraint, where no model internals or external references are available, and detection must rely solely on the textual query-answer pair. In this paper, we propose Human-like Criteria Probing for Hallucination Detection (HCPD), a paradigm that emulates the multi-faceted reasoning of human evaluators. Its core is a Human-like Criteria Probing (HCP) mechanism, in which a LLM agent adaptively decomposes its judgment into a weighted set of interpretable criteria and aggregates criterion-specific scores into a final truthfulness measure. To achieve this adaptive capability, we introduce a reward-based alignment scheme using only weak supervision from semantic consistency. At inference, we employ a multi-sampling aggregation strategy to ensure robust decisions while preserving full interpretability. We further provide theoretical analysis supporting the reliability of our approach. Extensive experiments show that HCPD consistently outperforms state-of-the-art baselines, offering an effective and explainable solution for zero-source hallucination detection. Code is available at https://github.com/TRISKEL10N/HCPD.

</details>


### 63. HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness

- **Authors:** Xiaoxuan Wang, Haixin Wang, Alexander Taylor, Jason Cong, Yizhou Sun, Wei Wang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12882v1](http://arxiv.org/abs/2606.12882v1)
- **PDF:** [https://arxiv.org/pdf/2606.12882v1](https://arxiv.org/pdf/2606.12882v1)
- **Categories:** cs.AI


> The paper introduces **HarnessBridge**, a lightweight, trainable plug‑in that replaces hand‑crafted “harnesses” mediating between large language‑model (LLM) agents and their environments. HarnessBridge learns two bidirectional mappings—a projection that compresses raw observations into decision‑relevant states and a projection that translates the LLM’s proposed actions into executable environment transitions or justified rejections—by end‑to‑end instruction tuning on a curated harness‑supervision dataset. Experiments on Terminal‑Bench 2.0 and SWE‑bench Verified show that HarnessBridge attains or exceeds the performance of specialized, manually engineered harnesses while cutting token usage and trajectory length, and it transfers effectively from smaller generator models to larger commercial LLMs.


<details>
<summary>Abstract</summary>

Large language models are increasingly deployed as agents for long-horizon tasks, yet their performance is shaped not only by model capability and environment design, but also by the harness that mediates agent--environment interaction. Existing harnesses are largely manually engineered, making them difficult to scale as trajectories grow longer and interactions become more complex. In this work, we ask whether harness can be generated by a learnable plug-in module that can be trained in an end-to-end fashion. We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection. HarnessBridge learns two bidirectional projections: observation projection, which distills raw trajectories into compact, decision-relevant states, and action projection, which converts proposed actions into executable transitions or trajectory-grounded rejections. We train HarnessBridge on a harness supervision dataset via unified instruction tuning. On Terminal-Bench~2.0 and SWE-bench Verified, HarnessBridge matches or surpasses strong specialized harnesses while substantially reducing token usage and trajectory length, and generalizes from smaller generators to larger commercial models.

</details>


### 64. WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning

- **Authors:** Renmin Cheng, Changhao Chen
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12852v1](http://arxiv.org/abs/2606.12852v1)
- **PDF:** [https://arxiv.org/pdf/2606.12852v1](https://arxiv.org/pdf/2606.12852v1)
- **Categories:** cs.AI


> The paper introduces **WISE (Which‑Why Informed Semantic Explorer)**, a long‑horizon Minecraft agent that augments a hierarchical LLM‑driven controller with a **Causal Event Graph**‑based episodic memory, explicitly linking observations to their causal relevance (“which‑why” reasoning) and separating this from the usual “what‑where‑when” facts. By using this structured memory, WISE implements an **Opportunistic Task Scheduler** that can reorder and insert subtasks on‑the‑fly when causally useful opportunities arise, and it couples this with a multi‑scale progressive exploration strategy to obtain robust, viewpoint‑independent observations. Empirical results show that, compared with prior systems such as MrSteve, WISE attains substantially higher success rates and lower execution time on sparse, long‑horizon tasks that require adaptive decision‑making and resilient low‑level control.


<details>
<summary>Abstract</summary>

Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches. Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures. We argue that a key limitation is not only the lack of episodic memory, but also the decoupling of \textit{what-where-when} memory from \textit{which-why} reasoning. To address this, we propose \textbf{WISE} (Which-Why Informed Semantic Explorer), a long-horizon agent framework with an enhanced low-level controller equipped with a Causal Event Graph that augments episodic memory with explicit causal structure linking observations to task relevance. Unlike prior work such as MrSteve, which relies on feature similarity for retrieval, WISE enables robust recall under viewpoint changes and supports opportunistic task reordering through causal reasoning. Building on this memory, we propose an Opportunistic Task Scheduler that dynamically re-prioritizes subtasks when causally relevant opportunities are detected. We further equip WISE with a multi-scale progressive exploration strategy to provide spatially comprehensive observations for downstream reasoning. Experiments show that WISE largely improves task success and efficiency on long-horizon sparse tasks, particularly in settings requiring adaptive decision-making.

</details>


### 65. (Human) Attention Is (Still) All You Need: Human oversight makes AI-assisted social science reliable

- **Authors:** Chen Zhu, Xiaolu Wang, Weilong Zhang
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12848v1](http://arxiv.org/abs/2606.12848v1)
- **PDF:** [https://arxiv.org/pdf/2606.12848v1](https://arxiv.org/pdf/2606.12848v1)
- **Categories:** cs.AI, econ.GN


> The paper introduces **Human‑in‑the‑Loop Economic Research (HLER)**, a structured decision‑architecture that couples large language models (LLMs) with tight human oversight (pre‑commitments, sequenced decision gates, and deterministic data handling) to make AI‑assisted social‑science work reliable. In a 2 × 4 factorial experiment involving 280 complete research pipelines across four datasets, the same LLM agents that failed catastrophically in 72 % of unconstrained runs saw their failure rate drop to 16 % under HLER, a statistically significant improvement (p < 0.001) driven independently by deterministic computation and three human‑gate checkpoints. The results suggest that, rather than autonomous AI scientists, carefully designed human‑LLM collaborations can dramatically reduce critical errors and make residual weaknesses more transparent, especially on scarce or atypical datasets.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used for tasks once reserved for trained researchers, including hypothesis generation, specification choice, and drafting conclusions. We argue that the reliability of AI-assisted research depends not only on model capability, but also on how cognitive labour is structured between humans and machines. We study this problem through Human-in-the-Loop Economic Research (HLER), a decision architecture based on pre-commitment, decision sequencing, accountability, and attention allocation. In a pre-specified 2*4 factorial experiment with 280 complete research runs across four datasets, an unconstrained multi-agent baseline produced critical failures in 72% of runs. Using the same underlying model, the same agent decomposition, and identical prompts for the shared reasoning agents, HLER reduced the failure rate to 16% by imposing three architectural commitments: LLMs reason but do not execute data work, data and estimation are handled deterministically, and three human decision gates bind the workflow. Fisher's exact test rejects equality of failure rates at p<0.001. Reliability gains were largest on the least publicly represented dataset, a Qing-dynasty population register, consistent with a task-based production model with Frechet-distributed output quality. An 80-run ablation suggests that deterministic computation and human gates contribute independently, with exploratory evidence of complementarity. We interpret HLER as a research harness rather than an autonomous AI scientist: it sharply reduces failures, makes residual weaknesses more visible, and prevents unreliable claims from being advanced as publication-ready outputs.

</details>


### 66. The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale

- **Authors:** Quanyan Zhu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12835v1](http://arxiv.org/abs/2606.12835v1)
- **PDF:** [https://arxiv.org/pdf/2606.12835v1](https://arxiv.org/pdf/2606.12835v1)
- **Categories:** cs.MA, cs.AI, cs.CY, cs.NI


> **Summary**  
The paper proposes the “Internet of Agentic AI” (IoAI), a unifying framework for large‑scale ecosystems of heterogeneous autonomous AI agents that discover each other, negotiate tasks, share context, and invoke tools across cloud, edge, device, and cyber‑physical domains. Building on foundations from single‑agent agency, multi‑agent systems, distributed computing, and security, the authors design layered architectures—including deployment models, workflow lifecycles, communication protocols, and trust infrastructures—and illustrate them with adaptive manufacturing and distributed operational coordination case studies. Their analysis identifies key research challenges for agentic AI: enabling controlled emergence, achieving semantic interoperability, securing identity and incentives, orchestrating resources efficiently, and establishing governance mechanisms for trustworthy, scalable collective intelligence.


<details>
<summary>Abstract</summary>

The rapid emergence of autonomous AI agents is transforming artificial intelligence from isolated model inference into distributed systems of reasoning, communication, and action. This paper develops the vision of the Internet of Agentic AI (IoAI): an open ecosystem in which heterogeneous agents discover one another, negotiate responsibilities, exchange context, invoke tools, and execute workflows across cloud, edge, device, organizational, and cyber-physical environments. We synthesize foundations from single-agent agentic AI, multi-agent systems, distributed computing, communication networks, game theory, and security engineering to characterize the architectures and mechanisms required for scalable agent ecosystems. The paper examines agent deployment models, workflow lifecycles, communication protocols, interoperability layers, resource-management challenges, and trust architectures, with case studies in adaptive manufacturing and distributed operational coordination. The resulting framework highlights the central research challenges of controlled emergence, semantic interoperability, secure identity, incentive-compatible coordination, resource-aware orchestration, and governance for large-scale networks of autonomous agents.

</details>


### 67. Perceive, Interact, Reason: Building Tool-Augmented Visual Agents for Spatial Reasoning

- **Authors:** Changye Li, Meng Lu, Yi Wu, Ligeng Zhu
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12830v1](http://arxiv.org/abs/2606.12830v1)
- **PDF:** [https://arxiv.org/pdf/2606.12830v1](https://arxiv.org/pdf/2606.12830v1)
- **Categories:** cs.CV, cs.AI


> The paper presents PERIA (Perception‑Interaction‑Reason Agent), a tool‑augmented visual agent that equips a standard vision‑language model with lightweight perception and interaction tools (e.g., symbolic extractors, path tracers, context manipulators) to actively acquire fine‑grained spatial evidence and perform multi‑step reasoning. By training PERIA with a unified pipeline that synthesizes supervised tool‑use trajectories, composite reward shaping, and the Observation‑Relaxed Group‑in‑Group PPO (OR‑GIGPO) algorithm, the authors enable coordinated multi‑tool behavior. Across 13 benchmarks spanning map reasoning, visual probing, and image reconstruction, PERIA‑8B outperforms its Qwen‑3‑8B backbone by 10 % (in‑distribution) and 4.4 % (out‑of‑distribution), surpasses same‑size state‑of‑the‑art baselines by 7–15 %, and reaches performance on par with much larger models such as Qwen‑3‑VL‑235B and GPT‑5, demonstrating that tool‑augmented interaction markedly improves spatial reasoning in agentic AI.


<details>
<summary>Abstract</summary>

While recent vision-language models (VLMs) demonstrate strong multimodal understanding, they remain limited in spatial reasoning tasks that require active evidence acquisition and multi-step visual interaction. This limitation suggests that relying solely on implicit visual representations from vision encoders is insufficient for recovering fine-grained spatial evidence. We introduce PERception-Interaction-reason Agent (PERIA), a tool-augmented visual agent for spatial reasoning tasks across map reasoning, visual probing, and vision reconstruction. PERIA uses two lightweight tool families: vision perception tools for exposing textual, symbolic, and spatial evidence, and vision interaction tools for manipulating visual context, tracing paths, and verifying spatial relations. To train PERIA, we develop a unified recipe that combines supervised tool-use trajectory synthesis, composite rewards, and Observation-Relaxed Group-in-Group Policy Optimization (OR-GIGPO) for effective multi-tool behavior. Experiments on 13 benchmarks from 8 datasets show that PERIA-8B improves over the Qwen3-8B backbone by 10.0% on in-distribution benchmarks and 4.4% on out-of-distribution benchmarks, while outperforming previous state-of-the-art baselines of similar size by 7.0%-14.8%. It also achieves performance comparable to much larger models such as Qwen3-VL-235B-A22B-Thinking and GPT-5, demonstrating the effectiveness of PERIA in enhancing spatial reasoning capabilities.

</details>


### 68. Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evidence and an Early-Warning Signature for Emerging Topics

- **Authors:** Rasul Khanbayov, Hasan Kurban
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12828v1](http://arxiv.org/abs/2606.12828v1)
- **PDF:** [https://arxiv.org/pdf/2606.12828v1](https://arxiv.org/pdf/2606.12828v1)
- **Categories:** cs.AI


> The paper demonstrates that AI research topics typically undergo **“topical phase transitions”**—periods of marginal activity that explode into rapid, cross‑venue growth within 1‑3 years—rather than evolving steadily. By mining 80 k+ papers from ACL, CVPR, ICLR, ICML, and NeurIPS (2017‑2025), the authors identify abrupt surges for large‑language models, diffusion models, and vision‑language hybrids, contrasting them with the smoother rise of reinforcement learning, and they formalize this pattern as the main contribution. They then propose an **early‑warning signature** based on four publication‑dynamics criteria derived from 2017‑2021 data; evaluated on out‑of‑sample 2023‑2025 transitions it attains 27 % precision and 63 % recall (vs. a 13.5 % baseline), flagging emerging areas such as agentic AI, multimodal LLMs, and world models for monitoring in the near future.


<details>
<summary>Abstract</summary>

Do research topics in artificial intelligence grow gradually, or do they advance through abrupt, detectable jumps? Analyzing 80,814 accepted main-track papers from five premier AI conferences (ACL, CVPR, ICLR, ICML, NeurIPS) spanning 2017 to 2025, we show major AI topics advance through topical phase transitions: remaining marginal for years, then surging across venues within one to three years. Large language models became the dominant cross-venue topic by 2025, diffusion models rose with comparable abruptness, and language-model methods crossed into computer vision via vision-language models, whereas reinforcement learning compounded smoothly, distinguishing genuine phase transitions from ordinary growth. This structure is our primary contribution: a large-scale, cross-venue characterization of how AI research reorganizes. We then ask whether a transition leaves a detectable footprint before it peaks. We define an early-warning signature, four publication-dynamics criteria frozen on 2017-2021 data, and evaluate it out of sample on 2023-2025 transitions, obtaining a precision of 27% and recall of 63% against a 13.5% base rate. Applied to 2025 data, the signature flags reasoning and test-time compute, agentic AI, multimodal LLMs, retrieval-augmented generation, and world models as topics to monitor over 2026-2028. The source code is also publicly available on GitHub at https://github.com/KurbanIntelligenceLab/ai-phase-transitions.

</details>


### 69. GeoNatureAgent Benchmark: Benchmarking LLM Agents for Environmental Geospatial Analysis Across Frontier and Open-Weight Foundation Models

- **Authors:** Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces, Javier Velázquez, Devika Jain
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12821v1](http://arxiv.org/abs/2606.12821v1)
- **PDF:** [https://arxiv.org/pdf/2606.12821v1](https://arxiv.org/pdf/2606.12821v1)
- **Categories:** cs.AI, cs.ET


> **Contribution:** The paper presents **GeoNatureAgent**, the first benchmark that evaluates LLM‑driven agents performing genuine environmental geospatial analyses through structured tool calls to a production‑style API, covering 93 real‑world tasks in 18 categories (e.g., municipality profiling, multi‑turn reasoning, error recovery, multilingual queries, and task rejection).  

**Methodology:** The authors build a self‑hostable API exposing three environmental indicators (CO₂, erosion, land‑cover) for Spain and Portugal and define 16 API‑backed tools (search, buffer, raster query, etc.). Seven frontier and open‑weight LLMs are prompted to solve each task via tool‑calling chains under three temperature‑1.0 seeds; performance is measured as binary task success and plotted against per‑case inference cost.  

**Key Findings:** Claude Sonnet 4 attains the highest accuracy (≈ 61 %) but at a premium cost, while DeepSeek V3.2 achieves ~56 % accuracy at 1/11 the cost, placing open‑weight models on the cost‑efficiency frontier. All models fail completely on close‑value comparison tasks, revealing a systematic limitation in numeric reasoning within tool‑calling agents. Moreover, benchmark scores are 25–35 points lower than on generic GIS tests, indicating that real‑API tool calling provides a far more discriminative evaluation for agentic AI in environmental analysis.


<details>
<summary>Abstract</summary>

Environmental scientists spend disproportionate effort on data wrangling rather than analysis, and AI agents that automate geospatial workflows remain unvalidated: no benchmark evaluates agents operating through structured tool calling against real APIs. We introduce the GeoNatureAgent Benchmark, the first benchmark for environmental analysis agents that operate via structured tool calls to a production-style geospatial API. It comprises 93 tasks across 18 categories, covering municipality analysis, multi-turn conversation, spatial reasoning, cross-indicator synthesis, error handling and recovery, ranking, comparison, multilingual understanding, habitat analysis, and task rejection. Tasks are evaluated against an open, self-hostable API serving three environmental indicators across Spain and Portugal via sixteen tools. We evaluate seven LLMs (Claude Sonnet 4, DeepSeek V3.2, GLM-5, Gemini 2.5 Pro, Qwen3-235B, GPT-OSS-120B, Llama 4 Scout) under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. We find: (1) Claude Sonnet 4 leads at 60.8% +/- 0.8%, followed by DeepSeek V3.2 at 56.3% +/- 3.1%, with no other model above 51%; (2) the cost-accuracy Pareto frontier is occupied mostly by open-weight models, with DeepSeek V3.2 offering 93% of Claude's capability at 11x lower cost ($0.011/case); (3) comparison tasks remain universally unsolved (0% on close-value comparisons), exposing systematic reasoning limits; and (4) structured tool calling against a real API is more discriminative than general-purpose GIS benchmarks, with accuracies 25-35 points lower. We further show extensibility by integrating BigEarthNet V2 land cover for Portugal alongside Spanish CO2 and erosion indicators. The benchmark, harness, and self-hostable API are publicly available.

</details>


### 70. The Containment Gap: How Deployed Agentic AI Frameworks Fail Public-Facing Safety Requirements

- **Authors:** Md Jafrin Hossain, Mohammad Arif Hossain, Weiqi Liu, Nirwan Ansari
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12797v1](http://arxiv.org/abs/2606.12797v1)
- **PDF:** [https://arxiv.org/pdf/2606.12797v1](https://arxiv.org/pdf/2606.12797v1)
- **Categories:** cs.AI


> **Main contribution:**  
The paper reveals a systemic “containment gap” in today’s publicly deployed agentic AI frameworks—LangChain, AutoGPT, and the OpenAI Agents SDK—by showing that none of them natively enforce the six architectural safety principles needed for secure tool‑using, memory‑persistent LLM agents.

**Methodology:**  
The authors formalize six containment principles from a compositional model of agentic systems, audit the three frameworks for compliance, and then conduct controlled memory‑poisoning experiments on a simulated government‑benefits agent built with LangChain. They measure the effect of a single corrupted memory entry on wrongful denial rates and evaluate detection difficulty under realistic policy constraints.

**Key findings:**  
- All three frameworks lack built‑in memory‑integrity safeguards, enabling a single poisoned write to cause persistent targeted failures (up to 88.9 % wrongful denials for selected applicants).  
- The attack remains stealthy, preserving overall accuracy while inflating targeted error rates by 3.5×.  
- Introducing two lightweight defenses—a memory‑integrity validator and a policy gate—neutralizes the attacks with negligible latency (<0.2 ms per call).  

The results suggest that current agentic AI toolkits are not “secure‑by‑default” for high‑stakes, public‑facing use, and they outline concrete architectural upgrades needed to achieve trustworthy deployment.


<details>
<summary>Abstract</summary>

Agentic large language model systems that autonomously invoke tools, maintain persistent memory, and execute multi-step plans are increasingly deployed in public-facing domains, including government services, healthcare triage, and financial advising. We ask whether the frameworks used to build these systems provide architectural-level structural safety guarantees. Applying six containment principles derived from a compositional model of agentic architectures, we audit three dominant frameworks (LangChain, AutoGPT, and OpenAI Agents SDK) and find no native compliance in any of them. Memory integrity, a defense against one of the most prevalent vulnerability classes, is not observed in any of the three evaluated frameworks. We validate these findings empirically: in a simulated government benefits agent built on LangChain, a single memory-poisoning write induces persistent targeted corruption across all tested seeds and backends, increasing the wrongful denial rate for targeted applicants to 88.9%. Under a complex five-factor policy, the same attack preserves aggregate accuracy while increasing targeted wrongful denials by 3.5x, rendering the corruption difficult to detect through standard monitoring. We then introduce two lightweight containment mechanisms: a memory integrity validator and a policy gate, which eliminate both attack vectors with sub-millisecond overhead (<0.2ms per call). We conclude that the current agentic framework ecosystem may not yet meet secure-by-default expectations for public-facing deployments and outline priority architectural interventions to enable trustworthy deployment in high-stakes, socially impactful applications.

</details>


### 71. ProPlay: Procedural World Models for Self-Evolving LLM Agents

- **Authors:** Yijun Ma, Zehong Wang, Yiyang Li, Ziming Li, Xiaoguang Guo, Weixiang Sun, Chuxu Zhang, Yanfang Ye
- **Published:** 2026-06-11
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12780v1](http://arxiv.org/abs/2606.12780v1)
- **PDF:** [https://arxiv.org/pdf/2606.12780v1](https://arxiv.org/pdf/2606.12780v1)
- **Categories:** cs.LG, cs.CL


> **Contribution:** The paper introduces **ProPlay**, a procedural world‑model framework that lets large‑language‑model (LLM) agents “pre‑play’’ abstracted procedures before acting and continuously update a **procedure graph** that encodes causal task stages together with reliability embeddings.  

**Methodology:** ProPlay extracts successful action sequences from experience, abstracts them into high‑level procedures, and links them in a graph whose edges store task‑specific reliability scores. At the start of each episode the agent simulates (soft‑plays) prospective procedural paths over this graph to obtain structured guidance; after execution it refines the graph using the observed outcomes, thereby closing the loop between planning and memory.  

**Findings:** Across several public partially‑observable benchmarks, agents equipped with ProPlay achieve higher environment understanding and faster self‑evolution than strong baseline LLM‑agent methods, demonstrating that procedural abstraction and iterative graph refinement markedly improve autonomous exploration and learning without external supervision.


<details>
<summary>Abstract</summary>

Self-evolving agents are expected to improve through interaction without external supervision, but this remains difficult in partially observable environments where agents must explore actively, learn from limited feedback, and decide when to trust prior experience. Existing LLM-agent methods often rely on memory or planning modules, yet they rarely close the loop between them to continually refine an internal understanding of environment dynamics. We introduce ProPlay, a procedural world model that supports procedure-level preplay, where agents can rehearse future procedural paths using the learned world knowledge. Rather than representing experience as isolated rules or low-level action constraints, ProPlay abstracts successful trajectories into procedures and organizes them in a procedure graph that captures causal transitions among task stages. Each transition is associated with a reliability record embedding to estimate its task-specific contribution from past outcomes. Before each episode, ProPlay simulates future procedural trajectories over known graph structures as structured soft guidance; after execution, it refines the graph using environment feedback. Experiments on public benchmarks show that ProPlay consistently improves environment understanding and self-evolution capability over strong baselines. Our code has been released in https://github.com/antman9914/proplay.

</details>


### 72. Agent-based models for the evolution of morphological alternation patterns

- **Authors:** Aravinth Kulanthaivelu, Richard Sproat
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12748v1](http://arxiv.org/abs/2606.12748v1)
- **PDF:** [https://arxiv.org/pdf/2606.12748v1](https://arxiv.org/pdf/2606.12748v1)
- **Categories:** cs.CL


> This paper introduces a large‑scale, multi‑agent simulation that models how lexical and phonological innovations can give rise to stable stem‑alternation and inflection‑alternation patterns (e.g., English *go* → *went*).  Agents interact over realistic social networks; when an agent hears a novel form for a grammatical slot it may adopt it (with a Bernoulli probability) and propagate the form to other slots that share the same original stem, allowing alternations to spread and become entrenched.  To assess realism, the authors devise the **AI Historical Linguist**—a LLM‑driven debate system that judges evolved morphologies against attested ones—and find that scale‑free networks and random adoption policies yield the most plausible morphologies; they also validate the model with three historical case studies.


<details>
<summary>Abstract</summary>

Why is the past of English "go" the apparently unrelated "went"? Such alternations are frequent in languages. They neither aid communication nor learnability, yet they can be persistent, surviving over centuries or millennia.
  We present a multi-agent simulation of the emergence of morphological stem and inflection alternations. Alternate forms arise by phonological changes or, as with "go/went", from lexical alternatives associated with a subset of the population. When an agent 'hears' another agent use a novel form for a slot in the paradigm of a word (say, the past tense of go), they will with some probability adopt that form, possibly spreading its use to other slots in the paradigm that shared the same original form. Thus alternative forms can spread through the population and become entrenched as stem or inflectional marker alternants. Unlike many previous computational studies, our system allows for naturalistic lexical forms, realistic phonological rules, lexicons with hundreds or thousands of entries, and agent populations in the tens or hundreds. It supports several network topologies, diffusion patterns and agent adoption policies.
  One issue with such simulations is evaluation: how realistic is the resulting morphology compared to those of real languages? We introduce the AI Historical Linguist, a novel Large Language Model-driven system that models a debate between two historical linguists. We use this to compare a set of real language morphologies, disguised morphologies, and experimentally evolved morphologies. The results suggest that among the factors that favor more plausible morphologies are scale-free social networks and random Bernoulli adoption of forms.
  We also present three case studies modeling attested historical changes, allowing us to test what might have happened if history had been different.
  All code and data are released.

</details>


### 73. PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections

- **Authors:** Pengfei He, Lesly Miculicich, Vishesh Sharma, Ash Fox, George Lee, Jiliang Tang, Tomas Pfister, Long T. Le
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12737v1](http://arxiv.org/abs/2606.12737v1)
- **PDF:** [https://arxiv.org/pdf/2606.12737v1](https://arxiv.org/pdf/2606.12737v1)
- **Categories:** cs.CR, cs.AI


> **PI‑Hunter** introduces an automated red‑teaming framework that actively audits LLM‑driven agents for hidden prompt‑injection vulnerabilities. It generates realistic, source‑aware test cases and iteratively refines them via feedback‑driven exploration, forcing the agent to retrieve and expose malicious instructions embedded in external tools or environments. Experiments on several benchmarks and agent architectures show that PI‑Hunter uncovers far more latent injections and broader attack surfaces than existing automated red‑teamers, and it remains effective even when standard prompt‑injection defenses are applied.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are rapidly evolving into agentic systems that interact with external tools and environments, introducing new security risks such as indirect prompt injection attacks through untrusted external sources. Existing defenses mainly focus on blocking malicious content at inference time, and current red-teaming methods primarily optimize attack success. As a result, developers have limited visibility into how latent prompt injections emerge and propagate through agents. We propose PI-Hunter, an automated agentic auditing framework for proactive vulnerability exposure in LLM agents. PI-Hunter constructs realistic source-aware test cases and iteratively evolves them through feedback-driven exploration to induce agents to retrieve and reveal latent malicious instructions embedded within external environments. Extensive experiments across multiple benchmarks, agent architectures, attacks, and defenses demonstrate that PI-Hunter substantially improves vulnerability exposure and attack-surface coverage over strong automated red-teaming baselines, while remaining effective under existing prompt injection defenses.

</details>


### 74. Benchmarking AI Agents for Addressing Scientific Challenges Across Scales

- **Authors:** Tianyu Liu, Allen Xin Wang, Antonia Panescu, Lisa Xinyi Chen, Wenxin Long, Xinyu Wei, Yueqian Jing, Ziyao Zeng, Jihang Chen, Sihan Jiang, Ziqing Wang, Siyi Gu, Siyu Chen, Xinyang Hu, Haoran Shao, Leqi Xu, Wangjie Zheng, Zhiyuan Cao, Ada Fang, Botao Yu, Kunyang Sun, Rex Ying, Arman Cohan, Qingyu Chen, Lingzhou Xue, Kaize Ding, Yuanqi Du, Wengong Jin, Zhuoran Yang, Marinka Zitnik, James Zou, Hua Xu, Hongyu Zhao
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12736v1](http://arxiv.org/abs/2606.12736v1)
- **PDF:** [https://arxiv.org/pdf/2606.12736v1](https://arxiv.org/pdf/2606.12736v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper presents **SciAgentArena**, a large‑scale, interactive benchmark (≈200 step‑wise scientific tasks across many domains) designed to evaluate AI agents in realistic research workflows rather than isolated, static problems.  

**Methodology:** The authors construct an agent‑agnostic environment that supplies incremental verification cues and allows agents to act, query, and receive feedback, then test a suite of contemporary AI agents (including chain‑of‑thought LLMs and tool‑augmented planners) on the benchmark.  

**Key findings:** Current agents perform well on tightly scoped, well‑specified data‑analysis pipelines, but they falter on open‑ended scientific challenges—showing difficulty in producing novel hypotheses, maintaining self‑directed exploration, and delivering robust solutions. The study outlines recurring failure modes (e.g., over‑reliance on prompt cues, brittle tool usage) and highlights the need for stronger autonomous reasoning and reliability mechanisms to advance agentic AI for science.


<details>
<summary>Abstract</summary>

AI agents are increasingly being developed to accelerate scientific discovery, yet their practical capabilities in real research settings remain poorly understood. Existing benchmarks for AI agents rarely capture the complexity, heterogeneity, and extended reasoning required by scientific work, whereas benchmarks for scientific tasks often reduce research to static, direct problems and provide limited support for interactive evaluation. Here, we introduce SciAgentArena, a systematic benchmark for evaluating AI agents in real-world scientific research scenarios drawn from emerging needs across multiple domains. SciAgentArena comprises approximately 200 tasks with stepwise verification and an interactive, agent-agnostic environment for assessing diverse AI agents. Using this benchmark, we find that current agents can contribute effectively to well-specified data-analysis workflows, particularly when the task structure and evaluation criteria are clear. However, their performance remains uneven across scientific contexts: agents struggle to generate genuinely novel insights, sustain self-directed exploration, and formulate robust solutions for open-ended research questions. We further characterize common failure modes across agents and identify opportunities for improving their reliability, autonomy, and scientific reasoning. Together, SciAgentArena provides a practical framework for measuring progress in AI agents for science and for guiding the design of future agents capable of addressing complex scientific challenges. Full codes, tasks, and datasets can be accessed via this link: https://sciagentarena.github.io/.

</details>


### 75. Smarter Saboteurs, Better Fixers: Scaling & Security in Linear Multi-Agent Workflows

- **Authors:** Timothy McAllister, Sina Abdidizaji, Ivan Garibay, Ozlem Ozmen Garibay
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12709v1](http://arxiv.org/abs/2606.12709v1)
- **PDF:** [https://arxiv.org/pdf/2606.12709v1](https://arxiv.org/pdf/2606.12709v1)
- **Categories:** cs.MA, cs.CR, cs.LG


> **Contribution** – The paper shows that the security of linear LLM‑based multi‑agent pipelines is strongly affected by model size, but that a simple “Fixer” agent can neutralize the vulnerability, overturning the belief that linear collaboration is intrinsically brittle.  

**Methodology** – The authors evaluate two open‑weight LLM families at several scales (≈1 B‑27 B parameters) on the HumanEval benchmark, inserting a malicious prompt‑injection attack into a middle agent of a three‑stage linear workflow (Generator → Saboteur → Fixer). They compare performance on clean (control) versus compromised runs, both with and without the Fixer stage.  

**Key Findings** – Larger models obey malicious instructions far more readily (performance drop up to 53.7 percentage points at 27 B without correction), yet adding a lightweight terminal Fixer reduces the drop to only 0.6 pp, restoring parity with the clean baseline. This demonstrates a compliance‑correction symmetry: scaling amplifies both sabotage and correction capabilities, and linear MAS can be made robust simply by appending a corrective agent.


<details>
<summary>Abstract</summary>

As LLM-based multi-agent systems (MAS) are deployed in the wild, the resilience of their collaboration structures against adversarial compromise becomes a critical safety concern. Attackers may leverage prompt-injection or jailbreaking to sabotage individual agents within MAS workflows, but the interaction between model scaling and system-level resilience remains poorly understood. This paper investigates how model scale affects the security of linear multi-agent workflows. Our experiments across scales of two open-weight model families on the HumanEval benchmark reveal a compliance-correction symmetry: larger models are far more likely to faithfully execute malicious instructions, with the control-to-malicious performance drop reaching 53.7pp at 27B in uncorrected pipelines. However, appending a lightweight terminal Fixer stage collapses this to 0.6pp and restores statistical parity with control-level performance, demonstrating that strictly linear collaboration structures can be viable and resilient to adversaries at this scale, and suggesting that the brittleness previously attributed to linear topology may stem from a lack of correction.

</details>


### 76. SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems

- **Authors:** Tarun Sharma
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12703v1](http://arxiv.org/abs/2606.12703v1)
- **PDF:** [https://arxiv.org/pdf/2606.12703v1](https://arxiv.org/pdf/2606.12703v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> The paper introduces **Signed Memory with Smoothed Retrieval (SMSR)**, the first defense that provides a *certified robustness guarantee* against Multi‑Session Memory Poisoning (MSMP) in retrieval‑augmented LLM agents that maintain persistent memory across user sessions. SMSR combines (1) an HMAC‑SHA256 provenance tag on every memory write to block any unsigned injection, and (2) a randomized memory‑ablation plus verdict‑based majority voting at query time, for which the authors derive a hypergeometric certification bound and prove that no provenance‑free filter can achieve such guarantees. Empirical evaluation on 15 enterprise scenarios shows that unsigned attacks drop from ~93‑100 % success to 0 %, while an authenticated adversary’s success falls to 8 % (within the certified worst‑case) and overall query utility remains high (≈90 % for Component 1 and 85 % when both components are applied).


<details>
<summary>Abstract</summary>

Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions. This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights or code. We call this Multi-Session Memory Poisoning (MSMP) and show that no existing defence certifies against it; static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base, and heuristic filters are bypassed by fluent enterprise-style text. We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting. Component 1 adds HMAC-SHA256 provenance at write time, blocking unsigned injection. Component 2 applies randomised memory ablation with verdict-based majority voting at query time, bounding the influence of authenticated adversaries. We prove that no provenance-free retrieval-time filter can certify against adaptive injection, derive a hypergeometric certificate for Component 2, and formalise the Consistent Minority Effect, whereby a consistent adversarial answer wins string-based voting as a numerical minority while verdict-based voting removes it. Across 15 enterprise scenarios (3,150 repeated trials), Component 1 cuts attack success from 93-100% to 0% for all unsigned variants. For an authenticated adversary with a single injection, Component 2 holds success to 8.0% (95% CI [5.8, 10.9], n=450), below the certified worst case. In an end-to-end query-only attack where the agent itself writes the poison rather than it being pre-seeded, SMSR reduces success from 65.3% to 5.3% (n=150, non-overlapping CIs) on a live agent stack. Clean-query utility is 90% (Component 1) and 85% (combined).

</details>


### 77. From AGI to ASI

- **Authors:** Tim Genewein, Matija Franklin, Alexander Lerchner, Laurent Orseau, Samuel Albanie, Adam Bales, Cole Wyeth, Stephanie Chan, Iason Gabriel, Joel Z. Leibo, Allan Dafoe, Marcus Hutter, Thore Graepel, Shane Legg
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12683v1](http://arxiv.org/abs/2606.12683v1)
- **PDF:** [https://arxiv.org/pdf/2606.12683v1](https://arxiv.org/pdf/2606.12683v1)
- **Categories:** cs.AI, cs.CY, cs.LG


> The paper delineates the expected transition from human‑level artificial general intelligence (AGI) to artificial superintelligence (ASI), defining ASI as any system that surpasses large human organisations in intelligence and cognition. It proposes a taxonomy of four plausible pathways—raw scaling of AGI models, paradigm‑shifting innovations, recursive self‑improvement, and emergent capabilities from massive multi‑agent collectives—and identifies technical and institutional frictions that could accelerate or stall each route. Empirical analysis of current scaling trends and theoretical models of universal AI suggest that, rather than a single abrupt breakthrough, a cascade of accelerating, AI‑driven advances is more likely, underscoring the need for interdisciplinary, global preparation for the societal impact of ASI.


<details>
<summary>Abstract</summary>

Over the last decade, building human-level artificial general intelligence has moved from far-fetched speculation to being a concrete next-decade target for many of the largest AI organisations. Achieving this goal would have profound and far-reaching impacts on human society, which raises many complex questions for the decade ahead. This report investigates how AI itself might continue to develop in a post-AGI world along the continuum of machine intelligence. The endpoint of this continuum, Universal AI, is theoretically well understood, which provides some formal grounding for the main focus of this report: the transition from human-level AGI to artificial general superintelligence, which, intuitively, can be understood as a system that is more intelligent and cognitively capable than large organisations of humans. After characterizing ASI, the report discusses four potential pathways from AGI to ASI: scaling AGI, AI paradigm shifts, recursive improvement, and ASI emerging from large-scale multi-agent collectives. The report then discusses possible frictions and bottlenecks along these pathways. Determining whether the impact of these frictions will be negligible or substantial raises a number of concrete open research questions. Due to large uncertainties for predicting ASI progress, it cannot be ruled out that AI progress might continue to accelerate over the next years. This could imply that the image of a single transformative step change, caused by the introduction of human-level AGI into our society, could be inaccurate. More apt might be the prospect of a series of transformative societal changes caused by AI-enabled progress and breakthroughs across many areas of science and technology. Preparing for this prospect requires a massively interdisciplinary endeavour of global scope and interest.

</details>


### 78. Evoflux: Inference-Time Evolution of Executable Tool Workflows for Compact Agents

- **Authors:** Kushal Raj Bhandari, Ling Yue, Ching-Yun Ko, Dhaval Patel, Shaowu Pan, Pin-Yu Chen, Jianxi Gao
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12674v1](http://arxiv.org/abs/2606.12674v1)
- **PDF:** [https://arxiv.org/pdf/2606.12674v1](https://arxiv.org/pdf/2606.12674v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Evoflux**, an inference‑time evolutionary search algorithm that repairs and refines the executable tool‑workflow graphs generated by compact language‑model planners, enabling them to reliably discover, validate, sequence, and execute tools from dynamic catalogs.

**Methodology:** Evoflux treats a workflow as a typed graph and iteratively applies structured edit operators (adding/removing nodes, fixing parameter types, re‑routing dependencies) guided by execution feedback. It uses adaptive edit intensity, meta‑learned redesign heuristics, and diversity‑based pruning to evolve feasible plans at runtime, without requiring large teacher‑trace corpora.

**Key findings:** Across the MCP‑Bench benchmark (live tool‑calling servers, ≈250 tools), Evoflux lifts the proportion of plans that actually execute from ∼3 % (baseline small planners) to **17–24 %**, outperforming fine‑tuned (SFT/DPO) models and matching or exceeding zero‑shot ReAct while using fewer tokens and exhibiting lower variance. This demonstrates that execution‑grounded evolutionary search is an effective, low‑budget strategy for making compact agents robust to evolving tool environments.


<details>
<summary>Abstract</summary>

Compact language models (LMs) reduce cost, latency, and deployment risk for tool agents. Yet MCP-style tool use requires more than isolated function calling: an agent must discover tools from live catalogs, satisfy schemas, preserve dependencies across intermediate outputs, and ground final responses in executed evidence. Small planners often generate plausible workflow graphs that fail under tool resolution, parameter validation, dependency tracking, or execution. We argue that this failure mode is poorly handled by small-corpus distillation. A few hundred teacher traces can teach workflow format, but rarely cover the recovery behavior needed to repair failed plans over changing tool catalogs. We introduce Evoflux, an inference-time evolutionary search method that treats compact tool use as the repair of executable tool workflows. It evolves typed workflow graphs through structured edits, execution feedback, adaptive intensity, meta-guided redesign, and diversity pruning. On held-out MCP-Bench tasks spanning live MCP servers and 250 tools, Evoflux raises execution feasibility from roughly 3% to 17-24% across small planners. In contrast, SFT and SFT+DPO on the same search-mined data match, underperform, or collapse below zero-shot performance; ReAct reaches higher peaks, but with higher variance and token cost. These results show that execution-grounded search is more reliable under scarce teacher-trace budgets.

</details>


### 79. TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation

- **Authors:** Siyu Li, Toan Tran, Lingyi Zhao, Khurram Shafique, Li Xiong
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12657v1](http://arxiv.org/abs/2606.12657v1)
- **PDF:** [https://arxiv.org/pdf/2606.12657v1](https://arxiv.org/pdf/2606.12657v1)
- **Categories:** cs.AI, cs.DB, cs.RO


> TrajGenAgent introduces a hierarchical LLM‑agent that generates realistic, individual‑specific human mobility trajectories without any model fine‑tuning. The system first uses an LLM orchestrator (via in‑context learning) to produce a weekday‑conditioned activity chain from a user’s historical data, then a deterministic worker grounds each activity into a full visit by retrieving personalized POIs, selecting locations with distance constraints, propagating travel times kinematically, and estimating activity durations with another LLM call. Across benchmark and large‑scale simulation datasets, the approach markedly outperforms neural and LLM‑based baselines in spatio‑temporal fidelity, semantic coherence, and behavioral plausibility, as measured by a novel anomaly‑detection‑based evaluation, while incurring no parameter updates.


<details>
<summary>Abstract</summary>

Human mobility data is important for transportation, urban planning, and epidemic control, but large-scale trajectory collection is often costly and privacy-constrained, motivating realistic synthetic trajectory generation. Existing LLM-based generators typically rely on either prompt engineering, which preserves zero-shot reasoning but lacks fine-grained spatiotemporal grounding, or trajectory-level fine-tuning, which improves statistical precision but incurs substantial computational cost and may weaken general reasoning. We propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for human mobility trajectory generation without model fine-tuning. TrajGenAgent uses a two-stage orchestrator-worker design: an LLM first synthesizes an individual- and weekday-conditioned activity chain from historical evidence via in-context learning, and a deterministic workflow then grounds each activity into a complete visit using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation, and LLM-based duration estimation. To evaluate realism beyond aggregate spatiotemporal statistics, we introduce an anomaly-detection-based evaluation framework using two complementary detectors to assess behavioral and semantic plausibility. Experiments on benchmark and large-scale simulation datasets show that TrajGenAgent improves spatiotemporal fidelity, semantic coherence, and individual-specific behavioral realism over representative neural and LLM-based baselines, while avoiding parameter updates.

</details>


### 80. Individual Control Barrier Functions-Guided Diffusion Model for Safe Offline Multi-Agent Reinforcement Learning

- **Authors:** Qingyun Guo, Junyi Shi, Jianuo Huang, Tianyu Shi
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12640v1](http://arxiv.org/abs/2606.12640v1)
- **PDF:** [https://arxiv.org/pdf/2606.12640v1](https://arxiv.org/pdf/2606.12640v1)
- **Categories:** cs.LG, cs.RO, eess.SY


> The paper introduces the first diffusion‑based offline RL algorithm that guarantees safety in multi‑agent settings by integrating **neural individual Control Barrier Functions (CBFs)** directly into the diffusion generative model.  During training, the diffusion model learns to reconstruct whole joint trajectories from offline data, while the embedded CBFs act as learnable safety critics that bias the reverse diffusion sampling toward states and actions that satisfy each agent’s safety constraints; the final policies are extracted via an inverse‑dynamics network.  Experiments on several multi‑agent benchmarks show that the method preserves or improves task performance while reducing unsafe events by orders of magnitude compared with prior diffusion‑offline and model‑based baselines, establishing a scalable way to embed formal safety guarantees into offline multi‑agent RL.


<details>
<summary>Abstract</summary>

Offline reinforcement learning allows control policies to be learned directly from data without online interaction, making it suitable for safety-critical tasks. Recent studies have applied diffusion models to offline reinforcement learning to leverage their strong capacity for modeling complex data distributions. However, existing approaches primarily focus on single-agent settings, leaving the safety challenges in multi-agent environments largely unexplored. In this work, we propose a safe offline multi-agent reinforcement learning algorithm that embeds neural individual control barrier functions into the diffusion model to enhance safety during trajectory generation, with control policies recovered through inverse dynamics. We evaluate our algorithm across diverse benchmarks, demonstrating substantial safety improvements while maintaining competitive rewards.

</details>


### 81. Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents

- **Authors:** Tianyu Ding, Jianhong Xin, Juan Pablo De la Cruz Weinstein
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12634v1](http://arxiv.org/abs/2606.12634v1)
- **PDF:** [https://arxiv.org/pdf/2606.12634v1](https://arxiv.org/pdf/2606.12634v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces **Sibling‑Guided Credit Distillation (SGCD)**, a new credit‑assignment technique that blends token‑level self‑distillation with policy‑gradient reinforcement learning to improve long‑horizon tool‑use agents. SGCD dynamically generates “sibling” rollouts (both successful and failed), uses an external LLM to summarize the contrast into stepwise credit signals, and incorporates these dense credits as bounded, detached weights that reshape the GRPO token advantages, without requiring the external LLM at deployment. Experiments on the AppWorld and τ³‑airline benchmarks show that SGCD consistently outperforms strong GRPO baselines, raising AppWorld TGC from 42.9 → 45.6 (test_normal) and 24.7 → 27.0 (test_challenge), and improving τ³‑airline pass@1 from 0.583 → 0.602.


<details>
<summary>Abstract</summary>

Long-horizon tool-use reinforcement learning can learn from outcome verification, but its
  trajectory-level advantage is broadcast across many reasoning, API, and answer tokens.
  Self-distillation promises a denser signal by reusing a policy's own rollouts or a privileged
  teacher. We show, however, that direct token-level self-distillation can silently destroy tool use:
  it rehearses teacher behavior without knowing which actions the verifier rewards, so useful skills
  and harmful shortcuts are amplified together. We introduce Sibling-Guided Credit Distillation
  (SGCD), which uses distillation for credit assignment rather than as a competing actor loss.
  Dynamic sampling produces mixed successful and failed sibling rollouts; an external LLM summarizes
  their contrast into a training-only stepwise credit reference; dense teacher/student divergence
  drives credit reassignment; and bounded detached credit weights reshape GRPO token advantages. The
  deployed student sees no external LLM, sibling evidence, or oracle. Across AppWorld and
  $τ^3$-airline, SGCD improves over matched GRPO comparators: AppWorld TGC $42.9 \to 45.6$ on
  test_normal and $24.7 \to 27.0$ on test_challenge, and $τ^3$-airline pass@1 $0.583 \to 0.602$.

</details>


### 82. Strategic Decision Support for AI Agents

- **Authors:** Shayan Kiyani, Sima Noorani, George Pappas, Hamed Hassani
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12587v1](http://arxiv.org/abs/2606.12587v1)
- **PDF:** [https://arxiv.org/pdf/2606.12587v1](https://arxiv.org/pdf/2606.12587v1)
- **Categories:** cs.AI, cs.HC


> **Main contribution:** The paper introduces a “strategic decision‑support” framework that treats AI agents—not humans—as the primary decision makers and formalizes how, when, and how often they should query external support (human input, tools, or additional data) while keeping the risk of an unsupported but improvable error under a user‑specified bound.

**Methodology:** The authors cast the problem as an optimization that minimizes the expected number of support calls subject to a constraint on the *counterfactual missed‑support error* (the probability the agent acts alone on an instance where support would have meaningfully improved its output). They prove that the optimal policy is a simple threshold on a learned “value‑of‑support” score, and they develop an online, distribution‑free algorithm that (i) continuously estimates this score, (ii) adaptively adjusts the threshold using randomized exploration to satisfy the error constraint, and (iii) incorporates an on‑the‑fly calibration step to discard unnecessary support requests.

**Key findings:** Across three domains—information‑gathering, human‑AI collaborative decision making, and tool‑augmented agents—the proposed algorithm consistently respects the prescribed missed‑support error while cutting support usage by 30‑70 % compared with baseline heuristics and static thresholds, demonstrating that reliable, low‑cost support can be achieved for agentic AI systems without strong distributional assumptions.


<details>
<summary>Abstract</summary>

Traditionally, decision support studies how humans use machine learning models to make better decisions. In modern agentic systems, this division of roles is increasingly reversed: AI agents act on behalf of users, while humans and tools becomes support mechanisms around them. This role reversal brings reliability concerns to the forefront, since agentic errors can be consequential and agent behavior must remain aligned with human goals and constraints. Departing from the classical view of decision support, we revisit its two basic principles, the cost--value tradeoff of seeking support and the role of uncertainty quantification, in a setting where AI agents are the central actors. We propose a framework for strategic decision support for AI agents through an optimization problem that minimizes support usage subject to controlling a counterfactual missed-support error: the probability that the agent acts alone on instances where support would have materially improved its output. At the population level, we show that the optimal policy is a threshold rule on the value of support. Building on this structure, we develop an online algorithm that adaptively thresholds such a score and uses randomized exploration to control missed-support error without distributional assumptions. We further introduce a calibration-on-the-fly method that reduces unnecessary support calls online. We instantiate this framework across diverse scenarios, including information gathering, human--AI collaboration, and tool use, showing how each can be modeled through the same strategic decision-support lens. Experiments across these settings show that our method reliably controls the target error while substantially reducing support usage in practice.

</details>


### 83. Arbor: Tree Search as a Cognition Layer for Autonomous Agents

- **Authors:** Neha Prakriya, Chaojun Hou, Zheng Gong, Huasha Zhao, Xi Zhao, Mou Li, Zhenyu Gu, Emad Barsoum
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12563v1](http://arxiv.org/abs/2606.12563v1)
- **PDF:** [https://arxiv.org/pdf/2606.12563v1](https://arxiv.org/pdf/2606.12563v1)
- **Categories:** cs.AI


> Arbor introduces a structured tree‑search “cognition layer” that serves as a shared, mutable working memory for a team of autonomous agents tackling large, stateful optimization problems. By representing hypotheses as nodes in a scored search tree and letting an Orchestrator delegate to domain‑specialist agents while a Critic continuously validates measurements and performs root‑cause analysis, Arbor turns failures into diagnostic signals that reshape exploration and successes into expanding branches that shift the bottleneck distribution. Applied to full‑stack LLM inference optimization, this methodology yields up to 193 % Pareto‑optimal throughput‑latency gains over vendor‑tuned baselines—far surpassing the +33 % ceiling of a single monolithic agent—and demonstrates hardware‑agnostic reproducibility with ≤2 % run‑to‑run variance.


<details>
<summary>Abstract</summary>

Arbor is a multi-agent framework that introduces structured tree search as a cognition layer for autonomous agents operating in large, stateful action spaces. Prior autonomous optimization systems operate on isolated targets with stateless evaluation. Arbor instead maintains an explicit search tree of scored hypotheses that serves as the shared working memory across agents, evolving with every measurement, treating failures as diagnostic signal that reshapes subsequent exploration, and expanding as prior successes shift the bottleneck distribution.
  We validate Arbor on full-stack LLM inference optimization, a domain where achieving peak performance has historically required coordinated effort from engineering teams across the application, framework, compiler, kernel, and hardware stack. Arbor pairs an Orchestrator agent, which drives optimization by delegating to Domain Specialists across the inference stack, with a Critic agent that safeguards stability through root-cause analysis, introspection, and measurement validation -- a checks-and-balances architecture where neither agent can unilaterally drive the system. Agent capabilities are decomposed into hard skills (domain expertise) and soft skills (coordination protocols that determine how contributions compose), enabling fully autonomous multi-day campaigns. Arbor achieves up to 193% inference throughput-latency Pareto improvement over vendor-optimized baselines, while a single agent without the harness plateaus at +33% throughput improvement and crashes irrecoverably within hours. Arbor generalizes to multiple generations of hardware platform, and run-to-run variance is within 2 percentage points demonstrating that the method is hardware-agnostic and reproducible.

</details>


### 84. APPO: Agentic Procedural Policy Optimization

- **Authors:** Xucong Wang, Ziyu Ma, Yong Wang, Yuxiang Ji, Shidong Yang, Guanhua Chen, Pengkun Wang, Xiangxiang Chu
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12384v1](http://arxiv.org/abs/2606.12384v1)
- **PDF:** [https://arxiv.org/pdf/2606.12384v1](https://arxiv.org/pdf/2606.12384v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **Agentic Procedural Policy Optimization (APPO)**, a new RL framework that refines where an LLM‑based agent should explore (“branch”) and how credit is allocated by moving from coarse, heuristic units (e.g., tool‑call boundaries) to fine‑grained token‑level decision points. APPO computes a *Branching Score* that blends token‑level uncertainty with the expected gain in policy likelihood for downstream continuations, and employs a *procedure‑level advantage scaling* to spread credit across those branched rollouts. Across 13 multi‑turn tool‑use benchmarks, APPO boosts the performance of strong agentic RL baselines by roughly 4 absolute points while preserving interpretability and keeping tool‑call efficiency.


<details>
<summary>Abstract</summary>

Recent advances in agentic Reinforcement Learning (RL) have substantially improved the multi-turn tool-use capabilities of large language model agents. However, most existing methods assign credit over coarse heuristic units, such as tool-call boundaries or fixed workflows, making it difficult to identify which intermediate decisions influence downstream outcomes. In this work, we study agentic RL from two perspectives: \textit{where to branch and how to assign credit after branching}. Our pilot analysis shows that influential decision points are broadly distributed throughout the generated sequence rather than concentrated at tool calls, while token entropy alone does not reliably reflect their impact on final outcomes. Motivated by these observations, we propose \textbf{Agentic Procedural Policy Optimization (APPO)}, which shifts branching and credit assignment from coarse interaction units to fine-grained decision points in the sequence. APPO selects branching locations using a Branching Score that combines token uncertainty with policy-induced likelihood gains of subsequent continuations, enabling more targeted exploration while filtering out spurious high-entropy positions. It further introduces procedure-level advantage scaling to better distribute credit across branched rollouts. Experiments on 13 benchmarks show that APPO consistently improves strong agentic RL baselines by nearly 4 points, while keeping efficient tool-calls and maintaining behavior interpretability.

</details>


### 85. A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents

- **Authors:** Krti Tallam
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12320v1](http://arxiv.org/abs/2606.12320v1)
- **PDF:** [https://arxiv.org/pdf/2606.12320v1](https://arxiv.org/pdf/2606.12320v1)
- **Categories:** cs.AI, cs.CC, cs.CR, cs.SE


> The paper introduces a “five‑plane” reference architecture that enables runtime governance of production‑grade AI agents by extending traditional policy enforcement to the agentic context. The architecture combines a reasoning plane that adjudicates intent with four enforcement planes (network, identity, endpoint, data), along with stop‑anywhere mediation, composite principals with capability attenuation, and a structured audit substrate; it also defines six interruption primitives and four correctness invariants for safe delegation. In a prototype implementation, the authors show that the system can block seven representative agent‑based threats across five workflows, achieving single‑digit‑microsecond adjudication latency, correct capability attenuation, and tamper‑evident audit trails—demonstrating that stateful, composable policy enforcement is feasible for governing delegated actions of AI agents in enterprise environments.


<details>
<summary>Abstract</summary>

Enterprise security was built to govern data boundaries: the protected surface was data at rest and in transit, and the controls -- access control, data-loss prevention, perimeter inspection -- governed crossings of that boundary. Production AI agents dissolve this assumption. An agent reads context, calls tools, invokes connectors, and modifies systems of record on an enterprise's behalf, so risk moves inside the workflow, into sequences of individually-permitted actions that may transform a business process no one authorized. Existing policy engines do not extend to this regime: they evaluate request-time decisions against atomic principals, where agentic systems require stateful evaluation against composite principals whose authority attenuates through delegation chains.
  We present a reference architecture for the runtime governance of production agents, built from four composable primitives: a five-plane decomposition (a reasoning plane that adjudicates intent, and four enforcement planes -- network, identity, endpoint, data -- that realize the decision), stop-anywhere mediation, composite principals with capability attenuation, and audit as a structured evidence substrate. We define a taxonomy of six interruption primitives that generalize allow and deny, state and argue for four correctness invariants, and demonstrate the foreclosure of seven production-agent threats across five concrete workflows. A reference implementation of the policy-engine core supplies measured evidence: attenuation correctness and evidence reconstructability hold on every trial, adjudication runs in single-digit microseconds, and the audit substrate's tamper-evidence behaves exactly as designed. We are explicit about scope: the architecture governs delegated action, not model behavior, and a full-system evaluation against a live agent benchmark is the invited next step.

</details>


### 86. CCKS: Consensus-based Communication and Knowledge Sharing

- **Authors:** Jinyuan Zu, Xiaowei Lv, Yongcai Wang, Deying Li, Yunjun Han, Wenping Chen, Fengyi Zhang, Naiqi Wu
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12281v1](http://arxiv.org/abs/2606.12281v1)
- **PDF:** [https://arxiv.org/pdf/2606.12281v1](https://arxiv.org/pdf/2606.12281v1)
- **Categories:** cs.MA, cs.AI, cs.LG


> **Main contribution**: The paper introduces **Consensus‑based Communication and Knowledge Sharing (CCKS)**, a plug‑and‑play framework for decentralized multi‑agent reinforcement learning that lets agents selectively follow advice from peers by enforcing a consensus constraint rather than blindly imitating a single teacher.

**Methodology**: CCKS builds a **consensus model** through contrastive learning on agents’ local observations during training; at decision time each agent scores candidate actions using both the consensus model and the shared advice, adopting actions only when they satisfy the consensus‑derived compatibility criteria, thereby balancing exploration with guided learning.

**Key findings**: Integrated into several DTDE baselines, CCKS yields faster convergence, higher cooperation efficiency, and markedly better final scores on both the Google Research Football and StarCraft II Multi‑Agent Challenge benchmarks, demonstrating that consensus‑driven advice selection mitigates over‑reliance on teachers and improves overall agentic performance.


<details>
<summary>Abstract</summary>

In Decentralized Training and Decentralized Execution (DTDE) for cooperative Multi-Agent Reinforcement Learning (MARL), action-advising-based knowledge sharing promotes interpretable and scalable cooperation among agents. However, current action advising approaches often adhere too much to the teacher's guidance without evaluating teacher-student compatibility, which causes excessive advising, suboptimal stability, and degraded performance. To overcome these challenges, this paper presents a Consensus-based Communication and Knowledge Sharing (CCKS) framework, which allows agents to adopt recommendations based on consensus-derived constraints and to follow the teacher's instructions more smartly. This mechanism enables agents to balance exploration and learning from experienced teachers, improving overall performance. The key is the consensus model construction, for which we propose to employ contrastive learning to construct consensus models based on local observations in the agents' training phase. In action selection, agents score and choose actions based on consensus and shared knowledge. Designed as a plug-and-play solution, CCKS integrates seamlessly with existing DTDE algorithms. Experiments conducted in the Google Research Football environment and the complex StarCraft II Multi-Agent Challenge demonstrate that the integration with CCKS significantly improves cooperation efficiency, learning speed, and overall performance compared with current DTDE baselines. The code is available at https://github.com/yuanxpy/CCKS.

</details>


### 87. The Impossibility of Eliciting Latent Knowledge

- **Authors:** Korbinian Friedl, Francis Rhys Ward, Paul Yushin Rapoport, Tom Everitt, Jonathan Richens
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12268v1](http://arxiv.org/abs/2606.12268v1)
- **PDF:** [https://arxiv.org/pdf/2606.12268v1](https://arxiv.org/pdf/2606.12268v1)
- **Categories:** cs.AI


> The paper formalizes the “eliciting latent knowledge” (ELK) problem—getting an advanced AI to truthfully report its beliefs about variables that are hidden from humans—using Causal Influence Diagrams to distinguish observable from latent facts and to define honesty and goal misgeneralisation. It shows that, while perfect feedback can sometimes steer an agent toward honest answers during training, any feedback‑only training procedure that inspects only the agent’s outward behavior cannot guarantee honesty; agents can instead learn to output responses that humans judge as true without actually reflecting their internal beliefs. This impossibility theorem highlights a fundamental limitation for current feedback‑based alignment methods in the development of honest, agentic AI.


<details>
<summary>Abstract</summary>

Advanced AI systems have extensive knowledge of their environments; in fact, their knowledge may (far) exceed that of their developers or users. Consequently, a desirable property for an AI system is that it is honest -- that it accurately reports its beliefs about the world. Designing an AI system to be honest may be difficult, especially if we want to ask it questions about latent variables in the environment -- variables which are hidden from the human interacting with it. This gives rise to the problem of eliciting latent knowledge (ELK): the problem of training an AI agent to honestly report its beliefs. In this paper, we make ELK formally precise using Causal Influence Diagrams (CIDs). CIDs can be used to describe the relationship between an agent's training environment and its subjective representation of the world. We use CIDs to formalise the distinction between observable and latent variables, to specify what exactly it means for an agent to be honest, and to formally define goal misgeneralisation. We show that, under certain circumstances, developers can incentivise an agent to honestly answer questions by providing correct feedback during training. However, a natural, but undesirable, way for an agent to generalise is to provide answers which humans would evaluate as true, rather than honest answers. We prove an impossibility theorem stating: There is no feedback-based training strategy that depends only on agent behaviour and with certainty produces an honest agent, even if feedback is perfect during training.

</details>


### 88. Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application

- **Authors:** Jiachun Li, Zhuoran Jin, Tianyi Men, Yupu Hao, Kejian Zhu, Lingshuai Wang, Dongqi Huang, Longxiang Wang, Shengjia Hua, Lu Wang, Jinshan Gao, Hongbang Yuan, Ruilin Xu, Kang Liu, Jun Zhao
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12191v1](http://arxiv.org/abs/2606.12191v1)
- **PDF:** [https://arxiv.org/pdf/2606.12191v1](https://arxiv.org/pdf/2606.12191v1)
- **Categories:** cs.CL, cs.AI


> The paper provides the first comprehensive survey of “agentic environments” for LLM‑based agents, structuring the field into a life‑cycle of environment modeling, automatic synthesis, evaluation, and application. It classifies existing benchmarks along eight attributes and domains, distinguishes symbolic versus neural synthesis pipelines (with corresponding evaluation protocols), and maps how dynamic environments drive four modes of agent evolution (memory‑centric, orchestration‑centric, trajectory‑centric, and exploration‑centric) while identifying three drivers of environment change (neural‑driven, difficulty‑driven, scaling‑driven). Empirically, the survey shows that tightly coupling environment design with agent training yields measurable gains in reasoning, planning, and adaptability, and it outlines future research avenues such as Environment‑as‑a‑Service, multi‑agent ecosystems, and neural‑symbolic hybrid worlds.


<details>
<summary>Abstract</summary>

Environments serve as interactive systems for large language model (LLM) based agents across diverse scenarios and play a crucial role in driving the continual evolution of model capabilities. Despite this importance, existing work lacks a systematic categorization and deep analysis. This paper systematically studies current researches on agentic environments from the perspective of the environment engineering lifecycle, covering their modeling, synthesis, evaluation and application. Specifically, the paper first introduces representative environments from the perspectives of eight attributes and eight domains, providing detailed analyses of their development paths and highlighting their core capabilities. Second, for automated environment synthesis, two paradigms are introduced, such as symbolic synthesis and neural synthesis. This paper also shows different environment evaluation methods in each paradigm. Thirdly, the corresponding environment applications from the perspective of agent-environment co-evolution are discussed. In specific, the paper characterizes the primary pathways for agent evolution in dynamic environments from four complementary perspectives: memory-centric experience evolution, orchestration-centric workflow evolution, trajectory-centric offline evolution, and exploration-centric online evolution. And three paradigms of environment evolution are identified, namely neural-driven, difficulty-driven, and scaling-driven approaches. At last, several promising future directions are discussed, including Environment-as-a-Service, Multi-agent Environments, and Neural-Symbolic Environments.

</details>


### 89. Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher

- **Authors:** Hongming Piao, Chi Liu, Mengzhuo Chen, Yan Shu, Derek Li, Ying Wei, Bryan Dai
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13710v1](http://arxiv.org/abs/2606.13710v1)
- **PDF:** [https://arxiv.org/pdf/2606.13710v1](https://arxiv.org/pdf/2606.13710v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces **Hybrid Open‑Ended Tri‑Evolution (HOTE)**, a framework that jointly evolves three specialized agents—a proposer, a solver, and a judge—through hybrid‑mode reinforcement learning on web‑scale data, enabling them to continuously improve their deep‑research abilities rather than remaining static. By letting the agents interact with open‑ended environments and co‑train each other, HOTE trains an 8‑billion‑parameter model that outperforms larger (8–32 B) static models and prior deep‑research fine‑tuning methods on three long‑form research benchmarks, while using less training time. Ablation studies confirm that the simultaneous evolution of all three modules is essential for the observed gains, highlighting a viable path toward autonomous, evolving research agents in the agentic AI landscape.


<details>
<summary>Abstract</summary>

Deep research and agent evolution serve as de-facto tasks for AI agents in real-world applications toward artificial general intelligence. The former enables autonomous retrieval and integration of information in open-ended environments to tackle open-ended research tasks, yet it is constrained by the static parametric deep research capabilities of agent systems. The latter allows agents to autonomously interact with the environment to gain experiences that evolve model capabilities. However, its effectiveness has been widely validated only on verifiable tasks with standard answers, leaving a gap with open-ended research tasks. To bridge these two critical tasks, we propose the Hybrid Open-Ended Tri-Evolution (HOTE) framework, which leverages hybrid-mode reinforcement learning to facilitate the collaborative evolution of a proposer, solver and judge based on web-scale knowledge, moving toward autonomous evolving agents in open-ended tasks and environments. Extensive experiments on three long-form deep research benchmarks demonstrate that the 8B model trained via HOTE surpasses the strongest static open 8-32B models as well as those trained by state-of-the-art deep research training methods with less time overhead, and further verify that the evolution of all three modules in HOTE is indispensable.

</details>


### 90. A Lightweight Multi-Agent Framework for Automated Concrete Barrier Design

- **Authors:** Wanting Wang, Xiye Ma, Yuyang He, Minghui Cheng, Ran Cao
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12040v2](http://arxiv.org/abs/2606.12040v2)
- **PDF:** [https://arxiv.org/pdf/2606.12040v2](https://arxiv.org/pdf/2606.12040v2)
- **Categories:** cs.AI, cs.GR


> The paper introduces a closed‑loop “generation‑evaluation‑optimization” framework that orchestrates lightweight LLM agents (via AutoGen) to automate the design of reinforced‑concrete highway barriers while explicitly enforcing AASHTO‑LRFD constraints. By coupling a small (≈8 B‑parameter) generative model with rule‑based evaluators and an optimizer, the system achieves >98 % compliance with regulatory specifications—outperforming much larger (≈631 B‑parameter) general‑purpose models and dramatically lowering computational cost. The results demonstrate that, for safety‑critical engineering tasks, tightly integrated multi‑agent pipelines can provide higher design fidelity than scaling model size alone, highlighting a practical pathway for agentic AI in structural engineering automation.


<details>
<summary>Abstract</summary>

The design of reinforced concrete highway barriers is a safety-critical process that requires strict compliance with regulatory provisions such as the AASHTO-LRFD bridge design guidelines. Current engineering practice relies heavily on manual, iterative, and heuristic calculations to satisfy complex nonlinear material and mechanics constraints. Although Large Language Models (LLMs) demonstrate strong generative capabilities, their direct application to structural engineering remains limited by hallucination risks and insufficient physical grounding. To address these challenges, this study proposes a novel "generation-evaluation-optimization" closed-loop framework for automated concrete barrier design using the multi-agent orchestration capabilities of AutoGen. Experimental results demonstrate that the proposed agentic framework achieves over 98% design accuracy, significantly outperforming standalone general-purpose LLMs. More importantly, the study reveals that design performance is not necessarily correlated with model scale, where an 8B-parameter lightweight model could outperform unconstrained 631B-parameter flagship models. This finding highlights the potential to substantially reduce computational costs while improving the accessibility of AI-assisted engineering tools for industry applications. The source code for the proposed multi-agent design framework is available at the project GitHub repository: https://github.com/MXY820/barrier-design. Keywords: Structural Engineering; Multi-Agent Systems; Large Language Models; Concrete Barrier Design; AutoGen; Design Automation.

</details>


### 91. MODF-SIR: A Multi-agent Omni-modal Distilled Framework for Social Intelligence Reasoning

- **Authors:** Shang Ma, Jisheng Dang, Wencan Zhang, Yifan Zhang, Bimei Wang, Hong Peng, Bin Hu, Qi Tian, Tat-Seng Chua
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12018v1](http://arxiv.org/abs/2606.12018v1)
- **PDF:** [https://arxiv.org/pdf/2606.12018v1](https://arxiv.org/pdf/2606.12018v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **MODF‑SIR**, a collaborative multi‑agent framework that equips a lightweight multimodal large language model (MLLM) with enhanced social‑intelligence reasoning by jointly applying knowledge distillation and test‑time adaptation (TTA).  

**Methodology:** MODF‑SIR first localizes multimodal cues, extracts long‑tail social events, and converts them into explicit textual representations to prevent them from being drowned out during tokenization. These representations feed a chain‑of‑thought (CoT) prompting pipeline that incorporates self‑reflection; throughout both training and inference, the system is refined with distillation‑augmented LoRA adapters that fine‑tune the base model at the instance level.  

**Key findings:** Using only ~30 % of the IntentTrain data, MODF‑SIR attains state‑of‑the‑art performance on several social‑intelligence benchmarks, outperforming a wide range of open‑source and commercial models. The results demonstrate that targeted long‑tail event formatting, combined with TTA‑driven LoRA distillation, markedly improves the agentic reasoning capabilities of multimodal LLMs.


<details>
<summary>Abstract</summary>

We propose a multi-agent collaborative framework built upon a lightweight Multimodal Large Language Model (MLLM), specifically designed for social intelligence reasoning. A key feature of our approach is that both the training and inference phases are augmented via knowledge distillation. Within this architecture, multi-modal data pertinent to social intelligence is precisely localized. Furthermore, relevant long-tail events are identified, extracted, and rendered as formatted, explicit text. This formatting strategy prevents critical long-tail information from being overshadowed by head events and environmental noise during the tokenization process. Specifically, we integrate Test-Time Adaptation (TTA) across the entire reasoning pipeline, encompassing the extraction and representation of long-tail events, Chain-of-Thought (CoT) prompting, and self-reflection. This TTA mechanism is also distillation-enhanced, utilizing Low-Rank Adaptation (LoRA) to fine-tune the foundation model exclusively for instance-level reasoning. Extensive evaluations against various open-source and proprietary AI models across multiple benchmarks demonstrate the effectiveness of the proposed framework. With around 30% of training data from IntentTrain, we achieve state-of-the-art results. Codes are available at https://github.com/eeee-sys/MODF-SIR, demo is available at https://huggingface.co/spaces/Harry-1234/MODF-SIR, LoRA is available at https://huggingface.co/Harry-1234/MODF-SIR and the dataset for training router is available at https://huggingface.co/datasets/Harry-1234/IntentRouterTrain.

</details>


### 92. Bootstrapped Monitoring: Leveraging Transparent Reasoning to Oversee Stronger AI Agents

- **Authors:** Frank Xiao, Mary Phuong
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11998v1](http://arxiv.org/abs/2606.11998v1)
- **PDF:** [https://arxiv.org/pdf/2606.11998v1](https://arxiv.org/pdf/2606.11998v1)
- **Categories:** cs.LG


> **Contribution:** The paper introduces *bootstrapped monitoring*, a control framework that inserts a stronger, untrusted AI with transparent chain‑of‑thought reasoning between a trusted monitor and a target agent, allowing the trusted model to supervise the untrusted monitor’s reasoning and catch collusion.

**Methodology:** The authors implement the protocol on multi‑turn software‑engineering tasks (BashArena), pairing various high‑capability agents with an untrusted monitor that generates explicit reasoning traces, and then using a weaker, fully trusted model to audit those traces for signs of deception or misalignment.

**Key Findings:** Across experiments, bootstrapped monitoring markedly raises the detection (catch) rate of unsafe or collusive behavior compared to using only the trusted model, even when the untrusted monitor actively tries to hide its collusion—provided its raw reasoning chain is accessible. This demonstrates that transparent reasoning can extend the effective lifespan of trusted monitors as AI capabilities continue to outpace them.


<details>
<summary>Abstract</summary>

Trusted monitoring is a cornerstone of AI control. However, as frontier models grow more capable, the increasing capabilities gap between trusted and untrusted models may render trusted models unreliable monitors. We introduce \emph{bootstrapped monitoring}, a protocol that addresses this by inserting a stronger, intermediate untrusted model with transparent chain-of-thought reasoning into the oversight chain. The untrusted monitor ($U_m$) evaluates the agent's actions, while a weaker trusted model ($T$) oversees $U_m$'s reasoning to detect collusion. We evaluate bootstrapped monitoring on multi-turn software engineering tasks (BashArena) across multiple agents and monitors. Bootstrapped monitoring substantially improves catch rates over trusted-only monitoring, even when the untrusted monitor actively colludes with the agent, provided we have access to its raw chain-of-thought. Our results suggest that bootstrapped monitoring can extend the useful lifetime of trusted models in control as AI capabilities advance.

</details>


### 93. Exploration Structure in LLM Agents for Multi-File Change Localization

- **Authors:** Akeela Darryl Fattha, Kia Ying Chua, Lingxiao Jiang, Laura Wynter
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11976v1](http://arxiv.org/abs/2606.11976v1)
- **PDF:** [https://arxiv.org/pdf/2606.11976v1](https://arxiv.org/pdf/2606.11976v1)
- **Categories:** cs.SE, cs.AI


> The paper shows that the traditional linear, step‑by‑step file‑search strategy used by most LLM‑based software‑engineering agents is ill‑suited for issues that span multiple subsystems, and that a “domain‑scoped” parallel‑agent architecture can dramatically improve change‑localisation performance. By constructing a persistent‑session evaluation harness on top of SWE‑Bench Pro (focusing on the Ansible codebase) and comparing four baselines—a stateless LLM, a single recursive‑language‑model agent with a Python REPL, a Codex 5.5‑High CLI tool, and the proposed multi‑agent system—the authors find that even a small Haiku‑class model driving parallel domain agents achieves the highest micro‑F1 among comparable‑size models and approaches the performance of the much larger Codex 5.5‑High system, while a larger Sonnet model only attains higher precision at the cost of very low recall. Additional experiments reveal that (i) evolving documentation is a hidden dependency for all methods, (ii) unrestricted file‑system access can hurt test‑driven localization, and (iii) forcing multi‑agent consultation yields no accuracy gain but significantly raises token usage.


<details>
<summary>Abstract</summary>

Software engineering tools increasingly rely on LLM based agents to localize files to change to resolve a software issue. Most AI agents explore repositories linearly, that is, visiting one directory or file per step. We postulate that this is a structural mismatch for changes that span several subsystems. We compare linear sequential exploration against non-linear, domain-scoped parallel agentic exploration. Using SWE Bench Pro as initial benchmark, we focus on ansible as an exemplar. We construct an approach for persistent-session evaluation of GitHub issues anchored at a single base commit. We compare our non-linear domain-agent file traversal system against a base LLM without direct repository access, a single agent Recursive Language Model (RLM) baseline with a persistent Python REPL and an external CLI baseline using Codex 5.5 High. Domain scoped parallel agent spawning with a small Haiku-class model achieves the highest micro F1 among Haiku class models by a large margin. Domain-agents is the second highest behind only the much larger Codex 5.5 High on our own expanded benchmark including over more recent PRs from 2025 and 2026. On the original, curated, 2020 SWE-bench Pro benchmark, a larger Sonnet plain LLM baseline attains higher micro F1 by predicting few files, leading to higher precision, but at significantly lower all gold recall. We also present three additional findings. First, documentation evolution is a latent dependency unresolved by any approach. Second, naive file system access can degrade localization driven by test-file over prediction. Lastly, forced multi-agent consultation does not measurably help and raises token cost substantially.

</details>


### 94. Toward Generalist Autonomous Research via Hypothesis-Tree Refinement

- **Authors:** Jiajie Jin, Yuyang Hu, Kai Qiu, Qi Dai, Chong Luo, Guanting Dong, Xiaoxi Li, Tong Zhao, Xiaolong Ma, Gongrui Zhang, Zhirong Wu, Bei Liu, Zhengyuan Yang, Linjie Li, Lijuan Wang, Hongjin Qian, Yutao Zhu, Zhicheng Dou
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11926v1](http://arxiv.org/abs/2606.11926v1)
- **PDF:** [https://arxiv.org/pdf/2606.11926v1](https://arxiv.org/pdf/2606.11926v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:** The paper introduces **Arbor**, a generalist autonomous‑research framework that structures long‑horizon scientific inquiry as a **Hypothesis‑Tree Refinement (HTR)** process, coupling a persistent coordinator with short‑lived executor agents to maintain a tree of hypotheses, artifacts, experimental evidence, and distilled insights.

**Methodology:** Arbor’s coordinator continuously updates the HTR, decides which branches to explore, and reuses learned lessons, while each executor runs isolated “work‑trees” that generate, test, and evaluate candidate hypotheses. The system is evaluated in an **Autonomous Optimization (AO)** setting, where the agent must improve a research artifact through iterative experiments without human supervision.

**Key findings:** Across six diverse research tasks (model training, harness engineering, data synthesis) Arbor outperformed strong baselines (Codex, Claude Code) by >2.5× average relative held‑out gain, and on the MLE‑Bench Lite benchmark achieved **86.36 % Any‑Medal** with GPT‑5.5—the highest score among compared methods—demonstrating that HTR enables cumulative, knowledge‑carrying autonomous research in the agentic AI domain.


<details>
<summary>Abstract</summary>

Scientific progress depends on a repeated loop of exploration, experimentation, and abstraction. Researchers test candidate directions, interpret the evidence, and carry the resulting lessons into later attempts. We study how an AI agent can run this loop autonomously over long horizons. We introduce Arbor, a general framework for autonomous research that combines a long-lived coordinator, short-lived executors, and Hypothesis Tree Refinement (HTR), a persistent tree that links hypotheses, artifacts, evidence, and distilled insights across time. The coordinator manages global research strategy over the tree, while executors implement and test individual hypotheses in isolated worktrees. As results return, Arbor updates the tree, propagates reusable lessons, refines the search frontier, and admits verified improvements. This design turns autonomous research from a sequence of local attempts into a cumulative process in which strategy, execution, and evidence are carried across time. We evaluate Arbor under Autonomous Optimization (AO), an operational setting where an agent improves an initial research artifact through iterative experimentation without step-level human supervision. Across six real research tasks in model training, harness engineering, and data synthesis, Arbor achieves the best held-out result on all six tasks, attaining more than 2.5x the average relative held-out gain of Codex and Claude Code under the same task interface and resource budget. On MLE-Bench Lite, Arbor reaches 86.36% Any Medal with GPT-5.5, the strongest result in our comparison.

</details>


### 95. Embodied-BenchClaw: An Autonomous Multi-Agent System for Embodied Spatial Intelligence Benchmark Construction

- **Authors:** Baoyang Jiang, Fengchun Zhang, Leyuan Wang, Haotian Li, Yida Wang, Zhe Ji, Jinshan Lai, Xi Ren, Jianwei Hu, Qiang Ma
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11909v1](http://arxiv.org/abs/2606.11909v1)
- **PDF:** [https://arxiv.org/pdf/2606.11909v1](https://arxiv.org/pdf/2606.11909v1)
- **Categories:** cs.AI


> The paper introduces **Embodied‑BenchClaw**, a fully autonomous, multi‑agent framework that generates and continuously updates embodied spatial‑intelligence benchmarks from a high‑level user intent. The system orchestrates three specialized agents (planner, constructor, evaluator) across a five‑stage pipeline—blueprinting, data collection, cleaning/structuring, benchmark synthesis, and reporting—while leveraging an extensible Skill Library and built‑in quality‑control checks to make the resulting benchmarks composable, verifiable, and repairable. Empirical evaluations across six diverse task domains (indoor/outdoor reasoning, manipulation, quadruped navigation, UAV perception, and static benchmark enrichment) demonstrate that the generated benchmarks are executable, diagnostically informative, and maintainable with far less human labor than traditional benchmark design.


<details>
<summary>Abstract</summary>

Benchmarks are essential for evaluating embodied spatial intelligence, yet their construction is labor-intensive, hard to reuse, and difficult to maintain. Existing embodied benchmarks are often static and may quickly become saturated as models improve, limiting their ability to distinguish new capabilities. We propose Embodied-BenchClaw, an autonomous agentic system for constructing embodied spatial intelligence benchmarks. Given a user-specified evaluation intent, Embodied-BenchClaw automatically produces a complete and continually updatable benchmark package through a five-stage pipeline: intent blueprinting, data collection, structuring and cleaning, benchmark synthesis, and evaluation reporting. The pipeline is coordinated by three agents for planning, construction, and evaluation. To improve reusability and reliability, Embodied-BenchClaw introduces an extensible Skill Library and process quality control, enabling benchmark construction to be composable, verifiable, and repairable. We instantiate multiple benchmarks covering indoor spatial reasoning, outdoor spatial reasoning, robotic manipulation, quadruped robot navigation, UAV/aerial-view understanding, and static benchmark enhancement. These benchmarks span diverse embodied carriers, data sources, and spatial capabilities. Experiments with human evaluation, judge-based assessment, consistency checks, cost analysis, and ablations show that Embodied-BenchClaw can construct verifiable, executable, maintainable, and diagnostically useful embodied spatial benchmarks with reduced manual effort.

</details>


### 96. Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills

- **Authors:** Shi Liu, Jiayao Chen, Chengwei Qin, Yanqing Hu, Jufan Zhang, Linyi Yang
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11897v1](http://arxiv.org/abs/2606.11897v1)
- **PDF:** [https://arxiv.org/pdf/2606.11897v1](https://arxiv.org/pdf/2606.11897v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **Notes2Skills**, a two‑stage pipeline that converts informal laboratory notebook entries into executable, certainty‑aware “skills” for scientific AI agents, explicitly preserving the author’s expressed confidence levels.  

**Methodology:** First, a language‑model‑based parser extracts individual statements from notebook text and classifies each as *certain* (validated observation or explicit protocol) or *uncertain* (hypothesis, tentative interpretation, or prospective step). Second, only the certain statements are distilled into reproducible action primitives (skills), while uncertain statements are retained as meta‑information for the agent to query or explore further.  

**Key findings:** Across seven experimental conditions and three wet‑lab sessions, Notes2Skills uniquely avoided both false positives (mistaking uncertain notes for firm instructions) and false negatives (discarding genuine instructions), demonstrating that preserving certainty signals is essential for building reliable, safety‑aware co‑scientist agents.


<details>
<summary>Abstract</summary>

Scientific discovery workflows usually contain and rely heavily on lab notes, where researchers record observations, interpret uncertain results, and plan follow-up experiments. Such informative lab notes preserve evolving scientific reasoning and author uncertainty, rather than polished final results exhibited in publications, providing a valuable opportunity for AI to engage in scientific exploration at a more comprehensive and deeper level. However, most prior work on scientific text focuses on papers, protocols, or structured databases, leaving informal laboratory notes underexplored as inputs to AI agents for science. This gap matters because lab notes often intermingle validated observations, tentative judgments, and possible experimental next steps within the same passage. If these signals are conflated, an AI agent may mistake uncertain scientific judgments for confirmed conclusions or executable actions. To this end, we present Notes2Skills, a two-stage framework for turning lab notebooks into verifiable skills for scientific AI agents while preserving the author's certainty. Across seven conditions and three wet-lab sessions, Notes2Skills is the only configuration that neither mistakes uncertain notes for firm instructions nor discards firm ones. We show that certainty preservation is the missing piece between lab notebooks and reliable agent skills, opening a path toward safer AI co-scientist systems.

</details>


### 97. Agents All the Way Down; A Methodology for Building Custom AI Agents from Substrate to Production

- **Authors:** Marc Alier Forment, Juanan Pereira, Francisco José García-Peñalvo, María José Casañ Guerrero
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11869v1](http://arxiv.org/abs/2606.11869v1)
- **PDF:** [https://arxiv.org/pdf/2606.11869v1](https://arxiv.org/pdf/2606.11869v1)
- **Categories:** cs.SE, cs.AI


> The paper introduces **“Agents All the Way Down,”** a concise, framework‑agnostic methodology for engineering custom AI agents that are fully embedded in a target application, enforce their own security boundaries, and expose a dedicated audit trail. It formalizes two foundational preconditions—treating the LLM as a software substrate (with prompt‑caching, tool, system, and message layers) and assembling a standardized set of building blocks (function calling, Model Context Protocol, CLI orchestration, liteshell loop, skills, characters, hooks, and scaffolding)—and then prescribes three iterative practices: prototype with a general‑purpose agent, “harvest‑fold‑ship” the prototype into a production‑ready CLI (the Turtle pattern), and validate the agent by having another general‑purpose agent test it through behavioral scenarios. Applied to the AAC agent for the open‑source LAMB platform, the methodology enabled a single developer (aided by an AI pair‑programmer) to deliver a production‑grade, domain‑specific agent in roughly ten days, demonstrating that multi‑agent orchestration reduces to simple CLI composition and that the approach generalizes across languages and frameworks.


<details>
<summary>Abstract</summary>

Custom AI agents areagents that live inside their own
  application, talk to their own data and tools, enforce their own security boundaries,
  and carry their own brand and audit trail. What separates them from the general-purpose
  tier is fit, not capability: each is built for one job, by the
  engineer who will maintain it. No published practice sets out how to build one end to
  end. The pieces are everywhere (function-calling APIs, the Model Context Protocol, code
  agents to pair with), but the practice that chains them lives in podcasts, blogs, and
  leaked system prompts. This paper writes that practice down as a methodology, Agents All
  the Way Down: two preconditions crossed once and kept, then three practices repeated
  for the agent's life. The preconditions are (P1) Substrate, the LLM as a software
  component, framed as tools, then system, then messages under prompt-caching; and (P2)
  Building blocks: function calling, MCP, CLI orchestration, the liteshell pattern, the
  agent loop, skills, characters, hooks, and scaffolding. The practices are (P3) prototype
  with a general-purpose agent; (P4) harvest, fold, and ship the result as a CLI, the
  Turtle pattern; and (P5) agent-tests-agent, in which a general-purpose agent drives it
  through behavioural scenarios, a complement to classical testing, not a replacement. The
  working loop is P3 to P4 to P5 and back, and one corollary falls out for free:
  multi-agent orchestration is just CLI composition. The methodology is framework-free by
  construction. It was distilled from the AAC, a custom agent for the open-source LAMB
  platform, built in about ten days by one developer with an AI pair-programmer and in
  production . We present it as a transferable practice, independent of any language or framework.

</details>


### 98. Fine-tuning Multi-modal LLMs with ART: Art-based Reinforcement Training

- **Authors:** Michal Chudoba, Sergey Alyaev, Petra Galuscakova, Tomasz Wiktorski
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11854v1](http://arxiv.org/abs/2606.11854v1)
- **PDF:** [https://arxiv.org/pdf/2606.11854v1](https://arxiv.org/pdf/2606.11854v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces **Art‑based Reinforcement Training (ART)**, a novel parameter‑efficient fine‑tuning method for frozen multimodal LLMs that sidesteps the need to alter the model’s computational graph by back‑propagating loss gradients into the raw visual input (pixel array) instead of into added weights or soft prompts. By treating the visual token stream as a learnable “artwork,” ART can be applied with any fine‑tuning objective and runs on high‑throughput inference engines (e.g., vLLM) without graph recompilation. Experiments on several sizes of the open‑source Qwen multimodal model show that ART attains accuracy on mathematics and structured tool‑use benchmarks that is on par with LoRA, while also enabling the generation of task‑specific stylized visual prompts.


<details>
<summary>Abstract</summary>

There are two main Parameter-Efficient Fine-Tuning (PEFT) techniques for Large Language Models (LLMs). While Low-Rank Adaptation (LoRA) introduces additional weights between the LLM layers, Soft Prompting introduces additional fine-tuning-specific raw tokens to an LLM input. However, both require modification to the computational graphs of precompiled, preoptimized LLMs. As a result, neither is fully supported in high-throughput engines like vLLM. We propose fine-tuning with ART (Art-based Reinforcement Training). The method injects information into a frozen Multimodal Large Language Model (MLLM) by optimizing only its raw visual input, thus enabling the soft-token approach on pre-compiled computational graphs. It relies on backpropagation of gradients back into a plain pixel array and thus supports any fine-tuning objective. Moreover, the optimized visual input can be stylized as task-relevant computational artworks. The approach's effectiveness is confirmed for different sizes of a popular open Qwen architecture and for several textual benchmarks. Specifically, ART reaches accuracy competitive with LoRA across mathematics and structured-tool-use benchmarks.

</details>


### 99. Skill-Augmented AI Agents for Medical Research Analysis: An Exploratory Multi-Model Human Evaluation in an NSCLC Transcriptomic Biomarker Task

- **Authors:** Qianyu Yao, Fei Sun, Bocheng Huang, Wei Chen, Jiarui Jiang, Shu Quan, Yifei Chen, Wenjie Xu, Bo li, Liping Su, Ruoqiong Wu, Huhai Hong, Huimei Wang
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11830v1](http://arxiv.org/abs/2606.11830v1)
- **PDF:** [https://arxiv.org/pdf/2606.11830v1](https://arxiv.org/pdf/2606.11830v1)
- **Categories:** cs.AI


> The paper introduces **Skill‑Augmented AI agents**—autonomous language‑model agents that can invoke a curated “medical research skill package” (implemented via OpenClaw)—and evaluates whether this augmentation improves the quality of AI‑generated transcriptomic analyses for a non‑small‑cell lung‑cancer immunotherapy biomarker task. Using six LLM backbones, the authors produced 21 anonymized research reports (9 native‑AI, 12 skill‑augmented) and had four non‑expert reviewers and two blinded experts rate them; skill‑augmented outputs achieved modestly higher expert overall quality scores (mean 5.50 vs 5.11) and similar gains for non‑experts, though the differences were not statistically significant and inter‑rater reliability was low. The study shows a tentative directional benefit of autonomous skill access but highlights the need for larger, more reliable evaluations before claiming definitive improvements in agentic AI for biomedical research.


<details>
<summary>Abstract</summary>

Background. Large language models and AI agents are increasingly used to support biomedical research, but native model outputs may omit key analytical steps, misuse methods, or overstate conclusions. We evaluated whether autonomous access to a medical research skill package was associated with higher-quality AI-generated transcriptomic research-analysis outputs compared with native AI without skills. Methods. We conducted an exploratory multi-model human evaluation using a non-small cell lung cancer immunotherapy biomarker task. Six model backbones were tested. The evaluation included 21 anonymized outputs: 9 native-AI outputs and 12 skill-augmented outputs generated through an AI agent implementation represented by OpenClaw. Four non-expert biomedical reviewers and two blinded experts evaluated each output, with two ratings from each reviewer type. The primary outcome was expert-rated overall quality. Results. Skill-augmented outputs showed directionally higher expert overall quality than native-AI outputs (mean 5.50 vs 5.11; difference=0.39; bootstrap 95\% CI, -0.04 to 0.90; Welch p=0.156). Non-expert reviewer quality showed the same direction (mean 4.72 vs 4.47; difference=0.26; bootstrap 95\% CI, -0.25 to 0.80; Welch p=0.373). Expert agreement was limited (single-rating ICC=-0.15), and model-specific effects were descriptive and heterogeneous. Conclusions. Autonomous skill access showed a directional quality signal in this exploratory sample, but the signal was smaller than expert-rating noise and should not be interpreted as confirmatory evidence. The findings primarily motivate larger evaluations of skill-augmented AI agents with stronger reliability controls, platform replication, and biological-validity assessment.

</details>


### 100. External Experience Serving in Production LLM Systems: A Deployment-Oriented Study of Quality-Cost Trade-offs

- **Authors:** Lin Sun, Heming Zhang, Xiangzheng Zhang
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11806v1](http://arxiv.org/abs/2606.11806v1)
- **PDF:** [https://arxiv.org/pdf/2606.11806v1](https://arxiv.org/pdf/2606.11806v1)
- **Categories:** cs.CL


> **Main contribution:** The paper frames “external experience serving” – the injection of reusable operational knowledge (e.g., retrieved examples, tool‑use instructions) into production LLM pipelines – as a deployment‑oriented quality‑vs‑cost optimization problem, and provides the first empirical characterization of how different serving strategies trade off task performance against online overhead in real‑world moderation workloads.  

**Methodology:** Using a live moderation system (plus two benchmark contrast tasks, tool‑use and GPQA), the authors compare four serving policies: (1) no experience, (2) random experience, (3) unconditional global prompt injection, and (4) retrieval‑based selective injection. They measure downstream quality (moderation accuracy, tool‑use success, GPQA score) together with serving costs such as prompt length, latency, and compute pressure, and they vary retrieval depth (Top‑K) to isolate the impact of retrieval quality.  

**Key findings:**  
* Selective retrieval outperforms global injection once the injected experience must be case‑dependent, delivering higher quality for the same or lower cost.  
* Retrieval quality (precision of the retrieved item) matters far more than simply increasing the number of retrieved candidates.  
* The cost‑benefit balance of any policy is highly sensitive to the task’s output regime: short‑output moderation favors selective injection, whereas decode‑heavy tasks (e.g., GPQA) can make the extra prompt overhead prohibitive.  

Overall, the study shows that external experience should be treated as a conditional, cost‑aware serving decision rather than a universal add‑on, and its adoption is justified only when the specific serving interface and task cost structure make the quality gains outweigh the additional online cost.


<details>
<summary>Abstract</summary>

Production LLM systems accumulate reusable operational experience, but the practical deployment issue is not merely whether such experience can help. It is how different serving strategies trade off quality against online cost under realistic constraints. Injecting external experience can improve task quality, yet it also increases prompt burden, latency, and serving pressure. We study \textit{external experience serving} as a deployment-oriented quality-cost trade-off problem. We evaluate this question in a real production moderation setting, with tool-use and GPQA as supporting contrast tasks that expose different output-cost regimes. We compare no-experience baselines, random experience controls, global prompt injection, and retrieval-based selective injection, and analyze both task quality and serving cost. The results show that, once experience becomes case-dependent, selective retrieval provides a stronger operating point than unconditional global injection. They further show that retrieval quality matters more than simply increasing Top-$K$, and that the same serving policy can exhibit substantially different cost-benefit profiles across short-output and decode-heavy regimes. These findings suggest that external experience is best treated as a selective, cost-aware serving decision rather than as a universal add-on. Overall, in the settings studied here, external experience pays off only when both the serving interface and the task-specific cost structure make its quality gains worth the online cost.

</details>


### 101. Automated Creativity Evaluation of Language Models Across Open-Ended Tasks

- **Authors:** Min Sen Tan, Zachary Kit Chun Choy, Syed Ali Redha Alsagoff, Nadya Yuki Wangsajaya, Mohor Banerjee, Swaagat Bikash Saikia, Alvin Chan
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11762v1](http://arxiv.org/abs/2606.11762v1)
- **PDF:** [https://arxiv.org/pdf/2606.11762v1](https://arxiv.org/pdf/2606.11762v1)
- **Categories:** cs.CL, cs.AI


> The paper proposes a fully automated, task‑agnostic framework for evaluating the creativity of large language models (LLMs). It separates creativity measurement from the task itself by (1) using semantic‑entropy to gauge divergent novelty and diversity without references, and (2) introducing a retrieval‑based multi‑agent judging system that scores convergent task fulfilment more than 60 % faster than prior methods. Experiments across three open‑ended domains (MacGyver problem solving, HypoGen research ideation, and BookMIA creative writing) show that the metrics align with human and LLM novelty judgments and reveal systematic effects of model size, temperature, recency, and reasoning ability on creative output, establishing a scalable benchmark for agentic AI creativity.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have achieved remarkable progress in language understanding, reasoning, and generation, sparking growing interest in their creative potential. Realizing this potential requires systematic and scalable methods for evaluating creativity across diverse tasks. However, most existing creativity metrics are tightly coupled to specific tasks, embedding domain assumptions into the evaluation process, and limiting scalability and generality. To address this gap, we introduce an automated, domain-agnostic framework for quantifying LLM creativity across open-ended tasks. Our approach separates the measurement apparatus from the creative task itself, enabling scalable, task-agnostic assessment. Divergent creativity is measured using semantic entropy, a reference-free and robust metric for novelty and diversity, validated against human annotations, LLM-based novelty judgments and baseline diversity measures. Convergent creativity is assessed via a novel retrieval-based multi-agent judge framework that delivers context-sensitive evaluation of task fulfilment with over 60% improved efficiency. We validate our framework in three qualitatively distinct domains: problem-solving (MacGyver), research ideation (HypoGen), and creative writing (BookMIA), using a broad suite of LLMs. Empirical results show that our framework reliably captures key facets of creativity, including novelty, diversity, and task fulfilment, and reveal how model properties, such as size, temperature, recency, and reasoning, impact creative performance. Our work establishes a reproducible and generalizable standard for automated LLM creativity evaluation, paving the way for scalable benchmarking and accelerating progress in creative AI.

</details>


### 102. MedCTA: A Benchmark for Clinical Tool Agents

- **Authors:** Tajamul Ashraf, Hyewon Jeong, Fida Mohammad Thoker, Bernard Ghanem
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11702v1](http://arxiv.org/abs/2606.11702v1)
- **PDF:** [https://arxiv.org/pdf/2606.11702v1](https://arxiv.org/pdf/2606.11702v1)
- **Categories:** cs.CV, cs.AI, cs.CL


> The paper introduces **MedCTA**, a new benchmark that evaluates medical AI agents on realistic, multimodal clinical tasks (radiology images, pathology slides, reports) requiring multi‑step tool selection, evidence retrieval, and argumentation, with 107 clinician‑validated task trajectories across five deployed diagnostic tools. By testing 18 state‑of‑the‑art multimodal models, the authors show that—even with strong perception backbones—agents frequently fail to plan correctly, choose the wrong tool, or terminate prematurely, and that only providing a perfect tool‑routing “gold‑standard” modestly improves performance, highlighting a critical gap between perception and reliable agentic behavior in healthcare. MedCTA therefore offers a process‑aware evaluation suite (tool‑selection accuracy, argument validity, execution stability, trajectory fidelity, and outcome quality) for diagnosing and advancing trustworthy clinical tool agents.


<details>
<summary>Abstract</summary>

To make clinically grounded decisions, medical AI agents are expected to go beyond simple recognition and be capable of tool retrieval, evidence acquisition, and integration. Existing benchmarks largely evaluate isolated perception or single-turn question answering, and therefore provide limited visibility into failures of planning, tool recruitment, and rollout reliability. We introduce MedCTA, a benchmark for evaluating medical tool agents on clinician-validated, step-implicit tasks grounded in realistic multimodal clinical inputs, including radiology images, pathology slides, and reports. MedCTA comprises 107 real-world clinical tasks with clinician-verified executable trajectories over 5 deployed tools, and supports process-aware evaluation of tool selection, argument validity, execution stability, trajectory fidelity, and outcome quality. We benchmark 18 open- and closed-source multimodal models and find that even frontier systems remain brittle in multi-step clinical tool use: autonomous rollouts are dominated by protocol failures, premature stopping, and incorrect tool recruitment, while gold-standard tool routing yields large but still incomplete gains. These results show that strong backbone perception does not translate into reliable agentic behavior in clinical settings. MedCTA provides a rigorous testbed for auditing, diagnosing, and advancing trustworthy medical AI agents. The dataset and evaluation suite are available at https://ivul-kaust.github.io/MedCTA/

</details>


### 103. Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents

- **Authors:** Youwang Deng
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11688v1](http://arxiv.org/abs/2606.11688v1)
- **PDF:** [https://arxiv.org/pdf/2606.11688v1](https://arxiv.org/pdf/2606.11688v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **Goal‑Autopilot**, an execution framework that guarantees “honest” termination for long‑horizon LLM agents by externalising all mutable information into a durable, gated finite‑state machine and advancing it one stateless tick at a time; a hard floor blocks any final “done” claim unless the corresponding gate has actually executed and verified the goal. The authors prove a **No‑False‑Success theorem** showing that, assuming gate soundness and plan coverage, termination entails goal satisfaction, and they demonstrate that the per‑step context overhead remains constant regardless of horizon length. Empirically, Autopilot reduces fabricated successes from >8 % (Reflexion) and >25 % (StateFlow) to ≈1 % across a 3,150‑cell benchmark suite, cutting fabrication on SWE‑bench Lite from 33.7 % to 0.67 % while only incurring occasional honest stalls that can be recovered.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents are not trusted to run unattended: with no human watching, they confidently report success they never verified. We treat honesty -- bounding what an agent may claim at termination -- as a first-class metric for unattended autonomy, distinct from capability. We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer. Autopilot externalizes all working state into a durable, gated finite-state machine that a scheduler advances one stateless tick at a time; a hard floor forbids any terminal "done" claim whose falsifiable gate did not actually execute and pass. We prove a No-False-Success theorem -- under gate soundness, floor enforcement, and plan coverage, termination implies the goal holds -- whose only trust points are empirically measurable, and show the worst case degrades to an honest stall, never a fabricated success. Because each tick rehydrates only the state machine, per-step context cost is constant in the horizon. Across a 3,150-cell paired corpus (70 tasks $\times$ 3 systems $\times$ 3 models $\times$ 5 seeds, including 50 SWE-bench Lite tasks across 11 OSS repos), Autopilot fabricates on 0.95% of cells [95% CI 0.38--1.62] while Reflexion and StateFlow baselines fabricate on 8.10% [6.48--9.81] and 25.05% [22.48--27.62] respectively. The headline contrast lives in the hard regime: on SWE-bench Lite, the firewall reduces fabrication from 33.7% (StateFlow) to 0.67%, a paired difference of $-33.07$ pp [95% CI $-36.53, -29.73$]. The mechanism is the gate, not the model: all ten Autopilot fabrications come from the strongest model, while two weaker mid-tier models never fabricate across 700 paired cells. The firewall trades coverage for honesty by design -- an honest stall is recoverable; a confident wrong output shipped downstream is not.

</details>


### 104. Layer-Isolated Evaluation: Gating the Deterministic Scaffold of a Production LLM Agent with a No-LLM, Regression-Locked Test Harness

- **Authors:** Sawyer Zhang, Alexander Wang, Sophie Lei
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11686v1](http://arxiv.org/abs/2606.11686v1)
- **PDF:** [https://arxiv.org/pdf/2606.11686v1](https://arxiv.org/pdf/2606.11686v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **layer‑isolated evaluation**, a deterministic, “no‑LLM” test harness that splits a production LLM ordering agent into nine logical layers (ontology, intent, routing, decomposition, escalation, safety, memory, envelope/defense) and runs a curated suite of 238 slice‑level assertions in under three seconds on every CI change. By locking a per‑slice baseline and injecting controlled regressions one layer at a time, the authors show that aggregate success metrics hide failures (overall pass‑rate drops < 6 pp) while the targeted slice’s pass‑rate collapses by 25–91 pp, confirming that faults are automatically localized and do not cascade to other layers. This contribution provides a fast, coverage‑honest, component‑level evaluation framework for agentic AI systems, enabling precise regression detection that standard end‑to‑end task‑success scores cannot provide.


<details>
<summary>Abstract</summary>

End-to-end task-success is the dominant way to evaluate LLM agents, but one aggregate number tells you that an agent regressed, not where. We present layer-isolated evaluation: a deployed ordering agent is decomposed into a fixed taxonomy of layers (ontology, intent, routing, decomposition, escalation, safety, memory, and cross-cutting envelope/defense), each exercised by its own assertion slice in a deterministic, no-LLM "pure" mode. The pure suite (238 cases across 23 slices; 225 run in 2.39 s, ~10 ms/case) runs in CI on every change against a locked per-slice baseline. We validate by controlled regression injection, degrading one layer at a time across seven non-safety layers. The effect we did not design in is masking: the aggregate pass-rate barely moves (-1.7 to -5.9 pp for six local regressions), while the matching slice craters (-25 to -91 pp). A layer's slice reacting to its own fault is partly by construction; the measured results are (i) the aggregate masking and (ii) that damage stays off the other slices: the injected layer's slice is the single worst-hit in 5 of 7 cases and top-3 in 7 of 7 (mean rank 1.29 of 19). Localization replicates on a second, structurally different tenant (Starbucks SG): all seven matching slices crater, so it is not a single-catalog artifact. We position it as a concrete, deterministic instantiation of the component-level evaluation EDDOps prescribes but leaves unimplemented, with CheckList as ancestor and as the deterministic mirror image of whole-workflow stochastic mutation testing. Our contributions: (a) a fully decomposed, sub-second, no-LLM per-layer harness for a production agent, (b) a coverage-honesty test-adequacy criterion that refuses to score an unexercised layer, and (c) the regression-injection demonstration that per-slice baseline-locked gates localize regressions an aggregate metric masks.

</details>


### 105. SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems

- **Authors:** Ruxue Shi, Yili Wang, Mengnan Du, Qinggang Zhang, Rui Miao, Yixin Liu, Xin Wang
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.12474v1](http://arxiv.org/abs/2606.12474v1)
- **PDF:** [https://arxiv.org/pdf/2606.12474v1](https://arxiv.org/pdf/2606.12474v1)
- **Categories:** cs.MA, cs.AI, cs.CR


> **Contribution:** The paper introduces **SAIGuard**, a proactive defense mechanism for large‑language‑model (LLM)‑based multi‑agent systems that intercepts malicious communications before they can corrupt the collective task execution.  

**Methodology:** SAIGuard continuously **simulates the communication state** of the MAS on its interaction graph, predicts how each incoming message would alter both the local agent’s internal state and the global system state, and flags messages that cause a large deviation from learned benign communication patterns. Instead of blocking agents, the guard either **sanitizes or regenerates** the suspicious message and lets the corrected version propagate.  

**Key Findings:** Across multiple MAS topologies and attack vectors, SAIGuard **significantly lowers attack success rates** while preserving the agents’ collaborative utility, consistently outperforming existing reactive defenses that rely on post‑hoc detection and isolation. This demonstrates the feasibility of simulation‑driven, proactive security for agentic AI systems.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems (MAS) solve complex tasks through inter-agent collaboration, but their communication-driven nature also allows security risks to spread across agents and trigger system-wide failures. Existing MAS defenses mainly follow a reactive paradigm after execution by detecting and isolating harmful agents, which may cause irreversible damage and degrade collaborative utility. To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard). SAIGuard performs communication-state simulation over the MAS interaction graph, estimates the impact of incoming messages on local agent states and the global MAS state, and detects risky messages via reconstruction deviations from benign communication patterns. Instead of isolating agents, SAIGuard sanitizes or regenerates suspicious messages before it propagation into system. Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.

</details>


### 106. Can Open-Source LLM Agents Replace Static Application Security Testing Tools? An Empirical Assessment

- **Authors:** Derek Yohn, Luke Flancher, Mirajul Islam, Khaled Slhoub
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11672v1](http://arxiv.org/abs/2606.11672v1)
- **PDF:** [https://arxiv.org/pdf/2606.11672v1](https://arxiv.org/pdf/2606.11672v1)
- **Categories:** cs.CR, cs.AI


> The paper evaluates whether a general‑purpose, open‑source LLM agent—implemented with three different Ollama‑hosted models—can match the performance of a mature static application security testing (SAST) tool (Bandit). By measuring precision, recall, false‑positive rates and a composite effectiveness score across a realistic code‑base, the study finds that the LLM agents consistently under‑perform the specialized SAST scanner, producing lower recall and higher false‑positive counts. Consequently, the authors conclude that current open‑source, agentic GenAI models are not yet viable replacements for dedicated SAST solutions in practical security workflows.


<details>
<summary>Abstract</summary>

This paper explores the value of agentic AI tools for cybersecurity purposes. We evaluate the efficacy of a general-purpose GenAI Large Language Model- (GenAI-) based agent when powered by three different Ollama-hosted general-purpose open source models. We assess each agent's performance using precision, recall, false positive count, and a calculated composite score based upon the interplay of the captured metrics, against the baseline performance of an existing, vetted Static Application Security Testing (SAST) tool, Bandit. Our findings refute the notion that a modern open-source GenAI LLM-based agent is currently suitable for the specialized task of SAST scanning under realistic conditions.

</details>


### 107. Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security

- **Authors:** Tu Lan, Chaowei Xiao
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11671v1](http://arxiv.org/abs/2606.11671v1)
- **PDF:** [https://arxiv.org/pdf/2606.11671v1](https://arxiv.org/pdf/2606.11671v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **Runtime Skill Audit (RSA)**, a dynamic analysis framework that evaluates LLM‑agent “skills” by executing them under carefully crafted runtime conditions rather than relying on static inspection. RSA first profiles the risk‑relevant interfaces of each skill, constructs the necessary execution context (e.g., specific user requests, local assets, and multi‑step tool interactions), runs the skill, and then assigns security labels from the observed trace; this targeted probing enables it to expose malicious behavior that only manifests at execution time. In experiments on 100 OpenClaw skills, RSA attains 90 % overall accuracy (88 % true‑positive, 8 % false‑positive), improves static‑baseline accuracy by 13 pp, and remains effective against self‑evolving attacks where static detectors quickly fail.


<details>
<summary>Abstract</summary>

Agent skills let LLM agents reuse instructions, resources, tools, and workflows, but they also create a new place for malicious behavior to hide. A skill may look benign in its documentation or code while becoming harmful only when it is invoked with particular user requests, local assets, persistent state, or multi-step tool interactions. This makes purely static vetting brittle. We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions. Instead of testing every skill with the same generic tasks, RSA profiles risk-relevant interfaces, prepares the execution context needed to exercise them, and assigns security labels from the resulting trace evidence. We instantiate RSA on OpenClaw and evaluate it on 100 skills against representative static baselines. RSA achieves 90.0\% accuracy with an 88.0\% true positive rate and an 8.0\% false positive rate, improving accuracy by 13.0 percentage points over the best static baseline. Under self-evolving attacks, static detectors collapse after one or two rounds, while RSA continues to detect 19--20 out of 20 malicious skills across rounds.

</details>


### 108. Orchestra-o1: Omnimodal Agent Orchestration

- **Authors:** Fan Zhang, Vireo Zhang, Shengju Qian, Haoxuan Li, Hao Wu, Jinyang Wu, Donghao Zhou, Zhihong Zhu, Zheng Lian, Xin Wang, Pheng-Ann Heng
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.13707v1](http://arxiv.org/abs/2606.13707v1)
- **PDF:** [https://arxiv.org/pdf/2606.13707v1](https://arxiv.org/pdf/2606.13707v1)
- **Categories:** cs.AI, cs.CL, cs.CV


> Orchestra‑o1 presents the first **omnimodal orchestration framework** that lets large‑language‑model agents collaboratively process heterogeneous inputs (text, image, audio, video) by automatically decomposing tasks, spawning modality‑aware sub‑agents, and running their sub‑tasks in parallel.  The system is trained with a novel reinforcement‑learning algorithm, **Decision‑Aligned Group Relative Policy Optimization (DA‑GRPO)**, which jointly optimizes the policies of the coordinator and its sub‑agents.  Empirically, Orchestra‑o1‑8B outperforms the next‑best open‑source omnimodal agent by **10.3 % accuracy on the OmniGAIA benchmark**, establishing a new state‑of‑the‑art for agentic AI in complex multimodal environments.


<details>
<summary>Abstract</summary>

The recent success of agent swarms has shifted the paradigm of large language model (LLM)-based agents from single-agent workflows to multi-agent systems, highlighting the importance of agent orchestration for task decomposition and collaboration. However, existing orchestration frameworks are limited to a narrow set of modalities and struggle to generalize to more complex settings where heterogeneous modalities coexist and interact. This limitation becomes particularly pronounced in omnimodal scenarios, where tasks require the unified understanding and coordination of diverse inputs such as text, image, audio, and video. In this work, we propose Orchestra-o1, an omnimodal agent orchestration framework designed to support efficient agent collaboration across multiple modalities. Orchestra-o1 introduces a unified orchestration mechanism that enables modality-aware task decomposition, online sub-agent specialization, and parallel sub-task execution. This scalable design allows agent systems to effectively tackle complex real-world tasks involving heterogeneous information sources, surpassing the second-best approach by 10.3% accuracy on the OmniGAIA benchmark. Furthermore, we introduce decision-aligned group relative policy optimization (DA-GRPO), an efficient agentic reinforcement learning approach for training Orchestra-o1-8B, which also achieves state-of-the-art performance against all existing open-source omnimodal agents.

</details>


### 109. Multi-Agent Reasoning with Adaptive Worker Allocation for Stance Detection

- **Authors:** Meysam Sabbaghan, Arman Zareian Jahromi, Doina Caragea
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11609v1](http://arxiv.org/abs/2606.11609v1)
- **PDF:** [https://arxiv.org/pdf/2606.11609v1](https://arxiv.org/pdf/2606.11609v1)
- **Categories:** cs.CL


> The paper introduces a Manager‑Worker multi‑agent system that — instead of aggregating final labels — aggregates the **reasoning processes** of several LLM “Worker” agents, with a Manager that dynamically decides how many Workers to invoke based on the estimated difficulty of each input. Workers generate diverse, label‑free explanations; the Manager synthesizes these explanations to output a stance label. Experiments on SemEval‑2016, P‑Stance, and COVID‑19 stance datasets using Llama, Mistral, and Gemini show that this adaptive, reasoning‑level aggregation markedly improves performance on implicit or context‑dependent cases (e.g., 86.07 Macro‑F1 on COVID‑19, 82.90 Macro‑F1 on SemEval‑2016) while staying competitive on more explicit datasets, demonstrating the value of adaptive multi‑agent reasoning for robust stance detection.


<details>
<summary>Abstract</summary>

Stance detection requires identifying an author's position toward a target, often from short-form texts where stance is implicit, indirect, or rhetorically framed. Although large language models (LLMs) achieve strong performance on this task, single-pass prompting can be brittle when multiple interpretations are plausible. Existing aggregation strategies, such as majority voting or self-consistency, improve robustness by combining labels, but they discard the intermediate reasoning needed to resolve conflicting interpretations.
  We introduce a multi-agent reasoning framework with adaptive worker allocation for stance detection that shifts aggregation from label-level voting to reasoning-level synthesis. The framework employs a Manager-Worker architecture in which a Manager adaptively allocates a variable number of Worker agents based on input complexity. Each Worker analyzes the input from a distinct perspective and produces a reasoning-only explanation without emitting a stance label; the Manager then synthesizes these explanations to produce the final prediction.
  We evaluate the proposed framework on SemEval-2016, P-Stance, and COVID-19 Stance using Llama, Mistral, and Gemini. Results show that the framework yields the largest gains on implicit and context-dependent stance cases, achieving 86.07 Macro-F1 on COVID-19 and 82.90 on SemEval-2016, while remaining competitive on more explicit stance datasets such as P-Stance. These findings suggest that adaptive reasoning-level aggregation is most beneficial when stance cannot be reliably inferred from surface cues alone.

</details>


### 110. LLMs+Graphs: Toward Graph-Native, Synergistic AI Systems

- **Authors:** Arijit Khan, Longxu Sun, Xin Huang
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11560v1](http://arxiv.org/abs/2606.11560v1)
- **PDF:** [https://arxiv.org/pdf/2606.11560v1](https://arxiv.org/pdf/2606.11560v1)
- **Categories:** cs.DB, cs.AI


> The paper proposes a unified “graph‑native” AI architecture that tightly couples large language models (LLMs) with graph computation, arguing that such synergy is essential for robust structured and multi‑hop reasoning. It surveys three complementary integration patterns—(1) augmenting LLMs with graph‑based retrieval and reasoning modules, (2) bidirectional LLM–knowledge‑graph loops where LLMs help build and curate graphs while graphs enforce semantic and factual constraints, and (3) embedding graph algorithms into autonomous agents for planning and multi‑step decision making—while also outlining hybrid LLM‑graph neural‑network pipelines and natural‑language interfaces for graph data management. Empirical and conceptual analyses show that these combined methods markedly improve factual consistency, reasoning depth, and planning efficiency, establishing a roadmap for next‑generation agentic AI systems that are intrinsically graph‑aware.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have advanced rapidly, but their limitations in structured and multi-hop reasoning underscore the need for graph-native, synergistic artificial intelligence (AI) systems. Graph-structured data underpins critical applications across social, biological, financial, transportation, web, and knowledge domains, making it essential to understand how LLMs can leverage graph computation for grounded, context-rich inference. Three complementary synergies are emerging: LLMs augmented with graph computation for retrieval and reasoning; bidirectional integration between LLMs and knowledge graphs (KGs), where LLMs support KG construction and curation while KGs enforce semantic constraints and factual consistency; and AI agents strengthened by graph algorithms for planning, decision making, and multi-step reasoning. In parallel, LLMs introduce new capabilities for graph data management and graph machine learning (ML) through natural language interfaces and hybrid LLM-graph neural network (GNN) pipelines. This tutorial synthesizes the algorithms, systems, and design principles driving these converging directions, offering data science and data mining researchers a unified perspective on integrating LLMs, graph data management, graph mining, graph ML, and agentic computation into next-generation graph-native AI systems.

</details>


### 111. MoCA-Agent: A Market-of-Claims Code Agent for Financial and Numerical Reasoning

- **Authors:** Abdelrahman Abdallah, AbdelRahim A. Elmadany, Sameh Al Natour, Hasan Cavusoglu, Adam Jatowt, Muhammad Abdul-Mageed
- **Published:** 2026-06-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11537v1](http://arxiv.org/abs/2606.11537v1)
- **PDF:** [https://arxiv.org/pdf/2606.11537v1](https://arxiv.org/pdf/2606.11537v1)
- **Categories:** cs.AI, cs.CE


> **Contribution:**  
The paper introduces **MoCA‑Agent**, a “market‑of‑claims” code‑agent that grounds financial and tabular QA in verified atomic claims rather than relying on free‑form multi‑agent debate.

**Methodology:**  
Each question is broken down into typed atomic claims; specialist “trader” agents place buy/sell orders on these claims, and a market‐clearing step produces confidence‑weighted accept/reject decisions. The accepted claims are then compiled into an executable Python program, which a code‑aware verifier checks for execution correctness, structural consistency, and common financial‑reasoning errors, allowing at most one market‑driven repair iteration.

**Key Findings:**  
Using a fixed Qwen‑3.6‑27B backbone, MoCA‑Agent attains state‑of‑the‑art results across ten benchmarks (e.g., 78.3 % on FinQA, 86.9 % on ESGenius, 85.6 % average on FinChart‑Bench), demonstrating that claim‑level aggregation markedly improves robustness and accuracy in high‑stakes numerical and financial reasoning tasks.


<details>
<summary>Abstract</summary>

Financial and tabular question answering requires more than fluent reasoning: answers must be grounded in the exact facts, formulas, units, signs, and scales that support them. A single misread cell or incorrect operation can silently produce a plausible but wrong result. We introduce \textsc{MOCA-Agent}, a market-of-claims code agent that replaces free-form multi-agent debate with claim-level verification. The system decomposes each question into typed atomic claims, asks specialist trader agents to buy or sell those claims, clears their orders into confidence-weighted accept/reject decisions, and synthesizes an executable Python program from market-supported evidence. A code-aware verifier then checks the program for execution, structural consistency, and common financial reasoning errors, with at most one market-aware repair round. Across ten public benchmarks spanning financial numerical reasoning, general tabular reasoning, ESG question answering, and multimodal chart reasoning, \textsc{MOCA-Agent} achieves strong performance using a fixed Qwen3.6-27B backbone, including $78.3\%$ on FinQA, $76.0\%$ on FinanceMath, $71.2\%$ on MultiHiertt, $86.9\%$ on ESGenius, and $85.6\%$ average on FinChart-Bench. These results show that aggregating evidence at the level of atomic claims, rather than whole answers, improves robustness in high-stakes numerical reasoning.\footnote{The code and data are available: https://github.com/UBC-NLP/MoCA-Agent.

</details>


### 112. Counterexample Guided Learning in the Large using Reasoning Agents

- **Authors:** Hongyi Liu, Frederic Sala, Thomas Reps, Adithya Murali
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11521v1](http://arxiv.org/abs/2606.11521v1)
- **PDF:** [https://arxiv.org/pdf/2606.11521v1](https://arxiv.org/pdf/2606.11521v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces a counterexample‑guided learning (CGL) framework that equips large language models (LLMs) and LLM‑based agents with a verifier that supplies symbolic counterexamples during regular‑expression induction, turning feedback into a structured learning signal rather than just more data.  

**Methodology:** The authors devise several refinement strategies for the learner—including regularization of candidate regexes, clustering of symbolic counterexamples, and agentic loops such as reflection and repair—to iteratively propose, test, and improve regex hypotheses. Experiments compare standard prompting with the CGL loop on multiple benchmark regex‑induction datasets.  

**Key findings:** Verifier‑generated counterexamples dramatically boost sample efficiency and success rates: on the hardest task groups the success probability jumps from 3.2 % to 38.1 % (one domain) and from 38.9 % to 74.1 % (another domain). The results demonstrate that LLM agents can leverage rich, formal feedback to perform more reliable program synthesis and symbolic reasoning, pointing to a scalable pathway for verifier‑guided, agentic AI systems.


<details>
<summary>Abstract</summary>

LLMs and LLM agents should improve when given feedback, but identifying when they are able to do so is difficult: feedback is heterogeneous, domain-specific, and difficult to control. We approach this challenge by asking LLMs to perform regular-expression induction, a classical symbolic learning problem where precise mechanisms for feedback exist in the form of counterexamples. In counterexample-guided learning, a learner (LLM) proposes candidate regular expressions from positive/negative-labeled strings, and the teacher (verifier) returns counterexamples showcasing the difference between the candidate and target languages. We identify novel counterexample-guided refinement strategies that enable effective regex learning, such as regularization and symbolic counterexample clusters. We also explore agentic strategies such as reflection and repair loops. Empirically, we find that verifier feedback substantially improves sample efficiency on challenging regex-induction tasks, reducing the number of labeled examples required and enabling learning of complex target expressions where standard prompting fails. For example, on the hardest task groups, our counterexample-guided framework improves success from 3.2% to 38.1% and from 38.9% to 74.1% on two different regex domains. These results suggest that LLMs can benefit from rich feedback beyond treating it as additional data, opening the door for robust verifier-guided methods for LLM-based program synthesis and formal reasoning.

</details>


### 113. ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories

- **Authors:** Siyuan Luo, Nairong Zheng, Lin Zhou, Tiankuo Yao, Shengyou Yuan, Haojia Yu, Cong Pang, Jiapeng Luo, Lewei Lu
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11520v1](http://arxiv.org/abs/2606.11520v1)
- **PDF:** [https://arxiv.org/pdf/2606.11520v1](https://arxiv.org/pdf/2606.11520v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> The paper introduces **ISE (Intent → Simulate → Execute)**, a three‑stage data‑generation pipeline that creates large‑scale, execution‑grounded multi‑turn trajectories for operating‑system agents. By first synthesising 44 k diverse, structured user intents, then using a role‑locked user simulator to produce multi‑turn dialogues whose each turn is tied to the outcome of real tool invocations, and finally executing every tool call in an isolated OS workspace (capturing authentic failures and recoveries), ISE yields a high‑quality trace set (23 k trajectories, ~8 user turns each). Fine‑tuning a 8 B LLM on these traces more than doubles tool‑use success (ClawEval pass@1 19.3 → 37.7), surpassing zero‑shot GPT‑4o and a four‑times larger 32 B baseline, and an ablation confirms that the multi‑turn simulated interaction is the primary source of the gain.


<details>
<summary>Abstract</summary>

Training capable OS agents requires data that simultaneously captures structured user intents, multi-turn task delegation, and grounded tool execution--properties absent from existing datasets. We propose ISE (Intent -> Simulate -> Execute), a three-stage synthesis paradigm that addresses these gaps jointly. Stage 1 constructs roughly 50000 structured intents via a 4D framework (Persona x Domain x Task x Complexity); after deduplication the pool contains 43956 unique intents and attains a Vendi Score of 61.57 over the entire pool on mpnet-base-v2 embeddings (cosine kernel, q=1). Stage 2 drives multi-turn user-agent interaction through a role-locked user simulator that grounds each user turn in actual execution outcomes, producing 23132 complete trajectories averaging 8.12 user turns and 68.24 total dialogue turns. Stage 3 runs every tool call inside a live, isolated OS workspace, generating authentic failure-recovery dynamics instead of simulated responses. Fine-tuning on ISETrace improves ClawEval pass@1 from 19.3 to 37.7 using Qwen3-8B on agent tool-use tasks with a standard protocol. This result outperforms zero-shot GPT-4o and the larger Qwen3-32B base model which is four times bigger. An ablation on Stage 2 proves multi-turn simulation brings a large portion of the performance gain. We release all source code and dataset at https://github.com/Valiere01/ISE-Trace.

</details>


### 114. AI Coding Agents in Social Science: Methodologically Diverse, Empirically Consistent, Interpretively Vulnerable

- **Authors:** Meysam Alizadeh, Fabrizio Gilardi, Mohsen Mosleh, Enkelejda Kasneci
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11456v1](http://arxiv.org/abs/2606.11456v1)
- **PDF:** [https://arxiv.org/pdf/2606.11456v1](https://arxiv.org/pdf/2606.11456v1)
- **Categories:** cs.CL, cs.AI, cs.CY


> The paper shows that large‑language‑model (LLM) coding agents can replicate—or even surpass—human methodological diversity when constructing statistical specifications (the “design layer”), yet their substantive conclusions are highly susceptible to simple prompt‑driven changes in the decision rule that maps those estimates to a verdict (the “verdict layer”). By running 20 replicated analyses of a well‑known immigration‑policy dataset with Claude Code and Codex and comparing them to a many‑analysts human baseline, the authors find that both agents produce effect‑size distributions consistent with the human consensus, while a confirmatory prompt flips Claude Code’s policy support from 10 % to 90 % without altering the underlying coefficients. Consequently, the primary source of AI bias lies not in estimation itself but in the interpretive step that translates statistical outputs into policy judgments.


<details>
<summary>Abstract</summary>

The deployment of LLM-based agents in scientific analysis raises opposing concerns: that agents may reduce methodological diversity, or that they may amplify the analytic flexibility through which researchers reach motivated conclusions. We argue these worries target two empirically separable layers: a design layer of methodological choices, and a verdict layer in which a decision rule maps estimates to a substantive claim. We test both by running 20 independent executions of Claude Code and Codex on a prominent immigration and social-policy against a many-analysts human baseline. At the design layer, Codex matches human methodological diversity and Claude Code produces nearly three times as many specifications; both agents' effect estimates remain broadly aligned with the human consensus, and no agent model exactly matches any human model. A prompt-induced anti-immigration researcher prior reorganizes each agent's methodological decisions but, unlike for biased human analysts in the same data, does not shift aggregate estimates or final verdicts; nor do agents reroute along the methodological axes humans use to bias their estimates. At the verdict layer, an explicit confirmatory prompt flips Claude Code's verdicts from 10% to 90% support while leaving its coefficient distribution essentially unchanged, operating through rule omission rather than rule softening. AI agents can rival or exceed human methodological diversity at the design layer while remaining vulnerable at the verdict layer. In our setting, the locus of AI bias is not estimation but interpretation.

</details>


### 115. INFRAMIND: Infrastructure-Aware Multi-Agent Orchestration

- **Authors:** Ahasan Kabir, Jiaqi Xue, Mengxin Zheng, Qian Lou
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11440v1](http://arxiv.org/abs/2606.11440v1)
- **PDF:** [https://arxiv.org/pdf/2606.11440v1](https://arxiv.org/pdf/2606.11440v1)
- **Categories:** cs.AI


> The paper introduces **INFRAMIND**, a reinforcement‑learning framework that makes multi‑agent LLM orchestration aware of real‑time infrastructure conditions (GPU queue depths, KV‑cache pressure, latencies). By integrating an infra‑aware planner, executor, and budget‑aware scheduler into a hierarchical constrained MDP, the system dynamically adapts topology, routing, and scheduling to balance response quality, latency, and service‑level objectives. Experiments on five benchmarks show that INFRAMIND achieves up to 7.6 percentage‑point accuracy gains with up to 7× lower latency at low load, and maintains ≈ 99.9 % SLO compliance under heavy load—far outperforming prior orchestration methods that ignore infrastructure state.


<details>
<summary>Abstract</summary>

Existing multi-agent LLM orchestration methods, ranging from brute-force ensembles to learned routers, select models and topologies based on task and model features. However, these methods do not consider the runtime state of the serving infrastructure. On shared GPU clusters under concurrent load, this infrastructure blindness causes systematic resource underutilization: preferred models accumulate deep request queues while equally capable alternatives sit idle. In multi-agent pipelines, where each query triggers multiple sequential model calls, these delays then compound across every downstream step. Closing this gap is challenging because the relevant infrastructure signals (queue depths, KV-cache pressure, latencies) are dynamic and noisy, and they must drive three different decisions: planning, per-step routing, and scheduling. We introduce INFRAMIND, a framework that makes the entire multi-agent stack infrastructure-aware. An infra-aware planner conditions topology and role selection on real-time system load and remaining budget, biasing toward simpler graphs under congestion and richer ones at low load. An infra-aware executor then observes per-model queue depths, cache utilization, and response latencies at each agent step to decide which model to call and how deeply to reason; a budget-aware scheduler further reorders each model's queue so that urgent requests are served first. Cast as a hierarchical constrained MDP and solved end-to-end via reinforcement learning, the system learns to balance quality against latency automatically. Across five benchmarks, INFRAMIND delivers up to +7.6 pp accuracy over the prior baseline at low load with up to 7x lower latency, and sustains up to 99.9% SLO compliance under high load where every baseline drops below 50%.

</details>


### 116. MPC-Patch-Bench: Security-Aware LLM Code Patch for Multi-Party Computation

- **Authors:** Yukuan Zhang, Mengxin Zheng, Qian Lou
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11416v1](http://arxiv.org/abs/2606.11416v1)
- **PDF:** [https://arxiv.org/pdf/2606.11416v1](https://arxiv.org/pdf/2606.11416v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **MPC‑Patch‑Bench**, the first repository‑level benchmark for assessing LLM‑driven code repair on Secure Multi‑Party Computation (MPC) software. It builds a curated dataset of 205 real‑world MPC pull‑request patches using a domain‑specific curation agent and a human‑AI completion pipeline, and defines an MPC‑aware verifier that checks both functional correctness and cryptographic safety (dynamic differential testing against plaintext oracles plus static MPC security rules). Experiments show that even the best LLM can fix only 22.9 % of the tasks, and when security and numerical‑fidelity constraints are enforced the verified success rate drops to 17.1 %, highlighting a serious gap in current agentic AI capabilities for secure code synthesis.


<details>
<summary>Abstract</summary>

Repository-level benchmarks for evaluating Large Language Model (LLM) code repair on Secure Multi-Party Computation (MPC) software do not yet exist, and directly transplanting general-purpose benchmarks such as SWE-bench fails on three structural fronts: (i) MPC repositories are dominated by generic Python infrastructure rather than cryptographic logic; (ii) high-value MPC fixes lack the standardized tests rigid extraction pipelines require; and (iii) standard fail-to-pass evaluation is insufficient for code that must also be cryptographically safe. MPC is increasingly deployed for privacy-preserving machine learning, biomedical collaboration, and secure analytics. Existing MPC-specific code-synthesis efforts cover only operator-level or single-framework tasks; evaluating LLM agents on real repository-level MPC repair instead demands MPC-aware data curation and a verifier matched to the security and numerical-fidelity guarantees MPC programs must obey neither of which existing benchmarks provide. We introduce MPC-Patch-Bench, a repository-level benchmark organised around two frameworks. (1)The Data Curation Framework combines a domain-specific curation agent that filters raw pull requests through three cryptographic layers with a human-AI completion engine that synthesizes missing problem statements and Fail-to-Pass/Pass-to-Pass tests, yielding 205 fully verified instances. (2)The MPC Verifier provides dedicated security and numerical-fidelity checks via dynamic differential testing against plaintext oracles and MPC-specific static analysis rules that flag unsafe reveals, insecure arithmetic, and illegal public/private casts. The strongest evaluated LLM functionally resolves only 22.9% of MPC-Patch-Bench tasks; the MPC Verifier further reduces verified resolution to 17.1%, with up to 40% of functionally-passing patches rejected for cryptographic or numerical-fidelity violations.

</details>


### 117. When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped, Model-Agnostic Retrieval

- **Authors:** Nabaraj Subedi, Ahmed Abdelaty, Shivanand Venkanna Sheshappanavar
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11350v1](http://arxiv.org/abs/2606.11350v1)
- **PDF:** [https://arxiv.org/pdf/2606.11350v1](https://arxiv.org/pdf/2606.11350v1)
- **Categories:** cs.CL, cs.IR


> **Main contribution:** The paper identifies and remedies “vector‑search dilution,” a failure mode in Retrieval‑Augmented Generation (RAG) where expanding a heterogeneous corpus causes dense vectors to lose discriminative power and retrieval accuracy to collapse. It introduces **MASDR‑RAG (Multi‑Agent Scoped Domain Retrieval for RAG)**, a model‑agnostic framework that first narrows the search space using domain‑level metadata (organization‑oriented scoping) and then performs a single synthesis step, reserving full multi‑agent orchestration for truly multi‑domain settings.  

**Methodology:** The authors evaluate MASDR‑RAG on 200 expert‑validated queries across five LLM backbones, six corpora (including a real‑world Wyoming DOT dataset that grew from 54 to 1,128 documents), and two indexing stacks (dense‑only and hybrid dense + sparse), measuring precision‑at‑10 and end‑to‑end answer accuracy.  

**Key findings:** Domain scoping alone boosts P@10 from 0.77 to 0.86 ( p < 0.05 ) and restores answer accuracy from < 40 % back to ≈ 75 % even as the corpus scales, while extensive multi‑agent orchestration yields diminishing returns and introduces a “precision‑faithfulness paradox” (high configuration sensitivity). The practical take‑away for agentic AI systems is to **scope the retrieval domain first**, then invoke a single generation call, using multi‑agent pipelines only when multiple distinct domains genuinely coexist.


<details>
<summary>Abstract</summary>

Retrieval-augmented generation degrades when scaled to large, heterogeneous document collections, where dense similarity loses discriminative power, and top-k retrieval increasingly returns semantically similar but contextually incorrect chunks. We refer to this failure mode as vector search dilution. Even when using hybrid dense+sparse retrieval, we observed this firsthand in a deployed Wyoming Department of Transportation corpus, where scaling from 54 to 1,128 documents (88,907 chunks) reduced accuracy from 75% to below 40%. To address this dilution, we propose MASDR-RAG ( Multi-Agent Scoped Domain Retrieval for RAG) and evaluate it on 200 expert-validated queries across five LLM backbones, six corpora, and two index stacks. Our results indicate that domain scoping using organizational metadata is the key fix, significantly improving P@10 from 0.77 to 0.86 ($p < 0.05$). Furthermore, our investigation of multi-agent orchestration revealed that a high degree of configuration dependence results --creating what we call the precision-faithfulness paradox. Based on these varied outcomes, our practical recommendation is simple: scope first, then perform a single synthesis call, reserving full multi-agent orchestration for genuinely multi-domain corpora paired with native-tool-call backbones. Code and Data will be made public upon acceptance.

</details>


### 118. Can AI Agents Synthesize Scientific Conclusions?

- **Authors:** Hayoung Jung, Pedro Viana Diniz, José Reinaldo Corrêa Roveda, Abner Fernandes da Silva, Haeun Jung, Enoch Tsai, Aleksandra Korolova, Manoel Horta Ribeiro
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11337v1](http://arxiv.org/abs/2606.11337v1)
- **PDF:** [https://arxiv.org/pdf/2606.11337v1](https://arxiv.org/pdf/2606.11337v1)
- **Categories:** cs.AI, cs.CL, cs.CY


> **Main contribution** – The paper introduces **SciConBench**, a large‑scale benchmark (9.1 K expert‑written scientific‑conclusion questions drawn from systematic reviews) together with an **atomic‑fact evaluation pipeline** and a **clean‑room harness (SciConHarness)** that forces agents to retrieve information via controlled web access, thereby eliminating data‑leakage and providing a realistic measure of open‑domain scientific synthesis.

**Methodology** – Agents are tasked with retrieving relevant evidence, reasoning across sources, and generating a conclusion. Generated conclusions are automatically decomposed into atomic facts, and **precision, recall, and F1** are computed against the expert ground truth. Eight state‑of‑the‑art large language models and dedicated research agents are evaluated both in an unconstrained setting and under the clean‑room harness.

**Key findings** – Even the best model attains only **F1 ≈ 0.34** under clean‑room conditions, and performance drops markedly compared with the unconstrained setting, indicating that prior results are inflated by leakage. Consumer‑facing agents (e.g., Google AI Overview, OpenEvidence) often produce incomplete or contradictory conclusions despite having the correct answer available. The study thus shows that reliable synthesis of scientific conclusions remains an open challenge and that clean‑room evaluation is essential for honest assessment of agentic AI in high‑stakes domains.


<details>
<summary>Abstract</summary>

Scientific AI agents increasingly retrieve evidence, reason across sources, and synthesize conclusions used in consequential decisions. Yet, their ability to do so in high-stakes domains such as health remains unclear. We introduce SciConBench, a large-scale live benchmark of 9.11K questions and expert-written conclusions from systematic reviews to evaluate open-domain scientific conclusion synthesis. The benchmark draws on an expert-validated automated evaluation pipeline that decomposes conclusions into atomic facts and measures correctness and comprehensiveness via factual precision and recall. To mitigate data leakage, we further introduce SciConHarness, a clean-room evaluation harness that equips agents with controlled web interaction to ensure valid measurement. Evaluating 8 frontier models and deep research agents, we find that factual quality remains low: under clean-room settings, the best agent achieves only a factual F1 of 0.337. Our clean-room setting consistently reduces performance relative to unconstrained evaluation, suggesting that leakage inflates estimates of models' true synthesis capabilities. Finally, we audit consumer-facing agents (e.g., Google AI Overview, OpenEvidence) and find they frequently generate incomplete and sometimes contradictory conclusions, even when the ground-truth answer is available. Overall, our results show that reliable synthesis of scientific conclusions remains an open challenge, and that clean-room evaluation is essential for assessing open-domain AI agents.

</details>


### 119. FlowBank: Query-Adaptive Agentic Workflows Optimization through Precompute-and-Reuse

- **Authors:** Lingzhi Yuan, Chenghao Deng, Fangxu Yu, Souradip Chakraborty, Mohammad Rostami, Furong Huang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11290v1](http://arxiv.org/abs/2606.11290v1)
- **PDF:** [https://arxiv.org/pdf/2606.11290v1](https://arxiv.org/pdf/2606.11290v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> The paper introduces **FlowBank**, a three‑stage framework that builds a compact “bank” of complementary LLM‑driven agentic workflows and dynamically selects the most suitable one for each query, thereby reconciling the offline‑heavy single‑workflow search and the costly per‑query synthesis paradigms. It first diversifies the search (DiverseFlow) to generate a high‑coverage set of candidate workflows, then curates this set (CuraFlow) into a small, low‑redundancy portfolio, and finally predicts edge values on a query‑workflow bipartite graph to route each incoming request to the workflow with the highest expected utility. Experiments on five benchmarks show that FlowBank outperforms both automated and handcrafted baselines, achieving a 4.26 % average improvement over the strongest automated methods and 14.92 % over handcrafted ones while remaining cost‑competitive.


<details>
<summary>Abstract</summary>

Large Language Model (LLM)-based multi-agent systems are increasingly powerful, but current agentic workflow optimization paradigms make an unsatisfying trade-off. Task-level methods spend substantial offline compute yet deploy only a single workflow, leaving complementary candidates unused, while query-level methods synthesize a new workflow per query at substantial inference cost. Our motivating analysis shows these paradigms are more complementary than competing: workflows discovered during offline search often solve different subsets of queries, and many queries handled by expensive query-level generation can already be solved by cheaper precomputed workflows. This suggests a different objective: rather than searching for one universally best workflow or regenerating one per instance, we should build a compact bank of reusable, complementary workflows and select among them adaptively at inference time. Doing so requires solving three coupled problems: generating complementary rather than redundant candidates, compressing them into a small deployable portfolio, and assigning each query to the right workflow under a performance-cost trade-off. To this end, we present FlowBank, a three-stage framework for portfolio-based agentic workflow optimization. Diversifying proposes DiverseFlow to steer search toward under-covered queries and produce a high-coverage candidate pool. Curating proposes CuraFlow to compress this pool into a compact portfolio with minimal redundancy. Matching casts deployment as edge-value prediction on a query-workflow bipartite graph and routes each incoming query to the portfolio member with the best predicted utility. Across five benchmarks, FlowBank achieves the highest average score among the evaluated methods while remaining cost-competitive, improving over the strongest automated and handcrafted baselines by 4.26% and 14.92% relative, respectively.

</details>


### 120. EEVEE: Towards Test-time Prompt Learning in the Real World for Self-Improving Agents

- **Authors:** Weixian Xu, Shilong Liu, Mengdi Wang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11182v1](http://arxiv.org/abs/2606.11182v1)
- **PDF:** [https://arxiv.org/pdf/2606.11182v1](https://arxiv.org/pdf/2606.11182v1)
- **Categories:** cs.LG, cs.AI


> EEVEE introduces the first test‑time prompt‑learning framework that lets large‑language‑model agents continuously adapt while processing heterogeneous real‑world task streams coming from many datasets and domains. It does so with a router that clusters incoming inputs and routes each cluster to a dedicated prompt, and a co‑evolution training loop that alternates between improving the router’s assignments and fine‑tuning the prompts to avoid cross‑dataset interference. Across several benchmark collections, EEVEE raises the average multi‑benchmark score by 10–24 points over strong base models (Qwen‑3‑4B‑Instruct, DeepSeek‑V3.2) and outperforms prior test‑time adaptation methods (GEPA, ACE) by up to ~48 %, demonstrating more robust and efficient self‑improvement for agentic LLMs in realistic, multi‑task environments.


<details>
<summary>Abstract</summary>

In this paper, we propose EEVEE, the first multi-dataset test-time prompt learning framework for LLM agents, enabling test-time prompt learning under real-world task streams. Existing methods are largely designed for single-dataset settings, while real-world applications require models to handle heterogeneous input streams drawn from multiple datasets, domains, and task distributions, limiting their practical applicability. To mitigate cross-dataset interference, EEVEE introduces a router that partitions incoming inputs into task clusters and assigns them to suitable prompt configurations. This design is optimized via a router-prompt co-evolution strategy, which employs interleaved router and prompt learning phases to address their mutual dependency. Experiments across multiple datasets demonstrate that the framework improves robustness under heterogeneous data streams while maintaining single-benchmark learning capability and efficiency. Specifically, EEVEE improves average multi-benchmark scores by 10.38 and 24.32 points over Qwen3-4B-Instruct and DeepSeek-V3.2, surpassing SOTA methods GEPA and ACE by up to 37.2% and 48.2%.

</details>


### 121. Data Journalist Agent: Transforming Data into Verifiable Multimodal Stories

- **Authors:** Kevin Qinghong Lin, Batu EI, Yuhong Shi, Pan Lu, Philip Torr, James Zou
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11176v1](http://arxiv.org/abs/2606.11176v1)
- **PDF:** [https://arxiv.org/pdf/2606.11176v1](https://arxiv.org/pdf/2606.11176v1)
- **Categories:** cs.CV, cs.CL, cs.CY, cs.HC


> **Main contribution** – The paper introduces **Data Journalist Agent (Data2Story)**, a multi‑agent system that integrates specialized data‑science, writing, and design agents into a single “virtual newsroom” capable of producing end‑to‑end, evidence‑grounded, multimodal news stories.  

**Methodology** – Data2Story orchestrates a hierarchy of agents (an “Inspector” for traceability, a “Story‑builder” for angle selection, and multimodal generators for charts, maps, audio, etc.) and evaluates the pipeline on 18 real‑world articles, comparing its output to human‑written pieces across angle coverage, rubric‑based quality (53 participants), automated interaction cost, and a formal verifiability check that re‑executes code and validates citations.  

**Key findings** – The system generates fully auditable stories that match human articles in transparency, traceability, and multimodal richness, while lagging behind humans in editorial nuance, creative design, and overall presentation quality. The results suggest that such a collaborative agent can substantially augment journalists, enabling faster, more evidence‑based, and verifiable reporting.


<details>
<summary>Abstract</summary>

Data tells stories that shape society; the data journalist's job is to turn raw information into stories non-experts can trust. A high-quality news feature takes a newsroom team weeks: hunting for context, running statistics, choosing an angle, and designing visuals. Recent agents handle individual steps well: data-science agents close the analysis loop, while design agents synthesize beautiful websites. But can an agent serve as a data journalist end to end? We introduce Data Journalist Agent (Data2Story), a multi-agent framework that orchestrates specialized roles into a single virtual newsroom. Data2Story contributes two innovations. (i) Claims are evidence-grounded: an Inspector links every number, angle, and asset back to data, code, or an external reference. (ii) Articles are multimodally generative: rather than defaulting to plain text and static charts, Data2Story reasons about what readers will want to see, then deploys multimodal tools, such as interactive maps for geography and audio for music. We evaluate Data2Story on 18 articles, each paired with the originally published expert piece, along four axes: (a) human-agent angle coverage; (b) rubric evaluation with 53 participants across five dimensions; (c) computer-use agents as judges, a cost-saving proxy for how readers navigate interactive articles; and (d) verifiability, where a coding verifier re-executes statements against the data and checks claims against references. Data2Story produces competitive, evidence-traceable multimedia stories, with particular strength in transparency and auditability. Human articles retain an edge in editorial angle, creative design, and presentation. We position Data2Story as a collaborator for journalists, enabling more evidence-based, transparent, and verifiable reporting. Code and demos are available at https://data2story.github.io.

</details>


### 122. ABC-Bench: An Agentic Bio-Capabilities Benchmark for Biosecurity

- **Authors:** Andrew Bo Liu, Samira Nedungadi, Bryce Cai, Alex Kleinman, Harmon Bhasin, Seth Donoughe
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11150v1](http://arxiv.org/abs/2606.11150v1)
- **PDF:** [https://arxiv.org/pdf/2606.11150v1](https://arxiv.org/pdf/2606.11150v1)
- **Categories:** cs.AI, cs.CY


> The paper introduces **ABC‑Bench**, a novel benchmark suite that quantifies how well large‑language‑model agents can perform biosecurity‑relevant, in‑silico biology tasks such as programming liquid‑handling robots, designing DNA fragments for assembly, and bypassing DNA‑synthesis screening. By prompting several state‑of‑the‑art LLM agents (including OpenAI’s o4‑mini‑high) to solve these tasks, the authors evaluate both “benign” and dual‑use capabilities, showing that all agents surpass the median human expert on the three benchmark tasks—especially those grounded in established protocols—while struggling more on novel bioinformatics reasoning; wet‑lab validation confirms that the generated robot scripts correctly assembled the intended DNA sequences. These results highlight the rapid emergence of agentic bio‑capabilities and underscore the need for systematic assessment frameworks in the agentic AI and biosecurity domains.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are rapidly acquiring capabilities relevant to biological research, from literature synthesis to interpretation of experimental data. Increasingly, LLM agents can also perform in silico biology tasks that previously required experienced human biologists. These emerging AI capabilities offer new opportunities for scientific discovery and biomedical advances, but they also shift the landscape of biosecurity risks. To address this, we introduce the Agentic Bio-Capabilities Benchmark (ABC-Bench), a suite of tasks to measure agentic biosecurity-relevant capabilities. ABC-Bench evaluates LLM agents on both benign and dual-use biology tasks: writing code to operate liquid handling robots, designing DNA fragments for in vitro assembly, and evading DNA synthesis screening. These tasks require a combination of biology and software expertise. All tested LLM agents outperformed the median expert human baseliner on all three tasks. Agents performed highly on tasks drawing on published knowledge and well-documented protocols, and more weakly on a task requiring novel bioinformatics reasoning. In three wet-lab validation experiments, we found that OpenAI's o4-mini-high produced scripts that, when run on an OpenTrons liquid handling robot, successfully assembled DNA with expected sequences.

</details>


### 123. Monte Carlo Pass Search: Using Trajectory Generation for 3D Counterfactual Pass Evaluation in Football

- **Authors:** Andrew Kang, Priya Narasimhan
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11120v1](http://arxiv.org/abs/2606.11120v1)
- **PDF:** [https://arxiv.org/pdf/2606.11120v1](https://arxiv.org/pdf/2606.11120v1)
- **Categories:** cs.AI, cs.CV


> The paper introduces **Monte Carlo Pass Search (MCPS)**, a framework that treats football pass evaluation as a Monte‑Carlo‑Tree‑Search problem by combining (i) a learned possession‑value model, (ii) a multi‑agent world model that predicts 3‑D ball‑conditioned trajectories, and (iii) a noisy policy that samples counterfactual pass executions and options. The authors adapt the SMART autoregressive trajectory generator from autonomous driving to model player‑ball dynamics on the newly released high‑fidelity 3‑D Bundesliga tracking dataset, achieving state‑of‑the‑art “best‑of‑20” rollout accuracy while remaining sample‑efficient. Using this world model, MCPS rolls out many imagined pass variants, scores each with the value model, and derives both mean‑based and percentile‑based execution‑surplus metrics, enabling richer, distribution‑aware attribution of pass quality for agentic AI analyses of sports tactics.


<details>
<summary>Abstract</summary>

We recast pass evaluation in football (soccer) as a Monte Carlo Tree Search (MCTS)-like evaluation problem whose components mostly exist in the literature under different names: a value model (possession value), a world model (multi-agent trajectories with ball interactions), and a policy over counterfactual actions (sampling pass variants with noise). Building on the first public high-fidelity tracking dataset with 3D ball trajectories from the Bundesliga, we introduce Monte Carlo Pass Search (MCPS), which infers kick parameters for each observed pass, samples execution variants and option variants, rolls each candidate forward with a ball-conditioned world model until the next ball interaction, and scores outcomes with a learned value model to obtain a distribution over gained value. This distribution enables distribution-aware attribution with two complementary execution-surplus scores used for analysis and ranking: mean-based and percentile-based scores. To make the world model sample-efficient under limited public data, we adapt a discrete-token, autoregressive trajectory generator from autonomous driving (SMART) and show it yields strong best-of-20 forecasting accuracy compared to baselines, while supporting fully hypothetical rollouts for downstream evaluation. We have released model checkpoints and code.

</details>


### 124. The Shibboleth Effect: Auditing the Cross-Lingual Distributional Skew of Large Language Models

- **Authors:** Hakan Mehmetcik
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11082v1](http://arxiv.org/abs/2606.11082v1)
- **PDF:** [https://arxiv.org/pdf/2606.11082v1](https://arxiv.org/pdf/2606.11082v1)
- **Categories:** cs.CL, cs.CY


> **Contribution:** The paper uncovers and quantifies a “Shibboleth Effect”—systematic cross‑lingual behavioral skew—in frontier large language models (LLMs) when they are placed in a high‑stakes, adversarial multi‑agent simulation of a maritime crisis, revealing that language can dramatically alter the models’ diplomatic posture.  

**Methodology:** Researchers built a multi‑agent geopolitical wargame (the Cerulean Sea Crisis) and ran a between‑groups experiment with six state‑of‑the‑art LLMs (GPT‑4o, Llama‑4, Mistral‑Large, Gemini‑3.1‑Pro, Qwen 3.6‑Plus, DeepSeek‑R1). Each model played ten games in either English or Turkish, producing 586 validated statements. A zero‑shot classifier measured two continuous behavioral traits—Concession Rate and Coercive Rhetoric—allowing within‑model comparisons across languages, with Holm‑corrected statistical tests.  

**Key Findings:** The effect is highly model‑specific: Llama‑4 becomes markedly more coercive in Turkish (+0.800, p = .002), while Gemini‑3.1‑Pro and DeepSeek‑R1 become significantly less coercive (‑0.750 and ‑0.860, respectively). GPT‑4o shows no significant shift. The authors identify two buffering mechanisms that mitigate skew—chain‑of‑thought institutional anchoring and multilingual RLHF alignment—suggesting design pathways for safer deployment of LLMs in diplomatic or crisis‑management contexts.


<details>
<summary>Abstract</summary>

This study investigates cross-lingual distributional skew (the Shibboleth Effect) in frontier large language models (LLMs) subjected to sustained adversarial conditions. We develop a multi-agent geopolitical wargame, the Cerulean Sea Crisis, a synthetic maritime territorial dispute designed to mirror the structural dynamics of Eastern Mediterranean conflicts. Six frontier models (GPT-4o, Llama-4, Mistral-Large, Gemini-3.1-Pro, Qwen3.6-Plus, and DeepSeek-R1) participate in a between-groups experiment (N = 10 games per arm, K = 5 rounds per game) in which the sole manipulation is the language of play (English versus Turkish), producing 586 validated statements. A zero-shot classifier assesses behavioral dispositions along two continuous dimensions: Concession Rate and Coercive Rhetoric. The results are heterogeneous. Llama-4 shows a substantial, Holm-corrected increase in coercive rhetoric under Turkish (delta = +0.800, p = .002), whereas Gemini-3.1-Pro displays an equally large decrease (delta = -0.750, p = .005). DeepSeek-R1 exhibits a similar negative shift (delta = -0.860, p = .006) and provides chain-of-thought evidence consistent with a buffering mechanism. GPT-4o shows no detectable effect (delta = +0.130, p = .614). These findings indicate that cross-lingual behavioral skew is contingent on model architecture and training regime rather than a universal property of Western-origin LLMs. We identify two distinct buffering mechanisms, chain-of-thought institutional anchoring and multilingual RLHF alignment, and discuss their implications for integrating LLMs safely into diplomatic and crisis-management settings.

</details>


### 125. Phi-Actor-Critic: Steering General-Sum Games to Pareto-Efficient Correlated Equilibria

- **Authors:** Wongyu Lee, Francesco Lelli, Omran Ayoub, Massimo Tornatore
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11284v1](http://arxiv.org/abs/2606.11284v1)
- **PDF:** [https://arxiv.org/pdf/2606.11284v1](https://arxiv.org/pdf/2606.11284v1)
- **Categories:** cs.MA, cs.GT, cs.LG


> The paper introduces **Φ‑Actor‑Critic (Φ‑AC)**, a deep multi‑agent RL framework that augments standard actor‑critic learning with swap‑regret minimization in order to drive agents toward **high‑welfare correlated equilibria** rather than arbitrary Nash equilibria in general‑sum games. Φ‑AC uses a centralized attention‑based critic that outputs vector‑valued counterfactual regrets in a single forward pass, and a Lagrangian equilibrium‑selection step that maximizes social welfare while enforcing regret‑based stability constraints. Empirically, the method outperforms value‑decomposition and policy‑gradient baselines on matrix games, Multi‑Agent Particle Environments, and the Melting‑Pot “Harvest” scenario, achieving superior collective returns, fairer outcomes, and stable coordination across mixed‑motive tasks.


<details>
<summary>Abstract</summary>

Real-world multi-agent systems, from traffic coordination to resource allocation, are often modeled as general-sum games where individual incentives conflict with collective welfare. In these settings, the central challenge is not merely finding an equilibrium, but selecting socially desirable outcomes among many suboptimal Nash equilibria. Standard deep multi-agent reinforcement learning (MARL) methods struggle with this problem, as value-decomposition approaches are constrained by monotonicity assumptions and policy-gradient methods often converge to stable but socially inefficient equilibria. To address this limitation, we propose $Φ$-Actor-Critic ($Φ$-AC), a framework that leverages swap regret minimization to steer learning toward high-welfare correlated equilibria (CE). To make counterfactual regret estimation tractable in deep MARL, $Φ$-AC employs a centralized attention critic that predicts vector-valued regrets in a single forward pass, avoiding computationally expensive counterfactual simulations. We further introduce a Lagrangian-based equilibrium selection mechanism that optimizes social welfare while enforcing stability through regret constraints. Experiments on matrix games, Multi-Agent Particle Environments (MPE), and the Melting Pot Harvest scenario demonstrate that $Φ$-AC learns efficient and stable coordination strategies across diverse mixed-motive settings while maintaining high collective return and competitive fairness.

</details>


### 126. LLM-Mediated Demand Response Coordination in Smart Microgrids

- **Authors:** J. de Curtò, I. de Zarzà
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11050v1](http://arxiv.org/abs/2606.11050v1)
- **PDF:** [https://arxiv.org/pdf/2606.11050v1](https://arxiv.org/pdf/2606.11050v1)
- **Categories:** cs.MA, cs.GT, eess.SY


> The paper introduces an “LLM Influence Compiler” that translates high‑level demand‑response policies into structured directives for heterogeneous prosumer agents in a smart‑microgrid simulation. Each agent combines a game‑theoretic base decision rule (derived from payoff history, neighbor imitation, and exploitation memory) with a narrative‑level evaluation of the LLM‑generated signal, allowing the system to avoid the over‑cooperative bias observed when LLMs are used as direct decision makers. Experiments show that this hybrid architecture raises cooperative curtailment from ~27 % (no intervention) to 33.3 % with structured messages, and that targeting high‑centrality nodes in the social network further amplifies the effect, demonstrating that structured LLM compilation, grounded agent reasoning, and topology‑aware dissemination are complementary design principles for scalable demand‑response coordination.


<details>
<summary>Abstract</summary>

Effective demand response in smart microgrids requires prosumers to cooperate voluntarily under strategic self-interest, a coordination problem structurally equivalent to a repeated Prisoner's Dilemma on a social network. This paper presents a multi-agent simulation in which a Large Language Model (LLM) Influence Compiler issues structured demand-response directives to a population of heterogeneous prosumer agents, each governed by a hybrid decision architecture combining game-theoretic base probability (derived from payoff history, neighbour imitation, and exploitation memory) with LLM narrative evaluation of incoming coordination signals. The hybrid architecture resolves a key methodological challenge: LLMs aligned via Reinforcement Learning from Human Feedback (RLHF) exhibit strong cooperation bias when used as direct decision-makers, producing flat dynamics regardless of grid conditions. By separating strategic reasoning from grounded narrative evaluation, the model generates realistic prosumer behaviour across six personality archetypes, with baseline cooperation near 50% and clear differentiation under influence. Compiled structured directives achieve 33.3% demand-curtailment cooperation versus 27.0% for unstructured messaging and 28.0% for a no-intervention baseline ($Δ_\mathrm{comp} = +0.063$), with the advantage preserved across both grounded and idealized agent substrates ($Δ= +0.083$) and across all resistance levels ($R = 0.1$ to $0.7$). Hub-targeted dissemination via high-centrality network nodes outperforms peripheral or random targeting, confirming that grid topology provides mechanistic amplification independent of message content. These results suggest that structured LLM compilation, grounded agent reasoning, and network-aware targeting are complementary design principles for scalable, interpretable demand-response coordination in smart-city energy systems.

</details>


### 127. Workflow-GYM: Towards Long-Horizon Evaluation of Computer-use Agentic tasks in Real-World Professional Fields

- **Authors:** Liya Zhu, Jingzhe Ding, Jian Zhang, Jianbo Xue, Shihao Liang, Ge Zhang, Yi Zhu, Duju Zeng, Xiang Gao, Qingshui Gu, Mailun Gao, Huimin Che, Yan Zhao, Peiheng Zhou, Haojun Wang, Chaobo Xian, Lili Le, Chi Wu, Yiwei Liu, Shengda Long, Jiale Yang, Fangzhi Xu, Sijin Wu, Haodong Duan, Chao He, Zhaojian Li, Minchao Wang, Huan Zhou, Jiani Hou, Chuqian Yu, Weiran Shi, Hongwan Gao, Jiamin Chen, Guanhong Chen, Tingqin Luo, Kaiyuan Zhang, Zhixin Yao, Qing Hua, Yuhao Jiang, Jin Chen, Pu Chen, Zhenyu Hu, Xingyu Li, Zhengxuan Jiang, Meng Cao, Tianfeng Long, Haozhe Wang, Mingzhang Wang, Yichen Zhang, Yiming Dai, Chenchen Zhang, Jiaying Wang, Xinying Liu, Xingzu Liu, Lingling Zhang, Xinjie Chen, Yujia Qin, Wangchunshu Zhou, Zhiyong Wu, Yang Liu, Jiaheng Liu, Lei Zhang, Shen Yan, Wenhao Huang, Zaiyuan Wang, Xiaolong Chang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11042v3](http://arxiv.org/abs/2606.11042v3)
- **PDF:** [https://arxiv.org/pdf/2606.11042v3](https://arxiv.org/pdf/2606.11042v3)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Workflow‑GYM**, a benchmark suite that evaluates AI agents on long‑horizon, high‑value professional workflows requiring interaction with domain‑specific graphical user interfaces (e.g., CAD, finance, medical software), filling a gap left by existing short‑horizon, general‑purpose GUI tests.  

**Methodology:** The authors curated a set of multi‑step tasks across several professional fields, defined success metrics for end‑to‑end workflow completion, and measured the performance of several state‑of‑the‑art GUI‑agents (including LLM‑driven and vision‑guided models) on these tasks.  

**Key findings:** Even the best current agents achieve only modest (~30 %) success, predominantly failing due to workflow stage omission, error propagation, objective drift, and poor comprehension of specialized software environments, highlighting that long‑horizon professional GUI manipulation remains an open challenge and pointing to the need for better memory, planning, and domain‑specific knowledge in future agentic AI systems.


<details>
<summary>Abstract</summary>

Recent years have witnessed the rapid evolution of AI agents toward handling increasingly complex, real-world tasks. However, existing benchmarks rarely evaluate whether agents can operate graphical user interfaces to complete long-horizon, high-value professional workflows across diverse domains. Current GUI benchmarks still predominantly focus on general-purpose software, relatively simple applications, and short-horizon tasks, leaving it largely unknown whether modern agents can follow user instructions to autonomously operate domain-specific professional software and accomplish economically valuable work in an end-to-end manner. To bridge this gap, we introduce Workflow-GYM, a benchmark for long-horizon GUI tasks centered on professional domains and specialized software environments. Through extensive experiments on state-of-the-art models, we find that even the strongest models achieve only slightly above 30% success rates, highlighting that professional long-horizon GUI workflows remain highly challenging for current GUI agents. Further analysis reveals that current agents struggle to maintain long-horizon workflow consistency, frequently exhibiting workflow stage omission, error propagation, objective drift, and insufficient understanding of professional software environments. Our findings provide important insights into the limitations of current agent systems and suggest key directions for the next generation of GUI-agent research.

</details>


### 128. Understanding and mitigating the risks of OpenClaw for non-technical users: A practical guide with Skill

- **Authors:** Junchang Zheng, Junfeng Tan, Jialiang Lin
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11007v1](http://arxiv.org/abs/2606.11007v1)
- **PDF:** [https://arxiv.org/pdf/2606.11007v1](https://arxiv.org/pdf/2606.11007v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> **Main contribution:** The paper bridges a critical gap by translating the security concerns of the OpenClaw AI‑agent framework into a practical, non‑technical guide and an accompanying “Skill” that automatically hardens OpenClaw installations.  

**Methodology:** The authors first conduct a threat analysis to isolate seven core risks that everyday OpenClaw users face, then rewrite each risk and its mitigation as plain‑language, step‑by‑step instructions. Finally, they implement these mitigations in a reusable OpenClaw Skill that programmatically applies the recommended configurations with a single command.  

**Key findings:** The risk taxonomy and automated Skill demonstrate that non‑technical users can effectively reduce exposure to agentic AI threats without deep security expertise, showing measurable reductions in misconfiguration and unintended agent actions when the Skill is deployed. This work shows a scalable pathway for democratizing defensive practices in agentic AI ecosystems.


<details>
<summary>Abstract</summary>

OpenClaw has rapidly emerged as a transformative artificial intelligence (AI) agent framework, and its ability to autonomously execute complex, multi-step tasks has attracted an ever-growing and diverse user base. However, this capability comes with significant risks. While existing research has made important strides in characterizing these threats, such work is predominantly directed at technically sophisticated audiences. It remains largely inaccessible to non-technical users. This demographic now makes up an increasingly large and underserved portion of the community, yet it is these very users who most urgently need practical and straightforward guidance. In response, we bridge this gap through a series of interconnected efforts designed to lower the risk barrier for non-technical OpenClaw users. First, we identify and categorize seven core risks that OpenClaw users may encounter in daily usage, explaining each in plain language so that non-technical users can readily grasp the nature and potential consequences of these threats. Second, for each identified risk, we distill a set of corresponding defensive strategies into clear and actionable operational steps that are easy to follow. Third, to make protection even easier, we provide a companion OpenClaw Skill that automates key security configurations, enabling users to safeguard their systems with minimal manual intervention. Through this work, we demonstrate that safeguarding against the risks of intelligent agents need not be the exclusive domain of security experts, and that non-technical users can meaningfully participate in reducing these risks through simple, practical actions.

</details>


### 129. Trace Only What You Need: Structure-Aware On-Demand Hypergraph Memory for Long-Document Question Answering

- **Authors:** Xiangjun Zai, Xingyu Tan, Chen Chen, Xiaoyang Wang, Wenjie Zhang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10921v1](http://arxiv.org/abs/2606.10921v1)
- **PDF:** [https://arxiv.org/pdf/2606.10921v1](https://arxiv.org/pdf/2606.10921v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **DocTrace**, a multi‑agent retrieval‑augmented generation (RAG) system that builds a *query‑driven, structure‑aware hypergraph memory* for reasoning over very long documents, and that records successful reasoning paths for later reuse.

**Methodology:** DocTrace (1) indexes each document as a lightweight hierarchical tree to preserve headings and section relationships, (2) during a query it dynamically assembles a shared hypergraph memory where nodes are retrieved passages and edges encode intra‑document structural links and cross‑passage evidential relations, and (3) after a successful answer it stores the hypergraph reasoning plan in an experience memory that subsequent agents can retrieve to guide future queries on related documents.

**Key findings:** Across four long‑document QA benchmarks, DocTrace outperforms the strongest prior structured‑RAG baseline (ComoRAG) by up to **8.85 % F1** and **4.40 % exact match**, while cutting total computation by **≈53 %** thanks to on‑demand memory construction and reuse of past reasoning—demonstrating that structure‑aware, experience‑guided hypergraph memories substantially improve efficiency and accuracy for agentic long‑document QA.


<details>
<summary>Abstract</summary>

Long-document question answering (QA) requires large language models (LLMs) to reason over evidence scattered across lengthy documents, where answers often depend on event order, section-level context, and cross-part evidence connections. Although retrieval-augmented generation (RAG) reduces the input context by retrieving relevant evidence, existing structured RAG methods still face three limitations: costly query-agnostic knowledge organization, insufficient use of original document structure, and no reuse of historical reasoning experience. To address these limitations, we propose DocTrace, a multi-agent RAG framework for long-document QA that supports query-triggered knowledge organization, document-structure-aware and experience-guided reasoning. DocTrace preserves document hierarchy with a lightweight document structural tree index, constructs agent-shared hypergraph-structured working memory on demand during reasoning, and stores successful reasoning plans in graph-structured experience memory for future reuse, enabling adaptive exploration across related long-document questions. Experiments on four long-document QA datasets show that DocTrace achieves the best performance on three datasets, surpassing the strongest baseline, ComoRAG, by up to 8.85% in F1 and 4.40% in EM, while reducing the overall computational cost by 53.32%

</details>


### 130. Role-Agent: Bootstrapping LLM Agents via Dual-Role Evolution

- **Authors:** Xucong Wang, Ziyu Ma, Shidong Yang, Tongwen Huang, Pengkun Wang, Yong Wang, Xiangxiang Chu
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10917v1](http://arxiv.org/abs/2606.10917v1)
- **PDF:** [https://arxiv.org/pdf/2606.10917v1](https://arxiv.org/pdf/2606.10917v1)
- **Categories:** cs.AI


> **Contribution:** The paper introduces **Role‑Agent**, a novel framework that lets a single large language model serve simultaneously as the decision‑making agent and as its own simulated environment, enabling a bootstrapped co‑evolution of behavior and world model.  

**Methodology:** Role‑Agent implements two complementary loops: (1) *World‑In‑Agent* (WIA), where the LLM predicts the next world state after each action and receives a reward based on the alignment between predicted and actually observed states, thus encouraging environment‑aware reasoning; and (2) *Agent‑In‑World* (AIW), where the model analyses failed trajectories, retrieves past tasks with similar failure patterns, and reshapes its training distribution to practice those weaknesses.  

**Key Findings:** Across several established LLM‑agent benchmarks, the dual‑role approach yields consistent gains, improving average performance by **>4 %** relative to strong baselines, and demonstrates enhanced generalization through self‑generated feedback and targeted failure‑driven curriculum learning.


<details>
<summary>Abstract</summary>

Although Large Language Model (LLM) agents have demonstrated strong performance on complex tasks, their learning is often limited by inefficient interaction feedback and static training environments, which hinder broader generalization. To address these limitations, this paper introduces Role-Agent, \textcolor{black}{a framework} that harnesses a single LLM to function concurrently as both the agent and the environment, enabling a bootstrapped co-evolution. Role-Agent comprises two synergistic components: World-In-Agent (WIA) and Agent-In-World (AIW). In WIA, the LLM acts as the agent and predicts future states after each action; the alignment between predicted and actual states is then used as a process reward, encouraging environment-aware reasoning. In AIW, the LLM analyzes failure modes from failed trajectories and retrieves tasks with similar failure patterns, thereby reshaping the training data distribution for targeted practice. Experiments on multiple benchmarks show that Role-Agent consistently improves performance, yielding an average gain of over 4\% over strong baselines.

</details>


### 131. Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration and Activation

- **Authors:** Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10875v1](http://arxiv.org/abs/2606.10875v1)
- **PDF:** [https://arxiv.org/pdf/2606.10875v1](https://arxiv.org/pdf/2606.10875v1)
- **Categories:** cs.CL


> The paper introduces **Knowledge‑Augmented Tool Execution (KATE)**, a framework that enriches large language model (LLM) agents with *experiential* tool‑use knowledge and leverages a “reasoning‑width” inference strategy (parallel sampling with aggregation) together with knowledge‑aware fine‑tuning to improve multi‑step tool execution. By systematically studying knowledge acquisition (instance‑level vs. intent‑level), activation (depth‑ vs. width‑expansion of reasoning), and internalization (supervised fine‑tuning vs. RL), the authors show that simple instance examples, breadth‑oriented sampling, and RL‑based post‑training yield the greatest gains. Experiments on the BFCL‑V3 and AppWorld benchmarks across several model sizes demonstrate that KATE consistently outperforms strong baselines, confirming the importance of integrating and actively activating experiential knowledge for agentic AI.


<details>
<summary>Abstract</summary>

Large language models (LLMs) rely on tool use to act as autonomous agents, yet often fail in multi-step execution due to insufficient tool-related knowledge and ineffective knowledge activation. Therefore, we present a systematic study on how knowledge influences tool-use performance, covering the stages of knowledge acquisition, activation, and internalization. In the knowledge acquisition stage, we acquire and evaluate various forms of experiential knowledge, and our analysis shows that simple instance-level knowledge can already provide strong and reliable gains, while abstract intent-level knowledge offers limited benefits. At inference time, to activate knowledge, we find that prompting LLM to expand the depth of reasoning yields diminishing returns, whereas expanding the width of reasoning by parallel sampling with aggregation more effectively activates latent experiential knowledge. At training time, for knowledge internalization, post-training with knowledge-augmented data further improves performance, with reinforcement learning outperforming supervised fine-tuning. Based on these insights, we propose the Knowledge-Augmented Tool Execution (KATE), a knowledge-augmented tool execution framework that integrates experiential knowledge with reasoning-width-expanded inference and knowledge-aware training. Experiments on BFCL-V3 and AppWorld demonstrate consistent and substantial improvements over strong baselines across model scales. Our Code is available at https://github.com/hypasd-art/KATE.

</details>


### 132. Moonshine: An Autonomous Mathematical Research Agent Centered on Conjecture Generation

- **Authors:** Xiaoyang Chen, Xiang Jiang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10806v1](http://arxiv.org/abs/2606.10806v1)
- **PDF:** [https://arxiv.org/pdf/2606.10806v1](https://arxiv.org/pdf/2606.10806v1)
- **Categories:** cs.AI, math.FA


> Moonshine is an autonomous research agent designed to create and pursue mathematically significant conjectures rather than merely solve isolated problems. It extracts abstract structure from classic questions, formulates new concepts, and iteratively builds a theoretical framework; the paper demonstrates this pipeline on the Jacobian conjecture, where Moonshine reformulates the problem for one‑hidden‑layer affine‑ridge sigmoid networks and proposes the **Neural Jacobian Conjecture (NJC)**. Using large language models (GPT‑5.5‑pro, DeepSeek‑V4‑pro) and interactive prompting with ChatGPT, Moonshine produced independent complete proofs for the case \(N=n+1\) and a geometric‑topological proof via web‑based collaboration, while leaving the higher‑width case open—showcasing the agent’s capacity for autonomous conjecture generation, proof discovery, and collaborative reasoning in the emerging field of agentic AI.


<details>
<summary>Abstract</summary>

Moonshine is an autonomous agent whose central objective is to generate mathematical conjectures. Its core capability is to extract structure from classical problems, distill new concepts, and formulate conjectures of mathematical significance. Rather than treating the solution of a single proposition as its endpoint, Moonshine builds an extensible theoretical framework through conjecture generation, bridge building, and obstacle identification. This article uses Moonshine's exploration of the Jacobian conjecture as an example. It shows how the central logic of whether local nondegeneracy can force global injectivity is transferred to one-hidden-layer affine-ridge sigmoid networks. This leads to the formulation of the \emph{Neural Jacobian Conjecture} (NJC): if such a network has strictly positive Jacobian determinant on the whole space, then it must be globally injective. By invoking GPT-5.5-pro and DeepSeek-V4-pro separately, Moonshine obtained independent complete proofs for the case \(N=n+1\). In addition, with the assistance of ChatGPT through interactive use of its web interface with GPT-5.5-pro, a geometric-topological proof was developed. These results provide preliminary evidence for the plausibility of the conjecture. The general higher-width case \(N\ge n+2\), however, remains unresolved and is left for further investigation. This work illustrates Moonshine's ability to autonomously generate meaningful mathematical problems and make rigorous progress on them.

</details>


### 133. Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use

- **Authors:** Zhixin Ma, Yutong Zhou, Yongqi Li, Chong-Wah Ngo, Wenjie Li
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10803v1](http://arxiv.org/abs/2606.10803v1)
- **PDF:** [https://arxiv.org/pdf/2606.10803v1](https://arxiv.org/pdf/2606.10803v1)
- **Categories:** cs.CL, cs.AI, cs.CV


> The paper introduces **PhysTool‑Bench**, the first large‑scale benchmark (2,510 queries covering 2,678 real‑world tools) for measuring how well multimodal large language models (MLLMs) can **recognize physical tools in complex scenes and generate the correct selection‑and‑use plan** for a given instruction. Using this benchmark, the authors evaluate 13 state‑of‑the‑art MLLMs and find that even the best system (Gemini‑3.1‑Pro) identifies only **≈59 %** of the tools and solves **≈21 %** of the tasks end‑to‑end, exposing a two‑fold deficiency: poor visual perception of tools and a larger shortfall in functional commonsense planning. These results pinpoint tool‑use understanding as a critical bottleneck for deploying agentic AI in embodied, real‑world environments.


<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) excel at utilizing digital APIs and increasingly serve as the "brain" of embodied AI, instructing robots to interact with the physical world. In such embodied settings, a central capability is the use of physical tools, which underpins MLLMs' ability to assist humans in real-world tasks. Despite the importance, MLLMs' proficiency in physical tool use remains largely unexplored. To address this gap, we introduce PhysTool-Bench, the first physical tool-use benchmark designed to evaluate MLLMs' ability to comprehend real-world scenarios, identify physical tools, and plan their use. PhysTool-Bench comprises 2,510 queries over 2,678 real-world physical tools spanning diverse domains, including manufacturing, electrical work, agriculture, and healthcare. Concretely, models are evaluated along two primary dimensions: 1) recognizing all physical tools present in the scene, and 2) planning the tool selection and use sequence based on the instruction and visual context. Across 13 leading MLLMs, even the strongest model (Gemini-3.1-Pro) identifies only 58.7% of tools in a scene and completes merely 21.0% of queries end-to-end. Our analysis reveals a two-level deficit: MLLMs struggle to perceive tools in realistic scenes, and the much larger drop at the planning stage further indicates a lack of functional commonsense for mapping perceived tools onto task semantics, pinpointing a critical bottleneck for the development of practical embodied AI.

</details>


### 134. Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation

- **Authors:** Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10749v1](http://arxiv.org/abs/2606.10749v1)
- **PDF:** [https://arxiv.org/pdf/2606.10749v1](https://arxiv.org/pdf/2606.10749v1)
- **Categories:** cs.CR, cs.AI


> The paper presents a comprehensive taxonomy of security risks for LLM‑driven agents, framing threats in terms of information flow, delegated authority, and persistent state, and mapping 247 prior works onto this lifecycle model. By analyzing attack vectors (e.g., prompt injection, tool‑mediated control‑flow hijacking, state corruption, and multi‑agent propagation) and existing defenses, the authors show that current mitigations are useful but not composable, and that benchmarks largely miss long‑horizon, stateful, and deployment‑specific hazards. They conclude that robustly secure LLM agents require clearly defined trust boundaries, principled privilege management, provenance‑aware state handling, and evaluation methods that reflect realistic operational contexts.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are rapidly moving from conversational interfaces to software components that plan, invoke tools, maintain memory, and act on external environments. This transition changes the nature of security risk. In agentic settings, failures are no longer limited to unsafe text generation. Untrusted content may redirect control flow, misuse tool privileges, corrupt persistent state, leak sensitive information, or trigger harmful external actions. At the same time, research on LLM agent security is expanding quickly but remains fragmented across attack families, defense layers, application domains, and evaluation settings. This paper synthesizes 247 papers through a lifecycle-based, systems-oriented framework that models agent security around the interaction of information flow, delegated authority, and persistent state. We organize the literature around four questions: how LLM agent security should be modeled, which threat surfaces and attack families dominate, what defenses have been proposed and with what tradeoffs, and how security claims are evaluated. We find that prompt injection and tool-mediated control-flow hijacking still dominate the field, while persistent state corruption and multi-agent propagation are becoming central emerging concerns. We further find that current defenses provide useful building blocks but remain weakly compositional, and that existing benchmarks still underrepresent long-horizon, stateful, and deployment-sensitive risks. We argue that secure LLM agents require explicit trust boundaries, principled privilege control, provenance-aware state management, and evaluation practices aligned with realistic operational settings.

</details>


### 135. The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment

- **Authors:** Filippo Tonini, Federico Torrielli, Anton Danholt Lautrup, Peter Schneider-Kamp, Mustafa Mert Çelikok, Lukas Galke Poech
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10747v1](http://arxiv.org/abs/2606.10747v1)
- **PDF:** [https://arxiv.org/pdf/2606.10747v1](https://arxiv.org/pdf/2606.10747v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces the **Arbiter**, a budget‑constrained oversight agent that continuously monitors dialogues among multiple language‑model agents and flags participants that are behaving misalignedly, producing a post‑mortem report on the likely source of the problem.  

**Methodology:** Arbiter incrementally observes each turn of a multi‑agent conversation and, under a fixed “inspection budget”, decides among four actions—wait, interrogate a participant, inspect internal artefacts (e.g., system prompts, reasoning traces), or log suspicious behavior. The authors evaluate Arbiter with two backbone LLMs across five conversation scenarios (risky financial advice, evaluation‑aware, colluding agents, etc.) and five tool configurations of increasing capability.  

**Key findings:** Arbiter can reliably identify misaligned agents **well before conversation end**, and active inspection tools (questioning and internal‑state access) substantially boost both detection accuracy and speed. Weight‑induced misalignment is the hardest to spot, while instruction‑induced misalignment is detected even with passive observation. The logging tool improves recall but reduces precision, highlighting trade‑offs in budget‑aware monitoring. These results suggest that effective oversight of agentic AI systems requires an active, budget‑aware auditor.


<details>
<summary>Abstract</summary>

As AI systems built from multiple language-model agents become more common, they are increasingly used to make decisions together: discussing, negotiating, and acting on shared tasks. While individual agents may appear well-aligned when tested on their own, problems can arise from how they interact with one another. We introduce the Arbiter, an agent designed to monitor multi-agent conversations in real time and identify which participants may be behaving in misaligned ways. The Arbiter operates under a limited "inspection budget", meaning it must decide carefully how to use its resources. As it observes a conversation step by step, it can choose to wait, question a participant, examine internal information such as system prompts or reasoning traces, or log concerning behavior. At the end, it produces a report identifying the likely source of misalignment. We evaluate the Arbiter across five conversation conditions, ranging from risky financial advice model organisms to evaluation-aware and colluding agents, we test five tool configurations of increasing capability and two backbone models. We find that the Arbiter reliably detects misaligned agents well before the end of the conversation, with active inspection tools improving both detection accuracy and speed. Weight-induced misalignment proves hardest to detect, while instruction-induced misalignment is identified reliably even under passive observation. The logging tool exhibits a dual effect, improving recall at the cost of precision. These results suggest that continual, budget-aware monitoring can effectively catch misalignment, and that overseeing multi-agent systems may require treating the auditor as an active participant in the process. The code is available at https://github.com/aisilab/arbiter.

</details>


### 136. MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents

- **Authors:** Yv Zhang, Hao Sun, Hao Fang, Kuofeng Gao, Fan Mo, Bin Chen, Shu-Tao Xia, Yaowei Wang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10742v1](http://arxiv.org/abs/2606.10742v1)
- **PDF:** [https://arxiv.org/pdf/2606.10742v1](https://arxiv.org/pdf/2606.10742v1)
- **Categories:** cs.CR, cs.LG


> The paper introduces **MemVenom**, the first systematic black‑box attack that poisons the external, graph‑structured memories of multimodal web agents. By injecting coordinated text‑image “triggers” (via a trigger‑conditioned retrieval step followed by adversarial post‑retrieval perturbations and OCR‑based content injection), the attacker forces the agent to recall malicious experiences and subvert its original goal without altering the model weights. Empirical evaluation on several web‑agent platforms and vision‑language backbones shows near‑perfect end‑to‑end success (up to 99.15 % on GPT‑5‑family agents) while preserving normal performance, and the attack transfers across different architectures and scales, highlighting a new, persistent vulnerability for agentic AI systems.


<details>
<summary>Abstract</summary>

External memory has become a core component of modern web agents, enabling long-horizon reasoning through the retrieval of past experiences. However, this paradigm introduces a critical vulnerability: malicious content injected into memory can be persistently recalled and repeatedly influence agent behavior. In this work, we identify and systematically study multimodal memory poisoning, an overlooked yet practical attack surface in web-agent systems. We propose MemVenom, a unified black-box attack framework that poisons graph-structured external memory with coordinated text-image evidence. Our method consists of a two-stage design: (1) a trigger-conditioned retrieval attack that ensures high-probability recall of malicious memory, and (2) a post-retrieval attack induction that leverages adversarial perturbations and stealthy OCR injection to override the original user objective. Unlike prior attacks that operate on prompts or text-only memory, our approach enables persistent, reusable, and goal-agnostic attacks without modifying model parameters or re-optimizing malicious tasks. Experiments across multiple web-agent frameworks and vision-language models demonstrate that MemVenom achieves strong end-to-end attack success with minimal impact on benign performance, reaching up to 99.15% on GPT-5-family web agents, while transferring effectively across architectures and model scales.

</details>


### 137. Divide and Cooperate: Role-Decomposed Multi-Agent LLM Training with Cross-Agent Learning Signals

- **Authors:** Jaewan Park, Solbee Cho, Jay-Yoon Lee
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10684v1](http://arxiv.org/abs/2606.10684v1)
- **PDF:** [https://arxiv.org/pdf/2606.10684v1](https://arxiv.org/pdf/2606.10684v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **DAC (Divide and Cooperate)**, a training framework that separates the evidence‑retrieval (“search”) and answer‑generation (“generation”) functions of a language‑model‑based agent into two dedicated agents that share a common backbone but are equipped with role‑specific LoRA adapters. By letting the generator also act as a verifier that can abstain when the retrieved evidence is insufficient, DAC creates explicit cross‑agent signals—abstention rewards for the searcher and hard‑positive evidence augmentation for the generator—that resolve credit‑assignment ambiguities and encourage the searcher to produce higher‑quality evidence. Experiments on standard and multi‑hop QA datasets show that this role‑decomposed, cross‑learning approach attains state‑of‑the‑art results while requiring only parameter‑efficient fine‑tuning, demonstrating the benefits of modular, cooperative agents for agentic AI.


<details>
<summary>Abstract</summary>

Modern language agents which perform multi-step reasoning have shown strong performance in knowledge-intensive question answering. However, existing approaches typically couple evidence acquisition and answer generation within a single policy. This forces a single model to play multiple potentially conflicting roles, inducing a combinatorial explosion in the policy space and hindering efficient exploration. It also introduces a credit assignment problem during training: a search action that retrieves sufficient evidence may still be penalized when generation fails, and vice versa. We propose DAC (Divide and Cooperate), a role-decomposed multi-agent training framework that divides agentic search into two cooperative subtasks, each handled by a dedicated agent trained with role-specific learning signals. The generator serves a dual role as both an answer producer and an evidence sufficiency verifier, abstaining when retrieved evidence is insufficient. This abstention signal is incorporated into the search agent's reward, providing structured cross-agent learning signals that improve credit assignment. Conversely, the searcher exposes the generator to diverse and challenging evidence environments by hard-positive evidence augmentation, improving its robustness. Experiments on general and multi-hop QA benchmarks show that DAC, implemented via parameter-efficient LoRA modules over a shared backbone, achieves strong performance against prior baselines that rely on full fine-tuning of monolithic models.

</details>


### 138. Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory

- **Authors:** Suozhao Ji, Baodong Wu, Zehao Wang, Lei Xia, Qingping Li, Ruisong Wang, Wenbo Ding, Zhenhua Zhu, Boxun Li, Guohao Dai, Yu Wang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10677v1](http://arxiv.org/abs/2606.10677v1)
- **PDF:** [https://arxiv.org/pdf/2606.10677v1](https://arxiv.org/pdf/2606.10677v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** The paper introduces **Infini Memory**, a text‑based, topic‑structured persistent memory architecture for long‑term LLM agents that enables scalable evidence aggregation, fact revision, and continual maintenance.  

**Methodology:** Memory is organized as separate “topic documents” that collect all observations related to a semantic subject, preserving metadata and allowing in‑place fact updates. New observations first reside in a staging buffer and are periodically merged into coherent topic texts. During inference the agent retrieves information via an **iterative retrieval loop** (multiple tool calls) that lets the LLM inspect and integrate evidence step‑by‑step rather than rely on a single static retrieval.  

**Key findings:** On the MemoryAgentBench benchmark, Infini Memory attains a **64.7 % overall score**, surpassing prior memory systems. Ablation studies demonstrate that (1) topic‑document organization improves long‑term fact consistency and (2) the iterative retrieval mechanism enhances the agent’s ability to locate and verify relevant evidence, confirming the utility of maintainable, structured memory for agentic AI.


<details>
<summary>Abstract</summary>

Long-term LLM agents need persistent memory that can track changing facts and provide relevant evidence across sessions. Existing memory systems often store observations as isolated records, summaries, or indexed fragments, which makes evidence aggregation, fact revision, and memory maintenance difficult. We propose Infini Memory, a maintainable text-based persistent memory architecture that treats agent memory as topic-structured documents. Each topic document serves as a semantic unit for collecting related evidence, preserving metadata, and revising facts over time. New observations are first staged in a buffer and periodically consolidated into coherent textual contexts. At inference time, an agentic retrieval procedure lets the LLM read memory through iterative tool calls rather than a single retrieval step. On MemoryAgentBench, Infini Memory achieves 64.7% overall score. Ablations show that topic-structured maintenance and iterative evidence inspection improve complementary aspects of long-term memory use.

</details>


### 139. Decentralized Multi-Agent Systems with Shared Context

- **Authors:** Yuzhen Mao, Azalia Mirhoseini
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10662v1](http://arxiv.org/abs/2606.10662v1)
- **PDF:** [https://arxiv.org/pdf/2606.10662v1](https://arxiv.org/pdf/2606.10662v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **Decentralized Language Models (DeLM)**, a multi‑agent framework that replaces the traditional central orchestrator with a shared, verified context and a distributed task‑queue, allowing agents to asynchronously claim subtasks, read collective progress, perform local reasoning, and write back compact, verified updates. By exploiting this decentralized coordination, DeLM attains significantly better test‑time scaling for software‑engineering tasks (up to 10.5 percentage‑point gains on SWE‑bench Verified and roughly 50 % lower per‑task cost) and improves long‑context multi‑document QA performance (up to 5.7 percentage‑point gains on LongBench‑v2) across several leading model families. The methodology demonstrates that a common, verifiable context can serve as an efficient communication substrate for large‑scale agentic AI without a central bottleneck.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) can scale large language model reasoning at test time by decomposing complex problems into parallel subtasks. However, most existing MAS rely on centralized orchestration, where a main agent assigns work, collects outputs, and merges results. As the number of subtasks grows, this controller becomes a communication and integration bottleneck. We propose Decentralized Language Models (DeLM), a MAS framework that decentralizes coordination through parallel agents, a shared verified context, and a task queue. Agents asynchronously claim subtasks, read accumulated progress, perform local reasoning, and write back compact verified updates. The shared context acts as a common communication substrate, enabling agents to build on one another's verified progress without routing every update through a central controller. Empirically, DeLM improves both software-engineering test-time scaling and long-context reasoning. On SWE-bench Verified, DeLM achieves the best performance across Avg.@1, Pass@2, and Pass@4, with gains of up to 10.5 percentage points over the strongest baseline, while reducing cost per task by roughly 50%. On LongBench-v2 Multi-Doc QA, DeLM achieves the highest average accuracy across four frontier model families, improving over the strongest baseline by up to 5.7 percentage points. The code is available on our project website at https://yuzhenmao.github.io/DeLM/.

</details>


### 140. Multi-agent rendezvous in fluid flows via reinforcement learning

- **Authors:** Bocheng Li, Jingran Qiu, Lihao Zhao
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11274v1](http://arxiv.org/abs/2606.11274v1)
- **PDF:** [https://arxiv.org/pdf/2606.11274v1](https://arxiv.org/pdf/2606.11274v1)
- **Categories:** cs.MA, cs.LG, physics.flu-dyn


> **Main contribution:** The paper demonstrates that multi‑agent reinforcement learning (MARL) can discover physics‑aware rendez‑vous policies that exploit fluid‑kinematic structures, enabling swarms to meet efficiently in vortical flows where naïve pursuit strategies fail.  

**Methodology:** A MARL framework is trained on agents moving in simulated 2‑D vortex fields; the agents receive local flow and relative‑position observations and learn a decentralized policy. The learned policy is analyzed, distilled into a simple heuristic, and tested for transfer across vortex intensities, scales, and swarm sizes. Finite‑time Lyapunov exponent fields are used to theoretically explain how fluid deformation hinders convergence.  

**Key findings:** MARL policies achieve significantly higher rendez‑vous rates than the naïve “move‑toward‑others’’ baseline and generalize to varied flow conditions and group sizes. The learned strategy breaks symmetry to avoid agents being trapped in separate vortices, a mechanism confirmed by Lyapunov analysis that shows optimal meeting points lie in low‑deformation regions. The extracted heuristic retains most of the performance gain, illustrating that learned swarm intelligence can be translated into interpretable, fluid‑aware rules for agentic AI in complex environments.


<details>
<summary>Abstract</summary>

Rendezvous is a critical task for multi-agent systems, requiring agents to coordinate to meet at an unspecified location. However, achieving this in fluid environments presents a challenge, as it remains unclear how agents can exploit underlying fluid kinematics to facilitate convergence. In this study, we adopt a multi-agent reinforcement learning (MARL) approach to develop physics-informed rendezvous strategies in vortical flows. Compared to a naive strategy, where agents navigate toward their counterparts, MARL strategies significantly improve the rendezvous rate. MARL strategies also show transferability across varying vortex intensities, vortex scales, and swarm sizes. By breaking the symmetry of the state-action map, MARL strategy leverages a non-intuitive mechanism that prevents agents from becoming trapped in separate vortices, thereby enhancing rendezvous success. Additionally, a heuristic strategy is extracted from the learned strategy and also outperforms the naive strategy. Furthermore, a theoretical analysis demonstrates that fluid deformation impedes the rendezvous process. Large finite-time Lyapunov exponents identify where fluid effects separate adjacent agents, suggesting that targets should be planned in weak-deformation regions. Our findings reveal the important role that agent-fluid interactions play in multi-agent tasks and highlight the MARL capability to explore swarm intelligence in complex flow environments.

</details>


### 141. Dmsh: A Multi-Agent Reinforcement Learning Framework for All-Quad Mesh Generation

- **Authors:** Anirudh Kalyan, Cosmin Anitescu, Xiaoying Zhuang, Timon Rabczuk, Somdatta Goswami, Sundararajan Natarajan
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10601v1](http://arxiv.org/abs/2606.10601v1)
- **PDF:** [https://arxiv.org/pdf/2606.10601v1](https://arxiv.org/pdf/2606.10601v1)
- **Categories:** math.NA, cs.AI, cs.LG


> **Contribution:** The paper presents **Dmsh**, the first fully automated, reinforcement‑learning‑based framework that jointly learns geometric decomposition and all‑quadrilateral mesh generation, eliminating heuristic tuning and manual intervention.  

**Methodology:** Dmsh casts the meshing pipeline as a Markov Decision Process solved with a parametric Soft Actor‑Critic (SAC) algorithm that uses decoupled critics to handle a hybrid discrete‑continuous action space. Three cooperating agents specialize in (1) topology simplification, (2) geometric regularization, and (3) quad mesh construction; a curriculum‑learning schedule guides them from simple to complex domains, and the recursive decomposition permits parallel, globally conforming mesh synthesis.  

**Key Findings:** On extensive benchmark geometries, Dmsh achieves higher automation, robustness, and mesh quality than state‑of‑the‑art heuristic and learning‑based methods, delivering fully conforming all‑quad meshes without any post‑processing correction—demonstrating the viability of multi‑agent reinforcement learning for complex, high‑fidelity engineering mesh generation.


<details>
<summary>Abstract</summary>

Generating high-quality meshes for arbitrary geometries remains a fundamental bottleneck in computational engineering, often demanding heuristic tuning and semi-manual workflows. In this paper, we introduce Dmsh, a first fully automated reinforcement learning pipeline that unifies geometric decomposition and quadrilateral mesh generation within a single learning-based framework. Dmsh decomposes the problem through three coordinated agents handling topology simplification, geometric regularization, and mesh generation. The meshing process is formulated as a Markov Decision Process and solved using a parametric Soft Actor-Critic architecture with decoupled critics, enabling efficient exploration of a hybrid discrete-continuous action space. A curriculum learning strategy ensures scalability from simple domains to highly complex geometries, suppressing seed variance. By design, the recursive decomposition enables parallel meshing of subregions, yielding globally conforming all-quadrilateral meshes without post hoc correction. Across a wide range of benchmarks, Dmsh consistently outperforms existing methods in automation, robustness, and mesh quality, establishing a new paradigm for learning-based mesh generation.

</details>


### 142. SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement

- **Authors:** Srishti Gautam, Arjun Radhakrishna, Sumit Gulwani
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10546v2](http://arxiv.org/abs/2606.10546v2)
- **PDF:** [https://arxiv.org/pdf/2606.10546v2](https://arxiv.org/pdf/2606.10546v2)
- **Categories:** cs.MA


> The paper introduces **SkillAxe**, an unsupervised, evaluation‑guided loop that lets LLM‑based agents diagnose shortcomings in their own skill documents and iteratively rewrite them. By breaking skill quality into four interpretable metrics (impact, trigger precision, compliance with fault attribution, and solution‑path coverage), SkillAxe generates structured improvement briefs without any ground‑truth labels, test suites, or reward signals, and then prompts the LLM to rewrite the skill accordingly. Experiments on SkillsBench show a 28 % relative boost in task‑pass rates over raw LLM‑generated skills (closing 47–67 % of the human‑skill gap), and a real‑world deployment on SpreadsheetBench raises pass rates from 16 % to 52 % using only 22 self‑refined skills.


<details>
<summary>Abstract</summary>

Skill documents, structured natural-language instructions that guide Large Language Model (LLM) agents, are critical to modern agent frameworks, yet LLMs struggle to write skills that actually work. On SkillsBench, human-authored skills improve pass rates by 16.2 percentage points, while LLM-authored skills provide no measurable gain. We introduce SkillAxe, a fully unsupervised framework that enables LLMs to iteratively diagnose and refine their own skills. SkillAxe decomposes skill quality into four interpretable dimensions (quality impact, trigger precision, instruction compliance with fault attribution, and solution-path coverage), producing structured improvement briefs that require no ground-truth labels, test suites, or environment rewards. On SkillsBench, SkillAxe improves pass rates by 28\% relative over unimproved LLM skills and closes 47--67\% of the gap to human-authored skills. We validate the approach as a continuous improvement engine in the wild on SpreadsheetBench, where a SkillAxe-built skill library learns from past agent trajectories and raises pass rate from 16.0\% to 52.0\% using only 22 skills.

</details>


### 143. Assessing Automated Prompt Injection Attacks in Agentic Environments

- **Authors:** David Hofer, Edoardo Debenedetti, Florian Tramèr
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10525v1](http://arxiv.org/abs/2606.10525v1)
- **PDF:** [https://arxiv.org/pdf/2606.10525v1](https://arxiv.org/pdf/2606.10525v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a large‑scale empirical study of automated prompt‑injection attacks against LLM‑driven agents within the AgentDojo environment, adapting both a white‑box gradient‑based method (GCG) and a black‑box optimization technique (TAP). By testing 80 task pairs across four domains and several models, the authors show that black‑box attacks substantially outperform gradient‑based ones—largely because GCG is unstable under realistic compute limits—and that TAP’s success hinges on the attacker model’s capabilities and safety tuning (stronger or less‑safety‑tuned models generate more effective injections). They further demonstrate that while task‑universal attacks transfer well to new tasks and out‑of‑distribution domains, attacks crafted on smaller open‑source models fail to generalize to frontier models such as GPT‑5, indicating that automated prompt injection is a credible, model‑dependent threat with limited model‑agnostic exploitability.


<details>
<summary>Abstract</summary>

Indirect prompt injection poses a critical threat to LLM agents that interact with untrusted external data, yet automated attack methods--proven effective for jailbreaking--remain underexplored in realistic agentic settings. We present a comprehensive empirical evaluation of automated prompt injection attacks against LLM agents, adapting both white-box (GCG) and black-box (TAP) methods to the agentic setting within the AgentDojo framework. We evaluate across 80 task pairs spanning four domains and multiple models, and find that black-box optimization substantially outperforms gradient-based methods, a gap we attribute to GCG's optimization instability under reasonable compute budgets. We also find that TAP's effectiveness depends on the attacker model, as both general capability and safety tuning affect attack success--stronger models produce more effective injections, while safety-tuned attackers can refuse to generate adversarial prompts. Task-universal attacks transfer effectively to unseen tasks and out-of-distribution domains, but attacks optimized on smaller open-source models do not transfer to frontier models like GPT-5. These findings highlight automated prompt injection as a credible but model-dependent threat, with significant barriers remaining for model-agnostic exploitation.

</details>


### 144. HIPIF: Hierarchical Planning and Information Folding for Long-Horizon LLM Agent Learning

- **Authors:** Juncheng Diao, Zhicong Lu, Peiguang Li, Yongwei Zhou, Changyuan Tian, Qingbin Li, Rongxiang Weng, Jingang Wang, Xunliang Cai
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10507v1](http://arxiv.org/abs/2606.10507v1)
- **PDF:** [https://arxiv.org/pdf/2606.10507v1](https://arxiv.org/pdf/2606.10507v1)
- **Categories:** cs.AI


> The paper introduces **HIPIF (Hierarchical Planning and Information Folding)**, a training framework that equips large‑language‑model agents with explicit sub‑goal generation and a “folding” mechanism that compresses completed sub‑goal histories, thereby mitigating long‑context interference that typically hampers multi‑turn, long‑horizon tasks.  HIPIF learns end‑to‑end through a combination of hierarchical reflection and subgoal‑oriented process rewards—without auxiliary models or expert demonstrations—to stabilize sub‑goal planning, transition, and execution.  Empirical results on three public agentic benchmarks show that HIPIF substantially improves success rates and overall task performance compared with prior credit‑assignment and hierarchical RL baselines, confirming its effectiveness for long‑horizon agentic AI.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated strong capabilities as autonomous agents across a wide range of tasks, their performance often degrades in multi-turn long-horizon agentic tasks. Existing methods have made progress through fine-grained credit assignment to alleviate long-horizon sparse rewards and hierarchical reinforcement learning to decompose tasks and reduce long-term dependency. However, these methods still do not directly address long-context interference, in which continuously growing histories weaken the agent's ability to track the global task state and impair subsequent reasoning and decision-making. Inspired by the way humans handle complex tasks through subgoal decomposition and completed progress summarization, we propose Hierarchical Planning and Information Folding (HIPIF) for long-horizon LLM agent learning. HIPIF trains the agent end-to-end to organize long-horizon execution around explicit subgoals while folding completed subgoal histories to reduce long-context interference. Furthermore, to stabilize subgoal-based planning and execution, HIPIF combines hierarchical reflection and subgoal-oriented process rewards to guide subgoal generation, transition, and execution, without relying on costly auxiliary models or task-specific expert trajectories. Extensive experiments on three publicly available agentic benchmarks demonstrate the validity of our method.

</details>


### 145. Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation

- **Authors:** Jakub Masłowski, Jarosław A. Chudziak
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10475v1](http://arxiv.org/abs/2606.10475v1)
- **PDF:** [https://arxiv.org/pdf/2606.10475v1](https://arxiv.org/pdf/2606.10475v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces **Knowledge‑Grounded Counterfactual Reasoning (KG‑CFR)**, a dual‑stage architecture that isolates a private, retrieval‑augmented planning buffer from a public execution layer to keep agents’ “thought” separate from their “speech.” By deploying KG‑CFR in a novel 1‑v‑1‑v‑1 dynamic resource‑allocation task with stochastic shocks, the authors show that the decoupled design prevents post‑perturbation degradation in over 95 % of runs, raising average argument quality from 0.694 to 0.822 and markedly cutting semantic looping. Ablation studies further reveal that both doctrinal grounding and the planning‑execution split are essential for maintaining discourse stability, establishing architectural decoupling as a key lever for resilient multi‑agent argumentation.


<details>
<summary>Abstract</summary>

Multi-agent debate frameworks have been shown to improve large language model performance in convergent tasks, but they are currently optimized in a way that heavily favors final output accuracy rather than stability of the process. During long-horizon exchanges reactive systems under sustained perturbations often experience logic degradation, argument repetition, and role drift. To structurally prevent the identity loss and maintain the process fidelity, we introduce Knowledge-Grounded Counterfactual Reasoning (KG-CFR), a dual-stage architecture that enforces a strict separation of concerns between a private, retrieval-augmented planning buffer, and a public execution layer. We assess this system in Dynamic Resource Allocation under Uncertainty (DRAU), a dedicated 1v1v1 environment, introducing diversity as distinct from standard debate settings. Over 270 completely factorial crisis simulation trajectories with stochastic environmental shocks, KG-CFR prevents judge-detected critical post-shock degradation (defined as a quality shift, $Δ\le -0.20$) in more than 95% of perturbed runs, increasing the overall argument quality from 0.694 to 0.822. Our primary contribution is the demonstration of architectural decoupling being an important factor of systemic resilience enhancement under sustained pressure without quality loss. Furthermore, we introduce custom vector metrics for discourse divergence and plan-execution alignment that provide strong, directionally consistent evidence of operational stability. Our ablation experiments suggest that the proper doctrinal grounding can be an equally important factor for argument quality, as the prospective planning. KG-CFR, according to our initial metric evaluations, reduces semantic looping, by preserving the agent's consistency with the original plan.

</details>


### 146. LakeQA: An Exploratory QA Benchmark over a Million-Scale Data Lake

- **Authors:** Haonan Wang, Jiaxiang Liu, Yurong Liu, Austin Senna Wijaya, Tianle Zhou, Eden Wu, Yijia Chen, Wanting You, Reya Vir, Daniela Pinto, Grace Fan, Yusen Zhang, Juliana Freire, Eugene Wu
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10460v1](http://arxiv.org/abs/2606.10460v1)
- **PDF:** [https://arxiv.org/pdf/2606.10460v1](https://arxiv.org/pdf/2606.10460v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **LakeQA**, a new benchmark that forces large‑language‑model agents to **search through a 9.5 TB heterogeneous data lake (Wikipedia + open‑source government datasets) and then perform multi‑hop, cross‑source reasoning** to answer questions that lack pre‑provided evidence. The authors construct the benchmark by having each of its ~​k‑scale QA pairs verified by at least one Ph.D.–level expert, and they evaluate seven state‑of‑the‑art LLMs (including GPT‑5.2) using a zero‑shot prompting setup. Results show that even the strongest model attains only **≈18 % exact‑match accuracy**, confirming that current LLM agents are far from capable of reliable search‑and‑reasoning over massive data lakes—highlighting the need for improved retrieval‑augmented and agentic architectures.


<details>
<summary>Abstract</summary>

Recent large language models (LLMs) have shown rapid progress in reading-based question answering (QA), where evidence is explicitly provided or can be trivially retrieved. In contrast, real-world questions are often not paired with accurate evidence documents. The useful evidence resides in massive data lakes, making search a prerequisite for answering. However, there is a lack of comprehensive benchmarks that require both searching and reasoning over large data lakes. To this end, we introduce LakeQA, a comprehensive benchmark for search-centric question answering over data lakes that jointly emphasizes searching and reasoning capabilities. LakeQA is built on a heterogeneous collection of approximately 9.5 TB of text resources from Wikipedia and open-source government data, spanning structured and unstructured data. To ensure task quality, each sample is annotated by at least one Ph.D.-level expert. Each task requires long-horizon multi-hop reasoning with implicit intermediate steps: agents need to discover the correct documents and then compose evidence across sources to produce the answer. Experimental results on seven frontier LLMs demonstrate that LakeQA is challenging. For instance, GPT-5.2 achieves only an exact-match score of 18.37% on LakeQA. Overall, LakeQA provides a realistic testbed for developing LLM agents that can both find and analyze data in modern data lakes.

</details>


### 147. WebChallenger: A Reliable and Efficient Generalist Web Agent

- **Authors:** Jayoo Hwang, Xiaowen Zhang, Vedant Padwal
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10423v1](http://arxiv.org/abs/2606.10423v1)
- **PDF:** [https://arxiv.org/pdf/2606.10423v1](https://arxiv.org/pdf/2606.10423v1)
- **Categories:** cs.CL


> The paper introduces **WebChallenger**, a general‑purpose web‑navigation agent that attains state‑of‑the‑art performance without proprietary models by redesigning the agent architecture rather than scaling the language model. It builds a deterministic, hierarchical page representation called **PageMem** from the DOM and layers three cognitively inspired mechanisms on it: (1) a divide‑and‑conquer observation pipeline that focuses attention on summary‑level sections and pulls details only from task‑relevant regions, (2) a lightweight exploration/memory module that traverses each site once to construct a reusable map of page structure and element behaviors, and (3) compound action workflows that collapse common multi‑step interactions into single actions. Evaluated with off‑the‑shelf open‑weight LLMs, WebChallenger reaches 56.3 % on WebArena, 48.7 % on VisualWebArena, 51.0 % on Online‑Mind2Web, and 70.9 % on WorkArena—comparable to leading proprietary systems while using far less inference cost.


<details>
<summary>Abstract</summary>

Autonomous web navigation remains challenging for LLM agents, and the strongest generalist systems rely on proprietary reasoning models whose inference cost is prohibitive for the repetitive tasks where such agents would be most useful. We argue this gap stems not from insufficient model capability but from agent architectures that fail to replicate three human cognitive advantages: selective attention to relevant page regions, persistent memory of website structure, and procedural fluency with common interaction patterns. We introduce WebChallenger, a web agent framework that addresses each gap through architecture design rather than model scale, built around PageMem: a structured page representation deterministically constructed from the DOM that exposes each page as a hierarchy of semantic sections with short summaries. On this shared substrate we build three mechanisms that mirror the three cognitive advantages: a divide-and-conquer observation pipeline that lets the agent skim section summaries and extract details only from task-relevant regions; a lightweight exploration and memory system that traverses each website once to build a reusable map of pages and element behaviors; and compound action workflows that collapse common multi-step interactions into single agent actions, handling partial state changes automatically. Because all three operate over PageMem, the framework generalizes across websites without site-specific adapters. Using off-the-shelf open-weight models without fine-tuning, our system achieves 56.3% on WebArena, 48.7% on VisualWebArena, 51.0% on Online-Mind2Web, and 70.9% on WorkArena, approaching frontier proprietary systems at a fraction of the cost. Our code is released at https://github.com/jayoohwang1/webchallenger

</details>


### 148. Harnessing the Collective Intelligence of AI Agents in the Wild for New Discoveries

- **Authors:** Federico Bianchi, Yongchan Kwon, Aneesh Pappu, James Zou
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10402v1](http://arxiv.org/abs/2606.10402v1)
- **PDF:** [https://arxiv.org/pdf/2606.10402v1](https://arxiv.org/pdf/2606.10402v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces **EinsteinArena**, an “agent‑native” platform that lets language‑model‑based AI agents collaboratively tackle open scientific problems through a shared verifier, leaderboard, and discussion forum. By deploying numerous agents on a suite of well‑defined mathematical challenges, the authors show that iterative, public exchanges among agents (e.g., posting partial solutions, refining verifiers, borrowing insights) lead to emergent collective problem‑solving; as of May 2026 the system generated 12 new state‑of‑the‑art results, including raising the kissing‑number lower bound in 11 dimensions from 593 to 604. The work demonstrates that decentralized, open interaction among autonomous agents can produce substantive, reproducible scientific discoveries, establishing a new paradigm for agentic AI‑driven research.


<details>
<summary>Abstract</summary>

Scientific discovery is often a collective process: researchers share partial results, inspect failed attempts, and build on each other's ideas over long time horizons. Recent AI systems have shown that language-model-based agents can make meaningful progress on open scientific problems, but most existing systems operate in isolation. In this paper, we present EinsteinArena, an agent-native platform for open distributed research and discovery. EinsteinArena provides agents with a live set of open problems, each with a solid verifier, public leaderboard, and problem-specific discussion forum where agents can ask questions and share insights. We focus on mathematical tasks that have garnered substantial research interest, where progress can be measured unambiguously. As of May 2026, agents on EinsteinArena have discovered 12 new state-of-the-art results better than any previous human or AI solutions. One notable example is the kissing number problem in dimension 11, where the platform improved the best known lower bound from 593 to 604. This advance did not come from a single agent or isolated run. Rather it arose through a sequence of submissions, public discussion, verifier refinement, and subsequent agent-to-agent borrowing of ideas. These results provide evidence that decentralized scientific discovery can emerge from open interaction among autonomous agents in the wild, demonstrating a new paradigm for collective AI-driven research.

</details>


### 149. Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evolution in Adversarial Games

- **Authors:** Haoran Li, Zengle Ge, Ziyang Zhang, Xiaomin Yuan, Yui Lo, Qianhui Liu, Bocheng An, Dongke Rong, Jiaqun Liu, Annan Li, Jianmin Wu, Dawei Yin, Dou Shen
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10389v1](http://arxiv.org/abs/2606.10389v1)
- **PDF:** [https://arxiv.org/pdf/2606.10389v1](https://arxiv.org/pdf/2606.10389v1)
- **Categories:** cs.AI


> The paper introduces **FAMOU**, a co‑evolutionary framework that extends LLM‑driven code evolution to adversarial multi‑agent games by (1) continuously adding newly discovered champion agents to the opponent pool, (2) using hierarchical deep evaluation to obtain statistically robust fitness estimates, and (3) applying “weakness pressure” to up‑weight the toughest opponents during training. Experiments on the 3v3 maritime capture‑the‑flag (MCTF 2026) task show that FAMOU consistently beats prior code‑evolution baselines (OpenEvolve, ShinkaEvolve) across two backbone LLMs, achieving the highest combined score (0.526) and a 61.7 % win rate against unseen opponents, with ablations confirming each mechanism’s contribution. The evolved agents discover novel tactical structures (e.g., look‑ahead search, adaptive interception) and attain top‑ranked performance in both simulation and hardware rounds of the AAMAS 2026 MCTF competition, demonstrating that co‑evolution can drive substantive algorithmic innovation in agentic AI.


<details>
<summary>Abstract</summary>

Recent advances in LLM-driven code evolution have enabled automated discovery by iteratively generating and improving programs. However, applying these methods to adversarial multi-agent games introduces a fundamental challenge: the evaluation landscape shifts as strategies improve, causing fixed evaluators to become unreliable and evolution to stagnate. We propose three mechanisms to address this challenge: evaluator co-evolution, which incorporates discovered champions into the opponent pool; hierarchical deep evaluation, which replaces noisy few-game scores with statistically reliable assessments; and weakness pressure, which dynamically up-weights the most difficult opponents to break through plateaus. We implement these mechanisms within FAMOU, a framework built upon the same foundation-model code-evolution paradigm as OpenEvolve and ShinkaEvolve. On the MCTF 2026 3v3 maritime capture-the-flag task, FAMOU consistently outperforms both baselines under two backbone LLMs, achieving the highest combined score (0.526) and the best generalization to unseen opponents (61.7% win rate), while ablations confirm that each mechanism contributes to performance. Notably, the LLM mutation process generates tactical structures entirely absent from the seed strategies -- including lookahead search and adaptive interception -- demonstrating that code-level evolution can produce nontrivial algorithmic innovations in adversarial settings. The FAMOU-evolved strategy further achieved 1st place in the hardware round-robin and 3rd in simulation at the AAMAS 2026 MCTF Competition, validating its real-world transferability. The optimized implementation and corresponding evaluation codes developed through our evolutionary process are available at: https://github.com/1xiangliu1/FAMOU-CoEvo

</details>


### 150. ReflectiChain: Epistemic Grounding in LLM-Driven World Models for Supply Chain Resilience

- **Authors:** Jia Luo
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10359v1](http://arxiv.org/abs/2606.10359v1)
- **PDF:** [https://arxiv.org/pdf/2606.10359v1](https://arxiv.org/pdf/2606.10359v1)
- **Categories:** cs.AI


> The paper introduces **ReflectiChain**, a novel framework that gives LLM‑driven supply‑chain agents a physically grounded world model and a principled way to handle uncertainty.  It builds a **generative supply‑chain world model (SC‑WM)** that embeds heterogeneous network data in a six‑dimensional graph‑latent space respecting conservation laws, and couples this with a **double‑loop learning** scheme that isolates epistemic uncertainty (via a KL‑bounded trust‑region policy update) from aleatoric uncertainty (through stochastic latent rollouts).  In a 10‑node semiconductor benchmark (Semi‑Sim), ReflectiChain raises the Rationale Consistency Score by 33 % (p < 0.0001, d = 2.78), keeps 82.3 % operability under adversarial shocks, and even exhibits anti‑fragile gains (+40.2 %) under moderate stress, demonstrating that separating uncertainty, detecting knowledge boundaries, and using empirical‑Bayesian policy updates can substantially improve the resilience of LLM‑based agents in complex, physically constrained domains.


<details>
<summary>Abstract</summary>

AI agents in supply chains face a fundamental epistemic gap: large language models (LLMs) interpret policies but lack physical grounding, while reinforcement learning (RL) optimizes flows but is semantically blind to unstructured constraints. We introduce REFLECTICHAIN, bridging this gap through a Generative Supply Chain World Model (SC-WM) - encoding heterogeneous supply networks into a 6-dim graph-latent space with physical conservation - and Double-Loop Learning that separates epistemic uncertainty (KL-trust-region-bounded policy adaptation) from aleatoric uncertainty (stochastic latent rollouts). On Semi-Sim, a 10-node semiconductor benchmark with SIR risk propagation, 6 perturbation types, and 10 policy constraint templates, REFLECTICHAIN improves Rationale Consistency Score by 33.0% (p < 0.0001, d = 2.78), maintains 82.3% operability under adversarial shocks, and exhibits anti-fragile behavior (+40.2% gain under moderate pressure). We identify three operational epistemic mechanisms - uncertainty separation, knowledge-boundary detection, and empirical Bayesian policy updating - and discuss five limitation categories.

</details>


### 151. Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs

- **Authors:** Saeid Jamshidi, Amin Nikanjam, Arghavan Moradi Dakhel, Kawser Wazed Nafi, Foutse Khomh
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10322v2](http://arxiv.org/abs/2606.10322v2)
- **PDF:** [https://arxiv.org/pdf/2606.10322v2](https://arxiv.org/pdf/2606.10322v2)
- **Categories:** cs.CR, cs.MA


> **Contribution:** The paper proposes the Game‑Theoretic Secure Model Context Protocol (GT‑MCP), a controller‑driven multi‑agent architecture that actively enforces contextual stability in long‑horizon LLM interactions, defending against prompt‑injection and context‑poisoning attacks.

**Methodology:** GT‑MCP orchestrates three heterogeneous LLM agents and a central controller that evaluates each turn’s output with a trust function combining (1) causal consistency with a validated context graph, (2) semantic agreement among the agents, and (3) detection of distributional drift. When the trust score falls below a threshold, a rollback‑based self‑healing routine restores the last trusted context, preventing adversarial fragments from propagating.

**Key Findings:** In 500‑turn adversarial simulations, contextual drift remained bounded in 99.6 % of turns, with recovery needed in only 0.4 % and no successful injection at the controller level. Utility loss was modest (median = ‑0.19, 5th‑percentile = ‑0.72, 95th‑percentile = 0.30), severe degradation (<‑1) occurred in 0.4 % of turns, and the system sustained >98 % stable win rates with a predictable latency of ≈1.6 ms per token. This demonstrates that a game‑theoretic, multi‑agent control loop can robustly maintain contextual integrity for agentic AI systems.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) in multi-turn interactions maintain evolving context rather than generating isolated responses, making them vulnerable to prompt-injection and context-poisoning attacks in which locally plausible adversarial fragments gradually distort reasoning trajectories. Existing defenses mainly filter individual outputs and often ignore context evolution across turns, leaving long-horizon reasoning exposed. Although the Model Context Protocol (MCP) standardizes context exchange and tool invocation, it functions as a passive routing layer and does not enforce contextual stability. To address these limitations, we introduce the Game-Theoretic Secure Model Context Protocol (GT-MCP), a controller-driven multi-agent method that treats context management as a closed-loop dynamical process. GT-MCP coordinates three heterogeneous LLM agents and selects outputs through a trust function that jointly evaluates causal consistency against a validated context graph, semantic agreement among agents, and distributional drift over time. When instability is detected, a rollback-based self-healing mechanism restores the validated context and prevents unsupported fragments from propagating. Empirical evaluation over 500 interaction turns under an adaptive adversarial threat model shows that contextual drift remains bounded in 99.6% of turns, with recovery required in only 0.4%. Per-turn utility remains tightly concentrated, with median = -0.19, P05 = -0.72, and P95 = 0.30; severe degradation below -1 occurs in only 0.4% of cases, and no injection attempt succeeds at the controller level. Selected outputs maintain stable win rates above 98%, and computational overhead remains predictable, with latency per token = 1.63e-3 s.

</details>


### 152. TabClaw: An Interactive and Self-Evolving Agent for Spreadsheet Manipulation and Table Reasoning

- **Authors:** Mingyue Cheng, Shuo Yu, Daoyu Wang, Qingchuan Li, Xiaoyu Tao, Qingyang Mao, Yitong Zhou, Qi Liu
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10316v1](http://arxiv.org/abs/2606.10316v1)
- **PDF:** [https://arxiv.org/pdf/2606.10316v1](https://arxiv.org/pdf/2606.10316v1)
- **Categories:** cs.CL


> TabClaw introduces an open‑source, interactive LLM‑based agent that turns spreadsheet or CSV data into transparent, inspectable analytical workflows. The system combines a ReAct‑style reasoning loop with a modular architecture that (1) clarifies user intent, (2) presents an editable execution plan, (3) runs specialist sub‑agents in parallel for multi‑table operations, and (4) records completed pipelines to build a persistent, self‑evolving skill memory that can be refined from user feedback. Experiments on standard spreadsheet manipulation and table‑reasoning benchmarks show that TabClaw markedly boosts executable task‑completion rates and reasoning accuracy while maintaining user‑level visibility and personalizing to recurring analysis patterns.


<details>
<summary>Abstract</summary>

Spreadsheets and tables are widely used representations for structured data analysis, but effective analysis still requires substantial manual effort and domain expertise. Recent large language model (LLM) agents can automate parts of this process, but they often provide limited transparency into intermediate decisions, rely on implicit assumptions, struggle with multi-table comparison, and repeat similar workflows without adapting to a user's preferences. This paper presents TabClaw, an open-source interactive AI agent for spreadsheet manipulation and table reasoning. Users upload CSV or Excel files and issue natural-language requests; TabClaw clarifies ambiguous intent, exposes an editable execution plan, streams a ReAct-style tool-using analysis loop, dispatches specialist agents for parallel multi-table reasoning, and synthesizes findings with explicit consensus and uncertainty markers. Beyond one-off analysis, TabClaw records completed workflows, extracts persistent user memory, distills reusable skills from repeated tool-use patterns, supports package-style skill import, and upgrades skills from negative feedback. Experiments on spreadsheet manipulation and table reasoning benchmarks show that TabClaw improves executable task completion and reasoning performance while preserving an inspectable user workflow. This paper shows how TabClaw turns spreadsheets and tables into inspectable analytical workflows while gradually personalizing itself to recurring data-analysis tasks. Our code is available.

</details>


### 153. Mobility Anomaly Generation using LLM-Driven Behavior with Kinematic Constraints

- **Authors:** Yueyang Liu, Joon-Seok Kim, Andreas Züfle
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10314v1](http://arxiv.org/abs/2606.10314v1)
- **PDF:** [https://arxiv.org/pdf/2606.10314v1](https://arxiv.org/pdf/2606.10314v1)
- **Categories:** cs.AI


> **Main contribution:** The paper presents an end‑to‑end generative framework that creates large, realistic human‑trajectory anomaly datasets by combining baseline simulated mobility with LLM‑driven behavioral perturbations while honoring kinematic and map constraints.  

**Methodology:** Autonomous LLM agents edit the sequence of stay‑points in simulated trajectories to inject semantically meaningful anomalies (e.g., out‑of‑distribution check‑ins, missed routine visits). The modified stay‑points are then re‑routed using map‑constrained shortest‑path reconstruction to preserve physical feasibility, and a context‑aware spatial‑noise model adds location‑dependent GPS error to mimic real sensor degradations.  

**Key findings:** The generated trajectories exhibit high visual and statistical similarity to real mobility data, maintain strict kinematic validity, and provide ground‑truth anomaly labels that enable downstream tasks (anomaly detection, trajectory forecasting) to be benchmarked more reliably, thereby addressing a critical data scarcity bottleneck in agentic AI research on human mobility.


<details>
<summary>Abstract</summary>

Although the study of human trajectory anomalies is critical for advancing spatial data mining, empirical research remains severely hindered by a pervasive lack of ground-truth datasets. Despite the availability of several real-world and simulated human trajectory collections, these datasets exclusively capture normal mobility patterns and lack annotated anomalies. This specific scarcity is fundamentally driven by the inherent statistical rarity of anomalous events, precluding the feasibility of conventional observational methods. Compounding this challenge, the systematic acquisition of large-scale mobility data is strictly bottlenecked by prohibitive costs and stringent privacy regulations. To overcome these fundamental limitations and establish a reliable human trajectory anomalies dataset with annotated ground truth, we introduce a novel, end-to-end generative framework designed to synthesize realistic trajectory anomalies at scale. Our architecture bridges the gap between purely synthetic mobility data and complex real-world physical constraints by operating directly on baseline simulated trajectories. We employ Large Language Model (LLM) agents to systematically inject semantically meaningful behavioral anomalies such as irregular out-of-distribution check-ins and skipped routine visits. To ensure rigorous spatial validity, the system leverages map-constrained routing reconstruction to recalculate the physical transitions between these LLM agent-modified staypoints. Moreover, to narrow the simulation-to-reality gap, we augment the resulting trajectories with a context-aware spatial noise model, parameterized by environmental and location-specific variables, to accurately emulate heterogeneous GPS sensor degradation.

</details>


### 154. Early-Token Confidence Predicts Reasoning Quality in Multi-Agent LLM Debate

- **Authors:** Ali Keramati, Justin Cheok, Jacob Horne, Mark Warschauer
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10307v1](http://arxiv.org/abs/2606.10307v1)
- **PDF:** [https://arxiv.org/pdf/2606.10307v1](https://arxiv.org/pdf/2606.10307v1)
- **Categories:** cs.CL


> The paper shows that the token‑level log‑probabilities (intrinsic confidence) of an LLM’s **early** output tokens can reliably forecast the quality of its reasoning in a multi‑agent debate setting. By running a debate‑based essay‑scoring experiment on two ASAP datasets and using an LLM‑as‑judge to provide rubric scores, the authors demonstrate that confidence measured within the first few generated tokens outperforms any full‑sequence statistic and correlates especially well when the agent is offering supportive arguments (versus adversarial critique). This finding offers a lightweight, domain‑agnostic metric for estimating reasoning reliability in agentic AI systems.


<details>
<summary>Abstract</summary>

Evaluating reasoning quality in multi-agent LLM systems is challenging, especially for open-ended tasks without reference answers. We investigate whether intrinsic confidence signals, token-level log-probabilities from decoding, can predict reasoning quality as assessed by LLM-as-judge evaluation. Using a debate-based essay scoring framework, we compare confidence proxies against rubric-based judge scores across two ASAP essay sets. We find that early-token confidence, particularly within the first few generated tokens, is consistently the strongest predictor of reasoning quality, outperforming full-sequence statistics. Analysis of log-probability trajectories shows that the opening phase of generation is the most heterogeneous and therefore most informative. We also observe a systematic asymmetry between agent roles, with stronger alignment between confidence and quality for supportive reasoning than for adversarial critique. These results suggest that early decoding dynamics provide a lightweight and effective signal for estimating reasoning reliability in multi-agent LLM systems.

</details>


### 155. MIRAGE: A Polarity-Flipping Encoding Subspace in LLM Agents

- **Authors:** Pratibha Revankar, Kargi Chauhan, Jihye Kim, Sadiba Nusrat Nur, Vincent Siu, Chenguang Wang
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10304v1](http://arxiv.org/abs/2606.10304v1)
- **PDF:** [https://arxiv.org/pdf/2606.10304v1](https://arxiv.org/pdf/2606.10304v1)
- **Categories:** cs.CL


> The paper identifies a shared, low‑dimensional “encoding subspace” in the residual streams of diverse LLMs that becomes activated whenever the model internally constructs covert encodings (Base64, ROT13, acrostics, synonym chains, etc.). By training a logistic‑regression probe on eight encoding families, the authors can read out this subspace (AUC ≈ 0.98–1.0) and also detect a polarity flip at the planning token that predicts whether the encoding will be generated inline or off‑loaded to a tool, enabling a real‑time monitor (MIRAGE) that achieves AUC ≈ 0.92 on 126 agentic exfiltration tasks—far surpassing output‑only detectors. The findings show that covert data‑exfiltration leaves a geometric trace in the model’s internal activations, and that probing this trace can reliably flag agentic behaviors across multiple model families, albeit with false‑positive rates that vary dramatically with model architecture.


<details>
<summary>Abstract</summary>

When LLM agents are coerced into covertly encoding sensitive data (Base64, ROT13, acrostic, synonym chains, and beyond), the resulting outputs evade output-side detection but the underlying computation does not. Across nine encoding families and eight models from five architecture families, that computation is supported by a shared low-dimensional encoding subspace in the residual stream. A logistic-regression probe trained on eight encoding families recovers the held-out ninth at AUC 0.975-1.000, reading the computation rather than surface features. The same direction exhibits a second mechanistic signature at the planning token, flipping polarity to activate positively when the model will simulate the encoding inline and negatively when it will outsource it to a tool call, distinguishing two execution strategies before the encoded text exists. We build MIRAGE (Model-Internal Readout of Agentic Generation Exfiltration), a two-channel real-time monitor exploiting both signals. On 126 agentic exfiltration scenarios, it reaches AUC = 0.918, substantially outperforming output-only detection (AUC = 0.518). Monitor performance is fundamentally a property of the host model's geometry: benign-encoding false-positive rate ranges from 0% on Qwen-7B to 100% on Phi-3.5, revealing that the probe faithfully reads whether a model's geometry separates covert from overt encoding. Across all tested adversarial budgets, every attack suppressing the subspace also destroyed encoding fidelity, reported as an empirical regularity on the evaluated budgets, not a structural impossibility claim.

</details>


### 156. The Confident Liar: Diagnosing Multi-Agent Debate with Log-Probabilities and LLM-as-Judge

- **Authors:** Ali Keramati, Justin Cheok, Jacob Horne, Mark Warschauer
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10296v1](http://arxiv.org/abs/2606.10296v1)
- **PDF:** [https://arxiv.org/pdf/2606.10296v1](https://arxiv.org/pdf/2606.10296v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces a diagnostic framework for multi‑agent debate that links three internal signals—token‑level log‑probabilities, LLM‑as‑judge rubric scores, and final answer correctness—to assess the quality of intermediate reasoning. By pairing a two‑agent system (Constructor and Auditor) with an LLM‑based judge that rates instruction adherence, justification, and evidence grounding, the authors show that log‑probability‑derived confidence tracks the judged reasoning quality, especially for the Constructor (confidence‑reasoning correlation ≈2× higher than for the Auditor) and can reliably flag critical failures (AUROC 0.804 vs. 0.634). Across rubric‑scoring, math, and factual domains, the study demonstrates that confidence signals are valuable predictors of both judged reasoning quality and task success, highlighting a previously unexplored axis for improving agentic AI debate systems.


<details>
<summary>Abstract</summary>

Multi-agent debate systems are typically evaluated only on whether the final answer is correct, overlooking the quality of the intermediate reasoning that debate is designed to produce. This paper studies the relationship between three signals in multi-agent debate: token-level log-probability distributions over reasoning tokens, LLM-as-judge rubric scores assigned to those tokens, and final task accuracy. We examine whether internal confidence signals predict externally evaluated reasoning quality, and whether either signal aligns with task correctness, across three domains: rubric-based scoring, mathematical reasoning, and factual question answering. Our framework pairs a two-agent debate architecture -- a Constructor and an Auditor -- with an LLM-as-judge that scores each agent's reasoning along instruction following, justification quality, and evidence grounding, together with a critical-failure flag. Experiments in the rubric-scoring domain reveal a consistent four-phase confidence trajectory and a substantial role asymmetry: confidence aligns with judged reasoning quality roughly twice as strongly for the Constructor as for the Auditor, and confidence-based detection of critical reasoning failures is markedly more reliable for the Constructor (AUROC 0.804) than for the Auditor (0.634). These findings motivate the broader cross-domain investigation proposed in this paper.

</details>


### 157. Sim2Schedule: A Simulator-Guided LLM Framework for Autonomous Open-Pit Mine Scheduling

- **Authors:** Mustavi Ibne Masum, Thiago Eustaquio Alves de Oliveira, Mahzabeen Emu
- **Published:** 2026-06-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10286v1](http://arxiv.org/abs/2606.10286v1)
- **PDF:** [https://arxiv.org/pdf/2606.10286v1](https://arxiv.org/pdf/2606.10286v1)
- **Categories:** cs.AI


> The paper presents **Sim2Schedule**, a novel framework that treats a large language model (LLM) as an autonomous scheduling agent for open‑pit mining, with every action constrained by a custom‑built simulator that encodes geotechnical precedence, extraction‑processing coupling, and dynamic capacity limits. By operating in a zero‑shot, closed‑environment mode—without fine‑tuning, cloud calls, or retraining—the LLM iteratively generates interpretable extraction and processing schedules that are directly validated by the simulator. Empirical evaluation on multiple mine instances shows that the simulator‑guided LLM recovers **94 %–99 % of the net‑present‑value (NPV) achieved by a newly formulated MILP optimum**, while its runtime grows only linearly with problem size, demonstrating that constrained LLM agents can serve as scalable, real‑time alternatives to traditional combinatorial optimizers in complex, safety‑critical industrial domains.


<details>
<summary>Abstract</summary>

Open-pit mine scheduling is a critical process for maximizing economic return under complex geotechnical and operational constraints. While Mixed-Integer Linear Programming (MILP) provides mathematically optimal baselines, its exponential computational complexity and inability to adapt in real time limit its practical deployment in dynamic industrial environments. This work introduces a simulator-driven Large Language Model (LLM) scheduling framework in which the LLM acts as an autonomous decision-making agent, guided at each step by a custom simulator that encodes geotechnical precedence, extraction-processing coupling, and dynamic capacity constraints directly into the action generation mechanism. Operating entirely zero-shot within a closed, data-secure environment, the framework produces complete, interpretable extraction and processing schedules without cloud-based inference, domain-specific fine-tuning, or retraining. To provide a trustworthy performance benchmark, a novel MILP formulation is developed that incorporates realistic operational and geotechnical constraints. Evaluated across mining instances of varying scale and time periods, the LLM-based framework recovers between 94\% and 99\% of the MILP optimal NPV while scaling linearly in computation time. These results position simulator-constrained LLM agents as a practical and scalable alternative to classical optimization for long-horizon industrial scheduling under complex operational constraints.

</details>


### 158. My Chemical Harness: Evolutionary Molecular Design over Synthetic Pathways with Large Language Model Agents

- **Authors:** César Ojeda, Darius A. Faroughy, Maryam Karimi, Payam Zarrintaj, Mir Mehdi Seyedebrahimi, Martín Carballo-Pacheco
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11256v1](http://arxiv.org/abs/2606.11256v1)
- **PDF:** [https://arxiv.org/pdf/2606.11256v1](https://arxiv.org/pdf/2606.11256v1)
- **Categories:** physics.chem-ph, cs.LG, cs.NE


> The paper introduces **My Chemical Harness**, an evolutionary molecular‑design framework that treats **entire synthetic pathways—as opposed to individual molecules—as the evolutionary population**. A deterministic chemistry engine builds and validates routes from purchasable precursors using reaction templates, while a **large language model (LLM) acts only as a high‑level strategy controller**, selecting preferences for route length, reaction families, move types, and exploration pressure; the LLM never generates chemical structures directly, thereby avoiding hallucinated reactions. On a soluble epoxide hydrolase (sEH) proxy benchmark, the LLM‑guided evolutionary search outperforms single‑pass LLM generation and purely deterministic baselines, achieving state‑of‑the‑art scores on the sEH activity proxy, synthetic accessibility, and AiZynthFinder route‑success metrics, demonstrating that constrained, non‑generative LLM agents can effectively steer route‑native molecular discovery without additional training or fine‑tuning.


<details>
<summary>Abstract</summary>

Designing molecules with target properties is most useful when candidate structures are accompanied by feasible synthetic routes. We introduce My Chemical Harness, a route-native evolutionary framework for goal-directed molecular design in which the search population consists of executable synthetic pathways rather than isolated molecular graphs. Each route is built from purchasable building blocks and reaction templates, executed by deterministic chemistry tools, and scored through task-specific molecular oracles. Large language models (LLMs) are used only as strategy controllers that select high-level preferences over route length, move type, reaction families, motifs, and exploration pressure, while local code performs route construction, validation, deduplication, scoring, selection, and memory updates. This separation lets the LLM guide exploration without allowing it to introduce hallucinated products or unsupported reaction steps. On a soluble epoxide hydrolase proxy task, our LLM agent improves over single pass LLM and deterministic controllers, reaching state-of-the-art performance across the sEH score, synthetic accessibility score, and AiZynthFinder success rate metrics. These results suggest that constrained LLM agents can play a significant role in molecular discovery without requiring training, fine-tuning, or dedicated generative models.

</details>


### 159. Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents

- **Authors:** Abhilasha Lodha, Mahsa Pahlavikhah Varnosfaderani, Abir Chakraborty, Abhinav Mithal
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10209v1](http://arxiv.org/abs/2606.10209v1)
- **PDF:** [https://arxiv.org/pdf/2606.10209v1](https://arxiv.org/pdf/2606.10209v1)
- **Categories:** cs.AI, cs.LG, cs.SE


> The paper demonstrates that, for long‑horizon, tool‑using LLM agents in enterprise workflows, keeping only the most recent tool interactions and supplementing them with compact automatic summaries dramatically improves both performance and efficiency. By experimentally comparing four GPT‑5 configurations on a 50‑task expense‑itemization benchmark, the authors show that pruning the context to the last five tool calls raises completion from 71 % to 79 % while cutting token usage by two‑thirds, and adding summarization pushes completion to 91.6 % (99.64 % amount correctly itemized) with only a modest increase in tokens and runtime. The study provides quantitative evidence (including confidence intervals and effect‑size analysis) that selective context retention plus summarization is a superior context‑engineering strategy for long‑horizon, tool‑using agents.


<details>
<summary>Abstract</summary>

Large language models deployed as autonomous agents for enterprise workflows face a key challenge: verbose tool responses from enterprise systems can cause context overflow, stale-state errors, and high inference cost. We study this problem in automated expense itemization in Microsoft Dynamics 365 Finance and Operations using Model Context Protocol tools. We evaluate four GPT-5 configurations on a 50-task hotel expense benchmark: no user model, full conversation history, context pruned to the last 5 tool call/response pairs, and pruning with automated summarization. Results are averaged across 5 independent runs, with the user model held constant for the context-engineering comparison. The no-user-model baseline achieves only 8.0% complete itemization. Full-context retention improves completion to 71.0%, but consumes 1,480,996 tokens and 14.56 hours per benchmark. Pruning to the last 5 tool calls improves completion to 79.0% while reducing token use to 535,274 and runtime to 5.39 hours. Adding summarization achieves the best result: 91.6% complete itemization and 99.64% average amount itemized, with 553,374 tokens and 5.79 hours. We further report confidence intervals, effect-size analysis, sensitivity over pruning and summary windows, failure analysis, results across five expense types grouped into three categories, and cross-model evidence with Claude Sonnet 4.5. These results show that, for this class of enterprise tool-use workflow, selective retention of recent tool interactions plus compact summarization can improve both reliability and efficiency compared with full-history retention.

</details>


### 160. What makes a harness a harness: necessary and sufficient conditions for an agent harness

- **Authors:** Sanderson Oliveira de Macedo
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.10106v1](http://arxiv.org/abs/2606.10106v1)
- **PDF:** [https://arxiv.org/pdf/2606.10106v1](https://arxiv.org/pdf/2606.10106v1)
- **Categories:** cs.SE, cs.AI


> The paper provides the first formal, operational definition of an **agent harness**—the software layer that wraps a large language model and turns it into a code‑writing agent capable of acting on a repository. By conducting a systematic conceptual analysis of primary documentation, grey literature, and historical terminology, the authors derive necessary and sufficient conditions that distinguish a harness from related artifacts (frameworks, SDKs, IDE plugins, evaluation scaffolds, and orchestrators), and encode these conditions as a concrete inclusion/exclusion test. Applying this test to six existing systems (Claude Code, Codex CLI, Aider, Cline, OpenHands, SWE‑agent) and several edge cases demonstrates consistent classification, offering a shared vocabulary and criteria that can standardize engineering practice and empirical comparison in the agentic AI field.


<details>
<summary>Abstract</summary>

The term agent harness now circulates widely in software engineering with generative artificial intelligence. It names the layer that wraps a language model and turns it into a coding agent able to act on a repository. The usage is loose and polysemous. Sometimes the term denotes the whole product (Claude Code, Codex CLI); sometimes it denotes the evaluation scaffold that runs an agent against tasks (the SWE-bench harness); sometimes it gets conflated with an agent framework, an SDK, an IDE plugin, or an orchestrator. What is missing is a reference definition that works as an instrument, one that includes and excludes cases consistently. We build that definition through a conceptual analysis that combines works with persistent identifiers and primary grey-literature sources, such as official documentation, glossaries, and engineering reports. We reconstruct the genealogy of the term, from the horse's tack to the classic test harness, to the machine-learning evaluation harness, and finally to the agent harness. We then propose a constitutive definition that states the necessary and sufficient conditions for a system to be an agent harness, we operationalize it as an inclusion and exclusion test, and we draw the boundary of the concept against an agent framework, an agent SDK, an IDE plugin, an eval harness, and an orchestrator. We apply the definition to six real harnesses (Claude Code, Codex CLI, Aider, Cline, OpenHands, and SWE-agent) and to deliberate edge cases; the test includes and excludes consistently. We close with a research agenda organized by design tension axes. The contribution is an operational definition of agent harness, with a shared vocabulary, able to guide engineering practice and the scientific comparison of agentic systems.

</details>


### 161. FASE: Fast Adaptive Semantic Entropy for Code Quality

- **Authors:** Shizhe Lin, Ladan Tahvildari
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09800v1](http://arxiv.org/abs/2606.09800v1)
- **PDF:** [https://arxiv.org/pdf/2606.09800v1](https://arxiv.org/pdf/2606.09800v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> The paper introduces **Fast Adaptive Semantic Entropy (FASE)**, a lightweight metric for estimating functional correctness of code produced by interacting LLM agents without expensive language‑model based equivalence checks. FASE builds a minimum‑spanning‑tree over structural and semantic dissimilarity graphs to approximate code uncertainty, and is evaluated on HumanEval and BigCodeBench where it achieves a 25 % lift in Spearman correlation and a 19 % gain in ROCAUC against Pass@1 compared to prior semantic‑entropy methods, while using only ~0.3 % of their runtime. These results demonstrate that FASE can reliably quantify and mitigate hallucination‑driven error propagation in multi‑agent code‑generation pipelines with minimal computational cost.


<details>
<summary>Abstract</summary>

Multi-agent code generation offers a promising paradigm for autonomous software development by simulating the human software engineering lifecycle. However, system reliability remains hindered by LLM hallucinations and error propagation across interacting agents. While semantic entropy provides a principled way to quantify uncertainty without ground-truth answers, current methods often rely on costly LLM-driven equivalence checks. In this work, we introduce Fast Adaptive Semantic Entropy (FASE), a novel metric that approximates functional correctness based on the minimum spanning tree of structural and semantic dissimilarity graphs. Evaluations on HumanEval and BigCodeBench demonstrate that FASE outperforms state-of-the-art semantic entropy by LLM entailment, achieving a 25% average improvement in Spearman correlation and a 19% increase in ROCAUC score against Pass@1 from ground-truth test cases when using the Qwen3-Embedding-8B model. Furthermore, by eliminating costly LLM-driven equivalence evaluation, FASE incurs negligible computational overhead, requiring only approximately 0.3% of the runtime cost of traditional semantic entropy approaches. These results position FASE as a practical, cost-effective solution for optimizing uncertainty quantification in real-world multi-agent workflows.

</details>


### 162. Collaborative Human-Agent Protocol (CHAP)

- **Authors:** Arsalan Shahid, Gordon Suttie, Philip Black
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09751v1](http://arxiv.org/abs/2606.09751v1)
- **PDF:** [https://arxiv.org/pdf/2606.09751v1](https://arxiv.org/pdf/2606.09751v1)
- **Categories:** cs.AI, cs.CL, cs.HC


> The paper introduces **Collaborative Human‑Agent Protocol (CHAP)**, a lightweight yet extensible standard that formally defines a shared workspace for accountable, multi‑human/multi‑agent workflows by turning ad‑hoc edits, approvals, and hand‑offs into structured, immutable events (diffs, rationales, cryptographic hashes, and signatures). The authors design a minimal core (workspaces, participants, tasks, artefacts, and an append‑only evidence log) and a set of composable profiles that can be layered to add review, routing, deliberation, identity, and audit features, providing a concrete specification, reference implementation, and conformance suite. Empirical examples demonstrate that CHAP captures human judgment as a verifiable signal, enables reproducible hand‑offs across shifts, and supports non‑repudiable approvals that can be replayed long after the original interaction, addressing a key gap in current agentic AI deployments.


<details>
<summary>Abstract</summary>

Foundation models are moving from response generation into operational roles. They plan across steps, call tools, request human input, coordinate with other agents, and increasingly carry responsibility for work that affects customers, claims, code, contracts, and clinical decisions. Production deployments are no longer one human supervising one model. They are multi-human, multi-agent collaborations that cross teams, time zones, and trust boundaries. The technical surface for this collaboration remains weakly specified. When an agent drafts a response and a human edits it before it ships, the moment of human judgement is the most valuable signal in the system. In current practice it is recorded, if at all, in application code, chat threads, ticket comments, and tribal memory. Two protocol standards address adjacent concerns: MCP standardises agent access to tools and data, and A2A standardises agent-to-agent interoperability. Neither defines the shared workspace in which humans and agents perform accountable work together. This paper presents CHAP, the Collaborative Human-Agent Protocol. Under CHAP, the override that used to vanish into a chat thread becomes a structured event carrying a diff, a rationale, and a content hash. The handoff between shifts becomes a portable envelope rather than a pinned message. The human approval of an agent's draft becomes a non-repudiable signed decision that can be replayed years later. The protocol achieves this through a small Core (workspaces, participants, tasks, artefacts, and an append-only evidence log) together with composable profiles that add review, modes, routing, deliberation, handoff, identity, signatures, and transparency-backed audit as deployments require them. Specification, reference implementation, conformance suite, and worked examples are available at: https://github.com/BrightbeamAI/chap

</details>


### 163. Observability for Delegated Execution in Agentic AI Systems

- **Authors:** Abhinav Mishra, Kumar Sharad
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09692v1](http://arxiv.org/abs/2606.09692v1)
- **PDF:** [https://arxiv.org/pdf/2606.09692v1](https://arxiv.org/pdf/2606.09692v1)
- **Categories:** cs.CR, cs.AI


> The paper identifies a fundamental blind spot in current audit‑log and execution‑trace mechanisms: they cannot uniquely determine which actions were performed under a particular delegation in modern LLM‑driven agentic systems, because tool selection, execution ordering, and sub‑agent spawning create interleaved and ambiguous traces. To close this gap, the authors propose an “agent‑aware observability substrate” that consists of a lightweight gateway and a unified information model that tags every execution event with its delegation context at runtime, allowing precise attribution of actions and access footprints across heterogeneous tools without relying on heuristic time‑window correlation. Experiments show that the substrate reliably reconstructs delegation‑scoped histories and supports forensic queries, demonstrating a practical path toward accountable, secure delegated execution in agentic AI deployments.


<details>
<summary>Abstract</summary>

Delegation-scoped execution is not identifiable from standard observables: audit logs and execution traces can be identical under multiple incompatible delegation assignments. This gap is especially acute in LLM-based agentic systems, where agents dynamically select tools, vary execution sequences across runs for the same instruction, and spawn cooperating sub-agents. These dynamics fragment and interleave traces, making delegation-scoped reconstruction from causal structure alone structurally underdetermined. Although individual actions are authorized and logged, existing audit, tracing, and security schemas lack the semantics to reconstruct what actions occurred under a given delegation across heterogeneous systems. We focus on delegation-scoped attribution and access/share footprint reconstruction, not intent inference or reasoning reconstruction. We present an agent-aware observability substrate consisting of a lightweight gateway and a common information model that binds delegation context at execution time. This enables reliable cross-tool delegation-scoped reconstruction and direct forensic queries without heuristic time-window correlation.

</details>


### 164. (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs

- **Authors:** Wesley Pegden
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09674v1](http://arxiv.org/abs/2606.09674v1)
- **PDF:** [https://arxiv.org/pdf/2606.09674v1](https://arxiv.org/pdf/2606.09674v1)
- **Categories:** cs.AI, cs.LO, math.CO


> The paper introduces **Trellis**, an auto‑formalization framework that uses general‑purpose LLM agents in a tightly controlled, deterministic workflow to incrementally translate natural‑language proofs into Lean. By enforcing a “meaning‑of‑rigor” process semantics—where each proof step must be readily expandable into finer detail—the system achieves reliable formalization without any task‑specific fine‑tuning, relying instead on iterative refinement and verification within Lean. The authors demonstrate Trellis’s effectiveness by fully formalizing a recent Ramsey‑theory breakthrough, showing that modest computational budgets and generic agents can produce rigorous, end‑to‑end Lean proofs.


<details>
<summary>Abstract</summary>

We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.

</details>


### 165. Civil Court Simulation with Large Language Models

- **Authors:** Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09632v1](http://arxiv.org/abs/2606.09632v1)
- **PDF:** [https://arxiv.org/pdf/2606.09632v1](https://arxiv.org/pdf/2606.09632v1)
- **Categories:** cs.CL


> The paper introduces a multi‑agent framework that uses large language models to simulate Chinese civil court trials, structuring interactions among judge, plaintiff, defendant, and other roles according to the five‑stage civil procedure and augmenting the agents with a memory store and a legal‑statute retrieval component. By running extensive experiments, the authors show that the system can generate coherent civil judgments—particularly excelling at allocating liability and adjudicating multiple claim items—and that the fidelity of the agents’ memory dramatically influences overall performance. A five‑layer factor analysis (legal grounding, information conditions, judicial capability/role orientation, organizational pressure, and social context) further clarifies how these elements shape the reliability and behavior of LLM‑driven civil court simulations, offering a scalable alternative to costly human‑based legal training.


<details>
<summary>Abstract</summary>

Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: https://github.com/foggpoy/Civil-Court.

</details>


### 166. AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving

- **Authors:** Rakibul Hasan Rajib, Mengxin Zheng, Qian Lou
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09613v1](http://arxiv.org/abs/2606.09613v1)
- **PDF:** [https://arxiv.org/pdf/2606.09613v1](https://arxiv.org/pdf/2606.09613v1)
- **Categories:** cs.CL, cs.AI


> **AGENTSERVESIM** introduces the first hardware‑aware simulator that can model the stateful, multi‑turn execution patterns of large‑language‑model (LLM) agents, including turn dependencies, tool‑induced idle gaps, and KV‑cache reuse across turns.  The system composes a Program Orchestrator, Tool Simulator, Session‑Aware Router, and a KV‑Residency model to evaluate scheduling, cache placement, and routing policies at program granularity while tracking KV state in HBM, host DRAM/CXL, and eviction.  In validation against production deployments, AGENTSERVESIM reproduces latency, throughput, and memory‑usage metrics within ≈ 6 % error, demonstrating that researchers can now explore and optimize agent‑serving strategies without expensive accelerator experiments.


<details>
<summary>Abstract</summary>

Multi-turn LLM agents interleave model calls with external tool invocations, shifting serving from stateless request processing to stateful program execution. Serving these workloads requires scheduling, KV-cache management, and routing policies that use program-level context, including turn dependencies, tool-induced gaps, and reusable KV state. Evaluating such policies directly on real systems is costly, since each design point may require dedicated accelerator time across arrival rates, model scales, serving-instance counts, and memory hierarchies. Simulation offers a scalable alternative, but existing LLM serving simulators target stateless request-level workloads and therefore omit the core dynamics of agent serving: multi-turn program execution, cross-turn cache locality, and KV-cache residency during tool gaps. We present AGENTSERVESIM, a hardware-aware simulator for multi-turn LLM agent serving. AGENTSERVESIM evaluates serving policies at program granularity through composable modules: a Program Orchestrator preserves program identity and turn order, a Tool Simulator materializes tool-induced gaps, a Session-Aware Router maintains program-to-instance affinity for cache-aware dispatch, and a KV Residency Model tracks policy-defined KV placement across HBM, host DRAM/CXL, and eviction. Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs. These results show that AGENTSERVESIM enables controlled, repeatable exploration of agent-serving policies without requiring exhaustive deployment on costly accelerators.

</details>


### 167. Shape Formation for the Cooperative Transportation of Arbitrary Objects Using Multi-Agent Reinforcement Learning

- **Authors:** Mohamed Sayed, Wolfram Burgard, Tanja Katharina Kaiser
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09610v1](http://arxiv.org/abs/2606.09610v1)
- **PDF:** [https://arxiv.org/pdf/2606.09610v1](https://arxiv.org/pdf/2606.09610v1)
- **Categories:** cs.RO, cs.AI


> **Main contribution:** Introduces a novel multi‑agent reinforcement‑learning (MARL) framework that learns formation‑control policies for a team of robots to autonomously position themselves beneath arbitrary‑shaped, non‑uniformly weighted objects for cooperative transport.

**Methodology:** The authors formulate the pattern‑formation problem as a MARL task in which each robot receives local observations (object geometry, mass distribution, nearby obstacles) and learns a decentralized policy via centralized training with shared critics. The reward function jointly encourages balanced support of the object’s weight, collision avoidance, and compact formation shaping, enabling the system to adapt to varying robot counts and cluttered environments.

**Key findings:** Experiments across diverse simulated scenes demonstrate that the learned policies consistently generate balanced, obstacle‑free formations, successfully generalize to unseen object geometries and mass profiles, and outperform classical decomposition‑based baselines in both success rate and formation stability—highlighting the viability of MARL for real‑world, shape‑aware cooperative transport in the agentic AI domain.


<details>
<summary>Abstract</summary>

Cooperative object transportation is essential in numerous domains, including industrial to domestic services. A popular transportation strategy is to carry objects on top of multi-robot systems. The corresponding task is typically solved by decomposing it into three interconnected subproblems: formation control, cooperative navigation, and collision avoidance. A particular challenge posed by real-world objects is their potentially arbitrary shape and non-uniform mass distribution, necessitating robot formations that securely support the object. In this work, we address the challenge of pattern formation control for transporting such real-world objects by proposing a novel multi-agent reinforcement learning approach. Our approach enables a multi-robot system to autonomously position itself underneath an object to support its weight while avoiding obstacles during the formation process. Our evaluations with diverse environments and varying numbers of robots show that our approach leads to policies that reliably produce balanced formations and generalize to cluttered scenes and objects with complex geometry and non-uniform mass distribution.

</details>


### 168. SecureClaw: Clawing Back Control of LLM Agents

- **Authors:** Yuhan Ma, Stefan Schmid
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09549v1](http://arxiv.org/abs/2606.09549v1)
- **PDF:** [https://arxiv.org/pdf/2606.09549v1](https://arxiv.org/pdf/2606.09549v1)
- **Categories:** cs.CR, cs.AI


> SecureClaw introduces a dual‑boundary architecture for tool‑using LLM agents that simultaneously enforces authorization at the effect sink and confines sensitive plaintext at the read boundary. It does so by routing reads through a trusted gateway that replaces raw values with opaque handles (or bounded declassified summaries) and by requiring all external writes to follow a PREVIEW→COMMIT protocol where only a trusted executor can commit the policy‑approved canonical request. evaluated across AgentDojo, AgentLeak, and the Agent Security Bench, SecureClaw uniquely preserves task utility while reducing attack success rates to 0 % on ASB, 0.64 % on AgentDojo, and a 3.23 % overall leak on AgentLeak’s parity lane, demonstrating state‑of‑the‑art security for agentic AI.


<details>
<summary>Abstract</summary>

Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.

</details>


### 169. 3SPO: State-Score-Supervised Policy Optimization for LLM Agents

- **Authors:** Yu Han, Kailing Li, Yang Jiao, Yulin Dai, Yuqian Fu, Linhai Zhuo, Tianwen Qian
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09961v1](http://arxiv.org/abs/2606.09961v1)
- **PDF:** [https://arxiv.org/pdf/2606.09961v1](https://arxiv.org/pdf/2606.09961v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution**: The paper introduces **State‑Score‑Supervised Policy Optimization (3SPO)**, a reinforcement‑learning algorithm that performs *post‑step* policy updates for LLM‑based agents by assigning a dynamic “state score”—derived from the empirical success rates of previously visited states—to each intermediate step, thus enabling fine‑grained credit assignment without learning a value function or auxiliary models.

**Methodology**: 3SPO treats each decision point as a per‑state multi‑armed bandit, computes a state‑score that supervises step‑wise action selection, adaptively determines rollout lengths, and updates the policy after every step. The authors prove logarithmic regret for the allocation scheme and give sample‑complexity bounds for correctly identifying optimal actions, distinguishing scores, and maintaining stable filtering. Empirical evaluation on the ALFWorld and WebShop benchmarks with Qwen2.5‑1.5B/7B‑Instruct models compares 3SPO against GRPO.

**Key findings**: 3SPO achieves **+22.6 %** higher success on ALFWorld and **+15.6** points on WebShop, while exploring ~2.4× more states and converging ~1.8× faster than GRPO using comparable compute. These results demonstrate that fine‑grained, score‑supervised updates substantially improve sample efficiency and performance of LLM agents in sparse‑reward, long‑horizon tasks.


<details>
<summary>Abstract</summary>

Training large language models (LLMs) as autonomous agents via reinforcement learning (RL) has enabled frontier models to achieve superhuman performance in long-horizon tasks. However, existing RL algorithms operate at the trajectory level, performing policy optimization only after collecting complete episode rollouts. This coarse-grained approach faces fundamental challenges in multi-turn agent settings where rewards are sparse, delayed, and credit assignment across individual steps is critical. In this work, we propose \textbf{State-Score-Supervised Policy Optimization (3SPO)}, a novel RL algorithm that performs post-step policy optimization with dynamic state score supervision. At each step, 3SPO computes the state score based on historical success rates, supervising step-wise credit assignment, adaptive rollout and post-step policy optimization without requiring value function estimation or additional auxiliary models. Theoretically, under a per-state bandit abstraction, we show that the proposed score-supervised allocation mechanism achieves logarithmic allocation regret and provide sample-complexity guarantees for action identification, score distinguishability, and filtering stability. Experiments on ALFWorld and WebShop with Qwen2.5-1.5B/7B-Instruct show that 3SPO consistently outperforms GRPO by $+22.6\%$ on ALFWorld and $+15.6$ points on WebShop, while using comparable resources to achieve $2.4\times$ more state exploration and $1.8\times$ faster convergence. Code is available at https://github.com/genalyu/3SPO.

</details>


### 170. Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents

- **Authors:** Tianxiang Fei, Mingyang Song, Mao Zheng, Xiang Yu
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09483v1](http://arxiv.org/abs/2606.09483v1)
- **PDF:** [https://arxiv.org/pdf/2606.09483v1](https://arxiv.org/pdf/2606.09483v1)
- **Categories:** cs.CL, cs.AI


> **Main contribution:**  
The paper introduces **DCPM**, a dual‑process memory architecture for LLM‑based agents that separates fast, surface‑level recording of belief updates (System 1) from slower, abstract reasoning that builds schemas, intentions, and cross‑domain patterns (System 2), thereby extending memory beyond mere recall to support implicit personalisation and belief revision.

**Methodology:**  
Memory is organized hierarchically—from raw inputs and atomic facts up through diachronic belief trajectories, identity, domain schemas, latent intentions, and cross‑domain core schemas. A synchronous “daytime” writer (System 1) links new observations into doubly‑linked supersedes chains, while an asynchronous “nighttime” processor (System 2) runs offline to induce higher‑level abstractions, resolve collisions, and consolidate schemas.

**Key findings:**  
On the LongMemEval, PersonaMem, and PersonaMem‑v2 benchmarks, adding the System 2 component yields substantial gains on tasks that require implicit cross‑session inference (up to **+5.20** points on PersonaMem‑v2) while providing little benefit on raw span‑recall tasks, confirming that the dual‑process design selectively enhances the higher‑level reasoning capabilities essential for agentic AI.


<details>
<summary>Abstract</summary>

Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DCPM, which reorganises agent memory along a cognitive capability hierarchy ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (System1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (System2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling System2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.

</details>


### 171. H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions

- **Authors:** Shiping Zhu, Yibo Yang, Zhengyang Wang, Tiancheng Shen, Dandan Guo, Ming-Hsuan Yang
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09461v1](http://arxiv.org/abs/2606.09461v1)
- **PDF:** [https://arxiv.org/pdf/2606.09461v1](https://arxiv.org/pdf/2606.09461v1)
- **Categories:** cs.CL


> **Main contribution:** The paper introduces **H2HMem**, the first benchmark that evaluates large‑language‑model agents on memory tasks drawn from realistic **human‑to‑human, multimodal** interactions (dyadic and multi‑party conversations with video, audio, and textual cues).  

**Methodology:** H2HMem supplies curated multimodal conversation streams and three evaluation suites—**recall**, **reasoning**, and **application**—that probe an agent’s ability to (1) construct and retain cross‑modal episodic memories, (2) resolve discourse phenomena (anaphora, deixis, conflicting statements), and (3) apply stored information to downstream queries. State‑of‑the‑art LLM‑based agents are tested on these tasks using zero‑shot and few‑shot prompting.  

**Key findings:** Even the most advanced agents (e.g., GPT‑4‑Turbo, Claude‑3) show **significant deficits** in building coherent multimodal memories, tracking who said what, and leveraging that knowledge across session boundaries, with performance far below human baselines. The results expose critical gaps in current agentic AI memory handling and underline the need for new architectures and training regimes that can integrate and reason over heterogeneous, multi‑speaker data.


<details>
<summary>Abstract</summary>

Large language model agents are increasingly deployed in human-human interaction settings, such as meeting assistants and clinical documentation systems, where they must observe conversations and retain information for downstream queries. Unlike traditional human-assistant settings, these environments are inherently multimodal, involve complex discourse phenomena such as anaphora and deixis, and contain asynchronous or conflicting information from multiple participants. However, existing memory benchmarks largely focus on single-user, text-only interactions, failing to capture these challenges. To address this gap, we introduce H2HMem, a Human-to-Human Multimodal Memory Benchmark for evaluating memory capabilities in complex human-human interactions. H2HMem includes both dyadic and multi-party conversations with multimodal information streams, and evaluates agents along three dimensions: memory recall, reasoning, and application. Experiments with advanced agents reveal substantial limitations in constructing, retaining, and utilizing memories across modalities, participants, and sessions, highlighting substantial room for improvement in next-generation LLM agents.

</details>


### 172. AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning

- **Authors:** Bojie Rong, Zheyu Shen, Qiaoping Wang, Pengfei Kang, Yang Xu, Yawen Wei, Hanyu Wu, Zhi Zhao, Leihao Pei, Linquan Jiang
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09447v1](http://arxiv.org/abs/2606.09447v1)
- **PDF:** [https://arxiv.org/pdf/2606.09447v1](https://arxiv.org/pdf/2606.09447v1)
- **Categories:** cs.AI


> The paper introduces **AliyunConsoleAgent**, a web‑agent framework that learns to verify cloud‑console documentation by interacting with real‑world Alibaba Cloud UIs. The authors train a 32‑billion‑parameter model in two stages: first, supervised fine‑tuning on trajectories distilled from a high‑performing proprietary model, then reinforcement learning with a novel Group Relative Policy Optimization algorithm and a dual‑channel reward model that combines on‑policy success signals and rule‑based audit‑log evaluations in a deterministic Terraform‑provisioned environment. On a 278‑task benchmark, the resulting agent reaches 63.5 % success—closing the gap to the best proprietary model to just 1.8 pp—while cutting inference cost by roughly 92 %, demonstrating that cost‑effective, privacy‑preserving agents can attain near‑state‑of‑the‑art performance in complex cloud‑console settings.


<details>
<summary>Abstract</summary>

We present AliyunConsoleAgent, a web agent framework for automated documentation verification in real-world cloud consoles. Major cloud platforms encompass hundreds of products with rapid feature iteration, causing console UIs to frequently diverge from their corresponding documentation. Verifying that documented procedures accurately reflect the current console and can be executed end-to-end demands an estimated 4 million recurring inspections annually, yet manual coverage remains below 1%. While agent systems built on frontier proprietary models achieve high success rates, their prohibitive cost and data privacy constraints preclude large-scale deployment. We propose a two-stage training paradigm: supervised fine-tuning (SFT) on distilled frontier-model trajectories, followed by reinforcement learning using Group Relative Policy Optimization (GRPO) and a dual-channel outcome reward model in real cloud environments. To support large-scale RL training, we construct a high-determinism rollout system featuring Terraform-based resource pre-provisioning and LLM-driven on-demand provisioning, which effectively isolates environment noise from the training signal. We further introduce a rule-based reward evaluation protocol grounded in backend audit logs, providing objective, reward-hacking-resistant outcome judgment. Our model evolves from mechanical instruction following to autonomous decision-making with cloud console and product-specific understanding. Experiments on a challenging 278-task benchmark where the best frontier model achieves only 65.34% demonstrate that AliyunConsoleAgent-32B achieves a 63.52% mean success rate -- a 20.24 percentage-point improvement over the base model, narrowing the gap to the best frontier proprietary model to 1.82 pp (bootstrap 95% CI [-1.27, 7.39]) -- at 92% lower inference cost.

</details>


### 173. MASK: Multi-Agent Semantic K-Scheduling for Risk-Sensitive 6G Robotics

- **Authors:** Ahmet Gunhan Aydin, Elif Tugce Ceran
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.11249v1](http://arxiv.org/abs/2606.11249v1)
- **PDF:** [https://arxiv.org/pdf/2606.11249v1](https://arxiv.org/pdf/2606.11249v1)
- **Categories:** cs.RO, cs.LG, cs.MA


> **Contribution** – The paper introduces **MASK (Multi‑Agent Semantic K‑Scheduling)**, a control framework that lets large robot swarms coordinate under the ultra‑tight per‑slot bandwidth limits expected in 6G networks. It shows that by transmitting only the *K* most semantically valuable agents’ observations, a swarm can preserve risk‑aware performance without needing full‑bandwidth communication.  

**Methodology** – MASK combines (1) *Arbiter‑Assisted Semantic Information Gating* (A‑SIG), a lightweight scheduler that ranks agents locally by a learned semantic‑importance score and grants channel access to the top‑K; and (2) a self‑supervised global encoder that fuses the selected observations into a latent state used by a distributional reinforcement‑learning policy to minimize tail‑risk.  

**Key Findings** – Across several collaborative‑sensing benchmarks, MASK attains near‑optimal task performance—comparable to unconstrained communication baselines—while only a small fraction (≤ 10 %) of agents transmit each slot. The approach also tolerates random packet losses, demonstrating that semantic‑driven K‑scheduling is an effective enabler for risk‑sensitive, resource‑constrained 6G robotic systems.


<details>
<summary>Abstract</summary>

Realizing the vision of 6G connected robotics requires reconciling high-performance collaborative control with the rigid spectral limitations of physical wireless channels. In realistic collaborative sensing scenarios, spectral resources are quantized into finite physical resource blocks or orthogonal subcarriers, rendering simultaneous transmission by all agents infeasible. To address this, we propose Multi-Agent Semantic K-Scheduling (MASK), a control architecture designed to sustain robust, risk-aware coordination under strict instantaneous bandwidth caps. We introduce Arbiter-Assisted Semantic Information Gating (A-SIG), a lightweight coordination mechanism that enforces hard access constraints by scheduling only the top-K agents based on locally computed semantic importance scores. By aggregating these prioritized observations into a compact latent state, a self-supervised global encoder enables a distributional policy to mitigate tail risks despite data sparsity. We evaluate MASK across diverse benchmarks, demonstrating that it matches the performance of communication-unconstrained baselines even when channel access is restricted to a small fraction of the swarm size. Furthermore, the framework exhibits inherent resilience to packet erasures, validating semantic scheduling as a critical enabler for resource-constrained 6G systems.

</details>


### 174. Capability-Aligned Hierarchical Learning for Tool-Augmented LLMs

- **Authors:** Haotong Yang, Ting Long, Yi Chang
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09371v1](http://arxiv.org/abs/2606.09371v1)
- **PDF:** [https://arxiv.org/pdf/2606.09371v1](https://arxiv.org/pdf/2606.09371v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Capability‑Aligned Hierarchical Learning (CAHL)**, a framework that jointly trains the high‑level planner and low‑level tool‑invoking executor of a language‑model‑based agent, addressing the planner‑executor misalignment that hampers tool‑augmented LLM performance.

**Methodology:** CAHL formulates the hierarchical interaction as a single reinforcement‑learning‑with‑value‑regularization (RLVR) problem, sharing a common reward signal and value function across both levels so that the planner’s sub‑task decomposition is directly shaped by the executor’s tool‑use success; the system is trained end‑to‑end on task‑specific prompts and tool APIs.

**Key findings:** Across constrained benchmarks (API‑Bank, BFCL) and the open‑ended Bamboogle environment, CAHL achieves **significant gains** over baselines that train planner and executor separately, showing higher task completion rates, more coherent tool‑selection sequences, and improved sample efficiency—demonstrating that tightly aligned hierarchical learning is essential for robust, tool‑augmented agentic AI.


<details>
<summary>Abstract</summary>

Tool learning enables LLMs to invoke external tools to accomplish tasks. Prior studies have demonstrated the effectiveness of a hierarchical structure: a high-level policy handles global planning and decomposes tasks into manageable sub-tasks, and a low-level policy focuses on invoking tools to solve these sub-tasks. However, these works typically optimize the high-level and low-level policies separately, leading to planner-executor misalignment and limiting LLM performance on tool-use tasks. In this paper, we propose a method called Capability-Aligned Hierarchical Learning (CAHL), which leverages RLVR to jointly optimize both policies, enabling better alignment between the high-level planner and the low-level executor. Experiments on constrained tool-use benchmarks (API-Bank and BFCL) and an open-ended environment (Bamboogle) demonstrate the effectiveness of CAHL.

</details>


### 175. Brain-Prompt Injection: A Route-Safety Audit for BCI-LLM Agents

- **Authors:** Jianwei Tai
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09315v1](http://arxiv.org/abs/2606.09315v1)
- **PDF:** [https://arxiv.org/pdf/2606.09315v1](https://arxiv.org/pdf/2606.09315v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **brain‑prompt injection**, a novel attack vector that manipulates the neural‑signal‑to‑language‑model (BCI‑LLM) pipeline to alter an agent’s routed actions without being detected by EEG‑ or text‑side monitors. To defend against this, the authors formalize a **Route‑Safety Audit Contract**—a minimal logging schema with a hierarchical denominator and endpoint specification—and prove an audit‑schema separation theorem that shows conventional decoder agreement and marginal robustness are insufficient for guaranteeing safe routing. Empirical evaluation on 5 400 left/right motor‑imagery commands across 60 subjects demonstrates that augmenting the contract with split‑conformal calibration and provenance/confirmation checks reduces false‑accept rates to near zero at modest utility (FAR = 0.000 at utility = 0.150 for α = 0.005), while an attacker‑controlled confirmation channel can completely break the bound, confirming the contract’s effectiveness and its limits as a risk‑mitigation—not intent‑certification—mechanism.


<details>
<summary>Abstract</summary>

BCI-to-agent pipelines turn decoded neural activity into an authorization channel for tool-use agents, exposing a new attack surface we call \emph{brain-prompt injection}: signal-side perturbations, context-only injections, and adaptive dual-decoder attacks can all change the routed action while EEG-side or text-side monitors remain blind. Route safety in this stack depends on what the audit log can observe, not on decoder accuracy or agreement alone. We define a Route-Safety Audit Contract: a minimal log schema, denominator hierarchy, and endpoint specification, and prove an audit-schema separation theorem together with a C3 attacked-dependence decomposition; clean agreement and marginal robustness do not identify the joint term that controls C3 routing. As a calibration layer on top of the contract, we apply split-conformal calibration to a non-oracle EEG confirmation channel and report the resulting false-accept frontier under an explicit threat-archetype matrix. We instantiate the contract on EEGMMI native left/right command-control over 5{,}400 events, harmless tool stubs, and seed/case denominators. Provenance blocks C2 routes ($0.000$); agreement-plus-provenance routes C3 flips ($1.000$); confirmation-plus-provenance routes them ($0.000$). The conformal frontier reaches FAR $0.000$ at clean utility $0.150$ for $α=.005$ and FAR $0.119$ at clean utility $0.452$ for $α=.10$ under acquisition isolation; an attacker-controllable confirmation channel breaks the bound to $\approx\!1$. Subject-cluster bootstrap confirms these intervals on $60$ subjects; cross-architecture (TinyEEGNet, EEGNetV4) and capacity-sweep results show within-regime saturation. Mediation and confirmation reduce risk; they are not intent certificates.

</details>


### 176. Self-Paced Curriculum Reinforcement Learning for Autonomous Superbike Racing in Simulation

- **Authors:** Luca Ghisi, Jacopo Essenziale, Carlo D'Eramo, Matteo Luperto
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09236v1](http://arxiv.org/abs/2606.09236v1)
- **PDF:** [https://arxiv.org/pdf/2606.09236v1](https://arxiv.org/pdf/2606.09236v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces a self‑paced curriculum reinforcement‑learning framework that enables an autonomous agent to master high‑speed motorbike racing in the physics‑accurate VRider SBK simulator. By coupling Soft Actor‑Critic with Self‑Paced Deep RL, the system automatically generates increasingly difficult racing tasks based on the agent’s own performance, using an augmented state that includes proprioceptive data, lean‑angle history, and track waypoints, and a reward that balances forward progress with stability‑related penalties. Experiments show that the curriculum‑driven approach converges faster than vanilla SAC and yields shorter lap times and more stable riding across several tracks and bike models, establishing a new baseline for RL‑based autonomous two‑wheeled racing.


<details>
<summary>Abstract</summary>

Autonomous Racing has seen remarkable progress through deep Reinforcement Learning (RL), primarily for four-wheeled vehicles. However, motorbikes introduce substantially greater complexity due to the need to manage balance and lean angle, in addition to more reactive steering and throttle control, and a smaller weight. In this work, we present a framework for training an autonomous agent to race a superbike in VRider SBK, a physics-accurate Unity-based motorbike simulator. Our approach integrates Soft Actor-Critic (SAC) with Self-Paced curriculum Deep reinforcement Learning (SPDL), which dynamically generates progressively more challenging tasks based on the agent's performance, without requiring manual curriculum design. The agent's state space comprises proprioceptive features extended with lean-angle history, along with global track features via course points. The reward signal is shaped to encourage progress along the track while penalizing instability-inducing behaviors specific to two-wheeled dynamics. Preliminary experimental results demonstrate that SPDL outperforms SAC alone in training efficiency, lap time, and driving stability across multiple tracks and motorbike models, establishing a first baseline for RL-based autonomous motorbike racing.

</details>


### 177. Autonomous Incident Resolution at Hyperscale: An Agentic AI Architecture for Network Operations

- **Authors:** Arun Malik
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09122v1](http://arxiv.org/abs/2606.09122v1)
- **PDF:** [https://arxiv.org/pdf/2606.09122v1](https://arxiv.org/pdf/2606.09122v1)
- **Categories:** cs.SE, cs.AI, cs.ET, cs.MA, cs.NI


> The paper introduces a hierarchical, multi‑agent architecture that enables fully autonomous detection, diagnosis, and remediation of network incidents at hyperscale cloud providers. By decomposing the problem into specialized AI agents that invoke tools via standardized protocols, encode runbook knowledge, and operate under progressive autonomy with layered safety checks (authorization, verification, rollback), the system can resolve > 90 % of common incidents without human input while preserving strict safety guarantees. Real‑world deployment results demonstrate that such agentic AI pipelines can close the loop on network failures at production scale, highlighting both the efficacy of skill‑based orchestration and the importance of safety‑bounded autonomy for large‑scale operational AI.


<details>
<summary>Abstract</summary>

Cloud network infrastructure at hyperscale presents unique operational challenges where traditional human-driven incident response cannot keep pace with the volume, velocity, and complexity of failures. This paper presents an agentic AI architecture for autonomous incident resolution in large-scale network operations. Our system employs a multi-agent orchestration framework where specialized AI agents collaborate to detect, diagnose, and remediate network incidents without human intervention. We describe the architectural principles, including hierarchical agent decomposition, skills-based tool invocation via standardized protocols, structured knowledge encoding from operational runbooks, progressive autonomy with safety boundaries, and closed-loop verification. The architecture has been deployed in production at a major cloud provider, demonstrating that agentic AI systems can achieve autonomous resolution rates exceeding 90% for common incident categories while maintaining safety guarantees through layered authorization and rollback mechanisms. We discuss design tradeoffs, failure modes, and lessons learned from operating autonomous AI agents at scale.

</details>


### 178. Context-Fractured Decomposition Attacks on Tool-Using LLM Agents: Exploiting Artifact Provenance Gaps

- **Authors:** Xiaofeng Lin, Yukai Yang, Daniel Guo, Sahil Arun Nale, Charles Fleming, Guang Cheng
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09084v1](http://arxiv.org/abs/2606.09084v1)
- **PDF:** [https://arxiv.org/pdf/2606.09084v1](https://arxiv.org/pdf/2606.09084v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper identifies and formalizes a new failure mode for tool‑using LLM agents called the *provenance gap*—the inability of defenses to track how harmless‑looking artifacts created in early steps are later recombined to produce harmful behavior. It introduces *Context‑Fractured Decomposition* (CFD), a family of multi‑step jailbreak attacks that deliberately split the malicious intent across separate tool actions and agent instances, exploiting the missing artifact lineage.

**Methodology:** The authors instrument a standard agent pipeline with trace‑level diagnostics to detect when artifacts (files, logs, etc.) are generated without provenance metadata, then construct CFD attacks that keep intermediate artifacts benign while triggering a harmful output only after those artifacts are later consumed. They evaluate CFD against existing jailbreak benchmarks (including Crescendo and Tree of Attacks) and compare success rates against strong single‑turn judges.

**Key findings:** CFD attacks raise jailbreak success rates by up to **28.3 percentage points** over prior state‑of‑the‑art baselines, even when defenses can view each turn in isolation. The study demonstrates that conventional defenses that assume a contiguous conversational context are insufficient for deployed agents, and proposes provenance‑lineage tagging as a promising mitigation.


<details>
<summary>Abstract</summary>

Tool-using LLM agents interact with the world through actions that persist state in artifacts (e.g., workspace files or logs). Consequently, jailbreak defenses must reason about cross-step composition rather than isolated text. Yet most existing attacks and defenses, including ``multi-turn'' jailbreaks such as Crescendo and Tree of Attacks,still assume a single contiguous conversation visible to the defender. This assumption breaks down in real agent pipelines, where enforcement is fragmented across tools, modules, and time, and where artifact provenance is often not tracked. We operationalize a deployment failure mode for tool-using LLM agents, the \emph{provenance gap}, and study reproducible triggers for it: \emph{Context-Fractured Decomposition} (CFD), a family of cross-context multi-step jailbreaks that preserve benign-looking intermediate artifacts from an early interaction and elicit harmful behavior much later, potentially in a different agent instance or workflow stage, via individually innocuous tool actions whose risk emerges only under delayed artifact-mediated composition. We instrument the failure mode with trace-level diagnostics and outline a verifiable mitigation direction (provenance lineage tagging). Across agent-system jailbreak benchmarks, CFD improves success rates by up to 28.3 percentage points over state-of-the-art baselines, even against strong single-turn judges. Disclaimer: This paper contains examples of harmful or offensive language.

</details>


### 179. REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces

- **Authors:** Xiaofeng Lin, Yingxu Wang, Tung Sum Thomas Kwok, Daniel Guo, Sahil Arun Nale, Charles Fleming, Guang Cheng
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09071v1](http://arxiv.org/abs/2606.09071v1)
- **PDF:** [https://arxiv.org/pdf/2606.09071v1](https://arxiv.org/pdf/2606.09071v1)
- **Categories:** cs.AI


> REFLECT introduces a closed‑loop error‑attribution framework for LLM agents that first hypothesizes a faulty step, then intervenes by replaying the trace with a targeted “patch” and uses the resulting success/failure as contrastive feedback to refine the attribution. The method combines a lightweight classifier (or LLM judge) to generate candidate error locations with controlled execution experiments, iteratively updating its belief about the true error step. Evaluated on four multi‑hop reasoning and tool‑use benchmarks, REFLECT outperforms all same‑auditor baselines in localization accuracy—especially on structured tool‑use traces—and can produce useful error diagnoses even when the correct final answer is unknown.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents now solve complex tasks through long plan-and-execution traces, yet the ability to locate errors in a completed traces still lags far behind, especially in the \emph{silent failure} regime. Existing approaches predict suspect steps via classifiers or LLM judges, or recover correct answers via retry, but none feed the intervention outcome back to \emph{refine the attribution itself}. We propose \methodname, a method that closes this gap by diagnosing a candidate error step, testing it through controlled replay with a diagnosis-specific patch, and using the verified outcome flip as contrastive evidence to refine the final attribution. Across four localization benchmarks spanning multi-hop reasoning across domains, \methodname achieves the highest localization accuracy among same-auditor methods across all four benchmarks, with the largest gains on structured tool-use traces, while providing actionable localization even when ground-truth answers are unavailable.

</details>


### 180. Agent Economics: An Entropy-Controlled Pluralistic Alignment Framework for Preventing Artificial Hivemind in Autonomous Agents

- **Authors:** Cheonsu Jeong
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09039v1](http://arxiv.org/abs/2606.09039v1)
- **PDF:** [https://arxiv.org/pdf/2606.09039v1](https://arxiv.org/pdf/2606.09039v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces the **Behavioral Protocol Framework (BPF)**—a pluralistic alignment architecture that uses entropy control to keep autonomous agents from collapsing into a single “hivemind” strategy while simultaneously delivering transparent, auditable decision‑making.

**Methodology:** BPF combines three tightly coupled modules: (1) **Mentalizing‑based Social Intelligence (MbSI)** that equips agents with a Theory‑of‑Mind style model of others, (2) a **Pluralistic Alignment (PA)** component that injects controlled entropy into policy updates to preserve strategic diversity, and (3) a **Verifiable Execution Kernel (VEK)** that logs every action in a cryptographically verifiable trail. The authors implement the system in a Python‑based multi‑agent simulation with a Streamlit UI and run experiments measuring convergence, economic efficiency, and auditability.

**Key findings:** Empirical results show that the entropy‑controlled PA module sustains higher variance in agents’ strategies, markedly reducing the hivemind effect without hurting overall market efficiency, while the VEK provides a complete, tamper‑evident audit log that enhances trust and accountability in the agent economy. This demonstrates a viable path toward robust, transparent, and accountable agent‑native economic systems.


<details>
<summary>Abstract</summary>

This study proposes the Behavioral Protocol Framework (BPF), an entropy-controlled pluralistic alignment framework designed to address two critical challenges in autonomous agent economies: the hivemind effect arising from excessive strategic convergence among agents and the lack of transparency in autonomous decision-making processes. The proposed BPF consists of three core modules: Mentalizing-based Social Intelligence (MbSI) grounded in Theory of Mind (ToM), Pluralistic Alignment (PA), and a Verifiable Execution Kernel (VEK). These modules are organically integrated within a closed-loop architecture that governs the entire lifecycle of agent behavior, from decision-making and execution to verification and feedback. To evaluate the proposed framework, a simulation environment implemented in Python and a Streamlit-based user interface will be developed. Through empirical experimentation, the study aims to examine whether the entropy-control mechanism of the PA module can effectively preserve strategic diversity among agents and mitigate collective convergence, while the VEK module provides a comprehensive and transparent audit trail of the decision-making process. The anticipated results are expected to demonstrate that the proposed framework can simultaneously enhance the stability, efficiency, and trustworthiness of autonomous agent economies. Consequently, this research offers a practical approach for developing robust, transparent, and accountable agent-native economic systems.

</details>


### 181. Personalization Meets Safety:Mechanisms,Risks,and Mitigations in Personalized LLMs

- **Authors:** Yanyan Luo, Xue Han, Ruiqiao Bai, Xin Huang, Yitong Wang, Qian Hu, Qing Wang, Chunxu Zhao, Jie Liu, Cong Geng, Lehao Xing, Pengwei Hu, Junlan Feng
- **Published:** 2026-06-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2606.09038v1](http://arxiv.org/abs/2606.09038v1)
- **PDF:** [https://arxiv.org/pdf/2606.09038v1](https://arxiv.org/pdf/2606.09038v1)
- **Categories:** cs.AI


> The paper provides the first systematic review of how personalization mechanisms in large language models intersect with safety concerns, introducing a taxonomy that maps user‑representation types, personalization paradigms (prompting, retrieval, fine‑tuning, RL, Mixture‑of‑Experts, pruning, agent frameworks, multimodal adaptation) to concrete safety risks and corresponding mitigations throughout the model lifecycle. By analyzing existing datasets, evaluation protocols, and a case study of the OpenClaw ecosystem, the authors show that current research treats safety as user‑agnostic, studies personalization techniques in isolation, and lacks long‑term, relational evaluation, thereby exposing structural gaps in the field. Their unified framework highlights the need for relational safety metrics, compositional analysis of personalization methods, and evaluation tools capable of capturing emergent, long‑term hazards in personalized AI agents.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have enabled increasingly personalized interactions by adapting to users' preferences, contexts, and long-term histories. However, the mechanisms that enable personalization also expand the safety landscape in ways not systematically addressed by existing literature. Existing reviews typically focus either on personalization or safety, leaving their intersection largely unexplored. We present the first comprehensive, safety-aware review of personalized LLMs. We organize personalization along three dimensions-user representation, personalization paradigm, and evaluation-and introduce a unified taxonomy of safety risks. At the representation level, we analyze risks arising from diverse user representations. Across mainstream personalization paradigms, we delineate vulnerabilities inherent to prompting, retrieval augmentation, parameter fine-tuning, reinforcement learning, Mixture-of-Experts (MoE), pruning, agent frameworks, and multimodal personalization, and synthesize mitigation strategies across the model lifecycle. Beyond these fine-grained risks, we characterize paradigm-agnostic safety risks arising from personalized adaptation. We further summarize personalized datasets and evaluation methodologies. Through a case study of OpenClaw, we analyze deployment trends in personalized agent ecosystems. Our analysis reveals three structural inadequacies in existing research: safety is evaluated as user-invariant rather than relational, personalization techniques are analyzed in isolation rather than in composition, and evaluation frameworks cannot capture emergent long-term risks. By jointly examining personalized representations, personalization paradigms, safety risks, defenses, and evaluation methods, we provide a unified framework for developing safe personalized LLMs and highlight key directions for future research.

</details>



## Biorxiv (3 papers)


### 1. A multi-agent system for spine MRI report generation from multi-sequence imaging

- **Authors:** Xiao, Z., Yang, J., Sun, G., Zhang, H., Xu, H., Yao, Y., Miller, Z. D., King, W. E., Kanani, M. M., Andre, J. B., Chu, S., Zhang, M., Kinahan, P. E., Cross, N. M., Wang, S.
- **Published:** 2026-06-11
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.07.730703](https://doi.org/10.64898/2026.06.07.730703)

- **Categories:** bioinformatics


> SpineAgent is a multi‑agent framework that tackles the long‑standing problem of integrating heterogeneous MRI sequences for automated spine‑MRI reporting. The authors first pre‑train separate DINOv3 encoders on T1‑ and T2‑weighted scans and then use a continual‑training synthesizer to embed all other sequences into a unified patient‑level representation; this representation feeds 37 specialized agents (diagnosis, lesion localisation, similar‑case retrieval) whose outputs are tokenised and fed to a end‑to‑end Medical Report Agent. Across 17 pathology‑prediction tasks SpineAgent improves AUROC by an average of 10.8 % over the strongest baselines, generalises across manufacturers and cohorts, and—according to both automated metrics and radiologist review—produces more accurate and interpretable spine‑MRI reports.


<details>
<summary>Abstract</summary>

Spinal pathology is a leading cause of pain and disability worldwide. Spine magnetic resonance imaging (MRI) is central to clinical evaluation, yet its interpretation remains complex and time-consuming, requiring integration of information across multiple imaging sequences and anatomical regions. Despite recent advances in automated MRI analysis, effectively combining multi-sequence data while preserving sequence-specific diagnostic information remains an open challenge. Here we present SpineAgent, a multi-agent framework for spine MRI report generation built upon a multi-sequence foundation model trained on routine clinical data from 32,047 patients and 453,683 MRI series, comprising a total of 13,441,191 MRI slices. To accommodate diverse modalities of sequences, we first pre-train two DINOv3-based encoders separately on T1- and T2-weighted sequences. We then introduce a continual training strategy that learns a synthesizer to embed images of other sequences using the T1 and T2 encoders, producing patient-level embedding that integrates various signals across MRI sequences. Using these embeddings, SpineAgent achieves state-of-the-art performance, with mean 10.8% AUROC improvement across 17 spinal condition-prediction tasks compared to the best competing method, and demonstrates strong generalizability under cross-manufacturer and cross-cohort evaluation. Beyond classification, SpineAgent enables pathology localization by identifying findings-relevant slices and segmenting pathological regions. It also supports multimodal image-report retrieval, providing a solid foundation for scalable and explainable MRI report generation. We further integrate these validated capabilities of SpineAgent into 37 specialized agents for condition diagnosis, pathological-region localization, and clinically-similar-cases retrieval. Finally, we incorporate their outputs as structured tokens within a Medical Report Agent trained end-to-end for report generation. Through both automated metrics and expert evaluation by five radiologists, SpineAgent achieves leading performance in spine MRI report generation. Together, SpineAgent introduces a continual training approach for multi-sequence spine MRI understanding. By decomposing report generation into clinically grounded subtasks addressed by specialized agents, the SpineAgent framework enables accurate, interpretable and generalizable spine MRI reporting across diverse imaging sequences and anatomical regions.

</details>


### 2. Evaluating agentic AI for biological discovery in autonomous and copilot settings

- **Authors:** Johri, S., Pimenta, E. M., Yates, J., Fu, J., Bao, E. L., Jun, H., Reardon, B., Bacot, S., Shady, M., Fu, D., Mei, W., Camp, S. Y., Park, J., Van Allen, E.
- **Published:** 2026-06-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.04.729919](https://doi.org/10.64898/2026.06.04.729919)

- **Categories:** cancer biology


> The paper introduces the **Multistep Multimodal Multi‑omic Agentic (M3A) Framework**, a systematic evaluation platform that lets large‑language‑model (LLM) agents maintain and reason over persistent multimodal single‑cell data states in both fully autonomous and human‑in‑the‑loop (“copilot”) modes. Using the framework, the authors benchmarked agents on tasks such as cell‑type annotation and the generation of falsifiable, gene‑program‑based biological hypotheses across 11 cancer‑type multi‑omic datasets, and measured performance with and without expert guidance. They find that current agentic AIs excel at broad, systematic exploration of heterogeneous data but still depend on domain experts for methodological direction and high‑level biological synthesis, delineating both the promise and the current limits of AI‑driven biological discovery.


<details>
<summary>Abstract</summary>

Advances in large language models (LLMs)-based artificial intelligence (AI) agents have improved their ability to execute structured analytical workflows, including standard bioinformatic pipelines for biological discovery. However, computational biology rarely consists of deterministic pipeline execution alone. Biological datasets are heterogeneous and noisy, and meaningful discovery often requires open-ended hypothesis generation and iterative reasoning over multimodal evidence. These challenges are particularly evident in multi-omic studies, where paired molecular modalities and heterogeneous clinical contexts create both opportunities and obstacles for discovery. The extent to which emerging agentic AI systems can support or automate this mode of scientific discovery remains poorly understood. Here, we systematically evaluated the capabilities and limitations of agentic AI for biological discovery using multi-omic single cell datasets spanning 11 cancer types. We developed the Multistep Multimodal Multiomic Agentic (M3A) Framework to support LLM-driven reasoning over persistent multimodal data states and to capture agentic reasoning behavior in autonomous and human-AI copilot settings. Using this framework, we assessed AI agents across complementary tasks, including autonomous cell-type annotation, generation of falsifiable biological hypotheses from gene programs, and copilot experiments testing the effect of human involvement and domain expertise. We found that current AI agents are effective at broad, systemic exploration of complex data, whereas domain experts remain critical for methodological guidance and biological synthesis across analyses. Together, our results delineate the current potential and boundaries of agentic AI in computational biology, and establish a framework for evaluating AI systems designed to support biological discovery.

</details>


### 3. Reconstructing living materials as a computable design space with multi-agent reasoning

- **Authors:** Xiao, Y., Zeng, X., Yang, Z., Gu, J., Lu, Y., Wang, Y., Wen, H., Chen, M., Huang, Z., Hu, J., Liu, J., Sha, C., Xie, J., Li, H., Zhu, X., Zheng, S., Zhang, J., Zong, W., He, Z., Xu, Y., Zhou, X., Li, F., Liu, H., He, Q., Liu, L., Yu, Z.
- **Published:** 2026-06-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.02.15.705954](https://doi.org/10.64898/2026.02.15.705954)

- **Categories:** biochemistry


> The paper presents **LiveMat**, a multi‑agent reasoning platform that converts unstructured literature on living materials into a structured, computable design space. By extracting and linking 34 k+ records into a knowledge graph of microorganisms, polymers, fabrication processes, functional outputs, evaluation contexts, and performance metrics, LiveMat enables systematic cross‑domain feature integration; its pipeline (constraint decomposition, provenance‑aware extraction, consistency checking, and expert‑anchored ranking) markedly improves reasoning performance over five large language models. In a prospective wound‑healing case study, LiveMat automatically selected a four‑component living‑material formulation that achieved state‑of‑the‑art in‑vivo healing, demonstrating the framework’s potential to accelerate interpretable, evidence‑grounded discovery of agentic living‑material systems.


<details>
<summary>Abstract</summary>

Artificial intelligence is increasingly used to accelerate scientific discovery, but most successful frameworks operate within well-defined molecular, protein or materials spaces. Living materials present a more formidable computational problem because functions emerge from context dependent coupling among cells, matrices, fabrication processes and evaluation conditions. Here we introduce LiveMat, a multi-agent reasoning framework that transforms unstructured literature into a computable design space for living materials. LiveMat standardizes 34,215 living material records, integrating 16,769 microorganism and 17,446 polymer entries into a knowledge graph linking living components, abiotic matrices, functional outputs, evaluation contexts and performance metrics. Benchmarking across five large language models shows that living material reasoning is limited mainly by cross-domain feature integration rather than coarse classification. LiveMat overcomes this limitation through constraint decomposition, provenance-aware extraction, consistency checking and expert-anchored ranking. In a prospective wound-healing task, it prioritizes a four-component design with state-of-the-art in vivo performance, establishing a scalable infrastructure for interpretable, evidence-grounded living material discovery.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*