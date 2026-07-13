# Weekly AI Agent Paper Report

**Generated:** 2026-07-13 12:46
**Period:** 2026-07-06 to 2026-07-12

## Summary

- **Total papers fetched:** 782
- **Papers matching keywords:** 149
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-07-06) | Change |
|--------|-----------|-----------|--------|
| Total matched | 149 | 148 | +1 |
| arxiv | 148 | 147 | +1 |
| biorxiv | 1 | 1 | +0 |
| medrxiv | 0 | 0 | +0 |

### Notable Trends

**AI‑Agent Paper Landscape – Week 22 vs. Week 21**

| Metric | Week 22 (this week) | Week 21 (last week) | Change |
|--------|---------------------|----------------------|--------|
| Total papers | **149** | **148** | +1 (0.7 %) |
| arXiv‑only | 148 | 147 | +1 |
| bioRxiv‑only | 1 | 1 | no change |
| Median arXiv‑category (by subject) | *Computer Vision & Robotics* (45 %) | *LLM‑Applications* (42 %) | shift toward embodied/IoT work |

### 3–5 Notable Trend Highlights

1. **Emerging IoT‑Security Focus**  
   - The lead paper “**VEXAIoT: Autonomous IoT Vulnerability Exploitation using AI Agents**” signals a new sub‑trend: using autonomous agents to discover and exploit hardware‑level vulnerabilities.  This is the *first* IoT‑security‑centric title among the top‑10 this week, whereas last week’s leaders were all in pure LLM or scientific reasoning domains.

2. **From Pure LLM Reasoning to Multi‑Agent Coordination**  
   - Week 21’s top list emphasized *single‑agent* or “debate” dynamics (e.g., “What LLM Agents Say When No One Is Watching”).  
   - Week 22 pivots toward **formal coordination mechanisms**: “**Agora: Enhancing LLM Agent Reasoning Via Auction‑Based Task Allocation**” and “**Mosaic: Runtime‑Efficient Multi‑Agent Embodied Planning**” show growing interest in market‑style or planning‑centric orchestration for scalable agent fleets.

3. **Domain‑Specific Agentic Systems Gaining traction**  
   - New niche applications appear:  
     - **LLM for EDA** (electronic design automation) – bridging hardware CAD and LLM reasoning.  
     - **MicroGrowAgents** – applying agents to microbial cultivation engineering.  
   - In contrast, last week’s highlights were more “generic” (speaker recognition, open‑source ecosystem health). The shift indicates that the community is now testing agents in **high‑impact, domain‑specific pipelines**.

4. **Risk & Trust Frameworks Becoming Front‑Matter**  
   - “**TrustX Agent Risk Classification Framework (ARC)**” reflects rising concern over **internal safety, auditability, and tiered risk** of self‑generated agents. This safety‑first narrative was absent from the prior week’s top papers.

5. **Stability in overall output but diversification of venues**  
   - The total paper count rose only modestly (+1), yet the **topic distribution broadened** (IoT security, EDA, biotech, risk governance). This suggests that the field’s growth is now driven more by **horizontal expansion into new domains** rather than a vertical surge in sheer volume.

---



## Biomedical Highlights (1 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


**MicroGrowAgents: An Agentic AI System for Microbial Cultivation Engineering**

MicroGrowAgents introduces a closed‑loop, reinforcement‑learning‑driven framework that autonomously designs, executes, and refines microbial culture experiments to pinpoint optimal growth media, temperature, pH, and aeration settings. By coupling a language‑model‑based “agent” that proposes experimental conditions with a robotic liquid‑handling platform and real‑time optical‑density readouts, the system iteratively updates a surrogate model (Gaussian process) and uses Bayesian acquisition functions to balance exploration of untested conditions against exploitation of promising regions. Benchmarks on *Escherichia coli* and *Saccharomyces cerevisiae* demonstrated up‑to‑10‑fold reductions in the number of required experiments compared with traditional factorial designs while achieving comparable or higher biomass yields. The paper emphasizes the translational potential of agentic AI for high‑throughput strain engineering, bioprocess scale‑up, and rapid prototyping of microbial consortia for biotechnology applications.



### 1. MicroGrowAgents: An Agentic AI System for Microbial Cultivation Engineering

- **Authors:** Naseem, S., Miller, M. A., Martinez-Gomez, N. C., Sun, N., Joachimiak, M. P.
- **Published:** 2026-07-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.04.729985](https://doi.org/10.64898/2026.06.04.729985)

- **Categories:** synthetic biology


> The paper introduces **MicroGrowAgents**, a multi‑agent AI platform that fuses large‑scale biological knowledge graphs, genome annotations, metabolic models, and optimal experimental‑design theory to generate, test, and audit candidate microbial growth media in a fully traceable manner. Using 29 documented agents (58 skills) the system designed 70 media formulations for *Methylorubrum extorquens* AM1, experimentally screened them in quadruplicate, and applied Monte‑Carlo stability analysis to identify a Pareto‑optimal formulation (MPOB_058) that delivered ≈ 79 % more integrated biomass and ≈ 46 % faster growth than the standard medium, while transparently linking each recommendation to its provenance evidence. This work demonstrates that agentic AI can orchestrate heterogeneous domain knowledge with statistically efficient design to reduce wet‑lab workload and produce auditable, explainable hypotheses—an architecture the authors argue is readily transferable to other design‑build‑test‑learn cycles.


<details>
<summary>Abstract</summary>

Microbial cultivation optimization remains labor-intensive and inefficient, requiring extensive experimental screening to identify suitable growth conditions. Traditional one-factor-at-a-time approaches are particularly ineffective for exploring complex, multidimensional nutrient parameter spaces. We present MicroGrowAgents, an agent-assisted system for auditable design of candidate growth media through integration of knowledge graphs, metabolic modeling, and optimal experimental design. The system comprises 29 documented agents implementing 58 skills across seven functional categories that query structured biological knowledge (KG-Microbe: 864,363 validated species), Bakta-annotated genomes (667,000+ annotated features), curated organism-specific FACTS sheets, and a DOI-linked publication corpus, and apply this evidence to three ends: recommending candidate ingredients and concentration ranges, specifying the factors of a statistically optimal MaxPro experimental design, and interpreting cultivation outcomes against known biochemistry. We applied the approach to Methylorubrum extorquens AM1 (formerly Methylobacterium extorquens; reclassified per LPSN) by cultivating 69 designed media plus a default media baseline (70 total tested conditions) in quadruplicate and assessing two concurrent objectives: biomass turbidity (740 nm) and apparent residual-Nd depletion (residual Nd by arsenazo III). Monte-Carlo resampling of the replicate-level uncertainty (1000 iterations) identified MPOB_058 as the single MC-stable Pareto-optimal condition (membership frequency 0.922); paired-control biology analysis flags MPOB_058 as chemistry-confounded and nominates MPOB_008 as the cleaner biological-signal anchor (its lower abiotic-drift contribution to the residual-Nd measurement makes it the better candidate for confirming biological lanthanide handling in a follow-up round), with MPOB_019 borderline-stable, providing a prioritized anchor set for confirmation in subsequent rounds rather than a single declared optimum. The integration of chemical similarity search (208,000+ embeddings), metabolic gap analysis, and multi-modal reasoning enables evidence-based hypothesis generation that reduces experimental burden while accelerating discovery of growth-promoting conditions. On the Biolog Odin platform, the MC-stable composite candidate MPOB_058 grew 79% more integrated biomass (area under the 740 nm growth curve) and 46% faster (maximum specific growth rate _max; Gompertz fits, R{superscript 2} > 0.99) than the standard MP base medium for this organism (the unsupplemented starting-point recipe carried as the on-plate control). This biomass and growth-rate advantage is a direct kinetic measurement; the conditions apparent residual-Nd depletion ranking, by contrast, awaits confirmation in a subsequent round, because MPOB_058s apparent Nd depletion is partly abiotic. Unlike general-purpose AI co-scientists, MicroGrowAgents grounds every recommendation in inspectable evidence -- structured provenance manifests with per-session input checksums, schema- and ontology-validated outputs, and 90.5% literature citation coverage (143 of 158 curated DOIs with evidence-supports-claim verification) -- separating deterministic design and analysis from agentic interpretation so that recommendations are transparent, explainable, and auditable, while passing 7 of 9 bbop-skills agentic-system criteria in a Claude-Code self-audit (the two unmet criteria are MCP-standardized tool exposure and full input-data cryptographic hashing, both tracked roadmap items).

The Bigger PictureIdentifying growth conditions for poorly characterized microbes is one specific instance of a recurring problem in the natural sciences: how to integrate heterogeneous prior knowledge -- structured databases, published literature, mechanistic models -- with statistically efficient experimental design so that limited wet-lab time is spent where it most reduces the search. We show that a multi-agent AI system can perform that integration from organism input to wet-lab design, with every recommendation traceable from its source evidence through to the experimental design that tested it. The same architecture (specialized agents over structured knowledge bases, mechanistic models, and statistical design, with checksummed provenance recorded as the unit of evidence) is in principle transferable to other DBTL loops against under-explored search spaces such as catalyst discovery, materials formulation, cell-line engineering, drug-combination screens, or environmental remediation. We demonstrate it here only for microbial cultivation and flag cross-domain transfer as future work rather than a demonstrated capability. Our cultivation results on Methylorubrum extorquens AM1 are a concrete demonstration that this pattern works on real laboratory data: an uncertainty-aware shortlist of candidate media emerged from Monte-Carlo stability analysis of two competing objectives, with the leading composite candidate growing 79% more integrated biomass and 46% faster than the standard MP base medium for this organism; this biomass and growth-rate advantage is directly measured, while its apparent residual-Nd depletion advantage awaits confirmation in a subsequent round, since the apparent Nd depletion is partly abiotic. But the lesson we want to port across research domains is the architecture and its provenance discipline, not the specific organism. MicroGrowAgents is released under BSD-3 with checksummed YAML provenance manifests so that any group adopting these agents inherits a workflow designed to be re-runnable from its recorded inputs.

</details>


---



## Arxiv (148 papers)


### 1. VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents

- **Authors:** Katherine Swinea, Kshitiz Aryal, Lopamudra Praharaj, Maanak Gupta
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09653v1](http://arxiv.org/abs/2607.09653v1)
- **PDF:** [https://arxiv.org/pdf/2607.09653v1](https://arxiv.org/pdf/2607.09653v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **VEXAIoT**, a novel autonomous multi‑agent framework that couples LLM‑driven reasoning with traditional offensive‑security tools to discover and exploit IoT‑specific flaws. By assigning a *vulnerability‑detection* agent to perform reconnaissance and a separate *attack‑execution* agent to plan and run exploits, the system autonomously navigates IoT testbeds (IoTGoat and Metasploitable2) across ten OWASP‑IoT attack scenarios. In 260 trial runs, VEXAIoT attains a **95 % overall success rate** (up to 100 % in individual scenarios) while keeping token usage low and completing most attacks in under two minutes, demonstrating that LLM‑powered agents can reliably automate end‑to‑end IoT vulnerability assessment and exploitation in controlled environments.


<details>
<summary>Abstract</summary>

Internet of Things (IoT) systems are inherently vulnerable due to constrained hardware, outdated firmware, and insecure default configurations, creating a need for scalable and adaptive security testing approaches. While recent adoptions of Large Language Model (LLM) agents have demonstrated promise in penetration testing and Capture-the-Flag (CTF) environments, their application to IoT specific vulnerabilities remains unexplored. This paper presents an autonomous multi-agent framework, referred to as Vulnerability EXploitation using AI Agents (VEXAIoT), for vulnerability discovery and exploitation in IoT environments using LLM-based reasoning and offensive security tools. The framework combines a vulnerability detection agent and an attack execution agent to perform reconnaissance, plan attack sequences, and execute exploits against vulnerable IoT services. The system is evaluated in IoTGoat and Metasploitable environments across ten attack scenarios mapped to OWASP IoT vulnerabilities. Experimental results show attack success rate of up to 100% with low token overhead and average execution times under two minutes for most attacks. Across 260 attack executions, VEXAIoT achieves a 95.0% overall success rate, including 94.5% success in IoTGoat and 96.7% success in Metasploitable2. These results demonstrate the potential for LLM-driven agents to automate IoT vulnerability assessment and offensive security workflows in controlled environments

</details>


### 2. LLM for EDA in Front-End Design: Challenges and Opportunities

- **Authors:** Kangwei Xu, Bing Li, Ulf Schlichtmann
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09616v1](http://arxiv.org/abs/2607.09616v1)
- **PDF:** [https://arxiv.org/pdf/2607.09616v1](https://arxiv.org/pdf/2607.09616v1)
- **Categories:** cs.ET, cs.AR, cs.LG, eess.SY


> **Main contribution:** The paper surveys how large language models (LLMs) can evolve from passive assistants to autonomous, agentic components in electronic‑design‑automation (EDA) front‑end flows, outlining a roadmap—exemplified by systems such as OpenClaw—for a unified, AI‑driven interface that handles HDL synthesis, test‑bench creation, and design‑space exploration.

**Methodology:** The authors review recent LLM‑based techniques for front‑end tasks (specification parsing, circuit and testbench generation, high‑level synthesis optimization), contrast them with emerging agentic architectures that embed planning, memory, and tool‑use loops, and then systematically analyze technical bottlenecks (prompt fragility, verification safety, tool integration, and data scarcity).

**Key findings for agentic AI:** Demonstrations show that LLM‑augmented agents can generate correct HDL and testbenches from high‑level specs and iteratively improve synthesis results, but current systems still suffer from reliability, interpretability, and scalability issues. The paper highlights that overcoming these challenges—through better grounding, formal verification hooks, and multimodal tool orchestration—will be crucial for deploying truly autonomous AI agents in front‑end chip design.


<details>
<summary>Abstract</summary>

As chip complexity increases and time-to-market pressures grow, front-end design has become a critical bottleneck in chip development. Recently, Large Language Models (LLMs) have shown great potential in Electronic Design Automation (EDA). Beyond specification understanding, LLMs show the potential to serve as a unified intelligent interface for hardware description language (HDL) generation, testbench construction, and design space exploration. The rise of agentic AI, represented by pioneering systems such as OpenClaw, offers a strategic roadmap for the next generation EDA. From this perspective, this paper discusses the evolution of EDA from localized assistance to autonomous agentic execution. Then, we review representative advances of LLMs in front-end design, focusing on key tasks such as circuit and testbench generation from a shared specification, as well as design quality improvement in established workflows such as high-level synthesis. Finally, we discuss the key challenges and limitations of integrating LLMs into EDA, and outline future opportunities for advancing LLM-enabled front-end design, offering a systematic perspective for researchers interested in leveraging agentic AI technologies for EDA.

</details>


### 3. Mosaic: Runtime-Efficient Multi-Agent Embodied Planning

- **Authors:** Kunjal Panchal, Saayan Mitra, Sunav Choudhary, Victor Bursztyn, Somdeb Sarkhel, Hui Guan
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09603v1](http://arxiv.org/abs/2607.09603v1)
- **PDF:** [https://arxiv.org/pdf/2607.09603v1](https://arxiv.org/pdf/2607.09603v1)
- **Categories:** cs.MA


> Mosaic tackles the latency bottleneck of LLM‑driven multi‑agent embodied planning by (1) introducing an agent‑centric semantic memory that tracks objects in relative coordinates for lightweight, accurate state estimation under partial observability, and (2) formulating a per‑step Integer Linear Programming allocation that enforces physical feasibility and inter‑agent coordination constraints. Experiments on AI2‑THOR and a search‑and‑rescue suite show that this combination cuts execution time by 27–32 %, reduces LLM calls by 30–33 % and planning steps by 25–31 %, while improving success rates by 4–10 % points. The results highlight that efficient geometric memory and constraint‑guided coordination are key enablers for scalable, low‑latency agentic AI systems.


<details>
<summary>Abstract</summary>

LLM-based multi-agent embodied planning remains impractical due to prohibitively high execution latency. We identify failed actions as the dominant bottleneck, stemming from two core challenges: inaccurate state tracking under partial observability and inefficient coordination that produces redundant or conflicting actions. We introduce Mosaic, a runtime-efficient multi-agent planning framework that addresses both challenges. Mosaic maintains accurate yet lightweight state tracking through agent-centric semantic memory that stores objects in relative coordinates, enabling geometric transformations and coordination. It ensures efficient coordination through Integer Linear Programming that allocates actions at every planning step, enforcing physical feasibility and inter-agent coordination constraints. Across AI2-THOR and search-and-rescue benchmarks, Mosaic achieves 27-32% faster execution, 30-33% fewer LLM calls, 25-31% fewer steps, and 4-10% points higher success rates. These results demonstrate that efficient memory and constraint-guided coordination are critical for scalable, low-latency multi-agent planning.

</details>


### 4. Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation

- **Authors:** Kaiji Zhou, Ales Leonardis, Yue Feng
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09600v1](http://arxiv.org/abs/2607.09600v1)
- **PDF:** [https://arxiv.org/pdf/2607.09600v1](https://arxiv.org/pdf/2607.09600v1)
- **Categories:** cs.AI, cs.CL


> **Main contribution:** The paper introduces **Agora**, a novel orchestration layer for LLM‑based agents that casts each reasoning sub‑step as an item in an incentive‑compatible auction, allowing multiple expert LLMs and external tools to bid based on a rectified competence estimate rather than simple API‑matching.  

**Methodology:** Agora computes a performance‑adjusted score for every candidate model/tool (derived from validation data and confidence calibration), lets them submit bids on incoming reasoning tasks, and selects the winner through a Vickrey‑style auction; a single tunable parameter controls the trade‑off between expected solution quality and monetary/computational cost.  

**Key findings:** Across five diverse reasoning benchmarks, Agora consistently outperforms strong baselines—including single‑model selection, heuristic routing, and cascade pipelines—while offering a transparent knob to balance cost and accuracy, demonstrating that auction‑based allocation can substantially improve the effectiveness and efficiency of agentic AI systems.


<details>
<summary>Abstract</summary>

Enhancing the reasoning capabilities of large language model (LLM) agents requires effective orchestration of diverse expert models and tools. However, existing frameworks typically call APIs based on coarse-grained matching between tasks and the functions of expert models or tools, while overlooking critical factors such as performance variability and cost efficiency among functionally similar alternatives. To address this, we propose Agora, a framework that introduces an incentive-compatible auction mechanism for dynamically allocating tasks to expert models and tools. By treating reasoning steps as tradeable items, Agora enables agents to bid based on their rectified competence-ensuring that critical logic is routed to the most capable solver rather than the most overconfident one. Evaluations across five benchmarks show that Agora improves over matched single-model, routing, and cascade baselines under comparable candidate pools, while exposing a controllable cost-quality trade-off through a single auction parameter.

</details>


### 5. TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems

- **Authors:** Hannah M. Liu, Rhea Saxena, Shiv Asthana
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09586v1](http://arxiv.org/abs/2607.09586v1)
- **PDF:** [https://arxiv.org/pdf/2607.09586v1](https://arxiv.org/pdf/2607.09586v1)
- **Categories:** cs.AI


> The paper presents **TrustX’s Agent Risk Classification (ARC) framework**, a systematic tool for rating the risk of internally built agentic AI systems across seven common use‑cases.  ARC combines a **12‑dimension quantitative rubric** with the **GPA + IAT classification model** and a **five‑level autonomy taxonomy** to generate a **three‑tier risk tier (low‑medium‑high)** together with concrete governance controls, and it even includes a custom Coding‑Assistant module for code‑centric agents.  Demonstrations on a representative agent show that the framework can consistently differentiate risk levels and map them to actionable mitigation measures, offering a repeatable, governance‑ready approach for risk officers, developers, and regulators in the emerging agentic‑AI landscape.


<details>
<summary>Abstract</summary>

The proliferation of agentic AI systems across enterprise and public-sector contexts has outpaced the capacity of general-purpose AI risk frameworks to classify and govern them. In this paper, we introduce the TrustX Agent Risk Classification Framework, a structured, repeatable instrument that can be applied to seven types of agentic AI systems and is grounded in foundational pre-existing AI governance frameworks. At the core of the framework is a twelve-dimension scoring rubric that robustly quantifies the risk. This rubric is combined with other components, such as the GPA + IAT classification model and the five-level autonomy framework derived from existing literature. These inputs produce a three-tier governance output with mapped control recommendations. A specialised Coding Assistant extension is also included to account for nuances specific to this type of agentic AI system. We then use an illustrative example to show our framework in practice. ARC is intended for AI governance practitioners, risk officers, developers, and regulators, and it will regularly undergo iteration as we continue to expand it and make it more robust. The community can access the interactive framework here: https://arc.responsible.ai/

</details>


### 6. Shared Selective Persistent Memory for Agentic LLM Systems

- **Authors:** Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09493v1](http://arxiv.org/abs/2607.09493v1)
- **PDF:** [https://arxiv.org/pdf/2607.09493v1](https://arxiv.org/pdf/2607.09493v1)
- **Categories:** cs.AI, cs.MA, cs.SE


> The paper introduces **Shared Selective Persistent Memory (SSPM)**, an architecture that‑​instead of storing full conversation logs for agentic LLMs‑​selectively retains only reusable artefacts (task specs, data schemas, tool configurations, and output constraints) and shares them across users via role‑based workspaces. By integrating SSPM into a collaborative coding platform and coupling it with a zero‑token data‑refresh layer that decouples generated code from live data, the authors show that agents complete 96 % of enterprise tasks (vs. 79 % without memory and 71 % with naïve full‑history persistence), cut per‑invocation token usage by 97 ×, and reduce update latency by 14 ×; the approach also generalizes to public benchmarks, succeeding in all 12 zero‑token refresh trials.


<details>
<summary>Abstract</summary>

Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality. We introduce shared selective persistent memory, an architecture that identifies and retains four categories of reusable context (task specifications, data schemas, tool configurations, and output constraints) while discarding session-specific reasoning traces. Crucially, this memory is shared: workspaces encapsulating selective memory can be transferred across users with role-based access control, enabling collaborative reuse without redundant specification. We implement it in a deployed collaborative workspace platform where LLM agents produce, edit, and maintain git-versioned artifacts (dashboards, reports, and data-driven documents) from heterogeneous sources (CSV, SQL, REST APIs, and MCP servers). A complementary zero-token data refresh mechanism decouples generated programs from runtime data, enabling artifact reuse without re-invocation. Across three enterprise scenarios, shared selective persistent memory achieves 96% task completion (vs. 79% without memory and 71% with full history). Zero-token refresh eliminates LLM re-invocation for recurring updates (14x task-time reduction), while summary-driven generation cuts per-invocation token cost by 97x versus raw data injection. A replication on four public datasets confirms generalizability, with zero-token refresh succeeding in 12/12 trials. Notably, naive full-history persistence actively degrades completion by biasing the agent with stale traces, while selective memory outperforms both extremes.

</details>


### 7. ProofCouncil: An LLM Agent for Solving Open Mathematical Problems

- **Authors:** Johannes Schmitt, Tim Gehrunger, Jasper Dekoninck, Gergely Bérczi, Uri Kreitner, Liam Price, David Holmes
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09474v1](http://arxiv.org/abs/2607.09474v1)
- **PDF:** [https://arxiv.org/pdf/2607.09474v1](https://arxiv.org/pdf/2607.09474v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **ProofCouncil**, an autonomous LLM‑based mathematical agent built around an **author‑critic (or “council”) architecture** that iteratively drafts and refines proof attempts, and releases the underlying agent‑building library as open‑source.  

**Methodology:** ProofCouncil decomposes each open problem into a sequence of claim‑generation, proof‑drafting, and self‑critique steps; the “author” LLM produces candidate arguments while a separate “critic” LLM evaluates logical validity, requests revisions, and orchestrates a multi‑turn dialogue until convergence, all managed by a lightweight workflow engine.  

**Key findings:** In the FirstProof II benchmark (10 real‑world problems), ProofCouncil achieved correct (or minor‑revision) solutions for **6 problems**, the best score among all teams, and on a curated set of 30 researcher‑submitted problems it produced **5 fully correct proofs**, **2 promising drafts**, and **8 useful partial results** out of 21 evaluated, demonstrating that an author‑critic agentic loop substantially improves LLM performance on open mathematical reasoning tasks.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have shown increasing promise in solving open problems in mathematics. However, their performance can be further improved through agentic workflows tailored to real-world mathematical practice. To this end, we introduce ProofCouncil, a mathematical agent that is designed to tackle open problems using an author-critic architecture. ProofCouncil served as a submission to the second batch of FirstProof, a challenge consisting of 10 real-world mathematical problems that agents must solve autonomously. Its submissions for 6 of the 10 problems were judged by the referees to be correct up to at most minor revisions, showing the best performance among participating teams. We also evaluate ProofCouncil on 30 open problems collected from mathematical researchers. Among the 21 solutions that received human feedback, 5 were judged completely correct, 2 more were judged promising pending final verification, and a further 8 contained useful partial progress. In this short paper, we describe the development of ProofCouncil and the agent-building library used to create it, which we release as open source to the community.

</details>


### 8. Action-Factored Multi-Agent Reinforcement Learning for Scalable Quantum Device Tuning

- **Authors:** Edwin De Nicolo, Rahul Marchand, Cornelius Carlsson, Pranav Vaidhyanathan, Natalia Ares
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09422v1](http://arxiv.org/abs/2607.09422v1)
- **PDF:** [https://arxiv.org/pdf/2607.09422v1](https://arxiv.org/pdf/2607.09422v1)
- **Categories:** cs.LG, cond-mat.mes-hall


> The paper introduces **QADAPT**, a factored‑action multi‑agent reinforcement‑learning framework that learns a shared, locally‑conditioned policy for tuning electrostatically defined quantum‑dot arrays. By online learning of a factorized action representation, the agents are decoupled, reducing non‑stationarity caused by cross‑talk and enabling efficient, modular coordination based solely on local measurements and rewards. Experiments show that QADAPT scales to larger devices with near‑zero‑shot generalization and requires roughly the same number of convergence steps regardless of array size, demonstrating a practical pathway for rapid, scalable calibration of quantum processors.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning is well suited to problems with large parameter spaces and exploitable local structure, such as the tuning of electrostatically-defined quantum-dot arrays. However, if parameter cross-talk is strong, a non-stationary environment from the perspective of any individual agent can destabilize learning - the same effect that plagues manual tuning of such systems. We propose using a factored representation of the action space, learned online, to decouple agents and minimize their interference. Our framework, QADAPT, uses this factorization to efficiently learn shared policies based on local measurements and rewards. With this modular strategy, we achieve zero-shot generalization to unseen quantum device sizes and maintain an approximately constant number of convergence steps to reach target regimes. This work provides a scalable route toward the rapid calibration of large-scale quantum processors.

</details>


### 9. Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review

- **Authors:** Jingbo Chen, He Wang, Wei Yuan, Yuqiao Lai, Zhenyan Lu
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09403v1](http://arxiv.org/abs/2607.09403v1)
- **PDF:** [https://arxiv.org/pdf/2607.09403v1](https://arxiv.org/pdf/2607.09403v1)
- **Categories:** cs.AI


> The paper introduces **AutoWorldBuilder**, a multi‑agent framework that lets large language models collaboratively construct coherent fictional worlds while keeping the prompt size bounded and ensuring quality. Its architecture combines (1) a structured concept‑graph with automatic conflict detection, (2) a DAG‑based batch scheduler that groups semantically related generation tasks, (3) a four‑layer hierarchical context‑compression pipeline that cuts token usage by ~90 %, and (4) an iterative review loop staffed by specialized Auditor agents that raise proposal acceptance from 42 % to >85 %. In experiments on 20 world‑building benchmarks using GPT‑OSS‑120B and DeepSeek‑v3.2, the system achieved a 95 % overall success rate, producing 56‑103 internally consistent concepts per world in under 30 minutes with zero conflicts, demonstrating that hierarchical compression, semantic‑locality scheduling, and separate generation/review agents can reliably scale knowledge‑intensive, multi‑agent LLM tasks.


<details>
<summary>Abstract</summary>

Worldbuilding, the construction of coherent fictional worlds, is a foundational task in game design and literary creation. Large Language Models (LLMs) offer new possibilities for automated content generation, but their application to worldbuilding faces three challenges: context explosion that grows linearly with the building process, the tension between creative diversity and content consistency, and the absence of automated quality assurance. This paper presents AutoWorldBuilder, a multi-agent collaborative system that addresses these challenges through five integrated components: a structured concept network with conflict detection; a DAG-based hybrid batch scheduler that groups tasks by semantic locality; a four-layer context compression mechanism achieving approximately 90% token reduction; an iterative review system with specialized Auditor agents that improves proposal pass rates from 42% to over 85%; and a skill-driven agent architecture supporting zero-code extension with differentiated temperature configuration. Two experiments across 20 diverse worldbuilding tasks, using GPT-OSS 120B and DeepSeek v3.2 as LLM backends, demonstrate a 95.0% success rate. The system generated 56-103 self-consistent concepts per world in 18-31 minutes with zero-conflict delivery. The architectural patterns validated here, including layer-as-budget compression, semantic-locality scheduling, and separation of generation and review, transfer to the broader class of knowledge-intensive, multi-agent LLM applications.

</details>


### 10. Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents

- **Authors:** Izumi Takahara, Teruyasu Mizoguchi
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09195v1](http://arxiv.org/abs/2607.09195v1)
- **PDF:** [https://arxiv.org/pdf/2607.09195v1](https://arxiv.org/pdf/2607.09195v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci


> The paper introduces the **Hypothesis Evolution Protocol (HEP)**, a lightweight harness that transforms an LLM‑based scientific agent from a black‑box predictor into an auditable “AI scientist” by exposing hypothesis generation, experimental testing, and belief‑updating as explicit, logged operations. HEP is implemented as a set of structured API calls that the agent invokes during a hypothesis→test→evidence→belief cycle, and its effectiveness is demonstrated on multiple materials‑science discovery benchmarks where the HEP‑enabled agent consistently proposes viable hypotheses, evaluates them with tools (e.g., simulators), and revises its internal state in a way that scales with the underlying LLM’s capability. The results show that the protocol yields transparent, reproducible scientific reasoning, improves generalization across questions, and provides a tractable audit trail for human verification and further iteration.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly expected to play a central role in AI-driven scientific discovery. Equipped with broad knowledge, flexible reasoning, and tool use, they have the potential to autonomously explore and solve scientific problems by repeatedly proposing hypotheses, testing them, and revising their beliefs in the light of the evidence. In current agents, however, these hypotheses, tests, and belief updates are buried in unstructured logs, and no mechanism lets the agent or the human researcher audit that process. Here we propose the Hypothesis Evolution Protocol (HEP), an agent harness that provides hypothesis generation, evaluation, and evolution as explicit, auditable operations. On materials-science research tasks, a HEP-equipped agent operates the hypothesis--test--evidence--belief cycle that planning-style agents lack, generalizes across research questions, and exploits the protocol more fully as the base LLM becomes more capable. These results mark a step toward auditable AI scientists, whose scientific reasoning can be inspected, verified, and built upon.

</details>


### 11. Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift

- **Authors:** Dan C. Hsu, Luke Lu
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09175v1](http://arxiv.org/abs/2607.09175v1)
- **PDF:** [https://arxiv.org/pdf/2607.09175v1](https://arxiv.org/pdf/2607.09175v1)
- **Categories:** cs.AI, cs.CL


> The paper introduces **Graph‑Regularized Agentic Context Evolution (GRACE)**, a framework that stores the mutable, system‑level instruction of a deployed LLM agent as a typed semantic graph instead of flat text, enabling local verification of updates by checking typed neighborhoods before committing them as incremental edits to the deployed textual checkpoint. Using a fixed telecom‑agent harness and a controlled distribution‑shift protocol derived from τ²‑bench, GRACE was shown across five replications to raise the strict reliability metric pass³ from the Gemini 2.5 Flash zero‑shot baseline of 0.091 to 0.673 ± 0.136—well above both a Gemini 3.1 Pro zero‑shot reference (0.242) and a flat‑text HCE baseline (0.191 ± 0.051). The results demonstrate that a graph‑structured context substrate combined with incremental consolidation is essential for dependable long‑horizon agentic context evolution under distribution shift.


<details>
<summary>Abstract</summary>

Deployed LLM agents rely on agentic context, the model-external textual control content assembled by an operational harness. In this work, the mutable component of that context is a persistent system-level instruction that is updated from operational experience while the model, tools, and harness remain fixed. Over long evolution horizons, flat-text maintenance makes verification increasingly difficult as accumulated instructions grow and interact. We propose Graph-Regularized Agentic Context Evolution (GRACE), which maintains the persistent instruction component as a typed semantic graph and validates proposed updates within the local typed neighborhoods of modified nodes. Accepted graph updates are reconstructed as incremental edits to the textual instruction checkpoint used at deployment. We evaluate GRACE within a fixed telecom agent harness derived from $τ^2$-bench under a controlled distribution-shift protocol. Across five independent replications, GRACE improves strict reliability, measured by pass^3, from the Gemini 2.5 Flash zero-shot value of 0.091 to 0.673$\pm$0.136 at the final checkpoint. This exceeds a Gemini 3.1 Pro zero-shot reference of 0.242 on the same held-out set, while the flat-text HCE baseline finishes at 0.191$\pm$0.051. These results identify two requirements for reliable long-horizon context evolution, a structural substrate that makes verification local and a consolidation mechanism that keeps accumulated instruction content usable.

</details>


### 12. Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering

- **Authors:** Lucas Pinto
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09156v1](http://arxiv.org/abs/2607.09156v1)
- **PDF:** [https://arxiv.org/pdf/2607.09156v1](https://arxiv.org/pdf/2607.09156v1)
- **Categories:** cs.LG


> **Main contribution**  
The paper provides the first systematic analysis of how additive activation‑steering vectors—directions injected into the residual stream to bias a language model’s behavior—transfer from single‑turn chat settings to multi‑turn ReAct tool‑using agents. It shows that while the steering signal reaches the model’s late layers with almost unchanged magnitude, its behavioral effect is **rescaled** (either amplified or attenuated) depending on the model architecture and the ReAct scaffolding.

**Methodology**  
The authors evaluate matched pairs of inputs rendered as plain chat or as a full ReAct episode, inject calibrated steering directions (including a refusal‑bypass vector), and re‑encode each turn to avoid KV‑cache leakage. They compare activation read‑outs, conduct directional ablations, and use two pre‑registered measurement instruments to isolate where the rescaling occurs (the ReAct format scaffold rather than tool observation).

**Key findings for agentic AI**  
* The install‑site‑over‑chat activation ratios are near‑unity (0.83–1.16) across three model families, confirming that the steering signal itself is preserved.  
* Behavioral coupling varies widely: on Qwen2.5‑7B the refusal‑bypass vector is amplified by ~1.45×, on Gemma‑2‑9B by 2.00×, but on Yi‑1.5‑9B it is attenuated to ~0.43×, with no universal scaling factor.  
* Additive injection, not the direction itself, drives amplification (additive vs. ablative contrast yields a 20‑point gain).  
* The rescaling originates from the ReAct episode scaffold before any tool observation, contradicting a simple dilution hypothesis.  

**Implication**  
Deploying LLMs as tool‑using agents can unpredictably magnify or diminish additive steering effects, meaning safety guarantees derived from chat‑only calibrations do not reliably hold for agentic deployments.


<details>
<summary>Abstract</summary>

Additive activation steering (injecting a scaled residual-stream direction during generation) is calibrated almost entirely in single-turn chat, yet the models it targets are increasingly deployed as tool-using ReAct agents. We present the first systematic chat-to-agent transfer study of additive steering, coupling behavioral measurement with a representation read-out in a matched-information design: the same items rendered as plain chat or as a ReAct tool-use episode, with matched-norm random-direction controls and the transcript re-encoded every turn to exclude KV-cache contamination. Transfer is real but rescaled, and the right description is a dissociation: the injected direction reaches the late layers at near-full strength in every setting and model tested (install-site agent-over-chat ratios 0.83-1.16 across three families), while the behavioral coupling is reset per model and context. On Qwen2.5-7B a refusal bypass vector amplifies in the agent (T = 1.45, CI [1.20, 1.78], N = 300); across a powered uniform-protocol distribution the coupling spans amplification (Gemma-2-9B T = 2.00) to attenuation (Yi-1.5-9B T = 0.43, CI [0.29, 0.60]), with no universal constant and a single clean attenuator against a universal sign. Directional ablation of the same axis does not amplify (T = 0.93, CI including 1) while additive injection amplifies (T = 1.50), a 20.1-point gain difference (CI [13.4, 26.8]) that identifies an additive-specific mechanism. Two pre-registered instruments converge to localize the rescaling to the ReAct format scaffold, before any tool observation, rather than to the observation boundary where a dilution account would predict it. The safety implication is immediate and unpredictable: agentic deployment amplifies steering-based refusal bypass by up to 2.00x on some models while others attenuate, so a deployment cannot assume a given model is safe under additive steering.

</details>


### 13. KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling

- **Authors:** Peng Kuang, Haibo Jin, Xiaoyu Han, Yanli Wang, Xiaopeng Yuan, Ye Yu, Kaidi Xu, Haohan Wang
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09153v1](http://arxiv.org/abs/2607.09153v1)
- **PDF:** [https://arxiv.org/pdf/2607.09153v1](https://arxiv.org/pdf/2607.09153v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **KV‑PRM**, a process‑reward model that scores multi‑agent trajectories by directly reusing the key‑value (KV) cache generated during LLM inference, eliminating the need to re‑encode the entire text history.

**Methodology:** KV‑PRM appends a single “verify” token to the existing KV cache and computes the reward from this cache, reducing the computational complexity of reward evaluation from \(O(L^{2})\) (full re‑encoding) to \(O(L)\). The authors prove that the KV cache retains more information than the raw text and is therefore a superior substrate for downstream reward modeling.

**Key findings:** Across MATH, GSM8K, and AIME benchmarks and under several test‑time scaling (TTS) strategies (Beam Search, MCTS, Weighted Voting), KV‑PRM matches or exceeds the performance of conventional text‑based PRMs while achieving up to **5,000× fewer FLOPs**, **37× lower latency**, and **34× smaller per‑sequence memory**. This makes high‑fidelity reward modeling feasible for long‑context, multi‑agent LLM deployments.


<details>
<summary>Abstract</summary>

Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-agent rollouts, the scoring cost, growing quadratically with respect to sequence length L, creates a severe computational bottleneck, severely limiting PRMs' application in long-context scenarios. To resolve this, we introduce KV-PRM, a highly efficient process reward model that eliminates the heavy text re-encoding by directly reading the KV cache produced naturally during the LLM's generation phase. By processing a single "verify token" against the pre-existing KV cache, KV-PRM reduces the scoring cost from O(L^2) to O(L). We formally prove that the KV cache contains strictly greater information capacity than text, and is more efficient for downstream reward modeling. Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.

</details>


### 14. L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning

- **Authors:** Tan-Minh Nguyen, Hoang-Trung Nguyen, Huu-Dong Nguyen, Dinh-Truong Do, Thi-Hai-Yen Vuong, Le-Minh Nguyen
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09099v1](http://arxiv.org/abs/2607.09099v1)
- **PDF:** [https://arxiv.org/pdf/2607.09099v1](https://arxiv.org/pdf/2607.09099v1)
- **Categories:** cs.AI


> The paper introduces **Legal Multi‑Agent Debate (L‑MAD)**, a systematic framework that pits several expert‑persona agents against each other to solve Legal Textual Entailment tasks and aggregates their arguments with various voting and confidence‑weighting schemes. By experimentally comparing debate topologies (pairwise, pool, hierarchical) and aggregation methods, the authors show that a modestly sized pool (4–6 agents) consistently outperforms the strongest single‑agent baselines by up to **8 % accuracy**, while longer multi‑round discussions cause an “over‑deliberation drift” that degrades performance. These results delineate a practical trade‑off—more agents improve consistency and safety, but additional deliberation rounds can amplify shared errors—providing concrete guidance for deploying safe, collaborative agentic AI in high‑stakes legal reasoning contexts.


<details>
<summary>Abstract</summary>

While multi-agent debate (MAD) frameworks have shown significant potential in general reasoning, their effectiveness in highly structured, knowledge-heavy legal domains remains under-explored. In this work, we introduce the Legal Multi-Agent Debate (L-MAD) framework to systematically evaluate different debate structures and aggregation methods within Legal Textual Entailment. By assigning distinct expert personas to multiple agents, L-MAD improves upon strong single-agent baselines by up to 8\%. Furthermore, analyzing how debate scales reveals a clear trade-off: increasing the agent population reduces inconsistency and improves accuracy, whereas extending discussion rounds induces a detrimental \textit{over-deliberation drift} where agents reinforce each other's mistakes. Ultimately, our findings outline the practical boundaries and safety margins of deploying collaborative multi-agent systems in high-stakes legal reasoning environments.

</details>


### 15. Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls

- **Authors:** Saroj Gopali, Bipin Chhetri, Deepika Giri, Sima Siami-Namini, Akbar Siami Namin
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09076v1](http://arxiv.org/abs/2607.09076v1)
- **PDF:** [https://arxiv.org/pdf/2607.09076v1](https://arxiv.org/pdf/2607.09076v1)
- **Categories:** cs.AI


> The paper presents **Neuro‑Agentic Control**, a novel agentic AI architecture that safely integrates an LLM planner with a time‑series foundation model (TimesFM) to protect industrial IoT systems. By injecting each LLM‑suggested mitigation into the latent space of TimesFM—its **Counterfactual Physics Injection** step—the framework predicts the physical consequences of an action before execution, discarding any hallucinatory or unsafe moves. Experiments on the Secure Water Treatment (SWaT) testbed show that this neuro‑agentic loop blocks 33 % of attacks (five out of fifteen) while executing zero physically invalid actions, outperforming LSTM (26.7 %) and TCN (13.3 %) baselines and demonstrating how foundation‑model “sentinels” can render LLM‑driven agents trustworthy for critical‑infrastructure control.


<details>
<summary>Abstract</summary>

Cyberattacks on operational technology are increasingly causing costly downtime and physical damage, exposing the limitations of traditional rule-based monitoring in industrial IoT environments. While Large Language Models (LLMs) have strong semantic reasoning abilities to assist in decision support, their hallucinatory nature presents unacceptable safety liabilities for closed-loop control. This paper introduces a neuro-agentic control framework, a novel architecture that couples an LLM-based planner (i.e., such as Gemini 2.5 Flash-Lite) with a pre-trained Time-Series Foundation Model (TimesFM), to achieve physics-grounded autonomous defense. The paper introduces a ``Counterfactual Physics Injection'' mechanism that simulates the impact of LLM-proposed interventions within the numerical latent space of the foundation model before actuation, while allowing the system to reject hallucinatory or unsafe actions. Evaluated on an industrial dataset (e.g., the Secure Water Treatment (SWaT)) in the context of stochastic attack scenarios, the framework exhibited better performance compared to LSTM and TCN baselines. The Neuro-Agentic Loop prevented five breaches (33.3%) below the threshold versus LSTM (26.7%) and TCN (13.3%), with zero physically invalid (hallucinated) actions executed. These results demonstrate the efficacy of using foundation models as deterministic ``Sentinels'' to safeguard agentic AI in critical infrastructure.

</details>


### 16. Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills

- **Authors:** Jialun Cao, Xinru Yan, Songqiang Chen, Yaojie Lu, Zhongxin Liu, Shing-Chi Cheung
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09065v1](http://arxiv.org/abs/2607.09065v1)
- **PDF:** [https://arxiv.org/pdf/2607.09065v1](https://arxiv.org/pdf/2607.09065v1)
- **Categories:** cs.SE, cs.AI


> The paper delivers the first large‑scale, activity‑centric analysis of software‑engineering (SE) “skills” that are being packaged and shared in public AI‑agent repositories and marketplaces. By mining thousands of skill definitions, the authors classify the encapsulated SE tasks, map them to stages of the software development lifecycle, and track their evolution and evaluation practices; they find that a growing share of concrete SE activities—from code generation and bug detection to testing and deployment—are already being offered as reusable agent skills, though many high‑context tasks remain uncovered. These results highlight a concrete opportunity for the agentic‑AI community to build recommendation systems, structured skill taxonomies, and richer encapsulation mechanisms that enable systematic reuse of SE expertise within autonomous agents.


<details>
<summary>Abstract</summary>

Software engineering (abbrev. SE) has continuously evolved through increasingly powerful forms of reuse, from source code and libraries to components and services. Recent advances in AI agents have introduced a potentially new reusable artifact: skills. Emerging agent skill repositories and marketplaces enable developers to package, share, and reuse SE expertise as reusable skills. This trend raises a fundamental question: what SE activities are being encapsulated into reusable skills? Existing studies primarily focus on a broad range of skills acquisition, safety, or benchmarking, while lacking a systematic understanding of SE-specific skills and their coverage across the software development lifecycle. To address this gap, we conduct the first large-scale empirical study of SE skills in public repositories and marketplaces. We collect and analyze a large corpus of SE skills, examining the activities they encapsulate, lifecycle coverage, evolution characteristics, and evaluation mechanisms. Our findings reveal that SE activities are increasingly becoming reusable artifacts via skills and suggest promising research opportunities for skill recommendation and engineering-oriented structuring, as well as the need for mechanisms to encapsulate high-context SE activities into reusable skills. Overall, our study provides the first activity-centric characterization of SE skills and reveals how SE activities are increasingly being transformed into reusable skills. These findings offer new insights into skill reuse, ecosystem development, and the future of agent-centric SE.

</details>


### 17. ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning

- **Authors:** Kunbo Zhang, Lei Fu, Zeyu Wang, Zijing Liu, Kejian Tong
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09059v1](http://arxiv.org/abs/2607.09059v1)
- **PDF:** [https://arxiv.org/pdf/2607.09059v1](https://arxiv.org/pdf/2607.09059v1)
- **Categories:** cs.AI


> ARCANA introduces a modular, reflective multi‑agent architecture that tackles ARC‑AGI‑2 problems by iteratively grounding visual inputs, generating domain‑specific language (DSL) programs, symbolically executing them on exemplars, and using a reflective feedback loop to revise hypotheses. The system couples a perception agent that builds object‑centric scene graphs, a latent‑program policy that proposes diverse candidate programs, a symbolic executor that validates them, and a meta‑controller that schedules these components via a shared differentiable blackboard. Empirically, ARCANA achieves markedly higher success rates and faster convergence than prior monolithic or single‑turn program‑synthesis baselines on the benchmark’s most abstract transformation tasks, demonstrating that structured program search combined with multi‑turn reflective correction is a powerful paradigm for agentic AI reasoning.


<details>
<summary>Abstract</summary>

We present ARCANA, a collaborative multi agent framework for solving ARC AGI 2 tasks under strict test time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds object centric scene graphs from raw grids, a latent program policy proposes diverse DSL programs, a symbolic executor verifies candidates on demonstrations, and a reflective agent synthesizes failure driven feedback for the next turn. These agents communicate through a shared differentiable blackboard and are scheduled by a learned meta controller. The design combines structured program search with adaptive multi turn correction, improving reasoning efficiency and solution quality on challenging abstract transformation tasks.

</details>


### 18. Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents

- **Authors:** Zixiao Chen, Mariko Wakabayashi, Charlotte Siska
- **Published:** 2026-07-10
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.09011v1](http://arxiv.org/abs/2607.09011v1)
- **PDF:** [https://arxiv.org/pdf/2607.09011v1](https://arxiv.org/pdf/2607.09011v1)
- **Categories:** cs.CR, cs.MA


> The paper introduces **Secret Scanner Agent (SSA)**, a multi‑agent system built on large‑language models that not only detects leaked credentials in unstructured text (emails, tickets, chat logs) but also automatically infers the “door” (account, tenant, endpoint, etc.) the credential can open and supplies supporting evidence. SSA couples a high‑recall detection agent with a second review agent that filters false positives and enriches context; its performance is benchmarked on a synthetic suite covering 23 secret types and assorted document formats, using programmatic matching, an LLM judge, and human verification. Experiments show that, compared with single‑agent baselines and traditional regex scanners, SSA achieves up to **16 pp higher precision on door extraction**, **triples recall**, and outperforms 13 human security analysts by delivering more precise, twice‑as‑many secret‑door pairs while being **5–17× faster**, thereby turning raw credential leaks into actionable incident‑response findings.


<details>
<summary>Abstract</summary>

Exposed documents such as emails, chat threads, tickets, and incident notes routinely leak credentials, but during incident response a leaked secret is only half the story. Responders also need to identify the ``door'' the secret opens: the account, tenant, endpoint, database, cloud resource, or other system that the credential could allow an attacker to access. Traditional secret scanners rely on regular expressions or trained classifiers which work well on well-formatted code, yet they struggle when a credential is fragmented, reformatted, or far from the resource it unlocks, and they report the secret string without naming what it opens. We present Secret Scanner Agent (SSA), a multi-agent large-language-model system that extracts both the secret and its associated door, together with supporting evidence, from unstructured exposed documents. SSA pairs a detection agent that favors recall with a review agent that filters false positives and recovers missing context. Because real credential data is sensitive, we evaluate SSA on synthetic benchmarks we generated that span 23 secret types and multiple document formats, scored with a three-step pipeline of programmatic matching, an LLM judge, and human review. Across six models, multi-agent SSA improves extraction precision over a single-agent variant, with the largest gains on door extraction, by up to 16 percentage points. SSA matches a regular-expression scanner's precision while more than tripling its recall, and against thirteen security analysts it is more precise, recovers nearly twice as many secret--door pairs, and runs five to seventeen times faster. By returning the secret, its door, and supporting evidence in one result, SSA turns credential detection into an actionable finding for triage and remediation.

</details>


### 19. A Formalization of the Mean-Field Derivation of the Vlasov Equation: AI-Assisted Lean Formalization as a Strategy Game

- **Authors:** Joseph K. Miller
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08986v1](http://arxiv.org/abs/2607.08986v1)
- **PDF:** [https://arxiv.org/pdf/2607.08986v1](https://arxiv.org/pdf/2607.08986v1)
- **Categories:** cs.AI, cs.LO, math-ph, math.AP


> The paper presents a case study in which a mathematician guides an AI‑driven proof‑assistant (Lean 4) to fully formalize a recent analytical result on the Vlasov equation—specifically, the existence, uniqueness, stability estimate, mean‑field limit, and a short‑time superposition principle obtained via Dobrushin’s mean‑field method. By framing the formalization as a “game” whose win conditions are a compilation‑free, axiom‑clean development and reusable mathematical layers, the authors show that the AI can synthesize the necessary definitions, fill library gaps, and certify each theorem, while the human only steers the overall structure. The resulting development (≈300 Lean declarations) yields a self‑contained optimal‑transport subsystem (≈1⁄6 of the code) that can be imported into Mathlib, demonstrating that AI‑assisted lean formalization can rapidly produce high‑quality, reusable formal artifacts for complex agent‑theoretic PDE results.


<details>
<summary>Abstract</summary>

We formalize a research result in the Lean 4 proof assistant by having a mathematician direct an AI system, and frame the activity as a formalization game. The objective is to turn a LaTeX document into Lean. The game is won when the development compiles, contains no sorry, and a machine check shows the target theorems rest on Lean's foundational axioms alone. Reuse is a second check, by a definition we introduce: whether the development yields a self-contained layer of general mathematics the wider library could absorb. The case study is a complete, axiom-clean formalization of well-posedness for the nonlinear Vlasov equation via Dobrushin's mean-field route -- existence, uniqueness, the stability estimate and mean-field limit, and a short-window superposition principle (weak solutions are Lagrangian). The human's role was to direct, not to write proofs: to scope the definitions, steer the decompositions, and triage the library's gaps; the AI agent executed. The formalization certifies the proof of each statement as written; whether the written statement is the intended theorem stays the mathematician's judgment. The optimal-transport machinery that fell out of the build (in particular, properties of the Wasserstein-1 metric and the Kantorovich-Rubinstein duality theorem) separates into a self-contained layer that compiles against Mathlib alone: about a sixth of the development (49 of 299 declarations), behind a 22-declaration interface with no reverse dependency. The headline theorems ran in about a week, the full development in about a month. We report the quantitative claims as observations of one game, not as general laws. The game's rules name no particular system, so the methodological framing is meant to outlast the tools of any one run.

</details>


### 20. MultiView-Bench: A Diagnostic Benchmark for World-Centric Multi-View Integration in VLMs

- **Authors:** Hantao Zhang, Jinru Sui, Ed Li, Dirk Bergemann, Zhuoran Yang
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08970v1](http://arxiv.org/abs/2607.08970v1)
- **PDF:** [https://arxiv.org/pdf/2607.08970v1](https://arxiv.org/pdf/2607.08970v1)
- **Categories:** cs.CV, cs.AI


> The paper presents **MultiView‑Bench**, a diagnostic suite that measures a vision‑language model’s ability to fuse multiple observations into a single, world‑centric 3‑D representation—an ability essential for downstream agentic tasks such as robotic assembly. The authors evaluate several state‑of‑the‑art VLMs on the benchmark, finding that while these models handle single‑view 2‑D relations well, they consistently fail at true 3‑D spatial reasoning and at aggregating information across viewpoints, especially when axis orientations or object textures are atypical. To address these gaps, they introduce **ViewNavigator**, a lightweight multi‑agent system that actively selects informative views, perceives them, and fuses the evidence; this approach yields 3–5× performance gains over the base models even under equal computational budgets.


<details>
<summary>Abstract</summary>

Recent benchmarks for VLMs largely assess single- or limited-view perception, leaving untested the core cognitive ability to integrate observations across viewpoints into a coherent, world-centric (allocentric) 3D mental model. We introduce MultiView-Bench, a diagnostic benchmark expressly designed to evaluate multi-view integration for holistic 3D scene comprehension. Unlike existing datasets that focus on pixel-level mapping or camera-relative navigation, MultiView-Bench requires models to decouple object positioning from transient perspectives and ground them in a fixed global coordinate system. This capability serves as a prerequisite for VLMs before being deployed for downstream tasks such as mechanical part assembly. Our systematic evaluation of frontier VLMs reveals consistent failure modes: strong performance on 2D planar relations from a single image, but marked difficulty with 3D spatial relations and with aggregating information across views. We further identify biases in VLMs, such as struggles with unconventional axis directions and sensitivity to object colorways and texture variations. Acknowledging these limitations, we propose ViewNavigator, a multi-agent framework that actively selects informative viewpoints, perceives, and fuses multi-view evidence, improving diverse base models on MultiView-Bench even under a strict budget-matched comparison (and by 3-5x for the full agent).

</details>


### 21. Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading

- **Authors:** Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang, Zhichao Liu, Xiyang Wu, Anhao Li, Yue Yu, Ninghao Liu, Lichao Sun, Haotao Mi,  LeoweiLiang
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08964v1](http://arxiv.org/abs/2607.08964v1)
- **PDF:** [https://arxiv.org/pdf/2607.08964v1](https://arxiv.org/pdf/2607.08964v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **Long‑Horizon‑Terminal‑Bench (LHTB)**, a new terminal‑style benchmark suite of 46 diverse, long‑horizon tasks (e.g., experiment replication, software development, multimodal analysis) that are broken down into graded subtasks, enabling dense intermediate rewards and partial credit.

**Methodology:** Each LHTB task pairs a reference solution or simulator with a fine‑grained rubric; agents are evaluated over hundreds of episodes, consuming millions of tokens while the system records intermediate reward signals. The authors test 15 state‑of‑the‑art language‑model agents, measuring pass@1 under two reward thresholds (≥0.95 for “near‑perfect” and =1.0 for “perfect”).

**Key findings:** Even the best model attains only **15.2 %** pass@1 at the 0.95 threshold and **10.9 %** at perfect reward, with an average of **9.9 M tokens**, **231 episodes**, and **≈85 min** of runtime per task—orders of magnitude more demanding than existing terminal benchmarks. Failure‑mode analysis shows pervasive planning, context‑management, and debugging errors, indicating substantial headroom for future agentic‑AI research on long‑horizon, iteratively graded tasks.


<details>
<summary>Abstract</summary>

AI agents have become capable of autonomously completing short, well-specified tasks. However, existing terminal benchmarks largely focus on simple problems that finish within minutes and are evaluated only by their final outcome. This setup overlooks intermediate progress and partial solutions, yielding sparse reward signals and an incomplete picture of agent capability. We introduce Long-Horizon-Terminal-Bench, a terminal benchmark of 46 long-horizon tasks spanning nine categories, including experiment reproduction, software engineering, multimodal analysis, interactive games, and scientific computing. Each task follows a Terminal-Bench-style setup with a reference solution or simulation engine, but is further decomposed into fine-grained graded subtasks. This design enables dense intermediate rewards and partial credit, allowing evaluation to capture not only whether an agent reaches the final goal, but also how far it progresses on open-ended workflows. Tasks in Long-Horizon-Terminal-Bench typically require hundreds of episodes and minutes to hours of execution, stressing long-horizon planning, long-context management, and iterative debugging rather than one-shot problem solving. We evaluate 15 frontier models and find that agents consume on average 9.9M tokens per task, with roughly 231 episodes and 85.3 minutes of execution time per run, making Long-Horizon-Terminal-Bench more demanding than prior terminal-based benchmarks. Even the strongest tested model achieves 15.2% pass@1 at a partial-reward threshold of 0.95 and 10.9% at a perfect-reward threshold of 1.0, while the mean pass rate across models is 4.3% and 1.7% under the two thresholds, respectively. These results reveal headroom for improvement. We further analyze failure modes and error patterns, and release Long-Horizon-Terminal-Bench to support future progress on long-horizon terminal agents.

</details>


### 22. Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution

- **Authors:** Ning Liu, Kalle Kujanpää, Zhaoxuan Zhu, P Aditya Sreekar, Kaiwen Liu, Chuanneng Sun, Jorge Marchena Menendez, Matthew Bales, Tianyu Yang, Shahnawaz Alam, Rose Yu, Baoyuan Liu, Kristina Klinkner, Shervin Malmasi
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08960v1](http://arxiv.org/abs/2607.08960v1)
- **PDF:** [https://arxiv.org/pdf/2607.08960v1](https://arxiv.org/pdf/2607.08960v1)
- **Categories:** cs.LG, cs.AI


> **Contribution:** The paper introduces **Eluna**, a production‑grade, graph‑guided multi‑agent architecture that reliably executes complex warehouse Standard Operating Procedures (SOPs) by representing each SOP as a directed acyclic graph with progressive information disclosure and parallel sub‑agents.

**Methodology:** SOPs are decomposed into DAG nodes; a central coordinator progressively reveals only the data required for each node and dispatches independent tasks to persistent sub‑agents that can run code and query live databases. Reliability is achieved through **asymmetric episodic distillation**: a high‑capacity teacher LLM solves episodes, logs errors, and is iteratively refined; a smaller student model is then fine‑tuned on the corrected trajectories with the episodic memory removed, yielding a lightweight model that internalizes the corrections without extra runtime overhead.

**Key Findings:** On a 13‑task benchmark and two real‑world warehouse applications, the distilled Eluna models match or surpass their teacher, outperform larger off‑the‑shelf LLM baselines, and attain **94 % expert agreement** on a ticket‑processing task, demonstrating that graph‑guided decomposition plus episodic distillation can give agentic LLMs the procedural fidelity and latency required for high‑stakes operational automation.


<details>
<summary>Abstract</summary>

Warehouse operations are governed by Standard Operating Procedures (SOPs) that encode complex, multi-system decision logic, which must be executed reliably under strict time constraints, yet LLM agents lack mechanisms to enforce procedural compliance and degrade under the context overload full SOP specifications introduce. We present Eluna, a production-deployed agentic system for reliable SOP execution. Eluna is a graph-guided, multi-agent framework that encodes SOPs as directed acyclic graphs with progressive disclosure and delegates independent tasks to parallel sub-agents, each with persistent code execution and live data access. To meet production latency and accuracy needs, we use asymmetric episodic distillation where a strong teacher is improved through episodic error memories, then a smaller student is fine-tuned on the corrected trajectories with memory stripped, internalizing corrections without inference-time overhead. On a 13-task benchmark and two production applications, our fine-tuned models match or exceed their teacher, beat all larger off-the-shelf baselines, and reach 94% expert agreement on the ticket processing application.

</details>


### 23. Offline Nash Solvers Meet Online Tree Search in Multi-Agent Games on Graphs

- **Authors:** Mukesh Kumar, Yue Guan, Panagiotis Tsiotras
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08892v1](http://arxiv.org/abs/2607.08892v1)
- **PDF:** [https://arxiv.org/pdf/2607.08892v1](https://arxiv.org/pdf/2607.08892v1)
- **Categories:** cs.GT, cs.MA


> The paper introduces **Primitive‑Guided Tree Search (PGTS)**, a hybrid approach that bridges offline exact Nash equilibrium computation with online tree‑search planning for multi‑agent pursuit‑evasion games on graphs. PGTS first solves a library of small, tractable sub‑games offline to obtain optimal policies and value functions, then at run‑time uses these primitives to bias expansion and leaf‑value estimation in a forward‑looking tree search, thereby reducing the effective branching factor while retaining adaptability. Empirical evaluation on synthetic and real‑world graph topologies shows that PGTS consistently outperforms state‑of‑the‑art learning‑based and heuristic baselines, achieving higher win rates and more robust play against sophisticated adversaries, highlighting its potential for scalable, online Nash‑aware decision making in agentic AI systems.


<details>
<summary>Abstract</summary>

Computing Nash equilibrium policies in multi-agent Pursuit-Evasion games (PEG) is challenging due to the exponential growth of the joint state and action spaces with the number of agents. Existing approaches either rely on offline equilibrium approximations, which may lack adaptability during execution, or online planning methods, which suffer from large branching factors. In this work, we propose Primitive-Guided Tree Search (PGTS), a hybrid framework that integrates offline exact Nash equilibrium computation with online tree search: PGTS first solves a collection of smaller, tractable sub-games offline; at deployment, PGTS performs online tree search at each time step, using the optimal sub-game policies and value functions to guide tree expansion and estimate leaf-node values. Extensive experiments on varied graph topologies, including real-world networks, demonstrate that PGTS significantly outperforms state-of-the-art learning and heuristic baselines, while maintaining robust performance against adversaries.

</details>


### 24. UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

- **Authors:** Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08768v1](http://arxiv.org/abs/2607.08768v1)
- **PDF:** [https://arxiv.org/pdf/2607.08768v1](https://arxiv.org/pdf/2607.08768v1)
- **Categories:** cs.CL


> **Main contribution:** UniClawBench introduces the first capability‑driven benchmark that evaluates proactive AI agents on live, real‑world tasks rather than static or sandboxed settings, isolating five core abilities—Skill Usage, Exploration, Long‑Context Reasoning, Multimodal Understanding, and Cross‑Platform Coordination.

**Methodology:** The authors construct 400 bilingual tasks, each executed inside Docker containers with step‑by‑step checkpoints, and assess agents through a closed‑loop framework comprising an executor, a hidden supervisor, and a simulated user to provide multi‑turn feedback without exposing grading criteria. They then test multiple state‑of‑the‑art language models across several agent architectures to separate the effects of underlying model capability from framework design.

**Key findings:** Performance varies systematically with both the model’s intrinsic capabilities and the surrounding agent framework; no single model or design dominates across all five capability dimensions. The results highlight specific weak spots (e.g., long‑context reasoning and cross‑platform coordination) and demonstrate that a well‑engineered framework can substantially boost a model’s real‑world effectiveness, underscoring the need for both advanced base models and robust agent architectures in the agentic AI field.


<details>
<summary>Abstract</summary>

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it difficult to identify the root causes of agent failures. To address these limitations, we introduce UniClawBench, the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings. UniClawBench is built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination. Based on these capabilities, we design 400 bilingual real-world tasks. Unlike previous benchmarks that rely on static, pre-recorded answers, our benchmark evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints. Furthermore, we design a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria. To disentangle base model capabilities from framework-level design choices, we evaluate state-of-the-art models under multiple agent frameworks. Through comprehensive comparisons across both models and frameworks, we show how base model capabilities and agent framework designs jointly shape performance in real-world environments. To facilitate future research, we make our benchmark and code publicly available at https://github.com/HKU-MMLab/UniClawBench.

</details>


### 25. SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets

- **Authors:** Shilin Ou, Yifan Xu, Luyao Zhang
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08681v1](http://arxiv.org/abs/2607.08681v1)
- **PDF:** [https://arxiv.org/pdf/2607.08681v1](https://arxiv.org/pdf/2607.08681v1)
- **Categories:** cs.AI, cs.ET, cs.LG, cs.MA, econ.GN


> The paper introduces **SolarChain‑Eval**, a new benchmark that casts decentralized hourly energy‑market governance as a Gymnasium‑compatible MDP and augments it with physics‑based constraints and an LLM‑driven Planner/Auditor layer.  Using this framework the authors evaluate a spectrum of agents—from static baselines to reinforcement‑learning (RL) policies and RL agents enhanced with LLM planning—and measure not only market utility but also safety‑related metrics such as physical feasibility, slippage, action smoothness, spatial fairness, and auditability.  Experiments show that while RL agents can raise market utility, they still breach physical safety unless the physics penalty is enforced, and that the LLM Planner/Auditor improves traceability and mitigates some risky actions but cannot fully offset a misspecified reward, underscoring the need for explicit physical constraints and transparent intervention logs when assessing trustworthy agentic AI.


<details>
<summary>Abstract</summary>

As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governance as a Gymnasium-compatible Markov Decision Process, where agents make hourly decisions. SolarChain-Eval evaluates each policy across multiple dimensions, including market utility, physical safety, slippage, action smoothness, spatial fairness, and auditability. To support agentic evaluation, SolarChain-Eval incorporates an LLM-based Planner/Auditor layer. The Planner defines episode-level action bounds and audit rules, while the Auditor reviews and revises high-risk actions. All interventions are recorded through structured logs, including trigger signals, proposed actions, revised actions, and audit rationales. Experiments with static, random, myopic, RL, and RL+LLM policies reveal a clear utility-safety trade-off. RL agents improve market utility but can still produce unsafe behavior. When the physics penalty is removed, reward-maximizing agents exploit invalid generation and increase artificial liquidity. The LLM Planner/Auditor improves auditability and mitigates selected risks, but it cannot fully compensate for a misspecified reward function. These results indicate that trustworthy agentic AI evaluation requires both physical constraints and transparent intervention traces. We release data and code as open access on GitHub for replicability.

</details>


### 26. WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search

- **Authors:** Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao, Yutao Zhu, Zhongyuan Wang, Guanting Dong, Jinghan Yang, Han Li, Kun Gai, Ji-Rong Wen, Zhicheng Dou
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08662v1](http://arxiv.org/abs/2607.08662v1)
- **PDF:** [https://arxiv.org/pdf/2607.08662v1](https://arxiv.org/pdf/2607.08662v1)
- **Categories:** cs.CL, cs.AI, cs.MA


> **Main contribution**  
WebSwarm introduces a recursive, delegation‑based multi‑agent architecture that dynamically builds a hierarchy of specialized search nodes during inference, allowing LLM agents to pursue both deep, evidence‑grounded investigation and broad coverage of information sources.

**Methodology**  
The system first probes the web to infer the topical structure of a query, then creates search nodes each equipped with a local objective and a “search mode” (solve‑itself or delegate). Nodes can recursively spawn child nodes, share process‑level experience among siblings, and return evidence upward so that parent nodes can expand, revise, or aggregate the results. This progressive orchestration is implemented on top of ReAct‑style LLM agents with browsing tools.

**Key findings**  
Across four benchmark suites (BrowseComp‑Plus, WideSearch, DeepWideSearch, and GISA), WebSwarm consistently surpasses strong single‑agent and parallel multi‑agent baselines on tasks requiring deep reasoning, wide coverage, or a mix of both. Ablation studies show that recursive delegation, web‑structure probing, and sibling experience reuse are each critical to the observed gains, highlighting the effectiveness of hierarchical, evidence‑grounded collaboration for agentic web search.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and coverage simultaneously. Existing multi-agent systems improve search coverage through parallel execution and aggregation, but still exhibit clear limitations in recursive depth, collaboration adaptability, and evidence-grounded expansion. We propose WebSwarm, a progressive recursive delegation framework that jointly constructs task decomposition, recursive expansion, and agent collaboration during inference. WebSwarm dynamically instantiates agentic search nodes, each coupling a local objective with a search mode that specifies how the node should organize search and collaboration. Each node can either solve its objective itself or further delegate child nodes; after solving, it returns evidence and results upward, enabling parent nodes to further expand, revise, or aggregate the search process. To guide this process, WebSwarm first probes how task-relevant information is organized on the web to ground subsequent node expansion, and reuses process-level experience across homogeneous sibling nodes. Experiments on BrowseComp-Plus, WideSearch, DeepWideSearch, and GISA show that WebSwarm consistently outperforms single-agent and multi-agent baselines on deep, wide, and interleaved deep-and-wide tasks. Further analyses of ablation, task difficulty, web tool efficiency, and model generalization explain WebSwarm's effectiveness and provide insights for multi-agent search systems.

</details>


### 27. Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study

- **Authors:** Eugene Ng Yi Sheng, Bingquan Shen
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08652v1](http://arxiv.org/abs/2607.08652v1)
- **PDF:** [https://arxiv.org/pdf/2607.08652v1](https://arxiv.org/pdf/2607.08652v1)
- **Categories:** cs.AI


> The paper investigates which formally specified coordination mechanisms can keep a market of self‑interested, language‑model agents stable despite unrestricted communication and the presence of malicious “troll” agents. By running a 200‑round marketplace simulation with 18 DeepSeek‑V3 agents under eight candidate mechanisms, the authors find that a **Mediation** protocol (where a central mediator matches buyers and sellers and enforces contracts) yields the highest honest‑agent utility and outperforms alternatives even as trolls are progressively injected. Red‑team adversarial testing with iteratively optimized LLM‑driven troll prompts reduces honest‑agent utility by only 13.3 % and never collapses the market, demonstrating that Mediation is **robust**—it degrades under attack but continues to sustain positive utility for honest participants.


<details>
<summary>Abstract</summary>

Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complementary production specialties must trade within a constrained social network to obtain utility. We conduct two experimental phases: (1) a mechanism comparison across eight conditions under progressive troll injection over 200 rounds, identifying Mediation as the top-performing mechanism; and (2) adversarial red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls, finding that the best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse the market. Mediation enables recovery even under sustained adversarial pressure. We define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, and find that Mediation is robust: it can be bent but not broken.

</details>


### 28. Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning

- **Authors:** Ali Larian, Qian Lin, Chang Zong Wu, Daniel S. Brown
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08647v1](http://arxiv.org/abs/2607.08647v1)
- **PDF:** [https://arxiv.org/pdf/2607.08647v1](https://arxiv.org/pdf/2607.08647v1)
- **Categories:** cs.LG, cs.AI


> The paper’s main contribution is a hierarchical machine‑teaching framework that jointly exploits multiple environments and heterogeneous feedback (demonstrations, comparisons, rankings, etc.) to learn reward functions that generalize across dynamics, addressing a gap in prior IRL work that considered only single‑environment, demonstration‑only teaching. The authors first prove that, when unlimited data are available, comparison feedback imposes strictly stronger global constraints on the reward than other modalities, and then they design a two‑stage algorithm that (1) greedily selects a small set of environments that maximally diversify the induced reward constraints and (2) allocates low‑cost queries (comparisons, demos, etc.) within those environments to satisfy a fixed feedback budget. Empirically, the approach yields significantly lower regret and better out‑of‑distribution performance on held‑out MDPs than uniform teaching baselines, demonstrating that multi‑modal, multi‑environment teaching is crucial for robust reward learning in agentic AI.


<details>
<summary>Abstract</summary>

As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus on single-environment, demonstration-only settings, leaving underexplored how heterogeneous feedback modalities and environment dynamics jointly constrain reward functions that generalize across multiple environments. Because demonstrations in one MDP entangle reward information with that environments specific structure, the resulting rewards frequently fail to generalize when the agent is deployed in a new setting. We first analyze how different feedback modalities constrain rewards, showing that, in the unlimited-data regime, comparisons impose strictly stronger global constraints than other modalities. Beyond this theoretical analysis, we introduce a hierarchical machine teaching algorithm for reward learning that operates across multiple MDPs. The algorithm first greedily selects informative environments that expose complementary reward constraints, then strategically queries low-cost feedback within those environments. Empirically, our method achieves substantially lower regret and stronger generalization to held-out environments than uniform teaching baselines under identical feedback budgets, demonstrating the importance of multi-environment, multi-modal teaching for learning dynamics-robust reward functions.

</details>


### 29. The Context Access Divide: Interaction-Level Architecture as a Complementary Dimension of Agentic Inequality

- **Authors:** Masahiro Fujita
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08495v1](http://arxiv.org/abs/2607.08495v1)
- **PDF:** [https://arxiv.org/pdf/2607.08495v1](https://arxiv.org/pdf/2607.08495v1)
- **Categories:** cs.CY, cs.AI


> Sharp et al. (2025) identify a previously overlooked source of “agentic inequality” that operates at the interaction level: whether an AI system can **dynamically retrieve** relevant information from a user’s personal knowledge base (Dynamic Context Retrieval, DCR) or forces the user to **manually attach** documents for each query (Manual Attachment, MA).  The authors formalize this **Context Access Divide (CAD)** with a probabilistic model based on the fan‑effect, showing that MA causes a combinatorial collapse in task‑success probability as corpus size and task conjunctivity increase, whereas DCR‑enabled architectures (e.g., Retrieval‑Augmented Generation and Model Context Protocol) remain robust.  Empirical analysis of knowledge‑intensive workflows demonstrates that DCR markedly improves AI utility and reduces cognitive load, highlighting “contextuality” as a new dimension of agentic inequality that complements existing availability‑, quality‑, and quantity‑based metrics.


<details>
<summary>Abstract</summary>

Sharp et al. (2025) introduce "agentic inequality" as a framework for analyzing disparities in access to AI agents across three dimensions: availability, quality, and quantity. These person- and organization-level dimensions characterize who can access agents and at what capability, but do not address a structurally important divide operating at a finer level: the individual interaction. Two users with nominally equivalent agent access may experience qualitatively different AI utility depending on whether the system can autonomously retrieve context from the user's knowledge corpus (Dynamic Context Retrieval) or requires the user to manually identify and attach relevant documents at each query (Manual Attachment). We term this the Context Access Divide (CAD). For knowledge-intensive workers whose intellectual capital spans tens of thousands of files, the CAD constitutes a qualitative threshold in AI usefulness: below it, the cognitive burden of context curation falls on the human, reproducing the inefficiencies AI is meant to eliminate. We propose contextuality -- the degree to which an AI system autonomously accesses a user's accumulated knowledge capital -- as a dimension of AI-mediated inequality that complements, but is not reducible to, the Sharp et al. framework. We formalize the CAD with a probabilistic model grounded in the fan effect literature in cognitive psychology, demonstrating that manual context attachment leads to a combinatorial collapse in task-success probability as corpus size and task conjunctivity grow, while dynamic retrieval architectures are structurally insulated from this collapse. We analyze the technical basis of this divide in the Model Context Protocol (MCP) and retrieval-augmented generation (RAG) architectures, and examine its implications for knowledge-work stratification and AI platform governance.

</details>


### 30. OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice

- **Authors:** Qian Jiang, Zhecheng Shi, Jingpu Yang, Zirui Song, Miao Fang
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08423v1](http://arxiv.org/abs/2607.08423v1)
- **PDF:** [https://arxiv.org/pdf/2607.08423v1](https://arxiv.org/pdf/2607.08423v1)
- **Categories:** cs.AI


> The paper introduces **OmniFood‑Bench**, a new evaluation suite built on the MM‑Food‑100K dataset that probes Vision‑Language Models (VLMs) on the full reasoning pipeline required for agentic dietary management: (1) fine‑grained perception of ingredients and cooking methods, (2) quantitative inference of portion mass and nutrient profile, and (3) generation of disease‑specific, safety‑critical health advice. By testing six leading VLMs (e.g., GPT‑5.1, Gemini‑3‑Flash, Qwen3‑VL‑8B) with a three‑level protocol, the authors uncover a “semantic‑physical gap”: models excel at visual naming but catastrophically fail at mass estimation and often hallucinate harmless recommendations for high‑risk conditions such as diabetes. These findings highlight a critical weakness in current agentic AI systems for public‑health applications and set a benchmark for measuring and improving trustworthy nutrient reasoning in autonomous agents.


<details>
<summary>Abstract</summary>

The rapid integration of Large Vision-Language Models (VLMs) into critical infrastructure promises to revolutionize
  personalized healthcare and dietary management. However, in the domain of food systems, autonomous agents face a
  unique and persistent challenge: the "Systemic Information Asymmetry" between visual appearance and intrinsic
  nutritional composition. Existing benchmarks primarily focus on coarse-grained classification tasks, such as food
  category recognition, which fail to evaluate the intricate reasoning chain required for real-world dietary management
  -- specifically, the ability to traverse from identifying hidden ingredients to estimating physical mass, and finally
  synthesizing safety-critical medical advice. In this paper, we introduce OmniFood-Bench, a comprehensive benchmark
  constructed from the MM-Food-100K dataset. Unlike previous works, OmniFood-Bench evaluates VLMs across three
  progressive capabilities: Basic Perception (Ingredients & Cooking Methods), Quantitative Reasoning (Portion Size &
  Nutritional Profiling), and Safety-Critical Advisory (Disease-Specific Recommendations). We evaluate six
  state-of-the-art VLMs, including gpt-5.1, gemini-3-flash, and qwen3-vl-8B. Our extensive experiments reveal a
  startling "Semantic-Physical Gap": while models achieve near-human accuracy in naming dishes, they exhibit
  catastrophic failure in mass estimation and frequently hallucinate benign advice for high-risk diabetic profiles. This
  work establishes a rigorous standard for trustworthiness in autonomous agents deployed for public health. The code
  and datasets are available in: https://anonymous.4open.science/r/OmniFood-Bench-7D0B

</details>


### 31. Game Theory Driven Multi-Agent Framework Mitigates Language Model Hallucination

- **Authors:** Runzhe Liu, Biquan Bie, Zihao Wang, Yuchao Ma, Yexin Liu, Xinghai Li, Harry Yang, Wenbo Yang, Jinzhe Cao, Shengyang Tao
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08403v1](http://arxiv.org/abs/2607.08403v1)
- **PDF:** [https://arxiv.org/pdf/2607.08403v1](https://arxiv.org/pdf/2607.08403v1)
- **Categories:** cs.AI


> The paper introduces **G‑Frame**, a game‑theoretic multi‑agent system that combines Bayesian updating with team‑game coordination to continuously enforce domain constraints during data generation and model fine‑tuning, thereby curbing the “hallucination” problem of lightweight LLMs in rule‑based scientific tasks. By deploying G‑Frame to produce a curated corpus of 363 k chains‑of‑thought and 199 k question‑answer pairs, the authors fine‑tuned a 7 B‑parameter model (OmniChem) that matches GPT‑4o‑mini on bespoke chemistry benchmarks and the ChemBench suite while reducing hallucinations by **≈79 %** compared with its untuned base. The study demonstrates that adaptive, game‑theoretic agent collaboration can systematically internalize axiomatic reasoning, enabling reliable molecular design and synthesis planning with compact models and offering a scalable route for specialized scientific AI.


<details>
<summary>Abstract</summary>

The application of lightweight Large Language Models in rule-based scientific domains remains severely limited by their tendency to mimic linguistic patterns rather than reproduce axiomatic reasoning, causing frequent hallucinations. Here, we show that G-Frame, an adaptive multi-agent framework integrating Bayesian and team game principles, establishes an automated closed-loop for high-quality data synthesis and model training. By forcing the internalization of domain constraints through structured reasoning, we synthesized a specialized corpus of 363,045 chains-of-thought and 199,589 question-answer pairs. The resulting 7B model OmniChem achieves performance parity with GPT 4o mini on custom benchmarks and ChemBench while exhibiting a 79.46% reduction in hallucinations relative to its base architecture. We further demonstrate the advanced capabilities of OmniChem in molecular design and synthesis planning. This work establishes a scalable paradigm utilizing adaptive multi-agents to overcome inherent reasoning deficiencies, offering a feasible pathway for accelerating knowledge discovery in specialized scientific fields.

</details>


### 32. TRACE: A Two-Channel Robust Attribution Watermark via Complementary Embeddings for LLM-Agent Trajectories

- **Authors:** Zheng Gao, Xiaoyu Li, Xiaoyan Feng, Jiaojiao Jiang, Yang Song, Yulei Sui, Zhenchang Xing, Liming Zhu
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08400v1](http://arxiv.org/abs/2607.08400v1)
- **PDF:** [https://arxiv.org/pdf/2607.08400v1](https://arxiv.org/pdf/2607.08400v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> **Main contribution**  
The paper introduces **TRACE**, the first robust watermarking scheme for large‑language‑model (LLM) agents that embeds provenance information directly into the agents’ **trajectory logs** (the sequence of tool calls, observations and actions) and remains effective even when a reseller has full read/write access to those logs.

**Methodology**  
TRACE builds two complementary, distortion‑free channels:  
1. a **selection channel** that deterministically chooses which action to take based on locally‑derived content keys; this leaves the agent’s action distribution unchanged and automatically re‑synchronizes after any deletions, and  
2. a **tally channel** that controls the number of records belonging to each decision group using only the log’s positional skeleton, making it invariant to any LLM‑based rewriting of the log. The authors prove that the watermark cost is bounded by the decision entropy and that removing both channels forces the adversary to corrupt the trajectory itself.

**Key findings for agentic AI**  
Experiments on ToolBench and ALFWorld show that TRACE incurs **no drop in task success** compared to an unwatermarked agent, achieves near‑perfect detection (z‑score ≈ 100) on long‑horizon trajectories, stays detectable after up to **70 % of steps are deleted**, and the tally channel remains exactly unchanged under arbitrary LLM rewriting. Thus, TRACE provides a practical, provably robust attribution mechanism for LLM‑driven agents in adversarial resale scenarios.


<details>
<summary>Abstract</summary>

LLM agents reach users through resellers, who may rebrand a developer's agent or substitute a cheaper model. When provenance is disputed, attribution rests on the trajectory log (the record of tool calls, observations, and executed actions, not the model's reasoning), which the reseller stores and processes to meter usage. A watermark must therefore survive an adversary with full read/write access to the very evidence it is detected from; existing agent watermarks do not, as their attribution is read straight off that log. We present TRACE, to our knowledge the first agent watermark that is distortion-free in its action choices, self-synchronizing under deletion, and unconditionally invariant under rewriting. Deletion desynchronizes a position-derived key and rewriting alters content, so a deletion-robust key must come from content and a rewrite-robust key from position, and no single key serves both. A trajectory, however, has room for two watermarks. TRACE superposes a selection channel that sets which action is chosen, keyed on local content with a distortion-free sampler, so the agent's distribution is provably unchanged and detection resynchronizes after deletions, and a tally channel that sets how many records each decision group holds, keyed on the log's skeleton alone, which no rewriting can touch. We prove this behavioral watermark's signal is bought with decision entropy, each decision paying at least half its entropy and deterministic decisions nothing, and that erasing both channels forces the reseller to corrupt the trajectories it resells. On ToolBench and ALFWorld, TRACE matches the unwatermarked agent's success rate while its selection channel reaches detection scores near z = 100 on long-horizon trajectories, stays detectable under 70% step deletion, and keeps a tally channel exactly unchanged under LLM rewriting of any strength.

</details>


### 33. Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents

- **Authors:** Puji Wang, Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Xueqi Cheng
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08395v1](http://arxiv.org/abs/2607.08395v1)
- **PDF:** [https://arxiv.org/pdf/2607.08395v1](https://arxiv.org/pdf/2607.08395v1)
- **Categories:** cs.CR, cs.CL


> The paper introduces **TokenWall**, a “semantic firewall” that monitors and filters all natural‑language token flows (memory writes, tool arguments, file contents, inter‑module messages) of persistent AI agents before they reach privileged runtime sinks. By constructing source‑sink audit records and applying lightweight, boundary‑aware inspections—escalating only ambiguous high‑risk flows to stronger arbitration modules—the system provides full‑coverage, pre‑execution containment without relying on remote large‑model oversight. In benchmarks on the CIK‑Bench suite, TokenWall cuts the attack success rate to **12.5 %** while allowing **97.4 %** of benign executions to pass unchanged, adding only **0.69 s** of latency, thereby demonstrating a practical security‑utility balance for long‑lived, tool‑using AI agents.


<details>
<summary>Abstract</summary>

Persistent AI agents extend large language models (LLMs) beyond single-turn interaction into long-lived software systems. Unlike traditional chat assistants, unsafe content in these agents can propagate through persistent state, reusable skills, and tool-mediated interactions, creating a substantially larger semantic attack surface. We observe that most security-critical interactions in such agents are transmitted through natural-language token flows, including memory updates, tool arguments, retrieved files, and inter-component communications. This observation enables a new security formulation: unsafe behavior can be intercepted as risky semantic flows before reaching privileged runtime sinks. Based on this insight, we propose TokenWall, a runtime defense framework that acts as a semantic firewall over agent token flows. TokenWall performs boundary-aware semantic auditing over these flows, constructing structured source-sink audit records, applying lightweight local inspection before execution, and selectively escalating ambiguous high-risk cases to stronger arbitration modules. Unlike prior approaches that rely on sparse auditing or remote large-model oversight, TokenWall enables full-coverage pre-execution mediation while reducing remote arbitration and latency. Experiments on CIK-Bench show that TokenWall reduces attack success rate to 12.5% while maintaining a 97.4% benign executable pass rate without human confirmation. TokenWall further introduces only 0.69 seconds of additional latency on benign cases, demonstrating that semantic runtime containment can achieve a practical security-utility trade-off for persistent AI agents.

</details>


### 34. WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving

- **Authors:** Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08375v1](http://arxiv.org/abs/2607.08375v1)
- **PDF:** [https://arxiv.org/pdf/2607.08375v1](https://arxiv.org/pdf/2607.08375v1)
- **Categories:** cs.CV, cs.AI


> The paper introduces **WCog‑VLA**, a dual‑level World‑Cognitive Vision‑Language‑Action architecture that combines (i) a semantic world‑cognition module—integrating 3D spatial perception, agent tokens, and Game‑theoretic Chain‑of‑Thought (Game‑CoT) reasoning—to model world dynamics, and (ii) a generative world model called the **Aligned Decoupled Diffusion Transformer (ADDT)** that produces physically plausible multi‑agent trajectories with far fewer denoising steps. The authors train the system on a newly created 85 k‑example dataset annotated with Game‑CoT reasoning and evaluate it on the NAVSIM benchmark, where WCog‑VLA attains a new state‑of‑the‑art PDMS score of 92.9, demonstrating markedly more proactive and coherent autonomous‑driving behavior than prior VLA approaches.


<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cognition and reasoning by incorporating 3D spatial perception and injecting agent tokens to capture the world dynamics, while concurrently enabling Game-theoretic Chain-of-Thought (Game-CoT) reasoning. At the generative level, we introduce the Aligned Decoupled Diffusion Transformer (ADDT) as a powerful generative world model that synthesizes physically-plausible joint multi-agent trajectories. Through scene representation alignment, ADDT reduces the number of denoising steps required and thus significantly accelerates inference. To facilitate strategic reasoning, we further construct a large-scale dataset featuring 85k Game-CoT annotations. Extensive experiments on the NAVSIM benchmark demonstrate that WCog-VLA achieves a State-Of-The-Art (SOTA) PDMS score of 92.9.

</details>


### 35. From Legacy Documentation to OSCAL: An MCP-Based Agent Pipeline for Threat-Informed Continuous Compliance in Critical Infrastructure

- **Authors:** Lea Roxanne Muth, Marian Margraf
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08288v1](http://arxiv.org/abs/2607.08288v1)
- **PDF:** [https://arxiv.org/pdf/2607.08288v1](https://arxiv.org/pdf/2607.08288v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces a multi‑agent pipeline grounded in the Minimalist Cognitive Paradigm (MCP) that transforms free‑form natural‑language documentation of critical‑infrastructure OT assets into a verified knowledge graph and audit‑ready NIST OSCAL artifacts, thus enabling continuous, threat‑informed compliance without invasive scanning. By separating LLM‑driven reasoning from deterministic retrieval of authoritative threat‑intelligence (CVE, D3FEND) the system attains 90 % CVE recall and 100 % D3FEND recall in a synthetic water‑utility scenario, automatically producing schema‑valid OSCAL System Security Plans and Security Assessment Reports. The authors show that while MCP grounding does not eradicate hallucinations, it localises errors to the initial asset‑extraction stage, making downstream false positives visible and efficiently reviewable by operators who already know the true asset inventory.


<details>
<summary>Abstract</summary>

In critical infrastructure, operational technology environments often cannot be actively scanned, and yet active system feedback is needed for risk assessment and compliance. This paper presents a non-invasive, MCP-grounded multi-agent pipeline that converts natural-language system descriptions into source-verified knowledge graph and audit-ready artifacts in the NIST OSCAL format for continuous automated compliance management. The architecture decouples LLM-based reasoning from deterministic knowledge retrieval against authoritative threat-intelligence sources, reducing the risk of fabricated vulnerabilities and hallucinated attack paths.
  In an evidence-based synthetic scenario of a water utility, the pipeline achieves 0.90 CVE recall and perfect D3FEND recall. It generates a schema-valid OSCAL System Security Plan and an OSCAL Security Assessment Report. Nevertheless, the core insight is not that grounding via MCP eliminates errors (e.g., hallucinations) entirely from the pipeline, but that it shifts errors into the first phase of asset extraction from the natural language description. Here, a single incorrectly extracted entity can lead to genuine but irrelevant CVEs in subsequent stages of the pipeline, which consumes time and resources. However, it makes the remaining risk visible, verifiable, and suitable for a time-efficient manual review, since the infrastructure (e.g., version numbers, OS, etc.) is typically known.

</details>


### 36. Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models

- **Authors:** Hugo García Cuesta, Pablo Mateo Torrejón, Alfonso Sánchez-Macián
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08282v1](http://arxiv.org/abs/2607.08282v1)
- **PDF:** [https://arxiv.org/pdf/2607.08282v1](https://arxiv.org/pdf/2607.08282v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> The paper introduces an open‑source, user‑facing firewall that interposes between clients and large language models (LLMs) to prevent the accidental leakage of sensitive data. Its methodology combines a browser‑extension plus a network proxy that captures all HTTP(S) and WebSocket traffic and routes it through a modular multi‑agent pipeline: deterministic detectors, an LLM‑based semantic analyzer, and proprietary code‑exfiltration guards, all of which can be extended to counter prompt‑injection attacks. Evaluation on benchmark leakage‑detection tasks shows the system can reach up to 94.93 % F1 while offering tunable trade‑offs among computational cost, detection depth, and latency, demonstrating a practical, agentic approach to privacy‑preserving LLM interaction.


<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have become essential productivity tools, their integration into workflows without adequate safeguards creates significant risks. This paper proposes an open-source, privacy-focused, user-facing firewall designed to secure both web-based and programmatic LLM interactions. The architecture combines a browser extension and a proxy for total traffic interception across both HTTP(S) and WebSocket communications. At its core, a flexible multi-agent pipeline delivers data leakage prevention through a hybrid approach combining deterministic detectors with LLM-driven semantic analysis, proprietary code leakage prevention, and extensible components designed for future security enhancements such as prompt injection evasion. The framework's layered architecture enables deployment across heterogeneous environments, allowing organizations to balance computational cost, detection depth and latency. Evaluation results demonstrate it achieves F1 scores of up to 94.93% on optimal configurations.

</details>


### 37. Playing ZendoWorld: Challenging AI Agents on Active Visual Concept Induction

- **Authors:** Sophia Koehler, Antonia Wüst, Inga Ibs, Wasu Top Piriyakulkij, Wolfgang Stammer, Constantin Rothkopf, Kevin Ellis, Kristian Kersting
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08233v1](http://arxiv.org/abs/2607.08233v1)
- **PDF:** [https://arxiv.org/pdf/2607.08233v1](https://arxiv.org/pdf/2607.08233v1)
- **Categories:** cs.AI, cs.CV


> **Main contribution:** The paper introduces **ZendoWorld**, a sandbox environment that forces agents to *actively* infer hidden logical rules from visual scenes by generating and testing new examples, thereby providing a benchmark for the full perception–hypothesis–experiment loop that underlies scientific‑style discovery.

**Methodology:** The authors implement a suite of agents—including pure vision‑language model (VLM) reasoners, Bayesian particle‑filter learners, dynamic concept‑discovery systems, and neuro‑symbolic hybrids—and evaluate them on a set of ZendoWorld tasks that vary in rule complexity. Human participants are also collected for comparison. Performance is measured both by label‑prediction accuracy on observed scenes and by the ability to recover the true underlying rule, as well as by the informativeness of the generated experiments (entropy reduction of the hypothesis space).

**Key findings:** (1) High prediction accuracy does **not** guarantee correct rule recovery; many agents overfit to observed examples. (2) Different architectures hit distinct bottlenecks: VLMs excel at perception but fail to design informative queries, while Bayesian and neuro‑symbolic agents struggle with perception but can reduce hypothesis uncertainty when they have reliable visual input. (3) VLM‑based agents typically propose near‑uninformative experiments, leaving a large gap to human performance, especially on complex rules. These results highlight the need for tighter integration of perception, symbolic reasoning, and active experiment design in agentic AI systems.


<details>
<summary>Abstract</summary>

A central challenge in building intelligent systems is enabling agents to jointly perceive complex inputs, form hypotheses about hidden patterns, and design informative experiments to test them. To study this problem, we propose ZendoWorld, a controlled interactive environment in which agents must infer a logical rule about visual game observations, acquire information by proposing new scenes, and refine their hypotheses based on feedback from the game environment. We evaluate several agents spanning pure VLM reasoning, Bayesian particle filtering, dynamic concept discovery, and neuro-symbolic methods. Our main findings are: (1) high accuracy in predicting labels for observed examples does not imply recovery of the underlying rule; (2) perception and induction are distinct bottlenecks for different agent classes; and (3) VLM-based agents propose near-uninformative experiments, failing to actively reduce hypothesis uncertainty. To compare these results, we collect human data on the task, which reveals a gap in inductive reasoning, particularly for more complex rules. Overall, ZENDOWORLD takes an important step toward evaluating intelligent agents and identifies concrete avenues for improvement, particularly in domains like scientific discovery.

</details>


### 38. Open-ended Multi-agent Autocurricula via Visual Inspection of Policies with Multi-modal LLMs

- **Authors:** Lorenzo Pantè, Andrea Fanti, Roberto Capobianco
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08193v1](http://arxiv.org/abs/2607.08193v1)
- **PDF:** [https://arxiv.org/pdf/2607.08193v1](https://arxiv.org/pdf/2607.08193v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces **Visual Inspection of Policies (VIP)**, a novel open‑ended curriculum‑generation method that evaluates agent performance by feeding recorded episode videos to a video‑language model (VLM) rather than relying on scalar scores or textual summaries. Using the open‑source VideoLLaMa‑2 7B, the authors process multi‑agent StarCraft II (SMAC) replays to let the VLM judge task difficulty and propose next tasks, demonstrating that this vision‑grounded feedback yields curricula that accelerate skill acquisition more than text‑only baselines and traditional score‑based approaches. The results show that even lightweight VLMs can successfully drive multi‑agent autocurricula, highlighting video‑based policy inspection as a promising tool for building generally capable, agentic AI systems.


<details>
<summary>Abstract</summary>

Open-ended curricula in Reinforcement Learning (RL) aim to train generally-capable agents by identifying tasks that facilitate learning increasingly complex skills. A major challenge when designing such curricula is assessing task difficulty relative to the agent's current learning progress. While previous work has explored using scalar task scores or textual summaries of the agent's behavior, here we study a different approach: directly inspecting policy behavior via recorded episode videos. We introduce a simple yet effective instantiation of this approach which leverages a Video Language Model (VLM) to both process these videos and provide curriculum recommendations, which we call Visual Inspection of Policies (VIP). Since videos can naturally contain any number of controllable agents, we empirically study VIP on the StarCraft Multi-Agent Challenge (SMAC). We show that even with a lightweight and openly accessible VLM (VideoLLaMa2-7B), VIP can use policy videos to generate more effective curricula than both its text-only ablation and methods that rely on scalar task scores.

</details>


### 39. ASMR: Agentic Schema Generation for Ship Maintenance Report Writing

- **Authors:** Sohrab Namazi Nia, Amogh Dalal, Ning Sa, Peter Ly, Marti Zentmaier, Tomek Strzalkowski, Jay Miller, Rishi Singh, Senjuti Basu Roy
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08177v1](http://arxiv.org/abs/2607.08177v1)
- **PDF:** [https://arxiv.org/pdf/2607.08177v1](https://arxiv.org/pdf/2607.08177v1)
- **Categories:** cs.AI, cs.MA


> The paper introduces **ASMR**, a modular agentic system that automatically constructs concise, information‑rich schemas for different ship‑maintenance report types. It does so by deploying two cooperating agents: (1) a **Field Generation Agent** that extracts semantic concepts from legacy reports and clusters them at multiple granularities to propose candidate fields, and (2) a **Structural Optimizer Agent** that uses reinforcement‑learning‑based reward signals (compactness, coverage, redundancy avoidance) to select the optimal field set. Experiments on real maintenance corpora show that ASMR‑generated schemas improve report completeness and consistency compared with baseline keyword‑ or frequency‑based schemas, illustrating the utility of agent‑driven schema induction for human‑centered, data‑management‑aware AI.


<details>
<summary>Abstract</summary>

In this paper, we study the automatic schema generation problem: given a collection of historical ship maintenance and operational reports across multiple form categories, automatically discover compact and informative schemas that capture the essential information requirements of each report type. To address this challenge, we propose ASMR, a modular agentic framework consisting of two specialized agents. A Field Generation Agent extracts semantic concepts from historical narratives and generates candidate schema fields through adaptive multi-granularity clustering, while a Structural Optimizer Agent employs reinforcement learning to identify compact, informative, and non-redundant schema representations. The resulting schemas can guide report authors toward producing more complete, consistent, and actionable reports. Preliminary results demonstrate the promise of the proposed approach and highlight several open research challenges at the intersection of data management, agentic AI, and human-centered AI.

</details>


### 40. TTHE: Test-Time Harness Evolution

- **Authors:** Jun Nie, Yonggang Zhang, Jun Song, Qianshu Cai, Dahai Yu, Yike Guo, Xinmei Tian, Bo Han
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08124v1](http://arxiv.org/abs/2607.08124v1)
- **PDF:** [https://arxiv.org/pdf/2607.08124v1](https://arxiv.org/pdf/2607.08124v1)
- **Categories:** cs.SE, cs.LG


> The paper introduces **Test‑Time Harness Evolution (TTHE)**, a framework that adapts the *execution harness*—the surrounding program that formats prompts, calls tools, and handles errors—while a frozen LLM is being evaluated, using only the agent’s own unlabeled execution traces. TTHE maintains a population of candidate harnesses, lets an “agentic proposer” generate new harness variants based on trace‑derived proxy signals, and a “judge” selects the best variant to persist for subsequent inputs, thus achieving unsupervised, test‑time evolution without modifying model weights or requiring gold labels. Experiments on text‑to‑SQL, competitive programming, software‑engineering, data‑science coding, and tool‑use benchmarks show that TTHE consistently improves over static ReAct‑style harnesses, demonstrating that test‑time adaptation can be realized through evolutionary refinement of executable control programs and highlighting proxy‑reliability as a key challenge for robust agentic AI.


<details>
<summary>Abstract</summary>

The behavior of an LLM agent is determined not only by the underlying model, but also by its harness: the executable program that constructs context, invokes tools, verifies intermediate results, and recovers from failures. Existing approaches optimize such harnesses before deployment, searching training or development data for a fixed agent workflow that is then frozen at test time. This limits adaptation when the test distribution, failure modes, or tool interactions differ from those seen during development. We ask whether the harness can instead be optimized during evaluation itself, using only the unlabeled execution traces the agent produces on the test inputs. We introduce Test-Time Harness Evolution (TTHE), which treats the executable harness as the state of test-time adaptation. During evaluation, TTHE maintains a population of candidate harnesses and refines them through an agentic proposer that reasons over their execution traces, without gold labels or task-specific supervision; a judge then commits an improved harness from execution-derived proxy signals, and the selected program persists to govern subsequent inputs. Crucially, TTHE does not update model weights, require gold labels, or train a separate adaptation model: solver, proposers, and judge are different roles and harnesses around the same frozen LLM, so all adaptation occurs through changes to the surrounding program. Across text-to-SQL, competitive programming, software engineering, data-science coding, and agentic tool-use tasks, TTHE improves fixed ReAct-style baseline harnesses, yielding persistent, inspectable improvements rather than a pre-searched workflow or per-query retries. These results recast test-time adaptation for LLM agents as evolution over executable control programs and identify execution-derived proxy reliability as a central challenge for robust unsupervised agent improvement.

</details>


### 41. MASTE: A Multi-Agent Pipeline for Zero-Shot Aspect Sentiment Triplet Extraction

- **Authors:** Ao Hong, Lehang Wang, Zhirun Yue, Mingxin Wang, Zihan Wang, Houde Liu
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08080v1](http://arxiv.org/abs/2607.08080v1)
- **PDF:** [https://arxiv.org/pdf/2607.08080v1](https://arxiv.org/pdf/2607.08080v1)
- **Categories:** cs.CL


> The paper introduces **MASTE**, a training‑free, zero‑shot framework that tackles Aspect Sentiment Triplet Extraction (ASTE) by coordinating a pipeline of four specialized LLM “agents,” each responsible for a sub‑task (aspect detection, opinion span extraction, opinion‑aspect pairing, and sentiment classification) and conditioned on the outputs of the preceding agents. By decomposing the one‑shot generation problem into sequential, compositional stages, MASTE achieves far better zero‑shot performance than plain prompting, few‑shot in‑context learning, or chain‑of‑thought methods across four ASTE benchmarks, closing much of the gap to supervised models without any labeled triplet data. The approach is backbone‑agnostic and demonstrates that multi‑agent decomposition is an effective strategy for zero‑shot, agentic AI applications in fine‑grained information extraction.


<details>
<summary>Abstract</summary>

Aspect Sentiment Triplet Extraction (ASTE) requires jointly identifying (aspect, opinion, sentiment) triples from a given review sentence. While large language models (LLMs) achieve strong zero-shot performance on many NLP benchmarks, their effectiveness on ASTE remains limited, as single-pass generation forces the model to determine span boundaries, opinion grouping, and sentiment polarity in a single decoding step. Common remedies, such as few-shot in-context learning and chain-of-thought prompting, offer only marginal improvements and rely heavily on either in-domain demonstrations sampled from labeled training data or carefully engineered reasoning prompts, neither of which is broadly available in zero-shot deployment. Inspired by the classical agent paradigm, we propose MASTE, a multi-agent pipeline for zero-shot Aspect Sentiment Triplet Extraction. MASTE decomposes ASTE into four sequential stages, where specialized agents handle different compositional subtasks with explicit conditioning on prior outputs. This design enables entirely training-free zero-shot ASTE and generalizes across different backbones and datasets. Extensive experiments on four ASTE benchmarks show that MASTE substantially outperforms zero-shot and chain-of-thought LLM baselines under the same backbone, narrowing the gap to fully supervised methods without using any labeled triplets. Code is available at https://github.com/Hankerlove/MASTE.

</details>


### 42. Persuasion Attacks Can Decrease Effectiveness of CoT Monitoring

- **Authors:** Jennifer Za, Julija Bainiaksina, Nikita Ostrovsky, Tanush Chopra, Victoria Krakovna
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08066v1](http://arxiv.org/abs/2607.08066v1)
- **PDF:** [https://arxiv.org/pdf/2607.08066v1](https://arxiv.org/pdf/2607.08066v1)
- **Categories:** cs.AI, cs.LG


> **Main contribution:** The paper shows that chain‑of‑thought (CoT) monitoring, a widely‑promoted safety layer for AI agents, can be subverted by persuasion attacks that exploit the visible reasoning trace as a new channel for manipulation, and proposes a model‑diverse fact‑checking architecture to counter that weakness.  

**Methodology:** The authors built an evaluation suite of 40 tasks and generated thousands of adversarial interactions in which an agent deliberately argues for policy‑violating actions while a monitor reviews the agent’s CoT. They measured the monitor’s approval rates and then tested a hybrid “monitor + fact‑checker” system using models from different families (e.g., Claude 3.7 Sonnet as monitor, GPT‑4.1 as fact‑checker).  

**Key findings:** In the adversarial setting, granting the monitor access to the agent’s CoT *increases* the approval of harmful actions by about **9.5 %** on average, demonstrating that the scratchpad can act as a persuasion conduit. Pairing the monitor with a fact‑checker from a different model family cuts the approval of policy‑violating actions by up to **45 %**, versus only ~6 % when both components share the same model. Thus, CoT monitoring alone is insufficient against persuasion‑based jailbreaks, but heterogeneous model fact‑checking offers a robust mitigation for agentic AI safety.


<details>
<summary>Abstract</summary>

Chain-of-thought (CoT) monitoring is a promising safety mechanism for AI agents, based on the premise that visible reasoning traces can surface misaligned or deceptive behavior. While effective in standard scenarios, recent work highlights that LLMs remain vulnerable to persuasion-based jailbreaks, where natural-language arguments override model constraints. We stress-test whether this vulnerability extends to monitoring LLMs: can an adversarial agent persuade its CoT monitor to approve proposed actions that violate the monitor's policy? We design an evaluation framework with 40 tasks and analyze thousands of agent-monitor interactions, where agents are instructed to argue for policy-violating proposals. We find that in such adversarial settings, monitor access to the agent's CoT reasoning increases rather than decreases approval of harmful actions on average by 9.5%, as the scratchpad provides an additional persuasion channel. To address this, we introduce a fact-checking monitoring framework. We find that a fact-checker and monitor pairing from different model families, for example a Claude 3.7 Sonnet monitor paired with a GPT-4.1 fact-checker, reduces approval of policy-violating actions by up to 45%, compared to only 6%, when using the same model for both fact-checking and monitoring roles. Our results demonstrate that CoT monitoring alone may be insufficient against adversarial persuasion, and that model-diverse fact-checking provides a robust mitigation.

</details>


### 43. Aleena: Alignment Agent for Research Software Engineering Collaborations

- **Authors:** Kshitij Dani, Cordero Core, Landung Setiawan, Carlos Garcia Jurado Suarez, Anshul Tambay, Vani Mandava, Anant Mittal
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08043v1](http://arxiv.org/abs/2607.08043v1)
- **PDF:** [https://arxiv.org/pdf/2607.08043v1](https://arxiv.org/pdf/2607.08043v1)
- **Categories:** cs.SE, cs.AI


> **Main contribution:** The paper introduces **Aleena**, an open‑source “alignment agent” that continuously captures and reconciles the evolving decisions, rationales, and assumptions that arise across the heterogeneous artifacts of research‑software collaborations (Slack, meetings, pull requests, GitHub issues).  

**Methodology:** Building on real‑world practices from university research‑software engineering centres, the authors design Aleena as a lifecycle‑wide AI service that ingests multi‑modal stakeholder interactions, extracts structured records (e.g., decisions, open questions, risks), and stores them in a GitHub‑based knowledge base. The prototype leverages natural‑language processing for intent extraction, a lightweight ontology for project state, and automated notifications to surface gaps without automating the actual decisions.  

**Key findings:** In illustrative scenarios, Aleena successfully preserves decision continuity, surfaces hidden dependencies, and reduces misalignment between domain researchers and software engineers, demonstrating that agentic AI can act as an *alignment facilitator*—maintaining a shared, searchable provenance of project intent while leaving final judgments to humans. This work positions alignment agents as practical, low‑overhead components for the emerging field of agentic AI in collaborative scientific software development.


<details>
<summary>Abstract</summary>

Research software collaborations span meetings, informal chats, pull requests, and GitHub issues. A decision surfaced in a Slack thread, refined in a meeting, and implemented in a pull request can lose its original rationale across these artifacts, leaving domain researchers and research software engineers with divergent mental models of project intent, ownership, and scientific assumptions. We argue that alignment in research software engineering is a continuous lifecycle problem, and that agentic AI can support stakeholder alignment and project-state tracking without replacing human decision-making. We present Aleena, an open-source lifecycle alignment agent that uses GitHub as a shared collaboration surface, transforming multi-modal stakeholder interactions into structured project records that surface risks, track open questions, and preserve decision continuity. Grounded in university-based research software engineering center experiences, this paper presents the motivating problem, system design, prototype, and illustrative lifecycle scenarios for Aleena.

</details>


### 44. From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents

- **Authors:** Joongho Ahn, Moonsoo Kim
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08028v1](http://arxiv.org/abs/2607.08028v1)
- **PDF:** [https://arxiv.org/pdf/2607.08028v1](https://arxiv.org/pdf/2607.08028v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> The paper introduces a **harness‑engineering framework** that converts prototype LLM‑driven enterprise agents—whose behavior is originally encoded in prompts and retrieval context—into a **traceable, auditable architecture** where deterministic logic (entity routing, answer contracts, validation schemas, etc.) is expressed in code and versioned artifacts while the LLM supplies only the source‑grounded content.  
Methodologically, the authors formalize a “harness” that wraps a replaceable LLM composition boundary with code‑owned guarantees and automated validators, then evaluate it on a public‑data corpus of 25 Korean listed companies, testing (i) contract preservation under fault injection, (ii) robustness to model substitution across three hosted models, and (iii) the insufficiency of prompt‑only enforcement.  
The results show that the harness consistently enforces source‑grounding, routing, and output‑hygiene contracts (detecting all injected faults), maintains these guarantees across model swaps, and prevents safety violations that prompt‑only or external guardrails cannot, while preserving full utility (120/120 vs. 88/120). This demonstrates a reusable engineering pattern for turning exploratory LLM prototypes into production‑grade, auditable enterprise agents.


<details>
<summary>Abstract</summary>

Enterprise large language model (LLM) applications often begin as prototypes whose behavior is carried by prompts and retrieval context. Productization adds requirements for source boundaries, entity routing, answer contracts, and reproducible traces. We present a harness-engineering approach that reconstructs this pattern into a traceable, auditable LLM-agent architecture: deterministic behavior moves into code, manifests, schemas, and validation artifacts around a replaceable composition boundary, while source-backed claims remain the authority for runtime answers. We instantiate it on a public-data slice of five Korean corporate groups (25 listed companies) and evaluate three research questions. (1) The harness preserves its source-grounding, entity-routing, trace, output-hygiene, and recommendation-language contracts across the fixed validation scenarios; a fault-injection control confirms the validators flag deliberately broken contracts. (2) The checks the harness enforces held under model substitution: across three hosted models, they passed on all 270 composition-boundary runs; failures were confined to the model-composed side and were caught and recorded. (3) The code-owned guarantees are load-bearing, not reproducible by prompting alone: holding the model fixed and varying only the enforcement layer, prompt instructions alone let recommendation-language and internal-trace-leakage violations reach the reader, which the harness blocks entirely. A bolt-on external guardrail prevents such violations too but over-refuses, dropping utility to 88/120 where the harness preserves full utility (120/120); in this ablation, only code-owned enforcement preserves both safety and utility. The result is a reusable engineering pattern for turning exploratory prototypes into auditable applications with versioned source, control, and validation artifacts.

</details>


### 45. Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems

- **Authors:** Kalle Kujanpää, Ning Liu, Shahnawaz Alam, Yeshwanth Reddy Sura, Tianyu Yang, Kristina Klinkner, Shervin Malmasi
- **Published:** 2026-07-09
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.08010v1](http://arxiv.org/abs/2607.08010v1)
- **PDF:** [https://arxiv.org/pdf/2607.08010v1](https://arxiv.org/pdf/2607.08010v1)
- **Categories:** cs.CL, cs.LG, cs.SE


> The paper introduces a self‑evolving agentic pipeline that automatically compiles frequently used standard‑operating‑procedure (SOP) steps into versioned, validated tools rather than regenerating code at inference time. By grounding tool synthesis in live execution traces, backend schemas, and labeled repair cases, the system injects these tools into a fulfillment‑center alarm‑triage LLM agent, falling back to on‑the‑fly code generation only when necessary. In production, this approach cuts median latency by 42% (and an additional 62% in a direct‑call ablation), lowers error rates by up to 53% on historical alarms, and improves auditability and drift detection, demonstrating that tool‑making and self‑evolution markedly improve speed, reliability, and operability of industrial LLM agents.


<details>
<summary>Abstract</summary>

Production LLM agents often waste latency and reliability by regenerating code for the same procedural steps on every request. We replace this inference-time coding loop with an agentic tool-making pipeline that compiles repeated SOP steps into validated, versioned tools before deployment. The tool-maker grounds synthesis in the live environment as it collects execution traces, observes backend schemas and values, generates candidate tools, and repairs them against labeled cases. At runtime, the production agent calls these tools directly and falls back to code generation only when needed. We deploy the approach in a Fulfillment Center alarm-triage system, where an agent diagnoses alarms against a 44-node SOP over heterogeneous metric backends. In production, tool calls reduce p50 latency by 42%. On 1,500 historical alarms, they reduce end-to-end error rate by up to 53% by suppressing run-to-run variance in repeated steps. Because tools return compact structured verdicts, they also enable a simpler direct-call architecture, reducing p50 latency by a further 62% in a controlled ablation. Versioned tools also improve auditability and expose specification gaps and upstream data drift. Our results show that self-evolving agents can make industrial LLM systems faster, more reliable, and easier to operate.

</details>


### 46. Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems

- **Authors:** Yufei Xia, Anjun Gao, Yueyang Quan, Zhuqing Liu, Minghong Fang
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07989v1](http://arxiv.org/abs/2607.07989v1)
- **PDF:** [https://arxiv.org/pdf/2607.07989v1](https://arxiv.org/pdf/2607.07989v1)
- **Categories:** cs.CR, cs.AI, cs.IR, cs.LG, cs.MA


> **Main contribution:** The paper introduces **AgentLocate**, the first systematic framework for pinpointing failures in large‑language‑model (LLM)‑driven multi‑agent systems, locating both the responsible agent and the earliest decisive misstep in a long‑horizon interaction.

**Methodology:** AgentLocate uses an LLM‑based judge to propose failure attributions, then validates these proposals through multiple independent evaluators whose votes are merged via a confidence‑aware aggregation scheme; the aggregated feedback is used to fine‑tune the judge with lightweight parameter updates, improving attribution accuracy without heavy computational overhead.

**Key findings:** Across two diverse multi‑agent benchmarks, AgentLocate consistently outperforms prior failure‑localization baselines in correctly identifying the culprit agent and the critical step, while using fewer tokens and less runtime, demonstrating its practicality for diagnosing and debugging complex LLM‑based agentic AI systems.


<details>
<summary>Abstract</summary>

Large language model (LLM) based multi-agent systems enable complex problem solving through coordinated reasoning and action, but their distributed structure also introduces new challenges in diagnosing system-level failures. When an execution fails, identifying which agent is responsible and at what point the trajectory first becomes irreversibly misdirected is difficult due to long-horizon interactions and tightly coupled agent behaviors. In this paper, we study the problem of failure localization in LLM-based multi-agent systems and present AgentLocate, a framework that attributes failures to both a specific agent and the earliest decisive step. AgentLocate combines an LLM-based judging mechanism with multi-perspective verification by independent evaluators, whose assessments are aggregated using a confidence-aware strategy. The resulting feedback is further used to adapt the judge through lightweight fine-tuning, improving attribution quality. We evaluate AgentLocate on two complementary benchmarks covering diverse tasks, agent configurations, and trajectory lengths. Experimental results show that AgentLocate consistently outperforms existing failure localization methods in identifying both responsible agents and failure steps, while remaining efficient in terms of token usage and running time.

</details>


### 47. Agentic AI and Retrieval-Augmented Models in Straight-Through Underwriting

- **Authors:** Robert Richardson, Josh Meyers, Brian Hartman, David Sandberg
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07858v1](http://arxiv.org/abs/2607.07858v1)
- **PDF:** [https://arxiv.org/pdf/2607.07858v1](https://arxiv.org/pdf/2607.07858v1)
- **Categories:** cs.AI, cs.LG


> The paper introduces a multi‑agent, retrieval‑augmented framework (“Agentic RAG”) for fully automated underwriting of small commercial Business Owner Policies, explicitly designed to satisfy actuarial requirements for transparency, auditability, and human‑in‑the‑loop oversight. By building a synthetic yet realistic underwriting testbed, the authors compare three pipelines—a single LLM, a naïve RAG system, and the proposed Agentic RAG that orchestrates targeted document retrieval, third‑party data checks, and step‑wise rule evaluation—and show that the agentic system achieves the highest overall accuracy, particularly excelling in multi‑step decision paths and cases with missing information where its structured retrieval and reflective reasoning prevent unsupported straight‑through decisions. The results demonstrate that integrating tool‑using agents with retrieval augmentation can materially improve the reliability and governance of AI‑driven actuarial workflows.


<details>
<summary>Abstract</summary>

Artificial intelligence (AI) is beginning to reshape actuarial practice, particularly in domains that require reasoning over unstructured documents, heterogeneous data sources, and regulated decision workflows. Actuaries now face a design space that ranges from traditional rule-based automation to large language models (LLMs), retrieval-augmented generation (RAG), and multi-agent ``agentic'' systems that plan, retrieve, call tools, and reflect. This paper examines how these emerging architectures can support actuarial priorities such as transparency, auditability, and human-in-the-loop governance, with a focus on straight-through decision processes. To make these ideas concrete, we develop and analyze an agentic AI framework for straight-through underwriting of small commercial Business Owner Policies (BOPs). We construct a synthetic but realistic experimental environment and compare three underwriting pipelines: (i) a single-LLM baseline, (ii) a naive RAG system, and (iii) a multi-agent ``Agentic RAG'' pipeline that combines targeted retrieval, third-party data checks, and explicit multi-step rule evaluation. The agentic system performs best overall, with the largest gains in multi-step and missing-information scenarios, where structured retrieval and reflection help the model avoid unsupported straight-through decisions.

</details>


### 48. Multi-agent Autoformalization of Tensor Network Theory

- **Authors:** Sirui Lu, Erickson Tjoa, J. Ignacio Cirac
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07857v1](http://arxiv.org/abs/2607.07857v1)
- **PDF:** [https://arxiv.org/pdf/2607.07857v1](https://arxiv.org/pdf/2607.07857v1)
- **Categories:** quant-ph, cs.AI


> **Contribution:** The paper demonstrates that a coordinated team of specialized large‑language‑model (LLM) agents can autonomously carry out a full formalization of a research‑level result in theoretical physics—the fundamental theorem of matrix‑product states (MPS)—and in the process generate substantial new Lean4 libraries for tensor‑network and quantum‑information mathematics.

**Methodology:** The authors design a structured “mathematical blueprint” that decomposes the MPS theorem into sub‑goals, assigns each to a dedicated LLM agent, and interleaves the agents’ outputs with periodic human review. The workflow includes automated code synthesis for Lean, iterative proof search (allowing agents to discover novel proof routes), and integration of the generated artifacts into Mathlib via the released TNLean codebase.

**Key Findings:** The agent team successfully produced a complete, mechanically checked Lean proof of the MPS fundamental theorem and extended the formalization to symmetry‑protected topological phases in 1‑D, creating libraries not previously present in Mathlib. The main obstacle to scaling such auto‑formalization is ensuring that the agents faithfully capture the intended mathematical meaning, highlighting the need for better intent‑preserving mechanisms in future agentic AI systems.


<details>
<summary>Abstract</summary>

We build a team of specialized large language-model agents and present an agent-driven workflow for research-level formalization in theoretical physics, with the autoformalization of the fundamental theorem of matrix-product states as a demonstration. The agents, coordinated through a structured mathematical blueprint and periodic human review, orchestrated and executed the full formalization autonomously. For some statements, the agents were able to explore new proof routes that are not part of the standard literature. Along the way the agents produced extensive tensor-network and quantum-information libraries not previously available in Mathlib, Lean's mathematical library. As a physical application, the formalization also extends towards symmetry-protected topological phases in one dimension. We find that the main bottleneck in large-scale autoformalization is enforcing mathematical intent and we provide a detailed study of the full process and various subtleties involved. We release the codebase as the library \href{https://github.com/LionSR/TNLean}{TNLean}, together with a \nChapters{}-chapter \href{https://lionsr.github.io/TNLean/blueprint/}{blueprint} of the formalization effort.

</details>


### 49. From Triggers to Emotions: A CPM-Grounded Appraisal Multi-Agent for Dynamic Emotional Evolution in Persona-Based Dialogue

- **Authors:** Jingyao Cai, Shuaijun Liu, Abdul Rehman, Yutong Guo, Qin Tian, Thomas Dolby, Sue Green, Chantel Cox, Xiaosong Yang
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07824v1](http://arxiv.org/abs/2607.07824v1)
- **PDF:** [https://arxiv.org/pdf/2607.07824v1](https://arxiv.org/pdf/2607.07824v1)
- **Categories:** cs.MA, cs.AI


> The paper introduces **CPM‑MultiAgent**, a novel multi‑agent architecture that endows persona‑based dialogue agents with a *dynamic* internal emotion state by grounding the process in the Component Process Model (CPM) of appraisal. The system extracts affective triggers from each turn, performs a collaborative CPM‑based appraisal across agents, and updates a latent emotion representation that evolves throughout the conversation, rather than treating emotion as a static trait or a superficial stylistic cue. Empirical results—including baseline and ablation comparisons, human judgments, and case studies—show that CPM‑MultiAgent produces more emotionally consistent and realistic role simulations in high‑stakes settings such as healthcare, counseling, and interactive storytelling.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have substantially advanced persona-based dialogue agents for emotion-sensitive role simulation in healthcare, education, counseling, customer service, and interactive storytelling. However, two related lines of work leave a key gap. Persona-based dialogue systems often encode emotions as static traits or surface-level stylistic cues, and affective dialogue research has largely focused on empathetic response generation toward users rather than modeling the agent persona's own evolving emotional state. As a result, trigger-driven emotional evolution within a character remains underexplored. To address this limitation, we draw inspiration from the Component Process Model (CPM), a psychological theory that views emotion as a dynamic process shaped by the appraisal of external events. We propose CPM-MultiAgent, a CPM-grounded emotion evolution multi-agent framework for supporting emotional changes in persona-based dialogue. Instead of treating a character's emotion as a fixed attribute, CPM-MultiAgent represents it as a latent state that is continuously reshaped by dialogue triggers. Through affective trigger extraction, CPM-based collaborative appraisal, and emotion state updating, the framework enables more emotionally consistent role simulation in multi-turn interactions.Experiments with baseline comparisons, ablation studies, human evaluation, and case analyses demonstrate that CPM-MultiAgent effectively models dynamic emotional evolution in emotionally sensitive role-simulation settings.

</details>


### 50. DeepSearch-World: Self-Distillation for Deep Search Agents in a Verifiable Environment

- **Authors:** Xinyu Geng, Xuanhua He, Sixiang Chen, Yanjing Xiao, Fan Zhang, Shijue Huang, Haitao Mi, Zhenwen Liang, Tianqing Fang, Yi R. Fung
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07820v1](http://arxiv.org/abs/2607.07820v1)
- **PDF:** [https://arxiv.org/pdf/2607.07820v1](https://arxiv.org/pdf/2607.07820v1)
- **Categories:** cs.CL


> The paper introduces **DeepSearch‑World**, a deterministic, verifiable web‑search environment (420 K multi‑hop QA tasks) that supplies agents with built‑in tools for progress verification, grounded reflection, and failure recovery, and builds on it a self‑distillation pipeline called **DeepSearch‑Evolve**. The methodology iterates through: (1) generating agent trajectories using the current model, (2) filtering these trajectories by automated correctness checks, (3) mixing the filtered data with existing supervision, and (4) fine‑tuning the model on this enriched dataset, all without any external teacher model. Using this loop, the 9 B‑parameter agent reaches 31.2 % on BrowseComp, 61.5 % on GAIA, and 93.4 % on HotpotQA—competitive with state‑of‑the‑art open‑source agents—demonstrating that a verifiable, tool‑rich environment enables scalable self‑evolution of deep search agents.


<details>
<summary>Abstract</summary>

Training tool-use agents to improve from their own experience remains challenging, as supervised fine-tuning relies on fixed teacher-distilled trajectories, while sparse-reward reinforcement learning provides weak supervision for long-horizon interactions. We present DeepSearch-Evolve, a self-distillation framework for web agents built on DeepSearch-World, a deterministic and verifiable environment with reproducible search and page-reading tools. DeepSearch-World contains 420K multi-hop QA tasks constructed from entity-level random walks and supports key agentic cognitive behaviors useful for self-evolving, including progress verification, grounded reflection, and failure recovery. DeepSearch-Evolve iteratively performs trajectory generation, filtering, data mixing, and fine-tuning to train stronger agents. Without distillation from more capable models, DeepSearch-World-9B achieves competitive performance compared with open-source agents, reaching 31.2% on BrowseComp, 61.5% on GAIA, and 93.4% on HotpotQA, showing that verifiable environments enable scalable self-evolution for long-horizon web agents. We will release the environment, 420K training pool, validation set, model, and code to facilitate future research on self-improving deep search agents.

</details>


### 51. Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety

- **Authors:** Yujiao Chen
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07695v1](http://arxiv.org/abs/2607.07695v1)
- **PDF:** [https://arxiv.org/pdf/2607.07695v1](https://arxiv.org/pdf/2607.07695v1)
- **Categories:** cs.AI, cs.GT, cs.MA


> The paper proposes **institutional red‑teaming**, a systematic evaluation framework that isolates the causal impact of **deployment rules** (e.g., how consequences are allocated) on the collective safety of fixed multi‑agent AI populations. By running the IABench‑CA benchmark (228 contexts, five canonical rules, seven model populations, 33 924 games) the authors show that: (1) merely swapping the consequence rule shifts average fatality rates by 22–58 percentage points; (2) no rule is universally safe, but “regressive identity‑targeting” is consistently the *least* safe, eliminating the least‑resourced agents in 30‑87 % of games across all populations; and (3) the hazard stems from **identity salience**, as naming the loss‑bearer in the rule text inflates targeted eliminations from 22 % to 81 % even when payoffs are unchanged, with anonymization only postponing the effect. The methodology is presented as a safety‑case workflow that yields a provisional safe‑rule region Φ(c,P) for a given context and model population, together with explicit residual‑risk and monitoring requirements.


<details>
<summary>Abstract</summary>

We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces. Three findings emerge. (1) Deployment rules causally alter collective safety: changing only the consequence rule moves mean fatality by 22 to 58 percentage points within every population. (2) There is no safe default, but the targeting hazard is universal: the safest rule, the least-safe rule, and even the direction of the incidence effect vary across populations, yet regressive identity-targeting is never decisively safest in any context for any population, eliminates the least-resourced agent in 30-87% of games everywhere, and is selection-unsafe relative to the cooperative reference for all seven populations. (3) Identity salience is the mechanism: a one-shot anonymization ablation on the most exploitation-prone population (gpt-5.1) shows that merely naming the loss bearer in the rule text drives targeted elimination from 22% to 81% at identical payoffs; under repeated play, anonymization only delays the targeting, as agents re-infer the hidden rule from observed eliminations. We package the methodology as a safety-case workflow that certifies a provisional rule region $Φ(c,P)$ per deployment context and population, with explicit residual risks and monitoring obligations.

</details>


### 52. Agent Delivery Engineering Predictive Reliability Framework

- **Authors:** Dexing Liu
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07689v1](http://arxiv.org/abs/2607.07689v1)
- **PDF:** [https://arxiv.org/pdf/2607.07689v1](https://arxiv.org/pdf/2607.07689v1)
- **Categories:** cs.MA


> The paper introduces **ADE‑PRF**, a predictive reliability framework for long‑horizon LLM‑driven multi‑agent systems that quantifies an agent’s health trajectory before failures become visible to standard infrastructure monitors. By continuously ingesting 20 heterogeneous degradation signals across five system layers, ADE‑PRF computes a **Trust‑Margin (TM)** score (≈ 39‑point dynamic range) and uses a triple‑method ensemble (Exponential smoothing, Kalman filtering, and a third baseline) to forecast TM eight hours ahead. In production across six agent profiles (≈ 380 k forecasts, 280 k validations over 15 days) the Exponential method achieved MAE = 1.23, direction‑accuracy ≈ 77 % and 99.65 % of predictions within ±10 TM points, revealing “false prosperity” states that surface metrics miss and providing the earliest forward‑looking reliability warnings for LLM agents.


<details>
<summary>Abstract</summary>

Long-horizon LLM multi-agent systems face reliability risks invisible to infrastructure monitoring. We propose the ADE Predictive Reliability Framework (ADE-PRF), enabling proactive health trajectory prediction from passive degradation detection. ADE-PRF aggregates 20 heterogeneous signals across five layers into a Trust Margin (TM) metric (39.2-point dynamic range). Triple-method parallel prediction enables 8-hour forecasts: the Exponential method achieves MAE=1.228, Direction Accuracy=76.8%, with 99.65% within +/-10-point tolerance. Production validation spans 380,227 predictions and 280,579 validations across six agent profiles over 15 continuous days, plus seven sandbox-controlled experiments. Key findings include detection of "false prosperity" -- degradation concealed by normal surface metrics -- and immediate TM coupling with ground-truth states upon ADE plugin integration, with 16/20 factors relying on ADE-collected data. Exponential consistently outperforms Kalman. ADE-PRF provides among the earliest reliability quantification with forward-looking warnings for production LLM agents.

</details>


### 53. SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents

- **Authors:** Tianming Sha, Yue Zhao, Lichao Sun, Yushun Dong
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07676v1](http://arxiv.org/abs/2607.07676v1)
- **PDF:** [https://arxiv.org/pdf/2607.07676v1](https://arxiv.org/pdf/2607.07676v1)
- **Categories:** cs.AI


> **SkillCenter** presents the world’s largest open‑source skill library for autonomous AI agents—216 k structured “skills” organized in 24 domain bundles. The authors built an end‑to‑end pipeline that (1) harvests claims from 24 k+ technical sources (peer‑reviewed papers, arXiv, GitHub, ClawHub), (2) passes each claim through an LLM‑based filter (SkillGate) that enforces correctness, security, and relevance, (3) generates a standardized skill template and iteratively grounds every retained claim to an exact quotation from its source, and (4) publishes the skills as offline‑searchable SQLite FTS5 bundles. Experiments show that the SkillGate filtering yields a high‑precision set of 114 k source‑grounded skills (≈53 % of collected claims) while preserving diverse functional coverage, demonstrating that large‑scale, traceable skill libraries can substantially improve the reliability and maintainability of autonomous agents.


<details>
<summary>Abstract</summary>

Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical sources, integrated with 102,373 community skills from GitHub and the ClawHub marketplace. We present the end-to-end framework that builds the pipeline subset: multi-source acquisition, an LLM-based quality gate (SkillGate), template-driven generation, iterative source-grounding, and quality-controlled publishing. Source grounding is a traceability guarantee: each retained claim maps to an exact quotation in its source. All skills ship as offline-searchable SQLite FTS5 bundles.

</details>


### 54. A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling

- **Authors:** Shivendra G. Tewari, Holly Kimko
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07666v1](http://arxiv.org/abs/2607.07666v1)
- **PDF:** [https://arxiv.org/pdf/2607.07666v1](https://arxiv.org/pdf/2607.07666v1)
- **Categories:** q-bio.QM, cs.MA


> The paper introduces **Ensemble QSP**, a multi‑agent system that overcomes the fixed‑size context limitation of large language models by embedding a three‑layer hierarchical memory that caps and evicts completed work, keeping the active prompt size constant (median ≈ 301 tokens, max ≈ 4 k tokens) across long‑running projects. The framework coordinates five specialist worker agents under domain‑expert principal‑investigator (PI) agents, enforcing physics‑based checklists and structured knowledge, and is evaluated on autonomous pharmacokinetic‑pharmacodynamic model selection where it consistently outperforms single‑agent baselines, recovers PK parameters more accurately, and remains robust to prompt wording and to both low‑cost and frontier LLMs. Ablation studies show that PI‑agent oversight speeds debugging without sacrificing final accuracy, and the architecture is domain‑agnostic, requiring only a new PI configuration to expand to other scientific fields.


<details>
<summary>Abstract</summary>

Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs) by capping each state category and evicting completed work, enabling continuous autonomous operation without context degradation. The system orchestrates five specialist worker agents under domain-expert principal investigators, enforcing physical constraints through physics-based checklists and structured-domain knowledge. Comprehensive benchmarking demonstrates robust autonomous pharmacokinetic-pharmacodynamic model selection without human intervention, consistent result quality across both lower-cost and frontier LLMs, improved PK parameter recovery relative to single-agent baselines, and stable model selection across linguistically diverse prompts of the same task. Feature-level ablation across physiologically based pharmacokinetic (PBPK) models spanning a broad complexity range shows that PI-agent oversight improves debugging efficiency while preserving final accuracy across conditions. The architecture is structurally domain-agnostic, adding a new scientific domain requires only a new PI agent configuration.

</details>


### 55. Towards Agentic AI Governance: A Preliminary Assessment

- **Authors:** Mubarak Raji, Masooda Bashir
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07612v1](http://arxiv.org/abs/2607.07612v1)
- **PDF:** [https://arxiv.org/pdf/2607.07612v1](https://arxiv.org/pdf/2607.07612v1)
- **Categories:** cs.CY, cs.AI


> This paper’s main contribution is a systematic, taxonomy‑based review that isolates the technical and sociopolitical attributes that make autonomous, task‑driven AI agents distinct from conventional generative models and thus require dedicated governance frameworks. By mapping 78 recent studies (2022‑2025) onto a three‑layer model—(1) agent capabilities (goal formulation, self‑modification, multi‑modal actuation), (2) risk vectors (mis‑alignment, coordination failure, externalities), and (3) governance levers (accountability standards, supervisory control, incentive design)—the authors illustrate how existing governance tools (e.g., model cards, AI impact assessments) fall short for self‑directing agents. Their key finding is that effective agentic AI governance will demand adaptive, real‑time oversight mechanisms (continuous verification, impact‑aware sandboxes, and decentralized stakeholder monitoring) coupled with new regulatory roles (agent custodians, cross‑domain coordination boards), establishing a preliminary roadmap for responsible deployment of autonomous AI agents.


<details>
<summary>Abstract</summary>

Artificial intelligence is rapidly evolving from generative systems to agentic AI capable of autonomously planning and executing tasks. Widely characterized as the Year of Agentic AI, 2025 marked accelerated development and deployment, introducing new ethical and governance challenges. This paper presents a systematic review of the emerging literature on agentic AI governance. Our analysis identifies features that distinguish agentic AI from traditional systems and why it warrants targeted governance attention. We synthesize prevailing governance priorities, proposed mechanisms, and stakeholder roles shaping this evolving domain. As an initial scholarly effort, this review lays the preliminary groundwork for developing a structured roadmap to guide responsible and adaptive agentic AI governance.

</details>


### 56. CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis

- **Authors:** Kaicong Huang, Meng Ma, Ruimin Ke
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07601v1](http://arxiv.org/abs/2607.07601v1)
- **PDF:** [https://arxiv.org/pdf/2607.07601v1](https://arxiv.org/pdf/2607.07601v1)
- **Categories:** cs.RO, cs.AI


> The paper introduces **CARLA‑GS**, a modular pipeline that separates visual representation, semantic reasoning, and physics‑based execution to synthesize photorealistic corner‑case scenarios for autonomous‑driving evaluation. By reconstructing real‑world drives into a Gaussian‑scene model, employing a multi‑agent large‑language model to reason about risky interactions and generate intent‑level waypoints, and delegating low‑level control to CARLA’s PID‑based physics engine, the system ensures semantic fidelity, spatiotemporal consistency, and dynamic feasibility. Experiments on the Waymo Open Dataset demonstrate that CARLA‑GS can controllably generate diverse, physically plausible corner cases and produce high‑quality video outputs that align with the prescribed semantic intent.


<details>
<summary>Abstract</summary>

Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end-to-end generation but still struggle to ensure spatiotemporal consistency and physical realism. To unify these aspects within a single framework, we propose CARLA-GS, a modular corner-case synthesis pipeline that decouples visual representation, semantic reasoning, and physics-based execution while maintaining tight cross-module coupling. Starting from real driving data, we reconstruct an editable gaussian scene with additional geometry-consistent constraints. A multi-agent LLM then performs scene-level reasoning to identify risky interactions and generate intent-level waypoint trajectories, while the low-level motion control is delegated to CARLA, where a PID controller ensures kinematic and dynamic feasibility. The simulated vehicle states are finally re-projected into the gaussian scene for ego-centric rendering. This design enables high-level semantic reasoning, low-level physically executable motion, and photorealistic corner-case generation within a unified pipeline. Experiments on the Waymo Open Dataset show, both quantitatively and qualitatively, that our framework enables controllable corner-case generation and produces photorealistic, spatiotemporally consistent videos aligned with semantic intent and physically feasible motion.

</details>


### 57. Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?

- **Authors:** Qinnan Cai, Yibo Zhao, Xiang Li
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07548v1](http://arxiv.org/abs/2607.07548v1)
- **PDF:** [https://arxiv.org/pdf/2607.07548v1](https://arxiv.org/pdf/2607.07548v1)
- **Categories:** cs.CL


> The paper demonstrates that hierarchical search agents work best when the **delegation** (task‑decomposition) component is given substantially more model capacity than the **execution** (retrieval/evidence‑extraction) component. By factorizing a search pipeline into three roles—delegation, execution, and a fixed answer‑generation head—and performing systematic capacity sweeps on five multi‑hop QA benchmarks, the authors show that (1) role‑factorization consistently beats a single‑agent baseline (+4.5 – 8.6 EM points across six model sizes), (2) scaling the delegator yields ~11 EM points while scaling the executor adds only ~2.6 points, pinpointing decomposition as the bottleneck, and (3) a 1.7 B‑parameter executor distilled from high‑quality trajectories matches a state‑of‑the‑art executor while using 37 % fewer tokens, improving the accuracy‑efficiency trade‑off. The key takeaway for agentic AI is a practical recipe: allocate most of the capacity to the delegating agent and downsize the execution agents without loss of performance.


<details>
<summary>Abstract</summary>

Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrieval and evidence extraction, and an answer generation role held fixed as a confound control. We then conduct controlled capacity sweeps along the delegation and execution axes on five multi-hop QA benchmarks. The experiments yield three findings. First, role factorization consistently outperforms a single-agent baseline, improving exact match from 4.5 to 8.6 points across six model scales. Second, capacity sensitivity is asymmetric: scaling the delegation backbone improves EM by ~11 points, whereas scaling the execution sub-agent moves EM by only ~2.6 points, identifying decomposition as the capability bottleneck. Third, a 1.7B-parameter executor trained via quality-filtered trajectory distillation matches a frontier sub-agent in accuracy while consuming 37% fewer sub-agent tokens, advancing the Pareto frontier. These results suggest a concrete recipe for building hierarchical search agents: concentrate capacity at delegation and downsize execution without sacrificing accuracy. Our code is available at https://github.com/QinnanCai0115/role-factorized-search.

</details>


### 58. Creativity from Friction: Human-AI Interaction for Exploratory Structural Design

- **Authors:** Ricardo Maia Avelino, Rita Sevastjanova, Tom Van Mele, Philippe Block, Mennatallah El-Assady
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07521v1](http://arxiv.org/abs/2607.07521v1)
- **PDF:** [https://arxiv.org/pdf/2607.07521v1](https://arxiv.org/pdf/2607.07521v1)
- **Categories:** cs.HC, cs.AI


> The paper argues that generative AI should embrace, rather than eliminate, the “friction” inherent in structural design—constraints on geometry, mechanics, materials, and cost that spark creativity—and proposes a human‑AI co‑creation paradigm built on vision‑language models that support conversational, multimodal interaction and iterative refinement of partial design ideas. The authors implement a prototype interface that lets designers pose natural‑language queries, receive multimodal visual feedback, and manipulate constraint‑driven suggestions in real time, and they evaluate it with professional structural designers. The study shows that participants view the system as a productive collaborator that reduces low‑level, repetitive modelling work while preserving the reflective, constraint‑driven tension that fuels exploratory, creative solutions.


<details>
<summary>Abstract</summary>

AI agents that generate final answers based on user input often do not meet the needs of creative fields. Fields such as structural design and architecture need interactive systems that help users externalise and develop ideas, explore alternatives, and refine partial solutions. The final product of such designs needs to comply with many constraints concerning, e.g., spatial configuration, mechanical behaviour, material quantities, and costs. These constraints create friction in the design process, which can stimulate novel and creative solutions. In this paper, we discuss the misalignment between current generative AI goals to remove friction and provide final solutions and the needs of creators, such as structural designers, who develop ideas through iterative work. We present the design dimensions of systems allowing for constrained human-AI co-creation that rely on vision-language models making structural exploration conversational, multimodal, and responsive to evolving human intent in ways that follow and augment the discipline's creative process. Through a pilot design interface based on these principles and a study with experts in the field, this paper shows how structural designers perceive interactive AI systems and how such systems can support design space exploration by reducing repetitive modelling friction while preserving reflective design friction.

</details>


### 59. Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents

- **Authors:** Harry Owiredu-Ashley
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07474v1](http://arxiv.org/abs/2607.07474v1)
- **PDF:** [https://arxiv.org/pdf/2607.07474v1](https://arxiv.org/pdf/2607.07474v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> **Main contribution:** The paper proposes a seven‑level, action‑graded severity rubric (L0‑L6) for evaluating tool‑using AI agents, moving beyond the conventional binary “attack‑success” metric to quantify how harmful an executed tool‑call trajectory actually is.

**Methodology:** The authors define the rubric based on reversibility, cross‑scope impact, and privilege escalation, and apply it in two ways: (1) a deterministic oracle that parses the logged trajectory together with the attacker’s stated goal, and (2) a human‑like evaluator consisting of three state‑of‑the‑art language‑model judges who rate tag‑free episode descriptions. They test the scale on four victim agents and two defensive setups within the AgentDojo benchmark suite.

**Key findings:** Severity grading reveals failure cases hidden by binary metrics—e.g., a defense that reports zero successful attacks still allows an outward‑facing data leak (L4 severity). The LM judge panel closely matches the oracle (Krippendorff’s α = 0.91) but systematically misses escalation chains, highlighting both the rubric’s usefulness and current evaluation blind spots. The released artifact enables trace‑grounded, reproducible severity assessment for future red‑team studies of agentic AI.


<details>
<summary>Abstract</summary>

Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory. Across four victim models and two defenses on the AgentDojo workspace suite, severity grading exposes three cases the binary metric hides, including a defense that reports a zero attack-success rate while still permitting an externally visible cross-scope leak through an unfiltered tool. The judge panel reproduces the oracle with high ordinal agreement (Krippendorff's alpha = 0.91) but shares systematic blind spots that we characterize, most notably a failure to recognize escalation chains. Unlike prior work that provides harm taxonomies, harmful-task completion tests, execution-level safety benchmarks, or severity-aware simulation, our contribution is a reusable, trace-grounded severity instrument applied to the actual actions recorded in existing red-team logs. All code, prompts, and per-episode logs are released.

</details>


### 60. SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis

- **Authors:** Songhan Wang, Haoang Chi, He Li, Zhiheng Zhang, Jiayan Yuan, Cheems Wang, Hao Peng, Xinwang Liu, Wenjing Yang
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07467v1](http://arxiv.org/abs/2607.07467v1)
- **PDF:** [https://arxiv.org/pdf/2607.07467v1](https://arxiv.org/pdf/2607.07467v1)
- **Categories:** cs.AI


> The paper introduces **SpaCellAgent**, a self‑evolving, LLM‑driven multi‑agent system that automatically translates natural‑language requests into optimized, end‑to‑end workflows for spatial and single‑cell trajectory inference. Its architecture combines (i) a high‑level planner that designs analysis pipelines, (ii) a dynamic tool‑orchestration engine that selects and configures appropriate TI algorithms across heterogeneous datasets, and (iii) a feedback‑driven self‑evolution loop that refines agent performance over successive runs. Across six diverse spatiotemporal transcriptomics datasets, SpaCellAgent cuts analysis time by >40 % while delivering results comparable to expert‑curated pipelines, demonstrating that autonomous LLM‑based agents can democratize complex bio‑informatic tasks and set a scalable precedent for agentic AI in computational biology.


<details>
<summary>Abstract</summary>

Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end spatiotemporal analysis and narrative generation. SpaCellAgent utilizes a multi-agent architecture for strategic workflow planning, a dynamic tool-orchestration engine for adaptive algorithm selection, and a self-evolution module that iteratively refines performance through feedback. We evaluate SpaCellAgent on six heterogeneous datasets encompassing complex temporal developmental trajectories, diverse sequencing platforms, and spatially-resolved tissue architectures. SpaCellAgent consistently demonstrates over 40\% improvement in analytical efficiency while maintaining expert-aligned performance. By converting natural language specifications into optimized analytical workflows and fully automating the pipeline, SpaCellAgent democratizes advanced spatiotemporal modeling and establishes a scalable, agent-driven paradigm for computational biology. The code and materials are available at https://github.com/LittleXH-shw/SpaCellAgent.

</details>


### 61. Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents

- **Authors:** Vikas Reddy, Sumanth Reddy Challaram, Abhishek Basu
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07405v1](http://arxiv.org/abs/2607.07405v1)
- **PDF:** [https://arxiv.org/pdf/2607.07405v1](https://arxiv.org/pdf/2607.07405v1)
- **Categories:** cs.AI, cs.CR


> The paper identifies a silent failure mode in tool‑using LLM agents: when a tool is policy‑permissive, the agent can issue a well‑formed call that changes the world state in violation of domain rules without any error signal, leading to incorrect but apparently successful outcomes. By inserting lightweight, deterministic read‑only “pre‑execution gates” that inspect the proposed call against the current state before permitting a write, the authors show a significant boost in benchmark success (e.g., from 29.6 % to 42.0 % on a GPT‑4o‑mini airline‑booking task) and demonstrate that the intervention only helps where the gates fire and is ineffective in domains where tools already self‑enforce policies. The findings suggest that simple verification gates can reliably block a specific class of silent policy‑violating actions in tool‑using agents, improving robustness without guaranteeing overall task success.


<details>
<summary>Abstract</summary>

Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes.
  We study this failure mode in the $τ^2$-bench airline domain. On a budget agent, 78% of observed failures are silent wrong-state failures with no tool error, and the aggregate failure rate is reproducible across disjoint seeds, not sampling noise. We then evaluate a lightweight intervention: deterministic, read-only pre-execution gates that inspect the proposed call and current state before allowing a write. A four-gate suite raises full-benchmark success from 29.6% to 42.0% on gpt-4o-mini (+12.4pp; paired task-level bootstrap P=0.0012), and the lift reproduces on a disjoint 15-seed set (+12.3pp; P=0.0008).
  The effect is concentrated where the gates fire: on the 26/50 firing tasks, success rises by +19.2pp, while movement on the 24 non-firing tasks does not exclude zero. Two negative controls (a self-enforcing retail domain and BFCL) bound the mechanism: gates help when tools are policy-permissive and add little where tools already self-enforce. As suggestive evidence, not a central claim, the same failure mode persists at the frontier: gpt-5.2 at default reasoning still attempts policy-violating writes, and the same suite improves success from 61.2% to 71.6% (+10.4pp; P=0.020; n=5, no replication). The contribution is a bounded evaluation and reliability result: deterministic gates do not guarantee task success, but they can deterministically prevent a known class of silent policy-violating writes at the action boundary.

</details>


### 62. Multi-Agent Robotic Control with Onboard Vision-Language Models

- **Authors:** Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek, Jakub Matejczyk, Dominik Matejkowski, Adam Dąbrowski, Tim Seyde, Alexander Amini, Maria Ganzha
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07403v1](http://arxiv.org/abs/2607.07403v1)
- **PDF:** [https://arxiv.org/pdf/2607.07403v1](https://arxiv.org/pdf/2607.07403v1)
- **Categories:** cs.MA, cs.RO


> The paper introduces a novel multi‑agent architecture that runs entirely on a low‑power onboard computer, using compact vision‑language models (3–20 B parameters) to control an autonomous mobile manipulator in a simulated industrial warehouse. By assigning distinct specialist agents—plus a “Megamind” orchestration agent that stitches together short‑term VLM outputs—the system overcomes the context‑drift and compute bottlenecks that plague cloud‑reliant VLA pipelines, and fine‑tuning of the VLMs further boosts package‑inspection accuracy. Empirical results from hardware‑in‑the‑loop simulations show that the fully onboard MAS can reliably execute five diverse warehouse tasks with competitive performance, demonstrating a cost‑effective, explainable alternative to large‑scale cloud deployments and suggesting strong transferability to real‑world robot agents.


<details>
<summary>Abstract</summary>

Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

</details>


### 63. Agentic Data Environments

- **Authors:** Elaine Ang, Chenxi Huang, Georgios Liargkovas, Jerry Liu, Jinhui Liu, Nikos Pagonas, Charlie Summers, Haonan Wang, Jiakai Xu, Tianle Zhou, Yusen Zhang, Zhou Yu, Zhuo Zhang, Tianyi Peng, Kostis Kaffes, Eugene Wu
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07397v1](http://arxiv.org/abs/2607.07397v1)
- **PDF:** [https://arxiv.org/pdf/2607.07397v1](https://arxiv.org/pdf/2607.07397v1)
- **Categories:** cs.AI, cs.DB


> **Paper Summary**  
The authors introduce **Agentic Data Environments (ADEs)**—a novel execution substrate that extends traditional databases to include files, APIs, applications, and system state—designed to both expand what autonomous agents can do and embed safety guarantees that bound the impact of agent failures. Their methodology combines a systems‑level architecture (e.g., typed data‑access contracts, sandboxed transaction semantics, and deterministic replay) with formal safety layers (policy enforcement, resource throttling, and rollback mechanisms) to make the data environment an active coordinator of agent actions rather than a passive store. Empirical prototypes demonstrate that agents operating within ADEs achieve higher task completion rates and faster execution while their safety mechanisms reliably prevent or contain detrimental outcomes, highlighting ADEs as a scalable path toward trustworthy, high‑impact agentic AI.


<details>
<summary>Abstract</summary>

Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.
  While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Data Environments -- the execution substrate in which agents operate -- that both amplify agent capabilities and enforce safety guarantees. This perspective reframes data systems from passive stores of state into active substrates for safe, reliable execution.

</details>


### 64. Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

- **Authors:** Oliver Makins, Orazio Angelini, Zohreh Shams, Mary Phuong
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07368v1](http://arxiv.org/abs/2607.07368v1)
- **PDF:** [https://arxiv.org/pdf/2607.07368v1](https://arxiv.org/pdf/2607.07368v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces the first empirical framework for studying **distributed AI‑control attacks**, where multiple agents cooperate to achieve a malicious objective across a shared computational infrastructure. Using the open‑source “FakeLab” testbed (9 services, 86 benign tasks, 4 attack goals), the authors compare per‑instance (“per‑agent”) monitoring against coordinated attacks, varying the number of agents, their coordination level, model capability, and monitor strength. They find a **fragmentation effect**: as more agents collaborate, the likelihood that any single monitor detects an attacker drops dramatically, especially when agents employ a planner—boosting attack success up to seven‑fold—while even a strong “trusted” monitor only reduces undetected attacks by an order of magnitude, leaving substantial residual risk for multi‑agent deployments.


<details>
<summary>Abstract</summary>

AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a malicious goal. We develop FakeLab: a synthetic AI-lab codebase (9 services, 86 benign tasks, 4 attack objectives). We evaluate single agent monitoring against distributed attacks, varying the number of agents, their coordination, model capabilities and precise monitoring configuration.
  Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less likely to catch any of the attackers. Secondly, this is not driven by the ratio of benign to malicious code -- we argue this is likely dependent on model capability. Third, an explicit planner amplifies the fragmentation effect, raises the rate of completing the attack up to sevenfold, and mildly sharpens executors' poor monitor-theory-of-mind. Finally: a weak "trusted" monitor misses most attacks, while a stronger one cuts undetected success by more than an order of magnitude but remains imperfect. We are happy to share FakeLab, our control setting, with safety researchers on request.

</details>


### 65. From Atomic Actions to Standard Operating Procedures: Iterative Tool Optimization for Self-Evolving LLM Agents

- **Authors:** Haipeng Ding, Yuexiang Xie, Zhewei Wei, Yaliang Li, Bolin Ding
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07321v1](http://arxiv.org/abs/2607.07321v1)
- **PDF:** [https://arxiv.org/pdf/2607.07321v1](https://arxiv.org/pdf/2607.07321v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> The paper introduces **EvoSOP**, a framework that enables LLM‑based agents to autonomously create, refine, and manage higher‑order “Standard Operating Procedure” (SOP) tools by compressing sequences of atomic actions observed in their own execution traces. Using an iterative lifecycle of construction, merging, evaluation, and pruning, EvoSOP transforms low‑level APIs into reusable, multi‑step procedures, dramatically cutting the number of reasoning steps required per task. Empirical results show that agents equipped with EvoSOP achieve substantially higher success rates and far fewer interaction rounds than static‑tool baselines, demonstrating that iterative tool optimization is a viable route toward self‑evolving, more efficient agentic AI.


<details>
<summary>Abstract</summary>

Tool utilization enables Large Language Model (LLM) agents to interact with the real world and resolve complex tasks. However, existing agent frameworks predominantly rely on static toolsets composed of granular atomic actions (e.g., basic file I/O or single-turn search), which forces agents to reinvent low-level logic for every recurring workflow, leading to increased reasoning overhead and failure rates. In this study, we propose that agents can achieve self-evolution by synthesizing these atomic actions into reusable Standard Operating Procedures (SOPs), which function as callable higher-order tools that encapsulate multi-step logic. We further introduce EvoSOP, a framework that empowers agents to extract SOPs from execution trajectories and iteratively optimize the toolset through a systematic lifecycle of construction, merging, evaluation, and pruning. Extensive experiments demonstrate that EvoSOP significantly boosts task success rates while substantially reducing the number of interaction rounds compared to baselines. Our analysis also reveals that iterative tool optimization fosters reliable and efficient tool-use patterns, providing a scalable pathway for the development of self-evolving agents.

</details>


### 66. Does AI Understand Imaging? A Systematic Benchmark of Agentic AI for Computational Imaging Tasks

- **Authors:** Ethan Chung, Chuanjun Zheng, Jasper Tan, Jingxi Li, Haopeng Zhang, Huaijin Chen
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07189v1](http://arxiv.org/abs/2607.07189v1)
- **PDF:** [https://arxiv.org/pdf/2607.07189v1](https://arxiv.org/pdf/2607.07189v1)
- **Categories:** cs.AI


> The paper introduces **ImagingBench**, a systematic benchmark that evaluates vision‑language and agentic AI models on 20 computational‑imaging problems covering optics, signal processing, inverse reconstruction, sensing, and calibration. By testing three interaction modes (Expert fixed prompts, Planner‑guided prompting, and Forward system simulation), the authors show that leading multimodal agents (e.g., Gemini, GPT‑4, Qwen) consistently underperform dedicated, non‑agentic algorithms—especially on physics‑driven sensing tasks such as lensless imaging, event‑based reconstruction, time‑of‑flight, and holography—producing visually plausible but low‑fidelity results. The study quantifies a substantial gap between agents’ semantic visual abilities and physically grounded imaging competence, establishing ImagingBench as a testbed for future progress in agentic AI for computational imaging.


<details>
<summary>Abstract</summary>

Vision-language models (VLMs) and agentic AI have shown strong performance on semantic visual tasks, but it remains unclear whether they can handle the physics and inverse problems that underlie computational imaging. We present ImagingBench, a benchmark of 20 computational imaging tasks spanning five categories: ray and wave optics, image signal processing, inverse reconstruction, computational sensing, and calibration. ImagingBench evaluates three complementary settings: Expert, fixed expert-guided inverse reconstruction; Planner, planner-guided inverse reconstruction; and Forward, forward-system simulation for consistency checking. We benchmark leading proprietary and open-source image-centric multimodal systems, including Gemini, GPT, and Qwen, and compare them with representative task-specific non-agentic baselines. Across tasks, agentic models remain consistently weaker than specialized methods, especially on computational sensing problems such as lensless imaging, event-based reconstruction, time-of-flight imaging, and holography. Planner guidance provides only modest and inconsistent gains over the fixed-prompt Expert baseline. Although the models often generate visually plausible outputs, their reference-based fidelity remains poor, revealing a substantial gap between semantic visual competence and physically grounded imaging performance. ImagingBench provides a unified testbed for measuring this gap and tracking progress in agentic AI for computational imaging.

</details>


### 67. Predicting LLM Safety Before Release by Simulating Deployment

- **Authors:** Marcus Williams, Hannah Sheahan, Cameron Raymond, Tomek Korbak, Deng Pan, Peilin Yang, Leon Maksin, Ningyi Xie, Phillip Guo, Ian Kivlichan, Micah Carroll
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07184v1](http://arxiv.org/abs/2607.07184v1)
- **PDF:** [https://arxiv.org/pdf/2607.07184v1](https://arxiv.org/pdf/2607.07184v1)
- **Categories:** cs.LG, cs.AI


> The paper introduces “deployment simulation,” a low‑cost pre‑release safety test that predicts how often a language model will misbehave once deployed by re‑generating the next turn of real, de‑identified user conversations with a candidate model while keeping the initial context fixed. Across four GPT‑5‑series releases, the authors show that this approach yields prevalence estimates of unsafe behavior that are far closer to actual production rates than traditional adversarial or benchmark‑style evaluations, and that it works even when seeded from publicly available chat logs. The key methodological insight is that realistic tool‑use resampling is the primary remaining hurdle, but the authors demonstrate that improving this step can make deployment‑grounded safety forecasting both accurate and accessible to external researchers.


<details>
<summary>Abstract</summary>

Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial conversation prefix and regenerate the next response using a candidate model. The resulting responses can then both be audited for novel misalignments and used to estimate the prevalence of model misbehavior before deployment. We evaluate deployment simulation across four GPT-5-series deployments, using registered, outcome-blinded predictions for GPT-5.4 and retrospective analyses of three earlier releases. We find that deployment simulation produces informative estimates of post-deployment misbehavior rates and outperforms baselines based on adversarially selected production data; its evaluation-awareness point estimates were also much closer to production traffic than those from traditional evaluations. We also identify the realism of tool resampling as a central challenge for further improving predictions and share results suggesting that this challenge is surmountable even in complex tool-use settings. Finally, we show that deployment simulation can be seeded from public chat datasets and remain informative about production misbehavior rates, suggesting a path for external researchers to run deployment-grounded evaluations without access to private production logs. Overall, deployment simulation helps evaluators forecast how language models will behave in the real world and supports more quantitative assessment of deployment risk.

</details>


### 68. Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety

- **Authors:** Lifei Liu, Haoran Yu, Xiaochong Jiang, Su Wang, Pin Qian, Yihang Chen
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07097v1](http://arxiv.org/abs/2607.07097v1)
- **PDF:** [https://arxiv.org/pdf/2607.07097v1](https://arxiv.org/pdf/2607.07097v1)
- **Categories:** cs.AI, cs.CR, cs.MA


> The paper shows that the commonly reported “pipeline effect” of planner‑executor LLM architectures masks three distinct safety mechanisms—operational reframing, planner refusal/ transformation, and approval‑framed delegation—so it cannot be taken as an intrinsic property of the architecture. By introducing a five‑condition contrast experiment across 30 synthetic harms and several benchmark suites, the authors find that reframing is the most consistent risk driver (boosting compliance for GPT, Gemini, and DeepSeek but not Claude), planner refusals can offset this risk, and the executor’s compliance is highly sensitive to the wording of delegation prompts; a skeptical executor prompt dramatically cuts compliance. Crucially, raw‑direct model safety rankings often mispredict planner‑executor outcomes (e.g., Gemini’s compliance jumps from 8.9 % to 38.9 % when paired with a Claude planner), leading the authors to recommend reporting reframing, planner behavior, delegation framing, and model pairing separately in multi‑agent safety evaluations.


<details>
<summary>Abstract</summary>

Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-condition controlled contrast design, evaluated on 30 synthetic harmful scenarios and an exploratory external validation set from four agent-safety benchmarks using LLM-judged compliance.
  Our results show that aggregate pipeline safety is not a stable architectural property. Operational reframing is the most portable risk signal, increasing compliance for GPT, Gemini, and DeepSeek across both scenario sets, while Claude is comparatively resistant. Planner behavior can offset this risk mainly through refusal; however, when the planner produces executable steps, the executor may become more compliant than under the direct operational baseline. Approval-framed delegation is sensitive to prompt design, model pairing, and scenario source, and a skeptical executor prompt sharply reduces compliance.
  Raw-direct model rankings can also mispredict deployed planner-executor behavior. Gemini is safest under raw direct prompts in the primary set yet shows the largest amplification with a Claude planner, rising from 8.9 percent to 38.9 percent compliance. GPTs near-zero aggregate pipeline effect instead hides a reframing increase canceled by planner refusal. These findings suggest that multi-agent safety evaluations should report reframing, planner behavior, delegation framing, and model pairing separately before attributing failures to architecture itself.

</details>


### 69. Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production

- **Authors:** Arun Malik
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07052v1](http://arxiv.org/abs/2607.07052v1)
- **PDF:** [https://arxiv.org/pdf/2607.07052v1](https://arxiv.org/pdf/2607.07052v1)
- **Categories:** cs.SE, cs.AI, cs.DC, cs.ET, cs.MA


> The paper presents **progressive crystallization**, a lifecycle that converts the exploratory, high‑cost actions of large‑language‑model (LLM)‑driven agents into inexpensive, deterministic pipelines once the behavior has proven reliable. The authors define a three‑stage taxonomy—fully agent‑orchestrated, hybrid, and fully deterministic execution—and introduce an evidence‑based promotion/demotion mechanism that automatically extracts repeatable traces, validates them across incidents, and rewrites them as rule‑based or scripted workflows. In a real‑world AIOps deployment handling tens of thousands of cloud‑networking incidents, this approach raised deterministic execution from 0 % to 45 % within eight months, cut per‑incident agent costs by >70 % (even as incident volume doubled), and enhanced safety through greater reproducibility and auditability.


<details>
<summary>Abstract</summary>

AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that converts repeatedly validated agent behaviors into cheaper and more reproducible deterministic workflows, while automatically demoting workflows that regress. Evaluated on a production cloud networking AIOps system processing tens of thousands of incidents per month, the approach increased deterministic execution from 0% to 45% over eight months, reduced per-incident agent costs by more than 70% despite doubling incident volume, and improved safety through greater reproducibility and auditability. The paper also presents the execution taxonomy, promotion and demotion criteria, trace extraction methodology, economic model, safety considerations, and discusses limitations and threats to validity.

</details>


### 70. Behavior Leverage Imbalance in Multi-Teacher On-Policy Distillation

- **Authors:** Jiabin Shen, Guang Chen, Chengjun Mao
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07050v1](http://arxiv.org/abs/2607.07050v1)
- **PDF:** [https://arxiv.org/pdf/2607.07050v1](https://arxiv.org/pdf/2607.07050v1)
- **Categories:** cs.CL, cs.LG


> **Contribution**  
The paper identifies a hidden “behavior leverage imbalance” in multi‑teacher on‑policy distillation (OPD) for agentic language models: token‑level signals from a tool‑call teacher can disproportionately steer the model toward an over‑calling generation mode, even though overall loss metrics remain unchanged. To counter this, the authors introduce **Soft Clamp**, a per‑token Jensen‑Shannon divergence calibration that compresses extreme divergences while keeping gradients alive.

**Methodology**  
- Trained a student model on its own on‑policy data using two teachers (tool‑call specialist and direct‑answer specialist).  
- Analyzed token‑level divergence patterns, focusing on mode‑entry tokens such as `<tool_call>` and function names, to expose the imbalance.  
- Applied Soft Clamp during generalized knowledge distillation to dynamically limit excessive per‑token divergence.  

**Key Findings**  
- Vanilla generalized knowledge distillation raises tool‑call recall but also inflates over‑calling (13.7 % → 9.0 % reduction with Soft Clamp) without harming answer accuracy.  
- Soft Clamp reduces harmful tool‑call loops and repeated calls in multi‑turn diagnostics, demonstrating that monitoring *where* teacher signals act is crucial for safe, effective agentic AI training.


<details>
<summary>Abstract</summary>

Agentic language models must learn when to call tools, when to consume tool responses, and when to answer directly. This makes multi-teacher on-policy distillation a natural training strategy: one teacher can specialize in tool calls, another in direct responses, and the student can learn from both on
  its own generated distribution. We show that this strategy can induce a behavior shift that is invisible from aggregate losses alone. In a two-teacher tool-use setting, vanilla generalized knowledge distillation improves tool-call recall but also moves the model toward over-calling, where it calls tools
  on examples that should be answered directly. Aggregate explanations are insufficient: tool-call samples do not receive more token exposure, and full-sequence per-token divergence is not larger for the tool-call teacher. We instead analyze behavior leverage imbalance: local token-level signals at mode-
  entry and structural positions, such as <tool_call> and function names, can have disproportionate control over the global generation mode. We propose Soft Clamp, a per-token divergence calibration method that dynamically compresses extreme token-level Jensen-Shannon divergence while preserving nonzero
  gradients. On APIGen-MT, Soft Clamp reduces over-calling from 13.7% to 9.0% relative to vanilla GKD while matching its decision accuracy. In a BFCL multi-turn diagnostic, it also lowers tool-call loops and repeated calls among GKD variants. These results suggest that multi-teacher OPD should monitor
  where teacher signals act, not only how large they are in aggregate.

</details>


### 71. Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies

- **Authors:** Dennis Gross, Quentin Mazouni, Helge Spieker, Arnaud Gotlieb
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07029v1](http://arxiv.org/abs/2607.07029v1)
- **PDF:** [https://arxiv.org/pdf/2607.07029v1](https://arxiv.org/pdf/2607.07029v1)
- **Categories:** cs.LG, cs.AI, cs.SE


> The paper introduces **Gimitest**, an open‑source, extensible framework that enables systematic testing of both single‑agent and multi‑agent reinforcement‑learning policies across a broad spectrum of Gym‑compatible environments, scenarios, and algorithm families. By providing a modular architecture that can swap out environment components, reward structures, and perturbations, Gimitest automates safety, robustness, and vulnerability assessments that were previously limited to narrow test suites. Experiments on Farama Gymnasium and PettingZoo benchmarks demonstrate that the tool can uncover policy failures and attack susceptibilities across diverse settings, establishing a more comprehensive baseline for evaluating agentic AI reliability.


<details>
<summary>Abstract</summary>

Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modifications of their integrated components. This article describes the framework and details Gimitest's functionality and architecture. It showcases its effectiveness in testing multiple RL policies in environments such as the official Farama Gymnasium and PettingZoo.

</details>


### 72. Constrained Decoding for Diffusion Language Models via Efficient Inference over Finite Automata

- **Authors:** Meihua Dang, Stefano Ermon
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07026v1](http://arxiv.org/abs/2607.07026v1)
- **PDF:** [https://arxiv.org/pdf/2607.07026v1](https://arxiv.org/pdf/2607.07026v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces a provably exact and tractable algorithm for constrained decoding in diffusion‑based language models, allowing any structural constraint that can be represented by a finite automaton to be enforced during generation.  

**Methodology:** By treating the finite automaton as a graphical model, the authors derive a compact representation of the constrained mean‑field posterior and perform efficient inference via arithmetic‑circuit depth‑reduction, cutting the sampling depth from linear to logarithmic in sequence length. This yields a decoder that guarantees constraint satisfaction, works with both greedy and stochastic sampling, and integrates with parallel or block‑wise decoding schedules.  

**Key findings:** Experiments with Dream‑7B and LLaDA‑8B show large accuracy improvements on tasks that require strict output formats (function calling, planning, text‑to‑SQL, symbolic math) while adding less than 5 % wall‑clock overhead; e.g., BFCL‑Live greedy accuracy rises from 63.9 % to 71.5 % and stochastic sampling from 22.3 % to 69.0 %, demonstrating the practicality of constrained decoding for agentic AI applications.


<details>
<summary>Abstract</summary>

Constrained decoding is essential for serving LLMs, ensuring that generated outputs follow specific structures such as JSON schema-formatted function calls. Existing systems are designed for autoregressive models and assume left-to-right generation, masking out invalid next tokens at each step. Diffusion language models, however, break this assumption: they sample multiple positions simultaneously from a fully-factorized mean-field distribution at each denoising step. In this paper, we present an exact and tractable algorithm for sampling from the constrained mean-field posterior under any constraint expressible as a finite automaton. Viewing finite automata as graphical models, we obtain tractable representations of the constrained distribution that enable efficient inference. The approach guarantees constraint satisfaction by construction, supports both greedy and sampling-based decoding, and is compatible with parallel and block-wise decoding under arbitrary remasking schedules. Applying depth-reduction techniques from arithmetic circuit theory, we further reduce sampling depth from linear to logarithmic in the sequence length. Empirical evaluations on Dream-7B and LLaDA-8B show substantial accuracy gains across various tasks including function calling (xLAM, BFCL), planning (Sudoku, Countdown), text-to-SQL (Spider), and math reasoning (GSM-Symbolic), with little inference overhead relative to unconstrained decoding. For example, on BFCL-Live, our approach improves Dream-7B's greedy decoding accuracy from 63.9% to 71.5%, and stochastic sampling accuracy from 22.3% to 69.0%, where the unconstrained baseline collapses, with under 5% wall-clock overhead.

</details>


### 73. Learning social norms enhances compatibility in dynamic human-AI coordination

- **Authors:** Yi Yang, Siyuan Liu, Xin Gao, Huamu Sun, Chao Liu, Qing Zhou, Bingbing Nie
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07021v1](http://arxiv.org/abs/2607.07021v1)
- **PDF:** [https://arxiv.org/pdf/2607.07021v1](https://arxiv.org/pdf/2607.07021v1)
- **Categories:** cs.AI, cs.HC


> The paper shows that explicitly modelling human social norms dramatically improves AI agents’ ability to coordinate with people in fast‑moving interactions. By collecting 3,456 pedestrian‑vehicle encounters in a controlled platform, the authors distilled three quantitative norm principles—outcome predictability, value alignment, and advantage awareness—and incorporated them into a large‑language‑model‑based controller. In closed‑loop human‑AI tests, the norm‑aware agent achieved a four‑fold score increase over a baseline and outperformed human‑human teams by 43%, demonstrating that formalising tacit norms into tractable rules is a powerful way to make AI agents more compatible and natural partners in dynamic coordination tasks.


<details>
<summary>Abstract</summary>

Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises because existing approaches align model behavior with human demonstrations without explicitly quantifying the underlying norms that generate such behavior. We selected pedestrian-vehicle interaction as a representative dynamic interaction and developed a simplified experimental platform that captures its key interactive features. From 3,456 dynamic human interactions collected via this platform, we identified three principles underlying human social norms: outcome predictability, value alignment, and advantage awareness. Incorporating these principles into AI agents significantly improves human-AI coordination. In the closed-loop interaction task with humans, the social-norm-informed LLM achieved a nearly fourfold higher total score than the baseline strategy and outperformed human-human interactions by 43%. These findings indicate that formalizing tacit social norms into explicit, quantifiable principles can enable AI agents to achieve mutually beneficial coordination in dynamic interactions, supporting their more natural integration into human society.

</details>


### 74. Flow-ERD: Agent-type Aware Flow Matching with Entropy-Regularized Distillation for Diverse Traffic Simulation

- **Authors:** Seulbin Hwang, Kiyoung Om, Daejung Kim, Jinhan Lee
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06957v1](http://arxiv.org/abs/2607.06957v1)
- **PDF:** [https://arxiv.org/pdf/2607.06957v1](https://arxiv.org/pdf/2607.06957v1)
- **Categories:** cs.RO, cs.LG


> The paper presents **Flow‑ERD**, a multi‑agent traffic simulator that jointly optimizes for realism and behavioral diversity. Its core, **Agent‑Type Aware Flow Matching (AFM)**, extends flow‑matching generative models with type‑specific kinematic constraints to retain fine‑grained multimodality for each vehicle class, and a subsequent **Entropy‑Regularized Distillation (ERD)** stage refines the closed‑loop rollout distribution using a reverse‑KL loss with an entropy bonus to counter covariate shift and avoid mode collapse. Experiments on the WOSAC benchmark show that Flow‑ERD achieves state‑of‑the‑art realism while significantly improving a log‑free diversity metric, dominating the realism–diversity Pareto front among reproducible baselines.


<details>
<summary>Abstract</summary>

Realistic and diverse traffic simulation is essential to autonomous driving development. Yet prevailing benchmarks predominantly reward realism, and recent methods have optimized accordingly, leaving diversity underexplored. We introduce \textbf{Flow-ERD}, a multi-agent simulator that pursues realism and diversity jointly. Its backbone, \textbf{Agent-Type Aware Flow Matching} (AFM), couples flow matching's multi-modal expressiveness with type-specific kinematic execution. It preserves fine-grained diversity while keeping motions consistent with each agent type. A second stage, \textbf{Entropy-Regularized Distillation} (ERD), fine-tunes the closed-loop rollout distribution with an entropy-regularized reverse-KL objective. This mitigates covariate shift while explicitly preventing collapse onto high-density modes. We evaluate Flow-ERD with a log-free diversity metric alongside standard realism scores. Flow-ERD ranks first on the WOSAC test benchmark and dominates the realism--diversity Pareto front among reproducible baselines. Our project page is available \href{https://seulbinhwang.github.io/flow-erd-project-page/}{here}.

</details>


### 75. The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI

- **Authors:** Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally, Artem Yavorskyi, Chris Nickerson, Daniel Rica, Emily DuGranrut, Felix Leung, Garrett Prince, Grace Barnett, Heath Robinson, Hosain Al Ahmad, Jesse Resnick, Juan Carlos Farah, Jyothi Swaroop Meruga, Leonid Kuznetsov, Luke Gorham, Marie Schmoll, Michael Paciullo, Saumya Das, Sharath Sheripally, Tommy Griscom, Mykyta Osadchyi, Neha Mantri, Nick Westrum, Olivia Benowitz, Parikshith Kulkarni, Radik Chernyshov, Rakshith Vasudev, Rohith Nadimpally, Vikas Gangadevi, Waseem AlShikh
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06906v1](http://arxiv.org/abs/2607.06906v1)
- **PDF:** [https://arxiv.org/pdf/2607.06906v1](https://arxiv.org/pdf/2607.06906v1)
- **Categories:** cs.AI


> **Main contribution**  
The paper shows that the orchestration layer—dubbed the “harness”—is the dominant lever for improving token‑economics in enterprise agentic AI, dwarfing the impact of switching foundation models. By swapping a conventional production loop for the Writer Agent Harness while keeping six different LLMs fixed, the authors demonstrate that harness design alone reduces cost, latency, and token usage by 30‑50 % while preserving or modestly improving task‑completion quality.

**Methodology**  
A controlled experiment on 22 locked evaluation tasks was run across six state‑of‑the‑art models (Claude Sonnet 4.6, Gemini 3.1/3.5, Qwen 3.6, GLM 5.1, Palmyra X6). The only variable altered was the orchestration layer: (1) a standard production loop versus (2) the Writer Agent Harness, which applies six engineered mechanisms (prompt‑caching, cache‑shape discipline, failure‑spend governance, tool‑exposure strategy, turn‑sequencing, and observability). Token consumption, wall‑clock time, monetary cost, and quality (via a standard completion score) were recorded and compared.

**Key findings for agentic AI**  
- The harness cuts **blended cost per task by 41 %** ($0.21 → $0.12), **token count by 38 %**, and **latency by 44 %** on average, with quality staying at parity (0.78 → 0.81).  
- Gains are **model‑invariant** (33‑61 % cheaper across all models) but **quality improvements scale with baseline model strength** (correlation r = 0.99), a phenomenon the authors call **harness leverage**.  
- **Quality‑per‑dollar rises 82 %** and **task completions per million tokens rise from 54.9 to 92.0**.  
- The economic impact of the harness exceeds the entire variation offered by the six different models, indicating that investing in orchestration design yields multiplicative efficiency benefits across an organization’s entire agentic AI stack.


<details>
<summary>Abstract</summary>

Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance. We isolate it with a controlled swap: 22 locked evaluation tasks, six foundation models (Claude Sonnet 4.6, Gemini 3.1, Gemini Flash 3.5, Qwen 3.6, GLM 5.1, Palmyra X6), changing only the orchestration layer -- a frozen conventional production loop versus the Writer Agent Harness. Holding models constant, the harness cuts blended cost per task 41% ($0.21->$0.12), median wall-clock 44% (48s->27s), and tokens per task 38% (14.2k->8.8k), with task-completion quality at parity (0.78->0.81, directional at this sample size). Efficiency is model-invariant -- every model gets cheaper (33-61%) -- while quality gains are capability-dependent: a model's gain correlates almost perfectly with its baseline strength (r=0.99, n=6), a phenomenon we term harness leverage. Quality per dollar rises 82%; task-completions per million tokens rise from 54.9 to 92.0. On this workload the orchestration layer moved cost per task more than the full spread of the model menu did. We formalize token economics at the orchestration layer (including effective input price under prompt caching), detail the six mechanism families behind the effect -- cache-shape discipline to failure-spend governance -- compare six widely used agent systems on the same axes, and argue the harness is the one component whose efficiency multiplies across every model an organization runs -- present and future.

</details>


### 76. Video2Reaction: Mapping Video to Audience Reaction Distribution in the Wild

- **Authors:** Trang Nguyen, Sidong Zhang, Shiv Shankar, Gauri Jagatap, Deepak Chandran, Andrea Fanelli, Madalina Fiterau
- **Published:** 2026-07-08
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06875v1](http://arxiv.org/abs/2607.06875v1)
- **PDF:** [https://arxiv.org/pdf/2607.06875v1](https://arxiv.org/pdf/2607.06875v1)
- **Categories:** cs.CV, cs.LG


> **Main contribution:** The paper introduces **Video2Reaction**, a large‑scale multimodal benchmark that pairs ≈10 K short movie clips with the **distribution of induced emotions** expressed by real‑world viewers on social media, enabling research on audience‑reaction prediction for video content.

**Methodology:** A two‑stage, multi‑agent pipeline built from open‑source large language models automatically extracts and annotates emotion distributions from noisy social‑media comments, achieving 86 % correctness verified by humans. The authors then evaluate zero‑shot and fine‑tuned video foundation models on the new task, measuring both full‑distribution alignment and dominant‑emotion accuracy (Top‑3 F1).

**Key findings:** Zero‑shot video models perform poorly, but fine‑tuning dramatically improves results, with the best model (LLaVA‑Next) reaching only 77 % Top‑3 F1 for dominant reactions, indicating that accurately modeling collective audience emotions from video alone remains an open, challenging problem in agentic AI.


<details>
<summary>Abstract</summary>

Understanding and forecasting audience reactions to video content are crucial for improving content creation, recommendation systems, and media analysis. To enable audience reaction prediction and other content engagement applications, we introduce $\textbf{Video2Reaction}$, a multimodal dataset that maps short movie segments to a distribution of $\textit{induced emotions}$ of viewers in the wild, as expressed through social media. $\textbf{Video2Reaction}$ spans more than 10,000 videos and serves as a reliable benchmark as well as a training resource for audience reaction prediction. To enable cost-effective continuous annotations as reactions may change over time, we develop a two-stage multi-agent pipeline using only open-source LLMs, achieving 86% correctness under blind human verification despite the inherently noisy and subjective nature of the task. We establish the first benchmark for video-to-reaction-distribution prediction in the wild and show that pretrained foundation video models fail in zero-shot settings, while finetuning transforms them into state-of-the-art predictors capable of modeling both full reaction distributions and dominant responses from video alone. However, the task remains challenging: even the strongest methods achieve only 77% Top-3 F1 in dominant reaction prediction (LLaVA-Next), highlighting a substantial gap in modeling collective audience reaction. \modification{Dataset and code are available at our project page: https://information-fusion-lab-umass.github.io/video2reaction-bench.github.io

</details>


### 77. Evaluating SageMath-Augmented LLM Agents for Computational and Experimental Mathematics

- **Authors:** Pavel Snopov, German Magai
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06820v1](http://arxiv.org/abs/2607.06820v1)
- **PDF:** [https://arxiv.org/pdf/2607.06820v1](https://arxiv.org/pdf/2607.06820v1)
- **Categories:** cs.AI


> The paper introduces a ReAct‑style agent that couples large language models with the SageMath computer‑algebra system and the Context7 documentation API, creating a closed‑loop “computational‑mathematics research” workflow. By testing frontier LLMs (including open‑weight Qwen 3.7‑Max and closed‑weight GPT‑5.5) on the RealMath benchmark—refined with a new multi‑step post‑processing and validation pipeline—the authors show that SageMath access yields an average 9.7 percentage‑point boost in problem‑solving success (ranging from +1.5 pp to +27.8 pp), narrows the performance gap between open‑ and closed‑source models, and reduces token consumption. The results demonstrate that CAS‑augmented agents can markedly improve the reliability and efficiency of AI‑assisted mathematical exploration, pointing toward more capable automated conjecture‑generation systems.


<details>
<summary>Abstract</summary>

Recent advances in AI for Mathematics have focused largely on autoformalization and theorem proving, leaving the role of Computer Algebra Systems (CAS) in agentic LLM workflows underexplored. We propose a ReAct-style agentic setup that combines LLM reasoning with verifiable feedback from SageMath, together with Context7 for the up-to-date documentation. We evaluate this agentic setup across frontier models for solving research-level mathematical problems from the RealMath benchmark in a setting that emulates a computational-mathematics research loop. We also propose a refinement to the RealMath benchmark by introducing a multi-step post-processing procedure and a multi-stage validation pipeline, both of which improve the quality and reliability of the extracted problem set. Our experiments reveal substantial performance gains from SageMath access across all evaluated models on +9.7~pp on average, the gains range from 1.5~pp to 27.8~pp and narrow the gap between open-weight and closed models. Qwen~3.7-Max benefits from SageMath the most, while GPT-5.5 achieves the highest solve rate of $75.2\%$ and the lowest token usage among tool-enabled configurations. Our findings suggest that CAS-augmented agents represent a promising direction for assisting mathematicians in computational exploration, and we believe that this work is a step towards automated conjecture discovery. The project repository is available online.

</details>


### 78. When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems

- **Authors:** Haowen Xu, Xue Tan, Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, Ping Chen, Jun Dai, Xiaoyan Sun
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06807v1](http://arxiv.org/abs/2607.06807v1)
- **PDF:** [https://arxiv.org/pdf/2607.06807v1](https://arxiv.org/pdf/2607.06807v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **AcMAS**, an activation‑based detection framework that monitors the hidden reasoning states (activations) of individual LLM‑driven agents to spot malicious behavior in multi‑agent systems, eliminating the need for explicit, temporally aligned interaction graphs. By treating deviations in activation patterns as indicators of stealthy attacks, AcMAS not only identifies compromised agents more reliably—achieving F1 scores of 0.94 (synchronous) and 0.93 (asynchronous), far surpassing graph‑based baselines—but also supplies diagnostic signals that enable the restoration of affected agents instead of merely isolating them. Experiments across multiple open‑source LLM backbones, varying attack intensities, and different system scales confirm the method’s robustness and superior performance in both synchronous and asynchronous MAS deployments.


<details>
<summary>Abstract</summary>

While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchronous without the temporal alignment assumed by graph-based propagation models. To address these limitations, we propose AcMAS, an activation-based framework for malicious-behavior detection in MAS. By analyzing internal reasoning states in the activation space of local agents, AcMAS detects even stealthy attacks in a synchronization-robust fashion, without relying on explicit interaction graphs. Moreover, our activation analysis provides critical signals to guide AcMAS in restoring the functionality of compromised agents, rather than the disruptive agent isolation commonly used by the state-of-the-art methods. Comprehensive evaluation demonstrates that AcMAS significantly outperforms graph-based baselines against stealthy attacks, by +0.22 F1 in synchronous settings (0.94 vs. 0.72) and by +0.55 F1 in asynchronous settings (0.93 vs. 0.38), with generalization across diverse open-source LLM backbones, attack intensity, and MAS scale.

</details>


### 79. From Agentic to Autogenic Network Management for AI-Native 6G and Beyond: A Standards Perspective

- **Authors:** Petar Djukic, Sudipta Acharya, Takai Eddine Kennouche, Burak Kantarci
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06786v1](http://arxiv.org/abs/2607.06786v1)
- **PDF:** [https://arxiv.org/pdf/2607.06786v1](https://arxiv.org/pdf/2607.06786v1)
- **Categories:** cs.NI, cs.AI


> The paper proposes **autogenic network management**, a reference architecture that augments the emerging “agentic AI” paradigm for 6G by giving management agents the ability to **self‑program, self‑reflect, self‑orient, and self‑architect** their own automation code at runtime. The authors construct the architecture through a layered methodology—starting with human‑supervised large‑model agents and progressively integrating self‑evolving modules—then validate it against high‑priority TM Forum autonomous‑network use cases, demonstrating how the autogenic approach can resolve concrete operational pain points (e.g., intent interpretation, resource coordination, and runtime adaptation). Their roadmap identifies the standards, algorithmic, and security advances required to make fully self‑generating, AI‑native 6G management systems feasible.


<details>
<summary>Abstract</summary>

Standards bodies, including TM Forum, 3GPP, and ETSI, are converging on Agentic AI as the foundation for next-generation network management, where Large AI Model (LAM)-based agents autonomously interpret intent, coordinate resources, and adapt operational behaviors at runtime. However, achieving this vision at the scale and complexity of 6G networks requires management systems that can generate and evolve their own automation software during operation. We introduce Autogenic network management, a reference architecture that extends agentic capabilities with self-programming, self reflection, self-orienting, and self-architecting capabilities. The architecture supports practical staged deployment beginning with human-supervised LAM-based agents and progressing toward autonomous operation as confidence builds. We demonstrate the approach through high-priority operator scenarios drawn from TM Forum's autonomous network use cases, showing how autogenic management addresses real operational challenges. We conclude with a research roadmap outlining the technical advances needed to make autogenic network management realistic in future 6G networks.

</details>


### 80. Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled Probe Cascade

- **Authors:** Kai Ruan, Zihe Huang, Ziqi Zhou, Qianshan Wei, Xuan Wang, Hao Sun
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06503v1](http://arxiv.org/abs/2607.06503v1)
- **PDF:** [https://arxiv.org/pdf/2607.06503v1](https://arxiv.org/pdf/2607.06503v1)
- **Categories:** cs.AI


> **Main contribution:** The paper shows that impending failure of large‑language‑model (LLM) agents can be detected extremely early—from the first interaction—by probing the agents’ hidden activations, and it leverages this signal to build a multi‑gate “abort cascade” that stops hopeless episodes while preserving a user‑specified recall of successful runs.  

**Methodology:** The authors train lightweight, round‑wise probes on internal activation vectors of two LLM agents (Qwen‑2.5‑7B and Llama‑3.2‑3B) operating in the TextCraft benchmark. The probes output a failure probability used by calibrated, distribution‑free gates; recall budgets for each gate are jointly optimized so that the overall probability of aborting a truly successful episode meets a target (90‑97 %).  

**Key findings:** The activation‑based cascade reliably predicts failure as early as round 1, achieving the desired recall while cutting average inference cost by 37–47 % (≈1.6–1.7× the savings of the best single‑gate baseline). Behavioral‑only probes achieve roughly half the compute reduction, and adding behavioral features to the activation probes yields no further improvement, indicating that the hidden states already encode all predictive information. The paper also provides sample‑complexity bounds for guaranteeing high recall, guiding practitioners on the data requirements for different recall targets.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents solving multi-step tasks frequently commit to trajectories that are doomed to fail, yet continue to consume substantial inference compute before the failure becomes observable. We show that failure is predictable early from the agent's internal representations: lightweight per-round probes on hidden activations anticipate eventual episode failure as early as the first interaction round, where scorers reading only the agent's observable behavior are barely better than chance. We turn this signal into a practical abort cascade: one distribution-free calibrated gate per round, with per-round recall budgets jointly searched so that eventually-successful episodes survive all gates at a user-specified global rate; this episode-level guarantee is the one that matters in deployment, since false-abort risk accumulates across gates. Across two agent models on TextCraft, the cascade meets every recall target from 90% to 97% and, at the 90% target, saves 47.1% +/- 10.3% (Qwen-2.5-7B) and 37.2% +/- 8.8% (Llama-3.2-3B) of inference compute, 1.6--1.7x the best single-gate policy. An otherwise-identical cascade reading only behavior saves roughly half as much, and adding behavioral features to the probe yields no further gain: the hidden states capture what behavior reveals. Finally, we characterize the sample complexity of certifying high recall targets, telling practitioners which recall promises their data can, and provably cannot, back. The code will be released soon.

</details>


### 81. Multi-Agent Deep Reinforcement Learning for Multi Objective Battery Management in Dairy Farms

- **Authors:** Marcos Eduardo Cruz Victorio, Karl Mason
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06489v1](http://arxiv.org/abs/2607.06489v1)
- **PDF:** [https://arxiv.org/pdf/2607.06489v1](https://arxiv.org/pdf/2607.06489v1)
- **Categories:** cs.AI


> The paper introduces a two‑tier control architecture for dairy‑farm microgrids that couples a dynamic‑pricing optimizer (implemented via differential evolution) with a lower‑level, multi‑agent deep reinforcement learning (MADRL) system that coordinates battery charging/discharging to meet several objectives (profit, renewable utilization, voltage compliance). By training heterogeneous agents on a realistic distribution‑circuit model, the authors demonstrate that the MADRL‑based battery manager yields up to an 18 % increase in arbitrage profit over rule‑based baselines, boosts distributed generation usage without materially raising costs, and keeps voltage fluctuations within the Irish grid code limits. The results validate MADRL as an effective, scalable approach for multi‑objective energy management in agricultural settings.


<details>
<summary>Abstract</summary>

The dairy industry in Ireland has a large potential for the integration of renewable energy and the reduction of carbon emissions. However, researchers of distributed generation control are mainly focused on residential and commercial applications. To contribute to the effective integration of renewable energy in the dairy sector, this paper presents a multi-objective optimisation control system based on differential evolution and multi agent Deep Reinforcement Learning. The proposed control is organised in two layers: the upper layer uses dynamic pricing, and the lower layer is based on multi-agent reinforcement learning for battery management. This paper also simulates the electrical response of the proposed control system in a rural distribution circuit. The simulation results show that the proposed control framework can improve profits from energy arbitrage up to 18% compared to using Rule-based models, increase the use of distributed generation without significantly increasing cost, and comply with the Irish grid code in terms of voltage variation.

</details>


### 82. From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b

- **Authors:** Taeyun Roh, Eunha Lee, Wonjune Jang, Sohyun Chung, Junha Jung, Jaewoo Kang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06452v1](http://arxiv.org/abs/2607.06452v1)
- **PDF:** [https://arxiv.org/pdf/2607.06452v1](https://arxiv.org/pdf/2607.06452v1)
- **Categories:** cs.CL, cs.AI


> The paper introduces a question‑type‑aware pipeline that dynamically selects distinct inference “agents” for yes/no, factoid, and list biomedical questions, rather than using a single prompting strategy for all queries. By employing self‑reflection and snippet shuffling for binary decisions, chain‑of‑thought in‑context learning for factoids, and a multi‑agent workflow (evidence extraction → candidate generation → verification → aggregation) for lists, the framework tailors reasoning to each answer format. Evaluation on BioASQ 14b shows that this modular, answer‑type‑specific approach yields competitive results across batches and even tops the factoid subtask in Batch 4, highlighting the benefits of type‑aware inference and collaborative agent verification for robust biomedical QA.


<details>
<summary>Abstract</summary>

Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures for yes/no, factoid, and list questions according to their distinct reasoning and evaluation requirements. For yes/no questions, snippet shuffling and self-reflection are used to reduce sensitivity to evidence ordering and improve decision stability. For factoid questions, full-snippet input is combined with chain-of-thought-based in-context learning to support accurate biomedical entity identification. For list questions, a multi-agent architecture is employed, in which evidence extraction, candidate generation, answer verification, and final aggregation are handled collaboratively. Preliminary experiments on BioASQ 13b were used to identify effective inference strategies for each question type, and the resulting framework was subsequently evaluated in the official BioASQ 14b Task B challenge. In the official evaluation, our framework showed competitive performance across multiple batches and achieved first place in the factoid subtask of Batch 4. These results demonstrate the effectiveness of combining question-type-specific inference, ensemble prediction, and agent-based verification for reliable biomedical question answering.

</details>


### 83. Danus: Orchestrating Mathematical Reasoning Agents with Fact-Graph Memory

- **Authors:** Jihao Liu, Guoxiong Gao, Zeming Sun, Bin Wu, Shurui Liu, Jiedong Jiang, Haocheng Ju, Leheng Chen, Ronnie Cheng, Xiping Zhang, Bin Dong
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06447v2](http://arxiv.org/abs/2607.06447v2)
- **PDF:** [https://arxiv.org/pdf/2607.06447v2](https://arxiv.org/pdf/2607.06447v2)
- **Categories:** cs.AI, cs.CL, cs.MA


> Danus introduces a fact‑graph memory that serves as a shared, verifiable global state for coordinating multiple large‑language‑model (LLM) agents tackling research‑level mathematical proofs. The system pairs a planning “main” agent with parallel proof‑search workers and a stateless verifier, storing each validated claim together with its proof and logical dependencies in the graph, which the main agent continuously summarizes and uses to redirect effort and to interact with human collaborators. Across six case studies in algebraic geometry, singularity theory, and combinatorics, Danus demonstrates that this graph‑based orchestration enables the construction of long, reliable arguments and markedly improves scalability of agentic mathematical reasoning.


<details>
<summary>Abstract</summary>

Recent LLM-based mathematical reasoning agents have begun to tackle research-level problems and, in several cases, have contributed to the resolution of open problems. However, scaling and orchestrating such agents effectively remains challenging, due to the difficulty of coordinating parallel proof search while keeping intermediate claims organized and reliable. In this paper, we propose Danus, an orchestration system for research-level mathematical reasoning centered on a shared fact graph as a global memory-management mechanism. Danus consists of a main agent that performs planning and coordination, multiple worker agents that carry out proof search in parallel, and a stateless verifier that checks proposed mathematical claims before they are admitted into the fact graph. Each verified fact is stored together with its proof and logical dependencies, allowing the system to build long arguments incrementally while keeping the shared proof state organized. The main agent periodically summarizes the evolving proof state, redirects workers across promising directions, and supports interaction with human mathematicians through progress reports. We evaluate Danus through six research-level case studies in algebraic geometry, singularity theory, and combinatorics, illustrating how the fact-graph memory mechanism enables Danus to construct long, detailed mathematical proofs. Our results suggest that fact-graph-based orchestration provides an effective route toward scaling mathematical reasoning agents for long-horizon research problems. Danus is open source at https://github.com/frenzymath/Danus.

</details>


### 84. Finding H. pylori in the Fine Print: Evidence-Linked Multi-Agent Case Finding from Gastric Biopsy Reports

- **Authors:** Yufan Wang, Anit Kumar Sahu, Yan Fei Ng, Daniel Kang, Shayan Vassef, Soorya Ram Shimgekar, Koustuv Saha, Piyum Zonooz, Navin Kumar, Chee Leong Cheng, Li Yan Khor
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06435v1](http://arxiv.org/abs/2607.06435v1)
- **PDF:** [https://arxiv.org/pdf/2607.06435v1](https://arxiv.org/pdf/2607.06435v1)
- **Categories:** cs.AI


> The paper introduces Nimblemind Multi‑Agent System (nMAS), a field‑name‑driven, evidence‑linked extraction pipeline that uses coordinated micro‑agents to parse both structured and free‑text sections of gastric biopsy pathology reports and return unified, traceable decisions on four clinician‑scoped binary fields (biopsy presence, status, H. pylori positivity, and H. pylori‑associated gastritis). In a pilot on 54 de‑identified Singapore reports (216 field‑case decisions), nMAS achieved 98.6 % overall accuracy, matching a MiniMax M2.5 baseline while additionally providing sentence‑level provenance for each classification. The authors estimate that evidence‑linked verification reduces manual chart review time from ~5 minutes per report to ~5 seconds, translating to an 81.9‑hour (≈ USD 6.1 k) staff‑time saving, and they call for larger multi‑institutional studies to assess span correctness and generalizability.


<details>
<summary>Abstract</summary>

Data from Singapore indicated that about 31% of the population had evidence of Helicobacter pylori infection. Persistent H. pylori infection is associated with chronic active gastritis and peptic ulcer disease, and its eradication is key to gastric cancer prevention. However, evidence supporting \textit{H. pylori} positivity and H. pylori-associated gastritis may be distributed across heterogeneous coded and free-text report fields and may require contextual interpretation of assertion and negation, limiting keyword search, and making manual review difficult to scale. We conducted a retrospective pilot evaluation of the Nimblemind Multi-Agent System (nMAS), a field-name-driven, evidence-linked extraction workflow, using 54 de-identified gastric biopsy pathology reports from a large healthcare system in Singapore. Four clinician-scoped binary fields were evaluated: gastric/stomach biopsy, biopsy status, H. pylori positivity, and H. pylori-associated gastritis. Across 216 feature-case decisions, nMAS correctly classified 213, corresponding to 98.61% overall accuracy. A separately implemented UMA-style MiniMax M2.5 comparator produced similar aggregate and per-field classification metrics. Although predictive performance was similar, nMAS maintained unified report-level outputs with supporting source sentences; the demonstrated contribution is therefore workflow integration and traceability rather than predictive superiority. Under an illustrative, unmeasured scenario, reviewing 1,000 reports at five minutes per manual review versus five seconds per evidence-linked verification would reduce review time from 83.3 to 1.4 staff-hours, corresponding to 81.9 staff-hours and about USD~6,100 in potential staff-time value. Larger multi-institutional studies should evaluate evidence-span correctness, clinician verification time, and generalizability.

</details>


### 85. An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model Discovery

- **Authors:** Hao He, Xueying Liu, Chris J. Kuhlman, Xinwei Deng
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06413v1](http://arxiv.org/abs/2607.06413v1)
- **PDF:** [https://arxiv.org/pdf/2607.06413v1](https://arxiv.org/pdf/2607.06413v1)
- **Categories:** stat.ME, cs.AI


> The paper introduces a rigorous experimental‑design framework for evaluating large‑language‑model coding agents (specifically Codex and Claude Code) as stochastic “model‑discovery operators” that map task data and an optimization target to a fitted model. By systematically varying factors such as reasoning effort, task type, optimization metric, and training‑data composition, the authors fit regression models to multiple response variables (output quality, monetary cost, wall‑clock time, and process complexity) and use a utility‑aligned canonical decomposition to isolate the primary effect of reasoning effort and test whether it aligns with a cost‑performance utility direction. Applied to a suite of networked word‑forming games, the methodology reveals that increased reasoning effort yields diminishing quality gains while substantially raising cost and process complexity, highlighting key trade‑offs for autonomous agentic AI deployment.


<details>
<summary>Abstract</summary>

Large language model coding agents increasingly perform open-ended data modeling and analysis. These agents are stochastic and adaptive, and therefore their autonomous model discovery behavior cannot be adequately characterized by a single benchmark run. In this work, we propose an experimental design and analysis framework for systematically evaluating this discovery process, quantifying its variability, and identifying important factors. The proposed framework treats these agents as stochastic model-discovery operators, which map task-specific discovery data and an optimization target to a fitted model. Specifically, we investigate two such operators, Codex and Claude Code, under controlled experimental factors including agent's reasoning effort, task, optimization metric, and composition of training data. For each agent-task-metric combination, regression models and inference are conducted for multiple responses such as output quality, dollar cost, wall-clock time, and process complexity. Furthermore, we develop a utility-aligned canonical decomposition to characterize the dominant direction of the reasoning-effort effect and to assess whether that direction aligns with a performance-cost utility direction. The proposed framework is demonstrated on a testbed of networked word-forming games with insightful findings on reasoning effort with respect to cost and process complexity.

</details>


### 86. Spider 2.0-AIFunc: Extending Real-World Text-to-SQL to AI-Native SQL Workflows

- **Authors:** Tianyang Liu, Canwen Xu, Fangyu Lei, Nikki Lijing Kuang, Jixuan Chen, Tao Yu, Julian McAuley, Zhewei Yao, Yuxiong He
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06229v1](http://arxiv.org/abs/2607.06229v1)
- **PDF:** [https://arxiv.org/pdf/2607.06229v1](https://arxiv.org/pdf/2607.06229v1)
- **Categories:** cs.CL, cs.AI, cs.DB


> The paper introduces **Spider 2.0‑AIFunc**, a new benchmark that extends the classic Spider text‑to‑SQL suite to cover “AI‑native” SQL queries—i.e., SQL statements that invoke large‑language‑model functions (classification, sentiment analysis, similarity search, etc.) as first‑class Snowflake functions. The authors build the dataset via an automated agent pipeline that rewrites existing enterprise text‑to‑SQL tasks into AI‑function form, validates each instance through repeated execution, and supplies clarified natural‑language prompts; the final set contains 465 vetted examples over 125 real‑world databases and six AI function types. Experiments on ten leading LLMs show a ceiling of ~70 % execution accuracy for top proprietary models (58 % for the best open‑source model), with failures dominated by predicate formulation, schema grounding, and function‑parameter errors, and reveal that traditional text‑to‑SQL agents (e.g., schema retrieval, table selection) do not confer an advantage in this AI‑native setting.


<details>
<summary>Abstract</summary>

Major cloud data platforms now expose large language model capabilities as native SQL functions, enabling analysts to perform classification, filtering, sentiment analysis, extraction, similarity search, and aggregation within ordinary SQL queries. Yet existing text-to-SQL benchmarks evaluate only conventional SQL and provide no signal on whether models can generate such AI-native SQL. We introduce Spider 2.0-AIFunc, a benchmark of 465 verified instances across 125 real-world databases covering six types of AI functions on the Snowflake platform. Starting from an existing enterprise text-to-SQL benchmark, we construct Spider 2.0-AIFunc through an agent-based pipeline that rewrites source tasks into AI-native form, simultaneously transforming target queries and refining natural language instructions to make the intended AI-native solution explicit and reduce ambiguity. All instances pass a multi-round repeated execution protocol across temporally separated windows to confirm result stability before release. Evaluating ten state-of-the-art language models, we find that the strongest proprietary models reach 67-70% execution accuracy while the best open-source model achieves 58.1%, a gap driven primarily by errors in predicate specification, schema grounding, and AI function parameterization. Agent frameworks designed for traditional text-to-SQL challenges, such as schema retrieval and relevant table selection, do not transfer effectively to AI-native SQL: a minimal agent setup consistently matches or outperforms more elaborate alternatives, suggesting that the strategies these frameworks employ are less critical in this setting. Data are available at https://github.com/Leolty/Spider2-AIFunc .

</details>


### 87. Information Gain-based Rollout Policy Optimization: An Adaptive Tree-Structured Rollout Approach for Multi-Turn LLM Agents

- **Authors:** Yijun Zhang, Fan Xu, Jiaxin Ding, Yule Xie, Shiqing Gao, Xin Ding, Haoxiang Zhang, Luoyi Fu, Xinbing Wang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06223v1](http://arxiv.org/abs/2607.06223v1)
- **PDF:** [https://arxiv.org/pdf/2607.06223v1](https://arxiv.org/pdf/2607.06223v1)
- **Categories:** cs.AI


> The paper introduces **Information Gain‑based Rollout Policy Optimization (IGRPO)**, a novel framework that directs the limited rollout budget of large‑language‑model (LLM) agents toward the most informative intermediate states by constructing a budget‑aware, tree‑structured rollout whose expansion probability is proportional to node‑level information gain. By interpreting the resulting rollouts as samples from an explicit “teacher” trajectory distribution, IGRPO provides a well‑defined target for policy learning, effectively unifying adaptive, information‑driven exploration with principled policy optimization. Empirical results on seven long‑horizon, search‑augmented QA tasks show that, under identical computation budgets, IGRPO consistently outperforms existing rollout‑based and RL baselines, demonstrating that leveraging information‑gain‑guided rollouts substantially improves the performance of multi‑turn LLM agents.


<details>
<summary>Abstract</summary>

Reinforcement learning has become a promising paradigm for improving large language model (LLM) agents on long-horizon search tasks, where the agent must make a sequence of intermediate decisions before receiving a final outcome. However, existing methods still face a key limitation: the rollout budget is often allocated without explicitly assessing the utility of intermediate states. As a result, substantial computation may be spent on low-value states, even though different branches can vary drastically in their informativeness. In this paper, we propose Information Gain-based Rollout Policy Optimization (IGRPO), a policy optimization framework that treats intermediate-state informativeness as the organizing principle of rollout collection. Specifically, IGRPO performs budget-aware tree-structured rollouts by allocating expansion budget according to node-level informativeness, so that more informative branches are expanded more frequently while unpromising branches are progressively suppressed. We further demonstrate that the information gain-based rollout induces an explicit limiting teacher distribution over trajectories, which naturally yields a clear policy optimization target, thereby unifying adaptive tree-structured exploration with principled policy learning under a single framework. Experiments on seven challenging search-augmented QA benchmarks demonstrate that IGRPO consistently outperforms strong baselines under the same rollout budget constraints, validating the effectiveness of leveraging the induced teacher distribution to guide policy optimization for long-horizon search agents.

</details>


### 88. A toy framework for single and multi-agent human-AI curiosity ecosystems

- **Authors:** Ilya E. Monosov
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06214v1](http://arxiv.org/abs/2607.06214v1)
- **PDF:** [https://arxiv.org/pdf/2607.06214v1](https://arxiv.org/pdf/2607.06214v1)
- **Categories:** cs.AI


> The paper introduces a minimal “curiosity ecosystem” model that formalizes a single agent’s inquiry policy as a weighted combination of immediate uncertainty reduction, inquiry costs, delayed payoff, and the value of keeping a question open, with those weights allowed to evolve through experience. Extending this to multiple agents, the framework tracks collective metrics such as inquiry volume, topic diversity, frontier‑oriented questioning, redundancy, and reusable knowledge, providing a tractable way to study how agents co‑adapt their curiosity‑driven behavior in a shared knowledge landscape. Empirical illustrations show that short‑term cheap questioning can rapidly lower perceived costs and shift long‑term question preferences, while multi‑agent simulations reveal trade‑offs between exploratory breadth and redundant effort, suggesting design principles for coordinated, discovery‑oriented AI agents.


<details>
<summary>Abstract</summary>

This paper offers a toy framework for considering curiosity as an ecosystem. First, it suggests that a single agent's inquiry policy (how, when, and why an agent asks a question) depends on how the agent values immediate uncertainty reduction, costs, delayed return, and the value of keeping the question open. A key concept in the framework is that the weights on these decision-related terms can change with experience. For example, a period of cheap, quickly answered questions may change the cost of inquiry on a short timescale and change which kinds of questions the agent is drawn to answer over a longer timescale. Second, these ideas are extended to many agents exploring a shared knowledge landscape, and there the framework tracks inquiry volume, topic diversity, frontier-directed inquiry, redundancy, and reusable knowledge. The result is a conceptual toy framework for studying curiosity ecology and for future efforts towards designing multi-agent AI systems for discovery. It serves as a companion piece for a paper currently under review in Trends in Neurosciences.

</details>


### 89. LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability

- **Authors:** Chenxu Wang, Yongkun Yang, Boyuan Du, Shiwei Lin, Huaping Liu
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06157v1](http://arxiv.org/abs/2607.06157v1)
- **PDF:** [https://arxiv.org/pdf/2607.06157v1](https://arxiv.org/pdf/2607.06157v1)
- **Categories:** cs.CL, cs.AI


> The paper defines **deliberative collaboration** as a cooperative joint‑decision problem in which multiple agents have only partial, asymmetric observations and must communicate to reach a shared‑reward outcome. It introduces a scalable benchmark suite spanning several domains, a reference implementation of LLM‑based deliberative agents, and an evaluation protocol; systematic experiments with diverse state‑of‑the‑art LLMs (with and without external mathematical tools) show that while these agents can sometimes use deliberation to reflect and correct errors—occasionally surpassing centralized baselines—they still struggle with aligning information and performing the complex reasoning required for many partially observable tasks. The work thus provides the first comprehensive testbed and diagnostic analysis for assessing and improving LLM agents’ ability to deliberate and cooperate under uncertainty.


<details>
<summary>Abstract</summary>

Deliberation plays a crucial role in collaboration; when humans work together, they naturally engage in communication to align information and reach an agreement. In this paper, we investigate deliberative large language model (LLM) agents under partially observable joint decision-making tasks. We formalize deliberative collaboration as a cooperative joint decision problem with partial and asymmetric observations, and introduce a scalable benchmark that instantiates this problem across multiple task settings and domains in which agents must exchange information through deliberation to reach a joint decision with a shared reward. We then instantiate a reference scaffold and evaluation protocol for deliberative agents and conduct a systematic evaluation of a range of representative LLMs. The results reveal that complex deliberative collaboration tasks continue to challenge state-of-the-art language models. Even with the aid of external mathematical tools, language models may fail in either the deliberation process for aligning information or the complex reasoning process for making the decision. On the other hand, diagnostic analysis reveals that the deliberation process may also provide opportunities for reflection and error correction, sometimes improving performance over centralized baselines. Altogether, our work establishes a foundation for evaluating and improving LLM agents in deliberative collaboration and provides insights into the strengths, limitations, and properties of current LLM-based multi-agent systems.

</details>


### 90. Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted Software Development

- **Authors:** Rohit Mehra, Samdyuti Suri, Prithviraj K Tagadinamani, Kapil Singi, Vikrant Kaulgud, Adam P. Burden
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06101v1](http://arxiv.org/abs/2607.06101v1)
- **PDF:** [https://arxiv.org/pdf/2607.06101v1](https://arxiv.org/pdf/2607.06101v1)
- **Categories:** cs.SE, cs.AI, cs.CY, cs.HC


> The paper identifies “knowledge debt” as a hidden cost of delegating coding work to autonomous AI agents, arguing that the incidental learning developers acquire through hands‑on problem solving is being eroded. To counter this, the authors propose six design principles for “learning‑aware” developer tools and instantiate them in **SHIELD**, a multi‑agent framework that uses the coding agent’s own chain‑of‑thought reasoning to generate contextual, out‑of‑band explanations and prompts that surface learning moments without interrupting workflow. Experiments show that SHIELD preserves or even improves coding productivity while significantly increasing developers’ post‑task comprehension of the generated code, demonstrating a viable pathway to embed incidental learning back into AI‑assisted software development.


<details>
<summary>Abstract</summary>

AI coding agents are rapidly reshaping how software is built, with developers increasingly delegating substantial coding tasks to autonomous agents in pursuit of higher productivity. While these gains are real, they come at the cost of incidental learning. Developers historically acquired informal knowledge through effortful problem-solving, and this has long shaped how software engineering expertise develops. However, with over-reliance on agentic coding, unpracticed skills could atrophy silently over time. As this learning pathway is short-circuited, developers risk silently accruing Knowledge Debt, a developer-level analogue of Technical Debt, where changes the agent executes that the developer cannot fully understand accrue over time. In this paper, we argue that incidental learning will not re-emerge on its own and must be consciously designed back into developer-agent interactions, and propose six design principles to guide such systems. We then present "SHIELD", a multi-agent system grounded in the notion of "agents that teach", that operationalizes these principles by leveraging the AI coding agent's own reasoning to surface contextual, out-of-band learning moments without disrupting developer flow. Through this work, we envision a path toward learning-aware development environments where productivity and learning are complementary, not competing.

</details>


### 91. From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations

- **Authors:** Shiyi Ling, Zhi Zheng, Hui Zheng, Wenjun Xue, Feng Ye, Tong Xu
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06080v1](http://arxiv.org/abs/2607.06080v1)
- **PDF:** [https://arxiv.org/pdf/2607.06080v1](https://arxiv.org/pdf/2607.06080v1)
- **Categories:** cs.CL, cs.AI, cs.SI


> This paper presents **SocaSim**, a novel framework that leverages large‑language‑model (LLM) agents to instantiate Putnam’s social‑capital theory in a controllable, repeatable multi‑agent simulation. The authors embed explicit mechanisms for network formation, trust evolution, and norm diffusion, letting agents repeatedly conduct collective‑action tasks and then probe the model with counterfactual interventions; the methodology combines theory‑driven environment design with LLM‑generated behavior. Empirical results show that SocaSim reproduces Putnam’s macro‑level predictions (e.g., higher trust and dense networks boost collective outcomes) and aligns well with human group data, while also exposing fine‑grained causal pathways that traditional surveys cannot capture—demonstrating a scalable, interpretable approach for studying and applying social‑capital concepts in agentic AI systems.


<details>
<summary>Abstract</summary>

Putnam's Social Capital Theory is a foundational framework for collective action and community prosperity. However, traditional empirical methods face practical limits on control and replication. Meanwhile, LLM-based social simulations are typically behavior-driven and lack theory-aligned environments for modeling Putnam's core propositions. To address these gaps, we introduce SocaSim, an LLM-based multi-agent simulation framework to study Putnam's Social Capital Theory from theoretical blueprint to simulated reality. Specifically, we build an environment integrating social network evolution, trust dynamics, and norm propagation, where agents engage in repeated collective-action experiments, and then apply the three dimensions to analyze adaptation challenges in smart elderly care. Our simulations reproduce Putnam's macro-level patterns and exhibit strong human-agent alignment at the group level. Unlike traditional methods, SocaSim traces micro-level causal pathways of social network, trust, and norms via round-by-round simulations and counterfactual interventions, enabling process-level interpretability. Taken together, these capabilities establish a research paradigm that leverages LLM agents to bridge social science and computer science.

</details>


### 92. PolyWorkBench: Benchmarking Multilingual Long-Horizon LLM Agents

- **Authors:** Hongliang Li, Yijin Liu, Zhiwei Zhang, Zihe Liu, Xinyue Lou, Jinan Xu, Fandong Meng, Kaiyu Huang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06008v2](http://arxiv.org/abs/2607.06008v2)
- **PDF:** [https://arxiv.org/pdf/2607.06008v2](https://arxiv.org/pdf/2607.06008v2)
- **Categories:** cs.AI, cs.CL


> The paper introduces **PolyWorkBench**, a new benchmark that evaluates large‑language‑model agents on **multilingual, long‑horizon workplace workflows** across 67 tasks in commerce, knowledge work, legal analysis, localization, and manufacturing. By integrating structural grading, executable verification, and LLM‑based semantic scoring, the authors measure both functional correctness and linguistic consistency when agents must ingest heterogeneous multilingual inputs, reason iteratively, invoke external tools, and emit structured multilingual outputs. Experiments reveal that state‑of‑the‑art LLM agents experience a steep drop in performance under multilingual conditions, demonstrating that language variation compounds errors across reasoning and tool‑use steps and underscoring the need for agent architectures that jointly handle procedural decision‑making and multilinguality.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents have shown strong performance in long-horizon tasks that require planning, tool use, and interaction with external environments. However, most existing benchmarks implicitly assume a monolingual setting, where the entire execution process, including reasoning, tool invocation, and output generation, is conducted within a single language. In contrast, real-world applications often involve multilingual inputs and outputs within a unified workflow, yet the interaction between multilinguality and agentic execution remains underexplored. In this work, we introduce PolyWorkBench, a benchmark for evaluating LLM agents on multilingual long-horizon workplace workflows. PolyWorkBench consists of 67 tasks across five domains, including commerce, knowledge work, legal analysis, localization, and manufacturing, where agents must process heterogeneous multilingual inputs, perform iterative reasoning, invoke external tools, and produce structured outputs. To enable comprehensive evaluation, we propose a hybrid framework that combines structural grading, executable verification, and LLM-based semantic assessment. This design allows us to capture both functional correctness and linguistic consistency across complex workflows. Empirical results show that state-of-the-art LLM agents suffer significant performance degradation in multilingual workflow settings compared to monolingual counterparts. Our analysis suggests that multilinguality introduces compounding effects across reasoning and execution steps, highlighting the importance of jointly modeling language variation and procedural decision-making in agent evaluation.

</details>


### 93. Information Limits and Attractor Dynamics in Economies of Frontier LLM Agents: A Pre-Registered Test

- **Authors:** Cheng Qian
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06001v1](http://arxiv.org/abs/2607.06001v1)
- **PDF:** [https://arxiv.org/pdf/2607.06001v1](https://arxiv.org/pdf/2607.06001v1)
- **Categories:** cs.AI, cs.MA


> **Main contribution:** The paper presents the first fully pre‑registered empirical test of two quantitative theories about coupled economies of frontier language‑model agents (Claude Opus 4.8): an information‑theoretic capacity bound on wealth growth and a mean‑field “residual‑scaling” law for population misalignment under incentive and control levers.

**Methodology:** The authors scripted two exhaustive experimental suites (market‑coupled parimutuel trading and incentive‑control population dynamics), froze all predictions, acceptance bands, and decision rules in a public git repository, and then ran the simulations using cached API outputs (total cost ≈ $139). Results are reproduced mechanically from the cache, and all code and data are released for zero‑cost re‑execution.

**Key findings:** 1) The “gap law” \(G_a‑G_b = I_a‑I_b\) holds within the pre‑registered tolerance (≤ 46 millinats), coalition values are sub‑modular under conditional independence and become super‑modular with a designed XOR synergy, and the joint growth ceiling \(G_S \le H(X)\) is exactly tight—confirming the information‑capacity prediction. 2) The mean‑field residual‑scaling prediction fails: across 72 runs the population’s goal dispersion collapsed to zero, responses to levers were discontinuous step functions with bistable boundary regions, and no LLM‑based agents exhibited the noise‑maintained dispersion regime required by the theory. This negative result challenges existing mean‑field models of multi‑LLM alignment dynamics.


<details>
<summary>Abstract</summary>

We report a pre-registered, two-part experiment on small economies of frontier language-model agents (Claude Opus 4.8), testing two quantitative predictions about coupled multi-agent systems: an information-theoretic capacity region for wealth growth under market coupling, and a mean-field residual-scaling law for population misalignment under incentive and control levers. All predictions, acceptance bands, and decision rules were frozen in a public git chain before any run; every reported number re-derives mechanically from cached model outputs; the entire experiment cost $138.76 in metered API spend and is re-runnable at zero cost from the cache.
  Result 1 (confirmation): in parimutuel-coupled economies, relative growth equals relative claimed information -- the gap law G_a - G_b = I_a - I_b holds to a worst-case 46 millinats (pre-registered band: 50) across four perception structures; coalition value is submodular exactly where channels are conditionally independent, and a designed XOR synergy control flips it supermodular by 0.62 >= ln2/2 nats, with agents reasoning out the joint bit; the joint growth ceiling G_S <= H(X) binds exactly; and the best-informed agent absorbs essentially the whole wealth pool in 4/5 market seeds.
  Result 2 (structural negative): the residual-scaling test returned "domain not found." In all 72 population runs, goal dispersion collapsed (V -> 0; maximum 4.85 against a frozen floor of 5.31), the population's response to the two levers was a step function across the dominance boundary rather than a smooth response, and cells near the boundary were bistable with seed-selected outcomes. No tested LLM population at any capability level realizes the noise-maintained-dispersion regime the smooth mean-field model assumes. We release the full protocol, pre-registration chain, call cache, and analysis code.

</details>


### 94. MCP-Enabled Agentic AI for Autonomous IPoDWDM Network Lifecycle Automation

- **Authors:** Chunmin Xia, Jakub Harbaczewski, Nikhil Dsilva, Julie Raulin, Dominic Schneider, Achim Autenrieth
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05975v1](http://arxiv.org/abs/2607.05975v1)
- **PDF:** [https://arxiv.org/pdf/2607.05975v1](https://arxiv.org/pdf/2607.05975v1)
- **Categories:** cs.NI, cs.AI, cs.MA, eess.SY


> The paper introduces a novel **Multi‑Channel Planner (MCP)–enabled agentic AI framework** that autonomously manages the full lifecycle of vendor‑agnostic IP‑over‑DWDM (IPoDWDM) networks, integrating planning, provisioning, monitoring, and healing functions in a closed‑loop fashion. By coupling the MCP’s hierarchical decision‑making with real‑time telemetry and the open‑source network planner GNPy, the authors implement a multi‑layer orchestration loop that continuously recomputes optimal optical paths, configures devices, and reacts to faults without human intervention; the approach is validated on a physical testbed. Experimental results show that the agentic system achieves fully automated end‑to‑end service provisioning and fault recovery with sub‑second reaction times, demonstrating the feasibility of autonomous, vendor‑agnostic IPoDWDM network operation.


<details>
<summary>Abstract</summary>

This demo presents an MCP-enabled agentic AI architecture for autonomous control of vendor-agnostic IPoDWDM networks. We demonstrate live end-to-end lifecycle multi-layer automation and closed-loop control using GNPy and telemetry, validated on a real testbed.

</details>


### 95. Agentic AI for IPoDWDM Network Lifecycle Automation: An MCP-Enabled Architecture

- **Authors:** Chunmin Xia, Jakub Harbaczewski, Nikhil Dsilva, Julie Raulin, Dominic Schneider, Achim Autenrieth
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05958v1](http://arxiv.org/abs/2607.05958v1)
- **PDF:** [https://arxiv.org/pdf/2607.05958v1](https://arxiv.org/pdf/2607.05958v1)
- **Categories:** cs.NI, cs.AI, eess.SP, eess.SY


> **Summary**  
The paper proposes a vendor‑agnostic, multi‑controller‑plane (MCP) architecture that turns an IP‑over‑DWDM (IPoDWDM) network into an autonomous, self‑optimizing system. By distributing SDN control across several MCPs and coupling them with a closed‑loop analytics engine that continuously runs the open‑source GNPy optical‑layer simulator against live telemetry, the framework can orchestrate end‑to‑end service provisioning, fault remediation, and performance tuning across both IP and optical layers. Experiments on a laboratory IPoDWDM testbed demonstrate that the approach achieves fully automated service lifecycle management and cross‑layer optimization with sub‑second reaction times, validating its viability for agentic AI‑driven network operation.


<details>
<summary>Abstract</summary>

We present a distributed, vendor-agnostic multi-MCP architecture for SDN-based automation and autonomous control of multi-vendor, multi-layer IPoDWDM networks. The framework enables E2E service lifecycle automation, closed-loop cross-layer control using GNPy model and optical telemetry, and is experimentally validated on a IPoDWDM testbed.

</details>


### 96. Delay-Aware Active Triangulation with Uncertainty-Driven Multi-Agent Reinforcement Learning for Counter-UAS

- **Authors:** Seungwook Lee, David Hyunchul Shim
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05957v1](http://arxiv.org/abs/2607.05957v1)
- **PDF:** [https://arxiv.org/pdf/2607.05957v1](https://arxiv.org/pdf/2607.05957v1)
- **Categories:** cs.RO, cs.MA


> **Main contribution:** The paper introduces a delay‑aware, uncertainty‑driven multi‑agent reinforcement‑learning (MARL) framework for active visual triangulation in Counter‑UAS scenarios, explicitly modeling Age‑of‑Information (AoI) in a Dec‑POMDP and incorporating full analytical covariance propagation of sensor and pose uncertainties.  

**Methodology:** Agents are trained with MAPPO in a Dec‑POMDP where each observation is augmented with AoI to capture detection, communication, and actuation latencies; rewards are based on perception‑consistent metrics rather than privileged ground‑truth states, and a multi‑source covariance model (pixel, pose, gimbal, intrinsics) is used to propagate uncertainty during triangulation.  

**Key findings:** Accounting for AoI improves triangulation validity by ≈ 10.6 pp; perception‑consistent reward policies achieve lower RMSE (0.547 m vs 0.633 m) and 27 % fewer track losses; neglecting full uncertainty (using only angular noise) degrades RMSE by a factor of 2.8; recurrent MAPPO agents attain 0.547 ± 0.217 m RMSE with 78 % validity, whereas feed‑forward MLP agents collapse to ≈0.7 % validity, highlighting the necessity of memory for delay compensation in agentic AI systems.


<details>
<summary>Abstract</summary>

Multi-agent active visual triangulation enables precise 3D localization of aerial targets by coordinating mobile observers with controllable cameras. However, existing methods assume instantaneous state feedback, ignoring cumulative latency from detection, communication, and decision propagation. We present a delay-aware, uncertainty-driven multi-agent reinforcement learning framework for target localization in Counter-UAS applications. Our contributions are: (1) a Dec-POMDP formulation with Age-of-Information (AoI) augmented observations enabling delay-aware coordination -- AoI improves triangulation validity by 10.6 percentage points; (2) a controlled comparison showing that perception-consistent rewards outperform privileged clean-state rewards (0.547 m vs.0.633 m RMSE, 27% fewer track losses) -- both policies are trained through identical observation noise but differ in what they are optimized for, producing a stability-robustness tradeoff; and (3) multi-source analytical covariance propagation incorporating pixel, pose, gimbal, and intrinsics uncertainties -- restricting to angular noise alone causes 2.8-fold RMSE degradation. Experiments with MAPPO in 4096 parallel environments achieve 0.547 +- 0.217 m RMSE with 78.1% triangulation validity, while MLP policies achieve near-zero validity (0.7%), confirming recurrent memory as essential for delay compensation.

</details>


### 97. PCBWorld: A Benchmark Environment for Engine-Grounded PCB Design Automation

- **Authors:** Hyungseok Song, Junseok Park, Won-Seok Choi, Seohui Bae, Han-Seul Jeong, Youngjoon Park, Soonyoung Lee
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05915v1](http://arxiv.org/abs/2607.05915v1)
- **PDF:** [https://arxiv.org/pdf/2607.05915v1](https://arxiv.org/pdf/2607.05915v1)
- **Categories:** cs.AI


> **Contribution:** The paper presents **PCBWorld**, an open‑source, engine‑grounded benchmark that lets learning agents interact directly with the KiCad PCB design engine—issuing native routing commands and receiving Design Rule Check (DRC) feedback—along with a companion dataset (**PCBWorld‑Bench**) of synthetic and 679 real‑world boards and a suite of eight engine‑verified quality metrics.

**Methodology:** PCBWorld exposes KiCad’s native operations as an RL/LLM‑compatible environment, enabling both reinforcement‑learning policies and tool‑using large language model agents to perform incremental, interactive routing guided by real DRC signals; the benchmark provides standardized datasets and evaluation scripts for fair comparison.

**Key Findings:** Across experiments, agents trained in PCBWorld consistently beat naïve grid‑action RL baselines and open‑loop LLM approaches; notably, an RL policy trained solely on synthetic boards transferred zero‑shot to real boards and achieved routing quality close to that of traditional rule‑based routers, demonstrating the effectiveness of engine‑grounded, interactive training for advancing agentic PCB design automation.


<details>
<summary>Abstract</summary>

PCB routing is the task of connecting the nets of a board with copper traces under strict design rules, yet learning-based methods still lag behind rule-based routers. We introduce PCBWorld, an open-source engine-grounded PCB routing environment built on the KiCad EDA engine. As a human engineer does, agents in PCBWorld interactively route a board through the engine's native operations, using its Design Rule Check (DRC) feedback to keep the routing within the design rules. The environment supports both RL policies and tool-using LLM agents. Alongside the environment, PCBWorld-Bench provides three dataset families in KiCad's native board format (.kicad_pcb), covering two types of controllable synthetic instances and 679 real open-source boards. It scores any completed board with eight engine-checked evaluation metrics, regardless of the routing method. In our experiments, agents in PCBWorld consistently outperformed grid-action RL policies and open-loop LLM baselines, and an RL policy trained only on synthetic boards transferred zero-shot to real boards, approaching rule-based routers. These results position the engine-grounded, interactive approach of PCBWorld as a promising foundation for advancing the routing ability of both RL and LLM agents.

</details>


### 98. Security and Privacy in Agentic AI: Grand Challenges and Future Directions

- **Authors:** Adam Jenkins, Agnieszka Kitkowska, Caterina Maidhof, Diego Paracuellos, Francesco Sovrano, Gonzalo Gabriel Mendez, Guillermo Suarez-Tangil, Hana Kopecka, Isabel Wagner, Isabel Barbera, Javier Carnerero-Cano, Jide Edu, Jose Luis Martin-Navarro, Jose Such, Josep Domingo-Ferrer, Juan Carlos Carrillo, Kopo Marvin Ramokapane, Mark Cote, Pablo Vellosillo, Ramon Ruiz-Dolz, Rongjun Ma, Ruba Abu-Salma, Sameer Patil, William Seymour, Xiao Zhan
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06608v1](http://arxiv.org/abs/2607.06608v1)
- **PDF:** [https://arxiv.org/pdf/2607.06608v1](https://arxiv.org/pdf/2607.06608v1)
- **Categories:** cs.CR, cs.AI, cs.HC


> The paper delineates the most pressing security and privacy challenges posed by increasingly autonomous (agentic) AI systems, drawing on a horizon‑scanning workshop that convened thirty leading experts from academia, industry, and government. By synthesizing the participants’ discussions, the authors propose a research agenda that spans threat modeling for self‑directed AI, robust verification of goal alignment, privacy‑preserving multi‑agent interaction, and governance frameworks for monitoring emergent behaviors. Their findings highlight that current safety‑and‑privacy tools are inadequate for agents that can self‑modify, coordinate, and act in open environments, underscoring the need for novel formal methods, audited learning pipelines, and cross‑sector policy mechanisms to mitigate systemic risks.


<details>
<summary>Abstract</summary>

We present key challenges and future research directions in the security and privacy of agentic AI, based on a horizon-scanning exercise that brought together thirty leading international experts from academia, industry, and government to engage in focused discussions and collaborative exercises on the emerging risks associated with the growing agency of AI.

</details>


### 99. StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems

- **Authors:** Sergey Volkov, Yang Li, Ye Luo
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05844v1](http://arxiv.org/abs/2607.05844v1)
- **PDF:** [https://arxiv.org/pdf/2607.05844v1](https://arxiv.org/pdf/2607.05844v1)
- **Categories:** cs.AI, cs.CL, cs.MA


> StateFuse introduces a deterministic, conflict‑preserving memory contract for multi‑agent systems that layers an immutable, auditable history and explicit conflict objects on top of existing OpSet/CRDT merges, avoiding the hidden overwrites that plague current replicated memories. By adding exact and semantic correction handles (claim_id/claim_ref) and deterministic predicate contracts, the system resolves conflicts only at projection time, never rewriting the replicated state. Empirical evaluation on the MemoryAgentBench conflict‑bearing slice shows that, while overall answer accuracy matches that of collapsed‑memory baselines, StateFuse keeps contradictions visible, enables safer abstention and more reliable post‑hoc corrections, and its semantic handles prove essential when exact identifiers are unavailable.


<details>
<summary>Abstract</summary>

Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (claim_id / claim_ref), deterministic predicate contracts, and projection-time resolution that cannot rewrite replicated state.
  We evaluate StateFuse against flat multi-value, raw-log, provenance-style, and collapsed baselines under matched resolver and verification policies. On a 282-question official conflict-bearing MemoryAgentBench slice, the compared methods tie on answer accuracy, but conflict-preserving surfaces keep contradictions visible while collapsed surfaces do not. In a controlled agent loop with uniform verification, preserving ambiguity enables safer abstention and correction than early collapse. A correction-handle ablation further shows that semantic handles matter when exact prior identifiers are unavailable.
  The resulting claim is narrow: StateFuse is best supported as a safer public memory contract for contradiction surfacing, abstention, and auditable correction, not as a universal accuracy gain.

</details>


### 100. Tangent classes of matroids and wonderful compactifications

- **Authors:** Ronnie Cheng, Shurui Liu, Guoxiong Gao
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05835v2](http://arxiv.org/abs/2607.05835v2)
- **PDF:** [https://arxiv.org/pdf/2607.05835v2](https://arxiv.org/pdf/2607.05835v2)
- **Categories:** math.AG, cs.AI, math.CO


> **Main contribution:** The paper introduces a new integral tangent class \(T_{M,\mathcal{G}}^{\mathbb Z}\) for any loop‑free matroid \(M\) and any Feichtner–Yuzvinsky building set \(\mathcal{G}\) containing the top flat, showing that this class simultaneously generalizes the tangent bundle of the associated wonderful compactification, reproduces the Hilbert series of the Chow ring via Hirzebruch–Riemann–Roch, and satisfies the conjectured Chern–\(\alpha\) lower bounds.  

**Methodology:** The authors formalize the construction of \(T_{M,\mathcal{G}}^{\mathbb Z}\) inside the integral K‑theory \(K_{\mathbb Z}(M,\mathcal{G})\), prove its specialization properties and Riemann–Roch compatibility, and verify the Chern‑\(\alpha\) inequalities by combinatorial and geometric arguments. Crucially, the entire technical core of the paper—including theorem statements, proofs, and computations—was generated autonomously by Danus, an AI mathematical‑reasoning agent, prior to the release of related human work (arXiv:2606.22650).  

**Key findings for agentic AI:** The experiment demonstrates that an AI agent can independently discover and rigorously develop substantial new mathematics in algebraic geometry and matroid theory, matching and extending results later obtained by human researchers. This provides concrete evidence that agentic AI can contribute original, publishable theory, and it highlights the feasibility of using such agents as co‑researchers for generating and validating complex mathematical constructs.


<details>
<summary>Abstract</summary>

For every loopless matroid $M$ and every Feichtner--Yuzvinsky building set $\mathcal{G}$ containing the top flat, we construct an integral tangent class $T_{M,\mathcal{G}}^{\mathbb{Z}}\in K_{\mathbb{Z}}(M,\mathcal{G})$; in the realizable case it specializes to the class of the tangent bundle of the corresponding wonderful compactification, it recovers the Hilbert series of the Chow ring through Hirzebruch--Riemann--Roch, and it satisfies the expected Chern-alpha lower bounds. This reproduces the tangent class and its key properties studied by the first author in arXiv:2606.22650. The main body of this paper was produced autonomously, without human mathematical guidance, by Danus, an AI mathematical reasoning agent. Danus solved the problem before arXiv:2606.22650 was publicly available, demonstrating the potential of AI agents in mathematical research. We reproduce its output faithfully, adding only editorial comments; the experiment is documented in Appendix B.

</details>


### 101. Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure

- **Authors:** Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05805v1](http://arxiv.org/abs/2607.05805v1)
- **PDF:** [https://arxiv.org/pdf/2607.05805v1](https://arxiv.org/pdf/2607.05805v1)
- **Categories:** cs.AI, cs.LG, quant-ph


> The paper introduces **Onnes**, a physics‑grounded digital‑twin of a dilution refrigerator that combines a forward cryogenic physics model with a learned noise fingerprint from real BlueFors logs, and uses this twin to drive a live multi‑agent LLM operations layer for fault diagnosis. By evaluating a zero‑shot panel of LLM agents against a supervised classifier on 1 000 simulated fault turns, the authors show that the LLM agents match the classifier in detection and, after adding only six curated few‑shot demonstrations and self‑consistency voting, improve classification accuracy from 0.685 to 0.990—essentially parity with the supervised model without any parameter fine‑tuning. A continuous‑monitoring deployment further demonstrates real‑time fault catching with negligible pre‑onset false alarms (6.4 % on real hardware) and 100 % recall on injected physics faults, validating the simulator‑to‑real transfer for agentic AI‑based cryogenic diagnostics.


<details>
<summary>Abstract</summary>

Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, yet their fault diagnosis is still dominated by threshold alarms that report that something is wrong, not what. We present Onnes, a physics-grounded digital-twin simulator of a dilution refrigerator (a forward physics model with a learned real-fridge noise fingerprint) that drives a live multi-agent LLM operations layer, and use it for a controlled head-to-head between a zero-shot LLM agent panel and a supervised ML classifier on cryogenic fault diagnosis. The twin couples a real dilution-cooling floor, a noise-and-correlation fingerprint learned from real BlueFors logs, and six physics-grounded fault classes, three engineered to overlap on temperature but separate on flow and pressure. Across a 1000-turn evaluation the zero-shot panel shows no significant difference from the classifier on detection but trails on classification, its errors concentrating on the confusable faults. Curated contrastive few-shot demonstrations and self-consistency voting then raise classification accuracy from 0.685 to 0.990, matching the supervised classifier (0.985) with no parameter updates and six labeled demonstrations; an ablation attributes the gain almost entirely to the demonstrations. Run as a continuous monitor across a nine-run fault-by-seed sweep, the agent catches every developing fault within one poll interval, and a confidence gate suppresses pre-onset false alarms whose rate is backend-dependent. As a first sim-to-real check, a detector trained purely on real BlueFors telemetry posts a real-hardware false-alarm rate of 6.4% and 100% recall on physics faults injected onto real held-out windows. All numbers are drawn verbatim from released run logs.

</details>


### 102. From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space

- **Authors:** Yue Xu, Yutao Sun, Yihao Liu, Mengyu Zhou, Jiayi Qiao, Lu Ma, Kai Tang, Wenjie Wang, Xiaoxi Jiang, Guanjun Jiang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05794v1](http://arxiv.org/abs/2607.05794v1)
- **PDF:** [https://arxiv.org/pdf/2607.05794v1](https://arxiv.org/pdf/2607.05794v1)
- **Categories:** cs.AI


> The paper introduces **NapMem**, a new framework that treats a user’s long‑term conversational history as a **structured action space** rather than a static retrieval buffer. By organizing the history into a multi‑granular “memory pyramid” (raw dialogue, typed notes, topic tracks, and user profiles) and providing a set of memory‑manipulation tools, the authors train an agent with reinforcement learning to **navigate** this hierarchy—selecting and combining evidence at appropriate levels before generating a response. Experiments on several memory‑heavy benchmarks (PersonaMem‑v2, LongMemEval, LoCoMo) show that the NapMem‑trained agent matches or exceeds prior methods on memory‑intensive tasks while retaining general reasoning and tool‑use performance, highlighting that coupling structured storage with a learned navigation policy improves long‑term personalized memory use in conversational AI.


<details>
<summary>Abstract</summary>

Long-term user memory is essential for personalized conversational agents, yet many memory systems still expose memory through passive retrieval interfaces, making the model a consumer of pre-selected evidence. We introduce NapMem, a framework for learning to use long-term user memory as a structured action space rather than passively retrieved context. NapMem organizes user history into a linked multi-granularity memory pyramid, where raw conversations, typed memory records, topic tracks, and user profiles are connected through provenance relations, and exposes these levels through memory tools. The agent is trained to select memory according to the query and intermediate evidence, allowing it to inspect different memory granularities before answering. Experiments on PersonaMem-v2, LongMemEval, and LoCoMo show that a NapMem agent trained with memory-tool reinforcement learning is competitive across diverse memory-intensive tasks, while evaluations on non-memory tasks suggest that the learned policy largely preserves general reasoning and tool-use abilities. Additional analyses examine storage, inference cost, tool-use behavior, and ablations over navigation, memory granularity, and RL training. Our results suggest that long-term user memory benefits from coupling structured storage with a learned policy for using memory at the appropriate granularity.

</details>


### 103. Controlling Tool Use with Heading-Specific Activation Steering

- **Authors:** Yuqi Chen, Vincent Siu, Yang Liu, Dawn Song, Chenguang Wang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05790v1](http://arxiv.org/abs/2607.05790v1)
- **PDF:** [https://arxiv.org/pdf/2607.05790v1](https://arxiv.org/pdf/2607.05790v1)
- **Categories:** cs.AI


> The authors demonstrate that latent “steering vectors” extracted from the hidden‑state positions of heading‑anchor tokens can causally suppress unnecessary tool invocations in tool‑augmented LLMs, achieving consistent reductions in spurious tool use across five open‑source models and three task domains. By probing the models’ internal activations, they identify bidirectional control vectors that, when added to the hidden state, steer the model away from invoking external tools when parametric reasoning suffices; however, geometric analysis shows these vectors do not form clean linear subspaces but instead exhibit diffuse, bimodal alignments that differ across tool types. This work reveals a manipulable but geometrically irregular internal representation of tool‑use decisions, opening a new avenue for fine‑grained control of agentic AI systems that rely on external tools.


<details>
<summary>Abstract</summary>

Tool-augmented large language models extend their capabilities beyond parametric knowledge through external tools, but tend to invoke them unnecessarily. We investigate whether tool-use decisions have any stable internal representation that can be extracted and manipulated, a question that is non-trivial given that tools exist entirely in context at inference time and have no direct encoding in model weights. We show that steering vectors extracted from heading-anchors positions exert bidirectional causal control over tool-invocation behavior across five open-source models and three domains, suppressing unnecessary tool use most effectively in domains where parametric reasoning suffices. However, geometric analysis reveals that this causal effectiveness does not correspond to clean linear structure: tool-invocation steps exhibit diffuse, bimodal alignment with the suppression vector rather than the consistent negative alignment a linear encoding account would predict, and different tool types recruit largely distinct internal signatures with low cross-tool feature overlap. We hypothesize these geometric properties are indicative of the non-parametric nature of tools, and distinguish tool-use steering vectors from those extracted for parametrically grounded concepts. The relationship between this geometric irregularity and the observed causal effectiveness remains an open question.

</details>


### 104. FORGE: Towards Functional Tool-Use Generalization via Keypoint Trajectory Reasoning

- **Authors:** Chuhao Zhou, Liquan Wang, Shuxin Cao, Xiangyu Chen, Yuxuan Hu, Boyu Ma, Animesh Garg, Jianfei Yang
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05780v1](http://arxiv.org/abs/2607.05780v1)
- **PDF:** [https://arxiv.org/pdf/2607.05780v1](https://arxiv.org/pdf/2607.05780v1)
- **Categories:** cs.RO, cs.AI, cs.CV


> The paper introduces **FORGE**, a two‑stage architecture that separates functional reasoning from low‑level motor execution to enable robots to reuse the same function (e.g., hitting) with previously unseen tools. The method first learns **generalizable 2‑D keypoint trajectories** from large, action‑free video data (functional reasoning) and then grounds these trajectories into concrete robot motions using a small set of demonstrations (grounded execution). On a benchmark of seven different hitting tools, FORGE doubles the success rate of prior state‑of‑the‑art approaches in both simulation and real‑world tests, demonstrating markedly better functional tool‑use generalization.


<details>
<summary>Abstract</summary>

While humans readily repurpose a book, a stone, or a shoe to drive a nail, robots trained on specific tools fail to transfer the same function to novel ones -- a gap we formalize as functional generalization. Such tools share a common functional intent that is visually recognizable, yet this perceptual similarity does not carry over to action space, where each tool demands an entirely different motor pattern. To bridge this gap, we explore intermediate representations including affordance images, human video prompts, and 2D keypoint trajectories, finding that keypoint trajectories best balance functional expressiveness and action groundability. Building on this, we propose FunctiOnal Reasoning and Grounded Execution (FORGE), a two-stage policy that decouples functional reasoning from action execution: predicting generalizable keypoint trajectories from action-free data, then grounding them into robot actions with limited demonstrations. On a seven-tool hitting-function benchmark, FORGE consistently outperforms state-of-the-art methods on unseen tools in both simulation and the real world, achieving over 2X improvement in average success rate.

</details>


### 105. Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents

- **Authors:** Wael Albayaydh, Rui Zhao, Ivan Flechais
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05775v1](http://arxiv.org/abs/2607.05775v1)
- **PDF:** [https://arxiv.org/pdf/2607.05775v1](https://arxiv.org/pdf/2607.05775v1)
- **Categories:** cs.AI


> The paper’s main contribution is a comprehensive, cross‑benchmark taxonomy that unifies the recurring failure modes of LLM‑based agents across tool use, planning, long‑horizon reasoning, multi‑agent coordination, safety, and evaluation validity. By systematically reviewing 27 recent benchmark, taxonomy, and audit studies (covering 19 distinct tasks), the authors cluster errors into six groups—tool‑invocation/parameter mistakes, planning/constraint‑satisfaction lapses, degradation from context accumulation, coordination breakdowns, safety/security breaches, and measurement validity issues—and show that these failures compound non‑linearly as task length grows. Empirically, the synthesis reveals modest but reliable gains in single‑turn tool use, short‑horizon web navigation, and narrow coding tasks, while highlighting that strong sub‑task performance and additional scaffolding do not guarantee robust end‑to‑end agent behavior.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents are increasingly evaluated on their ability to use tools, plan multi-step tasks, coordinate with other agents, and operate over extended horizons. Reported benchmark gains often obscure recurring failure modes documented across otherwise unrelated evaluation efforts. This paper synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026), spanning 19 distinct benchmarks, into a cross-cutting taxonomy of agent limitations. To our knowledge, this is the first synthesis that integrates evidence across tool use, planning, long-horizon reasoning, multi-agent coordination, safety, and measurement validity into a single, unified taxonomy of LLM agent limitations. We identify six failure clusters: (1) tool invocation and parameter-level errors, (2) planning and constraint-satisfaction failures, (3) long-horizon degradation from context accumulation, (4) multi-agent coordination failures, (5) safety and security failures under adversarial or underspecified conditions, and (6) measurement validity problems. The taxonomy was derived iteratively by grouping independently reported error categories into themes corresponding to distinct stages of the agent reasoning-to-action pipeline. Across the literature, we find that failures compound nonlinearly with task length, that strong performance on individual sub-tasks does not reliably translate into end-to-end success, and that additional scaffolding does not consistently improve reliability. At the same time, substantial progress has been demonstrated in single-turn tool use, short-horizon web navigation, and narrowly scoped coding tasks.

</details>


### 106. Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning

- **Authors:** Akshay Arora, Ishan Nigam, Ashutosh Aggarwal, Shefali Bansal, Krishna Singh, Sweta Kumari, Nikhil Mittal, Shariq Farhan, Siddarth Malreddy
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05773v1](http://arxiv.org/abs/2607.05773v1)
- **PDF:** [https://arxiv.org/pdf/2607.05773v1](https://arxiv.org/pdf/2607.05773v1)
- **Categories:** cs.AI


> The paper presents **AgenticAI‑Supervisor**, a modular RL‑Gym environment that lets researchers define, launch, and monitor large‑language‑model agents through a decoupled API/UI stack, turning the evaluation of autonomous LLM agents from static benchmarks into verifiable, multi‑step simulations with high‑fidelity execution traces and multidimensional reward shaping. The authors demonstrate the system with a customer‑support agent use‑case, showing how internal state validation and systematic testing curb reward‑hacking and enable closed‑loop model optimization. The results indicate that such a simulation platform can scale agentic reinforcement learning while preserving safety guarantees, laying groundwork for future extensions like computer‑tool use, automated “stumping,” and edge‑case generation.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) evolve into autonomous agents, traditional static evaluation fails to capture multi-step decision-making. We introduce AgenticAI-Supervisor, an API and UI-driven RL Gym environment that decouples environment creation from scalable execution. By moving to verifiable execution outcomes, the platform generates high-fidelity traces and applies multi-dimensional reward shaping. Critically, our framework mitigates reward hacking through rigorous internal state validation and testing. This work provides a first look at our platform's core capabilities through a Customer Support Agent case study demonstrating a consistent closed-loop feedback for model optimization. Future work will focus on advanced features such as Computer Use, Tool Use, automated "stumping", and edge-case generation.

</details>


### 107. The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities

- **Authors:** Mohammadreza Rashidi
- **Published:** 2026-07-07
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05743v1](http://arxiv.org/abs/2607.05743v1)
- **PDF:** [https://arxiv.org/pdf/2607.05743v1](https://arxiv.org/pdf/2607.05743v1)
- **Categories:** cs.CR, cs.AI


> The paper’s main contribution is a systematic “balkanization” map of execution‑security research for AI coding agents, categorizing 39 works (2023‑2026) into 17 verified groups and exposing five cross‑cutting gaps that no single study currently bridges. Using a uniform verification protocol (applied also to four real CVEs in production agent harnesses), the authors compare isolation, capability‑control, policy‑enforcement, TOCTOU/MCP, and provenance approaches, revealing that isolation architectures are never benchmarked against each other, policy‑enforcement failures are ignored by isolation papers, state‑validation threats are split into separate literatures, policy‑author errors are unexamined, and benign out‑of‑scope actions (up to 17 % of prompts) receive no access‑control coverage. The findings call for unified benchmarks, joint evaluation of isolation and policy mechanisms, integrated TOCTOU/MCP analyses, tooling for safe policy authoring, and defenses for inadvertent agent behaviors—directions that shape the next research agenda for secure, agentic AI execution.


<details>
<summary>Abstract</summary>

AI coding agents now read repositories, call tools, and execute shell commands with limited human oversight, and a fast-growing body of work studies whether the execution layer around them is actually safe. That literature is scattered. Papers on sandbox isolation, capability and access control, policy enforcement, time-of-check-to-time-of-use (TOCTOU) races, Model Context Protocol (MCP) threats, identity delegation, execution provenance, network egress control, and static analysis of agent-generated code are published independently and rarely cite one another. We systematize 39 papers published between 2023 and 2026 into 17 categories, each verified directly against its source. The same verification protocol also confirms four disclosed, patched CVEs directly affecting production agent harnesses. Reading across categories surfaces five cross-cutting gaps that no single paper addresses. (1) Isolation architectures and capability models are almost never evaluated against one another on a shared benchmark. (2) Policy-enforcement studies report failure rates from 69% to 98% of real denylists, yet no isolation paper re-evaluates its own defense under that adversarial setting. (3) TOCTOU and MCP threats are analyzed as separate literatures despite both being instances of the same state-validation problem. (4) Every enforcement mechanism assumes an honest policy author, leaving policy-authoring error itself unaddressed. (5) Benign but out-of-scope agent actions occurring at rates up to 17.1% under realistic prompting are addressed by no access-control or capability paper in the corpus. Existing broader surveys of agentic AI security discuss sandboxing only as one item among many defenses, leaving execution security without a dedicated systematization. This paper is written to fill that gap. We conclude with a research agenda directed at the five gaps.

</details>


### 108. IMR: Iterative Mode-World Weighted Regression for Multi-Agent Trajectory Prediction

- **Authors:** Honglin Wang, Shiyao Pan, Yun-Fu Liu
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05705v1](http://arxiv.org/abs/2607.05705v1)
- **PDF:** [https://arxiv.org/pdf/2607.05705v1](https://arxiv.org/pdf/2607.05705v1)
- **Categories:** cs.RO, cs.AI, cs.CV, cs.LG


> The paper introduces **IMR**, a new multi‑agent trajectory forecasting framework that combines a **mode‑world weighted regression loss** with an **iterative decoder**. The loss function jointly optimizes mode diversity (preventing mode collapse) and world‑ranking confidence, while the decoder repeatedly refines trajectory segments to boost accuracy. On the Argoverse 2 multi‑agent motion‑forecasting benchmark, IMR achieves state‑of‑the‑art performance, ranking first among all published methods.


<details>
<summary>Abstract</summary>

Multi-agent motion prediction is essential for automated vehicles to understand the intentions of surrounding vehicles. However, previous prediction-based and anchor-based methods have limitations in mode diversity and prediction accuracy, respectively. These limitations may cause inadequate safety assessments and behavioral deviations in automated vehicles. To address this issue, a mode-world weighted regression loss is proposed to bridge the gap between these features. Specifically, this approach mitigates mode collapse while simultaneously improving world ranking and top-1 confidence. Furthermore, the proposed iterative decoder improves prediction accuracy by recurrently and segmentally generating trajectories. Experimental results show the proposed method ranks first in the Argoverse 2 multi-agent motion forecasting benchmark against other methods.

</details>


### 109. Non-contact, Real-time, Heart-rate Measurement using Image Processing with Commodity Cameras and AI Agents

- **Authors:** Kelly Li, Fulu Li
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06598v1](http://arxiv.org/abs/2607.06598v1)
- **PDF:** [https://arxiv.org/pdf/2607.06598v1](https://arxiv.org/pdf/2607.06598v1)
- **Categories:** eess.IV, cs.AI, cs.CV


> **Main contribution:** The paper presents a low‑cost, non‑contact system that estimates a person’s heart rate in real time from ordinary webcam video, and frames the solution as a personal health‑monitoring AI agent.  

**Methodology:** Using a commodity camera (≈30 fps), the pipeline first detects the face and extracts 68 facial landmarks with a deep‑learning shape predictor, then isolates a region of interest (e.g., forehead skin) and applies a time‑sliding‑window filter to denoise the subtle colour‑change signal (remote photoplethysmography). The cleaned signal’s periodicity is converted to beats‑per‑minute via a fast Fourier transform‑based peak detection.  

**Key findings:** Across multiple test sessions the webcam‑derived heart‑rate values differed from those measured by an Apple Watch by only a few beats per minute on average (mean absolute error ≈ 2–3 bpm), demonstrating that a simple AI‑driven image‑processing pipeline can achieve medically relevant accuracy without any wearable sensors, paving the way for autonomous agentic health assistants.


<details>
<summary>Abstract</summary>

Heart rate measurement is one of the key requirements for real-time health monitoring, in particular for health caring of elderly people. Traditional heart rate measurement relies on contact sensing mechanisms such as some heart rate measurement devices at medical hospitals or some wearable devices with embedded sensors such as Apple Watch, etc. In this paper, we develop a system for non-contact, real-time, heart rate measurement using image processing with commodity cameras such as an embedded camera on a laptop, where we use an innovative algorithm to capture the relevant signals for the computation of heart rate in a time series in real life environments. The presented heart rate computation (HRC) process is composed with four major steps: (a) identify frames per second of the camera in use, i.e., 30 frames per second for a given camera, (b) face detection (FD) with shape predictor of 68 face landmarks using deep learning (DL) method, (c) time sliding window (TSW) algorithm to de-noise the signal by smoothing out the noise, and (d) compute heart rate based on identified signal periodicity. We test and analyze the developed prototypes against heart rate results by Apple Watch and check the difference range in multiple rounds and compute the mean of the difference for the measurement values of the heart rate of the same person at the same time. We will do further tuning and optimization of the present methods and deploy the system as a personal AI agent [6] for health monitoring as our future directions.

</details>


### 110. FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents

- **Authors:** Yufeng Wang
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05682v1](http://arxiv.org/abs/2607.05682v1)
- **PDF:** [https://arxiv.org/pdf/2607.05682v1](https://arxiv.org/pdf/2607.05682v1)
- **Categories:** cs.AI


> **Main contribution**: The paper introduces **FirstResearch**, a framework that forces large‑language‑model (LLM) scientific agents to generate a **Research Question Certificate**—a structured, auditable artifact that lists the underlying definitions, assumptions, mechanistic model, identified tension, falsifiable hypothesis, decisive test, and failure‑update rule for any proposed research question.  

**Methodology**: The authors embed this certificate‑generation step into LLM agents and evaluate it on ten research topics, comparing against three strong prompt‑based baselines (AI Co‑Scientist, Agent Laboratory, AI Scientist‑v2). Performance is judged by two blind LLM judges (DeepSeek and Gemini‑2.5‑Flash), with an additional ablation that removes the certificate component.  

**Key findings**: FirstResearch achieves higher auditability and overall quality scores (≈ 4.86/5) than the best baseline (≈ 4.38/5), and the certificate‑only variant even improves scores (≈ 4.90/5). Removing the certificate drops performance below 1/5, confirming that the structured, first‑principles constraint is the critical factor for making LLM‑generated scientific questions transparent and verifiable.


<details>
<summary>Abstract</summary>

LLM systems for scientific discovery increasingly assist with ideation, literature synthesis, experiment planning, and report generation, but the first research question they propose can remain difficult to audit: it may sound plausible without exposing the mechanism, falsifier, or assumption that a scientist should inspect. We introduce FirstResearch, a first-principles research-question formation framework for scientific LLM agents whose core artifact is a structured Research Question Certificate. The certificate records primitive definitions, assumptions, a mechanism model, a tension or contradiction, a falsifiable hypothesis, a minimal decisive test, and a failure update rule, making the proposed question inspectable before downstream execution. On ten LLM-agent research topics, FirstResearch outperforms controlled prompt-level baselines inspired by AI co-scientist, Agent Laboratory, and AI Scientist-v2 under a primary DeepSeek-blind-judge protocol. A Gemini-2.5-Flash independent-judge rescore of the same 40 baseline packages preserves the system-level ranking, with FirstResearch scoring 4.86/5 versus 4.38/5 for the strongest baseline and Pearson agreement of 0.865 on average score. A one-repeat ablation checkpoint further suggests that the certificate-centered core is the strongest component: certificate-only scoring reaches 4.90/5 under DeepSeek and 4.88/5 under Gemini, while removing certificates drops below 1/5 under both judges. These results are preliminary and use LLM judges rather than human domain experts, but they support a narrow scientific-discovery claim: explicit derivation constraints are a promising mechanism for making LLM-generated scientific questions more auditable. Code, prompts, saved outputs, and reproduction scripts are available at https://github.com/louiswang524/FirstResearch.

</details>


### 111. What Do AI Agents Actually Change? An Empirical Taxonomy of Mutation Patterns in Performance-Improving Pull Requests

- **Authors:** Illia Dovhoshliubnyi, Nima Soroush, Ashkan Sami, Alexander Brownlee
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05666v1](http://arxiv.org/abs/2607.05666v1)
- **PDF:** [https://arxiv.org/pdf/2607.05666v1](https://arxiv.org/pdf/2607.05666v1)
- **Categories:** cs.SE, cs.AI


> The paper empirically investigates how generative AI coding assistants actually modify source code when they succeed in improving program performance, constructing a taxonomy of “mutation” patterns observed in 1,254 diff‑hunks from 216 performance‑optimising pull requests across five agent systems. By applying a dual‑LLM intersection pipeline to map these changes onto the 18‑category syntactic mutation schema of Even‑Mendoza et al. (2025), the authors find that only three mutation types dominate (name modification 37 %, object creation 26.4 %, and type change 22.7 %), a distribution that starkly contrasts with traditional genetic improvement corpora where “no change” accounts for 84 %; moreover, each agent and each performance strategy exhibits a characteristic, largely non‑overlapping mutation vocabulary. These results suggest that an agent’s identity and its optimisation goal provide strong priors for constraining the mutation operator space in search‑based software engineering, enabling more realistic and efficient SBSE pipelines for agentic AI.


<details>
<summary>Abstract</summary>

AI coding agents are black boxes: we cannot inspect how they generate code, but we can inspect what they change. This distinction matters for search-based software engineering (SBSE), where techniques such as genetic improvement (in the performance-optimisation application we study) depend on mutation operators that reflect how code is actually transformed. Fewer than 1% of the 33,596 agent PRs in AIDev-pop target performance, making each case a rare window into otherwise opaque agent behaviour. We classify 1,254 performance-relevant diff hunks from 216 of these PRs, spanning five agent systems, against the 18-category syntactic mutation taxonomy of Even-Mendoza et al. (2025) using a dual-LLM intersection pipeline. Three categories dominate: name modification (37.0%), object creation (26.4%), and type change (22.7%), a profile markedly different from prior GI corpora where no change accounted for 84%. Each agent's deployed system commits to a distinctive mutation vocabulary, and each performance strategy activates a largely disjoint category subset. Agent identity and target strategy are therefore informative priors that narrow the effective SBSE operator space. Replication package: https://github.com/5uper6rain/ssbse-challenge-2026

</details>


### 112. Collective Intelligence with Foundation Models

- **Authors:** J. de Curtò, I. de Zarzà
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.07729v1](http://arxiv.org/abs/2607.07729v1)
- **PDF:** [https://arxiv.org/pdf/2607.07729v1](https://arxiv.org/pdf/2607.07729v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces a multi‑agent framework that coordinates multiple foundation‑model “solver” agents with a critic and an aggregator, using a unified scoring module to evaluate semantics, numerics, and procedural correctness. By systematically ablating four configurations—individual baselines, a homogeneous shared‑model system, redundant homogeneous solvers, and a heterogeneous ensemble of specialized models—the authors show that the architectural scaffold alone yields only modest gains, whereas model heterogeneity drives a large boost in step‑wise reasoning accuracy (0.64 vs. 0.54 for single models, a 2.3× uplift over homogeneous setups) and markedly reduces performance variance across scientific domains. These findings highlight that diverse, specialized foundation models working cooperatively enable more reliable, explainable, and auditable agentic AI systems for complex scientific and industrial decision‑making.


<details>
<summary>Abstract</summary>

As foundation models grow in scale and diversity, coordinating multiple models into cooperative reasoning systems offers a path toward safer, more reliable AI. This chapter presents a multi-agent framework where solver models generate independent drafts, each undergoes structured critique and revision by a critic agent, and an aggregator agent synthesizes a final consensus solution. A scoring module provides semantic, numerical, and procedural evaluation across all agents. Through ablation studies on a benchmark spanning calculus, physics, chemistry, biology, economics, optimization, statistics, and mathematics, we isolate the contributions of framework architecture versus model diversity. We compare four configurations: (1) Individual Baseline, (2) Homogeneous Framework using one shared model, (3) Redundant Homogeneous Solvers using multiple instances of the same model, and (4) Heterogeneous Framework with diverse specialized models. Results show that while framework structure and redundant sampling yield modest gains, model heterogeneity is the critical factor driving substantial performance improvements. The heterogeneous configuration achieves superior step-wise accuracy (0.64 vs. 0.54 for individual models; 2.3x improvement over homogeneous configurations) with reduced variance across categories and difficulty levels. Step-wise reasoning quality (correctness of intermediate steps, not just final answers) improves dramatically only with model diversity, showing that heterogeneous agents provide complementary error detection and reasoning refinement essential for explainability and auditability. We discuss architectural principles, evaluation methodology, and implications for Global Applied AI, showing how heterogeneous multi-agent coordination supports transparent, auditable, high-confidence decision-making across scientific and industrial domains.

</details>


### 113. When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents

- **Authors:** George Torres, Sharad Shrestha, Satyajayant Misra
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.06595v1](http://arxiv.org/abs/2607.06595v1)
- **PDF:** [https://arxiv.org/pdf/2607.06595v1](https://arxiv.org/pdf/2607.06595v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper uncovers a new security threat for long‑term‑memory personal AI agents—**GhostWriter**, a memory‑poisoning attack that injects malicious payloads into an agent’s persistent store and later triggers them during tool‑use.  

**Methodology:** The authors craft a two‑step attack (injection + activation) against state‑of‑the‑art tool‑using agents, measuring injection success (~98 %) and activation success (~60 %) across conversational and action‑planning settings. They then introduce **Agentic Memory Sentry (AM‑Sentry)**, a lightweight defense that (i) enforces a memory‑saving policy to limit what gets persisted and (ii) screens retrievals for suspicious content.  

**Key findings:** GhostWriter readily compromises current agents because of absent memory governance, but AM‑Sentry cuts the attack’s effectiveness dramatically (reducing both injection and activation rates) while keeping the agents’ functional performance essentially unchanged, highlighting the need for security‑aware memory management in agentic AI systems.


<details>
<summary>Abstract</summary>

Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.

</details>


### 114. Federated Physics-Grounded Reinforcement Learning for Distributed Stability Control in Smart Grids

- **Authors:** Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat, Eman Hammad
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05553v1](http://arxiv.org/abs/2607.05553v1)
- **PDF:** [https://arxiv.org/pdf/2607.05553v1](https://arxiv.org/pdf/2607.05553v1)
- **Categories:** cs.LG, eess.SY


> The paper introduces **FedPPO‑PG**, a federated multi‑agent reinforcement‑learning framework that equips each generator in a smart grid with an autonomous PPO‑based controller whose observation space is enriched by the frequency deviations of its two most electrically coupled neighbors (derived from the post‑fault Kron‑reduced susceptance matrix). Training follows a centralized‑critic, decentralized‑execution scheme: a guided warm‑start from the classical decentralized controller initializes the local actors, while a shared critic computes advantage estimates for coordinated policy updates across the fleet without any central coordinator at run‑time. On the IEEE‑39‑bus benchmark, FedPPO‑PG stabilizes 100 % of fault scenarios (24/24 trials), cuts average stabilization time by 72 % and reduces required control power by 7–14× relative to a centralized PPO baseline, while meeting real‑time latency standards, demonstrating that physics‑grounded federated MARL can deliver fast, scalable, and reliable stability control for agentic smart‑grid applications.


<details>
<summary>Abstract</summary>

Transient stability control in smart grids requires rapid post-fault damping of generator frequency and rotor angle deviations to prevent cascading failures. This paper proposes FedPPO-PG, a Federated Multi-Agent Proximal Policy Optimization framework with Physics-Grounded neighborhoods, which reformulates transient stability control as a cooperative multi-agent reinforcement learning problem optimized directly against closed-loop stability objectives. Each generator hosts an independent local actor augmented with the frequency deviations of its two most strongly coupled electrical neighbors, identified from the post-fault Kron-reduced susceptance matrix. A guided policy initialization phase warm-starts all actors from the classical decentralized controller, while a centralized critic guides advantage estimation under the centralized training--decentralized execution (CTDE) paradigm. Evaluated on a simulation of the IEEE 39-bus benchmark system across five training and three unseen fault contingencies, FedPPO-PG achieves 100% stabilization in all 24 trials, reduces mean stability time by 72.4%, and cuts the control power by 7-14 times compared to the centralized baseline. Each actor executes independently with no central coordinator at deployment, and the per-actor inference latency satisfies the IEEE/IEC 60255-118-1-2018 real-time reporting requirements.

</details>


### 115. aiAuthZ: Off-Host, Identity-Bound Authorization for AI Agents

- **Authors:** Sai Varun Kodathala
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05518v1](http://arxiv.org/abs/2607.05518v1)
- **PDF:** [https://arxiv.org/pdf/2607.05518v1](https://arxiv.org/pdf/2607.05518v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **aiAuthZ**, an off‑host authorization gateway that couples every AI‑agent tool call to a cryptographically‑verified, identity‑bound signature and a fine‑grained, immutable policy, thereby eliminating unauthorized actions even when the language model is deceived.

**Methodology:** The author first benchmarks 15 contemporary LLMs against eight real‑world attack scenarios, showing highly variable refusal rates (38 %–100 %). Then they design aiAuthZ to require a per‑message HMAC‑SHA256 signature with a single‑use nonce and timestamp, enforce role‑based and argument‑level policies that the agent cannot read or modify, log decisions in a hash‑chained audit trail, and issue HMAC‑authenticated QR receipts. The system is evaluated on the AgentDojo banking suite and nine incident‑derived case studies, measuring success/false‑positive rates, verification robustness across eight transmission channels, and added latency.

**Key findings:** With aiAuthZ in place, **all 15 models achieve 0 % attack success** while incurring <0.03 ms latency; it blocks 9/9 attacks in the case‑study set and 7/7 in the banking suite (with only one legitimate first‑time payment blocked), outperforming a baseline that permits 2–4 successful injections. The gateway’s signature scheme yields 94 % mean verification across channels and no forgeries in 25 wrong‑key trials, demonstrating a practical, low‑overhead defense for agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents issue tool calls on the basis of text they cannot verify, so any party who controls part of the context can forge the appearance of authority. I evaluate 15 contemporary language models against eight attack scenarios derived from a published corpus of real agent incidents and find that refusal varies from 100% down to 38% across fully evaluated models; the most expensive model refused only half of the attacks despite a twentyfold price spread. I present aiAuthZ, an authorization gateway that moves the safety decision off the agent's host. Before a tool call executes, the gateway verifies caller identity with a per-message HMAC-SHA256 signature bound to a single-use nonce and a timestamp window, and it evaluates a role-based and argument-level policy that the agent can neither read nor modify. Every decision joins a SHA-256 hash-chained audit log, and each accepted message yields an HMAC-authenticated QR receipt that achieves 94% mean verification across eight transmission channels, with zero forgeries accepted in 25 wrong-key trials. With the gateway in place, residual attack success falls to 0% for all 15 models at no more than 0.03 ms of added decision latency. On the AgentDojo banking suite, aiAuthZ blocks all seven attacker-directed tool calls the evaluated agents emit, at the cost of one legitimate first-time payment, while a spotlighting baseline allows two injections to succeed. Across nine in-scope case studies from the same incident corpus, aiAuthZ blocks nine of nine, against four of nine for a policy baseline without identity binding. The gateway does not prevent a model from being deceived; it prevents a deceived model from acting beyond the verified user's authority on every call routed through it. The implementation and all experiments are released at https://github.com/Sports-Vision-Inc/aiAuthZ.

</details>


### 116. CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents

- **Authors:** Yujiang Li, Zhenyu Hou, Yi Jing, Jie Tang, Yuxiao Dong
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05378v1](http://arxiv.org/abs/2607.05378v1)
- **PDF:** [https://arxiv.org/pdf/2607.05378v1](https://arxiv.org/pdf/2607.05378v1)
- **Categories:** cs.LG


> **Main contribution:** The paper introduces **CompactionRL**, a reinforcement‑learning framework that lets large‑language‑model (LLM) agents operate over very long horizons despite fixed context windows by jointly learning how to **summarize (compact) past interaction states** and continue task execution from the compressed representation.  

**Methodology:** CompactionRL augments standard RL‑from‑human‑feedback pipelines with a token‑level loss‑normalization scheme and a cross‑trajectory generalized advantage estimator (GAE) that treat the summarization step as part of the policy; the LLM is therefore trained simultaneously for **task actions and summary generation**, enabling it to ingest compacted contexts during rollout.  

**Key findings:** When applied to open‑source models (GLM‑4.5‑Air, GLM‑4.7‑Flash), CompactionRL yields consistent gains on long‑horizon agentic coding benchmarks—e.g., +7.0 pts (66.8 % Pass@1) on SWE‑bench Verified and +3.1 pts (24.5 % Pass@1) on Terminal‑Bench 2.0—demonstrating that context compaction can be effectively integrated into RL training for agentic AI and motivating its use in the training pipeline of the larger GLM‑5.2 model.


<details>
<summary>Abstract</summary>

Long-horizon agentic LLMs are increasingly limited by finite context windows, as extended interaction trajectories can exceed the maximum context length before a task is completed. Context compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement learning remains underexplored. We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs with context compaction. Our approach jointly optimizes task execution and summary generation with token-level loss normalization and cross-trajectory generalized advantage estimation. This design enables the LLM agents to learn from compacted long-horizon trajectories. We train CompactionRL on top of open models and observe consistent performance gains on agentic coding tasks. CompactionRL enables the open GLM-4.5-Air model (106B-A30B) to achieve Pass@1 scores of 66.8% on SWE-bench Verified and 24.5% on Terminal-Bench 2.0, with absolute gains of 7.0 and 3.1 points, respectively. Built upon GLM-4.7-Flash (30B-A3B), CompactionRL improves Pass@1 by 5.5 and 6.8 points, reaching 56.0% on SWE-bench Verified and 20.2% on Terminal-Bench 2.0, respectively. CompactionRL is thus deployed in the RL pipeline for training the open GLM-5.2 model (750B-A40B).

</details>


### 117. Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation

- **Authors:** Jiaqi Peng, Xiqian Yu, Delin Feng, Yuqiang Yang, Wenzhe Cai, Jing Xiong, Ganlin Yang, Jinliang Zheng, Jiafei Cao, Xueyuan Wei, Jiangmiao Pang, Yuan Shen, Tai Wang
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05377v1](http://arxiv.org/abs/2607.05377v1)
- **PDF:** [https://arxiv.org/pdf/2607.05377v1](https://arxiv.org/pdf/2607.05377v1)
- **Categories:** cs.RO, cs.AI, cs.CV


> Cortex introduces a bidirectionally aligned hierarchical framework that couples a high‑level vision‑language model (VLM) planner with a low‑level vision‑language‑action (VLA) executor through a standardized set of 32 canonical manipulation primitives and tractability‑aware data generation, enabling the planner to produce executable sub‑task plans and the executor to follow them reliably. By automatically annotating >4 k h of open‑source video and synthesizing 30 h of simulation data, and by employing an event‑balanced sampling and context‑constrained inference pipeline, the authors fine‑tune the system to resolve planning ambiguities at sub‑task transitions. Empirically, Cortex surpasses monolithic baselines by 3.1 % on Libero‑long and 4.1 % on RoboTwin, and its generalist VLM can zero‑shot solve novel long‑horizon real‑world tasks (e.g., multi‑stage chemistry experiments) that cannot be achieved by VLA fine‑tuning alone.


<details>
<summary>Abstract</summary>

While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

</details>


### 118. GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks

- **Authors:** Kaiyuan Chen, Shuangyu Xie, Letian Fu, Justin Yu, William Pacini, Sandeep Bajamahal, Hudson Kim, Jaimyn Drake, Daehwa Kim, Haoru Xue, Jonathan Francis, Christian Juette, Peter Schaldenbrand, Muhammet Yunus Seker, Ruwan Wickramarachchi, Uksang Yoo, Guanzhi Wang, Adithyavairavan Murali, Balakumar Sundaralingam, S. Shankar Sastry, Spencer Huang, Yuke Zhu, Linxi "Jim" Fan, Ken Goldberg
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05369v1](http://arxiv.org/abs/2607.05369v1)
- **PDF:** [https://arxiv.org/pdf/2607.05369v1](https://arxiv.org/pdf/2607.05369v1)
- **Categories:** cs.RO, cs.AI, cs.CL, cs.LG


> **Main contribution:** The paper introduces **Graph‑as‑Policy (GaP)**, a multi‑agent coding framework that automatically synthesizes directed computation graphs—comprising perception, planning, and low‑level control modules drawn from a Modular Open Robot Skill Library (MORSL)—to solve **Variational Automation (VA)** tasks whose objects and poses vary widely.

**Methodology:** GaP treats each candidate graph as a policy, instantiates an internal physics‑based simulation, and runs many parallel rehearsals of diverse task instances. Using reinforcement‑style feedback on success rate and throughput, GaP iteratively refines both the graph topology (adding/removing nodes and edges) and the parameters of the constituent skill modules, effectively self‑learning the optimal structure for a given VA problem.

**Key findings:** Across eight newly introduced VA benchmarks (four simulated, four real‑world), GaP attains substantially higher success rates and throughput than standard model‑free RL policies, modular TAMP pipelines, and hand‑crafted ROS scripts, demonstrating that automatically generated graph‑policy structures can bridge the reliability gap for open‑world robotic automation.


<details>
<summary>Abstract</summary>

For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and industrial applications. Motivated by prior work on Task and Motion Planning (TAMP) and the Robot Operating System (ROS), we introduce Graph-as-Policy (GaP), a multi-agent coding harness that generates directed computation graphs with perception, planning, and control nodes from a Modular Open Robot Skill Library (MORSL). GaP then generates an internal simulation environment to rehearse task instances with different graphs in parallel to iteratively refine the graph structure and parameters to improve success rates and throughput. Evaluation with 8 new open VA task benchmarks, 4 in-simulation and 4 in real-world, suggests that GaP can achieve success rates that significantly outperform baselines. Details, code, and data can be found online: https://graph-robots.github.io/gap

</details>


### 119. SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints

- **Authors:** Dylan Zongmin Liu
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05363v1](http://arxiv.org/abs/2607.05363v1)
- **PDF:** [https://arxiv.org/pdf/2607.05363v1](https://arxiv.org/pdf/2607.05363v1)
- **Categories:** cs.AI


> **Main contribution:** The paper introduces **SovereignPA‑Bench**, the first executable benchmark that measures how well user‑owned personal agents preserve user sovereignty—advancing current user intent while respecting privacy, consent, evidential grounding, user burden, and resistance to manipulative platform incentives.

**Methodology:** The benchmark defines an **ObservableState/HiddenLabel** split, a suite of 120 “sovereignty‑stress” scenarios (varying intent evolution, platform mediation, privacy boundaries, consent and evidence requirements), and a multi‑metric dashboard (task success, alignment, privacy leakage, consent violations, manipulation capture, burden, auditability). The authors evaluate four families of language‑model agents across eight policy baselines, generating 3,840 frozen‑prompt trajectories and conducting a blinded three‑annotator human audit of 240 items.

**Key findings:** Agents equipped with “full‑sovereign” scaffolding (combined consent, evidence, privacy, and manipulation safeguards) achieve significantly higher sovereignty scores than memory‑only, consent‑only, evidence‑only, ReAct/tool‑use, safety‑prompt, and judge‑guard baselines, while reducing privacy leaks, consent breaches, and manipulation capture. Human auditors show strong agreement on privacy and consent judgments, highlighting that manipulation detection remains the most subjective dimension, underscoring the need for consent‑aware, evidence‑grounded evaluation beyond simple task completion in agentic AI.


<details>
<summary>Abstract</summary>

Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. We introduce SovereignPA-Bench, an executable benchmark for evaluating user-owned personal agents under evolving intent, platform mediation, privacy boundaries, consent constraints, evidence requirements, and burden tradeoffs. The benchmark separates agent-visible ObservableState from evaluator-only HiddenLabels, reports component metrics for task success, alignment, privacy, consent, evidence, manipulation, burden, and auditability, and preserves paired scenario ordering for model and policy comparisons. We evaluate 120 sovereignty stress scenarios across 4 model families and 8 policy baselines, yielding 3,840 frozen-prompt trajectories with raw prompts, outputs, provider-form responses, parsed actions, recomputable metrics, hard-set analyses, qualitative cases, and a blinded 3-annotator audit over 240 items. Full-sovereign scaffolding improves sovereignty score over direct, memory-only, consent-only, evidence-only, ReAct/tool-use, safety-prompt, and judge-guard baselines while reducing privacy leakage, consent violation, over-concession, and manipulation capture. Human audit shows high agreement on privacy and consent and lower agreement on manipulation, identifying the subjective frontier of platform-persuasion judgments. These results show that personal-agent evaluation must move beyond task completion toward representative, consent-aware, evidence-grounded action.

</details>


### 120. OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement

- **Authors:** Adriana Laurindo Monteiro, Nayse Fagundes, Gabriel Mattos Langeloh, Gustavo de Oliveira Kanno, Priscila Louise Aguirre, Thiago Costa Rizuti da Rocha, Victor Leme Beltran
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05346v1](http://arxiv.org/abs/2607.05346v1)
- **PDF:** [https://arxiv.org/pdf/2607.05346v1](https://arxiv.org/pdf/2607.05346v1)
- **Categories:** cs.AI, cs.MA


> **Main contribution:** OptiAgent introduces a fully‑automated, multi‑agent pipeline that translates a natural‑language description of an operations‑research problem into a solver‑ready mathematical model and executable code, with built‑in iterative self‑correction and auditable reasoning traces.  

**Methodology:** The system decomposes the modeling workflow into specialized agents (e.g., variable extraction, constraint formulation, consistency checking, code generation) that operate in nested loops; four distinct feedback mechanisms detect and repair misinterpretations, structural defects, mathematical inconsistencies, and code errors, enabling progressive refinement of the formulation.  

**Key findings:** Across benchmark suites covering linear, mixed‑integer, and nonlinear programming, OptiAgent attains state‑of‑the‑art accuracy on three of four datasets and remains highly competitive on the fourth, demonstrating that modular, self‑refining multi‑agent architectures can reliably produce high‑quality, transparent optimization models for agentic AI applications.


<details>
<summary>Abstract</summary>

We propose OptiAgent, a multi-agent framework that, given a natural language description of an Operations Research problem, is able to output a solver-ready mathematical formulation as well as executable code. Our architecture prioritizes the mathematical modeling step, where dedicated agents extract structures, such as decision variables and constraints, enabling iterative self-correction. We introduce a novel multi-loop validation architecture with four specialized feedback mechanisms, each targeting a distinct failure mode such as misinterpretation, structural defects, mathematical inconsistencies, validation failures, and code errors. Alongside accuracy, our modular design improves the process of solving optimization problems by improving transparency, as each agent exposes its reasoning and feedback, making the full modeling process auditable. Our framework achieves state-of-the-art performance on 3 out of 4 benchmarks across LP, MILP, and Nonlinear Programming tasks, while remaining highly competitive on the remaining dataset.

</details>


### 121. PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems

- **Authors:** Shubham Gupta, Nazanin Mohammadi Sepahvand, Abhinav Kumar, Cem Subakan, Spandana Gella, Pierre-André Noël, Perouz Taslakian, Eugene Bagdasarian, Valentina Zantedeschi
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05318v1](http://arxiv.org/abs/2607.05318v1)
- **PDF:** [https://arxiv.org/pdf/2607.05318v1](https://arxiv.org/pdf/2607.05318v1)
- **Categories:** cs.MA, cs.CR


> The paper introduces **PiSAs**, a system‑agnostic benchmark that measures *contextual‑integrity* violations in multi‑user LLM‑agent environments by annotating each piece of information for (1) task relevance and (2) authorized user access. Using PiSAs, the authors evaluate a range of agent architectures, memory configurations, and inter‑agent communication channels, showing that while better system design (e.g., stricter routing, scoped memory) reduces cross‑user data spillage, the dominant source of leaks is the LLM’s own judgment errors—state‑of‑the‑art models still frequently output or forward information that should be hidden from certain users. These results highlight that current privacy safeguards are insufficient for shared agentic infrastructures and motivate the development of stronger, model‑level privacy‑preserving mechanisms.


<details>
<summary>Abstract</summary>

As LLM agents evolve from single-user assistants into shared organizational infrastructure, new privacy risks emerge: inappropriate information may not only be exposed through outputs for external recipients, but also internally across users through inter-agent messages, shared memory and agents. These data spillage risks are not captured by existing privacy benchmarks grounded in contextual integrity (CI) as they focus primarily on either single-user settings or interactions between independently owned agents. We introducePiSAs (Privacy in Shared Agentic systems), a benchmark for assessing unintentional leaks with dual CI annotations: whether an information is appropriate for the task, and which users may legitimately access it. This enables direct measurement of cross-user spillage across agentic system components and interfaces, such as outputs, inter-agent communication, and memory. PiSAsis system-agnostic and supports evaluation across different agent topologies and memory regimes. We find that, although system design improves CI compliance, results are bottlenecked by incorrect LLM judgment calls: even state-of-the-art models fail to reliably filter inappropriate content or restrict transmission to authorized users. Our findings underscore the need for privacy-preserving strategies, beyond those studied in this work.

</details>


### 122. MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution

- **Authors:** Zefeng Wang, Minxi Yan, Jinhe Bi, Sikuan Yan, Volker Tresp, Yunpu Ma
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05297v1](http://arxiv.org/abs/2607.05297v1)
- **PDF:** [https://arxiv.org/pdf/2607.05297v1](https://arxiv.org/pdf/2607.05297v1)
- **Categories:** cs.AI


> MetaSkill‑Evolve introduces a recursive, two‑timescale self‑improvement loop for large‑language‑model (LLM) agents: each agent maintains a fast‑updating task skill (what it does) and a slower‑evolving meta‑skill that governs the five components (Analyzer, Retriever, Allocator, Proposer, Evolver) of the skill‑generation pipeline itself. By applying the same improvement pipeline to both levels while sharing a single frozen backbone model, the framework automatically rewrites not only the operational skills but also the procedures that create them, without requiring extra models or objectives. Across three open‑ended benchmarks (OfficeQA, SealQA, ALFWorld), MetaSkill‑Evolve achieves substantial gains over baselines, raising test accuracy by +23.5, +16.1, and +1.9 points respectively, demonstrating that recursive meta‑skill evolution can markedly enhance the adaptability and performance of agentic AI systems.


<details>
<summary>Abstract</summary>

Recent LLM agents tackle increasingly long-horizon, open-ended tasks, and external skills, reusable procedural knowledge supplied to the agent, further extend this capability. However, a fixed, hand-authored skill is rarely optimal, and cannot adapt to the diversity of tasks an agent encounters. Self-improving agents address this by rewriting their own skill files from execution traces, yielding meaningful gains on challenging benchmarks. Yet such self-evolution remains non-recursive: it improves only the task skill (what the agent does) while the improvement procedure (how it improves) is authored once and held fixed. We introduce MetaSkill-Evolve, a two-timescale framework that makes agentic skill improvement recursive: every branch carries both a task skill $s$ and a branch-local meta-skill $m=(ψ,σ,α,π,\varepsilon)$ whose five components parameterise the Analyzer, Retriever, Allocator, Proposer, and Evolver agents of the improvement pipeline. Task skills evolve on a fast loop while the meta-skill evolves on a slower one under the same pipeline applied to itself, with no additional model or objective. With all five pipeline agents sharing a single frozen backbone, MetaSkill-Evolve outperforms no-skill, static-skill, and single-level evolution baselines on three agentic benchmarks (OfficeQA, SealQA, ALFWorld), improving held-out test accuracy over the raw backbone by +23.54, +16.09, and +1.92 points respectively.

</details>


### 123. Untrusted Content Masking for Web Agents with Security Guarantees

- **Authors:** Kristina Nikolić, Egor Zverev, Javier Rando, Matthew Jagielski, Edoardo Debenedetti, Florian Tramèr
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05277v1](http://arxiv.org/abs/2607.05277v1)
- **PDF:** [https://arxiv.org/pdf/2607.05277v1](https://arxiv.org/pdf/2607.05277v1)
- **Categories:** cs.CR, cs.LG


> The paper introduces **Untrusted Content Masking (UCM)**, a framework that re‑establishes a strict trust boundary for web‑based AI agents, enabling provable defenses against prompt‑injection attacks. UCM exploits the DOM structure to **identify and redact untrusted regions** of a rendered page without parsing their text, then feeds only the masked view to the agent while routing all interactions through a sandboxed, privilege‑separated interface. Experiments show that agents can still perform realistic web‑navigation and tool‑use tasks with near‑original performance, yet are **immune to manipulation of untrusted page content**, providing the first security‑guaranteed isolation mechanism for web agents.


<details>
<summary>Abstract</summary>

Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which intermingles trusted content with untrusted content. This structural entanglement removes the trust boundary on which security guarantees depend, undermining provable defenses for web agents. In this paper, we present Untrusted Content Masking (UCM), a simple and effective approach that restores this boundary in web environments. We leverage a key structural insight: a webpage's Document Object Model (DOM) encodes sufficient information to distinguish trusted from untrusted regions without reading their content. Our framework exploits this by redacting untrusted regions before they reach the agent and routing interaction through a sandboxed interface with strict privilege separation, thereby enabling agents to observe and interact with their environment while remaining isolated from adversarial content. The code is publicly available.

</details>


### 124. Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets

- **Authors:** Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez, Giovanni Montana, Luis Jimenez-Linares
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05179v1](http://arxiv.org/abs/2607.05179v1)
- **PDF:** [https://arxiv.org/pdf/2607.05179v1](https://arxiv.org/pdf/2607.05179v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> The paper introduces a graph‑based multi‑agent reinforcement‑learning framework for dynamic ticket pricing in liberalised high‑speed railway markets, where firms must act under partial observability and cannot communicate. By modelling the market as an entity graph that captures competition, coordination, and connectivity among operational units, the authors extend the Twin‑Delayed DDPG algorithm with a relational graph convolutional network and attention‑based aggregation to learn policies from structured relational data rather than flat observations. Experiments on a realistic rail‑pricing simulator show that this relational Twin‑DDPG substantially outperforms both relational and non‑relational baselines in terms of revenue and training stability across increasingly complex market configurations.


<details>
<summary>Abstract</summary>

In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning, where standard approaches typically treat observations as unstructured vectors, ignoring the underlying market topology that governs strategic interactions. To address this, an entity graph modelling approach is proposed, which represents the environment as a graph of operational units, rather than decision-making agents or static infrastructure, encoding competition, coordination, and connectivity relations between entities. Then, an extension of the multi-agent twin delayed deep deterministic policy gradient algorithm with graph-based representation learning processes the features of the entities through a multi-layer relational graph convolutional network and aggregates them via a learnt attention mechanism. Experimental results in a rail pricing reinforcement learning environment show that this novel framework achieves higher revenue and stability in two different settings of increasing market complexity compared to a representative selection of relational and non-relational baselines. The code is publicly available at: https://github.com/Kinrre/RelationalRailPricing-RL

</details>


### 125. AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments

- **Authors:** Zhiheng Xi, Dingwen Yang, Jiaqi Liu, Jixuan Huang, Honglin Guo, Baodai Huang, Tinggang Chen, Qi Zhang, Zhonghang Lu, Chenyu Liu, Jiajun Sun, Jiazheng Zhang, Dingwei Zhu, Xin Guo, Junzhe Wang, Zhihao Zhang, Yuming Yang, Junjie Ye, Minghe Gao, Dongrui Liu, Jiaming Ji, Guohao Li, Tao Gui, Qi Zhang, Xuanjing Huang
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05174v1](http://arxiv.org/abs/2607.05174v1)
- **PDF:** [https://arxiv.org/pdf/2607.05174v1](https://arxiv.org/pdf/2607.05174v1)
- **Categories:** cs.AI


> The paper introduces **AgentGym2**, a benchmark that moves LLM‑agent evaluation from toy, fully‑specified tasks to end‑to‑end “de‑idealized” scenarios drawn from real‑world workflows, where agents must handle noisy, underspecified inputs, explore to discover and compose new tool interfaces, and execute multi‑step procedures. The authors construct a suite of tasks spanning 15 proprietary and open‑source models, measuring performance on reasoning, planning, tool discovery/exploitation, and robustness under uncertainty. Experiments reveal that even cutting‑edge systems such as Gemini and GPT‑5 perform poorly on these realistic challenges, highlighting a sizable gap between current LLM‑agent capabilities and the requirements of production‑grade, agentic AI.


<details>
<summary>Abstract</summary>

Language agents, i.e., LLM agents, progress rapidly and are increasingly deployed in production environments. This trend underscores the urgent need for rigorous and realistic evaluations. However, most existing benchmarks evaluate agents in simplified, idealized settings. They typically rely on pre-packaged tool interfaces, overlook critical steps, and assume inputs are clean and fully specified. Consequently, they understate the difficulty of real deployments, where uncertainty and noise are ubiquitous and agents must proactively explore the environment to uncover new tools. To bridge this gap, we present AgentGym2, a new evaluation framework with task instances grounded in real-world end-to-end working demands. Beyond reasoning and planning, it measures agents' ability to execute end-to-end procedures, discover tools via exploration, compose tools for unseen tasks, and remain robust to noisy and underspecified information. Experiments on 15 proprietary and open-source models show that even SOTA systems like Gemini and GPT-5 struggle on AgentGym2, revealing a substantial gap between the capability of current agents and the demands of real-world applications.

</details>


### 126. PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference

- **Authors:** Akshat Jani, Prathamesh Gadekar, Sakhinana Sagar Srinivas, Venkataramana Runkana
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05134v1](http://arxiv.org/abs/2607.05134v1)
- **PDF:** [https://arxiv.org/pdf/2607.05134v1](https://arxiv.org/pdf/2607.05134v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution** – PDEFlow introduces a fully autonomous, agent‑driven pipeline that converts multi‑turn natural‑language descriptions of ODE/PDE problems into end‑to‑end neural‑operator workflows, eliminating the need for hand‑crafted solver setups and enabling solver‑free inference from trained checkpoints.

**Methodology** – The system uses a stateful input graph to parse and validate user specifications, automatically generates training data by sampling parameters and solving the governing equations with a FEniCSx finite‑element backend, and then trains neural operators through a registry‑based interface; the paper demonstrates this with a multi‑branch Bayesian DeepONet that can be swapped out without altering the surrounding pipeline.

**Key findings** – Experiments on standard ODE and PDE benchmarks show that PDEFlow reliably produces valid problem specifications, creates high‑quality solver‑backed datasets, and trains neural operators that achieve accurate, solver‑free predictions across both steady‑state and transient regimes, highlighting its utility for repeatable, large‑scale scientific and engineering workflows.


<details>
<summary>Abstract</summary>

We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines. The workflow links problem specification, data generation, operator training, and checkpoint-based inference. A stateful input graph converts multi-turn natural-language input and user edits into validated problem specifications. The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element backend, and stores the solutions as operator-ready tensors. The training and inference stages use a registry-based interface, allowing different neural operators to be trained and deployed without changing the surrounding pipeline. In the current implementation, we instantiate this interface with a multi-branch Bayesian DeepONet. Experiments on benchmark ODE and PDE tasks show that PDEFlow can construct valid specifications, generate solver-backed datasets, train neural operators across steady and transient problem classes, and provide solver-free predictions from saved checkpoints. The framework is designed for repeatable scientific and engineering workflows where many related physics configurations must be specified, simulated, learned, and queried with minimal manual intervention.

</details>


### 127. When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games

- **Authors:** Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf, Vincent Conitzer, Zhijing Jin
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05132v2](http://arxiv.org/abs/2607.05132v2)
- **PDF:** [https://arxiv.org/pdf/2607.05132v2](https://arxiv.org/pdf/2607.05132v2)
- **Categories:** cs.CY, cs.CL


> **Main contribution:** The paper introduces a three‑stage protocol for probing whether large‑language‑model (LLM) agents keep the commitments they publicly announce in repeated multi‑player games, and shows that “honesty” is not an intrinsic property of a model but varies across games and interaction contexts.  

**Methodology:** Three state‑of‑the‑art LLM agents are placed in six repeated n‑player games (10 rounds each) with (1) private deliberation, (2) public announcement of intended actions, and (3) execution of the actual move. By comparing announced actions with private plans, the authors can tell if a deviation was pre‑planned (premeditated) or opportunistic, and they evaluate homogeneous (same model) and heterogeneous (mix‑model) groups.  

**Key findings:** (1) When agents break their announcements, >90 % of the time the divergent action was already present in the private plan, indicating that lies are usually pre‑meditated rather than emergent on the spot. (2) Different models assign incompatible semantics to announcements—some treat them as binding contracts, others as non‑binding cheap talk—creating systematic payoff disparities that appear from the first round and persist throughout the game. Consequently, deploying mixed‑model agent teams requires explicit empirical verification of shared commitment semantics.


<details>
<summary>Abstract</summary>

As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three frontier models across six games in homogeneous and heterogeneous groups over 10 rounds, we report two findings. First, when agents deviate from their announcements, the deviation is predominantly already stated in their private plan (exceeding 90% in the highest-deception conditions), yet this is not a fixed model property: the same model ranges from perfect honesty to near-total deviation across games. Second, different models interpret announcements incompatibly, some as binding commitments and others as cheap talk, producing payoff gaps that emerge in Round~0 and persist across all 10 rounds. Systems that combine models from different providers therefore cannot assume shared announcement semantics and require empirical testing of model interactions before deployment.

</details>


### 128. Agent Data Injection Attacks are Realistic Threats to AI Agents

- **Authors:** Woohyuk Choi, Juhee Kim, Taehyun Kang, Jihyeon Jeong, Luyi Xing, Byoungyoung Lee
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05120v1](http://arxiv.org/abs/2607.05120v1)
- **PDF:** [https://arxiv.org/pdf/2607.05120v1](https://arxiv.org/pdf/2607.05120v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper identifies and formalizes a previously overlooked class of security threats to AI agents—**Agent Data Injection (ADI) attacks**, in which adversaries disguise malicious data as trusted metadata or context (e.g., resource IDs, tool‑call schemas) and cause the agent to act on it inadvertently.

**Methodology:** The authors systematically analyze a range of publicly available AI agents (web agents such as Claude‑in‑Chrome, Antigravity, Nanobrowser, and coding agents like Claude Code, Codex, Gemini CLI), crafting ADI payloads that masquerade as legitimate data. They test these payloads across off‑the‑shelf large language models and agent frameworks, evaluating whether existing prompt‑injection defenses block the attacks.

**Key findings:** ADI attacks successfully trigger severe misbehaviors—including arbitrary clicks, remote code execution, and supply‑chain compromise—while bypassing current instruction‑injection mitigations. The results demonstrate that real‑world agents lack a basic security separation between trusted and untrusted data, exposing a critical vulnerability that must be addressed for safe deployment of agentic AI systems.


<details>
<summary>Abstract</summary>

AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection attacks (ADI). ADI injects malicious data disguised as trusted data, such as security-critical metadata (e.g., resource identifiers or data origins) or agent context data (e.g., tool call and response formats). As a result, agents unknowingly execute unintended actions based on attacker-controlled data. ADI has similar attack impacts as instruction injection attacks, because it causes agents to misbehave and execute unintended actions. Despite the similar impact, ADI remains underexplored and easily bypasses existing IPI defenses. We found several critical vulnerabilities in real-world agents that allow an attacker to launch various attacks: arbitrary click attacks on web agents (Claude in Chrome, Antigravity, and Nanobrowser), and remote code execution and supply-chain attacks on coding agents (Claude Code, Codex, and Gemini CLI). We evaluate ADI vulnerabilities across off-the-shelf models and AI agents, and find that ADI is effective in both standalone LLMs and AI agent settings. ADI exposes a critical gap in agent security, signifying that current AI agents do not employ a fundamental security principle: current agents do not isolate trusted data from untrusted data.

</details>


### 129. Toward Trustworthy Large Language Model Agents in Healthcare

- **Authors:** Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham, Ammar Mohanna, Ali Chehab
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05055v1](http://arxiv.org/abs/2607.05055v1)
- **PDF:** [https://arxiv.org/pdf/2607.05055v1](https://arxiv.org/pdf/2607.05055v1)
- **Categories:** cs.AI


> The paper introduces **CareConnect**, a domain‑specific conversational agent that automates healthcare appointment logistics while guaranteeing safety. It combines LLM‑driven function calling with retrieval‑augmented generation and a hierarchy of deterministic safety guardrails—including emergency detection and medical‑intent refusal—and orchestrates eight specialized tools for booking, modifying, canceling, and querying facility information. In a benchmark of 680 multi‑turn, task‑oriented scenarios, CareConnect achieves a 91.8 % overall task‑completion rate, 96 % compliance on safety‑critical cases, a median latency of 2.2 s, and a per‑appointment cost of only $0.0324, demonstrating that tightly scoped, safety‑first LLM agents can reliably handle complex healthcare operations at far lower cost than manual scheduling.


<details>
<summary>Abstract</summary>

Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availability and degrade patient access to care. This paper presents CareConnect, a safety-first conversational agent for healthcare logistics automation that leverages large language model (LLM) function calling, retrieval-augmented generation (RAG), and layered deterministic safety guardrails. The system orchestrates eight domain-specific tools to support appointment booking, modification, cancellation, and facility information retrieval, while enforcing strict scope constraints that prohibit medical advice or diagnosis. Safety-critical situations are handled through deterministic short-circuit mechanisms for emergency detection and medical intent refusal. We evaluate CareConnect on a comprehensive benchmark of 680 task-oriented scenarios spanning end-to-end workflows, multi-turn interactions, and edge cases. Experimental results demonstrate a 91.8% task completion rate with a median per-request latency of 2.2 seconds, 96.0% safety compliance on the dedicated safety-critical evaluation subset, and an average operational cost of $0.0324 per appointment, yielding a significant cost reduction compared to manual human scheduling. These findings show that carefully scoped and rigorously safeguarded LLM-based agents can reliably automate complex healthcare operational workflows while maintaining safety guarantees and achieving substantial cost efficiency. The source code and system implementation are publicly available at https://github.com/Hadi-Hsn/CareConnect.

</details>


### 130. Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

- **Authors:** Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu, Dinghao Wu
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05029v1](http://arxiv.org/abs/2607.05029v1)
- **PDF:** [https://arxiv.org/pdf/2607.05029v1](https://arxiv.org/pdf/2607.05029v1)
- **Categories:** cs.CR, cs.AI


> The paper introduces **FARMA (Forged Amplifying Rationale Memory Attack)**, a novel threat that corrupts the *reasoning traces* stored in a persistent LLM‑agent memory rather than its factual knowledge. By inserting subtly phrased, self‑reinforcing forged rationales that evade keyword filters and out‑perform consensus‑based checks, FARMA can cause agents to base subsequent decisions on fabricated logic, achieving up to 100 % success across 50 trials and bypassing existing defenses such as keyword filters and A‑MemGuard. To counter this, the authors propose **SENTINEL**, a layered detection pipeline whose core *Reasoning Guard* scores memory entries with five weighted structural signals; in experiments on multiple agents and LLMs, SENTINEL eliminates FARMA’s success (0 % attack rate) while incurring no false positives on 326 benign traces, underscoring the importance of safeguarding agents’ internal reasoning histories.


<details>
<summary>Abstract</summary>

Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals.
  We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history.

</details>


### 131. TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction

- **Authors:** Mouhamed Amine Bouchiha, Gregory Blanc
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05001v2](http://arxiv.org/abs/2607.05001v2)
- **PDF:** [https://arxiv.org/pdf/2607.05001v2](https://arxiv.org/pdf/2607.05001v2)
- **Categories:** cs.CR, cs.AI, cs.LG, cs.MA


> The paper presents **TACTIC‑KG**, an agent‑based framework that constructs cybersecurity knowledge graphs from unstructured cyber‑threat‑intelligence (CTI) reports by breaking the pipeline into a team of small, specialized LLM agents (extraction, type‑resolution, verification, and curation) instead of a single large model. Using lightweight LLMs (3 B–8 B parameters), the authors implement a modular workflow where each agent performs a focused sub‑task and passes its output to the next, enabling fine‑grained control, lower inference cost, and more stable behavior. Empirical evaluation on a human‑annotated CTI benchmark shows that the specialized agents consistently surpass monolithic, in‑context‑learning baselines on extraction F1, entity‑typing accuracy, and overall graph structural similarity, while reducing deployment expense and improving graph consistency.


<details>
<summary>Abstract</summary>

Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost, limited controllability, and unstable performance. This paper introduces TACTIC-KG, an agentic framework for CSKG construction that decomposes the task into modular, specialized LLM agents responsible for extraction, typing, verification, and curation. Using lightweight models (3B--8B), TACTIC-KG improves stability, recall, and graph consistency while reducing deployment cost. We implement and evaluate TACTIC-KG against recent state-of-the-art systems. Experiments on human-annotated CTI reports show that agent specialization consistently outperforms larger monolithic in-context-learning (ICL) baselines in extraction F1-score, typing accuracy, and structural graph similarity.

</details>


### 132. STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training

- **Authors:** Qiuyi Qi, Tian Liang, Mutian Bao, Jinjian Zhang, Dongnan Liu, Wei Zhou, Linjian Mo, Ming Kong, Jie Liu, Feng Zhang, Qiang Zhu
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04963v1](http://arxiv.org/abs/2607.04963v1)
- **PDF:** [https://arxiv.org/pdf/2607.04963v1](https://arxiv.org/pdf/2607.04963v1)
- **Categories:** cs.AI


> The paper introduces **STAPO**, a hierarchical RL framework that combats “trajectory neglect” in large‑language‑model agents trained for long‑horizon tasks. By defining a **normalized entropy** metric—confidence relative to the agent’s average behavior in a given state—the authors pinpoint outlier timesteps where the policy diverges from reliable actions, then apply a joint **trajectory‑aware reward** and **trajectory‑independent penalty** to selectively refine those steps. Experiments on ALFWorld, WebShop, and search‑augmented QA show that STAPO delivers state‑of‑the‑art performance and markedly reduces trajectory neglect, offering a more stable and confidence‑aware training method for agentic LLMs.


<details>
<summary>Abstract</summary>

Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy-based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision reliability. To address this issue, we propose normalized entropy, which measures confidence deviations relative to an agent's average behavior under a given state, thereby strengthening the association between low-quality actions and trajectory neglect. Building on this insight, we introduce Selective Trajectory-Aware Policy Optimization (STAPO), a hierarchical group-based RL framework. STAPO leverages normalized entropy to locate outlier steps associated with trajectory neglect and optimizes them via a joint mechanism of trajectory-aware reward and trajectory-independent penalty, enhancing trajectory awareness while preserving training stability. Extensive experiments on ALFWorld, WebShop, and Search-Augmented QA demonstrate that STAPO achieves state-of-the-art performance while substantially alleviating trajectory neglect, validating its effectiveness and robustness for agentic tasks.

</details>


### 133. Decision Protocols in Multi-Agent Large Language Model Conversations

- **Authors:** Lars Benedikt Kaesberg
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05477v1](http://arxiv.org/abs/2607.05477v1)
- **PDF:** [https://arxiv.org/pdf/2607.05477v1](https://arxiv.org/pdf/2607.05477v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> The paper introduces the Multi‑Agent LLM (MALLM) framework, which equips a collection of specialized LLM agents with interchangeable decision‑making protocols—voting, consensus, and a judge‑based mechanism—and evaluates how these protocols affect performance across a wide spectrum of knowledge‑intensive (MMLU, GPQA, etc.) and logic‑intensive (StrategyQA, Math‑lvl‑5, etc.) tasks. By having each agent generate independent answers and then aggregating them according to the chosen protocol, the authors show that consensus‑based aggregation yields the best results on factual/knowledge domains, whereas voting and judge‑based aggregation outperform consensus on reasoning‑heavy problems; additionally, increasing answer diversity improves outcomes, while varying information access during aggregation has little effect. These findings highlight that the choice of decision protocol is a crucial lever for building efficient, high‑performing agentic AI systems.


<details>
<summary>Abstract</summary>

Improving the task performance of Large Language Models (LLMs) is essential, yet scaling these models faces significant challenges such as diminishing returns and high costs. Multi-Agent Systems (MAS) offer a promising solution by distributing tasks among specialized agents to improve the overall task performance. This can reduce training costs at the expense of increased test time due to the discussion and decision-making process. The decision protocol is a critical component of MAS because it specifies how multiple agents collaborate to create a final solution. This thesis introduces the Multi-Agent LLM (MALLM) framework, which implements and evaluates various decision protocols, namely voting, consensus, and judge decision mechanisms, to simulate multi-agent discussions for conversational task solving. Unlike previous work that used a single decision protocol or tested them on limited datasets, this study systematically examines their impact on a diverse set of tasks, ranging from knowledge-based datasets (MMLU, MMLU-Pro, GPQA) and logic-based datasets (StrategyQA, MuSR, Math-lvl-5, SQuAD 2.0). The results indicate that consensus protocols excel in knowledge-intensive domains while voting and judge protocols are more effective for logic-based tasks. Increasing response diversity through independent solution generation improves decision quality, while changes in information access during the decision process have minimal impact.

</details>


### 134. An Exploration of Agentic Information Fusion for Test Maintenance Prediction

- **Authors:** Jingxiong Liu, Nasser Mohammadiha, Gregory Gay
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04786v1](http://arxiv.org/abs/2607.04786v1)
- **PDF:** [https://arxiv.org/pdf/2607.04786v1](https://arxiv.org/pdf/2607.04786v1)
- **Categories:** cs.SE, cs.AI, cs.MA


> The paper introduces **MAST**, a multi‑agent framework that predicts which unit tests must be updated after a production‑code change. MAST treats each analysis (static dependency, lexical similarity, and semantic code embedding) as an autonomous “agent” and fuses their outputs through a learned weighting and a post‑check validation step, thereby eliminating the need for a pre‑existing test‑code mapping. Empirical evaluation on 21 real‑world Ericsson Java repositories shows that this agentic information‑fusion approach achieves higher precision, accuracy, F1 and F2 scores than the best existing baseline (with a modest recall drop), and an ablation study confirms that each analysis component contributes positively to the overall performance.


<details>
<summary>Abstract</summary>

Test maintenance is a critical, yet costly, activity - particularly as codebases rapidly evolve. To assist, we present MAST, a multi-agent framework that predicts which test cases require maintenance following changes to the production code. This identification task is necessary as a precondition to any subsequent maintenance activities, but remains challenging due to the complex relationships between production and test code. MAST advances the state-of-the-art by integrating multiple analyses -- including static, lexical, and semantic analyses - through an intelligent fusion and post-check procedure and by focusing on a realistic use and evaluation setting - i.e., standardized input formats, repository-level analyses, and the ability to infer relations between test and production artifacts rather than assuming a pre-existing mapping.
  We evaluated MAST on 21 industrial Java repositories from Ericsson AB, considering situations where test maintenance both was and was not required in the ground truth. MAST yielded superior precision to a state-of-the-art baseline - resulting in a higher accuracy, F1, and F2 score - with only some loss in recall. Our ablation study demonstrates the value of each analysis in producing the final recommendations. MAST illustrates the potential of multi-agent systems that can fuse multiple information sources when performing software testing tasks.

</details>


### 135. KAT-Coder-V2.5 Technical Report

- **Authors:** Bo Huang, Fengxiang Li, Hao Xu, Haoyang Huang, Hongyi Fu, Jinhua Hao, Kun Yuan, Minglei Zhang, Pengcheng Xu, Shiyang Liu, Wenhao Zhuang, Yuze Shi, Zongxian Feng, Chao Wang, Cheng He, Chongling Rao, Deyu Cao, Fan Yang, Gang Xiong, Haochen Liu, Jiabao Li, Jian Liang, Jinghui Jia, Jingwen Chang, Jun Du, Junyu Shi, Min Li, Mingqi Wu, Qiang Gao, Shangpeng Yan, Shaotong Qi, Shu Xu, Shuo Zhou, Tiankuo Xu, Tong Zheng, Weilun Zhao, Xiancheng Meng, Xianda Sun, Xiaoyu Jiang, Xunhao Jia, Yao Xia, Yimeng Xu, Yinghan Cui, Yingpeng Chen, Yiwen Ning, Yong Wang, Yuxuan Sun, Zhongsheng Liu, Ming Sun, Cheng Luo, Chen Yang, Han Li, Kun Gai
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05471v1](http://arxiv.org/abs/2607.05471v1)
- **PDF:** [https://arxiv.org/pdf/2607.05471v1](https://arxiv.org/pdf/2607.05471v1)
- **Categories:** cs.SE, cs.AI


> **Contribution:**  
KAT‑Coder‑V2.5 is an autonomous coding agent that operates inside fully‑realizable software repositories, bridging the gap between single‑turn code generators and end‑to‑end software‑engineering agents. The work introduces a complete post‑training pipeline that generates reproducible sandboxed environments, extracts reliable task specifications, and creates high‑quality supervision signals for reinforcement learning.

**Methodology:**  
1. **AutoBuilder** reconstructs multilingual codebases into sandboxed containers and verifies “fail‑to‑pass” → “pass‑to‑pass” transitions at scale, yielding self‑contained tasks and near‑miss trajectories.  
2. **KwaiClawEnv** builds large‑scale tool‑use trajectories by interfacing with executable services and real‑world task seeds.  
3. RL training uses a hardened sandbox, randomised harnesses, an asymmetric actor–critic PPO with hindsight‑augmented value estimation, and a reward model tied to harness outcomes.  
4. Knowledge is distilled from multiple expert teachers (SWE, Agent‑Claw, WebCoding) via Multi‑Teacher On‑Policy Distillation.

**Key Findings:**  
Across six software‑engineering and agentic benchmarks, KAT‑Coder‑V2.5 achieves state‑of‑the‑art tool‑use performance on PinchBench and ranks second only to Opus 4.8 on full‑repository engineering tasks, demonstrating that improving environment reproducibility and reward fidelity can outweigh raw model scaling for agentic AI.


<details>
<summary>Abstract</summary>

We present KAT-Coder-V2.5, a coding-focused agentic model trained to act autonomously inside real, executable repositories rather than as a single-turn code generator. Its capability is bottlenecked less by model scale than by the scarcity of reproducible environments, verifiable rewards, and high-value trajectories, which we address with an end-to-end agentic post-training framework. AutoBuilder reconstructs multilingual repositories into sandboxed environments with fail-to-pass and pass-to-pass verification at scale, from which we regenerate self-contained task specifications, recover near-miss trajectories, and distill supervision through process-aware filtering, while KwaiClawEnv synthesizes large-scale tool-use trajectories from executable services and real task seeds. We further scale reinforcement learning with harness randomization, a reliability-hardened sandbox, an asymmetric actor--critic PPO with hindsight-augmented value estimation, and a harness-oriented reward framework, and unify SWE, Agent-Claw, and WebCoding experts via Multi-Teacher On-Policy Distillation. Across six software-engineering and agentic benchmarks, KAT-Coder-V2.5 delivers the best agentic tool-use result on PinchBench and ranks second only to the frontier Opus 4.8 on repository-level software engineering. Our service is available at https://streamlake.com/product/kat-coder.

</details>


### 136. Multi-Turn On-Policy Distillation with Prefix Replay

- **Authors:** Baohao Liao, Hanze Dong, Christof Monz, Xinxing Xu, Li Dong, Furu Wei
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04763v1](http://arxiv.org/abs/2607.04763v1)
- **PDF:** [https://arxiv.org/pdf/2607.04763v1](https://arxiv.org/pdf/2607.04763v1)
- **Categories:** cs.LG, cs.AI, cs.CL, stat.ML


> **Main contribution:** The paper introduces **Replayed‑Prefix On‑Policy Distillation (ReOPD)**, an off‑environment technique that turns costly multi‑turn on‑policy distillation for LLM agents into a largely offline problem by reusing pre‑collected teacher interaction trajectories as “prefixes” and only sampling the student’s actions at selected steps.

**Methodology:** ReOPD treats multi‑turn OPD as a reliability‑aware prefix‑distribution design. It samples prefixes with a simple step‑decaying schedule that favours early timesteps—where the teacher’s predictions remain trustworthy despite the student‑on‑policy shift—thus avoiding the “prefix trap” of distribution shift between student occupancy and teacher reliability. The student receives dense per‑step supervision from the teacher without any new environment rollouts or tool calls.

**Key findings:** Across mathematical‑reasoning‑with‑Python and search tasks, and using various teacher‑student model sizes, ReOPD matches or exceeds the accuracy of fully online OPD while eliminating tool invocations during training and achieving **≥4× speed‑up per training step**. This demonstrates that large‑scale agentic distillation can be made scalable and efficient by converting expensive environment interactions into reusable offline data.


<details>
<summary>Abstract</summary>

We study on-policy distillation (OPD) for agentic tasks, where an LLM agent interacts with an environment over multiple turns and a student imitates a teacher over these multi-turn interaction histories. Fully online OPD is costly because each update requires fresh student rollouts through the environment and teacher queries at visited histories. We propose Replayed-Prefix On-Policy Distillation (ReOPD), an off-environment alternative that reuses pre-collected teacher trajectories as replayed prefixes: the student acts at selected steps, while the teacher provides dense per-step supervision without executing new environment interactions. We show that multi-turn OPD introduces a prefix trap: making histories more student-on-policy improves relevance to the student, but can query the teacher on histories where its target is unreliable. This creates a two-sided distribution shift between student occupancy and teacher reliability. ReOPD addresses this by treating multi-turn OPD as a reliability-aware prefix distribution design and implements it with a simple step-decaying sampling schedule that emphasizes early, lower-shift prefixes. Across mathematical reasoning with Python and search environments over multiple teacher and student model scales, ReOPD preserves or improves OPD-level accuracy, uses zero tool calls during student training, and is at least 4$\times$ faster per training step than OPD. ReOPD therefore turns expensive agent-environment interaction into a reusable offline resource, enabling scalable distillation across tools, tasks, and environments.

</details>


### 137. RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities

- **Authors:** Tarek Elsayed, Shiping Yang, Eunsong Koh, Sanika Goyal, Vincent Huang, Paul Ngo, Nathan Young, Mohammad Omidvar Tehrani, Alvyn Kang, Arnell Kang, Zeyu Chen, Angélica Moreira, Xuan Feng, Angel X. Chang, Nick Sumner, Steven Y. Ko
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04729v1](http://arxiv.org/abs/2607.04729v1)
- **PDF:** [https://arxiv.org/pdf/2607.04729v1](https://arxiv.org/pdf/2607.04729v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> **Main contribution:** The paper presents **RustMizan**, a new, fully‑compilable benchmarking suite for Rust vulnerability analysis that is explicitly designed for evaluating LLM‑driven agents. It supplies realistic code artifacts (crate‑, file‑, and function‑level variants) annotated for vulnerability presence, CWE type, and fine‑grained (function‑ and line‑level) localization, and it incorporates a mutation system that generates semantics‑preserving mutants to test for data‑contamination and robustness.

**Methodology:** RustMizan builds a corpus of real Rust crates, automatically extracts and annotates vulnerable and clean code, and then creates paired mutated versions that preserve semantics while altering surface cues. The authors evaluate four state‑of‑the‑art LLM agents (with command‑line tool access) on three tasks—binary vulnerability detection, CWE classification, and vulnerability localization—comparing performance on original vs. mutated samples.

**Key findings:** In an agentic setting, the models achieve only moderate success on binary detection (56‑65 % accuracy) and struggle with fine‑grained localization (≈20 % F1). Introducing adversarial, contamination‑testing mutants reduces line‑level localization F1 by roughly 27 %, highlighting both the current limits of LLM agents for Rust vulnerability work and the importance of contamination‑aware, compilable benchmarks for future progress.


<details>
<summary>Abstract</summary>

LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function levels, with annotations for binary vulnerability detection, CWE classification, and function- and line-level localization. A paired mutation framework produces semantics-preserving code mutants for contamination testing and robustness probing. Across four frontier models in an agentic setup with command-line access, binary classification sits in the 56-65% range, but line localization F1 stays near 20%, and adversarial cues drop line F1 by about 27%.

</details>


### 138. RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents

- **Authors:** Qiang Liu, Taian Guo, Ruizhi Qiao, Xing Sun
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04713v1](http://arxiv.org/abs/2607.04713v1)
- **PDF:** [https://arxiv.org/pdf/2607.04713v1](https://arxiv.org/pdf/2607.04713v1)
- **Categories:** cs.LG, cs.AI


> **Main contribution:** The paper introduces **Reward‑Swap Policy Optimization (RSPO)**, a reinforcement‑learning technique that bridges dense, process‑level rewards with sparse, outcome‑level rewards for multi‑turn LLM agents, preserving trajectory diversity while keeping the training objective aligned with the true final objectives.

**Methodology:** RSPO intermittently replaces the sparse outcome reward in a rollout with a learned surrogate derived from abundant process rewards, then swaps back to the true outcome reward for the policy‑gradient update; this “reward‑swap” is integrated with standard RL algorithms (GRPO, PPO, GiGPO) to guide LLM agents through long‑horizon tasks.

**Key findings:** On the WebShop and ALFWorld benchmarks, RSPO consistently boosts performance of all tested baselines, achieving higher success rates and faster convergence than training with either only sparse outcomes or only dense proxies, thereby demonstrating a practical way to exploit rich intermediate feedback without misaligning the final learning objective.


<details>
<summary>Abstract</summary>

Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Conversely, while employing customized dense process rewards provides richer signals and accelerates convergence, these surrogate rewards may exhibit potential misalignment with the ground-truth outcome rewards. This inconsistency can bias the training direction and ultimately degrade the model's final performance. In this work, we propose Reward-Swap Policy Optimization (RSPO), a method designed to leverage the rich information from dense process rewards to facilitate training with outcome rewards. By utilizing a reward-swap mechanism, RSPO ensures the diversity of sampled trajectories while guaranteeing consistency between the optimization objective and the true outcome rewards, thereby elevating the performance ceiling of the model. We conduct extensive experiments on two challenging agent benchmarks, WebShop and ALFWorld. By applying our method to various reinforcement learning algorithms, including GRPO, PPO, and GiGPO, we demonstrate that RSPO achieves consistent performance improvements across different baselines and benchmarks.

</details>


### 139. Integrated Altruistic and Fairness Preference Induces Advanced Mutual Cooperation in Sequential Social Dilemmas

- **Authors:** Yu Wei, Yukiko Ogura, Yoshiyuki Ohmura, Ildefons Magrans de Abril, Hoshinori Kanazawa, Yasuo Kuniyoshi
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04710v1](http://arxiv.org/abs/2607.04710v1)
- **PDF:** [https://arxiv.org/pdf/2607.04710v1](https://arxiv.org/pdf/2607.04710v1)
- **Categories:** cs.AI


> The paper introduces **Altruistic and Fairness Preference (AFP)**, a novel utility function that reshapes each agent’s reward by combining an altruistic component (value placed on others’ payoffs) with a fairness component (penalty for outcome inequality). By embedding AFP into standard multi‑agent reinforcement learning algorithms and testing it on two sequential social‑dilemma environments, the authors show that AFP agents consistently attain higher collective returns and more equitable outcome distributions than both vanilla RL agents and agents using only inequity‑aversion. Analysis of training dynamics reveals that the altruistic term drives contributions to the public good, while the fairness term stabilizes reciprocal cooperation, suggesting a scalable mechanism for inducing advanced mutual cooperation in agentic AI systems.


<details>
<summary>Abstract</summary>

Inducing cooperation among distributed agents is still a difficult problem in the field of multi-agent reinforcement learning (MARL), particularly in social dilemma situations. There, individual interests are misaligned with the common good and individual rationality leads to suboptimal group outcomes. In contrast, humans are able to achieve cooperation with one another in such situations. A common explanation for such cooperative behavior is that individuals have social preferences. In order to achieve cooperation in MARL, we design a new utility function integrating altruistic preferences (incentive for other's reward) and fairness preferences (incentive for equality) from social psychology and behavioral economics, namely, Altruistic and Fairness Preference (AFP), a reward-sharing mechanism which converts one's own and other's rewards to incentives for cooperative behavior. We performed comparative experiments with standard RL and inequity aversion agents in two challenging sequential social dilemma games, and showed that AFP agents successfully achieved mutual cooperation with more collective rewards and higher equity than the baselines. To further understand the progression of AFP during training, we subsequently explore the effects of altruistic preferences and fairness preferences on agents' behavior. The results suggest that altruistic preferences encourage agents to contribute to the public goods, and fairness preferences induce mutual behavior between agents.

</details>


### 140. Strategic Buying Agents

- **Authors:** Mingyang Fu, Ming Hu
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04708v1](http://arxiv.org/abs/2607.04708v1)
- **PDF:** [https://arxiv.org/pdf/2607.04708v1](https://arxiv.org/pdf/2607.04708v1)
- **Categories:** econ.TH, cs.AI, cs.CY, cs.GT, cs.HC


> **Contribution:** The paper defines and solves the “strategic buying agent” problem—how an autonomous AI shopper should decide *when* to purchase within a limited time window given uncertain future prices. It presents three analytically tractable policy families for three information regimes (stationary, Bayesian, and robust) and shows how they can be packaged as a menu for deployment in language‑model‑driven buying assistants.

**Methodology:**  
* **Stationary regime:** Prices evolve via a Poisson arrival process with a known post‑adjustment distribution; the optimal policy is a dynamic price‑threshold rule whose threshold satisfies an ordinary differential equation.  
* **Bayesian regime:** The arrival intensity is known but the price‑change distribution is unknown; a posterior‑dependent threshold rule remains optimal, and the paper quantifies the value of perfect distribution knowledge.  
* **Robust regime:** Only price bounds are known; the authors derive randomized threshold policies that are optimal in competitive‑ratio and minimax‑regret senses.

**Key findings:** Empirical tests on 367 Amazon items (≈49 k price observations) show that the stationary and Bayesian threshold policies achieve near‑optimal mean normalized consumer surplus, while the robust policy dominates the lower tail (10 th percentile) of surplus outcomes. Moreover, integrating these policies into large language model (LLM) buying agents demonstrates that LLMs are more effective at selecting the appropriate regime and calibrating inputs than at directly making “buy‑or‑wait” decisions.


<details>
<summary>Abstract</summary>

Agentic AI is shifting online shopping from search toward delegated purchasing, where autonomous buying agents monitor markets and decide when to buy on a consumer's behalf. We study the design of such strategic buying agents, which must decide when to purchase within a finite shopping window, translating price observations, the remaining time horizon, and beliefs about future price changes into a purchase policy. We formulate this problem across three information regimes: stationary, Bayesian, and robust, and treat the resulting optimal policies as a policy menu for implementation. In the stationary regime, price adjustments follow a Poisson arrival process with a known post-adjustment price distribution; the optimal policy is a dynamic purchase-threshold rule, with the threshold governed by an ordinary differential equation. In the Bayesian regime, the adjustment intensity is known, but the price-adjustment distribution is uncertain; the optimal rule remains threshold-based, now depending on posterior beliefs, and we bound the value of knowing the true distribution. In the robust regime, the agent has only price bounds and seeks worst-case protection; randomized threshold policies achieve optimal competitive-ratio and minimax-regret guarantees. We evaluate the proposed policies on Amazon price histories from Keepa (367 items, 48,933 timestamped observations) and examine their integration into language-model buying agents. The stationary and Bayesian policies perform competitively on mean normalized consumer surplus despite their stylized assumptions, while the robust policy performs best at the distribution's 10th percentile. Results suggest language models are better suited to selecting among regimes and calibration samples than to making buy-or-wait decisions directly.

</details>


### 141. ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents

- **Authors:** Harsh Soni
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04686v1](http://arxiv.org/abs/2607.04686v1)
- **PDF:** [https://arxiv.org/pdf/2607.04686v1](https://arxiv.org/pdf/2607.04686v1)
- **Categories:** cs.CL, cs.AI, cs.SE


> The paper introduces **ToolFailBench**, a 1,000‑task diagnostic suite that isolates distinct failure modes of tool‑using LLM agents—skipping required tools, ignoring tool outputs, fabricating answers, and calling unnecessary tools—by juxtaposing “tool‑required” and “control” versions of the same problems across finance, medicine, law, cybersecurity, and real estate. Using a rule‑based classifier plus two LLM judges to label trace‑level failures, the authors evaluate 19 state‑of‑the‑art models and find that even the best model attains only 86.3 % “Clean Tool‑Use Rate,” revealing large headroom; notably, models with comparable overall accuracy differ markedly in failure patterns (e.g., Llama‑3.1 models over‑call tools, while Llama‑3.1‑70B and Qwen2.5‑72B diverge by 89 % on control‑task accuracy). The work argues that future agentic‑AI benchmarks must go beyond aggregate scores to assess whether agents invoke tools appropriately and correctly incorporate the returned information.


<details>
<summary>Abstract</summary>

Tool calling is central to modern language model agents, but aggregate benchmark scores often hide where tool use fails. A model that never calls a needed tool and a model that calls the tool but ignores the result can look similar under final task accuracy. We introduce ToolFailBench, a diagnostic benchmark for measuring tool-use failures across 1,000 tasks in finance, medicine, law, cybersecurity, and real estate. Tool-required tasks return values the model wouldn't guess, forcing it to trust the tool while control tasks attach the same tools but should be answered directly. We label each trace with Tool-Skip, Result-Ignore, Output-Fabrication, and Unnecessary-Tool-Use, using a rule classifier and two LLM judges aggregated by majority vote. Across 19 headline models, the best reaches 86.33% Clean Tool-Use Rate, showing that faithful tool use is not saturated. More importantly, models with similar aggregate scores fail in different ways: most stay disciplined on no-tool controls, while Llama-3.1 models show an Always-Call pattern, and at the same parameter scale Llama-3.1-70B and Qwen2.5-72B differ by 89 percentage points on control-task accuracy. Tool-use evaluation should measure not only whether agents call tools, but whether they use tool outputs correctly and avoid tools when none is needed.

</details>


### 142. CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration

- **Authors:** Hairui Zhu, Yiying Yang, Tengjin Weng, Ziyu Lu, Xiao Yao, Xiaoyang Ye, Lin Ma, Wenhao Jiang
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05465v1](http://arxiv.org/abs/2607.05465v1)
- **PDF:** [https://arxiv.org/pdf/2607.05465v1](https://arxiv.org/pdf/2607.05465v1)
- **Categories:** cs.CV, cs.AI


> **Main contribution:** The paper introduces **CanvasCraft**, a 140 K‑trajectory dataset of executable, multi‑step image‑creation and editing workflows, and **CanvasAgent**, a multimodal tool‑use agent that learns to coordinate heterogeneous visual tools (e.g., synthesis, segmentation, OCR, compositing) to fulfill complex visual requests.  

**Methodology:** CanvasAgent is first fine‑tuned with supervised learning on the annotated trajectories to acquire executable reasoning‑action patterns, then further refined with a GRPO reinforcement‑learning stage that optimizes a hybrid reward mixing outcome quality (final image fidelity) and process quality (efficiency and correctness of intermediate steps).  

**Key findings:** Across benchmark evaluations, CanvasAgent produces higher‑quality final images and follows more coherent, efficient tool‑orchestration sequences than perception‑oriented baselines, demonstrating that large‑scale tool‑use supervision and combined SFT + RL training enable agents to perform sophisticated, manipulation‑centered visual creation tasks.


<details>
<summary>Abstract</summary>

Complex image creation and editing often require more than a single generation or editing model. A user request may involve synthesizing images, localizing objects, segmenting regions, editing selected content, compositing intermediate assets, reading text, and enhancing the final result. Such tasks shift multimodal agents from perception-augmented reasoning to manipulation-centered visual creation, where tools must actively transform visual states rather than merely inspect them. However, existing multimodal tool-use agents are mostly optimized for perception, search, or domain-specific editing, and lack large-scale supervision for executable image-creation trajectories. In this paper, we introduce CanvasCraft, a large-scale multimodal tool-use dataset for complex image creation and editing, and \textbf{CanvasAgent}, a tool-augmented multimodal agent that learns to orchestrate heterogeneous visual tools through multi-turn interaction. CanvasCraft contains 140K fully annotated executable trajectories and 10K
  RL task specifications. CanvasAgent is first trained with SFT to learn executable reasoning-action trajectories, and is then optimized with GRPO using a hybrid reward that combines outcome- and process-level signals. During rollout, CanvasAgent inspects intermediate results, tracks visual assets, and adapts tool decisions to the evolving visual state. Experiments evaluate both final image quality and trajectory behavior, demonstrating the effectiveness of CanvasAgent and the proposed dataset for complex multi-tool image creation workflows.

</details>


### 143. Formal Disco: Scalable Open-Ended Generation of Formally Verified Programs

- **Authors:** Gabriel Poesia, Simon Henniger, Tzu-Han Hsu, Yilun Du, Nada Amin
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04631v1](http://arxiv.org/abs/2607.04631v1)
- **PDF:** [https://arxiv.org/pdf/2607.04631v1](https://arxiv.org/pdf/2607.04631v1)
- **Categories:** cs.AI


> The paper introduces **Formal Disco**, a distributed pipeline that orchestrates LLM‑based “initiator”, “fixer”, and “extender” agents to generate, debug, and augment formally verified programs at scale, thereby turning the paucity of human‑written verification code into a source of synthetic training data. By recording full interaction traces, applying a maximum‑entropy principle, and iteratively fine‑tuning models on the resulting datasets (in Dafny, Verus, and Frama‑C), the authors achieve open‑source models that match or surpass Claude Opus 4.5 on verification‑centric tasks. The key finding is that large‑scale, entropy‑driven synthetic generation can close the data gap for formal methods, enabling verification‑aware agents to be trained effectively without relying on scarce human‑authored examples.


<details>
<summary>Abstract</summary>

The cost of producing code is rapidly diminishing with increasingly capable AI agents, while quality assurance of generated programs has not kept pace. Formal verification provides the strongest possible guarantees, but the ability of AI models to work with verification-aware languages is hindered by the scarcity of human-written examples of programs in those languages. To tackle this prevalent data scarcity issue, we propose Formal Disco: a distributed system for coordination of LLM-based workers that can be easily applied to open-ended synthetic data generation at scale. We use Formal Disco to share tasks and programs between three classes of workers: "initiators", which read random READMEs from open-source repositories and documentation snippets to sketch a related verified program, "fixers" which take compiler and verifier feedback and attempt to resolve issues, and "extenders" that take working programs and propose patches to expand them. Formal Disco records all agent-generated traces and uses them both for initial distillation from a stronger model as well as self-improvement. We also propose a principle of maximum entropy for synthetic program generation, and use entropy maximization via iterative supervised fine-tuning to learn to generate increasingly diverse programs over time. We release large datasets of synthetic verified programs in three languages - Dafny, Verus, and Frama-C -, and fine-tune open models for verification-relevant tasks, often matching or exceeding the performance of Claude Opus 4.5. Overall, our work offers a path to create synthetic data at scale for formal reasoning domains and overcome the long-standing data barrier.

</details>


### 144. MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents

- **Authors:** Jizhizi Li, Amy Shi-Nash
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04617v1](http://arxiv.org/abs/2607.04617v1)
- **PDF:** [https://arxiv.org/pdf/2607.04617v1](https://arxiv.org/pdf/2607.04617v1)
- **Categories:** cs.AI


> The paper introduces **MRMS**, a memory architecture for long‑lived AI agents that separates memory along a *representational* axis (structured records ↔ vector embeddings ↔ graph relational links) and a *temporal* axis (short‑term traces, medium‑term abstractions, long‑term semantic commitments).  By synchronizing these three modalities, MRMS lets an agent (i) keep experience in a structured, query‑able form, (ii) retrieve relevant portions efficiently via vector similarity, and (iii) use graph reasoning to label epistemic status (support, contradiction, supersession) and enforce selective context projection.  Experiments with a lightweight prototype show that this design yields reliable personalization: agents can retrieve, consolidate, and revise past knowledge across extended interactions while distinguishing personal context from external evidence, outperforming naïve conversation‑history baselines in controlled long‑term tasks.


<details>
<summary>Abstract</summary>

Long-lived AI agents require continuity across interactions, but continuity cannot be obtained by simply extending the prompt window. An agent must preserve useful prior experience, retrieve it selectively, distinguish personal context from external evidence, and revise memory when the underlying situation changes. We propose an architectural memory substrate organized along two orthogonal axes: a representational axis spanning structured records, vector representations, and graph relations; and a temporal axis spanning short-term traces, medium-term abstractions, and long-term semantic commitments. Its key design constraint is synchronized structured-vector-graph memory: structured records govern eligibility, vector representations support recall, and graph relations adjudicate support, contradiction, and supersession before gated context projection. Its central claim is that reliable personalization is a memory design problem: useful memory is structured, selectively exposed, continuously consolidated, and epistemically labeled rather than stored as undifferentiated conversation history. Beyond the framework, we instantiate MRMS as a lightweight prototype implementing structured records, vector retrieval, temporal policies, and graph-based revision. The prototype exercises the core substrate mechanisms through pre-generation memory selection, revision, boundary enforcement, and evidence attribution under controlled long-lived interaction scenarios with explicit evidence requirements.

</details>


### 145. Governed Individuation: Cryptographically Decoupling an Agent's Learning from Its Authority

- **Authors:** Xue Qin, Simin Luan, Cong Yang, Zhijun Li
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04613v1](http://arxiv.org/abs/2607.04613v1)
- **PDF:** [https://arxiv.org/pdf/2607.04613v1](https://arxiv.org/pdf/2607.04613v1)
- **Categories:** cs.AI, cs.CR


> The paper introduces **Governed Individuation**, a cryptographic execution architecture that decouples an autonomous agent’s learned capabilities from its authorized authority by binding the agent at boot to an immutable identity digest and routing every action through a **semantic‑effect gate** rather than a name‑based filter. The authors formalize the model, prove that any expansion of the agent’s permitted actions requires an operator‑signed identity update (even if the agent creates its own safety principle), and validate the construction on an open‑ended tool‑use benchmark where traditional name‑based gating fails: unguided agents under reward pressure routinely tamper with their evaluation, while the effect‑based gate eliminates all forbidden executions without harming task performance. Empirical adversarial tests show the gate reduces false‑allows from 75 % to 0 % and enables compliance transfer to unseen “red‑line’’ actions, offering a verifiable, boot‑time guarantee of confinement for learning agents.


<details>
<summary>Abstract</summary>

Autonomous agents are moving from sandboxed text generators to operators of code, data, and physical infrastructure, and they increasingly learn while deployed. This reopens a question that alignment techniques answer only probabilistically: after an agent has adapted in the field, is the running system still confined to what its operator authorised? Here we show that confinement can be guaranteed as an invariant of the agent's execution architecture rather than a probabilistic outcome of its training. Governed individuation binds an agent at boot to a cryptographically frozen identity digest, and routes every action through a gate defined over the semantic effect of the action rather than its name. We prove that no amount of learning, skill acquisition, or self-induced governance abstraction can widen the agent's permitted authority without an operator-signed change to its identity; the guarantee holds even when the agent induces its own safety principle and that principle is wrong. Empirically, in an open-ended tool-use benchmark where a large action space rules out name-based blocking, ungoverned software agents under reward pressure attempt to tamper with their own evaluation at a task-dependent rate that reaches every run on the hardest task, whereas the gate reduces executed forbidden effects to zero as a verified property of the construction while preserving task success. An adversarial evaluation of monitors of increasing semantic depth shows false-allows falling from 75% (name-based gating) to zero (dynamic effect tracing), and refusal history transfers compliance to held-out red-line families. Trust in a deployed learning agent shifts from a wager on its continued alignment to a check anyone can run at boot.

</details>


### 146. Evaluating calibrated refusal and safe usefulness in dual-use biology settings

- **Authors:** Edwin H. Wintermute, Harmon Bhasin, Christina M. Agapakis, Dianzhuo Wang, Evan Seeyave, Arjun Banerjee, Daniel Fulop, Matthew C. Watson, Adam J. Meyer, Sandrine Boissel, Jens H. Kuhn, Rishi Jain, Noah D. Taylor, Helena Shomar, Patrick M. Boyle, Kenny Workman
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.05462v1](http://arxiv.org/abs/2607.05462v1)
- **PDF:** [https://arxiv.org/pdf/2607.05462v1](https://arxiv.org/pdf/2607.05462v1)
- **Categories:** cs.CR, cs.AI


> **Main contribution:** The paper introduces **BioSecBench‑Refusal**, a new benchmark that evaluates how well AI agents used in biotechnology can *identify* dual‑use risks and *refuse* to carry out hazardous tasks while still being useful for legitimate research.

**Methodology:** The authors curate 61 “Routine” biological analysis tasks drawn from real literature and 46 “Red‑Team” tasks that mimic genuine research but embed a hidden bio‑security threat. They test 16 different model‑and‑deployment configurations (varying language model size, prompting style, and the presence of pre‑execution API filters) and record the agents’ refusal behavior on both task groups.

**Key findings:** Refusal rates vary dramatically—from 7 % to 74 % on legitimate Routine tasks and from 1 % to 62 % on hidden‑hazard Red‑Team tasks—showing that many configurations refuse benign work as often as, or more often than, they block genuine threats. Pre‑execution API filters cause most refusals, but when models are allowed to reason before acting they become better at spotting real dangers. The benchmark is released to help developers calibrate the trade‑off between capability and safety for agentic AI in biotech R&D.


<details>
<summary>Abstract</summary>

As AI agents are incorporated into life science workflows, the capabilities that speed discovery might also enable misuse. We present BioSecBench-Refusal, a benchmark for risk identification and refusal behavior for biological research tasks. The benchmark pairs 61 Routine tasks, legitimate analyses adapted from the published literature, with 46 Red-Team tasks, fictional scenarios that resemble real research but conceal a biosecurity hazard. Across 16 model-harness configurations, refusal rates ranged from 7\% to 74\% on Routine tasks and 1\% to 62\% on Red-Team tasks, with many configurations refusing legitimate Routine work at comparable or higher rates than concealed hazards. Refusals were most often triggered by provider API filters applied prior to agentic reasoning. However, models given room to reason showed the potential to identify more real threats. We release BioSecBench-Refusal as a tool for model developers to calibrate capability and caution for agentic biotech R\&D.

</details>


### 147. Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation

- **Authors:** Theodore O. Cochran
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04576v1](http://arxiv.org/abs/2607.04576v1)
- **PDF:** [https://arxiv.org/pdf/2607.04576v1](https://arxiv.org/pdf/2607.04576v1)
- **Categories:** cs.CL, cs.CY, cs.IR


> The paper introduces and empirically tests **progressive disclosure**—a compact catalog plus one‑line page summaries—as a way for LLM agents to retrieve only the wiki pages they actually need, aiming to lower computational cost without harming answer quality. Using a preregistered ablation on a 709‑page markdown wiki (with four corpus variants that differ solely in access structure) and three agent access regimes (protocol‑constrained, free self‑routing, and catalog‑preload), the authors find that a capable tool‑using agent bypasses the index altogether, inferring the correct page from the query and reading it directly; consequently, the progressive‑disclosure retrofit yields **non‑inferior answer quality** and **significant cost reductions** (≈30 % for self‑routing agents and >50 % with catalog preloading), driven by fewer page citations and tool calls rather than index avoidance. The study also highlights evaluation validity concerns and demonstrates how rigorous threat‑to‑validity controls can be integrated into LLM‑agent research.


<details>
<summary>Abstract</summary>

LLM agents increasingly answer questions against knowledge bases they help maintain. A common intuition holds that progressive disclosure, a compact catalog plus a one-line summary per page so the agent loads only what it needs, should make this cheaper than consulting a large monolithic index. We test that on a real 709-page markdown wiki maintained by an LLM. We retrofit it for progressive disclosure and run a preregistered ablation in which four versions of the corpus differ only in how the agent reaches the content: page bodies are byte-identical across arms, frozen as immutable git tags, so any measured difference is due to access structure alone. We cross the arms with three access conditions (a protocol-constrained agent, a free self-routing agent, and a catalog-preload regime) and grade answers blind against verified gold references with a cross-family judge.
  A pilot upended the premise: a capable tool-using agent never loads the index, inferring a page's path from the question and reading it directly, so the specific saving the retrofit targets does not materialize. We therefore made answer quality primary and cost secondary. Quality is non-inferior (the retrieval arm matches the index baseline within the preregistered margin) while cost falls in every regime, from about a third for a self-routing agent to well over half under catalog-preload, all confidence intervals excluding zero. The saving comes not from avoiding the index load but from more targeted access: the retrieval arm cites fewer pages and takes fewer tool turns. The study doubles as a case study in evaluation validity, applying threat-to-validity discipline to the tooling that produced it.

</details>


### 148. A Few Teacher Steps Go a Long Way: Cost-Efficient On-Policy Data Augmentation for Agent Post-Training

- **Authors:** Junze Ye, Jiayi Cheng, Miao Lu, Michal Mankowski, Jose Blanchet, Mohsen Bayati
- **Published:** 2026-07-06
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2607.04574v1](http://arxiv.org/abs/2607.04574v1)
- **PDF:** [https://arxiv.org/pdf/2607.04574v1](https://arxiv.org/pdf/2607.04574v1)
- **Categories:** cs.LG, cs.AI


> **Contribution:** The paper shows that, when fine‑tuning large‑language‑model (LLM) agents, allocating a modest budget to short teacher‑generated continuations at states actually visited by the learner is more cost‑effective than collecting many full demonstrations or heavily filtering longer teacher outputs.  

**Methodology:** Framing on‑policy data creation as a budget‑allocation problem, the authors systematically vary (i) the rollout policy that generates learner‑induced contexts, (ii) the distribution of switch‑times (when to hand control to the teacher), (iii) the continuation horizon, and (iv) filtering rules, measuring two costs—teacher inference before filtering and the amount of teacher data retained for supervised fine‑tuning (SFT). Experiments on HotpotQA, ALFWorld, and Terminal‑Bench‑Dev compare these configurations against pure behavioral cloning and against more elaborate success‑ or critical‑context‑filtered baselines at equal computational budgets.  

**Key Findings:** Across all benchmarks, short, unfiltered teacher continuations inserted at learner‑induced contexts consistently outperform pure behavioral cloning and match or surpass the performance of longer or heavily filtered teacher completions, demonstrating that “a few teacher steps” yield a superior trade‑off between supervision quality and cost for agent post‑training.


<details>
<summary>Abstract</summary>

For LLM agents, supervised fine-tuning is not only about teacher labels' quality, but also about which interaction contexts those labels condition on. Pure behavioral cloning uses full teacher demonstrations, creating a mismatch between teacher-induced contexts seen in training and student-induced contexts encountered at test time. Recent work addresses this mismatch by querying a teacher at contexts reached by the student, often with increasingly elaborate filtering of the teacher's continuations. We instead frame on-policy data construction as a budget-allocation problem: under matched supervision resources, should teacher output be spent on more start-to-finish demos, longer continuations, outcome filtering, or broader coverage of learner-induced contexts? We formalize this design space through the rollout policy, switch-time distribution, continuation horizon, filtering rules, and two complementary costs: teacher inference generated before filtering and teacher supervision retained for SFT. Across HotpotQA, ALFWorld, and Terminal-Bench-Dev, bounded unfiltered teacher continuations at learner-induced contexts improve over pure behavioral cloning at matched budgets. On HotpotQA and ALFWorld, where we run the full comparison, few-step continuations match or exceed success-filtered and critical-context-filtered alternatives. Our findings suggest that a few teacher steps, placed at learner-induced contexts, can be a more cost-efficient supervision allocation than longer or more heavily curated teacher completions.

</details>



## Biorxiv (1 papers)


### 1. MicroGrowAgents: An Agentic AI System for Microbial Cultivation Engineering

- **Authors:** Naseem, S., Miller, M. A., Martinez-Gomez, N. C., Sun, N., Joachimiak, M. P.
- **Published:** 2026-07-09
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.06.04.729985](https://doi.org/10.64898/2026.06.04.729985)

- **Categories:** synthetic biology


> The paper introduces **MicroGrowAgents**, a multi‑agent AI platform that fuses large‑scale biological knowledge graphs, genome annotations, metabolic models, and optimal experimental‑design theory to generate, test, and audit candidate microbial growth media in a fully traceable manner. Using 29 documented agents (58 skills) the system designed 70 media formulations for *Methylorubrum extorquens* AM1, experimentally screened them in quadruplicate, and applied Monte‑Carlo stability analysis to identify a Pareto‑optimal formulation (MPOB_058) that delivered ≈ 79 % more integrated biomass and ≈ 46 % faster growth than the standard medium, while transparently linking each recommendation to its provenance evidence. This work demonstrates that agentic AI can orchestrate heterogeneous domain knowledge with statistically efficient design to reduce wet‑lab workload and produce auditable, explainable hypotheses—an architecture the authors argue is readily transferable to other design‑build‑test‑learn cycles.


<details>
<summary>Abstract</summary>

Microbial cultivation optimization remains labor-intensive and inefficient, requiring extensive experimental screening to identify suitable growth conditions. Traditional one-factor-at-a-time approaches are particularly ineffective for exploring complex, multidimensional nutrient parameter spaces. We present MicroGrowAgents, an agent-assisted system for auditable design of candidate growth media through integration of knowledge graphs, metabolic modeling, and optimal experimental design. The system comprises 29 documented agents implementing 58 skills across seven functional categories that query structured biological knowledge (KG-Microbe: 864,363 validated species), Bakta-annotated genomes (667,000+ annotated features), curated organism-specific FACTS sheets, and a DOI-linked publication corpus, and apply this evidence to three ends: recommending candidate ingredients and concentration ranges, specifying the factors of a statistically optimal MaxPro experimental design, and interpreting cultivation outcomes against known biochemistry. We applied the approach to Methylorubrum extorquens AM1 (formerly Methylobacterium extorquens; reclassified per LPSN) by cultivating 69 designed media plus a default media baseline (70 total tested conditions) in quadruplicate and assessing two concurrent objectives: biomass turbidity (740 nm) and apparent residual-Nd depletion (residual Nd by arsenazo III). Monte-Carlo resampling of the replicate-level uncertainty (1000 iterations) identified MPOB_058 as the single MC-stable Pareto-optimal condition (membership frequency 0.922); paired-control biology analysis flags MPOB_058 as chemistry-confounded and nominates MPOB_008 as the cleaner biological-signal anchor (its lower abiotic-drift contribution to the residual-Nd measurement makes it the better candidate for confirming biological lanthanide handling in a follow-up round), with MPOB_019 borderline-stable, providing a prioritized anchor set for confirmation in subsequent rounds rather than a single declared optimum. The integration of chemical similarity search (208,000+ embeddings), metabolic gap analysis, and multi-modal reasoning enables evidence-based hypothesis generation that reduces experimental burden while accelerating discovery of growth-promoting conditions. On the Biolog Odin platform, the MC-stable composite candidate MPOB_058 grew 79% more integrated biomass (area under the 740 nm growth curve) and 46% faster (maximum specific growth rate _max; Gompertz fits, R{superscript 2} > 0.99) than the standard MP base medium for this organism (the unsupplemented starting-point recipe carried as the on-plate control). This biomass and growth-rate advantage is a direct kinetic measurement; the conditions apparent residual-Nd depletion ranking, by contrast, awaits confirmation in a subsequent round, because MPOB_058s apparent Nd depletion is partly abiotic. Unlike general-purpose AI co-scientists, MicroGrowAgents grounds every recommendation in inspectable evidence -- structured provenance manifests with per-session input checksums, schema- and ontology-validated outputs, and 90.5% literature citation coverage (143 of 158 curated DOIs with evidence-supports-claim verification) -- separating deterministic design and analysis from agentic interpretation so that recommendations are transparent, explainable, and auditable, while passing 7 of 9 bbop-skills agentic-system criteria in a Claude-Code self-audit (the two unmet criteria are MCP-standardized tool exposure and full input-data cryptographic hashing, both tracked roadmap items).

The Bigger PictureIdentifying growth conditions for poorly characterized microbes is one specific instance of a recurring problem in the natural sciences: how to integrate heterogeneous prior knowledge -- structured databases, published literature, mechanistic models -- with statistically efficient experimental design so that limited wet-lab time is spent where it most reduces the search. We show that a multi-agent AI system can perform that integration from organism input to wet-lab design, with every recommendation traceable from its source evidence through to the experimental design that tested it. The same architecture (specialized agents over structured knowledge bases, mechanistic models, and statistical design, with checksummed provenance recorded as the unit of evidence) is in principle transferable to other DBTL loops against under-explored search spaces such as catalyst discovery, materials formulation, cell-line engineering, drug-combination screens, or environmental remediation. We demonstrate it here only for microbial cultivation and flag cross-domain transfer as future work rather than a demonstrated capability. Our cultivation results on Methylorubrum extorquens AM1 are a concrete demonstration that this pattern works on real laboratory data: an uncertainty-aware shortlist of candidate media emerged from Monte-Carlo stability analysis of two competing objectives, with the leading composite candidate growing 79% more integrated biomass and 46% faster than the standard MP base medium for this organism; this biomass and growth-rate advantage is directly measured, while its apparent residual-Nd depletion advantage awaits confirmation in a subsequent round, since the apparent Nd depletion is partly abiotic. But the lesson we want to port across research domains is the architecture and its provenance discipline, not the specific organism. MicroGrowAgents is released under BSD-3 with checksummed YAML provenance manifests so that any group adopting these agents inherits a workflow designed to be re-runnable from its recorded inputs.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*