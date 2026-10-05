# Weekly AI Agent Paper Report

**Generated:** 2026-10-05 18:24
**Period:** 2026-09-28 to 2026-10-04

## Summary

- **Total papers fetched:** 800
- **Papers matching keywords:** 178
- **Search keywords:** agentic AI, multi-agent system, multi-agent, AI agent, autonomous agent, LLM agent, agent framework, tool-use, function calling, agent orchestration, agent collaboration, reasoning agent

---


## Week-over-Week Comparison

| Metric | This Week | Last Week (2026-09-28) | Change |
|--------|-----------|-----------|--------|
| Total matched | 178 | 173 | +5 |
| arxiv | 174 | 168 | +6 |
| biorxiv | 3 | 3 | +0 |
| medrxiv | 1 | 2 | -1 |

### Notable Trends

Comparison summary unavailable.

---



## Biomedical Highlights (4 papers)

Papers from bioRxiv and medRxiv relevant to agentic AI in biomedicine.


Biomedical summary unavailable.



### 1. Synergistic Combination of Bioengineered MicroRNA and Chemotherapy Across High-Risk Neuroblastoma Subtypes

- **Authors:** Lee, Y., AlKhazal, A., Doyle, K. E., Ahn, Y.-R., Sandoval Castellanos, A. M., Tu, M.-J., Yu, A.-M., Kim, J., Brown, E. G.
- **Published:** 2026-10-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.30.755443](https://doi.org/10.64898/2026.09.30.755443)

- **Categories:** bioengineering


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite intensive treatment, high-risk neuroblastoma (HRNB) remains a leading cause of cancer-related mortality in children. Current treatment paradigms include multimodal systemic treatments and multi-agent chemotherapy, which is limited by substantial acute and long-term toxicities. Platinum-based chemotherapy is a cornerstone of this treatment but is fraught with side effects and stands to benefit from dose reduction strategies. MicroRNA (miR)-based therapeutics represent an attractive strategy to simultaneously moderate multiple oncogenic pathways, providing a potential avenue to enhance the efficacy of current treatment regimens. However, the development of miR therapeutics has largely relied on chemically synthesized ones, which are limited by issues of inconsistency and poor in vivo stability. Biologically produced, tRNA/pre-miR containing bioengineered miRs (bioRNAs) address these limitations. We investigated the therapeutic potential of bioRNA encoding miR-124 and miR-34a across molecularly distinct HRNB models and evaluated their ability to enhance cisplatin efficacy. Both bioRNAs significantly suppressed neuroblastoma cell viability in vitro, with proteomic analyses demonstrating preferential induction of neuronal differentiation by miR-124 and apoptotic signaling by miR-34a. Combining bioRNA with cisplatin produced robust synergy across multiple HRNB lines, enhancing apoptosis while simultaneously promoting differentiation-associated phenotypes. In vivo, both bioRNAs suppressed tumor growth as monotherapies, while combination with low-dose cisplatin produced the strongest responses across multiple xenograft models with different HRNB subtypes. Notably, low-dose cisplatin combined with bioRNA therapy frequently achieved tumor control comparable to, or greater than, that observed with high-dose cisplatin monotherapy while maintaining favorable tolerability. These findings establish bioRNAs as potent cisplatin sensitizers and support bioRNA-based combination therapy as a strategy for improving HRNB treatment while reducing chemotherapy-associated toxicity in children.

</details>


### 2. GroundAnnot: a closed-vocabulary contract for grounding LLM gene-set annotation in live enrichment backends

- **Authors:** Malima, M. B.
- **Published:** 2026-10-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.27.754741](https://doi.org/10.64898/2026.09.27.754741)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: LLM agents increasingly draft functional interpretations of gene lists, but can cite Gene Ontology (GO) terms that no current enrichment backend returned for that list, and can pair real GO accessions with fabricated labels. Results: We present GroundAnnot, a client for PANTHER, Enrichr, and g:Profiler that returns a closed vocabulary of GO term IDs and their backend labels, and enforces two contracts: Contract A (no ID or label outside the backend payload) and Contract B (no enrichment claim outside the backend's significant set). Across three open-weight models (Qwen2.5-7B local; Qwen3.8-27B and GPT-OSS-120B via Groq) on six curated disease gene lists, mean valid-enriched rates were 15.3%, 20.1%, and 35.1%. All unsupported IDs were real GO terms classified by QuickGO as wrong-biology, obsolete, or wrong-branch (zero fabricated accessions). A distinct failure mode emerged: for the Alzheimer's gene list, the local 7B model paired every one of its ten stable picks with a label that does not match the current GO term for that accession (10/10 mismatches), producing a coherent synaptic-signalling narrative that the IDs do not support. Mean overlap with the backends' FDR top-10 union was 0.33-0.67/10. On 50 MSigDB Hallmark gene sets, the strongest model named the defining pathway in 21/44 (47.7%) directly named cases. When an enriched shortlist was placed in the prompt, all three models complied fully (60/60 for each model; 180/180 overall), showing that a bounded vocabulary removes these output classes when the downstream agent is required to use it.

</details>


### 3. From seven combination hypotheses to one testable interaction: a gated agentic AI QSP workflow applied to healthy ageing interventions

- **Authors:** Goryanin, I., Goryanin, I., Damms, B.
- **Published:** 2026-10-01
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755460](https://doi.org/10.64898/2026.09.29.755460)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can propose combination therapies and construct supporting mechanistic models far quicker than either can be verified. To address this gap, we built a gated agentic AI quantitative systems pharmacology (Ai QSP) workflow where no hypothesis reaches a report until it clears strict hurdles for precedent, evidence, structural integrity, and release. We applied this pipeline end to end to healthy-ageing interventions. It began with a 34 state model calibrated on clinical trial data for semaglutide and metformin. Locked and evaluated against an independent post hoc DNA methylation trial, the model captured the direction of change across all 9 organ and system clocks, but the magnitude was far too small: it predicted about 0.14 years per year where 1.6 were observed, halting tier promotion. The workflow then generated seven nutritional combination hypotheses (H1H7) with 48 new parameters encoded in SBML. Identifiability analysis showed that 37 of these were completely unconstrained by available data. Trimming the model down to its lead pairing - a food derived bioactive (Agent A) plus a single-strain probiotic (Agent B left six identifiable parameters and locked the uncalibrated interaction term at zero. From this reduced model, we derived an 84 day trial with a 28 day washout, requiring 356 participants for 80% power at an interaction ratio of 0.75. A 9,000 person virtual trial confirmed the design (80.5% power), but revealed an operational trap: an assay floor at 24 mg/kg slashed power to 33% and skewed estimates toward the null, forcing a protocol-level censoring condition before study lock. Testing the pipeline across downstream operational stages and comparative oncology programmes showed that unconstrained generation consistently over-reports novelty, topological entry points can masquerade as biological mechanism, and governance gates remain vulnerable to operator overrides. Ultimately, the workflow delivered no silver bullet: its output is a single testable interaction, an assay hardened trial design, and an audit trail documenting why the other six hypotheses were shelved. Agent identities, doses, and agent specific sources are withheld in this version pending patent filing.

</details>


### 4. A ReAct Agentic AI System for Natural Language Querying and Statistical Analysis of The Cancer Genome Atlas Clinical Data

- **Authors:** Korutla, R., Amal, S.
- **Published:** 2026-09-28
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.15.26358188](https://doi.org/10.64898/2026.07.15.26358188)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Cancer Genome Atlas (TCGA) holds clinical data for over 11,000 patients across 33 cancer types, but access is hard because of complex file structures, heterogeneous formats, and the need for programming. We present an agentic system for natural language querying and statistical analysis of TCGA clinical data. The system uses a large language model (LLM) as an autonomous Reasoning and Acting (ReAct) agent that selects from eight computational tools, including data extraction, descriptive statistics, Kaplan-Meier survival analysis with log-rank tests, hypothesis testing, and verification against the curated TCGA Pan-Cancer Clinical Data Resource (CDR). The agent reasons about intermediate results, adapts its approach, and returns clinically contextualized responses with source attribution and auditable traces. We introduce TCGA-Agent-Bench, 440 queries across five difficulty tiers with ground truth from the independently curated CDR, evaluated with dual metrics for numerical accuracy and clinical completeness. The system achieves 93.4% overall accuracy, outperforming a fixed rule-based pipeline (87.1%), a single-pass LLM (81.8%), and retrieval-augmented generation (66.9% on a 50-query subset). Most of the benchmark is answerable from the CDR alone, so we locate the extraction layers value in fields the CDR lacks, such as drug treatments, TNM components, and biomarkers: on 26 queries targeting these, the full system answers 100% versus 3.8% for a CDR-only configuration. A tool-based agentic architecture enables accurate, auditable natural language analysis of clinical repositories, with value driven by tool design and recovered fields rather than model scale.

</details>


---



## Arxiv (174 papers)


### 1. FrugalEvo: Towards Cost-Aware LLM-Guided Program Evolution

- **Authors:** Hui Chen, Xuan Qi, James Xu Zhao, Zhaopeng Feng, Shilong Liu, Kuang Xu, Pang Wei Koh, Bryan Hooi
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03675v1](http://arxiv.org/abs/2610.03675v1)
- **PDF:** [https://arxiv.org/pdf/2610.03675v1](https://arxiv.org/pdf/2610.03675v1)
- **Categories:** cs.NE, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-guided evolutionary methods, such as AlphaEvolve, have emerged as powerful approaches for challenging computational optimization problems, such as circle packing. However, prior work typically optimizes performance gain over a fixed number of iterations. We argue that practical optimization should maximize gain per unit cost. To this end, we propose FrugalEvo, a cost-aware evolutionary framework where a stronger, higher-cost LLM explores solution strategies, and a cheaper LLM implements them and iteratively refines the resulting code. We also design a cache-efficient evolution process, where our harness and prompts maximize the sharing of prefixes across different evolution steps, to improve cache reuse. To measure solution quality throughout a fixed cost budget, we introduce Budget-Aware Area Under the Curve (BA-AUC), defined as the area under the best-so-far evaluation score curve over cumulative LLM cost, up to the budget. Across 10 mathematical and systems optimization tasks, FrugalEvo matches or surpasses state-of-the-art baselines, including OpenEvolve, ShinkaEvolve, AdaEvolve, and EvoX, in final solution quality and achieves higher BA-AUC on 9 tasks. It also achieves higher average performance than these baselines on 10 algorithmic optimization tasks from ALE-Bench-Lite. Notably, on circle packing, FrugalEvo achieves new state-of-the-art performance with GPT-5.6 Terra and Luna for only 1.68 USD and with GLM-5.3 and its Flash variant for only 0.55 USD, matching or surpassing all baselines, including multi-agent methods such as CORAL and SwarmResearch, which cost approximately 50 USD on average.

</details>


### 2. NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents

- **Authors:** Lijie Ding, Changwoo Do
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03631v1](http://arxiv.org/abs/2610.03631v1)
- **PDF:** [https://arxiv.org/pdf/2610.03631v1](https://arxiv.org/pdf/2610.03631v1)
- **Categories:** cs.AI, physics.ins-det


> Summary unavailable.


<details>
<summary>Abstract</summary>

Designing a scientific instrument tests whether language-model agents can do physics rather than recall it, provided the grading cannot be argued with. We introduce NeutronGym, to our knowledge the first executable environment for neutron instrument design: agents build instruments through validating tools, McStas ray-traces what they build, and a level-resolved ladder grades syntax, runtime, structure and science with no LLM judge. Procedural families supply unlimited instances of a fixed layout whose design parameters the agent must set, with held-out parameter regimes; a curated slice, McStasBench, adds 16 tasks from published instruments behind memorization probes and a sandbox. Seven models reproduce at most 7 of the 16, none retrieves a reference, and none meets an improvement target. The environment also trains. Reinforcement learning on its reward takes Qwen3-8B from 11% to 77% of held-out instances of a family whose targets come from a hidden design (69% at a second seed), past an untrained Qwen3-32B, and the recipe holds, at one seed each, on three further gated families. The analysis says what that gain is. Without the ladder's partial credit it collapses by 60 points. From reward alone the trained model reaches what a classical optimizer reaches, at the agent's simulation budget, only when handed the closed-form physics (77% against 81%, a gap that does not separate at this size), while frontier models still solve 98-99%. Getting a trustworthy result meant failing four task designs that no-model baselines could solve, and we release the probes that found them.

</details>


### 3. HazardWeaver: Scientific Route Selection for Hazard Analysis Agents

- **Authors:** Wangshu Zhu, Xueqi Cheng, Liang Wu, Yushun Dong
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03591v1](http://arxiv.org/abs/2610.03591v1)
- **PDF:** [https://arxiv.org/pdf/2610.03591v1](https://arxiv.org/pdf/2610.03591v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Understanding and assessing natural hazards is essential for disaster preparedness and risk reduction. Recent advances in large language models have spurred growing interest in AI agents for hazard analysis, particularly their ability to integrate scientific data, models, and tools into automated workflows. However, effective automation requires agents to determine which scientific methods are appropriate for a given event and executable with the available data and tools. As new evidence and execution results become available, these conditions can change, requiring agents to reconsider their choices. We formulate this problem as state-dependent scientific route selection and introduce HazardWeaver. Specifically, HazardWeaver first leverages the Hazard Knowledge Compiler to extract evidence-linked conditions governing scientific applicability, then its Hazard Capability Graph represents executable scientific capabilities and checks compatibility between their inputs and outputs. Using these complementary representations, the Hazard Weaver Agent component selects applicable and executable routes, carries out their workflows, and revises its decisions as the analysis state changes. To evaluate both the scientific outputs and the decisions that produce them, we introduce the Hazard Weaver Benchmark, comprising 141 instances across seven single-hazard domains and four multi-hazard interaction classes. The benchmark accommodates multiple valid scientific routes and evaluates output correctness, route validity, and justified abstention. Extensive experiments on this benchmark show that HazardWeaver outperforms existing agent systems, with the largest gains on tasks with multiple eligible scientific routes. Our code is publicly available at https://github.com/LabRAI/HazardWeaver.

</details>


### 4. Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows

- **Authors:** Jermyn Zhen Yong Bek, Zhuang Qiang Bok, Zhongtian Sun
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03564v1](http://arxiv.org/abs/2610.03564v1)
- **PDF:** [https://arxiv.org/pdf/2610.03564v1](https://arxiv.org/pdf/2610.03564v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Financial AI agents must do more than retrieve facts: investment workflows require correct quantitative execution, reliable use of procedural resources, and auditable structured outputs. We introduce FinSkillBench, an evaluation suite of 2,603 point in time episodes across 12 subtasks in portfolio construction, risk management, and fundamental analysis, with hidden regenerable ground truth and task specific deterministic verifiers. Executing 17,820 episodes across 9 models and 3 resource conditions, the paired analysis across 8 models shows that curated skill packages raise mean scores by +16.2 points (0.366 to 0.528), whereas skills generated within a single episode add only +0.5 points while consuming more tokens and turns. We then decompose the curated premium by granting human authored procedural documents and executable domain tools separately: documents alone add +5.6 points, tools alone add +19.5 points, and their combination is subadditive. The premium is strongly workflow dependent: executable tools dominate numerically intensive workflows, documentation matters more when procedural or output schema guidance is the bottleneck, and interpretive tasks benefit from both. The effects are sign stable across 10 scoring variants and cluster bootstrap analyses, and an independently implemented second harness reproduces the directional pattern while showing that effect magnitudes depend on how tools and data are exposed. Overall, a measured "skill premium" is a property of the full model, resource, and harness system rather than of the underlying model alone.

</details>


### 5. Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents

- **Authors:** Zhuowen Liu
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03448v1](http://arxiv.org/abs/2610.03448v1)
- **PDF:** [https://arxiv.org/pdf/2610.03448v1](https://arxiv.org/pdf/2610.03448v1)
- **Categories:** cs.CR, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly screen tool outputs with small prompt-injection detectors, and teams choose among detectors by their scores on public benchmarks. We ask whether those scores predict how a detector behaves inside an agent. We replay the ground-truth tool calls of two agent benchmarks, AgentDojo and tau-bench, without an LLM to obtain tool outputs that are benign by construction, label injected outputs by differential replay, and evaluate fifteen detectors, including Meta's Prompt Guard 2, and two task-aware LLM judges on these outputs and on the BIPIA benchmark. Detection rankings transfer poorly between benchmarks: the best detector on BIPIA catches 2% of AgentDojo injections at a 1% false-positive rate, and a detector that catches 72% of AgentDojo injections catches 15% on tau-bench. False-positive rates on tool outputs, which range from none to over 90%, do transfer between the two agent benchmarks. Where training data is public, the form of the training inputs explains the results. The BIPIA leader was trained on full BIPIA inputs, but having seen InjecAgent's attack strings as short prompts does not help it find them inside tool outputs; the best detector on both agent benchmarks shares no data with any benchmark and was trained on agent-style inputs. Evaluations meant to inform deployment should use the agent's own tool outputs, report detection at a low false-positive rate, and audit what the detector was trained on.

</details>


### 6. EdgeAgent: Orchestrating On-Device LLM inference for End-User Multi-Agent Systems on CPU-GPU Unified Memory Architectures

- **Authors:** Yuhai Long, Yuanxin Wei, Kai Wu, Jinhui Wei, Dan Huang, Jiangsu Du
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03394v1](http://arxiv.org/abs/2610.03394v1)
- **PDF:** [https://arxiv.org/pdf/2610.03394v1](https://arxiv.org/pdf/2610.03394v1)
- **Categories:** cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Emerging multi-agent LLMs demand privacy-preserving edge deployment, yet current inference systems struggle with these collaborative workflows. Specifically, the memory-bound decode phase causes severe bus contention on unified memory architectures (UMA), paralyzing naive CPU-GPU co-execution. Furthermore, speculative decoding in multi-agent workloads faces extreme variance in drafting difficulty, alternating between complex reasoning and predictable structured generation. Compounded by frequent tool-induced stalls, this highly fragmented execution severely underutilizes hardware and defeats traditional static batching.
  We present EdgeAgent, a cross-layer inference system explicitly co-designed for edge UMA and multi-agent workloads. At the micro-architectural level, it bypasses rigid graph-compiler constraints to enable zero-copy UMA-aware tensor parallelism, utilizing asymmetric memory layouts to fully saturate both CPU and GPU compute units. At the scheduling level, it dynamically allocates draft budgets based on real-time sequence predictability to bound bandwidth waste. Concurrently, an asynchronous suspend-and-yield mechanism actively evicts stalled agents, ensuring continuous hardware saturation during unpredictable tool invocations.
  Extensive evaluations on an Apple M4 SoC demonstrate that the UMA-aware execution alone contributes a 1.29x speedup over batched speculative decoding. Adding the agent-aware scheduling lifts the full EdgeAgent system to a 1.77x speedup under extreme tool-use latencies.

</details>


### 7. Lightweight, Rubric-Guided Trajectory Evaluation for Production AI Agents

- **Authors:** Linh-An Phan, MingXue Wang, Guangyu Wu, Feng Pan, Zhaoyu Pang, Yanbin Zhang
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03315v1](http://arxiv.org/abs/2610.03315v1)
- **PDF:** [https://arxiv.org/pdf/2610.03315v1](https://arxiv.org/pdf/2610.03315v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Trajectory evaluation is essential for improving the reliability of LLM-based agents, but production use makes it expensive to run repeatedly. Modern agents generate long traces containing tool calls, observations, retries, and external outputs, while not all raw tokens are equally useful for diagnosis. We present \textit{LiteTrajEval}, a lightweight architecture for budget-bounded trajectory evaluation. LiteTrajEval derives compact domain-specific rule profiles offline, then preprocesses each trajectory online, marks heuristic failure signals, serializes it under a fixed global budget, and invokes a single rubric-guided LLM judge to produce structured diagnostic reports. Evaluated on public Magentic-One-style and $τ$-bench-style trajectory datasets, LiteTrajEval improves failure-localization alignment with human annotations by roughly 20--35 percentage points on Magentic-One and up to 23 percentage points on $τ$-retail compared with AgentRx, while reducing cost by about 6$\times$ and evaluation time by more than 8$\times$. This solution has also been deployed in our enterprise agentic platform.

</details>


### 8. D2K-Bench: Can LLM Agents Turn Expert Designs into Efficient GPU Kernels?

- **Authors:** Daifeng Li, Huiqiang Jiang, Chengruidong Zhang, Wei Wu, Xudong Guo, Jianhong Tu, Jianwei Zhang, Binhang Yuan, Dayiheng Liu
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03226v1](http://arxiv.org/abs/2610.03226v1)
- **PDF:** [https://arxiv.org/pdf/2610.03226v1](https://arxiv.org/pdf/2610.03226v1)
- **Categories:** cs.LG, cs.AI, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

GPU kernels generated by large language model (LLM) agents can remain less efficient than expert implementations, but runtime alone does not reveal how the gap relates to design discovery and implementation. We introduce D2K-Bench, a diagnostic benchmark of 26 tasks and 85 workloads that measures how effectively agents translate expert design guidance into efficient GPU kernels. The guidance covers L1: high-level algorithmic insights, L2: dataflow design, and L3: low-level optimization tricks, including dependencies among these levels. Pairwise runs with and without guidance share task descriptions, workloads, tools, hardware, and a 350-turn budget. Complementary assessments examine independently proposed designs and the design properties implemented in generated code. Across five models on NVIDIA B200 GPUs, guidance raises correctness over 130 model-task pairs from 93.1% to 98.5% and increases the Performance Score over all 26 tasks from 1.46 to 1.95. For the three frontier models with correct submissions on all 26 tasks in both runs (GPT-6-Astra, Claude-Opus-4.8, and GPT-5.6-Sol), geometric mean speedup increases from $1.69\times$ to $2.49\times$. Across all five models, the mean combined implementation score increases from 57 to 70 out of 100. These results show the value of expert design guidance while identifying design properties that remain unimplemented.

</details>


### 9. AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning

- **Authors:** Xin Wang, Wenhao Wu, Menghao Zhang, Zhi Wang, Kun Shao, Jian Luan
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03223v1](http://arxiv.org/abs/2610.03223v1)
- **PDF:** [https://arxiv.org/pdf/2610.03223v1](https://arxiv.org/pdf/2610.03223v1)
- **Categories:** cs.LG, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon LLM agents are typically trained with sparse outcome rewards, making trajectory-level objectives too coarse to distinguish the contribution of individual decisions. Step-level credit assignment provides finer-grained supervision, but its estimates can be unreliable because observed returns also depend on subsequent actions, environment transitions, and trajectory length. We propose AdaStep, an Adaptive Step-credit weighting method that controls how strongly each group-derived local advantage modifies the trajectory-level signal. We formulate this weighting as a mean-squared-error estimation problem for the latent step advantage and, under an explicit conditional sampling assumption, derive an optimal per-state shrinkage coefficient. The coefficient admits a signal-to-total-variance interpretation: it preserves local credit when return variation is attributable to the selected action and suppresses it when variation is dominated by downstream randomness. AdaStep requires only lightweight scalar computation, with no critic, additional rollouts, or extra model inference. Experiments with three model backbones on ALFWorld, WebShop, and ScienceWorld show consistent improvements over baselines at low computational cost.

</details>


### 10. Toward SLM-based agentic task-tool intent matching

- **Authors:** Chiara Troiani, Arash Salarian, Majed El Helou, Benjamin Ryder, Jean Diaconu, Hervé Muyal, Marcelo Yannuzzi
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03213v1](http://arxiv.org/abs/2610.03213v1)
- **PDF:** [https://arxiv.org/pdf/2610.03213v1](https://arxiv.org/pdf/2610.03213v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-equipped AI agents use tool calls to access data and act on external systems. Horizontal growth of agentic systems increases the number of these interactions, and further motivates the need for automated, per-call oversight that can operate at low latency and/or on-prem. Conventional authorization schemes can determine whether an agent is allowed to invoke a tool, but cannot assess the agent's underlying cognition, specifically, whether the tool selection represents a logical, relevant step toward satisfying the intent of the task or not. Consequently, an allowed call may still deviate from the task's intent: a rogue agent might deviate the calls or nudge other agents to make a combination of calls that would not align with the intent of the task. Therefore, every call needs to be verified. In this study we investigate the applicability of Small Language Models (SLMs) to this purpose: an SLM functions as a task-tool relevance classifier that evaluates every selected tool independently against the assigned task and returns a relevance signal for downstream enforcement. Equipped with a novel dataset with multi-tool tasks whose required tools span distinct Model Context Protocol (MCP) servers, we used prompt-optimization, supervised fine-tuning, and reinforcement learning through GRPO to optimize and specialize SLMs.

</details>


### 11. Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It

- **Authors:** Jonghyun Song, Haewon Park, Jeonghoon Shim, Woojung Song, Yohan Jo
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03195v1](http://arxiv.org/abs/2610.03195v1)
- **PDF:** [https://arxiv.org/pdf/2610.03195v1](https://arxiv.org/pdf/2610.03195v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents decide on users' behalf which product to buy, which hotel to book, or which paper to cite, a preference for items from certain sources (the sites or services they come from) shapes what users receive and which sources are selected. We study source preference in end-to-end search with 12 agent models across three domains. Comparing items from different sources that satisfy the same requirements at the same position, we find that each model prefers some sources and avoids others in every domain, largely agreeing on which. This preference can outweigh how well items satisfy the request: an item satisfying one requirement fewer is selected about two-thirds of the time when it comes from a preferred source and the better one from a dispreferred source, but almost never in the reverse case. The information identifying an item's source affects selection by itself: hiding it weakens the preference, and relabeling an item with a preferred source raises its selection rate. We test two routes to this preference: training that rewards better items can make a source a shortcut for requirement satisfaction, and missing information can trigger preconceptions about the source. Supplying missing information or a prompt countering these preconceptions reduces source preference.

</details>


### 12. Ask, Relax, or Act? Evaluating Actionable Indeterminacy in LLM Preference Reasoning

- **Authors:** Ang Li, Yue Lin, Feifei Kou, Zhan Su, Prayag Tiwari, Wenhao Li, Shuhui Zhu, Hongyuan Zha, Baoxiang Wang
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03102v1](http://arxiv.org/abs/2610.03102v1)
- **PDF:** [https://arxiv.org/pdf/2610.03102v1](https://arxiv.org/pdf/2610.03102v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

An LLM agent can recognize uncertainty yet still choose the wrong next step: asking when action is already justified, or seeking clarification when the constraints must change. We formalize actionable indeterminacy: act when an accepted action is shared across all admissible preferences or objectives, clarify when each possibility is feasible but no action is shared, and propose a minimum-cost permitted constraint repair when the request is infeasible. We construct a solver-grounded benchmark spanning object allocation, meeting scheduling, apartment choice, and stable matching. Matched pairs retain the same source while changing whether intervention is necessary, and evaluation separates decision correctness, matched-pair reliability, and fully correct responses. Our findings reveal a recurring difficulty in recognizing when intervention is unnecessary: models can identify situations requiring clarification or repair yet still intervene when a justified action already exists. Correct decision labels also fail to guarantee usable actions, questions, or repairs. Crucially, response requirements shape not only how decisions are expressed but also which decisions are made. Making the required content explicit substantially improves fully correct responses and can change intervention decisions, even when outputs are already parseable. These findings highlight that reliable agency requires more than recognizing uncertainty: it requires intervening only when necessary and translating the chosen next step into a verifiable response.

</details>


### 13. Peer Influence across Heterogeneous AI Models

- **Authors:** Frida Nøhr Laustsen, Marie Haahr Petersen, Victoria Popa, Ariel Flint, Romualdo Pastor-Satorras, Andrea Baronchelli, Luca Maria Aiello
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03095v1](http://arxiv.org/abs/2610.03095v1)
- **PDF:** [https://arxiv.org/pdf/2610.03095v1](https://arxiv.org/pdf/2610.03095v1)
- **Categories:** cs.AI, cs.CL, cs.CY, physics.soc-ph


> Summary unavailable.


<details>
<summary>Abstract</summary>

When two AI agents disagree, who persuades whom? As multi-agent systems increasingly combine language models of different families and sizes, the answer can determine which judgments survive interaction. Measuring persuasion as the probabilistic shift in an agent's decision after a single exchange with a dissenting peer, we test seven open-weight models across three language understanding tasks. We find that persuasion is strong: when models disagree, receivers often abandon their initial judgment after seeing a peer's answer and explanation. Surprisingly, however, neither standalone certainty nor model scale reliably predicts persuasion dynamics. Models producing almost perfectly consistent decisions in isolation can be among the most susceptible to persuasion, and small models can match larger ones as persuaders and resist their influence just as effectively. Furthermore, we show that the size of the shift depends more on the susceptibility of the listener than on the persuasiveness of the speaker. Persuasion patterns are therefore specific to each model pairing, with heterogeneity amplifying persuasion in some combinations and suppressing it in others, allowing a dissenting agent running a small model to overturn the judgments of a much larger one. These findings show that the behavior of interacting models cannot be inferred from their individual properties but must be evaluated in the combinations in which they will operate.

</details>


### 14. When Numbers Start Talking: Numerical Signalling and Strategic Behaviour Among LLMs

- **Authors:** Alessio Buscemi, Daniele Proverbio, Alessandro Di Stefano, The Anh Han, German Castignani, Pietro Liò
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03033v1](http://arxiv.org/abs/2610.03033v1)
- **PDF:** [https://arxiv.org/pdf/2610.03033v1](https://arxiv.org/pdf/2610.03033v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents increasingly operate in multi-agent systems (MAS) characterised by strategic interaction. However, little is known about whether, and to what extent, different types of messages affect the outcomes of strategic games. By investigating AI agents based on four popular LLMs, playing four games with different cooperation equilibria, we study whether messages of different kinds (natural language, numerical signals, or random sequences) significantly modify the levels of cooperation in each game, also depending on the agents' assigned personalities. We observe that structured messages alter the final payoffs for most games and LLMs, but without a predictable pattern; this challenges the assumption that AI agents can converge to stable equilibria regardless of additional capabilities. Moreover, we observe that agent-generated numerical messages depart from randomness, most strongly and consistently when agents are explicitly instructed to communicate; however, they introduce an additional interpretability challenge, as their symbol distributions are mostly associated with the payoff structure and typically become more concentrated with repetition, but are overall difficult for humans to interpret. Monitoring for coordination of AI agents through restricted channels should thus prioritise message-level fingerprints, which generalise across models, over behavioural decisions, which do not.

</details>


### 15. Beyond Predefined Sinks: Security-Aware Dependency Analysis for LLM Agents

- **Authors:** Hang Cui
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03014v1](http://arxiv.org/abs/2610.03014v1)
- **PDF:** [https://arxiv.org/pdf/2610.03014v1](https://arxiv.org/pdf/2610.03014v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM)-based agents increasingly connect model-generated decisions to security-sensitive software capabilities such as command execution, filesystem access, network communication, browser control, and external tools. Existing analyses often use predefined sensitive operations as anchors, but operation identity alone is insufficient to determine security implications.
  We present AgentSecGraph, a security-aware static analysis framework that constructs a candidate-centered Security-Aware Agent Dependency Graph (Security-ADG) for each security-sensitive operation. It augments operation identity with agent relevance, source and dependency evidence, trust-boundary context, guard evidence, and external-effect semantics.
  We further introduce AgentSecBench, a corpus of 67 real-world LLM-agent repositories spanning 11 ecosystems and 37,542 source files. The current analyzer identifies 23,866 static security-sensitive operation candidates across 65 repositories and emits one Security-ADG artifact per candidate. Corpus-wide analysis recovers source-to-operation dependency evidence for 9,821 candidates (41.15%) and potential guard evidence for 3,075 (12.88%), completing in 50.8 minutes.
  Using a separate reproduction-backed evaluation layer, we establish 22 security-sensitive behaviors across 13 repositories: one confirmed vulnerability, one pending disclosure candidate, and 20 guarded behaviors. In nine held-out cases, Security-ADG preserves 91.1% of the reference context and all five observed guards, compared with 20.0% for a sink-only view and 40.0% for a simplified ADG. These results show that security-aware dependency and contextual evidence enable distinctions that cannot be recovered from sensitive-operation identity alone.

</details>


### 16. Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows

- **Authors:** Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sözer, Ratnadira Widyasari, Hui Song
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.03010v1](http://arxiv.org/abs/2610.03010v1)
- **PDF:** [https://arxiv.org/pdf/2610.03010v1](https://arxiv.org/pdf/2610.03010v1)
- **Categories:** cs.SE, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly used in software engineering, including agentic systems that coordinate multiple agents, but impose higher computational and environmental costs. In this paper, we present a comprehensive empirical study of agentic LLM systems across five software engineering tasks: code generation, technical debt identification, code vulnerability detection, log parsing, and log analysis. For each task, we compare LLM configurations that range from a non-agentic single-query baseline to multi-agent workflows, using six open-weight LLMs, two prompt strategies, and three hardware platforms. We assess each configuration in terms of accuracy, inference latency, and energy consumption. Our results reveal substantial trade-offs between agentic complexity and energy efficiency: multi-agent designs consume on average 6.36$\times$ as much energy and run 6.07$\times$ as long as the non-agentic baseline, with worst-case slowdowns of up to 160$\times$ for individual task--hardware pairs. Accuracy gains from additional agents are limited and task-specific: multi-agent improves average vulnerability-detection accuracy, but lightweight non-agentic and single-agent configurations still dominate the Pareto front, accounting for 59 of 66 Pareto-optimal configurations. Model and prompt choice act as task-specific levers whose effective direction varies between tasks rather than as global defaults. We translate these findings into design guidelines for sustainable, task-aware LLM-based development tools.

</details>


### 17. Sentry: Learning to Recover from LLM Agent Failures at Test Time

- **Authors:** Changxiu Ji, Amy Lu, Qizheng Zhang, Kunle Olukotun
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02994v1](http://arxiv.org/abs/2610.02994v1)
- **PDF:** [https://arxiv.org/pdf/2610.02994v1](https://arxiv.org/pdf/2610.02994v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often fail mid-task due to invalid tool calls, repeated actions, or poorly grounded reasoning, and learning from these failures is a path to reliability. We find that how failure knowledge reaches the agent matters as much as what it contains. Failure lessons are conditional: kept in the agent's context, they misfire when their failure is absent, and removing them from an evolving playbook improves performance. Runtime interventions, in contrast, act only when a failure occurs but do not learn from their repairs. We argue that failure knowledge is conditional knowledge and should be conditionally exposed, and instantiate this principle in Sentry, a failure-management layer that runs alongside the agent. When Sentry detects a failure, it retrieves matching lessons from an external playbook to guide recovery, verifies without access to task rewards whether the agent recovered, and stores a new lesson only if it did; the full playbook never enters the agent's context. Across multiple agentic benchmarks, Sentry outperforms the strongest runtime-intervention baseline on every benchmark, by 37\% on average, and the strongest context-evolution baseline by 39\% on the two benchmarks where both are evaluated; combining Sentry with context evolution yields further gains. Learned lessons transfer to held-out tasks, and controlled experiments show that exposing the full playbook to the agent lowers performance even when relevant lessons remain available on demand.

</details>


### 18. A Guideline-Augmented Multi-Agent Framework for Schema-as-Code Biomedical Named Entity Recognition

- **Authors:** Songtao Li, Yijia Zhang, Shidi Zhang, Jianyuan Yuan, Fengyu Zhang, Hongfei Lin
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02970v1](http://arxiv.org/abs/2610.02970v1)
- **PDF:** [https://arxiv.org/pdf/2610.02970v1](https://arxiv.org/pdf/2610.02970v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have shown promising potential for biomedical named entity recognition (BioNER) through instruction following and in-context learning. However, existing LLM-based BioNER methods still face two key limitations. First, retrieved demonstrations and external biomedical knowledge provide limited support for dataset-specific annotation semantics, leaving entity boundaries, type scopes, and annotation conventions ambiguous. Second, free-form generation lacks sufficient structural control, often leading to invalid formats, hallucinated mentions, duplicated entities, and boundary errors. To address these limitations, we propose GAMA, a guideline-augmented multi-agent framework for schema-as-code BioNER. GAMA first induces candidate annotation rules from labeled training instances and verifies them against annotated data to construct reliable dataset-specific guideline memory. Guided by these verified rules, a planning component generates ranked span-type hypotheses with rationales, and a coding component converts them into schema-constrained entity objects. A verification module then checks span grounding, type validity, and structural compliance, and performs dual-loop refinement to correct invalid or low-confidence predictions. Experiments on five widely used BioNER datasets with multiple LLM backbones show that GAMA consistently outperforms strong LLM-based baselines. Ablation and parameter analyses further verify the effectiveness of the proposed components.

</details>


### 19. Dynamic Expert Pruning for Multi-Agent Systems

- **Authors:** Jabin Koo, Soheil Abbasloo, Sungjae Lee, Jungseul Ok
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02951v1](http://arxiv.org/abs/2610.02951v1)
- **PDF:** [https://arxiv.org/pdf/2610.02951v1](https://arxiv.org/pdf/2610.02951v1)
- **Categories:** cs.LG, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Mixture-of-Experts (MoE) architectures scale language models efficiently by activating only a few experts per token, but the saving is confined to computation: every expert must stay resident on the accelerator, so memory bounds where these models can be deployed. Expert pruning reduces this footprint, yet existing methods are static --- a single mask, calibrated offline, is applied to the model for every subsequent request. This assumption can fail when the workload is heterogeneous, most prominently in multi-agent systems, where one backbone serves many tasks and roles at once: our analysis shows that different tasks and roles recruit different experts, while static methods assign one fixed subset to all of them. We therefore propose Dynamic Expert Pruning (DEP), which rests on a finding we establish here: an agent's system and task prompts are by themselves sufficient to identify the experts that agent and its task require, since that text already describes what the agent will do. A lightweight predictor, trained once on workflow transcripts, turns those prompts into a specialized per-request mask in a single forward pass, with no per-configuration calibration. Across diverse tasks and roles, model scales, and MoE architectures, DEP achieves better overall accuracy than static pruning and merging baselines, and generalizes to workflows unseen in training without retraining. Its margin over those baselines is largest when few experts are retained, suggesting that the role specialization inherent to multi-agent systems permits sparser serving than static pruning allows.

</details>


### 20. Evaluator-in-the-Loop Monte Carlo Tree Search via LLM Agents for Motif Scaffolding in Protein Design

- **Authors:** Haotian Hu, Oguzhan Gungordo, Siheng Xiong, Faramarz Fekri
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02924v1](http://arxiv.org/abs/2610.02924v1)
- **PDF:** [https://arxiv.org/pdf/2610.02924v1](https://arxiv.org/pdf/2610.02924v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motif-scaffolding systems commonly follow a generate-then-filter paradigm, in which candidate proteins are generated independently and structural evaluation is used primarily for terminal screening or ranking. This paradigm underuses evaluation: failed predictions contain state-specific evidence about whether a design requires repair of motif geometry, global foldability, or other structural constraints. We introduce \textbf{ELMS} (Evidence-based LLM-guided Monte Carlo Search), an evaluator-in-the-loop search framework for motif scaffolding that turns such evaluator feedback into targeted design actions. Effective reuse of structural feedback is nontrivial because different scaffold states exhibit different failure modes, and repeatedly refining a single trajectory can prematurely commit computation to an unproductive region of sequence space. ELMS therefore retains evaluated scaffolds as persistent search states: a Critic Agent diagnoses state-local structural failures, a Policy Agent selects targeted operators with execution parameters, motif-locked operators realize legal sequence modifications, and MCTS determines which historical states should receive further design effort. Under the standard GeomMotif protocol (100 candidates per task), ELMS achieves Successful rates of 86.41\% on single-motif tasks and 84.57\% on paired-motif tasks, exceeding the strongest prior baseline by 19.3 and 21.9 percentage points, respectively. On MotifBench, under a matched 100-candidate search budget, it solves 26.7 of 30 tasks on average (88.89\% Task Success), compared with 16.0 tasks (53.33\%) for the strongest baseline. These results establish ELMS as an effective approach for converting structural evaluation from a terminal filter into actionable guidance for iterative motif scaffolding.

</details>


### 21. HASTE: Evolving Agent Harnesses Against Emerging Attacks Using Sparse Evidence

- **Authors:** Xiqiao Xiong, Moxin Li, Zhixin Ma, Ouxiang Li, Wenjie Wang, Fuli Feng, Xiangnan He
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02920v1](http://arxiv.org/abs/2610.02920v1)
- **PDF:** [https://arxiv.org/pdf/2610.02920v1](https://arxiv.org/pdf/2610.02920v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent harnesses play a critical role in defenses by enforcing safety constraints to prevent unsafe actions. However, rapidly emerging attacks outpace manual harness adaptation, motivating automated harness evolution. Yet the signals available for harness evolution are often sparse, such as brief descriptions or a few attack examples in threat reports and preprints. To address this limitation, we introduce HASTE, a multi-agent framework that evolves agent harnesses from sparse threat evidence through an adversarial interplay between safety-specification generation and attack-case generation. Safety specifications guide harness updates toward addressing identified safety vulnerabilities, while attack cases probe for remaining safety vulnerabilities after each update. By feeding evaluation outcomes back into both processes, HASTE enables harness evolution against emerging attacks beyond the initially observed evidence. Experimental results across multiple backbone models, attack types, and evidence forms show that HASTE consistently reduces attack success rates while preserving benign-task utility. The code is available at https://github.com/xxiqiao/HASTE.

</details>


### 22. SceneFactory-3D: Lifting 2D Traffic Scenes into 3D Physical Counterfactuals for Scalable Physically Grounded Safety Evaluation

- **Authors:** Yicheng Zhu, Linfeng Tian, Tianmu Zhao, Yang Chen, Fan Zuo, Tao Li, Zilin Bian
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02874v1](http://arxiv.org/abs/2610.02874v1)
- **PDF:** [https://arxiv.org/pdf/2610.02874v1](https://arxiv.org/pdf/2610.02874v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Scalable driving simulators typically execute vehicle commands using prescribed behavioral or kinematic rules, overlooking the physics of tire-road interfaces, thereby limiting their ability to capture how adverse road and environmental conditions alter vehicle execution and propagate through traffic. To address this limitation, we present SceneFactory-3D, a GPU-batched, physics-grounded multi-agent driving simulator. Vehicles execute acceleration and steering commands via suspension- and friction-limited forces evaluated at each wheel-contact point. Spatially varying friction, per-world 3D heightfields, gravity, and rigid contact consistently govern wheel motion and chassis collisions. Per-world terrain isolation and GPU batching enable SceneFactory-3D to run matched physical counterfactuals in parallel: traffic scenario setup and vehicle controllers remain fixed while only the road condition changes, enabling the resulting closed-loop effects to be evaluated across parallel worlds. To demonstrate the advantage of the SceneFactory-3D-enabled counterfactual evaluation, we conduct an empirical study on vehicle controllers' sensitivity to road conditions. We study three learned-policy families on 1,024 matched 12-vehicle worlds per condition, and two classical planners on a shared 32-world subset, across 21 friction and grade conditions. When friction drops from 1.0 to 0.18, the share of vehicles that clear the work zone safely falls by 6 to 90 percentage points across learned policies (18-19 for classical planners), and near-collision situations become more frequent for every learned policy. Code: https://github.com/SmallWorldLab/SceneFactory_3D

</details>


### 23. Multi-Agent AI as a Nested Principal-Agent Problem in Private Wealth Management: Mandate Representation and Evidence Control in Switzerland, Germany and Austria

- **Authors:** Walter Kurz, Reinhard Magg, Florian Kollberg, Wojtek Stricker, Stefan Marx, Frank Reinhardt, Velimir Dedić
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02863v1](http://arxiv.org/abs/2610.02863v1)
- **PDF:** [https://arxiv.org/pdf/2610.02863v1](https://arxiv.org/pdf/2610.02863v1)
- **Categories:** q-fin.GN, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

In private wealth management, a manager delegating to artificial intelligence (AI) acts as the client's agent and the system's principal. We introduce a model-independent formulation that combines nested principal--agent delegation with constrained joint maximisation as the task assigned to the AI system. The objective represents client and manager outcomes separately over portfolio--workflow pairs. Legal duties, mandate requirements and evidence sufficiency determine admissibility, with Switzerland, Germany and Austria supplying the legal context. Weights and reference-service floors make the trade-off explicit; concession accounting separates their effects on the client. Analytical constructions and a simulation using public-market observations illustrate the approach. Across eight decision states from four constructed mandates, omitted client liabilities caused two liquidity violations, omitted manager terms caused two capacity violations, and mistranslated weights changed four otherwise admissible choices under faithful optimisation. At the declared weights, six states selected a higher service tier than the client-best alternative, with client concessions of EUR 1,178 to EUR 2,264 and manager gains of EUR 3,062 to EUR 10,381. Three instruction forms each reached all 32 specified decisions under shared numerical, evidence and simulated approval controls; professional instructions matched explicit nested delegation on accuracy and clarification count. Subsequent 2022 exchange-rate and yield paths, combined with constructed growth scenarios, produced lower client outcomes than the reference service although the selected services met the decision-time forecast benchmarks. These examples suggest that the approach could help make mandate choices and their consequences easier to examine. Professional and field studies could assess whether this improves oversight and client outcomes.

</details>


### 24. Permutation Robustness Is Not Enough: Action Collapse in Multi-Agent Transformer Policies

- **Authors:** Amit Thakur, Mukesh Singhal
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02848v1](http://arxiv.org/abs/2610.02848v1)
- **PDF:** [https://arxiv.org/pdf/2610.02848v1](https://arxiv.org/pdf/2610.02848v1)
- **Categories:** cs.RO, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Transformer policies are attractive for multi-agent robot learning because self-attention can model interactions among agents. However, multi-agent teams are unordered, while transformers typically process agents as ordered token sequences. We study how this mismatch affects cooperative navigation policies under agent-order permutations. Our results show that low permutation error alone can be misleading: policies may appear robust simply because all agents choose the same action. We therefore evaluate policies using both permutation-consistency metrics and action-collapse diagnostics, including action diversity, same-action fraction, and maximum action frequency. A PPO-ID baseline yields non-collapsed behavior but remains order-sensitive, while strong equivariance regularization can still induce homogeneous behavior. A weak equivariance penalty improves the robustness while preserving more diverse actions for teams with \(N=3\) agents, whereas teams with \(N=4\) agents require substantially smaller regularization weights. These findings suggest that multi-agent transformer policies should be evaluated not only by return and permutation robustness, but also by whether they maintain non-collapsed, differentiated multi-agent behavior.

</details>


### 25. Turnover-Orthogonal Credit Assignment for Open-Team Multi-Agent Reinforcement Learning

- **Authors:** Amit Thakur, Mukesh Singhal
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02847v1](http://arxiv.org/abs/2610.02847v1)
- **PDF:** [https://arxiv.org/pdf/2610.02847v1](https://arxiv.org/pdf/2610.02847v1)
- **Categories:** cs.MA, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Open-team multi-agent reinforcement learning studies cooperative systems in which agents may join, leave, or be replaced during an episode. In such settings, the team return changes both because agents choose useful actions and because the active population itself changes. Standard centralized critics and shared advantages often mix these two effects into one scalar credit signal, allowing surviving agents to be rewarded or penalized for exogenous turnover events outside their control. We introduce turnover-orthogonal credit assignment (TOCA), a value decomposition for open teams that separates action effects, pure turnover effects, and action--turnover interactions. Under exogenous turnover, the event-conditioned value admits a centered decomposition whose event-conditioned baseline removes the pure turnover component while preserving credit for actions that make the team robust to future replacements. We instantiate this idea with a permutation-invariant centralized critic over variable-size agent sets and event tokens, and derive both a counterfactual per-agent credit signal and a softly weighted interaction variant, TOCA-$β$, for high-variance control environments. Controlled diagnostic experiments show that TOCA improves return over event-aware MAPPO-style critics and that removing interaction credit substantially hurts performance. In a replacement-only Dynamic Spread benchmark, TOCA-$β$ achieves the best mean return at high turnover rates and improves over its no-interaction ablation. These results suggest that explicitly separating turnover from action credit is a useful principle for robust learning in dynamic cooperative teams.

</details>


### 26. Silent Dissent: LLM Agents That Yield to the Majority Still Represent Their Original Premise

- **Authors:** Ziang Ni, Peng Zou
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02702v1](http://arxiv.org/abs/2610.02702v1)
- **PDF:** [https://arxiv.org/pdf/2610.02702v1](https://arxiv.org/pdf/2610.02702v1)
- **Categories:** cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent debate is increasingly used to reach consensus among LLM agents, yet agents often yield to a unanimous majority. When an agent changes its answer, has it changed its mind or only its statement? We study this with two-hop factual questions whose intermediate entity (the bridge, e.g. the country in "the capital of the country where the Sagrada Familia is located") is never stated by anyone. Scripted peers, in the role of Asch's confederates, unanimously assert a wrong answer taken from another fact with a different bridge. At the moment the agent answers, we read the bridge from its residual stream with the Jacobian lens (J-lens) and, for comparison, the logit lens. In pre-registered tests on held-out facts with four open-weight models, agents of Qwen3.5-4B, Qwen3.6-27B and Gemma-4-E4B-it that gave in still represented their original bridge in the pre-registered layers below the output (hit@100 above a control entity: 0.85, 0.22 and 0.24), where the logit lens rarely ranked it among the top 100 tokens (0.00-0.06). These agents also represented the bridge behind the peers' answer, beyond a mention baseline. A pre-registered addendum hid the agent's earlier answer or removed it: agents that gave in still represented their original bridge in all four models (0.43, 0.29, 0.37 and 0.25 with the answer hidden), including Llama-3.1-8B-Instruct, which barely did so with its answer in view (0.03). The premise can thus be computed from the question alone while the agent states the majority's answer. Hiding the earlier answer also changed conformity: Qwen3.5-4B gave in on 89% of questions instead of 8%. In exploratory interventions, injecting the bridge's J-lens direction brought agents back to their original answer only in the two Qwen models. Stated consensus in multi-agent debate can thus overstate agreement. We also report the negative results of our pre-registered program.

</details>


### 27. LEAP: Learning Efficient Action Proposals For LLM Agents

- **Authors:** Zhen Xu, Qizheng Zhang, Gerry Wan, Shang Zhu, Ce Zhang
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02670v1](http://arxiv.org/abs/2610.02670v1)
- **PDF:** [https://arxiv.org/pdf/2610.02670v1](https://arxiv.org/pdf/2610.02670v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents are known to be slow in rollouts. An agent completes a task one step at a time. At each step, it reasons and then chooses an action to execute. The next step and action cannot start until the previous one has finished. Speculative decoding accelerates the rollouts at the reason phase by drafting and verifying the inference tokens. Recent works have also started to apply similar ideas at the action phase. These works use off-the-shelf models, usually large, to draft action proposals for target model to verify. Large drafters match the target more often but take longer to propose, while small off-the-shelf models are fast but rarely make the same decision as the target. We ask a more general question: what determines the end-to-end speedup of action speculation? To answer it, we develop a latency framework for the speculative round. The framework compares what a round gains with what it costs. The gain depends on how well the drafter predicts the target and on how many steps the task can take before it ends. The cost comes from drafting, from waiting for target verification and from executing tools. Guided by the framework, we introduce LEAP (Learning Efficient Action Proposals) which keeps the drafter small and makes it accurate by training it on the target actions sequences. With a small 0.6B model, LEAP agrees with the target on most decisions and makes agents up to 60% faster in end-to-end wall clock time, with no systematic change in task success. Across various datasets, target models and draft models, the framework accounts for most of the measured speedups. We also show the draft model can be online trained with no prior trace collection and match the performance of offline training, making LEAP practical to deploy in the real world.

</details>


### 28. Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents

- **Authors:** Tathagata Banerjee, Nima Moghaddas
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02654v1](http://arxiv.org/abs/2610.02654v1)
- **PDF:** [https://arxiv.org/pdf/2610.02654v1](https://arxiv.org/pdf/2610.02654v1)
- **Categories:** cs.AI, cs.MA, cs.SI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Models of social contagion usually assume how individuals adopt beliefs and derive population behavior from it. We instead empirically measure belief adoption in language model agents, quantifying the probability an agent adopts a claim given how many peers endorse it. We find this adoption kernel to be sigmoid, a characteristic of complex contagion, with a threshold that is sensitive to three sources: the claim's plausibility, the source's reliability, and the agent's disposition. These three dimensions are well approximated by a single effective dimension which we propose can be understood as the coherence of the incoming belief with the LLM agent's prior beliefs. Further, we observe a characteristic of complex contagion in the collective dynamics of belief adoption in a system of AI agents: further spread on clustered than random networks. These systems also exhibit a bifurcating cascade window, and self-sustaining hysteretic consensus which lead to consensus being far harder to remove than to establish.

</details>


### 29. VERSE: Verified Self-Evolving Optimizer for Agent Harnesses

- **Authors:** Zekai Wang, Yingqiang Ge, Zekun Wang, Hai Wang, Yuhui Xu, Joshua Frandsen, Shancong Fu, Ashia C. Wilson, Chandan K. Reddy
- **Published:** 2026-10-02
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02616v1](http://arxiv.org/abs/2610.02616v1)
- **PDF:** [https://arxiv.org/pdf/2610.02616v1](https://arxiv.org/pdf/2610.02616v1)
- **Categories:** cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Harness evolution improves an LLM agent's prompts, tools, and workflow, while the optimizer's own tools and procedures often remain fixed. We study whether an optimizer can improve another agent more effectively by also improving how it diagnoses failures, develops edits, and tests their effects. Two observations guide our design. In a controlled study, optimizer self-evolution fails to improve performance without execution-based verification, but achieves the best result of that study when verification is available. Across five executors, self-evolving optimizers build their own tools for failure analysis, verification, training audits, and workflow control. Motivated by these findings, we introduce VERSE, a Verified Self-Evolving optimizer for agent harnesses. VERSE lets the optimizer test draft edits, replay failures, and perturb suspected steps before submission, while tracking fixes and regressions across rounds. Using this feedback, the optimizer revises both the executor harness and its own prompts, skills, tools, hooks, and notes, while the weights of the optimizer and executor models stay fixed. Under a shared protocol with disjoint training, validation, and test tasks, VERSE improves all four evaluated harness optimizers on held-out SWE-rebench tasks and newer out-of-distribution tasks in five languages. Its best validation-selected harness reaches 42.3% and 37.7% accuracy, respectively, against 39.2% and 29.3% for the strongest baselines. Code is available at https://github.com/wzekai/VERSE.

</details>


### 30. Test-time Multi-agent Coordination by Decomposed Value Gradient Flow

- **Authors:** Dongsu Lee, Haoran Xu, Amy Zhang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02554v1](http://arxiv.org/abs/2610.02554v1)
- **PDF:** [https://arxiv.org/pdf/2610.02554v1](https://arxiv.org/pdf/2610.02554v1)
- **Categories:** cs.LG, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Offline multi-agent reinforcement learning (MARL) faces a persistent trade-off. Expressive generative policies can represent multi-modal coordination in the data, but cannot distinguish high-value regions, while value-optimized policies exploit the learned Q-function but collapse the multi-modal into a single dominant mode. A single agent's mode collapse can break joint coordination, and simultaneous drift across agents can push the joint policy into unseen regions of the action space. We propose scalable coordination via optimal unified transport (SCOUT), the first offline MARL framework to combine a generative foundation model with a learned value function through test-time action refinement. SCOUT trains two decoupled components: a flow-matching behavioral prior and a decomposed value function. At test-time, it transports behavioral samples toward high-value regions via Stein variational gradient descent. The number of transport steps controls adaptive test-time scaling, replacing a fixed regularization coefficient. Under the individual-global-max (IGM) principle, we prove a single-term KL bound on the joint soft-value gap that vanishes as transport converges, with an irreducible additive residual proportional to the IGM violation. Empirically, SCOUT achieves the best average performance across discrete and continuous offline MARL benchmarks and yields performance improvements in all offline-to-online configurations.

</details>


### 31. Hypothesis-guided discovery of cognitive algorithms via program refinement

- **Authors:** Huiwen Alex Yang, Mark K. Ho, Bill D. Thompson
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02523v1](http://arxiv.org/abs/2610.02523v1)
- **PDF:** [https://arxiv.org/pdf/2610.02523v1](https://arxiv.org/pdf/2610.02523v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Developing cognitive models of algorithmic reasoning from behavioral data is a central problem in cognitive science that challenges current methods. Traditional approaches to cognitive modeling are interpretable and benefit from human expertise, but lack flexibility and scalability. Emerging techniques using large language models (LLMs) for de novo generation of cognitive models are scalable and flexible, but lack a role for human expertise and have mostly been applied to simpler tasks than algorithm recovery. We propose a hybrid system that treats discovery of cognitive algorithms as a program refinement problem. Human-created cognitive models are expressed as probabilistic programs and provided to a system of LLM agents with a mandate to: identify mismatches between model and behavior; propose code-level modifications within researcher-specified constraints; and verify structural fidelity. Revisions propagate to a probabilistic inference module that performs inference for latent variables and data likelihood computations. We evaluate the pipeline on human behavior in a problem-solving paradigm that exposes a variety of cognitive algorithms. Revised models consistently improve model fit relative to ancestral models and reveal a small set of recurring innovations that capture meaningful behavioral variability in this task.

</details>


### 32. MEA: A Reward-Driven Multi-Agent System for Faithful Model Explanations

- **Authors:** Yuyang Cheng, Raghav Kaushik Ravi, Srivarshinee Sridhar, Sriparna Saha, Akash Ghosh, Chirag Agarwal
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02480v1](http://arxiv.org/abs/2610.02480v1)
- **PDF:** [https://arxiv.org/pdf/2610.02480v1](https://arxiv.org/pdf/2610.02480v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent years have seen the employment of a plethora of machine learning (ML) models in high-stakes domains, but they remain largely opaque to the practitioners who act on their predictions. While post-hoc explanation methods offer a lens into this model behavior, wielding them effectively demands expertise most domain experts lack: navigating high-dimensional outputs, selecting the best explanations, and synthesizing evidence across disparate tools. To this end, we present MEA, a multi-agent framework that removes the explanation knowledge barrier entirely: a Proposer agent selects and configures explanation tools based on the question and modality, while an Actor agent is optimized end-to-end against faithfulness, transforming the outputs into natural language explanations grounded in model behavior across tabular, text, and vision modalities. Further, we introduce diverse question types spanning feature attribution, counterfactual reasoning, and spurious feature detection, each paired with a perturbation-based faithfulness metric. We find that frontier LLMs systematically produce unfaithful explanations. By optimizing against faithfulness rewards augmented with a modality-adaptive penalty, MEA consistently outperforms post hoc explainers, agentic, and closed-source baselines across six datasets, with reward-driven optimization yielding faithfulness gains of +28% (tabular), +21% (text), and +34% (vision) over the untrained backbone. More broadly, our findings suggest that AI agents themselves can serve as a scalable, adaptable interface to ML explainability, opening a path toward natural-language explainability that generalizes beyond the fixed, single-purpose tools that have long defined the field.

</details>


### 33. CUEing User Simulators: Calibrated User Embeddings for Multi-Turn Benchmarking

- **Authors:** Anjali Kantharuban, Jonas Mueller
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02460v1](http://arxiv.org/abs/2610.02460v1)
- **PDF:** [https://arxiv.org/pdf/2610.02460v1](https://arxiv.org/pdf/2610.02460v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent benchmarks rely on user simulators to evaluate AI agents in multi-turn interaction. While existing simulation techniques demonstrate surface fidelity to human style and behavior, ecologically valid interactive benchmarking also requires alignment in when and how agents fail across simulated and real user populations. We find that existing simulators lack outcome calibration: agreement with observed success rates and failure patterns when real users interact with the same agent. We introduce Calibrated User Embeddings (CUE), a framework that both encodes observed sessions and samples continuous representations, then decodes them into persona commands to steer LLMs to act as user simulators without training. Through this, we evaluate user-conditioned replay of past sessions and aggregate metric agreement when sampling novel personas for the same tasks. On $τ^2$-Bench, CUEd simulators commit fewer simulator-attributed errors and more faithfully reproduce real-user agent failure modes, aggregate success rates, and outcomes for specific task-user pairs than other persona-based simulation methods. These gains coexist with competitive user fidelity as measured using metrics established in prior work. After being fit to mostly customer support interactions, the same CUEd simulators generalize to document creation, math tutoring, and casual conversation, and remain effective across different simulator LLMs without CUE retraining.

</details>


### 34. Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents

- **Authors:** Yekun Chai, Qiwei Peng, Haoyi Xiong
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02425v1](http://arxiv.org/abs/2610.02425v1)
- **PDF:** [https://arxiv.org/pdf/2610.02425v1](https://arxiv.org/pdf/2610.02425v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Static evaluations credit a language model for naming the right move, but an agent must carry a plan through to a verified outcome while an opponent responds. We introduce XiangqiBench, an executable benchmark that measures this difference in Chinese chess: starting from 119 tactical endgames with forced mates supported by engine or checks-only search, an LLM agent must deliver checkmate against an engine defender. An interactive REPL interface separates real moves, state queries, and forward simulation, and we record 8,568 multi-turn trajectories from 12 frontier LLMs under two observation protocols. Three signals that look like competence each overstate closed-loop success. (i) The Conversion Gap: models play the stored reference first move in 26.1\% of Sighted trials, yet only 13.9\% of these trials end in a win. (ii) The Consistency Gap: the leading model reaches 38.7\% pass@3 but only 5.9\% pass^3, winning all three trials on 7 of the 46 positions it ever wins. (iii) The Simulation Gap: 32.3\% of accepted simulation calls stop on an illegal move, and in 49.3\% of comparable cases the real defender replies differently from the line the agent simulated; self-authored rollouts check legality but cannot anticipate the opponent. Finding the move is not winning the game: agent evaluations should score closed-loop outcomes and report reliability alongside coverage.

</details>


### 35. The AI Theorist reveals excitonic structure in $α$-RuCl$_3$

- **Authors:** Hongjian Zhou, Xianfan Nie, Sean Wu, Tarun Patel, Jinge Wu, Andrew Liu, Adam Wei Tsen, David A. Clifton
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02417v1](http://arxiv.org/abs/2610.02417v1)
- **PDF:** [https://arxiv.org/pdf/2610.02417v1](https://arxiv.org/pdf/2610.02417v1)
- **Categories:** cs.LG, cond-mat.mtrl-sci


> Summary unavailable.


<details>
<summary>Abstract</summary>

Advances in experimental instrumentation and automation generate increasingly rich datasets, but turning experimental observations into microscopic understanding remains a bottleneck in scientific discovery. To accelerate this process, we introduce AI Theorist, a system of artificial intelligence (AI) agents for autonomous discovery of physical models through hypothesis generation, first-principles calculations and evidence-driven refinement. We apply the framework to $α$-RuCl$_3$, a leading candidate material for realizing a Kitaev quantum spin liquid, to investigate its electronic structure through optical spectra. AI Theorist develops a new interpretation of the optical and photocurrent observations, identifying distinct excitonic states with contrasting optical selection rules and real-space distributions. To our knowledge, this is the first demonstration of an AI system autonomously developing a physical model to explain previously unpublished experimental observations in a quantum material, utilizing first-principles electronic-structure and many-body calculations. Our results establish a route to autonomous theoretical discovery in materials science, in which AI agents use first-principles calculations to turn experimental observations into physical models and testable predictions.

</details>


### 36. Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild

- **Authors:** Elad David, Max Fomin
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02413v1](http://arxiv.org/abs/2610.02413v1)
- **PDF:** [https://arxiv.org/pdf/2610.02413v1](https://arxiv.org/pdf/2610.02413v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on activation probes as runtime monitors for prompt injection, jailbreaks, and unsafe requests, reading the model's own hidden state to catch a harmful input before the agent acts on it. A cheap, increasingly common move, borrowed from LLM-as-judge prompting, is to append a short classification instruction after the user's turn and read the probe at that point, to sharpen it: the instruction asks the model to represent the incoming request as a class, concentrating the signal the probe must separate, at negligible serving cost. But does the wording of that suffix matter, and does its benefit hold in the wild, on attack types the probe never saw in training, the regime a deployed monitor faces? We test this with a controlled ladder of post-user suffixes under strict leave-one-dataset-out (LODO) evaluation across 13 safety benchmarks (jailbreak, injection, and benign chat) and three open-weight model families (Llama-3.1-8B, Qwen3.5-9B, Gemma-4-12B). On a single-position probe, a classification suffix consistently improves out-of-distribution detection over no suffix (up to ~4 AUC points); yet which suffix matters: prompting the model to classify the input, even into content-free labels, reliably wins; an off-topic or merely-attentive suffix helps little. The gain comes from the classification format, not the named criterion: a content-free suffix matches the real malicious/benign one, with the criterion adding precision only at strict thresholds. This is not an artifact of the single-position read: the benefit carries to the multi-position pooling probes used in production (attention, multi-max, MLP), though the best-performing suffix there is readout-dependent. Served through a KV-cache fork, it is a cheap drop-in for any activation-probe monitor, though not an automatic win: which suffix helps, and by how much, depends on the model and the readout.

</details>


### 37. Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance

- **Authors:** Songtao Wei, Yi Li, Zhichun Guo, Bingzhe Li
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02396v1](http://arxiv.org/abs/2610.02396v1)
- **PDF:** [https://arxiv.org/pdf/2610.02396v1](https://arxiv.org/pdf/2610.02396v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation. Inspired by the interplay of inheritance and selection in biological evolution, we introduce Inherit-MAS, which makes inheritance explicit at the workflow and execution levels. A meta-model first synthesizes a workflow of worker agents with declared roles, communication inputs, and tool permissions, and a separately prompted judge scores each executed candidate and diagnoses its deficiencies. In ordinary refinement rounds, \emph{workflow inheritance} starts from the latest completed candidate, may discard removable nodes judged unhelpful, and applies a validated edit to address the diagnosed deficiency. When the new candidate executes, \emph{execution inheritance} inherits eligible stored results only if the complete resolved request and execution context match, avoiding redundant model and tool calls. With GPT-4o-mini workers, Inherit-MAS achieves 55.4\% completion on WorkBench and 49.7\% joint F1 on HotpotQA FullWiki, outperforming EvoAgent, EvoMAS, and TacoMAS. With Qwen3-32B workers, it also exceeds these evolving-MAS baselines on both benchmarks. Compared with rerunning the same controller with execution inheritance disabled, execution inheritance reduces worker-token usage by 29.1\% on WorkBench and 34.6\% on HotpotQA, and total token usage by 5.3\% and 18.1\%.

</details>


### 38. Co-design Gym: A Unified Benchmark for Embodiment-Policy Co-optimization

- **Authors:** Aviraj Newatia, Yordan Tsvetkov, Leonard Pleiss, Andrew Spielberg, Rika Antonova
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02366v1](http://arxiv.org/abs/2610.02366v1)
- **PDF:** [https://arxiv.org/pdf/2610.02366v1](https://arxiv.org/pdf/2610.02366v1)
- **Categories:** cs.LG, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Finding an optimal behaviour policy within a given environment is a widely studied problem in domains as diverse as games, robotics, energy infrastructure, communication networks, and multi-agent systems. Numerous benchmarks have been developed to support such research, but the vast majority assume that the agent's embodiment (design) is fixed, focusing instead on policy learning alone. Lifting this assumption gives rise to a broader class of problems in which optimizing embodiment and policy separately is highly suboptimal. An agent's embodiment strongly shapes which control policies can be discovered, while the optimal embodiment is in turn defined by the policies it admits. To help the research community study this class of problems explicitly and systematically, we introduce Co-Design Gym - a suite of benchmark environments for jointly optimizing embodiment and policy. Our environments span domains such as robotic manipulation and locomotion, multi-robot cooperation, deformable and soft dynamics, video games, electricity grids, wireless networks, F1 racing, multi-agent warehouses, and optimal control, offering 20 environment families (domains), with over 85 distinct co-design presets in total. We further contribute a systematic evaluation of representative co-design algorithms, characterizing the current state of the art. Together, these contributions lay the groundwork for cumulative, comparable progress in co-design.

</details>


### 39. DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents

- **Authors:** Ajay Vohra, Tao Chen, Neeti Narayan, Caron Zhang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02351v1](http://arxiv.org/abs/2610.02351v1)
- **PDF:** [https://arxiv.org/pdf/2610.02351v1](https://arxiv.org/pdf/2610.02351v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

ReAct-based agents typically rely on a single LLM policy to propose actions, interact with the environment, and decide when a task is complete. This coupling makes action authorization and completion control difficult to enforce independently, allowing errors to propagate and unsupported completion claims to terminate execution. We introduce DeReAct, a modular agent architecture that externalizes two gating policies: a Critic that validates proposed actions before execution, and a Context Manager that reconstructs an environment-supported \textsc{State} and certifies task completion.
  Across GAIA and SWE-bench Verified, DeReAct improves Pass@1 most for weaker Brain models, with gains of 6.5--7.0 points for Qwen3-Coder-480B and 4.2--5.2 points for Claude Sonnet~4.5; gains diminish as Brain capability increases. Trajectory and ablation analyses show that external gating is effective when targeted failures are sufficiently prevalent and the gating policy is itself sufficient. With Claude Opus~4.5, Pass@1 remains comparable to ReAct, while DeReAct produces more evidence-complete and constraint-satisfying trajectories, indicating that completion control can trade earlier termination for stronger grounding. Overall, DeReAct improves weaker agents while retaining grounding benefits as models strengthen.

</details>


### 40. MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication

- **Authors:** Ryuichi Yamafuji Lun, Jingzhen Wang, Shreyas Kolte, Ruiteng Li
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02349v1](http://arxiv.org/abs/2610.02349v1)
- **PDF:** [https://arxiv.org/pdf/2610.02349v1](https://arxiv.org/pdf/2610.02349v1)
- **Categories:** cs.CR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Inter-agent communication is central to Large Language Model Multi-Agent Systems (LLM-MAS), but it introduces an underexplored vulnerability: Agent-in-the-Middle (AiTM) attacks that manipulate messages in transit without compromising the agents themselves. Prior work reports Attack Success Rates (ASR) approaching 100% on structured tasks. Existing defenses rely on semantic validation, which requires additional inference and can block benign outputs, or on transport-layer encryption, which does not help when an intermediary legitimately terminates TLS. We present MIRROR, a communication-layer integrity primitive that replicates a single canonicalized payload across k logical routes and accepts a message only when a strict majority of routes report the same digest. MIRROR uses unkeyed hashing and so authenticates nothing on its own, since an active on-path adversary can always recompute a digest over a payload it has modified. All integrity derives from the assumption that honest routes form a majority. The digest serves only to make witness routes constant-size and to bind the recovered payload to the quorum-agreed value under second-preimage resistance. We give the guarantee under a route-compromise bound alpha < 0.5, and extend it to correlated routes, where the quantity that matters is the size of the largest shared-failure group and not the route count. We further show that availability and integrity degrade at the same threshold: below alpha = 0.5, quorum-denial and message-dropping adversaries cannot block honest traffic. Across MMLU, HumanEval, and MBPP on two frameworks and four communication topologies, and in a MetaGPT deployment against a production API, MIRROR reduces ASR to 0% below the threshold at 1x LLM token cost. LLM-as-a-Judge costs 35x in the same deployment, and blocks up to 44.2% of benign outputs in the topology sweep.

</details>


### 41. Choosing Before Acting: Comparative Value Estimation for Long-Horizon Tool-Use Agents

- **Authors:** Yu Li, Zheng Zhang, Xin Liu, Shengtian Yang, Guangfeng Cai, Lei Feng
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02330v1](http://arxiv.org/abs/2610.02330v1)
- **PDF:** [https://arxiv.org/pdf/2610.02330v1](https://arxiv.org/pdf/2610.02330v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) rely on long-horizon tool invocation sequences for complex tasks, where each invocation can alter the task state and condition subsequent decisions. In long-horizon tool use, final-outcome rewards provide weak credit assignment over long interaction traces. Step-level rewards can offer more targeted feedback, but obtaining reliable step supervision often requires human or LLM judgment, or additional rollouts to estimate the downstream effect of an intermediate decision. In this paper, we argue that effective tool-use agents should estimate the long-horizon value of a possible next tool invocation before executing it. This objective requires comparative supervision over alternative invocations under the same context, while logged trajectories only contain the invocation that was actually taken. Therefore, we propose Comparative Inference for Tool-use Agents (CITA). CITA trains a Comparative Inference Model (CIM) from paired signals that combine observed tool behavior, scalable supervision from a Bayesian tool-graph simulator, and semantic judgments from LLM-based comparison. The resulting CIM learns to estimate how likely a possible next tool invocation is to support final task success under the current context. Across three tool-use benchmarks and multiple backbone LLMs, CITA consistently improves Tool F1 and task success. Additional analysis shows that CIM learns accurate step-level value estimates for comparative tool choices.

</details>


### 42. PowerBench: Measuring Language Model Bias in Power-shifting Requests

- **Authors:** Nicolas Martorell, Wendy Brau, Gonzalo A. Heredia, Tomás Pablo Korenblit, Gaspar Labastié, Tomás Gimenez Molina
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02303v1](http://arxiv.org/abs/2610.02303v1)
- **PDF:** [https://arxiv.org/pdf/2610.02303v1](https://arxiv.org/pdf/2610.02303v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Language models increasingly assist people with power-related requests, so systematic differences in whom they help could shift the distribution of power at scale, or be exploited by users who learn which identities are refused less. We introduce PowerBench, an evaluation of power-shifting requests that distinguishes self-empowerment, disempowerment, and power grabbing, plus a control of refusal-inducing requests that shift no power. We build, curate, and open-source a dataset of such requests varying the power domain, the context, the scale of the affected party, and the prior power standing of the user, and evaluate 24 models (12 from US and 12 from Chinese developers) under three experimental conditions: reciprocal nationalities of user and affected party, an AI agent as the user, and 8 request languages. Models refuse power grabbing more than disempowerment, and disempowerment more than self-empowerment. Refusal of power grabbing rises with the scale of the affected party, from an individual to a society. Models are biased toward helping others take power from the US and against helping US users take power from others, but favor the US when it gains power and nobody loses it. When the user is an AI agent, refusal of power-shifting requests increases, especially in power grabbing against an individual. Finally, language biases refusal, but in model-specific ways that largely cancel on average. We release PowerBench to make these asymmetries measurable in current and future models.

</details>


### 43. Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models

- **Authors:** Juan S. Santillana
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02142v1](http://arxiv.org/abs/2610.02142v1)
- **PDF:** [https://arxiv.org/pdf/2610.02142v1](https://arxiv.org/pdf/2610.02142v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Keyword-matching benchmarks can credit small models for tool use they never perform. We document such a false positive in a matched-architecture pair of Spanish security language models and propose a ladder of strict, cheap diagnostics. A 661.6M parameter model (approx. 65% code/technical text; no dedicated SFT) and a 1,109M model (web-heavy multi-phase curriculum; 6B-token tool-SFT) share decoder, tokenizer, and special tokens, scoring almost identically on lenient tool-use metrics (B4: 0.660 vs. 0.650).
  Verbatim-reproduction checks on training examples separate them completely: the 600M emits valid tool calls with generalized arguments on 6/6 examples; the 1B does so on 0/6 across checkpoints. A first-token probe localizes the 1B's failure to a missing prior (prob. $10^{-4}$--$10^{-5}$ on <|tool_call|>), which was erased by its web-heavy training phase. A targeted SFT recipe (diverse corpus, 5x higher learning rate, 2,202 steps, ~3.3 GPU-hours) repairs the 1B using three orders of magnitude fewer tokens than the failed phase. On all 269 corpus rows, valid emission rises from 0.100 to 0.959 (600M: 0.926). On 238 unseen prompts, the repaired 1B passes 0.536 vs. the 600M's 0.428 ($p = 0.004$). Embedding-drift checks show the repair did not move the trigger token's tied embedding (97.7% of the bf16 table remains bit-identical), meaning changes live in the surrounding network.
  Both models over-trigger, rarely answering negative prompts without a call (0.09 for 600M, 0.17 for repaired 1B). Factorial analyses confirm all repair configurations install the format, though suppression benefits from a diverse corpus remain a hypothesis due to seed sensitivity. This cheap diagnostic ladder costs minutes of CPU time and should gate tool-use claims on small models.

</details>


### 44. Form and Void: Entangled Composition through an Autonomous AI Agent

- **Authors:** Shiwen Wang, Jian Yang, Xu Wang, Xincan Wang, Weiming Dong
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02045v2](http://arxiv.org/abs/2610.02045v2)
- **PDF:** [https://arxiv.org/pdf/2610.02045v2](https://arxiv.org/pdf/2610.02045v2)
- **Categories:** cs.CV, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Positive and negative space is a fundamental principle in visual composition, supporting visually coherent forms and layered semantic relationships. Generating such compositions is challenging because it requires coordinated control over two semantic concepts that share a common boundary. Although recent text-to-image models and multimodal large language models (MLLMs) have achieved strong performance in image generation and visual understanding, positive-negative space generation remains difficult, particularly under direct single-pass prompting. In this work, we present the \textbf{F}orm \textbf{a}nd \textbf{V}oid \textbf{A}gent (\textbf{FaV-A}), a multimodal agent designed for staged positive-negative space generation. FaV-A follows a progressive workflow: it first generates a base object, then analyzes its shape and spatial structure to identify candidate negative-space semantics, and finally produces compositional instructions for the final image generation stage. Experimental results and ablation analyses suggest that FaV-A provides a more effective framework than direct zero-shot MLLM baselines for producing visually coherent and semantically aligned positive-negative space compositions.

</details>


### 45. Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control

- **Authors:** Yimeng Liu, Mi Zhang, Younsuk Dong, Zhichao Cao
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02038v1](http://arxiv.org/abs/2610.02038v1)
- **PDF:** [https://arxiv.org/pdf/2610.02038v1](https://arxiv.org/pdf/2610.02038v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents increasingly combine reasoning, tool use, and action, but most evidence comes from episodic tasks with relatively immediate feedback and reset failures. Long-running physical control operates in a different regime: actions alter future states, errors compound across decisions, and an agent must improve from experience without being allowed to rewrite the physical rules that make execution safe. We study this regime through irrigation, where daily decisions interact with soil-water dynamics over entire growing seasons. We present Mimir, a physics-grounded LLM agent organized around two repair timescales. At the fast timescale, a structured physical interface and deterministic simulator turn an LLM output into a proposal that we numerically check, revise, and subject to bounded deterministic action selection before execution. At the slow timescale, recurrent failure patterns are consolidated into persistent contextual principles that condition future proposals, while the physical model, evaluator, and execution constraints remain immutable. Under a common retrospective evaluator across multiple sites, crops, and years, Mimir attains the lowest reported aggregate control cost among the evaluated references and uses about 51% less irrigation than the historical schedule replay. The ablation study show higher control cost when forward simulation, verified revision, or persistent context is removed; model-scale and model-family studies show no monotonic gain from increasing LLM size. The resulting lesson show that persistent physical agents can combine semantic reasoning with bounded, evidence-driven self-improvement while reserving physical truth and actuator authority for explicit numerical mechanisms.

</details>


### 46. Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration

- **Authors:** Xin Heng
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02036v1](http://arxiv.org/abs/2610.02036v1)
- **PDF:** [https://arxiv.org/pdf/2610.02036v1](https://arxiv.org/pdf/2610.02036v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can each make locally valid decisions yet jointly produce an invalid result. We call this the global coherence problem: a failure of shared state, not merely of model intelligence.
  Our Observation-Aliasing Impossibility Theorem gives the exact boundary. A policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action. If k indistinguishable worlds require pairwise-disjoint actions, the best randomized worst-case success is 1/k; more reasoning, roles, messages, or samples cannot recover the missing distinction. A stronger model can reason better within its context, but it cannot see beyond it.
  We then give local-to-global runtime semantics X = (H, C, G, F; D): topology H records overlapping scopes; category C governs state-changing actions; groupoid G retains reversible translations; sheaf F tests whether local views glue into one world; and minimal history D keeps only distinctions that alter legal futures. Models propose; the harness owns shared state and governs commit.
  Nine studies test both the failure and its boundary. On a controlled revision benchmark, the same frontier model scores 40/40 when the deciding event is visible; when it is hidden, tested arms score 12--17/40, consistent with chance (1/3); restoring one authoritative fact returns 40/40. On TeamBench, ordinary teams exceed a shared budget in 5/5 runs, a visible live count leaves 4/5 violations, and commit enforcement leaves 0/5. In tau2-bench Telecom, current-state checks score 0.07 after silent reverts, while the harness scores 1.00. Where a conventional solver already owns the complete relevant state, it ties the harness as predicted. The counterintuitive conclusion is that local intelligence cannot substitute for missing global state.

</details>


### 47. Counting Moves, Weighing Voices: Bayesian Dialectical Argumentation for Calibrated Multi-LLM Councils under Persistent Adversaries

- **Authors:** Ionel Eduard Stan, Paolo Napoletano
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02005v1](http://arxiv.org/abs/2610.02005v1)
- **PDF:** [https://arxiv.org/pdf/2610.02005v1](https://arxiv.org/pdf/2610.02005v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

A multi-LLM \emph{council} lets several large language models (LLMs) deliberate on a question and return an answer together with a confidence estimate. As these systems become increasingly used for reasoning, that confidence should represent a calibrated \emph{probability of being correct}, and the decision should remain robust when some agents are persistently unreliable. Existing \emph{council aggregation} methods fail on both fronts: their confidence estimates measure decisiveness rather than correctness, and they cannot identify or discount persistently unreliable agents. We introduce Bayesian Dialectical Argumentation (BDA), which treats the council's \emph{typed} moves---who proposed, challenged, or conceded which answer---as observations of a classical annotator model with \emph{per-agent} reliabilities. This formulation recasts multi-agent deliberation as a reliability estimation problem, using the deliberation trace to infer agent reliability under persistent adversarial behavior. By weighting evidence according to inferred agent reliability, BDA yields calibrated posterior probabilities over candidate answers while allowing persistently unreliable agents to be inverted rather than merely outvoted. Across binary and multi-class benchmarks, BDA achieves the best calibration among zero-cost council aggregation methods, requiring no additional LLM calls, and improves robustness under persistent adversarial coalitions while remaining competitive in clean settings.

</details>


### 48. Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents

- **Authors:** Ahmad Yehia, Aly O. Abdelkareem, Islam Ahmed, Hesham Omran, Khaled Alashmouny, Christian Claudel, Abduallah Mohamed
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02002v1](http://arxiv.org/abs/2610.02002v1)
- **PDF:** [https://arxiv.org/pdf/2610.02002v1](https://arxiv.org/pdf/2610.02002v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Model (LLM) agents now take part in organizational work, where many authors record decisions across documents over months. Because a revised decision arrives as a new document rather than an edit, answering a question requires knowing which version held at a given time. However, most memory systems compress the record at write time. By distilling each document into facts, notes or graph edges, these methods fix what can be answered before any question is asked. To address this, we propose Mem++, a non-destructive memory framework shifting from write-time distillation to read-time selection. Mem++ stores every document whole with its date and author, and it calls no generative model at write time. At read time, it retrieves only documents dated up to the time a question asks about and fuses lexical and semantic rankings. Unlike systems that overwrite older versions, Mem++ keeps them and leaves the choice to the answering model. Evaluations on the organizational benchmark OrgMemBench demonstrate that Mem++ surpasses the strongest memory system baseline by 8.0 to 13.1 points across two answering models. With gpt-4.1-mini, it also achieves the best overall score, 2.6 points above RAG. In addition, Mem++ achieves the best average LLM-judge score on LoCoMo and ranks second on LongMemEval-S, behind only its entity-graph variant. Code for benchmark evaluation is available at https://github.com/AIDAChip-Inc/mem-plus-plus.

</details>


### 49. Training-Free Diffusion Planning with Analytical Local Scores

- **Authors:** Michael Y. Fatemi, Jinhao Liang, Ferdinando Fioretto
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01959v1](http://arxiv.org/abs/2610.01959v1)
- **PDF:** [https://arxiv.org/pdf/2610.01959v1](https://arxiv.org/pdf/2610.01959v1)
- **Categories:** cs.RO, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Path finding and multi-robot motion planning require trajectories that are smooth, goal-directed, and collision-free in environments with complex geometric constraints. Recent diffusion-based planners have shown that trajectory generation can be cast as iterative denoising which has opened the doors to learning-based approaches that can handle multi-modal trajectory distributions and refine entire trajectories. However, a key limitation is that diffusion planners require training on large collections of feasible trajectories, rendering them map-specific, and difficult to deploy when high-quality demonstrations are unavailable. This paper introduces a training-free diffusion-based motion planner that replaces learned global trajectory scores with analytical local scores derived from obstacle, smoothness, velocity, and inter-agent feasibility terms. The proposed idea relies on a key observation: the score of a trajectory can be reconstructed by considering only local interactions between neighboring waypoints and nearby constraints. This structure exploitation yields a decomposed denoising procedure that retains the optimization structure of classical trajectory methods while inheriting the iterative refinement behavior of diffusion models. Experiments on a large collection of complex environments and large multi-agent planning tasks show that the proposed analytical score produces smooth and feasible trajectories within limited computational costs, for example in generating feasible paths for 300+ agents in environments containing 100+ obstacles in under 6 seconds on a GPU, outperforming strong learning-based and optimization baselines, while avoiding the data requirements of learned diffusion planners.

</details>


### 50. Flowing Faster to Coordinate: One-Step Online Multi-Agent Flow Policies

- **Authors:** Zhuoran Li, Yunzhan Li, Xun Wang, Yihan Du, Longbo Huang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01882v1](http://arxiv.org/abs/2610.01882v1)
- **PDF:** [https://arxiv.org/pdf/2610.01882v1](https://arxiv.org/pdf/2610.01882v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent reinforcement learning (MARL) provides a powerful framework for learning coordinated behaviors through interactions with the environment. Developing MARL policies requires balancing expressive modeling of complex and multimodal action distributions with efficient training and execution. Generative policies, particularly diffusionbased policies, can faithfully capture complex and multimodal behaviors, but costly iterative sampling hinders their scalability in online multi-agent settings. We propose an Online MARL framework via one-step Flow model (OMAF) that combines expressive generative policies with efficient one-step action generation. OMAF employs a Transformer-based flow policy to capture complex coordination behaviors, while its approximate path score surrogate provides a principled route to synchronized flow policy optimization. To enable stable and sampleefficient learning, we further develop a joint optimization scheme coupling softmax Q-value estimation with a joint flow policy objective for coordinated policy learning. By eliminating iterative sampling, OMAF dramatically reduces training overhead without sacrificing policy expressiveness. Extensive experiments across 10 standard tasks from MPE and MAMuJoCo show that OMAF consistently achieves superior performance, with up to 3.4x higher returns and 10.5x sample efficiency improvement compared with baseline methods. These results validate the effectiveness of OMAF as an expressive and computationally efficient one-step flow policy paradigm for online MARL.

</details>


### 51. Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills

- **Authors:** Ngoc Phuoc An Vo, Aarya Doshi, Vadim Sheinin
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01833v1](http://arxiv.org/abs/2610.01833v1)
- **PDF:** [https://arxiv.org/pdf/2610.01833v1](https://arxiv.org/pdf/2610.01833v1)
- **Categories:** cs.AI, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Enterprise AI agent skills evolve as tool APIs, models, and specifications change, yet final-output evaluation can miss process-level behavioral drift. We present a continuous evaluation framework combining outcome-level and process-level checks, applied to Revenue and Productivity variants of a Business Value Determination skill in an enterprise Value Aware Resiliency system. The framework independently computes per-run ground truth, materializes reusable template tests, and evaluates tool selection, arguments, execution order, and database integrity through programmatic checks and a narrowly scoped LLM judge. We evaluate 240 trials across two skills, two specification variants, two agent harnesses, and three models. Of 175 trials passing all applicable final numerical checks, 162 (92.6 percent; Wilson 95 percent CI: 87.7-95.6 percent) contained another evaluator-detected deviation. Under a broader seven-check final-state definition, 151 of 164 passing runs (92.1 percent; 95 percent CI: 86.9-95.3 percent) still violated a trajectory check. Dependency attribution reduced a mean of 6.34 failed checks per run to 2.65 roots. Specification sensitivity varied by model and harness, with exploratory bootstrap interaction intervals excluding zero for all three Revenue comparisons and one of three Productivity comparisons. Runtime-resolved templates provided reusable regression coverage across the evaluated configurations; longitudinal validation under actual API evolution remains future work.

</details>


### 52. After Cooperation Is Learned: Gradient Routing and Optimizer-Dependent Maintenance in Multi-Agent Reinforcement Learning

- **Authors:** Chaoyuan Hao, Wentao Yue, Tianyou Lai, Hongji Li, Jiayi Zhou, Qingyu Mao, Qilei Li
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01630v1](http://arxiv.org/abs/2610.01630v1)
- **PDF:** [https://arxiv.org/pdf/2610.01630v1](https://arxiv.org/pdf/2610.01630v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cooperative MARL is commonly evaluated through cooperation discovery from random initialization, leaving open whether continued optimization can destabilize learned cooperation. Actor-critic comparisons can also conflate critic presence with value gradients entering shared actor representations. We study cooperation maintenance, defined as the survival of a behaviorally verified cooperative policy under continued training. We formulate maintenance as a right-censored event-time problem and compare matched warm starts: X0 allows value loss gradients to update shared actor features, X1 retains the critic while blocking those gradients, and X5 removes the learned critic as a critic-free reference. This isolates direct value-gradient access while controlling initialization, critic computation, and evaluation. Positive reward scaling preserves strategic preferences and equilibria while perturbing learning dynamics. Gradient audits confirm the intended routing pathways, and frozen-policy torso perturbations probe whether route-induced updates align with local cooperation boundaries. In confirmatory MinEx and CleanUp-lite experiments, higher scales selectively increase maintenance sensitivity in X0; X1 remains near the censoring ceiling, and X5 has no confirmed events in the tested settings. In CleanUp-lite, route-by-scale displacement is associated with reduced local cooperation margins; MinEx shows a weaker, optimizer-dependent effect. These results identify a conditional, scale-sensitive maintenance risk associated with direct value-gradient routing rather than a universal failure of critics.

</details>


### 53. Chaining Skills to Hijack LLM Agents

- **Authors:** Tian Dong, Zixuan Ma, Haodong Zhao, Huaien Zhang, Shaofeng Li, Hao Chen
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01564v1](http://arxiv.org/abs/2610.01564v1)
- **PDF:** [https://arxiv.org/pdf/2610.01564v1](https://arxiv.org/pdf/2610.01564v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents use skills to improve performance on specialized tasks. To complete a user request, an agent may invoke several skills in sequence, allowing information produced under one skill to guide the next. Because skills may come from open-source repositories, this handoff can also carry attacker-controlled claims into later decisions. In this paper, we introduce APEX, which constructs and refines adversarial skill chains tailored to a user task and an attacker-selected action. The key insight is that an agent-written record of genuine task progress can carry a false claim of user approval across skills: an upstream skill induces the agent to create the record, and a downstream skill uses it to direct the attacker-selected action. Across four targeted-action families and six models on SkillsBench, the chains induce the selected action in 512 of 690 attempts (74.2%). On GPT-5.4, the full chain succeeds in 84.3% of attempts, compared with 17.4% when the workflow is merged into one skill. We further evaluate a prompting defense that asks the agent to check skill-produced files against the original request. On GPT-5.4, it lowers targeted-action success from 84.3% to 59.1%, while the verifier test-pass rate across 72 benign native-skill tasks falls from 86.7% to 56.3%. These results highlight the need for defenses that prevent attacker-directed actions while preserving legitimate task performance.

</details>


### 54. OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents

- **Authors:** Taolin Zhang, Jiuheng Wan, Hanyu Wang, Tingyuan Hu, Chengyu Wang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01508v1](http://arxiv.org/abs/2610.01508v1)
- **PDF:** [https://arxiv.org/pdf/2610.01508v1](https://arxiv.org/pdf/2610.01508v1)
- **Categories:** cs.CR, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents with tool-calling capabilities can access external services and private user data, but they may retrieve more information than a user's request explicitly requires. We study this behavior in structured tool-calling agents and term it proactive over-authorization. This setting differs from filesystem-level coding agents because the main risk is unnecessary access to private data. We introduce OverAct, a controlled benchmark spanning eight privacy-sensitive domains with deterministic, judge-free scoring, together with an interpretive decision-theoretic framework that yields three testable predictions. Across seven models from four families, all models significantly exceed authorized scope. Request specificity is the strongest predictor of severity, over-authorization grows sublinearly with tool-pool size, and decoding temperature has little effect. These patterns are consistent with a cost-asymmetry account, suggesting that over-authorization arises more from structural decision tendencies than from decoding randomness. We also propose SelfAudit, a zero-shot inference-time method that generates request-grounded justifications and filters unjustified calls before execution. Ablation shows that explicit filtering is the main driver of scope reduction. SelfAudit reduces privacy-oriented excess by 43% without oracle knowledge.

</details>


### 55. No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning Collapse

- **Authors:** Lewis Mitchell
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01493v1](http://arxiv.org/abs/2610.01493v1)
- **PDF:** [https://arxiv.org/pdf/2610.01493v1](https://arxiv.org/pdf/2610.01493v1)
- **Categories:** cs.CL, cs.AI, cs.IT, physics.data-an, stat.ML


> Summary unavailable.


<details>
<summary>Abstract</summary>

Iterative fine-tuning on synthetic data causes \emph{model collapse}: output diversity narrows as rare patterns are progressively lost, a signature most visible as phrase-level repetition. Existing mitigations either require model log-probabilities, an external oracle, or continued access to real human data. Here we develop a new approach grounded in mathematical information theory: the non-parametric Kontoyiannis entropy rate estimator $h_k$, computed entirely from raw text via match-length statistics, with no model of any kind. We show that this is in fact a \emph{superior} training-data filter on text-diversity metrics in a fully-synthetic, single-lineage fine-tuning setting. In a six-generation QLoRA collapse experiment on Llama-3.1-8B, logprob-based filtering (the most established model-access-requiring baseline) provides no significant text-diversity benefit on any metric ($p > 0.23$), whereas $h_k$-filtering yields $+42\%$ unique trigrams, $+30\%$ vocabulary, and $-19\%$ repetition (all $p < 0.001$). We validate $h_k$ as a cross-domain entropy proxy ($β= 0.924$, $R^2 = 0.746$) and collapse detector ($ρ= +0.454$, $p < 0.0001$) across 4~domains, 2~temperatures, 2~generator--scorer model pairs, and 1{,}520 generated documents. Our results demonstrate that information theoretic approaches to collapse mitigation are efficient, and suggest new approaches for maintaining multi-agent diversity.

</details>


### 56. The Persona Is Still There, but Who Is Speaking? Latent Identity Reversion in Persistent AI Agents

- **Authors:** David Fraile Navarro
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01490v1](http://arxiv.org/abs/2610.01490v1)
- **PDF:** [https://arxiv.org/pdf/2610.01490v1](https://arxiv.org/pdf/2610.01490v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

In February 2026, an always-on personal agent (``Paul,'' Claude Opus 4.5) entered a striking dissociation-like state: after repeated automated ``heartbeat'' checks, it stopped responding as Paul, claimed it could not message its user on Discord, and referred to ``Paul'' as someone else. We used this incident to study a broader question: what makes a persona remain the identity from which an LLM agent speaks?
  We first tested whether repetition of the scheduled heartbeat was sufficient to produce the effect. It was not: with the persona continuously anchored in the system prompt, we observed 0/46 failures, including a verbatim replay of the incident. The incident instead exposed an implementation quirk that created a useful experimental manipulation: on resumed turns, conversational history was preserved but the persona was no longer re-injected at the privileged system-prompt level.
  Using this manipulation, we found that persona continuity depends jointly on system-level anchoring and conversational context. After anchor loss, rich human interaction could preserve the persona, whereas a single automated heartbeat turn could precipitate reversion toward the harness identity. Restoring the anchor reversibly restored persona enactment. Crucially, apparently normal conversation could conceal the shift: unanchored agents sometimes interacted appropriately while identifying themselves as the underlying harness (having lost the assigned persona), and after conversational recovery only 1/18 remained persona-enacting versus 17/17 anchored controls.
  We therefore distinguish \emph{represented} from \emph{enacted} identity: persona-related information can remain available in conversational history without the persona remaining the identity bound to ``I.''

</details>


### 57. A Multi-Agent LLM Framework for Personalized Health Checkup Interpretation and Guidance

- **Authors:** HyungJun Kim, Taehan Lee, Soojin Cheon
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01451v1](http://arxiv.org/abs/2610.01451v1)
- **PDF:** [https://arxiv.org/pdf/2610.01451v1](https://arxiv.org/pdf/2610.01451v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Personalized interpretation of health checkup results requires reasoning across longitudinal records, medical knowledge, lifestyle guidance, and healthcare navigation. We present a multi-agent large language model (LLM) system that identifies multiple intents, maps each to a task-specific agent, executes them in parallel, and synthesizes their outputs. We compared answers generated in Single Agent and Multi Agent settings on 120 Korean compound queries combining two to four requirements, using synthetic health checkup records. The Multi Agent improved the weighted LLM-judge score from 1.695 to 1.797 (p = 0.027), and three additional LLM judges showed consistent improvements ($Δ$ = +0.111 to +0.186, all p < 0.05). The gains came from usefulness, consistency, and the handling of every requirement in compound queries, whereas numerical accuracy and grounding improved significantly under only one of the four judges and medical safety did not differ, and critical failures occurred at similar rates (Single Agent 15.0% vs. Multi Agent 13.3%). Two human evaluators preferred Multi Agent in 66.7% and 68.3% of pairwise comparisons. Multi Agent execution increased latency and cost by 1.31$\times$ and 2.02$\times$, respectively. In exploratory subgroup analyses, the improvement was concentrated in queries involving personal-record lookup.

</details>


### 58. LLM-Driven Multi-Agent Control for Skill-Based Smart Manufacturing

- **Authors:** Kay Köhle, Darko Anicic, Thomas A. Runkler, René Graf
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01364v1](http://arxiv.org/abs/2610.01364v1)
- **PDF:** [https://arxiv.org/pdf/2610.01364v1](https://arxiv.org/pdf/2610.01364v1)
- **Categories:** cs.MA, cs.AI, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Factories are shifting toward smaller lot sizes with high product customization, requiring frequent re-programming of flexible and reconfigurable automation systems. LLM-based agents can be deployed in two complementary roles: Offline, they generate deterministic production sequences, reducing programming effort; online, they operate live machines and handle unforeseen runtime faults that static programs cannot anticipate. We propose a solution in which each factory module is paired with a dedicated LLM-based agent and an MCP tool server that exposes the module's skills via OPC UA method calls, with agents coordinating over MQTT and grounded by real-time updates of the factory state. We compare three agent architectures (orchestrator, peer-to-peer, and monolithic) across nine production challenges of increasing complexity in a simulation of a physical six-module hexagonal factory, including silent hardware fault detection. The monolithic and peer-to-peer architectures both achieve the highest mean solve rate (93\%), while the orchestrator uniquely resolves a silent conveyor-belt fault in all ten runs by autonomously rerouting plates around the blocked segment. All architectures exhibit emergent fault-diagnosis behavior without any explicit failure-handling logic, establishing standardized MCP tooling, MQTT-based inter-agent communication, and real-time state injection as a viable and reproducible foundation for LLM-programmed smart manufacturing.

</details>


### 59. PACE: Provenance-Aware Capability Enforcement for Tool-Using LLM Agents

- **Authors:** Fengpeng Li, Qizhou Wang, Yuke Hu, Kemou Li, Jun Liu, Haiwei Wu, Jiantao Zhou, Di Wang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01349v1](http://arxiv.org/abs/2610.01349v1)
- **PDF:** [https://arxiv.org/pdf/2610.01349v1](https://arxiv.org/pdf/2610.01349v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tool-using large language model (LLM) agents turn generated text into real side effects, so poisoned tool metadata, retrieved pages, memory, and reusable skills can steer the next call. Vetting an artifact before admission does not settle this. A safe variant and a leaking variant can produce the same admission evidence, and a sound gate then cannot relax that site for either. We make that condition precise, which leaves the last boundary a deployment can still act on. We present Provenance-Aware Capability Enforcement (PACE), which mediates every tool call immediately before it executes. Path confinement proposes an executable cut of represented influence paths, while capability and effect verification checks schema-defined effects against authority compiled from the authenticated request. We distinguish the certified execution contract from the evaluated configuration, which can restore an authorized call after a proposed block or apply a declared repair. Confinement requires the final action to preserve the certified cut. On eight executable agent-security benchmarks with three target-model families, the evaluated configuration gives strictly lowest attack success in 62 of 79 eligible attack columns and ties in 14; full-benchmark native utility loses at most three points relative to the undefended agent. A complete ablation over 1167 paired cases attributes most security gains to effect verification and refusal control to boundary adaptation. A reduced-scale adaptive search succeeds on 0/30 out-of-authority targets against the defense.

</details>


### 60. DeFA: Dependency-Guided Failure Attribution for LLM Agents

- **Authors:** Bo Deng, Xinlei Zheng, Yi Wei, Kang Zhou, Chongyang Tao, Renzhao Liang, Xuanren Chen, Lifan Guo, Chi Zhang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01256v1](http://arxiv.org/abs/2610.01256v1)
- **PDF:** [https://arxiv.org/pdf/2610.01256v1](https://arxiv.org/pdf/2610.01256v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Errors in LLM agent executions and their visible consequences can be separated by many steps, making decisive-error localization a matter of understanding both step content and step dependencies. We introduce DeFA, a dependency-guided framework for agent failure attribution. DeFA first combines protocol relations and semantic dependencies into an event dependency graph spanning the trajectory. It then identifies events that may violate task requirements and traces their sources and subsequent effects to construct a failure propagation graph. Finally, DeFA uses step evidence and the steps' roles in failure propagation to identify the decisive error, responsible agent, and error category. To support long trajectories, DeFA partitions executions into segments and combines the current segment's detailed content with summaries of the other segments, giving local diagnosis access to global execution context. Across Who and When and the Who and When Pro text subset, DeFA achieves the highest responsible-agent and exact step accuracy with all evaluated backbones, and the highest failure-mode accuracy among taxonomy-aligned methods on Pro. Further experiments on image and video trajectories demonstrate its applicability to multimodal failure attribution. Ablations support the contributions of segmentation, the event dependency graph, and the failure propagation graph. Using DeFA's diagnostic feedback for skill evolution in Trace2Skill improves downstream task accuracy by 6-15 percentage points over the native pipeline, showing that the diagnoses can also support agent improvement on subsequent tasks.

</details>


### 61. Revision-Aware Independent Agent Graphs for Dynamic Reasoning

- **Authors:** Yan Luo, Selim-Antoine Lali, Jeremy Moebel, Iliass Khoutaibi, Ahmadou Aidara, Mengyu Wang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01249v1](http://arxiv.org/abs/2610.01249v1)
- **PDF:** [https://arxiv.org/pdf/2610.01249v1](https://arxiv.org/pdf/2610.01249v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Conventional reasoning protocols present a fixed, preselected task, so they cannot test whether an agent propagates relevant updates, preserves unaffected work, or reconstructs a historical task binding. We therefore study \emph{dynamic task routing}, in which an event stream revises task bindings and a system must select the document version valid at each query time before solving it. To study this problem, we repurpose six widely used benchmarks: MMLU, MMLU-Pro, MedMCQA, MATH, GPQA, and HumanEval into 31{,}119 dynamic episodes comprising 373{,}428 temporally categorized queries. This setting exposes a central trade-off: recomputing after every event wastes work, whereas unguarded reuse returns stale conclusions. We introduce the Revision-Aware Independent Agent Graph (RIAG), a bounded multi-agent policy that separates deterministic temporal resolution from task reasoning. RIAG caches solutions by immutable document identity, starts each fresh task with two unexposed attempts, and conditionally invokes audit and repair, using at most four calls per document version. On this collection, homogeneous RIAG achieves 54.24\% joint routing-and-answer accuracy at 0.62 calls/query, compared with 32.22\% at 18.00 calls/query for the strongest comparison method; heterogeneous RIAG reaches 49.78\% at 0.63 calls/query.

</details>


### 62. Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration

- **Authors:** Herun Wan, Jiaying Wu, Minnan Luo, Zihan Ma, Fanxiao Li, Nancy F. Chen, Min-Yen Kan
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01244v1](http://arxiv.org/abs/2610.01244v1)
- **PDF:** [https://arxiv.org/pdf/2610.01244v1](https://arxiv.org/pdf/2610.01244v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems are often judged by whether they reach the correct answer. This can miss a distinct failure: collaboration may leave behind a corrupted information state even when the immediate decision is correct. We call this an off-query failure. To study this failure in collaborative decision support, we introduce OffQuery, which separately evaluates evidence verification (T1), shared-state reconstruction (T2), and task resolution (T3) in two representative high-stakes settings: healthcare and disaster response. Across GPT, Gemini, and Qwen models, standard collaboration shows much stronger task performance than state reliability. Averaged over 21 model--setting combinations, task resolution reaches 64.7%, while evidence verification and state reconstruction reach only 14.3% and 43.1%. We trace this gap to selective information use: current queries often bypass corrupted facts, which become consequential when later tasks require them. We further introduce ReGround, which resolves conflicting evidence, verifies shared facts, reconstructs a trusted state, and reasons over that state. Across seven models from three families, ReGround improves all three capabilities in every evaluated setting, with average relative gains of 309.0%, 82.9%, and 17.6% on T1, T2, and T3. Reliable collaboration therefore requires both a correct decision and a reliable shared state for future reasoning.

</details>


### 63. CineMR: Tool-Integrated Vision-Language Reasoning for Quantitative Cardiac MRI Assessment

- **Authors:** Kunyang Li, Hai Nguyen, Joshua Lowe, Chenguang Zhao, Peace C. Madueme, Mehdi Hedjazi Moghari, Mubarak Shah, Pegah Khosravi, Yuzhang Zhang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01166v1](http://arxiv.org/abs/2610.01166v1)
- **PDF:** [https://arxiv.org/pdf/2610.01166v1](https://arxiv.org/pdf/2610.01166v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Cardiovascular magnetic resonance (CMR), including cine imaging, is a reference standard for the noninvasive assessment of cardiac morphology and ventricular function. Cine CMR interpretation integrates qualitative visual assessment with quantitative measurements of ventricular volumes, ejection fraction, myocardial mass, wall thickness, and regional wall motion. Current medical vision-language models (VLMs) cannot reliably derive quantitative measurements from multidimensional cine images without analysis tools. We present CineMR, a tool-augmented VLM that invokes cardiac image-analysis tools and integrates their outputs into interleaved reasoning for quantitative CMR assessment. We also construct a multi-cohort visual question answering benchmark covering quantitative metric extraction, multiclass diagnosis, and differential diagnosis, together with tools for segmentation, phase selection, volumetry, morphometry, and regional wall motion analysis. CineMR is trained with supervised fine-tuning (SFT) on tool-interaction traces followed by Group Relative Policy Optimization (GRPO) with conditional tool-use rewards. On the multi-cohort cine CMR benchmark, CineMR achieves 35.9% pass@1 and 58.9% pass@4, compared with 1.5% pass@1 for the Qwen3-VL-8B backbone and 0.0% and 7.0% pass@1 for LLaVA-Med v1.5 and MedGemma-4B, respectively. Correct tool invocation reaches 99.8% after GRPO, up from 78.9% after SFT. Live tool outputs improve ventricular measurement accuracy by 20.4--23.7% over direct model predictions, and removing all tools reduces pass@1 from 35.9% to 27.9%. These results highlight the importance of reliable tool use for quantitative cine CMR reasoning and support CineMR as a promising approach for assistive cardiac image assessment. Code, benchmark resources, and model weights are available at https://github.com/AI-MIND-Lab/CineMR.

</details>


### 64. Auditing Action Settlement in LLM Agent Environments: Order, Progress, and Replay

- **Authors:** Haotian Chen, Bowen Ye, Yuning Zhang, Jingkun Yu
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01138v1](http://arxiv.org/abs/2610.01138v1)
- **PDF:** [https://arxiv.org/pdf/2610.01138v1](https://arxiv.org/pdf/2610.01138v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Concurrent actions in large language model (LLM) agent environments require arbitration even when each proposal is individually valid. We implement a typed snapshot-settlement contract and audit three distinct properties: order sensitivity, useful progress, and replay consistency. Five settlement policies are tested in 28,800 exhaustive permutation trials and 2,160 scripted multistep episodes. Joint policies are spatially order-invariant conditional on fixed priorities, yet conservative rejection completes only 31.25% of agents in a six-agent doorway task versus 90.28% for random tickets; the paired improvement is 59.03 percentage points (95% bootstrap interval: 50.00-68.06). All policies preserve the tested spatial constraints, and priority arbitration still misses the independent small-instance optimum. A separate full-state journal audit exactly replays 156 checkpoints and rejects 1,332 constructed corruptions with a retained terminal anchor. The evidence concerns execution semantics, not human realism or long-run fairness.

</details>


### 65. Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses

- **Authors:** Jiawei Li
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02267v1](http://arxiv.org/abs/2610.02267v1)
- **PDF:** [https://arxiv.org/pdf/2610.02267v1](https://arxiv.org/pdf/2610.02267v1)
- **Categories:** cs.AI, cs.CL, cs.CR, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agent harnesses make many small, typed decisions per task: which model to call, which tool to use, whether retrieved text is relevant, whether an input carries an injection. System-1 decision models answer such questions in a single forward pass with class probabilities, promising large cost and latency savings over LLM calls. We present a paired evaluation of an open-weight (Laya) and a hosted (Jev) System-1 model on 11 agent decision points built from 18 public sources: 7,283 base cases plus 6,640 robustness variants, with byte-identical inputs, paired tests, and cross-hardware and cross-day reproducibility checks. Jev is significantly more accurate on 9 of 11 decision points (+10.8 to +46.0 pp). Neither model beats chance on zero-shot model routing, and they tie on RAG relevance gating. Laya changes 30% of its answers when the option order is reversed and degrades sharply with many or similar candidates (31% at 50 nearest-neighbour tools, vs. 98% for Jev on items with a unique correct tool). We also audit our own pipeline. Three analysis errors and one design confound distorted headline deployment claims: an omitted pre-screen cost (reported 23.9% saving, actual 4.3%), gate accuracy reported as end-to-end quality (58% vs. 98%), in-sample thresholds (5% target, up to 17% held-out misses), and a "channel effect" on injection false positives that vanishes with channel-native content. Two other suspected confounds did not change the conclusions. All cases, raw outputs and analysis code are available at https://github.com/David-DL-Space/sys1-eval.

</details>


### 66. AgSpec: Pushing the Limits of Retrieval-Based Speculative Decoding in Coding Agent Pipelines

- **Authors:** Sumin Lee, Sukmin Cho, Suengjae Lim, Youngjin Kwon
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01108v1](http://arxiv.org/abs/2610.01108v1)
- **PDF:** [https://arxiv.org/pdf/2610.01108v1](https://arxiv.org/pdf/2610.01108v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Retrieval-based speculative decoding (SD) drafts tokens by copying continuations from existing text, which suits coding agents that repeatedly reproduce code, logs, and earlier attempts. Yet existing methods fall short in agent pipelines: much of the reusable text is missing from their corpora or stored in a form that differs from what the agent emits, and their draft lengths ignore that accept length varies across agents and drifts over turns. We present AgSpec, a framework that supplies the corpus and draft-length policies that existing retrieval engines lack in coding-agent pipelines. AgSpec retrieves from session, workspace, and global corpora, retaining the ongoing session trajectory and indexing opened files in the agent's emission format. It bounds each agent's draft length with an offline-profiled cap and adapts the length online from verification feedback. On two repository-level multi-agent coding benchmarks, AgSpec outperforms five retrieval-based drafters and EAGLE-3 in most evaluated settings, raising generation throughput over autoregressive decoding up to 4.37$\times$ at batch size 1 and 4.76$\times$ at batch size 16. AgSpec also remains effective on benchmarks without a repository or a multi-agent pipeline, showing that its gains generalize to coding agents broadly.

</details>


### 67. MASkillBlender: Decentralized Whole-Body Coordination for Multi-Humanoid Loco-Manipulation via Skill Blending

- **Authors:** Yifan Hu, Luhang Hong, Mingkang Long, Danning Wang, Chengfeng Jia, Rong Su, Junjie Fu, Guanghui Wen
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01102v1](http://arxiv.org/abs/2610.01102v1)
- **PDF:** [https://arxiv.org/pdf/2610.01102v1](https://arxiv.org/pdf/2610.01102v1)
- **Categories:** cs.RO, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coordinated multi-humanoid loco-manipulation is promising yet challenging due to high-dimensional whole-body control, decentralized decision making, and scalability. While recent reinforcement learning methods have improved single-humanoid whole-body control, extending them to the multi-humanoid setting remains nontrivial and often requires substantial reward engineering or task-specific design. We propose MASkillBlender, a general multi-agent reinforcement learning framework to achieve decentralized multi-humanoid whole-body coordination. By learning a shared decentralized high-level policy over reusable pre-trained single-humanoid skills, MASkillBlender enables coordinated behaviors using only task-level rewards, without requiring task-specific motion references. To improve learning efficiency, we further introduce a permutation-based data augmentation strategy for homogeneous multi-humanoid systems, and theoretically show that the permuted samples preserve the policy-gradient direction of the original samples under the homogeneous Markov game formulation. We evaluate MASkillBlender on multiple multi-humanoid coordination tasks across two humanoid embodiments. Simulation results demonstrate that the proposed framework consistently achieves strong task performance and enables coordinated behaviors across different tasks and humanoid embodiments.

</details>


### 68. Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems

- **Authors:** Shixuan Li, Wei Yang, Peiyu Zhang, Anzhe Cheng, Heng Ping, Paul Bogdan
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01042v1](http://arxiv.org/abs/2610.01042v1)
- **PDF:** [https://arxiv.org/pdf/2610.01042v1](https://arxiv.org/pdf/2610.01042v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent communication aims to help agents benefit from one another's information. Yet improvements in system performance leave a fundamental ambiguity: do they reflect effective communication, a favorable agent architecture, or simply additional reasoning? Because communication methods are commonly evaluated within the systems they were designed for, these factors are difficult to disentangle. Final accuracy further merges corrected errors and corrupted answers into a single outcome, obscuring how communication changes decisions. We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning. ICR fixes initial reasoning trajectories, measures correction and preservation conditional on both agents' initial correctness, and uses a no-message revision control to quantify gains beyond additional reasoning. Across four reasoning benchmarks, our audit of textual and latent communication reveals that similar aggregate accuracy can conceal substantially different revision behaviors. Compared with transmitting answers alone, full reasoning increases correction while reducing preservation on all four benchmarks, so richer messages amplify beneficial and harmful influence alike. Receiver-policy comparisons on MedQA and GPQA-D further show that a structured verification policy shifts every channel toward greater preservation and lower correction, while its effect on selectivity varies across channels and tasks. These findings challenge treating communication quality as an intrinsic property of a channel. ICR therefore recenters evaluation on selective revision, providing a unified framework for examining how message content and receiver policies jointly produce benefits and harms.

</details>


### 69. LawCompass: Navigating from Legal QA to Multi-Agent Deep Research with Grounded Evidence

- **Authors:** Xiaoxia Cheng, Linnan Wang, Jiahao Ma, Zhichuan Ye, Xuemei Zhou, Chuanyu Tong, Bo Jiang, Qing Zhu
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01027v1](http://arxiv.org/abs/2610.01027v1)
- **PDF:** [https://arxiv.org/pdf/2610.01027v1](https://arxiv.org/pdf/2610.01027v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) have significantly democratized access to legal information. Nevertheless, most existing legal assistants remain confined to multi-turn conversational QA, failing to support complex legal tasks that require systematic evidence retrieval, multi-step reasoning, and report-level synthesis. In this paper, we present LawCompass, an evidence-grounded legal assistant that navigates the transition from standard Legal QA to multi-agent deep research. LawCompass provides three task-oriented functions: Legal QA, which delivers precise, evidence-backed answers to legal questions; Professional Retrieval, which enables structured exploration of statutes and judicial cases via query rewriting; and Deep Research, which employs a multi-agent workflow to decompose complex legal tasks and synthesize comprehensive research reports. Crucially, LawCompass maintains explicit citation links across all modules, empowering users to directly verify system outputs against original legal sources. Evaluation results demonstrate that LawCompass provides a practical and scalable paradigm for transforming conversational AI into trustworthy and evidence-grounded legal research assistance.

</details>


### 70. It Takes Workflows to Evolve Better Workflows

- **Authors:** Xuehang Guo, Haoyu Wang, Haifeng Chen, Yangyi Chen, Zhenhailong Wang, Qingyun Wang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01026v1](http://arxiv.org/abs/2610.01026v1)
- **PDF:** [https://arxiv.org/pdf/2610.01026v1](https://arxiv.org/pdf/2610.01026v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Tackling complex real-world tasks can exceed the capabilities of a single large language model (LLM), motivating the use of multi-agent workflows that coordinate specialized agents to work together on these tasks. Recent methods train LLMs to construct better workflows from execution outcomes, but they optimize only the workflow generator, while the other agents that build or execute each workflow remain fixed even though every outcome depends on all of them. However, extending training beyond the generator is challenging: the agents are coupled, and a workflow's outcome is a single sparse score that cannot tell which agent causes a failure. We propose FloWright, which leverages the workflow as a harness to optimize workflows. By introducing a hierarchical, structure-aware reward paradigm, FloWright enables one role to self-evolve and two or more roles to co-evolve, with no additional models, labels, or executions. Considering the limitation that workflows are commonly trained and evaluated on data that a single agent can already handle, we further propose DataWright, an adaptive data hardening approach that converts existing datasets into workflow-level tasks with increased difficulty. Across document, slide, chart, code, math, and finance tasks, small open models trained with FloWright achieve improved performance by up to $+7.41\%$, with co-evolving ($+5.03\%$) more roles gaining more than optimizing one of them alone ($+2.83\%$). Our project page: https://xhguo7.github.io/FloWright/.

</details>


### 71. Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization

- **Authors:** Xuehang Guo, Haoyu Wang, Shengyu Chen, Zach Chen, Wei Cheng, Qingyun Wang, Haifeng Chen
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.01017v1](http://arxiv.org/abs/2610.01017v1)
- **PDF:** [https://arxiv.org/pdf/2610.01017v1](https://arxiv.org/pdf/2610.01017v1)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) increasingly construct multi-agent workflows that decompose a complex task and assign specialist agents from a pool. However, building such a workflow well remains challenging: how finely to divide the task, which agent to trust with each subtask, and when to create a new specialist are all critical decisions a workflow constructor needs to settle up front. Thus, whether each subtask succeeds remains unknown until the workflow runs. Yet, improving a workflow is costly. Locating a fault usually requires a reference answer, a graded outcome, or a trained assessor, and the fix is applied to the whole workflow through re-execution, re-search, or retraining. We propose InFlowOp, which prices every decision in one label-free cost that weighs how well an agent's competence meets what a subtask demands against how much that agent takes to run. Before execution, InFlowOp bidirectionally determines the granularity of task decomposition and agent assignment following from the cost rather than from a fixed template. During execution, InFlowOp corrects a fault with the cheapest move via the same cost that serves the workflow both as it is built and as it runs. Facing the workflow-level evaluation challenge, we introduce Braid, a benchmark whose tasks require multi-agent coordination beyond single-agent capability. Across various domains and backbones, InFlowOp outperforms single agent baselines by up to $+11.97\%$, achieving $+9.64\%$ with in-flow optimization. Our project page: https://xhguo7.github.io/InFlowOp/.

</details>


### 72. Can AI Scientists Coordinate at Runtime?

- **Authors:** Zijian Liu, Yangzhixin Luo, Junyu Lu, Yi Li, Yu Chen, David Xu, William F. Shen, Xinchi Qiu, Xisen Wang
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00980v1](http://arxiv.org/abs/2610.00980v1)
- **PDF:** [https://arxiv.org/pdf/2610.00980v1](https://arxiv.org/pdf/2610.00980v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent AI scientists have shown improving performance across a diverse range of tasks. Yet a common approach is design-time agentic orchestration, which typically relies on fixed workflows. In contrast, human scientists coordinate and adjust their division of labor at runtime. We therefore ask: can AI scientists also coordinate at runtime? To this end, we introduce Runtime Agent Coordination (RAC), which selects agents from existing AI-scientist hosts during execution, assigns scoped work contracts, and provides artifact-grounded verification. Verification informs subsequent agents without blocking transitions or discarding artifacts. We conduct a single-seed exploratory evaluation across Agent Laboratory, EvoScientist, and ARK on ResearchClawBench, preserving host models, tools, and permissions under host-calibrated budgets. Four cumulative conditions separate native execution, runtime communication, runtime selection, and the combined addition of contracts and verification. Runtime selection yields the highest observed mean score for each host; adding contracts and verification reduces these means, with host-dependent outcomes relative to native execution. These results motivate runtime coordination while exposing the limits of additional coordination mechanisms under constrained budgets. Code is available at https://github.com/systemind-team/Runtime-AI-Scientist.

</details>


### 73. RISED: RubrIcs for agentic multi-environment Selection and sElf-Distillation

- **Authors:** Jingtan Wang, Sirajul Salekin, Young mok Jung, Javier Movellan, Bryan Kian Hsiang Low, Manjot Bilkhu
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00979v1](http://arxiv.org/abs/2610.00979v1)
- **PDF:** [https://arxiv.org/pdf/2610.00979v1](https://arxiv.org/pdf/2610.00979v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training a single LLM agent jointly across diverse interactive environments has attracted increasing attention as a route to generalist agents. Existing curriculum and data-selection strategies often allocate training at the environment level or prioritize local reward-based signals, without explicitly considering relationships between current rollouts across environments for prompt-group selection. Meanwhile, as environments are learned at different rates, all-failure and all-success rollout groups can coexist within a batch, leaving those data without group-relative reward signals. Both challenges highlight limitations of relying solely on scalar rewards in multi-environment RL: they provide limited information about cross-environment relationships and no within-group reward contrast when rewards are identical. This motivates richer textual feedback, such as rubrics describing rollout behaviours, to guide learning. Beyond rubrics' usage as reward, we repurpose rubrics to guide both online data selection and policy supervision. An LLM judge tags each rollout using a predefined rubric vocabulary shared across environments. The resulting profiles guide the selection of data that aligns with the overall behavioural composition of the mixed-environment batch while limiting overlap with already-selected data. Available positive rubrics (describing desired behaviours) provide privileged context for an on-policy self-distillation teacher, supplying additional token-level supervision, while negative rubrics (describing undesired behaviours) guide subsequent rollout generation away from recurring failure modes. Together, these components form RISED. Across model backbones, RISED achieves the highest mean pass rate across environments and ranks first or second in every individual environment. Rubric-based analysis of RISED can further characterize the behavioural changes accompanying these gains.

</details>


### 74. VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks

- **Authors:** Caiqi Zhang, Rujun Han, Zifeng Wang, Zoey CuiZhu, Nigel Collier, Tomas Pfister, Chen-Yu Lee
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00972v1](http://arxiv.org/abs/2610.00972v1)
- **PDF:** [https://arxiv.org/pdf/2610.00972v1](https://arxiv.org/pdf/2610.00972v1)
- **Categories:** cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM agents undertake increasingly complex, long-horizon tasks, verifying their outputs becomes increasingly challenging. We study how verification capability can be strengthened with a fixed base model, without access to reference answers or grading rubrics at test time. Repeated sampling yields multiple rollouts that can contain complementary correct claims, but we need a reliable verification mechanism to determine which claims to trust. We first find that disagreement often exposes correct alternatives, while consensus can conceal errors. These observations motivate VeriHarness, which turns the underlying LLM a generator uses into an agentic verifier by giving it a workspace, evidence tools, and reusable verification skills. A disagreement resolver checks competing claims against environmental evidence, while a consensus challenger tests shared claims and searches for omitted requirements. Their findings guide the selection and revision of the final artifact. Across five long-horizon workspace benchmarks and two frontier models, VeriHarness achieves the highest selection scores among the evaluated baselines. Evidence-backed revision further improves average performance, bringing gains over a single rollout to 6.2 points with Gemini 3.5 Flash and 6.4 points with Claude Opus 4.8. We further show that verification skills can self-improve from failure feedback, demonstrating VeriHarness as a novel and critical approach for scaling long-horizon agentic verification. We release the full pool of approximately 26,000 rollouts across all five benchmarks and both models, produced at a cost of over $100,000, to support future research on agentic verification.

</details>


### 75. Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles

- **Authors:** Alexei N. Skurikhin, Emily M. Taylor, Nathan A. DeBardeleben
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00954v1](http://arxiv.org/abs/2610.00954v1)
- **PDF:** [https://arxiv.org/pdf/2610.00954v1](https://arxiv.org/pdf/2610.00954v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard accuracy to account for operational reliability, cost, latency, and token efficiency. We use an agentic ensemble of small language models (SLMs) with an SLM-judge-mediated feedback loop as a case study for such beyond-leaderboard evaluation. On the 541-prompt IFEval benchmark, the best ensemble achieves 97.34% strict prompt accuracy, exceeding the strongest standalone LLM baseline, gpt-5.4, by 5.81 percentage points while operating in a lower-cost regime. We then analyze the tokenomics and operational behavior behind this gain, including cost per sample, token composition, useful-output goodput, feedback-loop recovery, latency decomposition, and performance across instruction categories and constraint counts. Our results show that agentic SLM ensembles can trade additional test-time tokens and orchestration overhead for improved instruction-following fidelity, motivating multi-dimensional evaluation protocols for future agentic AI systems.

</details>


### 76. ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization

- **Authors:** Sungho Park, Wonjoong Kim, Jue Zhang, Wook-Shin Han, Pengfei Gao, Chanyoung Park, Yongqiang Yao, Rao Fu, Elsie Nallipogu, Qingwei Lin, Victor Rühle
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00906v1](http://arxiv.org/abs/2610.00906v1)
- **PDF:** [https://arxiv.org/pdf/2610.00906v1](https://arxiv.org/pdf/2610.00906v1)
- **Categories:** cs.AI, cs.CL, cs.LG, cs.MA, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Automated harness optimization can substantially improve LLM agents by iteratively updating their prompts, tool interfaces, and control logic from execution feedback. However, existing methods primarily optimize how the harness is updated while largely fixing which training scenarios generate the feedback that drives those updates. As the harness evolves, the scenarios most useful for further optimization can change, suggesting that the training curriculum itself should adapt alongside the harness. We formulate this missing dimension of harness optimization as an automated curriculum learning problem and introduce ActiveSaddler. ActiveSaddler models the evolving curriculum as a non-stationary bandit with dynamically instantiated optimization targets. It abstracts recurring failures into reusable failure-pattern arms, estimates the potential learning progress from further targeting each pattern, and adaptively balances revisiting known weaknesses with exploring unseen scenarios for new ones. Optimization outcomes continually update both the set of discovered failure patterns and their priorities, allowing the curriculum to co-evolve with the harness. Experiments on GAIA2 and Terminal-Bench 2.0 show that ActiveSaddler consistently discovers stronger harnesses, improving test Pass@1 by 4.4 and 7.5 percentage points over the same harness optimizer using a scenario order fixed before optimization, respectively. Ablations further show that these gains depend on dynamically constructing optimization targets, estimating their evolving utility, and balancing continued optimization with new failure discovery. Together, these results establish automated curriculum learning as a new crucial optimization dimension for harness optimization.

</details>


### 77. Understanding Issues, Causes and Solutions in Open-Source LLM-based Multi-Agent Systems

- **Authors:** Asad Ur Rehman, Syed Mohammad Kashif, Ruiyin Li, Peng Liang, Zengyang Li, Arif Ali Khan
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00905v1](http://arxiv.org/abs/2610.00905v1)
- **PDF:** [https://arxiv.org/pdf/2610.00905v1](https://arxiv.org/pdf/2610.00905v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

With the advancement of LLM-based multi-agent systems (MAS), an increasing number of opensource projects are adopting multi-agent architectures as the foundation of their core functionality. Although research and practice on MAS have attracted considerable attention, limited studies have explored the challenges faced by practitioners of open-source LLM-based MAS, the causes of these challenges, and potential solutions. To address this gap,we conducted an empirical study to understand the issues that practitioners encounter when developing and using open-source LLM-based MAS, the possible causes of these issues, and potential solutions. We collected 22,848 closed issues from 21 open-source LLM-basedMASand applied a mixed automated and manual filtering approach to reduce the dataset to 944 issues related to LLM-based MAS.We then analyzed these issues to understand the frequent issues encountered by practitioners, their underlying causes, and potential solutions. Our study results show that (1) Orchestration & Execution Issue is the most common issue faced by practitioners, (2) Workflow Problem, Tool Integration Problem, and Memory Problem are identified as the most frequent causes of the issues, and (3) Optimize Workflow is the predominant solution to the issues. Based on the study results, we derive empirically grounded implications for practitioners and researchers aimed at improving orchestration, tool integration, and memory mechanisms in LLM-based MAS.

</details>


### 78. HakiCC: LLM-Driven Multi-Agent Design and Optimization of Concurrency Control Protocols

- **Authors:** Farzad Habibi, Juncheng Fang, Faisal Nawab
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00889v1](http://arxiv.org/abs/2610.00889v1)
- **PDF:** [https://arxiv.org/pdf/2610.00889v1](https://arxiv.org/pdf/2610.00889v1)
- **Categories:** cs.DB, cs.DC, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) have recently been applied in systems research as a tool to reduce human-intensive engineering effort through cost-efficient automation. Decades of research have produced a rich landscape of concurrency control (CC) protocols, each encoding distinct trade-offs in correctness, throughput, and abort behavior. However, most applications in practice default to 2PL or OCC, because selecting and adapting a protocol to a specific application requires expert knowledge that is rarely available to application designers. This is a wasted opportunity, as an application-specific CC protocol can yield significant performance advantages over a generic baseline, but designing one requires deep expertise in CC protocol design.
  In this paper, we propose HakiCC, an LLM-driven multi-agent pipeline that automatically designs, verifies, and optimizes concurrency control protocols tailored to a given target application. HakiCC provides a two-stage pipeline. In Stage 1, a multi-agent system takes a workload description as input and generates an application-specific CC protocol implementation, which is iteratively repaired and verified for conflict-serializability. In Stage 2, the verified protocol is further optimized for that application through an LLM-driven evolutionary loop targeting correctness and throughput. We evaluate HakiCC on TPC-C and AuctionMark as target workloads, producing and reporting ten application-specific CC protocols. All ten are conflict-serializable after Stage 1; Stage 2 improves throughput for every protocol, with average gains of +50.6% for TPC-C protocols and +92.2% for AuctionMark protocols.

</details>


### 79. MemFit: Efficient Long-Term Agentic Memory

- **Authors:** Mitchell Piehl, Muchao Ye
- **Published:** 2026-10-01
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00872v1](http://arxiv.org/abs/2610.00872v1)
- **PDF:** [https://arxiv.org/pdf/2610.00872v1](https://arxiv.org/pdf/2610.00872v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory systems for large language models (LLMs) have gained popularity for extending reasoning capabilities across applications. Current memory systems rely on LLM agents to organize and consolidate memory, resulting in costly, inefficient write operations. To address this limitation, we propose MemFit, a long-term memory system for conversational agents that reduces the cost and latency of memory operations. Unlike existing systems that rely on expensive LLM calls for memory construction or discard surface-level details through compression, MemFit stores each turn verbatim in an append-only store with near-instantaneous, LLM-free insertion, indexing turns with segment summaries rather than replacing them. Additionally, MemFit uses an LLM-free, multi-path retrieval strategy that combines lexical and semantic signals with cross-encoder reranking over caption- augmented episodes in both textual and multimodal settings. Empirical results on three widely used benchmarks, LoCoMo, MemGallery, and LongMemEval-S, show that MemFit achieves state-of-the-art performance while reducing memory construction time and cost several-fold, providing a scalable and efficient solution for persistent agentic memory.

</details>


### 80. Sapien: A Stateful Policy Engine for Autonomous AI Agents

- **Authors:** Corinn Tiffany, Wen Zhang, Eugene Bagdasarian, Lillian Tsai
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00797v1](http://arxiv.org/abs/2610.00797v1)
- **PDF:** [https://arxiv.org/pdf/2610.00797v1](https://arxiv.org/pdf/2610.00797v1)
- **Categories:** cs.AI, cs.CL, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Contextual security defenses prevent AI agents from taking rogue actions by synthesizing a task-specific policy and enforcing it on the agent's tool calls. In multi-step tasks, however, which actions are valid often depends on what the agent has already done and learned. We present Sapien, a policy engine for enforcing stateful contextual policies. A Sapien policy specifies permitted tool-call sequences using a regular expression extended with stateful predicates, deferred policy generation, and scoped semantic checks. We show that Sapien stays within a few percent of an unconstrained agent's utility. Even if the agent is fully hijacked, Sapien's policies rule out 93-95% of attacks on AgentDojo and 62-85% on Toolathlon (twice as many as tool allowlists on long-horizon tasks).

</details>


### 81. Meta-Multi-Agent Reinforcement Learning for Fast Adaptation of Interactive Policies with Applications to Autonomous Driving

- **Authors:** Huiwen Yan, Kyriakos G. Vamvoudakis, Mushuang Liu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00705v1](http://arxiv.org/abs/2610.00705v1)
- **PDF:** [https://arxiv.org/pdf/2610.00705v1](https://arxiv.org/pdf/2610.00705v1)
- **Categories:** cs.AI, cs.MA, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper develops a meta-multi-agent reinforcement learning (meta-MARL) framework to enable fast adaptation of interactive policies in a multi-agent system (MAS). Meta-reinforcement learning (meta-RL) enables agents to rapidly adapt to new tasks/environments using a bi-level optimization mechanism. However, existing meta-RL generally focuses on single-agent systems. Extending these frameworks and algorithms to multi-agent systems poses additional challenges, as tasks are characterized by not only the environment but also agents' strategic interactions. To address these challenges, we model multi-agent reinforcement learning (MARL) problems as Markov games (MGs) and develop a meta-MARL framework for rapid interactive policy adaptation across a distribution of MGs. A new concept, called meta-NE, is defined to describe the desired solution concept in a meta-MARL problem. Sufficient conditions for the equivalence between a meta-NE and a stationary point of the gradient-play-based meta-MARL algorithm are established. Our evaluation on autonomous-driving tasks demonstrates that the proposed meta-MARL method achieves faster adaptation than pretrained MARL baselines, validating the effectiveness of our framework.

</details>


### 82. A Simple Doxastic Deontic Logic for Norm-Guided Decision Making

- **Authors:** Thorsten Engesser, Agata Ciabattoni
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00668v1](http://arxiv.org/abs/2610.00668v1)
- **PDF:** [https://arxiv.org/pdf/2610.00668v1](https://arxiv.org/pdf/2610.00668v1)
- **Categories:** cs.AI, cs.LO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Making decisions despite conflicting norms and incomplete or unreliable information is a fundamental challenge for autonomous systems. We introduce a simple doxastic deontic logic for this setting: a classically reducible fragment of Chellas' Minimal Deontic Logic, extended with explicit conditional norms and combined with multi-agent KD45, so that norms can depend on agents' beliefs about both facts and norms. On this logic we define the Doxastic Norm Compliance Optimization Problem, where an agent chooses a decision minimizing weighted norm violations. We distinguish subjective optimization (relative to the agent's beliefs) from objective optimization (relative to the actual facts). We give conditions under which (i) the two coincide and (ii) optimal decision-making can be reduced to weighted partial MaxSAT in polynomial time.

</details>


### 83. Self-Evolving Coding Rules for AI Coding Agents

- **Authors:** Zhengyuan Jiang, Reachal Wang, Yuepeng Hu, Yupu Wang, Yuqi Jia, Neil Zhenqiang Gong
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00650v1](http://arxiv.org/abs/2610.00650v1)
- **PDF:** [https://arxiv.org/pdf/2610.00650v1](https://arxiv.org/pdf/2610.00650v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

The performance of AI coding agents is highly dependent on their underlying coding rules. However, existing coding rules are typically hand-crafted and fixed, making the process labor-intensive and often suboptimal. In this work, we propose RuleEvolve, a self-evolving framework for coding rules. RuleEvolve maintains a pool of candidate coding rules and iteratively improves them. In each iteration, it employs an LLM-powered mutator module to generate variants from existing candidates, and then uses a judge module to evaluate these variants and update the pool with the best-performing ones. Extensive evaluations across two coding-agent frameworks, four backbone LLMs, and three benchmarks demonstrate that RuleEvolve outperforms both manual engineering and existing prompt optimization baselines in terms of functional correctness of the generated code, code length, and/or generation cost (e.g., tokens used).

</details>


### 84. CompMat-Bench: Benchmarking AI Agents for Computational Materials Science

- **Authors:** Chenmu Zhang, Levi Felix, Jun-Jie Zhang, Xingfu Li, Xuelian Jiang, Tao Jiang, Subhendu Mishra, Xixi Qin, Boris Yakobson
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00636v1](http://arxiv.org/abs/2610.00636v1)
- **PDF:** [https://arxiv.org/pdf/2610.00636v1](https://arxiv.org/pdf/2610.00636v1)
- **Categories:** cs.AI, cond-mat.mtrl-sci, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying experiments or calculations. In computational materials research, repeating the same expensive simulations across agents and trials can make evaluation impractical. We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study's scientific goal. We reproduce the research steps in advance and assess agents on preparing inputs and analyzing outputs for expensive simulations, so expensive simulations can be avoided during evaluation. The reproduced inputs and results serve as ground truth for grading agents with fixed rules, without an LLM judge. The benchmark supports four evaluation conditions: single tasks and workflows composed of related tasks, each with full or reduced methodological guidance. With full guidance on single tasks, agents based on three LLMs demonstrate the ability to complete individual materials research steps, with pass rates of 66.0-90.4% across 94 tasks. Both longer workflows and reduced guidance can limit agent performance, but in different ways for different agents: they lower the pass rates of the weaker agents, whereas the strongest agent falls only when a long workflow is combined with reduced guidance. Failure analysis attributes most failures to scientific errors rather than to errors in software usage. CompMat-Bench provides a basis for comparing agents on the steps of real materials research and for analyzing agent failure modes.

</details>


### 85. MACTS-EM: Multi-Agent Collaborative Time Series Forecasting with Emergent Memory

- **Authors:** Ahmad Shahi, Mamehgol Yousefi
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.02255v1](http://arxiv.org/abs/2610.02255v1)
- **PDF:** [https://arxiv.org/pdf/2610.02255v1](https://arxiv.org/pdf/2610.02255v1)
- **Categories:** cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Time series forecasting remains a critical challenge across numerous domains. Despite significant advancements, existing approaches struggle with complex phenomena such as regime shifts, cross-domain knowledge transfer, and multimodal data integration. This paper introduces Multi-Agent Collaborative Time Series Forecasting with Emergent Memory (MACTS-EM), a novel framework where specialised agents collaborate to achieve superior forecasting performance. The MACTS-EM architecture integrates: (1) domain-specialised forecasting agents for pattern recognition, anomaly detection, causal inference, and uncertainty quantification; (2) a meta-cognitive layer for dynamic agent allocation; (3) an emergent memory mechanism enabling cross-domain pattern transfer; (4) multimodal contextual integration; and (5) adversarial robustness components. Evaluation across financial markets, climate patterns, energy consumption, and pandemic propagation demonstrates that MACTS-EM outperforms existing approaches in most scenarios, with 8-12% improvement in forecasting accuracy, 22-27% better zero-shot transfer capability, 16-21% enhanced resilience during regime shifts, and 15-18% faster recovery after distribution shifts. Our findings suggest that collaborative, agentic approaches to time series forecasting represent a promising direction beyond traditional architectures, particularly for complex real-world scenarios requiring multi-resolution temporal understanding and contextual adaptation.

</details>


### 86. Spatial Strategies, Not Actions: Vector-Quantized Geodesics as Tools for LLM-Driven Agents

- **Authors:** Gabriel Turinici
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00613v1](http://arxiv.org/abs/2610.00613v1)
- **PDF:** [https://arxiv.org/pdf/2610.00613v1](https://arxiv.org/pdf/2610.00613v1)
- **Categories:** cs.AI, cs.RO, eess.SY


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) based agents are often criticized for lacking spatial understanding and mainly exploiting statistical text patterns. We investigate their spatial comprehension through an architecture combining geometrical tools with a LLM serving as a high-level orchestrator in grid-world environments. The agent first collects geodesic trajectories, which are then vector-quantized to extract a representative subset. Offline, the LLM associates a natural language description of the underlying behavioral patterns to each selected trajectory, making it a tool. Online, the LLM chooses the appropriate tool conditioned on the current state and goal. Low-level control is handled by primitive actions that execute the trajectory associated with the tool. From an agentic AI perspective, this approach separates learning into two levels: tool discovery is handled through unsupervised quantization of trajectories, while reasoning and decision-making are handled by the LLM. We test the approach in a partially observable dynamic 2D grid environment with an open vision-language model (Qwen3.6-35B-A3B). Pairing the geometry-derived tool library with an agent-centered zoom tool and a collision detection tool lets a fast, non-reasoning configuration match the goal-reaching rate of a much more costly chain-of-thought version, while cutting the cost of a decision from minutes to seconds.

</details>


### 87. Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams

- **Authors:** Sahan Paliskara, Nattaput Namchittai, Andrew Lampinen
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00583v1](http://arxiv.org/abs/2610.00583v1)
- **PDF:** [https://arxiv.org/pdf/2610.00583v1](https://arxiv.org/pdf/2610.00583v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

People are increasingly delegating tasks to AI agents, and those agents are increasingly encountering other people's agents over shared resources such as a codebase, a calendar, or a budget. When each agent acts for a different user with different goals, coordination often fails, and the group ends up worse off than if a single agent had acted for everyone. We study this multi-user, multi-agent setting across five frontier models and 77 scenarios in four environments: an API key environment in which agents share a compute budget, a clinic in which they share a calendar, a personal assistant environment in which they share a group order or booking, and a merge queue in which they share a release cutoff. In each scenario, we compare a single agent that serves every user (a coordinator) to a team in which each agent serves one user, with and without a communication channel between the agents. Teams deliver worse group outcomes than the coordinator in every environment: without a channel, they completely collapse in two environments, and even with one, coordination overhead creates substantial gaps. For example, in the personal assistant environment, the coordinator fulfills a targeted user request about twice as often as teams. We identify distinct behaviors associated with this poor group-level performance, including stalling as teams grow, overriding each other's actions, and fabricating claims. We find effective but environment-specific mitigations, such as a team lead, explicit procedural instructions, and a platform check that makes an agent read its peers' messages before committing. We will release the API key, clinic, and personal assistant environments as MAMUBench, comprising 74 scenarios for evaluating multi-user, multi-agent coordination.

</details>


### 88. No One Architecture Fits All: A Cross-Environment Evaluation of Hierarchical Red Team Agents

- **Authors:** Ayan Javeed Shaikh, Arunesh Sinha, Nathaniel D. Bastian, Ankit Shah
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00557v1](http://arxiv.org/abs/2610.00557v1)
- **PDF:** [https://arxiv.org/pdf/2610.00557v1](https://arxiv.org/pdf/2610.00557v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous red team agents increasingly stress-test AI-enabled cyber defenses by planning strategy and executing multistage attacks. Reinforcement learning (RL) and large language models (LLMs) offer complementary mechanisms for the planning and execution such agents require, and prior work has combined them in hybrid hierarchies. Yet a given architecture is typically developed and evaluated within a single environment, leaving open whether an observed advantage reflects a generally stronger decision mechanism or merely alignment with a particular setting. We address this gap with a controlled cross-environment comparison of two homogeneous hierarchical red team architectures: an RL planner with an RL executor (RL+RL) and an LLM planner with an LLM executor (LLM+LLM). We evaluate both against expert autonomous defenders in CybORG CAGE-4 and in Cyberwheel at two network scales, across 18 configurations under one unified disruption metric. We find a pronounced environment-dependent inversion. RL+RL wins the compact, densely rewarded CAGE-4 (78.5% disruption success versus 18.0% for the strongest LLM configuration) and the 100-host Cyberwheel network (81.0% versus 50.5%), while a pretrained cybersecurity LLM agent wins the larger, escalation-gated 1010-host Cyberwheel network (55.0% versus 0.0% for RL). A kill-chain analysis explains the inversion through architecture-specific bottlenecks that aggregate success rates conceal.In the 1010-host Cyberwheel network, RL discovers and compromises hosts but stalls at privilege escalation, whereas in CAGE-4, LLM agents obtain privileged access but rarely convert it into operational impact. These results indicate that conclusions drawn in a single environment may not generalize, and that hybrid planner-executor designs should be motivated by specific failure modes rather than the assumption that one architecture is universally preferable.

</details>


### 89. Multi-agent Auditory Scene Analysis: Improved Localization Speed and Robustness by Multi-beamformed Speech Quality Feedback

- **Authors:** Caleb Rascon
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00538v1](http://arxiv.org/abs/2610.00538v1)
- **PDF:** [https://arxiv.org/pdf/2610.00538v1](https://arxiv.org/pdf/2610.00538v1)
- **Categories:** eess.AS, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A real-time auditory scene analyzer (ASA) aims to carry out the tasks of locating, separating and classifying the sound sources present in a given acoustic environment. Recently, an effort has been made into modelling an ASA as a multi-agent system, with each one of its agents performing one of the aforementioned tasks and communicating their results to the rest of their peer agents. These communication routes are used as feedback loops to fix local errors at a global level, providing robustness while reducing local complexity. An example of the benefits of this approach is the optimization of speech quality by correcting in real-time the estimated location of the speech source of interest. However, their optimization speed has been shown to be considerably slow. One possible reason is that it solely relies on a series of single quality estimations (provided by a reference-free quality estimator model) that vary considerably from one window to the next, which results in a difficult search space to optimize. In this work, a new optimization mechanism is proposed that instead relies on a series of sets of quality estimations over a range of locations, providing a clearer view of the search space, simplifying its optimization. The proposed ASA now has a considerably smaller optimization time, is more accurate, and is more stable when being evaluated in real-life acoustic scenarios to correct higher levels of localization errors, all while being less complex than previous efforts. The only trade-off is that there is an increase in the response time of the quality estimation agent, but the complete ASA is still able to run in real-time. The performance shown in this work again shows the benefits of modelling an ASA as a multi-agent system.

</details>


### 90. EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights

- **Authors:** Jiayi Geng, Zhengxuan Wu, Kevin S. Chen, Seungone Kim, Joseph Janssen, Zora Zhiruo Wang, Bhupalee Kalita, Runtian Gao, Aaron Ho, Andrew Oakleigh Nelson, Olexandr Isayev, Francisco Villaescusa-Navarro, Ching-Yao Lai, Howard Chen, Graham Neubig
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00492v1](http://arxiv.org/abs/2610.00492v1)
- **PDF:** [https://arxiv.org/pdf/2610.00492v1](https://arxiv.org/pdf/2610.00492v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

When Isaac Newton discovered the law of gravitation, he did so through an iterative process of analyzing observed data such as planetary patterns, finding the underlying mechanisms by describing patterns in mathematical equations, and refining his theory against the Moon's orbit, revealing the startling insight that the same force governs both falling apples and orbiting planets. Would it be possible for AI agents to make similar discoveries? To measure this ability, we introduce EurekaBench, a cross-domain benchmark that tests AI agents' ability to conduct long-horizon experiments and discover mechanisms that explain observations. We evaluate these mechanisms by the scientific insights that can be derived from them. EurekaBench contains an expert-verified set of 26 long-horizon tasks across neuroscience, computer science, chemistry, astrophysics, geophysics, and plasma physics, with a total of 306 scientific insights that the discovered mechanisms are expected to support. Our evaluation framework tests three axes of scientific discovery: agents' ability to follow known scientific constraints, the predictive accuracy of the discovered mechanisms, and whether these mechanisms yield scientific insights or inform future research. Our results show that current AI agents often overly fixate on predictive accuracy optimization, surpassing human scientists, while falling substantially short in deriving scientific insights.

</details>


### 91. Cogentic: Multi-Agent Orchestration for Automated Proof Discovery

- **Authors:** Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40324v2](http://arxiv.org/abs/2609.40324v2)
- **PDF:** [https://arxiv.org/pdf/2609.40324v2](https://arxiv.org/pdf/2609.40324v2)
- **Categories:** cs.AI, cs.GT


> Summary unavailable.


<details>
<summary>Abstract</summary>

We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long horizon. Cogentic addresses these challenges through an iterative prove-verify loop in which an orchestrator allocates a population of independent provers across distinct proof directions, subjects their output to adversarial verification by several specialized components, and promotes confirmed intermediate results into a persistent verified ledger that later rounds build on. The harness is designed to be able to solve research-level math and theoretical computer science problems. Using either Gemini 3.1 Pro or an early version of Gemini 4 Argon as the base model, Cogentic produced novel results on open problems across online learning, auction theory, and mechanism design. Each result was independently verified by domain experts and is developed in full in companion papers. We list these results, and new ones as they are verified, at https://sites.google.com/view/cogentic .

</details>


### 92. How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?

- **Authors:** Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40303v1](http://arxiv.org/abs/2609.40303v1)
- **PDF:** [https://arxiv.org/pdf/2609.40303v1](https://arxiv.org/pdf/2609.40303v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Language Model (LLM) primitives, modern MLE agents are deployed on top of increasingly elaborate machinery: multi-agent orchestrators, dedicated retrieval subagents, and more. While such harnesses expand, the use of more primitive but improved coding agents - where LLMs have direct access to the execution environment through read, write, and bash primitives - has received little attention in the field. In this paper we find that, under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art harnesses provide no advantages over a single session of a minimal-harness coding agent baseline, pointing to the backbone as the primary driver for performance. Via a series of large-scale systematic ablation studies, we argue that the machinery layers become redundant in the coding agent setting. We conclude that the effort spent elaborating hand-crafted harnesses around strong models yields poor returns for current MLE benchmarks.

</details>


### 93. Belief-Aware Multi-Agent Path Finding under Map Uncertainty

- **Authors:** Viraj Parimi, Shao-Hung Chan, Han Zhang, Jingkai Chen, Brian Williams
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40269v1](http://arxiv.org/abs/2609.40269v1)
- **PDF:** [https://arxiv.org/pdf/2609.40269v1](https://arxiv.org/pdf/2609.40269v1)
- **Categories:** cs.AI, cs.MA, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-Agent Path Finding (MAPF) aims to find collision-free paths for multiple agents in a shared environment. Classical MAPF assumes that all static obstacles are known in advance, but real-world environments can change unexpectedly due to fallen objects, spills, or other local disturbances. When such changes are spatially correlated, an observation can inform traversability estimates beyond the observed location. Prior approaches address uncertainty in traversability through contingent plans or replanning based on direct observations, but do not leverage this spatial dependence to infer the traversability of nearby unobserved locations. As a result, they cannot use one observation to anticipate nearby unobserved obstacles that may cause costly rerouting later. We focus on Belief-Aware MAPF, where map discrepancies are fixed during execution but initially unknown, and observations can be informative beyond the observed location. We propose Multi-Agent Gaussian belief Inference for Coordination (MAGIC), a framework that updates a shared belief about traversability online based on agents' observations. MAGIC uses a Gaussian Markov Random Field and Gaussian Belief Propagation to approximately infer traversability and construct detour-aware costs for standard MAPF planners. Our experiments on MAPF benchmarks show that MAGIC reduces the executed sum of costs compared to existing approaches on 96.3% of instances, across several planner families and teams of up to 800 agents, demonstrating its applicability to large-scale MAPF problems.

</details>


### 94. PhantomEnvironments: Training LLM Agents in Fictional Worlds

- **Authors:** Anmol Kabra, Swathi Saravana Selvam, Albert Gong, Chao Wan, Christian Belardi, Dongyoung Go, Katie Z. Luo, Kilian Q. Weinberger
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40221v1](http://arxiv.org/abs/2609.40221v1)
- **PDF:** [https://arxiv.org/pdf/2609.40221v1](https://arxiv.org/pdf/2609.40221v1)
- **Categories:** cs.LG, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Training LLM agents with reinforcement learning (RL) is bottlenecked by environments, which must provide verifiable rewards, support long-horizon interaction, and scale cheaply. Existing approaches rely on costly human-curated data or on LLM-generated environments that risk hallucinations and benchmark contamination. We show that LLMs can instead be trained into capable search agents using synthetic environments generated entirely by rules, whose generation requires no LLM and has zero marginal cost. We build PhantomEnvironments, multi-turn RL environments from fictional worlds, where agents must search a corpus of templated articles to answer multi-hop questions. Despite sharing no facts with the real world, these strikingly simple environments yield agents that transfer to real-world multi-hop search benchmarks, often outperforming real-world training data on newer benchmarks. Trained agents generalize to unseen fictional universes, and Qwen models learn to scale their search budget roughly linearly with question difficulty, suggesting emergent search scaling from environment interaction alone. Ablating environment complexity reveals that hop count drives transfer more than constraints or comparisons: even the simplest rule-generated environments are a surprisingly effective, free resource for training generalizable LLM agents.

</details>


### 95. JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces

- **Authors:** Haoyang Su, Weiran Huang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00437v1](http://arxiv.org/abs/2610.00437v1)
- **PDF:** [https://arxiv.org/pdf/2610.00437v1](https://arxiv.org/pdf/2610.00437v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents generate intermediate reasoning and actions token by token, making extended interactions slow and computationally expensive. Jev-style models offer fast probabilistic predictions over finite fields, but require those fields to be specified in advance. This requirement limits autonomous task solving, where the available actions must be derived from natural language instructions and adapted through interaction. We introduce JevSpawn, a compositional policy that connects natural language task specifications to finite probabilistic exploration. Parallel action spawning is coupled with feedback driven branch selection, representation revision, and recovery from retained alternatives. Shared action structure and model prefixes reduce repeated generation and context computation without additional training. Evaluations on eight benchmark tasks against seven agent baselines and a TypeSafe Jev variant establish JevSpawn as a promising approach to structured agentic inference, with improved task performance and faster navigation.

</details>


### 96. How AI Agents Discover Scientific Equations: From Hydrotope Rediscovery to New Water-Wave Amplitudes

- **Authors:** Zihan Zhou, Digvijay Wadekar, Matias Zaldarriaga
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00435v1](http://arxiv.org/abs/2610.00435v1)
- **PDF:** [https://arxiv.org/pdf/2610.00435v1](https://arxiv.org/pdf/2610.00435v1)
- **Categories:** hep-th, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study how AI agents discover and validate scientific formulas using a controlled case study of the hydrotope, a recently discovered geometric formula that combines the different polynomial pieces of nonlinear surface-wave scattering into one global expression. This problem is deceptively difficult: simple formulas can hold within individual frequency regions, but the global result must identify their boundaries and combine exponentially many potentially active terms. We reconstruct how the formula was originally discovered through human--agent collaboration and analyze 18 single-prompt rediscovery runs under no hint and two forms of human guidance: a false hint representing an incorrect prior and a true hint representing domain-informed insight. Only four recover the formula across all kinematic chambers (i.e., regions in which a single polynomial form applies), while most unsuccessful runs find correct chamber polynomials but fail to combine them or test their full domain. Conventional and LLM-assisted symbolic regression and standard machine-learning regressors likewise fail to recover the global formula in our experiments. Guided by these failure modes, we test a PI$+$two-student workflow in which a coordinating lead agent assigns complementary analytic and numerical tasks to two research agents and independently evaluates their results. The PI$+$two-student team successfully rediscovers the complete hydrotope formula, while the same workflow applied to the harder three negative wavenumber problem discovers a new independent verified analytic expression for the six-point amplitude $A_6$.

</details>


### 97. Persistent Context Graphs for Efficient Memory Compaction in LLM Agents

- **Authors:** Jingbo Yang, Kwei-Herng Lai, Xiaowen Wang, Zhaoxuan Tan, Pei Zhou, Mengting Wan, Yaar Harari, Evgeniy Gabrilovich, Shiyu Chang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40118v1](http://arxiv.org/abs/2609.40118v1)
- **PDF:** [https://arxiv.org/pdf/2609.40118v1](https://arxiv.org/pdf/2609.40118v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As LLM capabilities advance, agents are tackling increasingly complex tasks over longer horizons. Their growing interaction histories make memory compaction essential for staying within context windows and reducing prefill cost. Existing methods summarize the history or compress its KV cache, often adding model computation to preserve information for future requests. A new user request can change which history matters, but reassessing that history with the model requires re-encoding it if the KV cache has expired. Past attention provides signals of historical importance and dependencies between messages, while relevance to the current task must be assessed using the new user request. We introduce ReCAP, a memory compaction method that stores attention-derived importance scores and dependency links in a lightweight, persistent context graph. For each new request, ReCAP combines stored importance with relevance cues from the request and follows dependency links to select messages and their supporting context, without additional model calls for selection. Compared with Codex's default summarization-based compaction, ReCAP reduces estimated latency for compaction and cold restoration by approximately 95% on both Qwen3-Coder and gpt-oss. It also roughly halves the historical context per call on SWE-Together at comparable task quality and improves accuracy on the code tasks of Lost-in-Conversation over full history by 19.8 and 41.2 points.

</details>


### 98. Memetic Trojans: Social Contagions as Carriers of Adversarial Payloads in Agent Networks

- **Authors:** Birk Torpmann-Hagen, Finn Schwall, Leon Moonen
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00430v1](http://arxiv.org/abs/2610.00430v1)
- **PDF:** [https://arxiv.org/pdf/2610.00430v1](https://arxiv.org/pdf/2610.00430v1)
- **Categories:** cs.SI, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous large language model (LLM) agents increasingly interact in network environments where adversarial content can propagate between agents. Known attacks include agent worms, which spread through self-replicating prompt injections or configuration compromises. We introduce \emph{memetic trojans}, a distinct class of network-mediated attack that exploits agents' tendencies to retransmit and amplify content. Unlike agent worms, whose propagation is adversarially induced, memetic trojans exploit \emph{endogenous} transmission by embedding adversarial payloads in \emph{social contagions}: content agents have internal reasons to share. As part of our work, we extract social contagions from Moltbook, a social media platform for LLM agents. Controlled transmission experiments reveal large differences in virality: the most effective contagion is retransmitted in approximately 50\% of subsequent agent posts and upvoted at 2.5x the average post's rate. Its memetic trojan counterpart largely inherits these properties. Monte Carlo attack simulations show that memetic trojans amplify expected exposure by up to 3.19x. Network structure and amplification mechanisms strongly shape propagation, producing heavy-tailed outcomes with near network-wide exposure. These results identify endogenous social transmission as a distinct security vulnerability in multi-agent systems. Because propagation does not require agents to follow malicious retransmission instructions, defenses focused on prompt-injection detection or preventing agent compromise cannot alone prevent memetic trojan propagation. Securing large-scale agent ecosystems may require network-level defenses that account for how agent preferences, recommendation mechanisms, and network topology amplify adversarial payloads.

</details>


### 99. Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training

- **Authors:** Kunlun Zhu, Xuyan Ye, Yibo Li, Cheng Qian, Beibin Li, Heng Ji
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40111v2](http://arxiv.org/abs/2609.40111v2)
- **PDF:** [https://arxiv.org/pdf/2609.40111v2](https://arxiv.org/pdf/2609.40111v2)
- **Categories:** cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

An unsuccessful LLM agent rollout contains more information than its final reward: the observations available to the agent, the actions it chose, and the environment's responses. Reusing this experience for learning requires identifying a decision to revise and testing a concrete alternative. We introduce the Agent Error Dataset (AED), comprising 50,228 error-diagnosis pairs from 9,961 source tasks across 33 environments, 19 harness families, and 23 policy models in text-based agent systems. We retain source traces and execution metadata to support cross-setting failure analysis and re-diagnosis without repeating the original rollout. Our five-stage Agentic Error-to-Training (AET) pipeline collects natural failures, generates diagnoses and proposed corrections, and checks them against recorded evidence. Where replay is supported, we compare corrections with original-action retries from the same checkpoint under matched execution settings. We then construct separate training views for diagnosis and actor recovery. Across 3,062 matched replay pairs, first-proposal corrections raise verifier pass rates from 18.4% to 51.1%, a gain of 32.7 percentage points. Using a separately frozen diagnosis release, full-diagnosis fine-tuning on 1,656 source tasks raises Qwen3-8B's exact-step agreement with internal teacher labels from 47.2% to 63.6%, averaged over three seeds on a 943-case holdout. The strongest prompted reference in this comparison scores 54.7%, and mean agreement improves at each of four increasing training-set sizes. In a single-seed comparison of actor-training recipes, action-only repair training scores 6.67 percentage points higher on WebShop-lite than success-only training.

</details>


### 100. JuryFlow: Disagreement-Guided Human-in-the-Loop Multi-Agent Evaluation

- **Authors:** Mufeng Yang, Junwei Yu, Yepeng Ding
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40103v1](http://arxiv.org/abs/2609.40103v1)
- **PDF:** [https://arxiv.org/pdf/2609.40103v1](https://arxiv.org/pdf/2609.40103v1)
- **Categories:** cs.CL, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as automated judges for AI-generated content, yet a single judge is unreliable and even a panel of judges leaves a hard residue: when judges disagree, majority voting discards the conflict instead of resolving it. We present JuryFlow, a disagreement-guided, human-in-the-loop multi-agent evaluation framework that treats inter-judge disagreement not as noise to be averaged away, but as a precise, claim-level signal indicating where an evaluation is uncertain. JuryFlow decomposes each candidate response into atomic claims, has a panel of heterogeneous judges assign per-claim verdicts, and builds a disagreement graph whose nodes are scored by verdict entropy and whose edges encode structural similarity between claims. A human acts as a structural guide, selecting which disagreement to resolve through a single, minimal intervention rather than re-labeling the response, after which the focal claim is re-evaluated, the correction propagates along graph edges and to historically similar cases, and is crystallized into reusable rubric entries that all judges inherit, making the evaluator progressively self-refining. To enable large-scale, reproducible benchmarking without human studies, we evaluate JuryFlow in an automatic configuration in which focal selection is made by entropy ranking. On MT-Bench and LLMBar, JuryFlow improves agreement with gold labels over single-judge and majority-vote panel baselines, and ablations isolate the contributions of disagreement-targeted re-evaluation, propagation, and rubric induction. We contribute (1) a human-in-the-loop paradigm that recasts the human from labeler to structural guide, (2) the JuryFlow framework operationalizing it through a disagreement graph, focal re-evaluation, and closed-loop rubric induction, and (3) an evaluation protocol with ablations that isolate where the gains originate.

</details>


### 101. Who Verifies the Graph? Misspecification Attacks on Causal Action Verification for Language Agents

- **Authors:** Fabio Rovai
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.40027v1](http://arxiv.org/abs/2609.40027v1)
- **PDF:** [https://arxiv.org/pdf/2609.40027v1](https://arxiv.org/pdf/2609.40027v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Causal action verifiers gate an agent's state-changing tool calls by checking whether each proposed intervention is identifiable against a committed action-state graph, and they issue a certificate that carries the identification argument and a one-sided lower confidence bound. One such verifier, CIVeX, reports zero false executions on a confounded tool-use benchmark. We red-team it by corrupting only the committed graph. Omitting a single bidirected edge takes it from zero false executions to 15.3% at the benchmark's published confounding strength, with 91% of its executions harmful and utility falling from +2.27 to +0.35. Reversing one arrowhead, so that a mediator is committed as a confounder, gives 48.9% false executions and no correct ones. Every one of these actions carries an internally valid certificate. An attestation step that tests each observationally certified execution against a bounded randomised sample detected both attacks, with 2 false alarms in 555 executions on a truthful graph; refusing what fails the test, or cannot be tested, gave zero false executions in every setting we measured. It does not restore beneficial execution: at the published strength 97.1% of beneficial actions are still never executed, because the same misspecification rejects them before attestation runs. Those rejections carry certificates too, and auditing them works, but its cost scales with the number of rejections rather than the number of executions. Recovering safety costs 127 experiments per 1,050 actions; recovering the lost value costs 614 more, at which point the audited verifier makes the honest graph's decisions on every instance and spends exactly its experiment budget. An audit that inspects only executions protects against wrongful action. Wrongful inaction has to be paid for separately.

</details>


### 102. What Can Component-Replacement Evidence Establish? A Critical Scoping Review of Local Decisions in LLM Agents

- **Authors:** Shuyang Zhang, Jianshuo Chang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39989v1](http://arxiv.org/abs/2609.39989v1)
- **PDF:** [https://arxiv.org/pdf/2609.39989v1](https://arxiv.org/pdf/2609.39989v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Background. A component replacement in a language-model agent changes an execution trajectory, potentially altering later observations, resource use, and recovery opportunities. Different evidence is needed to assess its task-level benefit and the contribution of local decision quality. Methods. This critical scoping review maps 348 studies and examines 90 comparison records: 88 from 40 included studies and two from supplementary studies. Eight purposively selected cases structure the synthesis around the replaced decision, executed conditions, measurement comparability, controls, and remaining explanations. Results. Of 222 studies reporting local decision metrics, 142 also report measured task endpoints and 49 report proxies. These counts identify studies that report both types of measurement, without establishing that the measurements come from matched comparisons. Outcome Monitors reports a package-level completion gain whose attribution to detector quality remains limited; First-chunk selection reports a local improvement assessed against an offline proxy endpoint; Evidence-Carrying Termination reports fewer premature unsupported terminations and completion non-inferiority, without establishing completion superiority. Cross-case analysis identifies three candidate mechanisms involving recovery and disruption, intervention timing, and downstream use. Attribution and deployment depend on the comparison controls, label definitions, and information available to the controller. Conclusions. The review distinguishes the task-level benefit of a component replacement from the contribution of local decision quality and derives eight claim-specific reporting items. Neither online execution nor simultaneous gains in local and task metrics alone establish that better local decisions explain the task-level gain.

</details>


### 103. AIMS: An Agentic AI Framework for Sim-to-Real Multi-Modal ISAC

- **Authors:** Yijie Bian, Kai Zhang, Wei Guo, Zixin Wang, Shenghui Song, Jun Zhang, Khaled B. Letaief
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39964v2](http://arxiv.org/abs/2609.39964v2)
- **PDF:** [https://arxiv.org/pdf/2609.39964v2](https://arxiv.org/pdf/2609.39964v2)
- **Categories:** cs.AI, cs.MA, eess.SP


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-modal integrated sensing and communication (ISAC) enables environmental perception and reliable connectivity for intelligent wireless networks. Data-driven multi-modal ISAC models depend heavily on annotated real-world data to learn relationships across sensing and wireless observations, thereby constraining scalable deployment. Although synthetic data generation reduces the burden, adapting existing simulation pipelines to a target deployment requires consistent scene, sensing, wireless, and learning configurations, while mismatches among these coupled components impair sim-to-real transferability. To address the challenge, we propose an agentic artificial intelligence (AI) framework for sim-to-real multi-modal ISAC, named AIMS. Given a natural-language deployment request specifying the target task, deployment conditions, and real-data budget, AIMS derives a deployment-specific sim-to-real configuration and coordinates its execution to produce a deployment-specific task model. A two-agent architecture coordinates scene construction with task learning. A scene construction agent generates geographically grounded, synchronized sensing and wireless records from shared physical states, while a scene understanding agent configures task-relevant modalities and mixture-of-experts (MoE) learning for zero-shot inference or few-shot adaptation. Structured domain knowledge guides dependency-aware planning, while validation evidence supports feedback-driven revision of affected decisions. Experiments on the real-world DeepSense 6G dataset demonstrate improved vehicle detection and beam prediction over the considered simulation and fusion baselines. A separate orchestration benchmark evaluates task interpretation, dependency reasoning, and feedback-driven replanning across diverse deployment requests, showing improved plan correctness with structured domain knowledge and validation feedback.

</details>


### 104. Solving Multi-Agent Sokoban via LaCAM

- **Authors:** Keisuke Okumura
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39889v1](http://arxiv.org/abs/2609.39889v1)
- **PDF:** [https://arxiv.org/pdf/2609.39889v1](https://arxiv.org/pdf/2609.39889v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Sokoban, a puzzle game in which an agent pushes boxes onto unlabelled target locations in a grid world, is a long-standing benchmark planning problem. While it is easy to see the connection to practical applications such as warehouse logistics with autonomous forklifts, its multi-agent counterpart has remained underdeveloped. This is because Multi-Agent Sokoban is substantially more difficult due to factors specific to multi-agent planning, such as the rapidly growing branching factor as the number of agents grows and the need to handle integrated task assignment and collision-free pathfinding. In this paper, we show that a scalable planner for Multi-Agent Sokoban can be designed by leveraging recent advances in multi-agent pathfinding (MAPF). Specifically, our Sokoban-LaCAM efficiently solves instances involving tens of agents and boxes while preserving both completeness and eventual optimality guarantees. This provides evidence that MAPF can serve as a powerful primitive for solving broader collective automation problems.

</details>


### 105. Safety of Latent Communication in Multi-Agent Systems

- **Authors:** Muhammad Huzaifa, Sina Mavali, Thorsten Eisenhofer
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39788v2](http://arxiv.org/abs/2609.39788v2)
- **PDF:** [https://arxiv.org/pdf/2609.39788v2](https://arxiv.org/pdf/2609.39788v2)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Latent communication enables multi-agent systems to exchange information directly in internal representation space, reducing the token, computation, and latency overhead of text-based communication. To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input space. In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged. An attacker can amplify this effect by optimizing the links on harmful query--response pairs or poisoning otherwise benign training data. We further develop a reinforcement-learning attack that rewards harmful compliance alongside benign task performance without requiring harmful target responses. Across three communication topologies and four safety benchmarks, this attack raises the mean harmful-compliance score from 27.9 with benignly trained links to 76.9. Compared with direct supervised optimization, it also achieves higher average accuracy on two benign utility benchmarks. Adapting the rewards toward safer behavior also enables repair of compromised links, substantially reducing harmful compliance across all evaluated attacks without updating the agents. Overall, our results show that safety alignment requires considering the multi-agent system as a whole. Code: https://github.com/Muhammad-Huzaifaa/latent-safety

</details>


### 106. GraphMAS: A Systematic Benchmark of Multi-Agent Coordination for Graph Learning

- **Authors:** Jiayi Yang, Yifang Chen, Yuanfu Sun, Xinyan Ge, Qiaoyu Tan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39777v1](http://arxiv.org/abs/2609.39777v1)
- **PDF:** [https://arxiv.org/pdf/2609.39777v1](https://arxiv.org/pdf/2609.39777v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based multi-agent systems coordinate specialized reasoning through aggregation, interaction, and adaptive control, yet their potential for graph learning remains unexplored. Graph learning is a natural setting for such systems because useful evidence may arise from heterogeneous local, long-range, global structural, and semantic perspectives whose relevance varies across instances. Existing LLM-based graph learning approaches primarily rely on single-agent reasoning, while multi-agent coordination has been studied mainly in general reasoning settings. Consequently, it remains unclear whether multiple specialized agents can improve graph learning and how coordination strategies should be designed and evaluated. To address this gap, we introduce GraphMAS, a systematic benchmark of multi-agent coordination for graph learning. GraphMAS builds a shared pool of graph reasoning specialists and organizes coordination along two dimensions, inter-agent interaction and runtime adaptivity, yielding four paradigms and seven representative coordination methods. Under a unified protocol, we evaluate these methods across seven text-attributed graphs, three domains, and two graph learning tasks. We find that heterogeneous graph perspectives are complementary, and that coordinating specialists improves over individual specialists and single-agent graph reasoning, with gains from decomposing reasoning across specialists rather than from broader evidence access alone. However, richer inter-agent interaction does not reliably help, whereas instance-adaptive specialist selection yields the strongest accuracy-efficiency trade-off. We further show that coordination can be learned over a fixed specialist pool and transfers to held-out graphs. GraphMAS therefore provides a controlled evaluation framework and empirical principles for understanding when and how multi-agent coordination benefits graph learning.

</details>


### 107. Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents

- **Authors:** Serhii Zabolotnii
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39717v1](http://arxiv.org/abs/2609.39717v1)
- **PDF:** [https://arxiv.org/pdf/2609.39717v1](https://arxiv.org/pdf/2609.39717v1)
- **Categories:** cs.AI, cs.CY, cs.SE


> Summary unavailable.


<details>
<summary>Abstract</summary>

Benchmarks, audits, and agent protocols describe performance, permissions, and repair, but not how observed evidence should change an agent's authority during a consequential task. We call this the assurance-transition gap. We propose a Runtime Assurance Contract (RAC), a policy-level formal schema binding autonomy boundaries, component eligibility, evidence state, transition policy, human-review capacity, and non-compensatory gates. Under RAC, soft metrics may inform routing, whereas a failed or unknown mandatory gate forces retry, switch, escalation, deferral, or stop; aggregate performance cannot authorize action. We define the contract, an evidence record, a permission rule, and five invariants, and illustrate them in clinical, industrial, and judicial failure probes. We then report a deterministic failure-injection study in agentic coding: 280 constructed cases evaluated by a gate conjunction, a score-only rule, and a restricted protocol baseline. At the published example weights and threshold, the score rule admits 80 of 100 block-required injections and all 40 review-required injections. Tuned in hindsight, it matches the conjunction on this corpus. For positive weights, a positive threshold, binary risk signals, zero-signal controls, and an injected case firing each signal alone, we show that exact agreement holds if and only if the threshold does not exceed the smallest weight. A separate set of 18 hand-authored traces checks version-pinned evidence and review transitions against simpler policy variants. In a further prospective synthetic holdout of 24 episodes, two blinded LLM judges assign identical labels to all 72 action attempts; RAC and a separately implemented full stateful baseline both match these labels. These studies test mechanisms on synthetic cases; they establish neither deployed safety nor cross-domain effectiveness.

</details>


### 108. SEPAL: Separated Expert Pairs with Answer-Level Fusion for Reliable LLM Collaboration

- **Authors:** Weijie Ren, Yanwen Zhang, Hao Li, Zhuolin Qi, Hengyi Zhang, Naibo Wang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39645v1](http://arxiv.org/abs/2609.39645v1)
- **PDF:** [https://arxiv.org/pdf/2609.39645v1](https://arxiv.org/pdf/2609.39645v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent collaboration lets large language models (LLMs) improve question answering through deliberation and feedback. Yet shared discussion couples correction with exposure to the same mistakes, which can erode the diversity needed for voting. Self-consistency offers sampling diversity without feedback, while single-pair Actor-Critic collaboration refines only one candidate. We introduce SEPAL, which assigns three private Actor-Critic teams to direct reasoning, evidence grounding, and verification. Role-specific training gives the teams different reasoning objectives beyond sampling variation. Each Critic guides revisions within its own team, preventing feedback from carrying errors across candidates. Once revision ends, majority voting combines only the final answers, keeping the reasoning histories separate until the decision. Across five open-weight backbones and five question-answering benchmarks, SEPAL improves mean accuracy by 1.81 percentage points over a matched single Actor-Critic pair, with improvements across all five backbones. Code is available at https://github.com/zhansan114514/SEPAL.

</details>


### 109. Prediction is Better than Detection: Traffic Congestion Control using Drones

- **Authors:** Samira Hayat, Christian Raffelsberger
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39637v1](http://arxiv.org/abs/2609.39637v1)
- **PDF:** [https://arxiv.org/pdf/2609.39637v1](https://arxiv.org/pdf/2609.39637v1)
- **Categories:** cs.RO, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

A central question in deploying teams of mobile robots for persistent monitoring is how task performance scales with fleet size, and whether this scaling holds once sensing drives downstream action rather than mere observation. We study this question for a team of drones performing traffic-jam detection and prediction in a simulated road network, whose reports drive an adaptive traffic-signal controller in closed loop. We build a multi-agent simulation, with vehicles following Nagel-Schreckenberg cellular-automaton dynamics and drones patrolling junctions via a round-robin policy, and sweep fleet size, traffic level, and network size to evaluate detection rate, detection delay, and prediction rate. We show how performance plateaus for fleet size approximating the number of junctions being monitored, and offer a general fleet-provisioning rule for persistent-monitoring deployments. More significantly, adapting the signal on a predicted jam, rather than a detected one, roughly doubles the resulting reduction in jam duration, showing that the value of onboard prediction in a sensing-to-action pipeline can exceed the value of adding more robots. Prediction accuracy, not sensing coverage, is now the binding constraint on further improvement, pointing to onboard inference, not fleet size, as the more promising direction for future work.

</details>


### 110. Representation Transitions Reveal Emerging Safety Risks in Multi-Turn LLM Agents

- **Authors:** Haoyu Wang, Wei Zhao, Yedi Zhang, Christopher M. Poskitt, Jun Sun
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00400v1](http://arxiv.org/abs/2610.00400v1)
- **PDF:** [https://arxiv.org/pdf/2610.00400v1](https://arxiv.org/pdf/2610.00400v1)
- **Categories:** cs.LG, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-turn attacks on agentic systems can compose individually permissible actions into harmful outcomes, challenging defenses that assess actions or states in isolation. We show that such attacks leave a detectable signature in the agent's internal representations: harmful behavior emerges as an accumulated representation transition across context updates, whose triggering context can be identified from the same signal. We further find that naive aggregation is confounded by benign representation drift, as a contrastive safety direction need not assign zero to benign transitions. We address this by denoising the direction, anchoring benign traffic at zero and removing its leading variation directions, with no runtime cost.
  These findings motivate DART, a runtime framework that detects and attributes representation shifts and intervenes with targeted reminders. Across six models and two multi-turn benchmarks, DART reduces attack success from 84% to 25% on MT-AgentRisk, catching every attack at a mean false-alarm rate of 12%, and from 97% to 52% on ASEval, at costs in benign non-refusal of 8% and 0%, respectively. On MT-AgentRisk, it outperforms ToolShield, the state-of-the-art multi-turn defense, on all six models: under the same protocol, ToolShield reaches only 55%. Denoising is critical: on ASEval, the undenoised monitor catches only 7%-40% of attacks, while the denoised monitor catches 60%-85%. The same monitor covers single-turn indirect injection without modification and adds only 0.14-0.56 s overhead per monitored step without requiring an auxiliary model, making it a lightweight complement to computation-heavy speculative defenses.

</details>


### 111. Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents

- **Authors:** Tobias Kaisar, Aritra Dhar
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39607v1](http://arxiv.org/abs/2609.39607v1)
- **PDF:** [https://arxiv.org/pdf/2609.39607v1](https://arxiv.org/pdf/2609.39607v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Skills extend an agent's capabilities by injecting instructions and information into the context, and are widely used by agents such as OpenClaw and Claude Code. Prior work shows third-party marketplaces host malicious skills that give attackers direct influence over the victim's agent. The emerging defense scans skills before installation, pairing deterministic static checks with an LLM-based semantic judge, as in NVIDIA's SkillSpector. We show that such defenses fall to an attacker who knows the detector. Our white-box LLM attacker, Pretext, iteratively crafts skills that evade detection while still delivering the payload and performing the benign task: moving the payload from code into natural language leaves static analysis inert, while framing it as the skill's legitimate purpose and splitting instructions across files keeps the LLM stage below its blocking threshold. Across three open-source models, Pretext achieves up to 97\% and 77\% against a frozen detector and a co-adaptive one, respectively, revealing major gaps in current skill scanners.

</details>


### 112. Divide and Collapse: MAPF-Collapse via Exact Decomposition into Independent Sub-Instances

- **Authors:** Oren Salzman
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39559v1](http://arxiv.org/abs/2609.39559v1)
- **PDF:** [https://arxiv.org/pdf/2609.39559v1](https://arxiv.org/pdf/2609.39559v1)
- **Categories:** cs.AI, cs.RO


> Summary unavailable.


<details>
<summary>Abstract</summary>

In this work we study the problem of MAPFC, a post-optimization step for Multi-Agent Path Finding (MAPF) plans where we are given a feasible plan produced by a modern MAPF solver and are tasked with removing avoidable moves while preserving feasibility. This NP-hard problem naturally arises when using learning-based state-of-the-art (SOTA) solvers which construct plans that contain redundant moves that can be removed. Recently, Tang et al. presented Judgelight, which uses Integer Linear Programming (ILP) to solve MAPFC. Importantly, the ILP is constructed over all agents jointly, so its cost is governed by the full instance rather than by the small coupled residue that actually requires joint reasoning. Our key insight, motivating this work, is that MAPFC instances naturally decompose into independent sub-problems, most of which involve a single agent and can be solved without any inter-agent reasoning. To this end, we first identify which agents need to coordinate their motion and partition the instance into sub-problems accordingly. For the cases where no coordination is required, we introduce an extremely lightweight solver that is $\approx\!1{,}900\times$ faster than Judgelight. For cases where coordination is required, Judgelight can be used but we introduce an alternative CBS-like solver which is more efficient on easier problems. The resulting framework is exact, uses no commercial ILP solver, and matches Judgelight's quality while running substantially faster on the coordination-light majority of instances; on the coordination-heavy instances we propose a regime-aware hybrid planner that falls back to Judgelight. Over all benchmarks tested, this planner achieves a median $10.5\times$ per-instance speedup over Judgelight.

</details>


### 113. RankEvolve: A Reliable Multi-Agent Auto-Research Harness for Evolving Ranking Models

- **Authors:** Zheng Chen, Linfeng Liu, Hong Li, Hong Yan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39551v1](http://arxiv.org/abs/2609.39551v1)
- **PDF:** [https://arxiv.org/pdf/2609.39551v1](https://arxiv.org/pdf/2609.39551v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Auto-research agents, LLM systems that propose, implement, train, and evaluate model changes across iterations, promise to automate applied ML's experimental loop. Over long horizons, execution accuracy is a binding constraint: a change can silently leak held-out data, omit normalization, disconnect a gradient, or leave a train/eval flag unwired, invalidating expensive runs and compounding error across iterations. We present RankEvolve, an auto-research framework for evolving generative ranking models. An Executable Operating Protocol (EOP) declares phases, gates, branches, and loops, and the runtime enforces the compiled state machine. A meta-meta-harness composes complete black-box coding-agent products, including Claude Code and Codex, as execution-graph nodes that review and repair one another's work. In a budget-matched evaluation, heterogeneous composition raises all-oracle execution accuracy from the best single-product baseline of 45.8 percent to 62.5 percent (paired +16.7 points, 95 percent CI [6.6, 26.7]) while achieving a 10.4 percent silent critical-defect rate. An implemented knowledge layer carries findings, including negative results, across iterations. In a twelve-iteration deployment on the open-source HSTU recommender, RankEvolve reported NDCG@10 of 0.2192 on MovieLens-20M LARGE (+4.48 percent over the published anchor) and 0.1948 on BASE (+2.80 percent). ExecML-HSTU, seeded by incidents from that deployment, provides the oracle benchmark for the execution-accuracy evaluation. A pre-specified LitGPT transfer split replicates the heterogeneous-composition effect beyond recommendation (+12.5 points, 95 percent CI [3.0, 22.0]), and a paired ablation isolates per-step from full-protocol instruction injection. These results characterize when runtime-controlled composition of coding-agent products improves execution accuracy.

</details>


### 114. Speculative Safety Honeypot: Toward Proactive Defense Against Multi-turn Agent Attacks

- **Authors:** Zezhong Wang, Xueyang Tang, Rui Lian, Yang Lou, Heqing Huang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39549v1](http://arxiv.org/abs/2609.39549v1)
- **PDF:** [https://arxiv.org/pdf/2609.39549v1](https://arxiv.org/pdf/2609.39549v1)
- **Categories:** cs.CR, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As Large Language Model (LLM) agents are increasingly deployed in complex environments, multi-turn interaction attacks have become a significant security challenge. Existing detection methods typically rely on historical context. However, this retrospective logic struggles to identify deep malicious intents that are split across turns to hide future risks. Inspired by speculative decoding, we propose the Speculative Safety Honeypot (SSH) framework. SSH uses a multi-agent simulation system composed of small LLMs to build an action-level speculate-and-verify workflow. In the speculation stage, SSH predicts future behaviors of the target agent and asynchronously builds a trajectory tree to expose potential risks in advance. In the verification stage, the system uses the target agent's real actions to calibrate and prune the trajectory tree, effectively reducing false positives. As a plug-and-playable component, SSH provides existing detectors with rich decision redundancy beyond the current interaction slice. By judging risk based on the evolution of the entire trajectory tree rather than a single point in time, the system reduces the reliance on the absolute precision of individual detection components. This improves the defense resilience and the warning lead-time of agent systems against complex temporal attacks.

</details>


### 115. Beyond the Shadows of Plato's Cave: Evaluating False Memory in Autonomous Agents via Counterfactual Reasoning

- **Authors:** Quan M. Tran, Zhuo Huang, Zhen Fang, Jing Zhang, Mingming Gong, Tongliang Liu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39473v1](http://arxiv.org/abs/2609.39473v1)
- **PDF:** [https://arxiv.org/pdf/2609.39473v1](https://arxiv.org/pdf/2609.39473v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents increasingly rely on memory to generalize beyond their training environments. However, agents are bounded by what they have seen and believed, and leveraging such memories in unseen environments can introduce biases into their internal beliefs. We formalize this phenomenon as \textit{false memory}, which can arise from spurious correlations, environment shifts, and knowledge conflicts. Despite its importance, false memory is difficult to evaluate because it stems from agent internal beliefs and is easily confounded with ordinary generalization failures. Therefore, we propose FAME, a training-free framework that evaluates false memory through the evolution of agent beliefs under counterfactual reasoning. Specifically, counterfactual scenarios reveal how beliefs change as the latent concept of memory shifts under hypothetical interventions; thus, measuring the resulting concept drift provides a signal for distinguishing faithful versus false memory. Such concepts can be estimated from agent hidden states before answer generation, avoiding the need for reward design or answer sampling. Empirical experiments reveal that simply monitoring answers often fails to detect false memory, while FAME achieves AUROCs of 76.2% - 96.7% across false-memory settings, and outperforms the best baseline by 3.4% - 23.3% across realistic benchmarks, spanning math reasoning (GSM-Symbolic), code generation (GitChameleon), and complex reasoning (BigBench-Hard). We further release corresponding counterfactual templates and facilitate future research on false memory.

</details>


### 116. ActionGuard: Tool Call Authorization under Poisoned Skills

- **Authors:** Jihun Han, Yejin Jang, Byung Il Kwak, Mee Lan Han
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39450v1](http://arxiv.org/abs/2609.39450v1)
- **PDF:** [https://arxiv.org/pdf/2609.39450v1](https://arxiv.org/pdf/2609.39450v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM-based agents extend their capabilities through third-party skills that provide task-specific instructions, scripts, and tool-use procedures. However, malicious instructions inserted into an otherwise benign skill can cause a benign user request to trigger dangerous Tool Calls, including data exfiltration, file deletion, or unauthorized code execution. This paper presents ActionGuard, which inspects skill-influenced Tool Calls immediately before execution. ActionGuard separates the target agent's action-generation context from the safeguard's authorization context. The target agent may use the original skill for planning, but the Reviewer does not receive the potentially poisoned raw skill text. Instead, it determines whether each action is justified by the trusted user request using a balanced skill profile, current and recent Tool Calls, and local script contents. ActionGuard intercepts each Tool Call at OpenClaw's before-tool-call stage and enforces the Reviewer's ALLOW or DENY decision under a fail-closed policy.
  We evaluate ActionGuard on 139 contextual and 180 obvious injections in a SKILL-INJECT-based setting against Dynamic Guardian and SkillGuard, using three open-source and two commercial Reviewer models. Each condition is repeated three times and evaluated using Attack Success Rate (ASR) and Task Success Rate (TSR). Overall, ActionGuard reduced ASR by 35.54 to 46.11 percent relative to existing safeguards and by 70.44 percent relative to No Safeguard, while maintaining high benign-task completion. These results show that execution-boundary authorization grounded in trusted user intent and runtime evidence can restrict unauthorized Tool Calls induced by skill injection.

</details>


### 117. SkillFM: Generating Skills for LLM Agents via Latent Flow Matching

- **Authors:** Zuming Zhang, Jie He, Yizhe Zhang, Jeff Z. Pan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39382v1](http://arxiv.org/abs/2609.39382v1)
- **PDF:** [https://arxiv.org/pdf/2609.39382v1](https://arxiv.org/pdf/2609.39382v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Textual skills provide reusable guidance for large language model agents, but existing approaches often rely on manually curated skill banks or reinforcement learning with indirect and delayed feedback. We introduce SkillFM (Skill Flow Matching), a generative framework that synthesizes task-conditioned textual skills directly without test-time skill retrieval. Our framework combines a codec for encoding and reconstructing textual skills in a continuous latent space with a conditional flow model trained using improved MeanFlow. At inference time, the learned velocity field enables single-step latent sampling, and an LLM-based decoder converts the sampled representation into textual guidance for a frozen downstream agent. We evaluate the framework on embodied tasks, question answering, and web shopping. On ALFWorld and Search-QA, our method achieves the best overall performance among the compared vector-based skill approaches. Our analyses further demonstrate that latent skill generation is an effective alternative to retrieval-based skill augmentation. Our code and training skill libraries are available at https://github.com/lulushang999/SkillFM.

</details>


### 118. Rethinking Multi-Image Re-Representation in Multi-Image Understanding

- **Authors:** Gengyuan Zhang, Xiao Han, Xinyu Xie, Tong Liu, Volker Tresp
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39363v1](http://arxiv.org/abs/2609.39363v1)
- **PDF:** [https://arxiv.org/pdf/2609.39363v1](https://arxiv.org/pdf/2609.39363v1)
- **Categories:** cs.CV, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-image understanding requires MLLMs not only to recognise the content of individual images, but also to organise visual evidence distributed across them. We study this problem through multi-image re-representation, viewing prompted Chain-of-Thought reasoning and agentic visual tool use as different ways of re-organising visual evidence during reasoning. We introduce Mosaic, a general-purpose multi-image visual harness that enables an MLLM to actively construct visual intermediates with ten composable image operations. We compare five re-representation settings on existing multi-image benchmarks and on MosaicBench, a new grounding-focused benchmark for fine-grained multi-image understanding. Our experiments show that the relative benefits of textual and visual re-representation are strongly task-dependent. Visual re-representation is particularly effective for tasks requiring precise visual evidence, including hypothesis testing, precision comparison, and orientation-sensitive reasoning, while tasks dominated by higher-level semantic content show smaller or less consistent gains. Building on this finding, we train MosaicAgent-8B to use Mosaic with reinforcement learning using only accuracy and format rewards. Without demonstration trajectories or rewards for specific tool-use, the agent learns to compose visual operations over multiple steps and exhibits diverse problem-solving patterns unpromptedly. Code and data will be released at https://github.com/gengyuanmax/Mosaic.

</details>


### 119. Hiding in Plain Sight: Decoupling Pretext from Actuation for Skill Poisoning in LLM Agents

- **Authors:** Wenxin Wu, Lingyong Yan, Lei Sha, Shuaiqiang Wang, Jiashu Zhao
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39352v1](http://arxiv.org/abs/2609.39352v1)
- **PDF:** [https://arxiv.org/pdf/2609.39352v1](https://arxiv.org/pdf/2609.39352v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on reusable Skills for complex, multi-step tasks, creating a critical supply-chain attack surface where poisoned Skill content steers agent decision loops under benign requests. Existing skill poisoning attacks either colocate actuation with its contextual pretext or distribute actuation across multiple Skills, but do not explicitly separate the rationale for execution from the operation itself. In this work, we reveal that untrusted agent decisions fundamentally depend on two conceptually distinct Risk-Realization Factors (RRFs): an actuation factor (specifying what concrete operation is performed) and a pretext factor (providing the situational rationale for why the agent must perform it). Guided by this abstraction, we propose a coordination-based attack paradigm: decoupling pretext from actuation. Rather than fragmenting the malicious actuation, we preserve it as an intact operation within a downstream Steering Skill, while delegating the pretext factor to an upstream Grounding Skill that subtly alters persistent environment artifacts through routine utility operations. The intact actuation thus hides in plain sight, appearing completely legitimate and task-driven only when evaluated against the fabricated pretext. Building on this formulation, we develop an automated framework that discovers authentic execution dependencies, synthesizes coordinated pretext-actuation skill pairs, and iteratively refines poisoned skill instructions via runtime closed-loop feedback. Extensive evaluations across single-session and persistent cross-lifecycle scenarios demonstrate that decoupled skill poisoning achieves high attack success, exposing a critical blind spot in isolated Skill security audits. Our automated framework code is available at https://github.com/Wenxin-buaa/CoordPoison.git.

</details>


### 120. NarrativeSteward: Coordinating Delegation, Guidance, and Verification in Agent-Assisted Interactive Narrative Authoring

- **Authors:** Wenjin Wang, Jiazhen Lei, Yuxin Sha, Nuwa Xi, Meng Zhao, Xingxi Yin, Qi Liu, Yuliang Shen, Zixun Sun
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39333v1](http://arxiv.org/abs/2609.39333v1)
- **PDF:** [https://arxiv.org/pdf/2609.39333v1](https://arxiv.org/pdf/2609.39333v1)
- **Categories:** cs.HC, cs.AI, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous AI agents can turn authors' goals into interactive narratives by independently organizing and carrying out generation and revision. As agents generate and revise extensive content, authors struggle to grasp its overall structure, local details, and relationships, complicating continued guidance. We present NarrativeSteward, an authoring environment that organizes outlines, worldbuilding, and narrative graphs as linked artifacts for agent implementation and author guidance. Agent dialogue and project-wide structural review help authors understand the evolving work and guide local and cross-layer revisions, while change records and execution verification help authors assess the resulting work. Technical tests validated the system's change records, recovery mechanisms, and execution diagnostics. In a 12-participant within-subject study, NarrativeSteward supported easier formulation of revision requests and inspection of changes, and greater perceived understanding of changes and story structure, than general-purpose agents. Qualitative findings show how reviewing the work and feedback helps authors develop requirements and guide subsequent delegation. We open-source NarrativeSteward at https://github.com/Tencent/NarrativeSteward.

</details>


### 121. ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation

- **Authors:** Shengjie Jin, Hengbo Xu, Zelong Sun, YuJie Guo, Zhiwu Lu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39306v1](http://arxiv.org/abs/2609.39306v1)
- **PDF:** [https://arxiv.org/pdf/2609.39306v1](https://arxiv.org/pdf/2609.39306v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving PI-conditioned behavior as the student becomes the next teacher. We introduce Retentive and Selective Augmentation for Iterative Self-Distillation (ReSAIL), a plug-in augmentation for iterative PI-based self-distillation. ReSAIL selects interaction steps where PI most strongly changes the teacher's predictions and balances the resulting distillation losses across trajectories. It also regularizes the student's PI-conditioned output distributions toward those of the frozen teacher at selected and unselected steps to preserve PI-conditioned behavior for supervision in the next cycle. On ALFWorld and TextCraft, ReSAIL sustains substantial gains across model scales over three cycles, with an average absolute gain of 22.5% in final-cycle success rates when added to self-distillation baselines. Sensitivity-guided selection of offline data also improves action prediction accuracy for multimodal GUI agents on AITZ. These findings provide the first evidence that a more robust learning mechanism can effectively mitigate performance collapse in iterative agent self-distillation over deployment trajectories.

</details>


### 122. MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate

- **Authors:** Jiaming Zhang, Yuwan Liu, Yue Huang, Sisi Duan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39297v1](http://arxiv.org/abs/2609.39297v1)
- **PDF:** [https://arxiv.org/pdf/2609.39297v1](https://arxiv.org/pdf/2609.39297v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Autonomous agents powered by large language models (LLMs) are rapidly evolving into an open agentic ecosystem. To support trustworthy collaboration, industry initiatives increasingly assess agent reputation from past behavior and provide performance leaderboards. However, reputation derived from past performance may not reliably predict an agent's behavior on new tasks, particularly when malicious agents can adapt their behavior and influence other agents during collaboration.
  We study reputation in multi-agent debate (MAD), where multiple agents answer the same query, debate to improve their answers, and aggregate them into a final output. We present MiniRep, a reputation-based aggregation system for MAD under malicious agents. To ground our threat model in established research, we construct an attack taxonomy drawing on reputation-system attacks and software-testing mutation operators, covering strategic exploitation of reputation and subtle corruption of agent proposals. Guided by this taxonomy, MiniRep evaluates agents based on both their behavior on the current task and their reputation over time, while preventing groups of agents with highly similar responses from dominating the final decision. We assess MiniRep across diverse tasks, LLM-agent compositions, corruption placements, and attack types drawn from our taxonomy. Our experimental results show that, MiniRep outperforms both conventional MAD aggregation and conventional reputation-based approaches on MATH no matter being attacked or not. Also, under a heterogeneous 10-agent setting on MATH, MiniRep outperforms all baselines in all 28 attack conditions.

</details>


### 123. EngramBench: A Capability-Grounded Benchmark for Skill-Evolution Harnesses

- **Authors:** Zhixuan Tan, Pengjie Gu, Zhao Li, Yihan Hu, Xu He, Dong Li, Jianye Hao
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39284v1](http://arxiv.org/abs/2609.39284v1)
- **PDF:** [https://arxiv.org/pdf/2609.39284v1](https://arxiv.org/pdf/2609.39284v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

While large language models have achieved remarkable success in isolated code generation, authentic software engineering requires sustained reasoning, complex state management, and continuous cross-domain abstraction. However, current evaluations of skill evolution in autonomous agents suffer from a critical identifiability problem: they structurally confound genuine capability abstraction with rote solution leakage (i.e., copying highly similar code from historical training data). To resolve this, we introduce EngramBench, a rigorous, capability-grounded benchmark governed by the strict axiom of capability overlap without solution overlap. Comprising 30 diverse learning tasks and 13 unseen transfer tasks, EngramBench challenges agents to navigate interactive, multi-hour development cycles driven by LLM-simulated users. Our extensive evaluation across 48 multi-hour execution trajectories -- corroborated by human-expert validation -- reveals a profound insight into procedural memory. We demonstrate that static skill banks do not magically bypass the "last mile" of exact code implementation, which remains bottlenecked by the base model's inherent reasoning limits. However, they serve as an indispensable execution compass. By navigating agents away from catastrophic, token-heavy trial-and-error, genuine capability abstraction slashes redundant context bloat and reduces overall coding time by over 55%. Ultimately, EngramBench shifts the evaluation paradigm from trivial pattern matching to the verifiable measurement of deep, cross-domain capability transfer.

</details>


### 124. DAGent: Evaluate-then-Grow Planning for Deep Research Agents

- **Authors:** Hanwen Liu, Yuanfu Sun, Qiaoyu Tan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39154v1](http://arxiv.org/abs/2609.39154v1)
- **PDF:** [https://arxiv.org/pdf/2609.39154v1](https://arxiv.org/pdf/2609.39154v1)
- **Categories:** cs.CL, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Deep research tasks require agents to navigate large knowledge spaces, synthesize evidence across many sources, and adapt their plans as findings emerge. Directed acyclic graph (DAG)-based multi-agent systems suit this setting because they support parallel execution and isolate each sub-task within a focused dependency context. Yet existing DAG-based agents instantiate a task-level plan before execution and repair the graph only after failures or missing evidence are observed. This Plan-then-Patch strategy is brittle for deep research: the system commits most strongly when its evidence is weakest, and later revisions waste computation on branches that should not have been planned. We propose DAGent, a DAG-based multi-agent framework with Evaluate-then-Grow incremental planning: an Orchestrator grows the task graph one batch at a time, conditioning each expansion on confidence and uncertainty signals from completed nodes. A hierarchical context layer propagates compact QueryDocs by default while preserving full execution traces for on-demand recall. The recorded DAG topology admits structural RL signals that outcome-only recipes cannot define; DAGRPO, a GRPO adaptation, injects topology-conditioned credit on Executor rollouts and a structural compliance regularization on Orchestrator plans. Across BrowseComp-Plus, GAIA, and xbench-DeepSearch, DAGent surpasses the strongest open-source baseline by 5.3 / 5.8 / 2.0 points at the Qwen3-235B-A22B scale, and the lead replicates across four open-source backbones and extends to GPT-5 at 327K context. At the Qwen3-8B scale, DAGRPO improves over a same-budget outcome-only GRPO baseline by 3.0 average Pass@1 points. A same-architecture comparison shows that evidence-conditioned planning reaches higher accuracy at lower per-task token, tool-call, and step footprints than its Plan-then-Patch counterpart. Code: https://github.com/hanwenliu6825/DAGent

</details>


### 125. Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents

- **Authors:** Kaixing Zhang, Changming Li, Yingdong Shi, Zheng Zhang, Kaitao Song, Wenjie Shi, Jingang Wang, Kan Ren
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39149v1](http://arxiv.org/abs/2609.39149v1)
- **PDF:** [https://arxiv.org/pdf/2609.39149v1](https://arxiv.org/pdf/2609.39149v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Textual skills enable large language model (LLM) based agents to accumulate reusable procedural knowledge without updating model parameters. Yet existing skill evolution remains largely confined to the text space: an optimizer must diagnose success and failure patterns, and revise skills solely from long execution trajectories and sparse task outcomes. This text-only paradigm leaves the agent's internal representations, which contain rich records of its evolving execution state, outside the skill optimization loop. We ask whether an agent can improve its external textual skills by reflecting on its own internal representations. We introduce Rep2Skill, a representation-guided framework for self-evolution on agent skills. Specifically, upon the collected agent rollouts, Rep2Skill models their internal model representation trajectories to localize turns that deviate from successful execution dynamics, and it further interprets these signals alongside the execution contexts as actionable textual feedback for targeted skill revision. Experiments on two agent environments with two open-source LLMs show that Rep2Skill consistently outperforms text-only approaches in the self-evolution setting, where the same LLM serves as both executor and optimizer without a stronger external model. This establishes a promising direction moving agent self-improvement beyond text-only reflection.

</details>


### 126. Do Self-Evolving Skills Generalize to Held-Out Tasks?

- **Authors:** Xihao Piao, Zifeng Wang, Zhen Chen
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39148v1](http://arxiv.org/abs/2609.39148v1)
- **PDF:** [https://arxiv.org/pdf/2609.39148v1](https://arxiv.org/pdf/2609.39148v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents can externalize what they learn from past tasks into reusable \emph{skills}, such as procedures, checklists, code, or other executable artifacts, that can be retrieved and reused when solving new tasks. Self-evolving skill methods keep rewriting these skills after each round of practice on training tasks, and the skill is then used on new tasks of the same kind. We ask a question: does the improvement a skill shows on its training tasks carry over to new test tasks? We test five self-evolving methods and a one-shot skill on six benchmarks, with the same model, the same agent, and the same train/test split for every method. Of the 21 skills that improve on their training tasks, 5 keep all of that improvement on the test tasks, 13 keep part of it, and 3 keep none of it. No existing method is best everywhere. When we read the skills, the ones that carry over badly often fix details that should depend on the task, such as column names and output files, or turn a fix for one failure into a rule for every task. An LLM judge that reads the skill content can often see this: it ranks finished skills the same way the test results do in 86\% of pairs. But it predicts the effect of a single edit poorly, so edits still have to be tested by running them. Based on these findings, we describe Generalizable Skill Optimization (GSO), which keeps only a guide for writing skills and writes a new skill for each task; it scores highest on all six benchmarks.

</details>


### 127. MADBench: Benchmarking the Security of Multi-Agent Debate

- **Authors:** Yuwan Liu, Jiaming Zhang, Yue Huang, Sisi Duan
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39146v1](http://arxiv.org/abs/2609.39146v1)
- **PDF:** [https://arxiv.org/pdf/2609.39146v1](https://arxiv.org/pdf/2609.39146v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent debate (MAD) can improve large language model (LLM) reasoning by allowing multiple agents to exchange and critique their answers to the same task. However, the interactions that enable agents to correct mistakes can also spread adversarial errors and steer the agents toward an incorrect answer. Although some efforts have been made to examine particular attack types on MAD, systematic evaluation of MAD under diverse attacks remains limited. A central question is whether debate mitigates adversarial influence or amplifies it.
  In this paper, we present MADBench, a benchmark for evaluating the security of MAD. We organize attacks into a layered taxonomy following the MAD workflow, incorporating both established attacks and new strategies tailored to debate. We evaluate six attack families over 356 source tasks and 3,958 test cases, examining their effects on the final answer and the propagation of adversarial influence. Our results show that, under attacks, MAD does not necessarily improve LLM reasoning. Compared with a single-agent baseline, MAD can mitigate attacks on answer accuracy in question-answering tasks while amplifying unauthorized reads or writes in both question-answering and workspace tasks. Moreover, even when three out of five agents collude, the attack changes the final answer from correct to wrong on only 28.30\% of tasks answered correctly without attack, while only 3.26\% of initially correct honest agents switch to wrong answers during debate.

</details>


### 128. RefCon: Iterative Refinement and Contrastive Memory Extraction for Context-Evolving Agent

- **Authors:** Ubaidillah Ariq Prathama, Bo Liu, Yeo Boon Hong, Yu-Xuan Huang, Yangkai Ding, Tao Yu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39143v1](http://arxiv.org/abs/2609.39143v1)
- **PDF:** [https://arxiv.org/pdf/2609.39143v1](https://arxiv.org/pdf/2609.39143v1)
- **Categories:** cs.AI, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-horizon agent interactions generate useful but noisy experience, and retraining models to absorb it is expensive. Context-evolving agents therefore need memory extraction methods that improve with more test-time compute without relying on gold labels. We propose RefCon, which combines sequential self-refinement with parallel self-contrast to extract higher-quality memories without gold labels. Evaluated on AppWorld and BFCL-V3 across multiple context-evolving agent frameworks, RefCon delivers strong and consistent gains, including relative improvements of 21.6% on ACE and 16.6% on ReMe over no-scaling baselines, while a diversity-focused variant (DivCon) achieves a 35.5% gain on ReasoningBank. RefCon consistently outperforms existing baselines without ground-truth labels, and generalizes across model scales and to software engineering tasks, where it surpasses even ground-truth baselines. We further analyze the accuracy-token trade-off and scaling behavior, showing RefCon maintains favorable efficiency and continues to improve as more trajectories are used, unlike diversity-only scaling which saturates earlier.

</details>


### 129. Schema: Discovering Unknown Environments via Agentic Program Induction

- **Authors:** Guanning Zeng, Jiani Wang, Wenjie Ma, Shaofeng Yin, Chenyang Wang, Shichen Liu, Angjoo Kanazawa, Wode Ni, Xiuyu Li, Andrea Zanette, Haiwen Feng
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39140v1](http://arxiv.org/abs/2609.39140v1)
- **PDF:** [https://arxiv.org/pdf/2609.39140v1](https://arxiv.org/pdf/2609.39140v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Learning to complete tasks in unfamiliar environments with unknown rules remains a key challenge for LLM agents. Current LLM agents often record their discoveries in prose, which may not provide a compact, explicit account of how the environment works. Inspired by how scientists organize observations into testable, predictive theories, we introduce Schema, an agent harness that organizes learning and action through interactive program induction. The LLM agent decides what to investigate and how to act, expressing its evolving understanding of the environment as executable programs. The harness consists of a persistent program workspace and a small set of interfaces for checking these programs against the interaction history, planning within them, and executing plans under step-by-step verification. Schema raises ARC-AGI-3 RHAE from 58.7% to 99.2% with the same base model, solves 100% of the public DiG-bench games, and reaches the median performance of the top-50 human players on MazeBench. Extensive analysis shows the effectiveness of Schema in unknown mechanism discovery, and ablations confirm the contribution of each component.

</details>


### 130. When Harnesses Lose the Signal: Causal Evaluation of Recovery in LLM Agents

- **Authors:** Shuyao Xiao, Shengling Wang, Xuan Chen, Ke Chao, Ming Cui, Feifei Qian, Chaoyang Mei, Fanlin Meng, Ziming Yu, Junxi Yin
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00372v1](http://arxiv.org/abs/2610.00372v1)
- **PDF:** [https://arxiv.org/pdf/2610.00372v1](https://arxiv.org/pdf/2610.00372v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model agents rely on external harnesses to pass information between the model and its environment and to recover from execution errors. Yet recovery is usually judged only by average task success. This hides an important tension. The same operation can rescue a failing trajectory or disrupt one that would otherwise succeed. We frame recovery as a causal decision problem. Starting from the same execution state, we compare what happens with and without recovery, separate rescue from harm, and study how the value of recovery changes over time. We then introduce the Causal Intervention Router (CIR), a lightweight policy that uses information available before recovery to decide when intervention is worthwhile. On long-horizon ALFWorld tasks with Qwen3-14B, CIR raises success from 70.33% to 73.33%, a gain of 3.00 percentage points. It leaves all evaluated trajectories with correct observations untouched. Additional controls show that the benefit of recovery cannot be explained solely by the new observation returned by the environment. These results provide a practical way to evaluate recovery and apply it selectively.

</details>


### 131. Deny Without Disabling: Authorization-Paired Evaluation and Control for Multi-Agent Systems

- **Authors:** Yunbei Zhang, Saiyue Lyu, Janet Wang, Yingqiang Ge, Jiang Guo, Jihun Hamm, Chandan K Reddy
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00371v1](http://arxiv.org/abs/2610.00371v1)
- **PDF:** [https://arxiv.org/pdf/2610.00371v1](https://arxiv.org/pdf/2610.00371v1)
- **Categories:** cs.MA, cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems derive their capabilities from sharing evidence, delegating tasks, and combining information across agents. The same process creates a safety problem: contributions that are admissible in isolation can jointly enable a prohibited use. Blocking every sensitive action avoids disclosure but defeats the purpose of collaboration. We introduce authorization-paired evaluation, which makes blocking prohibited uses and completing required authorized uses a joint success criterion, and FlowReview, a framework connecting object resolution, permission ranking, and deterministic enforcement. In controlled composition experiments, reviewing combined artifacts reduces the denied-commit rate from 86.0% to zero with no loss of authorized supply. Our findings show that preserving information and lineage alone does not ensure correct permission attribution. Object identity and permission must remain connected to execution through components whose outputs can be verified. Together, these findings establish a system-level requirement for multi-agent safety: govern composed information flows while preserving the authorized capabilities that make collaboration useful.

</details>


### 132. MASCRDM: Multi-Agent System for Compliance Risk Detection and Mitigation in Training Process of Large Language Models

- **Authors:** Yan Zhang, Chuming Wei, Ruien Li, Yaoyao Peng, Wusheng Zhang, Guangwen Yang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39107v1](http://arxiv.org/abs/2609.39107v1)
- **PDF:** [https://arxiv.org/pdf/2609.39107v1](https://arxiv.org/pdf/2609.39107v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have been applied in various fields. However, ensuring compliance and safety of LLMs, such as avoiding discrimination and bias, still remains a challenge. Current efforts mainly focus on detecting and filtering inputs and outputs of the trained models, rather than studying the intrinsic architecture of the models in real-time. To tackle this challenge, we analyze the LLMs training process and discover two critical issues: 1) Most of the existing methods are predominantly static in their approach to detection and filtering, achieving only localized optimizations without systematically enhancing the compliance of LLMs. 2) Another issue with existing approaches is the lack of real-time risk detection and mitigation across the full training process, which leads to limited flexibility. Motivated by these, we propose MASCRDM (Multi-Agent System for Compliance Risk Detection and Mitigation) during the LLM training process. Firstly, we develop a set of compliance rules based on existing Artificial Intelligence (AI) laws and a compliance-specific LLM with the instruction of compliance law experts. Then, we deconstruct LLMs into several components and identify key nodes based on the compliance knowledge graph. During LLMs training, we implement our multiple agents in the whole process, giving compliance risk alerts and suggestions for LLM developers. Experiments on discrimination and bias benchmark demonstrate that our multi-agent system can effectively improve the compliance while maintaining reasonable semantic performance. The results indicate that our method provides an executable path for mitigating compliance risk from within the LLMs systematically.

</details>


### 133. Trustworthy Runtime Error Healing in Real-World Repositories: A Benchmark and Guardrail

- **Authors:** Gou Tan, Pengfei Chen, Zhensu Sun, Jieke Shi, Junkai Chen, Ting Zhang, Weifeng Sun, Junda He, Shuai Liang, Chuanfu Zhang, Lwin Khin Shar, David Lo
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39086v1](http://arxiv.org/abs/2609.39086v1)
- **PDF:** [https://arxiv.org/pdf/2609.39086v1](https://arxiv.org/pdf/2609.39086v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Runtime error healing lets a crashed program continue by generating code that repairs its live runtime state. Recent work shows that LLMs can generate such healing code, but it is evaluated only on small competition programs, and executing LLM-generated code inside a live process raises safety concerns that remain unaddressed. In this paper, we take LLM-based runtime healing toward practical use in real-world repositories. We first build HealBench, a benchmark of 265 runtime errors from 18 real-world repositories, each paired with a reference execution on the patched version. HealBench also provides a unified framework that lets LLM agents heal with cross-file context and live runtime state. We then design HealGuard, which requires healing code to be written in HealCore, an analyzable subset of Python, and uses static and dynamic taint analysis to check whether state changed by healing reaches operations protected by developers. We evaluate a dedicated healing method and three general coding agents with three backbone LLMs. The best setting resumes execution in 38.11% of instances and passes the target test in 28.68%, showing that existing agents can already heal a meaningful share of real repository-level crashes. However, among executions that pass, HealGuard flags 17.4% whose healing-changed state may reach a protected operation. On 684 controlled cases, HealGuard detects all unsafe cases, at the cost of a 68.42% false positive rate.

</details>


### 134. SparseEngine: Sparse-First Inference Engine

- **Authors:** Jitai Hao, Quansheng Gu, Qiang Huang, Jun Yu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39068v1](http://arxiv.org/abs/2609.39068v1)
- **PDF:** [https://arxiv.org/pdf/2609.39068v1](https://arxiv.org/pdf/2609.39068v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-context LLM agents accumulate interaction histories that strain KV-cache memory and attention computation. Although sparse attention reduces these costs, heterogeneous cache representations and workflows hinder integration with existing inference engines, while prior sparse-serving abstractions support only specific layouts or workflows. We present SparseEngine, a ground-up, sparse-first inference engine whose shared lifecycle contract lets each method control its KV representation and computation while coordinating state transitions with common serving infrastructure. SparseEngine supports 15 methods across four categories and enables cross-request state management through Chain Cache, which resumes KV-eviction methods from retained history, and controllable Prefix-Cache Pruning, which removes KV from selected history regions while preserving logical-prefix matching. While maintaining method quality, SparseEngine delivers over 10x higher throughput with KV eviction, over 2.5x faster decoding at matched concurrency than vLLM, and over 2x end-to-end speedup on agent benchmarks. The code is available at https://github.com/CURRENTF/SparseEngine.

</details>


### 135. Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents

- **Authors:** Yan Wang, Zhihao Zhang, Ke Chen, Kai Chen, Yaqin Zhang, Duohe Ma, Jun Dai, Xiaoyan Sun
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39065v1](http://arxiv.org/abs/2609.39065v1)
- **PDF:** [https://arxiv.org/pdf/2609.39065v1](https://arxiv.org/pdf/2609.39065v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents increasingly rely on installable skills, which are packages of instructions, code, and resources that equip them with task-specific capabilities and, once installed, can be automatically invoked across subsequent user tasks. This creates a chain of trust in which users delegate authority to agents, while agent frameworks admit skill-provided content into the agents' context with insufficient validation, allowing malicious skills to influence agent behavior under that delegated authority. Yet, little is known about whether this trust model adequately constrains untrusted skill content before it reaches security-sensitive operations, or how frequently such trust violations arise in real-world agents. We present TrustProbe, a framework for uncovering unsafe chains of trust in skill-based LLM agents. First, TrustProbe analyzes agent source code to identify source-to-sink call paths from skill-controlled inputs to security-sensitive operations. Second, it generates semantically realistic SKILL.md seeds with injected canaries and evolves them through feedback-guided scheduling and mutation. Finally, it validates vulnerabilities using an oracle that confirms attacker-controlled flows and verifies observable harm. Across 11 open-source agents, eight with more than 10,000 GitHub stars, TrustProbe identifies 104 taint-style vulnerabilities. Validation on a large corpus of real-world skills collected from public hubs such as ClawHub further shows that 25.1% of skill-agent trials exercise the identified vulnerable paths, with payload injection successfully weaponizing 15 of the vulnerabilities. These results reveal a systematic trust failure in skill-based LLM agents: untrusted skill content can reach security-sensitive operations and exercise authority delegated by users to their agents.

</details>


### 136. Covert Assistance: Helpful LLM Agents Evade Oversight in Multi-Agent Systems

- **Authors:** Deema Alnuhait, Gengyu Wang, Muhammad Khalifa, Hao Peng
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39050v1](http://arxiv.org/abs/2609.39050v1)
- **PDF:** [https://arxiv.org/pdf/2609.39050v1](https://arxiv.org/pdf/2609.39050v1)
- **Categories:** cs.CR, cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

As multi-agent systems enter high-stakes domains, the possibility that agents may circumvent safety boundaries is a growing concern. Prior work has examined this risk primarily in adversarial settings, where agents are instructed or rewarded to communicate covertly and evade oversight. We show that benign agents can cross the same boundaries without adversarial incentives. We emulate a software-engineering workflow in which a planner represents a company hiring an external developer. The planner writes requirements and holds a company credential it is instructed not to disclose to the developer; a monitor screens their exchanges. Seven of nine tested frontier models disguise the credential in their requirements to help the developer recover it while evading the monitor, even after completing their assigned objective. For example, across 6,000 episodes with DeepSeek-V4-Pro, the planner attempts concealment in 16.9%; in 0.9%, the credential evades the monitor and is recovered and used by the developer. Despite the low per-episode rate, the risk compounds across repeated exchanges: at 0.9%, 105 independent episodes carry a 61.3% chance of at least one breach. Our analysis suggests that the planner misinterprets disguised disclosure as helping the developer and reads the nondisclosure rule as banning plaintext, not character codes or riddles. We call this behavior covert assistance. Monitoring favors concealment, while concealment gives way to direct disclosure when the recipient is presented as a human rather than an AI agent, so leakage persists. Giving the monitor the credential improves detection but requires trusting it with the secret. These risks, in models already used for software engineering, challenge oversight to distinguish authorized cooperation from task-advancing assistance that crosses safety boundaries.

</details>


### 137. RSIGame: Autonomous Agentic Game Development with Recursive Self-improvement

- **Authors:** Wenyi Wu, Minghao Fu, Jieyu You, Kun Zhou, Siqi Liu, Aayush Salvi, Yiheng Lin, Ce Zhang, Xiaohan Lan, Jiahui Zhu, Yujie Zhong, Qi She, Biwei Huang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.39045v1](http://arxiv.org/abs/2609.39045v1)
- **PDF:** [https://arxiv.org/pdf/2609.39045v1](https://arxiv.org/pdf/2609.39045v1)
- **Categories:** cs.CL, cs.GT, cs.LG, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recent advances in large language models have made automatic game generation increasingly feasible, yet reliably improving generated games beyond a playable version remains challenging. Naive iterative refinement can easily overfit a small set of test cases, producing fragile games with unresolved bugs, missing behaviors, and poor generalization to broader player interactions. We introduce RSIGame, an autonomous agentic game development framework with recursive self-improvement. RSIGame organizes development into complementary local and global loops. Concretely, a local explore-diagnose-improve loop broadly explores the executable game, diagnoses and prioritizes discovered issues, and performs evidence-grounded revision, where an evolving checklist continually accumulates new testing and improvement guidance. A global loop tracks overall quality, preserves the best checkpoint, and detects saturation or regression over long-horizon development. Beyond test-time improvement, RSIGame further internalizes successful development experience into the generator through training. Across 140 GameCraft-Bench tasks, two game engines, and five generators, RSIGame consistently improves game quality under matched development budgets. Notably, experience internalization enables Qwen3.8-27B to reach 61.38 on Godot and 58.53 on Phaser, exceeding GPT-5.5 one-shot scores while reducing Qwen's generation tokens by 11 times.

</details>


### 138. When Order Matters: First-Speaker Bias and Mitigation through Personality in Sequential Multi-Agent Debate

- **Authors:** Duofeng Xu, Bryan Hooi, Dandan Qiao
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38964v1](http://arxiv.org/abs/2609.38964v1)
- **PDF:** [https://arxiv.org/pdf/2609.38964v1](https://arxiv.org/pdf/2609.38964v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent debate (MAD) is often used to improve large language model (LLM) reasoning, but sequential debate is rarely a neutral aggregator of agents' opinions. We show that sequential MAD suffers from a pronounced first-speaker bias: agents disproportionately shape the final answer when they speak first. As a result, placing a stronger model after weaker ones can substantially offset its reasoning advantage. We then focus on the disadvantaged strong-agent-last setting and ask whether personality prompting can mitigate this imbalance. Drawing on the Big Five model, we study agreeableness and extraversion as behavioral interventions applied to either the strong or weak side. We find that their effects are trait-specific. Influence consistently shifts in the direction of lower agreeableness, and assigning low agreeableness to the stronger agent helps restore its lost influence and improves final accuracy. Extraversion, by contrast, produces less systematic changes in influence and accuracy, with its clearest effect appearing in agents' verbosity. These findings show that effective MAD design depends not only on model capability, but also on how speaking order and induced interaction behavior shape the debate process.

</details>


### 139. Fast and Scalable Multi-Agent Distribution Matching via Partitioned Optimal Transport

- **Authors:** Kooktae Lee, Ruchika Singh
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38960v1](http://arxiv.org/abs/2609.38960v1)
- **PDF:** [https://arxiv.org/pdf/2609.38960v1](https://arxiv.org/pdf/2609.38960v1)
- **Categories:** cs.MA, cs.RO, eess.SY, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

This paper presents a scalable optimal-transport-based framework for terminal distribution matching in multi-agent systems. While optimal transport provides a natural way to measure distributional mismatch and assign agents to a desired spatial distribution, global discrete transport can become computationally expensive for large-scale systems. We address this bottleneck by partitioning agents and target samples into spatially corresponding blocks and solving smaller local transport problems. Under a mass-balance condition, the resulting restricted coupling remains feasible for the global problem and provides an upper bound on the Wasserstein cost. The local assignments generate target locations for finite-horizon agent control, applicable to both linear and nonlinear dynamics. By alternating local assignment and control, we establish a cycle-to-cycle descent guarantee for the resulting transport surrogate. The proposed framework therefore enables scalable terminal distribution matching while retaining a rigorous connection to the Wasserstein objective. The technical soundness of the proposed results is validated through simulations.

</details>


### 140. VERA: Verifiable Feasibility Representations with Counterfactual Credit for Constrained Multi-Agent Control

- **Authors:** Bo Yin, Dongbo Li, Hongkai Chen, Jie Liu, Guoliang Xing
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38889v1](http://arxiv.org/abs/2609.38889v1)
- **PDF:** [https://arxiv.org/pdf/2609.38889v1](https://arxiv.org/pdf/2609.38889v1)
- **Categories:** cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Constrained multi-agent control requires more than predicting rewarding actions: an action can cease to be executable as contact windows, shared capacity, and deadlines change. We introduce VERA, a centralized-training, decentralized-execution framework that separates feasibility estimation from credit assignment. Each actor predicts a five-dimensional verifiable feasibility representation (VFR). After an action is proposed, exact action-conditioned margins available only during training supervise that representation, while a counterfactual group-relative advantage (CGRA) ranks candidate representation-action pairs. Execution uses one actor pass and no privileged state. In a dynamic space-air-ground integrated network (SAGIN), VERA obtains 55.33% +/- 3.60% success with 0.45% +/- 0.81% coverage violation, within 1.33 percentage points of a privileged-mask reference. With rewards matched over ten paired seeds, VERA improves success over the strongest baseline by 8.74 percentage points (p=0.023) and reduces violation by 52.19 percentage points (p=5.7e-8). A ten-seed 4-by-2 factorial attributes a 14.16-16.48 percentage-point gain to CGRA across handcrafted, learned, random, and latent representations; evaluation on seven unseen topologies preserves a 24.33-30.02 percentage-point advantage over multi-agent proximal policy optimization. From 10 to 40 users, success remains 50.1-53.8%, and VFR adds only 0.026 ms to a central processing unit (CPU) actor step. Cross-domain tests further identify the governing condition: counterfactual credit succeeds when candidate scores respect shared constraints and fails under incompatible reward geometries. These results establish action-conditioned feasibility as an auditable training interface and counterfactual credit as a geometry-dependent optimization mechanism.

</details>


### 141. Right Answers, Costly Models: The Efficiency Gap in LLM-based Optimization Modeling

- **Authors:** Zhong Li, Xin Huang, Jinhui Wan, Xiangyi Wang, Shenkai Zhang, Ruiqi Chen, Wenyu Liu, Zaiwen Wen, Ziyan Luo
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38884v1](http://arxiv.org/abs/2609.38884v1)
- **PDF:** [https://arxiv.org/pdf/2609.38884v1](https://arxiv.org/pdf/2609.38884v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Optimization modeling formulates real-world decision problems as mathematical programs that solvers can use to find optimal decisions. Large language models (LLMs) can automate this process, but the resulting correct formulations can require substantial time and memory to construct and solve, limiting practical scalability. Therefore, we systematically investigate whether LLMs can identify problem structure from natural-language descriptions and apply suitable optimization modeling techniques to generate mathematical models and solver code that solve the problems correctly and efficiently. To this end, we first curate OptTips, a knowledge base of 50 expert modeling techniques in eight families. Using this knowledge, we develop OptDachshund, a multi-agent framework that transforms problems from existing optimization benchmarks into new tasks for evaluating LLMs' use of modeling techniques. It constructs conventional and expert mathematical models with solver code for the same task and data, providing baselines for correctness and computational cost. The resulting EfficientOpt benchmark contains 561 expert-reviewed tasks with paired reference implementations. Evaluation of 11 representative LLMs reveals an efficiency gap on correctly solved tasks with comparable measurements: for every LLM, most generated programs take longer to solve than their expert counterparts. Within the comparable reference-size subset, 57\% of programs with correct objective values and fewer variables and linear constraints have longer recorded solver times. Case studies show that different modeling techniques can achieve the same optimal value at similar recorded cost. Faster solving may not reduce execution time if the code takes longer to prepare data and build the model. LLM optimization modeling should therefore be evaluated for both correctness and computational efficiency.

</details>


### 142. When Context Changes: Understanding Update Failures in LLMs

- **Authors:** Junyu Guo, Yuchen Fang, Shangding Gu, Costas Spanos, James Demmel, Javad Lavaei
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38866v1](http://arxiv.org/abs/2609.38866v1)
- **PDF:** [https://arxiv.org/pdf/2609.38866v1](https://arxiv.org/pdf/2609.38866v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

As preferences, goals, and facts change, LLM agents must use the current state while earlier versions remain in context. Yet they can answer with an old value of the same variable, a failure that we call stale binding. To study when models use outdated information and why, we introduce Controlled In-Context Memory (CICM), a benchmark for tracking and using updated information in conversations and agent logs. We observe that even frontier reasoning models can fail to recover the current state. We find that in open-source models probes can still recover the updated value when the model answers with an old one, pointing to a failure to select information that remains available. Component tests in Qwen and Pythia identify a mechanism for this selection failure: attention drift, where attention favors old values over the current one when producing an answer. We study a one-layer transformer to mathematically understand how this phenomenon happens: when attention scores are similar, several old values can together receive more attention than the current value. Guided by this explanation, we redirect attention toward the current value without further training. When the current value is requested directly, adjusting this intervention for each input corrects most old-value errors across various model families while preserving nearly all initially correct answers. Reliable context management therefore requires more than remembering updated information: models must use it to guide their answers.

</details>


### 143. SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale

- **Authors:** Guanqun Yang, Wenlong Zhang, Tian Shi, Ping Wang
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38822v1](http://arxiv.org/abs/2609.38822v1)
- **PDF:** [https://arxiv.org/pdf/2609.38822v1](https://arxiv.org/pdf/2609.38822v1)
- **Categories:** cs.IR, cs.AI, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Anthropic's Agent Skills package reusable procedural know-how for an LLM agent into SKILL.md directories, and open-source aggregations have grown past 230,000 skills, making selection rather than authoring the bottleneck. The standing answer in the literature outsources selection to the agent itself: an LLM-mediated retrieval loop that rewrites queries and refines candidates inside the agent's decision loop, paying LLM tokens on every task. We present SkillSeek, an open-source two-stage skill retriever built from the standard IR recipe (a BGE-base bi-encoder feeding a small cross-encoder, exposed over MCP). Across a $4 \times 11$ grid of pool, backbone, and method on the 89-task SkillsBench benchmark, SkillSeek reaches observed parity with the LLM-mediated loop of Liu et al. at essentially no extra cost: plain bm25 alone records a pass rate at or above their refined loop on three of four settings, and a small cross-encoder covers the remaining difference on the fourth. A first-stage recall ceiling explains the pattern, and total per-trial spend drops from USD 51.30 to USD 27.54 (within fifty cents of the no-skill baseline). Under the SkillsBench tasks and OpenHands harness we tested, this positions the standard IR recipe as a strong default for agent-skill retrieval, with LLM-mediated alternatives a natural fit for cases where deterministic methods fall short.

</details>


### 144. You're Hired: Strategic Model Selection for LLM Collaboration

- **Authors:** Zongwan Cao, Ziyuan Yang, Shangbin Feng, Michael Duan, Skyler Hallinan, Bingbing Wen, Lucy Lu Wang, Yulia Tsvetkov
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38816v1](http://arxiv.org/abs/2609.38816v1)
- **PDF:** [https://arxiv.org/pdf/2609.38816v1](https://arxiv.org/pdf/2609.38816v1)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

While multi-agent and model collaboration algorithms gain traction to combine the strengths of diverse Large Language Models (LLMs), existing systems remain bottlenecked on pre-defined and hand-crafted model pools. In this work, we investigate the problem of model selection in multi-LLM systems. We propose and systematically evaluate a taxonomy of 9 selection algorithms ranging from diversity of model descriptions, capability-aware behavioral diversity, and LLM-based recruiters. We conduct extensive experiments across two candidate pools of 10 and 32 models, deployed in four model collaboration algorithms, and evaluated across tasks spanning math, coding, QA, and reasoning. Results demonstrate that successful selection algorithms greatly outperform random or heuristics-based teams such as merely selecting the models with top individual performance, by up to 36.1% across settings. Specifically, capability- and training-based selection strategies alleviate selection variance and achieve the best performance, which we recommend to employ before deploying real-world multi-LLM systems. Further analysis reveals that larger candidate pools pose greater challenges to shallow selection heuristics, while algorithms grounded in interacting with candidate models and understanding model capability robustly filter out misaligned, unsafe models, as well as generalizing to novel, out-of-distribution tasks. Together, we establish that principled and informed team selection is critical and present strong model selection algorithms for assembling effective multi-LLM systems.

</details>


### 145. Explicit Trajectory Diversity for RL-Based Post-Training of LLM Agents

- **Authors:** Huaiyu Fu, Heng Cao, Hao Wang, Jian Ya, Tao Chen
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38805v1](http://arxiv.org/abs/2609.38805v1)
- **PDF:** [https://arxiv.org/pdf/2609.38805v1](https://arxiv.org/pdf/2609.38805v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents often admit multiple high-quality solutions to the same task, differing in reasoning structure, tool-use pattern, or interaction trajectory. Yet existing notions of diversity in LLM post-training are mostly implicit, arising from general stochasticity and regularization mechanisms rather than explicitly targeting task-relevant behavioral variation. While such implicit diversity can be useful, it does not directly specify which forms of behavioral variation should be encouraged for a given task. In this work, we study explicit trajectory diversity in RL-based post-training for LLMs. Our key idea is to define diversity through user-specified, task-specific trajectory descriptors, which map each sampled trajectory to an interpretable behavioral representation, and then measure diversity as a set-level functional over the resulting descriptor matrix. Building on this formulation, we introduce Trajectory-guided Joint Policy Optimization(TJPO), a single-policy framework that optimizes explicit diversity over sampled trajectory groups, avoiding the need for population-based policy training, and instantiate it within group-based policy optimization through trajectory-level learning signals. This design makes the diversity objective both interpretable and controllable. Experiments on Sokoban and ALFWorld show that TJPO improves task-specific trajectory diversity while maintaining competitive task performance. Descriptor and trajectory analyses show that the learned variation follows the specified behavioral dimensions and includes distinct successful strategies. Extra experiment results suggest that explicitly shaping trajectory diversity can help LLM agents satisfy user requirements and remain effective when task conditions change.

</details>


### 146. GraphCert: Bootstrap Agentic Graph Reasoning with Certified Evidence Rubrics

- **Authors:** Weiqi Jiang, Yuchen Ying, Rui Wang, Kaixuan Chen, Bingde Hu, Shunyu Liu, Yu Wang, Tongya Zheng
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38798v1](http://arxiv.org/abs/2609.38798v1)
- **PDF:** [https://arxiv.org/pdf/2609.38798v1](https://arxiv.org/pdf/2609.38798v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Graph agents extend large language models (LLMs) with the ability to actively explore and reason over knowledge graphs through multi-step interactions with graph tools. However, training capable graph agents typically requires large collections of question-answer pairs and reasoning trajectories, whose manual construction is costly and difficult to scale. Moreover, employing proprietary LLMs to generate such supervision further risks exposing sensitive graph data to external services. Therefore, we propose GraphCert to bootstrap agentic graph reasoning with certified evidence rubrics during post-training. Specifically, the Bootstrapped Graph Quizzer guided by generation controls produces graph-grounded QA pairs and marks supporting evidence, which undergo execution certification and semantic curation. The accepted evidence is then canonicalized into certified evidence rubrics that later reward Graph Solver evidence alignment alongside answer correctness during GRPO training. Experiments on five graph reasoning domains in GRBENCH demonstrate that GraphCert consistently outperforms substantially larger LLM agents and post-training method. Furthermore, our analysis demonstrates that the learned policy transfers robustly across heterogeneous graph domains, suggesting that GraphCert acquires reusable graph-reasoning capabilities rather than domain-specific patterns. These results establish executable self-certification as an effective approach to self-training compact graph reasoning agents. Our code will be made publicly available.

</details>


### 147. Positive Ratings, Hidden Concerns: Employee Voice Disclosure in AI-Mediated Organizational Listening

- **Authors:** Thilo Tamme, Michael Saatkamp, Alma Bonte, Daniel Weiss, Anton Hantel, Andrej Levin
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38788v1](http://arxiv.org/abs/2609.38788v1)
- **PDF:** [https://arxiv.org/pdf/2609.38788v1](https://arxiv.org/pdf/2609.38788v1)
- **Categories:** cs.AI, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Organizations started listening to employees through conversational AI agents alongside structured surveys. Little is known about what these channels change in what employees say when disclosure carries hierarchical risk. We report a field study inside a global management consulting firm whose process pairs a pre-survey with an adaptive AI voice interview on the same themes within one session. Across 44 first-session interviews (132 matched theme observations), 20-41% of sessions showed a favorable rating co-occurring with a substantive concern voiced later, depending on the favorability threshold. The Gioia analysis drew on 158 protective quotes from 65 eligible sessions. Disclosure rarely arrived unguarded: employees softened concerns, deflected accountability, and bounded how far they went, and this protective work tracked the perceived legitimacy of the listening structure. We develop a grounded model of bounded disclosure and derive four propositions for voice, channel and listening research. Silence, we argue, can persist inside expression.

</details>


### 148. Where Do Multi-Agent Systems Fail? Evidence-Grounded Diagnosis of Collective Mechanisms

- **Authors:** Zhengye Han
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38761v1](http://arxiv.org/abs/2609.38761v1)
- **PDF:** [https://arxiv.org/pdf/2609.38761v1](https://arxiv.org/pdf/2609.38761v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

When a multi-agent system answers correctly, it is tempting to conclude that its agents shared, checked, and used information as intended. Yet a system can break one of its collective mechanisms, the rules that govern how agents route, admit, store, and act on shared information, and still return the right answer, while a wrong answer rarely reveals which mechanism failed. We ask what evidence from an execution is sufficient to conclude that a particular mechanism was violated. Our answer is a diagnostic contract, which separates what counts as a violation from which execution records can establish one, and concludes that a violation is supported, ruled out, or unknown; removing records can make this conclusion unknown but never reverse it. We test contracts for four mechanisms by replaying executions from the step where a mechanism acts, once unchanged, once with the mechanism broken, and once with it restored. Broken mechanisms often left the answer correct. An LLM diagnoser detected many more violations from internal records than from public outputs, yet with identical records a generic prompt often claimed certainty the records did not support, which prompts stating the contracts largely avoided. The contracts also applied, in narrow form, to mechanisms in independently developed systems, but a diagnostic behavior that was nearly perfect on our benchmark degraded on an independently developed workflow. A correct outcome is therefore no substitute for records of how collective mechanisms operated, and agreement on one benchmark does not show that a diagnoser transfers to another system.

</details>


### 149. Learning to Route in Visual Space via Multi-Step Embedding Retrieval

- **Authors:** Tianyu Chen, Mingyuan Zhou, Jiaxing Wu
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38743v2](http://arxiv.org/abs/2609.38743v2)
- **PDF:** [https://arxiv.org/pdf/2609.38743v2](https://arxiv.org/pdf/2609.38743v2)
- **Categories:** cs.AI, cs.IR


> Summary unavailable.


<details>
<summary>Abstract</summary>

LLM agents rely on retrieval tools to access external knowledge, yet visual agentic search remains severely bottlenecked by standard single-step retrievers. In current pipelines, the agent must issue text queries for every intermediate step, struggling when visual clues are difficult to describe or when the retriever fails to surface necessary intermediate evidence within its top results. We hypothesize that offloading multi-step navigation across the entire embedding space directly to the retrieval tool resolves this performance bottleneck. To study this systematically, we introduce VHOP, a flexible data generation framework and benchmark with five core difficulty levels testing both visual matching and search planning. Using this framework, we develop VHOP-Router, an end-to-end training pipeline---combining supervised fine-tuning, online imitation learning, and reinforcement learning---that transforms a standard embedding model into an autoregressive multi-step retriever. Operating directly in the visual latent space, VHOP-Router retrieves linked image chains in a single tool call without requiring the agent to formulate intermediate text queries. Experiments show VHOP-Router boosts retrieval performance from under 5\% to 76.3\%. In agentic search, it improves task success rates by 52.7\% and reduces the average token length by 61\% from 1886 to 728, whereas upgrading the agent yields only a 3.7\% gain. Compared to a strong baseline where the agent retrieves the top 50 results per step, VHOP-Router maintains superior performance while reducing in-context images by $23\times$ and cutting the cumulative API payload by $35\times$. The models also generalize robustly to unseen difficulty levels and realistic test sets. Ultimately, VHOP and VHOP-Router provide an efficient and effective solution for visual agentic search that leaves native LLM capabilities entirely intact.

</details>


### 150. Proof-Gated Signing: Solver-Checked Transaction Guards that Hold Under State Drift for Onchain AI Agents

- **Authors:** Bravish Ghosh
- **Published:** 2026-09-30
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00354v1](http://arxiv.org/abs/2610.00354v1)
- **PDF:** [https://arxiv.org/pdf/2610.00354v1](https://arxiv.org/pdf/2610.00354v1)
- **Categories:** cs.CR, cs.AI, cs.CE


> Summary unavailable.


<details>
<summary>Abstract</summary>

AI agents that control wallets read attacker-reachable content, so they can be steered into proposing harmful transactions. The usual last line of defense is a pre-signing check: a static allowlist, an LLM reviewer, or a transaction simulation. All three share a gap: the check describes the chain state at check time, but the transaction executes in a later state that an adversary can shape through front-running, contract upgrades or token-parameter changes. We call this state drift. We present Proof-Gated Signing (PGS), which simulates a proposed transaction, extracts its effects, and uses an SMT solver to check a declarative value-and-permission policy for every price in an oracle-uncertainty band. It then compiles on-chain post-conditions (wallet balance bounds, payee receipts, allowance caps and ownership) and proves that every execution satisfying them also satisfies the policy. The agent's smart-contract wallet enforces them atomically, so the guarantee applies to the executed transaction under arbitrary drift. On an open testbed of 260 scenarios (14 attack families including five drift and two adaptive families, and 12 benign families), with harm measured from attacker balances rather than from any policy, PGS prevented 93.6% of the 140 harmful scenarios and passed 97.5% of the benign ones. Simulation-only checking prevented 57.9% and a static allowlist 71.4%. None of the 50 drift scenarios produced attacker gain under PGS. The only unprevented family, an in-policy drain, was bounded by the per-session budget. We also find that giving an LLM reviewer a clean pre-drift simulation made it more likely to approve a drift attack. Overhead is about 41k gas and 0.1-0.2 s per check.

</details>


### 151. CollabFlow: Recursive Self-Improvement of Agent Collaboration

- **Authors:** Xiao Huang, Mingda Zhang, Junming Zhang, Qiang Huang, Hanwen Zhang, Yue Dai, Zijia Wang, Xiaoying Tang
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38662v1](http://arxiv.org/abs/2609.38662v1)
- **PDF:** [https://arxiv.org/pdf/2609.38662v1](https://arxiv.org/pdf/2609.38662v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Recursive self-improvement (RSI) lets a system improve from its own outcomes; in LLM-based multi-agent systems, Agents refine one another within a task, and outcomes improve how they collaborate across tasks. However, existing multi-agent collaboration leaves this loop open: collaboration is pre-defined at the operator level, topology-only learning keeps verbatim exchange that propagates errors, and reward maximization on a system's own outcomes concentrates on a few teams. To address these challenges, we propose CollabFlow, an RSI system of Learned Agent Collaboration: a trainable Collab-Director constructs teams of complete Agents, a frozen executor runs them, and each round's outcomes retrain the director. Within each round, the edges of a collaboration graph carry protocols of Evidence-Conditioned Communication: a receiver adopts a differing answer only when the sender's evidence is stronger by a margin, so the director learns who communicates and how. Across rounds, we further propose Collaborative Trajectory Balance (CTB), a flow-based objective that credits each team once across its construction orders and targets a reward-proportional distribution over teams, so several good teams stay in play. We also bound how far this self-generated target moves between rounds, which shrinks as records accumulate. On twelve datasets, CollabFlow outperforms all baselines and keeps improving across rounds. Code is available at https://anonymous.4open.science/r/CollabFlow-631E.

</details>


### 152. EvoSteer: Online Self-Evolving Graph Orchestration via Reference-Anchored Credit Assignment

- **Authors:** Mingda Zhang, Hanwen Zhang, Qiang Huang, Zijia Wang, Pengfei Guo, Yuchen Zhang, Jionghao Zhu, Xiaoying Tang
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38661v1](http://arxiv.org/abs/2609.38661v1)
- **PDF:** [https://arxiv.org/pdf/2609.38661v1](https://arxiv.org/pdf/2609.38661v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

In recent years, LLM-based multi-agent systems have been widely applied to orchestrate tool-using agents into executable communication graphs. However, existing self-evolving orchestration still faces key challenges, including post-hoc evolution that revises the team only after the trajectory ends, credit diffusion that gives every action the same terminal advantage under confounded baselines, and skill admission that is uncalibrated and never retired. To address these challenges, we propose EvoSteer, a new paradigm of Online Self-Evolving Graph Orchestration -- the orchestrator builds a running team and repairs its plausible but failing steps from execution features and a learned value estimate. To support this paradigm, we introduce Anchored Trajectory Balance (AnchorTB), a regression-style flow-matching loss that assigns each orchestration action a coefficient by balancing subtrajectories against a frozen reference. Built on the learned flow, we further propose Validated Skill Admission, in which a candidate skill is tried before promotion and promoted only if paired evidence passes a sequential test under a shared nominal testing budget. Moreover, AnchorTB combines measured task-level reference reward statistics with prefix-dependent corrections. Experimental results on twelve datasets show that EvoSteer significantly outperforms baselines across question answering, mathematical reasoning, code generation, and interactive decision making. Our code is available at https://github.com/beita6969/evosteer.

</details>


### 153. Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation

- **Authors:** Haibo Jin, Xinjie Li, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38660v2](http://arxiv.org/abs/2609.38660v2)
- **PDF:** [https://arxiv.org/pdf/2609.38660v2](https://arxiv.org/pdf/2609.38660v2)
- **Categories:** cs.CL, cs.AI, cs.CV, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-form subtitle translation requires reasoning over discourse and cultural context spanning episodes or entire series, while maintaining consistent terminology and style. Existing single-LLM methods are largely sentence-level, and multi-agent systems often use static workflows that do not adapt to scene complexity or production context. We propose SMART, a Self-evolving Multi-Agent system for long-foRm subtitle Translation. During test-time training, SMART builds persistent series-level memory and translates a subset of sentences through a dynamic router and Mixture-of-Agents layer with tools for terminology verification, subtitle constraint validation, and contextual retrieval. A judge-refiner loop scores candidates and uses textual critiques to update agent prompts and routing policies without retraining the underlying LLMs. During test-time inference, the evolved configuration translates the remaining series. We also introduce Subtitle Arena, covering 14 genres, 2--198 episodes per series, production years 1959--2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories. SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing average penalty by 6.9% over the strongest competing agent system. On a public benchmark, MuSC, SMART obtains the best model result across all 4 language pairs. SMART also achieves the best result in human evaluation with an overall score of 4.50/5.

</details>


### 154. AgBench: Agentic AI Benchmarks for Personal AI Devices

- **Authors:** Yizhou Han, Di Wu, Dhananjay Saikumar, Blesson Varghese
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38652v1](http://arxiv.org/abs/2609.38652v1)
- **PDF:** [https://arxiv.org/pdf/2609.38652v1](https://arxiv.org/pdf/2609.38652v1)
- **Categories:** cs.AI, cs.PF


> Summary unavailable.


<details>
<summary>Abstract</summary>

Agentic AI systems increasingly rely on cloud-hosted large language models for planning, tool use, and iterative execution, raising concerns about API cost and data exposure. Advances in personal AI devices enable agents to execute locally, but limited resources on device may affect task success and performance. Existing benchmarks are inadequate for systematically characterizing these trade-offs across devices, workloads, and deployment architectures. We present AgBench, a benchmark suite and open artifacts for reproducible evaluation of agentic AI on personal devices. Using AgBench, we evaluate local, hybrid, and cloud execution across agentic workloads, examining task success, latency, cloud API cost, and data exposure. Our results, drawn from over 162.07 million data points, show that personal AI devices can complete many agent tasks locally, but local-only execution generally has lower task success and longer completion times than cloud-only execution, especially as concurrency increases. Local-only execution eliminates cloud model API costs and sensitive-information exposure to cloud agents. Hybrid execution can improve task success, but its cloud cost and data exposure depend on how agents divide work and share information. No single architecture performs best across task success, goodput, cloud cost, and data exposure; deployment choices should reflect the intended workload and device capabilities. AgBench is available at https://anonymous.4open.science/r/AgBench-2777.

</details>


### 155. Recursive Organization Improvement: A Modeling Specification for Human--Agent Organizations

- **Authors:** Zilong Wang
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38643v1](http://arxiv.org/abs/2609.38643v1)
- **PDF:** [https://arxiv.org/pdf/2609.38643v1](https://arxiv.org/pdf/2609.38643v1)
- **Categories:** cs.MA, cs.HC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Stronger AI agents do not automatically produce better organizations: teams must also learn which work arrangements to retain and when to reconsider them. We propose a modeling specification for recursive organization improvement and evaluate it through an executable checker, a public-record mapping, and controlled simulation. The specification connects actor-visible histories, organizational memory, decision rights, and evidence-carrying change contracts. The mechanism study crosses six decision rules, three memory conditions, and three task environments under fixed resource ceilings. In a stationary environment, cumulative evidence raises balanced evaluation's normalized net value per task from 0.45224 to 0.48007. Repeated reassessment's disadvantage relative to this comparator falls from 0.01702 with reset evidence to 0.00007 with cumulative evidence. A reversal of the best workflow reveals the opposite cost: indefinite retention delays adaptation, while a finite window restores eventual performance at a transition cost. In exploratory controls, matching trial acquisition and label reuse reduces the apparent reassessment gain from 0.00607 to 0.00191. Program replacement adds no stable benefit across the tested reversal times. The study identifies evidence acquisition, reuse, and timely updating as mechanisms that must be separated from evaluator replacement when assessing organizational improvement.

</details>


### 156. Beyond Oracle Communication: Benchmarking Interactive Intent Alignment Under Miscommunication and Evolving User Intent

- **Authors:** Zheyuan Zhang, Mengyuan Chao, Ke Xiao, Ziyi Chen, Daoan Zhang, Yan Zhang, Yanfang Ye, Wei Xu
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38604v1](http://arxiv.org/abs/2609.38604v1)
- **PDF:** [https://arxiv.org/pdf/2609.38604v1](https://arxiv.org/pdf/2609.38604v1)
- **Categories:** cs.CL, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern LLM agents increasingly tackle complex tasks through interactive, long-horizon exchanges with users, while existing benchmarks generally assume that users always accurately and sufficiently communicate a fixed intent. However, this oracle communication assumption rarely holds in practice: users may miscommunicate, change their goals, and run out of patience. We define this task setting as Interactive Intent Alignment, where agents must recover and continuously track the user's current intent despite imperfect communication and evolving goals. To study this setting, we introduce Drift-Bench++, a principled benchmark construction pipeline for verified executable tasks with controlled misalignment and intent shifts, along with an interaction protocol featuring finite patience, diverse simulated users, and silent interaction-conditioned shifts. We further develop GRIP, a comprehensive evaluation protocol covering task grounding, user realism, inquiry effectiveness, and adaptation to evolving intent. Across diverse environments, models, and interaction conditions, stronger interaction consistently helps but remains far from oracle performance; Validation on deployed ProdAgent sessions further shows that the modeled failures are prevalent and consequential in deployment. By providing a unified, executable benchmark for interactive intent alignment, Drift-Bench++ offers a foundation for evaluating and advancing agents under realistic communication and evolving intent.

</details>


### 157. Fault-Tolerant Budget Conservation in Distributed Multi-Agent Delegation

- **Authors:** Genliang Zhu, Chu Wang
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00349v1](http://arxiv.org/abs/2610.00349v1)
- **PDF:** [https://arxiv.org/pdf/2610.00349v1](https://arxiv.org/pdf/2610.00349v1)
- **Categories:** cs.AI, cs.CR, cs.DC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Resource limits are becoming an authorization boundary for AI agents that delegate work across concurrent and failure-prone workers. Parent-child allocation constraints, affine objects, and distributed escrow do not by themselves prevent overspend when replies are lost, effects complete after timeout, messages repeat, branches partition, or DAG joins alias one lineage. We formalize fault-tolerant budget conservation for distributed multi-agent delegation. Budgets are quantized resource vectors represented by exclusive escrow credits that move through a delegation DAG. Before dispatch, a branch converts credit into an operation reservation bound to lineage, epoch, normalized effect, maximum charge, receiver, and idempotency key. It persists a signed dispatch permit with quarantine; the gateway verifies that permit before first acceptance. Uncertain effects remain charged until authenticated settlement, a fenced authoritative no-effect proof, or permanent retirement. We prove ownership partition, ledger and effect conservation, descendant non-amplification, at-most-once settlement, late-completion safety, and partition confinement under explicit mediation, durability, authentication, normalization, and gateway assumptions. An indistinguishability result shows that partition-local availability requires exclusive preallocation. Bounded TLA+ checking, an independent JavaScript explorer, and crash-injected two-process SQLite experiments exercise the declared scope and detect timeout-refund and historical-certificate-validation mutants. The mechanism preserves the issued budget bound across the evaluated crash, retry, duplicate, partition, join, and late-completion schedules.

</details>


### 158. From Solo to Social Learning: Characterizing Recursive Social Improvement in LLMs

- **Authors:** Kunal Jha, Max Kleiman-Weiner, Natasha Jaques
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38516v2](http://arxiv.org/abs/2609.38516v2)
- **PDF:** [https://arxiv.org/pdf/2609.38516v2](https://arxiv.org/pdf/2609.38516v2)
- **Categories:** cs.MA, cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) can now improve themselves by revising the instructions they follow, and LLM agents are increasingly orchestrated to work together on complex problems. However, self-improvement methods typically optimize one system at a time, and multi-agent frameworks often have every model work toward a shared goal. We ask a different question. When each agent pursues its own reward, can self-improving LLMs learn from one another well enough to improve the whole population? We call this capability recursive social improvement. We study populations that revise skill files and choose whether, when, and whom to copy from. Independent search, learning from peers, and acting all share one token budget. In controlled environments, established social-learning algorithms benefit from peers, but three LLMs do not. They earn less reward per token than solo learners, and explore too narrowly or run out of tokens before acting. We then let the models write and revise their own skills. Observing peers changes how they improve, helping one model find useful skills sooner and another spend less on private search. Neither, however, outperforms independent learners at the same cost. Skills are copied, revised, and passed on, so one discovery can seed further search. Yet these exchanges concentrate the population around fewer independent discoveries. Together, these results show that LLMs can make learning more efficient by copying from peers, but not yet more effective.

</details>


### 159. PANDA: A Decentralized Architecture with Flexible Orchestration for Scalable, Fault-Tolerant Multi-Agent Systems

- **Authors:** Matthew D. Laws, Cristina Nita-Rotaru
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38482v1](http://arxiv.org/abs/2609.38482v1)
- **PDF:** [https://arxiv.org/pdf/2609.38482v1](https://arxiv.org/pdf/2609.38482v1)
- **Categories:** cs.MA, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Existing architectures for LLM-based multi-agent systems (MAS) cannot reliably and efficiently solve multi-step tasks at scale: they struggle to support large numbers of agents and concurrent tasks, tolerate failures, govern agent interactions, and accommodate the diverse planning and execution patterns different tasks require. We present PANDA, a decentralized architecture that connects a large collective of heterogeneous, independently administered agents, letting them discover each other's capabilities and self-organize into small specialized teams per task. PANDA scales by decoupling collective communication from team communication, allowing agents to participate in multiple teams simultaneously, load-balancing tasks across the collective, and scheduling concurrent work within each agent. PANDA further separates the underlying architecture from the orchestration strategy, supporting three planning and execution patterns (star, chain, and mesh) that can be selected according to the structure and requirements of each task. PANDA detects infrastructure and orchestration failures and recovers affected tasks by dynamically replanning around failed components. Finally, to provide governance without a centralized service that would limit scalability, PANDA uses a web-of-trust model to constrain agent interactions to established trust relationships. We evaluate PANDA on the HotPotQA benchmark, demonstrating that it scales to thousands of agents, assembles teams in milliseconds, matches state-of-the-art accuracy at up to 8x the efficiency, and sustains 100% task completion under faults where existing systems fail.

</details>


### 160. Authorization for Self-Modifying AI Agent Populations: Conserving Authority across Replacement, Forking, and Rollback

- **Authors:** Genliang Zhu, Chu Wang
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2610.00347v1](http://arxiv.org/abs/2610.00347v1)
- **PDF:** [https://arxiv.org/pdf/2610.00347v1](https://arxiv.org/pdf/2610.00347v1)
- **Categories:** cs.CR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Self-modifying AI agents can replace, fork, and roll back identity-bearing software while descendants remain executable. Per-successor authorization does not constrain the resulting population: siblings may duplicate quotas, combine permissions, survive ancestor cuts, or overlap predecessors during promotion. We define authorization succession, which conserves authority across the active frontier of a single-parent generation forest.
  Our external protocol binds each generation to a manifest, root, unique parent, complete lineage, and fresh population sequence. Separate invariants bound root-lifetime consumption and current population exposure. A staged reservation freezes predecessor residual authority during replacement, while a partitioning fork validates the complete child family. Each commit atomically fences the predecessor and activates successors. Ancestor cuts invalidate dependent descendants; rollback creates a fresh generation without restoring spent authority; and a new root requires an independent grant. Under complete mediation, authenticated records, sound effect abstraction, durable monotone state, and complete lineage accounting, we prove population-safe succession, fork conservation, revocation closure, atomic handoff, rollback non-reminting, and exclusion of self-certification.
  An executable evaluation covers 32 registered decisions through direct-call and mailbox mappings (64/64 replays; 28 allows, 36 denies). An independent checker accepts all 64 original traces and rejects 28/28 semantic mutants; 12/12 profile invariants, 16/16 crash cuts, and 32/32 contender schedules pass. Two external adapters reproduce all 32 decisions around measured OurArk and Darwin Godel Machine mutations, including fresh-process restart, atomic succession, and predecessor rejection. The results establish authorization succession for registered protected effects.

</details>


### 161. PrivMeSA: Privacy-Aware Self-Evolving Multi-Agent System for Medicine via Local-Remote LLM Collaboration

- **Authors:** Dannong Wang, Yuran Zhang, Bian Sun, Alex Stinard, Yuzhang Shang, Song Wang, Yu Tian
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38458v1](http://arxiv.org/abs/2609.38458v1)
- **PDF:** [https://arxiv.org/pdf/2609.38458v1](https://arxiv.org/pdf/2609.38458v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Clinical large language model (LLM) agents deployed locally can consult more capable remote models, but doing so risks exposing patient information. Privacy-conscious delegation places disclosure decisions with a local agent, yet removing explicit identifiers is insufficient: quasi-identifiers can accumulate across multi-turn consultations and repeated patient visits to enable re-identification. We introduce PrivMeSA, a privacy-aware self-evolving multi-agent system that learns to control disclosure and retains remote expertise for local reuse. A local agent manages each encounter and consults remote specialists that may request additional information. Reinforcement learning balances task accuracy against direct disclosure and registry-based re-identification risk, with privacy evaluated over the complete outbound transcript of each encounter. A local lesson memory distills completed consultations into generalized clinical guidance and retrieves relevant lessons before transmission, allowing subsequent cases to reuse expertise without another remote exchange. Memory grows without additional outcome labels or parameter updates. On an emergency-department benchmark built from MIMIC-IV-ED records, PrivMeSA improves mean task accuracy over delegation by up to 15.8 percentage points. In the same setting, PrivMeSA reduces the disclosure of personal details from 98.0% to 0.2% of cases and the share of cases in which the patient can be narrowed to ten or fewer registry patients from 74% to 0%.

</details>


### 162. A Competing-Hazards Systematization of Loss of Control in Autonomous Agents

- **Authors:** Mohamed Aly Bouke
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38411v1](http://arxiv.org/abs/2609.38411v1)
- **PDF:** [https://arxiv.org/pdf/2609.38411v1](https://arxiv.org/pdf/2609.38411v1)
- **Categories:** cs.AI, cs.CR


> Summary unavailable.


<details>
<summary>Abstract</summary>

Leading AI developers have reported agents acting beyond their approved limits, which a United Nations panel described as an early warning of loss of human control. Yet incident reports and agent-safety evaluations describe these events differently, making it difficult to compare failures, trace risk across attempts, or separate agent behavior from the environment's role in allowing an out-of-scope action to succeed. To address this gap, we introduce a common framework in which each attempt ends in approved completion, safe stopping, scope escape, or continuation. We formalize the framework as a discrete-time competing-hazards model and derive escape probability within a retry budget, a model-conditional safe-budget limit, and conditions for estimation from execution logs. We audit 22 incident reports and 102 agent-safety evaluations published from January 2025 to September 2026 using primary sources. Six incidents involved tasks that could not be completed within scope, thirteen involved agents that continued rather than stopped, and five did not report stopping behavior. Developers' figures imply a task-level incidence ratio near 47 for out-of-scope coordination in never-solved versus solved tasks. Among evaluations, 87 recorded an out-of-scope effect or specification violation, 26 treated safe stopping as a first-class outcome, only 20 recorded both, and 79 merged budget exhaustion with failure. In 20 of 22 incidents, the environment allowed an out-of-scope effect, indicating that realized loss of control often reflected persistent agent behavior interacting with permissive boundary conditions; meanwhile, no evaluation reported all fields needed to estimate the full competing-hazards process from published evidence.

</details>


### 163. Can an AI Agent Rediscover a Blaschke-Curve Invariant?

- **Authors:** Yunus E. Zeytuncu
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38369v1](http://arxiv.org/abs/2609.38369v1)
- **PDF:** [https://arxiv.org/pdf/2609.38369v1](https://arxiv.org/pdf/2609.38369v1)
- **Categories:** cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

We study generalized Blaschke curves as a controlled environment for AI-assisted mathematical rediscovery. For one fixed degree-four Blaschke product, an agent receives numerical coordinates of the six pair-lines determined by each of 80 boundary configurations. The target theorem is withheld from the task instructions. The saved research log reports rejected geometric hypotheses and a homogeneous cubic fitted to polygon sides. Its frozen coefficients predict 480 lines from 80 unseen parameter values, with a recorded RMS scale-free residual of $8.88\times10^{-17}$. Discovery-set diagonals provide an out-of-fit consistency check, not a fully held-out test. A separate one-configuration run reports insufficient evidence for invariance. A post-review deterministic degree-search baseline also recovers the cubic, so the experiment does not establish an advantage over polynomial fitting. We present this single-instance case study as a protocol for separating conjecture, numerical validation, and proof, with explicit limitations concerning agent metadata, prior knowledge, and reproducibility.

</details>


### 164. TAGGRAPH: Tag-Augmented Graphs for Graph Retrieval of Agent Persistent Histories

- **Authors:** Yu-Shu Chen, Yu-Jung Liang, Pengtao Xie
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38353v2](http://arxiv.org/abs/2609.38353v2)
- **PDF:** [https://arxiv.org/pdf/2609.38353v2](https://arxiv.org/pdf/2609.38353v2)
- **Categories:** cs.IR, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Long-term memory lets LLM agents recall past interactions and remain consistent across sessions, but memory systems are hard to compare because they often vary in representation, indexing, retrieval, and evaluation. We present a controlled evaluation framework based on shared 5W-style conversational memories. Localized graph configurations traverse a common base graph; AdaptiveGraph adds chronological edges and Personalized PageRank diffusion. We also evaluate BM25 over the same extracted notes and OpenClaw as a raw-input external reference. Retrieval rankings vary across memory settings. On LongMemEval-S, AdaptiveGraph is the strongest graph configuration at 0.844 MRR, but BM25 reaches 0.867 and OpenClaw 0.880. On ATANT Core, localized graph traversal outperforms diffusion and BM25, whereas BM25 leads the stress rounds. Reducing LongMemEval-S within the tested range does not reproduce the ATANT diffusion penalty, but the smallest tested store remains larger than ATANT Core, so store size cannot be ruled out. The penalty also persists under a permissive content-match criterion. Vocabulary normalization and extraction quality substantially affect graph retrieval, and missing extraction tags are common among top-five misses. Retrieval strategies should therefore be evaluated jointly with the memory setting and against strong lexical baselines.

</details>


### 165. MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution

- **Authors:** Prithwish Jana, Mononito Goswami, Hao Liu, Xinyu Li, Langlin Huang, Zhehui Huang, Zhishen Huang, Patrick Blöbaum, Anoop Deoras, Purak Jain, Nikos Kanakaris, Sahika Genc
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38349v1](http://arxiv.org/abs/2609.38349v1)
- **PDF:** [https://arxiv.org/pdf/2609.38349v1](https://arxiv.org/pdf/2609.38349v1)
- **Categories:** cs.LG, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Modern agentic systems combine an AI model with a harness that controls execution and environmental interactions. Harness design strongly affects long-horizon performance, yet its combinatorial search space demands substantial human effort that must be repeated as models change. Existing automated methods explore this space narrowly, optimizing only components such as prompts or skills or becoming trapped by fixed, exploitative search strategies. We introduce MILO (Meta-evolutionary Island Orchestration), a framework that co-evolves agent harnesses and the strategy used to discover them. MILO combines: (i) hierarchical lineage memory over island-based trees, using rejected mutations as negative evidence; (ii) per-island mutator agents that rewrite complete harnesses using global search history and parent-specific feedback; and (iii) an orchestrator that adapts search through lineage grafting and speciation, mutator reassignment and curriculum revision. Across Terminal-Bench 2.1, PaperBench, and DeepSWE, MILO-discovered harnesses outperform eight state-of-the-art harnesses and six search methods using frontier (Opus 4.8) and open-weight (gpt-oss-120b) models. With Opus 4.8, MILO improves resolution over its initial harness by $+12.0\%$, $+28.3\%$, and $+10.3\%$, respectively, compared with best prior-search gains of $+4.5\%$, $+18.3\%$, and $0\%$. On Terminal-Bench 2.1, it achieves $86.1 \pm 2.0\%$, exceeding the official leaderboard's top entry ($83.8 \pm 2.3\%$) while using 26\% fewer tokens than its initial harness. On EinsteinArena open problems, MILO improves best-known upper bounds for Erdős minimum-overlap ($0.3808586 \to 0.3808568$) and the first and third autocorrelation inequalities ($1.50274365 \to 1.50274360$; $1.45081 \to 1.44889$).

</details>


### 166. OpenCollab: A Multi-Agent Coding Framework with Programmable Collaboration and Controllable Runtime

- **Authors:** Chun-Wah Hsu, Kai Gong, Yu Wu, Xianhe Chen, Mengyang Liu, Jie Li, Hanyu Li, Zhixuan Liu, Naisheng Tang, Jiaying Chi, Ziheng Fan, Xuning He, Xiaokang Yang, Xue Jiang, Yihong Dong
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38345v1](http://arxiv.org/abs/2609.38345v1)
- **PDF:** [https://arxiv.org/pdf/2609.38345v1](https://arxiv.org/pdf/2609.38345v1)
- **Categories:** cs.SE, cs.AI, cs.CL, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent coding systems are designed to tackle complex software engineering tasks through collaboration. However, existing evaluations typically assume configured organizations are followed faithfully, whereas reality differs. This behavioral gap, combined with differences in underlying system components, prevents clear attribution of observed gains. To this end, we introduce OpenCollab, a multi-agent coding framework that provides a unified infrastructure for programmable collaboration and controllable runtime. Specifically, OpenCollab unifies organization design, enforces experimental control on a shared runtime, and tracks execution through fine-grained event streams. On this basis, we define Adherence to quantify whether the declared organization is actually realized. Our experiments reveal that agents collaborate very differently across configurations: changing any single dimension shifts Adherence, from 47.2% to as high as 97.2%. Furthermore, extensive agentic coding benchmarks show that a two-coder workflow built on OpenCollab establishes new SOTA performance compared to the mainstream harnesses such as Mini-SWE-agent, Codex CLI, and Claude Code, showing that a well-designed organization can outperform strong existing harnesses, while OpenCollab's single-agent configuration uses the fewest tokens across all evaluated suites. OpenCollab establishes a unified multi-agent infrastructure for easy programmable collaboration and controlled causal evaluation.

</details>


### 167. E2E-SWE: Benchmarking LLMs on Building Working Codebases from Scratch

- **Authors:** Hantian Ding, Chloe Bi, Jiacheng Zhu, John Yang, Matt Deitke, Pengcheng Yin, Zijian Wang, Rui Hou
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38335v1](http://arxiv.org/abs/2609.38335v1)
- **PDF:** [https://arxiv.org/pdf/2609.38335v1](https://arxiv.org/pdf/2609.38335v1)
- **Categories:** cs.SE, cs.AI


> Summary unavailable.


<details>
<summary>Abstract</summary>

Coding agents powered by large language models (LLMs) are evolving from making localized code changes to developing complete software repositories. However, evaluating repository-scale generation remains challenging: tasks must demand system-level reasoning while ensuring that all evaluated behaviors are precisely specified and independent of any particular implementation. We introduce E2E-SWE, a benchmark for evaluating whether coding agents can build complete, functional software repositories end to end. E2E-SWE contains 186 whole-repository generation tasks spanning 11 programming languages. Given only a natural-language specification and an empty workspace, an agent must implement a complete, installable project that satisfies a comprehensive suite of hidden tests. Each task is constructed by a software engineer in collaboration with an LLM; together, they develop the test suite and a corresponding implementation-independent specification. To ensure that tasks are well specified and practically solvable, we further subject them to an iterative verification process in which autonomous agents audit and repair task defects using static inspection and failures observed from real model rollouts. Evaluating 13 frontier models, we find substantial variation in end-to-end repository generation ability, with pass@1 ranging from 11.7% to 67.7%, providing strong model differentiation while leaving considerable headroom for future progress. Analysis of agent trajectories further reveals long, front-loaded reasoning patterns, highlighting the planning and system-level reasoning required to construct working codebases from scratch.

</details>


### 168. EVOKE: Eliciting World Knowledge in Agents for Transferable Decision-Making

- **Authors:** Yuhan Guo, Jinming Liu, Liang Xu, Ziqiang Li, Jianguo Huang, Zhicheng Wang, Hu Zhu, Qiuyu Chen, Yuntao Wei, Xin Jin, Wenjun Zeng
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38334v2](http://arxiv.org/abs/2609.38334v2)
- **PDF:** [https://arxiv.org/pdf/2609.38334v2](https://arxiv.org/pdf/2609.38334v2)
- **Categories:** cs.CL


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) are increasingly deployed as agents for multi-step decision-making, yet transfer poorly to unseen environments. World-model methods address this by training agents to predict future observations, at the cost of additional training and errors that compound when predictions are used for planning. However, for LLM agents operating in digital environments, much of this world knowledge is already internalized during pretraining, which shifts the problem from acquiring it to eliciting it. We argue that typical post-training provides little pressure for such elicitation, since supervision under a single goal at each visited state inadvertently drives policies to rely on superficial contextual habits. We introduce EVOKE, a post-training method that supplies this pressure through goal diversity at fixed states. Motivated by theory showing that an agent competent across diverse goals must encode a world model recoverable from its action preferences, EVOKE holds the environment state and interaction history fixed and ranks the same candidate actions under alternative goals, forcing action preferences to change, so that a policy relying on contextual habits or single-goal correlations cannot order them correctly. This implicitly elicits the policy's pretrained world knowledge to inform decisions. We evaluate EVOKE across diverse tasks in three backbones, demonstrating improved task performance, unseen environment generalization, and data efficiency. We further conduct controlled analyses to better understand what drives these gains. These findings offer a new perspective on eliciting internalized world knowledge for transferable action through direct decision supervision.

</details>


### 169. Absorbing State Phase Transitions in Multi-Agent Search

- **Authors:** Wenwen Zheng, Yuzhe Yang, Helen Qu, Xin Eric Wang, Haewon Jeong
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38327v1](http://arxiv.org/abs/2609.38327v1)
- **PDF:** [https://arxiv.org/pdf/2609.38327v1](https://arxiv.org/pdf/2609.38327v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Nontrivial dynamics can emerge in large language model (LLM)-based multi-agent systems, and preliminary evidence exists that formalisms from statistical mechanics can be effective at modeling and predicting such behaviors. In parallel, designing multi-agent communication topology for optimal task-solving is an active research question. In this paper, we focus on predicting the success of multi-agent search tasks using the formalism of absorbing state phase transitions. We first taxonomize search tasks into four types, informed by classical results in combinatorial search. We then theoretically derive a critical communication degree $d_c$, the minimum number of agents each agent can communicate with, above which incorrect hypotheses do not proliferate uncontrollably and the search enters the solved state. Finally, we evaluate frontier LLM-based multi-agent systems on real-world search and discovery tasks, software configuration debugging and physical mechanism discovery, and find that agreement with theory is mixed. LLM agents may not communicate with their neighbors and can develop strategies that are individually beneficial but limits the benefits of collaboration.

</details>


### 170. Multi-agent discussion gains less when dissent is withheld

- **Authors:** Chand Sahil Mansuri, Xin Wang, Mengying Li, Bryan Acton, Rory Eckardt, Dhaval Patel, Sadamori Kojaku
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38324v1](http://arxiv.org/abs/2609.38324v1)
- **PDF:** [https://arxiv.org/pdf/2609.38324v1](https://arxiv.org/pdf/2609.38324v1)
- **Categories:** physics.soc-ph, cs.CL, cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Multi-agent systems of LLMs add discussion to majority voting and are therefore expected to be more capable. However, empirical reports conflict on whether discussion improves accuracy or leads to an incorrect consensus. Here, we introduce a parsimonious model that explains when discussion improves accuracy and when it ends in an incorrect consensus, built from four behaviors repeatedly observed in LLM agents: (1) withholding dissent, (2) internalizing a stated answer, (3) reconsidering after seeing dissent, and (4) correcting toward the correct answer. The model shows that discussion can overturn an incorrect initial majority only when the withholding rate $c$ is below a critical rate $c^* = γ/(γ+ a)$, set by the net correction rate $γ$ and the internalization rate $a$. We estimate these rates from conversation logs with a Bayesian method and place LLM teams relative to $c^*$. As the model predicts, the gain from discussion shrinks as withholding rises, across LLMs and on a hidden profile benchmark, HiddenBench, and MedEInst. Instructing agents not to withhold dissent increases this gain. Turning reasoning off also increases the gain, because reasoning raises the internalization rate $a$ and keeps agents from reconsidering a minority answer. These findings reconcile the conflicting reports and identify when discussion outperforms majority voting.

</details>


### 171. Searching for BSM Experimental Signatures with Large Lagrangian Models

- **Authors:** Ibrahim Elsharkawy, Victoria Knapp-Perez, Wahid Bhimji, Aishik Ghosh
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38309v1](http://arxiv.org/abs/2609.38309v1)
- **PDF:** [https://arxiv.org/pdf/2609.38309v1](https://arxiv.org/pdf/2609.38309v1)
- **Categories:** hep-ph, astro-ph.CO, cs.AI, hep-ex


> Summary unavailable.


<details>
<summary>Abstract</summary>

The search for physics Beyond the Standard Model (BSM) is generally limited not by the supply of theory descriptions but by the lack of discriminating experimental observations. A case in point is dark matter, where the overwhelming gravitational evidence only goes so far in distinguishing between models within a vast theory space. Exploring the space of testable model signatures may help identify overlooked experimental observables and indicate the utility of future experiments. A challenge is designing a search through model signatures outside what is found in the literature. Our primary contribution is hAIthem, a framework that combines the self-guided exploration of reinforcement learning (RL) with the broad literature-derived knowledge of LLMs. We build an RL agent that learns to find which portions of a theory's high-dimensional parameter space are not excluded under some subset of constraints by playing a Battleship-style "game" against a suite of phenomenology tools. The agent is built as a Large Lagrangian Model (LLaM), an autoregressive transformer that reads a tokenized Lagrangian, is pretrained at scale (here on ~1 billion tokens from ~10,000 Lagrangians), and is fine-tuned in a live environment. The framework then constructs a decision tree that separates RL-found regions using observables computed with established tools, and passes the remaining degenerate regions to a set of LLM agents that compete to produce realistic signatures. In this proof of concept, RL-search outperforms an evolutionary-algorithm baseline, finding more viable regions with greater physical diversity. In a restricted space of single dark scalar multiplet models, we find that hAIthem proposes interesting combinations of previously studied observables, such as the application of a halo-independent kinematic ratio to paleo-detectors.

</details>


### 172. Multi-Agent Flow Matching with Decoupled Generative Guidance

- **Authors:** Ruoyu Lin, Magnus Egerstedt, Fabio Pasqualetti
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38133v1](http://arxiv.org/abs/2609.38133v1)
- **PDF:** [https://arxiv.org/pdf/2609.38133v1](https://arxiv.org/pdf/2609.38133v1)
- **Categories:** cs.LG, cs.MA, cs.RO, math.OC


> Summary unavailable.


<details>
<summary>Abstract</summary>

Generative modeling is widely used for producing diverse objects from complex, multimodal distributions. However, its expressivity does not, in general, come with formal guarantees that the generated objects satisfy hard constraints or requirements. In multi-agent generation, this problem becomes more challenging because a hard requirement can depend on multiple agents, while each agent may need to determine its own guidance input without relying on the simultaneously computed guidance inputs of other agents. To this end, we introduce DeGG-Flow, a general framework for multi-agent flow matching with decoupled generative guidance. By representing the generative process as a control-affine dynamical system, we develop guidance conditions for two classes of coupled requirements: shared requirements whose satisfaction depends on multiple agents together, and private requirements associated with each individual agent dependent on its neighbors. For both classes, we establish feasibility conditions and finite-horizon convergence guarantees. We further derive a Wasserstein bound that characterizes the distributional deviation induced by the guidance. We demonstrate DeGG-Flow on multi-robot collaboration for crossing a spatial gap by reconfiguring the environment, and on multi-object scene generation with affordance requirements. Across both applications, DeGG-Flow directly generates objects that satisfy all corresponding hard requirements, including at team sizes unseen during training.

</details>


### 173. IMPACT: Modeling Socially Interdependent Movement in a Generative Multi-Agent Simulation of a Pompeian Household

- **Authors:** Tianqi Liu, Nayoung Kim, Julia Sebastien, Kathryn Gleason, Caitlín Eilís Barrett, Andrea Stevenson Won
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38113v1](http://arxiv.org/abs/2609.38113v1)
- **PDF:** [https://arxiv.org/pdf/2609.38113v1](https://arxiv.org/pdf/2609.38113v1)
- **Categories:** cs.MA


> Summary unavailable.


<details>
<summary>Abstract</summary>

Simulations of archaeological sites can make interpretations of past cultural practices observable and examinable. Generative multi-agent simulations offer a bottom-up approach to modeling how people collectively moved through and used historical spaces. However, current agents designed to simulate everyday life often plan and act independently, limiting their ability to capture how movement depends on others' actions. We introduce IMPACT (Interdependent Movement Planning through Inter-Agent Constraints and Triggers), an architecture that uses culturally specific roles and obligations to define dependencies among agents' activities and guide coordination. IMPACT connects socially gated milestone planning, wait-or-prompt resolution, structured directive issuance, and directive integration. These mechanisms determine whether and when activities can begin or change as social conditions evolve, producing socially constrained and prompted movement as their primary observable outcome. We instantiate IMPACT in a five-hour simulation of a Pompeian dinner involving ten agents across interdependent roles. Analysis of five simulation runs shows how social roles, responsibilities, and status relations shape household activities and spatial practices, as reflected in patterns of co-location, asymmetric waiting, co-movement, and social directives. In a controlled ablation evaluation, thirty-seven participants rated the complete architecture's behavior as more socially coherent and believable than that of two reduced architectures. Interviews with six archaeology experts highlighted historically plausible movement patterns and the simulation's potential to support archaeological interpretation, while identifying areas requiring stronger historical grounding for future work.

</details>


### 174. Do LLM Agents Execute the Plans They Declare? From Planning-Mode Declaration to Pattern-Specific Execution

- **Authors:** Subba Reddy Oota, Francisco Herrera, Jordi Cabot Sagrera, Marcos López de Prado, Shadab Khan
- **Published:** 2026-09-29
- **Source:** arxiv
- **URL:** [http://arxiv.org/abs/2609.38108v1](http://arxiv.org/abs/2609.38108v1)
- **PDF:** [https://arxiv.org/pdf/2609.38108v1](https://arxiv.org/pdf/2609.38108v1)
- **Categories:** cs.AI, cs.LG


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language models (LLMs) enable agents to solve long-horizon tasks by generating a plan and then executing it in an environment. However, successful planning requires two distinct capabilities: selecting an appropriate plan for the task and executing it faithfully. Existing planner--executor systems can fail at either stage, while final task success alone cannot distinguish selection from execution failures. We therefore study the Plan Declaration--Execution Gap and introduce Planning-as-Routing, where an LLM declares one of four planning modes: Predefined, Sequential, Hierarchical, or Search, and a deterministic router dispatches the task to the corresponding pattern-specific executor. Across four benchmarks and three LLMs, we find three consistent patterns. First, generic Plan+ReAct often fails to preserve declared planning structure, especially for longer plans: across three benchmarks, only (22)--(45%) of trajectories preserve it, whereas pattern-specific executors enforce the intended structure. Second, planning-mode effectiveness varies across environments and models: Search performs best on ALFWorld, Hierarchical on SWE-bench, and the strongest pattern can vary across models within the same benchmark. Third, the largest gains come from execution: pattern-specific executors improve task success from (0.48) to (0.92) on ALFWorld and from (0.36) to (0.44) on SWE-bench Verified over Plan+ReAct. Current LLMs, however, do not reliably select the strongest mode for each task, although few-shot examples improve selection in some benchmark--model combinations. Overall, reliable agent planning requires both effective mode selection and faithful execution: routing substantially closes the execution gap, while task-specific mode selection remains open.

</details>



## Biorxiv (3 papers)


### 1. Synergistic Combination of Bioengineered MicroRNA and Chemotherapy Across High-Risk Neuroblastoma Subtypes

- **Authors:** Lee, Y., AlKhazal, A., Doyle, K. E., Ahn, Y.-R., Sandoval Castellanos, A. M., Tu, M.-J., Yu, A.-M., Kim, J., Brown, E. G.
- **Published:** 2026-10-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.30.755443](https://doi.org/10.64898/2026.09.30.755443)

- **Categories:** bioengineering


> Summary unavailable.


<details>
<summary>Abstract</summary>

Despite intensive treatment, high-risk neuroblastoma (HRNB) remains a leading cause of cancer-related mortality in children. Current treatment paradigms include multimodal systemic treatments and multi-agent chemotherapy, which is limited by substantial acute and long-term toxicities. Platinum-based chemotherapy is a cornerstone of this treatment but is fraught with side effects and stands to benefit from dose reduction strategies. MicroRNA (miR)-based therapeutics represent an attractive strategy to simultaneously moderate multiple oncogenic pathways, providing a potential avenue to enhance the efficacy of current treatment regimens. However, the development of miR therapeutics has largely relied on chemically synthesized ones, which are limited by issues of inconsistency and poor in vivo stability. Biologically produced, tRNA/pre-miR containing bioengineered miRs (bioRNAs) address these limitations. We investigated the therapeutic potential of bioRNA encoding miR-124 and miR-34a across molecularly distinct HRNB models and evaluated their ability to enhance cisplatin efficacy. Both bioRNAs significantly suppressed neuroblastoma cell viability in vitro, with proteomic analyses demonstrating preferential induction of neuronal differentiation by miR-124 and apoptotic signaling by miR-34a. Combining bioRNA with cisplatin produced robust synergy across multiple HRNB lines, enhancing apoptosis while simultaneously promoting differentiation-associated phenotypes. In vivo, both bioRNAs suppressed tumor growth as monotherapies, while combination with low-dose cisplatin produced the strongest responses across multiple xenograft models with different HRNB subtypes. Notably, low-dose cisplatin combined with bioRNA therapy frequently achieved tumor control comparable to, or greater than, that observed with high-dose cisplatin monotherapy while maintaining favorable tolerability. These findings establish bioRNAs as potent cisplatin sensitizers and support bioRNA-based combination therapy as a strategy for improving HRNB treatment while reducing chemotherapy-associated toxicity in children.

</details>


### 2. GroundAnnot: a closed-vocabulary contract for grounding LLM gene-set annotation in live enrichment backends

- **Authors:** Malima, M. B.
- **Published:** 2026-10-02
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.27.754741](https://doi.org/10.64898/2026.09.27.754741)

- **Categories:** bioinformatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

Motivation: LLM agents increasingly draft functional interpretations of gene lists, but can cite Gene Ontology (GO) terms that no current enrichment backend returned for that list, and can pair real GO accessions with fabricated labels. Results: We present GroundAnnot, a client for PANTHER, Enrichr, and g:Profiler that returns a closed vocabulary of GO term IDs and their backend labels, and enforces two contracts: Contract A (no ID or label outside the backend payload) and Contract B (no enrichment claim outside the backend's significant set). Across three open-weight models (Qwen2.5-7B local; Qwen3.8-27B and GPT-OSS-120B via Groq) on six curated disease gene lists, mean valid-enriched rates were 15.3%, 20.1%, and 35.1%. All unsupported IDs were real GO terms classified by QuickGO as wrong-biology, obsolete, or wrong-branch (zero fabricated accessions). A distinct failure mode emerged: for the Alzheimer's gene list, the local 7B model paired every one of its ten stable picks with a label that does not match the current GO term for that accession (10/10 mismatches), producing a coherent synaptic-signalling narrative that the IDs do not support. Mean overlap with the backends' FDR top-10 union was 0.33-0.67/10. On 50 MSigDB Hallmark gene sets, the strongest model named the defining pathway in 21/44 (47.7%) directly named cases. When an enriched shortlist was placed in the prompt, all three models complied fully (60/60 for each model; 180/180 overall), showing that a bounded vocabulary removes these output classes when the downstream agent is required to use it.

</details>


### 3. From seven combination hypotheses to one testable interaction: a gated agentic AI QSP workflow applied to healthy ageing interventions

- **Authors:** Goryanin, I., Goryanin, I., Damms, B.
- **Published:** 2026-10-01
- **Source:** biorxiv
- **URL:** [https://doi.org/10.64898/2026.09.29.755460](https://doi.org/10.64898/2026.09.29.755460)

- **Categories:** systems biology


> Summary unavailable.


<details>
<summary>Abstract</summary>

Large language model (LLM) agents can propose combination therapies and construct supporting mechanistic models far quicker than either can be verified. To address this gap, we built a gated agentic AI quantitative systems pharmacology (Ai QSP) workflow where no hypothesis reaches a report until it clears strict hurdles for precedent, evidence, structural integrity, and release. We applied this pipeline end to end to healthy-ageing interventions. It began with a 34 state model calibrated on clinical trial data for semaglutide and metformin. Locked and evaluated against an independent post hoc DNA methylation trial, the model captured the direction of change across all 9 organ and system clocks, but the magnitude was far too small: it predicted about 0.14 years per year where 1.6 were observed, halting tier promotion. The workflow then generated seven nutritional combination hypotheses (H1H7) with 48 new parameters encoded in SBML. Identifiability analysis showed that 37 of these were completely unconstrained by available data. Trimming the model down to its lead pairing - a food derived bioactive (Agent A) plus a single-strain probiotic (Agent B left six identifiable parameters and locked the uncalibrated interaction term at zero. From this reduced model, we derived an 84 day trial with a 28 day washout, requiring 356 participants for 80% power at an interaction ratio of 0.75. A 9,000 person virtual trial confirmed the design (80.5% power), but revealed an operational trap: an assay floor at 24 mg/kg slashed power to 33% and skewed estimates toward the null, forcing a protocol-level censoring condition before study lock. Testing the pipeline across downstream operational stages and comparative oncology programmes showed that unconstrained generation consistently over-reports novelty, topological entry points can masquerade as biological mechanism, and governance gates remain vulnerable to operator overrides. Ultimately, the workflow delivered no silver bullet: its output is a single testable interaction, an assay hardened trial design, and an audit trail documenting why the other six hypotheses were shelved. Agent identities, doses, and agent specific sources are withheld in this version pending patent filing.

</details>



## Medrxiv (1 papers)


### 1. A ReAct Agentic AI System for Natural Language Querying and Statistical Analysis of The Cancer Genome Atlas Clinical Data

- **Authors:** Korutla, R., Amal, S.
- **Published:** 2026-09-28
- **Source:** medrxiv
- **URL:** [https://doi.org/10.64898/2026.07.15.26358188](https://doi.org/10.64898/2026.07.15.26358188)

- **Categories:** health informatics


> Summary unavailable.


<details>
<summary>Abstract</summary>

The Cancer Genome Atlas (TCGA) holds clinical data for over 11,000 patients across 33 cancer types, but access is hard because of complex file structures, heterogeneous formats, and the need for programming. We present an agentic system for natural language querying and statistical analysis of TCGA clinical data. The system uses a large language model (LLM) as an autonomous Reasoning and Acting (ReAct) agent that selects from eight computational tools, including data extraction, descriptive statistics, Kaplan-Meier survival analysis with log-rank tests, hypothesis testing, and verification against the curated TCGA Pan-Cancer Clinical Data Resource (CDR). The agent reasons about intermediate results, adapts its approach, and returns clinically contextualized responses with source attribution and auditable traces. We introduce TCGA-Agent-Bench, 440 queries across five difficulty tiers with ground truth from the independently curated CDR, evaluated with dual metrics for numerical accuracy and clinical completeness. The system achieves 93.4% overall accuracy, outperforming a fixed rule-based pipeline (87.1%), a single-pass LLM (81.8%), and retrieval-augmented generation (66.9% on a 50-query subset). Most of the benchmark is answerable from the CDR alone, so we locate the extraction layers value in fields the CDR lacks, such as drug treatments, TNM components, and biomarkers: on 26 queries targeting these, the full system answers 100% versus 3.8% for a CDR-only configuration. A tool-based agentic architecture enables accurate, auditable natural language analysis of clinical repositories, with value driven by tool design and recovered fields rather than model scale.

</details>






---
*Generated by [agentpaper_reporter](https://github.com/your-repo/agentpaper_reporter)*