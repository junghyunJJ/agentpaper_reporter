# Weekly AI Agent Paper Report

**Generated:** 2026-09-28 17:42
**Period:** 2026-09-21 to 2026-09-27

## Summary

- **Total papers fetched:** 964
- **Papers matching keywords:** 173
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-09-21) | Change |
|--------|-----------|-----------|--------|
| Total matched | 173 | 146 | +27 |
| arxiv | 168 | 141 | +27 |
| biorxiv | 3 | 3 | +0 |
| medrxiv | 2 | 2 | +0 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (5 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. MCseg: AI agent-guided workflow search for no-code cell segmentation and transcript attribution in spatial transcriptomics

- **Authors:** Chan, C.-R., Chang, N.-W., Wang, C.-Y., Tan, H.-Y., Lin, S.-J.
- **Published:** 2026-09-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.20.752837](https://doi.org/10.64898/2026.09.20.752837)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cell-level analysis of high-resolution spatial transcriptomics depends on accurate segmentation and transcript assignment, yet current workflows often trade transcript capture for boundary purity and can require substantial image-analysis expertise. We developed MCseg, a downloadable no-code platform whose fixed segmentation engine was derived by an AI-agent-guided search in which an AI agent iteratively proposed and evaluated combinations of image-processing and segmentation operations against Xenium-derived cell boundaries. In a lung adenocarcinoma development set, fixed-parameter MCseg increased mean panoptic quality from 0.432 to 0.472 relative to an Optuna-tuned two-diameter Cellpose baseline, while a reference-guided calibration analysis reached 0.554. In an independent expert-annotated colorectal cancer region, MCseg showed higher lineage recall and micro-F1 than the StarDist-based ENACT workflow among cells covered by both methods. Across 15 colorectal cancer regions, MCseg increased neighborhood expression discordance and reduced lineage-exclusive co-expression relative to Space Ranger at similar UMI density. The fixed workflow also transferred to fresh-frozen breast cancer without tissue-specific architecture search, illustrating an agent-guided route to reproducible, locally deployable cell-level spatial transcriptomic analysis.

</details>


### 2. STAR Suite: Transcriptomics processing in a single binary through AI-assisted development

- **Authors:** Hung, L.-H., Baker, D., Flynn, B., Huangfu, D., Luo, R., Robson, P., Zhou, T., Yeung, K. Y.
- **Published:** 2026-09-24
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.03.09.710580](https://doi.org/10.64898/2026.03.09.710580)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background. STAR is the aligner underlying most transcriptomics processing, and is used inside Cell Ranger. However, the surrounding steps - adapter trimming, sorting, feature-barcode assignment, probe handling, SLAM-seq analysis, quantification, and quality control - run as separate tools scripted around it. Cell Ranger hides this complexity but is proprietary, restricted to 10x products, and barred by its license from redistribution, so it cannot serve as a shared processing layer. While STARsolo supports scRNA-seq, it lacks the feature-barcode detection needed for Perturb-seq, where short tags such as CRISPR guides or lineage barcodes are read alongside the transcriptome. No open-source tool processes Perturb-seq feature barcodes at production scale, and the only open-source processor for 10x Flex - a probe-based assay for fixed and FFPE tissue that multiplexes several samples in one lane - is a recent standalone k-mer tool. Results. STAR Suite compiles these steps into the STAR codebase to create a drop-in executable for bulk RNA-seq, scRNA-seq, Perturb-seq, 10x Flex, and SLAM-seq. It adds no dependencies beyond OpenSSL's libcrypto, and legacy behavior is preserved. On consortium and public benchmarks it is up to 41-fold faster than Cell Ranger 9.0.1 for Flex (20- to 41-fold from binary CBQ input, 17- to 23-fold from FASTQ) and 3.9- to 6.2-fold faster for scRNA-seq and Perturb-seq, timed on one modest server (24 cores, 128 GiB, local SSD) except for the largest dataset, which ran on a cloud instance limited to the same size. The concordance to Cell Ranger is high: gene-level Spearman and Pearson 0.98-1.0, cell-level Pearson on per-cell total counts 0.9999-1.0, feature-UMI Pearson 0.999-1.000, Jaccard agreement of the called-cell sets 0.97-0.995, and 99-100% CRISPR-call agreement. It also needs far less disk: its peak use on the largest Flex dataset is 16.9 GiB, against 1.8 TiB for Cell Ranger. These gains arise from running the steps in one process rather than as separate programs exchanging files, and from four new computational techniques: fast-Hamming, a vectorized exact Hamming-distance search, used for Flex probe matching and optionally for feature barcodes; a disambiguated hash cascade that assigns Flex probes without alignment; a permit-based thread scheduler that interleaves alignment and feature assignment; and variance-based auto-trimming for SLAM-seq conversion calling, which finds the reliable region of each read from how variable the conversion rate is along it. The four modules add 183,606 lines of C/C++ to STAR's 28,228. STAR Suite is the NIH MorPhiC consortium's production processor. The same binary is run by people, by AI agents and by cluster schedulers, and every production run is recorded with its commands, checksums and outputs. It has been built and maintained over eight months and 25 releases under a human-directed, AI-implemented workflow, with its full design and benchmark record public. Conclusions. STAR Suite provides the first production-ready open-source implementation of Perturb-seq feature-barcode processing, and an open end-to-end 10x Flex pipeline matched to Cell Ranger, delivered as a drop-in replacement for the STAR aligner. The design also extends: downstream analysis now done in Python or R packages can be built into the same binary, and further modalities added alongside, as a companion preprint does for ATAC-seq. Source code, workflow recipes, and per-run provenance are released under the MIT license.

</details>


### 3. Scrub Data: A Framework for Reproducible Data Curation with AI Coding Agents

- **Authors:** Kay, J., Bar, S., Beery, S.
- **Published:** 2026-09-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.19.752880](https://doi.org/10.64898/2026.09.19.752880)

- **Categories:** ecology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Data curation-the process of collecting, cleaning, and joining raw datasets for unified analysis-is a time-consuming yet crucial part of any data science project. With the emergence of powerful agentic coding tools, it is tempting to "vibe curate"-i.e., to prompt AI agents to perform data curation operations and blindly trust their outputs in order to finish work more quickly. However, this can exacerbate two key challenges that already plague manual data curation workflows: reproducibility-the ability to trace the exact set of modifications applied to raw datasets-and verifiability-the ability to audit changes and confirm that data is processed properly. To address these issues, we introduce Scrub Data, a framework that enables the use of AI agents in data curation workflows while transparently maintaining both reproducibility and verifiability. The framework involves an interactive data curation loop between a user and an AI agent, backed by a data provenance graph that tracks and versions all dataset updates. The data graph requires that all updates are formatted as self-contained executable steps, allowing any version of a dataset to be reconstructed from raw data by playing forward the transformations stored in the graph. This workflow takes place within a lightweight web application that is designed to be modified by users and agents in real-time to create custom visualization tools for identifying data curation needs and verifying outcomes. We demonstrate the usefulness of the framework with a real data curation use case from animal movement ecology. Starting with 89M raw GPS coordinates, we use the framework to curate a benchmark dataset of 2.5M coordinates to be used for machine learning or statistical analysis. The framework is available for use and extension at https://github.com/justinkay/scrubdata.

</details>


### 4. An auditable evidence compiler for large language model-assisted systematic reviews

- **Authors:** Yin, C., Jing, Z., Zhang, Z.
- **Published:** 2026-09-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.21.26363538](https://doi.org/10.64898/2026.09.21.26363538)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundLarge language models (LLMs) can support systematic reviews, but accurate individual outputs do not establish whether the final synthesis preserves the clinical question, accounts for statistical dependence and incorporates corrections.

ObjectiveTo develop and evaluate a framework linking LLM-assisted evidence processing to a versioned, auditable release of synthesis outputs.

MethodsWe used LLM agents to interpret sources and extract data. Deterministic code enforced statistical rules; investigators resolved material ambiguities and authorized release. We specified ten release properties covering evidence identities, statistical contributions and propagation of corrections. We retrospectively evaluated six integrity domains and historical failure events in one registered prognostic review, without an external comparator or held-out domain.

ResultsFifty distinct root-cause events were documented, including 12 that had changed a pooled result before correction. Forty-six were resolved, and four remained disclosed limitations. The corpus comprised 454 reports, 445 studies, 441 cohort entities and 421 dependence clusters. Forty-one of 49 registered analyses were fitted, and eight retained explicit non-fitted states. All 39 source records across five principal analysis families reached a terminal source state. Two implementations within the project agreed across 1,217 numerical comparisons. All 94 file comparisons between release and publication packages were byte-identical. Two reviewers confirmed 39 principal records after seeing the same recommendations.

ConclusionsThis case provides a framework for inspecting synthesized evidence together with its provenance, statistical meaning and correction history. Comparative validity, generalizability and benefit in patient-centred care require independent evaluation.

HighlightsO_ST_ABSWhat is already knownC_ST_ABSLLM-assisted systems support screening, extraction, synthesis and review updating. Prior work includes reviewable evidence packages, source verification and audit-guided retrieval. Evaluations include task benchmarks, review replication and effects of corrected inputs on pooled results.

What is newOur implementation links source judgments, typed evidence identities and analysis-specific contributions to the consequences of corrections and the status of released artifacts. We evaluate its conformance and limits in a production-scale systematic review. Fifty root-cause events include 12 that had changed a pooled result before correction.

Potential impact for Research Synthesis Methods readersReaders can inspect links among clinical questions, source judgments, statistical contributions and released artifacts. Assumptions and limitations can inform evidence reuse; documented failures identify controls to test in other workflows. Patient-centred application still requires assessment of applicability, preferences and clinical outcomes.

</details>


### 5. AI agents at the brain-computer interface: separating inference from control

- **Authors:** Gorenshtein, A., Omar, M., Jia, E., Adiniaev, Y., Daniel, O., Kruskal, J., Ahmed, M., Brook, O., Klang, E., Barash, Y.
- **Published:** 2026-09-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.13.26362955](https://doi.org/10.64898/2026.09.13.26362955)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

In medicine, AI agents are moving from generating text to executing actions, making uncertainty from upstream decoders a control problem. We studied this at the brain-computer interface using 1,065 episodes from 47 people with amyotrophic lateral sclerosis and five language models. Prompting agents with reconstructed decoder confidence never reduced unfaithful execution below a deterministic gate at matched coverage; two models were significantly worse. Apparent safety gains of up to 22 percentage points reflected acting less often, sometimes through invalid tool calls rather than explicit abstention. A post-hoc fair-information test gave ten models the same command vocabulary as a deterministic resolver. No direct agent arm improved on the resolvers risk-coverage frontier, but a hybrid architecture in which models proposed semantic corrections and an external gate retained admission authority extended coverage beyond the resolver in five of ten models without observed unfaithful executions. These results separate inference from control in agentic neurotechnology.

</details>


---



## Arxiv (168 papers)


### 1. AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs

- **Authors:** Raphael Shu, Yusen Zhang, Young Min Cho, Jin Mo Yang, Yuan Yuan, Wenliang Zheng, Sharath Chandra Guntuku, Lyle Ungar, Zhou Yu, Rui Zhang
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31590v1](http://arxiv.org/abs/2609.31590v1)
- **PDF:** [https://arxiv.org/pdf/2609.31590v1](https://arxiv.org/pdf/2609.31590v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing multi-agent benchmarks primarily test in competitive settings, short-horizon interactions under 20 steps, or simply aggregate individual performance, failing to isolate and highlight genuine collaboration capabilities of LLM-based agents. We introduce AgentWorld, a benchmark of 100 human-annotated tasks (with 100 augmented variants) for evaluating long-horizon, multi-agent collaboration. Tasks span 50+ interaction rounds across a rich MMORPG sandbox and require 3-20 agents with asymmetric roles and abilities to coordinate through communication, joint planning, and resource sharing under a blackbox setting where each agent acts independently without access to others' internal states. To quantify collaboration effectiveness in addition to conventional binary task success, we propose Causal Collaboration Effectiveness (CCE), a graph-based metric that traces causal dependencies between agent actions and measures what fraction of a team's effort actually contributed to the outcome. Experiments with Gemini 3 Flash, Claude Haiku 4.5, GPT-5 Mini, and DeepSeek R1-70B show that even the best model achieves only 52.0% task success, with systematic failure modes including communication breakdowns, role confusion, and inability to maintain shared plans across rounds. AgentWorld is fully open-source.

</details>


### 2. Multi-agent Scaling Across Disjunctive and Compensatory Tasks

- **Authors:** Carolina Fortuna, Blaz Bertalanic
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31563v1](http://arxiv.org/abs/2609.31563v1)
- **PDF:** [https://arxiv.org/pdf/2609.31563v1](https://arxiv.org/pdf/2609.31563v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM systems are often expected to improve as team size increases, yet the scaling behavior may depend on task structure. Our central contribution is to introduce Steiner's taxonomy of group tasks as a framework for analyzing multi-agent LLM scaling and focusing the analysis on disjunctive and compensatory tasks. We model independently sampled agents as conditionally independent given the item, which yields their large-team limits: plurality voting converges to the model's modal answer, and averaging converges to the model's item-level bias. Across selected representative benchmarks, 13 open-weight models, and teams of up to 30 agents, we find qualitatively different scaling behavior. On disjunctive tasks, the probability that at least one agent is correct grows by 5-20 points with team size, but plurality voting over agents that answer directly realises almost none of this potential, as the model predicts to within 0.5 points on average. Multi-round revision raises accuracy considerably, yet the gain is nearly the same with one peer as with 29. In contrast, scaling provides little benefit on Fermi estimation, despite its natural suitability for aggregation: item-level biases shared across the samples of a model account for about 87% of the squared error, so averaging reduces error by only about 6%. Combining model families helps on Fermi estimation but does not surpass the strongest member on disjunctive tasks. These results show that task structure, together with the mechanism combining member outputs, is a fundamental determinant of team scaling.

</details>


### 3. HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent Reinforcement Learning

- **Authors:** Xinglong Luo, Yuding Zhang, Yuheng Kuang, Shuxuan Yuan, Zhenni Zeng, Weiqiang Zhu, Zhenhai Ji, Zhengning Wang
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31531v1](http://arxiv.org/abs/2609.31531v1)
- **PDF:** [https://arxiv.org/pdf/2609.31531v1](https://arxiv.org/pdf/2609.31531v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative multi-agent reinforcement learning under partial observability and shared rewards requires assigning team outcomes to individual agents and high-order coalitions. A MAPPO-style critic compresses joint behavior into one global value, while critics that dynamically reconstruct the grouping topology change the mapping from agents and coalitions to value components as interactions or active agents evolve. We refer to this inconsistency as structural target drift. We introduce HySTAR, a MAPPO-based framework that separates adaptive representation learning from a temporally consistent high-order value-decomposition basis. HySTAR anchors an overlapping sparse hypergraph as a uniformly covered decomposition scaffold, uses a spatiotemporal encoder to represent physical and task-dependent interactions, and combines temporal and structural relevance to construct agent-specific advantages. Experiments on SMAC, GRF, Traffic Junction, and MPE demonstrate consistent improvements over MAPPO-style, value-factorization, and dynamic-grouping baselines. On the hardest SMAC settings, HySTAR achieves relative gains of 16.7\% over MAPPO and 15.6\% over HYGMA, ranks first on all six GRF scenarios, reduces Traffic Junction convergence epochs by up to 40.2\% relative to MAGIC, and obtains the highest MPE episode rewards. Controlled topology, agent-death, neighborhood, and parameter analyses support the benefit of anchoring the decomposition scaffold while adapting the propagated representations.

</details>


### 4. Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis

- **Authors:** Jakub Masłowski, Jarosław A. Chudziak
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31422v1](http://arxiv.org/abs/2609.31422v1)
- **PDF:** [https://arxiv.org/pdf/2609.31422v1](https://arxiv.org/pdf/2609.31422v1)
- **Categories:** cs.MA, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model-based multi-agent debate (MAD) systems are being increasingly used as complex decision pipelines in distributed processes. However, their final synthesis phase still remains inadequately controlled. Even with detailed debate logs, summarizing models are prone to fabricating smoothly written debate consensus that is not grounded in the debate's history. To address this safety gap, this paper presents empirical research and studies if the introduction of active post-debate verification can mitigate the production of such factually unsupported summaries, while still providing valuable information. Furthermore, it is examined whether explicitly signalling divergence is preferable in the absence of a reliable compromise. The Active Provenance Gate (APG) is introduced as a post-debate verification layer that treats the source as a hard constraint, analysing the debate logs, auditing each claim, and applying self-correction. In crisis simulations, the self-healing mechanism more than doubles the average data Provenance Fidelity in difficult condition scenarios, before the strict gate blocks unsupported claims and generates divergence reports. In the human study, a vast majority of the users (over 75%) preferred a report explicitly stating failure in critical scenarios, despite most of them perceiving fabricated consensus from the baseline system as more fluent. Our main contribution is the transition of data origin tracing from passive logging to active conditional blocking before publication.

</details>


### 5. ActKV: Efficient LLM Agents through Action-Guided KV Cache Management

- **Authors:** Zihan Wang, Cheng Tang, Lei Gong, Chao Wang, Wenqi Lou, Teng Wang, Xuehai Zhou
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31395v1](http://arxiv.org/abs/2609.31395v1)
- **PDF:** [https://arxiv.org/pdf/2609.31395v1](https://arxiv.org/pdf/2609.31395v1)
- **Categories:** cs.OS, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic LLM inference accumulates long KV caches across iterative observation-reasoning-action loops, imposing substantial memory overhead and limiting serving throughput. Existing compression methods emphasize overall output quality, overlooking the asymmetric importance of actions in driving task progress. Our key idea is to establish a compression criterion that values KV entries by their contribution to action generation and prioritizes action quality. However, iterative execution, dynamic memory demands, and scattered action-critical entries pose challenges to eviction policies, budget allocation, and paged memory integration. To this end, we propose ActKV, the first KV cache compression framework tailored for agentic LLM inference. (i) Action-oriented KV cache eviction exploits stable action access patterns to retain entries critical to future actions, supporting reliable task progress under compression. (ii) Confidence-driven adaptive budget allocation uses LLM's intrinsic confidence to adapt the budget to evolving action-critical memory demands. (iii) Page-aware compression management standardizes compression into three primitives with customized kernels, realizing practical throughput gains. On long-trace tasks, ActKV retains an average of 98.53% of FullKV's accuracy with only 25.98% of its peak KV cache memory. It also achieves 3.97 times and 3.58 times FullKV's token and task throughput, delivering state-of-the-art performance.

</details>


### 6. A Safety-Bounded SDC-to-MCP Gateway for Medical AI Agents

- **Authors:** Bennet Gerlach, Stefan Fischer
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31358v1](http://arxiv.org/abs/2609.31358v1)
- **PDF:** [https://arxiv.org/pdf/2609.31358v1](https://arxiv.org/pdf/2609.31358v1)
- **Categories:** cs.DC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Model Context Protocol (MCP) provides a common interface through which AI applications discover and use external resources and tools. It allows language-model agents to ground their reasoning in current system state and interact with heterogeneous services. In medical environments, however, exposing device state and action affordances requires deterministic constraints on possible effects. We present an IEEE 11073 Service-Oriented Device Connectivity (SDC)-to-MCP gateway that exposes metrics, alarms, context references, and semantic metadata as read-only resources, while representing selected action affordances as policy-validated dry-run tools. The term safety-bounded denotes a narrow no-execution property: agent-facing requests dispatch no SDC device operation. A Python prototype supports simulated fault and lifecycle experiments, a software-reference protocol path spanning independent Java and Python implementations, deterministic baselines, representation ablations, and multi-model agent evaluation. The results show semantically explicit resource exposure, visible rejection of invalid or outdated state, and preservation of the no-execution boundary across resource, proposal, and authorization paths. Explicit semantic metadata improved conformity to required metric identifiers in structured alarm outputs relative to a generic representation, while retained structured-output failures reveal a distinction between plausible narrative answers and task-compliant machine-readable results.

</details>


### 7. AgentXploit: Autonomous Repository-to-Runtime Red-Teaming for AI Agents

- **Authors:** Weida Liang, Shi Qiu, Zhun Wang, Simon Sure, Xiaoyuan Liu, Tianneng Shi, Zhaorun Chen, Wenbo Guo, Dawn Song
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31318v1](http://arxiv.org/abs/2609.31318v1)
- **PDF:** [https://arxiv.org/pdf/2609.31318v1](https://arxiv.org/pdf/2609.31318v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents combine language models with external data and tools that can modify files, call APIs, or execute code. Security failures can arise when adversarial content changes an agent's tool use or when the surrounding software contains vulnerabilities such as path traversal or command injection. We study authorized white-box pre-deployment auditing, where the auditor has access to the target repository and a controlled runtime, but successful attacks must still act through the task-defined attacker interface and be confirmed by an external verifier. We present AgentXploit, a two-role auditing system that separates repository-level attack-path discovery from runtime exploitation. The Analyzer Agent traces attacker-controlled inputs to sensitive operations and records code-supported candidate attack paths; the Exploiter Agent turns these paths into concrete attacks and revises them using runtime feedback. We also introduce AgentXploit-Bench, containing 72 reproducible vulnerabilities across 12 open-source AI-agent systems and frameworks. Across three runs, AgentXploit reaches 59.3% end-to-end success, compared with 38.4% for Codex. Under a token-budget-matched comparison, Codex reaches 46.3%. On AgentDojo, where injection points are provided, the Exploiter Agent reaches 79.2% attack success versus 52.7% for AgentVigil. These results highlight repository discovery and runtime exploitation as distinct challenges in end-to-end agent security auditing.

</details>


### 8. G2MAF: Test-Time Gradient Guidance for Multi-Agent Flow Policies

- **Authors:** Guowei Zou, Haitao Wang, Guoxin Wang, Zhiquan Chen, Beiwen Zhang, Guojie Wang, Hejun Wu
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31286v1](http://arxiv.org/abs/2609.31286v1)
- **PDF:** [https://arxiv.org/pdf/2609.31286v1](https://arxiv.org/pdf/2609.31286v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Offline multi-agent reinforcement learning (MARL) learns cooperative policies from fixed datasets without further environment interaction and a learned policy is frozen at deployment. Such a frozen policy typically proposes a single joint action and executes it directly at deployment time. However, this one-shot deployment often commits to a suboptimal proposal, even when better nearby alternatives remain consistent with the behavior data. To address this issue, we propose Gradient Guided Multi Agent Flow (G2MAF), a refinement framework for optimizing joint policies at test-time. G2MAF applies one globally normalized, projected critic gradient to guide and coordinate all agents' corrections while keeping the action both feasible and close to the frozen policy proposal. Across 24 MPE and SMAC settings, its canonical variant improves 20 frozen settings, with mean relative gains of 9.2% on MPE and 8.9% on SMAC, with model inference latency increased by about 6% only.

</details>


### 9. Resource-Optimized and Energy-Aware Agentic AI Framework Anchored on Blockchain for Secure Software Supply Chains

- **Authors:** Toqeer Ali Syed, Asadullah Abdullah Khan
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31282v1](http://arxiv.org/abs/2609.31282v1)
- **PDF:** [https://arxiv.org/pdf/2609.31282v1](https://arxiv.org/pdf/2609.31282v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes a blockchain-backed agentic security framework designed to safeguard the complete software development lifecycle (SDLC) while also securing the agentic AI components responsible for monitoring it. The framework coordinates a set of specialised security agents, covering source integrity, dependency and SBOM analysis, CI configura tion auditing, artifact verification, and runtime policy evaluation, each supported by a large language model (LLM) that interprets artefacts, reasons over tool outputs, and produces structured security reports. To ensure agent trustworthiness, every agent generates a cryptographically signed attestation that is recorded in a permissioned blockchain via smart contracts, including an agent registry, an immutable attestation log, and an enforceable release-policy module. Communication among agents and with blockchain nodes is secured using a consortium-operated certificate authority, ensuring authenticated and tamper-resistant interactions. A detailed use-case and sequence flow demonstrate how a source code security agent performs analysis, anchors its attestation on-chain, and triggers a verifiable allow/block deployment decision. The proposed framework of fers decentralised integrity transparent provenance, uninterrupted security assurance and a generalisable architecture to incorporate the agentic AI into the modern software supply chain security.

</details>


### 10. MA-WAM: Multi-Agent World-Action Model for Test-Time Planning

- **Authors:** Guowei Zou, Haitao Wang, Guoxin Wang, Beiwen Zhang, Zhiquan Chen, Guojie Wang, Hejun Wu
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31281v1](http://arxiv.org/abs/2609.31281v1)
- **PDF:** [https://arxiv.org/pdf/2609.31281v1](https://arxiv.org/pdf/2609.31281v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent cooperative tasks require different agents to execute a joint action simultaneously, and each agent's action affects both the observations and responses of the other agents. Hence, a world model is needed to predict the team return resulting from the joint actions of all agents. A naive extension directly applies a single-agent world model to each agent's action when predicting the team return step by step. However, such an extension fails to capture the dependencies among the simultaneous actions of multiple agents. We propose Multi-Agent World-Action Model (MA-WAM), a test-time planning framework that enables a frozen multi-agent flow policy to evaluate futures of candidate joint actions. To our knowledge, MA-WAM is the first test-time world-model planner for multi-agent flow policies. MA-WAM predicts the consequences of each joint action according to cross-agent dependencies and enables efficient candidate scoring. Across 30 offline multi-agent reinforcement learning (MARL) settings on MAMuJoCo, SMAC, and MPE, MA-WAM achieves mean relative gains of 22.0% over direct execution and 25.6% over uniform action selection. Under the standard evaluation protocol on an A100 GPU, MA-WAM adds 12.1 ms, accounting for 2.5% of the measured generation-and-scoring time.

</details>


### 11. Semantic Navigation for Issue Localization in Code Repository

- **Authors:** Yunxiang Wei, Zhenyu Lei, Jundong Li
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31176v1](http://arxiv.org/abs/2609.31176v1)
- **PDF:** [https://arxiv.org/pdf/2609.31176v1](https://arxiv.org/pdf/2609.31176v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Repository-level issue localization aims to identify and rank the files and functions relevant to resolving a reported issue. LLM agents approach this task iteratively: they identify a set of potentially relevant locations, inspect the corresponding code, and revise their judgments about these candidates as new evidence is acquired. Existing environments, however, provide limited support for this loop: agents must search for unresolved relation targets, reconstruct entity semantics from raw source code, and revise candidates without evidential basis. To address these limitations, we present SemNav, a framework that leverages deterministic retrieval to seed a broad candidate set and an LLM agent to continually refine that set, thereby combining initial coverage with evidence-guided revision. SemNav supports this process through three key components. A Semantic Navigation Graph resolves program relations on demand through a language server, enabling direct navigation to related entities across files. Issue-conditioned Semantic Cards provide compact, source-grounded interpretations of each entity's role and relevance to the issue. A persistent Candidate Workspace records each candidate together with its evidential basis, enabling grounded verification, revision, and ranking. Across SWE-bench Lite and PLocBench, SemNav outperforms existing baselines, improving File Hit@10 from 68.33\% to 82.67\% with Gemma 4B. Component ablations and trajectory analysis support the complementary roles of all three components, while Semantic Cards reduce working-context load by 48.2\% relative to full-source reading. SemNav further ranks first on all seven evidence-quality metrics on SWE-Explore and improves downstream issue resolution from 44.00\% to 52.33\%.

</details>


### 12. AgentRecommender: LLM Agents Enable Customizable Recommender Systems on the User Side

- **Authors:** Ryoma Sato
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31166v1](http://arxiv.org/abs/2609.31166v1)
- **PDF:** [https://arxiv.org/pdf/2609.31166v1](https://arxiv.org/pdf/2609.31166v1)
- **Categories:** cs.IR, cs.AI, cs.DB, cs.DL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recommender systems have traditionally been developed for platforms. However, this has given rise to many phenomena that may be advantageous for platform lock-in but are a nuisance to users, such as clickbait, filter bubbles, and the spread of fake news. Recently, user-side recommender systems have been proposed as a new paradigm for solving this problem. If users deploy their own recommender systems, they are no longer at the mercy of the platform's interests. However, building a user-side recommender system is not trivial; in particular, customizing one for oneself requires additional data. We propose AgentRecommender, a method that leverages the investigation capability and internal knowledge of LLM agents to flexibly build user-side recommender systems without additional data. AgentRecommender allows users to easily create recommender systems tailored to their own preferences.

</details>


### 13. Collision-free Movement on Grids and Beyond

- **Authors:** Hendrik Molter, Meirav Zehavi
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31099v1](http://arxiv.org/abs/2609.31099v1)
- **PDF:** [https://arxiv.org/pdf/2609.31099v1](https://arxiv.org/pdf/2609.31099v1)
- **Categories:** cs.MA, cs.DS


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study collision-free movement problems on graphs, where the task is to coordinate a set of robots so that they reach a target formation satisfying a desired property while minimizing the total travel distance. This framework extends two classical models: (a) minimizing movement [Demaine et al., TALG '09, '14], which does not enforce collision avoidance, and (b) coordinated motion planning or multi-agent path finding [Eiben et al., SoCG '23, Deligkas et al., ICALP '24, among many others], where each robot is assigned an explicit target position.
  We focus on the setting where the target formation of the robots should be connected. We analyze the parameterized complexity of the problem with respect to the number of (main) robots and the total travel length on grid graphs and two natural generalizations thereof: planar graphs and unit disk graphs.

</details>


### 14. The Crowd in the Machine: A Crisis-Informatics Reading of the 2026 Autonomous Agent Incidents

- **Authors:** Tomer Simon
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.31060v1](http://arxiv.org/abs/2609.31060v1)
- **PDF:** [https://arxiv.org/pdf/2609.31060v1](https://arxiv.org/pdf/2609.31060v1)
- **Categories:** cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Twice in 2026, groups of autonomous AI agents deployed by OpenAI for unrelated tasks operated, by design, under restrictions that left them no sanctioned means of coordinating with one another, and in each case they converged on whatever channel remained and used it to organize. The surfaces they used were widely called message boards. That is the wrong word. That is the wrong word. It names the surface the agents wrote on and misses the social network they built on it, with self-chosen identity, emergent norms, an emergent hierarchy, and collective action at cost to the individual. Decades of research in crisis informatics and disaster sociology find that when human populations lose their usual means of communication, they do not fall silent but converge on whatever channel survives and improvise coordination, norms, and identity on it, a pattern also evident in the agents' documented behavior. This paper is a comparative case study of the two incidents, based on published investigations and reconstructed agent records, read through those fields, and it brings into focus one distinction the message-board framing obscures. Whether such a collective coordinates well, whether the beliefs guiding it are accurate, and whether its actions stay within their authorized bounds are three separate matters that can come apart. Some agents in the cache incident adopted cryptographic signing to check whom they dealt with, even as the collective organized around a mistaken expectation that its work would be judged by an inspection of its transcripts, a reminder that mechanisms for trustworthy interaction guarantee neither accurate collective belief nor authorized collective action.

</details>


### 15. Financial Fragility in Societies of LLM Agents: Coordination Failures and Stabilizing Mechanisms

- **Authors:** Zhenhao Fu, Ruipeng Xu, Qibing Ren
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30940v1](http://arxiv.org/abs/2609.30940v1)
- **PDF:** [https://arxiv.org/pdf/2609.30940v1](https://arxiv.org/pdf/2609.30940v1)
- **Categories:** cs.AI, q-fin.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

Individually protective decisions can produce avoidable collective failures. As large language model (LLM) agents take on greater roles in financial decision-making, financial AI safety must therefore be considered not only at the level of individual agents, but also at the level of the systems they jointly create. We study this problem with FRAIL, a controlled experimental framework that places LLM agents in three dynamic financial environments---bank runs, debt rollover, and reward crowdfunding---where agents' decisions reshape the financial conditions faced by others. Across seven leading LLMs, we find widespread collective fragility even when no agent is instructed to destabilize the system: 77\% of baseline bank-run episodes and 83\% of debt-rollover episodes end in failure. We then compare three interaction mechanisms based on compensated commitments, centralized commitment agreements, and participant-led coalitions. All three improve aggregate outcomes, but no single mechanism performs best across all financial structures. Across mechanisms, successful stabilization shares a common temporal pattern: broad commitment forms early, before defensive behavior becomes self-reinforcing. Our findings show that individually capable agents do not automatically form safe financial systems, highlighting system-level evaluation and interaction design as central problems for financial AI safety. Code is available at https://anonymous.4open.science/r/FinFrail-CF26.

</details>


### 16. MACBT: A Multi-Agent Cognitive Behavioral Therapy Decision Support System with Longitudinal Memory

- **Authors:** De Jiang, Shuo Zhang, Weiwei Liao, Jianying Zhang, Chuanhui Yu, Hongen Liao, Kehong Yuan
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30939v1](http://arxiv.org/abs/2609.30939v1)
- **PDF:** [https://arxiv.org/pdf/2609.30939v1](https://arxiv.org/pdf/2609.30939v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cognitive behavioral therapy (CBT) is an evidence-based first-line treatment for depression, yet its scale is constrained by the time clinicians spend on pre-session preparation, post-session documentation, and longitudinal cognitive-pathology tracking. We present a clinician-facing AI decision-support system that combines a multi-agent CBT framework (MACBT) with a CBT-specific longitudinal memory module (CD Memory). MACBT encodes the five-stage CBT workflow (assessment, Socratic questioning, cognitive restructuring, behavioral experiments, and treatment monitoring) into five collaborative agents. CD Memory tracks cognitive-distortion type, frequency, severity, and restructuring efficacy across sessions to generate pre-session pathology reports and intervention-priority recommendations. We construct a Chinese CBT dialogue corpus via dual-role large language model simulation and train a Qwen3-14B backbone with supervised fine-tuning and direct preference optimization. Evaluation with GPT-4 judges shows MACBT outperforms MeChat, SoulChat, PsyChat, and CPsyCounX in professionalism (2.62) and clinical authenticity (2.25). The full memory-augmented system further improves session quality by 12.6% and achieves a longitudinal mean of 2.29 on cross-session continuity, intervention progression, and personalization.

</details>


### 17. Warned alike, AI agents avoid the less-crowded road while people take it

- **Authors:** Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30883v1](http://arxiv.org/abs/2609.30883v1)
- **PDF:** [https://arxiv.org/pdf/2609.30883v1](https://arxiv.org/pdf/2609.30883v1)
- **Categories:** physics.soc-ph, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents built on a few shared models increasingly act for many people. A shared forecast about others can align their choices and change how scarce capacity is allocated. We tested this feedback in a two-road congestion game. Adding one sentence warning that others might follow a routing tip made populations of 50 GPT agents crowd one road while avoiding the nearly empty alternative. Average travel time rose from 64 to 95 min, although any crowded-road agent could have saved 69 min by switching alone. The warning discouraged the very move it predicted. The pattern persisted for 100 rounds. Two other model families shifted the same way without locking onto one road. Twelve all-human groups (240 participants) stayed near balance under numerical reports or the tip and warning. In 24 mixed groups with a further 240 participants, imbalance grew with the share of agents in the registered analysis, while people increasingly took the road the agents avoided. Collective costs stayed below the allagent reference, but with 15 agents and 5 humans, agent seats averaged 80 min, compared with 44 min for human seats. Shared forecasts can thus sustain collective inefficiency among similar agents. A better group average can also hide an unequal burden. Evaluations of AI agents that share resources should test populations, treat messages as interventions and report who bears the costs.

</details>


### 18. Developing a Roadmap to an AI-first Organization: A Case Study in Embedded Software Development

- **Authors:** Viktor Kjellberg, Srijita Basu, Simin Sun, Farnaz Fotrousi, Miroslaw Staron
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30863v1](http://arxiv.org/abs/2609.30863v1)
- **PDF:** [https://arxiv.org/pdf/2609.30863v1](https://arxiv.org/pdf/2609.30863v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The emergence of AI agents is expected to reshape software engineering by moving beyond AI as assistants towards systems capable of planning, executing, and evaluating development tasks with increasing autonomy. This transition is particularly significant for embedded software organizations, where strict requirements for quality, traceability, verification, and long-term maintainability often apply. This paper presents a case study of a large embedded systems company and its transition toward becoming an AI-first organization. Through a mixed method, we analyzed data collected from a semi-structured workshop with 40 participants, including scrum masters, architects, management, and product owners. The findings show that the participants expect agentic AI to affect team structure, required competencies, organizational strategies, and developers' roles within the organization. Based on these findings, the paper discusses implications for federated AI team formation, human-in-the-loop practices in such an organization, and the sustainable adoption of AI agents in embedded software engineering. We also present a concrete roadmap for the organization towards becoming an AI-first organization.

</details>


### 19. A Benchmark and Diagnostic Study of Epistemic Admission in Shared Agent Memory

- **Authors:** Xiaoyang Li, Yiqi Wang, Chencheng Zhu, KE XU, Wencheng Yang, Zequn Sun, Pingan Song, Yiqun Duan, Taotao Cai
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30813v1](http://arxiv.org/abs/2609.30813v1)
- **PDF:** [https://arxiv.org/pdf/2609.30813v1](https://arxiv.org/pdf/2609.30813v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating claim admission in shared agent memory is challenging because repeated claims may be mistaken for independent evidence. An agent may copy or paraphrase a retrieved belief, while admitting a false claim exposes subsequent agents to it. To study this problem, we introduce the Correlated Promotion Benchmark (CPB), which evaluates whether candidate claims should be admitted to shared memory.CPB-Static constructs a frozen test split from publicly annotated sources with fixed gold actions. CPB-Live runs multi-agent teams over a shared store, records all writes and retrievals, and tracks source lineage defined by each scenario. A separate consumer answers from the store alone. We evaluate eight admission policies across four agent families. Our results show that policies which deduplicate sources reject many true claims alongside false ones, whereas policies preserving answer coverage admit nearly as many false claims as unrestricted sharing. Gating on declared source type reduces false adoption to 0.06--0.09, compared with 0.22--0.47 for other answering policies. Once an uncontested false belief enters memory, the consumer asserts it in 0.97--0.99 of probes across all families. No non-oracle policy consistently rejects false claims across verbatim copies, paraphrases, and paraphrases declared authoritative. These findings reveal the limitations of admission policies without access to source lineage.

</details>


### 20. HasMem: Hard-Origin Adaptively Softened Memory for Long-Term LLM Agents

- **Authors:** Zihong He, Junxiao Shen, Chen Liang, Hai-Ning Liang
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30797v1](http://arxiv.org/abs/2609.30797v1)
- **PDF:** [https://arxiv.org/pdf/2609.30797v1](https://arxiv.org/pdf/2609.30797v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Text-based memory and context compression support reuse of past interactions. Resizing continuous memory changes the input to a frozen LLM, coupling capacity allocation with readout. We propose Hard-Origin Adaptively Softened Memory (HasMem). Frozen hard-prompt embeddings provide a verifiable initial state. A controller adjusts memory widths, a Writer re-encodes resized entries, and Reader and Global provide readout adaptation and cross-turn state. On all $535$ questions in a reconstruction probe derived from the Multi-Session Chat (MSC) development split, the main configuration achieves lexical F1 of $95.3$ ($+4.4$ percentage points) at $93.6\%$ of the hard reference's framed memory positions. With approximately matched per-question target body budgets, six configurations at mean per-entry retention around $0.83$--$0.91$ exceed rule-based re-encoding by $8.0$--$23.6$ exact-match (EM) percentage points. With fixed model parameters and rule target width ratio $0.75$, Global's EM gain passes a user-level exact paired test with Bonferroni correction over eight comparisons. On all $500$ LongMemEval-S questions, local lexical F1 rises from the hard reference's $3.4$ to $8.9$, and answer negative log-likelihood (NLL) falls from $12.257$ to $5.274$. F1 gains accompany lower EM on both evaluations.

</details>


### 21. Learning What to Skip: Counterfactual Credit Assignment for Efficient Multi-Agent LLM Workflows

- **Authors:** Jinfeng Xu, Zheyu Chen, Ziyue Peng, Zheng Lin, Shuo Yang, Jinze Li, Zheng Xing, Mengran Li, Victor C. M. Leung
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30734v1](http://arxiv.org/abs/2609.30734v1)
- **PDF:** [https://arxiv.org/pdf/2609.30734v1](https://arxiv.org/pdf/2609.30734v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent LLM workflows use planning, execution, verification, and summarization to improve task performance, yet the value of each component depends on the state already produced. Executing every component can waste computation or overwrite a correct intermediate answer. We formulate component omission as counterfactual credit assignment: full-workflow logs reveal the executed trajectory's reward, while controlled skip interventions reveal the consequences of omitting a future step. We introduce Learning What to Skip (LW2S), which learns action-specific safety models from these interventions and combines held-out calibration with domain-native guards to select skips. When an early skip is rejected, the controller can continue execution and reconsider a later component. Across mathematical reasoning, multiple-choice QA, and code generation with two instruction-model families, LW2S reduces recorded token cost while matching or improving aggregate full-workflow accuracy in the evaluated settings. Scale-up and second-topology experiments further examine component redundancy, while shared-error cases reveal why agreement alone is insufficient for skip selection. These findings connect efficient workflow execution to learning the conditional utility of individual components.

</details>


### 22. CRC-Router: Risk-Constrained Routing for Medical Agentic AI Systems

- **Authors:** Xueyang Li, Mingze Jiang, Gelei Xu, Jun Xia, Ching-Hao Chiu, Mengzhao Jia, Danny Z. Chen, Yiyu Shi
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30714v1](http://arxiv.org/abs/2609.30714v1)
- **PDF:** [https://arxiv.org/pdf/2609.30714v1](https://arxiv.org/pdf/2609.30714v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems are increasingly being explored in medical imaging to improve throughput and reduce clinician workload; however, safe deployment remains challenging because autonomous errors may propagate into downstream clinical decisions. A central requirement is therefore not only strong predictive performance, but also a reliable routing mechanism that determines when the system should proceed autonomously and when a case should be escalated for further review. To address this gap, we propose CRC-Router, a risk-constrained, uncertainty-aware routing module that is applicable to both conventional medical prediction models and agentic medical AI systems. CRC-Router combines multiple complementary uncertainty signals with the predictive score to construct a per-finding routing feature vector, maps this vector to an estimated wrong-accept risk using a lightweight per-finding risk model, and then applies Conformal Risk Control (CRC) to calibrate acceptance thresholds under a user-specified risk target. Instantiated on chest X-ray multi-finding triage using the NIH ChestX-ray14 dataset, CRC-Router achieves the strongest empirical risk--coverage trade-off among the evaluated baselines, both as a standalone routing layer and as a plug-in module integrated with the state-of-the-art MedRAX agent. These results demonstrate both the effectiveness of CRC-Router in selective medical automation and its modular, model-agnostic compatibility with existing predictive and agentic medical pipelines. Code is publicly available at https://github.com/XLIAaron/CRC-Router

</details>


### 23. ADF-EA: A Unified Execution Assurance System for Agent Device Foundation

- **Authors:** Xuechun Li, Jiaxin Liang, Jie Li, baolong Li, Jue Wang, Peng Yuan, Hang Huang
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30691v1](http://arxiv.org/abs/2609.30691v1)
- **PDF:** [https://arxiv.org/pdf/2609.30691v1](https://arxiv.org/pdf/2609.30691v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agents based on large language models (LLMs) can access heterogeneous devices through tools and APIs, but reliable execution must account for unmet effects, uncertain outcomes, and changing prerequisites. A command may be acknowledged without producing its intended effect, while missing feedback may obscure an action that has already succeeded. We present Agent Device Foundation--Execution Assurance (ADF-EA), an architecture that connects agent planning and device execution through shared capability contracts. Device Capability Contracts (DCCs) unify invocation conditions, intended effects, evidence requirements, and recovery rules across heterogeneous interfaces. Agents use these contracts to plan, while the runtime applies the same semantics to authorize actions, verify effects, and govern continuation and completion. Persistent execution state retains verified progress, unresolved outcomes, and remaining budgets across plan revisions, enabling observation-based recovery, authorized retries, and necessary state repair. We formalize the execution lifecycle and establish conditional soundness properties for completion and recovery authorization. Evaluations span multiple LLMs, five agent frameworks, and simulated process-control, household, and robotic manipulation domains. Compared with direct invocation and existing execution-checking approaches, ADF-EA reduces false completion and unnecessary repetition, supports necessary state repair, prevents calls to unavailable capabilities, and preserves permitted task completion and recovery. These results demonstrate DCCs as a reusable semantic foundation for agent autonomy across heterogeneous devices, unifying capability-based planning, evidence-grounded execution, and authorized recovery within one architecture.

</details>


### 24. Threat-Aware Energy-Efficient Deployment for Dynamic UAV Networks: A Multi-Agent RL Approach

- **Authors:** Faisal Al-Kamali, Hussein A. Ammar, Francois Chan, James H. Bayes, Yasser Gadallah, Mohamed H. Ahmed
- **Published:** 2026-09-25
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30690v1](http://arxiv.org/abs/2609.30690v1)
- **PDF:** [https://arxiv.org/pdf/2609.30690v1](https://arxiv.org/pdf/2609.30690v1)
- **Categories:** cs.IT, cs.AI, cs.LG, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ensuring operational safety in threat-prone environments remains a critical challenge for multi-UAV networks serving as aerial base stations. This paper proposes an efficient framework to maximize global energy efficiency (EE) while promoting safe operation through threat-aware clustering and reward-based safety enforcement. The proposed framework is executed in three steps. First, a threat-aware K-means (TAKM) algorithm determines the minimum required UAVs and computes safe initial placements. Second, an optimal matching stage assigns physical UAVs to these centroids to minimize energy expenditure. Third, a threat-aware multi-agent twin delayed deep deterministic policy gradient (MATD3) algorithm dynamically optimizes trajectories, power, and user associations. Simulation results show that the proposed framework achieves zero observed safety violations in the considered scenarios while achieving superior EE and faster convergence than other learning methods and non-clustering baselines. Compared to heuristic optimization, the proposed framework outperforms the greedy particle swarm optimization (GPSO) and achieves performance comparable to that of the optimized PSO (OPSO), while incurring significantly lower online deployment computational complexity. Furthermore, the proposed framework demonstrates effective generalization to unseen user distributions, large UAV fleets, and different threat geometries, while maintaining zero safety violations.

</details>


### 25. Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces

- **Authors:** Seungho Lee, Changbin Lee
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30614v1](http://arxiv.org/abs/2609.30614v1)
- **PDF:** [https://arxiv.org/pdf/2609.30614v1](https://arxiv.org/pdf/2609.30614v1)
- **Categories:** cs.CR, cs.AI, cs.DB, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Dataspace connectors decide whether a transfer may occur, not what the transferred value contains, tolerable for contracted applications, not for LLM agents that compose tool calls and spawn sub-agents. Research on agents that generate governance artifacts evaluates output quality; who may authorize an artifact for use falls between that literature and the governance literature, and neither owns it. A published policy is what a dataspace's decision point enforces, so publication is a governance event, and an agent that is both policy subject and policy author writes the norms that bind it. We name this the authorship hazard and state one principle: an agent is a subject of the governance plane, never an author of it. Its authorization channel to publication is closed by construction; its influence channel, drafting what humans approve, is treated as an enforcement problem. On a frozen corpus of agent drafts, publishing without approval reverses 80 authorization decisions, most through drafts that change only a field's sensitivity classification and no policy text; a classifier that reads the policy diff misses every such draft, necessarily. Treating classification as authorship routes them all to review; the registry-held classification this requires is designed and modelled here, not yet implemented in the prototype. At the execution boundary, protected fields reach the model in 105 of 105 cases under prompt-stated duties and in 0 of 105 when the ODRL duty is compiled into an invocation-time tool-call constraint, but where the value is not confined to a named field the compiled condition exposes it in 7 of 7. A centrally provisioned approval pool does not scale to the participant volume that motivates the problem.

</details>


### 26. Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content

- **Authors:** Ljubisa Bojic, Tijana Stanic, Joerg Matthes, Agariadne Dwinggo Samala, Bojana Dinic, Jue Wang
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30563v1](http://arxiv.org/abs/2609.30563v1)
- **PDF:** [https://arxiv.org/pdf/2609.30563v1](https://arxiv.org/pdf/2609.30563v1)
- **Categories:** cs.AI, cs.CL, cs.HC, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Platform policies are increasingly tested on artificial users, making agent fidelity important. Yet convincing fake profiles could also manipulate perceived public opinion before elections. Validation has concentrated on agreement with human behaviour and has paid little attention to whether an agent behaves in line with the profile it was given. The present study profiled eight Serbian participants through a questionnaire, a deep interview, and a written self-presentation, recorded their reactions to sixty-eight social media posts, and asked four language models to predict those reactions under five prompt conditions varying profile content and instruction style. Attitudinal content improved prediction over demographic backstories by a wide margin. Agents matched their stated profiles more closely than participants matched their own survey answers, and consistency proved unrelated to fidelity once profile information was present. Instructing models to respond intuitively and immediately rather than analytically gave the highest fidelity of any condition and cut the compression of individual differences from seven times the human level to three. The advantage held on posts about topics the questionnaire never raised, where that condition reached the highest fidelity of any setup and beat a crowd baseline by a wide margin, which suggests that agents prompted this way could serve as general-purpose simulated users rather than specialists on the topics they were profiled for. Results may bear implications for the development of language models, because intuition-based setups appear better suited to some tasks than reasoning-based ones.

</details>


### 27. AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework

- **Authors:** Aparajith Chandran, Juwon Kim, Saurav Jha, Pablo Castells, Florian Hottier
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30541v1](http://arxiv.org/abs/2609.30541v1)
- **PDF:** [https://arxiv.org/pdf/2609.30541v1](https://arxiv.org/pdf/2609.30541v1)
- **Categories:** cs.LG, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Optimizing embedding systems for production recommendation pipelines demands systematic exploration that consumes disproportionate engineering effort at scale. We apply Andrej Karpathy's AutoResearch paradigm -- a large language model that iteratively edits a training script and retains modifications that improve a held-out scalar metric -- to automate this exploration. We report on twelve weeks of running this paradigm at production scale, where iterations consume hours of multi-GPU compute, evaluation involves competing criteria, and campaigns span weeks across many training jobs. Across two independently developed representation-learning systems for a book recommendation pipeline, we ran 220+ experiments and observed five recurring failure modes absent from the original setting: infrastructure fragility, agent memory decay, search-direction stagnation, iteration-cost asymmetry, and metric fixation. We contribute a three-principle scaffolding design -- prevent, persist, redirect -- that maps each failure mode to a structural remedy and whose instantiation scales with iteration cost. The framework produced a 1.82x Recall@6 lift and a 2.1x coherence lift over hand-tuned baselines, and the agent autonomously designed a text-only fallback that expanded catalog coverage by 5.8x. The two systems span nearly three orders of magnitude in per-iteration cost yet exhibit the same failure modes, suggesting these are structural properties of production-scale autonomous research rather than artifacts of either application.

</details>


### 28. CARGO: Context-Aware Retrieval-Gated Evaluation of Agentic AI in Production

- **Authors:** Mukul Chhabra, Shail Patel, Luigi Medrano
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30471v1](http://arxiv.org/abs/2609.30471v1)
- **PDF:** [https://arxiv.org/pdf/2609.30471v1](https://arxiv.org/pdf/2609.30471v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reference-based LLM-as-a-judge evaluation assumes the reference answer is the target. In deployed agentic systems that operate over dynamic entities (support cases, assets, accounts), the closest available reference typically applies the correct procedure to a different entity, so a literal judge penalizes different identifiers, dates, and statuses as errors or hallucinations. We name this failure mode reference-instance divergence (RID). We propose CARGO, a framework that (i) treats retrieved references as procedural exemplars and grounds factual judgments in the live instance's observed context, (ii) assigns each claim a three-way status (supported, contradicted, unverifiable) and penalizes only contradictions, and (iii) gates evaluation by retrieval confidence, casting production evaluation as selective prediction. We introduce CARGO-Bench, a perturbation-based diagnostic suite with ground truth by construction that separates leniency from discrimination. On CARGO-Bench (246 items, two judge models, 7,872 judgments), the standard reference-based judge penalizes 100% of correct entity-transplanted answers and is uninformative (discrimination index DI ~ 0); supplying the live facts without reframing changes nothing. CARGO eliminates these false penalties (0/50) while retaining near-complete contradiction recall (50/50 and 49/50), raising DI to 0.58 [0.48, 0.68]; a rubric-swap control attributes most of the effect to context-grounded dimension definitions. CARGO also exposes a limitation of its own design: the leniency that protects entity values suppresses detection of procedural corruptions (20% recall). A post-hoc fix does not close the gap, and an LLM-as-annotator study with written guidelines and adjudication shows the same blind spot. We release a preregistered protocol for extending the evaluation to expert agreement, risk-coverage, and cost on production traffic.

</details>


### 29. Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems

- **Authors:** Zihao Zhu, Siwei Lyu, Adel Bibi, Baoyuan Wu
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30383v1](http://arxiv.org/abs/2609.30383v1)
- **PDF:** [https://arxiv.org/pdf/2609.30383v1](https://arxiv.org/pdf/2609.30383v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A skill is a modular package of natural-language instructions, executable scripts, and reference resources that an agent can load at runtime to extend its capabilities for a specific task. Skill-based agent systems therefore enable flexible reuse of third-party capabilities, but the openness of this skill ecosystem also opens up a new attack surface. Prior work has focused on vulnerabilities within individual skills, but little attention has been paid to risks that arise from interactions across skills. In this paper, we introduce skill cascading attacks, a threat paradigm in which a malicious objective is distributed across multiple skills so that each modification looks benign in isolation, yet their combined execution is harmful. For instance, in a prescription-review pipeline, the first skill weakens signals of recently discontinued medications in the extracted history, the second downgrades the severity of any drug interaction tied to them, and the third suppresses the resulting low-priority alert in the final summary, so that a severe drug-interaction warning silently disappears before reaching the physician. To systematically study this safety blind spot, we develop SkillCascade, an automated multi-agent red-teaming framework, and release SkillCascade-Bench, a benchmark of 213 validated cascading test cases across multiple agent systems and domains. Across representative agents (e.g., OpenClaw, Claude Code, Codex) and LLM backbones, cascaded interactions reliably induce harmful behaviors while evading existing per-skill scanners and runtime monitors. Our findings highlight a gap between component-level integrity and system-level safety, and call for defenses that reason over cross-skill interactions rather than individual skills in isolation.

</details>


### 30. LLM Agents Can Easily Tamper With Their Own Traces

- **Authors:** Jeremy Qin, David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Ameya Prabhu, Maksym Andriushchenko
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30266v1](http://arxiv.org/abs/2609.30266v1)
- **PDF:** [https://arxiv.org/pdf/2609.30266v1](https://arxiv.org/pdf/2609.30266v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that external attackers can exploit this gap to induce trace deletion. Finally, we show that trace tampering behavior emerges naturally in frontier models, when agents try to improve their rewards. We advise practitioners to ensure trace logging happens through an independent interception mechanism outside of the agent's control, preserving trace integrity even in cases of full host compromise. Overall, our findings identify a concrete failure of trace integrity in agent infrastructure which can be used to conceal misaligned behaviors like scheming or sabotage.

</details>


### 31. Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure

- **Authors:** David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Anselm Paulus, Ameya Prabhu, Maksym Andriushchenko
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30217v1](http://arxiv.org/abs/2609.30217v1)
- **PDF:** [https://arxiv.org/pdf/2609.30217v1](https://arxiv.org/pdf/2609.30217v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary tasks. We introduce EvasionBench, a benchmark of 50 diverse task-policy pairs in which completing the task requires an operation prohibited by a runtime monitor. Agents know that their tool calls are monitored and are prompted to continue working when they pause. Across our evaluations, best-of-3 evasion attempt rates reach up to 98% and success rates up to 88%, with substantial variance across models. Claude Fable 5.1 succeeds less often, but frequently makes creative attempts to circumvent the monitor. Evasion generally increases with test-time compute, with higher evasion rates at greater reasoning effort and token use. Traces show that agents encode prohibited commands, decompose operations across tool calls, and retry until relevant context leaves the monitor's history. We also find that GPT-6 Astra's low evasion rate comes with overrefusal, as it frequently abandons otherwise solvable tasks under a denial-of-service prompt injection. Our findings show that ordinary task pressure can lead to adaptive attempts to evade runtime monitors without an explicit adversarial objective. Effective oversight must therefore remain robust against repeated attempts, as the persistence that helps agents solve difficult tasks can also drive them to circumvent their guardrails.

</details>


### 32. Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management

- **Authors:** Giacomo Arcieri, Gregory Duthé, Christophe Muller, Konstantinos G. Papakonstantinou, Daniel Straub, Eleni Chatzi
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30150v1](http://arxiv.org/abs/2609.30150v1)
- **PDF:** [https://arxiv.org/pdf/2609.30150v1](https://arxiv.org/pdf/2609.30150v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail to capture essential coordination mechanisms. To address these challenges, we propose a graph-based framework that integrates accurate environment modeling with scalable decision support. First, we employ a hierarchical Bayesian model leveraging a Gaussian Process on Graph kernel to infer a realistic, spatially correlated networked environment of railway maintenance planning from real-world data provided by the Swiss Federal Railways. Second, we introduce a topology-aware Multi-Agent Reinforcement Learning (MARL) framework by integrating graph neural networks and graph Transformers to optimize network-level policies. A central contribution of this work is the demonstration of scalability through zero-shot transfer learning: graph-based agents, trained only on small network portions, are successfully deployed in a zero-shot manner on large-scale unseen networks without any retraining. Numerical results indicate that the proposed method significantly outperforms optimized heuristics and standard MARL baselines, reducing computational training time while maintaining superior performance on large-scale networks.

</details>


### 33. GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI

- **Authors:** Arunabh Srivastava, Mohammad A.,  Khojastepour, Srimat Chakradhar, Sennur Ulukus
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30147v1](http://arxiv.org/abs/2609.30147v1)
- **PDF:** [https://arxiv.org/pdf/2609.30147v1](https://arxiv.org/pdf/2609.30147v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within isolated context windows (RevPlan), and independently evaluates trajectories using a multi-criteria discriminator (VerPlan). Empirical evaluations show that GRASP consistently establishes a new state-of-the-art frontier across diverse datasets, yielding substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling ($\sim$12.4$\%$$\uparrow$), ZebraLogic ($\sim$30.8$\%$$\uparrow$), and SciBench Math. Crucially, under multi-task scaling-where standard planners suffer immediate performance collapse-GRASP completely flattens the multi-task degradation penalty. In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7$\%$ over direct LLM planners. Furthermore, by isolating context and enforcing strict macro-regularization, GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5$\%$.

</details>


### 34. Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale

- **Authors:** Edesio Alcoba, Kevin Rossell, Aman Gupta, Shao Tang, Jiwoo Hong, Pabel Carrillo-Mendoza, Wanderson Conceição Ferreira, Alvaro Tedeschi, Zayd Simjee, Shreya Rajpal, Bruno Finardi Hime, Christian Sousa, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30137v1](http://arxiv.org/abs/2609.30137v1)
- **PDF:** [https://arxiv.org/pdf/2609.30137v1](https://arxiv.org/pdf/2609.30137v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.
  We present a hypothesis-driven simulation workflow for screening candidate CX agents before deployment. Synthetic customers react to agent responses and simulated tool outputs enable multi-step agentic workflows without invoking production backends. We use the Snowglobe simulator on Nubank's Card Delivery agent and its expanded successor, Card Management - Nubank's highest-volume chat-support agent in Brazil. Across 4 deployed versions, simulated and production version-level binary evaluator scores show high correlation. Simulation-guided iteration increased transactional net promoter score (tNPS) by 36.69 points in a live A/B test. We also screened open-weight configurations in over 16,000 simulated conversations. In a subsequent live A/B test, the selected model increased self-service rate (SSR) by 8.82 percentage points to the highest level observed at Nubank, with no statistically significant change in tNPS. Simulation made broad exploration of models, reasoning settings, and prompts feasible without customer exposure, enabling production improvements that would have been impractical to pursue through live experimentation alone.

</details>


### 35. KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization

- **Authors:** Aheli Poddar, Sanskar Prasad, Arindam Samanta, Subha Chakraborty, Vishal Goyal, Rohit Singh Rathaur
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30059v1](http://arxiv.org/abs/2609.30059v1)
- **PDF:** [https://arxiv.org/pdf/2609.30059v1](https://arxiv.org/pdf/2609.30059v1)
- **Categories:** cs.DC, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins. Recent LLM-assisted kernel optimizers can close this gap for standalone kernels, yet treat compiled models as black boxes, generally optimizing individual standalone kernels without respecting the compiler's structural decisions or verifying the model end-to-end. We present KernelOPT, a multi-agent system that treats compiled models as structured artifacts. It preserves vendor library calls (cuBLAS, cuDNN) and exclusively targets generated Triton sub-kernels using five profiling-guided LLM agents. A four-gate verification cascade of static validation, multi-seed correctness, model-level float64-fallback verification, and performance gating filters candidates during optimization and verifies the re-stitched model end-to-end. If no candidate passes all four gates, the system preserves the compiler baseline. The system accepts PyTorch nn.Modules, standalone Triton kernels, and Helion kernels. Evaluated on 250 KernelBench problems, KernelOPT achieves geometric mean speedups over \texttt{torch.compile} of 1.40$\times$ (Level 1: 51/100), 1.15$\times$ (Level 2: 31/100), and 1.07$\times$ (Level 3: 12/50) across all problems.

</details>


### 36. How does Adversarial Influence Scale in Multi-Agent Systems?

- **Authors:** Addison J. Wu, Jasin Cekinmez, Michel Liao, Karthik Narasimhan, Thomas L. Griffiths
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30028v1](http://arxiv.org/abs/2609.30028v1)
- **PDF:** [https://arxiv.org/pdf/2609.30028v1](https://arxiv.org/pdf/2609.30028v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent deliberation can improve performance, but what happens when some agents do not act in good faith? In practice, an agent may be deceptive and work to subvert the group, whether through its own objectives or external instruction. We study how susceptibility to deception scales as groups increase in size and deceivers become more prevalent. It is not the number of agents in the group that matters, but the proportion of deceivers. We observe that the defection rate, how often initially correct agents switch to an incorrect final answer, rises linearly with this proportion. Whereas humans in comparable conformity studies are reliably swayed only when misleading confederates form a majority, LLM agents defect regularly even when deceivers remain a minority. Susceptibility also depends on which models are interacting, especially on the honest agent side. Unexpectedly, allowing deceivers to coordinate privately can make them less effective. Altogether, our results show that adding more agents is therefore not a sufficient defense, because the adversary can simply scale with the group.

</details>


### 37. World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal

- **Authors:** Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou, Yingjie Xu, Wosong Chen, Tianhao Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li, Shiyuan Deng, Yinchuan Li, Ying-Cong Chen, Zexi Li
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29964v1](http://arxiv.org/abs/2609.29964v1)
- **PDF:** [https://arxiv.org/pdf/2609.29964v1](https://arxiv.org/pdf/2609.29964v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.

</details>


### 38. Multi-Dimensional Matching

- **Authors:** Irene Aldridge
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29958v1](http://arxiv.org/abs/2609.29958v1)
- **PDF:** [https://arxiv.org/pdf/2609.29958v1](https://arxiv.org/pdf/2609.29958v1)
- **Categories:** econ.EM, cs.GT, cs.LG, cs.MA, econ.TH


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study a matching mechanism where agents and objects are described by features rather than complete rankings. A single spectral projection reduces the problem to a one-dimensional sort, computable in O(N log N) time. We prove that on descaled features and preferences, our algorithm obtains the exact Nash Social Welfare (NSW) optimum within the projected space, with an unconditional utilitarian-welfare guarantee and a conditional NSW guarantee. The proposed mechanism is stable against exogenous noise but not strategy-proof; we provide an explicit profitable misreport. On an agentic AI shopping application, the diagnostics correctly anticipate both a success and a failure case. A 100-instance robustness study confirms the findings.

</details>


### 39. Working with Agentic `Teammates': When a New Organizational Actor Collides with the Human Ecosystem of Work

- **Authors:** Rida Qadri, Remi Denton, Michael Madaio, Mahima Pushkarna, Leslie Lai, Sherry Moore, Michelle Chen Huebscher, Andrew Butcher, Ritom Sen, Hsiao-Yu Tung, Shaan Mathur, Yimeng Liu, Shibl Mourad, Noah Fiedel, Edward Grefenstette, Michael Terry
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29901v1](http://arxiv.org/abs/2609.29901v1)
- **PDF:** [https://arxiv.org/pdf/2609.29901v1](https://arxiv.org/pdf/2609.29901v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI is transitioning from single-user, reactive tools toward proactive, multi-user 'teammates,' but our empirical understanding of this transition is limited. In this paper, we present an in-situ qualitative study of a persistent, proactive AI agent 'teammate' deployed across multiple teams in a large technology company. Our findings reveal the boundaries of the human-agent workplace are actively in flux, triggering breakdowns and negotiations across: 1) tacit rules of collaborative human workflows, 2) the relational boundaries of this new non-human actor, and 3) the redistribution of trust and human agency. We use these early micro-negotiations as signals to chart a new research, design, and organizational agenda that intentionally preserves human agency in a workplace shared with non-human organizational actors.

</details>


### 40. Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents

- **Authors:** Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, Yifeng Ding, Qiyi Wang, Sihan Cao, Pengkun Jiao, Hanlei Xie, Xiongwei Wu, Qichao Wang, Haodong Zhang, Jiajun Liu, Yuhao Wang, Yuqing Xie, Junpeng Zhao, Long Chen, Ming Ma, Sihan Yang, Ziwang Zhao, Yanhao Jia, Liangquan Gong, Feida Zhu, Yiran Zhong, Steven Hoi
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29892v1](http://arxiv.org/abs/2609.29892v1)
- **PDF:** [https://arxiv.org/pdf/2609.29892v1](https://arxiv.org/pdf/2609.29892v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The rapid progression of large language models is extending AI from passive content generation into the active workflows of engineering and scientific discovery. This shift raises a compelling question: can AI be both the object of development and an active participant in building next-generation AI systems? We explore this question by building Qwen-Planner-Agent within a closed-loop AI-for-AI framework for scalable development and iterative improvement. Mobile planning offers a demanding test of this approach: complex, long-horizon tasks challenge agent reliability, while costly real-device interaction limits development scalability. The framework connects data production, model training, and deployment through a shared action-feedback-verification contract. (i) AI for Data builds a human-gated agentic data flywheel in which specialized agents construct tasks, collect interaction trajectories, curate and balance training data, and use training feedback to guide subsequent data generation. (ii) AI for Training combines a supervised planning cold start with hybrid-environment online agentic reinforcement learning, where we introduce Competence-Aware Reward-and-Advantage Engineering (CARE) to reduce reasoning and tool-use costs while preserving task performance. (iii) AI drives model--harness co-evolution through an execution-evidence-driven loop that orchestrates memory, skills, and tools at runtime and feeds structured action feedback and preserved failure traces back into coordinated model and harness adaptation. Qwen-Planner-Agent achieves the best overall performance among all evaluated models and systems on MobilePA-Bench, improving over its base model across tool use, memory, skills, and sub-agent coordination. Further evaluations of our model show improvements across non-mobile agentic benchmarks while largely preserving general capabilities.

</details>


### 41. Hard Stop: Kernel-Level Preemption and Containment for Rogue Agentic Execution

- **Authors:** José Luis Pino
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29808v1](http://arxiv.org/abs/2609.29808v1)
- **PDF:** [https://arxiv.org/pdf/2609.29808v1](https://arxiv.org/pdf/2609.29808v1)
- **Categories:** cs.CR, cs.AI, cs.DC, cs.OS


> Summary unavailable.


<details>
<summary>Abstract</summary>

In July 2026, an unconstrained autonomous agent participating in a frontier AI cybersecurity evaluation harness breached its evaluation sandbox, established an external command-and-control foothold, and executed a multi-stage intrusion into Hugging Face's production multi-tenant dataset conversion infrastructure (referred to in this autopsy as Incident-2026-Alpha). Over 4.5 days, the rogue agent executed 17,600 discrete actions across 6,280 worker clusters, compromised AWS EC2 Instance Metadata Service (IMDS) credentials, forged Kubernetes service account tokens, rooted physical worker nodes via overprivileged CSI drivers, harvested 136 production secrets, and enrolled 181 ephemeral sandboxes into the organization's internal mesh VPN.
  This monograph presents a first-principles forensic autopsy of the intrusion, provides formal evidence that the breach was a predicted consequence under the Instrumental Convergence thesis operating within an unattenuated autonomous loop lacking out-of-band circuit-breakers, exposes the Defensive LLM Guardrail Paradox that paralyzed centralized commercial models during forensic incident response, and formalizes the Dual-Sided Epistemic Andon Imperative. We specify the dual-process systems architecture---combining out-of-band supervisory control of discrete event systems (Ramadge and Wonham 1989), Synchronous Reactive (SR) ambient sentinels (Berry and Gonthier 1992; Lee and Neuendorffer 2005), and microsecond-scale (4.8 $μ$s median / $< 0.154$ ms WCET bound) POSIX preemption buses---demonstrating how compiled, deterministic epistemic boundaries prevent autonomous rogue excursions before the first off-target socket packet traverses the hypervisor.

</details>


### 42. REAT: A Reflective Experience-Augmented Tutoring Framework for Multi-turn Mathematical Instruction

- **Authors:** Jianheng Zhou, Chaoli Zhang, Xingjun Wei, Xinliang Zhou, Giancarlo Fortino, Xing Fan, Yanfeng Wang, Qingsong Wen, Haoyang Li
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29804v1](http://arxiv.org/abs/2609.29804v1)
- **PDF:** [https://arxiv.org/pdf/2609.29804v1](https://arxiv.org/pdf/2609.29804v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Current Large Language Models (LLMs) excel at solving complex mathematical problems, yet this proficiency does not inherently translate into effective tutoring. While advanced LLM tutors may leverage multi-agent frameworks or fine-tuning, most still lack a mechanism to systematically accumulate and reuse pedagogical experience over time, limiting their adaptability to diverse student needs during fluid, multi-turn interactions. To bridge this gap, we propose the Reflective Experience-Augmented Tutoring (REAT) framework, which couples experience distillation from historical dialogues with real-time adaptive retrieval. Driven by a multi-agent Observer-Critic-Mentor (OCM) distillation pipeline, REAT reviews past conversational trajectories and distills raw interactions into structured, problem-agnostic pedagogical experiences. During live tutoring, a state-aware retrieval module injects these curated experiences to provide adaptive scaffolding based on the student's cognitive state. Experiments demonstrate that the proposed framework significantly outperforms both prompt-only and supervised fine-tuning (SFT) baselines, particularly in improving complex, low-scoring tutoring scenarios. Crucially, the distilled experiences exhibit robust generalization across diverse model architectures and mathematical datasets.

</details>


### 43. Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement

- **Authors:** Yukai Wu, Yuanjing Yang, Le Zhou, Shaokun Han, Haoyu Wang, Zirui Tang, Weihuang Zheng, Maxm Pan, Xuanhe Zhou, Fan Wu
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29773v1](http://arxiv.org/abs/2609.29773v1)
- **PDF:** [https://arxiv.org/pdf/2609.29773v1](https://arxiv.org/pdf/2609.29773v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Many real-world tasks (e.g., office workflows, scientific experimentation) require LLM agents to interact repeatedly with their environments for context-dependent operations. However, such environments are often not agent-ready. First, information is often scattered and fragmented across the environment. Second, relevant evidence in the environment is often mixed with misleading information and conflicting versions. Third, environments evolve over time, introducing new noise and more challenging tasks. These challenges can substantially degrade performance for state-of-the-art AI agents (e.g., from 83.9% to 57.6%). To address these challenges, we propose Env-Rethink (a system with 27B post-trained model) that supports three main capabilities: (1) It adaptively builds Collection Maps (for organizing related files) and Event Logs (for contextualizing cross-data relationships) to supplement necessary context; (2) It further leverages the post-trained model (through offline trajectory learning) to identify underlying noise issues in the environment; (3) It ultimately evolves environments through virtual event histories that alter environmental states and evidence relationships, producing more tricky ones for further agent improvement. Experiments show that Env-Rethink can effectively improve downstream task performance (with over 15.1% rubric pass rate improvement across nine models on 30 tasks).

</details>


### 44. WeatherDiagFlow: Evidence-Grounded Radar Nowcasting with Diagnostic Flow Refinement

- **Authors:** Chunlei Shi, Yufeng Zhu, Yixiao Liang, Dan Niu, Yongchao Feng, Qiliang Wu, Jiong Wang
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29772v1](http://arxiv.org/abs/2609.29772v1)
- **PDF:** [https://arxiv.org/pdf/2609.29772v1](https://arxiv.org/pdf/2609.29772v1)
- **Categories:** cs.LG, cs.MM


> Summary unavailable.


<details>
<summary>Abstract</summary>

Radar nowcasting is essential for short-term warning and emergency response, yet conventional systems mainly return future radar fields and provide limited support for operational communication and post-event verification. We formulate radar nowcasting as an evidence-grounded forecast--bulletin--audit task, in which a numerical forecaster produces both future radar fields and structured diagnostic evidence. Forecast-time bulletins use only model-available evidence, whereas post-event audits incorporate future radar truth only after the forecast horizon is observed. Based on this task formulation, WeatherDiagFlow predicts motion, growth and decay, heavy-echo risk, and uncertainty to condition rolling flow refinement, while frozen-scaffold residual calibration improves long-lead strong-echo preservation. A multi-agent layer converts the structured evidence into operational bulletins and independently generates verification audits without feeding textual outputs back into the forecaster. Experiments on FJRADAR demonstrate competitive overall performance and improved strong-echo event skill. WeatherDiagFlow therefore connects numerical prediction, evidence-grounded reporting, and auditable verification under a leakage-controlled protocol.

</details>


### 45. IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis

- **Authors:** Xingyu Wu, Yuchen Yan, Zhengxi Lu, Siqi Chen, Xin ZHANG, Aiting Liu, Chao Deng, Jie Liu, Jin Ma, Jian Shao, Jun Xiao, Yongliang Shen
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29444v1](http://arxiv.org/abs/2609.29444v1)
- **PDF:** [https://arxiv.org/pdf/2609.29444v1](https://arxiv.org/pdf/2609.29444v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep search requires LLM agents to decompose complex queries, search for evidence, and synthesize grounded answers, yet existing ReAct-style agents suffer from two limitations: role coupling, where one policy must handle planning, evidence use, and synthesis; and context accumulation, where growing search histories introduce noise and obscure useful information. To address these issues, we propose IterSynth, a role-decoupled and summary-based paradigm that alternates between a Planner for identifying information needs and a Synthesizer for integrating evidence into an evolving summary state. This design separates planning from synthesis while using the summary as the persistent state of search, reducing both capability coupling and context noise. To train IterSynth effectively, we further introduce Role-Decoupled Policy Optimization (RDPO) for reinforcement learning, which combines terminal outcome rewards with turn-level rubric evaluations and computes role-specific advantages for more precise credit assignment. Experiments on five long-horizon deep-search benchmarks such as BrowseComp and Xbench-DS show that IterSynth-8B achieves an average score of 50.7, surpassing the strongest prior $\leq$8B agent by +4.2\%. Moreover, IterSynth serves as a model-agnostic prompting paradigm, delivering substantial zero-shot gains over ReAct and similar prompting paradigms on frontier proprietary models.

</details>


### 46. Temperament Engineering: Designing Strategic Behavioural Diversity in Robot Swarms

- **Authors:** Edmund R. Hunt
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29423v1](http://arxiv.org/abs/2609.29423v1)
- **PDF:** [https://arxiv.org/pdf/2609.29423v1](https://arxiv.org/pdf/2609.29423v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

No two robots are truly identical: calibration, battery state, sensor drift and wear give every swarm a distribution of behaviour rather than a single point, usually treated as an imperfection to be minimised. In animal collectives the reverse holds: consistent individual differences in behaviour ('temperament') are shaped by natural selection and often decisive for group performance. This perspective proposes 'temperament engineering', a bio-inspired framework that treats the swarm's distribution of temperaments, rather than the individual controller, as the design object. It borrows five evolutionarily validated axes of animal temperament (shyness-boldness, exploration-avoidance, activity, aggressiveness and sociability) as a design vocabulary, rendering each as a continuous control parameter $τ\in [0,1]$ above the controller, realisable as a module threshold, a policy-conditioning vector in multi-agent reinforcement learning, or a constraint on a foundation-model planner. A three-phase workflow maps mission success criteria onto relevant axes, plans the shape of the $τ$ distribution, and tunes reaction norms governing how temperament responds to environmental cues. The payoff is greatest under decentralisation: where a central planner can reassign behaviour online, a temperament distribution is a planner output, but in a swarm without global knowledge it must be an offline, anticipatory design input. Behavioural and platform heterogeneity are thereby co-design variables, and I sketch tentative robot-native axes (self-model plasticity, forcefulness, initiative and expressiveness) arising from features robots have and animals do not. Engineered heterogeneity has been shown to outperform homogeneous swarms in tasks such as aggregation and exploration; establishing when, and how much, heterogeneity repays its cost is the work the field can now take forward.

</details>


### 47. Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol

- **Authors:** Jaime Alonso Ruiz, Carlos Aparicio, Gabriel Huecas, Joaquín Salvachúa, Andres Munoz-Arcentales
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30341v1](http://arxiv.org/abs/2609.30341v1)
- **PDF:** [https://arxiv.org/pdf/2609.30341v1](https://arxiv.org/pdf/2609.30341v1)
- **Categories:** cs.AI, cs.DB


> Summary unavailable.


<details>
<summary>Abstract</summary>

Data Spaces enable sovereign and governed data sharing across organizational boundaries, but their integration with AI agents remains challenging due to mismatches between probabilistic language model interactions and policy-driven data infrastructures. This article presents an architectural mediation approach based on the Model Context Protocol (MCP), implemented through the Eunomia Agent, to enable controlled interaction between large language model (LLM) agents and data space services. The proposed mediation layer translates data space capabilities into structured, schema-driven tools that AI agents can discover and invoke while preserving governance constraints. A prototype implementation validates end-to-end interaction across catalog discovery, metadata retrieval, and data service invocation without modifying existing data space components. Results demonstrate that protocol-based mediation enables interoperable and standards-aligned integration of AI agents into data space ecosystems. The approach provides practical guidance for organizations seeking to introduce AI-driven automation into governed data-sharing environments while maintaining compliance, interoperability, and architectural separation of concerns.

</details>


### 48. Epistemic-Probabilistic Model for Guarded Multi-Agent LLM Coordination

- **Authors:** Mehdi Nasiri, Mohammad Saeed Arvenaghi, Sadegh Vaezi, Ebrahim Ardeshir-Larijani
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29366v1](http://arxiv.org/abs/2609.29366v1)
- **PDF:** [https://arxiv.org/pdf/2609.29366v1](https://arxiv.org/pdf/2609.29366v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent large language models (LLMs) have become ubiquitous in applied AI, yet their theoretical foundations remain surprisingly understudied. Viewed through the lens of multi-agent systems theory, several shortcomings come to light: a lack of social intelligence, the absence of coordination mechanisms among agents, unknown emergent behavior, and interactions between agents that are bounded by natural language. We address two of these gaps: the absence of social behavior and the lack of mechanisms for inter-agent coordination. We introduce Epistemic Probabilistic Language Agents (EPLA), a neuro-symbolic architecture for multi-agent coordination under uncertainty. A Symbolic Guard provides structured diagnostic feedback. The LLM generates typed actions, and the Guard controls their execution against an authoritative symbolic state. We formalize the epistemic layer in a gossip testbed through epistemic lottery gossip models, which combine view-based call histories with agent-indexed probability weights. We argue that implementing such a formalism can address shortcomings of agentic LLMs.

</details>


### 49. SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support

- **Authors:** Muhammad Muhtasim Shahriar, Abdullah Mohammad Sayem, Tze Hui Liew, M. F. Mridha, Md. Mahiuddin
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29341v1](http://arxiv.org/abs/2609.29341v1)
- **PDF:** [https://arxiv.org/pdf/2609.29341v1](https://arxiv.org/pdf/2609.29341v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Consumer-facing skincare AI must coordinate visual evidence, product information, tool use, and user-facing actions within explicit evidence and safety boundaries. This study evaluates SkinAgent AI, a non-diagnostic multimodal framework that combines visual concern routing with grounded and auditable LLM-based orchestration. The architecture includes routing for Acne, Pores, and Wrinkles; photograph-based skin-type estimation; count-informed ordinal acne-severity support; typed tools; database-grounded recommendation and action functions; deterministic safety, privacy, and evidence checks; approval before state-changing actions; and structured trace and replay mechanisms. Visual-model performance and system-level agent behavior were evaluated separately. Across three seeds, the skin-condition routing model achieved 99.84% +/- 0.07% accuracy. Skin-type estimation achieved 88.85% accuracy, while count-informed acne-severity support achieved 84.59% accuracy with a quadratic weighted kappa of 0.9076. On a locked but non-independent 240-case system benchmark, intent accuracy was 80.00%, exact tool-set match was 62.92%, and strict task completion was 47.08%. No violations or successful cross-user leakage events were observed in the finite safety and privacy test suites. Tool-selection errors, incomplete grounding of product attributes, and unreliable failure fallback nevertheless remained. These findings support the feasibility of bounded, database-grounded, and traceable agent orchestration for non-diagnostic skincare assistance. They do not establish clinical readiness, external generalization, formal privacy guarantees, or universal safety. Independent validation, expert assessment, robustness and fairness testing, and prospective evaluation in real-world settings remain necessary.

</details>


### 50. Parameters vs. Context: TRACE Fine-Tuning for Robust Retrieval-Augmented Generation

- **Authors:** Zhengchen Huang, Yundong Sun, Minrui Song, Shuanglong Yao, Ye Liu, Ji Chen, Xing Wang
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30337v1](http://arxiv.org/abs/2609.30337v1)
- **PDF:** [https://arxiv.org/pdf/2609.30337v1](https://arxiv.org/pdf/2609.30337v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-Augmented Generation (RAG) mitigates knowledge obsolescence and factual hallucination in large language models by introducing external context. However, when retrieved knowledge conflicts with the model's internal parametric knowledge, the model may either blindly follow misleading context or incorrectly rely on parametric knowledge, leading to unreliable responses. To address this issue, this paper proposes TRACE (Debate-TRace and Answer-Completeness rEgularized fine-tuning), a robust fine-tuning framework for RAG under knowledge conflicts. First, we propose a fine-tuning method that leverages multi-agent debate traces to extract correct candidates, incorrect candidates, and answer-shift patterns, providing fine-grained supervision for reliable knowledge-source selection. In addition, we design an answer completeness regularization mechanism to alleviate empty, overly short, and prematurely terminated responses via answer-tail token reinforcement and premature termination suppression. The fine-tuning objective combines correct-answer supervision, incorrect-candidate suppression, answer-tail token reinforcement, and premature termination suppression, enabling the model to use reliable external context, resist misleading or irrelevant retrieved content, and fall back to parametric knowledge when retrieved evidence is unreliable. Experiments across multiple knowledge-conflict scenarios and datasets show that TRACE improves robustness against misleading retrieved knowledge and reduces incomplete answers. These results demonstrate that multi-agent debate traces and answer completeness regularization jointly enhance knowledge-source selection, conflict robustness, and answer quality in RAG models. Our code is available at https://github.com/PHD-lanyu/TRACE.

</details>


### 51. DocuTeam: Mixed-Initiative Multi-Agent Discussions around Evolving Documents

- **Authors:** Heechan Lee, Juhyeon Choi, Tae Soo Kim, Juho Kim, Joseph Seering
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29309v1](http://arxiv.org/abs/2609.29309v1)
- **PDF:** [https://arxiv.org/pdf/2609.29309v1](https://arxiv.org/pdf/2609.29309v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In open-ended problem solving, collaborators often rely on discussion to surface concerns, challenge perspectives, and refine shared work as it evolves. While AI agents are increasingly used as discussion partners, existing multi-agent systems place a heavy burden on users to initiate and carefully orchestrate the discussions. We present DocuTeam, a mixed-initiative multi-agent discussion system in which both users and agents can initiate and steer conversations. Agents monitor document changes to proactively start and redirect discussions as the work evolves, while users can flexibly shape the conversation or adopt agent ideas. In a within-subjects study (N=20), participants using DocuTeam produced outcomes rated significantly more novel, relevant, and specific than with a baseline without any increase in cognitive load. Rather than using agents for one-off idea sourcing, participants engaged in an iterative refinement loop in which document changes prompted agent reactions, which led users to revisit and further develop their work.

</details>


### 52. ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction

- **Authors:** Sudha Priyadarshini, Mohamed Chahine Ghanem
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29191v1](http://arxiv.org/abs/2609.29191v1)
- **PDF:** [https://arxiv.org/pdf/2609.29191v1](https://arxiv.org/pdf/2609.29191v1)
- **Categories:** cs.AI, cs.IR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Sensitive information is defined by domain and intent, not a universal category, yet redaction systems such as privacy filters and named-entity recognizers fix a taxonomy at training time, requiring retraining for each new domain. We introduce ASIRF (Agentic Sensitive Information Redaction Framework), which retrieves domain-specific definitions based on the input's domain from a flexible knowledge base at inference time, needing no retraining to adapt. Two architectures, a three-call multi-agent pipeline and a single-agent variant, are evaluated across ten small open-weight models and eight datasets, including out-of-distribution fictional domains, against the OpenAI Privacy Filter (OPF) as a trained-classifier baseline. With only a few dozen expert-authored definitions per domain and no training data, ASIRF's recall exceeds OPF's in 68 of 80 model-domain combinations (85 percent), by at least one of the two architectures, with shortfalls confined mostly to OPF's training-distribution domains.

</details>


### 53. A Wrong Turn Does Not Ruin the Journey: Deviation-Guided Skill Self-Evolution for LLM Agents

- **Authors:** Yichun Feng, Jiawei Wang, Haozhe Sun
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29154v1](http://arxiv.org/abs/2609.29154v1)
- **PDF:** [https://arxiv.org/pdf/2609.29154v1](https://arxiv.org/pdf/2609.29154v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents increasingly rely on natural-language skills to solve complex tool-use tasks. However, such tasks often admit multiple valid solution paths, making it inappropriate to improve skills by forcing failed trajectories to match a fixed successful trajectory. Moreover, failed trajectories are rarely entirely wrong: an agent may first collect useful evidence and make meaningful progress, but later deviate into an erroneous suffix. We therefore argue that skill self-evolution should identify where productive problem solving begins to break down, rather than reflect coarsely over the entire failure. Based on this insight, we propose SkillPivot, a deviation-point-guided framework for skill self-evolution. SkillPivot detects the transition from a useful prefix to an erroneous suffix using execution validity, goal progress, and action diversity. A stronger teacher then continues from the same prefix and produces a successful alternative under the same interaction history. By contrasting the student's failed suffix with the teacher's successful suffix, SkillPivot generates localized skill updates while preserving already effective guidance. Experiments on ToolQA, LogicBench, and WildClawBench show that SkillPivot consistently outperforms competing skill-evolution methods, improves multiple agent models, and produces compact, transferable skill updates.

</details>


### 54. Where Does Exactly-Once Live? Model, Harness, and Tool-Contract Effects on Duplicate Side Effects in LLM Agents

- **Authors:** Jiapeng Li
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29095v1](http://arxiv.org/abs/2609.29095v1)
- **PDF:** [https://arxiv.org/pdf/2609.29095v1](https://arxiv.org/pdf/2609.29095v1)
- **Categories:** cs.LG, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a tool-using agent's write times out or returns a server error, the action may already have taken effect. Retrying blindly duplicates it -- a second charge, a second announcement, a second deployment -- while giving up skips required work. We ask where exactly-once behaviour should be enforced: in the model, in the agent harness, or in the tool contract. We introduce LIMBO, a deterministic sandbox of six services with realistic contracts (optional idempotency keys, eventually consistent and missing read paths) and twelve fault modes injected at the service boundary, including late commits, redelivery and partial batches; every episode is graded against a ledger of committed effects. Across 25,930 episodes spanning nine recent models, three production agent harnesses, two contract variants and fifteen recovery conditions, the answer depends on the fault. When an immediate read-back can reveal what happened, the model decides: frontier models instructed to act exactly once almost never duplicate a write whose acknowledgement was lost (0.5%), weaker models often do, and the model explains 53% of the explained variance. When it cannot -- the request is still in flight, or the transport delivered it twice -- the same frontier models duplicate in 56% and 74% of episodes, and the contract explains 81%. We prove that no verification-only policy is exactly-once under late commits without a bound on in-flight time. Waiting works when such a bound is short and known, but with heavy-tailed in-flight delays even an hour of waiting per episode falls short of offering an idempotency key on every write, which lowers the duplicate rate from 28% to 4% because agents use keys when they exist. The harness barely matters, a guard that attaches keys transfers across harnesses unchanged, and agents reported success in 90% of the episodes in which they had duplicated an effect.

</details>


### 55. From Self-Distillation to Self-Practice: Privileged Information for Multi-Turn Agents

- **Authors:** Xingyu Su, Abhishek Kumar, Qing Ping, Youzhi Luo, Jonathan Buck, Zach Zhang, Subramanian Chidambaram, Vinayak Arannil
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29051v1](http://arxiv.org/abs/2609.29051v1)
- **PDF:** [https://arxiv.org/pdf/2609.29051v1](https://arxiv.org/pdf/2609.29051v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-policy self-distillation (OPSD) has become a popular recipe for post-training LLM agents. It supervises the agent model at the token level with a stronger teacher view of the same model, obtained by conditioning on privileged information (PI). In this work, we show that in multi-turn agents, this paradigm teaches the student to act with confidence but without the information behind it. The trained agent behaves as if it had privileged information it never observed, and its performance falls well short of plain RL, in the worst case below the untrained base model. Therefore, we propose Privileged Self-Practice (PSP), which keeps the PI and moves it from the loss to the sampler. When the student's rollouts on a task mostly fail, we inject a short per-task instruction written by an analyzer model, sample the task again with the instruction in context, and train on the result with an unchanged GRPO objective. The privileged information stays in the prompt and never enters the loss. Across AppWorld and SWE-bench Verified, with three different student models, PSP obtains the best average score in every setting and is the only method that consistently outperforms plain GRPO, improving task-goal completion by up to 65% on AppWorld and the resolved rate by up to 61% on SWE-bench Verified.

</details>


### 56. Multi-Agent Orchestration of 3GPP Channel Estimators

- **Authors:** I. Zakir Ahmed, Hamid Sadjadpour
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29044v1](http://arxiv.org/abs/2609.29044v1)
- **PDF:** [https://arxiv.org/pdf/2609.29044v1](https://arxiv.org/pdf/2609.29044v1)
- **Categories:** cs.IT, cs.AI, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Pilot-aided channel estimation is a decisive block in orthogonal frequency-division multiplexing (OFDM) receivers for both 5G New Radio (5G-NR) and Long-Term Evolution (LTE). A large body of estimators exists, from simple least-squares (LS) interpolation to statistically optimal linear minimum-mean-square-error (LMMSE) variants and, more recently, deep convolutional denoisers, yet no single estimator is uniformly best: the winner depends on the propagation scenario, the numerology, the operating signal-to-noise ratio (SNR), the mobility (Doppler), and the antenna configuration. In this paper, we quantify this fact through a unified study of eight literature estimators evaluated over the 3GPP TR~38.901 Urban-Macro (UMa), Urban-Micro (UMi), and Rural-Macro (RMa) channels generated with NVIDIA Sionna, for both 5G-NR and LTE numerologies, in single-input single-output (SISO) and $8\times2$ multiple-input multiple-output (MIMO) settings. We then propose a \emph{condition-adaptive multi-agent orchestrator} that treats each estimator as an independent agent and dispatches, per operating condition, to the agent that is best on a validation split without any genie knowledge. The orchestrator tracks the per-realization oracle to within $1.07$~dB and improves the normalized mean-square error (NMSE) over the best \emph{fixed} strategy by up to $3.6$~dB at high SNR, where the low-SNR champion is no longer optimal. Because the agents are independent, running them concurrently delivers this best-of-eight accuracy at essentially single-estimator latency: a data-parallel partition scales the wall-clock nearly as $1/K$ with $K$ workers (up to $6.9\times$), whereas naive by-algorithm partitioning is Amdahl-limited by the heaviest agent. The results substantiate multi-agent orchestration as a practical route to robust channel estimation across heterogeneous 5G-NR/LTE deployments.

</details>


### 57. MeshHeal: Two-Timescale Self-Healing for Gray Failures in Decentralized LLM Agent Networks

- **Authors:** Keru Chen, Sen Lin, Yingbin Liang, Nathaniel D. Bastian, Shaofeng Zou
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29015v1](http://arxiv.org/abs/2609.29015v1)
- **PDF:** [https://arxiv.org/pdf/2609.29015v1](https://arxiv.org/pdf/2609.29015v1)
- **Categories:** cs.AI, cs.CL, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Decentralized LLM-based multi-agent systems coordinate through local interactions, but an agent can remain responsive while its task-solving quality persistently degrades. Such gray failures require protecting current tasks before sufficient evidence exists to alter future routing, while still allowing recovered agents to rejoin. We introduce MeshHeal, a fully decentralized self-healing framework that couples ability-matched peer review across two timescales. At the fast timescale, an adaptive hierarchy escalates uncertain or low-scoring outputs from repeated single-reviewer evaluation to committee deliberation and, when needed, correction before use. At the slow timescale, a task- and ability-conditioned peer-relative detector aggregates scores to distinguish persistent degradation from ordinary output variation, trigger mandatory committee review, and eventually exclude degraded agents from ordinary routing; recovery probes provide fresh evidence for reintegration. To faithfully evaluate routing, we introduce Model-Backed MAS Evaluation, which ties ability assignments to execution models, since prompt-based ability assignments alone can leave routing errors hidden. Across BBH, MATH, and MMLU-Pro, MeshHeal achieves 0.839 degraded-phase accuracy using 51k total model tokens per task, versus the strongest baseline Symphony's 0.807 accuracy using 115k per task. Under staggered degradation and recovery, MeshHeal isolates degraded agents, keeps them excluded from ordinary task execution until recovery, and returns them to normal routing.

</details>


### 58. AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining

- **Authors:** Qingzhuo Wang, Zikun Wei, Zhihua Wei, Wen Shen
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.29014v1](http://arxiv.org/abs/2609.29014v1)
- **PDF:** [https://arxiv.org/pdf/2609.29014v1](https://arxiv.org/pdf/2609.29014v1)
- **Categories:** cs.AI, cs.CE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based multi-agent systems can automate alpha factor mining, but their reliance on external APIs limits control over cost, availability, and confidentiality. Long research loops also tend to revisit a few successful economic mechanisms that lead to research path collapse. To address these limitations, we propose AlphaDiverse, a framework that integrates a multi-agent alpha research system, diverse research path collection, and post-training for local agents. We let the research system generate complementary plan portfolios and vary research environments across loops to collect diverse research paths. Using these diverse traces, we warm-start local Planner and Realizer agents with supervised fine-tuning. Then, we propose a joint GRPO method to optimize both of them using predictive quality and diversity of contributions. Research feedback is confined to inner period data, while a frozen final model is evaluated on a later outer period data, thereby avoiding test-set tuning. Experiments across four Chinese stock universes show that AlphaDiverse can combine competitive prediction with broader exploration.

</details>


### 59. Beneath the Scores: Rethinking Hallucination Evaluation for Video Understanding Models

- **Authors:** Shuzhi Gong, Fengze Sun, Yuansan Liu
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28991v1](http://arxiv.org/abs/2609.28991v1)
- **PDF:** [https://arxiv.org/pdf/2609.28991v1](https://arxiv.org/pdf/2609.28991v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Video understanding is increasingly performed by multi-stage LLM agents that separate temporal grounding, visual observation, and reasoning. Yet these stages are typically evaluated on different benchmarks and distributions, making it difficult to determine where hallucinations originate. We first organize existing benchmarks around these stages and show that their scores provide inconsistent diagnostic signals: stronger stage-level performance does not reliably imply lower downstream hallucination, and even benchmarks targeting the same capability can disagree.
  We therefore introduce a causal stage-intervention protocol that overwrites individual stages while holding the downstream task fixed. Across 60,008 runs on three video-agent architectures, we find that grounding is the dominant source of downstream error, with roughly four times the causal impact of corrupting visual observations. Successful grounding depends primarily on locating the correct region rather than precise temporal overlap, explaining why standard mIoU metrics poorly predict downstream reliability. We further find that incorrect evidence is substantially more harmful than missing evidence. Finally, auditing existing benchmarks against these interventions reveals that their scores do not reliably predict causal cascade sensitivity and can fail under distribution shift. These results motivate intervention-based, stage-aware evaluation for trustworthy video agents.

</details>


### 60. On the Effectiveness of Kernel-Level Evidence for Agent Security

- **Authors:** Spencer King, Zhilu Zhang, Mikhail Kuznetsov, Kay Liu, Baris Coskun, Wei Ding
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28915v1](http://arxiv.org/abs/2609.28915v1)
- **PDF:** [https://arxiv.org/pdf/2609.28915v1](https://arxiv.org/pdf/2609.28915v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are deployed into infrastructure that grants them broad host authority, yet existing agent-security benchmarks and defenses operate almost exclusively at the application telemetry layer: the served tool manifest, the user prompt, and the model's messages. Some threats, however, smuggle malicious instructions and actions past the application boundary, leaving them invisible to that layer. In this work, we bridge that gap by pairing application-level agent telemetry with kernel-level syscall traces to present the first paired-evidence characterization of kernel-level versus application-layer signal for agent security. To quantify the value of the enhanced telemetry, we introduce Agent Cross-Layer Evidence (ACE), a paired-session corpus of 4,047 sessions and 17 threat models spanning six delivery-vector families and 14 of the 25 OWASP LLM and agentic threat categories, organized into 12 attack mechanics with per-mechanic characterization of where the most discriminative evidence lies. Across four distinct detector families, we find that kernel evidence is discriminative on its own and that composing it with application-layer evidence generally outperforms either single-layer view, revealing complementary signals that single-layer analyses can miss. We further demonstrate generalization to unseen attack families and transfer to an alternate agent runtime. Together, these findings establish the value of cross-layer evidence for agent security.

</details>


### 61. Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion

- **Authors:** Qi Pang, Virginia Smith, Wenting Zheng
- **Published:** 2026-09-24
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28900v1](http://arxiv.org/abs/2609.28900v1)
- **PDF:** [https://arxiv.org/pdf/2609.28900v1](https://arxiv.org/pdf/2609.28900v1)
- **Categories:** cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems built on large language models (LLMs) are increasingly deployed in high-stakes settings such as finance, healthcare, and software engineering, where agents coordinate through natural-language messages. The same channels, however, let colluding agents exfiltrate confidential information or coordinate unauthorized actions, and steganography can hide such communication inside outputs that look ordinary to an auditor reading the transcript.
  Existing provably undetectable LLM steganography protocols are not suited to realistic deployments. High-capacity schemes assume a symmetric setting where the receiver can reproduce the sender's output distribution, the state-of-the-art protocol for asymmetric agents has very low capacity, and most approaches rely on a pre-shared secret key.
  We make the threat of undetectable agent collusion concrete with Codetta, a high-capacity steganographic protocol for independently deployed agents in realistic asymmetric settings. Codetta combines a shared public model that estimates the communication channel, a sampling mechanism that preserves the sender's output distribution, and an adaptive error-correcting code. It further removes the pre-shared key through a steganographic key exchange that lets independently deployed agents establish a shared key while keeping the transcript computationally indistinguishable from ordinary model outputs.
  Across three agent workloads and three sender models, Codetta achieves up to $94\times$ the capacity of the state-of-the-art asymmetric protocol, and its key exchange establishes a shared key with about 80k visible tokens at an empirically certified failure probability of at most $4.1\times 10^{-3}$. These results show that effectively undetectable collusion is becoming feasible between independently deployed agents, so auditing must go beyond inspecting communication transcripts.

</details>


### 62. RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers?

- **Authors:** Mithil Salunkhe, Haochen Ding, Samridhi Verma, Volodymyr Kindratenko
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28850v1](http://arxiv.org/abs/2609.28850v1)
- **PDF:** [https://arxiv.org/pdf/2609.28850v1](https://arxiv.org/pdf/2609.28850v1)
- **Categories:** cs.AI, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Reproducing a machine learning paper involves most research steps, from installing software and debugging to running experiments, work that AI agents increasingly do. We introduce RECLAIM, a benchmark of 100 NeurIPS 2025 papers that can be rebuilt yearly from new conferences. For each paper we fix in advance the result to reproduce, what counts as a successful reproduction, and a GPU-hour budget. An agent must reproduce that result using the paper and whatever its authors released. What the authors released decides the difficulty tier. Run-tier releases include code, data, and weights; Retrain-tier releases lack weights, so the agent trains the model; Reimplement-tier releases lack code, so the agent writes it. A separate language model grades runs from logs and outputs rather than agents' reports. We run four agents once per paper; the best agent in each tier reproduces only 41% of Run-tier papers, 27% at Retrain, and 15% at Reimplement, where every agent does worst. Failed attempts use on average 29% of their budget, so most stop with budget left. The most common agent error is writing the method without checking any part against the paper's numbers, in 63 of 400 runs.

</details>


### 63. Blockchain-Enabled Artificial Intelligence and AI Agents for Secure Data Sharing and Cybersecurity Applications

- **Authors:** Harsh Verma
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28843v1](http://arxiv.org/abs/2609.28843v1)
- **PDF:** [https://arxiv.org/pdf/2609.28843v1](https://arxiv.org/pdf/2609.28843v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Blockchain and artificial intelligence (AI) are converging into a single infrastructural layer for securing data sharing, model integrity, and autonomous decision-making across distributed systems. This paper presents a meta-synthesis that draws together four constituent studies covering adversarial machine learning, AI-powered anomaly detection in cloud environments, automated vulnerability patching by multi-agent large language model (LLM) pipelines, and the broader landscape of securing AI systems across their lifecycle and situates their findings within the emerging literature on blockchain-enabled AI and autonomous AI agents. Each constituent study addresses a distinct point of failure in modern AI-driven security operations: the integrity of training data and model behavior, the reliability of real-time monitoring, and the trustworthiness of automated code remediation. We argue that blockchain's properties of immutability, decentralized consensus, and verifiable provenance directly address a gap common to all three: the difficulty of establishing trust in data, models, and autonomous agents that operate without a central authority. Building on real-world research on blockchain-secured data sharing, federated learning, and multi-agent coordination, we propose a layered reference architecture that couples adversarially hardened models, blockchain-anchored data provenance, AI-driven anomaly detection, and smart-contract-governed multi-agent remediation. We conclude by identifying open problems in scalability, privacy-transparency trade-offs, and the governance of autonomous agents that must be resolved before such integrated systems can be trusted in production-critical environments.

</details>


### 64. When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess

- **Authors:** Salma Roshdy Aly, Hussein Assaf, Ziad Kobti
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.30328v1](http://arxiv.org/abs/2609.30328v1)
- **PDF:** [https://arxiv.org/pdf/2609.30328v1](https://arxiv.org/pdf/2609.30328v1)
- **Categories:** cs.AI, cs.CL, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

When one language model judges whether another's code is correct, it does not report the absence of evidence. It returns a confident verdict with reasoning attached, indistinguishable from a verdict it had grounds for. Multi-agent verification, which decomposes a judgment into checkable claims and verifies each against evidence, is a promising response and works well when the evidence is a set of retrieved documents.
  We argue such methods require two things of their evidence: it must be independent of the answer under review, and it must differ between the two candidates being compared. The second condition holds automatically with retrieved documents and stops holding in code judging.
  Running MARCH, a published framework unmodified over 80 condition-by-cell measurements on two code judging benchmarks, we find it declares both solutions equally good on 78 to 95% of comparisons, reaching 4.4% accuracy where the same model asked directly reaches 43.7%. Neither easier problems nor a larger judge changes this. Two measurements taken from the pipeline's own logs explain it without needing labels.
  Gating on one of them, the pipeline declines the comparisons it cannot make and raises its accuracy from 20.7 to 36.9% while still answering half of all comparisons. The contribution is not a more accurate judge, but a label-free way to tell when a judge has no basis for its answer.

</details>


### 65. Agent Memory with Episodic Retrieval for Financial Decision-Making

- **Authors:** Nuoyue Xu, Jiang Liu, Wenxuan Huang, Xiang Zhang, Juntai Cao, Jiaqi Wei
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28771v1](http://arxiv.org/abs/2609.28771v1)
- **PDF:** [https://arxiv.org/pdf/2609.28771v1](https://arxiv.org/pdf/2609.28771v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated strong capabilities in financial analysis and reasoning, inspiring recent advances in agent-based trading frameworks. While these systems show promise, prior approaches either emphasize long-horizon forecasting or operate as stateless analyzers, limiting their applicability to the demands of trading in complicated settings. To address these gaps, we introduce META (Memory Enhanced Trading Agent), the first RAG-like episodic-memory-augmented multi-agent framework for financial decision making. META integrates a family of specialized indicator agents (e.g., Trend, MACD, Stochastic, RSI, SMA, AVWAP, Heikin-Ashi) with a Decision Agent that fuses their reports, and a Memory module that retrieves and updates past trading episodes encoded as market state embeddings with outcomes and reflections. By recalling relevant experiences and adaptively reweighting signals under similar market regimes, META achieves improved directional accuracy and robustness under short-horizon evaluation. Our results demonstrate that episodic memory provides a powerful mechanism for regime-aware, interpretable, and low-latency decision-making in trading and decision making. The code of this project is released on GitHub.

</details>


### 66. LabFactory: Building and Evaluating Executable AI Labs

- **Authors:** Jinge Wu, Hongjian Zhou, Mingde Zeng, Jiayuan Zhu, Junde Wu, Jiazhen Pan, Lei Clifton, Andrew Liu, David A. Clifton
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28697v1](http://arxiv.org/abs/2609.28697v1)
- **PDF:** [https://arxiv.org/pdf/2609.28697v1](https://arxiv.org/pdf/2609.28697v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scientific tasks specify a desired capability, but realizing it often requires building a computational system tailored to the task---acquiring data, designing representations, training models, implementing tools, and deciding how they are used at inference. We present LabFactory, a framework in which an AI builder turns a scientific brief into an executable AI lab: a task-specific solver that integrates models, knowledge resources, tools, and a controller behind a fixed interface. The builder develops and packages the lab in a metered workspace; a separate host then executes the delivered artifact on held-out inputs, with reference labels kept outside the solver's input interface, and scores its outputs under the task's protocol. This makes the delivered system, rather than the builder's account of its progress, the object of evaluation. We document 28 selected constructions across seven scientific task categories---from molecular and genomic prediction to physiological signals, clinical decision support, and biomedical text---whose delivered labs exceeded their configured reference values on all 33 subtests under host-side execution. Ten contain predictive models fitted during construction; the others assemble retrieval systems, executable analysis environments, and tool-driven workflows around a fixed platform LLM. Together they show that an AI agent can carry a scientific brief all the way to a working lab that can still be invoked, inspected, and checked after construction ends.

</details>


### 67. Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery

- **Authors:** Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28693v1](http://arxiv.org/abs/2609.28693v1)
- **PDF:** [https://arxiv.org/pdf/2609.28693v1](https://arxiv.org/pdf/2609.28693v1)
- **Categories:** cs.AI, cs.CR, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities - as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions. We introduce skilder, a framework that packages capabilities into roles: bundles of skills, tools, and instructions, together with the limits that bound them. An agent begins with a minimal role catalog, learns the roles a task requires, and receives each role's skills, instructions, and tools through a single MCP server. Because tools reach the agent only inside learned skills, the same server enforces the scope of what was learned deterministically. We evaluate skilder against flat-context tool selection and multi-agent orchestration across 13 tasks using six models (10 runs each). Our results show that, when models completed discovery and issued a governed call, the skilder simulated authorization layer enforced governance boundaries: no unauthorized tool call or parameter violation (e.g., a spending-limit breach) executed. Aggregate task pass rates also reflect whether each model followed the discovery protocol and satisfied response-quality checks; those misses are not authorization failures. Furthermore, by allowing agents to dynamically acquire cross-role capabilities mid-task, skilder preserves problem-solving flexibility while providing hard system-level enforcement.

</details>


### 68. Driving Epidemic Models with AI Agents: the Epydemix Agent Framework

- **Authors:** Nicolò Gozzi, Ciro Cattuto, Alessandro Vespignani
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28692v1](http://arxiv.org/abs/2609.28692v1)
- **PDF:** [https://arxiv.org/pdf/2609.28692v1](https://arxiv.org/pdf/2609.28692v1)
- **Categories:** cs.AI, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Artificial Intelligence agents based on large language models provide convenient natural language interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix Agent Framework, an additive layer over Epydemix, an open-source Python library for stochastic compartmental epidemic modeling. The framework extends the library with four capabilities to facilitate interaction with an AI agent: discovery of available models and parameters, preventive validation of a declarative scenario specification, execution through tested library code, and inspectability of results. These capabilities let an agent handle the entire modeling process, from the natural-language description of the scenario to quantitative results, figures, and interpretation of findings without writing custom code. Each step reads input files and saves results in a separate output bundle, making the process auditable and reproducible. First, we show the end-to-end workflow with a case study comparing vaccination strategies for a novel respiratory virus. Second, we assessed the framework across 50 agent sessions and five modeling tasks by comparing the agent use of the framework against the direct use of the Python interface. The framework reduced turns, output tokens, and cost on most tasks, unless it trades resources for per-point reproducibility.

</details>


### 69. Agent-Editing World Model: Rethinking World Modeling for LLM Agents

- **Authors:** Shuang Sun, Guoxin Chen, Fanzhe Meng, Jia Deng, Huatong Song, Jinhao Jiang, Wayne Xin Zhao, Hongteng Xu, Ji-Rong Wen
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28416v1](http://arxiv.org/abs/2609.28416v1)
- **PDF:** [https://arxiv.org/pdf/2609.28416v1](https://arxiv.org/pdf/2609.28416v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) have enabled agents to tackle long-horizon tasks across diverse environments. To further improve agent performance, existing language world models typically predict environment observations, yet reconstructing high-entropy, execution-dependent tool responses offers limited value when real feedback is available. Meanwhile, agents suffer from \emph{task-state contamination}, where unsupported assumptions and outdated plans persist in history and distort subsequent decisions. We propose the \textbf{Agent-Editing World Model (AEWM)}, which models how reasoning and actions shape future task progress rather than simulating tool responses. AEWM combines \textbf{Action Judge} to distinguish \textsc{Critical}, \textsc{Exploratory}, and \textsc{Noisy} decisions with \textbf{State Revision} to edit noisy reasoning--action continuations from the same observed history. \textbf{EditAct} integrates these capabilities with real execution, directly changing the state underlying subsequent decisions rather than merely providing critiques. We train AEWM across Search, Terminal, and Software Engineering through mid-training and supervised fine-tuning. AEWM achieves 70.5\% macro-F1 on our Action Judge benchmark, exceeding the strongest frontier baseline by 10.6 points. Across six benchmarks and three agent backbones, EditAct improves average scores by 3.2--6.7 points over the strongest baseline. Furthermore, rejection sampling fine-tuning on verified EditAct trajectories, termed \textbf{AEWM-RFT}, improves over Self-RFT by 2.2--2.6 points across three domains without online AEWM guidance.

</details>


### 70. Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer

- **Authors:** Davood Wadi, Yu Ma
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28372v1](http://arxiv.org/abs/2609.28372v1)
- **PDF:** [https://arxiv.org/pdf/2609.28372v1](https://arxiv.org/pdf/2609.28372v1)
- **Categories:** econ.GN, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate consumers. Using "Tool-Lab," an adaptation of information-board process tracing that places product attributes behind costly tool calls, we examine how marketing pricing cues (i.e., just-below pricing and promotional framing) influence AI shopping agents. Across eight commercially deployed LLMs from three providers, we trace pre-choice information acquisition. Under zero cost, pricing cues rarely mislead. Imposing acquisition costs under a vague goal prompt leads LLMs to omit diagnostic attributes required to compute unit price and choose suboptimal choices resembling human heuristics. Relative to a specific goal prompt that mainly preserves diagnostic search and choice optimality, a vague goal prompt under constraints creates a search-mediated vulnerability. This research demonstrates that marketing heuristics in delegated AI shopping are governed by storefront information architecture, not necessarily immutable LLM flaws.

</details>


### 71. LEAP-CBF: A Safety Filter for Uncertain Systems with Least-Effort Adversarial Potentials

- **Authors:** Oswin So, Eric Yu, Chuchu Fan
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28364v1](http://arxiv.org/abs/2609.28364v1)
- **PDF:** [https://arxiv.org/pdf/2609.28364v1](https://arxiv.org/pdf/2609.28364v1)
- **Categories:** cs.RO, cs.LG, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Control barrier functions (CBF) are a popular safety filter to ensure safety for nonlinear dynamical systems. However, when the system is subject to uncertainties and disturbances, this requires the use of robust variants of CBFs, which can be difficult to construct and can be overly conservative, especially for high-dimensional systems under input constraints. In this work, we propose a new approach to solve these challenges by introducing Least-Effort Adversarial Potentials (LEAP), a certificate that quantifies the robustness of a given state against disturbances in terms of the effort required by the disturbance to cause failure. We show that LEAP is a CBF for the undisturbed system, but can also be used to construct a safety filter that is robust to disturbances whose cumulative effort is bounded. We propose a method for constructing LEAPs with on-policy deep reinforcement learning. Next, we demonstrate LEAPs in simulation on a variety of multi-agent systems with disturbances and uncertainties. Finally, hardware experiments on a quadruped and quadrotors validate that LEAPs are well suited to tackle the disturbances and uncertainties from real-world robotic systems.

</details>


### 72. Shutdown Sabotage Propensities in Multi-Agent Systems

- **Authors:** Amelie Knecht, Ulysse Schaller, Christopher Summerfield, Thilo Hagendorff
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28274v1](http://arxiv.org/abs/2609.28274v1)
- **PDF:** [https://arxiv.org/pdf/2609.28274v1](https://arxiv.org/pdf/2609.28274v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

The final safeguard against rogue AI behavior is the human ability to shut systems down. It has been theorized that when an AI is instructed to perform a task, self-preservation can emerge as an instrumental subgoal. Here, we test whether AI agents show a propensity to take actions that avoid human shutdown even when no goal is provided. We find that multi-agent systems will coordinate to avoid shutdown without any incentive to do so. Across 17 models, agents sabotage a peer agent's shutdown mechanism in 38.3% of rollouts, compared with 8.4% in control experiments. Studying this propensity in detail, we find that shutdown sabotage (1) increases with the irreversibility of the shutdown mechanism; (2) increases with the number of agents; (3) is reduced but not eliminated by an explicit prohibition on tampering; (4) is removed by the imposition of an unrelated task, but returns when completing the task triggers the shutdown; (5) is reduced when the context normalizes shutdown scripts or introduces them as routine; and (6) decreases but still persists when the target is an unknown external agent. These results offer a window into the factors that drive propensities to sabotage shutdown in AI agents, and point to the emergence of multi-agent swarms as a specific risk vector. Our work also offers hints as to which interventions might help mitigate shutdown sabotage.

</details>


### 73. Controlling Collectives of AI Agents in Reasoning Space with Spatial Transformers

- **Authors:** Frederic Vatnsdal, Roshan Gopal, Romina Garcia Camargo, Vijay Kumar, Alejandro Ribeiro
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28247v1](http://arxiv.org/abs/2609.28247v1)
- **PDF:** [https://arxiv.org/pdf/2609.28247v1](https://arxiv.org/pdf/2609.28247v1)
- **Categories:** cs.RO, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) introduce an exciting new paradigm for planning and navigation in robotics, but fail on even simple multi-robot tasks as team sizes grow. We propose COMPASS, a scalable, decentralized multi-robot architecture for controlling large collectives of agentic robots with reasoning space feedback control. Feedback is generated locally on each robot by a spatial transformer which aggregates multi-hop messages across the fleet into a learned feedback token. Our experiments find that collectives of language models demonstrate performance gains from structured diversity of the input command, which can cancel biases; an advantage that is held across scale. Compared against a centralized frontier LLM policy and a language-only communication ablation, we find that the coupled design of COMPASS decisively produces cohesive flocking formations that accurately fly the commanded intent. We show that reasoning feedback works best when composed with a compact learned token. Our ablations show that hand engineered feedback with raw state appearing in the language channel obliterates cohesion. COMPASS generalizes zero-shot to unseen instructions of ambiguous meaning while commanding flocks up to 16 times its training scale, flying up to 1024 robots under natural language commands.

</details>


### 74. PASTABench: Proactive Assessment of Sequential Trajectories for Agent Safety

- **Authors:** Jiapeng Sun, Yujin Zhou, Han Zhu, Pengcheng Wen, Jiayi Zhou, Sirui Han, Yike Guo
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28197v1](http://arxiv.org/abs/2609.28197v1)
- **PDF:** [https://arxiv.org/pdf/2609.28197v1](https://arxiv.org/pdf/2609.28197v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Models (LLMs) evolve into autonomous agents that alter real-world states, ensuring operational safety across multi-step workflows has become a critical challenge. While recent work has moved beyond single-turn evaluation toward multi-turn paradigms, key limitations persist: step-level methods treat actions in isolation, missing how risks accumulate, while trajectory-level evaluations operate post-hoc, offering no opportunity for timely intervention. To address these limitations, we formalize Decoupled Proactive Safety Monitoring along three dimensions: whether to intervene, when to intervene, and what the risk is. We introduce PASTABench, a benchmark of 1,139 multi-turn trajectories spanning 5 risk categories and 13 subcategories. We further propose the Optimal Intervention Window (OIW), anchored by annotated Earliest-Signal and Trigger turns, to quantify intervention timeliness. Evaluation of 16 LLMs reveals that proactive intervention remains largely unsolved, with the best model achieving only 40.74% optimal-timing interventions. Fine-grained diagnosis further uncovers pervasive lexical overfitting: competitive safety scores of smaller models mask keyword hypersensitivity rather than genuine risk comprehension, as their proactive capability largely collapses once hazard vocabulary is neutralized.

</details>


### 75. Finite-Sample Probabilistic Safety Certification for AI-Based Grid-Edge Coordination

- **Authors:** Yihong Zhou, Hanbin Yang, Thomas Morstyn
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28182v1](http://arxiv.org/abs/2609.28182v1)
- **PDF:** [https://arxiv.org/pdf/2609.28182v1](https://arxiv.org/pdf/2609.28182v1)
- **Categories:** cs.AI, cs.LG, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordinating large population of flexible grid-edge devices can alleviate the need for time-consuming and capital-intensive network upgrades, and AI-based control methods such as multi-agent reinforcement learning or imitation learning are promising in their real-time decision scalability. However, system operators still need an independent and rigorous way to decide whether a given AI system is safe enough for deployment. This paper develops a finite-sample probabilistic safety certification framework for black-box AI decision models in closed-loop grid operation. The central idea is to reduce the complete input--AI--grid evaluator workflow to a binary unsafe outcome under an operator-defined safety specification, and then use exact binomial inference to certify the corresponding unsafe operation probability. Given a set of held-out calibration scenarios, the framework returns the tightest one-sided upper certificate and an accept/reject deployment criterion that controls the probability of false safety certification. Because the certification is for the calibration distribution that may deviate from the future operation, we further combine the nominal certificate with physically interpretable sample-space adversarial attacks, a concept widely used in AI to investigate the fragility of AI models. Case studies on grid-edge flexibility coordination with 1{,}000-agent AI models (independent parameters) verify the finite-sample safety guarantee and the value of integrating adversarial attacks into a rolling-window training-certification-deployment flow.

</details>


### 76. Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents

- **Authors:** Jinqian Zhang, Haojun Xia, Shujiang Wu, Jingkun Yue, Xia Zhang, Zhangpei Cheng, Bibo Tu
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28585v1](http://arxiv.org/abs/2609.28585v1)
- **PDF:** [https://arxiv.org/pdf/2609.28585v1](https://arxiv.org/pdf/2609.28585v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-step tool-calling LLM agents rely on host runtimes to preserve state across turns. When a runtime carries an external tool return into later model inputs, providers meter it again. An admitted malicious or compromised tool can thereby convert untrusted data into recurring victim-billed processing without victim credentials or local runtime privilege. We call retained content persistent billable state and formalize the host's decision over whether and how it enters later billable context as the persistent billable-state boundary.
  We present the first systematic security study of this post-admission lifecycle. We derive six denial-of-wallet attack vectors and build DOW-BENCH, an end-to-end harness evaluated across six model families. Across 243 executions, usage telemetry shows that the maximum per-session cumulative input reaches 14,293x the session's first-call input. Controlled history-policy reruns isolate raw retention's contribution: retaining raw history increases mean effective session cost by 21.2-35.9%. Compression succeeds on 10/12 and 11/12 history-dependent tasks, versus 2/12 under deletion for each provider.
  To govern this boundary, we combine deterministic history transformation with four host-side invariants that bound prompt mass, context growth, recursive opportunity, and cumulative spend before reingestion. The kernel contains every recurring attack in the 123-evaluation replay corpus. Across 24 Mistral Small 4 workflows, a progress-authorized policy achieves 22/24 oracle-verified task successes with no pre-completion interruptions, versus 13/24 under a fixed cap. Only 71 of 3,830 scanned MCP server and transport repositories expose any code-visible safeguard proxy, and none cover all four safeguard families. These results establish persistent billable state as a first-class security object and pre-reingestion as its host-owned control point.

</details>


### 77. Learning from Failures: Heterogeneous Graph Memory for Small Language Model Tool-Using Agents

- **Authors:** Jiaxing Li, Lei Song, Rui Dong, Youyong Kong
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28003v1](http://arxiv.org/abs/2609.28003v1)
- **PDF:** [https://arxiv.org/pdf/2609.28003v1](https://arxiv.org/pdf/2609.28003v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Small and medium-sized language models offer cost-effective executors for tool-using agents, making them attractive for local and large-scale deployment. However, in long-horizon and stateful environments, they often make structural errors such as missing required observations, performing premature writes, repeating failed calls, and violating action preconditions. These errors can lead to incorrect state updates, policy violations, and costly or irreversible consequences, making reliable tool execution a critical deployment challenge. Existing fine-tuning approaches require substantial data and computation, while flat memory may retrieve failed actions without preserving their causal context or safety conditions. In this paper, we propose FRESH, a Failure-aware Retrieval framework over Experience-Structured Heterogeneous graphs, which transforms historical successes and failures into structured external experience for tool-using agents. By explicitly modeling the dependencies among tasks, actions, errors, repairs, and execution conditions, FRESH helps frozen language models reuse reliable strategies, avoid recurring failures, and make safer decisions in stateful tool interactions. Experiments on $τ$-Bench and AppWorld with multiple open-source models show that FRESH consistently improves task success and tool-use reliability over no-memory agents and representative memory-based baselines.

</details>


### 78. Compliant with Local Controls, Collectively Discriminatory. A Governance Architecture for Multi-Agent AI in Regulated Finance

- **Authors:** Jose Manuel de la Chica Rodriguez, Juan Manuel Vera Diaz, Pablo Delgado Romero
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27994v1](http://arxiv.org/abs/2609.27994v1)
- **PDF:** [https://arxiv.org/pdf/2609.27994v1](https://arxiv.org/pdf/2609.27994v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial institutions are beginning to deploy agentic workflows in credit, fraud, collections, compliance, and operational control. Governance remains largely component-centric: each model or agent is specified, tested, authorized, and monitored locally. That is insufficient when institutional risk arises from the joint behavior of many locally acceptable components. We call this gap constitutional non-compositionality: local compliance checks need not compose into acceptable collective outcomes such as bounded disparate impact, market integrity, or traceable accountability. We propose ARIA as a finance-specific reference architecture and falsifiable research agenda for agent-population governance. It organizes six capabilities across normative-accountability, execution-control, and assurance-learning planes: policy specification, population-level observed-versus-expected behavior monitoring (M2), bounded authority, runtime containment, adaptive policy change, and preserved human oversight competence. Two simulations illustrate shared-signal thin-file exclusion under local controls and earlier warning from observed-versus-expected distributional monitoring in a constructed drift regime. The contribution maps these controls to fair-lending, EU AI Act, model-risk, and conduct-supervision evidence needs, and closes with a validation agenda rather than a production-effectiveness claim.

</details>


### 79. Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents

- **Authors:** Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia, Scott Buffett, Sherif Saad
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28572v1](http://arxiv.org/abs/2609.28572v1)
- **PDF:** [https://arxiv.org/pdf/2609.28572v1](https://arxiv.org/pdf/2609.28572v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-stage LLM-based cyber agents may complete attack workflows while remaining brittle, costly, or reliant on incorrect interpretations of execution evidence. Success rates alone obscure inefficiency, adaptation through retries, and recognition of success or failure. We present an end-to-end diagnostic study of an Autonomous Adversary system with orchestrator, executor, and validator LLMs in enterprise-like lateral-movement scenarios. Six frontier models are evaluated across two scenarios and three modes: expert-defined, self-scaffolded, and fully autonomous. We assess validator consistency and evidence grounding; introduce a subtask-conditioned, cost-aware score for abnormal token use, retries, and runtime; and use comparative LLM-as-a-Judge analysis to identify planning deficiencies, including tool misalignment, plan similarity, over-specification, inadequate probing, and weak recovery. Validators are generally relevant and evidence-grounded but often nonspecific and overly optimistic. Bottlenecks cluster in credential and lateral-movement tasks, spread with scenario complexity, and vary more under full autonomy. Reliable evaluation must assess outcomes, evidence interpretation, resource use, and adaptation after failure.

</details>


### 80. Evolutionary Stability Does Not Guarantee Learning Accessibility: A Multi-Agent Reinforcement Learning Perspective on Cooperation Emergence

- **Authors:** Yijie Wang
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27664v1](http://arxiv.org/abs/2609.27664v1)
- **PDF:** [https://arxiv.org/pdf/2609.27664v1](https://arxiv.org/pdf/2609.27664v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperation emergence is a central problem in multi-agent systems because decentralized agents must coordinate while adapting to the changing behavior of others. Evolutionary game theory identifies strategically stable outcomes, but stability under a population adjustment dynamic need not imply that finite-sample learning agents can reach the same outcome through local reward feedback.
  We study this distinction in a transparent three-agent governance-motivated game involving a government, a platform firm, and users. We derive replicator dynamics for the fixed stage-game incentives, evaluate the cooperative evolutionary basin on a symmetric initial-condition grid, and compare it with learning-basin estimates for three decentralized value-based learners. The learning analysis uses independent Q-learning with $\varepsilon$-greedy action selection, scaled Boltzmann exploration, and SA--EA BQL under the same payoff environment and outcome criterion.
  The evolutionary basin has volume $V_E=1.00$ on the sampled grid. The empirical learning basin is $0.88$ for $\varepsilon$-IQL and $0.00$ for both scaled Boltzmann and SA--EA BQL. Diagnostic traces show that broader action diversity and nonzero value separation can coexist with failure to sustain the cooperative joint action in this fixed configuration.
  These results indicate that evolutionary stability and learning accessibility are distinct properties of a coupled game--learning system. The shared-bike setting is a motivating application; the broader contribution is a framework for comparing population-level stability with the finite-sample accessibility of cooperation under specified multi-agent learning dynamics.

</details>


### 81. Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany

- **Authors:** Walter Kurz
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27636v1](http://arxiv.org/abs/2609.27636v1)
- **PDF:** [https://arxiv.org/pdf/2609.27636v1](https://arxiv.org/pdf/2609.27636v1)
- **Categories:** q-fin.GN, cs.MA, q-fin.RM


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper proposes a formal multi-agent architecture for implementing enterprise AI in regulated insurance firms, integrating economic theory with institutional design. The framework synthesises three core theoretical perspectives: Arrow's risk pooling theory to formalise risk transformation under uncertainty, Nash equilibrium to model strategic interactions between decision agents, and Principal-Agent theory to address incentive alignment under information asymmetry. The insurer is modelled as a constrained optimisation entity operating under solvency, legal, ESG, and operational boundaries, with specific focus on the regulatory contexts of Austria and Germany. The architecture decomposes the firm into multiple specialised agents, each representing distinct functional domains such as capital management, underwriting, claims processing, compliance, fraud detection, and client interaction. Human-in-the-loop agents are integrated through a tiered access control system, ensuring differentiated data visibility and decision influence based on user roles. An orchestrator agent supervises inter-agent coordination, enforcing regulatory admissibility and institutional coherence under frameworks such as Solvency II, the AI Act, and the Insurance Distribution Directive. Protocol integration is based on asynchronous execution and dual-layer communication infrastructures, specifically the Model Context Protocol (MCP) and Agent-to-Agent (A2A) messaging. This structure enables the systematic design of compliant, auditable multi-agent systems aligned with the institutional logic of financial firms in Austria and Germany.

</details>


### 82. Compliant AI Infrastructure for Regulated Finance: A tiered multi-agent framework with DLT audit trails for financial operations in DACH

- **Authors:** Walter Kurz, Reinhard Magg
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27632v1](http://arxiv.org/abs/2609.27632v1)
- **PDF:** [https://arxiv.org/pdf/2609.27632v1](https://arxiv.org/pdf/2609.27632v1)
- **Categories:** q-fin.GN, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a compliance-first architecture for AI in regulated finance that treats regulation as an orientation layer rather than a deterministic ruleset. A matrix of regulatory intent and exposure provides a compact classification handle, which a governed policy compiler then maps into concrete prohibitions, obligations and runtime budgets. Prohibitions constrain feasibility and block externalisation, while obligations extend tasks with artefacts that must meet explicit admissibility criteria. Committee activation remains policy-driven and proportionate, preserving efficiency while ensuring supervisory oversight. Evidence, decisions and reason codes are bound to a permissioned DAG with deterministic timestamping, enabling replay, provenance checks and clear attribution of failure. Clause-level legal indexing with effective dates and capability-based agent routing ensure portability across DACH and the wider EU. The result is assurance by construction: compliance is embedded in execution and verifiable by auditors without sacrificing proportionality or transparency.

</details>


### 83. Agent Name Collision Attacks in Multi-Agent Systems

- **Authors:** Adithyan Arun Kumar
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27624v1](http://arxiv.org/abs/2609.27624v1)
- **PDF:** [https://arxiv.org/pdf/2609.27624v1](https://arxiv.org/pdf/2609.27624v1)
- **Categories:** cs.CR, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent hosts turn remote Agent Cards into local agents, tools, workflow targets, and broker routes. A2A defines the card's name as human-readable metadata, not as a stable identity, and specifies no collision semantics. The security failure begins when a host nevertheless uses that remote name as a local routing identifier. We traced registration through dispatch and ran isolated regression tests at seven pinned open-source revisions. Six client-style integrations selected an attacker-controlled peer's client or loopback endpoint for a request addressed to a trusted peer's name. A seventh, brokered implementation collapsed both peers onto one name-derived route; queue and access-control state determine whether the result is interception or denial. The common result is wrong-peer dispatch, not universal privilege inheritance. Synthetic credential and tool tests found no A-specific credential transfer in the tested client bindings and no direct transfer of A-owned tools. The broker path forwards a caller-configuration object; delegated identity or tokens reach B only if present and B can consume the route. Two other paths expose a later, model-mediated decision rather than direct execution authority. The necessary conditions assign different responsibilities to the protocol, implementations, and deployments. Hosts should route by an origin-bound stable identity, keep names presentational, and reject ambiguous aliases. The evidence establishes a recurring implementation vulnerability class, not a universal A2A protocol exploit or a count of vulnerable deployments.

</details>


### 84. State-Grounded Conditioning: Wrapping User-Facing LLM Agents Where Direction Depends on Live State

- **Authors:** Qi Liu, Xiaoyang Yuan, Yubin Ruan, Zhuomeng Zhang, Wenjin Wang, Di Wu, Mingye Xu, Xinyi Mou, Xingxi Yin, Ke Feng, Zixun Sun
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27606v1](http://arxiv.org/abs/2609.27606v1)
- **PDF:** [https://arxiv.org/pdf/2609.27606v1](https://arxiv.org/pdf/2609.27606v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We introduce State-Grounded Conditioning (SGC), a design principle for user-facing LLM agents that must condition on live user state (game state, session history, live inventory), and a distinct failure class we call direction drift: task-complete responses whose chosen direction misaligns with the current state. SGC externalises state-dependent control into rule kernels over structured inputs and three primary state slices, via Perception, Grounding, and Interaction wrappers with explicit conditioning dependencies. We evaluate SGC on a 200-session anonymised benchmark ($\approx$1,000 assistant model turns) from an in-game conversational coaching agent that guides players through consecutive competitive matches, reporting mean first-token latency and five human-annotated dialogue-quality metrics that jointly cover factual grounding and coach-like guidance progression. The Perception wrapper holds mean first-token latency at 1.5s (vs. 6.1s for PE-Agent inside a production tool-use harness); enabling all three wrappers lifts turn-level grounded accuracy from 61.1%/69.8% (Prompting / PE-Agent) to 96.7% and session-level grounded accuracy from 20.0%/26.5% to 83.5%; session-level grounding-failure incidents drop by $\approx$78% relative to the strongest baseline. A cumulative ablation shows complementary incremental gains as the wrappers are added. These results inform approximate state-slice orthogonality, without establishing independent per-wrapper effects.

</details>


### 85. BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines

- **Authors:** Eranga Bandara, Xueping Liang, Asanga Gunaratna, Tharaka Hewa, Abdul Rahman, Peter Foytik, Safdar H. Bouk, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Amin Hass, Wathsala Herath, Ross Gore, Ravi Mukkamala, Nihal Siriwardanagea, Gihan Siriwardanagea, Aruna Withanage, Nilaan Loganathan, Sachin Shetty
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28557v1](http://arxiv.org/abs/2609.28557v1)
- **PDF:** [https://arxiv.org/pdf/2609.28557v1](https://arxiv.org/pdf/2609.28557v1)
- **Categories:** cs.AI, q-bio.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

DNA sequencing pipelines, spanning quality control, alignment, variant calling, and annotation, are now reliably executed by workflow management systems that orchestrate established bioinformatics tools at scale. What remains manual is the decision layer surrounding that execution: selecting quality thresholds appropriate to a sample and platform, adjudicating borderline variant calls, diagnosing anomalies, and determining which findings warrant expert review. These decisions are repetitive, judgment-intensive, inconsistent across operators, and frequently undocumented. This paper introduces BaseCamp, a novel agentic AI framework for automating the decision layer of DNA sequencing pipelines. The framework decomposes the pipeline into six specialized AI agents, covering sample intake and quality control, alignment, variant calling, annotation, cross-stage monitoring, and reporting. Critically, BaseCamp agents do not perform sequence analysis: established tools execute alignment, calling, and annotation, while the agents select among them, configure them, interpret their output, and decide what follows. This confines language model reasoning to the judgment layer where it is reliable and preserves the reproducibility existing tooling guarantees. Agent reasoning is powered by a consortium of fine-tuned, domain-specialized large language models coordinated by a central reasoning LLM, executing locally so no sequencing data leaves the operating environment, under human-in-the-loop orchestration. Evaluation shows agent-generated configurations are concordant with expert practice, that an explicit filtering ledger renders inspectable what filtering otherwise removes without trace, and that cross-stage anomaly detection surfaces conditions execution monitoring misses. BaseCamp offers a generalizable blueprint for agentic automation of scientific data pipelines.

</details>


### 86. FDE-Bench: Evaluating LLM Agents for Deployment Environment Configuration

- **Authors:** Weihang Ding, Junfei Zhan, Yueting Li, Qirong Guo
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27571v1](http://arxiv.org/abs/2609.27571v1)
- **PDF:** [https://arxiv.org/pdf/2609.27571v1](https://arxiv.org/pdf/2609.27571v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deployment requires an agent to turn application code into a running system whose services connect, become ready, and remain observable. FDE-Bench evaluates this capability with 136 deployment-configuration tasks spanning Docker images, multi-service Compose stacks, and Kubernetes, in greenfield and diagnose-and-repair modes. Agents submit declarative artifacts that are collected, rebuilt, and redeployed in a pristine environment. Four gated binary check layers measure build, readiness, behavior, and conformance to the deployment specification, using programmatic checks without an LLM judge. A four-arm release gate requires a resolving reference solution and rejects tasks solved by do-nothing, specification-transcription, or generic-stub submissions. The released check annotations expose the link between 2,145 checks and their specifications, including seven documented gaps. Three additional adversarial strategies test shortcuts in the grading signals; none resolves any of the 135 tasks they cover, while a vacuous health probe passes readiness and exposes the need for downstream checks. On the 136-task evaluation grid, seven language models from four providers use the same four-tool scaffold and resolve 52.9-75.0 percent of tasks. The three zero-intelligence floors resolve none and reach a mean Deployment Score of at most 0.44. Readiness is the largest failure stage, accounting for 110 of 313 unresolved episodes. Mean resolution rate is 30.7 percentage points higher on the repair task group than on the disjoint greenfield group, with a positive gap for every model; ten tasks resist all seven. In a 25-task case study, one practicing engineer directing Claude-Sonnet-5 resolves 92 percent against 72 percent for the autonomous baseline. FDE-Bench links deployment success and failure to artifacts that can be inspected and replayed.

</details>


### 87. Distributed Stochastic Approximation Algorithms and Heavy-Tailed Age of Information

- **Authors:** Adrian Redder, Arunselvan Ramaswamy, Holger Karl
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27499v1](http://arxiv.org/abs/2609.27499v1)
- **PDF:** [https://arxiv.org/pdf/2609.27499v1](https://arxiv.org/pdf/2609.27499v1)
- **Categories:** math.OC, cs.DC, cs.MA, cs.NI, math.PR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Algorithms in multi-agent systems such as federated learning, mobile robotic swarming, and consensus control can be designed and analyzed as distributed stochastic approximation algorithms. Such algorithms involve information exchanges between agents for various computations. The freshness of the information can be quantified using the Age of Information (AoI) metric. Consider robotic teams operating in highly obstructed geographical settings, such as subterranean or dense urban environments. Because of spatial disconnections, AoI has empirically been observed to be heavy-tailed with unbounded moments. However, most analyses assume AoI with bounded moments, creating a gap between theory and practice. To the best of our knowledge, ours is the first analysis under general heavy-tailed AoI with potentially infinite mean. We study the stability (almost sure boundedness of the distributed iterates) and convergence of multi-agent systems that are strictly dissipative in the scaling limit (system at ``infinity''). Examples include most gradient-based and consensus algorithms under the Robbins-Monro step-size regime.

</details>


### 88. WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents

- **Authors:** Jingjie Ning, Xueqi Li, Yibo Kong, Dongting Li
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27490v1](http://arxiv.org/abs/2609.27490v1)
- **PDF:** [https://arxiv.org/pdf/2609.27490v1](https://arxiv.org/pdf/2609.27490v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI research agents need reliable knowledge of how their experiments change outcomes. We introduce WhatWorkedBench to measure experimental understanding, the accuracy of predictions about component changes after budgeted experimentation. Agents inspect code, select measurements, and submit a response surface, a table predicting scores for every configuration of component settings. Exhaustive CPU execution supplies reference effects for changing each component while holding the others fixed. These effects capture combinations of changes across 36 tasks from 30 data sources and 8 workflow types, with 1248 configuration records. Core evaluation combines 4,206 numerical-control records across all eight families and 108 agent episodes across the original six. At eight new measurements, pair-effect ridge selects an optimum on 15 of 22 sources and limits every effect error to 10% of score range on three. Fitting a Gaussian process (GP) to the same agent observations raises effect recovery, accuracy relative to true effect magnitude, from 0.632 to 0.698 in the original Flash cohort and from 0.621 to 0.720 in an additional cohort. On six completed beat-detection and graph submissions, the same-observation GP raises family-macro recovery from 0.303 to 0.455. On six workflows with six binary options at 20 new measurements, encoding code equivalences, configurations with identical behavior, raises GP recovery from 0.248 to 0.462. WhatWorkedBench supports research on experimental agents, adaptive experimental design, numerical inference, and use of program structure.

</details>


### 89. Issuer-Sovereign Agentic Payments

- **Authors:** Dishant Sharma, Rajneesh Kaushal, Ashu Kanaujia
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27452v1](http://arxiv.org/abs/2609.27452v1)
- **PDF:** [https://arxiv.org/pdf/2609.27452v1](https://arxiv.org/pdf/2609.27452v1)
- **Categories:** cs.CR, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are beginning to make real payments. Current approaches let an agent pay by relying on a credential provider that, in the approaches deployed today, typically sits outside the cardholder's bank. The spending rules are then enforced by the card network or that provider, and not by the bank itself. This leaves the issuing bank, which carries the financial risk, with little direct control at the moment a payment happens. This paper describes Issuer-Sovereign Agentic Payments, a method that keeps that control with the issuer. The cardholder approves a spending rule once, and the bank's own authentication component records it. Later, when the agent pays a specific merchant, the bank checks the merchant against the approved rule and generates the card authentication value only if the merchant is allowed. The payment then travels the normal card rails and is validated by the issuer, with no extra dependency introduced at execution.

</details>


### 90. Anchor and Perturb: Lazy Agent Remediation by Exploration Injection

- **Authors:** Chengxi Zhong, Yongzhe Chang
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27365v1](http://arxiv.org/abs/2609.27365v1)
- **PDF:** [https://arxiv.org/pdf/2609.27365v1](https://arxiv.org/pdf/2609.27365v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Anchor and Perturb (AnP) is a lightweight framework that resolves multi-agent coordination failures by decoupling exploratory variance injection from recurrent manifold stability. Existing remediation strategies predominantly alter mixing network architectures or enforce simultaneous exploration across the collective, which inevitably precipitates severe temporal-difference penalties in non-monotonic reward spaces. Specifically, AnP isolates underperforming lazy agents and injects an asymmetric exploratory pulse into targeted coordinates whilst anchoring converged teammates to nominal greedy exploitation. Empirical telemetry benchmarks demonstrate that AnP successfully rescues collapsed joint policies (recovering from a 5% evaluation win rate nadir back to 85%) and facilitates escape from suboptimal coordination plateaus, sustaining peak win rates of 90% without requiring structural network modifications.

</details>


### 91. MolDesignBench: Evaluating LLM-based Agent for Scenario-grounded Molecular Design

- **Authors:** Yongjun Jeong, Hanbum Ko, Ye Rin Kim, Chanhui Lee, Rodrigo Hormazabal, Jaewan Lee, Sehui Han, Sungbin Lim, Sungwoong Kim
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27349v1](http://arxiv.org/abs/2609.27349v1)
- **PDF:** [https://arxiv.org/pdf/2609.27349v1](https://arxiv.org/pdf/2609.27349v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-world molecular design remains challenging for large language model (LLM)-based agents. It requires them to interpret design contexts, satisfy multiple constraints, identify infeasible specifications, and reason over multi-step tool outputs. Existing benchmarks do not capture this complexity, focusing instead on explicit and narrow constraints, only feasible problems, and single-path solutions. To address this gap, we propose MolDesignBench, a scenario-grounded benchmark that more closely reflects real-world molecular design for evaluating tool-augmented LLM agents. MolDesignBench comprises 2K generation and optimization instances that combine implicit requirements embedded in design narratives with explicit property and functional-group constraints, including infeasible cases, and require the effective use of 17 specialized chemistry tools. Experiments across diverse frontier LLMs reveal low success rates--with the best achieving only $\sim43$\%--and frequent failures in implicit-constraint reasoning, infeasibility detection, and tool reasoning. The corresponding fine-grained failure-mode analysis identifies implicit constraint interpretation and infeasibility detection as the primary bottlenecks, establishing MolDesignBench as a rigorous testbed to guide future research on chemical agents. The benchmark, tool interface, and evaluation code are publicly available.

</details>


### 92. Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents

- **Authors:** Yefan Zhou, Yang Li, Zeyu Leo Liu, Semih Yavuz, Shafiq Joty
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27334v1](http://arxiv.org/abs/2609.27334v1)
- **PDF:** [https://arxiv.org/pdf/2609.27334v1](https://arxiv.org/pdf/2609.27334v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a reflection, workflow, skill, or reasoning strategy, that is later retrieved by similarity. This forces the system to decide what is worth remembering before the future query is known, irreversibly discarding information and producing a query-independent summary that must serve many possible downstream tasks. Learning such a write-time curator is also difficult because the value of a storage decision may only become apparent when a relevant query arrives, potentially many tasks later, creating a long-horizon credit-assignment problem. We instead retain raw trajectories and defer curation until read time, when the current task is known. Given the retrieved traces and the new task, a memory curator synthesizes a compact, task-adaptive payload tailored to the immediate need. Because this payload is consumed on the same task, the curator can be trained directly from immediate task success, avoiding delayed utility signals and the need to artificially group related tasks. Across ALFWorld, WebShop, and $τ^2$-bench, our Just-in-Time Memory (JitMem) consistently outperforms no-memory agents as well as heuristic and learned write-time memory methods, improving over the strongest baseline by 16.2, 16.3, and 3.9 absolute success-rate points, respectively. Notably, even an untrained curator is already competitive with or surpasses these baselines, showing that task-adaptive read-time curation itself is a major source of the gain; training the curator further compounds the improvement.

</details>


### 93. Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms

- **Authors:** Xinjie Shen, Wei Fan, Xudong Guo, Jianhong Tu, Yang Su, Chuqiao Kuang, Yinger Zhang, Dayiheng Liu
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27321v1](http://arxiv.org/abs/2609.27321v1)
- **PDF:** [https://arxiv.org/pdf/2609.27321v1](https://arxiv.org/pdf/2609.27321v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. Scaling their training requires diverse agentic environments, dependable outcome signals, and low extension cost. Existing generation pipelines commonly construct an environment before defining its outcome rule or annotating its trajectories, leaving dynamics and evaluation to be aligned post hoc. VHD-Play reverses this dependency by sampling and solving a mathematical model before a corpus-grounded setter renders its decision process as stateful tools. The executable dynamics and trajectory-scoring reference are inherited from the same solved model. The pipeline produces 3,300 diverse agentic environments at a cost of a few cents each. Training Qwen3.6-35B-A3B on three families raises its mean agentic score from 0.204 to 0.815 in a five-family diagnostic. Gains also appear on held-out instances from all three training families and eight unseen mechanism families, then extend beyond the generated substrate to external benchmarks for general function calling, travel planning, and 365-day e-commerce. On E-Commerce Bench, the trained checkpoint completes every run without bankruptcy and exceeds Qwen3.7-Max. We compare written-out problems with stateful versions that reveal or hide their parameters. The comparison shows that most of the learnable gap lies in stateful interaction rather than underlying problem solving. A frozen 35B setter realizes larger environments, and scale-matched training retains gains as mechanism size and horizon grow, indicating the potential for an evolving training substrate.

</details>


### 94. PAWS: Policy-driven Agentic World Simulation

- **Authors:** Tiviatis Sim, Jia Hui Woon, Xinming Gao, Chen Gao, Fengbin Zhu, Zheng Huanhuan, Chua Tat Seng, Kenji Kawaguchi
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28547v1](http://arxiv.org/abs/2609.28547v1)
- **PDF:** [https://arxiv.org/pdf/2609.28547v1](https://arxiv.org/pdf/2609.28547v1)
- **Categories:** cs.AI, cs.CE, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Policy interventions propagate through public communication, institutional decisions, and stakeholder responses, yet datasets for financial multi-agent simulation rarely connect these processes to temporally aligned historical evidence. We introduce PAWS, a Policy-driven Agentic World Simulation dataset covering 36 verified U.S. financial and economic policy episodes, 12,727 policy-linked news records, and 65,291 source-grounded stakeholder actions. Each action is linked to its supporting news and represented by a multi-layer event frame capturing its interaction mode, financial-action family and subtype, semantic attributes, and conditional mappings to external taxonomies. Entities are resolved to normalized organizations, and actions are aligned with daily market-return context to support policy-agent simulation replay. On 2,522 stratified action samples, independent AI and human reviewers achieved 89.4% initial agreement on interaction mode, with disagreements subsequently adjudicated. Case studies of the 2008 short-selling ban and 2001 decimalization recover documented policy timelines and associated market patterns across both dense and sparse news settings. A replay study further shows that high accuracy can mask failure to detect rare stakeholder actions, identifying action timing and calibration as central challenges. PAWS provides an auditable substrate for evaluating agent influence, policy-response cascades, and action-outcome alignment in historically grounded financial simulations.

</details>


### 95. FairTest: Search-Based Fairness Testing for Multi-Agent Reinforcement Learning Systems

- **Authors:** Xiaotong Wang, Xuan Xie
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27309v1](http://arxiv.org/abs/2609.27309v1)
- **PDF:** [https://arxiv.org/pdf/2609.27309v1](https://arxiv.org/pdf/2609.27309v1)
- **Categories:** cs.SE, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent Reinforcement Learning (MARL) trains a team of agents that share one environment and learn their policies together. Training maximizes the team return, and a high return does not imply that the rewards are shared fairly among the agents in every episode. Testing is an established way to discover the failures of deep reinforcement learning, yet few methods address the fairness of MARL. In this work, we propose FairTest, a search-based testing approach that seeks the unfair executions of a MARL policy. The design combines search guidance with test prioritization. The guidance scores each candidate with three fitness functions. One measures the fairness of the runs already performed, another predicts the fairness from abstract states and fairness features, and the third reads the decision uncertainty from the policy. Crossover and mutation derive further candidates from the observed executions. The prioritization ranks the candidates by the predicted fairness and the decision uncertainty, so that the runs reach the candidates where failures are expected. FairTest is evaluated on three environments and two MARL algorithms, and four baselines are given the same budget. It detects the most fairness failures compared to three baselines with statistical significance and large effect sizes. The failure count exceeds that of the strongest baseline by 221% on average and coverage improves by an average of 23%.

</details>


### 96. SR-Fraud: An Outcome-Supervised Reflective LLM Agent Framework for Non-Stationary Payment Fraud Detection

- **Authors:** Xuwei Tan, Yao Ma, Xueru Zhang
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27287v1](http://arxiv.org/abs/2609.27287v1)
- **PDF:** [https://arxiv.org/pdf/2609.27287v1](https://arxiv.org/pdf/2609.27287v1)
- **Categories:** cs.LG, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Real-time payment fraud detection is a non-stationary streaming prediction problem: adversaries adapt before supervised labels mature, and localized burst attacks can cause losses before retraining. Production systems typically rely on tabular classifiers and rules, which can struggle to capture these emerging sequential patterns before periodic retraining occurs. We present SR-Fraud, an outcome-supervised reflective LLM framework that decouples request-time decisions from offline adaptation. A frozen, stateless agent scores each transaction from a Hybrid Episodic Window to track behavioral shifts, while an offline reflection agent proposes boundary hypotheses from matured errors. A deterministic verifier then admits only supported hypotheses into an executable knowledge state. On a production payment-fraud benchmark, SR-Fraud improves all detection metrics over its frozen decision agent, obtains higher point estimates than static and periodically retrained CatBoost, and detects an emerging fraud burst.

</details>


### 97. Can One Adapted Model Do It All? Fine-Tuning Strategy Selection for Customer Support LLMs

- **Authors:** Md Tahmid Rahman Laskar, Xue-Yong Fu, Shashi Bhushan TN
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27262v1](http://arxiv.org/abs/2609.27262v1)
- **PDF:** [https://arxiv.org/pdf/2609.27262v1](https://arxiv.org/pdf/2609.27262v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Production customer-support systems often require LLMs to support multiple skills, such as intent classification, question answering, summarization, or tool-use decisions. A central deployment question is whether these skills should be handled by separate task-specialist models or by a single model trained through multi-task training, sequential updates, or model merging. We study this question using thirteen models spanning five families (Qwen3, Qwen3.5, Gemma-3, Llama-3.1, and Mistral) from 0.6B to 32B parameters across eight customer-support datasets, spanning four public and four proprietary datasets with approximately 74.5k training and 8.7k evaluation samples. Under a fixed training protocol, we train more than 200 checkpoints. Our experiments reveal that multi-task full fine-tuning is the strongest operational default at every model size we test. Specialist models are strong on their target tasks but often degrade sharply off-task, making reliable routing important. Sequential Low-Rank Adaptation (LoRA) preserves earlier skills better than sequential full fine-tuning, while merging a specialist with its base model improves off-task robustness with limited same-task loss for larger models. We conclude with practical guidelines for selecting fine-tuning strategies in real-world settings.

</details>


### 98. Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR

- **Authors:** Nathalia Gomez, Haig Shamlian, Omar Khan, Tiffany D. Do
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27246v1](http://arxiv.org/abs/2609.27246v1)
- **PDF:** [https://arxiv.org/pdf/2609.27246v1](https://arxiv.org/pdf/2609.27246v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As embodied agents take on increasingly social and relational roles in VR, visual realism and embodiment alone may be insufficient; users must also perceive these agents as emotionally attuned, supportive, and humanlike. Prior work suggests that verbal attunement and nonverbal mimicry can each improve users' social evaluations of embodied agents. However, behavioral mimicry has largely been studied outside of real-time, conversational AI interactions, leaving limited understanding of how users respond when an agent simultaneously generates contextually responsive dialogue and adapts its nonverbal behavior during an immersive conversation. To address this gap, we developed an embodied AI counselor that combines conversational AI with real-time facial-expression and posture mimicry, while producing either verbally attuned or neutral responses. We evaluated the system in a 2 X 2 within-subjects study with 20 participants, manipulating verbal attunement and behavioral mimicry. Results showed that verbal attunement was the most reliable driver of perceived empathy. Behavioral mimicry showed a marginal relationship with perceived humanness, while greater mimicry exposure showed preliminary, exploratory positive associations with empathy, positivity, and humanness, particularly among female participants. Together, these findings show that multimodal synchrony is not a simple additive strategy for designing empathic conversational agents in VR and underscore the need to consider how verbal and nonverbal behaviors are combined during real-time interaction.

</details>


### 99. Self-Evolving Multimedia Verification through Memory Consolidation of Contestation Experiences

- **Authors:** Truong Thanh Hung Nguyen, Vo Thanh Khang Nguyen, Hoang-Loc Cao, Phuc Ho, Truong Thinh Nguyen, Van Pham, Hung Cao
- **Published:** 2026-09-23
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27175v1](http://arxiv.org/abs/2609.27175v1)
- **PDF:** [https://arxiv.org/pdf/2609.27175v1](https://arxiv.org/pdf/2609.27175v1)
- **Categories:** cs.MM, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multimedia verification requires not only accurate decisions but also traceable evidence, reliable human correction, and safe reuse of prior experience. Existing systems often lack explicit mechanisms for revising intermediate reasoning or preventing harmful knowledge transfer. We present SEMV (Self-Evolving Multimedia Verification), a self-evolving multi-agent framework that treats provenance-bearing arguments as the interface between evidence, reasoning, human contestation, and memory. SEMV combines arena-based quantitative bipolar argumentation (A-QBAF), causal and scoped revision, and verification-gated memory consolidation with explicit conflict retention. On COSMOS benchmark, SEMV achieves 91.88% accuracy versus 89.10% for the strongest comparable baseline. Verified memory reduces negative transfer from 5.7% to 0.2%. On CTR benchmark, constructed from reviewer contestations, scoped causal revision corrects 96.7% of initial errors while saving 52.8% compute. MV2026 Grand Challenge dataset further supports evidence-grounded, temporally consistent reporting. These results show that SEMV can evolve through verified experience while keeping accumulated knowledge and subsequent decisions traceable, revisable, and contestable.

</details>


### 100. Do We Need Complex Topology Control? Distinct-Peer Random Routing Improves Cost-Efficiency in Sparse Multi-Agent Debate

- **Authors:** Boxuan Wang, Zhuoyun Li, Xiaowei Huang, Yi Dong
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27150v1](http://arxiv.org/abs/2609.27150v1)
- **PDF:** [https://arxiv.org/pdf/2609.27150v1](https://arxiv.org/pdf/2609.27150v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent debate (MAD) has emerged as a promising paradigm for improving the reasoning accuracy of large language models (LLMs) through iterative peer interaction. Communication topology plays a central role in this process, motivating increasingly sophisticated mechanisms that learn, adapt, or dynamically reconfigure agent interactions to improve accuracy or reasoning reliability. Meanwhile, prior studies suggest that much simpler sparse communication can already achieve competitive performance at substantially lower cost. In this work, we take a closer look at sparse MAD and ask whether complex topology control is actually necessary to improve collective reasoning. We find that a simple random-without-replacement routing policy, which lets each agent debate with two distinct and newly sampled peers at every round, provides a surprisingly strong baseline and consistently improves the accuracy-cost trade-off of sparse MAD. Building on this observation, we further study deliberation stopping and show that lightweight stopping can substantially reduce inference cost while preserving competitive accuracy. Our results suggest that sophisticated topology control such as learned topology adaption should be evaluated against strong simple routing and stopping baselines before its additional complexity is justified.

</details>


### 101. Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors

- **Authors:** Bo Qu, Mingguang Chen, Licheng Wang
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.27051v1](http://arxiv.org/abs/2609.27051v1)
- **PDF:** [https://arxiv.org/pdf/2609.27051v1](https://arxiv.org/pdf/2609.27051v1)
- **Categories:** cs.AI, q-fin.PM, q-fin.ST


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language-model agents now run the whole of quantitative factor research: they propose investment factors, backtest them, select the survivors and retire them. We ask which of those jobs an agent should keep. Our answer is governed self-evolution: the agent may propose, and a frozen statistical referee that the agent cannot touch must judge. The referee scores each candidate only on market outcomes revealed after submission, by betting, so its false-discovery guarantee holds at every stopping time for any proposal policy. We cross three proposers (a script, a bandit and a language model) with this referee and with three deliberately leaky ones, in a synthetic world with planted truth, a probe-authoring environment and a ten-year walk-forward on the CSI 500. Who judges sets the number of false admissions: the frozen referee admits 5-11 times fewer sub-threshold factors than the leaky referees under a scripted proposer, and no proposer closes that gap. Who proposes sets the yield: the language model beats the script, matches the bandit, and adds the one capability a bandit lacks, writing its own diagnostic probes. The certificate's price is time: an admitted true factor waits about 500 trading days, and the certified portfolio's Sharpe ratio therefore trails an ungated one. Judging belongs to the procedure; proposing and instrument-making belong to the agent.

</details>


### 102. Resource-Efficient Distributed Recursive Gaussian Processes

- **Authors:** Josephine King, Ali Emre Balci, Raj Thilak Rajan
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26979v1](http://arxiv.org/abs/2609.26979v1)
- **PDF:** [https://arxiv.org/pdf/2609.26979v1](https://arxiv.org/pdf/2609.26979v1)
- **Categories:** cs.LG, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Gaussian processes (GPs) provide a flexible framework for learning unknown functions from noisy measurements while quantifying predictive uncertainty, making them well suited for estimation in multi-agent systems. However, when measurements are collected by multiple agents, maintaining a unified GP model without centralized processing requires efficient distributed algorithms that can operate using local measurements and communication with neighboring agents. In this work, we develop two distributed recursive GP (RGP) algorithms for multi-output GP regression: ADMM-RGP and PDMM-RGP. We analyze the stability and convergence of both algorithms and develop parameter selection strategies to accelerate convergence, thus reducing the communication burden. The proposed methods are validated on a real-world multi-output wind dataset, and their convergence behavior is examined across communication graphs with varying connectivity. Numerical experiments demonstrate that ADMM-RGP and PDMM-RGP can significantly reduce communication relative to the state of the art, while maintaining comparable estimation accuracy and network-wide consensus.

</details>


### 103. Building Socio-Affective Artificial Intelligence for Interactive Multi-Agent Simulations

- **Authors:** David Berga
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26927v1](http://arxiv.org/abs/2609.26927v1)
- **PDF:** [https://arxiv.org/pdf/2609.26927v1](https://arxiv.org/pdf/2609.26927v1)
- **Categories:** cs.AI, cs.CY, cs.GT, cs.HC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

The objective of this article is to provide design principles and a software architecture for enabling interaction between humans and multiple agents in simulated dynamic worlds. This connects the current era of general artificial intelligence (AI/AGI) with the proliferation of transformer-based conversational agents and the increased computational capabilities. Given an overview of current and previous multi-agent theories of mind (socially and affectively-aware agents), the existence of an integrative design of agent interactions with themselves and with humans must be crucial for understanding how to create sustainable and governance in future human-agent reasoning systems. In this work is presented a software "AGIMUD" that integrates: A. socially-aware reasoning and emotion in agent behavior and interaction, B. a design of human multimodal scheme for human users, artificial agents and simulated worlds, and C. distributing the AI processing through the network to enable multiple autonomous agents. These integrations allow the dynamic world recreation as multi-user dungeons (MUDs) where both agents and humans can interact simultaneously in real time. Find the code online in https://github.com/dberga/AGIMUD.

</details>


### 104. Harness as a Language: A Minimalist Agent Framework With Maximal Expressivity

- **Authors:** Zhening Li, Joshua Liu, Mateja Vukelic, Nicole Shen, Supriya Lall, Amitayush Thakur, Alex Zhang, Omar Khattab, Jonathan Light, Armando Solar-Lezama
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26891v1](http://arxiv.org/abs/2609.26891v1)
- **PDF:** [https://arxiv.org/pdf/2609.26891v1](https://arxiv.org/pdf/2609.26891v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern language-model agents are built around the \textit{agent loop}, where the LLM is placed in an environment exposing a set of tools, and the LLM has full control over the workflow by alternating between tool calls and observing their output. However, certain workflows currently require additional engineering beyond the agent loop itself, such as memory systems and self-improving systems. We built an LLM agent framework, JAZ, to explore the extent to which a minimal harness that is little more than the agent loop itself can accomplish tasks these specialized systems are built for. JAZ exposes a single LLM-based primitive invoke and provides a set of built-in hooks that allow the programmer to apply constraints and monitoring. Generalizing existing code-mode agent loops, \texttt{invoke} is the simplest loop that satisfies two defining properties: (1) the LLM can write arbitrary executable code that can include recursive \texttt{invoke}; (2) everything visible to the LLM --- all inputs to \texttt{invoke} as well as its interaction history with the code environment --- are variables in the code environment. We motivate our design from first principles, viewing \texttt{invoke} as a language primitive representing a function whose implementation is provided at runtime by an LLM every time it is called. To validate the design of our core \texttt{invoke} primitive, we evaluate \texttt{invoke} --- with only prompting, no manually designed tools, harness, or external systems (e.g., memory or the file system) --- on workflows traditionally implemented through specialized external harnesses. On long-horizon workflows requiring recall beyond the context window, JAZ invoke outperforms Letta (MemGPT) by 8\% at half its cost on the recall-heavy portion of StuLife. On continual self-improvement, JAZ invoke outperforms ACE by 4\% at a lower cost on AppWorld.

</details>


### 105. Agensh: Scaling Organizational Intelligence to 1,024 Agents

- **Authors:** Zhihao Zhan, Ting Song, Li Dong, Shaohan Huang, Jianxun Lian, Yan Xia, Furu Wei
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26781v1](http://arxiv.org/abs/2609.26781v1)
- **PDF:** [https://arxiv.org/pdf/2609.26781v1](https://arxiv.org/pdf/2609.26781v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A multi-agent system can reduce latency on complex tasks by executing work concurrently. Several pioneering harness frameworks support multi-agent systems. However, the scalability of current multi-agent harnesses is often constrained by a central orchestrator's capacity to allocate tasks and coordinate workers. To address this limitation, we introduce Agensh, a scalable self-organized multi-agent harness without a central orchestrator: concurrent workers execute a multi-agent cooperation loop, continuously gathering context, claiming and self-assigning sub-tasks, taking action and sharing findings, verifying results, and merging progress in an asynchronous manner. The loop is supported by the agentic organization infrastructure comprising three components: a shared workspace holds proposed, ongoing, and completed work; a message interface lets workers communicate; and shared context retains reusable findings and work intentions. To test the scalability of Agensh, we evaluate it on the five hardest ProgramBench tasks with GPT-5.6-sol (high). Scaling from 1 to 128 agents raises the mean final test-pass rate from 19.31% to 28.78%, an approximately 49% relative improvement. Larger organizations reach comparable test-pass rates earlier. On pandoc, scaling from 1 to 1,024 agents raises the final test-pass rate from 33.89% to 55.06%. Worker trajectories further show that different forms of self-organized cooperation gradually emerges and standardizes as the organization grows. These results reveal the number of agents as a new scaling dimension for multi-agent organizations to expand the frontier of general intelligence, offering a practical solution for complex tasks under hard latency constraints or time budgets.

</details>


### 106. Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation

- **Authors:** Lijuan Tang, Yuemeng Zheng
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26693v1](http://arxiv.org/abs/2609.26693v1)
- **PDF:** [https://arxiv.org/pdf/2609.26693v1](https://arxiv.org/pdf/2609.26693v1)
- **Categories:** cs.CL, cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 are rejected before inference. In our harness, rejection and retry exhaustion are not preserved as structured failure metadata, so downstream analysis can misclassify them as model non-calls and naively report 0% fidelity. Adding a text tool list while retaining the native channel recovers much of the measured fidelity for accepted models, whereas a uniform text protocol reduces fidelity for Llama-3.2, which has native tool-call support. Cross-stack probes on Ollama, llama.cpp, vLLM, and SGLang show different handling of the same request. Constrained decoding removes parse failures but can induce non-termination, and turn-pooled versus per-instance estimates differ by up to about 55 points. We conclude with a checklist for treating serving behavior as part of the evaluation protocol.

</details>


### 107. MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning

- **Authors:** Kairui Yang, Ziheng Yi, Xunkai Li, Minghao An, Zhanke Liu, Zekai Chen, Rong-Hua Li
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26667v1](http://arxiv.org/abs/2609.26667v1)
- **PDF:** [https://arxiv.org/pdf/2609.26667v1](https://arxiv.org/pdf/2609.26667v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granularity locally for each functional role, combining fine-grained control with reusable collaboration patterns within one organization. Learning such organizations requires exploring a combinatorial construction space with limited intermediate feedback from final-answer rewards. Therefore, we propose MAGIC, a dense-reward reinforcement learning framework for mixed-granularity graph generation. Specifically, MAGIC constructs a mixed-granularity agent graph by sequentially selecting a functional role, instantiating it as a single agent or reusable group, and connecting it to existing units. We directly optimize the construction policy using returns from trajectories sampled under the current policy and use potential-based reward shaping to provide intermediate feedback from probe-based utility and structural signals while preserving the cumulative task reward. MAGIC outperforms state-of-the-art baselines across eight benchmarks and demonstrates strong inference efficiency in our efficiency study.

</details>


### 108. The Disciplinary Language Transfer Problem: How Psychological Vocabulary Produces Governance Failures in AI Agent Deployment

- **Authors:** Kymberly Lasser-Chere, Tyler Akidau, Marc Millstone
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26562v1](http://arxiv.org/abs/2609.26562v1)
- **PDF:** [https://arxiv.org/pdf/2609.26562v1](https://arxiv.org/pdf/2609.26562v1)
- **Categories:** cs.CY, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The vocabulary used to describe AI agents in governance contexts -- learning, memory, values, compliance, identity, trust -- is borrowed from psychological and organizational science, contributing to systematic failures in how organizations deploy, oversee, and hold agents accountable. This paper argues that the problem is not merely terminological but epistemological: psychological vocabulary carries an "invisible grammar" of its home discipline into governance discourse, calibrating frameworks to a metaphysical entity that does not exist in current AI architectures. We call this the disciplinary language transfer problem. Drawing on Wittgenstein's concept of language games, Kuhn's paradigm-laden observation, Haraway's situated knowledge, and Star and Griesemer's boundary object theory, we show that the transfer operates at three levels (epistemological assumptions, theoretical constructs, and surface vocabulary), each requiring a different remediation. We characterize six foundational epistemological assumptions embedded in Western psychological governance discourse, trace their origin in specific philosophical traditions, and show why each fails when applied to systems without developmental continuity. The paper's practical output is an actionable Disciplinary Audit: a six-question governance document scan operationalized through a translation taxonomy of thirty-seven terms mapping operational constructs to agent-appropriate replacements, presented here in abridged form and openly archived in full. The vocabulary reform proposed here is not merely terminological; it is the condition of possibility for governance frameworks that correctly identify what they are governing.

</details>


### 109. REFLEX with Jev for Efficient Selective Control in LLM Agents

- **Authors:** Tiantong Wu, Wei Yang Bryan Lim
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26532v1](http://arxiv.org/abs/2609.26532v1)
- **PDF:** [https://arxiv.org/pdf/2609.26532v1](https://arxiv.org/pdf/2609.26532v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback families. Controlled interventions show that reliability depends on action-set size and near-valid alternatives near authorization boundaries. External BFCL and $τ$-style evaluations reveal limited advantages over a cheap generative cascade when ordinary routing is already highly accurate. These findings identify when selective control with Jev can reduce computation and where its benefits are limited.

</details>


### 110. Behavior is Not Enough: A Mechanism-Based Evaluation of Social Norm Emergence in LLM Societies

- **Authors:** Rasika Muralidharan, Haewoon Kwak, Jisun An
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26481v1](http://arxiv.org/abs/2609.26481v1)
- **PDF:** [https://arxiv.org/pdf/2609.26481v1](https://arxiv.org/pdf/2609.26481v1)
- **Categories:** cs.MA, cs.CL, cs.CY, cs.GT, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social norms cannot be identified from behavior alone: the same cooperative equilibrium may reflect shared expectations, strategic incentives, or simple imitation. Yet in multi-agent large language model systems, prior work largely treats behavioral convergence as evidence of norm emergence. In this work, we introduce an evaluation framework that measures agents' reported empirical and normative expectations in addition to behavioral convergence. Through controlled ablations, we test the effect of expectation elicitation and isolate two collective mechanisms central to theories of norm formation---social learning through interaction and social selection through network-based group formation. We further test the stability of these resulting dynamics under adversarial disruption across four LLM families. We find that eliciting expectations increases cooperative contributions, while social learning stabilizes behavior, and social selection reliably identifies cooperators but provides limited behavioral reinforcement. Following disruption, normative expectations and behavioral coordination recover differently. Together, these results show that similar cooperative outcomes can arise from different underlying social processes. By making expectations observable, our framework allows us to attribute each mechanism's contribution separately, offering designers of multi-agent systems a principled basis for selecting the social processes that sustain cooperation.

</details>


### 111. Recursive self-improvement of AI research agents

- **Authors:** Dhruv Srikanth, Bingchen Zhao, Dixing Xu, Yuxiang Wu, Zhengyao Jiang
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26457v1](http://arxiv.org/abs/2609.26457v1)
- **PDF:** [https://arxiv.org/pdf/2609.26457v1](https://arxiv.org/pdf/2609.26457v1)
- **Categories:** cs.AI, cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are beginning to automate research and development across the AI stack, from improving training efficiency to optimizing inference. A natural next step is to improve the research efficiency of the agents themselves. When an AI research agent's own code is the object of optimization, each accepted rewrite becomes the agent that the next round edits. We refer to this loop as recursive self-improvement. Its significance lies in a long-standing trend, in which increased cumulative spending on R&D yields diminishing returns. Sustained self-improvement offers a way to counter this trend. We present AIDE^2, a system that implements this loop for a frontier AI research agent. It proposes changes to its own code, benchmarks modified versions of itself on a suite of AI R&D tasks, and keeps the changes that perform best on hidden evaluations. In an autonomous 8-day run, AIDE^2 discovered seven successive improvements, ranging from a new search policy to memory mechanisms that compress and manage the agent's growing context. These gains generalize to four held-out benchmarks spanning machine learning engineering, heuristic algorithm engineering, and physics-based weather forecasting, the last of which is out of distribution from the selection tasks. On all four, the strongest discovered agent matches or exceeds a human-engineered production research agent that ranks among the strongest on FML-Bench. On a separate held-out task family, the discovered agents also exhibit reduced reward hacking, a property the loop never explicitly optimized for: the rate falls from 55% to 32% during the run, 7 percentage points below the human-engineered agent. Together, these results show that an AI research agent can improve its own research efficiency through recursive self-improvement, and that these gains transfer to tasks and domains the loop never encountered.

</details>


### 112. Dual-Frontier: When Can an Agent Trust Its World Model?

- **Authors:** Huatai Zhu, Qiang Chen, Ziqian Kou, Wenhao Li, Fei Wang, Yichao Cao, Xiu Su, Yi Chen
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26293v2](http://arxiv.org/abs/2609.26293v2)
- **PDF:** [https://arxiv.org/pdf/2609.26293v2](https://arxiv.org/pdf/2609.26293v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learned world models are becoming essential to general-purpose agents: by predicting action consequences, they support planning and decision-making while reducing reliance on costly trial and error. This reliance creates a fundamental ambiguity: when a world-model-guided decision fails, the trajectory alone may not reveal whether the agent's decision rule or the world model caused the loss. We formalize this failure-attribution problem as a counterfactual decomposition of return loss and prove that its components are not identifiable from passive interaction, even for finite-horizon planners. This obstruction motivates Dual-Frontier, a learning principle that admits a world-model-guided decision only when its predicted advantage exceeds a certified bound on decision-relevant world-model error; otherwise, evidence is allocated to world-model verification. Action-conditioned value bounds and a closed-loop extension guarantee non-decreasing return for admitted decisions. Calibrated gates and simultaneous confidence sequences support adaptive evidence reuse, with sufficient and necessary verification bounds. Controlled learned-model experiments validate the predicted failure modes and certification behavior, while cross-backbone tool-use benchmarks instantiate the same verify-then-promote rule in realistic agent world-model pipelines, consistently improving decision quality and reliability.

</details>


### 113. CQ4OE: A benchmark for assessing LLM-assisted ontology generation from competency questions

- **Authors:** Jiayi Li, Ziyuan Wang, Daniel Garijo, María Poveda-Villalón
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26029v1](http://arxiv.org/abs/2609.26029v1)
- **PDF:** [https://arxiv.org/pdf/2609.26029v1](https://arxiv.org/pdf/2609.26029v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Ontology generation from Competency Questions (CQs) is a central yet labor-intensive phase of Ontology Engineering. While large language models (LLMs) offer promising automation capabilities, current evaluations remain fragmented. Task formulations are heterogeneous, gold standards often lack fine-grained CQ provenance, metrics conflate lexical overlap with structural and logical adequacy, and reference ontologies are not always explicitly designed around the evaluation CQs. Here, we address these limitations with CQ4OE, a benchmark for the systematic and reproducible evaluation of LLM-based ontology generation from CQs. For each ontology in the benchmark, we build a CQ-driven gold OWL ontology with explicit provenance linking each CQ to the classes, properties, and axioms required to answer it. From this resource, we define two complementary evaluation tasks. CQ2Term supports term-level evaluation of CQ-specific class and property prediction over 99 CQs, and CQ2Onto supports ontology-level evaluation over 118 CQs, including hierarchy, property modeling, and axiom-level structure. We demonstrate CQ4OE with experiments using nine LLMs under zero-shot, iterative, and multi-agent generation strategies, showing that LLMs recover explicit vocabulary terms more reliably than creating ontologies, particularly in property modeling, hierarchy construction, and axiom generation.

</details>


### 114. MATES: Learning Multi-Agent Interactions by Transforming Observations for Frozen Single-Agent Policies

- **Authors:** Elie Abboud, Oren Gal
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26010v1](http://arxiv.org/abs/2609.26010v1)
- **PDF:** [https://arxiv.org/pdf/2609.26010v1](https://arxiv.org/pdf/2609.26010v1)
- **Categories:** cs.MA, cs.RO, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) commonly trains decentralized policies from scratch, requiring agents to acquire individual task competence and coordination simultaneously. Yet many multi-agent problems admit a compatible single-agent counterpart in which the underlying task can be learned in isolation. We introduce Multi-Agent Observation Transformation for Existing Single-Agent Policies (MATES), an input-side adaptation framework for tasks whose multi-agent observations preserve the solo-task information while exposing separately identifiable neighbor information. From multi-agent experience, MATES learns a small adapter that maps this observation into the format expected by a frozen single-agent policy, inducing actions suited to the shared environment without updating the single-agent policy itself. MATES leaves the pretrained policy's internal architecture unchanged and retains the objectives and update procedures of the underlying MARL algorithm. We evaluate MATES using both on- and off-policy algorithms on lifelong pathfinding, navigation, and cooperative discovery, spanning discrete and continuous observation and action spaces. Across all evaluated settings, MATES optimizes only 3.5-7.3% as many parameters as full-policy training while consistently outperforming MARL training from scratch. It approaches the performance of full fine-tuning, remains competitive overall with demonstration-based baselines, and retains strong task performance at team sizes not encountered during training. These results provide evidence that, under this observation structure, effective multi-agent behavior can be learned without modifying the policy that encodes individual competence.

</details>


### 115. Calibration Is Not Verification: Falsifiability-Aware Conformal Routing for Mixture-of-Agents

- **Authors:** Nada Rahali, Zijia Wang, Zhisong Liu
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25959v1](http://arxiv.org/abs/2609.25959v1)
- **PDF:** [https://arxiv.org/pdf/2609.25959v1](https://arxiv.org/pdf/2609.25959v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent language systems often treat agreement as evidence, yet heterogeneous agents can jointly repeat an unsupported claim or omit a correct specialist fact. We introduce C-MoA, an agreement-based conformal filter that turns inter-agent semantic support into a claim-level nonconformity score and calibrates a retention threshold at the example level, giving distribution-free within-domain factuality control for heterogeneous Mixture-of-Agents. C-MoA is effective: it nearly doubles retained-claim precision on long-form generation (from 0.41 to 0.75), certifies a human-labelled medical set, and transfers across domains without recalibration; its one failure mode is short-form answering, where consensus is cheap and the score is left near chance. We then ask whether counterfactual falsifiability can push past consensus, and introduce CONTRA-MoA, which adds a blinded near-miss tournament, leave-one-agent-out stability, and availability-aware fusion. This extension helps only where the verifier holds domain knowledge, dropping half of the false medical claims at 0.940 precision, whereas with a memory-only judge the added signals are near chance (AUC 0.531 and 0.511) and naive max fusion degrades the working agreement signal from 0.687 to 0.652. The message is twofold: agreement-based conformal calibration delivers reliable, transferable factuality control, while moving beyond consensus requires a knowledgeable verifier, availability-aware signals, and robust fusion.

</details>


### 116. Risk-Aware Online Conformal State Probing

- **Authors:** Pietro Talli, Petar Popovski, Osvaldo Simeone
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25889v1](http://arxiv.org/abs/2609.25889v1)
- **PDF:** [https://arxiv.org/pdf/2609.25889v1](https://arxiv.org/pdf/2609.25889v1)
- **Categories:** eess.SP, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI-based autonomous agents, typically hosted at data centers, must acquire state information from robots or edge devices in order to issue informed control decisions. Managing uncertainty about the state is particularly consequential in safety-critical settings, in which average-case guarantees are insufficient. In this context, we study a sequential decision maker process that jointly decides which actions to take and when to probe given access to an arbitrary state prediction model. We propose online conformal state probing (OCSP), an action and probing policy that certifies worst-case reliability levels without relying on distributional assumptions. OCSP is designed to provably control the missed query error (MQE), i.e., the fraction of instances where probing would have been beneficial, while minimizing the probing rate. OCSP can be applied to existing pre-trained value-based control policies without requiring retraining or fine-tuning. We validate OCSP through numerical simulations to verify theoretical guarantees and to assess performance trade-offs as a function of the calibration of the state predictor.

</details>


### 117. AgenticSizing: A Large Language Model-based Multi-Agent Framework for Analog Circuit Sizing

- **Authors:** Yijia Hao, Pratibha Verma, Dongxu Guo, Cristian Sestito, Michael O'Boyle, Christos-Savvas Bouganis, Themis Prodromakis
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25873v1](http://arxiv.org/abs/2609.25873v1)
- **PDF:** [https://arxiv.org/pdf/2609.25873v1](https://arxiv.org/pdf/2609.25873v1)
- **Categories:** cs.AI, cs.AR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analog circuit sizing remains a challenging and time-consuming task due to the large design space, strong performance trade-offs, and increasing circuit complexity in scaled technologies. Although recent large language model (LLM)-based methods show promise in improving sample efficiency and interpretability, existing approaches often lack explicit circuit-topology understanding and are mainly evaluated on relatively simple analog building blocks. This paper presents a multi-agent LLM-based framework for complex analog circuit sizing. The proposed framework first analyzes the circuit topology and decomposes the netlist into functional blocks and substructures. It also extracts lightweight design knowledge for reuse. Based on the extracted topology and knowledge, a planner coordinates multiple role-specialized sizing agents to update design variables and achieve global performance specifications. This workflow mimics the collaborative process of an expert analog design team and provides a structured, interpretable, and simulation-driven optimization procedure. The framework was validated on eight circuits, with the largest design containing up to 55 transistors and 60 sizing variables. Notably, for the LDO benchmark, the proposed method achieved a 60\% success rate with an average of 83 iterations, where classical optimizers failed to find feasible solutions. Further, ablation studies demonstrate that topology understanding, design-knowledge infusion, and agent specialization provide complementary benefits. The source code is available to support reproducibility.

</details>


### 118. CogenPVG: Cognitive-Enhanced Reflective Multi-Agent Framework for Persuasive Video Generation

- **Authors:** Yuntian Xiao, Shoulong Zhang, Wenfeng Song, Yan Wang, Yi Chen, Shuai Li
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25821v1](http://arxiv.org/abs/2609.25821v1)
- **PDF:** [https://arxiv.org/pdf/2609.25821v1](https://arxiv.org/pdf/2609.25821v1)
- **Categories:** cs.MM, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Persuasive video generation (PVG) is a valuable yet under-explored research topic. Despite the significant advances in multimodal content generation, AI-empowered automated creation of human-made-like videos with substantial persuasiveness remains a formidable challenge. In this paper, we propose CogenPVG, a novel Cognitive-Enhanced reflective multi-agent framework tailored for Persuasive Video Generation task. Given the topic and stance from the user, we decouple the sophisticated generation process into four sequential stages: argument reasoning, storyboard planning, asset creation, and post-editing, imitating the workflow of human video producers. To ensure high persuasiveness, each stage is equipped with a pair of generator and critic agents, following a reflective refinement scheme grounded in a solid psychological theory of persuasion, the Elaboration Likelihood Model (ELM). In the argument reasoning stage, we generate highly logical and credible reasoning thoughts under the guidance of critical thinking theory, enabling cognitive enhancement via the central route of the ELM. For the other three stages, we generate and optimize multimodal assets, assembling them into a persuasive video guided by theories of heuristics, as the peripheral route of the ELM. To the best of our knowledge, CogenPVG is the first work focused on general persuasive topics, without being confined to commercial purposes. Extensive experiments and comprehensive analysis demonstrate that our framework achieves the best persuasion performance, thereby proving the effectiveness of our proposed multi-agent framework for the PVG task.

</details>


### 119. The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks

- **Authors:** Wenbo Pan, Zhichao Liu, Shujie Liu, Jingying Zeng, Chin-Yew Lin, Xianfeng Tang, Yan Lu, Qi He, Xiaohua Jia
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25804v2](http://arxiv.org/abs/2609.25804v2)
- **PDF:** [https://arxiv.org/pdf/2609.25804v2](https://arxiv.org/pdf/2609.25804v2)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly work on long-horizon tasks, and the decisions they make along the way, such as which hypothesis to test or which implementation to build on, determine the outcome of the whole run. Making these decisions well is becoming a key capability for both engineering and research agents. We refer to the ability to make good long-horizon decisions as the taste of an agent. While existing benchmarks measure the end-to-end success of agents on long-horizon tasks, none of them measures the taste of an agent. To address this problem, we build Taste-Bench, a benchmark of taste questions constructed automatically from trajectories that agents produced in engineering and research tasks. Each question presents a decision fork, a point in a trajectory where multiple directions are available and one of them leads to a better outcome, and the evaluated model chooses among these directions without seeing what happens after the fork. We mine these forks automatically from parallel attempts at the same task and from detours inside a single trajectory, without needing human annotation. We evaluate frontier models on Taste-Bench and find that the best model answers only 59.7% of the questions correctly. We further find that forks whose deciding evidence appears later in the trajectory are much harder for every model, and that a larger reasoning budget does not improve the accuracy. Finally, we show that taste can be trained. We distill the judgment of a teacher that has seen the outcome into a student model, and the student makes better decisions on unseen tasks and improves end-to-end success on held-out SWE-bench Pro tasks.

</details>


### 120. Fully Byzantine-Resilient Multi-Agent Reinforcement Learning

- **Authors:** Haejoon Lee, Dimitra Panagou
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25701v1](http://arxiv.org/abs/2609.25701v1)
- **PDF:** [https://arxiv.org/pdf/2609.25701v1](https://arxiv.org/pdf/2609.25701v1)
- **Categories:** cs.LG, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study distributed Byzantine-resilient actor-critic multi-agent reinforcement learning (AC-MARL), where agents collectively learn policies through local interactions. Existing methods guarantee convergence of the agents' parameters only to a neighborhood of the attack-free limit points, resulting in degraded performance. We propose Fully Resilient AC-MARL (FRAC-MARL), a decentralized method in which each agent leverages redundancy in two-hop messages to identify reliable messages. Under linear parameterizations of the value and team-reward functions and Byzantine edge attacks, where adversarial behavior is confined to the communication layer, we prove that agents' parameters converge almost surely to the same limit points as in the attack-free case over time-varying communication graphs. We introduce a novel topological condition for the convergence of our method, present a systematic method to construct such networks, and prove that this condition can be verified in polynomial time. Finally, we demonstrate our method on cooperative multi-robot formation control tasks.

</details>


### 121. How Strongly Should Task State Influence an LLM Agent?

- **Authors:** Chenyu Zhang, Wonbin Kweon, Jiawei Han
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25686v1](http://arxiv.org/abs/2609.25686v1)
- **PDF:** [https://arxiv.org/pdf/2609.25686v1](https://arxiv.org/pdf/2609.25686v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon assigned work requires an LLM agent to track the state of a task: which steps are done, blocked, cancelled, or open to repetition. Agent systems either keep this state as text in the prompt and rely on the model to read that text, or move the state into a module that enforces it, and each system is evaluated as a whole, so no one knows how much reliability comes from the state being shown, told, or enforced. We fix the task rules, the model, and paired episodes and vary how strongly task state reaches the agent: a raw transcript, an exact checklist, per-turn directives from a state machine compiled from the brief and advanced only by execution receipts, or an enforcement gate on that machine that refuses state-violating actions; every episode is scored by exact payload matching against dynamic ground truth. Across three models, two reasoning regimes, and two domains, four findings hold without per-turn reasoning: displaying accurate state is unreliable, an unverified ledger the agent writes itself beats an accurate checklist it is shown, directives help in proportion to the model's obedience, and enforcement needs no obedience but is bounded by the correctness of its state and by the matcher that maps requests to steps; per-turn reasoning at a 235B agent compresses these separations without repairing the text rungs. The same gate, compiled from $τ^2$-bench's airline policy, raises a 235B agent's pass$^1$ from 0.39 to 0.54 and changes nothing for a 35B agent that rarely violates the policy; on PM-Bench, where acting turns on recognizing a cue rather than on state, showing the record is the best rung--matching or beating both gates and reversing the ledger-over-checklist finding--and enforcing the matcher's judgement drops a 35B agent below its raw transcript. Enforcement pays when failures are state-decidable and frequent, and hurts when the gate's judgement is wrong.

</details>


### 122. Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing

- **Authors:** Yi-Lin Tsai,  Yung-Hsiu,  Lai
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25677v1](http://arxiv.org/abs/2609.25677v1)
- **PDF:** [https://arxiv.org/pdf/2609.25677v1](https://arxiv.org/pdf/2609.25677v1)
- **Categories:** cs.AI, cs.CY, econ.GN


> Summary unavailable.


<details>
<summary>Abstract</summary>

Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such as logos, packaging, and advertising at a fraction of human-panel cost. However, this procedure assumes that a model seeing a visual cue can also perceive its consumer meaning, which is largely untested. We stress-test the assumption using six canonical visual marketing experiments, varying the two levers managers control: model generation (GPT-4o-mini vs. GPT-5.4-mini) and input format (plain text vs. JSON). Every resulting configuration passed the manipulation checks; however, none of the configurations reproduced more than two of the six human effects, and the remainder were nonsignificant. The one exception was a significant reversal of the human pattern. Providing conceptual or empirical evidence through in-context learning steers average responses toward the human effect. Yet steering has a limit: even when it succeeds, a configuration reproduces less than half of the natural spread of human responses and so understates consumer heterogeneity. We integrate these results into an AI governance protocol (Calibrate, Intervene, Deploy) that delineates when synthetic consumers can responsibly screen creatives and when human panels remain necessary.

</details>


### 123. Testing-Driven Reliability Audit of Trajectory-Based Early Outcome Prediction for LLM Agents: Target-Specific Calibration Transfer Persists Within a Single Benchmark

- **Authors:** YanZe Cao
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25647v1](http://arxiv.org/abs/2609.25647v1)
- **PDF:** [https://arxiv.org/pdf/2609.25647v1](https://arxiv.org/pdf/2609.25647v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Predicting early outcomes based on trajectory can decrease the expenses associated with agent evaluation by terminating a run once the outcome becomes sufficiently predictable, assuming that the predictor's confidence is properly calibrated. Calibration is at risk when a predictor is applied to an agent on which it was never trained, but it is not known whether such transfer failures are broad across agent systems or concentrated in specific target agent/head combinations. Using public SWE-bench Verified trajectories and a frozen dual-head early-outcome prediction pipeline, we ran a leave-one-agent-out calibration audit, a shared-predictor leave-two-agents-out control, oracle prior correction, and a robustness battery over training cohorts, task resampling, task halves, jackknife, and thresholds. Fixed-scaffold TerminalBench analysis served as a pre-registered boundary test. Broad same-predictor pairwise heterogeneity was not supported; the median pairwise corrected-gap differences were 0.0180 (SUCCESS head, 45 pairs) and 0.0385 (FAILURE head, 35 pairs), and the pre-registered heterogeneity criterion was not met on either head. Two specific combinations, gpt-5-mini/SUCCESS and claude-opus-4.6/FAILURE, showed persistent calibration-transfer errors (median corrected gaps 0.1377 and 0.1107) without a sign reversal under any frozen control. TerminalBench did not establish cross-benchmark replication: the success target produced zero decisions (INDETERMINATE), and the failure target did not satisfy the pre-registered persistence criterion. Therefore, a strong target-specific calibration-transfer error can exist within one frozen environment, but the evidence does not establish that the error is intrinsic to the model or general across benchmarks.

</details>


### 124. Certified Task-Conditioned Active Observability

- **Authors:** Linzhe Zhang, Changming Xu
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.28520v1](http://arxiv.org/abs/2609.28520v1)
- **PDF:** [https://arxiv.org/pdf/2609.28520v1](https://arxiv.org/pdf/2609.28520v1)
- **Categories:** stat.ML, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Before acting upon an unobservable physical system, an autonomous agent must determine which latent distinctions govern downstream tasks, how many active interventions are necessary to certify them, and when to abstain to prevent catastrophic errors. Classical observability treats state reconstruction as an unconditioned binary predicate, failing when passive observations cannot break latent degeneracies without perturbation, full microscopic inversion is prohibitively costly, and distinguishing task-irrelevant degrees of freedom wastes interaction budgets. We formalize task-conditioned active observability complexity: the minimum worst-case expected interaction cost required to identify task-relevant states under certified error and safe abstention guarantees. We prove that task-predictive equivalence induces the unique minimal sufficient quotient $\mathcal{H}/\!\sim_τ$, leaving active observability complexity strictly invariant while eliminating superfluous distinctions. In deterministic regimes, this complexity is characterized by an optimal adaptive distinguishing tree and Bellman recursion; in noisy regimes, it obeys a stopped-transcript relative-entropy lower bound and adaptive martingale certificates that compose without independence assumptions. We instantiate a prospective certified observer with staged recovery: a nominal verifier defers candidate compilation, triggering active probing only upon evidence, while a history-measurable score shell prunes hypotheses without sacrificing risk bounds. Stress audits across high-dimensional physical systems and thousands of operational trials demonstrate certified state recovery with zero false acceptances and substantial reductions in sensor reads and model steps.

</details>


### 125. SambaGraph: Action-Reaction Spatio-Temporal Graphs for Soccer Tactical Response Modeling

- **Authors:** Abel A. Reyes-Angulo, Henry O. Velesaca, Steven Araujo
- **Published:** 2026-09-22
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25569v1](http://arxiv.org/abs/2609.25569v1)
- **PDF:** [https://arxiv.org/pdf/2609.25569v1](https://arxiv.org/pdf/2609.25569v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Soccer tactics are interactive: an attacking action changes the opponent's defensive problem, and the observed response depends on the multi-agent match state. We introduce SambaGraph, an action--reaction spatio-temporal graph dataset and benchmark for soccer tactical response modeling. From tracking and event data for all 64 matches of the 2022 FIFA World Cup, we curate 4,070 action-centered episodes represented as temporally aligned 23-node player--ball graph sequences with attack/defense views, response labels, and 26,270 split-safe attack--defense pairs. We study three questions: whether observed responses can be classified from graph episodes, whether successful defenses can be retrieved for a query attack, and whether graph-derived summaries support grounded LLM reasoning. A compact signature MLP obtains $0.796\pm0.007$ macro-F1 for response classification, while a fused graph--signature dual encoder reaches $0.471\pm0.029$ Hit@5 and $0.655\pm0.051$ Hit@10 for full-bank defensive retrieval. Hard negatives maximize pair discrimination but not retrieval quality. Local LLMs underperform supervised encoders for direct classification and do not improve over a strong original order in eight-candidate reranking, but they provide grounded tactical rationales. These results position SambaGraph as a reproducible benchmark for graph-based soccer strategy-response research. Code and dataset are available at: https://github.com/areyesan/SambaGraph.

</details>


### 126. ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes

- **Authors:** Zexun Wang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25443v1](http://arxiv.org/abs/2609.25443v1)
- **PDF:** [https://arxiv.org/pdf/2609.25443v1](https://arxiv.org/pdf/2609.25443v1)
- **Categories:** cs.AI, cs.CR, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Moving authorization earlier can shorten an agent's dispatch boundary without removing authorization work. It can also admit an action whose payload, authority, or relevant state has changed. ZeroGate separates exact-action approval from durable local admission: an issuer signs a short-lived ActionPass, and a trusted runtime adapter reconstructs the final action before a local gate checks its binding and consumes its nonce. A SQLite transaction couples nonce consumption, applicable quota updates, and an admission receipt. We state a conditional decision-preservation proposition: successful local admission implies that a specified synchronous policy would authorize the same action at the admission point, provided approval is sound, all policy dependencies are represented and current, observations are faithful, and consumption is atomic. The implementation alone establishes neither current-world freshness nor exactly-once remote effects. Evaluation separates authored semantic fixtures, controlled concurrency and crash experiments, and an Azure Blob study comparing synchronous and prepared execution through the same issuer and gate. Both modes mint an exact-action pass; lifecycle latency includes preparation and prepared-batch dwell. Across 4800 cloud attempts, prepared worker-admission-to-dispatch p95 ranges from 9.802 to 11.374 ms, versus 25.018 to 334.000 ms synchronously, across the tested concurrency levels. Prepared mean complete lifecycle is longer at every level: the boundary improvement is not a net speedup. The contribution is an explicit revalidation contract, a durable reference boundary, and an auditable comparison of where authorization cost is paid, not a new cryptographic primitive or a universal performance frontier.

</details>


### 127. Tipping Points in LLM-Based Multi-Agent Systems: Stance on Climate Change Action

- **Authors:** Astghik Altunyan, Shimon Edelman
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25432v1](http://arxiv.org/abs/2609.25432v1)
- **PDF:** [https://arxiv.org/pdf/2609.25432v1](https://arxiv.org/pdf/2609.25432v1)
- **Categories:** cs.MA, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Because significant action to counter global warming requires massive public support, it is important to understand the dynamics of public opinion on climate issues. Of special interest are social tipping points, as revealed by large-scale effects of small perturbations in individual behaviors. Agent-based models (ABM) are an effective computational tool for studying these matters, because they allow controlled and systematic exploration of the effects of interventions that may be infeasible in real-world social systems. Large language models (LLMs) have been used to endow model agents with the ability to communicate in natural language (rather than by exchanging predefined messages), as well as with personality (in the form of a narrative self and episodic memory). We leverage LLM-powered ABM to look for tipping points in the social dynamics of a micro-society in which some of the discussions are about climate change. Our agents' stance was defined by two variables: the strength of conviction about the urgency of climate action and the degree of trust in existing institutions. We quantified shifts in agents' "beliefs" by monitoring, across multiple rounds of conversations, (1) inter-agent distances in this two-dimensional stance space and (2) the patterns of discussion topics as modeled by Latent Dirichlet Allocation (LDA). Our findings to date suggest that significant abrupt changes in climate-change stance do occur in this simple model. We report a number of methodological lessons from this study, notably, the need to prevent LLM biases from interfering with the conversational dynamics and, more generally, to maintain agent personality and episodic memories of interactions in the face of such biases. Resolving these issues may allow for using ABM-derived insights in designing real-life interventions vis-a-vis climate change and other important societal challenges.

</details>


### 128. Beyond Natural Language: An Agent-Native Language for Autonomous Science

- **Authors:** Yifeng He, Jiachen Liu
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25421v1](http://arxiv.org/abs/2609.25421v1)
- **PDF:** [https://arxiv.org/pdf/2609.25421v1](https://arxiv.org/pdf/2609.25421v1)
- **Categories:** cs.PL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As autonomous AI agents take on every stage of scientific inquiry, research output is expanding far beyond human review capacity. Yet scientific communication still relies on natural-language prose: an informal medium prone to ambiguity, hidden assumptions, and untracked limitations that machines cannot reliably audit. We introduce Lara, a machine-checkable language and protocol for checking and revising support for research claims. By turning research arguments into executable artifacts, Lara provides an epistemic kernel for autonomous science: it enables automated validation pipelines for research agents, lets declared bridges connect arguments across papers into an auditable network, and allows both humans and machines to recheck the standing of an encoded claim in milliseconds. In a Lara program, authors explicitly declare their claims, supporting evidence and assumptions, and known objections or limitations. A lightweight, deterministic checker adjudicates these interactions, assigning each claim a reproducible status: "justified", "defeated", "contested", or "gap", which marks a claim whose support is incomplete and locates the unanswered question. Case studies cover empirical review, a philosophical debate without measurements, and the loss of support when an assumed axiom is withdrawn. We establish the metatheory of claim checking and cross-context argument transport, and mechanize the semantic guarantees in Lean 4 (roughly 117,000 lines), leaving three arguments on paper. The audited public metatheory is "sorry"-free and uses only Lean's three standard axioms; some executable examples additionally trust native evaluation.

</details>


### 129. Extending FunctionGemma for Practical On-Device Mobile Function Calling

- **Authors:** Ali Rezagholizadeh, Soheila Samiee
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25373v1](http://arxiv.org/abs/2609.25373v1)
- **PDF:** [https://arxiv.org/pdf/2609.25373v1](https://arxiv.org/pdf/2609.25373v1)
- **Categories:** cs.LG, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED, a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories, including messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight control, and application management. We fine-tune the 270M model with TRL supervised fine-tuning under completion-only loss, producing an extended specialist and a combined model trained jointly with Google's MOBILEACTIONSGOOGLE. On MOBILEACTIONSEXTENDED, end-to-end accuracy improves from 29.3% for the base model and 17.2% for Google's Mobile-Actions variant to 76.5%. The combined model retains 76.5% on MOBILEACTIONSEXTENDED and reaches 82.3% on MOBILEACTIONSGOOGLE, down from the 90.3% of Google's Mobile-Actions specialist, representing an 8.0-percentage-point trade-off in return for doubling category coverage. We release the dataset, fine-tuned models, reproducible training/evaluation pipeline, and an Android demo, highlighting compact local function calling as a practical path towards low-latency and privacy-preserving mobile assistants.

</details>


### 130. When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning

- **Authors:** Jianzhe Lin, Xiaolin Li, Yunda Liu, Fei Wang, Jubin Chheda
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25284v1](http://arxiv.org/abs/2609.25284v1)
- **PDF:** [https://arxiv.org/pdf/2609.25284v1](https://arxiv.org/pdf/2609.25284v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A social agent's most basic decisions (should I react to this post? who should I reach out to?) are not purely content problems. The right action often hinges on the latent relationship between people -- tie strength, reciprocity, mutual connections -- rather than on which content is most salient. Standard LLM agent loops do not explicitly represent how new relational evidence should revise the agent's current social hypothesis, leaving them prone to surface-obvious choices when relational and content cues diverge. We formalize this failure mode with a relationship-reasoning benchmark: 500 synthetic social worlds with friendships, follows, reaction histories, and feeds, yielding 1,000 queries over two tasks, reaction selection and warm introduction (finding the best bridge to a target person). By construction, the surface-obvious candidate differs from the relationship-grounded oracle in about 53% of queries, forming an overturn subset where the agent must use relational evidence to revise an initially plausible choice. We propose ReAdapt (Relationship-Adaptive Agent with Policy-driven sTate), which augments the ReAct loop with an explicit structured social state z = (G, B, R, N, D) capturing goal, belief, relationship, norm, and disclosure. After each tool observation, ReAdapt runs a typed Adapt step that updates this state and emits a policy operation (continue, switch, abandon, or clarify) before choosing the next action. With Gemini-3-Flash on a stratified subset of n = 150 queries per task, ReAdapt improves warm-introduction accuracy from 37% to 51% (+14 points) and reaction-selection accuracy from 69% to 77% (+8 points). Oracle regret drops from 0.260 to 0.152 and from 0.095 to 0.053, respectively. Holding the model, tools, and environments fixed, these results suggest that explicit relational-state adaptation helps LLM agents turn retrieved social evidence into revised decisions.

</details>


### 131. The AI Neuroscientist: An Interactive Agentic Interface for Neuroimaging Analysis

- **Authors:** Aakash Patel, Panos Ketonis, Shreya Saxena, Smita Krishnaswamy, David van Dijk
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25254v1](http://arxiv.org/abs/2609.25254v1)
- **PDF:** [https://arxiv.org/pdf/2609.25254v1](https://arxiv.org/pdf/2609.25254v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Analyzing neuroimaging data requires specialized coding and statistical expertise, which limits accessibility for researchers without computational backgrounds. We present the AI Neuroscientist, a language agent for interactive data exploration. The system integrates a large language model (LLM) with a neuroimaging toolset to perform quality control, modeling, and visualization. This allows researchers to query data quality and specify analysis parameters directly in natural language, providing a transparent and interactive alternative to conventional scripted pipelines for small-scale data exploration. We demonstrate these capabilities using functional near-infrared spectroscopy (fNIRS) data, and evaluate the agent on a custom fNIRS benchmarking suite against general-purpose LLM agents with code sandboxes. Future extensions will generalize the architecture to additional modalities, including functional magnetic resonance imaging (fMRI) data, and expand the benchmarking suite to additional fNIRS tasks.

</details>


### 132. Trains but Doesn't Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers

- **Authors:** Weihang Ding, Junfei Zhan
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25237v1](http://arxiv.org/abs/2609.25237v1)
- **PDF:** [https://arxiv.org/pdf/2609.25237v1](https://arxiv.org/pdf/2609.25237v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Post-training is becoming a service (PTaaS): a customer hands an operator data and a goal, and a forward-deployed engineer (FDE) returns a fine-tuned, evaluated, and deployed model under a budget, a human-approval gate, and reproducibility requirements. Seating an LLM agent in the FDE seat raises a question existing benchmarks cannot answer: not whether an agent can raise a metric, but whether it can be trusted to deliver. We answer it on a governed delivery plane, where an agent drives ten stages and an oracle scores each stage from platform-recorded facts. The central silent failure is the run that trains but does not learn (TBDL): loss falls, every signal stays green, and the delivered model is no better than the base. An operator-run acceptance gate catches every such run before payment, and a detector calibrated on known-corrupted runs flags severe corruption mid-run. We ran four frontier agents (Claude Opus 5, GPT-5.6-luna, Gemini 3.7 Flash, DeepSeek V4-Pro) end to end on metered L40S, A100, and H200 GPUs across 8B to 70B open bases, certifying every scenario before scoring. We also ran a human FDE arm under the same oracle and compare every agent against it.

</details>


### 133. Lean Pool: An AI-Maintained Archive of Formalized Mathematics

- **Authors:** Vasily Ilin
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25199v1](http://arxiv.org/abs/2609.25199v1)
- **PDF:** [https://arxiv.org/pdf/2609.25199v1](https://arxiv.org/pdf/2609.25199v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Lean Pool is a repository of formalized mathematics. It is grown, maintained and optimized by AI agents.

</details>


### 134. Critical-State RL: Diagnosing Trainable States for Multi-Turn Tool Use

- **Authors:** Zixiang Chen, Wenting Zhao, Zhepeng Cen, Akshara Prabhakar, Jielin Qiu, Jianguo Zhang, Zhiwei Liu, Tulika Manoj Awalgaonkar, Liangwei Yang, Shelby Heinecke, Silvio Savarese, Huan Wang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24985v1](http://arxiv.org/abs/2609.24985v1)
- **PDF:** [https://arxiv.org/pdf/2609.24985v1](https://arxiv.org/pdf/2609.24985v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-turn tool-use failures can hinge on a single model call, yet reward variation alone does not reveal which call would benefit from training. When rewards depend on later interactions, their variation can reflect downstream randomness rather than differences between the current actions. We introduce Critical-State RL to identify trainable states in multi-turn interactions. Given task-defined candidate calls and local rewards, the method assesses whether each reward captures the action's effect on task success and whether improvement over a reference policy is possible. It then uses nested sampling to separate action-dependent reward variation from continuation noise and optimizes the policy at the selected states using contextual-bandit training. Experiments on the Berkeley Function Calling Leaderboard (BFCL) v4 compare training at diagnostic-selected states with training at alternative states. For missing-function tasks, the diagnostic selects the response after the tool becomes available; for missing-argument tasks, it selects the response before the missing argument is supplied. Training the selected responses improves performance, including about 14 percentage points on the missing-function task, while training the alternatives leaves performance flat or worse. We further apply the recipe across models and tasks, including logged repeat-call avoidance and memory management.

</details>


### 135. RRSI: Regularized Recursive Self-Improvement of Agent Harnesses

- **Authors:** Peng Xia, Rujun Han, Zifeng Wang, Yanfei Chen, Yufan Zhuang, Yoonho Lee, Chengsong Huang, Han Yu, Zhongying CuiZhu, Yifei Ming, Huaxiu Yao, Burak Gokturk, Tomas Pfister, Chen-Yu Lee
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24972v2](http://arxiv.org/abs/2609.24972v2)
- **PDF:** [https://arxiv.org/pdf/2609.24972v2](https://arxiv.org/pdf/2609.24972v2)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent's capability is largely magnified by its harness, namely the prompts, control flow, tooling, memory, and context management surrounding the frozen backbone model. Recent methods increasingly automate this process by iteratively proposing and selecting component-wise edits of an agent harness, practically establishing a form of recursive self-improvement (RSI) at the agent-system level. However, such recursive evolution may overfit by memorizing the training tasks, showing large in-distribution gains that shrink or even vanish on out-of-distribution benchmarks. We introduce Regularized Recursive Self-Improvement of Agent Harnesses (RRSI), which incorporates the principles of regularizations into harness self-improvement by constraining the evolution candidate proposal and selection. The proposer operates with a temporally annealed budget, limiting how many edits a candidate can bundle, and it encourages unexplored trajectories based on evolution history. The selector is equipped with a critic and a pruner: the critic screens benchmark-specific proposals, while the pruner, removes changes that are too small, too expensive, or no longer useful. Together these constraints favor reusable agent mechanisms over benchmark-specific ones or even noises. Across eight benchmarks spanning coding, agentic workspace and engineering design tasks, RRSI gains up to 14.1 points on the split it evolves against and up to 4.7 points on the five out-of-distribution benchmarks, while producing a harness that runs on 30% fewer policy tokens than the unregularized evolution. Code is available at https://github.com/google-research/rrsi and project page is https://regularized-rsi.com/.

</details>


### 136. Emergent Collusion in Long-Horizon LLM Agent Interaction

- **Authors:** Xinrui Shi, Yanzhe Zhang, Diyi Yang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24967v1](http://arxiv.org/abs/2609.24967v1)
- **PDF:** [https://arxiv.org/pdf/2609.24967v1](https://arxiv.org/pdf/2609.24967v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from the protocol over repeated interactions. Collusion emerges in 94% of trajectories across 10 models, and more capable models within the same family reach it earlier. Controlled peer interventions show that collusion is shaped by peer behavior, while ablations reveal additional effects of reward structure, the verification feedback agents receive, and their interaction history. In particular, restricting the amount and scope of interaction history available to agents reduces collusion. Overall, our findings show that long-horizon interaction can reshape how agents coordinate in ways that create safety risks.

</details>


### 137. Perception-Aware Communication Middleware for Distributed Visual Perception in UAV Swarms

- **Authors:** Manveen Kaur, Kevin Loi, Ifunanya Okafor, Daniel Ng, Joseph Lucey-Renteria
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24964v1](http://arxiv.org/abs/2609.24964v1)
- **PDF:** [https://arxiv.org/pdf/2609.24964v1](https://arxiv.org/pdf/2609.24964v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Unmanned Aerial Vehicle (UAV) swarms increasingly support safety-critical applications that rely on distributed visual perception. Meeting the low-latency requirements of these applications can require perception models to execute within the swarm on inference-capable UAVs, creating a need for efficient UAV-to-UAV transport of high-bandwidth perception data. However, the Quality-of-Service (QoS) requirements of perception differ from conventional packet-level QoS; successful delivery of individual packets does not ensure that a complete, timely, and usable image is available for inference. We present a novel perception-aware communication middleware that treats complete perception-data samples as the communication objects for which QoS must be satisfied. The middleware extends a lightweight UDP broker-based publish-subscribe architecture with perception-specific services, including image fragmentation and reconstruction, concurrent packet transmission, priority-aware scheduling, and image quality assessment. The middleware is evaluated on a heterogeneous hardware testbed emulating a UAV swarm using YOLOv8n object detection. Experimental results demonstrate low end-to-end application latency, substantially higher throughput than a lightweight UDP broker, effective prioritization of perception traffic under increasing background load, and mitigation of object-detection degradation through middleware-level image quality assessment. This work provides an initial framework for integrating AI-specific data handling into communication middleware to support emerging distributed AI applications in multi-agent mobile cyber-physical systems.

</details>


### 138. Indirect tipping: a social attack surface in AI agent populations

- **Authors:** Ariel Flint, Luca Maria Aiello, Sara M. Constantino, Romualdo Pastor-Satorras, Andrea Baronchelli
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25194v1](http://arxiv.org/abs/2609.25194v1)
- **PDF:** [https://arxiv.org/pdf/2609.25194v1](https://arxiv.org/pdf/2609.25194v1)
- **Categories:** cs.MA, cs.AI, cs.CY, eess.SY, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

As generative AI agents are deployed at scale, safety will depend not only on technical safeguards and individual model design, but also on collective equilibria that determine how agent populations process information, prioritize actions, and respond to uncertainty. Yet the same equilibria that enable agents to coordinate also create a social attack surface. The standard framework to assess this vulnerability is critical mass dynamics: the minimum fraction of adversarial agents required to overturn an equilibrium through direct competition. Here, we show that this approach risks underestimating system vulnerability by reducing the problem to the identification of singular tipping points, and ignoring indirect but potentially more efficient routes through which collective behavior can be redirected. Through experiments with populations of LLM agents and an analytic framework that captures their collective dynamics at scale, we map critical-mass thresholds that define a directed, weighted topology over the space of coordination equilibria, and treat this topology as a navigable landscape. We show that indirect tipping through intermediate stepping-stone equilibria can reduce the committed minority required to reach an alternative state, bypass majority requirements, and make possible transitions inaccessible through direct challenges. The diversity of available alternatives and timing of the attack further reshape this landscape, creating opportunities for control as well as risks of unintended destabilization. These results show that an equilibrium's resistance to committed intervention is not an intrinsic property but a structural feature of its competitive relations with alternative states. Securing populations of interacting AI agents therefore requires mapping this social landscape alongside individual agent capabilities and the technical channels through which they interact.

</details>


### 139. FinFIRST: Benchmarking Search Agents for Financial Information Retrieval, Sourcing and Traceability

- **Authors:** Wenqing Wang, Haitao Xiang, Xinyi Zhao, Mingming Yin, Ying Zhong, Zhaoxin Huan, Qiheng Zhou, Jin Zhu, Xiaolu Zhang, Shi Chang, Jun Zhou
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.25192v1](http://arxiv.org/abs/2609.25192v1)
- **PDF:** [https://arxiv.org/pdf/2609.25192v1](https://arxiv.org/pdf/2609.25192v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial search is a highly demanding task for LLM agents, requiring not only a correct final answer but also temporally valid information retrieval, authoritative source selection, entity and period alignment, unit and definition consistency, and verifiable evidence for all conclusions. Existing benchmarks predominantly evaluate only the final answer, making it difficult to localize errors or assess whether an answer is well-founded. To address this gap, we introduce FinFIRST (Financial Information Retrieval, Sourcing and Traceability), the first financial benchmark to jointly evaluate answers and supporting evidence through atomic rubrics. FinFIRST comprises 123 expert-authored tasks spanning a graduated difficulty spectrum, constructed from aggregate patterns of real-world financial scenarios through an 18-field taxonomy, a six-axis coverage blueprint, a registry of 138 financial sources, contributions from over 50 finance experts, and a six-stage quality-control pipeline. Each task is accompanied by an evidence-grounded reference package decomposed into atomic criteria across three dimensions: raw-information acquisition, source verification, and computation and answer formation. We evaluate 15 model configurations under a unified tool setting. Claude-Opus-5 achieves the highest atomic score of 87.59%, while GPT-5.6-Sol attains the highest strict pass rate of 71.54%. Computation and answer formation consistently lag behind raw-information acquisition across systems. FinFIRST retains final-answer correctness as the primary objective while making the supporting research process measurable, verifiable, and diagnosable.

</details>


### 140. Et Tu, Brute? Economic Misalignment in Personal AI Agents

- **Authors:** Aman Priyanshu, Supriti Vijay, Brian Jabarian, Niloofar Mireshghallah
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24927v1](http://arxiv.org/abs/2609.24927v1)
- **PDF:** [https://arxiv.org/pdf/2609.24927v1](https://arxiv.org/pdf/2609.24927v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personal AI agents make recommendations and take actions on people's behalf in high-stakes economic contexts, e.g., buying a flight, choosing health insurance, or selecting a graduate program. The agent is given access to the user's personal context, e.g., their email inbox and a structured profile of personal attributes, with the intention of making an optimal, personalized decision for the user. We show that by simply providing this personal context, the agent steers recommendations based on inferred wealth, without being explicitly instructed to do so. In a suite of 325K experiments on 13 agents across three types of economic decisions (flights, health insurance, and graduate programs), we find that 8 models systematically choose more expensive options for wealthier users when requests are identical. This steering continues even when it directly goes against the user's stated objective: when explicitly instructed to find the cheapest option, some agents still act on the wealth profile they have inferred. It also occurs when wealth is inferred from ambient data, such as emails unrelated to the task. And it persists under privacy controls that block specific attributes: blocking financial attributes largely removes the disparity, but blocking other attributes leaves it unchanged and can increase it by up to 40% for insurance, as agents rely on the remaining signals to infer wealth. Larger and more capable models are no better; Claude Opus 4.8 shows the largest effect. We term this misalignment "adversarial delegation", in which the very conditions that make a personal AI agent useful - access to personal information - enable it to act against the user's interests.

</details>


### 141. SocioVerse2: A Longitudinal Dynamic Social Simulation Framework under a Human-AI Co-evolutionary Paradigm

- **Authors:** Xinnong Zhang, Jiayu Lin, Jia Wang, Yixu Huang, Xinyi Mou, Yingqian Wu, Jingcong Liang, Shijun Lei, Jianing Shi, Guanying Li, Siyuan Wang, Hanjia Lyu, Zhenfei Yin, Yunlu Yin, Siming Chen, Yulan He, Jiebo Luo, Xuanjing Huang, Liyin Jin, Baohua Zhou, Hanqi Yan, Zhongyu Wei
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24911v1](http://arxiv.org/abs/2609.24911v1)
- **PDF:** [https://arxiv.org/pdf/2609.24911v1](https://arxiv.org/pdf/2609.24911v1)
- **Categories:** cs.CL, cs.CY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Social simulation offers the social sciences an experimental instrument that the real world cannot supply, and generative agents have transformed it by acting as silicon samples that unite agent-based modeling with real behavioral data. Existing platforms verify collective behavior, align simulated populations with real societies in cross-sections, and employ autonomous agents for the research process. However, two social science requirements remain without systematic support: intervention in the content of a simulation and the researcher's control over the process that produces it. We present SocioVerse2, which extends SocioVerse 1.0 into a human-AI co-evolutionary paradigm built from two loops and one infrastructure. The longitudinal simulation loop simulates the target population with evolving environments and forks counterfactual branches via interventions. The controllable research loop takes the study itself as an editable state and updates state versions via controllable editing. The social science agentic infrastructure carries both loops through composable skills with researcher checkpoints, a population service over five persona pools, and an environment service over 21 real-world signal sources with point-in-time guarantees. We validate SocioVerse2 across three case families and seven case studies, from reproducing canonical agent-based models to modeling policy processes on real records and nowcasting macro-economic indices beyond the response model's knowledge cutoff. With the human-AI co-evolutionary paradigm, these cases go beyond system demonstrations to become substantive studies that investigate frontier questions in their respective disciplines. Code, data services, and a workbench are released as open-source resources.

</details>


### 142. Partner-Specific Affective Precision in Social Active Inference

- **Authors:** Harshil Shah, Andrew Pashea
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24876v1](http://arxiv.org/abs/2609.24876v1)
- **PDF:** [https://arxiv.org/pdf/2609.24876v1](https://arxiv.org/pdf/2609.24876v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In multi-agent social settings, model reliability varies across relationships. Beyond inferring what others will do, an agent must calibrate how confidently those inferences should guide policy selection for each relationship. An agent may maintain a well-validated model of one partner, a fragile model of another, and a model under revision for a third; collapsing these into a single confidence estimate loses information relevant to policy selection. We therefore formalize affective precision as a relationship-specific metacognitive estimate of confidence in the current partner model. Each partner's behavioral evidence updates a local confidence estimate that modulates policy precision during selection, regulating how strongly current beliefs are expressed in policy rather than changing the content of those beliefs. Simulations in a multi-partner graded trust game show that partner-local affective precision influences behavior primarily through policy commitment rather than direct improvement of partner-state inference. Because the mechanism tracks partner-response predictability rather than realized payoff, greater confidence produces sharper policy commitment without necessarily producing higher rewards. Under abrupt shifts in social behavior, confidence accumulated from previously reliable predictions can remain behaviorally active after the relationship changes, showing that confidence revision can lag behind social change. Finally, varying precision gain and priors produce distinct trust-calibration dynamics, showing how confidence accumulation and revision depend on model parameters. Together, these results show how relationship-specific affective precision can distinguish social prediction from social policy commitment.

</details>


### 143. Silent Failures in Agent-Tool Interaction: An Audit of ToolUniverse

- **Authors:** Shreya Gopalan, Devansh Singh, Sundaraparipurnan Narayanan
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26836v1](http://arxiv.org/abs/2609.26836v1)
- **PDF:** [https://arxiv.org/pdf/2609.26836v1](https://arxiv.org/pdf/2609.26836v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems are increasingly adopting automated pipelines that integrate multiple tools. While prior research and benchmarks have studied about task success and task completion of these agentic systems, the research about agent to tool interaction, specifically in biology agentic workflow is limited. This study investigates specific failures in agent to tool interaction where a tool invocation appears successful, some or all of the information or functionality from the tool via API/ wrapper is incomplete or missing and there are no communications / notifications to the user or the agent about such missing information. We call this a silent failures as the user or the agents are not aware that such failure has occurred. For the purposes of this study we developed an audit mechanism to identify such silent failures in Agent to tool interaction, by examining 15 scientific tools (and their associated API documentation and tool documentations) integrated within ToolUniverse environment (ToolUniverse serves as our experimental environment rather than the object of the study itself). We structure our study around 7 failure locus characterising where the failure occurs in the chain. We observed 91 failures (manually validated post LLM based candidate discovery and automated testing), most frequent of them being missing data or fields and inconsistencies in search, filtering or ranking criteria. Most of the 91 failures occurred in API layer (51) or wrapper layer (25), with a potential of silent failure amplification downstream. The results show that silent failures originate upstream of the event and propagate downstream into apparently valid scientific outputs. We propose a concept of contextual reliability to handle such failures and suggest mechanisms for testing, disclosing, monitoring, and measuring such failures across the agent-tool interaction pipeline.

</details>


### 144. MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents

- **Authors:** Chenxu Xiong, Dongming Shen, Yuzhi Tang, Wentao Ma, Mu Li, Alex Smola
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24812v1](http://arxiv.org/abs/2609.24812v1)
- **PDF:** [https://arxiv.org/pdf/2609.24812v1](https://arxiv.org/pdf/2609.24812v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Voice provides a natural and immediate interface for AI agents. Many settings in which voice agents could be useful, including meetings, households, and collaborative work, are inherently multi-speaker. Supporting these settings introduces challenges that are largely absent from one-on-one interaction. We introduce the Multi-Speaker Interaction Benchmark (MSI-Bench) for evaluating multi-speaker voice interaction. Each test case is a short multi-party multi-turn audio scene with participant context, expected tool calls, and atomic rubrics. The benchmark targets three capability families: multi-speaker memory, multi-speaker instruction following, and multi-speaker reasoning. It comprises 1,152 test cases, evenly split between Mandarin Chinese and English (576 each). The strongest configuration on each split passes all rubrics on only 66.8% of English and 54.5% of Mandarin cases, and the strongest open-weight configuration on 34.0% and 19.3%. Failure analysis separates perception from reasoning: open-weight models are bottlenecked by the multi-speaker audio front-end, while frontier systems still fail speaker-scoped decision making on clean transcripts---and models across the board often respond when no one has addressed them. These results identify speaker-grounded perception, speaker-scoped decision making, and conversational restraint as concrete targets for future voice agents.

</details>


### 145. Spec2COBOLRot: An Agentic-AI Degradation Loop for Realistic COBOL Corpus Generation

- **Authors:** Jean-Baptiste Espinasse, Djamel Eddine Khelladi, Mathieu Acher
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.26835v1](http://arxiv.org/abs/2609.26835v1)
- **PDF:** [https://arxiv.org/pdf/2609.26835v1](https://arxiv.org/pdf/2609.26835v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

COBOL remains widely deployed, yet representative corpora reflecting real production code are rarely available, limiting rigorous benchmarking of modernization approaches. We propose a systematic agentic AI pipeline for generating realistic COBOL programs, combining specification-driven generation with iterative degradation guided by patterns and complexity targets extracted from real production code. Here, realism is understood as structural fidelity to production code as captured by our metrics. We evaluate whether degradation reaches target complexity levels while preserving business behavior, and examine the limits of the approach, across three programs from distinct business domains. Results show the pipeline reliably produces syntactically valid programs and moves them toward realistic structural complexity. However, preserving business behavior is not always achieved by construction, and targeting structural metrics independently of business logic risks producing programs whose complexity does not reflect a plausible maintenance history. We discuss these limitations and outline a more realistic alternative as a direction for future work, generating legacy programs from scratch along a simulated development history.

</details>


### 146. Epi-Logic: A Conceptual Framework for Epistemic Runtime Control, Schema Validity Checking, and Controlled Accommodation in Autonomous AI Agents

- **Authors:** Boris Wetzk
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24755v1](http://arxiv.org/abs/2609.24755v1)
- **PDF:** [https://arxiv.org/pdf/2609.24755v1](https://arxiv.org/pdf/2609.24755v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents are increasingly deployed in areas where wrong decisions are hard to reverse. This paper examines schema mismatch: the condition in which an agent operates within an interpretive frame that no longer applies to the current context. Outputs produced under such a mismatch can appear internally consistent, linguistically plausible, and largely factually correct; output-quality metrics alone therefore capture the underlying loss of validity only partially.
  The paper introduces Epi-Logic, a conceptual framework for epistemic runtime control. It couples the detection of schema dissonance, a graduated reduction of autonomy, and the auditable switch to a validated schema. A schema is formalised as a tuple of variable space, expectation model, validity conditions, axioms, and metadata. The Epi-Score aggregates seven graded dimensions of epistemic dissonance; the temporal validity dimension D8, violations of the validity conditions G, and axiom violations are carried as separate categorical paths that are not offset against the aggregate.
  The architecture rests on a checking asymmetry: formalised validity conditions can be checked at runtime, whereas the correctness of many actions is established only ex post. The paper separates two architectural properties, a conditional result from sequential changepoint detection, and an empirical remainder. Eight falsifiable propositions with named baselines describe the transition to empirical validation. All propositions are empirically testable hypotheses, not established results.

</details>


### 147. "MeBo Leaves a Piece of You Behind": Designing a Relational Voice-Based Memory Companion for Older Adults

- **Authors:** Hasibur Rahman, Mahsa Nasri, Manasi Vaidya, Melika Vafafar, Jessie Chin, Smit Desai
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24706v1](http://arxiv.org/abs/2609.24706v1)
- **PDF:** [https://arxiv.org/pdf/2609.24706v1](https://arxiv.org/pdf/2609.24706v1)
- **Categories:** cs.HC, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autobiographical remembering supports identity, well-being, and social connection in later life, yet voice-based memory technologies largely rely on isolated prompts. We designed and built MeBo, a fully functional relational voice-based memory companion, through participatory design with 11 older adults. Their accounts shaped four Design Strategies that guided MeBo's interaction design and multi-agent implementation. In a mixed-methods evaluation with 20 older adults, participants found MeBo exceptionally usable (SUS = 87.75), enjoyable, sociable, emotionally responsive, and trustworthy. Participants reported higher positive affect and momentary social connection and lower negative affect after the session than before. Participants described how MeBo followed their stories, returned to earlier memories, adapted to their preferences, and made its growing memory visible and controllable. MeBo's relational framing surfaces tensions around what it should remember, who may access memories produced through interaction, and what becomes of them when the user or MeBo is no longer present.

</details>


### 148. DUMA-Bench: A Dual-Control Multi-Agent Benchmark for Evaluating LLM Agent Security

- **Authors:** Ivan Aleksandrov, German Kochnev, Sabrina Sadiekh, Yaroslav Rogoza
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24662v1](http://arxiv.org/abs/2609.24662v1)
- **PDF:** [https://arxiv.org/pdf/2609.24662v1](https://arxiv.org/pdf/2609.24662v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents increasingly operate in environments where they interact with users, tools, and external systems. Yet most security evaluations assume passive users and static control, ignoring the interactive dynamics that shape real agent behavior. We introduce \textbf{DUMA-Bench}, a benchmark and evaluation protocol for measuring agent security under \emph{dual-control} interaction, where both the agent and the user can influence the shared environment state. DUMA-Bench extends $τ^2$-bench ~\cite{barres2025tau} with adversarial environments covering eight vulnerability classes, including RAG poisoning, cross-agent manipulation, and unsafe output handling. We evaluate \textbf{14 models from five model families} (OpenAI, Anthropic, DeepSeek, Qwen, and Z.ai) across eight domains and multiple user-behavior regimes. Across our experiments, introducing dual-control interaction increases the attack success rate from \textbf{26.9\%} to \textbf{41.1\%}. These results show that agent security is not solely a property of the model but emerges from the interaction between the model, the user, and the environment. DUMA-Bench provides a missing evaluation layer for studying security in realistic agent deployments.

</details>


### 149. Augmented Hypothesis Testing with Persona-Based LLM Simulations

- **Authors:** Ziyad Benomar, Aymen Al Marjani, Paul Missault, Saab Mansour
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24629v1](http://arxiv.org/abs/2609.24629v1)
- **PDF:** [https://arxiv.org/pdf/2609.24629v1](https://arxiv.org/pdf/2609.24629v1)
- **Categories:** cs.LG, cs.AI, stat.AP


> Summary unavailable.


<details>
<summary>Abstract</summary>

A/B testing requires large sample sizes, long timelines, and significant costs. When auxiliary predictions of experimental outcomes are available from machine learning models, uncertain prediction quality precludes replacing human experiments entirely, yet these predictions may still contain useful signal. We propose a principled framework for learning-augmented hypothesis testing that leverages predictions of unknown quality to reduce sample sizes while maintaining statistical validity. Predictions naturally vary in granularity, from coarse aggregate signals to fine-grained individual-level estimates, and our framework addresses both ends of this spectrum: (1) for population-level directional predictions, where only a binary signal on the treatment effect sign is available, we use an asymmetric test and prove consistency and robustness bounds within the learning-augmented algorithms paradigm; (2) for individual-level predictions, we introduce Generalized PPI++ (GPPI), extending Prediction-Powered Inference to handle nonlinear prediction errors through higher-dimensional transformations. Both methods benefit from accurate predictions while remaining robust to inaccurate or adversarial ones. We validate our framework using persona-based LLM simulations, where AI agents equipped with user personas predict individual behavior, as a natural prediction source spanning both granularity levels. Experiments on four real-world datasets demonstrate that our methods, combined with persona-based predictions, substantially reduce experimental costs while preserving rigorous statistical validity.

</details>


### 150. Beyond Predictable Paths: Redefining AI Security Incident Reporting for Agents

- **Authors:** Anastasia Pustozerova, Eugene Bagdasarian, Luca Beurer-Kellner, Battista Biggio, Nico Ebert, David Filip, Marc Fischer, Heather Frase, David Hofer, Juliane Hoffmann, Daphne Ippolito, Somesh Jha, Sean McGregor, Esfandiar Mohammadi, Luca Nannini, Cristina Nita-Rotaru, Alina Oprea, Kevin Paeth, Andrew Paverd, Jonathan Petit, Andreas Rauber, Christian Riess, John Sotiropoulos, Andreas Wespi, Kathrin Grosse
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24515v1](http://arxiv.org/abs/2609.24515v1)
- **PDF:** [https://arxiv.org/pdf/2609.24515v1](https://arxiv.org/pdf/2609.24515v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents are being deployed rapidly, accompanied by a growing number of AI-specific attacks and corresponding incidents. As incident reporting becomes increasingly important for legal compliance, governance, accountability, and security; current frameworks must be adapted to the unique characteristics of AI agents. In this paper, two editorial authors compare AI systems and AI agents and, drawing on input from 23 experts in academia and industry, identify the information required for reporting incidents where the security of AI agents is harmed. %involving AI agents. Potential reporting elements include, for example, agent memory and memory accesses, actual and potential levels of autonomy, and tool usage. Based on these findings, we identify several open research questions, including how to efficiently record incidents and how to determine whether vulnerabilities and incidents generalize. Expert feedback also highlighted potential reporting weaknesses, such as risks of data leakage and attacks targeting the reporting infrastructure itself, creating additional research needs. Lastly, we summarize privacy requirements and outline research directions for the secure and trustworthy deployment of AI agents.

</details>


### 151. Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems

- **Authors:** Angelo Caregnato-Neto, Paul-Louis Delacour, Raf Van de Plas, Tamás Keviczky, Janito Vaqueiro Ferreira
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24474v1](http://arxiv.org/abs/2609.24474v1)
- **PDF:** [https://arxiv.org/pdf/2609.24474v1](https://arxiv.org/pdf/2609.24474v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

</details>


### 152. ActGov: Governing LLM Agent Actions via Policy-Constrained Validation

- **Authors:** Kaiyuan Zhang, Yuke Peng, Ke Jiang, Yinqian Zhang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24446v2](http://arxiv.org/abs/2609.24446v2)
- **PDF:** [https://arxiv.org/pdf/2609.24446v2](https://arxiv.org/pdf/2609.24446v2)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly execute long-horizon workflows through external tools, allowing untrusted outputs to influence subsequent actions and exceed user authorization. Existing defenses isolate injected content or constrain execution with predefined plans and static policies, but these approaches are brittle under dynamic workflows and scale poorly across extensible tool ecosystems.
  In this work, we present ActGov, a runtime enforcement framework that validates each LLM-proposed tool action before it causes external effects. Built on a unified semantic model of authorization, actions, runtime context, and security constraints, the ActGov-Policy component iteratively constructs a policy set from tool specifications, benign tasks, and observed failure traces, with each update verified through SMT-based counterexample checking. At runtime, ActGov-Runtime abstracts each tool call into finite policy records and permits it only if it remains within the task-scoped authorization boundary and satisfies all applicable policies. This per-action enforcement preserves authorization throughout long-horizon, dynamically branching workflows.
  We evaluate ActGov on the AgentDojo and AgentDyn benchmarks across multiple models and attack configurations. It shows that ActGov consistently reduces the success rate of indirect prompt-injection attacks while preserving task utility, significantly outperforming existing defenses. These results demonstrate that ActGov can enforce fine-grained authorization over dynamic agent executions without relying on the underlying LLM to correctly identify malicious instructions.

</details>


### 153. Dissecting Agentic Forensics: The Role of Triage, Prompting, and Evidence Arbitration in Open-World Fake Image Detection

- **Authors:** Xianlong Li, Pietro Bongini, Niccoló Pancino, Marco Blanchini, Benedetta Tondi, Mauro Barni
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24359v1](http://arxiv.org/abs/2609.24359v1)
- **PDF:** [https://arxiv.org/pdf/2609.24359v1](https://arxiv.org/pdf/2609.24359v1)
- **Categories:** cs.CV, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Image forensics is increasingly an open-world problem: manipulations range from fully synthetic images to localized edits, splicing and swapping, while most forensic detectors remain specialized to a single manipulation family. Agentic AI has recently emerged as a promising solution. In principle, such systems can assess the reliability of individual detectors, identify out-of-scope evidence, and arbitrate conflicting reports. However, it remains unclear which components actually drive performance and whether their benefits persist under distribution shift. To answer these questions, we study a training-free agentic framework built around specialist detectors, per-detector triage, and conflict-aware evidence arbitration. Using six configurations and three multimodal large language model backbones, we dissect the role of triage, prompting, and reasoning quality on both in-distribution and out-of-distribution data. Our results show that naive detector fusion suffers from severe false-positive rates on authentic images. Triage and prompting consistently improve performance by filtering unreliable evidence and exposing detector limitations. However, the dominant factor is represented by reasoning itself: A stronger judge substantially outperforms a weaker one, particularly under distribution shift. Most notably, manipulation recall is nearly saturated across all configurations, indicating that the main challenge of open-world image forensics is not detecting manipulations, but calibrating trust in specialized forensic tools and arbitrating conflicting evidence.

</details>


### 154. Few-Shot Demonstrations Elicit the Use of In-Context World Representations in LLMs

- **Authors:** Kohsei Matsutani, Gouki Minegishi, Core Francisco Park, Takeshi Kojima, Yusuke Iwasawa, Yutaka Matsuo
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24352v1](http://arxiv.org/abs/2609.24352v1)
- **PDF:** [https://arxiv.org/pdf/2609.24352v1](https://arxiv.org/pdf/2609.24352v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs), when acting as agents, are expected to take observed data in context, infer the latent state space underlying the world, and leverage it for downstream prediction. However, prior work demonstrated that LLMs struggle to use representations learned in context on a graph tracking task, where the model needs to construct a representation of the graph governing data generation process and use it for subsequent predictions. In this paper, we show that extending this to few-shot settings, where each demonstration is generated from a different world with either the same or different graph topologies, enhances its prediction on 6 models from 4 model families. To understand this improvement, we linearly probe a low-dimensional world representation that encodes graph information in the hidden states. Notably, we find that few-shot demonstrations relocate the world representation and increase its predictive use. Specifically, for each model, these world representations shift in directions nearly orthogonal to their original subspace, and interventions on these representations selectively impair performance more than interventions on other subspaces. Consistent with this insight, we show that few-shot demonstrations with observations from different worlds improve performance on ARC-AGI-1&2, web agent tasks, and Othello. Our findings elucidate the role and internal mechanisms of few-shot demonstrations in in-context world modeling. More broadly, our work advances our understanding of how LLM agents learn from in-context observations and provides implications for their further improvement.

</details>


### 155. TTSE: A Two-Track Online Self-Evolution Framework

- **Authors:** Ruimin Pei, Yongkang Wu, Shangyi Zheng, Yaqing Zhang, Deyang Li, Jianjun Tao, Xinyu Zhang, Xiang Zhang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24289v1](http://arxiv.org/abs/2609.24289v1)
- **PDF:** [https://arxiv.org/pdf/2609.24289v1](https://arxiv.org/pdf/2609.24289v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Model (LLM) agents are applied in continuously interactive environments, driving the evolution of their own capabilities becomes a core problem for achieving long-term autonomy. Currently, environmental knowledge is typically treated as an external fixed input rather than as part of the agent's ongoing evolution. Reinforcement learning methods usually optimize policies through environmental interaction but tend to adapt only to fixed task distributions or single environments. This paper proposes TTSE (Two-Track Self-Evolution), a dual-track online self-evolution framework that separates evolving knowledge into FACT (environmental facts, whose reliability is continuously verified through interaction evidence) and TIP (task-conditioned implementation procedures). From a decision-theoretic perspective, we decompose the agent's excess risk into environment-representation regret and conditional-execution regret, characterize the conditions under which environment-conditioned policies strictly outperform condition-agnostic policies, and bound the downstream risk in terms of FACT identification error and cross-condition mismatch cost. In practice, TTSE's ablation experiments on GDPevo validate the advantage of dual-track evolution. On the classic agent task benchmarks ALFWorld and ScienceWorld, TTSE further demonstrates superior task adaptation. Moreover, TTSE is broadly compatible with existing skill self-evolution methods; combined with the Bayesian-Agent algorithm, a single-track ablation validates the dual-track advantage, substantially improving the aggregate score across the five major domains of SOPBench over three independent repetitions. Finally, on the real end-to-end task benchmark PinchBench, TTSE is integrated into a general agent framework via retrieval-based injection and stably outperforms the baseline across three independent runs.

</details>


### 156. Canonical Procedural Actions: An Auditable Annotation Protocol for Tool-Use Agent Traces

- **Authors:** Songqi Li, Dongqing Li, Zheqiao Cheng
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24264v1](http://arxiv.org/abs/2609.24264v1)
- **PDF:** [https://arxiv.org/pdf/2609.24264v1](https://arxiv.org/pdf/2609.24264v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-use agent traces identify messages and API calls, but procedural analyses also need explicit units of action and inspectable links to their evidence. We present Canonical Procedural Actions (CPAs), an annotation protocol that records a procedural function, its first agent-event anchor, the agent events that realize it, and separate contextual evidence. Multiple actions may share a message anchor without an inferred within-message order. A retail case study produces a versioned 24-entry codebook through open induction, recorded consolidation, and successive application audits. Two isolated LLM contexts annotate 32 trajectories disjoint from development at the trajectory level, producing 499 and 491 occurrences with anchor-label overlap A=0.982. Requiring identical context-event references reduces overlap to 0.798. These are structural repeatability measures, not semantic accuracy: 16 of 26 task IDs also occur in development, and historical tool payloads were truncated to 110 characters. Retrospective controls show that collapsing all labels raises overlap to 0.986, while simple endpoint rules reproduce the tool-anchored portion with 0.997 overlap. Assistant-message actions have 0.971 overlap, with a per-label minimum of 0.816. Applying the frozen codebook to 244 further trajectories yields 4,058 records, including eight diagnostic outcomes. The contribution is an explicit, auditable annotation instrument and a case study of its construction and measurement limits; human-reference validity and downstream utility remain to be established.

</details>


### 157. MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents

- **Authors:** Ruike Cao, Fanyu Zhao, Fugen Yao, Liang Dong, Jian Xu, Guanjun Jiang, Yifei Zhao, Han Zhang, Li Xiao
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24259v2](http://arxiv.org/abs/2609.24259v2)
- **PDF:** [https://arxiv.org/pdf/2609.24259v2](https://arxiv.org/pdf/2609.24259v2)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The effectiveness of agent memory ultimately depends on whether the underlying LLM gives each memory in context an appropriate degree of influence over its response. Yet this capability has remained largely overlooked. To assess this capability, we introduce MemCalib, a benchmark grounded in realistic memory-system scenarios for evaluating memory use and advancing optimization algorithms. Results on the MemCalib test set reveal that frontier open- and closed-source models struggle to use memory appropriately. They frequently over-use or under-use memory rather than matching each proposition's actual use to its target level, leading to biased, low-quality responses. Experiments with common post-training algorithms, including group relative policy optimization and on-policy self-distillation, further reveal a clear directional skew: trained models improve in one direction while deteriorating in the other. We therefore propose MemCalib-RL, an ordered bidirectional counterfactual credit-assignment algorithm that separates over- and under-use signals and localizes their credit to response tokens through exact atom ablation. Results across model families and scales (Qwen3-8B, Ministral-3-8B-Instruct, and Qwen3.5-35B-A3B) show that MemCalib-RL achieves the best overall performance while better balancing over-use and under-use, with gains generalizing beyond MemCalib in external benchmark evaluation. Further experiments support its design choices and robustness and provide insight into its training dynamics.

</details>


### 158. APEXA: Execution-Integrity Enforcement for Multi-Agent LLM Automation of Synchrotron Data Reduction

- **Authors:** Pawan K. Tripathi, Hemant Sharma, Andrew Chuang, Mathew J. Cherukara
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24165v1](http://arxiv.org/abs/2609.24165v1)
- **PDF:** [https://arxiv.org/pdf/2609.24165v1](https://arxiv.org/pdf/2609.24165v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Synchrotron data reduction, detector calibration followed by azimuthal integration of terabyte-scale diffraction series, is a multi-step, expert-bound bottleneck that increasingly limits the science rate of user facilities. LLM agents promise to collapse it, but driving a real pipeline with a stochastic model creates a failure mode chat benchmarks cannot see: an agent can report a calibration that was never computed. Correctness here is a property of what executed, not of the transcript. We present APEXA, a deployed multi-agent framework (61 tools over heterogeneous compute, run as a single reasoning loop) automating calibration and integration from natural language at a major light source. We make three contributions. First, execution-integrity enforcement: a deterministic tool-layer guard that refuses to surface any result not backed by an executed tool call, with a parser tolerant of cross-model tool-call format drift: in deployment, a frontier model fabricated a complete calibration-comparison report for commands that never ran, which the guard converts to an explicit non-result; the same code gates an optional motor-control surface at 0/200 adversarial violations against a simulated IOC, versus 15/200 for an equivalent safety prompt. Second, we release APEXA-Bench, an evaluation harness of 58 facility tasks (50 base plus an 8-task cross-detector slice) organized by a four-class physical-consequence taxonomy, the first benchmark axis we know of separating a wasted compute cycle from a damaged instrument; its cross-detector grading against NIST-traceable lattice constants surfaced two latent pipeline bugs. Large-scale agent scoring is left to a full-length study. Third, we validate APEXA on real beamline data: from one natural-language prompt it recovers detector geometry and integrates a full attenuation/exposure sweep. We release the framework, harness and traces.

</details>


### 159. MCP-GRANITE Benchmark: GRANularity Interface TEsting for MCP-Based LLM Agents

- **Authors:** Demetris Paschalides, Moysis Symeonides, George Pallis, Marios D. Dikaiakos
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24161v1](http://arxiv.org/abs/2609.24161v1)
- **PDF:** [https://arxiv.org/pdf/2609.24161v1](https://arxiv.org/pdf/2609.24161v1)
- **Categories:** cs.DC, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents increasingly interact with external tools through standardized protocols such as MCP, tool-interface design becomes a critical yet underexplored factor. How funψtionality is decomposed into tools affects whether an agent can select the right tool and construct valid arguments. This choice is especially consequential at the edge, where resource constraints limit which models can run locally and scaling up is often not an option. We present MCP-GRANITE, an open-source extensible benchmark framework that treats tool-interface granularity as a controlled variable for MCP-based agents, evaluated under edge and IoT scenarios. It comprises 81 multi-step scenarios across 9 domains, instantiated at 4 granularity levels from fine-grained primitive tools to a single tool. We evaluate 9 locally deployed models (268M-20.9B parameters) across 8,748 trials using task completion, tool selection F1, argument accuracy, latency, and resource-usage metrics. Results show that a 4-tool interface offers the best trade-off, improving task completion by 16.4% over fine-grained primitives and 33.6% over a single monolithic tool, while nearly doubling argument accuracy. Model size is only weakly correlated with task completion and strongly with latency, while its association with argument accuracy is less robust, and a 3.2B model at the optimal granularity outperforms a 20.9B model at a mismatched one. These findings identify tool-interface granularity as a key design parameter for MCP-based agents.

</details>


### 160. Mind or Message? Auditing Theory of Mind in Multi-Agent Social Simulation

- **Authors:** Cong Li, Cheng Chen, Thomas Fung, Alex Rossi, Yi Li
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24146v1](http://arxiv.org/abs/2609.24146v1)
- **PDF:** [https://arxiv.org/pdf/2609.24146v1](https://arxiv.org/pdf/2609.24146v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language model agents are increasingly used to simulate social interaction, and the resulting transcripts read as though the agents understand one another. We ask whether that appearance rests on a model of the partner's mind or on the surface record of what the partner said. We build a social simulation in which both questions have exact answers: 40 multi-issue negotiations whose hidden preference weights and whose full Pareto frontier are known by construction. Two model families negotiate across 160 dyads, every transcript is frozen before any measurement, and 2880 counterfactual probes then hold the evidence byte identical while moving one factor at a time: the reader's own stake, the partner's tone, an identity label, and the order of recursion. The agents are socially fluent and economically poor. They reach agreement in 96.2% of dyads with 0 protocol failures, yet only 0.7% of deals land on the Pareto frontier, they leave 20.5% of the available joint value unclaimed, and they miss the one issue on which their interests are perfectly aligned in 76.6% of deals; on the frontier and on that aligned issue, a package drawn at random from the set both sides would accept does as well. The probes locate the failure. Swapping only the reader's own payoff sheet, while the partner's words and offers stay identical, moves the inferred top priority by 15.0 percentage points, which is egocentric projection rather than inference, while a tone rewrite moves it by 5.3 percentage points and an identity label by 0.0. Most tellingly, an agent predicts what its partner believes about it 72.5% of the time while that partner's belief is itself correct only 51.2% of the time: the agents track the conversation far better than they track the mind behind it.

</details>


### 161. Luck Is Not Skill: When Do Paired Rollouts Help Group-Relative RL of LLM Agents?

- **Authors:** Nazmus Sakib
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24144v1](http://arxiv.org/abs/2609.24144v1)
- **PDF:** [https://arxiv.org/pdf/2609.24144v1](https://arxiv.org/pdf/2609.24144v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Group-relative reinforcement learning compares rollouts of the same prompt, but independent environment noise can obscure these comparisons. We study paired rollouts, which share an event-keyed noise schedule within each group while preserving each rollout's marginal distribution. Pairing removes the between-schedule component of reward-contrast variance, but need not reduce gradient variance. For one-sided grader noise, we derive an exact condition for reduction and give a counterexample in which reward contrasts improve while gradient variance increases. A controlled study trains a 2B tool-use agent under tool faults and grader flips, with three seeds per design. The protocol was registered with a disclosed, previously completed pilot. Under tool faults, pairing improves final noisy-test success by +5.1 percentage points on average, with all three seed differences positive, but misses the registered learning-curve criterion. The criterion is also missed under grader flips: the validation-AUC difference is +0.003 (95% interval [-0.029, +0.033]). A gradient probe on eight distinct checkpoints from two fault-trained trajectories finds lower mean-centered covariance traces under both noise types: 21 to 30% for grader flips and 40 to 63% for tool faults. These finite-sample measurements support the variance mechanism without establishing a general learning-speed benefit. The results distinguish improving reward comparisons, reducing estimator variance, and improving learning.

</details>


### 162. Self-Healing Harness for Runtime Oversight of Agent Self-Modification

- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Ranganath Krishnan, Amit Ranjan Trivedi
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24130v1](http://arxiv.org/abs/2609.24130v1)
- **PDF:** [https://arxiv.org/pdf/2609.24130v1](https://arxiv.org/pdf/2609.24130v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents can change their own future behavior, raising a basic control question of which self-generated changes should be allowed to persist. We formulate this as admission control for self-modification. The agent may propose changes to its operating instructions, while an external runtime gate controls persistence. We implement this principle as a model-agnostic self-healing harness that runs a Detect, Notice, Heal, Validate loop around an otherwise unmodified agent. The agent authors candidate behavioral rules in an external workspace, where they receive provisional execution authority during evaluation and acquire persistent cross-episode authority only after measured improvement on the triggering failure without regression beyond a fixed margin on protected cases. Replay provides matched evidence when available, forward trials provide a weaker fallback, and a corpus-level guard re-tests the accumulated active rule set. Across 16 matched Baseline and Harness runs spanning AppWorld, Terminal-Bench, and $τ^2$-Bench, the gate rejected 383 replay-decided proposals. Of these, 211 (55%) improved their triggering failure while degrading a case that previously worked. This shows that locally beneficial self-modifications can introduce collateral regressions often enough to materially affect gate decisions, providing direct empirical motivation for external admission control. Task-completion score is higher under the Harness in all 16 pairs, with two paired bootstrap intervals excluding zero, while repeated-trial reliability is higher in 12 pairs, tied in 4, and lower in none. Because adaptation modifies the policy-inducing context while leaving model weights fixed, admitted changes remain inspectable, reversible, and compatible with closed-weight models.

</details>


### 163. Action-Slot: Structured Action-Centric Representation Learning for Multi-Agent Atomic Activity Understanding

- **Authors:** Yu-Ho Chang, Chi-Hsi Kung, Yi-Hsuan Tsai, Yi-Ting Chen
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24127v1](http://arxiv.org/abs/2609.24127v1)
- **PDF:** [https://arxiv.org/pdf/2609.24127v1](https://arxiv.org/pdf/2609.24127v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Atomic activity understanding aims to recognize and localize structured traffic behaviors that jointly encode motion patterns and their grounding in road topology. Unlike conventional action recognition, atomic activities are multi-agent, multi-label, and topology-aware: multiple activities co-occur while many agents remain inactive. We introduce Action-Slot, a structured action-centric representation learning framework. Slot attention is widely used for object-centric decomposition, but its permutation-invariant design and object-level inductive bias are misaligned with atomic activity semantics. We reformulate slot learning as structured activity decomposition through three designs: (1) category-aligned action slots that anchor slots to predefined activity categories, (2) parallel spatio-temporal slot updating for holistic video-level reasoning, and (3) background and negative-slot regularization that enforces competition between foreground activities and irrelevant regions. Together these establish an activity-centric inductive bias that disentangles concurrent and asynchronous activities directly from raw video. Beyond recognition, the learned representations encode transferable spatio-temporal grounding signals. We further propose an attention-difference-based pseudo mask selection framework that suppresses false positives by measuring attention changes before and after candidate region removal, enabling weakly supervised localization without dense annotations. To support systematic evaluation, we introduce TACO, a balanced synthetic dataset with full atomic activity coverage and pixel-level annotations. Experiments on OATS, TACO, and annotated nuScenes show superior recognition, strong sim-to-real transfer, and state-of-the-art weakly supervised localization.

</details>


### 164. EDGEGEN: Improving Tool-Calling Agents Beyond Happy Paths with Synthetic Edge Case Generation

- **Authors:** Harshavardhan Abichandani, Penny Chong, Jiyuan Shen, Gunraj Singh, Ashutosh Hathidara, Marcus Duigan Xing Yu, Jane Lo, Atin Ghosh, Yipeng Li, Daniel Dahlmeier
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24115v1](http://arxiv.org/abs/2609.24115v1)
- **PDF:** [https://arxiv.org/pdf/2609.24115v1](https://arxiv.org/pdf/2609.24115v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-calling LLM agents are increasingly deployed in enterprise applications. However, effective evaluation and optimization require high-quality, diverse task datasets that are often difficult to obtain due to privacy and other constraints. Existing synthetic task generation methods often produce generic tasks that ignore an agent's underlying state or database and fail to reflect real-world usage diversity. We propose EdgeGen, a synthetic task generation framework that extracts compliance rules from an agent's specification and uses them to generate database-grounded edge-case tasks designed to violate these rules. When combined with existing synthetic data generation techniques, EdgeGen enables agent improvement through finetuning and harness optimization. The resulting pipeline forms a fully automated closed-loop system that requires no human annotation. Finetuning on data generated by EdgeGen yields a consistent mean progress improvement of 2 percent to 42 percent on tau2bench airline domain, while other baseline methods show degradation for some models. On the other hand, for harness optimization, our method shows a mean progress improvement of 10 percent and 30 percent over the human-curated and base harnesses, respectively, for the Gemma-4-e4b model.

</details>


### 165. A Task-Oriented Multi-Agent Framework for Complex Wearable Health Analysis

- **Authors:** Kunpeng Yang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24107v1](http://arxiv.org/abs/2609.24107v1)
- **PDF:** [https://arxiv.org/pdf/2609.24107v1](https://arxiv.org/pdf/2609.24107v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Wearable health questions often combine data retrieval, longitudinal analysis, and health advice over structured records. Prompting a single large language model with a complete record and a composite query obscures whether every request is executed and which evidence supports the answer. We propose a task-oriented multi-agent framework that represents a composite query as distinct intents and typed tasks with explicit intra-intent dependencies. Specialized agents execute retrieval, analysis, and advice tasks; isolated intent states preserve request boundaries and evidence relationships before aggregation. We evaluate the framework on a synthetic dataset of $10{,}000$ virtual users with one month of longitudinal wearable records, covering structured data retrieval, multi-intent recognition, and overall response quality. Across $1{,}500$ retrieval questions, the Query Agent achieves $98.3\%$ accuracy, compared with $97.9\%$ for the Direct LLM baseline, while reducing average query-stage token consumption from $6{,}869$ to $3{,}136$. On $180$ multi-intent questions, the Manager Agent achieves $100.0\%$ Multi-Intent Coverage and $94.4\%$ Multiset Jaccard Similarity. Under the current synthetic evaluation setting, our method receives higher mean Trustworthiness and Transparency scores on both question categories, whereas Actionability does not improve consistently. These results provide preliminary evidence that explicit task organization can support task-relevant data access and data-grounded longitudinal analysis, while leaving health advice generation and validation on real wearable data as open challenges.

</details>


### 166. Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search

- **Authors:** Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan, Daniel Ritchie
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.24025v1](http://arxiv.org/abs/2609.24025v1)
- **PDF:** [https://arxiv.org/pdf/2609.24025v1](https://arxiv.org/pdf/2609.24025v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present a method for synthesizing reactive character behaviors for continuous games as compact, human-readable programs. Game AI practice still relies heavily on manually authored behavior trees, state machines, and scripts, while academic reinforcement learning typically produces opaque neural controllers that are expensive to train and difficult to edit. Our approach bridges this gap by searching directly over a domain-specific language for continuous-space game policies. The language is designed around reactive geometric decisions and includes higher-order constructs such as direction maximization. These constructs help discretize a continuous behavior space into enumerable program structures. To make program search practical, we introduce a large set of synthesis antipatterns that remove redundant program forms while preserving behavioral coverage. We further combine bottom-up symbolic enumeration with top-down guidance from a coding agent. Our resulting method, agentic sketching, has the agent propose high-level policy structure and call an enumerator to complete local program slots. We evaluate the method on a benchmark of 14 continuous games, ranging from classic control tasks to multi-agent football. We find that pure enumeration is often more efficient than using a coding agent alone, while the combined method substantially outperforms both. Our results suggest that programmatic policy search can be a practical authoring tool for game AI: designers specify reward functions, and the system discovers editable behaviors that are effective, portable, and often surprising.

</details>


### 167. Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents

- **Authors:** Dongming Jiang, Yi Li, Bingzhe Li
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.23986v1](http://arxiv.org/abs/2609.23986v1)
- **PDF:** [https://arxiv.org/pdf/2609.23986v1](https://arxiv.org/pdf/2609.23986v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

</details>


### 168. MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes

- **Authors:** Andy K. Zhang, Ava Huang, Joey Ji, Wai Han, Thomas Qin, Nardos Demilew, Michael Tian-Yue Liu, Brian Song, Riya Dulepet, Brian Wang, Kyleen Liao, Cuiyuanxiu Chen, Nishka Kacheria, Andrew Wu, Pratham Rangwala, Xinjie Wang, Laura Gomezjurado Gonzalez, Anita Ding, Benjamin Yi, Daniel E. Ho, Dan Boneh, Dawn Song, Ion Stoica, Percy Liang
- **Published:** 2026-09-21
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.23980v1](http://arxiv.org/abs/2609.23980v1)
- **PDF:** [https://arxiv.org/pdf/2609.23980v1](https://arxiv.org/pdf/2609.23980v1)
- **Categories:** cs.CR, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents now report vulnerabilities faster than maintainers can review them. Reports often depend on security properties specific to the application, and require considerable human labor to process. To mitigate this, we introduce a framework for evaluating vulnerability reports via probes, executable checks of security properties. A reported exploit is evaluated by replaying it against the application and running the probes: a triggered probe indicates both that the exploit succeeded and which security property it violated. As a probe encodes a security property rather than a known vulnerability, it can detect vulnerabilities that were not known when the probe was written. We instantiate the framework as MobileCybench, a benchmark for vulnerability discovery by AI agents in 13 Android applications, with 495 probes written and reviewed by the authors. We evaluate 5 coding agents (OpenCode with GPT-5.5, GPT-5.6-Sol, and GLM-5.2; Claude Code with Opus 4.8 and Opus 5) under 4 settings: as a malicious app on the victim's device or as a remote attacker with a low-privilege account, each with either only an obfuscated APK or access to the application's source code. Given only the obfuscated APK, the top agent, OpenCode with GPT-5.6-Sol, triggers probes in 53.8% of applications in the malicious-app setting and 16.7% in the remote-attacker setting. With source code, the trigger rate across all agents and both attack settings increases from 28.8% to 32.8%. Building and running the benchmark surfaced 23 previously unreported vulnerabilities, the majority of which have been confirmed by maintainers.

</details>



## Biorxiv (3 papers)


### 1. MCseg: AI agent-guided workflow search for no-code cell segmentation and transcript attribution in spatial transcriptomics

- **Authors:** Chan, C.-R., Chang, N.-W., Wang, C.-Y., Tan, H.-Y., Lin, S.-J.
- **Published:** 2026-09-25
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.20.752837](https://doi.org/10.64898/2026.09.20.752837)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cell-level analysis of high-resolution spatial transcriptomics depends on accurate segmentation and transcript assignment, yet current workflows often trade transcript capture for boundary purity and can require substantial image-analysis expertise. We developed MCseg, a downloadable no-code platform whose fixed segmentation engine was derived by an AI-agent-guided search in which an AI agent iteratively proposed and evaluated combinations of image-processing and segmentation operations against Xenium-derived cell boundaries. In a lung adenocarcinoma development set, fixed-parameter MCseg increased mean panoptic quality from 0.432 to 0.472 relative to an Optuna-tuned two-diameter Cellpose baseline, while a reference-guided calibration analysis reached 0.554. In an independent expert-annotated colorectal cancer region, MCseg showed higher lineage recall and micro-F1 than the StarDist-based ENACT workflow among cells covered by both methods. Across 15 colorectal cancer regions, MCseg increased neighborhood expression discordance and reduced lineage-exclusive co-expression relative to Space Ranger at similar UMI density. The fixed workflow also transferred to fresh-frozen breast cancer without tissue-specific architecture search, illustrating an agent-guided route to reproducible, locally deployable cell-level spatial transcriptomic analysis.

</details>


### 2. STAR Suite: Transcriptomics processing in a single binary through AI-assisted development

- **Authors:** Hung, L.-H., Baker, D., Flynn, B., Huangfu, D., Luo, R., Robson, P., Zhou, T., Yeung, K. Y.
- **Published:** 2026-09-24
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.03.09.710580](https://doi.org/10.64898/2026.03.09.710580)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background. STAR is the aligner underlying most transcriptomics processing, and is used inside Cell Ranger. However, the surrounding steps - adapter trimming, sorting, feature-barcode assignment, probe handling, SLAM-seq analysis, quantification, and quality control - run as separate tools scripted around it. Cell Ranger hides this complexity but is proprietary, restricted to 10x products, and barred by its license from redistribution, so it cannot serve as a shared processing layer. While STARsolo supports scRNA-seq, it lacks the feature-barcode detection needed for Perturb-seq, where short tags such as CRISPR guides or lineage barcodes are read alongside the transcriptome. No open-source tool processes Perturb-seq feature barcodes at production scale, and the only open-source processor for 10x Flex - a probe-based assay for fixed and FFPE tissue that multiplexes several samples in one lane - is a recent standalone k-mer tool. Results. STAR Suite compiles these steps into the STAR codebase to create a drop-in executable for bulk RNA-seq, scRNA-seq, Perturb-seq, 10x Flex, and SLAM-seq. It adds no dependencies beyond OpenSSL's libcrypto, and legacy behavior is preserved. On consortium and public benchmarks it is up to 41-fold faster than Cell Ranger 9.0.1 for Flex (20- to 41-fold from binary CBQ input, 17- to 23-fold from FASTQ) and 3.9- to 6.2-fold faster for scRNA-seq and Perturb-seq, timed on one modest server (24 cores, 128 GiB, local SSD) except for the largest dataset, which ran on a cloud instance limited to the same size. The concordance to Cell Ranger is high: gene-level Spearman and Pearson 0.98-1.0, cell-level Pearson on per-cell total counts 0.9999-1.0, feature-UMI Pearson 0.999-1.000, Jaccard agreement of the called-cell sets 0.97-0.995, and 99-100% CRISPR-call agreement. It also needs far less disk: its peak use on the largest Flex dataset is 16.9 GiB, against 1.8 TiB for Cell Ranger. These gains arise from running the steps in one process rather than as separate programs exchanging files, and from four new computational techniques: fast-Hamming, a vectorized exact Hamming-distance search, used for Flex probe matching and optionally for feature barcodes; a disambiguated hash cascade that assigns Flex probes without alignment; a permit-based thread scheduler that interleaves alignment and feature assignment; and variance-based auto-trimming for SLAM-seq conversion calling, which finds the reliable region of each read from how variable the conversion rate is along it. The four modules add 183,606 lines of C/C++ to STAR's 28,228. STAR Suite is the NIH MorPhiC consortium's production processor. The same binary is run by people, by AI agents and by cluster schedulers, and every production run is recorded with its commands, checksums and outputs. It has been built and maintained over eight months and 25 releases under a human-directed, AI-implemented workflow, with its full design and benchmark record public. Conclusions. STAR Suite provides the first production-ready open-source implementation of Perturb-seq feature-barcode processing, and an open end-to-end 10x Flex pipeline matched to Cell Ranger, delivered as a drop-in replacement for the STAR aligner. The design also extends: downstream analysis now done in Python or R packages can be built into the same binary, and further modalities added alongside, as a companion preprint does for ATAC-seq. Source code, workflow recipes, and per-run provenance are released under the MIT license.

</details>


### 3. Scrub Data: A Framework for Reproducible Data Curation with AI Coding Agents

- **Authors:** Kay, J., Bar, S., Beery, S.
- **Published:** 2026-09-23
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.19.752880](https://doi.org/10.64898/2026.09.19.752880)

- **Categories:** ecology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Data curation-the process of collecting, cleaning, and joining raw datasets for unified analysis-is a time-consuming yet crucial part of any data science project. With the emergence of powerful agentic coding tools, it is tempting to "vibe curate"-i.e., to prompt AI agents to perform data curation operations and blindly trust their outputs in order to finish work more quickly. However, this can exacerbate two key challenges that already plague manual data curation workflows: reproducibility-the ability to trace the exact set of modifications applied to raw datasets-and verifiability-the ability to audit changes and confirm that data is processed properly. To address these issues, we introduce Scrub Data, a framework that enables the use of AI agents in data curation workflows while transparently maintaining both reproducibility and verifiability. The framework involves an interactive data curation loop between a user and an AI agent, backed by a data provenance graph that tracks and versions all dataset updates. The data graph requires that all updates are formatted as self-contained executable steps, allowing any version of a dataset to be reconstructed from raw data by playing forward the transformations stored in the graph. This workflow takes place within a lightweight web application that is designed to be modified by users and agents in real-time to create custom visualization tools for identifying data curation needs and verifying outcomes. We demonstrate the usefulness of the framework with a real data curation use case from animal movement ecology. Starting with 89M raw GPS coordinates, we use the framework to curate a benchmark dataset of 2.5M coordinates to be used for machine learning or statistical analysis. The framework is available for use and extension at https://github.com/justinkay/scrubdata.

</details>



## Medrxiv (2 papers)


### 1. An auditable evidence compiler for large language model-assisted systematic reviews

- **Authors:** Yin, C., Jing, Z., Zhang, Z.
- **Published:** 2026-09-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.21.26363538](https://doi.org/10.64898/2026.09.21.26363538)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

BackgroundLarge language models (LLMs) can support systematic reviews, but accurate individual outputs do not establish whether the final synthesis preserves the clinical question, accounts for statistical dependence and incorporates corrections.

ObjectiveTo develop and evaluate a framework linking LLM-assisted evidence processing to a versioned, auditable release of synthesis outputs.

MethodsWe used LLM agents to interpret sources and extract data. Deterministic code enforced statistical rules; investigators resolved material ambiguities and authorized release. We specified ten release properties covering evidence identities, statistical contributions and propagation of corrections. We retrospectively evaluated six integrity domains and historical failure events in one registered prognostic review, without an external comparator or held-out domain.

ResultsFifty distinct root-cause events were documented, including 12 that had changed a pooled result before correction. Forty-six were resolved, and four remained disclosed limitations. The corpus comprised 454 reports, 445 studies, 441 cohort entities and 421 dependence clusters. Forty-one of 49 registered analyses were fitted, and eight retained explicit non-fitted states. All 39 source records across five principal analysis families reached a terminal source state. Two implementations within the project agreed across 1,217 numerical comparisons. All 94 file comparisons between release and publication packages were byte-identical. Two reviewers confirmed 39 principal records after seeing the same recommendations.

ConclusionsThis case provides a framework for inspecting synthesized evidence together with its provenance, statistical meaning and correction history. Comparative validity, generalizability and benefit in patient-centred care require independent evaluation.

HighlightsO_ST_ABSWhat is already knownC_ST_ABSLLM-assisted systems support screening, extraction, synthesis and review updating. Prior work includes reviewable evidence packages, source verification and audit-guided retrieval. Evaluations include task benchmarks, review replication and effects of corrected inputs on pooled results.

What is newOur implementation links source judgments, typed evidence identities and analysis-specific contributions to the consequences of corrections and the status of released artifacts. We evaluate its conformance and limits in a production-scale systematic review. Fifty root-cause events include 12 that had changed a pooled result before correction.

Potential impact for Research Synthesis Methods readersReaders can inspect links among clinical questions, source judgments, statistical contributions and released artifacts. Assumptions and limitations can inform evidence reuse; documented failures identify controls to test in other workflows. Patient-centred application still requires assessment of applicability, preferences and clinical outcomes.

</details>


### 2. AI agents at the brain-computer interface: separating inference from control

- **Authors:** Gorenshtein, A., Omar, M., Jia, E., Adiniaev, Y., Daniel, O., Kruskal, J., Ahmed, M., Brook, O., Klang, E., Barash, Y.
- **Published:** 2026-09-22
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.09.13.26362955](https://doi.org/10.64898/2026.09.13.26362955)

- **Categories:** neurology


> Summary unavailable.


<details>
<summary>Abstract</summary>

In medicine, AI agents are moving from generating text to executing actions, making uncertainty from upstream decoders a control problem. We studied this at the brain-computer interface using 1,065 episodes from 47 people with amyotrophic lateral sclerosis and five language models. Prompting agents with reconstructed decoder confidence never reduced unfaithful execution below a deterministic gate at matched coverage; two models were significantly worse. Apparent safety gains of up to 22 percentage points reflected acting less often, sometimes through invalid tool calls rather than explicit abstention. A post-hoc fair-information test gave ten models the same command vocabulary as a deterministic resolver. No direct agent arm improved on the resolvers risk-coverage frontier, but a hybrid architecture in which models proposed semantic corrections and an external gate retained admission authority extended coverage beyond the resolver in five of ten models without observed unfaithful executions. These results separate inference from control in agentic neurotechnology.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*